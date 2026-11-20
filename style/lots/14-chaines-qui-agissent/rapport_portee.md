# Contrôle de portée — `14-chaines-qui-agissent`

- Original : `/home/ai-user/Documents/Sandbox/review_epist_ag/style/lots/14-chaines-qui-agissent/original.md`
- Réécriture : `/home/ai-user/Documents/Sandbox/review_epist_ag/monographie/chapitres/14-chaines-qui-agissent.md`
- Généré le 2026-11-20 par `style/diff_portee.py` (STYLE_PASS_SPEC.md, §6.3)

**Mode d'emploi.** Pour chaque case : la cocher et écrire après « décision : » *accepté* ou *rétabli* (avec, au besoin, la formulation retenue). `python3 style/diff_portee.py --controle <ce fichier>` échoue tant qu'une case reste vide. ⛔ = invariant de la spec touché ; ⚠ = portée ou contenu possiblement modifié. Les éléments · (reformulation à effectif constant, variantes morphologiques, mots ajoutés) sont à parcourir et ne demandent pas de décision.

**Bilan :** 1 décision(s) à prendre — ⛔ 0 · ⚠ 1 ; 1 élément(s) · à parcourir

## Synthèse par section

| Section | ⛔ | ⚠ | · |
| :-- | --: | --: | --: |
| `sec:ch14` Des chaînes qui agissent |  |  |  |
| `sec:ch14-pipelines` Des *pipelines* d’IA comme chaînes orchestrées |  | 1 | 1 |
| `sec:ch14-agents` Les agents : quand les erreurs s’exécutent |  |  |  |
| `sec:ch14-chaine-n-maillons` Un danger structurel : la chaîne à $N$ maillons |  |  |  |
| `sec:ch14-reponses-actions` Un danger opérationnel : des réponses aux actions |  |  |  |
| `sec:ch14-trajectoire-longue` Chiffrer une trajectoire longue |  |  |  |
| `sec:ch14-blanchiment` Le blanchiment dans les chaînes d’IA |  |  |  |
| `sec:ch14-autorite-garanties` Autorité d’exécution et garanties inversées |  |  |  |
| `titre:Points clés` Points clés |  |  |  |

## Invariants structurels (fichier entier)

Aucune différence : identifiants, renvois, attributs `statut` et clés de citation identiques.

## `sec:ch14-pipelines` — Des *pipelines* d’IA comme chaînes orchestrées

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (2) — décision : 
    - *inexact* : « … relecture entre maillons Il serait toutefois **inexact** d'affirmer que tout pipeline est condamné … »
    - *affirmer* : « … entre maillons Il serait toutefois inexact **d'affirmer** que tout pipeline est condamné par … »
- · Quantificateurs absolus — *tout / tous / toute(s)* : 2 → 2 (reformulé autour)
    - retiré : « … ni relecture entre maillons Il serait toutefois inexact d'affirmer que **tout** pipeline est condamné par nature à demeurer une chaîne aveugle … »
    - ajouté : « … fractions de seconde sans pause critique ni relecture entre maillons **Tout** pipeline n'est toutefois pas condamné par nature à demeurer une … »

