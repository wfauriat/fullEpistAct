# Vérification — lot VX

## Bilan chiffré

- **Constats reçus :** 45 dans `entrees/VX.json`, plus 2 ajouts issus de `hors_perimetre.md` (`hp-p0-ancrage`) et `pistes/repetitions.md` (`piste-rep-genese`) ; les pistes de `pistes/termes.md` hors V0–V5 sur « vérification » rejoignent `C-018` (`VX-003`).
- **Grappes produites :** 36 (`VX-001` à `VX-036`), couvrant les 45 IDs d'entrée exactement une fois.
- **Répartition par verdict :** `CONFIRME` : 25 · `PLAUSIBLE` : 9 · `REJETE` : 2.
- **Répartition par gravité :** `A` : 0 · `B` : 16 · `C` : 20.
- **Répartition par groupe d'action :** `G1` : 22 · `G2` : 13 · `G3` : 1.

## Les problèmes les plus importants du lot

1. **Répétition *in extenso* de quatre études de cas (`VX-005`, `CONFIRME`, B, G2 — 3 lecteurs : C, P2, P3) :** *METR 2025* (0.1 et 15.2), *Mata v. Avianca* (0.1 et 11.3), *Challenger* (nuance 5.5 et étude de cas 6.4) et *Mars Climate Orbiter* (8, 10, 11, 12, 13) sont réexposés avec les mêmes détails en lecture linéaire (point déjà signalé dans `REV-3.1` / `P2.4`, non encore appliqué).
2. **Redondance structurelle des pages de partie et des ponts de frontière (`VX-034`, `CONFIRME`, B, G3 — T5) :** les 5 pages d'ouverture de partie (3 831 mots au total) résument chapitre par chapitre ce que disent 0.7, les chapeaux et les *Points clés*, et chaque frontière répète trois fois le même pont.
3. **Surcharge de la notation $z$ entre facteur omis et probabilité d'échec (`VX-002`, `CONFIRME`, B, G2 — C) :** $z$ est une variable au ch. 5 et au ch. 7 ($Y = g(x, z)$), mais une probabilité dans $[0, 1]$ au ch. 17, en A.4.2 et en C ($p_w = 1 - (1 - p)(1 - z)$).
4. **Incohérences internes de l'annexe A sur M2 et M3 (`VX-012` et `VX-013`, `CONFIRME`, B, G1 — PA) :** en A.4.2, le régime 4 ($p < p^\ast \le p + b$) inclut à tort « ou renoncement justifié si $p \ge p^\ast$ » ; en A.6, l'indépendance vis-à-vis de $e(x, z) = g(x, z) - f_1(x)$ suppose $f_1(x)$ déterministe sachant $x$ (même imprécision au ch. 7).
5. **Renvoi à vide de l'annexe D vers l'avant-propos et incohérences locales de D (`VX-014`, `VX-016`, `VX-019`, `CONFIRME`, B, G1 — PA, T2) :** D invoque un « principe de source unique posé dans l'avant-propos » absent de `00-avant-propos.md` ; D.3 attribue $z = 0$ aux trois situations du ch. 4 alors que la roulette russe porte $z = 1/6$ dans le tableau ; A.7.2 et D.4 notent $p$ le taux d'oubli $m$ du pair.
6. **Suremploi de l'auto-référence `[@fauriat2026frame]` (`VX-011`, `CONFIRME`, B, G2 — P5, T5) :** citée 36 fois, y compris pour des distinctions présentées comme classiques (aléatoire/épistémique en 5.2, vérification/validation en 13.3).
7. **Collisions de symboles entre chapitres et dans l'annexe A (`VX-018`, `CONFIRME`, B, G2 — PA, T2) :** $E$, $A$, $D$, $B$, $H$, $c$, $f$, $m$, $\alpha$ changent de sens sans note de portée locale en annexe C.

## Signaux sur des décisions antérieures

- **« Contrôles en chaîne » (`VX-007`, `C-026`, `DECISIONS_SYNTHESE V16`) :** V16 a adopté « met nos contrôles en chaîne » en partie V et au ch. 18, mais « met les étapes en chaîne » au ch. 0. Un lecteur neuf y relève à juste titre une contradiction avec le ch. 8 (où la chaîne assemble des composants/étapes, par opposition au contrôle croisé).
- **Répétitions des études de cas (`VX-005`, `TODO_ETAT_ACTUEL P2.4` / `REV-3.1`) :** le point avait été recensé et arbitré dans le journal des tâches, mais les doublons subsistent dans le texte figé.
- **Vérification / état de vérification (`VX-003`, `C-018`, `DECISIONS_SYNTHESE V2`) :** V2 a figé « état de vérification » au ch. 18 ; le lecteur C continue d'y voir un recouvrement avec la validation.

## Rejets : motifs récurrents

Deux rejets nets seulement (`VX-015` et `VX-033`), dus à :
- une méprise sur le périmètre des artefacts générés (`PA-004` : le ch. 0 ne contient aucun tableau ni figure issus de `parametres.py`, seul un calcul en prose reprend `ch09-taux-echappement`, ce que D.5.1 précise) ;
- un artefact de conversion du dossier d'extraits (`T1-023` : « Points clés » doublé aux ch. 3 et 14 dans l'extrait de T1, alors que les sources Markdown n'ont qu'un seul titre).

## Vérification des points de `hors_perimetre.md`

- **Points confirmés comme corrects dans le livre :**
  - Les modèles M1 (ch. 8–9), M2 (ch. 4, 17) et M3 (ch. 7) ainsi que les propositions 1–5 figurent bien aux chapitres annoncés ; les chiffres des voiliers (5 %, 0,1 %, rapport 25) concordent entre ch. 3, 4 et 17.
  - Les entrées bibliographiques vérifiées (`russell1912` et `russell2021`, `mco1999`, `rogers1986`, `tufte1997`, `mata2023`, `moffatt2024`, `sec2013knight`, `stockman2019`, `wu2022`) ont été auditées et corrigées lors de la passe `P5.1a`/`P5.1b` (`TODO_ETAT_ACTUEL.md`) ; `biblio_a_verifier.bib` est vide.
  - Le ch. 6 (l. 29) annonce bien l'élargissement des trois familles de comparateurs en quatre sources au ch. 13 ; le ch. 14 (l. 43) ne présente pas *Knight Capital* comme un modèle de langage ; le ch. 16 (l. 53) explique explicitement la baisse du risque (1,93 % contre 5,57 %) ; l'avant-propos (l. 58) distingue bien définitions structurantes et cinq propositions principales ; le glossaire concorde avec le texte sur *dérive de distribution*, *sévérité* et *vérification* (sous réserve de `C-018`).
- **Points ayant donné lieu à une grappe :**
  - `P0 § 4` (ancrage de l'*arrière-plan tacite* attribué au ch. 2 en 0.7 alors qu'il est introduit au ch. 1) $\rightarrow$ **`VX-035`** (`CONFIRME`, C, G1).
  - Les questions de `C`, `P1`, `P4`, `PA` et `T2` sur les annexes C et D ($z$, $p$, $m$, $\Lambda$, $S$, $A$, $D$) rejoignent les grappes **`VX-002`**, **`VX-008`**, **`VX-018`**, **`VX-019`**, **`VX-021`**.

## Remarques pour la synthèse

- Les grappes **`VX-002`** ($z$), **`VX-006`** (*dix fois plus exact*), **`VX-007`** (*contrôles en chaîne*), **`VX-011`** (`fauriat2026frame`), **`VX-018`** (collisions de notations) et **`VX-034`** (pages de partie et transitions) touchent l'ensemble des lots V0–V5 et devront être appliquées de façon coordonnée si elles sont retenues.
- Plusieurs pistes de `RAPPORT_AUDIT_CALQUES.md` (notamment `décider sur`, `conditionner sur`, `attraper`) restent ouvertes hors de ce lot et sont déjà recensées dans ce rapport.
