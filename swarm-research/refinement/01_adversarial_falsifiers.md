# Adversarial Falsification Pass: Counter-Evidence, Boundary Conditions, and Weak Counterclaims

## Epistemic Mandate & Classification Key

This document stress-tests the empirical claims and prescriptive remedies of *Agir d’après une représentation du monde* ([livre.html](../../livre.html), reviewed in [cross_review_monograph.md](../../cross_review_monograph.md)) and [synthesis.md](../../synthesis.md). In the monograph’s *Conclusion* (*« Ce qui affaiblirait l’argument »*), the author separates results *under hypotheses* (which lose practical weight if their hypotheses rarely hold) from empirical generalizations and Part V’s untested *working hypotheses*. Following that standard, this pass surveys 2022–2026 literature across four fault lines and classifies every finding as:
- **(a) Genuine Counter-Evidence:** Repeated findings that weaken the monograph’s or synthesis’s practical scope.
- **(b) Scope-Narrowing Boundary Condition:** Evidence pinning down where a claimed law holds versus reverses.
- **(c) Weak / Methodologically Flawed Counterclaim:** Apparent refutations that fail under scrutiny (e.g., conflating *in-frame* optimization with *out-of-frame* omissions, or raw volume with end-to-end quality).

---

## 1. Internal & Iterative Checks vs. Proposition 3 (M3) and Ch. 12.4 Pessimism

### Target Claims
- **Monograph:** **Proposition 3(a)** (Ch. 7, *Model M3*) proves no comparator computed solely from inside a frame $\Theta$ can detect an error caused by an omitted factor $z$ ($\Lambda(A \mid X=x) = 1$). **Ch. 12.4** argues that on *constant* LLM errors, re-asking often fails; the *Conclusion* notes Prop. 3(a) would lose practical weight if real representations *« laisseraient passer bien plus d’information que le livre ne le suppose »*.
- **Synthesis:** Law 1 (*In-frame rigor cannot certify frame completeness*) and Coupling C (*Correlated Escape*).

### (a) Genuine Counter-Evidence: Salience & Reasoning Errors Are Often Catchable Internally
Where the monograph treats single-pass errors as symptomatic of absent frame variables ($z \notin \Theta$), 2023–2025 inference-time scaling research shows many errors stem from **elicitation and salience failures inside $\Theta$** (Ch. 12.3’s *omission de saillance*), not structural omissions:
- **Compute-optimal test-time scaling:** **Snell et al. (2024)** showed that dynamically allocating inference compute (tree search, iterative verification conditioned on prompt difficulty) lets a smaller model outperform a **14× larger** model without external variables or retraining.
- **Process supervision:** **Lightman et al. (2023 / ICLR 2024)** (*"Let's Verify Step by Step"*, PRM800K) demonstrated that **Process Reward Models (PRMs)** scoring intermediate reasoning steps outperform Outcome Reward Models (ORMs) on MATH, solving **78%** of a representative test subset by pruning bad reasoning paths early.
- **Adversarial debate:** Challenging the assumption that intra-paradigm checks fail to expose hidden flaws, **Khan et al. (2024)** (*"Debating with More Persuasive LLMs Leads to More Truthful Answers"*) found on the QuALITY comprehension benchmark that multi-round debate between expert LLMs raised **non-expert model judge accuracy from 48% to 76%** and **human judge accuracy from 60% to 88%**, with persuasiveness optimization *increasing* truthfulness.

Together, these weaken any blanket claim that iterative re-interrogation or same-paradigm critique rarely catches reasoning or salience omissions.

### (b) Scope-Narrowing Boundary Conditions
1. **Verifiable vs. open-ended domains:** **Snell et al. (2024)** and **Lightman et al. (2023/2024)** show test-time scaling and PRMs excel in verifiable domains (math, code, logic) and hit steep diminishing returns on trivial prompts or tasks exceeding the base model's proposal distribution.
2. **External verifiers required for self-correction:** **Kamoi et al. (2024)** limits iterative refinement: *unguided* LLMs fail to reliably recognize their own reasoning errors and frequently **overwrite right answers with wrong ones** unless steered by external signals (compilers, execution checks, or trained PRMs).
3. **Grounded evidence in debate:** In **Khan et al. (2024)**, expert debaters accessed the underlying QuALITY passage; debate converted open-ended truth discovery into *localized textual entailment* for the judge, rather than discovering variables omitted from the text.

### (c) Weak / Methodologically Flawed Counterclaims
Claiming that extended test-time reasoning refutes **Proposition 3(a)** commits a category error. Prop. 3 governs **variables absent from the frame** ($z$ unrepresented in $X$). Test-time search pushes accuracy toward the *ceiling of $\Theta$*; it cannot detect held-constant background variables ($Z_t \approx z_0$), *ceteris paribus* shifts, or *proof-driven statement distortion* in autoformalization ([Field 6](../06_software_formal_verification.md)). **Mirzadeh et al.** (*GSM-Symbolic*) and Apple ML Research (*Illusion of Thinking*) document abrupt accuracy cliffs under irrelevant clause insertions and compositional depth shifts even in reasoning models, confirming that deeper in-frame search does not cure frame or syntactic fragility.

---

## 2. Human–AI Synergy Moderators vs. Negative Synergy & METR Slowdowns

### Target Claims
- **Monograph & Synthesis:** Ch. 15 argues passive oversight erodes the *signe révélateur*; Coupling D cites **Vaccaro et al. (2024)** ($Hedges'\ g = -0.23$ across 106 studies / 370 effect sizes) and **Becker et al. (2025)** (METR RCT: **+19% slower** completion despite **+20%** perceived speedup).

### (a) Genuine Counter-Evidence: Replicated Coding Speedups & Creation Synergy
Treating Vaccaro et al. (2024) and Becker et al. (2025) as proof that human–AI teams uniformly lose speed or quality is falsified by controlled and enterprise trials:
- **Coding RCTs:** **Peng et al. (2023)** measured a **55.8% speedup** for developers using GitHub Copilot on a controlled JavaScript HTTP server task. At enterprise scale across Microsoft and Accenture, **Cui et al. (2024)** ran RCTs/field experiments showing developers with Copilot completed **26.08% more pull requests per week**.
- **Positive subgroups in Vaccaro et al. (2024):** The aggregate $g = -0.23$ is driven by *decision-making tasks* and settings where AI alone outperforms humans. Conversely, **Vaccaro et al. (2024)** observed **statistically positive synergy in content creation/generation** and when **humans outperform AI alone** (allowing calibrated selective acceptance).
- **Clinical coding workflows:** Bounded extraction trials such as *Easy-ICD* (**Chomutare et al., 2024/2025**) and structured human–AI paradigms (**Gao et al., 2024**) test ICD-10/11 coding on long clinical notes, where targeted administrative search avoids open-ended diagnostic interference.

### (b) Scope-Narrowing Boundary Conditions
Comparing **Peng et al. (2023)** (+55.8%) and **Cui et al. (2024)** (+26.08% PRs) against **Becker et al. (2025)** (+19% slowdown) exposes three decisive moderators:
1. **Codebase familiarity & tenure:** Peng et al. tested an isolated greenfield task, and Cui et al.’s gains concentrated among **junior and shorter-tenure developers**. **Becker et al. (2025)** tracked **16 experienced OSS maintainers (averaging 5 years repository familiarity) on mature repositories** rich in implicit invariants—where debugging subtle integration mismatches erased drafting speedups.
2. **Creation vs. diagnostic decision-making:** **Goh et al. (2024, *JAMA Network Open*)** ran an RCT giving physicians GPT-4 on complex diagnostic vignettes and found **no significant improvement** over conventional resources (median ~76% vs. ~74%), even though the **standalone LLM outperformed human-only cohorts**—confirming Vaccaro et al.’s negative-synergy regime in high-stakes clinical judgment.
3. **Frontier localization (Dell’Acqua et al. 2023):** Synergy holds inside the *jagged frontier* and reverses just outside it when operators lack calibrated abstention cues.

### (c) Weak / Methodologically Flawed Counterclaims
1. **Using self-reports to refute Becker et al. (2025):** Subjective productivity surveys fail because Becker et al. documented a **39-point perception inversion** (+20% perceived vs. -19% actual speed), driven by salient generation masking fragmented debugging time.
2. **Equating PR volume with net engineering safety:** **Cui et al. (2024)**’s +26.08% PR metric excludes downstream defect escape, maintenance debt (Sculley et al. 2015), and skill erosion—where **Budzyń et al. (2025)** observed unaided adenoma detection drop from **28.4% to 22.4%** post-AI exposure, and **Bastani et al. (*PNAS*)** found +48% aided practice yielded **-17% unaided exam loss** (noting Budzyń et al.’s observational design still leaves open reversible adaptation vs. lasting deskilling; [Field 9](../09_human_factors_oversight.md)).

---

## 3. When Shared / Homogenized Models Reduce Net Systemic Risk $R$ Despite $\rho > 0$

### Target Claims
- **Monograph:** **Ch. 16** warns shared models elevate correlated escape across producers and reviewers; the *Conclusion* names *"Des communautés à modèle partagé dont l’échappement ne monte pas"* as a core falsifier.
- **Synthesis:** Law 2 and Coupling C ($P(\text{escape}) = p_{\text{AI}} q_{\text{AI}} + \rho \sqrt{p_{\text{AI}}(1 - p_{\text{AI}}) q_{\text{AI}}(1 - q_{\text{AI}})}$).

### (a) Genuine Counter-Evidence: Accuracy Dominance & Conditional Collapse
1. **Baseline accuracy gains can dwarf $\rho$:** By [Field 8](../08_information_economics.md)’s escape equation, when a shared model slashes marginal producer and reviewer errors ($p_{\text{AI}} \ll p$, $q_{\text{AI}} \ll q$)—especially for resource-constrained teams with high baseline error rates—mean escape $P(\text{escape})$ **drops below** unassisted checking ($p \cdot q$) even with substantial $\rho > 0$. In routine regimes, accuracy dominance reduces net systemic risk $R$.
2. **Model collapse requires replacement, not accumulation:** Challenging Ch. 16.3’s reliance on **Shumailov et al. (2024)**, **Gerstgrasser, Schaeffer, Koyejo et al. (2024)** proved across LLMs, VAEs, and diffusion models that catastrophic collapse depends on **data replacement**; **accumulating** synthetic data alongside a fixed real-data anchor keeps test error bounded. In verifiable domains (code, proofs), verifier-filtered synthetic loops *improve* performance ([Field 7](../07_ml_llm_behavior.md)).

### (b) Scope-Narrowing Boundary Conditions
Monoculture risk survives once scoped to **tail risk, collective welfare, and verifier architecture**:
- **Routine error vs. welfare and tails:** **Kleinberg & Raghavan (2021, *PNAS*)** proved that even a *strictly more accurate* shared algorithm can reduce aggregate social welfare (Braess’ paradox) by erasing compensatory diversity. **Bommasani et al. (2022)** showed overlapping base models induce **outcome homogenization**, and **Wataoka et al. (2024/2025)** linked LLM-judge self-preference to perplexity. Thus, shared models can lower *mean* routine risk while inflating *correlated tail risk* ($\rho \to 1$ on shared edge cases).
- **Orthogonal verifiers vs. vendor swapping:** Cross-family neural judges still share web corpora and alignment priors, necessitating anchors like the EMNLP 2025 **DBG score** to isolate self-preference. Genuine decorrelation ($\rho \approx 0$ on logic/execution flaws) comes from pairing neural generators with **programmatic/formal verifiers** (Lean 4, Z3, **CaMeL**, **VeriGuard**).

### (c) Weak / Methodologically Flawed Counterclaims
1. **Using mean accuracy to dismiss tail correlation:** Lower routine escape does not falsify Ch. 16 when asymmetric losses ($p^* = \Delta U / (\Delta U + L) \to 0$) make rare correlated misses catastrophic.
2. **Extending Gerstgrasser et al. (2024) to live RAG:** Pre-2023 human archives anchor *pretraining*, not *live web RAG* on post-2023 facts where unattributed synthetic content can trigger effective replacement ([Field 7](../07_ml_llm_behavior.md)).

---

## 4. Empirical Failures & Backfires of Part V Remedies

### Target Claims
- **Monograph (Ch. 17.3 & Ch. 18):** Recommends CFF-style *ancrage documentaire*, *pré-mortem* protocols, throughput caps, explicit *état de vérification* tags, outcome ledgers, and *bacs à sable / verrous*—all explicitly marked unmeasured *hypothèses de travail*.

### (a) Genuine Counter-Evidence: Bypass, Safety Clutter, and Tag Pathology
1. **CFFs drive dissatisfaction and Shadow AI bypass:** **Buçinca et al. (2021)** proved that while CFFs cut overreliance, they **significantly lower user satisfaction and subjective trust**, moderated by *need for cognition*. Outside enforced labs, **Bastani et al.** note workers under deadline pressure bypass scaffolded tools when unguarded ones exist, and enterprise governance studies document that friction-heavy approval gates or rigid bans push staff toward **Shadow AI** (unauthorized personal accounts/extensions), increasing unmonitored data leakage.
2. **Safety Clutter:** **Rae, Provan, & Dekker (2018)** showed that procedural checklists and redundant sign-offs (*"safety work"*) divorced from operational hazards (*"the safety of work"*) create **safety clutter** and "zombie" compliance that drain cognitive bandwidth ([Field 4](../04_decision_theory.md)).
3. **Safety-II adaptability loss:** Hollnagel’s **Safety-II** literature warns that rigid static locks (*verrous*) erode everyday human adaptability during unmodeled disturbances, provoking covert workarounds ([Field 5](../05_risk_safety_engineering.md)).
4. **Verification-status tags are laundered, gamed, or induce penalties:** As Ch. 18.3.2 concedes, self-declared *état de vérification* labels are cheap to imitate; [Field 8](../08_information_economics.md) notes C2PA manifests are stripped by CDNs (*interface laundering*) and ignored downstream. Worse, enforcing provenance via AI-text detectors causes disproportionate **false positives against non-native English writers** (**Liang et al. 2024**), while **Doshi & Hauser (2024)** documented an **ownership penalty** discounting disclosed AI work—incentivizing concealment over transparent tagging.

### (b) Scope-Narrowing Boundary Conditions
These backfires do **not** vindicate passive HITL oversight (which fails via System 1 rationalization in **Buçinca et al. 2021** and ~90% probability matching in **Bliss, Gilson, & Deaton 1995**). Instead, they restrict Part V to three viable mechanisms:
- **Uncertainty-tiered CFFs:** Trigger friction selectively via calibrated cues (**Kim et al. 2024** first-person hedges; **Steyvers et al. 2025** confidence-aligned rendering; semantic entropy) or high $L/\Delta U$ commits.
- **Non-launderable capability/taint metadata:** Replace prose tags with machine-enforced taint and verification tiers inside **CaMeL (2025)**, **AgentSpec (2025–2026)**, or **VeriGuard (2025)** orchestrators.
- **Clutter auditing:** Pair **Doorn & Hansson (2011)** safety-factor criteria with blinded fault injection and METR-style telemetry to prune dead rituals before Shadow AI bypass sets in.

### (c) Weak / Methodologically Flawed Counterclaims
1. **Equating targeted cognitive gates with safety clutter:** Rejecting all pre-commit checks via **Rae et al. (2018)** overlooks empirical efficacy where mechanisms are targeted: prospective hindsight (**Mitchell, Russo, & Pennington 1989**; **Klein 2007**) raises valid failure-cause discovery by **~30%**, and **CaMeL (2025)** blocks prompt injection architecturally.
2. **Using detector bias to abandon verification signals:** **Liang et al. (2024)** falsifies AI-*origin* detectors, not *verification-tier* signals backed by executable tests, comprehension checks, or outcome-contingent liability (**Bauer et al., 2025/2026**).

---

## 5. Summary Falsification Matrix & Revision Priorities

| Fault Line | Target Claim | Sharpest Counter-Evidence / Falsifier | Verdict `(a)/(b)/(c)` | Required Revision / Scope Qualification |
| :--- | :--- | :--- | :--- | :--- |
| **1. Internal & Iterative Checks** | Prop. 3(a), Ch. 12.4, Law 1 | **Snell et al. (2024)** (14× model equivalence); **Lightman et al. (2023/2024)** (78% MATH via PRMs); **Khan et al. (2024)** (debate 48%→76% / 60%→88%); **Kamoi et al. (2024)** (unguided self-correction fails). | **(a)** on salience errors; **(b)** verifiable/grounded tasks; **(c)** vs. $z \notin \Theta$ | Separate *in-frame salience elicitation* (search/PRMs/debate succeed) from *out-of-frame omission* ($z \notin \Theta$). |
| **2. Human–AI Synergy & Speed** | Ch. 15; **Vaccaro et al. (2024)** ($g=-0.23$); **Becker et al. (2025)** (+19% time) | **Peng et al. (2023)** (+55.8% coding speed); **Cui et al. (2024)** (+26.08% PRs/wk, esp. juniors); **Vaccaro et al. (2024)** creation/human-superior subgroups; **Goh et al. (2024)** clinical RCT (~76% vs. ~74% NS). | **(a)** vs. blanket drag; **(b)** greenfield/junior vs. mature OSS/diagnosis; **(c)** self-reports & raw PRs | Parameterize Ch. 15 by task (creation vs. decision), tenure, and codebase maturity; separate velocity from defect escape. |
| **3. Shared Models & Risk $R$** | Ch. 16; **Shumailov et al. (2024)**; Coupling C | Accuracy dominance ($p_{\text{AI}} \ll p, q_{\text{AI}} \ll q$) cuts mean $R$ despite $\rho > 0$; **Gerstgrasser et al. (2024)** bounds collapse via accumulation; **Kleinberg & Raghavan (2021)** / **Bommasani et al. (2022)** show welfare/tail loss. | **(a)** on mean risk & pretraining; **(b)** mean vs. tail risk & live RAG; **(c)** naive multi-LLM judges | Formalize the accuracy-vs.-$\rho$ crossover in Ch. 16; pair neural proposers with *programmatic/formal* verifiers. |
| **4. Part V Remedies & Friction** | Ch. 17.3–18 (CFFs, *pré-mortem*, *état de vérification*, locks) | **Buçinca et al. (2021)** (UX drop → Shadow AI); **Rae et al. (2018)** (*safety clutter*); **Hollnagel** (Safety-II loss); **Liang et al. (2024)** & **Doshi & Hauser (2024)** (detector bias & ownership penalty). | **(a)** vs. uniform manual rules/tags; **(b)** risk-tiered CFFs & **CaMeL/VeriGuard**; **(c)** rejecting all pre-commit checks | Replace uniform CFFs/prose tags with uncertainty-triggered friction, non-launderable capability tags, and clutter audits. |
