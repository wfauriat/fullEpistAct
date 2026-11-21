# Track 2 Simulation Results: Socio-Technical Phase Boundaries

**Execution:** Zero-LLM deterministic simulator (`engine.py`, `validation.py`, `sweeps.py`) executed via `/opt/venvs/pyDS/bin/python` (`4,096` Sobol quasi-random worlds $\times$ `1,000` sequential episodes $\times$ `4` CFF policies = `16,384,000` simulated episodes; runtime `28.12s`; Saltelli Sobol indices on `n=512` base samples).

---

## 1. Pre-Flight Validation (`validation.py`)
* **M1 Closed-Form Recovery:** Exact $R = 0.05569$, Simulated $\hat{R} = 0.05564$ (`abs_error = 5.56e-5 <= 5e-4`, `passed = True`).
* **Annex D Reproduction:** Exact recovery of `livre.html` Tables D.3, D.4 ($N=4, 12, p=6\%, q=3\%$), and all four columns of D.5 (`passed = True`).

---

## 2. Aggregate Policy Comparison (4,096 Sobol Worlds)

| Policy | Mean Step Risk | Mean Episode Fail | Mean Escape Rate | Mean Total Cost | Mean Bypass Rate | CFF Rate | Beats `none` (Cost) | Beats `static` (Cost) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`none`** | `4.39%` | `23.25%` | `57.24%` | `252.63` | `0.00%` | `0.00%` | — | — |
| **`static_always`** | `5.60%` | `27.93%` | `73.30%` | `303.42` | `31.06%` | `68.94%` | — | — |
| **`adaptive_uq` ($\hat{H}_t > \tau_H \lor K > 500$)** | `4.67%` | `24.66%` | `60.80%` | `300.75` | `10.99%` | `38.55%` | `40.1%` | `66.8%` |
| **`adaptive_uq_only` ($\hat{H}_t > \tau_H$)** | **`4.22%`** | **`23.09%`** | **`54.79%`** | **`250.79`** | **`1.30%`** | `23.94%` | **`61.1%`** | **`98.4%`** |

* **Key Pareto Result (`adaptive_uq_only`):** Purely uncertainty-triggered CFFs ($\hat{H}_t > \tau_H$) strictly beat **both** `none` and `static_always` on mean total cost with `< 10%` bypass in **`59.50%`** of all 4,096 worlds.

---

## 3. Three Core Findings

1. **Mean Risk Drops While Escape Probability Climbs (`fig1_monoculture_phase.png`):**
   * Increasing shared-AI intensity $\alpha \in [0, 1]$ lowers mean escaped step risk across baseline error rates (e.g., `3.89% → 1.67%` at $p_0 = 10\%$), while pushing per-error escape probability up from `~35–37%` to `~48–52%`. Uncertainty-gated CFFs lower both curves uniformly.
2. **Triggering Human Friction on High Stakes ($K > 500$) Backfires Into Shadow AI (`fig2_cff_pareto_bypass.png`):**
   * `static_always` induces `31.1%` average Shadow-AI bypass (`>25%` in `55.5%` of worlds), raising episode failure (`27.93%`) and total cost (`303.42`) **above doing nothing (`none`: `23.25%`, `252.63`)**.
   * Crucially, the spec's naive `adaptive_uq` rule ($\hat{H}_t > \tau_H \lor K > 500$) also collapses above $K = 500$: when every task in a high-stakes environment triggers manual friction, it degenerates into `static_always`. High-stakes ($K > 500$) regimes require **non-bypassable architectural locks (`verrous`)**, reserving human CFFs strictly for **high epistemic uncertainty** ($\hat{H}_t > \tau_H$, which holds bypass to `1.30%`).
3. **Chain Depth $N$ and False Alarms $f_0$ Drive Friction Exhaustion (`fig3_sobol_drivers.png`):**
   * Saltelli Sobol indices show `static_always` bypass is driven primarily by pipeline depth $N$ ($S_{Ti} = 0.504, S_i = 0.418$), bypass threshold $B_{\text{bypass}}$ ($S_{Ti} = 0.326$), and false-alarm rate $f_0$ ($S_{Ti} = 0.240$)—because multi-step agent chains multiply alert volume and rapidly exhaust human friction budgets.

---

## 4. Generated Artifacts
* [engine.py](engine.py), [validation.py](validation.py), [sweeps.py](sweeps.py)
* [phase_boundaries.json](artifacts/phase_boundaries.json), [sweep_results.parquet](artifacts/sweep_results.parquet), [sobol_indices.csv](artifacts/sobol_indices.csv), [alpha_slice.csv](artifacts/alpha_slice.csv)
* [fig1_monoculture_phase.png](artifacts/fig1_monoculture_phase.png), [fig2_cff_pareto_bypass.png](artifacts/fig2_cff_pareto_bypass.png), [fig3_sobol_drivers.png](artifacts/fig3_sobol_drivers.png)
