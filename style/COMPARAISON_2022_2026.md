# Comparing the two books: 2022 (author alone) and 2026 (author working with LLMs)

- **2022**: *Un discours de la méthode au XXIe siècle — Risques et limites de l'« intelligence artificielle »*. Written and researched by the author alone, with no LLM involvement (`ManuscritPDFpub.pdf`, 296 pp.).
- **2026**: *Agir d'après une représentation — Cadre, contrôles et décision, de l'informatique classique à l'IA*. The author's ideas and references, developed in dialogue with LLMs, with much of the text drafted automatically (`monographie/build/livre-ecran.pdf`, 264 pp.).

**What was read.**
- 2022: preface, prologue, the opening of Part I, the probability and risk chapters of Part II, all of Part III and the manifesto.
- 2026: front matter, chapter 0, chapter 7, chapter 15 and the full conclusion.
- Not every page was read. The word, sentence and punctuation counts below cover the full text of both books.

---

## 1. Short answer

The 2026 book is a direct continuation of the 2022 book. Most of its examples and core intuitions already appear in the 2022 text. The 2026 version has the stronger argument: narrower, more original, and better able to survive the progress AI has made since 2022.

The 2022 book is livelier and more personal. It ranges more widely in philosophy and is easier for a general reader. The 2026 prose is more precise, but it speaks in one uniform voice. Chapter 15 of the 2026 book describes exactly this effect as a risk of model-generated text, and the book partly compensates for it in its own pages.

---

## 2. The conceptual core

### 2.1 What carries over

Most of the starting points of the 2026 book are already in the 2022 text.

| 2022 | 2026 |
|---|---|
| "L'eau entre en ébullition à 100 °C… souvent vrai, mais pas toujours" | the unstated background `A ∩ (…) → B` (ch. 0, 2) |
| Russell's turkey | the turkey that reasons by induction (ch. 0, 3, 5, 13) |
| Russian roulette, the maximum-expected-utility (MUE) rule, insurance | the decision threshold `gain/(gain+perte)` (ch. 0, 4) |
| Two shipowners and the lifeboat ("qui a raison ? personne") | the sailing race of M. X and M. Y (ch. 0, 3, 4, 17) |
| Surprise as the gap between expected and actual utility; calibration needs repetition (footnote 68) | the logarithmic surprise score; "calibrer ce qui se répète, verrouiller ce qui ne se joue qu'une fois" (ch. 1, 3, 17) |
| "Formaliser c'est choisir… elles héritent du cadre qui leur est imposé" | the frame as a common cause of every check; the infinite regress of meta-procedures (ch. 7) |
| "Exploration statistique" | "découvrir par l'épreuve", sandboxes (ch. 7.5, 17.3) |
| Igor and Inès on "redondance… facteurs communs de défaillance" (Part III) | **common-mode failure, the central mechanism of the 2026 book** (ch. 7, 8) |
| "Diriger les financements vers les compétences plutôt que vers les moyens" | independent evaluation as its own budget line (ch. 16.4, 18.3) |

The seed of the 2026 core is a single exchange between two students in Part III of the 2022 book. That says a lot about where the ideas came from.

### 2.2 The real shift: from a virtue to an architecture

- **2022 is about the reasoner.** Rationality is necessarily subjective ("le risque est relatif à l'observateur"). The remedy is an **attitude**: humility, critical thinking, and human "intelligence subjective".
- **2026 is about the system.** The question becomes an engineering one: *which comparator can contradict me in time, and does it make mistakes differently from me?* The book states five conditions a check must meet and introduces the probability that an error escapes every check (*probabilité d'échappement*). It shows how errors build up along chains, how parallel cross-checks reduce them, and how a shared frame disables every internal check at once.

The attitude survives, but only as level 1 of 3, and the book says explicitly that it is not enough on its own ("Limite structurelle et nécessité collective").

The 2026 book also takes apart the remedy the 2022 book relied on implicitly, "keep a human in the loop". Under the 2026 analysis, a person only counts as a check if they form their own judgement before reading the machine's output (Bainbridge's irony, ch. 15).

This is a real conceptual advance, not a rewording.

### 2.3 What aged in 2022

The weakest claims in 2022 are the ones about what machines cannot do:

- "Les machines ne vont pas collecter spontanément des informations de leur propre initiative, ni s'attaquer à des questions nouvelles…"
- Intuition and intention as "hors de portée des machines".
- The prediction in the manifesto: "tous ceux qui le pensent finiront par se retrouver déçus."

The 2026 argument needs none of these. It still holds if the models are very capable, because it rests on structure rather than on capability:
- a comparator borrowed from the same model does not make different mistakes;
- a frame shared by the producer and the checker fails both at once;
- a factor can be present in a model's representation yet never used (*omission de saillance*).

The 2026 book also states which observations would weaken it ("Ce qui affaiblirait l'argument"). The 2022 manifesto makes a prophecy instead. This is the biggest difference in epistemic maturity between the two books.

### 2.4 What was lost between 2022 and 2026

- **The vocabulary of rationality.** "Rationalité" appears 91 times in 2022 and once in 2026. "Subjectiv*" drops from 62 to 20. The 2022 discussions of normative versus descriptive rationality, the Allais and Ellsberg paradoxes, and the subjectivity of preferences are mostly gone.
- **Exploration as an economic decision.** In 2022, deciding whether to learn more before acting is a cost-versus-gain trade-off: the "third limit, economic", with exploration framed as a sub-problem of the decision. As far as I read, 2026 treats exploration mainly as a safety question (sandbox or lock).
- **The fève image.** "Remarquez que celle-ci pourrait aussi se loger à l'extérieur du gâteau si l'issue qui se manifeste n'a pas été anticipée." This one sentence captures ontological uncertainty better than anything in chapter 5 of the 2026 book, and **it should go back in**.
- **Reach.** The 2022 book is written for everyone ("à la portée de tous"). The 2026 book is written for engineers, analysts and institutions. The narrower audience is a deliberate choice, but it has a cost.

---

## 3. Style

### 3.1 Measures (per 10,000 words)

| | 2022 | 2026 |
|---|---|---|
| Body text, in words | ~65,000 | ~98,000 |
| Mean sentence length (words) | 19.7 | 33.5 |
| Sentences longer than 40 words | 5 % | 26 % |
| Guillemets « » | 163 | 16 |
| Semicolons | 3 | 45 |
| Colons | 35 | 123 |
| Parentheses | 37 | 186 |
| Question marks | 42 | 33 |
| "nous" / "je" | 73 / 31 | 12 / 0.5 |
| "Néanmoins" / "Ainsi" / "il est bon de" | 6 / 6 / 3 | 0 / 0.2 / 0 |
| "non… mais", "non pas" constructions | 1.7 | 6.8 |
| "Or" opening a sentence | 0.2 | 3.0 |
| Vocabulary richness (MATTR, 1,000-word window) | 0.444 | 0.460 |

Notes:
- The 2026 sentence length is somewhat inflated by lists and tables in the extracted text. The prose chapters read in full (ch. 0, 7, 15) confirm the gap.
- Many of the 2026 parentheses are citations and section references.

### 3.2 The 2022 book

**Strengths**
- A personal, committed voice in short sentences, with many rhetorical questions and an advisory register ("il est bon de").
- The fictional frame gives the book a pace and a human stake: Professor Seracost, six students, a supercomputer to share, a manifesto to write.
- The teaching images work well: the cake, the stone throw divided into zones, the fève, the turkey.
- The manifesto has an energy that the 2026 book never reaches ("Investissons dans l'intelligence humaine… Ne misons pas tout sur la puissance de calcul").

**Weaknesses**
- **Overused guillemets.** They show you holding terms at a distance ("rationnel", "juste", "intelligence"). That is a real signature, but at 163 per 10,000 words it loses its force.
- **Stiff dialogue.** The characters are mostly mouthpieces ("répondirent-ils à l'unisson").
- **Repetition.** For example, "C'est l'intelligence humaine qui…" four times in a row.
- **Visible slips.** "UN DISOURS" on the title page, "orientât", "c'est-à dire", "Il est n'est pas", "Précisions maintenant", "butter", "le l'important".

### 3.3 The 2026 book

**Strengths**
- Precise, carefully qualified claims, with consistent terms: one French word per concept, glossed on first use, such as *vleu* for *grue*.
- A strong mix of sources: Mars Climate Orbiter, *Mata v. Avianca*, the METR study, Challenger, Google Flu Trends; Spence, Akerlof, Bainbridge, Wolpert–Macready and Goodman. The bibliography has about 100 entries, against about 25 in 2022.
- An explicit epistemic status on each claim, and a conclusion that applies the method to the book itself.

**Weaknesses**
- **Long sentences.** About a quarter run past 40 words.
- **Dense cross-references**, e.g. "(section 6.2, proposition 2, définition 5)". In places the scaffolding shows through the text.
- **The same rhythm in every chapter:** recap of earlier results, proposition, a "Nuance et discussion ouverte" box, "Question à se poser", "Points clés".
- **Recurring tics:** antitheses balanced on a semicolon ("La forme est toujours là ; elle a simplement cessé d'échouer lorsque le fond s'effondre."), short closing aphorisms ("La défaillance avait une adresse." / "ce n'est qu'un miroir."), and frequent "non X, mais Y".
- **Length.** The book is about 50 % longer than the 2022 one, without the narrative.

### 3.4 The irony, which the book half-handles

Chapter 15.2 argues that a language model speaks with "l'uniformité parfaite de sa voix" and so erases the visible sign of doubt. Chapter 15.3 argues that a polished form no longer signals that the substance is sound.

The 2022 book is full of exactly those signs: hesitations, repetitions, typos, places where you can tell the author is less sure. The 2026 book has none of them. By its own argument, the reader therefore loses a cue for where the reasoning is weakest.

The book compensates with **explicit disclosure**:
- an epistemic status for each proposition;
- a table of each claim's weakest point;
- a list of what would weaken the argument;
- a declared provenance, plus the warning that "la tenue du texte ne prouve rien sur son fond".

This is exactly the "divulgation crédible" remedy from chapter 15, so the book applies its own method, which is coherent and to its credit. The cost is that the text reads more like an audited report than like a person thinking.

---

## 4. Production defects in `livre-ecran.pdf`

Page numbers are the printed ones; add 12 to get the PDF page.

| Defect | Where |
|---|---|
| **169 unresolved citation markers**: citations print with a trailing "?", e.g. "(Becker et al. 2025)?" | throughout |
| **10 missing figures**: the "Figure à générer" placeholders are still in the PDF | pp. 7 (fig. 0.1), 13 (fig. 0.2), 27, 31, 67, 71, 76, 86 (fig. 7.1), 156, 226 |
| **Wrong gender agreement**: "au section" | p. 85 ("présentés au section 0.7"), p. 205 |
| **Broken cross-reference**: "un constat de la Vos propres contrôles : l'effacement par défaut…" | p. 181, opening of ch. 15 |
| **Wrong running header**: the conclusion pages carry "18 Un remède à trois niveaux" | pp. 231–242 |

---

## 5. Recommendations

1. **Bring back the fève** in ch. 5 (ontological uncertainty), and possibly in ch. 0.3.1.
2. **Restore exploration as an economic decision**, i.e. the value of learning more before acting, next to the safety framing (sandbox or lock) in ch. 7.5 and 17.
3. **Let the 2022 voice back into the conclusion**: a few direct, first-person sentences. The manifesto is the right tone to borrow.
4. **Shorten the sentences.** Split those over 40 words, and cut the inline cross-references in the prose, keeping them in the chapter openings and the "Points clés".
5. **Vary the chapter rhythm**, for example by not closing every chapter with both "Question à se poser" and "Points clés".
6. **Fix the production defects** in section 4.

---

## 6. Overall

> The 2026 book is the better argument. The 2022 book is the better read, and has more of the author in it.
