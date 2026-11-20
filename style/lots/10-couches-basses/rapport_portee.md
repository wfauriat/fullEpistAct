# Contrôle de portée — `10-couches-basses`

- Original : `/home/ai-user/Documents/Sandbox/review_epist_ag/style/lots/10-couches-basses/original.md`
- Réécriture : `/home/ai-user/Documents/Sandbox/review_epist_ag/monographie/chapitres/10-couches-basses.md`
- Généré le 2026-11-20 par `style/diff_portee.py` (STYLE_PASS_SPEC.md, §6.3)

**Mode d'emploi.** Pour chaque case : la cocher et écrire après « décision : » *accepté* ou *rétabli* (avec, au besoin, la formulation retenue). `python3 style/diff_portee.py --controle <ce fichier>` échoue tant qu'une case reste vide. ⛔ = invariant de la spec touché ; ⚠ = portée ou contenu possiblement modifié. Les éléments · (reformulation à effectif constant, variantes morphologiques, mots ajoutés) sont à parcourir et ne demandent pas de décision.

**Bilan :** 0 décision(s) à prendre — ⛔ 0 · ⚠ 0 ; 2 élément(s) · à parcourir

## Synthèse par section

| Section | ⛔ | ⚠ | · |
| :-- | --: | --: | --: |
| `sec:ch10` Pourquoi l’on peut oublier les couches basses |  |  |  |
| `sec:ch10-boite-outils` Boîte à outils : les contrats logiciels |  |  |  |
| `sec:ch10-composition` Des opérations élémentaires à la composition |  |  | 1 |
| `sec:ch10-promesse-ecrite` Chaque couche est une promesse écrite |  |  | 1 |
| `sec:ch10-verification-amont` Vérifier une fois, avant l’usage |  |  |  |
| `sec:ch10-adresse-defaillance` Les défaillances ont une adresse |  |  |  |
| `titre:Points clés` Points clés |  |  |  |

## Invariants structurels (fichier entier)

Aucune différence : identifiants, renvois, attributs `statut` et clés de citation identiques.

## `sec:ch10-composition` — Des opérations élémentaires à la composition

- · Statut épistémique — *établir* : 1 → 1 (reformulé autour)
    - retiré : « … classique est composition de ces opérations élémentaires Or nous avons **établi** au qu'une longue suite d'étapes mises en série risque de … »
    - ajouté : « … classique est composition de ces opérations élémentaires Nous avons pourtant **établi** au qu'une longue suite d'étapes mises en série risque de … »

## `sec:ch10-promesse-ecrite` — Chaque couche est une promesse écrite

- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 6 → 6 (reformulé autour)
    - retiré : « … que l'interface laisse tomber ou relègue hors du périmètre contrôlé **peut** traverser les maillons sans alerte même au cœur d'un logiciel … »
    - ajouté : « … que l'interface laisse tomber ou relègue hors du périmètre contrôlé **peut** ainsi traverser les maillons sans alerte même au cœur d'un … »

