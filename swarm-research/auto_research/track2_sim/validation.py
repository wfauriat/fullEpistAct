"""
Track 2 Validation Suite:
1. Closed-form M1 recovery under N=1, zero stress/friction, pure probability matching.
2. Exact numerical reproduction of monograph Annex D tables (D.3, D.4, D.5).
3. Confusion-matrix conservation and non-negativity invariants.
"""

from __future__ import annotations

import numpy as np
from engine import SimConfig, run_batch_policy


def validate_m1_closed_form() -> dict:
    """Verify simulated R matches P(E)*(1 - s*VPP) within Monte Carlo SE <= 5e-4."""
    p = 0.10
    c = 0.10
    m = 0.20
    f = 0.05
    s = (1.0 - c) * (1.0 - m)
    vpp_exact = (p * s) / (p * s + (1.0 - p) * f)
    r_exact = p * (1.0 - s * vpp_exact)

    # Zero-stress, zero-friction, pure beta_pm = 1 config
    cfg = SimConfig(
        T=2500,
        a_D=1e6,
        b_D=1e6,  # degenerate Beta -> constant D = 0.5
        sigma_H=0.0,
        gamma_p=0.0,
        gamma_c=0.0,
        delta_S=0.0,
        q_nom_to_stress=0.0,
        z_nom=0.0,
        delta_z=0.0,
        l_int=0.0,
        F_crit=-10.0,
        k_beta=10.0,  # beta_pm === 1.0
        phi_alert=0.0,
        phi_CFF=0.0,
        ema_window=5000,  # hold VPP near steady state
    )

    M = 120  # 300,000 total steps -> SE ~ sqrt(0.05*0.95/300000) ~ 4e-4
    params = {
        "N": np.ones(M, dtype=np.int32),
        "alpha": np.zeros(M),
        "p_base": np.full(M, p),
        "c_0": np.full(M, c),
        "m_0": np.full(M, m),
        "f_0": np.full(M, f),
        "K": np.full(M, 25.0),
        "B_bypass": np.ones(M),
    }

    out = run_batch_policy(params, "none", cfg=cfg, seed=123)
    r_sim = float(np.mean(out["mean_step_risk"]))
    err = abs(r_sim - r_exact)
    conservation_ok = bool(
        np.allclose(out["tp"] + out["fp"] + out["tn"] + out["fn"], out["total_steps"])
    )
    nonneg_ok = bool(np.all(out["mean_loss"] >= 0) and np.all(out["mean_delay"] >= 0))

    return {
        "test": "M1_closed_form_recovery",
        "r_exact": r_exact,
        "r_sim": r_sim,
        "abs_error": err,
        "passed": bool(err <= 5e-4 and conservation_ok and nonneg_ok),
        "conservation_ok": conservation_ok,
        "nonneg_ok": nonneg_ok,
    }


def validate_annex_d() -> dict:
    """Reproduce exact closed-form figures from livre.html Annex D (D.3, D.4, D.5)."""
    # D.3: M2 sailing race & night flight
    p_star_25 = 1.0 / (1.0 + 25.0)
    pw_sailing = 1.0 - (1.0 - 0.02) * (1.0 - 0.03)
    d3_ok = abs(p_star_25 - 1.0 / 26.0) < 1e-12 and abs(pw_sailing - 0.0494) < 1e-12

    # D.4: N=4 and N=12, p=0.06, q=0.03 (exact livre.html Table D.4)
    fail_unc_4 = 1.0 - (0.94 ** 4) * 0.97
    fail_chk_4 = 1.0 - ((1.0 - 0.0036) ** 4) * 0.97
    share_q_4 = 0.03 / fail_chk_4

    fail_unc = 1.0 - (0.94 ** 12) * 0.97
    fail_chk = 1.0 - ((1.0 - 0.0036) ** 12) * 0.97
    share_q = 0.03 / fail_chk
    d4_ok = (
        abs(fail_unc_4 - 0.243) < 1e-3
        and abs(fail_chk_4 - 0.0439) < 2e-4
        and abs(share_q_4 - 0.683) < 1e-3
        and abs(fail_unc - 0.538) < 1e-3
        and abs(fail_chk - 0.0711) < 2e-4
        and abs(share_q - 0.422) < 1e-3
    )

    # D.5: Four controller configurations
    configs = [
        ("peer_review", 0.10, 0.10, 0.20, 0.05, 0.72, 0.615, 0.557, 0.0557),
        ("one_model", 0.02, 0.60, 0.20, 0.05, 0.32, 0.116, 0.963, 0.0193),
        ("shared_sharp", 0.02, 0.60, 0.20, 0.005, 0.32, 0.566, 0.819, 0.0164),
        ("indep_sharp", 0.02, 0.10, 0.10, 0.005, 0.81, 0.768, 0.378, 0.00756),
    ]
    d5_checks = []
    for name, p, c, m, f, s_exp, vpp_exp, esc_exp, r_exp in configs:
        s = (1.0 - c) * (1.0 - m)
        vpp = (p * s) / (p * s + (1.0 - p) * f)
        esc = 1.0 - s * vpp
        r = p * esc
        ok = (
            abs(s - s_exp) < 1e-3
            and abs(vpp - vpp_exp) < 1e-3
            and abs(esc - esc_exp) < 1e-3
            and abs(r - r_exp) < 1e-4
        )
        d5_checks.append({"name": name, "s": s, "vpp": vpp, "esc": esc, "r": r, "ok": ok})

    return {
        "test": "Annex_D_reproduction",
        "d3_ok": d3_ok,
        "d4": {"fail_unc": fail_unc, "fail_chk": fail_chk, "share_q": share_q, "ok": d4_ok},
        "d5": d5_checks,
        "passed": bool(d3_ok and d4_ok and all(x["ok"] for x in d5_checks)),
    }


def main() -> None:
    res_m1 = validate_m1_closed_form()
    res_d = validate_annex_d()
    print("=== Track 2 Validation ===")
    print(f"M1 Recovery: exact={res_m1['r_exact']:.5f}, sim={res_m1['r_sim']:.5f}, err={res_m1['abs_error']:.5f}, passed={res_m1['passed']}")
    print(f"Annex D Reproduction: passed={res_d['passed']}")
    for row in res_d["d5"]:
        print(f"  D.5 {row['name']}: s={row['s']:.3f}, VPP={row['vpp']:.3f}, esc={row['esc']:.3f}, R={row['r']:.5f}, ok={row['ok']}")
    if not (res_m1["passed"] and res_d["passed"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
