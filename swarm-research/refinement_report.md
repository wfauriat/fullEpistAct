# Refinement Pass Report: Adversarial Falsifiers, 2021–2026 Empirical Audit & Formal Bridges

**Scope:** Synthesizes the three **Gemini 4 Hydrogen (High)** refinement passes conducted after [cross_review_monograph.md](cross_review_monograph.md) and [synthesis.md](synthesis.md), paired with the automated research specifications in [specs_automated_research.md](specs_automated_research.md):
1. [01_adversarial_falsifiers.md](research/refinement/01_adversarial_falsifiers.md) — Active hunt for counter-evidence, scope-narrowing moderators, and backfire mechanisms against *Agir d’après une représentation du monde* ([livre.html](livre.html)) and [synthesis.md](synthesis.md).
2. [02_empirical_2024_2026.md](research/refinement/02_empirical_2024_2026.md) — Primary-source audit of 2021–2026 empirical studies (sample sizes, designs, effect sizes, caveats, and citation corrections).
3. [03_formal_bridges.md](research/refinement/03_formal_bridges.md) — Mathematical and architectural extensions linking Models **M1–M3** and Ch. 10–18 to coupled-stress copulas, $\mathcal{M}$-open Bayesianism / SAVI, Eckhardt–Lee CCFs, and CaMeL / VeriGuard / Lean 4 containment.

---

## Executive Takeaway: What Survives, What Narrows, and What Breaks

Subjecting both the monograph and our initial synthesis to a primary-source and adversarial stress test leaves the **core formal architecture (M1, M2, M3, Ch. 13 matrix)** intact—while forcing **four material refinements** to their empirical claims, scope boundaries, and remedy designs:

1. **In-frame salience elicitation *is* often solvable internally:** Test-time compute scaling (Snell et al. 2024), Process Reward Models (Lightman et al. 2023/2024), and evidence-grounded debate (Khan et al. 2024) genuinely catch *in-frame* reasoning and salience omissions. **Proposition 3(a)** holds strictly for *out-of-frame* omissions ($z \notin \Theta$), whereas Ch. 12.4's pessimism about re-interrogation narrows to *unguided* self-correction (Kamoi et al. 2024) and low-entropy systematic errors.
2. **Human–AI teams are bifurcated by task type and familiarity—not uniformly negative:** While Vaccaro et al. (2024) ($g = -0.23$), Becker et al. (2025) ($+19\%$ slowdown on mature OSS), and Goh et al. (2024, *JAMA Network Open* RCT) confirm negative/null synergy in diagnostic decisions and legacy-code maintenance, controlled greenfield coding (Peng et al. 2023, $+55.8\%$ speed) and enterprise junior/short-tenure deployments (Cui et al. 2024, $+26.08\%$ PRs/week) show real throughput gains.
3. **Shared models often reduce *mean* routine risk $R$ even when $\rho > 0$:** By M1 and Field 8's escape equation, when $p_{\text{AI}} \ll p$ and $q_{\text{AI}} \ll q$, mean residual risk drops below unassisted baselines despite correlation—and pretraining collapse requires *data replacement* rather than *accumulation* (Gerstgrasser et al. 2024). The durable risk concentrates in **asymmetric tails** ($p^* \to 0$), **welfare homogenization** (Kleinberg & Raghavan 2021; Bommasani et al. 2022), and **live post-2023 RAG contamination**.
4. **Uniform Part V friction backfires via UX drop and Shadow AI:** Buçinca et al. (2021) ($N=199$) confirms CFFs cut overreliance at the cost of lower satisfaction; Bastani et al. (*PNAS*) and enterprise telemetry show rigid barriers push users toward unguarded Shadow AI, while Rae, Provan & Dekker (2018) warn against *safety clutter*. Viable remedies must be **uncertainty-tiered** and **orchestrator-enforced** (CaMeL / VeriGuard) rather than uniform manual checklists.

---

## 1. Consolidated Adversarial Falsification Matrix

Synthesized from [01_adversarial_falsifiers.md](research/refinement/01_adversarial_falsifiers.md):

| Fault Line | Claim Tested | Sharpest Counter-Evidence & Moderators | Classification | Required Scope Revision |
| :--- | :--- | :--- | :--- | :--- |
| **1. Internal & Iterative Checks** | Prop. 3(a), Ch. 12.4, Law 1 | **Snell et al. (2024)** (test-time compute matches 14$\times$ larger model); **Lightman et al. (2023/2024)** (PRMs solve 78% MATH subset); **Khan et al. (2024)** (grounded debate lifts judge accuracy 48%$\to$76% / 60%$\to$88%). Bounded by **Kamoi et al. (2024)**: unguided self-correction fails without external verifiers. | **Genuine falsifier** on in-frame salience; **Category error** if extended to $z \notin \Theta$. | Separate *in-frame salience elicitation* (where search/PRMs/grounded debate work) from *structural omission* ($z \notin \Theta$). |
| **2. Human–AI Synergy & Speed** | Ch. 15; Vaccaro et al. (2024); Becker et al. (2025) | **Peng et al. (2023)** ($+55.8\%$ greenfield JS task); **Cui et al. (2024)** ($+26.08\%$ PRs/wk, concentrated in junior/short-tenure devs); **Vaccaro et al. (2024)** positive synergy on content creation & human > AI tasks; contrasted with **Goh et al. (2024)** clinical RCT (~76% vs. ~74% NS) & **Becker et al. (2025)** ($+19\%$ slowdown on 5-yr mature OSS). | **Scope-narrowing moderators**: task structure, codebase familiarity, and tenure. | Parameterize Ch. 15 claims by task (creation vs. decision), developer tenure, and implicit-invariant density. |
| **3. Shared Models & Collapse** | Ch. 16; Shumailov et al. (2024); Coupling C | Accuracy dominance ($p_{\text{AI}} \ll p, q_{\text{AI}} \ll q$) reduces mean $R$ despite $c > 0$; **Gerstgrasser et al. (2024)** proves accumulation alongside real data bounds test error; verifier-filtered loops improve math/code. Tail/welfare warnings hold via **Kleinberg & Raghavan (2021)** & **Bommasani et al. (2022)**. | **Genuine qualifier** on mean risk & replacement collapse; **Tail warning intact**. | Formalize the accuracy-vs.-$c$ tipping curve in Ch. 16; qualify Ch. 16.3 with Gerstgrasser accumulation vs. live RAG drift. |
| **4. Part V Friction & Provenance Tags** | Ch. 17.3–18 (CFFs, *état de vérification*, locks) | **Buçinca et al. (2021)** (CFFs cut satisfaction); Shadow AI bypass under deadlines; **Rae, Provan & Dekker (2018)** (*safety clutter*); Hollnagel (**Safety-II** adaptability erosion); **Liang et al. (2023)** (61.22%–97%+ false positives on TOEFL essays by AI detectors). | **Genuine backfire** against uniform manual gates and AI-origin policing. | Replace uniform friction and self-declared prose tags with *uncertainty-tiered CFFs*, clutter audits, and CaMeL/VeriGuard taint metadata. |

---

## 2. Primary-Source Empirical Audit & Citation Repairs

Synthesized from [02_empirical_2024_2026.md](research/refinement/02_empirical_2024_2026.md). This pass caught **concrete citation, venue, and causal over-extrapolation errors** across both `livre.html` and our earlier Phase 1–2 files:

### 2.1 Key Corrections Required Across Project Files
1. **Kim et al. (2024):** Published at ***ACM FAccT 2024*** ($N = 404$), **not** *ACM CHI* as mis-cited in `research/09` and `cross_review_monograph.md`.
2. **Liang et al. (2023) vs. Liang et al. (2024):** Two distinct papers were conflated in `research/08` and `cross_review_monograph.md`:
   * *Non-native detector bias:* **Liang et al. (2023, *Patterns*)** — audited 7 GPT detectors on 91 TOEFL essays (`61.22%` overall FPR, up to `97%+` on individual detectors).
   * *Peer-review LLM footprints:* **Liang et al. (2024)** — estimated `6.5%–16.9%` LLM-modified review text across **ICLR 2024, NeurIPS 2023, CoRL 2023, and EMNLP 2023** (`ICML` inclusion cited in `research/08` is **`[UNVERIFIED]`**).
3. **Steyvers et al. (2025):** *Nature Machine Intelligence* ($N = 301$, GPT-3.5 / PaLM 2 / GPT-4o); published title is *"What large language models know and what people think they know"* (not the preprint title cited in `research/09`).
4. **Causal vs. Observational Overstatement on Budzyń et al. (2025):** `synthesis.md` overstated Budzyń et al. ($N = 1,443$ non-AI colonoscopies across 4 Polish centres: ADR `28.4% → 22.4%`, $-6.0\%$, 95% CI $[-10.5, -1.6]$, $\text{OR} = 0.69$) as causal proof of deskilling; it is a **non-randomized observational before/after study** vulnerable to temporal/patient-mix confounders. Causal proof of unaided decay comes from **Bastani et al. (*PNAS*)** ($\sim 1,000$ students: GPT Base `$+48%$` practice / `$-17%$` unaided exam; GPT Tutor `$+127%$` practice / no exam decay—the `$+127%$` Tutor gain had been omitted from prior summaries).
5. **Items Flagged `[UNVERIFIED]` Requiring Primary Inspection or Removal:**
   * Attributing an *"ownership penalty"* against disclosed AI assistance specifically to **Doshi & Hauser (2024)** (`n=300` creators / `n=600` raters on 8-sentence stories) could not be verified in retrieved primary summaries of that paper (`research/09`, `cross_review_monograph.md`, and `01_adversarial_falsifiers.md` carried this attribution over).
   * Exact metrics/sample sizes for the EMNLP 2025 **DBG score**, *"millions of GitHub PRs"* analysis (`research/08`), and quantitative **Retrieval Collapse** rates in 2025–2026 RAG studies remain `[UNVERIFIED]` in this pass.

---

## 3. Formal & Architectural Upgrades to the Monograph's Models

Synthesized from [03_formal_bridges.md](research/refinement/03_formal_bridges.md):

1. **Model M2 Under Dependence & Common Stress:**
   * Separating **fixed-marginal event coupling** ($\max(p,z) \le p_w \le \min(1, p+z)$) from **latent stress coupling** $S \mapsto (p(S), z(S))$ reveals that under positive upper-tail dependence ($\lambda_U > 0$, unlike Li 2000's Gaussian copula where $\lambda_U = 0$), a stress jump $s_0 \to s_1$ lowers the silent-trap threshold $z(s_1) \ge \frac{p^* - p(s_1)}{1 - p(s_1)}$ from *both sides simultaneously* while breaking $k$-unit redundancy via Jensen's inequality.
   * **Humility buffer $b$** decomposes formally into: *(i)* **Arrow–Fisher (1974) QOV** for reversible staging (*bacs à sable* under pure SEU, provided $Z$ varies during staging); *(ii)* **Manski minimax-regret** ($b_{\text{MMR}} = \frac{\overline{p}_w - p}{2}$) or **Hansen–Sargent KL-tilting** inside $\Theta$ (noting KL's absolute-continuity *support-blindness* outside $\Theta$); and *(iii)* institutional **verrous** neutralizing **Al-Najjar & Weinstein's (2009)** free-information aversion under static ambiguity rules.
2. **$\mathcal{M}$-Open Statistics & Online Falsification:**
   * **Kleijn & van der Vaart (2012)** (sandwich mismatch $I_{\theta^*}^{-1} \neq I_{\theta^*}^{-1}\Sigma_{\theta^*} I_{\theta^*}^{-1}$), **Grünwald & van Ommen (2017) SafeBayes**, **Kennedy & O'Hagan (2001) / Brynjarsdóttir & O'Hagan (2014)** ($\theta$–$\delta(x)$ unidentifiability), **Wimmer et al. (2023)** (entropy-decomposition incoherence + identifiability leakage), and **Barber et al. (2021)** (impossibility of distribution-free $X$-conditional conformal coverage) formalize Proposition 1 across asymptotics, calibration, and ML UQ.
   * **Lerch et al. (2017)** (*Forecaster's Dilemma*) + **Gneiting & Ranjan (2011)** (`twCRPS`) formalize Ch. 3's rare-event scoring dilemma, while **Ramdas et al. (2023) SAVI e-processes** ($E_t = \prod_{i=1}^t [1 + \lambda_i(X_i/p_0 - 1)]$) turn Ch. 18.3's *historique* into an anytime-valid automated *verrou* (still bounded by the $\Theta$-wall before dormant $Z_0$ activates).
3. **Micro-Founding M1's Parameter $c$ & Operationalizing Ch. 14:**
   * **Eckhardt & Lee (1985)** and **Littlewood & Miller (1989)** derive M1's shared-cause parameter directly from input-difficulty covariance:
     $$c_{\text{eff}} = \frac{\mathrm{Cov}_X\big(\theta(X), \psi(X)\big)}{P(E)(1 - \bar{m})},$$
     explaining why shared LLM priors force $c_{\text{eff}} > 0$ ($c_{\text{eff}} \to 1$ on low-entropy misconceptions), why orthogonal deterministic checks achieve $c_{\text{eff}} \le 0$, and why $z \notin \Theta$ drives $c_{\text{eff}} \to 1$.
   * Ch. 14's anti-*blanchiment* and execution containment map directly to **CaMeL (2025)** (taint/capability tags, residual: data-channel smuggling), **AgentSpec / VeriGuard (2025)** (offline-verified / online-deterministic policy monitors), **CBFs**, and **Lean 4 proof-driven statement distortion** (requiring counterexample fuzzing + human statement validation).

---

## 4. Executable Next-Step Roadmap: [specs_automated_research.md](specs_automated_research.md)

Building directly on these formal bridges and falsifiers, [specs_automated_research.md](specs_automated_research.md) defines **three oracle-grounded automated research tracks** (explicitly excluding non-automatable human uptake $u$ and L1 ontological discovery):

1. **Track 1 — Formal & Symbolic Extensions (`SymPy`/`Z3` + `Lean 4`):** Prove coupled $p$–$z$ M2 bounds (`M2-FH`, `M2-Copula`), M1 non-monotonicity and monoculture tipping frontiers (`M1-NonMonotonic`, `M1-Monoculture`), M3 salience-omission edge theorems, and SAVI Ville bounds behind SHA-256 spec locks, `lean4checker`, and `Hypothesis` fuzzing (`1e-12`).
2. **Track 2 — In-Silico Phase-Transition Simulator:** Vectorized 4,096-point Sobol RDM testbed sweeping $(N, c, m, f, P(E), u, L/\Delta U, \pi_{\text{CFF}})$ with endogenous alert fatigue and shadow-AI bypass, validated against `livre.html` Annex D tables (`D.3`–`D.5`).
3. **Track 3 — "Kill Your Own Checker" Correlated Escape Benchmark:** Six out-of-frame defect classes ($E_1$ unit laundering, $E_2$ regime-locked constants, $E_3$ citation fabrication, $E_4$ Lean hypothesis drops, $E_5$ prompt injection, $E_6$ sycophancy traps) embedded at $\pi_{\text{inj}} \le 0.05$ behind a strict blinding gate ($\text{ROC-AUC} \le 0.55$) to measure $\hat{P}_{\text{esc}}(E_k)$ and difficulty-stratified $\hat{\rho}_c(E_k)$ across 4 stacks (`single_llm`, `cross_family`, `camel_isolated`, `neuro_symbolic`), governed by pre-registered refutation triggers (`F1`, `F2`) and hard budget circuit breakers.
