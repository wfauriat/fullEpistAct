# Whole-Book Review Pass — *Agir d’après une représentation du monde*

**Reviewed artifact:** `monographie/build/livre-ecran.pdf` (264 PDF pages: front matter `i–xii`, body and back matter `1–252`)  
**Author listed:** W. Fauriat  
**Review scope:** Blind, cover-to-cover read of the compiled PDF (conceptual coherence, argumentative flow, formal/quantitative accuracy, terminology, cross-references, typography, and build completeness).

---

## 1. Executive Summary

The monograph addresses a single organizing question: *when we act on the world through finite representations—models, rules, software systems, or learned components—what can warn us in time that our representation is wrong?*

Its central thesis unfolds across five parts:

1. **Every deliberate action is mediated by a finite representation built inside a frame (*cadre*)**—a pre-inferential choice of variables, categories, model class, and objective—leaving an open **tacit background** ($\mathcal{T}$, noted $(\dots)$ in formulas). Because the world responds to the *action* rather than to the *representation*, no internal rigor (deductive, inductive, or statistical) can certify the adequacy of the frame itself.
2. **Error bars and robustness tools stay inside the frame:** predictive uncertainty only measures disagreement among *admitted* alternatives ($\Theta$). Detecting an error—whether internal or caused by an omitted factor $z$—requires confronting an affirmation with a **comparator** satisfying five simultaneous conditions: *existence*, *difference* (failing differently), *comparability*, *arrival on time*, and *uptake* (*prise en compte* with authority). Internal checks share the frame as a common cause; chains accumulate blind spots and *launder* conditions at interfaces; cross-checks keep only shared blind spots; and when producer error rates drop faster than checker false-alarm rates, PPV collapses and human uptake erodes.
3. **Classical software vs. learned components:** Classical software earned trust at scale by wrapping layers in **written contracts** verified upfront (*vérification en amont*), ensuring failures retain an *address*. Machine learning and LLMs *spend* upfront guarantees and readability to gain reach on unspecifiable tasks. At the top of the stack, a **regime flip** occurs simultaneously on what is promised, how failure looks (fluent, assured prose), and where post-hoc inquiry lands (a distribution, not a line of code). Competence follows a *jagged frontier*; generative calibration mathematically forces invention on singleton rare facts; and repeated sampling catches random guesses (*erreurs hasardées*) while remaining blind to *constant errors*.
4. **Automation compounds these vulnerabilities on three axes:** it **chains** learned components into autonomous agents whose errors execute directly at machine speed while laundering conditions into plain text; it **erodes** implicit human checks (removing the slow friction that built personal comparators, erasing visible hesitation *tells*, breaking the costly signal of polished form into an Akerlof pooling equilibrium, and triggering Bainbridge's irony); and it **correlates** blind spots collectively when whole communities borrow from the same foundation models ("single lender"), launder provenance across shared knowledge commons, and starve independent evaluation capacity under output pressure.
5. **Practical stance:** Rather than offering a closed meta-procedure (impossible by infinite regress), the book separates *repeated* decisions (amenable to calibration) from *one-shot* high-stakes decisions (requiring a **humility buffer** $b$ and **gates**/*verrous*), pairs **sandboxes** with gates for safe exploration, gives recipients of confident numbers four diagnostic questions, and organizes controls across three mutually dependent levels (*attitude*, *placement*, *organization*, including *seeded errors*). The *Conclusion* turns the book's own framework back onto itself.

Overall, the monograph is intellectually serious, remarkably cohesive, and unusually honest about the epistemic status of its own claims. Its core strength—building the general theory of controls in Part II *before* touching AI in Parts III–IV—prevents the AI chapters from reading like transient commentary. The remaining issues fall mainly into four buckets: (a) a small number of conceptual/numerical tensions in Chapters 5, 13, 16, and 17; (b) cover-to-cover repetition from modular chapter self-containment; (c) cross-reference and layout regressions in the compiled PDF; and (d) expected incomplete placeholders (9 figures, 1 table, 2 appendices, 3 verification tags, and bibliography `?` markers).

---

## 2. Chapter-by-Chapter Decomposition

### Front Matter & Chapter 0
* **Avant-propos (pp. viii–xii):** States the practical aim; positions the book as a *working hypothesis* rather than a prescription; transparently declares the hybrid human–LLM authoring process and assumes full human responsibility; defines the reading rules (main text vs. 6 box types: *Boîte à outils*, *Noyau formel*, *Exemple quantitatif*, *Étude de cas*, *Nuance et discussion ouverte*, *Question à se poser*) and 4 epistemic statuses (*définition*, *résultat sous hypothèses*, *hypothèse de travail*, *constat empirique*).
* **Ch. 0 — Cartographier le terrain (pp. 1–17):** Non-technical overview anchored by three opening cases (*Mars Climate Orbiter*, *Mata v. Avianca*, METR 2025), previewing every major theme, the 5-part architecture (Fig. 0.2 placeholder), the 7+ recurring examples, and 8 selective reading paths (Table 0.1).

### Part I — Agir d’après une représentation (pp. 18–59)
* **Ch. 1 — Boîte à outils : logique, conditionnement, probabilité (pp. 20–29):** Contrasts deduction (validity vs. soundness) and induction (Hume's "provided that"); introduces open-background rules $A \cap (\dots) \to B$ and $\mathcal{T}$; reviews Kolmogorov axioms, frequentist vs. judgment readings, conditioning, total probability, Bayes in odds form (ultrasonic weld example, missing table placeholder on p. 27), and logarithmic surprise $S(p) = -\ln p$.
* **Ch. 2 — Le cadre : ce qui compte et ce qu’on tait (pp. 30–41):** Defines *représentation* (Def. 1) and *cadre* (Def. 2: variables, categories, model class, objective). Unfolds the boiling-water progression (Table 2.1); shows formal rigor does not escape the frame via Pearl's *do*-calculus and conformal prediction; illustrates distribution shift via a clinical hospitalization model; connects to McCarthy/Hayes and Dennett's *frame problem*.
* **Ch. 3 — Mondes possibles : la probabilité comme jugement (pp. 42–50):** Interprets probabilities as weights over possible worlds (Russell & Norvig); introduces *reasoning in reverse* (finding what hidden variation in $\mathcal{T}$ flips the conclusion); defends subjective coherence + empirical confrontation; quantifies single-outcome ambiguity on the sailing race (Fig. 3.1, Table 3.1: surprise 3.00 vs. 6.91, $\Lambda = 50$ when breaking; $\Lambda = 0.951$ when holding); introduces *calibration*, strictly proper scoring rules (log score, Brier), and written *track records*.
* **Ch. 4 — Décider d’après ce que l’on croit (pp. 51–59):** Introduces Savage's SEU and derives the failure threshold $p^* = \Delta U / (\Delta U + L) = 1 / (1 + L/\Delta U)$ (Fig. 4.1, Table 4.1: sailing $L/\Delta U = 25 \Rightarrow p^* \approx 3.85\%$; Russian roulette $L/\Delta U = 10\,000 \Rightarrow p^* \approx 0.0100\%$); distinguishes repeated vs. *one-shot decisions*; leaves open how to decide when the frame may omit a fatal risk.

### Part II — Ce qui peut nous détromper (pp. 60–119)
*(Deliberately uses non-AI examples to establish generality; houses all 5 numbered Propositions.)*
* **Ch. 5 — Trois incertitudes, et ce que mesure une barre d’erreur (pp. 63–72):** Uses the law of total variance (Eq. 5.1) to separate *aleatory* and *epistemic* uncertainty as a modeling choice; defines *ontological uncertainty* outside $\Theta$; establishes **Proposition 1** (*résultat sous hypothèses*): error bars measure disagreement within $\Theta$. Distinguishes constant vs. varying omitted factors (Russell's turkey, pre-2008 mortgage models); shows safety factors (1.8 on a bracket facing salt corrosion) and OOD/perturbation tools remain inside the frame; nuances *Challenger* as a mixed failure.
* **Ch. 6 — Détecter une erreur : comparateurs et cinq conditions (pp. 73–82):** Defines *affirmation* (Def. 3), *contrôle* (Def. 4), *comparateur* (Def. 5: another affirmation, prior written text, world observation), *prise en compte* (Def. 6), and *probabilité d'échappement* (Def. 7). States **Proposition 2** (*définition*) and the five necessary detection conditions (*existence*, *différence*, *comparabilité*, *arrivée à temps*, *prise en compte*; Fig. 6.1 placeholder, Eq. 6.1–6.3); analyzes *Challenger* (Tufte's missing 23-flight temperature contrast + rejected engineer objection); contrasts disagreement (proves $\ge 1$ side false) vs. agreement (worthless without severity).
* **Ch. 7 — Le cadre, cause commune de nos contrôles (pp. 83–92):** Transposes engineering common-mode failure to reasoning; states **Proposition 3** (*résultat sous hypothèses*) via **Model M3** (Fig. 7.1 placeholder, Eq. 7.1): (a) internal comparators depend only on $x$ and carry $\Lambda = 1$ toward omitted $z$; (b) world observations detect $z$ only if $z$ varied during collection and affected recorded variables (else *distribution shift*, e.g., Google Flu Trends 2014). Proves infinite regress of meta-procedures (No Free Lunch, Hume, Goodman's *grue*/*vleu*); identifies the two external channels: being warned vs. low-cost/reversible trial.
* **Ch. 8 — Indépendance, chaînes et contrôles croisés (pp. 93–107):** Series vs. parallel reliability; defines *angle mort* $B_i$ (Def. 8). States **Proposition 4** (*hypothèse de travail* / composite): independence is relative to an error class and tends to cost comparability (Table 8.1; Levins/Orzack & Sober; Knight & Leveson 1986 27-version study). States **Proposition 5** (*résultat sous hypothèses*) via **Model M1** (Eq. 8.1–8.4; Fig. 8.1, Table 8.2 for $N=4$): chains cumulate blind spots; cross-checks reduce them to $B_1 \cap (B_2 \cup B_{\text{cmp}})$. Defines *blanchiment* (Def. 9) and its cousins (dropped units/definitions, dropped provenance) via *Mars Climate Orbiter*.
* **Ch. 9 — Sévérité, fausses alertes et probabilité d’échappement (pp. 108–119):** Base-rate fallacy (1% prevalence, 90% sensitivity, 5% false alarms $\to$ 15.4% PPV); defines *sévérité* (Def. 10, Mayo, Eq. 9.1); demonstrates PPV collapse as producer errors fall against a fixed checker (1% vs. 10% $\to$ 91.7% false disagreements); distinguishes Bayes's VPP from behavioral *probability matching* (Bliss et al. 1995, $u \in [0,1]$); decomposes residual risk in **Model M1** as $R = P(E)(1 - su)$ (Eq. 9.3–9.5, Fig. 9.1, Table 9.4), showing how a 10× more accurate producer can form a 9× riskier system (Table 9.3).

### Part III — De l’informatique classique à l’IA (pp. 120–165)
* **Ch. 10 — Pourquoi l’on peut oublier les couches basses (pp. 123–132):** Explains classical composition via Hoare triples $\{P\}\,C\,\{Q\}$, Design by Contract (Meyer), *composant spécifié* (Def. 11), and *vérification en amont* (types, unit tests, review, static analysis, fuzzing, formal proof—with Dijkstra's caveat). Emphasizes that failures have an *adresse*, though they can remain silent (*Mars Climate Orbiter* 1999); distinguishes three contract enforcement degrees (mechanically enforced, written prose, implicit/formulable).
* **Ch. 11 — Quand la règle est tirée des données (pp. 133–140):** Defines *composant appris* (Def. 12): trades upfront guarantees and readability for reach (BCG 2023 inside-frontier gains: +12.2% tasks, +25.1% speed, ~40% quality). Explains next-token prediction, *logit lens*, fluent errors with no contract violation (*Mata v. Avianca*, contrasted in a *Nuance* box with *Moffatt v. Air Canada*), and why *steering* (prompts, RLHF, benchmarks, Goodhart's law) is not specifying ("training a dog vs. wiring a circuit breaker").
* **Ch. 12 — Au sommet de la pile, un autre régime (pp. 141–152):** Defines *changement de régime* (promise, failure appearance, post-hoc inquiry flip together); characterizes the *frontière en dents de scie* (BCG outside-frontier −19 pp accuracy drop); distinguishes *omission structurelle* from *omission de saillance*; defines *calibration générative* and Kalai–Vempala's singleton lower bound (Eq. 12.1) plus benchmark incentives against abstention (Kalai et al. 2025); shows in a 5-draw example (Fig. 12.1, Table 12.1) that repetition catches *erreurs hasardées* (semantic entropy, Farquhar et al. 2024) but fails on *erreurs constantes* (42.0% severity on a common misconception).
* **Ch. 13 — Synthèse : deux axes et quatre sources de comparateurs (pp. 153–165):** Replaces the 1D uncertainty list with a 2×2 matrix (Table 13.1, Fig. 13.1 placeholder) crossing cause location (*dans le cadre* / *hors du cadre*) with comparator response (*erreur signalée* / *erreur silencieuse*); shows formalism shifts the column, never the row. Splits comparators into 4 sources (Table 13.2): prior formal rules (compilers, Lean 4 autoformalization, Simplex), personal checks, another reasoner, and the world (fast in deterministic software, unchanged in physical matter). Maps the matrix onto *vérification* (top row) vs. *validation* (row boundary).

### Part IV — L’automatisation et ses angles morts (pp. 166–200)
* **Ch. 14 — Des chaînes qui agissent (pp. 169–180):** Analyzes pipelines and autonomous *agents* as self-reinforcing $N$-step series chains (Fig. 14.1, Table 14.1 for $N=12$: uncontrolled failure jumps from 21.9% at $N=4$ to 52.4% at $N=12$; with $q=3\%$ and cross-checks, $q$ participates in 42.2% of remaining failures); highlights the operational shift from passive answers to executed actions (Knight Capital 2012: 45 min, >\$460M loss); tracks textual *blanchiment* across extract–summarize–plan–execute; diagnoses the **inversion of authority** giving maximal action power to the least guaranteed layer.
* **Ch. 15 — L’érosion des vérifications humaines (pp. 181–189):** Details four erosion mechanisms: (1) loss of slow analytical friction that spontaneously forged personal comparators; (2) disappearance of the hesitation *signe révélateur* and subjectivity vs. measurement illusion (METR 2025: +19% slower measured vs. −20% perceived); (3) collapse of clean form as a Spence *signal coûteux* into Akerlof's *équilibre mélangeant* (requiring audited disclosure); (4) Bainbridge's irony (1983) plus framing and *complaisance* (*sycophancy*, Sharma et al. 2023) traps, yielding two conditions for genuine human–model cross-checking.
* **Ch. 16 — Angles morts collectifs (pp. 190–200):** Reuses Model M1 (Fig. 16.1, Table 16.1) to separate shared-model correlation ($c$: 10% $\to$ 60%) from false-alarm fatigue ($f$: 5% vs. 0.5%); introduces the "single lender" metaphor (borrowed comparators never catch the lender's blind spots); analyzes *blanchiment de provenance* (echo chambers + Shumailov et al. 2024 recursive *model collapse* degrading epistemic commons); explains the institutional evaluation bottleneck starving review capacity as output volume surges.

### Part V — Décider et se prémunir & Conclusion (pp. 201–242)
* **Ch. 17 — Décisions sans appel (pp. 204–216):** Introduces **Model M2** with real-world risk $p_w = 1 - (1-p)(1-z)$ (Eq. 17.1) and the *marge d'humilité* $b$ ($p+b < p^*$, Eq. 17.2), partitioning outcomes into 4 quadrants (Fig. 17.1, Tables 17.1–17.2); explains why $z$ cannot enter the decision rule; separates calibration (repeated stable tasks) from *verrous* (Def. 13) + *bacs à sable* (Def. 14); provides 4 questions for recipients of any confident number (and notes institutions—not the LLM—must answer them).
* **Ch. 18 — Un remède à trois niveaux (pp. 217–229):** Organizes defenses across three interdependent levels: (1) **Attitude** (pre-commitment expectation, *pré-mortem*, deliberately widening $\Theta$—bounded by the person's own frame and incentives); (2) **Placement** (*where*: transition points to action; *who*: sharing the interface and understanding the underlying level; *what*: output vs. representation; *how much*: scaling to stakes and capping output; RAG as placement rather than truth-maker); (3) **Organization** (budgeting/capping by evaluation capacity, mandatory verification status, written track records, and *erreurs injectées* modeled on aviation TIP and mutation testing). Maps levels onto the 5 conditions (Fig. 18.1 placeholder) and closes with 5 pre-action questions.
* **Conclusion : la méthode appliquée à elle-même (pp. 230–242):** Catalogs every major claim's epistemic status and weakest point (Table 1); lists 6 unresolved tensions (optimal checker distance, cost/independence as mere tendency, salience omission softening Prop. 3, uptake as behavioral rather than Bayesian, net risk variation left unmeasured, remedies as working practices); specifies empirical observations that would refute the argument; evaluates the book's own LLM-assisted provenance and comparators; submits the book to its own 4 questions and reaffirms its working-hypothesis posture.

### Appendices & Bibliography (pp. 243–252)
* **Annexe A — Outils de référence (p. 243):** Placeholder (*Annexe à rédiger*).
* **Annexe B — Glossaire (pp. 244–247):** Complete alphabetical glossary of 35+ defined French terms with English equivalents and introducing chapters.
* **Annexe C — Notation (p. 248):** Table C.1 of core symbols and introducing chapters.
* **Annexe D — Paramètres des exemples quantitatifs (p. 249):** Placeholder (*Annexe à rédiger*).
* **Bibliographie (pp. 250–252):** 35 references spanning philosophy of science, probability/decision theory, software/safety engineering, economics of information, and ML/LLMs.

---

## 3. Argumentative Flow and Readability

### Strengths
* **Macro-architecture ("forge the keys before the locks"):** Placing general epistemology and reliability theory (Parts I–II) ahead of software and LLMs (Parts III–IV) makes the diagnosis of AI agents, sycophancy, and collective correlation feel earned rather than speculative.
* **Disciplined separation of text and apparatus:** Moving proofs (*Noyau formel*), refreshers (*Boîte à outils*), and objections (*Nuance et discussion ouverte*) into typed boxes keeps the main prose flowing cleanly without losing rigor.
* **Concrete, persistent anchors:** The recurring scenarios (sailing race, boiling water, corroded bracket, *Mars Climate Orbiter*, *Challenger*, *Mata v. Avianca*) create strong thematic continuity as the formal tools deepen.
* **Prose quality:** The French is crisp, concrete, and free of inflated jargon; key analogies (nautical chart vs. hull, shipping containers, training a dog vs. wiring a breaker, climbing a ridge vs. helicopter drop, single lender vs. borrowers) carry genuine explanatory weight.

### Friction Points for a Linear Reader
* **Redundant retellings across chapters:** Designed for the 8 selective reading paths (Table 0.1), each chapter opens with a summary of prior chapters, repeats key definitions, and ends with *Points clés*. More noticeably, several case studies are told in full multiple times:
  * *Mars Climate Orbiter* is narrated in full detail four times (Ch. 0.1 p. 1, Ch. 8.6 p. 106, Ch. 10.5 pp. 129–130, and Ch. 12.1 p. 142).
  * *METR (2025)* appears twice as a full *Étude de cas* box with almost identical wording (Ch. 0.1 p. 2 and Ch. 15.2 pp. 183–184).
  * *Mata v. Avianca* appears in full in Ch. 0.1 (pp. 1–2) and Ch. 11.3 (p. 137).
* **Out-of-order model labels (`M3` $\to$ `M1` $\to$ `M2`):** In reading order, **Model M3** appears first (Ch. 7), followed by **Model M1** (Ch. 8–9) and **Model M2** (Ch. 17). Even with the pointer in Section 0.7 (p. 15), encountering `M3` before `M1` is jarring and reads like numbering carried over from an external source paper.

---

## 4. Logical, Conceptual, and Quantitative Findings

### A. Substantive Argumentative & Formal Tensions

1. **Ch. 16 Table 16.1 vs. the Ch. 0.5.4 / Ch. 16.1 Risk Warning (pp. 192–195, 236):**
   * Section 0.5.4 and Ch. 9.5 demonstrate how a 10× more accurate producer can create a 9× riskier system ($10\% \times 1\% = 0.1\%$ vs. $1\% \times 90\% = 0.9\%$).
   * Yet in Ch. 16's flagship illustration (**Table 16.1**, p. 194), moving from *Contrôle entre pairs* ($P(\text{faux})=10\%, c=10\%$) to *Un modèle pour tous* ($P(\text{faux})=2\%, c=60\%$) **reduces** residual risk from $5.57\%$ to $1.93\%$ under probability matching, and from $2.80\%$ to $1.36\%$ under full alert review—remaining below the uncontrolled 2% rate.
   * The *Conclusion* candidly acknowledges this (p. 236), noting that net risk direction is empirical. Within Ch. 16 itself, however, the table currently blunts the section's warning (*"Le taux d'erreur baisse, la probabilité d'échappement monte"*). Furthermore, because $c$ is a *conditional* share of errors ($P(\text{shared} \mid E)$), eliminating 80% of idiosyncratic errors mechanically inflates $c$ even when absolute shared-cause errors barely shift ($1.0\%$ vs. $1.2\%$ in Table 16.1).
   * Additionally, the caption of Fig. 16.1 and text on pp. 193–195 describe the 68.0% escape floor as *"imposé par les 60 % de causes partagées"*, whereas $1 - s = 1 - (1-0.60)(1-0.20) = 68.0\%$ combines the 60% shared-cause floor $c$ with the 8% independent misses $(1-c)m$.

2. **Humility Buffer $b$ vs. Savage's SEU Axioms (Ch. 17, pp. 205–210):**
   * Model M2 states that $b$ is *"ni une mesure ni un estimateur de $z$"*, yet prescribes setting $b$ in light of the stakes ratio $L/\Delta U$ (p. 205) and adds $b$ directly to $p$ in probability units ($p + b < p^*$, Eq. 17.2).
   * In strict Savage SEU, $L/\Delta U$ is already fully encoded in $p^* = 1/(1 + L/\Delta U)$, so sizing $b$ by $L/\Delta U$ risks double-counting stakes; and adding $b$ to $p$ is formally equivalent to either revising subjective $p$ upward (for model misspecification) or departing from SEU toward ambiguity aversion. The *Nuance* box on p. 210 explains why $z$ cannot enter the decision rule, but does not address how $b$ relates to $p$ and $L/\Delta U$ under Savage's axioms.

3. **Shift in the Meaning of *cadre* Between Def. 2 and Table 13.1 (Ch. 2, 12, 13):**
   * Definition 2 (p. 34) defines a *cadre* by four explicit choices: variables, categories, model class, and **objective**.
   * In **Table 13.1** (p. 154), LLM hallucinations (*Mata v. Avianca*) and *omissions de saillance* are placed in **"Cause dans le cadre"**. For an LLM trained on next-token plausibility, however, there is no explicit variable list $X$, and its optimization *objective* (plausibility) diverges from the user's objective (factual truth)—which by Def. 2 would implicate the *cadre* itself. The *Conclusion* partially concedes this (p. 233: *"le classement d'une omission de saillance peut hésiter"*; p. 236: *"devient donc une affaire de degré"*), but Ch. 13.1 itself does not clarify that *"dans le cadre"* in Table 13.1 refers to the *task/domain* rather than a formal variable set $X$.

4. **Scope of Proposition 1 vs. Its Formal Proof (Ch. 5, pp. 67–69):**
   * Proposition 1 states universally: *"Tout énoncé quantitatif d'incertitude résume à quel point les membres d'un ensemble spécifié d'alternatives admises sont en désaccord."*
   * The *Noyau formel* (pp. 68–69) proves this only for predictive variance $\operatorname{Var}(Y \mid X=x)$ via the law of total variance (assuming finite second moments). Non-variance measures (worst-case intervals, quantile/conformal sets) obey the same structural exclusion of unmodeled hypotheses, but are not covered by Eq. (5.1).

5. **Dual Meaning of *risque* Across Parts I/V vs. II/IV:**
   * In Ch. 4 and Ch. 17, *risque* ($p$, $p_w$) denotes failure probability paired explicitly with stakes $L/\Delta U$. In Ch. 9 and Ch. 16, *risque* ($R = P(E)(1-su)$, Eq. 9.3) denotes the *probability of an unchecked false affirmation leading to action*, implicitly weighting all errors equally unless coupled back to stakes.

### B. Local Mathematical, Logical, and Definitional Precision

* **Table 8.2 (p. 103) & Table 14.1 (p. 174) column header:** The rightmost column is labeled *"Part des défaillances restantes due à q"*, whereas the formula $q / P(\text{échec})$ ($68.3\%$ and $42.2\%$) computes the fraction of failures *in which $q$ occurs* ($P(Q \mid Q \cup I)$, matching the figure captions and prose *"dans lesquelles intervient le facteur partagé"*). Failures attributable *solely* to $q$ would be $q(1-p_{\text{ind}})/P(\text{échec})$.
* **Ch. 12 5-draw example (pp. 149–150):** Item 2 (*Fait rare et arbitraire*) lists *"une autre date 10 %"* as the 6th outcome, and the calculation adds $0.10^5$ inside the collision probability as if *"une autre date"* were a single specific date rather than a residual bucket of many dates.
* **Ch. 6 Prop. 2 & Def. 6 circular echo (pp. 74, 76):** *Définition 6* defines *prise en compte* as *"le fait qu'un désaccord parvienne à quelqu'un qui à la fois en prend acte et a l'autorité pour agir"*, echoing *"en prend acte"* from Proposition 2.
* **Ch. 6 vs. Ch. 9 symbol reuse:** *Noyau formel* in Ch. 6 (p. 78) denotes *"detected and acted upon before action"* as $D$ (and the five conditions as $C_1,\dots,C_5$), whereas Ch. 9 Eq. (9.3) (p. 113) denotes the same *"caught and stopped before action"* event as $C$, alongside lowercase $c$ for shared error fraction. (Appendix C omits $C$ and $D$, listing only $P(E)$.)
* **Ch. 7 Model M3 Hypothesis 2 (p. 86):** *"z n'est pas enregistré dans x, et aucune variable retenue dans X ne varie avec z au-delà de ce que x fixe déjà"*—the second clause is redundant once Hypothesis 3 conditions on $X = x$.
* **Ch. 18.4 Level 3 coverage (p. 227):** The Level 3 bullet highlights *différence*, *comparabilité*, and *prise en compte*, omitting that naming domain controllers also establishes *existence* of a comparator.

---

## 5. Build, Cross-Reference, Typography, and Completeness Defects

1. **Broken section cross-reference phrasing (`\nameref` / `@sec:` artifacts):**
   * Gender mismatch `"au section 0.7"` in Ch. 7 (p. 85) and Ch. 17 (p. 205).
   * Missing *"section"* after French articles:
     * `"à la Le monde : rapide dans le calcul, inchangé dans la matière"` (Ch. 14, p. 178)
     * `"sur un constat de la Vos propres contrôles : l’effacement par défaut d’une compétence préalable"` (Ch. 15, p. 181)
     * `"batterie de tests écrite à l’avance : Un énoncé fixé à l’avance : reconstruire..."` (Ch. 17, p. 213)
     * `"comme le décrivait la Un danger structurel : la chaîne à N maillons"` (Ch. 17, p. 214)
   * Bare parenthetical section-title injections without *"section"* across Ch. 14–18 and the Conclusion (e.g., `(Le monde : rapide dans le calcul, inchangé dans la matière)` on p. 199; `(Limite structurelle et nécessité collective)` on p. 239).
2. **Wrong running headers (`\markboth`) & Conclusion visual placement:**
   * *Avant-propos* (pp. ix–xii) carries the running header *Table des matières*.
   * *Conclusion : la méthode appliquée à elle-même* (pp. 230–242) carries the running header *18 Un remède à trois niveaux* and appears sequentially inside Part V without a part-level break.
   * *Bibliographie* (pp. 251–252) carries the running header *D Paramètres des exemples quantitatifs*.
3. **Broken glyph for $\mathcal{T}$:**
   * Renders as a missing-character box (`□`) in Appendix B (p. 244, entry *arrière-plan tacite*) and Appendix C (p. 248, Table C.1), whereas $\mathcal{T}$ renders properly in body text.
4. **Unresolved citations & editorial markers:**
   * Every inline citation carries a trailing `?` (e.g., `(Hume 1748)?`).
   * Three highlighted `[à vérifier : ...]` tags remain in the text:
     * Ch. 2 (p. 40): `[à vérifier : Shanahan, « The Frame Problem », SEP]`
     * Ch. 5 (p. 66): `[à vérifier : rapport ou étude sur les modèles de risque hypothécaire et la corrélation des défauts avant 2008]`
     * Ch. 11 (p. 137): `[à vérifier : déclaration d’Air Canada (technologie antérieure)]`
5. **Missing content placeholders (known incomplete build items):**
   * **9 figures marked *Figure à générer*:** `figures/ch00-serie-parallele.pdf` (p. 7), `figures/ch00-carte-ouvrage.pdf` (p. 13), `figures/ch02-cible-monde-action.pdf` (p. 31), `figures/ch05-trois-incertitudes.pdf` (p. 67), `figures/ch05-ferrure-marge.pdf` (p. 71), `figures/ch06-cinq-conditions.pdf` (p. 76), `figures/ch07-cause-commune.pdf` (p. 86), `figures/ch13-deux-axes.pdf` (p. 156), `figures/ch18-trois-niveaux.pdf` (p. 226). *(All remaining figures in Ch. 3, 4, 8, 9, 12, 14, 16, and 17 are rendered and legible.)*
   * **1 missing table:** `[Contenu généré manquant : tableaux/ch01-bayes-cotes.md]` (Ch. 1, p. 27).
   * **2 unauthored appendices:** Annexe A *Outils de référence* (p. 243) and Annexe D *Paramètres des exemples quantitatifs* (p. 249), both reading *"Annexe à rédiger."*
