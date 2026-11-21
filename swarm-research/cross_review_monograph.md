# Cross-Review: *Agir d’après une représentation du monde* vs. the 9-Domain Research Synthesis

**Objects Compared:**
* **Monograph:** *Agir d’après une représentation du monde* (W. Fauriat) — [livre.html](livre.html), cold-reader report in [rapport_lecture_pdf.md](rapport_lecture_pdf.md).
* **Independent Comparator Corpus:** [synthesis.md](synthesis.md) and the nine domain surveys oriented by [starter_research.md](starter_research.md):
  1. [01_philosophy_epistemology.md](research/01_philosophy_epistemology.md)
  2. [02_bayesian_probability.md](research/02_bayesian_probability.md)
  3. [03_uq_robustness.md](research/03_uq_robustness.md)
  4. [04_decision_theory.md](research/04_decision_theory.md)
  5. [05_risk_safety_engineering.md](research/05_risk_safety_engineering.md)
  6. [06_software_formal_verification.md](research/06_software_formal_verification.md)
  7. [07_ml_llm_behavior.md](research/07_ml_llm_behavior.md)
  8. [08_information_economics.md](research/08_information_economics.md)
  9. [09_human_factors_oversight.md](research/09_human_factors_oversight.md)

---

## Executive Verdict

Evaluated against the independent 9-domain literature synthesis, *Agir d’après une représentation du monde* is **unusually coherent, intellectually disciplined, and structurally aligned with the cross-disciplinary state of the art**. Its central architecture—models **M1**, **M2**, and **M3**, the five detection conditions, and the two-axis error matrix—captures genuine invariants confirmed independently across epistemology, $\mathcal{M}$-open statistics, structural UQ, reliability engineering, formal verification, ML behavior, information economics, and human factors.

At the same time, reading the monograph alongside our 2021–2026 domain surveys acts as a genuine external comparator (*se tromper autrement*): it fills the **empirical thinness of Parts III–V** explicitly acknowledged in the monograph's *Conclusion*, surfaces **missing modern formalisms** (in $\mathcal{M}$-open Bayes, CCF theory, and agentic security), and highlights **counterarguments and design tensions**—notably around conditional model collapse, equity traps in signaling proxies, and user bypass of uniform friction—that sharpen or qualify the monograph's working hypotheses.

---

## 1. Where the Monograph Holds Up & Contributes Original Value

### 1.1 Structural Alignment with the 9-Domain Corpus
* **The $\Theta$-Boundary Wall:** The monograph's progression from *ceteris paribus* rules ($A \cap (\dots) \to B$, Ch. 1–2) and Savage's decision threshold ($p^* = \Delta U / (\Delta U + L)$, Ch. 4) to variance-inside-$\Theta$ (Proposition 1, Ch. 5), the frame as common cause (Proposition 3 / Model **M3**, Ch. 7: $\Lambda(A \mid X=x) = 1$), and the Ch. 13 two-axis matrix (in/out of frame $\times$ signalled/silent) maps directly onto the **5-Layer Epistemic Boundary Stack** proposed in [synthesis.md](synthesis.md).
* **Resistance to Conceptual Flattening:** One of the chief risks flagged in [Field 9](research/09_human_factors_oversight.md) is *unnoticed conceptual flattening* in interdisciplinary syntheses. The monograph systematically avoids this:
  * It preserves Oberkampf & Roy's (2010) *verification vs. validation* distinction (Ch. 13.3).
  * It separates *scoring-rule calibration* (Ch. 3) from *generative token calibration* (Ch. 12.4).
  * It distinguishes *omission structurelle* from *omission de saillance* (Ch. 12.3, Conclusion) and separates *alert fatigue* from *shared-cause correlation $c$* (Ch. 9 & Ch. 16).

### 1.2 Distinct Contributions Not Found in Any Single Field
1. **The Five-Condition Comparator Decomposition (Proposition 2, Model M1, Ch. 6):** Factoring error interception into *existence, différence, comparabilité, arrivée à temps, prise en compte* ($D \subseteq \bigcap_{j=1}^5 C_j$) and residual risk $R = P(E)(1 - su)$ (Ch. 9) builds an exact bridge between Bayesian positive predictive value (VPP), Bliss et al.'s (1995) behavioral probability matching, and interface *blanchiment* (*Mars Climate Orbiter*).
2. **"Forger les clés avant d'aborder les serrures" (Parts I–II Before III–IV):** Establishing M1–M3 on sailing, corroded brackets, 2008 mortgage copulas, and *Challenger* before introducing ML/LLMs prevents readers from mistaking general systems-reliability and epistemological laws for temporary artifacts of current language models.
3. **Self-Referential Epistemic Audit (Conclusion):** Labeling every major proposition and chapter claim with an explicit epistemic status (*définition*, *résultat sous hypothèses*, *hypothèse de travail*, *constat empirique*), enumerating six open tensions, stating empirical falsification criteria (*Ce qui affaiblirait l'argument*), and documenting two corrections relative to the foundational preprint (Fauriat 2026) sets a high standard for hybrid human–AI scholarship.

---

## 2. Where the 9-Domain Synthesis Extends, Challenges, or Sharpens the Monograph

Comparing [livre.html](livre.html)'s 41-entry Bibliography and its Conclusion's self-identified limitations against the 9-domain corpus reveals four concrete areas of leverage.

### 2.1 Stronger Empirical Anchoring for Parts III–V
The monograph's *Conclusion* notes that Parts III–IV rest on sparse empirical citations for AI effects (principally Dell'Acqua et al. 2023 and Becker et al. 2025) and that Part V's remedies are untested working hypotheses. Recent 2021–2026 empirical studies strongly corroborate the diagnosis while adding crucial boundary conditions:

| Monograph Claim / Section | Corroborating Empirical Evidence from Corpus | Key Nuance / Qualification Added |
| :--- | :--- | :--- |
| **Ch. 15.4 — Bainbridge's irony & skill erosion** | Budzyń et al. (2025): routine AI colonoscopy exposure lowered unaided clinician ADR from `28.4%` to `22.4%`. Bastani et al. (*PNAS*): unguarded GPT-4 raised practice scores `+48%` but cut subsequent unaided exam scores `-17%`. Lee et al. (2025): higher AI confidence lowers critical thinking effort. | Bastani et al. shows *scaffolded* tutor interfaces preserve learning—though workers under deadline pressure bypass guardrails when unguarded tools exist ([Field 9](research/09_human_factors_oversight.md)). |
| **Ch. 15.1–15.3 — Loss of *signe révélateur* & miscalibrated oversight** | Vaccaro et al. (2024) meta-analysis (106 studies): human–AI decision teams underperform best solo agent (`Hedges' g = -0.23`). Steyvers et al. (2025): length bias inflates perceived confidence above accuracy. Kim et al. (2024): first-person hedges reduce overreliance. | Synergy *does* appear in content creation and when humans outperform AI alone (Vaccaro et al. 2024); linguistic hedges risk habituation and alert fatigue over time ([Field 9](research/09_human_factors_oversight.md)). |
| **Ch. 16 — Shared models, monoculture & evaluation bottlenecks** | Kleinberg & Raghavan (2021); Bommasani et al. (outcome homogenization); Wataoka et al. (2024/2025) (perplexity-linked LLM-as-judge self-preference); Liang et al. (2024) (LLM footprints in ICLR/ICML reviews); OSS congestion (*curl* HackerOne shutdown, *tldraw* PR freeze). | Cross-family ensembling is not a free fix due to overlapping pretraining corpora and distillation; structural benchmarks like EMNLP 2025 DBG score are needed to separate quality from self-preference ([Field 8](research/08_information_economics.md)). |
| **Ch. 18 — *Pré-mortem*, *ancrage documentaire* & written expectation** | Buçinca et al. (2021) Cognitive Forcing Functions (CFFs) and Klein (2007) / Mitchell et al. (1989) prospective hindsight cut overreliance; Doshi & Hauser (2024) documents collective semantic homogenization in AI-assisted ideation. | Buçinca et al. (2021) shows CFFs **lower user satisfaction**, incentivizing "shadow AI" bypass; Doshi & Hauser (2024) documents an "ownership penalty" against disclosed AI use, complicating transparency norms ([Field 9](research/09_human_factors_oversight.md)). |

### 2.2 Important Counterarguments & Nuances Missing from the Monograph
1. **Model Collapse Is Conditional on Data Replacement (Ch. 16.3):**
   * The monograph cites Shumailov et al. (2024) on recursive collapse. [Field 7](research/07_ml_llm_behavior.md) emphasizes Gerstgrasser et al. (2024): catastrophic collapse arises under **data replacement**; when synthetic data is **accumulated** alongside a retained human data anchor, test error stays bounded. The sharper operational risk is **Strong Model Collapse** (scaling-law ceilings) and **live RAG/web epistemic contamination** on post-2023 facts where provenance is untracked.
2. **Equity Counterpoint to Costly-Signaling Collapse (Ch. 15.3):**
   * Ch. 15.3 frames the loss of Spence's (1973) form-based signaling primarily as an Akerlof (1970) pooling failure. [Field 8](research/08_information_economics.md) notes the counterargument: polished prose was always a socially biased proxy penalizing non-native speakers, and automated AI-text detectors trigger disproportionate false positives against non-native academic writing (Liang et al. 2024)—creating an acute inclusion vs. screening dilemma.
3. **The Friction–Clutter–Safety-II Tension (Ch. 17–18):**
   * While Ch. 17–18 explicitly warn against compliance theater, [Field 4](research/04_decision_theory.md) (*safety clutter*, Rae, Provan & Dekker: *safety work* vs. *safety of work*; Doorn & Hansson 2011) and [Field 5](research/05_risk_safety_engineering.md) (Hollnagel's *Safety-II*; Vaughan 1996 *normalization of deviance*) sharpen the practical warning: uniform, static friction degrades into box-ticking or drives users to unmonitored tools unless controls are **risk-tiered** (triggered near high uncertainty or irreversible boundaries) and **measured against work-as-done**.
   * Additionally, invoking Diane Vaughan (1996) alongside Tufte (1997) deepens Ch. 6.4's *Challenger* analysis: *prise en compte* failed not only due to chart design, but through organizational *normalization of deviance* under schedule pressure.

### 2.3 Missing Modern Statistical & Decision-Theoretic Machinery (Fields 2–4)
* **$\mathcal{M}$-Open Bayesianism & Calibration Limits ([Field 2](research/02_bayesian_probability.md)):**
  * Ch. 1–3 and Ch. 5 rely on classical subjective Bayes (Savage 1954; de Finetti 1974; Lindley 2006), Gneiting & Raftery (2007), and Mayo (1996, 2018). Integrating **Kleijn & van der Vaart (2012)** (credible intervals lose frequentist coverage under misspecification), **Grünwald & van Ommen (2017)** (hypercompression & *SafeBayes*), **Bayesian stacking (Yao et al. 2018)**, and **Lerch et al. (2017)** (*Forecaster's Dilemma*: conditional scoring on rare extremes destroys propriety and rewards alarmism) would formalize Ch. 3's rare-event intuition.
  * **SAVI / e-values (Ramdas et al. 2023)** resolve much of the Bayesian–frequentist stopping-rule dispute and offer an anytime-valid online falsification tool for Ch. 18's longitudinal monitoring.
* **Beyond Model M2's Independence Assumption ([Fields 3 & 4](research/03_uq_robustness.md)):**
  * As the monograph's *Conclusion* explicitly notes, Model M2 ($p_w = 1 - (1-p)(1-z)$) assumes omitted risk $z$ is independent of modeled risk $p$, and leaves humility buffer $b$ without a formal rule. In complex failures, stressed operating regimes elevate *both* $p$ and $z$ simultaneously.
  * Connecting M2 to **imprecise probabilities (Walley 1991)**, **Manski's partial identification & minimax regret**, **Hansen–Sargent robust control** (and its zero-weight blind spot for out-of-support events), **Al-Najjar & Weinstein (2009)** (free-information aversion under ambiguity rules), and **Arrow–Fisher (1974)** quasi-option value (directly underpinning Ch. 17.3's sandboxes vs. gates) would anchor Part V in formal decision theory.
* **UQ Discrepancy & Impossibility Results ([Field 3](research/03_uq_robustness.md)):**
  * **Kennedy & O'Hagan (2001)** / **Brynjarsdóttir & O'Hagan (2014)** (parameter–discrepancy unidentifiability), **Barber et al. (2019–2021)** (impossibility of distribution-free conditional conformal coverage), **Sniedovich (2007–2014)** (critique of Info-Gap as strictly local robustness), and **Wimmer et al. (2023)** (incoherence and *identifiability leakage* in ML entropy/MI decompositions) directly reinforce Proposition 1.

### 2.4 Missing Micro-Foundations of Error Correlation & Agentic Containment (Fields 5–6)
* **Formal Cause of Check Correlation ([Field 5](research/05_risk_safety_engineering.md)):** Ch. 8 cites Knight & Leveson (1986) empirically, but omits **Eckhardt & Lee (1985)** and **Littlewood & Miller (1987, 1989)**, which prove mathematically that varying problem difficulty across inputs forces positive error correlation even across zero-communication checkers—providing a micro-foundation for parameter $c$ in Model M1.
* **Concrete 2024–2026 Agentic Containment Patterns ([Field 6](research/06_software_formal_verification.md)):** Ch. 10–14 cite Hoare (1969), Meyer (1992), Sha (2001), Sculley et al. (2015), Moura & Ullrich (2021), and Wu et al. (2022), but omit the concrete architectures that operationalize Ch. 14's separation of untrusted data from privileged control: **Dual LLM / CaMeL (2025)** (capability metadata and taint tags), **IsolateGPT**, **AgentSpec**, **VeriGuard**, **Control Barrier Functions (CBFs)**, and the 2024–2026 autoformalization failure mode of **proof-driven statement distortion** (RL-trained provers weakening theorem statements so Lean compiles).

---

## 3. Recommended High-Leverage Next Steps (Using Both Works Together)

1. **Test M1 & M2 with Fault-Injection Benchmarks:** Use the *error-class-relative correlation* protocol proposed in [synthesis.md](synthesis.md) (Tier 1, Lead 1) to empirically measure parameters $c$, $m$, $f$, and $u$ in hybrid LLM–human workflows—directly addressing the monograph's central falsifiability test (*Ce qui affaiblirait l'argument*).
2. **Operationalize Ch. 14 & Ch. 18 via Anti-Laundering Typed Interfaces:** Pair the monograph's *état de vérification* display (Ch. 18.3.2) and *bacs à sable / verrous* (Ch. 17.3) with **CaMeL-style taint tracking** and **uncertainty-triggered adaptive CFFs** ([synthesis.md](synthesis.md) Tier 1, Leads 2–3), keeping friction low on reversible tasks and non-bypassable at irreversible commits.
3. **Extend Model M2 for Coupled Stress ($p$ and $z$ Correlated):** Relax M2's independence assumption in future editions to analyze regimes where extreme operating stress activates both in-frame failure probability $p$ and omitted factor $z$.
4. **Incorporate Post-2023 Nuances in Future Revisions:** Add Gerstgrasser et al. (2024) on synthetic data accumulation vs. live RAG contamination, Liang et al. (2024) on non-native detector bias, Eckhardt & Lee (1985) / Littlewood & Miller (1989) on difficulty-induced correlation, and $\mathcal{M}$-open statistical tools (SafeBayes, SAVI/e-values, Forecaster's Dilemma).
