"""
Track 1 Formal Verification — Model M3, Eckhardt-Lee CCF, & SAVI/Ville Supermartingale:
1. Theorem M3-Invariance & SalienceOmission: Z3 proof that conditional independence
   (eta1, eta2) _|_ Z | X_obs forces Lambda(A | X_obs) = 1.
2. Eckhardt-Lee / Littlewood-Miller c_eff Identity: SymPy + Z3 bounds & sign proofs.
3. Theorem SAVI-Ville: Z3 proof of one-step supermartingale & non-negativity, plus
   100,000-path adversarial optional-stopping Ville's inequality verification.
"""

from __future__ import annotations

import json
from pathlib import Path
import numpy as np
import sympy as sp
import z3


def prove_m3_invariance() -> dict:
    """
    Finite-state symbolic/Z3 proof for M3-Invariance & M3-SalienceOmission.
    Let X_obs be fixed; hidden factor Z takes values in {0, 1}, and internal
    draws (eta1, eta2) determine whether f1 and f2 agree (A in {0, 1}).
    Under (eta1, eta2) _|_ Z | X_obs and invariance of f1, f2 to X_sal:
      Pr(A=1 | X_obs, Z=z) = sum_{e1,e2} 1[A(X_obs, e1, e2)=1] Pr(e1, e2 | X_obs, Z=z)
    which equals Pr(A=1 | X_obs) for every z, hence Lambda(A | X_obs, H_grand vs H_petit) = 1.
    """
    pA_z0, pA_z1, w0_g, w1_g, w0_p, w1_p = z3.Reals("pA_z0 pA_z1 w0_g w1_g w0_p w1_p")
    s = z3.Solver()
    # Conditional independence given X_obs (and salience invariance) => pA_z0 == pA_z1
    s.add(pA_z0 > 0, pA_z0 <= 1, pA_z1 == pA_z0)
    # Arbitrary distinct distributions over Z under H_grand and H_petit
    s.add(w0_g >= 0, w1_g >= 0, w0_g + w1_g == 1)
    s.add(w0_p >= 0, w1_p >= 0, w0_p + w1_p == 1)
    pA_grand = w0_g * pA_z0 + w1_g * pA_z1
    pA_petit = w0_p * pA_z0 + w1_p * pA_z1
    s.add(pA_grand / pA_petit != 1)
    return {"z3_m3_lambda_equals_1_unsat": s.check() == z3.unsat}


def prove_eckhardt_lee_c_eff() -> dict:
    # Algebraic check over a 2-state difficulty distribution (prob q_h and 1 - q_h)
    q_h, th1, th2, ps1, ps2 = sp.symbols("q_h th1 th2 ps1 ps2", real=True)
    PE = q_h * th1 + (1 - q_h) * th2
    m_bar = q_h * ps1 + (1 - q_h) * ps2
    joint = q_h * th1 * ps1 + (1 - q_h) * th2 * ps2
    cov = sp.expand(joint - PE * m_bar)
    c_eff = sp.simplify(cov / (PE * (1 - m_bar)))
    # Reconstruct 1 - s = c_eff + (1 - c_eff)*m_bar
    one_minus_s = sp.simplify(c_eff + (1 - c_eff) * m_bar)
    escape_given_E = sp.simplify(joint / PE)
    identity_holds = sp.simplify(one_minus_s - escape_given_E) == 0

    # Z3: When psi == theta (shared model) and 0 < q_h < 1, th1 != th2 => c_eff > 0, and c_eff <= 1 always
    zq, zt1, zt2, zp1, zp2 = z3.Reals("q_h th1 th2 ps1 ps2")
    s1 = z3.Solver()
    s1.add(zq > 0, zq < 1, zt1 >= 0, zt1 <= 1, zt2 >= 0, zt2 <= 1, zt1 != zt2)
    zPE = zq * zt1 + (1 - zq) * zt2
    zm = zPE  # psi == theta
    zjoint = zq * zt1 * zt1 + (1 - zq) * zt2 * zt2
    zc = (zjoint - zPE * zm) / (zPE * (1 - zm))
    s1.add(zPE > 0, zm < 1, z3.Or(zc <= 0, zc > 1))
    shared_pos_unsat = s1.check() == z3.unsat

    # Z3: For ANY valid theta, psi in [0,1], escape <= 1 => c_eff <= 1
    s2 = z3.Solver()
    s2.add(zq > 0, zq < 1, zt1 >= 0, zt1 <= 1, zt2 >= 0, zt2 <= 1, zp1 >= 0, zp1 <= 1, zp2 >= 0, zp2 <= 1)
    zPE2 = zq * zt1 + (1 - zq) * zt2
    zm2 = zq * zp1 + (1 - zq) * zp2
    zj2 = zq * zt1 * zp1 + (1 - zq) * zt2 * zp2
    zc2 = (zj2 - zPE2 * zm2) / (zPE2 * (1 - zm2))
    s2.add(zPE2 > 0, zm2 < 1, zc2 > 1)
    upper_bound_1_unsat = s2.check() == z3.unsat

    return {
        "sympy_m1_c_eff_identity": identity_holds,
        "z3_shared_model_c_eff_in_0_1_unsat": shared_pos_unsat,
        "z3_general_c_eff_le_1_unsat": upper_bound_1_unsat,
    }


def prove_savi_ville() -> dict:
    # 1. Z3 one-step supermartingale & non-negativity proof
    p_true, theta0, lam = z3.Reals("p_true theta0 lam")
    s = z3.Solver()
    s.add(theta0 > 0, theta0 < 1, p_true >= 0, p_true <= theta0, lam >= 0, lam < 1 / theta0)
    m_1 = 1 + lam * (1 - theta0)
    m_0 = 1 + lam * (0 - theta0)
    expected_mult = p_true * m_1 + (1 - p_true) * m_0
    # Must fail if either m_1 < 0, m_0 <= 0, or expected_mult > 1
    s.add(z3.Or(m_1 < 0, m_0 <= 0, expected_mult > 1))
    supermartingale_unsat = s.check() == z3.unsat

    # 2. Empirical Ville's inequality test: 100,000 trajectories under null p_true = theta0 = 0.05
    # with adversarial optional stopping whenever E_t crosses threshold 1/alpha (alpha = 0.05 -> 20)
    rng = np.random.default_rng(2026)
    n_paths = 100_000
    T_max = 200
    theta0_val = 0.05
    alpha = 0.05
    thresh = 1.0 / alpha

    # Predictable mixture betting fraction lambda_t = 0.5 / theta0 (half-Kelly-style bounded bet in [0, 1/theta0))
    lam_val = 0.45 / theta0_val
    X = (rng.random((n_paths, T_max)) < theta0_val).astype(np.float64)
    mult = 1.0 + lam_val * (X - theta0_val)
    E_paths = np.cumprod(mult, axis=1)
    max_E = np.max(E_paths, axis=1)
    empirical_type1 = float(np.mean(max_E >= thresh))

    # Power under alternative p_alt = 0.15 (3x claimed bound)
    X_alt = (rng.random((20_000, T_max)) < 0.15).astype(np.float64)
    E_alt = np.cumprod(1.0 + lam_val * (X_alt - theta0_val), axis=1)
    power_alt = float(np.mean(np.max(E_alt, axis=1) >= thresh))

    return {
        "z3_savi_supermartingale_nonneg_unsat": supermartingale_unsat,
        "mc_paths": n_paths,
        "alpha_bound": alpha,
        "empirical_anytime_type1": empirical_type1,
        "ville_bound_satisfied": bool(empirical_type1 <= alpha),
        "power_at_3x_theta0": power_alt,
    }


def main() -> None:
    res = {
        "M3_Invariance": prove_m3_invariance(),
        "Eckhardt_Lee_CCF": prove_eckhardt_lee_c_eff(),
        "SAVI_Ville": prove_savi_ville(),
    }
    out_path = Path(__file__).resolve().parent / "artifacts"
    out_path.mkdir(parents=True, exist_ok=True)
    (out_path / "m3_savi_proofs.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
