# Cross-Disciplinary Research Brief: Representations, Controls, Uncertainty, and Automated Systems

## Purpose & Ground Rules for This Research Session

This document outlines a set of interconnected research questions spanning philosophy of science, statistics, decision theory, uncertainty quantification, safety engineering, software engineering, machine learning, information economics, human factors, and AI-assisted research.

For each area below, please survey the existing literature with an open, non-presupposing lens:
1. **What is broadly settled** (standard theorems, widely replicated empirical findings, established definitions).
2. **What is actively debated or unresolved** (competing schools of thought, open formal or empirical questions, strong counterarguments to conventional wisdom).
3. **What concrete solutions, concepts, or empirical tests exist** (and where their known limitations lie).

Do **not** treat any framing or starter reference below as an established conclusion to validate; actively seek out dissenting perspectives, counterexamples, and alternative frameworks.

---

## 1. Philosophy of Science, Epistemology & the Frame Problem

* **Open-background rules & ceteris paribus laws**: Every practical empirical or engineering rule operates against an implicit, unenumerated background of normal conditions ($A \cap (\dots) \to B$). How does philosophy of science characterize the trade-off between specifying more conditions (making rules brittle or unusable) versus leaving conditions tacit (hiding exceptions)?
* **The frame problem & model boundaries**: How do AI and epistemology connect the classical *frame problem* (McCarthy & Hayes 1969; Dennett 1984; Shanahan 2016) to the broader problem of how new relevant variables or causal mechanisms enter a finite representation?
* **Limits of self-auditing & meta-procedures**: Can an automated or formal auditing procedure reliably detect when its own underlying model frame is incomplete, or does it face an inevitable regress? How do accounts like Deborah Mayo’s *severe testing* (Mayo 1996, 2018) or William Wimsatt’s *robustness analysis* (Wimsatt 1981) propose breaking out of circular validation in practice?
* **Verification vs. validation**: How is the distinction between internal mathematical/code *verification* and external real-world *validation* formalized in computational science (e.g., Oberkampf & Roy 2010), and what remains unresolved about validating models of rare or unprecedented events?

---

## 2. Bayesian Statistics & Foundations of Probability

* **Frequentist vs. subjective/judgment interpretations**: Where does the modern debate stand between frequentist, logical/objective Bayesian (e.g., Jaynes 2003), and subjective Bayesian (de Finetti 1974; Savage 1954; Lindley 2006) interpretations—particularly regarding single-shot events where long-run frequencies do not exist?
* **Calibration & proper scoring rules**: How well do strictly proper scoring rules (e.g., log score, Brier score; Gneiting & Raftery 2007) distinguish forecasters or evaluate calibration when outcomes are rare, delayed, or non-stationary?
* **Model misspecification ($\mathcal{M}$-open settings)**: How do modern Bayesian and statistical learning theories handle cases where the true data-generating process lies *outside* the specified hypothesis/model class? How useful are subjective priors in scarce-data regimes versus the risk of encoding blind spots?
* **Inductive generalization**: Beyond classical bias–variance trade-offs and *No Free Lunch* theorems (Wolpert & Macready 1997), what frameworks best explain when data-driven induction succeeds versus fails abruptly under distribution shift?

---

## 3. Uncertainty Quantification (UQ) & Robustness Analysis

* **Aleatory vs. epistemic uncertainty**: Is the split between irreducible ("aleatory") and reducible ("epistemic") uncertainty a fundamental property of systems or strictly a modeling convenience (e.g., Der Kiureghian & Ditlevsen 2009)?
* **Structural / ontological uncertainty ("unknown unknowns")**: By construction, variance decomposition, ensemble spread, and parameter perturbation measure disagreement *within* an admitted model space $\Theta$. How do modern UQ methods—such as *conformal prediction* (Vovk, Gammerman & Shafer 2005; Angelopoulos & Bates 2023), *imprecise probabilities*, *info-gap theory*, or *Robust Decision Making (RDM)* (Lempert, Popper & Bankes 2003; Walker et al. 2003)—attempt to cope with omitted mechanisms, and what are their theoretical limits?
* **Visibility of omitted variables**: Under what empirical conditions do omitted factors manifest as elevated noise/variance in historical data versus remaining completely invisible (e.g., when a factor stayed constant during observation, as in pre-2008 mortgage correlation models)?

---

## 4. Decision Theory (Single-Shot, High-Stakes & Exploration)

* **Normative vs. descriptive rationality**: How do modern decision theorists reconcile Subjective Expected Utility (Savage 1954) with ambiguity aversion (Ellsberg), risk-sensitivity paradoxes (Allais), and bounded rationality?
* **Asymmetric one-shot decisions**: When loss $L$ vastly outweighs gain $\Delta U$, the expected-utility threshold $p^* = \Delta U / (\Delta U + L)$ approaches zero. What decision rules or safeguards (e.g., precautionary criteria, minimax regret, ad hoc safety margins, physical/operational locks, sandboxes) are used when probabilities near $p^*$ cannot be reliably estimated from data?
* **Information gathering vs. action**: How is the trade-off between *exploring* to reduce uncertainty and *deciding/acting* under finite budgets formalized (e.g., value of information, optimal stopping), especially when the exploration strategy itself relies on an uncertain framing of what matters?
* **Safety margins as judgment vs. ritual**: When do informal "humility margins" or safety factors genuinely protect against unmodeled risks versus degenerating into arbitrary heuristics or box-ticking?

---

## 5. Risk Engineering, System Reliability & Safety Science

* **Independence of checks & common-cause failure**: Why do supposedly independent reviewers, redundant sensors, or N-version software implementations fail together in practice (e.g., Knight & Leveson 1986)? How is partial or error-class-relative independence modeled?
* **The independence–comparability trade-off**: Intuition suggests a tension when designing cross-checks: a reviewer very close to the producer shares its blind spots, while a distant reviewer from another discipline or method may fail to translate objections into comparable, actionable terms. Is there formal or empirical work characterizing this trade-off and how organizations find an effective "distance"?
* **Error rate vs. escape probability**: Total system risk depends not only on how often a producer errs, but on the *escape probability* (the fraction of errors that bypass checks and reach action). How do industries measure escape probability empirically (e.g., fault injection, mutation testing in software [DeMillo, Lipton & Sayward 1978], threat image projection in aviation security), and what are the blind spots of synthetic error injection?
* **Alert fatigue & low base rates**: When false alarms rise relative to true defects (low positive predictive value), human operators discount alerts (e.g., Bliss, Gilson & Deaton 1995). How can monitoring systems separate true signal degradation from false-positive saturation?
* **Interface laundering & organizational uptake**: In historical failures (e.g., *Challenger* 1986, *Mars Climate Orbiter* 1999, *Knight Capital* 2012, *Google Flu Trends* 2014), why do caveats, units, error bars, and dissenting signals disappear across handoffs or fail to trigger action even when detected in time?

---

## 6. Software Engineering & Formal Verification

* **Specified vs. learned components**: Classical software relies on explicit contracts (Hoare 1969; Meyer 1992), static verification, and localizable failure addresses. ML shifts the "specification" into training datasets, loss functions, and preference tuning, creating entangled dependencies ("hidden technical debt," Sculley et al. 2015). What architectural patterns best manage the boundary between deterministic and learned modules?
* **Runtime monitors, Simplex & autoformalization**: Wrapping an untrusted or learned controller inside a formally verified safety monitor (e.g., Sha 2001) or translating informal reasoning into proof assistants like Lean (Moura & Ullrich 2021; Wu et al. 2022) recovers *verification* against a spec—but does not solve *validation* of the spec itself. What are the state-of-the-art capabilities and limits of neuro-symbolic and verified-wrapper architectures?
* **Agentic pipelines vs. deterministic orchestration**: When LLM agents plan tool-calling loops over $N$ steps, errors can compound serially and mutate external state. What concrete sandboxing, rollback, contract-checking, and capability-control patterns are proving effective in production?

---

## 7. Machine Learning & LLM Behavior

* **Irregular competence boundaries**: Empirical studies document "jagged frontiers" (e.g., Dell'Acqua et al. 2023) where AI excels on hard tasks yet fails unpredictably on seemingly adjacent or simpler ones. What theoretical or empirical accounts explain and predict where these boundaries lie?
* **Calibration & unavoidable hallucinations**: Theoretical work argues that calibrated generative models must hallucinate on rare/arbitrary facts (e.g., Kalai & Vempala 2024; Kalai et al. 2025). What is the current consensus on why hallucinations persist, and what distinguishes *high-entropy/random errors* (detectable via semantic entropy or repeated sampling, e.g., Farquhar et al. 2024) from *consistent/systematic errors* (widespread misconceptions, salience omissions, context-induced errors)?
* **Preference tuning, Goodhart’s Law & sycophancy**: Optimizing proxies (benchmarks, RLHF, human preference ratings; Christiano et al. 2017; Ouyang et al. 2022) invites Goodhart/Strathern effects (Goodhart 1975; Strathern 1997) and sycophancy (Sharma et al. 2024), where models sound confident and agreeable rather than calibrated. What training, prompting, or decoding techniques measurably counteract this without degrading usefulness?
* **Synthetic feedback loops**: How severe is model collapse / epistemic contamination when AI-generated outputs re-enter training corpora and web knowledge bases without provenance tracking (e.g., Shumailov et al. 2024)?

---

## 8. Information Economics & Collective Epistemology

* **Collapse of costly signaling**: In Spence’s (1973) signaling model, polished prose, clean syntax, or thorough formatting separated careful work from sloppy work because form was costly to fake. When generative AI drives the marginal cost of polished form toward zero while substantive verification remains slow and expensive, does trust collapse into an Akerlof (1970) "pooling equilibrium"? What credible verification or provenance mechanisms (e.g., cryptographic provenance, reproducible artifacts, independent audits) have been proposed or tested?
* **Shared-model monoculture**: If both producers and reviewers/auditors rely on the same small set of foundation models, individual error rates may drop while *correlated* errors pass unchecked. Under what mathematical and empirical conditions does shared AI assistance reduce overall system risk versus increase systemic tail risk?
* **Evaluation bottlenecks**: When production volume scales cheaply via automation while independent human/experimental verification capacity stays fixed, what institutional governance structures (e.g., verification-status tagging, throughput caps, pre-registered expectations, outcome ledgers) work in real organizations?

---

## 9. Human Factors, Oversight & AI-Assisted Research

* **Ironies of automation & loss of cognitive friction**: Bainbridge (1983) observed that automating routine tasks leaves humans with harder supervision and rarer edge-case interventions while eroding their hands-on feel for the system. How does AI assistance affect domain experts’ mental models, order-of-magnitude intuition, and skill retention?
* **Erosion of uncertainty cues & miscalibrated perception**: Humans rely on subtle hesitation cues (*tone, hedging, rough drafts*) to allocate verification effort; fluent AI outputs suppress those cues. Moreover, subjective feelings of speed can invert objective measurements (e.g., the 2025 METR randomized trial of experienced open-source developers, Becker et al. 2025). What factors explain when experts misjudge AI’s net productivity or accuracy impact?
* **Effective human-in-the-loop protocols**: Which lightweight cognitive or organizational practices—such as *pre-mortems* (Klein 2007), writing down expected magnitudes/results before consulting an AI, retrieval-grounded verification (Lewis et al. 2020), or structured adversarial prompting—have empirical evidence of reducing error escape?
* **Methodology of AI-assisted research & writing**: When researchers use LLMs to survey disparate literatures, stress-test arguments, and draft prose, what best practices prevent circular self-confirmation, citation hallucination, and unnoticed conceptual flattening? What empirical studies exist on the reliability and quality of hybrid human–AI scholarship?
