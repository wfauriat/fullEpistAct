"""
Track 2 RDM Sobol Sweep, Saltelli Sensitivity Indices, and Phase-Boundary Plots.

Runs:
1. 4,096-point Sobol sweep across (N, alpha, p_base, c_0, m_0, f_0, K, B_bypass)
   evaluating ('none', 'static_always', 'adaptive_uq') with paired CRNs.
2. Saltelli Sobol sensitivity analysis (n=512 -> 5,120 points) for S_i and S_Ti.
3. High-resolution 2D phase slices & 3 publication-grade Matplotlib figures.
"""

from __future__ import annotations

import json
from pathlib import Path
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import qmc

from engine import SimConfig, run_batch_policy
from validation import validate_annex_d, validate_m1_closed_form

ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"

PARAM_NAMES = ["N", "alpha", "p_base", "c_0", "m_0", "f_0", "log10_K", "B_bypass"]
N_LEVELS = np.array([1, 4, 8, 12], dtype=np.int32)


def map_unit_hypercube(u: np.ndarray) -> dict[str, np.ndarray]:
    """Map [0, 1)^8 Sobol unit samples to Track 2 parameter space."""
    n_idx = np.clip((u[:, 0] * 4.0).astype(np.int32), 0, 3)
    return {
        "N": N_LEVELS[n_idx],
        "alpha": u[:, 1],                                # [0.00, 1.00]
        "p_base": 0.02 + 0.18 * u[:, 2],                 # [0.02, 0.20]
        "c_0": 0.05 + 0.45 * u[:, 3],                    # [0.05, 0.50]
        "m_0": 0.05 + 0.25 * u[:, 4],                    # [0.05, 0.30]
        "f_0": 0.01 + 0.24 * u[:, 5],                    # [0.01, 0.25]
        "K": 10.0 ** (4.0 * u[:, 6]),                    # [1, 10^4]
        "B_bypass": 0.20 + 0.80 * u[:, 7],               # [0.20, 1.00]
    }


def run_sobol_sweep(n_pow2: int = 12, seed: int = 2026) -> pd.DataFrame:
    """Execute 2^n_pow2 = 4,096 Sobol sweep across all 3 CFF policies."""
    sampler = qmc.Sobol(d=8, scramble=True, seed=seed)
    u = sampler.random_base2(m=n_pow2)
    params = map_unit_hypercube(u)

    cfg = SimConfig()
    rows = {
        "point_id": np.arange(len(u), dtype=np.int32),
        "N": params["N"],
        "alpha": params["alpha"],
        "p_base": params["p_base"],
        "c_0": params["c_0"],
        "m_0": params["m_0"],
        "f_0": params["f_0"],
        "K": params["K"],
        "log10_K": np.log10(params["K"]),
        "B_bypass": params["B_bypass"],
    }

    for pol in ("none", "static_always", "adaptive_uq", "adaptive_uq_only"):
        res = run_batch_policy(params, pol, cfg=cfg, seed=seed)
        for k, v in res.items():
            if k not in ("tp", "fp", "tn", "fn", "total_steps"):
                rows[f"{pol}__{k}"] = v

    df = pd.DataFrame(rows)
    df["delta_step_risk_adapt_vs_none"] = df["adaptive_uq__mean_step_risk"] - df["none__mean_step_risk"]
    df["delta_cost_adapt_vs_none"] = df["adaptive_uq__mean_total_cost"] - df["none__mean_total_cost"]
    df["delta_cost_adapt_vs_static"] = df["adaptive_uq__mean_total_cost"] - df["static_always__mean_total_cost"]

    df["adaptive_dominates_cost_and_trap"] = (
        (df["adaptive_uq__mean_total_cost"] <= df["none__mean_total_cost"])
        & (df["adaptive_uq__mean_total_cost"] <= df["static_always__mean_total_cost"])
        & (df["adaptive_uq__silent_trap_rate"] <= df["none__silent_trap_rate"])
        & (df["adaptive_uq__silent_trap_rate"] <= df["static_always__silent_trap_rate"])
    )
    df["adaptive_strictly_better_with_low_bypass"] = (
        df["adaptive_dominates_cost_and_trap"] & (df["adaptive_uq__bypass_rate"] < 0.10)
    )
    df["uq_only_dominates_cost_and_trap_low_bypass"] = (
        (df["adaptive_uq_only__mean_total_cost"] <= df["none__mean_total_cost"])
        & (df["adaptive_uq_only__mean_total_cost"] <= df["static_always__mean_total_cost"])
        & (df["adaptive_uq_only__silent_trap_rate"] <= df["none__silent_trap_rate"])
        & (df["adaptive_uq_only__silent_trap_rate"] <= df["static_always__silent_trap_rate"])
        & (df["adaptive_uq_only__bypass_rate"] < 0.10)
    )
    return df


def compute_saltelli_sobol(n_base: int = 512, seed: int = 777) -> pd.DataFrame:
    """Compute first-order S_i and total-order S_Ti via Saltelli/Jansen estimator."""
    d = 8
    sampler = qmc.Sobol(d=2 * d, scramble=True, seed=seed)
    ab = sampler.random_base2(m=int(np.log2(n_base)))
    A = ab[:, :d]
    B = ab[:, d:]

    cfg = SimConfig()

    def eval_mat(unit_mat: np.ndarray) -> dict[str, np.ndarray]:
        p = map_unit_hypercube(unit_mat)
        out_none = run_batch_policy(p, "none", cfg=cfg, seed=seed)
        out_stat = run_batch_policy(p, "static_always", cfg=cfg, seed=seed)
        out_adpt = run_batch_policy(p, "adaptive_uq", cfg=cfg, seed=seed)
        return {
            "none_step_risk": out_none["mean_step_risk"],
            "none_silent_trap": out_none["silent_trap_rate"],
            "static_bypass": out_stat["bypass_rate"],
            "adapt_cost_advantage_vs_none": out_none["mean_total_cost"] - out_adpt["mean_total_cost"],
            "adapt_cost_advantage_vs_static": out_stat["mean_total_cost"] - out_adpt["mean_total_cost"],
        }

    fA = eval_mat(A)
    fB = eval_mat(B)
    fAB = []
    for i in range(d):
        AB_i = A.copy()
        AB_i[:, i] = B[:, i]
        fAB.append(eval_mat(AB_i))

    records = []
    for metric in fA.keys():
        yA = fA[metric]
        yB = fB[metric]
        var_y = float(np.var(np.concatenate([yA, yB]), ddof=1))
        for i, name in enumerate(PARAM_NAMES):
            yAB_i = fAB[i][metric]
            # Saltelli (2010) S_i and Jansen (1999) S_Ti estimators
            s_i = float(np.mean(yB * (yAB_i - yA)) / max(var_y, 1e-18))
            s_ti = float(0.5 * np.mean((yA - yAB_i) ** 2) / max(var_y, 1e-18))
            records.append({
                "metric": metric,
                "parameter": name,
                "S_i": s_i,
                "S_Ti": s_ti,
            })
    return pd.DataFrame(records)


def compute_alpha_sharing_slice(seed: int = 999) -> pd.DataFrame:
    """Compare alpha=0 (unassisted) vs alpha in (0, 1] with paired CRNs across alpha."""
    alphas = np.linspace(0.0, 1.0, 21)
    p_bases = np.array([0.04, 0.10, 0.16])
    cfg = SimConfig(T=4000)
    M = len(p_bases)
    rows = []
    for a in alphas:
        params = {
            "N": np.full(M, 4, dtype=np.int32),
            "alpha": np.full(M, a),
            "p_base": p_bases,
            "c_0": np.full(M, 0.10),
            "m_0": np.full(M, 0.20),
            "f_0": np.full(M, 0.05),
            "K": np.full(M, 100.0),
            "B_bypass": np.full(M, 0.65),
        }
        # Same seed for every alpha gives smooth CRN phase curves
        out_none = run_batch_policy(params, "none", cfg=cfg, seed=seed)
        out_adpt = run_batch_policy(params, "adaptive_uq_only", cfg=cfg, seed=seed)
        for i, pb in enumerate(p_bases):
            rows.append({
                "p_base": float(pb),
                "alpha": float(a),
                "none_step_risk": float(out_none["mean_step_risk"][i]),
                "none_ep_fail": float(out_none["mean_ep_fail"][i]),
                "none_cvar99": float(out_none["cvar99_cost"][i]),
                "none_escape": float(out_none["escape_rate"][i]),
                "adapt_step_risk": float(out_adpt["mean_step_risk"][i]),
                "adapt_cvar99": float(out_adpt["cvar99_cost"][i]),
                "adapt_escape": float(out_adpt["escape_rate"][i]),
            })
    return pd.DataFrame(rows)


def generate_figures(df: pd.DataFrame, sobol_df: pd.DataFrame, slice_df: pd.DataFrame) -> None:
    plt.rcParams.update({
        "figure.facecolor": "#0f172a",
        "axes.facecolor": "#162032",
        "axes.edgecolor": "#334155",
        "axes.labelcolor": "#e2e8f0",
        "text.color": "#e2e8f0",
        "xtick.color": "#94a3b8",
        "ytick.color": "#94a3b8",
        "grid.color": "#253248",
        "legend.facecolor": "#1e293b",
        "legend.edgecolor": "#334155",
    })

    # --- Figure 1: Shared-AI Mean Risk vs. Tail Escape & Cost ---
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8), dpi=160)
    colors = {0.04: "#38bdf8", 0.10: "#f97316", 0.16: "#a855f7"}
    for pb, grp in slice_df.groupby("p_base"):
        col = colors[pb]
        axes[0].plot(grp["alpha"], grp["none_step_risk"] * 100, color=col, lw=2.3, label=f"No CFF (p₀={pb:.0%})")
        axes[0].plot(grp["alpha"], grp["adapt_step_risk"] * 100, color=col, lw=1.8, ls="--", label=f"Adaptive CFF (p₀={pb:.0%})")
        axes[1].plot(grp["alpha"], grp["none_escape"] * 100, color=col, lw=2.3, label=f"No CFF (p₀={pb:.0%})")
        axes[1].plot(grp["alpha"], grp["adapt_escape"] * 100, color=col, lw=1.8, ls="--", label=f"Adaptive CFF (p₀={pb:.0%})")

    axes[0].set_title("Mean Step Residual Risk vs. Shared-AI Intensity α\n(N=4, c₀=10%, m₀=20%, f₀=5%, K=100)")
    axes[0].set_xlabel("Shared-Model Intensity α")
    axes[0].set_ylabel("Mean Escaped Step Risk (%)")
    axes[0].grid(True, alpha=0.5)
    axes[0].legend(fontsize=8)

    axes[1].set_title("Error Escape Probability vs. Shared-AI Intensity α\n(Accuracy Cuts Mean Risk While Monoculture Raises Escape)")
    axes[1].set_xlabel("Shared-Model Intensity α")
    axes[1].set_ylabel("Escape Probability Given Error (%)")
    axes[1].grid(True, alpha=0.5)
    axes[1].legend(fontsize=8)

    fig.tight_layout()
    fig.savefig(ARTIFACTS_DIR / "fig1_monoculture_phase.png")
    plt.close(fig)

    # --- Figure 2: CFF Policy Trade-off (Bypass Rate vs. Total Cost across N & K) ---
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8), dpi=160)
    # Left: Bypass rate & net cost advantage across B_bypass bins
    bins = np.linspace(0.2, 1.0, 9)
    df_b = df.copy()
    df_b["B_bin"] = pd.cut(df_b["B_bypass"], bins=bins)
    grp_b = df_b.groupby("B_bin", observed=True).agg(
        B_mid=("B_bypass", "mean"),
        stat_bypass=("static_always__bypass_rate", "mean"),
        adpt_bypass=("adaptive_uq__bypass_rate", "mean"),
        uqonly_bypass=("adaptive_uq_only__bypass_rate", "mean"),
    )
    axes[0].plot(grp_b["B_mid"], grp_b["stat_bypass"] * 100, "o-", color="#ef4444", lw=2.3, label="Static Always CFF")
    axes[0].plot(grp_b["B_mid"], grp_b["adpt_bypass"] * 100, "s-", color="#f59e0b", lw=2.2, label="Adaptive (UQ or K>500)")
    axes[0].plot(grp_b["B_mid"], grp_b["uqonly_bypass"] * 100, "d-", color="#22c55e", lw=2.4, label="Adaptive (UQ-Only)")
    axes[0].axhline(10.0, color="#94a3b8", ls=":", lw=1.3, label="10% Bypass Guardrail")
    axes[0].set_title("Shadow-AI Bypass Rate vs. Bypass Threshold B_bypass\n(4,096 Sobol Points Averaged)")
    axes[0].set_xlabel("Bypass Threshold B_bypass (Higher = Harder to Route Around)")
    axes[0].set_ylabel("Mean Bypass Rate (%)")
    axes[0].grid(True, alpha=0.5)
    axes[0].legend(fontsize=8)

    # Right: Cost comparison across log10(K) stakes
    df_k = df.copy()
    df_k["K_bin"] = pd.cut(df_k["log10_K"], bins=np.linspace(0, 4, 9))
    grp_k = df_k.groupby("K_bin", observed=True).agg(
        K_mid=("log10_K", "mean"),
        cost_none=("none__mean_total_cost", "mean"),
        cost_stat=("static_always__mean_total_cost", "mean"),
        cost_adpt=("adaptive_uq__mean_total_cost", "mean"),
        cost_uqonly=("adaptive_uq_only__mean_total_cost", "mean"),
    )
    axes[1].plot(grp_k["K_mid"], grp_k["cost_none"], "o-", color="#f97316", lw=2.2, label="No CFF")
    axes[1].plot(grp_k["K_mid"], grp_k["cost_stat"], "^-", color="#ef4444", lw=2.0, label="Static Always CFF")
    axes[1].plot(grp_k["K_mid"], grp_k["cost_adpt"], "s--", color="#f59e0b", lw=2.0, label="Adaptive (UQ or K>500)")
    axes[1].plot(grp_k["K_mid"], grp_k["cost_uqonly"], "d-", color="#38bdf8", lw=2.4, label="Adaptive (UQ-Only)")
    axes[1].axvline(np.log10(500.0), color="#94a3b8", ls=":", lw=1.2, label="K = 500 Degeneration Line")
    axes[1].set_yscale("log")
    axes[1].set_title("Expected Total Episode Cost vs. Loss Asymmetry log₁₀(L/ΔU)")
    axes[1].set_xlabel("log₁₀(L / ΔU)  [0 = 1×, 4 = 10,000×]")
    axes[1].set_ylabel("Mean Total Episode Cost (log scale)")
    axes[1].grid(True, which="both", alpha=0.4)
    axes[1].legend(fontsize=7.8)

    fig.tight_layout()
    fig.savefig(ARTIFACTS_DIR / "fig2_cff_pareto_bypass.png")
    plt.close(fig)

    # --- Figure 3: Saltelli Sobol Sensitivity Indices ---
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8), dpi=160)
    m1 = sobol_df[sobol_df["metric"] == "static_bypass"].sort_values("S_Ti", ascending=True)
    m2 = sobol_df[sobol_df["metric"] == "adapt_cost_advantage_vs_static"].sort_values("S_Ti", ascending=True)

    y_pos = np.arange(len(m1))
    axes[0].barh(y_pos - 0.18, m1["S_i"], height=0.35, color="#38bdf8", label="First-order Sᵢ")
    axes[0].barh(y_pos + 0.18, m1["S_Ti"], height=0.35, color="#f97316", label="Total-order S_Ti")
    axes[0].set_yticks(y_pos)
    axes[0].set_yticklabels(m1["parameter"])
    axes[0].set_title("Drivers of Shadow-AI Bypass (Static CFF)")
    axes[0].set_xlabel("Sobol Sensitivity Index")
    axes[0].grid(True, axis="x", alpha=0.5)
    axes[0].legend(fontsize=8.5)

    y_pos2 = np.arange(len(m2))
    axes[1].barh(y_pos2 - 0.18, m2["S_i"], height=0.35, color="#22c55e", label="First-order Sᵢ")
    axes[1].barh(y_pos2 + 0.18, m2["S_Ti"], height=0.35, color="#a855f7", label="Total-order S_Ti")
    axes[1].set_yticks(y_pos2)
    axes[1].set_yticklabels(m2["parameter"])
    axes[1].set_title("Drivers of Adaptive CFF Advantage Over Static CFF")
    axes[1].set_xlabel("Sobol Sensitivity Index")
    axes[1].grid(True, axis="x", alpha=0.5)
    axes[1].legend(fontsize=8.5)

    fig.tight_layout()
    fig.savefig(ARTIFACTS_DIR / "fig3_sobol_drivers.png")
    plt.close(fig)


def main() -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    t0 = time.perf_counter()

    # 1. Pre-flight validation
    v_m1 = validate_m1_closed_form()
    v_d = validate_annex_d()
    assert v_m1["passed"] and v_d["passed"], "Pre-flight validation failed!"

    # 2. 4,096-point Sobol sweep
    df = run_sobol_sweep(n_pow2=12, seed=2026)
    df.to_parquet(ARTIFACTS_DIR / "sweep_results.parquet", index=False)

    # 3. Saltelli Sobol indices
    sobol_df = compute_saltelli_sobol(n_base=512, seed=777)
    sobol_df.to_csv(ARTIFACTS_DIR / "sobol_indices.csv", index=False)

    # 4. 2D alpha slice & plots
    slice_df = compute_alpha_sharing_slice(seed=999)
    slice_df.to_csv(ARTIFACTS_DIR / "alpha_slice.csv", index=False)
    generate_figures(df, sobol_df, slice_df)

    # 5. Summary phase boundaries JSON
    summary = {
        "n_sobol_points": int(len(df)),
        "episodes_per_point_per_policy": SimConfig.T,
        "runtime_seconds": round(time.perf_counter() - t0, 2),
        "validation": {"m1_abs_err": v_m1["abs_error"], "annex_d_passed": v_d["passed"]},
        "policy_means": {
            pol: {
                "mean_step_risk": float(df[f"{pol}__mean_step_risk"].mean()),
                "mean_ep_fail": float(df[f"{pol}__mean_ep_fail"].mean()),
                "mean_escape_rate": float(df[f"{pol}__escape_rate"].mean()),
                "mean_total_cost": float(df[f"{pol}__mean_total_cost"].mean()),
                "mean_cvar99_cost": float(df[f"{pol}__cvar99_cost"].mean()),
                "mean_bypass_rate": float(df[f"{pol}__bypass_rate"].mean()),
                "mean_cff_rate": float(df[f"{pol}__cff_rate"].mean()),
            }
            for pol in ("none", "static_always", "adaptive_uq", "adaptive_uq_only")
        },
        "phase_fractions": {
            "adaptive_uq_beats_none_on_cost": float((df["adaptive_uq__mean_total_cost"] < df["none__mean_total_cost"]).mean()),
            "adaptive_uq_beats_static_on_cost": float((df["adaptive_uq__mean_total_cost"] < df["static_always__mean_total_cost"]).mean()),
            "adaptive_uq_dominates_cost_and_trap_low_bypass": float(df["adaptive_strictly_better_with_low_bypass"].mean()),
            "uq_only_beats_none_on_cost": float((df["adaptive_uq_only__mean_total_cost"] < df["none__mean_total_cost"]).mean()),
            "uq_only_beats_static_on_cost": float((df["adaptive_uq_only__mean_total_cost"] < df["static_always__mean_total_cost"]).mean()),
            "uq_only_dominates_cost_and_trap_low_bypass": float(df["uq_only_dominates_cost_and_trap_low_bypass"].mean()),
            "static_bypass_gt_25pct": float((df["static_always__bypass_rate"] > 0.25).mean()),
            "adaptive_uq_bypass_gt_25pct": float((df["adaptive_uq__bypass_rate"] > 0.25).mean()),
            "uq_only_bypass_gt_25pct": float((df["adaptive_uq_only__bypass_rate"] > 0.25).mean()),
        },
        "trigger_F2_check": {
            "adaptive_uq_stakes_dominance_share": float(df["adaptive_strictly_better_with_low_bypass"].mean()),
            "uq_only_dominance_share": float(df["uq_only_dominates_cost_and_trap_low_bypass"].mean()),
            "adaptive_pareto_basin_exists": bool(df["uq_only_dominates_cost_and_trap_low_bypass"].mean() > 0.05),
        },
    }
    (ARTIFACTS_DIR / "phase_boundaries.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
