# TODO — potential leads for the monograph (from the swarm-research audit)

**Date:** 2026-11-21. **Basis:** the verified edition of [`monograph_upgrade_sheet.md`](monograph_upgrade_sheet.md) and the fencing [`README.md`](README.md).

**Line numbers** refer to `monographie/chapitres/` on `main` at `4d05d56`. The unmerged `style-pass` branch may shift some lines.

**Status of the book:** it holds in its present form. This list is sharpening, not repair. Only **A1** corrects an actual overreach. Everything else adds scholarly completeness or precision.

**French drafts** below are first wordings for the author. They must go through the style judge before being applied. All figures in them have been checked, either against the book's own parameters or against the sources marked "web-checked" in § C.

---

## How to run this batch

1. **Merge with the whole-book review first.** Fold these items into the open items of `monographie/notes/SYNTHESE_RELECTURE_2026-11-20.md` so the book gets **one** pass. Known overlaps:
   - A2 ↔ `V2-036`: the Knight & Leveson attribution. The "Les auteurs attribuent…" wording is already on `main`; A2 adds the deeper mechanism.
   - A3 ↔ `V2-016` / `V2-012`: the *Challenger* reading in ch. 5 and ch. 6.
   - A5 ↔ `VX-001` / `V4-019`: a Table 16.1 column where risk rises. A5 supplies the numbers.
2. **Bibliography:** add each new reference to `monographie/commun/biblio_a_verifier.bib` with an `averifier` field stating the exact claim made in the text. Check it against the primary source, then move it to `biblio.bib`. Run `make verifier`.
3. **Edit, rebuild** (`make pdf`), and **run the style judge** on the touched chapters.
4. **Consistency pass on the Conclusion** (A12).

---

## A. Revision batch (priority order)

### A1 — Ch. 16.3: state the condition of model collapse · *moderate · the only factual fix*

- **Where:**
  - `16-angles-morts-collectifs.md:90`, after the second Shumailov sentence;
  - key point `16:117`.
- **Why:** the text reports recursive collapse without its experimental condition (each generation replaces the previous data). With accumulation alongside a retained human corpus, error stays bounded. The chapter's argument rests on provenance and severity (`16:86–88`), not on collapse, and is unaffected.
- **Draft (16:90, to append):**
  > Cet effondrement suppose toutefois que chaque génération remplace les données de la précédente : lorsque les textes synthétiques s’ajoutent à un corpus humain conservé au lieu de s’y substituer, l’erreur reste bornée [@gerstgrasser2024]. Le risque durable tient donc moins à la récursion elle-même qu’à la perte de provenance, qui empêche de savoir quelle part du fonds commun garde la trace d’une épreuve du monde.
- **Draft (16:117, end of the bullet):** « … et expose par récursion les générations suivantes de modèles à une dégradation *lorsque les données d’origine sont remplacées plutôt que conservées*. »
- **New reference:** `gerstgrasser2024`.

### A2 — Ch. 8.3: the deeper cause of coincident failures · *moderate*

- **Where:** `08-independance-chaines.md:91`, after « Les auteurs attribuent ce résultat… ».
- **Why:** shared specification is one cause. Eckhardt & Lee show that variation in input difficulty alone correlates failures, even between truly independent teams. Littlewood & Miller show that forced diversity can make the correlation negative. This grounds M1's parameter *c* and transfers directly to LLMs.
- **Draft:**
  > Une raison plus profonde, établie un an plus tôt par Dave Eckhardt et Larry Lee, vaut même sans énoncé partagé : si certaines entrées sont plus difficiles que d’autres pour tout programmeur, des équipes réellement indépendantes échouent plus souvent ensemble que ne le prédit le produit de leurs taux d’échec, parce que leurs défaillances se concentrent sur les mêmes entrées [@eckhardtlee1985]. Bev Littlewood et Douglas Miller ont montré qu’à l’inverse une diversité imposée — méthodes, langages ou outils délibérément différents — peut rendre cette corrélation négative [@littlewoodmiller1989] : c’est la forme rigoureuse d’un comparateur choisi pour se tromper autrement.
- **Optional:** one line in Annex A (A.7, M1) mapping *c* to the difficulty covariance. Keep the formula out of the main text; Track 1's c_eff can be negative, so it is not a "share" without a caveat.
- **New references:** `eckhardtlee1985`, `littlewoodmiller1989`.

### A3 — Ch. 6.4: Vaughan on *Challenger* · *moderate*

- **Where:** `06-detecter-une-erreur.md:123`, the « contresens répandu » paragraph. Possibly also the bullet *Prise en compte* at `06:121`.
- **Why:** Vaughan is the standard reference on the case and is absent from the bibliography. Her account explains the uptake failure and fits the book's two-sided reading.
- **Draft:**
  > La sociologue Diane Vaughan a montré que cette défaillance de prise en compte s’inscrivait dans une *normalisation de la déviance* : vol après vol, l’érosion des joints, d’abord tenue pour anormale, avait été reclassée en risque acceptable, si bien que l’objection de la veille du lancement butait sur une norme que l’organisation avait elle-même déplacée [@vaughan1996].
- **New reference:** `vaughan1996`.

### A4 — Ch. 15.4: measured evidence for Bainbridge's irony · *moderate*

- **Where:** `15-erosion-verifications.md:75`, after the Bainbridge sentences.
- **Why:** the passage rests on Bainbridge 1983 alone. Two recent studies give it measured form: one causal, one observational, and the text must label the second.
- **Draft:**
  > Deux études récentes donnent à cette ironie une forme mesurée. Dans un essai randomisé auprès de près d’un millier de lycéens, l’accès à un assistant conversationnel sans garde-fou a amélioré les résultats aux exercices d’entraînement de 48 %, mais abaissé de 17 % les résultats à l’examen passé sans lui, alors qu’une version conçue pour guider sans livrer la réponse évitait cette baisse [@bastani2025]. En coloscopie, une étude observationnelle multicentrique a relevé, après l’introduction d’une aide algorithmique, une baisse du taux de détection des adénomes lors des examens réalisés sans elle, de 28,4 % à 22,4 % [@budzyn2025] — un indice convergent, non une preuve causale.
- **New references:** `bastani2025`, `budzyn2025`.

### A5 — Ch. 16.1: break-even figure, monoculture reference, optional rising-risk column · *minor (closes `VX-001`)*

- **Where:**
  - `16-angles-morts-collectifs.md:53`, after « un gain brut plus modeste sur $P(\text{faux})$ suffirait à faire monter le risque total »;
  - `16:20` for the reference.
- **Draft (16:53, parenthesis):** « (dans ce jeu de paramètres, le risque sous appariement rejoint celui du contrôle entre pairs dès que $P(\text{faux})$ ne descend qu’à 6,15 % au lieu de 2 %, et à 4,12 % si chaque alerte est examinée) ».
- **Draft (16:20, end of paragraph):** « Jon Kleinberg et Manish Raghavan ont montré, dans un modèle formel, qu’une *monoculture algorithmique* peut dégrader la qualité globale des décisions même lorsque l’algorithme partagé est plus exact que chacun des décideurs pris isolément [@kleinbergraghavan2021]. »
- **Optional fifth configuration for Table 16.1 / D.6**, answering `VX-001` and `V4-019`: *Modèle partagé, gain modeste*, with $P(\text{faux}) = 8\,\%$, $c = 0{,}60$, $m = 0{,}20$, $f = 0{,}05$.

  | Quantity | Value |
  |---|---|
  | Sensitivity $s$ | 32% |
  | VPP | 35.8% |
  | Escape under matching | 88.6% |
  | **Risk under matching** | **7.08%** (peer review: 5.57%) |
  | Escape under full review | 68.0% |
  | **Risk under full review** | **5.44%** (peer review: 2.80%) |

  This requires adding the configuration to `commun/parametres.py` and regenerating the figure and tables.
- **New reference:** `kleinbergraghavan2021`.

### A6 — Ch. 17.1: dependence vs interaction in M2 · *minor*

- **Where:** `17-decisions-sans-appel.md:52`, the last sentence of *Statut de b et limites*.
- **Why:**
  - With fixed marginals, no dependence can push $p_w$ above $p + z$. The independence formula therefore underestimates by at most $p\,z$.
  - The example the book gives is an interaction that changes *p* itself.
- **Draft (replacing « L’indépendance entre $p$ et $z$ … de l’@eq:ch17-risque-reel. »):**
  > L’indépendance entre $p$ et $z$ est en outre une hypothèse simplificatrice, mais ce n’est pas elle qui expose le plus : à probabilités $p$ et $z$ données, aucune dépendance entre les deux causes ne porte le risque réel au-delà de $p + z$, de sorte que l’@eq:ch17-risque-reel ne le sous-estime jamais de plus de $p\,z$. Le danger tient plutôt à l’interaction : si un défaut caché aggrave l’effet des contraintes déjà modélisées (une fissure qui réduit la tenue du mât face aux rafales prévues), c’est l’estimation $p$ elle-même qui devient fausse, et le risque réel peut dépasser largement la valeur de l’@eq:ch17-risque-reel.

### A7 — Ch. 17: decision-theory anchors · *minor*

- **`17:97`.** The text likens the margin *b* to ambiguity aversion and to robustness to model misspecification, without citation. Cite Gilboa & Schmeidler 1989 (maxmin expected utility) and Hansen & Sargent 2008 (*Robustness*).
- **`17:130`.** Cite Arrow & Fisher 1974 for the rule « explorer là où la réponse est peu coûteuse et réversible ». Their quasi-option value is the value of keeping options open when an action is irreversible and learning is possible.
- **Al-Najjar & Weinstein 2009: do not cite as support for verrous.** If anything, they are an objection to *b* (see README).
- **New references:** `gilboaschmeidler1989`, `hansensargent2008`, `arrowfisher1974`.

### A8 — Ch. 12: self-correction and verifier-guided search · *minor*

- **12.4.** Cite Kamoi et al. 2024, optionally Huang et al. 2024, as empirical support for the existing claim. Re-asking a model without an external comparator does not catch *erreurs constantes*. Self-correction works mainly with reliable external feedback.
- **`12:77`, the salience-omission bullet.** Add one sentence. Inference-time search guided by a verifier (Snell et al. 2024; Lightman et al. 2023) does catch reasoning misses, but it succeeds *because* the verifier is a comparator from another source: tests, a proof checker, retrieved text (Ch. 13). P3(a) is untouched.
- **New references:** `kamoi2024`, optional `huang2024`, `snell2024`, `lightman2023`.

### A9 — Ch. 15.3: the equity counterpoint · *minor (new idea from the cross-review)*

- **Where:** the 15.3 Nuance on audited disclosure vs self-declared labels, in `15-erosion-verifications.md` § *La forme ne signale plus le fond*, from `15:40`.
- **Why:** polished prose was always a socially biased signal, penalising non-native writers. Automated AI-text detectors repeat the bias as false alarms. So the collapse of the costly signal is not only a loss. The detector case also illustrates the Ch. 9 false-alarm argument.
- **Exact figures to use:** across 7 detectors on 91 TOEFL essays, the average false-positive rate was 61.22%; 89 of 91 essays (97.8%) were flagged by at least one detector; near-perfect accuracy on US eighth-grade essays [@liang2023].
- **New reference:** `liang2023`.

### A10 — Ch. 15: remaining empirical anchors · *minor*

- **15.4.** Vaccaro et al. 2024: across 106 experiments, human–AI combinations underperform the better of the two on average ($g = -0.23$), with gains on content-creation tasks. This supports the claim that « le modèle rédige, l’humain relit » is not automatically a cross-check.
- **15.2, *signe révélateur* (`15:20`).** Steyvers et al. 2025: longer explanations raise users' confidence without raising accuracy.
- **METR box (`15:35`).** Cite Peng et al. 2023 (+55.8% speed on a greenfield task) or Cui et al. 2025 (+26% completed tasks, concentrated among less-experienced developers) as references for the existing hedge « d’autres outils à d’autres moments peuvent accélérer certaines tâches ». Do not expand the box.
- **New references:** `vaccaro2024`, `steyvers2025`, `peng2023` and/or `cui2025`.

### A11 — Optional precisions · *minor, take or leave*

- **`16:59`** (« sans le faire monter »): strictly true only when $s + f \le 1$ (miss rate at least the false-alarm rate). All four book configurations satisfy it. A footnote, or a qualifier in Annex A, at most.
- **`17:145`** (« Multiplier les verrous sur des actes bénins use la vigilance »): cite Buçinca et al. 2021 (forcing functions cut overreliance but lower user satisfaction) and Rae, Provan, Weber & Dekker 2018 (*safety clutter*).
- **Ch. 5 (P1):** Kennedy & O'Hagan 2001 (model discrepancy in calibrating computer models), the engineering face of P1.
- **Ch. 3 (judging forecasters on rare events):** Lerch et al. 2017. Evaluating forecasts only after extreme events rewards alarmism (the "forecaster's dilemma").
- **Ch. 2 Noyau formel (conformal prediction):** Barber et al. 2021. Exact distribution-free *conditional* coverage is impossible.
- **Ch. 18.3 (*erreurs injectées*):** one sentence on sample size. Distinguishing a 5% from a 15% escape rate for one error class takes on the order of a hundred-plus injected errors of that class. Ramdas et al. 2023 (anytime-valid monitoring) is optional as a pointer.

### A12 — Conclusion consistency pass · *after A1–A10*

- **Empirical thinness.** Reread the Conclusion passage on the empirical thinness of Parts III–IV (*L'échafaudage et ses statuts* and *Ce qui affaiblirait l'argument*, around `99-conclusion.md:5–41` and `:87–101`). Adjust it to the added studies, without overstating them: Part V remedies remain untested.
- **Net-sign tension.** Check that *Le sens de variation du produit… reste à mesurer* (`99:71`) still reads correctly once the 6.15% / 4.12% break-even is in Ch. 16.
- **Optional, on-thesis:** one sentence in *Les comparateurs de l'ouvrage* (`99:103–123`). The external literature pass used to test the book came from the same model families that helped draft it, so its agreement carries little severity (Def. 10). Only its primary-source checks do.

---

## B. Do not do

- **Track 2 rule** ("human checks only on uncertainty, never on stakes"), and any of its numbers (31.1%, 1.30%, 59.5%).
- **Copula figures** for M2, and the claim that verrous are "mathematically forced".
- **"Shadow AI" framing** of friction effects.
- **The full M-open Bayesian toolkit** in the main text (SafeBayes, sandwich covariance, KL tilting). It raises the register beyond the audience.
- **A catalogue of 2025–2026 agent-security tools** (CaMeL, IsolateGPT, AgentSpec, VeriGuard). It dates fast; the book argues « indépendamment de telle génération d’outils ». At most one example in Ch. 14 or 17.3.
- **New formal results in the main text** (non-monotonicity theorem, c_eff formula, Fréchet lemma). Annex A at most.
- **Further literature passes after this batch.** Same-family agreement proves little; see § D.

---

## C. Candidate references for `biblio_a_verifier.bib`

Keys follow the existing style (`authoryear`). **Web-checked** means checked during the 2026-11-21 audit. All other entries come from known primary sources but still need the usual verification, especially pages and volumes.

| Key | Reference | Check |
|---|---|---|
| `gerstgrasser2024` | Gerstgrasser, M., Schaeffer, R., et al. (2024). *Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.* arXiv:2404.01413 | confirm venue and author list |
| `eckhardtlee1985` | Eckhardt, D. E., & Lee, L. D. (1985). A theoretical basis for the analysis of multiversion software subject to coincident errors. *IEEE Transactions on Software Engineering*, SE-11(12), 1511–1517 | pages |
| `littlewoodmiller1989` | Littlewood, B., & Miller, D. R. (1989). Conceptual modeling of coincident failures in multiversion software. *IEEE Transactions on Software Engineering*, 15(12), 1596–1614 | pages |
| `vaughan1996` | Vaughan, D. (1996). *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA.* University of Chicago Press | — |
| `bastani2025` | Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122 | **web-checked** |
| `budzyn2025` | Budzyń, K., et al. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. *The Lancet Gastroenterology & Hepatology* | volume, pages, authors |
| `kleinbergraghavan2021` | Kleinberg, J., & Raghavan, M. (2021). Algorithmic monoculture and social welfare. *PNAS*, 118(22), e2018340118 | article number |
| `gilboaschmeidler1989` | Gilboa, I., & Schmeidler, D. (1989). Maxmin expected utility with non-unique prior. *Journal of Mathematical Economics*, 18(2), 141–153 | — |
| `hansensargent2008` | Hansen, L. P., & Sargent, T. J. (2008). *Robustness.* Princeton University Press | — |
| `arrowfisher1974` | Arrow, K. J., & Fisher, A. C. (1974). Environmental preservation, uncertainty, and irreversibility. *Quarterly Journal of Economics*, 88(2), 312–319 | — |
| `kamoi2024` | Kamoi, R., Zhang, Y., Zhang, N., Han, J., & Zhang, R. (2024). When can LLMs actually correct their own mistakes? A critical survey of self-correction of LLMs. *Transactions of the ACL*, 12 | pages |
| `huang2024` | Huang, J., et al. (2024). Large language models cannot self-correct reasoning yet. *ICLR 2024* | optional |
| `snell2024` | Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). Scaling LLM test-time compute optimally can be more effective than scaling model parameters. arXiv:2408.03314 | venue |
| `lightman2023` | Lightman, H., et al. (2023). Let's verify step by step. arXiv:2305.20050 (*ICLR 2024*) | — |
| `liang2023` | Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns*, 4(7), 100779 | **figures web-checked**; confirm article number |
| `vaccaro2024` | Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour*, 8 | pages |
| `steyvers2025` | Steyvers, M., et al. (2025). What large language models know and what people think they know. *Nature Machine Intelligence*, 7 | pages, N |
| `peng2023` | Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). The impact of AI on developer productivity: Evidence from GitHub Copilot. arXiv:2302.06590 | — |
| `cui2025` | Cui, Z. K., Demirer, M., Jaffe, S., Musolff, L., Peng, S., & Salz, T. (2024/2025). The effects of generative AI on high-skilled work: Evidence from three field experiments with software developers. Working paper (SSRN) | year, venue, exact figure |
| `bucinca2021` | Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proc. ACM Hum.-Comput. Interact.*, 5(CSCW1) | article number |
| `rae2018` | Rae, A., Provan, D., Weber, D., & Dekker, S. (2018). Safety clutter: the accumulation and persistence of "safety" work that does not contribute to operational safety. *Policy and Practice in Health and Safety*, 16(2) | **authors web-checked**; pages |
| `kennedyohagan2001` | Kennedy, M. C., & O'Hagan, A. (2001). Bayesian calibration of computer models. *JRSS B*, 63(3), 425–464 | — |
| `lerch2017` | Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., & Gneiting, T. (2017). Forecaster's dilemma: Extreme events and forecast evaluation. *Statistical Science*, 32(1), 106–127 | — |
| `barber2021` | Barber, R. F., Candès, E. J., Ramdas, A., & Tibshirani, R. J. (2021). The limits of distribution-free conditional predictive inference. *Information and Inference*, 10(2), 455–482 | — |
| `ramdas2023` | Ramdas, A., Grünwald, P., Vovk, V., & Shafer, G. (2023). Game-theoretic statistics and safe anytime-valid inference. *Statistical Science*, 38(4) | optional, pages |

---

## D. Longer-term leads (next edition or companion paper)

### D1 — A small Track 3: measure escape instead of arguing about it · *the only lead with refutation power*

The book's weakest point is the one it states itself: the Part V remedies are untested working hypotheses. Only measurement can move them. A minimal design:

- **Workflow:** one real review flow, e.g. code review of LLM-assisted pull requests, or review of LLM-drafted technical notes.
- **Error class:** one plausible class drawn *from a different frame than the reviewers'* (Ch. 18.3, illusion 1). Examples: a unit mix-up, a silently dropped precondition, a fabricated reference. The seeded errors must be indistinguishable in form from ordinary output (illusion 2).
- **Two arms:**
  - (a) the usual protocol, where the reviewer reads the model's draft first;
  - (b) the book's protocol, where the reviewer writes an expectation first and submits the bare problem neutrally (Ch. 15.4, Ch. 18.1).
  - Optionally (c): an LLM judge from the same family as the producer, to estimate *c*.
- **Measures:** escape rate per arm, false-alarm rate, uptake. These are the M1 parameters *c*, *m*, *f*, *u*, measured rather than assumed.
- **Size:** on the order of a hundred-plus seeded errors per arm to separate a 5% from a 15% escape rate.
- **Pre-registered refutation:** if arm (b) does not lower escape against arm (a), or if same-family review does not raise *c*, report it in *Ce qui affaiblirait l'argument*.

### D2 — Stop after the batch

Once § A is applied and the relecture items are settled, further automated literature passes are unlikely to add evidence: they would mostly be same-family agreement. Reserve effort for D1 and for real readers from the target audiences (engineers, analysts, reviewers). Those readers are comparators that err differently.
