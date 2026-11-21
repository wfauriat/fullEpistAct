# Genesis and Lineage of the Ideas in *Agir d'après une représentation du monde*

**Question.** Which ideas in the 2026 monograph are surely the author's own, and which entered through LLM-written texts or during the build?

**Short answer.**
- **The epistemic and decision core is yours, and most of it predates any LLM involvement.** This covers nearly all of Part I, the substance of chapter 5, the regress argument of chapter 7, the one-shot decision of chapter 17, the stance of humility, and most of the running examples. Nearly all of it is in the 2022 book, the one source certain to be free of any LLM. The winter 2025 talk restates much of it, written by you while LLM chats were already under way.
- **The theory of checks that organises Parts II–V was assembled with the models.** This covers the comparator, the five conditions, the escape probability, the criterion "se tromper autrement", the two-axis matrix and the three-level remedy. Its components are yours. The assembly was first proposed by Claude on 12 Nov 2026 and written up by Claude on 14 Nov 2026.
- **Most mechanisms and case studies were contributed by models and the literature.** This covers Hoare contracts, the jagged frontier, Spence, Bainbridge, sycophancy, severity, injected errors, Mars Climate Orbiter, Knight Capital, Mata v. Avianca and the weld inspection example.

---

## 0. Update of 21 Nov: what the housekeeping archive adds

Source: `miscMD/November_GH_housekeeping/`, the archive of your Nov 2026 housekeeping. It holds the claude.ai export metadata (665 conversations, Nov 2025 → Nov 2026; dates, sizes and titles only), a dated lineage of your notes, and your own provenance answers per artifact on the L0–L4 scale:
- **L0**: hand-written;
- **L1**: mostly or all AI;
- **L2**: AI-assisted training;
- **L3**: AI proposal with heavy human editing (**L3h** when the ideas and formulations are mostly yours);
- **L4**: transcript or summary of a human–AI conversation.

**What is certain.** You can guarantee two things:
- the 2022 book involved no LLM whatsoever, in the thinking or the writing;
- no LLM wrote any of the winter 2025 talk. LLM chat exchanges may still have influenced the thinking behind it: your first claude.ai conversation dates from 7 Nov 2025, the same day as `OverviewNotes.md`.

So only the 2022 book is certain. The talk, the Nov 2025 notes, the seminar and your build prompts are **written by you, in the LLM era**, marked ◉ below. Of the 23 human ideas on the lineage page, 19 already appear in the 2022 book. The other 4 are reasoning backwards, guarantees conditional on choices, the shift to model-free methods, and the book's design.

**How much weight the labels carry.** The L0–L4 labels are your own after-the-fact classification and are coarse. A label records how you see an artifact, not a measurement of who contributed which idea. They are used below as one signal among others: who wrote the text, the dates of first use, and the character counts. Where a classification rests mainly on a label, this section says so.

**Corrections to this report.**
- **The talk** was written by you in late Nov – Dec 2025, with no LLM writing and about 13 h of editing in the file's metadata. Your chats were under way, so its thinking may carry their influence. It was submitted for AI critique on 15 Dec and shown at the possible-worlds seminar on 16 Dec. You class the seminar as L0, with its LLM excerpts quoted openly.
- **The arXiv article** is L3h in your words: "an LLM-written patchwork of several works and discussions, distilled into a heavily editorialised argumentative line", with ideas and even formulations mostly yours. *Precisely Wrong*, *The Perspectival Trap* and the AI_Limits treatise (Jan 2026) are also L3h.
- **The bridge essay** (25 Jul 2026) is L3: drafted by Claude from a source document, with thesis, title, venue and scope confirmed by you.
- **The November essay** *Producing faster than we can check* (3–5 Nov 2026) is **L3h**, signed by you, from a chat with 18 of your turns. So the criterion "a check is worth something only if it can fail differently" first appears in a text whose ideas you claim. This moves that criterion from ○ towards ◐. The *assembly* into the book's thesis remains Claude's (12 Nov).
- **First written uses** of several terms:
  - "precisely wrong": the UQ manifesto, 14 Dec 2025 (chat output);
  - "epistemic humility": an AI answer in the critique of the talk, 15 Dec 2025;
  - "launder": 28 Dec 2025;
  - "frame problem": 16 Jan 2026, from the chat "Limits and perspectives in machine learning advances";
  - "ontological uncertainty": 18 Jan 2026, in the treatise;
  - "bottleneck inversion": coined by an AI map of your corpus, 30 Mar 2026;
  - "the world responds to the action": first in English in *The Perspectival Trap*, 1 Apr 2026. Its French form is in the 2022 book and in your Nov 2025 notes.

**The dialogue years, measured** (export metadata only, no message read):
- **85 % of conversations were deleted after harvest.** Their time still counts in your activity index.
- **The surviving dialogue is mostly model text.** Of the epistemics conversations that kept their text, 8 fall between 14 Dec 2025 and 9 Apr 2026, about 26 h. In them you typed about 65,000 characters and the model wrote about 560,000, so about 10 % of the text is yours, carrying the questions, directions and objections.
- **Activity on the epistemics thread:** about 66 h from Dec 2025 to May 2026, and about 85 h from Nov 2025 to Nov 2026 (chat 44 h, Claude Code 32 h, git 10 h).

**Effect on the ledger.** With the bridge essay counted as mixed, the 46 ideas on the lineage page now split 23 human, 13 mixed and 10 LLM. Three of those mixed rows, and the reclassification of the November essay and the seminar, rest mainly on your labels: the texts themselves were drafted or partly written by a model. Without the labels, the split would be 23 human, 10 mixed and 13 LLM, as first reported.

---

## 1. Sources and How Much Weight Each Carries

| Tier | Source | Date | Who wrote it | Status in this report |
| :-- | :-- | :-- | :-- | :-- |
| **H0** | *Un discours de la méthode au XXIe siècle* (`ManuscritPDFpub.pdf`, 296 pp.) | 2022 | you alone, no LLM | read by full-text search, key pages in full |
| **H1** | `OverviewNotes.md` (UQ position note) | 7 Nov 2025 (git), the day of your first claude.ai conversation | you; LLM era | read in full |
| **H1** | `source/TEDLike_pitch_v2.md` (talk, a 15-min video) | late Nov – Dec 2025 (about 13 h of editing) | you; no LLM writing (guaranteed), thinking possibly influenced by chats | read in full |
| **H2** | `corpora_content.md`, your list of claims | May 2026 (git) | you, in your own words, but after LLM dialogues had started (Dec 2025) | read in full |
| **L3h** | arXiv article `frame_problem_article_WF.tex` | May 2026 | ideas and line yours, prose by Claude (its *Note on production* says so) | searched |
| **L3** | *Where the Guarantees End* (bridge essay) | 25 Jul 2026 | drafted by Claude; thesis, title, venue and scope confirmed by you | searched |
| **L** | Lineage analysis `01_lineage_analysis.md` | 12 Nov 2026 | Claude | read in full |
| **L** | *Failing Differently* | 14 Nov 2026 | "Claude (Anthropic), at the request of W. Fauriat. Exploratory draft, not checked." | searched |
| **B** | Your prompts during the build | 18–21 Nov 2026 | you | read |
| **B** | Specs (`course_specs_draft.md`, `content_spec/`) and chapters | 18–21 Nov 2026 | models (Opus, Gemini) | searched |

**Classification rule.**

| Mark | Meaning | Where the idea first appears |
| :-- | :-- | :-- |
| ● | **Surely yours** | the 2022 book (H0), the only source certain to be free of any LLM influence |
| ◉ | **Yours in writing, LLM era** | the talk or your Nov 2025 notes (H1), with no 2022 trace; you wrote them, but chats were already under way |
| ◐ | **Yours, in your own words, during the LLM era** | H2, or your build prompts |
| ○ | **Co-produced** | first in an LLM-written text made under your direction (L3h or L) |
| · | **Contributed by a model or the literature** | first in the build specs or chapters, with no earlier trace |

**Limits.**
- A concept missing from a source does not prove it came from somewhere else.
- Several texts were used only through their provenance records: *Precisely Wrong*, *The Perspectival Trap*, the November essay *Producing faster than we can check*, and the October letter. For the claude.ai conversations only the export metadata was used (§0); most bodies were deleted, and none was read.
- Searches are keyword-based. Every match cited below was checked in context.
- Page numbers for the 2022 book are its printed pages (PDF page minus 2).

---

## 2. Ledger of Ideas, by Part of the 2026 Book

### Part I: Acting on a Representation (ch. 1–4)

| 2026 idea | Earliest human trace | Verdict |
| :-- | :-- | :-- |
| Boiling water as an imperfect rule, written `A ∩ (…) → B`; salt water, then pressure, as exceptions | **2022, pp. 124–125**: "Cette règle est souvent vraie. Mais pas toujours", salt water, a vessel under pressure, "∩ (eau douce) → B". TED: interns, salt water at 101 °C, pressure cooker at 104 °C, "eau ∩ pure ∩ pression atmosphérique ∩ 100° → ébullition" | ● |
| Conditional probability as a ratio of worlds; "mondes possibles" | **2022, pp. 115, 121, 125**: "Il faut penser en termes de mondes possibles… Pr(B∩A) décrit le poids des mondes…". TED and OverviewNotes | ● |
| Deduction valid "pourvu que…"; the problem of induction (Hume) | **2022, p. 55** ("corrects pourvu que l'on respecte les règles"), **p. 127** (Hume) | ● |
| Pearl's minefield; Russell and Norvig on possible worlds | OverviewNotes ("Idées reprises"); TED. Both works are also in the 2022 bibliography | ● |
| "Raisonner à l'envers" | OverviewNotes; TED | ◉ |
| The guarantee of deduction and of induction is conditional on choices | TED conclusion ("toute garantie est nécessairement conditionnée à des choix"); claims list ("guarantee regimes") | ◉ |
| The world responds to the action, not to the representation | **2022, p. 219**: "« la nature » est indifférente à nos anticipations"; p. 183, "Le réel vient contredire ses anticipations". OverviewNotes and TED: "Le réel se moque de nos anticipations" | ● |
| Law of total probability as the frame for prediction (eq. 2.1) | **2022, p. 227**; OverviewNotes (`Pr(Y)=ΣPr(Y|X)Pr(X)`); claims list | ● |
| The frame as four prior choices; conformal guarantees that stay relative to the frame | claims list (conformal prediction "rests on a framing-level condition"). The four-part definition was formalised in the specs | ◐ / · |
| Probability as judgment; every conclusion is subjective | **2022** (p. 220: "La rationalité d'une décision est bien une propriété subjective"); claims list | ● |
| The sailing race between M. X and M. Y; "who is right? nobody" | **2022, pp. 219–220**: two shipowners, one with a *canoé de sauvetage*, "Qui des deux armateurs « a raison » ? A l'heure du départ : personne". TED: light or reinforced sailboat, M. X at 5 %, M. Y at 1 ‰, 1 in 10,000, towing dearer than the prize. Your build prompt brought it in. You also restored "voilier léger / renforcé" when ch. 0 drifted | ● |
| Satellite phone | claims list ("lifeboat (or a satelite phone)") | ◐ |
| Savage: statistics serves deciding, not only believing | **2022, p. 134**; TED; OverviewNotes | ● |
| Russian roulette; expected utility; the decision threshold | **2022, p. 177** (roulette), **pp. 165–179** (MUE, insurance). TED. Your build prompt asked for the SEU one-shot thread. The formula `p* = ΔU/(ΔU+L)` and the value L/ΔU = 25 were set in the specs | ● (formula ·) |
| Calibration needs repetition; it is of limited use for a single decision | **2022, p. 185**: "La vérification de cette calibration ne peut s'effectuer qu'à posteriori, en répétant la décision. Ainsi, elle est d'une utilité limitée pour la décision unique" | ● |
| Surprise as a gap between expectation and outcome | **2022, p. 185** (utility gap) | ● idea; · log score and proper scoring rules |
| Bayes in odds form; ultrasonic weld inspection | 2022 has Bayes (p. 123 and others). The weld example appears in no earlier source | · |

### Part II: What Can Tell Us We Are Wrong (ch. 5–9)

| 2026 idea | Earliest human trace | Verdict |
| :-- | :-- | :-- |
| Ontological uncertainty: what lies outside the admitted alternatives | **2022, p. 185**, the fève: "pourrait aussi se loger à l'extérieur du gâteau si l'issue qui se manifeste n'a pas été anticipée". The *name* entered in Jan 2026, in an LLM-assisted pass. Your claims list defines aleatory, epistemic and ontological uncertainty in your own words | ● idea, ◐ name |
| The aleatory/epistemic split as a modelling choice (the die example) | **2022, p. 231**: a possibly loaded die, `Pr(Y)=Pr(Y|T)Pr(T)+…` | ● |
| The turkey that reasons by induction | **2022, pp. 182–184** (the turkey is "rationnelle"); TED; claims list | ● |
| P1: an error bar measures only disagreement inside Θ; the law of total variance | the idea follows from the fève and the claims list; the proposition and its proof were built in the specs | ○ / · |
| Common-mode failure; redundancy has a cost | **2022, p. 206**: Igor, "facteurs communs"; Inès, "redondance… facteurs communs de défaillance"; Elias, "Oui, mais cela a un coût". This is about physical and organisational systems, not checks | ● for systems |
| **The frame as the common cause of every internal check (P3)** | claims list: "it cannot audit the frame from within". 2022, p. 260: machines "héritent du cadre qui leur est imposé". Applying common-mode failure to *checks* first appears in the November essay and in *Failing Differently* | ◐ idea, ○ formulation |
| The infinite regress of meta-procedures; no free lunch | **2022, p. 260**: "Formaliser c'est choisir : un cadre plutôt qu'un autre…"; p. 274. Claims list: "choosing just moves the question… to the meta-level". Wolpert–Macready and Goodman's *grue* were added from the literature | ● |
| Two ways in for new relevance: being told, or finding out by trial | claims list: "either, someone told you, or, you bumped into it through exploration". This was first written in an LLM pass (Jan 2026), but the claims list is in your words | ◐ |
| Exploration and its limits | **2022, pp. 215–236**, "exploration statistique" and three limits (mathematical, epistemic, economic) | ● |
| Serial chains accumulate failures | **2022, pp. 242–245**: `Pr(S=1)=∏Pr(Xᵢ=1)`, "plus il y a d'éléments… plus la probabilité de fonctionnement chute"; cascades, p. 245. The 2026 version, about *blind spots of checks*, is new | ● for systems, ○ for checks |
| Blanchiment (laundering) of conditions | claims list: "Stripping uncertainty in long or complex reasoning chains… is risky". The word entered in Dec 2025, in an LLM pass | ◐ |
| **Comparator; the five conditions; escape probability (P2)** | no human-only trace. First appears in *Failing Differently* (Claude, 14 Nov 2026) | ○ |
| **"Se tromper autrement" as the organising criterion** | components are yours (common factors in 2022; "le réel tranche"). The criterion "can fail differently" appears in the July curricula and bridge essay (L3), then in the November essay, which is L3h by your account (§0). The *assembly* as the book's thesis was proposed by Claude on 12 Nov ("[mine; every component is in the texts, the assembly is not]") | ○ |
| Independence trades off against comparability and cost (P4) | the cost side is in 2022, p. 206 (Elias). The comparability trade-off is in *Failing Differently* and the specs | ● partly, ○ |
| Severity (Mayo); base rate and PPV; probability matching; `R = P(E)(1−su)`; M1 | not found in any human-only source | · |
| Challenger; 2008 mortgage models | arXiv article (L3h) | ○ |
| Corroded bracket and safety factor | *Failing Differently* (Claude) | ○ |

### Part III: From Classical Computing to AI (ch. 10–13)

| 2026 idea | Earliest human trace | Verdict |
| :-- | :-- | :-- |
| Machines as formal automata applying our instructions, inheriting our frame | **2022, pp. 63–65, 260** ("Les traitements et les raisonnements délégués aux machines sont en fin de compte nos traitements") | ● |
| Guarantees obtained before execution (the autopilot) | **2022, p. 69**: "Monteriez-vous à bord s'il existait des conditions dans lesquelles l'automate pouvait d…" | ● (weak link) |
| A stack of layers with formal contracts; the top layer gives up the contract to gain reach | your build prompt of 18 Nov describes it in your words. Its first written form is the bridge essay (Jul 2026, LLM) | ◐ / ○ |
| The shift to data-driven, model-free methods; careful model selection replaced by compute | OverviewNotes ("Mouvement vers l'inductif / data-driven / model-free"); claims list | ◉ |
| Hoare contracts; failures with an "address"; the change of regime; the jagged frontier; the hallucination bound | bridge essay (Jul 2026) and the specs | ○ / · |
| **The two-axis matrix (in or out of frame × signalled or silent)** | proposed by Claude in the 12 Nov lineage analysis (§5.2 and §6.2: "Needs a second axis [mine]"), then *Failing Differently*. The cold reader praised the conclusion for "correcting" your preprint on this point; that correction was model-proposed | ○ |
| Four sources of comparators; verification versus validation | *Failing Differently*, specs, Oberkampf & Roy. OverviewNotes has the "modélisation / simulation / validation" triptych | ○ / · |

### Part IV: Automation and Its Blind Spots (ch. 14–16)

| 2026 idea | Earliest human trace | Verdict |
| :-- | :-- | :-- |
| Growing complexity makes reasoning more fragile; automation is spreading | **2022, pp. 241–245**, "Une exploration de plus en plus complexe et risquée"; OverviewNotes ("Augmentation de l'automatisation… délégation de la décision à des agents artificiels") | ● |
| Production outpaces evaluation; resources should go to evaluation | **2022, p. 276**: "diriger d'abord les financements académiques vers les compétences, plutôt que vers les moyens". Claims list: "increase the throughput of automated judgements… a resource allocation issue". "The bottleneck has flipped" (Feb 2026, LLM pass) | ● / ◐ |
| Automation produces opacity and erodes reflexivity | claims list | ◐ |
| Agents as formal systems whose frame is a choice | claims list; 2022, p. 274 ("formaliser c'est déjà choisir… L'agent réel, humain ou machine") | ● / ◐ |
| Signe révélateur; costly signal (Spence/Akerlof); Bainbridge; sycophancy; prêteur unique; blanchiment de provenance; model collapse | not found before the LLM-written texts and the build | ○ / · |
| METR, BCG, Knight Capital, Google Flu Trends, Mars Climate Orbiter | bridge essay (Jul 2026) | ○ |
| Mata v. Avianca | specs (build) | · |

### Part V: Deciding and Protecting Ourselves (ch. 17–18, conclusion)

| 2026 idea | Earliest human trace | Verdict |
| :-- | :-- | :-- |
| The attitude: humility, critical thinking, not "chasing the right answer" | **2022** (manifesto, p. 275: "Faisons preuve d'humilité, d'un regard ouvert et d'esprit critique"); TED ("mieux vaut ne pas trop courir après la bonne réponse"); OverviewNotes (values) | ● |
| The marge d'humilité *b* | claims list: "an uncertainty buffer… an 'and what if we're missing something' branch". The parameter *b* in M2 and the four quadrants were built in the specs | ◐ idea, · model |
| Calibrate what repeats; lock what happens once | **2022, p. 185** (calibration of limited use for the single decision) | ● |
| Bac à sable: explore where the answer is cheap and reversible; verrou at the irreversible boundary | **2022, p. 185**: calibrate "par la simulation – dans le monde virtuel, sans conséquences". Claims list: "Exploration is not acceptable… damage… irreversibility of consequences". "Gate the action" in the bridge essay (Jul 2026) | ● / ◐ |
| The "ingénieur qualité" who checks other people's reasoning without their expertise | OverviewNotes | ● (it returns weakly as "who reads the layer underneath") |
| The three-level remedy (attitude, placement, organisation) | attitude: yours (2022). Placement: bridge essay. Organisation: November essay. The *three layers* were assembled by Claude on 12 Nov (§6.5, "attitude for the author, placement for the system, rules for the organisation") | ○ |
| Injected errors (TIP, mutation testing); the four questions; the five pre-action questions | specs and chapters | · |
| A working approach rather than a prescription; *faute de mieux*; a status for each claim; self-critique; the book "judged by what it says" | **your build prompt of 18 Nov** (L1–L4: "honest to acknowledge a working hypothesis from a claim backed by more evidence", "explicit and self-critical on the principle it preaches", "judged by what it says"). OverviewNotes: "pas de solution formelle, que des dispositions" | ◐ |

### The Book's Design

These all come from your build prompts (◐):
- the domain split: epistemic / computing stack / automation / decision, risk and verification;
- "keys" introduced before the core claims ("forger les clés avant d'aborder les serrures");
- examples before formalism;
- an introduction that covers the whole scope;
- quantitative examples treated like derivations;
- *Points clés* at the end of each chapter;
- the provenance rule;
- practice first, with formality as a means.

The block types, the reading paths and the five epistemic statuses were then formalised by the models (·).

---

## 3. Verification of `style/COMPARAISON_2022_2026.md`

That comparison was written by Claude on 20 Nov at 12:45, against the PDF as it stood *before* the style pass and the whole-book edit passes.

### 3.1 Conceptual Claims

| Claim | Verdict |
| :-- | :-- |
| Quotes in table 2.1 ("souvent vrai, mais pas toujours"; "qui a raison ? personne"; "Formaliser c'est choisir… elles héritent du cadre qui leur est imposé"; "Diriger les financements vers les compétences plutôt que vers les moyens") | **Confirmed** (pp. 124, 220, 260, 276). The "lifeboat" is a *canoé de sauvetage* |
| Calibration needs repetition (footnote 68) | **Confirmed** (p. 184, note 68; p. 185) |
| "Exploration statistique" → sandboxes | **Confirmed**, and stronger than stated: p. 185 already speaks of calibrating "par la simulation – dans le monde virtuel, sans conséquences" |
| Igor and Inès on common failure factors = the seed of the central mechanism | **Nuanced.** The 2022 passage is about *physical and organisational systems*, not checks. The "seed" is also not a single exchange: the series-reliability product and the cascades (pp. 242–245) carry the same idea. The transposition to *checks of reasoning* came later, through LLM-written texts |
| From a virtue (2022) to an architecture (2026) | **Confirmed.** The architecture was assembled with the models (§2) |
| What aged ("ne vont pas collecter spontanément", "hors de portée des machines", "finiront par se retrouver déçus") | **Confirmed** (pp. 253, 265, 263) |
| "Rationalité" 91 → 1; "subjectiv*" 62 → 20 | **Confirmed** within counting method: 95 → 1 and 63 → 25 on today's PDF. Allais and Ellsberg are each mentioned once in 2022 (p. 216) |
| Exploration as an economic decision lost | **Confirmed.** 2026 frames exploration by the *cost and reversibility of the world's answer*, not as investment against expected gain (2022, p. 236) |
| The fève is the best image of ontological uncertainty | **Confirmed.** It is still absent from 2026 |
| "À la portée de tous" | **Confirmed** |

**What the comparison missed** from 2022:
- the loaded-die decomposition (→ ch. 5);
- the series-reliability product (→ the chains of M1);
- Elias's remark on cost (→ P4);
- "la nature est indifférente à nos anticipations" (→ ch. 2);
- `A ∩ (…) → B` written out as notation (→ eq. 1.1);
- "pourvu que" (→ ch. 1);
- Hume and Savage;
- the remark on calibration for "la décision unique" (→ ch. 17).

### 3.2 Style Measures

| Measure (per 10,000 words) | Comparison (2022 / 2026) | Recount (2022 / 2026 today) | Verdict |
| :-- | :-- | :-- | :-- |
| Mean sentence length | 19.7 / 33.5 | 18.5 / 27.7 | direction confirmed; values depend on method |
| Sentences > 40 words | 5 % / 26 % | 3 % / 20 % | same |
| « » | 163 / 16 | 144 / 18 | confirmed |
| ; | 3 / 45 | 2.9 / 39.7 | confirmed |
| : | 35 / 123 | 34 / 108 | confirmed |
| ( | 37 / 186 | 37 / 200 | confirmed |
| ? | 42 / 33 | 37 / **12** | **2026 value was wrong**: inflated by the 169 unresolved citation markers ("?") in that PDF |
| nous / je | 73 / 31 vs 12 / 0.5 | 66 / 30 vs 9 / 0.4 | confirmed (the 2026 "je" are quotations) |
| "Or" opening a sentence | 0.2 / 3.0 | 0.3 / 1.3 | 2026 has dropped since: sentence-initial "Or" fell from 28 to 16 in the chapter sources after 19 Nov (style pass and edit passes) |

- **Typos in 2022:** all eight slips quoted are present, once each.
- **Bibliography:** "about 25 in 2022" is confirmed (about 23 entries). "About 100 in 2026" is stale: the verification pass left 69 verified entries, 41 of them cited.
- **Page count:** the 2026 book now has 277 pages, not 264.

### 3.3 Production Defects (§4 of the Comparison)

All are fixed in today's PDF:
- no "Figure à générer" placeholder;
- no "au section";
- no broken "Vos propres contrôles" reference;
- no unresolved ")?" citation markers.

The running header was not re-checked.

### 3.4 Status of the Comparison's Recommendations

| Recommendation | Status |
| :-- | :-- |
| 1. Bring back the fève | not done |
| 2. Exploration as an economic decision | not done |
| 3. First-person voice in the conclusion | not done (no "je" in the author's voice) |
| 4. Shorter sentences | partly done (style-pass splits) |
| 5. Vary the chapter rhythm | not checked |
| 6. Fix defects | done |

---

## 4. What You Can Claim, and How

**Surely yours, with documentary proof that predates any LLM** (the 2022 book):
- acting on a representation;
- imperfect rules and the unstated "(…)";
- probability as weight on possible worlds;
- subjectivity;
- calibration that needs repetition, hence the problem of the single decision;
- the threshold logic of roulette and the shipowners or sailboats;
- outcomes left out of the cake (ontological uncertainty);
- formalising as choosing, hence the regress;
- exploration and its limits;
- common failure factors and chains in systems;
- complexity and automation as rising risk;
- funding competence over means;
- the attitude of humility.

**Written by you in the LLM era, without LLM writing** (the winter 2025 talk and the Nov 2025 notes):
- reasoning backwards;
- every guarantee being conditional on choices;
- the shift to model-free methods;
- the talk's restatement of many 2022 ideas, such as the sailboats with M. X and M. Y, Pearl's minefield, and "le réel se moque de nos anticipations".

**Yours in your own words, during the LLM era** (claims list of May 2026, build prompts):
- the uncertainty buffer;
- refusing exploration where it is irreversible;
- being told or finding out by trial;
- the frame that cannot be audited from within;
- uncertainty stripped along chains;
- throughput against evaluation;
- opacity;
- the stack with contracts and the top layer that gives them up;
- the whole design and stance of the book.

**Co-produced** (first written by an LLM under your direction):
- the theory of checks: comparator, five conditions, escape probability, "se tromper autrement" as the thesis;
- the two-axis matrix;
- the three-level remedy;
- the computing-stack analysis;
- several case studies.

The key assembly happened in two Claude texts of 12 and 14 Nov 2026. The second is labelled "exploratory draft, not checked".

**Contributed by models and the literature:** most formal apparatus (severity, PPV, probability matching, M1–M3 as written, Hoare), most mechanisms of Part IV, the injected errors, and examples such as the weld inspection and Mata v. Avianca.

**Two observations.**
1. The 2026 book's thesis turns your 2022 *system-level* reliability intuitions into a theory of *checks on reasoning*. That transposition is the main thing the models added, and it is assembled from your parts.
2. The *Genèse et responsabilité* section of the preface is accurate but general. This map could make it specific, if you wish: the 2022 continuity is already claimed in the article's *Note on production*.

---

*Method: full-text search of the 2022 book (`pdftotext`) and of today's 2026 PDF, with every match checked in context; the human-written notes read in full; the LLM-era texts searched; your prompts taken from the session logs. 2022 page numbers are printed pages.*
