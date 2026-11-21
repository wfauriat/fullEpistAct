"""
Vectorized socio-technical phase-transition simulator (Track 2).

Implements sequential N-step episodes under Markov stress regimes, Eckhardt-Lee
difficulty-coupled error correlation, behavioral probability matching (VPP EMA),
cumulative friction stock, shadow-AI bypass, and three CFF policies:
('none', 'static_always', 'adaptive_uq').
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class SimConfig:
    """Global fixed simulation constants for Track 2 sweeps."""

    T: int = 1000
    a_D: float = 2.0
    b_D: float = 3.0
    sigma_H: float = 0.08
    gamma_p: float = 0.70
    gamma_c: float = 0.65
    kappa: float = 1.5
    delta_S: float = 0.04
    q_nom_to_stress: float = 0.05
    q_stress_to_nom: float = 0.25
    z_nom: float = 0.002
    delta_z: float = 0.025
    l_int: float = 0.06
    eta_c: float = 0.45
    eta_m: float = 0.40
    tau_H: float = 0.55
    tau_K: float = 500.0
    ema_window: int = 50
    lambda_F: float = 0.90
    phi_CFF: float = 0.14
    phi_alert: float = 0.04
    phi_rec: float = 0.08
    F_max: float = 2.0
    F_crit: float = 0.45
    k_beta: float = 8.0
    u_0: float = 0.15
    c_delay_cff: float = 0.15
    c_delay_alert: float = 0.05


def _sigmoid(x: np.ndarray) -> np.ndarray:
    x_clipped = np.clip(x, -40.0, 40.0)
    return 1.0 / (1.0 + np.exp(-x_clipped))


def run_batch_policy(
    params: dict[str, np.ndarray],
    policy: str,
    cfg: SimConfig = SimConfig(),
    seed: int = 42,
) -> dict[str, np.ndarray]:
    """
    Simulate T sequential episodes in parallel across M parameter vectors.

    Parameters
    ----------
    params : dict with arrays of shape (M,):
        N, alpha, p_base, c_0, m_0, f_0, K, B_bypass
    policy : {'none', 'static_always', 'adaptive_uq'}
    cfg : SimConfig
    seed : int (shared across policies for paired common random numbers)
    """
    if policy not in ("none", "static_always", "adaptive_uq", "adaptive_uq_only"):
        raise ValueError(f"Unknown policy: {policy}")

    rng = np.random.default_rng(seed)
    M = len(params["alpha"])

    N_arr = params["N"].astype(np.int32)
    N_max = int(np.max(N_arr))
    alpha = params["alpha"].astype(np.float64)
    p_base = params["p_base"].astype(np.float64)
    c_0 = params["c_0"].astype(np.float64)
    m_0 = params["m_0"].astype(np.float64)
    f_0 = params["f_0"].astype(np.float64)
    K = params["K"].astype(np.float64)
    B_bypass = params["B_bypass"].astype(np.float64)

    mean_D = cfg.a_D / (cfg.a_D + cfg.b_D)
    ema_alpha = 2.0 / (cfg.ema_window + 1.0)

    # State variables across M runs
    S = np.zeros(M, dtype=np.int8)  # 0=nom, 1=stress
    F = np.zeros(M, dtype=np.float64)

    # Initialize VPP EMA near analytical baseline to avoid cold-start noise
    s_init = (1.0 - c_0) * (1.0 - m_0)
    vpp_ema = (p_base * s_init) / np.maximum(p_base * s_init + (1.0 - p_base) * f_0, 1e-12)

    # Accumulators across T episodes
    sum_escaped_err = np.zeros(M, dtype=np.float64)
    sum_total_err = np.zeros(M, dtype=np.float64)
    sum_silent_trap = np.zeros(M, dtype=np.float64)
    sum_episode_fail = np.zeros(M, dtype=np.float64)
    sum_loss = np.zeros(M, dtype=np.float64)
    sum_delay = np.zeros(M, dtype=np.float64)
    sum_bypass = np.zeros(M, dtype=np.float64)
    sum_cff = np.zeros(M, dtype=np.float64)
    sum_alerts = np.zeros(M, dtype=np.float64)

    tp_tot = np.zeros(M, dtype=np.float64)
    fp_tot = np.zeros(M, dtype=np.float64)
    tn_tot = np.zeros(M, dtype=np.float64)
    fn_tot = np.zeros(M, dtype=np.float64)

    episode_losses = np.zeros((cfg.T, M), dtype=np.float64)

    for t in range(cfg.T):
        # 1. Markov regime transition
        u_trans = rng.random(M)
        to_stress = (S == 0) & (u_trans < cfg.q_nom_to_stress)
        to_nom = (S == 1) & (u_trans < cfg.q_stress_to_nom)
        S = np.where(to_stress, 1, np.where(to_nom, 0, S)).astype(np.int8)

        # 2. Task difficulty & uncertainty probe
        D = rng.beta(cfg.a_D, cfg.b_D, size=M)
        H_hat = np.clip(D + rng.normal(0.0, cfg.sigma_H, size=M), 0.0, 1.0)

        # 3. CFF decision and shadow-AI bypass
        if policy == "none":
            cff_req = np.zeros(M, dtype=bool)
        elif policy == "static_always":
            cff_req = np.ones(M, dtype=bool)
        elif policy == "adaptive_uq_only":
            cff_req = H_hat > cfg.tau_H
        else:
            cff_req = (H_hat > cfg.tau_H) | (K > cfg.tau_K)

        bypassed = cff_req & (F > B_bypass)
        cff_active = cff_req & (~bypassed)

        # 4. Behavioral uptake u_t
        beta_pm = _sigmoid(cfg.k_beta * (F - cfg.F_crit))
        u_t = np.where(
            bypassed,
            cfg.u_0,
            (1.0 - beta_pm) * 1.0 + beta_pm * vpp_ema,
        )

        # 5. Error rate, correlation c_t, miss m_t, omitted stress z_t
        p0_D = p_base * ((0.5 + D) / (0.5 + mean_D))
        p_E = np.clip(p0_D * (1.0 - cfg.gamma_p * alpha) + cfg.delta_S * S, 0.0, 1.0)
        c_t = np.clip(c_0 + cfg.gamma_c * alpha * (D ** cfg.kappa), 0.0, 1.0)
        z_t = cfg.z_nom + cfg.delta_z * S

        c_eff = np.where(cff_active, c_t * (1.0 - cfg.eta_c), c_t)
        m_eff = np.where(cff_active, m_0 * (1.0 - cfg.eta_m), m_0)
        s_base = (1.0 - c_eff) * (1.0 - m_eff)

        # 6. Execute N_max steps (masked by j < N_arr)
        # Draw all step randoms upfront with fixed shapes for clean CRN pairing
        u_err = rng.random((N_max, M))
        u_det = rng.random((N_max, M))
        u_upt = rng.random((N_max, M))
        u_z = rng.random(M)

        ep_escaped = np.zeros(M, dtype=bool)
        ep_alerts = np.zeros(M, dtype=np.float64)
        ep_true_alerts = np.zeros(M, dtype=np.float64)

        for j in range(N_max):
            active_j = j < N_arr
            launder_mult = (1.0 - cfg.l_int) ** j
            s_j = s_base * launder_mult

            err_j = active_j & (u_err[j] < p_E)
            alert_j = np.where(
                err_j,
                u_det[j] < s_j,
                active_j & (u_det[j] < f_0),
            )
            audited_j = alert_j & (u_upt[j] < u_t)
            escaped_j = err_j & (~audited_j)

            tp_j = err_j & alert_j
            fp_j = (~err_j) & active_j & alert_j
            tn_j = (~err_j) & active_j & (~alert_j)
            fn_j = err_j & (~alert_j)

            tp_tot += tp_j
            fp_tot += fp_j
            tn_tot += tn_j
            fn_tot += fn_j

            sum_total_err += err_j
            sum_escaped_err += escaped_j
            ep_escaped |= escaped_j
            ep_alerts += alert_j
            ep_true_alerts += tp_j

        z_fail = u_z < z_t
        ep_fail = ep_escaped | z_fail
        # Silent trap: frame cleared (no audited alert stopped an escape) yet world fails via z or missed err
        silent_trap = ep_fail & (ep_alerts == 0)

        # Update VPP EMA on episodes with >= 1 alert
        has_alert = ep_alerts > 0
        ep_vpp = np.where(has_alert, ep_true_alerts / np.maximum(ep_alerts, 1.0), vpp_ema)
        vpp_ema = np.where(has_alert, (1.0 - ema_alpha) * vpp_ema + ema_alpha * ep_vpp, vpp_ema)

        # Update friction stock F_t
        F = np.clip(
            cfg.lambda_F * F
            + cfg.phi_CFF * cff_active.astype(np.float64)
            + cfg.phi_alert * ep_alerts
            - cfg.phi_rec,
            0.0,
            cfg.F_max,
        )

        # Loss & delay accounting (normalized so dU = 1, loss = K)
        ep_loss = np.where(ep_fail, K, 0.0)
        ep_delay = cfg.c_delay_cff * cff_active.astype(np.float64) + cfg.c_delay_alert * ep_alerts
        total_cost = ep_loss + ep_delay

        episode_losses[t] = total_cost
        sum_episode_fail += ep_fail
        sum_silent_trap += silent_trap
        sum_loss += ep_loss
        sum_delay += ep_delay
        sum_bypass += bypassed
        sum_cff += cff_active
        sum_alerts += ep_alerts

    total_steps = cfg.T * N_arr.astype(np.float64)
    mean_cost = np.mean(episode_losses, axis=0)
    # CVaR_0.99 over the T sequential episodes
    sorted_cost = np.sort(episode_losses, axis=0)
    tail_k = max(1, int(np.ceil(0.01 * cfg.T)))
    cvar_99 = np.mean(sorted_cost[-tail_k:], axis=0)

    return {
        "mean_step_risk": sum_escaped_err / total_steps,
        "mean_ep_fail": sum_episode_fail / cfg.T,
        "escape_rate": sum_escaped_err / np.maximum(sum_total_err, 1e-12),
        "silent_trap_rate": sum_silent_trap / cfg.T,
        "mean_loss": sum_loss / cfg.T,
        "mean_delay": sum_delay / cfg.T,
        "mean_total_cost": mean_cost,
        "cvar99_cost": cvar_99,
        "bypass_rate": sum_bypass / cfg.T,
        "cff_rate": sum_cff / cfg.T,
        "empirical_vpp": tp_tot / np.maximum(tp_tot + fp_tot, 1e-12),
        "tp": tp_tot,
        "fp": fp_tot,
        "tn": tn_tot,
        "fn": fn_tot,
        "total_steps": total_steps,
    }
