# Contrôle de portée — `08-independance-chaines`

- Original : `/home/ai-user/Documents/Sandbox/review_epist_ag/style/lots/08-independance-chaines/original.md`
- Réécriture : `/home/ai-user/Documents/Sandbox/review_epist_ag/monographie/chapitres/08-independance-chaines.md`
- Généré le 2026-11-20 par `style/diff_portee.py` (STYLE_PASS_SPEC.md, §6.3)

**Mode d'emploi.** Pour chaque case : la cocher et écrire après « décision : » *accepté* ou *rétabli* (avec, au besoin, la formulation retenue). `python3 style/diff_portee.py --controle <ce fichier>` échoue tant qu'une case reste vide. ⛔ = invariant de la spec touché ; ⚠ = portée ou contenu possiblement modifié. Les éléments · (reformulation à effectif constant, variantes morphologiques, mots ajoutés) sont à parcourir et ne demandent pas de décision.

**Bilan :** 0 décision(s) à prendre — ⛔ 0 · ⚠ 0 ; 2 élément(s) · à parcourir

## Synthèse par section

| Section | ⛔ | ⚠ | · |
| :-- | --: | --: | --: |
| `sec:ch08` Indépendance, chaînes et contrôles croisés |  |  |  |
| `sec:ch08-serie-parallele` Boîte à outils : fiabilité en série et en parallèle |  |  |  |
| `sec:ch08-angles-morts` Les angles morts d’un composant |  |  |  |
| `sec:ch08-independance` L’indépendance est relative, et se paie en comparabilité |  |  | 1 |
| `sec:ch08-composer` Composer des étapes spécialisées |  |  |  |
| `sec:ch08-chaines-controles` Chaînes contre contrôles croisés |  |  | 1 |
| `sec:ch08-blanchiment` Le blanchiment aux interfaces |  |  |  |
| `titre:Points clés` Points clés |  |  |  |

## Invariants structurels (fichier entier)

Aucune différence : identifiants, renvois, attributs `statut` et clés de citation identiques.

## `sec:ch08-independance` — L’indépendance est relative, et se paie en comparabilité

- · Quantificateurs absolus — *tout / tous / toute(s)* : 8 → 8 (reformulé autour)
    - retiré : « … à se tromper autrement est nulle les deux exécutions partagent **tout** jusqu'à la moindre omission de cadre et ne contrôlent rien … »
    - ajouté : « … tromper autrement est nulle Les deux exécutions partagent en effet **tout** jusqu'à la moindre omission de cadre et ne contrôlent rien … »

## `sec:ch08-chaines-controles` — Chaînes contre contrôles croisés

- · Force de l'affirmation — *suffire* : 3 → 3 (reformulé autour)
    - retiré : « … qu'il reçoit pour se concentrer sur sa propre tâche il **suffit** qu'un seul maillon laisse passer une cause d'erreur qu'il ne … »
    - ajouté : « … qu'il reçoit pour se concentrer sur sa propre tâche Il **suffit** alors qu'un seul maillon laisse passer une cause d'erreur qu'il … »

