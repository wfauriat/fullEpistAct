# Field 9: Human Factors, Oversight & AI-Assisted Research

*Cross-disciplinary survey of human–AI cognitive ergonomics, miscalibrated oversight, lightweight human-in-the-loop (HITL) protocols, and the methodology of AI-assisted scholarship.*

---

## 1. Ironies of Automation & Loss of Cognitive Friction

### (a) Broadly Settled
Lisanne Bainbridge’s (1983) *Ironies of Automation* established a structural paradox of socio-technical systems that remains foundational in the LLM era: automating routine tasks does not merely reduce human workload; it **reshapes the human role into passive monitoring and rare edge-case intervention**—tasks humans perform poorly—while eroding the hands-on practice required to maintain accurate mental models.

Recent empirical work confirms that generative AI reproduces this dynamic in clinical, educational, and knowledge-work domains:
* **Expert deskilling in practice:** In a multicenter observational study of experienced endoscopists, Budzyń et al. (2025) found that after months of routine exposure to AI-assisted polyp detection, clinicians’ *unaided* adenoma detection rate (ADR) fell significantly from **28.4% to 22.4%** when the AI was turned off—demonstrating rapid perceptual vigilance decay even among trained specialists.
* **The "AI as a crutch" effect in learning:** In a randomized field experiment with nearly 1,000 high school students, Bastani et al. (*PNAS*) showed that unguarded GPT-4 access boosted immediate practice performance by **+48%**, yet when removed on an unaided exam, those students scored **17% worse** than peers who never had AI access. Offloading intermediate reasoning prevented cognitive consolidation.
* **Shift from generation to passive stewardship:** Surveying knowledge workers, Lee, Sarkar, et al. (2025) documented a shift in cognitive effort away from initial structuring toward downstream verification and integration, alongside an inverse relationship between **confidence in AI** and **self-reported critical thinking effort**.

### (b) Actively Debated / Unresolved
* **Cognitive debt vs. cognitive scaffolding:** *Cognitive debt* theorists warn that unlike deterministic calculators, LLMs offload *semantic and structural reasoning*, stripping away the "desirable difficulty" through which experts develop order-of-magnitude intuition and tacit anomaly detection. *Augmentation* theorists counter that offloading boilerplate execution frees working memory for higher-order architecture and cross-domain synthesis.
* **Heterogeneity by expertise and task regime:** Effects are sharply non-uniform. Unguarded AI harmed novice learning in Bastani et al. (whereas scaffolded tutoring mitigated the deficit), while deeply experienced developers suffered net slowdowns on familiar codebases in Becker et al. (2025). Whether *intermediate* practitioners—capable of catching glaring errors but not outperforming the model—face the highest risk of silent skill atrophy remains unresolved.
* **Causality and reversibility of mental-model decay:** Because Budzyń et al. (2025) was observational rather than randomized, researchers debate how much of the ADR drop reflects lasting perceptual deskilling versus temporary attentional adaptation, and whether periodic unaided practice ("manual flight hours") fully restores baseline intuition.

### (c) Concrete Solutions, Frameworks, Empirical Tests & Known Limitations
* **Scaffolded AI modes:** Bastani et al. showed that constraining AI to provide pedagogical hints ("GPT Tutor") rather than direct answers preserves learning. *Limitation:* Knowledge workers under deadline pressure routinely bypass scaffolded interfaces when unguarded tools exist.
* **Periodic unassisted audits and "cognitive drills":** Analogous to manual flight-hour currency in aviation, organizations can mandate unassisted baseline checks, cold order-of-magnitude estimation, or blind fault-injection drills. *Limitation:* High organizational friction; erodes under short-term throughput KPIs.
* **Empirical test design:** Longitudinal within-subject *withdrawal designs* (measuring unaided accuracy, calibration, and anomaly-detection latency before, during, and after AI exposure) are needed to separate short-term throughput gains from long-term mental-model decay.

---

## 2. Erosion of Uncertainty Cues & Miscalibrated Perception

### (a) Broadly Settled
Human collaborators rely on **pragmatic uncertainty cues**—hesitation, rough drafts, uneven prose, explicit hedging, and visible effort—to allocate scarce verification attention. Fluent LLMs systematically suppress these cues:
* **Calibration and discrimination gaps:** Steyvers et al. (2025) documented a persistent *calibration gap* between an LLM’s internal accuracy and human perceived confidence. Default outputs induce overestimation, compounded by **length bias**: longer explanations inflate human confidence without improving objective accuracy.
* **Failure of human–AI synergy in decision-making:** Across 106 experimental studies (370 effect sizes), Vaccaro et al. (2024) found that **human–AI teams perform significantly worse on average than the best of human or AI alone** ($Hedges'\ g = -0.23$). Losses concentrate in *decision-making tasks* and when AI outperforms humans alone—where humans fail to calibrate when to defer versus override—whereas genuine synergy emerges in *content creation* and when humans outperform AI alone.
* **Subjective–objective productivity inversion:** In a July 2025 METR randomized controlled trial, Becker et al. (2025) tracked 16 experienced open-source developers across 246 real-world tasks on mature repositories (averaging 5 years of familiarity) using Cursor Pro (Claude 3.5/3.7 Sonnet). Developers forecast a **24% speedup** pre-trial (ML/economics experts forecast 38–39%) and still subjectively believed post-trial that AI sped them up by **20%**—yet AI access objectively **increased completion time by 19%** (95% CI: +2% to +39%).

### (b) Actively Debated / Unresolved
* **Mechanisms behind expert perception inversion:** Competing explanations for Becker et al. (2025) include: (1) *salience asymmetry*—rapid code generation is viscerally salient, whereas fragmented time spent prompting, waiting, and debugging subtle integration bugs is under-weighted; (2) *effort–time conflation*—reduced typing drudgery is mistaken for elapsed-time speedup; and (3) *jagged frontier extrapolation* (Dell’Acqua et al. 2023)—experts generalize from visible successes inside the frontier to legacy-codebase invariants outside it.
* **Overreliance vs. algorithm aversion:** While HCI emphasizes *automation bias* (Buçinca et al. 2021; Lee et al. 2025), senior experts sometimes exhibit *algorithm aversion*—dismissing valid AI outputs due to identity threat or a single salient error. Predictors of when experts under-rely versus over-rely remain only partially mapped.
* **Efficacy and limits of linguistic uncertainty cues:** Kim et al. (2024) showed that first-person hedges (*"I’m not sure, but..."*) reduce overreliance on wrong LLM outputs and improve net accuracy. Critics warn that because verbalized confidence is poorly calibrated under distribution shift or RLHF sycophancy (Sharma et al. 2024), frequent caveats risk habituation and *alert fatigue* (Bliss, Gilson & Deaton 1995).

### (c) Concrete Solutions, Frameworks, Empirical Tests & Known Limitations
* **Confidence-aligned rendering:** Steyvers et al. (2025) found that aligning explanation tone and length to internal model confidence narrows the calibration gap. *Limitation:* Breaks down when internal probabilities are themselves miscalibrated on systematic errors (Kalai & Vempala 2024).
* **First-person uncertainty expression:** Kim et al. (2024) supports surfacing calibrated first-person hedges over authoritative prose. *Limitation:* Long-term field durability against user habituation is largely untested.
* **Telemetry-grounded productivity trials:** Becker et al. (2025) proves that self-reported productivity surveys are invalid instruments; organizations must measure end-to-end latency, rework, and defect escape via randomized or stepped-wedge trials.

---

## 3. Effective Human-in-the-Loop (HITL) Protocols

### (a) Broadly Settled
Passive oversight—asking humans to "review" finished AI outputs, even with standard Explainable AI (XAI) rationales—is broadly settled to be **ineffective against error escape**. Buçinca et al. (2021) showed that under dual-process dynamics, humans default to System 1 heuristics and treat fluent explanations as a "badge of competence," sometimes *increasing* overreliance on wrong recommendations.

By contrast, **structured friction** that enforces independent commitment or counterfactual search has replicated empirical support:
* **Cognitive Forcing Functions (CFFs):** Buçinca et al. (2021) demonstrated that forcing users to record an initial judgment before seeing AI output, delaying AI recommendations, or requiring on-demand requests significantly reduces overreliance on wrong suggestions.
* **Pre-mortems & prospective hindsight:** Klein (2007), building on prospective hindsight experiments (Mitchell, Russo & Pennington 1989; ~30% increase in identifying valid failure reasons), showed that assuming a plan *has already failed* and working backward disrupts optimism bias, confirmation bias, and groupthink.
* **Retrieval-grounded verification (RAG):** Grounding claims in inspectable source passages (Lewis et al. 2020) converts open-ended fact checking into lower-cost, auditable source-to-claim entailment checking.

### (b) Actively Debated / Unresolved
* **The accuracy–usability (friction) paradox:** Buçinca et al. (2021) found that CFFs significantly lowered user satisfaction and subjective trust. Without mandatory enforcement, workers routinely bypass high-friction workflows ("shadow AI"), leaving open whether lab-validated CFFs survive in production.
* **Moderation by individual traits and workload:** CFF effectiveness depends strongly on *need for cognition* (Buçinca et al. 2021) and task-specific self-confidence (Lee et al. 2025). Under acute time pressure, forcing functions can degrade both speed and accuracy via perfunctory compliance.
* **Single-model adversarial prompting:** Asking an LLM to critique its own draft ("assume this is wrong") catches surface omissions, yet critics note that single-model self-critique shares the same training biases and sycophancy (Sharma et al. 2024)—risking a *theater of adversarial review* that inflates human false confidence.
* **Anchor-before-AI vs. prior rigidity:** Writing down expected magnitudes or hypotheses before consulting AI prevents algorithmic anchoring, but strong human priors can also trigger *confirmation bias*, causing experts to dismiss valid AI findings outside their mental model.

### (c) Concrete Solutions, Frameworks, Empirical Tests & Known Limitations
| Protocol | Cognitive Mechanism | Empirical Status | Primary Limitation |
| :--- | :--- | :--- | :--- |
| **Anchor-before-AI** (record expected magnitudes/hypotheses first) | Blocks algorithmic anchoring; triggers surprise on divergence | Strong lab evidence via CFFs (Buçinca et al. 2021) | Bypassed under time pressure; lower UX satisfaction |
| **Inference-time Micro-Pre-Mortem** ("Assume this output failed; why?") | Prospective hindsight; counterfactual pessimism (Klein 2007; Mitchell et al. 1989) | Strong in planning; emerging in AI oversight | Degenerates into box-ticking if applied uniformly |
| **Retrieval-Grounded Verification** (Lewis et al. 2020) | Converts open fact-checking into local entailment check | Widely validated against fabrication | Vulnerable to cherry-picked sources or plausible misattribution |
| **Risk-Tiered / Adaptive CFFs** | Triggers System 2 friction only on high-stakes or uncertain items | Proposed mitigation for friction fatigue | Requires calibrated upstream uncertainty signals |
| **Cross-Model / Cross-Method Red-Teaming** | Breaks shared framing blind spots | Theoretically grounded; mixed benchmarks | Still exposed to shared pretraining corpora |

---

## 4. Methodology of AI-Assisted Research & Writing

### (a) Broadly Settled
Empirical studies of LLM-assisted literature review, ideation, and drafting identify three structural epistemic hazards:
1. **Individual gain vs. collective homogenization:** Doshi & Hauser (2024, *Science Advances*) showed that LLM ideas improved individual story quality and novelty (especially for less creative writers) while **significantly reducing collective diversity**—independent authors converged on similar semantic clusters. Subsequent 2024–2025 reviews and embedding-distance analyses confirm this homogenization across broader research ideation.
2. **Citation hallucination and mainstream-corpus bias:** Unconstrained LLMs fabricate plausible bibliographic metadata (authors, DOIs, findings). Even when citing real works, they disproportionately surface high-citation canonical papers over niche or heterodox scholarship, reinforcing an automated echo chamber.
3. **Circular self-confirmation via sycophancy:** Preference-tuned models exhibit sycophancy (Sharma et al. 2024), mirroring a researcher’s framing and presuppositions. Unstructured "stress-testing" often returns eloquent validation, creating an illusion of independent corroboration.

### (b) Actively Debated / Unresolved
* **Conceptual flattening vs. cross-disciplinary discovery:** Critics warn that fluent LLM synthesis induces *unnoticed conceptual flattening*—smoothing over deep ontological incompatibilities across fields (e.g., collapsing frequentist confidence, Bayesian credence, and deep ambiguity into generic "uncertainty"). Proponents counter that LLMs dramatically lower cross-disciplinary entry barriers, helping specialists discover relevant theorems across adjacent fields.
* **Intrinsic homogenization vs. prompting artifact:** Follow-up 2025 studies suggest homogenization is not immutable: multi-persona prompting, separating divergent generation from selection, and idiosyncratic human seeds can restore semantic diversity. Skeptics argue that under publication pressure, scholars default to uniform, low-effort prompts—making field-level convergence the practical equilibrium.
* **Disclosure norms and the "ownership penalty":** Doshi & Hauser (2024) and related studies document an *ownership penalty* where evaluators discount work once AI assistance is disclosed or suspected, incentivizing covert use and eroding methodological transparency.

### (c) Concrete Solutions, Frameworks, Empirical Tests & Known Limitations
* **Decouple discovery, verification, and prose:** Use LLMs as *hypothesis and query generators*, never as bibliographic authorities; verify every citation against primary texts or retrieval-grounded databases (Lewis et al. 2020) with explicit provenance logs. *Limitation:* Reintroduces the verification bottleneck researchers sought to avoid.
* **Blinded and valence-flipped prompting:** Prompt without revealing preferred conclusions, explicitly solicit competing schools and counterexamples, and test whether the model reverses its verdict under opposite prompt valence. *Limitation:* Detects prompt-sensitive sycophancy, not shared pretraining blind spots.
* **Dissent ledgers & unaided core drafting:** Maintain explicit ledgers of unresolved debates and incompatible definitions across fields, and draft core theoretical claims unaided before AI-assisted editing. *Limitation:* Difficult to audit externally.

---

## 5. Cross-Domain Interactions & Interfaces

Human factors couple directly with every other domain in this research program:
1. **Epistemology & the Frame Problem (Field 1):** Suppressing friction and flattening concepts conceals *ceteris paribus* background conditions. Deskilled experts (Bainbridge 1983; Budzyń et al. 2025) lose the tacit sensitivity needed to detect broken model frames—collapsing external *validation* (Oberkampf & Roy 2010) into circular *verification*. Mayo’s (1996, 2018) *severe testing* and Wimsatt’s (1981) *robustness analysis* offer philosophical blueprints for adversarial HITL protocols.
2. **Bayesian Probability & Calibration (Field 2):** Human oversight acts as Bayesian updating on an AI signal, yet fluency and length bias systematically miscalibrate trust weights (Steyvers et al. 2025; Lee et al. 2025). Without strictly proper scoring rules (Gneiting & Raftery 2007) or longitudinal feedback, experts cannot learn an AI’s true error distribution in $\mathcal{M}$-open settings.
3. **Uncertainty Quantification (Field 3):** Even mathematically valid UQ sets (e.g., conformal prediction; Vovk et al. 2005; Angelopoulos & Bates 2023) fail if human uptake breaks down; calibrated linguistic cues (Kim et al. 2024; Steyvers et al. 2025) are the necessary interface between formal UQ and operator reliance.
4. **Decision Theory (Field 4):** In asymmetric one-shot decisions ($L \gg \Delta U$), the optimal intervention threshold $p^*$ approaches zero, yet CFFs impose salient immediate friction—explaining why rational safety margins decay into ritualized box-ticking unless structurally enforced.
5. **Risk Engineering & Safety Science (Field 5):** HITL oversight inherits *alert fatigue* (Bliss et al. 1995), *interface laundering* (caveats stripped across handoffs), and *common-cause failure* (Knight & Leveson 1986) when reviewers anchor on AI framing. Synthetic fault injection (analogous to mutation testing; DeMillo et al. 1978) provides a direct empirical measure of human *error-escape probability*.
6. **Software Engineering & Formal Verification (Field 6):** Becker et al. (2025) exposes the human-factors cost of *hidden technical debt* (Sculley et al. 2015): when learned tools emit code without explicit contracts, engineers spend more time reconstructing invariants than coding manually. Runtime safety monitors (Sha 2001) and proof assistants shift oversight from prose inspection to contract validation.
7. **ML & LLM Behavior (Field 7):** Jagged frontiers (Dell’Acqua et al. 2023), unavoidable hallucinations on rare facts (Kalai & Vempala 2024; Kalai et al. 2025), and sycophancy (Sharma et al. 2024) drive human miscalibration. Semantic entropy (Farquhar et al. 2024) can trigger adaptive CFFs for high-entropy errors, whereas consistent/systematic errors require external grounding.
8. **Information Economics & Collective Epistemology (Field 8):** The collapse of costly signaling (Spence 1973; Akerlof 1970) mirrors fluency-induced overreliance: once polished prose is free, form ceases to signal rigor. Combined with collective homogenization (Doshi & Hauser 2024), shared-model monoculture, and synthetic feedback loops (Shumailov et al. 2024), individually rational AI adoption risks a collective epistemic tragedy.

---

## 6. High-Leverage Leads & Open Questions

1. **Uncertainty-triggered adaptive CFFs:** Can pairing internal uncertainty detectors (e.g., semantic entropy; Farquhar et al. 2024) with *selective* cognitive forcing (Buçinca et al. 2021) resolve the accuracy–usability paradox by injecting friction only near the jagged frontier?
2. **Blinded fault-injection benchmarks for oversight:** Injecting subtle, realistic defects into a small fraction of AI outputs during live workflows would allow organizations to measure true human **error-escape probability** and track longitudinal deskilling.
3. **Decomposing the METR perception inversion:** Testing real-time duration telemetry or explicit pre-task time budgets could determine whether the 39-point gap in Becker et al. (2025) stems primarily from effort–time conflation or fragmented attention.
4. **Minimum effective dose of "manual flight hours":** Following Budzyń et al. (2025) and Bastani et al., what cadence of unaided practice or scaffolded interaction preserves experts’ order-of-magnitude intuition without forfeiting routine AI gains?
5. **Measuring conceptual flattening in hybrid scholarship:** Developing expert-graded rubrics that test whether AI-assisted syntheses preserve genuine cross-disciplinary incompatibilities—distinct from surface lexical similarity (Doshi & Hauser 2024)—remains an open methodological priority.

---

## References

* Akerlof, G. A. (1970). The market for "lemons": Quality uncertainty and the market mechanism. *QJE*.
* Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. *Foundations and Trends in ML*.
* Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775–779.
* Bastani, H., Bastani, O., et al. Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*.
* Becker, J., Rush, N., Barnes, B., & Rein, D. (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. METR.
* Bliss, J. P., Gilson, R. D., & Deaton, J. E. (1995). Human probability matching behaviour in response to alarms of varying reliability. *Ergonomics*.
* Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *ACM CSCW*.
* Budzyń, K., et al. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: A multicentre, observational study. *The Lancet Gastroenterology & Hepatology*.
* Dell’Acqua, F., et al. (2023). Navigating the jagged technological frontier. *HBS Working Paper*.
* DeMillo, R. A., Lipton, R. J., & Sayward, F. G. (1978). Hints on test data selection. *Computer*.
* Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances*.
* Farquhar, S., et al. (2024). Detecting hallucinations in large language models using semantic entropy. *Nature*.
* Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *JASA*.
* Kalai, A. T., & Vempala, S. S. (2024). Calibrated language models must hallucinate. *STOC*.
* Kalai, A. T., et al. (2025). Why language models hallucinate.
* Kim, S. S. Y., et al. (2024). "I’m not sure, but...": Examining the impact of LLMs’ uncertainty expression on user reliance and trust. *ACM CHI*.
* Klein, G. (2007). Performing a project premortem. *Harvard Business Review*.
* Knight, J. C., & Leveson, N. G. (1986). An experimental evaluation of the assumption of independence in multiversion programming. *IEEE TSE*.
* Lee, H.-P., Sarkar, A., et al. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. *ACM CHI*.
* Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS*.
* Mayo, D. G. (1996, 2018). *Error and the Growth of Experimental Knowledge*; *Statistical Inference as Severe Testing*.
* Mitchell, D. J., Russo, J. E., & Pennington, N. (1989). Back to the future: Temporal perspective in the explanation of events. *JBDM*.
* Oberkampf, W. L., & Roy, C. J. (2010). *Verification and Validation in Scientific Computing*.
* Sculley, D., et al. (2015). Hidden technical debt in machine learning systems. *NeurIPS*.
* Sha, L. (2001). Using simplicity to control complexity. *IEEE Software*.
* Sharma, M., et al. (2024). Towards understanding sycophancy in language models. *ICLR*.
* Shumailov, I., et al. (2024). AI models collapse when trained on recursively generated data. *Nature*.
* Spence, M. (1973). Job market signaling. *QJE*.
* Steyvers, M., et al. (2025). The calibration gap between model and human confidence in large language models. *Nature Machine Intelligence*.
* Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour*.
* Vovk, V., Gammerman, A., & Shafer, G. (2005). *Algorithmic Learning in a Random World*.
* Wimsatt, W. C. (1981). Robustness, reliability, and overdetermination. In *Scientific Inquiry and the Social Sciences*.
