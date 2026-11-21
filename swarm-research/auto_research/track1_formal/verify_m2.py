"""
Track 1 Formal Verification — Model M2 Extensions:
1. Lemma M2-FH: Z3 universal proof of Fréchet–Hoeffding union bounds & strict interiority of independence.
2. Theorem M2-Copula: Numerical survival-Clayton copula stress coupling computing b_min(theta, p*, delta)
   and identifying infeasible departure boundaries across L/dU and upper-tail dependence lambda_U.
3. Decision-Theory Identities: SymPy/Z3 checks for Manski minimax-regret & Hansen–Sargent KL tilting.
"""

from __future__ import annotations

import json
from pathlib import Path
import numpy as np
from scipy import integrate, optimize
import sympy as sp
import z3


def prove_m2_frechet_hoeffding() -> dict:
    p, z, pi11 = z3.Reals("p z pi11")
    fh_low = z3.If(p + z - 1 > 0, p + z - 1, 0)
    fh_high = z3.If(p < z, p, z)
    max_pz = z3.If(p > z, p, z)
    min_sum1 = z3.If(p + z < 1, p + z, 1)

    # 1. Prove max(p, z) <= p + z - pi11 <= min(1, p + z) for all valid joint couplings
    s1 = z3.Solver()
    s1.add(p >= 0, p <= 1, z >= 0, z <= 1, pi11 >= fh_low, pi11 <= fh_high)
    pw = p + z - pi11
    s1.add(z3.Or(pw < max_pz, pw > min_sum1))
    fh_bounds_unsat = s1.check() == z3.unsat

    # 2. Prove independence lies strictly interior for p, z in (0, 1)
    s2 = z3.Solver()
    s2.add(p > 0, p < 1, z > 0, z < 1)
    pw_indep = p + z - p * z
    s2.add(z3.Or(pw_indep <= max_pz, pw_indep >= min_sum1))
    indep_interior_unsat = s2.check() == z3.unsat

    # 3. Non-vacuity SAT witness
    s3 = z3.Solver()
    s3.add(p == z3.RealVal("0.02"), z == z3.RealVal("0.03"), pi11 >= fh_low, pi11 <= fh_high)
    sat_ok = s3.check() == z3.sat

    return {
        "z3_fh_union_bounds_unsat": fh_bounds_unsat,
        "z3_independence_strictly_interior_unsat": indep_interior_unsat,
        "z3_nonvacuity_sat": sat_ok,
    }


def _survival_clayton_density(u: np.ndarray, v: np.ndarray, theta: float) -> np.ndarray:
    """Density of survival Clayton copula (positive upper-tail dependence lambda_U = 2^(-1/theta))."""
    if theta <= 1e-8:
        return np.ones_like(u)
    a = np.clip(1.0 - u, 1e-12, 1.0 - 1e-12)
    b = np.clip(1.0 - v, 1e-12, 1.0 - 1e-12)
    base = a ** (-theta) + b ** (-theta) - 1.0
    return (1.0 + theta) * (a * b) ** (-theta - 1.0) * (base ** (-2.0 - 1.0 / theta))


def compute_m2_copula_table() -> dict:
    """
    Model latent stress S coupling (P, Z) via survival Clayton copula C_bar_theta with
    Beta marginals centered near sailing/flight regimes:
      P ~ Beta(1.5, 73.5) (mean E[P] = 0.02), Z ~ Beta(1.2, 58.8) (mean E[Z] = 0.02).
    For stakes K = L/dU in {10, 25, 100, 1000, 10000} and upper tail dependence lambda_U in [0, 0.8]:
      Compute silent-trap probability Psi(b) and minimum safe margin b_min for delta=0.05
      when decision-maker observes noisy estimate P_hat ~ P (evaluated at p_hat = 0.02, or
      conditioning on P <= p* - b).
    """
    from scipy.stats import beta as beta_dist

    p_dist = beta_dist(1.5, 73.5)   # E[P] = 0.02
    z_dist = beta_dist(1.2, 58.8)   # E[Z] = 0.02

    # High-accuracy 2D tensor quadrature on (u, v) in [0, 1]^2
    n_grid = 180
    pts = (np.arange(n_grid) + 0.5) / n_grid
    du = 1.0 / n_grid
    U, V = np.meshgrid(pts, pts, indexing="ij")
    P_grid = p_dist.ppf(U)
    Z_grid = z_dist.ppf(V)
    PW_grid = P_grid + Z_grid - P_grid * Z_grid

    lambdas = [0.0, 0.2, 0.4, 0.6, 0.8]
    stakes = [10, 25, 100, 1000]
    delta = 0.05

    rows = []
    for K in stakes:
        p_star = 1.0 / (1.0 + K)
        for lam in lambdas:
            theta = 0.0 if lam <= 0 else -1.0 / np.log2(lam)
            dens = _survival_clayton_density(U, V, theta)
            weights = dens * (du * du)
            weights /= weights.sum()

            # Under decision rule P + b < p_star (modeled failure rate plus humility margin b),
            # silent trap event is (P + b < p_star) & (PW >= p_star).
            # Conditional probability Psi(b) = Pr(PW >= p_star | P < p_star - b).
            def psi_of_b(b_val: float) -> float:
                admitted = P_grid < (p_star - b_val)
                p_adm = float(weights[admitted].sum())
                if p_adm < 1e-9:
                    return 0.0
                trap = admitted & (PW_grid >= p_star)
                return float(weights[trap].sum() / p_adm)

            psi_0 = psi_of_b(0.0)
            # Find smallest b in [0, p_star] such that psi_of_b(b) <= delta
            b_grid = np.linspace(0.0, p_star, 200)
            psis = [psi_of_b(float(bv)) for bv in b_grid]
            feasible = [bv for bv, pv in zip(b_grid, psis) if pv <= delta]
            b_min = float(feasible[0]) if feasible else float(p_star)
            infeasible_departure = b_min >= 0.98 * p_star

            rows.append({
                "K": K,
                "p_star": p_star,
                "lambda_U": lam,
                "theta": float(theta),
                "psi_at_b0": psi_0,
                "b_min_for_delta_005": b_min,
                "infeasible_departure": infeasible_departure,
            })

    # Verify monotonicity of psi_at_b0 in lambda_U for each K
    mono_ok = True
    for K in stakes:
        vals = [r["psi_at_b0"] for r in rows if r["K"] == K]
        if any(vals[i + 1] < vals[i] - 1e-6 for i in range(len(vals) - 1)):
            mono_ok = False

    return {"delta": delta, "monotonic_trap_in_lambda_U": mono_ok, "grid_results": rows}


def prove_decision_identities() -> dict:
    # Manski minimax-regret: max regret act = (dU+L)*(p_hi - p*), abstain = (dU+L)*(p* - p_lo)
    p, p_hi, p_star = sp.symbols("p p_hi p_star", real=True)
    # Act iff (p_hi - p*) < (p* - p)  <=>  p + (p_hi - p)/2 < p*
    b_mmr = (p_hi - p) / 2
    lhs = sp.simplify(p + b_mmr - p_star)
    rhs = sp.simplify(((p_hi - p_star) - (p_star - p)) / 2)
    mmr_exact = sp.simplify(lhs - rhs) == 0

    # Hansen-Sargent exponential tilting on Bernoulli(p)
    zp, zdul, ztheta = z3.Reals("p dUL theta")
    # Since exp(dUL/theta) > 1 for dUL > 0, theta > 0, odds(q*) > odds(p) => q* > p.
    # Verify algebraic odds equivalence in Z3 using e_tilt > 1:
    e_tilt, q = z3.Reals("e_tilt q")
    s = z3.Solver()
    s.add(zp > 0, zp < 1, q > 0, q < 1, e_tilt > 1)
    s.add(q / (1 - q) == (zp / (1 - zp)) * e_tilt)
    s.add(q <= zp)
    hs_unsat = s.check() == z3.unsat

    return {"sympy_manski_mmr_exact": mmr_exact, "z3_hansen_sargent_q_gt_p_unsat": hs_unsat}


def main() -> None:
    res = {
        "M2_Frechet_Hoeffding": prove_m2_frechet_hoeffding(),
        "M2_Copula_Stress": compute_m2_copula_table(),
        "M2_Decision_Identities": prove_decision_identities(),
    }
    out_path = Path(__file__).resolve().parent / "artifacts"
    out_path.mkdir(parents=True, exist_ok=True)
    (out_path / "m2_proofs.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print("FH:", res["M2_Frechet_Hoeffding"])
    print("Decision:", res["M2_Decision_Identities"])
    print("Copula monotonic:", res["M2_Copula_Stress"]["monotonic_trap_in_lambda_U"])
    for r in res["M2_Copula_Stress"]["grid_results"]:
        print(f"  K={r['K']:4d} (p*={r['p_star']:.4f}) lam={r['lambda_U']:.1f} -> Psi(0)={r['psi_at_b0']:.3f}, b_min={r['b_min_for_delta_005']:.4f}, inf={r['infeasible_departure']}")


if __name__ == "__main__":
    main()
