# Remaining Editing Work — Whole-Book Reread (`relecture-livre`)

**Date:** `2026-11-20`  
**Branch / Baseline:** `relecture-livre`, frozen book text tagged `relecture-2026-11-20-base` (commit `159f951`, Wave 1 at `48764ac`, Wave 2 uncommitted).  
**Primary Sources:**
- `monographie/notes/SYNTHESE_RELECTURE_2026-11-20.md` (consolidated review synthesis)
- `relecture/sorties/synthese/corrections.json` (160 pre-verified exact `avant`/`apres` patches, all `count == 1`)
- `monographie/notes/RAPPORT_AUDIT_CALQUES.md` (unapplied English calques audit)
- `monographie/notes/TODO_ETAT_ACTUEL.md` (prior roadmap; only `P5.2 [STY-P2]` remains open)

---

## Executive Snapshot

The monograph's core thesis, five propositions, and arithmetic/tables were independently verified with **zero calculation errors**. Remaining editing work comes from **260 consolidated clusters** (`181 CONFIRME`, `50 PLAUSIBLE`, `20 REJETE`, `5 DEJA_TRANCHE`, `4 DEJA_RELEVE`) across **231 active items** (`124 G1`, `89 G2`, `18 G3`; severities `6 A`, `98 B`, `156 C`), plus two orthogonal polish passes (`RAPPORT_AUDIT_CALQUES.md` and `P5.2`).

| Workstream | Scope | Ready patches? | Requires author decision? |
| :--- | :--- | :--- | :--- |
| **1. Critical blockers (Sev. A)** | 6 clusters (`3 G1`, `1 G2`, `2 G3`) | 4 in `corrections.json` (`V2-039`, `V3-001`, `V3-030`, `V2-021`) | Yes on `G3`/`G2` (`V5-001`, `V2-029`, `V2-021`) |
| **2. Substantive questions (`G3`)** | 18 active (`13 CONFIRME`, `5 PLAUSIBLE`, incl. 2 Sev. A) | No | Yes (choose option in `SYNTHESE` § 3) |
| **3. Quick decisions (`G2`)** | 89 active (`56 CONFIRME`, `33 PLAUSIBLE`) | 23 `CONFIRME` (`25` ops) in `corrections.json` | Yes (approve patches or pick alternative) |
| **4. Direct fixes (`G1`)** | 124 active (`112 CONFIRME`, `12 PLAUSIBLE`) | 107 `CONFIRME` (`135` ops) + 11 `PLAUSIBLE` in `V*.json` | Spot-check `5` non-JSON `G1` & `12` `PLAUSIBLE` |
| **5. Redundancy & reading paths** | `VX-034`, `VX-005`, `V0-008`, `V0-001`, `V5-044`, `V4-002`, `V2-052` | Partial (`V1-005`, `V1-006`, `V1-022`, `V3-008`, `V3-022`, `V5-017`, `V5-034`) | Yes (cut strategy for part pages & case studies) |
| **6. Calques, style & blind spots** | `RAPPORT_AUDIT_CALQUES.md`, `P5.2`, PDF figures, `biblio.bib` | Suggested rewrites in audit report | Apply after structural/content edits |

---

## 1. Critical Points (Severity A — Blocking)

These 6 clusters are factual, mathematical, or conceptual contradictions that must be resolved before publication.

### 1.1 `V5-001` (merged `V1-002`, `CONFIRME`, `G3`) — Russian roulette contradiction in M2
- **Files:** `monographie/chapitres/04-decider.md` (l. 84, 119), `monographie/chapitres/17-decisions-sans-appel.md` (l. 64), `monographie/commun/parametres.py`, `monographie/tableaux/ch04-seuil.md`, `ch17-scenarios.md`, `ch17-decisions.md`.
- **Issue:** Despite `ARBITRAGES P2.2.2` (`DEC-S6`), 3 fresh readers (`C`, `P1`, `P5`) stumble on the same contradiction: the player estimates $p = 0{,}001\,\%$ for a *forgotten round in the chamber*, yet the round in the cylinder ($z = 1/6 \approx 16{,}7\,\%$) is treated as an independent omitted factor outside the frame. Once a round is inside $p$, a live round in the cylinder is an in-frame estimation error, not an independent omitted factor.
- **Alternative solutions:**
  - **Option A (keep numbers/tables, change ch. 17 scenario):** Keep Russian roulette only in ch. 4 § 4.3 as an extreme-stakes example ($L/\Delta U = 10\,000$, drop it from § 4.5), and replace line 6 of Table 17.2 in M2 with a clean physical case at $L/\Delta U = 10\,000$ where $p$ and $z$ are strictly disjoint (e.g., mountain flight or bridge crossing: $p = 0{,}001\,\%$ known mechanical failure vs. $z = 16{,}7\,\%$ unmodeled maintenance defect). Requires updating `parametres.py` label and regenerating `ch17-*` tables.
  - **Option B (keep Russian roulette in M2 without table regeneration, rewrite story):** State explicitly in § 4.3 and § 17.1 that the player believes they are handling a *deactivated/blank* prop gun ($p = 0{,}001\,\%$ covers a mechanical/primer mishap), whereas substitution with a live-loaded revolver ($z = 1/6$) is an unmodeled frame breach.
  - **Option C (remove Russian roulette row from M2):** Keep the 5 rows of Table 17.2 without Russian roulette and address $p^\ast = 0{,}0100\,\%$ vs. any plausible margin $b$ in a short paragraph.
- **Recommendation:** **Option A** (or **Option C** if you want to keep M2 lean). Option B remains strained and risks feeling contrived to careful readers; Option A eliminates the conceptual collision cleanly at the root.

### 1.2 `V2-029` (`CONFIRME`, `G3`) — Triple status contradiction on Proposition 4
- **Files:** `monographie/chapitres/08-independance-chaines.md` (l. 49–53), `monographie/chapitres/99-conclusion.md` (Table 1 l. 22, § 2.2 l. 53–57).
- **Issue:** 3 readers (`C`, `P2`, `T1`) flag that P4's block header displays `statut="hypothèse de travail"`, the parenthetical note immediately below calls it *composite* (labeling the structural tension *définition*), and Conclusion Table 1 classifies that structural tension as *résultat sous hypothèses*.
- **Alternative solutions:**
  - **Option A (single `composite` block + aligned breakdown):** Set `statut="composite"` on P4's header (checking/allowing `composite` in `filtres/monographie.lua` and `outils/verifier.py`) and harmonize ch. 8 + Conclusion Table 1 identically: *définition* (relativity to an error class), *résultat sous hypothèses* (structural tension: shared causes evade cross-checks, while comparability requires minimal sharing, following P2 conditions 2–3), and *hypothèse de travail* (empirical cost trend). Also remove the redundant prose recap in § 8.2.
  - **Option B (split P4 into P4a / P4b):** Separate the structural result (`résultat sous hypothèses`) and the empirical cost claim (`hypothèse de travail`) into two numbered propositions, updating cross-references (`00-cartographier.md`, `partie-2.md`, `99-conclusion.md`, `A-outils.md`).
- **Recommendation:** **Option A** if `filtres/monographie.lua` / `outils/verifier.py` cleanly supports `composite` (minimal ripple across cross-references); otherwise **Option B** is safer than leaving a mislabeled header.

### 1.3 `V2-039` (`CONFIRME`, `G1`) — Critical inversion: event $C$ glossed as « *contrôle franchi* »
- **Files:** `monographie/chapitres/09-severite-echappement.md` (l. 92).
- **Issue:** Introduced by `ARBITRAGES P1.10.4`: $C$ is defined as the error being *stopped* by a check, but the gloss « *contrôle franchi* » means the error *got past* the check ($\bar C$), inverting $C$ and $\bar C$.
- **Alternative solutions:**
  - **Option A (`corrections.json` patch):** Replace « *contrôle franchi* » with « *contrôle réussi* ».
  - **Option B:** Replace with « *erreur arrêtée* » (matching ch. 6's $D$ semantics explicitly).
- **Recommendation:** **Option A** (already patched in `corrections.json`; concise and unambiguous).

### 1.4 `V2-021` + `VX-013` (`CONFIRME`, `G2` / `G1`) — Mathematical flaw in M3 proof ($f_1$ determinism)
- **Files:** `monographie/chapitres/07-cadre-cause-commune.md` (l. 56), `monographie/annexes/A-outils.md` (A.6).
- **Issue:** In M3, $e(x,z) = g(x,z) - f_1(x)$. If $f_1$ is allowed internal random draws (currently permitted by Hypothesis 1), agreement $A$ between $f_1(x)$ and $f_2(x)$ depends on $f_1(x)$ and hence on $e(x,z)$ even when $A \perp z \mid X=x$, invalidating $A \perp e \mid X=x$.
- **Alternative solutions:**
  - **Option A (`corrections.json` patches for `V2-021` and `VX-013`):** Stipulate in Hypothesis 1 (ch. 7 and Annex A.6) that $f_1$ is *deterministic given $x$* (while $f_2$ may be randomized provided its internal draws are independent of $z$ given $x$).
  - **Option B:** Redefine error relative to $\mathbb{E}[f_1(x)]$ or explicitly assume $f_1$'s internal randomness is independent of $A$ given $x$ (which contradicts $A$ being a function of $(f_1(x), f_2(x))$ unless $f_1$ is deterministic).
- **Recommendation:** **Option A** (already prepared in `corrections.json`). It makes the proof mathematically airtight with a single-line hypothesis fix.

### 1.5 `V3-001` (`CONFIRME`, `G1`) — Part III overclaim: « *erreurs d’un type nouveau* »
- **Files:** `monographie/parties/partie-3.md` (l. 11), `monographie/chapitres/13-synthese-deux-axes.md`.
- **Issue:** `partie-3.md` calls silent, in-frame errors a « *type nouveau* » specific to learned components, contradicting ch. 10 and ch. 13 (*Mars Climate Orbiter* proves classical software also produces them) and `content_spec/00_global.md` § 9.3.
- **Alternative solutions:**
  - **Option A (`corrections.json` patch):** Remove « *d’un type nouveau* » in `partie-3.md` and phrase the learned-component shift as populating that cell massively/systematically (aligned with ch. 13 PC 3's *hypothèse de travail* status).
  - **Option B:** Clarify that what is new is *neither* silence *nor* in-frame origin, but the *absence of a pre-written contract* leaving no address for repair.
- **Recommendation:** **Option A** (already patched in `corrections.json`, directly aligned with `00_global.md` § 9.3).

### 1.6 `V3-030` (`CONFIRME`, `G1`) — Misleading interpretation of 99.9% severity in ch. 12
- **Files:** `monographie/chapitres/12-autre-regime.md` (l. 138).
- **Issue:** The reading bullet praises 99.9% severity on the rare fact (« *attrape efficacement* ») without mentioning in the same bullet that the false-alert rate is also 99.9% ($s/f \approx 1$), contradicting ch. 9 (a detector that rings almost always detects uncertainty/ignorance without discriminating true from false answers). Also carries the calque *attrape*.
- **Alternative solutions:**
  - **Option A (`corrections.json` patch):** Rewrite the bullet to note both 99.9% severity *and* 99.9% false-alert rate ($s/f \approx 1$), explaining that divergence flags lack of epistemic grounding rather than discriminating true vs. false answers.
  - **Option B:** Split the bullet into a positive signal statement (uncertainty detection) and an explicit warning referencing ch. 9 (`VPP` collapse).
- **Recommendation:** **Option A** (already patched in `corrections.json`; fixes both the conceptual contradiction and the calque).

---

## 2. Substantive Questions (`G3` — 18 Active Clusters)

*(Items `V5-001` and `V2-029` are detailed in § 1 above. The remaining 16 `G3` clusters are grouped below with options and recommendations; record decisions in `SYNTHESE_RELECTURE_2026-11-20.md` § 3.)*

### A. Propositions, Proofs & Conceptual Boundaries
1. **`V2-005` (`CONFIRME`, B) — Proposition 1 hypotheses & meaning of « *désaccord* » (`05-trois-incertitudes.md` l. 65, 82–91; Conclusion Table 1)**
   - *Problem:* Boxed P1 is stated universally despite its *résultat sous hypothèses* status, hiding hypotheses inside an optional `.formel` block, and eq. (5.1) splits into *internal dispersion* + *inter-model disagreement*.
   - *Alternatives:* (a) Fold conditions (finite moments, weighting on specified $\Theta$) and both terms into P1's boxed statement; (b) add the brief clause « *calculé sur un ensemble spécifié $\Theta$ sous des hypothèses données* » to the box and gloss both terms in running prose right below.
   - *Recommendation:* **(a)** (or **(b)** if you prefer keeping the short punchy title/phrase « *désaccord* »).
2. **`V2-008` (`PLAUSIBLE`, B) — Bayesian « catch-all » hypothesis in $\Theta$ (`05-trois-incertitudes.md` l. 73–77 or `17-decisions-sans-appel.md` § 17.1)**
   - *Problem:* No reply to the standard Bayesian objection of adding a residual hypothesis « something outside our models » with non-zero prior weight.
   - *Alternatives:* (a) Add 3 sentences (ch. 5 *Nuance* or ch. 17) explaining that a catch-all has no well-defined predictive likelihood on observables, so it yields neither a computable disagreement in $\Theta$ nor Bayesian updating (distinguishing it from act-level humility margin $b$); (b) leave as is.
   - *Recommendation:* **(a)** — 3 sentences disarm a predictable referee objection.
3. **`V2-014` (`CONFIRME`, B) — Proposition 2 *définition* status vs. 5 conditions (`06-detecter-une-erreur.md` l. 35–46, 57–62, 88; Conclusion Table 1)**
   - *Problem:* P2 is tagged *définition* with 3 terms (*comparateur*, *désaccord*, *prise d'acte*), yet text says 5 conditions « *découlent* » from it (including *difference*, *comparability*, *timeliness*) plus « escape = 1 if any lacks » without a declared status.
   - *Alternatives:* (a) Keep P2 as 3-term *définition* and explicitly label the 5-condition unpacking + `escape = 1` consequence as an *analytical decomposition / résultat sous hypothèses*; (b) fold all 5 conditions into P2 as *composite*.
   - *Recommendation:* **(a)** — preserves `00_global.md` § 3 (`P2 = définition`) and cleans up the logical step.
4. **`V2-022` (`CONFIRME`, B) — Proposition 3(b) unproved status (`07-cadre-cause-commune.md` l. 35–42; Conclusion Table 1)**
   - *Problem:* Signal on `DECISIONS_SYNTHESE S4`: P3(b) displays *résultat sous hypothèses*, whereas M3 only proves P3(a).
   - *Alternatives:* (a) Reclassify P3(b) as *hypothèse de travail* (or structural remark illustrated by empirical findings) in ch. 7 and Conclusion Table 1; (b) add a 4-line formal derivation in M3 linking a varying $z$ to unexplained conditional variance via eq. (5.1).
   - *Recommendation:* **(b)** — mathematically clean in 4 lines using eq. (5.1) already proved in ch. 5; if skipped, **(a)** is mandatory.
5. **`V2-040` (`CONFIRME`, B) — Severity $\Pr(\bar A \mid E)$ colliding with sensitivity $s$ (`09-severite-echappement.md` l. 48–50)**
   - *Problem:* Signal on `DECISIONS_SYNTHESE R4`: defining severity as $\Pr(\bar A \mid E)$ makes it identical to sensitivity $s$, creating two glossary terms for one quantity and obscuring Mayo's ratio $(1-f)/(1-s)$.
   - *Alternatives:* (a) Add one clarifying sentence in § 9.2 explaining that in a binary alert model ($A/\bar A$), Mayo severity reduces to sensitivity $s = \Pr(\bar A \mid E)$, whereas the probative weight of agreement ($A$) is governed by $(1-f)/(1-s)$; (b) drop the `R4` sentence and keep $(1-f)/(1-s)$ in eq. (9.2) as the quantitative measure.
   - *Recommendation:* **(a)** — preserves Mayo's link while eliminating the duplicate-term illusion.
6. **`V1-001` (`CONFIRME`, B) — Inclusion direction: *représentation* vs. *cadre* (`02-cadre.md` l. 77, `03`, `04`, `registre_termes.md` l. 18–19)**
   - *Problem:* Signal on `ARBITRAGES P1.2` (`SYN-D2`): § 2.3 says « *La représentation comprend ce cadre…* », then two lines later (and in ch. 3–4) writes « *à l'intérieur du cadre* » / « *construite dans un cadre* ».
   - *Alternatives:* (a) Keep nested reading ($\text{représentation} \supset \text{cadre}$) and replace residual « *à l'intérieur du / dans le cadre* » (when referring to the full representation) with « *à partir de / sur la base de ce cadre* »; (b) revert to disjoint reading (frame = container, representation = content).
   - *Recommendation:* **(a)** — honors `P1.2` without reopening the glossary.
7. **`V2-023` (`CONFIRME`, B) — Narrow definition of « *dérive de distribution* » (`07-cadre-cause-commune.md` l. 85; `registre_termes.md` l. 45)**
   - *Problem:* Defined strictly as an *omitted* factor changing in deployment, whereas in ML *distribution shift* covers recorded variables too.
   - *Alternatives:* (a) Rename term to *dérive d'un facteur omis* (or *dérive hors cadre*); (b) keep *dérive de distribution* and explicitly qualify both § 7.3 and `registre_termes.md` as « *au sens restreint retenu ici…* ».
   - *Recommendation:* **(b)** — preserves the standard English mapping in the glossary while preventing ML-practitioner confusion.
8. **`V3-003` (`PLAUSIBLE`, C) — Status of « *changement de régime* » in Conclusion Table 1 (`99-conclusion.md` l. 28)**
   - *Problem:* Table 1 labels it *définition*, mixing the naming of the 3 simultaneous shifts with the empirical/structural claim that lacking a written spec causes them together.
   - *Alternatives:* (a) Split Table 1 cell into *définition* (the 3 shifts) + *hypothèse de travail* (link to missing verifiable spec); (b) keep as is.
   - *Recommendation:* **(a)** — one-line fix that closes a status loophole.

### B. Examples, Formatting & Conventions
9. **`V1-003` (`CONFIRME`, B) — Fictional `.cas` block in ch. 2 (`02-cadre.md` l. 136–142; `07` l. 85)**
   - *Problem:* « *Un modèle clinique face à un changement de population* » is tagged `.cas` (*Étude de cas*, reserved by the preface for dated historical/industrial/legal cases) despite being a generic « *Considérons…* » scenario.
   - *Alternatives:* (a) Reclassify as an illustrative running example in prose (or `.nuance`/`.outils`) and soften § 7.3's back-reference; (b) replace with a real dated clinical population-drift case study (e.g., published EHR sepsis or readmission drift study).
   - *Recommendation:* **(b)** if a verified published case is readily available; otherwise **(a)** immediately so no invented scenario wears `.cas`.
10. **`V2-016` (`CONFIRME`, B) — *Challenger* across the 5 conditions (`06-detecter-une-erreur.md` l. 111–121)**
    - *Problem:* Signal on `ARBITRAGES P1.5` (`SYN-D4`): *existence* sounds contradictory (records existed vs. plot not assembled), and omitting 16 undamaged flights sits awkwardly under *différence* instead of *comparabilité*.
    - *Alternatives:* (a) Adopt Option (b) from `ARBITRAGES P1.5`: 1 clean fact per condition (*existence*: 23-flight data existed in files, full plot not assembled; *différence*: NASA/Thiokol qualification models shared cold-joint assumptions; *comparabilité*: meeting charts omitted the 16 undamaged flights; *timeliness*: eve-of-launch warning; *take-up*: dual breakdown); (b) tie the 16 omitted flights solely to *comparabilité* and clarify latent *existence*.
    - *Recommendation:* **(a)** — removes overlap across conditions 1–3.
11. **`V2-012` (`PLAUSIBLE`, C) — *Challenger* Nuance in ch. 5 (`05-trois-incertitudes.md` l. 116–122 vs. § 6.3)**
    - *Alternatives:* (a) Keep a 3-line conceptual guardrail in ch. 5 pointing to § 6.3 for the full facts; (b) leave as is; (c) delete in ch. 5.
    - *Recommendation:* **(a)** — preserves warning for selective readers without spoiling § 6.3.
12. **`V5-011` (`PLAUSIBLE`, C) — Which terms get numbered `.definition` boxes (`17` l. 17; `00-avant-propos.md`)**
    - *Alternatives:* (a) Keep the 14 formal `.definition` boxes and add one sentence in the preface explaining that `.definition` boxes are reserved for model/proposition building blocks while other glossary terms are bolded inline; (b) add `.definition` boxes for 4–5 key concepts (*marge d'humilité*, etc.).
    - *Recommendation:* **(a)** — avoids visual box clutter.

### C. Structural Redundancy & Reading Paths
13. **`V0-001` (`CONFIRME`, B) — Incomplete « *L’argument principal* » reading path (`00-cartographier.md` l. 213, Table 0.1)**
    - *Problem:* Flagged by 4 readers (`C`, `P0`, `T1`, `T5`): skips ch. 4, 8, 9, 17 even though ch. 13, 16, 18 directly rely on Propositions 4–5, M1, $p^\ast$, and $b$.
    - *Alternatives:* (a) Add ch. 8 & 9 (and ideally 4 & 17) to « *L’argument principal* » (12 or 14 chapters); (b) rename the path « *Traversée rapide* » and warn that P4–P5 and single-shot decisions are skipped.
    - *Recommendation:* **(a)** with ch. **4, 8, 9, 17** added (or at minimum **8 & 9** if keeping a shorter path, renaming it under (b)).
14. **`V0-008` (`CONFIRME`, B) — Redundancy & length of § 0.7 (`00-cartographier.md` l. 175–196)**
    - *Alternatives:* (a) Condense § 0.7 (~980 words) into a compact chapter-by-chapter table (`~250` words) or five 3–4 line part paragraphs without premature jargon; (b) keep § 0.7 detailed and strip only undefined terms (`V0-010`).
    - *Recommendation:* **(a)** — cuts ~700 redundant words right before Part I, coordinated with `VX-034`.
15. **`VX-034` (`CONFIRME`, B, merged `V2-004`) — Redundancy of the 5 part-opening pages (`partie-1.md`..`partie-5.md`, 3,831 words)**
    - *Alternatives:* (a) Condense each part page to ~150–250 words (guiding question + 1 sentence per chapter locating its role, dropping end-of-part previews of the next part, modeled on `V5-017`); (b) keep detailed part pages and trim chapter intros/closings instead.
    - *Recommendation:* **(a)** — saves ~2,500 words and removes the triple-bridge repetition at every part boundary.
16. **`V5-044` (`PLAUSIBLE`, B) — Length & repetition in Conclusion (`99-conclusion.md`, ~5,900 words)**
    - *Alternatives:* (a) Keep § 2 self-contained (applying only the `V5-034` *Genèse* cut) while tightening the 5 *Points clés* to one sentence each; (b) also halve § 2.1–2.6 by cross-referencing ch. 8, 9, 16.
    - *Recommendation:* **(a)** plus targeted **(b)** on the repeated ferrure & `10 % × 1 %` recaps in § 2.2–2.3.

---

## 3. Quick Decisions (`G2` — 89 Active Clusters: 56 Confirmed, 33 Plausible)

**23 `CONFIRME` G2 clusters already have exact patches in `relecture/sorties/synthese/corrections.json`** (marked `[JSON]` in `SYNTHESE_RELECTURE_2026-11-20.md` § 4). Below are the highest-impact G2 items requiring explicit author sign-off or choice; see `SYNTHESE` § 4 for the complete file-by-file checklist with empty `Décision :` lines.

| Cluster | Status / Sev. | File(s) | Issue & Alternatives | Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **`VX-001`** (+`V0-025`) | `CONFIRME` B `[JSON]` | `00-cartographier.md` (§ 0.5.4) | Teaser `10%×1%` vs `1%×90%` creates expectation that shared models always raise risk, clashing with Table 16.1 (`5.57% → 1.93%`). Alternatives: qualify teaser as conditional possibility (`[JSON]` patch) + decide on adding a column to Table 16.1 (`V4-019`). | Accept `[JSON]` patch + see `V4-019` below. |
| **`V4-019`** | `CONFIRME` B | `16-angles-morts-collectifs.md`, `partie-4.md` | Despite `P1.1`, § 16.1 title, PC 1, and `partie-4.md:9` assert escape rises unconditionally while Table 16.1 net risk falls. Alternatives: (a) make title/PC/part conditional (*Quand le taux d'erreur baisse mais que les causes partagées dominent…*); (b) also add a high-`c`/moderate-$P(\text{faux})$ column (e.g. $6{,}5\,\%$) to Table 16.1 where net risk rises. | **(a)** mandatory; consider **(b)** only if willing to regenerate `ch16-modele-partage.md`. |
| **`V4-023`** | `CONFIRME` B | `16-angles-morts-collectifs.md` (§ 16.4), `partie-4.md` | § 16.4 states institutional volume-reward dynamics without source/status. Alternatives: label explicitly as *hypothèse de travail* (and soften `partie-4.md:9`), or add empirical citation. | Label as *hypothèse de travail*. |
| **`V4-011`** | `CONFIRME` B | `15-erosion-verifications.md` (§ 15.4 l. 92) | Despite `P1.11.3`, « texte déjà rédigé » exception still clashes with strict « *problème nu* » summaries. Alternatives: (a) remove the exception; (b) explicitly flag it as a degraded fallback in intro & *Points clés*. | **(b)** (honest practical fallback without breaking summaries). |
| **`V4-013`** | `CONFIRME` B | `15-erosion-verifications.md` (l. 52, 60) | Attributes « *équilibre mélangeant* » to Akerlof 1970 and conflates initial pooling (Spence) with dynamic unraveling (Akerlof). Alternatives: drop attribution to Akerlof in l. 52 and distinguish Spence vs. Akerlof in the box (as `VX-025` does in Annex A). | Apply distinction (consistent with `VX-025`). |
| **`V3-033`** | `CONFIRME` B | `13-synthese-deux-axes.md` (§ 13.1) | Despite `P1.3`, « *cadre* » shifts to task/prompt frame and Table 13.1's gradual border for learned components is only admitted in Conclusion l. 63. Alternatives: own the « task frame » extension explicitly in § 13.1 and state upfront that the row boundary is a matter of degree. | Apply in § 13.1. |
| **`V3-039`** | `CONFIRME` B | `13-synthese-deux-axes.md` (§ 13.2.4) | Says the world has no own frame (l. 120), then places compilers/tests (formal frames) inside it (l. 122). Alternatives: separate physical/clinical/institutional world (no frame) from software execution environments (real test within a formal frame) at start of § 13.2.4. | Apply split in § 13.2.4. |
| **`V3-020`** | `CONFIRME` B | `12-autre-regime.md` (§ 12.1, PC 2), `partie-3.md` | Makes lack of written spec the sole criterion of regime change, whereas § 12.2 notes old statistical filters also lacked specs. Alternatives: cite the conjunction *no written spec + generalist/composable use* in § 12.1, PC 2, and `partie-3.md`. | Apply conjunction. |
| **`V3-015`** | `CONFIRME` C | `11-regle-tiree-des-donnees.md` (§ 11.4) | Post-training section omits RL on verifiable rewards (code/math), which embeds a mechanical comparator and bridges to ch. 12. Alternatives: add 2 sentences in § 11.4; or leave as is. | Add 2 sentences in § 11.4. |
| **`VX-011`** | `CONFIRME` B | Ch. 2, 5, 13, 17, 18 (`fauriat2026frame`) | Self-citation `[@fauriat2026frame]` appears 36 times, sometimes for classic distinctions (aleatoric/epistemic in § 5.2, V&V in § 13.3, 2008 crisis in § 5.3). Alternatives: add standard primary citations (e.g., Der Kiureghian & Ditlevsen 2009 / Hora 1996; Oberkampf & Roy / IEEE V&V) and trim redundant `fauriat2026frame` tags. | Add primary citations & trim redundant tags. |
| **`VX-002`** | `CONFIRME` B | `17-decisions-sans-appel.md`, `A-outils.md`, `C-notation.md`, `D-parametres.md` | Symbol $z$ is a physical variable in ch. 5/7 ($Y=g(x,z)$) and a probability in ch. 17/A.4.2/C ($p_w = 1-(1-p)(1-z)$). Alternatives: (a) rename probability $z \to p_z$ across ch. 17, A.4.2, D.3, scripts; (b) keep $z$ and document both senses explicitly in ch. 17 and Annex C (`registre_termes.md`). | **(b)** if avoiding script/figure churn; **(a)** is cleaner long-term. |
| **`VX-018`** & **`VX-021`** | `CONFIRME` B/C | `A-outils.md`, `C-notation.md`, `registre_termes.md` | Letters ($E, A, D, B, H, c, f, m, \alpha$) shift meaning across chapters and Table C (15 rows) omits $\Lambda, S(p), \mathrm{VPP}, R, P(\text{faux}), C/\bar C, D, U_{\text{sûr}}$. Alternatives: add local scope notes in A & C (renaming $c(a,\omega) \to u(a,\omega)$ in A.4), complete `registre_termes.md`, and say « *les principaux symboles* » in A.1. | Apply both. |
| **`V0-012`** (+`V5-016`) | `CONFIRME` C | `00-cartographier.md` (§ 0.7), `08-independance-chaines.md` | Despite `N3`, 4 readers stumble on `M3 → M1 → M2` order. Alternatives: (a) remove `M1–M3` labels from § 0.7 (describe models in chapter order) and explain in ch. 8 why M1 is numbered first; (b) renumber M1/M2/M3 globally. | **(a)** — zero cross-reference churn. |
| **`V0-003`**, **`V0-014`**, **`V0-022`**, **`V0-024`** | `CONFIRME` B/C | `00-cartographier.md` | Qualify METR (0.1, 0.5.2) as a dated illustration; update *Parcours critique* list in Table 0.1; clarify « *niveau situé dessous* » in 0.6; mark recurring-example chapter lists as « *notamment…* ». | Apply all 4. |
| **`V5-023`**, **`V5-024`**, **`V5-004`** | `CONFIRME`/`PLAUSIBLE` B/C | `18-remede-trois-niveaux.md`, `17-decisions-sans-appel.md` | Add proposition backing & limits for Level 2 (§ 18.2); trim capping duplication (§ 18.3.1 → § 18.2.4); add practical rule « set $b$ before checking $p+b < p^\ast$ » (§ 17.2). | Apply `V5-023` and `V5-024`; consider `V5-004`. |

*(Also review the 23 `[JSON]` G2 items in `SYNTHESE` § 4 — including `V1-005`, `V1-006`, `V1-011`, `V1-013`, `V1-021`, `V1-022`, `V2-001`, `V2-002`, `V2-024`, `V2-030`, `V2-042`, `V3-006`, `V3-008`, `V3-038`, `V4-021`, `V5-005`, `V5-017`, `V5-020`, `V5-036`, `V5-037`, `V5-039` — before batch-applying `corrections.json`.)*

---

## 4. Direct Fixes (`G1` — 124 Active Clusters: 112 Confirmed, 12 Plausible)

1. **Ready JSON patches (`relecture/sorties/synthese/corrections.json`):**
   - Contains **160 verified non-overlapping patches** (`135` from **107 `CONFIRME` G1** clusters + `25` from **23 `CONFIRME` G2** clusters), ordered per `monographie/livre.yaml`.
   - Recommendation: Apply the `G1` patches directly once any overlapping `G2`/`G3` choices are settled (note: `V5-002` in `partie-5.md:5` is subsumed if `V5-017` is accepted; otherwise apply `V5-002` manually to `partie-5.md:5`).
2. **5 `CONFIRME` G1 clusters NOT in `corrections.json` (manual/script work):**
   - **Generator scripts (then run `make figures`):**
     - `V1-012`: `monographie/scripts/fig_seu.py` l. 43 → remove « (sans facteur omis) » in `tableaux/ch04-seuil.md`.
     - `V3-028` (`P1.10.2` backlog): `monographie/commun/parametres.py` l. 128 → change `'une autre date'` to `'5 mars'` in `tableaux/ch12-plausibilite.md`.
   - **Annex D (`monographie/annexes/D-parametres.md`) additions/table formatting:**
     - `VX-017`: add legend beneath Table D.3 recalling $p$, $L/\Delta U$, « fissure non repérée », and units of $b$ and $z$.
     - `VX-030`: define « Part indépendante » = $q = 0\,\%$ beneath Table D.4.
     - `VX-031`: harmonize displayed decimal precision (or add note) in Table D.3.
3. **12 `PLAUSIBLE` G1 clusters (optional):**
   - `V0-026`, `V0-028`, `V1-024`, `V1-025`, `V1-028`, `V3-014`, `V3-023`, `V4-010`, `V5-010`, `V5-030`, `VX-009` (all 11 have optional patches in `relecture/sorties/verification/V*.json`), plus `VX-024` (harmonize « alerte à tort » vs « fausse alerte » across ch. 12 & tables, no patch). Accept or skip individually.

---

## 5. Redundancy Cuts, Orthogonal Audits & Blind Spots

1. **Coordinated Redundancy Plan (`SYNTHESE` § 6):**
   - **4 recurring case studies (`VX-005`):** keep full narrative once (METR in **§ 15.2**; Mata v. Avianca in **§ 11.3**; MCO in **§ 8.6** + `.cas` in **§ 10.5**; Challenger in **§ 6.3**) and reduce all other occurrences (especially § 0.1 vignettes, § 5.5 Nuance, § 10.5 prose `V3-008`, § 12.1/14.3 reminders) to 1–4 line hooks/cross-references.
   - **Running examples (`VX-004`, `V1-005`, `V1-006`, `V1-022`):** keep boiling table full in § 2.2 (salt/altitude only in § 1.2), trim ch. 3/4 sailing repetition, trim ferrure recaps outside § 5.4 / § 8.2.
   - **Structural transitions (`VX-034`, `V0-008`, `V2-052`, `V4-002`, `V4-024`, `V5-024`, `V5-034`):** condense § 0.7 (~700 words saved) and the 5 part pages (~2,500 words saved), remove repeated 5-condition lists in ch. 8/9 headers, trim `8.4 → 14.1` and `14.2.3`/`16.1` setups, and reduce Conclusion *Genèse* to 3 lines.
2. **English Calques Audit (`monographie/notes/RAPPORT_AUDIT_CALQUES.md` — unapplied):**
   - Recurrent false friends (`tenir`, `attraper`/`rattraper`, `manquer`, `délivrer`, `dérivation`, `passer`), prepositional calques (`décider sur`, `agir sur une affirmation`, `conditionner sur`, `sous`, `à travers`, `oubli sur`, `vos propres contrôles`), Anglo punctuation (`—,`), and telegraphic figure/table labels.
   - *Recommendation:* apply selectively after content/redundancy cuts (keeping intentional technical choices like *exact* vs. *précis* in ch. 9).
3. **Second Style Pass (`TODO_ETAT_ACTUEL.md` `P5.2 [STY-P2]` — optional):**
   - Dense chapters (`ch00`, `ch13`, `ch14`, `ch15`, `ch16`, ~29–31 words/sentence).
   - *Recommendation:* run *after* structural cuts so you don't polish deleted prose.
4. **Wave 2 Blind Spots to Check Before Final Lock (`SYNTHESE` § 9):**
   - Inspect compiled **`monographie/figures/*.pdf`** visually (label overlap, alignment with tables, e.g. `fig_ch00_*`, `fig_ch06_*`, `fig_ch13_*`, `fig_ch18_*`).
   - Verify remaining **primary sources / bibliography** (`commun/biblio.bib`): Gary Klein 2007 premortem (`V5-020`), `nostalgebraist` 2020 logit-lens example (`V3-014`), primary aleatoric/epistemic & V&V citations (`VX-011`).
   - Walk through the **8 selective reading paths** (Table 0.1) on compiled HTML/PDF after updating `V0-001`.
   - Final **PDF typography & build checks** (`make verifier`, `make glossaire`, `make figures`, `make`, inspecting `build/livre-ecran.pdf`).

---

## 6. Recommended Execution Sequence

1. **Author Decisions (Phase 1):** Decide the **6 Severity-A** points (`V5-001`, `V2-029`, `V2-021`, `V2-039`, `V3-001`, `V3-030`), the remaining **16 `G3`** items in `SYNTHESE` § 3, and the **`G2`** items in `SYNTHESE` § 4 (marking `Décision :` lines).
2. **Shared Schemas & Generators (Phase 2):** Update `monographie/commun/registre_termes.md` (`VX-021`, `VX-022`, `VX-002`/`V2-023` if chosen), `monographie/commun/parametres.py` (`V3-028` and `V5-001`/`V4-019` if table changes chosen), `monographie/scripts/fig_seu.py` (`V1-012`), and `commun/biblio.bib` (`V5-020`, `VX-011`). Run `make figures` and `make glossaire`.
3. **Apply Vetted `corrections.json` + G3/G2/Annex D Edits (Phase 3):** Apply approved patches from `corrections.json` (filter out any rejected G2 items or superseded lines first), then apply manual `G3`/`G2` rewrites and the 3 Annex D edits (`VX-017`, `VX-030`, `VX-031`).
4. **Structural Redundancy Pass (Phase 4):** Execute the § 5.1 plan (`V0-008`, `VX-034`, `VX-005`, `V4-002`, `V2-052`, `V5-044`).
5. **Language & Style Polish (Phase 5):** Apply `RAPPORT_AUDIT_CALQUES.md` Priority 1–3 fixes and run targeted `P5.2 [STY-P2]` on dense chapters (`ch00`, `ch13`–`ch16`).
6. **Final Verification (Phase 6):** Run `make verifier` (expect 0 errors), rebuild `make` (`livre.html` / `livre-ecran.pdf`), visually inspect `figures/*.pdf`, and spot-check the updated Table 0.1 reading paths.
