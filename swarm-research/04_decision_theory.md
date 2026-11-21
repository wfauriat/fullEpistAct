# Field 4: Decision Theory (Single-Shot, High-Stakes & Exploration)

Decision theory formalizes how agents should—and actually do—choose actions under uncertainty. In repeatable settings with stable distributions and bounded payoffs, Subjective Expected Utility (SEU) provides a unified calculus. That calculus strains sharply in **single-shot, high-stakes, and open-world settings**: where catastrophic losses dwarf modest gains, probabilities near the decision threshold cannot be estimated from data, exploration budgets are finite, and the decision-maker's framing of what matters may itself be incomplete.

This survey examines four core questions—normative vs. descriptive rationality, asymmetric one-shot decisions, exploration vs. action, and safety margins as judgment vs. ritual—explicitly separating settled results, active disputes, and operational frameworks with their limits.

---

## 1. Normative vs. Descriptive Rationality

### (a) What Is Broadly Settled
* **SEU Representation:** Savage (1954) proved that preferences satisfying completeness, transitivity, and the *Sure-Thing Principle* (independence of outcomes in states where two acts agree) act *as if* maximizing expected utility with respect to a unique subjective probability measure.
* **Systematic Descriptive Violations:** Human choice reliably departs from SEU via:
  * **Risk-sensitivity paradoxes (Allais):** Violating independence when certainty contrasts with high-probability gambles (nonlinear probability weighting, captured descriptively by Prospect Theory).
  * **Ambiguity aversion (Ellsberg):** Preferring known odds (*risk*) over unknown odds (*Knightian uncertainty* / *ambiguity*), directly violating Savage's Sure-Thing Principle.
* **Bounded Computation:** Finite time, memory, and attention make exact Bayesian updating and full backward induction intractable in large state spaces; heuristics and satisficing are structural necessities, not mere bias.

### (b) What Is Actively Debated or Unresolved
* **Are Ellsberg/Allais Preferences Irrational, or Are Savage's Axioms Too Narrow?**
  * *Orthodox SEU & Dynamic Inconsistency Critique:* Many theorists treat SEU as the sole normative standard. Al-Najjar and Weinstein (2009) showed that non-SEU ambiguity models (such as multiple-prior rules) suffer **dynamic inconsistency** under sequential updating: a "sophisticated" ambiguity-averse agent anticipating preference reversals will rationally **refuse free, valuable information** (information aversion)—an implication they deem normatively indefensible.
  * *Non-SEU Normative Defenses:* Gilboa and Schmeidler, Klibanoff, Marinacci, and Mukerji, Lara Buchak (2013), Brian Hill, and Marciano Siniscalchi counter that Savage's axioms force artificial point priors under sparse evidence. Buchak's (2013) **Risk-Weighted Expected Utility** argues that rational agents may weight worst-case tails directly rather than linearly averaging utility, reframing dynamic tension as a legitimate trade-off between flexibility and commitment.
* **The Ergodicity Economics Dispute:** Ole Peters (2019) argued from statistical physics that multiplicative wealth dynamics are non-ergodic (time averages $\neq$ ensemble averages), claiming risk aversion stems objectively from maximizing time-average growth rates (Kelly criterion) and avoiding absorbing ruin rather than subjective concave utility. Doctor, Wakker, and Wang (2020) countered in *Nature Physics* that Peters conflates expected *monetary* value with expected *utility*, ignores how SEU models dynamic wealth trajectories, and overextends infinite-horizon time averages to genuinely **one-shot** choices.
* **Normative Status of Boundedness:** **Resource-rational analysis** (Lieder & Griffiths 2020) reframes biases (e.g., extreme loss aversion) as *bounded-optimal* algorithms maximizing expected utility minus computational cost. Critics warn that without independent constraints on the cost model, resource rationality risks unfalsifiable post-hoc rationalization.

### (c) Concrete Solutions, Frameworks, and Limitations
| Framework | Core Mechanism | Practical Role | Known Limitations |
| :--- | :--- | :--- | :--- |
| **Maxmin EU (MEU)** (Gilboa & Schmeidler) | Maximizes $\min_{p \in \mathcal{P}} \mathbb{E}_p[u(a)]$ over a set of priors $\mathcal{P}$. | Formalizes ambiguity aversion and worst-case hedging. | Dominated by extreme boundary priors; dynamic inconsistency & free-information aversion (Al-Najjar & Weinstein 2009). |
| **Smooth Ambiguity** (Klibanoff, Marinacci, & Mukerji) | Separates second-order belief over models from ambiguity attitude ($\phi$). | Analytically tractable; interpolates between SEU and MEU. | Requires specifying a second-order prior; dynamic updating rules remain contested. |
| **Risk-Weighted EU** (Buchak 2013) | Weights outcomes via a risk function $r(P)$ sensitive to worst-case tails. | Normatively rationalizes Allais-style caution without distorting beliefs. | Sensitive to how dynamic decision trees and commitments are modeled. |
| **Resource Rationality** (Lieder & Griffiths 2020) | Optimizes $\mathbb{E}[U(\pi)] - \text{Cost}(\pi)$ under finite compute/cognition. | Explains heuristic success under time/data scarcity. | Circularity risk if computational cost functions are tuned post hoc. |

---

## 2. Asymmetric One-Shot Decisions

### (a) What Is Broadly Settled
* **Threshold Collapse:** For a binary one-shot choice with safe gain $\Delta U > 0$ and catastrophic loss $L \gg \Delta U$ at failure probability $p$, SEU recommends acting iff $p < p^* = \frac{\Delta U}{\Delta U + L} \approx \frac{\Delta U}{L}$. Under extreme asymmetry, $p^*$ collapses toward zero ($10^{-4}$ to $10^{-7}$).
* **Statistical Identifiability Barrier:** Probabilities near $p^* \ll 1$ cannot be reliably estimated from finite samples in novel or non-stationary systems. Zero failures in $N = 100$ trials only bounds failure rates near $1/N \sim 10^{-2}$, leaving orders of magnitude of unresolvable gap above $p^*$; plugging point estimates into EU launders prior assumptions as empirical precision.
* **Quasi-Option Value of Reversibility:** Arrow and Fisher (1974) proved that when an action is *irreversible* and future learning is expected, delaying commitment has strictly positive **quasi-option value** even under risk neutrality.

### (b) What Is Actively Debated or Unresolved
* **Precautionary Principle vs. Paralysis:**
  * *Paralysis Critique:* Cass Sunstein (2005, *Laws of Fear*) argued that strong Precautionary Principles are incoherent and paralyzing because **risks exist on both sides**: banning a new technology to avoid a novel tail risk can lock in severe status-quo harms.
  * *Structured Precaution:* Stephen Gardiner (2006) defended a *Core Precautionary Principle* restricted to catastrophic, unquantifiable threats with modest precautionary costs. Daniel Steel (2015) systematized precaution as a proportional meta-rule linking knowledge conditions, harm severity, and counter-risk checks to prevent paralysis.
* **Calibrating Worst-Case Rules:** Pure *maximin* is vulnerable to implausible contrived catastrophes unless the admissible model set is bounded. **Minimax Regret**—paired by Charles Manski with **partial identification**—avoids "assumption-dodging" (inventing point probabilities) by bounding policy outcomes strictly from data plus minimal assumptions. Critics note minimax regret violates *Independence of Irrelevant Alternatives* and still hinges on which model class is admitted.
* **Support Limits of Robust Control:** **Robust Control** (Hansen & Sargent) optimizes against worst-case distributions within a relative-entropy (KL-divergence) neighborhood of an approximating model. Yet the robustness radius remains exogenous, and KL neighborhoods assign zero weight to out-of-support mechanisms that the baseline model treats as impossible ($p = 0$).

### (c) Concrete Solutions, Frameworks, and Limitations
When $p^*$ is unestimable, high-stakes domains shift from *estimating $p$* to *reshaping $L$ and reversibility*:
1. **Robust Control (Hansen & Sargent):** Zero-sum game against entropy-bounded model misspecification. *Limitation:* Blind to out-of-support structural surprises.
2. **Partial Identification & Minimax Regret (Manski):** Evaluates actions over data-consistent identification bounds. *Limitation:* Bounds can be indecisively wide; sensitive to the candidate action set.
3. **Robust Decision Making (RDM) (Lempert, Popper, & Bankes 2003; Walker et al. 2003):** Stress-tests strategies across large scenario ensembles to find policies satisfactory over broad parameter regions. *Limitation:* Cannot expose failure modes absent from the scenario generator.
4. **Operational & Architectural Locks:** Sandboxes, staged/canary rollouts, physical interlocks, rollbacks, and verified runtime safety monitors (e.g., Simplex, Sha 2001) shrink $L$ or restore reversibility. *Limitation:* Safeguards add complexity, can share common-cause failures, and face bypass under schedule pressure.

---

## 3. Information Gathering vs. Action

### (a) What Is Broadly Settled
* **Value of Information (VoI):** Under SEU, the Expected Value of Sample Information (EVSI) measures expected utility gain from observing a signal minus acquisition cost; free information is always non-negative in value.
* **Formal Exploration–Exploitation:** Under a known model class and finite budget, optimal information gathering is formalized by **optimal stopping**, **multi-armed bandits** (Gittins indices, UCB, Thompson Sampling), and **POMDPs** (maintaining belief states over hidden variables where actions simultaneously alter state and yield observations).

### (b) What Is Actively Debated or Unresolved
* **Exploration Under Unawareness (Uncertain Framing):** Classical VoI, bandits, and POMDPs presuppose a fixed, pre-enumerated state space $S$ and observation space $O$. In open-world problems, the highest-value information is often discovering an **unimagined variable or failure mode** (*unawareness*).
  * Edi Karni and Marie-Louise Vierø (2013, 2017) formalized **Reverse Bayesianism** (expanding state spaces under growing awareness while preserving prior likelihood ratios among known events); Simon Grant and John Quiggin (2013) modeled inductive reasoning about unawareness; Burkhard Schipper (2013) analyzed language- and cognition-limited awareness-dependent SEU.
  * *The Valuation Paradox:* While "awareness of unawareness" (Karni & Vierø 2017) permits assigning probability to a catch-all residual state, computing *which* exploratory action maximizes the chance of productive frame expansion—versus burning budget on noise—remains formally unresolved.
* **Risky Exploration & Metareasoning Regress:** In high-stakes settings (clinical trials, autonomous systems), probing can itself trigger catastrophic loss $L$, coupling exploration to asymmetric one-shot risk. Meanwhile, exact POMDP planning is PSPACE-complete, and optimizing *how much compute* to spend planning faces an infinite metareasoning regress unless truncated by heuristics.

### (c) Concrete Solutions, Frameworks, and Limitations
* **Safe Exploration / Constrained POMDPs:** Restricts probing to verified safe sets or chance-constrained policies. *Limitation:* Relies on smoothness assumptions and known safe baselines; discontinuous failure cliffs break guarantees.
* **Unawareness-Aware POMDPs:** Embeds residual catch-all states that trigger model expansion upon anomalous observations. *Limitation:* Largely theoretical; fails when omitted variables remain silent or get absorbed into existing noise terms.
* **Non-Bayesian Frame-Breaking Probes:** Practitioners earmark budget for red-teaming, pre-mortems (Klein 2007), fault injection, and severe testing (Mayo 1996, 2018) aimed at falsifying the current frame rather than sharpening in-frame parameters. *Limitation:* Lacks a principled stopping rule when probes find nothing.

---

## 4. Safety Margins as Judgment vs. Ritual

### (a) What Is Broadly Settled
* **Evolution of Safety Factors:** Deterministic engineering safety factors (e.g., $3\times$ load multipliers) evolved inductively from failures to buffer both known aleatory variance and unmodeled epistemic/structural hazards.
* **Probabilistic Design Trade-Off:** Reliability-based design replaces uniform multipliers with explicit load/resistance distributions to target failure probabilities, exposing where crude factors over-design low-variance parts while leaving high-variance parts fragile.
* **Goodhart Drift:** Once a safety factor or risk metric becomes a compliance target, incentives shift from reducing real hazard to producing compliant documentation (Goodhart 1975; Strathern 1997).

### (b) What Is Actively Debated or Unresolved
* **Should Probabilistic Design Replace Safety Factors?** Neelke Doorn and Sven Ove Hansson (2011) argued that while probabilistic design clarifies *quantifiable* variability, it **cannot fully replace safety factors**: Probabilistic Risk Assessment struggles with model misspecification, human error, and unprecedented failure modes, risking false precision. Reliability engineers counter that unexamined deterministic factors hide what is guarded against and misallocate finite safety budgets.
* **Judgment vs. "Safety Clutter":** Andrew Rae, David Provan, and Sidney Dekker identified **safety clutter**—procedures, risk matrices, and formal margins performed in the name of safety that do not improve operational safety—distinguishing **safety work** (bureaucratic compliance and liability defense) from **the safety of work** (real physical margins and operational adaptability). The core tension: codifying informal "humility margins" into rigid rules breeds ritual, whereas leaving them informal invites erosion under production pressure.

### (c) Concrete Solutions, Frameworks, and Limitations
* **Diagnostic Criteria (Judgment vs. Ritual):** Drawing on Doorn & Hansson (2011) and Rae, Provan, & Dekker, a safety margin represents genuine judgment rather than clutter when it exhibits:
  1. *Operational Coupling:* Directly increases physical slack, containment, or recovery time in *work as done*.
  2. *Uncertainty Attribution:* Separates quantified aleatory buffers from explicit epistemic humility margins.
  3. *Falsifiability & Pruning:* Tested against near-misses and adversarial probes, and removable when shown ineffective.
* **Hybrid Partial-Factor Codes:** Modern codes combine probabilistic calibration for known loads with residual safety factors and independent barriers for unmodeled hazards. *Limitation:* Still ossifies into box-ticking when applied as black-box constants divorced from failure mechanics.

---

## 5. Cross-Domain Interactions & Interfaces

Decision theory bridges epistemic uncertainty (Fields 1–3) and operational control/governance (Fields 5–9):

* **Field 1 (Epistemology & Frame Problem):** The frame problem (McCarthy & Hayes 1969; Dennett 1984; Shanahan 2016) underpins decision-theoretic *unawareness* (Karni & Vierø 2013; Schipper 2013). Severe testing (Mayo 1996, 2018) and robustness analysis (Wimsatt 1981) supply frame-breaking exploration heuristics outside closed-frame SEU.
* **Field 2 (Bayesian Statistics):** In $\mathcal{M}$-open settings, strictly proper scoring rules (Gneiting & Raftery 2007) cannot reliably separate models near $p^* \ll 1$, motivating Manski's partial identification and Hansen–Sargent robust control.
* **Field 3 (UQ & Robustness Analysis):** Conformal prediction (Vovk, Gammerman, & Shafer 2005; Angelopoulos & Bates 2023), imprecise probabilities, and RDM (Lempert, Popper, & Bankes 2003) feed non-SEU decision rules; all share vulnerability to silent omitted variables that never varied historically.
* **Field 5 (Risk Engineering & Safety Science):** Unestimable $p^*$ hands off to structural defense-in-depth and escape-probability measurement. Conversely, alert fatigue (Bliss, Gilson, & Deaton 1995) and common-cause failure (Knight & Leveson 1986) show how nominal precautionary checks can *raise* net risk.
* **Field 6 (Software Engineering & Formal Verification):** Verified runtime monitors (Simplex, Sha 2001), sandboxes, and rollbacks operationalize **reversibility** and bounded $L$, converting asymmetric one-shot gambles into recoverable sequential decisions.
* **Field 7 (ML & LLM Behavior):** Jagged frontiers (Dell'Acqua et al. 2023) and fluent hallucinations (Kalai & Vempala 2024; Kalai et al. 2025) distort perceived $p$ and collapse perceived VoI of checking; semantic-entropy probing (Farquhar et al. 2024) or external grounding helps restore VoI calibration.
* **Field 8 (Information Economics):** AI collapsing the cost of polished form (Spence 1973; Akerlof 1970) destroys cheap reliability heuristics, while shared-model monoculture invalidates independent-check assumptions in sequential verification.
* **Field 9 (Human Factors & AI-Assisted Research):** Ironies of automation (Bainbridge 1983) and miscalibrated productivity perceptions (Becker et al. 2025) erode the tacit judgment behind living safety margins; pre-mortems (Klein 2007) and pre-committing to expected magnitudes act as practical awareness-expansion and anti-ritual protocols.

---

## 6. High-Leverage Leads & Open Questions

1. **Dynamic Coherence Without Information Aversion:** Can institutional commitment devices (pre-registered stopping rules, staged gates) pair with non-SEU ambiguity rules to preserve tail caution while neutralizing Al-Najjar & Weinstein's (2009) free-information-aversion pathology?
2. **Budgeting In-Frame vs. Out-of-Frame Exploration:** How should organizations or agentic pipelines split finite verification budgets between Bayesian VoI (refining known parameters) and open-ended anomaly-seeking (red-teaming, fault injection) when frame-incompleteness probability is itself uncalibrated?
3. **Action-Gating Thresholds for Agentic Systems:** Formalizing operational thresholds linking $p^* = \Delta U / (\Delta U + L)$, empirical error-escape rates, and Arrow–Fisher quasi-option value could determine when an LLM agent action requires sandboxing, human escalation, or formal verification.
4. **Leading Indicators of Safety Clutter:** What observable metrics distinguish a living humility margin from ritualized safety clutter (Rae, Provan, & Dekker) *before* failure, enabling pruning without triggering normalization of deviance?
5. **One-Shot Ruin as Option-Value Truncation:** Can the Peters (2019) vs. Doctor, Wakker, & Wang (2020) ergodicity dispute be resolved for one-shot high-stakes choices by modeling ruin not as an infinite-horizon time-average failure, but as irreversible truncation of all future Arrow–Fisher option values?
