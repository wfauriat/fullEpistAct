# Lookback: How *Agir d'après une représentation du monde* Was Built

**Scope.** This report covers the build of the monograph, from the first agent prompt (18 Nov 2026, 08:38) to the last commit (21 Nov 2026, 09:29). It looks at the amount of work, the time taken, how the work was organised, how agent sessions and agent swarms were used, and how much compute was spent, measured in tokens.

**Sources.**
- The git history of this repository: 61 commits on all branches.
- The Claude Code transcripts in `~/.claude/projects/-home-ai-user-Documents-Sandbox-review-epist-ag*` (57 JSONL files, subagents included).
- The Gemini / Antigravity CLI stores in `~/.gemini/antigravity-cli`: `history.jsonl`, `conversation_summaries.db`, and the per-conversation `conversations/*.db`, whose binary `gen_metadata` usage records were decoded.
- The project's own logs: `monographie/notes/`, `style/`, `relecture/`, and the memory files.

All times are local time (CET). Claude transcripts are stored in UTC and were converted.

---

## 1. Key Figures

| | |
| :-- | :-- |
| **Elapsed time** | about 73 h, from 18 Nov 08:38 to 21 Nov 09:29, over 3.5 calendar days |
| **Logged agent activity** | about 29 h. This is the union of all session intervals, with the overnight idle time removed. A cloud work block on 19 Nov is not included (§7) |
| **Time to a full first draft** | **7 h 22 min** for all 21 chapter files, from Part 0 to the conclusion (18 Nov 17:01 → 19 Nov 00:23) |
| **Commits** | 61 on all branches: 37 on `main`, plus the `style-pass` and `relecture-livre` branches. About 145,000 lines inserted |
| **Final product** | 277-page PDF (also HTML and DOCX); 21 chapter files, about 102,000 words of Markdown source; 5 part introductions; 4 appendices; 36 figures; 13 generated tables; 69 verified references; a register of 64 terms and 15 symbols. Two derived slide decks (a 3-hour deck of about 50 slides and a short deck of about 19) |
| **Process documentation** | 97 files in `monographie/notes/` (about 350,000 words, roughly 3.4 times the length of the book), plus `relecture/`, `style/`, and 43,000 words of specs |
| **Top-level agent sessions** | 28 working sessions: 12 Claude Code and 16 Antigravity. In addition, 7 Claude sessions were opened only for `/usage` or `/model` |
| **Subagent runs** | **84** in total: 38 Claude and 46 Gemini/Antigravity |
| **Models** | Claude Opus 5.5, Claude Sonnet 5.5, Gemini 4 Hydrogen (Low to XHigh), Gemini 4 Argon (Low to High) |
| **Model calls (API turns)** | **≈ 3,410**: 1,309 Claude and 2,102 Antigravity |
| **Input tokens processed** | **≈ 686 M**, of which about 95 % came from the prompt cache |
| **Output tokens** | **≈ 6.3 M**, reasoning and tool-call payloads included. That is about 38 times the token length of the finished text |
| **Author prompts** | about 132 substantive prompts (59 to Claude, 73 to Gemini). On top of that: 81 `/usage` checks, 17 `/context`, 14 `/model` and 8 `/remote-control` commands on the Gemini side alone |

---

## 2. What Came Before the Build (Not Measured)

The build turned material that already existed into a book. That material was written by a person; agents built on it but did not create it:
- the author's arXiv article (`source/frame_problem_article_WF.tex`, cited as `[@fauriat2026frame]`);
- two essays: *Failing Differently* and *Where the Guarantees End*;
- a talk (`TEDLike_pitch_v2.md`);
- an interactive "decision map" built with Claude in earlier sessions.

All of this came out of a research line the author had pursued for several months. A book the author wrote alone in 2022, with no LLM involvement, served as a comparison point for style (`style/COMPARAISON_2022_2026.md`).

None of this earlier work is counted in the figures above. The token figures measure turning existing ideas into a book, not producing the ideas.

---

## 3. Timeline by Phase

### Phase A: Ideation, Critique and Locked Specs (18 Nov, 08:38–16:27)

| Time | Agent | Work |
| :-- | :-- | :-- |
| 08:38–10:42 | Gemini Argon (High) | Critique of the "trilogy" (article and two essays). A French interactive map modelled on an earlier artifact. A suggested new thread on one-shot decisions under subjective expected utility (SEU) |
| 10:34–13:05 | Claude Opus | Answer to the cross-model critique. Removal of traces of "the author's talk" |
| 13:07–16:23 | Claude Opus (163 calls, the longest session of the project) | Interactive map v2 and its idiomatic French version, checked visually with Puppeteer. A critique of `course_specs_draft.md`, which Gemini had drafted, with the two models critiquing each other until **option D** was agreed. Then, in order: `authoring_conventions.md`, `course_outline.md`, `content_spec/` (7 Part files), `BUILDER_START_HERE.md`, the `monographie/` tree (LaTeX template, Lua filter, Makefile, verifier), the terminology register and the bibliography skeleton |
| 13:18–16:24 | Gemini Hydrogen (High) | Extraction of the map's structure. A discussion of the course design, in which the author fixed the provenance rule ("no mention of any previous document… the only reference on my material is the arXiv article") |

First commit at 16:27: 115 files and 34,000 lines, all of it specs, critiques and the HTML artifacts.

**What mattered:** the locked spec stack. It fixed the precedence between documents, the hard rules, terminology owned by one chapter each, statuses fixed per proposition, generated numbers, and `make verifier`. This is what later let models from two vendors write chapters in parallel without the book drifting apart.

### Phase B: Drafting and First Re-reads (18 Nov 16:37 → 19 Nov 06:49)

The working pattern was **Gemini drafts, Opus re-reads and edits**, chapter by chapter at first, then Part by Part through swarms.

| Commit time | Part | Drafted by | Re-read by |
| :-- | :-- | :-- | :-- |
| 17:01 | Preface + ch. 0 | Gemini Argon (High) | Claude Opus (17:36–17:54) |
| 17:35 / 18:03 / 18:20 / 18:46 | ch. 1 / 2 / 3 / 4 | Gemini Hydrogen (XHigh), one session per chapter (15–25 min each) | ch. 1: Opus session; ch. 2–4: **3 parallel Opus subagents** (18:52–19:07), then a full Opus re-read of Part I (20:08 commit) |
| 20:49 | Part II (ch. 5–9 + introduction) | **Antigravity orchestrator** `b465800e` running 5 + 1 Hydrogen (XHigh) subagents in parallel | an Opus "relecteur" subagent running *inside Antigravity* (the 30 Claude calls on the Gemini side), then Hydrogen |
| 22:09 | Part III (ch. 10–13) | Hydrogen (XHigh) batch, same orchestrator | an Argon (High) "relecteur-p3" subagent |
| 23:36 | Part IV (ch. 14–16) | Hydrogen (XHigh), "just one for now, as usage limit draws near" | Claude Opus session (23:36–23:54) |
| 23:53 | Part V (ch. 17–18) | Hydrogen (XHigh) batch | **2 parallel Opus subagents** (23:58–00:22): one re-reads and harmonises Part V, the other **writes the conclusion** |
| 23:04–23:36 | Part introductions | — | Claude Opus, rewriting phrasing that read like English |

That evening, the Antigravity orchestrator alone ran **21 subagents** over 3 h 40 min. It also ran a low-cost "monitor" agent that watched the others.

Between 06:38 and 06:57 the next morning, Opus made small corrections across the book and added a TODO to the outline.

### Phase C: Cold Reads and Arbitration (19 Nov, cloud clone)

The 16:57 commit `7afa571` reads "many edits done in clone environnement": 94 files and about 14,000 lines. It contains:
- **one fresh, isolated read per chapter by Opus and another by Sonnet**: `LECTURE_FRAICHE_{Opus,Sonnet}_chNN.md` for 20 chapters, plus readings of the part pages;
- the lists of points to decide: `A_TRANCHER_*`, `SYNTHESE_A_TRANCHER.md` and `DECISIONS_SYNTHESE.md`;
- the edits made from them (`EDITS_*`).

No local transcript of this work exists in either store. It presumably ran as a cloud or remote session, and its compute is **not counted** (§7). At 17:27, a Gemini Hydrogen session read only the rendered PDF and wrote a whole-book review, presumably `REVIEW_PASS_LIVRE_ECRAN.md`.

### Phase D: Automated Style Pass (20 Nov, 10:10–14:25)

1. **Diagnosis.** Claude Opus compared the 2026 text with the author's 2022 book (`style/COMPARAISON_2022_2026.md`). Gemini, separately, wrote `STYLE_PASS_SPEC.md` and rewrote ch. 0 as a pilot.
2. **Pilot failure.** A diff showed the pilot had rewritten **82 % of the sentences** and changed the meaning about 20 times. Spec v3 replaced free rewriting with small, bounded edits.
3. **Pipeline.** This was the first cross-vendor setup run automatically, in one folder on branch `style-pass`:
   - Gemini (`f92e6c2d`) writes `style/lots/<ch>/propositions.yaml`;
   - Claude watches for new lots with `veilleur.py`;
   - a mechanical re-check runs;
   - a **fresh Opus `juge-style` agent** judges each chapter at high effort;
   - `appliquer_edits.py` applies the accepted edits deterministically;
   - `make verifier` runs;
   - each chapter gets its own commit.
4. **Calibration before trust.** Before the run, the judge was tested:
   - it rejected **30 of 30** known meaning drifts;
   - it accepted 7 of 8 edits that were truly faithful;
   - it also rejected 7 of 8 pilot edits first labelled "faithful", and on inspection 6 of those really did lose some nuance.
5. **Run.** 21 chapter commits between 13:19 and 13:33 (14 minutes): **83 edits applied, 39 rejected**. The result was squash-merged as `24702a9`.

The author chose to stay out of the loop at this stage and planned one full human reread at the end instead.

### Phase E: Arbitration, Bibliography and Calques Audit (20 Nov, 13:55–16:13)

- **Arbitration swarm** (Antigravity `3f38c297`, 6 subagents):
  - roles: `editeur-p0-p2`, `editeur-p3-p5`, `biblio-check`, `artefacts-p4`, `verificateur` and `monitor`;
  - while it ran, the author asked the orchestrator to lower effort as quota ran short ("dial down effort on verificator and monitor, move to hydrogen on editors");
  - result: commit `c8acb4f` (67 files, 35,000 lines), which applied the P1–P2 arbitrations, generated the P4 artefacts and appendices, and promoted the verified references. `159f951` then fixed the remaining facts and emptied `biblio_a_verifier.bib`;
  - the author kept `ARBITRAGES_RESTANTS.md` "as a testimony".
- **English-calques swarm** (Antigravity `087dfb52`, 10 subagents):
  - roles: 6 Part readers, `verifier-prose`, `verifier-fig`, `figures` and `monitor`;
  - output: a **report only**, `RAPPORT_AUDIT_CALQUES.md`. Its edits were deliberately parked for the human reread.

### Phase F: Whole-Book Review (20 Nov, 15:26–18:59)

The review used a frozen tag (`relecture-2026-11-20-base`) and the `relecture-livre` branch.

- **Design** (Claude Opus `e4313594`):
  - a script builds reader dossiers from the rendered HTML (wave 0);
  - readers are **isolated, with no lateral communication**, a choice the author made to keep them independent;
  - no planted errors at that stage.
- **Wave 1** (16:16–16:32, *16 minutes of wall-clock time*): **11 readers in parallel**:
  - 10 Sonnet (medium): Parts P0–P5, appendices PA, and themes T1 (argument and statuses), T2 (numbers and models) and T5 (repetition and linear reading);
  - 1 Opus (high): "target reader C", who reads the whole book and keeps a journal;
  - result: **328 findings**, routed by `router_constats.py` into 7 verification lots.
- **Pause over quota, then a hand-over to the other vendor:**
  - the author paused the Claude side over usage cost;
  - Claude wrote `relecture/REPRISE.md` and a resume prompt that swaps Opus and Sonnet for Hydrogen;
  - Antigravity (`84e68ddf`) picked up the pipeline from those files.
- **Wave 2** (Antigravity, 17:12–17:30):
  - 7 verifiers, `v0`–`v5` and `vx` (Hydrogen, medium, which the author chose over high);
  - 1 `synthese` agent (Hydrogen, high);
  - result: `SYNTHESE_RELECTURE_2026-11-20.md` (273 clusters) and `TODO_wholebook_reread.md`, which includes alternatives and recommendations.
- **Edit and cold-reader passes:**
  - `e97f81b`: automated edit pass (82 files, ±1,580 lines);
  - a `lecteur-pdf` subagent (Hydrogen, medium) read *only the PDF*. Its context grew to 637,000 tokens, the largest of the project, and it wrote `rapport_lecture_pdf.md`;
  - `a6ce4be` fixed the table wrapping and prose slips it found.

### Phase G: Teaching Slides (20 Nov 22:07 → 21 Nov 09:29)

Antigravity `0491b338` built a Markdown-to-HTML/PDF/PPTX pipeline in `slides/`, reusing the book's figures and mathematics. It produced a short "message" deck, then a 3-hour deck, and finally an editable PPTX export.

---

## 4. How Agents and Swarms Were Used

### Inventory

| Swarm | Orchestrator | Subagents | Models (effort) | Wall-clock time | Output |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Part I re-read | Claude `054db021` | 3 | Opus | 15 min | ch. 2–4 edited |
| Parts II–V drafting | Antigravity `b465800e` | 21 (incl. 1 monitor) | Hydrogen (XHigh), Argon (High), Opus (High) | 3 h 40 min | ch. 5–18 + introductions drafted and re-read |
| Part V + conclusion | Claude `6fdce00e` | 2 | Opus | 24 min | Part V harmonised; conclusion written |
| Style judges | Claude `061db681` | 22 (2 calibration + 20 chapter lots) | Opus (`juge-style` custom agent) | 25 min | 83 / 39 accept / reject verdicts |
| Arbitration and bibliography | Antigravity `3f38c297` | 6 (incl. 1 monitor) | Argon / Hydrogen (High → Medium → Low) | ~20 min | `c8acb4f` |
| Calques audit | Antigravity `087dfb52` | 10 (incl. 1 monitor) | Hydrogen (High) | ~20 min | audit report |
| Whole-book review, wave 1 | Claude `e4313594` | 11 | 10 Sonnet (medium) + 1 Opus (high) | 16 min | 328 findings |
| Whole-book review, wave 2 + PDF reader | Antigravity `84e68ddf` | 9 | Hydrogen (Medium / High) | ~70 min | synthesis, TODO, edit pass, cold-reader report |

In compute terms, subagents made **56 % of all calls**, produced **53 % of the output tokens**, and took **44 % of the input**. The orchestrators, which carry the long context, took most of the remaining input.

### Recurring Patterns

1. **One vendor produces, the other reviews.** Gemini drafted and Opus re-read; later Gemini proposed and Opus judged. The project applied its own thesis to itself: an error is caught only by a check that can be wrong in a different way.
2. **Fresh, isolated readers.** Cold reads, review readers and the PDF-only reader each got a new context and no lateral communication, so their blind spots would not be correlated.
3. **Calibrate the judge before trusting it.** The style judge was tested on known drifts and known faithful edits before it was allowed to run unattended.
4. **Language models propose; scripts apply.** Edits went through YAML lots, deterministic application, `make verifier`, and one commit per chapter. No model rewrote prose freely once the pilot had failed.
5. **Coordination through files, which makes work resumable.** Lots, `constats.json`, `REPRISE.md`, `TODO_*` and memory files let work survive quota pauses, and even a switch of vendor in the middle of a pipeline.
6. **Model and effort tiers chosen under quota pressure.** XHigh was used for drafting, High for judging, Medium for verifiers, and Low for monitors. Effort was lowered while agents were running when quota ran short.
7. **A cheap monitor agent** ran in each large Antigravity swarm.
8. **The author's role:**
   - setting direction and provenance rules;
   - choosing between options (option D, style "option A", review scale);
   - deciding what not to automate (the calques edits, planted errors, the final human reread);
   - keeping an eye on quota.

---

## 5. Compute Effort (Tokens)

### By Vendor and Model

| Harness | Model | Calls | Input processed | of which cached | Output |
| :-- | :-- | --: | --: | --: | --: |
| Claude Code | Opus 5.5 | 1,180 | 327.5 M | 98 % (6.2 M cache writes) | 2.44 M |
| Claude Code | Sonnet 5.5 | 129 | 13.6 M | 89 % (1.5 M cache writes) | 0.45 M |
| Antigravity | Gemini 4 Hydrogen | 1,799 | 301.0 M | 92 % (23.6 M new) | 2.91 M |
| Antigravity | Gemini 4 Argon | 273 | 40.1 M | 91 % (3.5 M new) | 0.45 M |
| Antigravity | Claude Opus 5.5 (inside Antigravity) | 30 | 3.4 M | 92 % | 0.04 M |
| **Total** | | **3,411** | **≈ 686 M** | **≈ 95 %** | **≈ 6.28 M** |

### By Phase (both vendors combined)

| Phase | Calls | Input | Output | Share of output |
| :-- | --: | --: | --: | --: |
| A. Ideation and specs | 229 | 94.7 M | 0.96 M | 15 % |
| B. Drafting and re-reads | 1,714 | 308.1 M | 2.65 M | 42 % |
| C. PDF read, 19 Nov (logged part only) | 10 | 3.7 M | 0.07 M | 1 % |
| D. Style pass | 332 | 105.5 M | 0.57 M | 9 % |
| E. Arbitration, bibliography, calques | 400 | 56.4 M | 0.67 M | 11 % |
| F. Whole-book review | 616 | 96.4 M | 1.25 M | 20 % |
| G. Slides | 107 | 20.5 M | 0.12 M | 2 % |

### Reading These Numbers

- **Output against the book.** About 102,000 words of French Markdown is roughly 160,000–180,000 tokens. Total output of about 6.3 M tokens is therefore around **35–40 times the length of the finished text**. That covers drafts, rewrites, reviews, notes (about 350,000 words), scripts, tool calls and reasoning.
- **Input is dominated by re-reading context.** Each agent turn re-sends its whole context, which is why about 95 % of input came from the cache. The tokens that actually cost compute were about 7.8 M cache writes on Claude, about 27 M uncached input on Gemini, and the 6.3 M output tokens.
- **Context sizes.** Antigravity orchestrators reached a context of about 500,000 tokens; most chapter builders stayed within 200,000–300,000.
- **Quota, not money, was the constraint the author felt.** Both vendors were used on subscription quotas. The traces show 81 `/usage` checks in Antigravity and 7 Claude sessions opened only to check usage, along with explicit pauses, lowered effort and one switch of vendor. This report gives no money cost: list prices do not describe what a subscription costs.

---

## 5b. Cost at Public API List Prices

**Prices used** (per million tokens, standard tier, as published in November 2026):

| Model | Input | Cache read | Cache write | Output (thinking included) |
| :-- | --: | --: | --: | --: |
| Claude Opus 5.5 | $4.00 | $0.20 | $5.00 (5-min) / $8.00 (1-hour) | $20.00 |
| Claude Sonnet 5.5 | $2.00 | $0.10 | $2.50 (5-min) / $4.00 (1-hour) | $10.00 |
| Gemini 4 Hydrogen | $1.50 | $0.075 (implicit caching) | — | $7.50 |
| Gemini 4 Argon (introductory rate, to 30 Nov 2026) | $2.00 | $0.10 | — | $10.00 |

Sources: Anthropic's API pricing (as bundled with Claude Code), and Google's Gemini API pricing page (aistudio.google.com/docs/pricing). Every call was priced on its own usage record. Claude cache writes were split by lifetime, as the transcripts record them: Opus wrote 2.7 M tokens at 5 minutes and 3.4 M at 1 hour; Sonnet wrote 1.5 M at 5 minutes. All calls ran on the standard tier, with no fast mode.

### Result

| | API-equivalent cost |
| :-- | --: |
| Claude Code sessions (Opus 5.5 + Sonnet 5.5) | **$163.7** |
| Antigravity sessions (Hydrogen + Argon, plus 30 Opus calls) | **$95.5** |
| **Logged build, 18–21 Nov** | **≈ $259** |
| Same build with Argon at its standard rate ($4 / $20) | ≈ $274 |
| Plus the unlogged 19 Nov cloud session (estimated from the measured cost per token) | + $35–85 |
| **Plausible all-in range** | **≈ $260–360** |
| Not included: this lookback and lineage work | ≈ $10 |

| Phase | Cost | Share |
| :-- | --: | --: |
| A. Ideation and specs | $47.9 | 18 % |
| B. Drafting and re-reads | $107.6 | 42 % |
| C. PDF read (logged part) | $4.3 | 2 % |
| D. Style pass | $38.7 | 15 % |
| E. Arbitration, bibliography, calques | $20.2 | 8 % |
| F. Whole-book review | $36.2 | 14 % |
| G. Slides | $4.4 | 2 % |

### Reading the figure

- **Input cost more than output.** Input accounted for about $179 (69 %) and output for about $80 (31 %). Most of the input was cache reads and writes.
- **The prompt cache was the biggest saving.** At full input prices, the same token flow would have cost about **$1,960**, roughly 7.5 times more.
- **Two figures for scale.** The book cost about **$0.95 per page**, or about $2.50 per 1,000 words of source. Opus was the most expensive model: about 60 % of the total for about 35 % of the calls.
- **This is not what you paid.** You ran both vendors on subscriptions, so your actual cash cost is the prorated subscription fees. The usage limits you kept running into are the subscription's way of rationing what would otherwise be this API bill.
- **Uncertainties:**
  - the Gemini token fields were decoded by hand (§7), and if the decoded output excludes thinking, the Gemini cost is understated;
  - a constant 1,528-token field on every Gemini call was not counted, which would add up to about $5;
  - the cloud session is an estimate, not a measurement.

---

## 6. What Worked, What Rubbed

### What Worked

- **Specs first, then parallel builds.** With a locked structure, a register, fixed statuses, generated numbers and a verifier, about ten agents from two vendors could draft 21 chapters in one evening and still produce a coherent book. The cold reader later praised its terminology for being consistent.
- **Diversity across vendors used as a quality-control device**, not just as extra capacity.
- **Measured automation.** The style pilot's failure (82 % of sentences rewritten) was caught by diffing, not by hoping it was fine. The judge was then tested before it was trusted.
- **Resumability.** The whole-book review crossed a quota wall and a change of vendor without losing work.

### Friction

- **Quota management** cost a large share of the author's attention, and in places decided which model was used.
- **Logs are incomplete.** The 19 Nov cloud session, a full round of Opus and Sonnet cold reads, left no local transcript. It is the largest gap in this lookback.
- **Quality issues left at the end** (from `rapport_lecture_pdf.md`):
  - the book repeats itself when read linearly;
  - some symbols are reused locally ($z$, $D$/$C$);
  - a few figures dropped glyphs;
  - the empirical base of Parts III–V is thin, which the book itself admits.
  
  The English-calques audit is still parked for the human reread.
- **The style is homogeneous.** The diagnosis in Phase D found prose more uniform than in the 2022 book, written without an LLM. The conservative style pass only partly corrected it, as intended.

### Lessons for a Next Project

1. Log every session locally, cloud and remote-control sessions included, or export their transcripts. Otherwise the process cannot be audited.
2. Put a light token counter on each phase from the start. Two stores in two different formats had to be decoded after the fact here.
3. Keep "fresh isolated reader → independent verifier → deterministic application" as the default review loop. It was the most reliable pattern in the project.
4. Plan quota tiers in advance (which models and efforts go with which roles) instead of lowering effort in the middle of a swarm.
5. The final human reread remains the comparator no agent replaced. The author kept it on purpose: `ARBITRAGES_RESTANTS.md`, the calques audit and the TODO are its input.

---

## 6b. Human Hours: the 2022 Book Against the 2026 Build

**Source.** `TimeUnemployment.xlsx` is your own time log: 213 entries from 5 Oct 2020 to 28 Jul 2021, with hours estimated by hand. I sorted the entries by label. Your margin subtotals in the sheet (155.25 h to 7 Dec 2020, 431.9 h to 1 Jun 2021) add up to 587 h. My recount of book work over the same span gives 590 h, so the log is internally consistent.

### Self-declared hours on the 2022 book

| Category | Hours | Days | Period |
| :-- | --: | --: | :-- |
| Writing the book ("Writting book") | 572.1 | 113 | 22 Oct 2020 → 2 Jun 2021 |
| Correction and re-reading | 83.7 | 15 | Jan → 13 Jul 2021 |
| The manifesto (end of Part III) | 43.0 | 8 | 17 → 27 Jul 2021 |
| Thinking about and organising the book (plan, intro, style, A5 print layout) | 24.0 | 10 | Oct 2020 → Mar 2021 |
| **Core book work** | **≈ 723 h** | **145 days** (about 5 h a day) | **≈ 10 months** |
| Strategic thinking "and book content" (mixed) | 5.0 | 2 | Oct–Nov 2020 |
| Background reading (books on AI, Chalmers, *Think Bayes*, and others) | 44.3 | 11 | Oct 2020 → Apr 2021 |
| A talk and pitch on the book's themes (writing, recording, editing) | 52.5 | 15 | Nov 2020 → Jan 2021 |
| **Book work and everything around it** | **≈ 825 h** | | |
| Unrelated entries (job search, conferences, online profile, applications) | 128.2 | 30 | |

**This is a lower bound.** The log stops on 28 Jul 2021, but legal deposit was in Feb 2022, so the final edits, layout and publishing steps are not counted. Two "brainstorming / plan" entries (8 h) were left out because they are ambiguous.

### Comparison

| | 2022 book (author alone) | 2026 monograph (agents, under your supervision) |
| :-- | :-- | :-- |
| Text produced | about 65,000–75,000 words | about 102,000 words of source, 277 pages |
| Calendar time | about 10 months, 145 working days | 3 days (73 h elapsed) |
| Hours of work | **≈ 723 h** of core work, self-declared | **≈ 29 h** of logged agent activity, plus the unlogged cloud session of 19 Nov. Your own time was not logged. It is bounded above by the session time, roughly 30–40 h of supervision across about 132 prompts |
| Writing rate | about 100 words per hour of core work | about 2,500–3,500 words per hour of supervised time |
| Who typed the text | you | the models (about 6.3 M output tokens, against about 0.1 M tokens of finished text in 2022) |
| Re-reading and correction | 84 h of correction, plus 43 h for the manifesto | automated passes only. **Your full human reread is still to come** |

### How to read the comparison

1. **The ratio is about 20 times in hours, and about 100 times in calendar time.** It compares the writing of a book from settled ideas. It does not compare producing the ideas.
2. **The 2026 hours leave out what the build stood on:**
   - the 2022 book itself, where most of Part I and the core of Part II already are (`rapport_genealogie_idees.md`);
   - a year of LLM-assisted research, from Nov 2025 to Nov 2026 (notes, talk, treatise, arXiv article, essays). Your Nov 2026 housekeeping archive puts the epistemics thread at **about 85 h** (chat 44 h, Claude Code 32 h, git 10 h), plus about 13 h writing the talk. The computing line behind Part III (curricula, LADDER, bridge essay) is counted separately and is not included.
   
   Counted honestly, the 2026 book rests on at least the same 723 h, plus roughly 100 h of research-line work, plus the build.
3. **The two kinds of work differ.** In 2022 the hours went into writing and correcting. In 2026 your time went into deciding (specs, options, arbitration), supervising and checking quota. The prose and most of the mechanisms were produced by the models.
4. **The reread is the largest missing item.** In 2022, correction took about 12 % of core hours. A careful human reread of the 277 pages, with light edits, would take about 40 h. At the 2022 correction pace, scaled to the longer text, it would take about 120 h. That would bring the human cost of the 2026 book to roughly 70–160 h. This is still about 4.5 to 10 times less than in 2022.

---

## 7. Method and Limits

- **Claude tokens.** Taken from the `message.usage` of each assistant turn, counted once per `message.id`, over all top-level and `subagents/*.jsonl` files of the two Claude project folders for this repository. Output includes reasoning.
- **Gemini tokens.** Taken from the protobuf `gen_metadata` records of each `conversations/<id>.db`, decoded by hand. Fields were matched to meanings by checking that they behave consistently, not from documentation:
  - field 2: new input;
  - field 5: cached input, which grows monotonically through a conversation;
  - field 3: total output, equal to the sum of fields 9 and 10;
  - field 21: model label.
  
  These are reliable to within field interpretation. In particular, it is not clear whether the reasoning tokens are counted inside field 3.
- **Not counted:**
  - the 19 Nov cloud or "clone" session (commit `7afa571`, about 40 cold reads plus synthesis and edits). By analogy with the whole-book review, it plausibly adds on the order of **50–150 M input and 1–2 M output tokens**. This is an estimate, not a measurement;
  - the months of research and the earlier artifacts done before 18 Nov.
- **Active time.** Computed as the union of session intervals (first to last event), with the overnight idle time of session `6fdce00e` (00:22–06:38) removed. Thinking time between prompts within a session counts as active.
- **Author prompts.** Claude prompts are counted as non-meta user messages; Gemini prompts as `history.jsonl` entries that are not slash or shell commands.

---

## Appendix: Session Inventory

### Claude Code (times CET)

| Session | Date and time | Calls | Out | Subagents | Purpose |
| :-- | :-- | --: | --: | --: | :-- |
| `35e8683a` | 18/11 10:34–13:05 | 27 | 315 k | — | cross-model critique; provenance clean-up |
| `d05e1992` | 18/11 13:07–16:23 | 163 | 513 k | — | French map; specs; conventions; outline; scaffold |
| `d07499b2` | 18/11 17:36–17:54 | 33 | 87 k | — | Part 0 re-read |
| `9db975b5` | 18/11 17:55–18:07 | 18 | 67 k | — | ch. 1 re-read |
| `e0340584` | 18/11 18:24–18:47 | 47 | 49 k | — | build: screen layout, logs |
| `054db021` | 18/11 18:48–20:13 | 69 | 71 k | 3 (145 calls, 238 k out) | ch. 2–4 re-read; Part I pass |
| `97427b14` | 18/11 23:04–23:36 | 37 | 64 k | — | Part introductions |
| `b87d18e3` | 18/11 23:36–23:54 | 56 | 81 k | — | Part IV harmonisation |
| `6fdce00e` | 18/11 23:54 → 19/11 06:57 | 46 | 41 k | 2 (167 calls, 283 k out) | Part V + conclusion; morning fixes |
| `061db681` | 20/11 10:25–14:01 | 175 | 313 k | 22 (83 calls, 100 k out) | 2022/2026 comparison; style-pass orchestration |
| `e4313594` | 20/11 15:26–17:14 | 76 | 101 k | 11 (164 calls, 552 k out) | whole-book review, waves 0–1 |
| 7 empty sessions | 18–20/11 | 0 | — | — | `/usage`, `/model`, `/exit` only |

### Antigravity (Gemini) Top-Level Conversations

| Conversation | Date and time | Calls | Out | Subagents | Title / purpose |
| :-- | :-- | --: | --: | --: | :-- |
| `bb94fdf6` | 18/11 08:38–10:42 | 20 | 102 k | — | critique of the trilogy; interactive map |
| `706678bb` | 18/11 13:18–16:24 | 19 | 29 k | — | map structure; course specs |
| `f25721c2` | 18/11 16:37–17:04 | 25 | 42 k | — | build Part 0 |
| `fa237edf`, `80a934d3`, `c7591e1c`, `9b6faafb` | 18/11 17:04–18:50 | 130 | 274 k | — | build ch. 1–4 |
| `b465800e` | 18/11 20:14–23:56 | 103 | 117 k | 21 (838 calls, 1.22 M out) | orchestrating chapter subagents, Parts II–V |
| `3b1da9a8` | 19/11 17:27–18:24 | 10 | 65 k | — | PDF-only review of the book |
| `771cd3ab` | 20/11 10:10–12:39 | 41 | 60 k | — | style-pass spec; ch. 0 pilot |
| `f92e6c2d` | 20/11 13:05–13:53 | 33 | 92 k | — | style proposer (lots) |
| `3f38c297` | 20/11 13:55–15:37 | 90 | 107 k | 6 (197 calls, 258 k out) | arbitrations; bibliography; artefacts |
| `087dfb52` | 20/11 15:39–16:52 | 20 | 47 k | 10 (93 calls, 257 k out) | English-calques audit swarm |
| `84e68ddf` | 20/11 17:02–20:58 | 166 | 190 k | 9 (210 calls, 406 k out) | review wave 2; edit pass; cold PDF reader |
| `0491b338` | 20/11 22:07–23:53 (+ 21/11) | 107 | 116 k | — | teaching slides |
