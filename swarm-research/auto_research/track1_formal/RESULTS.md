# Track 1 Formal & Symbolic Verification Results (Tier 0 + Tier 1)

**Stack:** Zero-LLM deterministic verification using `.venv_track1/bin/python` (`SymPy 1.14.0`, `Z3 5.4.1`, `SciPy 1.18.1`, `Hypothesis 6.170.17`, `pytest 9.2.0`).

---

## 1. Summary of Verified Theorems & Proofs

| Theorem / Check | Tooling | Outcome | Key Result / Proven Condition |
| :--- | :--- | :---: | :--- |
| **M1-NonMonotonic** (`verify_m1.py`) | SymPy + Z3 | **PROVED** | Exact iff condition refined: $R(p)$ is monotone on $(0,1)$ **iff $s + f \le 1$** (`unsat` counterexample). Interior peak $p_{\text{peak}} \in (0,1)$ exists **iff $s + f > 1$** (e.g., $s=0.96, f=0.05 \implies p_{\text{peak}} = 0.4348$, $R(p_{\text{peak}}) = 0.04386 > R(1) = 0.04$). |
| **M1-Monoculture** (`verify_m1.py`) | SymPy + Z3 | **PROVED** | $R$ is strictly increasing in shared causes $c$ for all $p, m, f \in (0,1)$ (`unsat`). At $c=0.60, m=0.20, f=0.05$ vs. peer baseline ($0.05569$), exact break-even error rate is **$p_{\text{crit}} = 6.151\%$** ($2\% \to 0.01926 < 0.05569 < 7\% \to 0.06272$). |
| **M1-Track2-Bypass** (`verify_m1.py`) | Z3 | **PROVED** | Whenever $F_{\text{ss}} > B_{\text{bypass}}$ triggers bypass ($u_0 < \mathrm{VPP}$), residual risk $R$ strictly increases (`unsat`). |
| **M2-FH (Union Bounds)** (`verify_m2.py`) | Z3 | **PROVED** | $\max(p,z) \le p+z-\pi_{11} \le \min(1, p+z)$ for all valid couplings; independence $p+z-pz$ is strictly interior for $p,z \in (0,1)$ (`unsat`). |
| **M2-Copula Stress** (`verify_m2.py`) | SciPy 2D Quadrature | **COMPUTED** | Survival Clayton copula ($\lambda_U \in [0, 0.8]$, $\mathbb{E}[P]=\mathbb{E}[Z]=0.02$). Shows a sharp conditioning effect: when $p^* > \mathbb{E}[P]$ ($K=10$), rising $\lambda_U$ increases silent-trap risk (`0.030 → 0.071`) and $b_{\min}$ (`0 → 0.0297`); when $p^* \lesssim \mathbb{E}[P]$ ($K \ge 25$) and one conditions on $P < p^*$, positive dependence lowers conditional trap probability while still requiring nearly the entire $p^*$ budget for $b_{\min}$ at $K=100$ (`0.0096 / 0.0099`). |
| **M3-Invariance & Salience** (`verify_m3_savi.py`) | Z3 | **PROVED** | Under $(\eta_1, \eta_2) \perp Z \mid X_{\text{obs}}$ and invariance to $X_{\text{sal}}$, $\Lambda(A \mid X_{\text{obs}}) = 1$ identically (`unsat`). |
| **Eckhardt–Lee $c_{\text{eff}}$** (`verify_m3_savi.py`) | SymPy + Z3 | **PROVED** | $1 - s = c_{\text{eff}} + (1 - c_{\text{eff}})\bar{m}$ holds identically; shared difficulty ($\psi = \theta$, $\mathrm{Var}(\theta) > 0$) forces $c_{\text{eff}} \in (0, 1]$ (`unsat`). |
| **SAVI-Ville** (`verify_m3_savi.py`) | Z3 + MC ($10^5$ paths) | **PROVED** | One-step nonnegative supermartingale proved via Z3 (`unsat`); 100,000 trajectories under adversarial optional stopping yield empirical anytime Type-I error **`0.02112 <= 0.05`** (and `34.4%` power at $3\theta_0$). |
| **Property Fuzzing** (`test_track1_properties.py`) | Hypothesis + pytest | **5/5 PASSED** | `12,000` randomized examples across M1, M2-FH, Chains, Eckhardt–Lee, and SAVI passed (`0` failures in `4.65s`). |

---

## 2. Two Mathematical Corrections Surfaced by SymPy / Z3
1. **Tightening M1-NonMonotonic (`s + f > 1`, not `s(1-s) < f`):** Our earlier spec conjectured `f > s(1-s)` as the non-monotonicity threshold. SymPy + Z3 proved that when $f > s(1-s)$ *and* $s + f \le 1$ (e.g., $s=0.85, f=0.14$), both derivative roots lie outside $(0, 1)$, so $R(p)$ remains strictly increasing on $(0, 1)$. Non-monotonicity with an interior peak occurs **if and only if $s + f > 1$** (TPR + FPR $> 1$).
2. **Conditioning Nuance in M2-Copula:** Under exogenous unconditioned stress jumps $s_0 \to s_1$, positive tail dependence always worsens joint trap risk; however, when *conditioning* on low observed modeled risk ($P < p^*$), positive correlation $\lambda_U$ pulls $Z$ down whenever $p^*$ is near or below $\mathbb{E}[P]$, reversing the sign of $\partial \Psi / \partial \lambda_U$ for $K \ge 25$ while still consuming almost the entire $p^*$ budget in $b_{\min}$.

---

## 3. Artifacts
* Scripts: [verify_m1.py](verify_m1.py), [verify_m2.py](verify_m2.py), [verify_m3_savi.py](verify_m3_savi.py), [test_track1_properties.py](test_track1_properties.py)
* Outputs: [m1_proofs.json](artifacts/m1_proofs.json), [m2_proofs.json](artifacts/m2_proofs.json), [m3_savi_proofs.json](artifacts/m3_savi_proofs.json)
