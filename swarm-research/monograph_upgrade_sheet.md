# Surgical Upgrade Sheet for *Agir d’après une représentation du monde* (`livre.html`)

> **VERIFIED EDITION — 2026-11-21.** This sheet has been audited against the monograph sources (`monographie/chapitres/*.md`), the Track 1 and Track 2 code, and the cited literature. Each item now carries a **status**, a **severity for the current manuscript**, and a **revised action**. Wherever a claim is marked **SUPERSEDED**, the original wording is kept struck through for traceability, and the revised action replaces it. **Use the revised actions, not the original "Change" lines.**
>
> **Overall verdict:** none of the seven items reveals a serious logical or argumentative problem in the manuscript. The core (M1–M3, P1–P5, the five detection conditions, the Ch. 13 matrix, the Part V logic) holds. The highest severity found is **moderate**. The closest thing to an actual error is the unconditioned model-collapse sentence in Ch. 16.3 (item 2). Several of the "genuine falsifiers" raised by the refinement pass misread the book, which already contains the distinction or the result. The main prescriptive item (item 5) rests on simulation artifacts and must **not** be applied.
>
> **How the audit was done:**
> - Book passages located in the Markdown sources; line numbers below refer to `monographie/chapitres/`.
> - Track 1 re-derived with SymPy/NumPy (the `.venv_track1` Z3 environment no longer exists, so the Z3 calls were not re-run).
> - Track 2 re-run on a modified copy of `engine.py` with two added test switches (`rho_H`, `no_bypass`). The original artifacts were left untouched.
> - Four citations checked on the web (Bastani 2025, Liang 2023, Rae et al. 2018, VeriGuard); the rest checked against known primary sources.

**Original purpose (unchanged):** A 3-minute, high-ROI checklist of concrete revisions surfaced by our 9-domain synthesis, Hydrogen High refinement pass ([refinement_report.md](refinement_report.md)), and Track 1–2 formal/simulation validations ([Track 1](auto_research/track1_formal/RESULTS.md), [Track 2](auto_research/track2_sim/RESULTS.md)). Nothing here invalidates the book's core framework (**M1–M3**, the 5 detection conditions, or Ch. 13's matrix); each item sharpens scope or closes an empirical/formal gap. *(Audit: this sentence is confirmed.)*

---

## Verification summary

| # | Item | Status | Severity for the manuscript | Revised action in one line |
|---|---|---|---|---|
| 1 | P3(a) vs inference-time search | **PARTLY SUPERSEDED** (no scope fix needed) | Minor (citations only) | Add Kamoi 2024 to 12.4. Cite Snell/Lightman as search that works *because of* an external verifier. |
| 2 | Model collapse (Gerstgrasser) | **KEEP** | **Moderate**: only real factual overreach found | State the data-replacement condition at 16:90 and 16:117. |
| 3 | 2021–2025 empirical studies | **KEEP — revised** (select, fix Liang 2023) | Moderate (Bainbridge anchoring), otherwise minor | Bastani + Budzyń in 15.4; Kleinberg & Raghavan in 16.1; Vaccaro, Steyvers, Peng/Cui as listed below. |
| 4 | Coupled p–z stress in M2 | **PARTLY SUPERSEDED** (copula numbers and Al-Najjar link withdrawn) | Minor | Sharpen the dependence sentence at 17:52. Cite Arrow & Fisher at 17:130. Anchor 17:97. |
| 5 | Uncertainty-gated vs stakes-gated checks | **SUPERSEDED** (Track 2 rule withdrawn) | None: applying it would *create* an inconsistency | Only cite Buçinca 2021 and Rae et al. 2018 at 17:145 / 18.2 "Combien". |
| 6 | Eckhardt–Lee, Littlewood–Miller, Vaughan | **KEEP** (strongest item) | Moderate (scholarly completeness, not logic) | Add at 08:91 and 06:123. |
| 7 | M1 thresholds, SAVI | **PARTLY SUPERSEDED** (keep p_crit; demote the rest) | Minor | One sentence with the break-even at 16:53. Optional footnote at 16:59. SAVI as a pointer only. |

---

### 1. Narrow Proposition 3(a) & Ch. 12.4 Against Inference-Time Search *(Scope Fix)*

* **Where:** Ch. 7 (*M3*), Ch. 12.4, and *Conclusion*.
* **Original change:** ~~Distinguish **in-frame salience elicitation** (where test-time compute scaling [Snell et al. 2024], Process Reward Models [Lightman et al. 2023/2024], and grounded debate [Khan et al. 2024] genuinely catch reasoning misses) from **out-of-frame omissions** ($z \notin \Theta$) and **unguided self-correction** (which fails without external verifiers, Kamoi et al. 2024).~~

> **Verification — PARTLY SUPERSEDED. Severity: minor.**
>
> - **The scope fix is already in the book.**
>   - P3(a) is stated only for a factor *absent from the frame* (`07-cadre-cause-commune.md:31`).
>   - The ch07 Nuance (`07:79`, *Représenter un facteur sans le mobiliser*) and the ch12 Nuance (`12-autre-regime.md:77`) already distinguish structural omission from salience omission. They already say that P3(a) holds only for checks reusing the same parameters and the same prompt wording, and that rewording or decomposing the problem can surface a dormant relation.
>   - `07:80` already states that internal checks remain effective against in-frame errors.
>   - The refinement report's "genuine falsifier" classification is therefore a misreading.
> - **The cited facts are correct:**
>   - Snell et al. 2024: compute-optimal test-time scaling can beat a 14× larger model.
>   - Lightman et al. 2023: a PRM solves 78.2% of a MATH subset.
>   - Khan et al. 2024: judges reach 76% / 88% accuracy vs 48% / 60% baselines, with debaters holding the source text.
>   - Kamoi et al. 2024: self-correction works mainly with reliable external feedback.
> - **Revised action (optional):**
>   - In the ch12 Nuance at `12:77`, add one sentence: verifier-guided search mobilises represented-but-dormant relations, and it succeeds *because* the verifier is a comparator from another source (ch13: tests, proof checker, retrieved text).
>   - In 12.4, cite Kamoi 2024 (optionally Huang et al. 2024, *LLMs cannot self-correct reasoning yet*) as empirical support for the existing claim that re-asking without an external comparator does not catch *erreurs constantes*.
>   - No change to Ch. 7 or the Conclusion.

---

### 2. Qualify Model Collapse in Ch. 16.3 *(Dissenting Result)*

* **Where:** Ch. 16.3 (*Blanchiment de provenance*).
* **Original change:** Pair Shumailov et al. (2024) with **Gerstgrasser et al. (2024)**: recursive pretraining collapse requires *data replacement*; accumulating synthetic text alongside a retained human corpus bounds test error. ~~Redirect the practical warning to **live post-2023 RAG/web contamination** where provenance is lost.~~

> **Verification — KEEP (first sentence). Severity: moderate.** This is the only item that corrects a genuine overreach.
>
> - **What the book says now.** `16-angles-morts-collectifs.md:90` reports Shumailov's collapse without its experimental condition: each generation replaces the previous data. Key point `16:117` generalises it as "expose par récursion les générations suivantes de modèles à une dégradation".
> - **Revised action.**
>   - Add one sentence with the replacement condition and Gerstgrasser et al. 2024: collapse is avoided, with test error bounded, when synthetic data *accumulates* alongside a retained human corpus.
>   - Soften `16:117` accordingly, e.g. "lorsque les données d'origine sont remplacées plutôt que conservées".
> - **What does not change.** The chapter's argument rests on provenance laundering and on the near-zero severity of copy-based corroboration (`16:86–88`). Gerstgrasser does not touch it.
> - **The "redirect to RAG/web contamination" half is superseded.**
>   - It is already largely present: the illusion of corroboration at `16:86` explicitly includes "un moteur de recherche documentaire".
>   - The quantitative "Retrieval Collapse" figures behind it are flagged `[UNVERIFIED]` in `refinement/02_empirical_2024_2026.md`. Do not cite them.

---

### 3. Anchor Ch. 15–16 with Verified 2021–2025 Empirical Studies *(Fills Conclusion's "Empirical Thinness")*

* **Where:** Ch. 15 & Ch. 16 (*Bibliographie* update).
* **Original change:** Add these vetted studies alongside Becker et al. (2025) and Dell'Acqua et al. (2023)—noting moderators honestly:
  * **Skill decay:** Bastani et al. (*PNAS*, $\sim 1{,}000$ students: GPT Base `+48%` practice / `-17%` unaided exam vs. GPT Tutor `+127%` / no decay); Budzyń et al. (2025, *Lancet Gastroenterol. Hepatol.*, $N=1{,}443$: observational ADR drop `28.4% → 22.4%`).
  * **Human–AI synergy bifurcation:** Vaccaro et al. (2024, *Nat. Hum. Behav.*, $g = -0.23$ overall, positive on content creation); Goh et al. (2024, *JAMA Netw. Open* RCT, clinical diagnosis); vs. greenfield/junior coding speedups (Peng et al. 2023 `+55.8%`; Cui et al. 2024 `+26.08%` PRs/wk).
  * **Fluency & uncertainty:** Steyvers et al. (2025, *Nat. Mach. Intell.*, $N=301$, length bias); Kim et al. (2024, *ACM FAccT*, $N=404$, first-person hedges).
  * **Monoculture & equity trap:** Kleinberg & Raghavan (2021, *PNAS*); Wataoka et al. (2024/2025, perplexity self-preference); Liang et al. (2023, *Patterns*, ~~`61.22%–97%+` false positives on TOEFL essays by AI detectors~~) + Liang et al. (2024, `6.5%–16.9%` ~~LLM-modified peer reviews~~).

> **Verification — KEEP, revised (select, do not add all). Severity: moderate for the Bainbridge anchoring, minor otherwise.**
>
> **The studies are real and the figures match the primary sources, with two corrections:**
> - **Liang et al. 2023 (*Patterns*).** 61.22% is the *average* false-positive rate of 7 detectors on 91 TOEFL essays. 97.8% (89/91) is the share flagged by *at least one* detector, not an individual detector's rate. The range "61.22%–97%+" mixes the two and must not be used.
> - **Liang et al. 2024.** 6.5%–16.9% is a corpus-level estimate of the share of peer-review *text* substantially modified by LLMs (ICLR 2024, NeurIPS 2023, CoRL 2023, EMNLP 2023), not a share of reviews.
> - **Bastani et al.** confirmed as *PNAS* 2025, 122(26), e2422633122 (published 2025-06-25).
>
> **Revised action, by priority:**
> 1. **Bastani 2025 (RCT, causal) and Budzyń 2025 (label it *observational*, before/after)** in the Bainbridge passage (`15-erosion-verifications.md:75`). It currently rests on Bainbridge 1983 alone. This is the most valuable addition.
> 2. **Kleinberg & Raghavan 2021** in 16.1 (`16:20` or `16:53`). It formally shows that monoculture can lower overall decision quality *even when the shared algorithm is more accurate*, which is exactly the book's point that the net sign is open.
> 3. **Vaccaro et al. 2024** in 15.4: human–AI combinations underperform the better of the two on decision tasks on average. **Steyvers et al. 2025** in 15.2 (*signe révélateur*, `15:20`): longer explanations raise user confidence without raising accuracy.
> 4. **Peng et al. 2023 or Cui et al. 2024** as a citation for the existing hedge in the METR box (`15:35`, "d'autres outils à d'autres moments peuvent accélérer certaines tâches"). The book already makes the point; it only lacks the reference.
> 5. **Optional / low priority:**
>    - Kim et al. 2024 and Wataoka et al. 2024 (self-preference of LLM judges, relevant to `16:72` *prêteur unique*).
>    - Liang 2023, which fits the Ch. 9 false-alarm argument or the 15.3 Nuance on audited vs self-declared disclosure better than an "equity trap".
>    - Liang 2024 (16.4: the evaluators themselves borrowing from the same lender).
>    - Goh 2024.
> 6. **Framing.** Drop the "Shadow AI" framing attached to these studies elsewhere in the swarm files: none of them measures bypass (see item 5).

---

### 4. Clarify Coupled $p$–$z$ Stress in Model M2 & Cite Decision-Theory Anchors *(Ch. 17.1)*

* **Where:** Ch. 17.1 (*M2*) and Ch. 17.3 (*bacs à sable / verrous*).
* **Original change:** Distinguish fixed-marginal event bounds ($\max(p,z) \le p_w \le \min(1, p+z)$) from latent common stress $S$ elevating *both* $p(S)$ and $z(S)$ simultaneously; ~~note Track 1's copula finding that at $K \ge 100$ ($p^* \le 0.99\%$), safe margin $b_{\min}$ consumes $\sim 97\%$ of $p^*$ (`0.0096/0.0099`), mathematically forcing **verrous** over margin-tuning; connect *verrous* to neutralizing Al-Najjar & Weinstein's (2009) free-information aversion~~ and *bacs à sable* to Arrow & Fisher's (1974) quasi-option value.

> **Verification — PARTLY SUPERSEDED. Severity: minor.**
>
> **Superseded 1: the copula figure is a numerical artifact.**
> - In `verify_m2.py`, `psi_of_b` returns Ψ = 0 by convention when no grid cell is admitted.
> - The smallest P value on the 180-point quantile grid is 0.00033. At K = 100, **b = 0.0096 is exactly the first margin at which no grid cell satisfies P < p\* − b**, so the code declares it "feasible". The same happens at K = 1000 (b = 0.0007 = 67% of p\*).
> - b_min is identical at λ_U = 0 (independence), so the copula plays no role. The script's own check `monotonic_trap_in_lambda_U` returns `false`.
> - What the setup actually shows: with E[Z] = 2% ≈ 2 × p\* and P(Z ≥ p\*) = 65%, **no** margin makes departure safe. The book already says this (Ch. 17 *Lecture*: "lorsque $p^\ast$ devient inférieur à toute marge plausible, la règle revient simplement à s'abstenir").
> - "Mathematically forcing verrous" is not a result. Verrous are justified in the book on other grounds (Def. 13, `17:100–121`).
>
> **Superseded 2: the Al-Najjar & Weinstein link.** Their 2009 paper *critiques* ambiguity-aversion models (for example, refusing free information, dynamic inconsistency). Since `17:97` likens the humility margin *b* to ambiguity aversion, they are a potential **objection to b**, not support for verrous. If cited at all, cite them as that objection.
>
> **Kept, reformulated:**
> - **Dependence sentence (`17:52`).** With *fixed marginals*, no dependence can push $p_w$ above $p + z$. Independence ($p + z - pz$) therefore underestimates by at most $p\,z$. The case the book names ("une fissure qui réduit la tenue du mât face aux rafales prévues") is an **interaction**: the hidden factor changes the probability of the represented perils, so the true *p* is no longer the computed one. Sharpen the sentence accordingly. The "latent common stress S" formalism is not needed in the book.
> - **Arrow & Fisher 1974** (quasi-option value under irreversibility) as an anchor for the sandbox / gate split (`17:130`). Henry 1974 is optional.
> - **New: anchor the uncited claim at `17:97`** ("apparenté aux approches d'aversion à l'ambiguïté ou de robustesse à la mauvaise spécification") with Gilboa & Schmeidler 1989 (maxmin expected utility) and Hansen & Sargent 2008 (robustness).

---

### 5. Address Friction–Bypass & Split Uncertainty-Gated CFFs From Stakes-Gated Locks *(Ch. 18)*

* **Where:** Ch. 18.1–18.3.
* **Original change:** Acknowledge **Buçinca et al. (2021)** ($N=199$: CFFs cut overreliance *and* lower satisfaction~~, driving Shadow AI bypass~~) and **Rae, Provan~~ & Dekker~~ (2018)** (*safety clutter*). ~~**Crucial Track 2 refinement:** do **not** trigger manual human CFFs on high stakes ($L/\Delta U > \tau_K$)—in 4,096 Sobol worlds that degenerated into static overload (`31.1%` bypass for $K > 500$). Trigger human CFFs **strictly on epistemic uncertainty** ($\hat{H}_t > \tau_H$: `1.30%` bypass, dominating `none` and `static` in `59.5%` of worlds), and enforce high-$K$ boundaries via non-bypassable orchestrator **verrous** (**CaMeL / VeriGuard** style).~~

> **Verification — SUPERSEDED (the Track 2 rule). Severity for the manuscript: none.** Applying the rule would *introduce* an inconsistency. Gating human review only on the model's own uncertainty contradicts P1 (uncertainty measures only disagreement within $\Theta$, Ch. 5) and the *erreurs constantes* result (Ch. 12.4: confident, repeated errors raise no uncertainty).
>
> **Why the Track 2 result does not hold:**
> - **The headline figure is not the code's own criterion.** "Dominating in 59.5% of worlds" uses cost only. The code's pre-defined dominance flag (cost **and** silent traps, `sweeps.py:88–94`) gives **2.8%** (`phase_boundaries.json`). `static_always` actually has the *lowest* silent-trap rate (5.98% vs 6.95%).
> - **The winning margin is negligible.** `adaptive_uq_only` beats `none` by 250.8 vs 252.6 mean cost (0.7%); the mean per-world relative gain is 0.05%. 90% of total cost comes from worlds with K > 1000.
> - **Verrous were never simulated.** Adding a non-bypassable `static_always` makes it the **worst** policy (cost 309.0, escape 77%). In the model, a human check detects nothing itself: it only cuts the automatic checker's *c* by 45% and *m* by 40%, while its friction pushes uptake toward VPP.
> - **The uncertainty signal is built to track errors.** `H_hat = D + noise`, and D drives both $P(E)$ and $c$. With an uninformative probe (`rho_H = 0`), `adaptive_uq_only` does worse than `none` (253.0 vs 251.8).
> - **One unswept constant reverses the verdict.** With `phi_CFF` changed from 0.14 to 0.06, `static_always` ties `adaptive_uq_only` on cost (241.0 each) and beats it on escape (49.3% vs 52.5%) and silent traps (5.4% vs 6.9%). None of the 28 `SimConfig` constants is varied in the Sobol sweep.
> - **"High stakes backfire" is true by construction.** K changes no behaviour in the model, and `adaptive_uq` with K > 500 *is* `static_always`.
> - **"Shadow AI" bypass is an assumption, not evidence.** Buçinca et al. 2021 found lower satisfaction and preference, not bypass. The other support cited ("enterprise governance studies") is unnamed. The assumption enters the simulator as a constant and exits as a "finding" (31.1% bypass) with its conditions stripped. That is the book's own *blanchiment* (Def. 9), and its Sobol indices only explore the admitted parameters (P1).
>
> **Corrections:**
> - Rae et al. 2018 has four authors: **Rae, Provan, Weber & Dekker**, *Policy and Practice in Health and Safety*.
> - CaMeL (Debenedetti et al. 2025) and VeriGuard (Miculicich et al., arXiv 2510.05156) are real, but they are *pre-fixed-statement* comparators (ch13 source 1). They can enforce a verrou's timing and policy; they cannot replace an independent comparator on in-frame silent errors.
>
> **Revised action:** cite Buçinca 2021 and Rae et al. 2018 as support for what the book already says. `17-decisions-sans-appel.md:145`: "Multiplier les verrous sur des actes bénins use la vigilance". 18.2 "Combien": proportion checks to the stakes. Optionally mention CaMeL / VeriGuard in Ch. 14 or 17.3 as examples of orchestrator-enforced verrous. No change to the logic of Ch. 18.

---

### 6. Add Two Classic Micro-Foundations to Part II *(Ch. 6.4 & Ch. 8)*

* **Where:** Ch. 6.4 (*Challenger*) and Ch. 8.3 (Knight & Leveson).
* **Original change:** Add **Eckhardt & Lee (1985)** / **Littlewood & Miller (1989)** (input-difficulty covariance proves *why* zero-communication checks correlate, grounding M1's parameter $c$) and **Diane Vaughan (1996)** (*normalization of deviance* explaining why organizational *prise en compte* fails).

> **Verification — KEEP. This is the strongest item. Severity: moderate** (scholarly completeness, not a logical flaw).
>
> - **Eckhardt & Lee / Littlewood & Miller (`08-independance-chaines.md:91`).** The book explains the Knight & Leveson result by a shared specification and shared training habits. That is incomplete, not wrong. Eckhardt & Lee show that **variation in input difficulty alone** creates positive correlation even between truly independent teams: inputs hard for one are hard for all. This mechanism transfers directly to LLMs. Littlewood & Miller show that *forced* diversity can make the correlation negative, which is the theory of "se tromper autrement" by design.
> - **The $c_{\text{eff}}$ identity in Track 1 is algebraically correct but definitional.** $c_{\text{eff}}$ can be negative, so it does not map onto M1's $c$ (a *share* in [0,1]) without a caveat. Keep it out of the main text; Annex A at most.
> - **Vaughan 1996 (`06-detecter-une-erreur.md:123`).** This is the standard *Challenger* reference and it is absent from `biblio.bib`. Normalization of deviance explains the uptake (*prise en compte*) failure and fits the book's "contresens répandu" paragraph. Vaughan partly argues against a purely chart-based reading (Tufte 1997), which the book's two-sided account already accommodates. She is a good "se tromper autrement" source on the case itself.

---

### 7. Sharpen M1 Tipping Thresholds & Ground Ch. 18.3 Monitoring in SAVI *(Ch. 9, 16, 18)*

* **Where:** Ch. 9.5, Ch. 16.1, and Ch. 18.3 (*historique* & *erreurs injectées*).
* **Original change:** Note Track 1's ~~Z3-proven exact boundaries: M1's non-monotonic $R(p)$ inversion occurs **iff $s + f > 1$**, and~~ in Ch. 16.1's monoculture scenario ($c=60\%$), shared AI beats the `10%` peer baseline **iff** producer error drops below **$p_{\text{crit}} = 6.15\%$**. In Ch. 18.3, cite **SAVI / e-values** (Ramdas et al. 2023) ~~as the anytime-valid statistical engine allowing continuous escape monitoring without optional-stopping inflation~~ *(as a pointer only, see below)*.

> **Verification — PARTLY SUPERSEDED. Severity: minor.**
>
> **Kept: p_crit = 6.151%** (verified symbolically).
> - It uses exactly the book's Table 16.1 parameters: $c = 0.60$, $m = 0.20$, $f = 0.05$, and a peer baseline of $R = 5.569\%$.
> - Under full review ($u = 1$) the break-even is **4.12%**; the original item omits this.
> - **Revised action:** one sentence at `16-angles-morts-collectifs.md:53`, which already says "un gain brut plus modeste sur $P(\text{faux})$ suffirait". It would read something like "en deçà de 6,15 % (4,12 % si chaque alerte est examinée)". Optionally add the line to Table D.6.
>
> **Demoted: non-monotonicity "iff $s + f > 1$".**
> - It is true: $dR/dp$ at $p = 1$ equals $1 - s - f$, and the derivative's numerator is increasing in $p$.
> - It is practically irrelevant. It requires a miss rate below the false-alarm rate, and the decrease appears only at high producer error rates: above ≈ 18% for $s = 0.99, f = 0.02$, and above ≈ 43% for $s = 0.96, f = 0.05$.
> - None of the book's four configurations qualifies ($s + f$ ranges from 0.33 to 0.82).
> - **Revised action:** optional footnote or "si $s + f \le 1$" qualifier on the general claim at `16:59` ("sans le faire monter"), which is strictly true only under that condition. Nothing in Ch. 9.
>
> **Superseded wording: "Z3-proven".**
> - One of the two Z3 checks is vacuous: `verify_m1.py:41–43` adds `s + f > 1` and `1 - s - f >= 0` together, which is unsat regardless of the model.
> - The bypass "theorem" (`verify_m1.py:112–120`) is a tautology.
> - The M3 "proof" (`verify_m3_savi.py:31`) assumes its own conclusion (`pA_z0 == pA_z1`).
>
> **SAVI.**
> - Valid as a pointer for Ch. 18.3: anytime-valid monitoring of an escape rate.
> - **Do not quote the 34.4% power from `RESULTS.md`.** It results from overbetting (λ = 9, about 4× the Kelly fraction). With λ ≈ 2 the same e-process reaches ≈ 99% power after 200 injected errors (anytime type-I error ≈ 3.5%); a fixed-n binomial test reaches 99.9%.
> - The practical lesson worth one sentence in 18.3: distinguishing a 5% from a 15% escape rate for one error class takes on the order of a hundred-plus injected errors of that class.

---

## Appendix — audit notes on the evidence base

**Track 1 (`auto_research/track1_formal/`):**
- The algebra is correct where it matters (p_crit, the derivative at p = 1, Fréchet bounds, the c_eff identity).
- Three "proofs" are vacuous or tautological (item 7), and the copula table is an artifact (item 4).
- `RESULTS.md` labels all rows "PROVED", which overstates what was checked.
- The property tests (`test_track1_properties.py`) only check textbook bounds.

**Track 2 (`auto_research/track2_sim/`):**
- The "Annex D reproduction" in `validation.py` recomputes the book's closed-form formulas and never runs the simulator. Only the N = 1 M1 recovery exercises `engine.py`.
- Policy conclusions are driven by fixed constants (`phi_CFF`, `lambda_F`, `u_0`, `eta_c`, `eta_m`, `tau_H`) that the sweep does not vary (item 5).

**Reproduction of the audit runs:**
- Copy `engine.py` and add three things:
  - `rho_H` (`H_hat = rho_H·D + (1−rho_H)·D' + noise`, with D' an independent Beta(2,3) draw);
  - `no_bypass` (disables `F > B_bypass`);
  - a `phi_CFF` override.
- Then re-run the 4,096-point Sobol design (seed 2026) for `none`, `static_always`, `adaptive_uq` and `adaptive_uq_only`.
- The session copy was written to a temporary scratchpad and is not kept in the repository.

**Housekeeping:**
- `refinement_report.md` links to `research/refinement/...` and `specs_automated_research.md`, which do not exist at those paths (the files live in `refinement/`; the spec file is absent).
- `refinement/01_adversarial_falsifiers.md` attributes the non-native-writer false positives to Liang **2024**; they are Liang **2023**.
