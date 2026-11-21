# `swarm-research/` — status and rules of use

> **FENCED — 2026-11-21.** This folder is archived research material. **It is not a source for the monograph.** Nothing in it enters `monographie/` except through [`TODO_potential_leads.md`](TODO_potential_leads.md), after a primary-source check and the usual bibliography and style workflow (see "Rules" below).
>
> The **only reference document** for book changes is the **verified edition (2026-11-21)** of [`monograph_upgrade_sheet.md`](monograph_upgrade_sheet.md). Where any other file in this folder disagrees with it, the verified upgrade sheet wins.

---

## What this folder contains

The folder holds four layers of material:

1. **An automated literature review** run with a Gemini agent swarm in November 2026:
   - the brief, [`starter_research.md`](starter_research.md);
   - nine domain surveys, `01_…` to `09_…`;
   - a cross-domain synthesis, [`synthesis.md`](synthesis.md);
   - a review of the book against that synthesis, [`cross_review_monograph.md`](cross_review_monograph.md).
2. **A refinement pass**:
   - adversarial falsifiers, a primary-source empirical audit, and formal bridges, in [`refinement/`](refinement/);
   - their summary, [`refinement_report.md`](refinement_report.md).
3. **Automated research tracks** in [`auto_research/`](auto_research/):
   - Track 1: SymPy/Z3 proofs, in `track1_formal/`;
   - Track 2: a socio-technical Sobol simulator, in `track2_sim/`;
   - Track 3 (fault-injection benchmark): specified only, never run.
4. **Distilled outputs**:
   - [`monograph_upgrade_sheet.md`](monograph_upgrade_sheet.md), now the verified edition;
   - [`cheat_sheet.md`](cheat_sheet.md);
   - [`explorer.html`](explorer.html).

On 2026-11-21 an audit checked the upgrade sheet and the tracks against three things: the chapter sources (`monographie/chapitres/*.md`, `main` at `4d05d56`), re-runs and re-derivations of the code, and a sample of primary sources. Its verdict: **the monograph holds in its present form**, and the upgrade sheet's items are sharpening, not repair. The highest severity found was moderate.

---

## Withdrawn conclusions — do not cite, do not re-import

| Claim (where it appears) | Why it is withdrawn |
|---|---|
| **"Trigger human checks strictly on epistemic uncertainty, not on stakes"** (upgrade sheet item 5, `track2_sim/RESULTS.md`, `refinement_report.md` § Executive 4, `synthesis.md` Tier 1 Lead 2) | **Simulation artifact.** Five reasons:<br>• The "59.5% dominance" is 2.8% under the code's own criterion.<br>• The gain over doing nothing is 0.7%.<br>• The result reverses when one fixed constant changes (`phi_CFF` from 0.14 to 0.06).<br>• It depends on an uncertainty probe built to track errors.<br>• Gates (*verrous*) were never simulated; a non-bypassable check is the worst policy in the model's own terms.<br>It also contradicts P1 and the *erreurs constantes* result (Ch. 12.4). |
| **"Shadow AI bypass" caused by friction** (all files) | **An assumption, not evidence.** Buçinca et al. 2021 measured lower satisfaction, not bypass; the "enterprise governance studies" are unnamed. Track 2 then encodes the assumption as a constant. |
| **Copula result "b_min consumes ~97% of p\*, forcing verrous"** (upgrade sheet item 4, `track1_formal/RESULTS.md`) | **Numerical artifact.** 0.0096 is the first margin at which the grid has no admitted cell, and the code returns Ψ = 0 there. The value is identical under independence, and the script's own monotonicity check fails. |
| **"Z3-PROVED" labels** (`track1_formal/RESULTS.md`) | Three checks are vacuous or tautological:<br>• `verify_m1.py:41–43`: contradictory constraints.<br>• The bypass "theorem" at `verify_m1.py:112–120`.<br>• `verify_m3_savi.py:31`: assumes its own conclusion.<br>The algebra that matters (p_crit, dR/dp at p = 1, Fréchet bounds, the c_eff identity) is correct. |
| **SAVI "34.4% power"** (`track1_formal/RESULTS.md`) | Comes from overbetting (λ = 9, about 4× Kelly). With λ ≈ 2 the power is about 99%. |
| **"Genuine falsifier" of P3(a)** and **"shared models reduce mean R" presented as a new qualifier** (`refinement_report.md` § 1) | The book already contains both:<br>• Ch. 7 Nuance and Ch. 12 Nuance on salience omission.<br>• Table 16.1 and `16-angles-morts-collectifs.md:53`. |
| **"Al-Najjar & Weinstein 2009 support verrous"** (upgrade sheet item 4, `refinement_report.md` § 3) | Their paper critiques ambiguity-aversion models. If cited at all, it is an objection to the humility margin *b*, not support for gates. |
| **"Annex D validated by the simulator"** (`track2_sim/RESULTS.md`) | `validation.py` recomputes the book's closed-form formulas and never runs the simulator. |

## Unverified — primary check required before any use

- Doshi & Hauser 2024, "ownership penalty" (already flagged in `refinement/02`).
- Bauer et al. 2025/2026 on pooling equilibria.
- The *curl* HackerOne and *tldraw* incidents.
- The EMNLP 2025 "DBG score".
- "Millions of GitHub PRs".
- Quantitative "Retrieval Collapse" rates.
- Hollnagel "Safety-II" as applied to *verrous*.
- Citation details not listed as checked in `TODO_potential_leads.md` § C.

**Known citation errors in older files:**
- Liang **2023** (not 2024) is the detector-bias paper.
- Its "61.22%–97%+" range mixes an average false-positive rate (61.22%) with the share of essays flagged by *at least one* detector (97.8%).
- Kim et al. 2024 appeared at FAccT, not CHI.
- Rae et al. 2018 has four authors: Rae, Provan, **Weber** & Dekker.
- The book cites 69 works, not 41.

## How independent is this corpus?

Less than the files claim:
- The brief poses its questions in the book's own notation and seeds them with the book's references.
- The book was co-drafted with Claude and Gemini; this swarm is Gemini; the audit is Claude.

By the book's Definition 10 (*sévérité*), agreement such as "the monograph maps onto the corpus" or "invariants confirmed independently" could hardly have failed, so it carries little weight. Only two parts have real severity: the primary-source checks (`refinement/02_empirical_2024_2026.md`) and the code that was actually executed.

The pipeline also shows the book's Definition 9 (*blanchiment*) at work. "Uncertainty-gated checks" starts as a design proposal (synthesis), becomes a requirement (refinement), then an assumption (Track 2), then a "crucial refinement" (upgrade sheet). At each step it loses its condition: *only if the uncertainty signal tracks where the errors are*.

---

## File status

| File | Status | Use |
|---|---|---|
| `monograph_upgrade_sheet.md` | **Reference (verified edition 2026-11-21)** | The only basis for book changes |
| `TODO_potential_leads.md` | **Working list** | The revision batch and longer-term leads derived from the verified sheet |
| `refinement/02_empirical_2024_2026.md` | Reliable for study details it marks as checked | Source of sample sizes and designs; respect its `[UNVERIFIED]` flags |
| `cross_review_monograph.md` | Partly superseded | Its gap list is mostly right; the citation details listed above are wrong; it praises the book with low severity |
| `synthesis.md` | Background | A good research map; its "invariant laws" are working hypotheses; unverified items listed above |
| `01_…`–`09_…` domain surveys | Background | Reading lists only; verify each reference independently |
| `refinement_report.md`, `refinement/01_…`, `refinement/03_…` | Partly superseded | The falsifier classifications and the remedy prescriptions are withdrawn (see table above) |
| `auto_research/track1_formal/` | Partly valid | Correct algebra; labels overstate; copula and power figures withdrawn |
| `auto_research/track2_sim/` | **Conclusions withdrawn** | Keep as code only; its policy results must not be cited |
| `cheat_sheet.md`, `explorer.html` | Not audited | Built from pre-audit material; check against the verified sheet before use |

**Broken links:** `refinement_report.md` points to `research/refinement/…`, `research/0X_…` and `specs_automated_research.md`. The first two live at `refinement/…` and `./0X_…`; the spec file is not in the repository.

---

## Rules for future sessions and agents

1. **No direct import.** Anything here reaches `monographie/` only through `TODO_potential_leads.md` § A, after these steps:
   - a primary-source check of the claim;
   - adding the reference to `monographie/commun/biblio_a_verifier.bib` with an `averifier` note, then moving it to `biblio.bib` once verified;
   - `make verifier` and a rebuild;
   - the style judge pass.
2. **Do not re-run the swarm to "confirm" items.** Agreement from the same model family has low severity (Def. 10) and adds no evidence.
3. **Do not read `RESULTS.md` labels** ("PROVED", "Pareto", "dominates") as findings. Use the verified upgrade sheet instead.
4. **The one open lead with refutation power is Track 3**: measuring escape probability with seeded errors in a real mixed human–LLM workflow. See `TODO_potential_leads.md` § D.
5. **Merge with the whole-book review.** Book-level decisions also depend on `monographie/notes/SYNTHESE_RELECTURE_2026-11-20.md`. Treat its open items and the leads listed here as **one** revision pass.
