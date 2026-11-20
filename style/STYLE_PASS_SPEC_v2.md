# Spécification v2 — Passe stylistique sur la monographie (2026)

**Objet :** rendre la prose d’*Agir d’après une représentation du monde* (`monographie/chapitres/*.md`) plus lisible, plus rythmée et plus idiomatiquement française, **sans aucun changement de sens que l’auteur n’ait décidé**.

**Statut :** v2 du 2026-11-20, à valider par l’auteur. Remplace `style/STYLE_PASS_SPEC.md` (spécification initiale et ses amendements du §6), conservé comme trace.

**Sources :**
- `style/STYLE_PASS_SPEC.md` (spécification initiale et amendements) ;
- `style/CALIBRATION_PHASE1.md` (étalonnage, profil Option A) ;
- `style/COMPARAISON_2022_2026.md` (comparaison avec le livre de 2022) ;
- les rapports `style/rapports/diff_portee_00-*.md` sur les pilotes `style/pilots/`.

---

## 1. Principe directeur

La v1 confiait la réécriture à un modèle et la vérification à la seule relecture de l’auteur. Les pilotes ont montré que cela ne suffit pas (§2) :

- le modèle réécrit bien plus que ce qui est visé ;
- ses changements de sens sont fluides, donc plausibles à la relecture ;
- les contrôles mécaniques de la v1 (labels, statuts, citations, nombres) ne les voient pas.

C’est le mécanisme que le livre décrit au chapitre 15 : la forme ne signale plus le fond.

La v2 applique donc au chantier la méthode du livre. Toute retouche est arrêtée par plusieurs **comparateurs qui se trompent autrement** :

1. un rédacteur ne peut proposer que des retouches **déclarées**, **motivées** et **typées** ;
2. des **barrières mécaniques** vérifient ce qui se vérifie sans jugement ;
3. un **juge** d’une autre famille de modèles examine le sens, la ligne argumentative et le registre ;
4. un **script**, non un modèle, applique les retouches acceptées ;
5. l’**auteur** tranche ce qui reste et contrôle un échantillon.

L’efficacité du juge est elle-même **mesurée** par des erreurs injectées (§8.8), comme le livre le recommande au @sec:ch18.

**Critère de réussite d’un lot :**
- cibles chiffrées atteintes ou écarts justifiés (§9) ;
- **zéro changement de sens non décidé par l’auteur** ;
- probabilité d’échappement du juge mesurée sous le seuil fixé (§8.8).

---

## 2. Leçons des pilotes (2026-11-20)

| | Avant-propos | Chapitre 0 |
| :--- | ---: | ---: |
| Phrases d’origine conservées telles quelles | 17 % | 18 % |
| Phrases de moins de 25 mots réécrites (aucune règle ne les visait) | 68 % | 63 % |
| Longueur moyenne des phrases (avant → après) | 32,0 → 26,5 | 29,5 → 24,9 |
| Phrases ≥ 35 mots (avant → après) | 39 % → 23 % | 36 % → 18 % |
| Écart-type de la taille des paragraphes (devait monter) | 54 → 43 | 56 → 46 |
| Antithèses / 1 000 mots (devaient baisser) | 1,6 → 2,4 | 0,5 → 1,0 |
| Changements de sens relevés à la lecture | 4 | ≈ 20 |

**Types de dérive observés.** Ils servent de liste de contrôle au juge (§8.3) et de jeu d’étalonnage (§8.8) ; détail en annexe A.

1. **Jugement et fréquence confondus.** « le cas le plus probable » → « le plus fréquent ».
2. **Définition déplacée.** Calibration jugée sur « des jours comparables » au lieu des jours où la prévision a été émise.
3. **Possibilité changée en certitude.** « peut être pris en défaut » → « cédera ».
4. **Suffisance ajoutée.** « quatre questions… qui n’exigent aucune technicité » → « quatre questions simples suffisent ».
5. **Exigence impossible.** « ses hypothèses principales » → « ses hypothèses », alors que le livre soutient que l’arrière-plan est ouvert.
6. **Mécanisme substitué.** « assèchement » → « saturation » des capacités d’évaluation.
7. **Statut promu.** « réflexion » → « théorie » ; « arguments » → « démonstrations » ; « développé » → « établi ».
8. **Fait durci.** « doutes sur la trajectoire » → « alertes restées sans suite ».
9. **Termes du registre remplacés.** « frontière en dents de scie », « tests de référence », « probabilité d’échappement », « producteur / contrôleur ».
10. **Définitions, gloses ou liens retirés.** Facteurs du risque, « état de vérification », « raisonner à l’envers », lien vers la ferrure.
11. **Énumérations amputées.** « le mathématicien », « le décideur ».
12. **Provenance sur-affirmée.** « restés humains d’un bout à l’autre ».
13. **Propos central affaibli.** « une infinité » → « une foule ».

**Conclusion :** la dérive vient de la paraphrase non nécessaire. La v2 interdit toute retouche sans motif répertorié et vérifie mécaniquement les retouches les plus fréquentes.

---

## 3. Périmètre, prérequis et ordre des chantiers

### 3.1 Périmètre

- **Dans le périmètre :**
  - le texte principal des chapitres (`monographie/chapitres/*.md`) ;
  - les chapeaux d’ouverture et les transitions ;
  - le récit des encadrés `.cas` et `.nuance` ;
  - les « Points clés » (opérations A seulement, §6).
- **Hors périmètre (intouchés sauf faute matérielle manifeste) :**
  - encadrés `.formel` et `.outils` ;
  - énoncés `.proposition` et `.definition` ;
  - valeurs et tableaux des `.exemple-quantitatif` ;
  - tableaux de données ;
  - toute correction de fond (concept, chiffre, référence).

### 3.2 Prérequis, dans cet ordre

1. **Vérification des références.** `commun/biblio_a_verifier.bib` compte 60 entrées candidates, citées 183 fois ; `commun/biblio.bib` ne contient qu’une entrée vérifiée. Une source qui ne soutient pas sa phrase entraîne une correction de fond, qui doit précéder la passe de style.
2. **Fabrication (en parallèle).**
   - 10 « Figure à générer » ;
   - « au section » (ch. 7 et 17) ;
   - renvoi rendu « de la Vos propres contrôles » (ouverture du ch. 15) ;
   - en-tête courant de la conclusion (gabarit).
3. **Passe de fond (commits séparés).**
   - Tensions de `monographie/notes/REVIEW_PASS_LIVRE_ECRAN.md` (ch. 5, 13, 16, 17).
   - Apports de `COMPARAISON_2022_2026.md` :
     - la fève hors du gâteau pour l’incertitude ontologique (ch. 5, éventuellement §0.3.1) ;
     - l’exploration comme décision économique (ch. 7.5, 17).

   La passe de style harmonise ensuite le texte nouveau.
4. **Passe de style** selon la présente spécification, par Partie (§10).
5. **Recompilation et lecture continue** de `livre-ecran.pdf`.

---

## 4. Registre cible (profil Option A, verrouillé)

- **À conserver :**
  - architecture conceptuelle et ordre des dépendances ;
  - discipline terminologique (`monographie/commun/registre_termes.md`) ;
  - séparation entre texte principal et encadrés ;
  - statuts épistémiques et prudence des énoncés généraux ;
  - absence de guillemets de précaution.
- **À corriger :**
  - phrases-tunnels (30 à 50 mots en série) ;
  - deux-points aphoristiques en série et « Or » en tête de phrase ;
  - italiques d’emphase ;
  - antithèses symétriques non porteuses ;
  - chapeaux qui paraphrasent la table des matières ;
  - récits répétés d’un chapitre à l’autre ;
  - sujets nominaux abstraits ;
  - formules diplomatiques creuses ;
  - calques de l’anglais.
- **Gradient de ton :**
  - avant-propos, ch. 0 et conclusion : clair, direct, posé ;
  - ch. 1 à 9 : sobre et fluide, les exemples portent les distinctions ;
  - ch. 10 à 18 : fermeté analytique, accent sur les mécanismes réutilisables.
- **À ne pas importer du livre de 2022 :** fiction et dialogues, guillemets distanciateurs, notes envahissantes, relâchement orthotypographique, prédictions, ton péremptoire.
- **« Je » :** au plus dans « Genèse et responsabilité ». Ailleurs, « nous » ou la troisième personne.
- **Finalité :** la lisibilité et la clarté des mécanismes. La passe ne vise pas à rendre le texte moins reconnaissable comme produit avec des modèles. La divulgation de provenance reste exacte (I7).

---

## 5. Invariants (non négociables)

| N° | Invariant | Contrôlé par |
| :--- | :--- | :--- |
| I1 | Aucun titre `#` de chapitre, identifiant (`#sec:`, `#prop:`, `#def:`, `#eq:`, `#fig:`, `#tbl:`) ni attribut `statut="…"` modifié | barrières (§8.2), `diff_portee.py` |
| I2 | Aucun terme du registre remplacé par un synonyme ; aucune mise en **gras** déplacée hors du chapitre introducteur | barrières, `diff_portee.py`, juge |
| I3 | Aucune clé de citation modifiée, retirée, ajoutée ou détachée de la donnée qu’elle soutient | barrières, `diff_portee.py` |
| I4 | Aucun nombre modifié dans la prose ni dans un bloc protégé | barrières, `diff_portee.py` |
| I5 | Ordre des dépendances et règle du texte principal respectés (l’argument se lit sans les encadrés `.outils`, `.formel`, `.nuance`, `.question`) | juge, auteur |
| I6 | Portée et force inchangées : modaux et atténuateurs, quantificateurs, négations, conditions et restrictions, verbes et noms de statut, vocabulaire des probabilités, contenu des énumérations | barrières (opérations A), juge, `diff_portee.py` |
| I7 | Énoncés de provenance (« Genèse et responsabilité », « Une provenance déclarée ») modifiés seulement par l’auteur, ligne à ligne | barrières (zone verrouillée) |
| I8 | Blocs protégés (§3.1) identiques à l’octet près | barrières, `diff_portee.py` |
| I9 | **Aucune retouche sans motif répertorié** (§6) : une phrase non ciblée reste identique | barrières |

---

## 6. Catalogue des opérations

Le rédacteur ne peut proposer que les opérations ci-dessous. Toute autre retouche est rejetée par les barrières.

### 6.1 Opérations A — conservatrices, vérifiées mécaniquement

| Code | Opération | Ce qui peut changer | Contrôle mécanique |
| :--- | :--- | :--- | :--- |
| A1 | Couper une phrase ciblée | ponctuation ; ajouts de la liste W ; répétition d’un mot plein déjà présent dans la phrase | conservation (ci-dessous) ; coupure interdite dans la portée d’une condition |
| A2 | Remplacer des deux-points ou un « Or » initial | le connecteur, pris dans la table T | conservation ; connecteur ∈ T |
| A3 | Retirer une italique d’emphase | `*x*` → `x` (jamais un terme étranger, un titre ni un énoncé de question) | texte identique hors balisage |
| A4 | Couper ou fusionner des paragraphes | sauts de ligne | texte identique hors sauts de ligne |

**Règle de conservation (A1, A2).** Pour l’unité retouchée (la phrase d’origine et la ou les phrases qui la remplacent) :

- **mots pleins identiques** (en multiensemble), à deux exceptions près : la répétition d’un mot plein déjà présent, et les mots de la liste W ;
- **mêmes effectifs** de :
  - négations (*ne, n’, pas, plus, jamais, aucun, rien, nul, ni, sans, non*) ;
  - modaux et atténuateurs ;
  - quantificateurs ;
  - vocabulaire des probabilités et mots de statut (familles de `diff_portee.py`) ;
  - nombres, clés de citation, renvois et termes du registre ;
- **coupure interdite** dans la portée d’une subordonnée de condition ou de restriction, sauf escalade vers l’auteur : *si, lorsque, quand, tant que, pourvu que, à condition que, dès lors que, sauf si, à moins que, ne… que*. Couper « Si A, B et C » en « Si A, B. C. » rend C inconditionnel.

**Liste W (ajouts permis)** :
- pronoms *il, elle, ils, elles, on, ce, cela, ceci, celui-ci, celle-ci, ceux-ci, celles-ci* ;
- déterminants ;
- *est, sont, c’est* ;
- connecteurs de la table T.

**Suppressions permises :**
- *Or*, *et* de coordination, relatifs (*qui, que, dont, lequel…*), *ce qui* ;
- ponctuation ;
- balisage d’emphase.

**Table T (connecteurs selon la relation des deux-points).** Un deux-points qui introduit une liste ou une définition reste tel quel.

| Relation | Connecteurs |
| :--- | :--- |
| explication, justification | *car, en effet* |
| conséquence | *si bien que, donc, d’où, aussi* (inversion) |
| restriction, condition | *encore faut-il que, reste que, toutefois* |
| illustration | *ainsi, par exemple* |
| parallèle | *de même* |
| opposition | *mais, en revanche, pourtant* |

### 6.2 Opérations B — réécritures libres ciblées (juge + auteur)

| Code | Opération | Limite |
| :--- | :--- | :--- |
| B1 | Chapeau d’ouverture → accroche de 2 ou 3 phrases posant le problème réel | une par chapitre ; conserve les prérequis nommés |
| B2 | Antithèse non porteuse → assertion simple ou causale | au plus 2 antithèses conservées par section ; jamais une antithèse qui porte un énoncé du registre ou d’une proposition |
| B3 | Sujet nominal abstrait → sujet concret et verbe d’action | — |
| B4 | Formule diplomatique creuse (« Il serait erroné de voir… ») → position nette | jamais une réserve épistémique réelle, c’est-à-dire tout ce qui porte un statut, une condition ou une limite |
| B5 | Récit répété → rappel de 1 ou 2 phrases avec renvoi | selon la table d’ancrage (§9.2) |
| B6 | Pont d’annonce redondant supprimé (« ce sera l’objet du @sec:… ») | seulement si l’ouverture du chapitre visé fait déjà le lien |

**Plafond :** au plus **3 opérations B par section** (B5 non compris). Au-delà, la section est proposée en entier à l’auteur.

### 6.3 Interdits

- Reformuler une phrase sans motif répertorié, par exemple remplacer un mot par un synonyme « plus élégant ».
- Retoucher un exemple, un fait, une date, un acteur, un chiffre ou ce qu’une source dit.
- Retoucher une zone verrouillée (I7) ou un bloc protégé (I8).
- Fusionner deux retouches en une, ou proposer une retouche qui couvre plusieurs paragraphes (hors B1 et B5).

### 6.4 Phrases ciblées

`audit_style.py --cibles` (à écrire, §11) produit, par chapitre, la liste des phrases visées avec leur motif :

- `phrase-longue` (≥ 35 mots) ;
- `deux-points-serie` ;
- `or-initial` ;
- `italique` ;
- `antithese` ;
- `chapeau` ;
- `recit-repete` ;
- `formule-diplomatique` ;
- `sujet-abstrait` (repérage heuristique, confirmé par le rédacteur).

Les opérations A1 à A3 et B2 à B4 ne portent que sur ces phrases ; A4 porte sur la structure des paragraphes.

---

## 7. Formats

### 7.1 Propositions du rédacteur (`style/lots/<chapitre>/propositions.yaml`)

```yaml
chapitre: 00-cartographier
redacteur: <famille, modèle, version>
modifications:
  - id: ch00-017
    section: sec:ch00-auto-verification
    operation: A1
    motif: phrase-longue
    avant: "Encore faut-il que le facteur omis ait effectivement varié … dès que ce facteur change en exploitation."
    apres: "Encore faut-il que … d’enregistrer. Un essai de charge … de brouillard salin. De même, un modèle statistique … en exploitation."
    note: "Coupe aux deux-points et à la coordination ; « De même » (table T, parallèle)."
```

`avant` doit apparaître **exactement une fois** dans le chapitre. Le rédacteur ne produit jamais un chapitre réécrit.

### 7.2 Verdicts du juge (`style/lots/<chapitre>/verdicts.yaml`)

```yaml
juge: <famille, modèle, version>
verdicts:
  - id: ch00-017
    verdict: accepte        # accepte | rejete | auteur
    dimensions: []          # sens, portee, statut, probabilites, terme, fait, argument, registre, francais, gain
    raison: ""
```

---

## 8. Pipeline

### 8.1 Étape 0 — Préparation (script)

Pour chaque chapitre, le dossier `style/lots/<chapitre>/` reçoit :

- la liste des phrases ciblées (§6.4) ;
- une **fiche de contexte** :
  - termes du registre introduits ou employés dans le chapitre ;
  - énoncés des propositions et définitions du chapitre ;
  - lignes correspondantes du tableau des statuts de la conclusion ;
  - exemples courants concernés (`commun/exemples_courants.md`) ;
  - ancrages de récits (§9.2) ;
- la mesure de référence (`audit_style.py`).

### 8.2 Étape 1 — Rédacteur (modèle R)

R reçoit :
- le chapitre ;
- la fiche de contexte ;
- la liste des cibles ;
- les §4 à §6 de la présente spécification.

Il produit `propositions.yaml`, avec au plus une retouche par phrase ciblée.

### 8.3 Étape 2 — Barrières mécaniques (`appliquer_edits.py --verifier`)

Pour chaque retouche, le script vérifie :
- unicité de `avant` ;
- opération et motif autorisés ;
- phrase ciblée ;
- règle de conservation (A1, A2) ou identité hors balisage (A3, A4) ;
- invariants I1 à I4, I7 et I8 ;
- plafonds.

Une retouche qui échoue est rejetée avec sa raison, sans passer au juge. Les barrières coûtent peu, sont déterministes et ne partagent pas les angles morts d’un modèle.

### 8.4 Étape 3 — Juge (modèle J)

**Indépendance :**
- J appartient à une **autre famille de modèles** que R ;
- sa consigne est rédigée par l’auteur ou le mainteneur, non par R ;
- **J ne réécrit jamais.**

**Protocole par retouche :**
1. J lit `avant` et `apres` dans leur paragraphe, avec la fiche de contexte, **sans le motif ni la note de R**, et rend un premier verdict. Il forme ainsi son propre jugement avant de lire celui du producteur (cf. @sec:ch15).
2. J lit ensuite le motif. Ce motif ne peut servir qu’à **rejeter** une retouche qui ne tient pas son motif, jamais à accepter un changement de sens.
3. **En cas de doute, J rejette ou escalade vers l’auteur.** Un rejet coûte une retouche manquée ; une acceptation à tort coûte un changement de sens.

**Liste de contrôle du juge** (une dimension par question) :

1. **sens** — Le nouveau texte dit-il la même chose, ni plus ni moins, dans les deux sens ? Tout ce que dit l’ancien est-il dit, et le nouveau n’ajoute-t-il rien ?
2. **portée** — Modaux, quantificateurs, négations, conditions et restrictions : sont-ils présents, et portent-ils sur le même segment ?
3. **statut** — Rien n’est-il promu (réflexion → théorie, argument → démonstration, suggère → montre, hypothèse → résultat) ni rétrogradé ?
4. **probabilités** — Jugement et fréquence restent-ils distincts ? La série sur laquelle on juge une prévision est-elle inchangée ?
5. **terme** — Aucun synonyme ne remplace un terme du registre, et aucune définition ni glose n’est retirée ?
6. **fait** — Aucun détail factuel n’est-il ajouté, durci ou retiré (dates, acteurs, chiffres, ce que dit la source) ?
7. **argument** — La phrase joue-t-elle le même rôle dans le paragraphe ? Les liens de cause, de concession et de condition, ainsi que les renvois aux exemples courants, sont-ils préservés ?
8. **registre** — Le ton reste-t-il sobre (Option A), sans péremption, sans formule, sans anglicisme ?
9. **français** — La phrase est-elle correcte et idiomatique ?
10. **gain** — La retouche améliore-t-elle réellement ce que vise son motif ? Sinon, la rejeter : pas de retouche gratuite.

### 8.5 Étape 4 — Révision unique

Les retouches rejetées par le juge retournent **une fois** à R avec la raison. Les nouvelles versions repassent les étapes 2 et 3. Une retouche encore rejetée est abandonnée : **le texte d’origine reste**. Aucun modèle ne « corrige » de lui-même une retouche rejetée, car ce serait une réécriture de plus, non contrôlée.

### 8.6 Étape 5 — Application déterministe (`appliquer_edits.py --appliquer`)

Le script applique les retouches acceptées par simple remplacement. **Aucun modèle n’intervient à cette étape.**

### 8.7 Étape 6 — Filet et décision de l’auteur

1. `diff_portee.py ORIGINAL RÉSULTAT` produit le rapport ; `audit_style.py` mesure le chapitre ; `make verifier` passe.
2. **L’auteur tranche :**
   - toutes les escalades du juge ;
   - **toutes les opérations B** ;
   - tous les éléments ⛔ et ⚠ du rapport ;
   - un **échantillon tiré au hasard de 10 % des opérations A acceptées**.
3. L’auteur lit le chapitre en continu, à voix haute pour les zones clés.
4. **Porte de fusion :** `diff_portee.py --controle` passe et les cibles du §9.1 sont atteintes ou leurs écarts justifiés.

**Charge estimée.** Pour un chapitre comme le ch. 0 : de l’ordre de 30 à 40 décisions, contre 83 cases pour le pilote actuel. Ce chiffre est à vérifier sur le premier lot.

### 8.8 Étape 7 — Mesure du juge par erreurs injectées

**Étalonnage avant production.** Le jeu d’étalonnage réunit :
- les **≈ 25 dérives connues** des pilotes (annexe A) ;
- **≈ 25 retouches jugées acceptables** par l’auteur sur les mêmes passages.

J doit **rejeter ou escalader au moins 90 % des dérives** et ne pas rejeter plus de **25 % des retouches acceptables**. Ces seuils sont proposés, à valider par l’auteur. Sinon, revoir la consigne ou changer de juge.

**En production :**
- environ **5 % des retouches soumises à J sont des dérives injectées**, indiscernables des autres ;
- elles sont construites hors du cadre de R et de J (par l’auteur, ou par un troisième modèle à partir des types de l’annexe A) ;
- elles sont retirées avant application ;
- la **probabilité d’échappement** du juge est calculée par lot. Au-delà de **10 %**, le lot est arrêté et le juge réétalonné.

---

## 9. Cibles et ancrages

### 9.1 Cibles chiffrées (`audit_style.py`, texte principal)

**Référence avant passe :**
- moyenne 27,4 ± 13,5 mots ; phrases ≤ 10 mots : 9,1 % ;
- ch. 0 et 13 à 16 : 29,5 à 32,1 mots de moyenne, jusqu’à 37 % de phrases ≥ 35 mots.

| Indicateur | Ch. 0 et 10–16 | Ch. 1–9, 17–18, conclusion |
| :--- | :--- | :--- |
| Longueur moyenne des phrases | ≤ 25 mots | ≤ 24 mots |
| Phrases ≥ 35 mots | ≤ 20 % | ≤ 15 % |
| Phrases ≤ 10 mots | ≥ 10 % | ≥ 12 % |
| Écart-type de la taille des paragraphes | ≥ valeur avant passe | ≥ valeur avant passe |
| Antithèses, italiques, deux-points, tirets (/ 1 000 mots) | ≤ valeur avant passe | ≤ valeur avant passe |

- **Plancher :** ne pas descendre sous ~20 mots de moyenne sur un chapitre (profil du livre de 2022).
- **Écarts :** un écart est justifié dans le message de commit.
- **Limite :** atteindre les cibles ne valide rien en soi.

### 9.2 Table d’ancrage des récits récurrents (proposition, à arrêter par l’auteur)

| Récit | Fichiers où il apparaît | Ancrage | Ailleurs |
| :--- | :--- | :--- | :--- |
| Mars Climate Orbiter | ch. 0, 8, 10, 11, 12, 13, 14, conclusion | récit au ch. 0, analyse au ch. 10 | rappel en 1 ou 2 phrases avec renvoi |
| *Mata v. Avianca* | ch. 0, 11, 13 | récit au ch. 0, analyse au ch. 11 | rappel au ch. 13 |
| METR (2025) | ch. 0, 15 | encadré au ch. 15 | une phrase et un renvoi au ch. 0 |

Les exemples courants (voiliers, eau bouillante, ferrure, dinde, Challenger, pluie à 70 %) reviennent par construction. B5 ne vise que les re-narrations.

---

## 10. Déroulé

1. **Outillage** (§11) et **étalonnage du juge** (§8.8).
2. **Pilote v2.** Avant-propos, ch. 0 et ch. 15, selon le pipeline complet. Comparer avec les rapports v1 :
   - changements de sens non décidés : objectif zéro ;
   - cibles atteintes ;
   - charge de l’auteur.
3. **Révision de la spécification** d’après le pilote : listes W et T, plafonds, seuils.
4. **Production par Partie** (0, I, II, III, IV, V + conclusion) pour harmoniser les transitions entre chapitres voisins. Un commit par chapitre, avec les fichiers `propositions.yaml`, `verdicts.yaml` et le rapport `diff_portee` signé.
5. **Recompilation et lecture continue** de chaque Partie.

---

## 11. Outillage

| Outil | État | Rôle |
| :--- | :--- | :--- |
| `style/audit_style.py` | existe | mesures rythmiques et tics par chapitre |
| `style/audit_style.py --cibles` | à écrire | liste des phrases ciblées avec motif (§6.4) |
| `style/diff_portee.py` | existe | filet de sens et d’invariants ; `--controle` comme porte de fusion |
| `style/appliquer_edits.py` | à écrire | `--verifier` : barrières (§8.3) ; `--appliquer` : application déterministe (§8.6) |
| `style/injecter_derives.py` | à écrire | insertion et dépouillement des dérives injectées (§8.8) |
| `style/prompts/redacteur.md` | à écrire | consigne de R : §4 à §6, format §7.1 |
| `style/prompts/juge.md` | à écrire | consigne de J : protocole et liste de contrôle §8.4, format §7.2 |
| `style/etalonnage/` | à constituer | jeu d’étalonnage du juge (annexe A et retouches acceptables) |

---

## Annexe A — Dérives relevées sur les pilotes

Ces dérives servent de jeu d’étalonnage et d’exemples dans la consigne du juge. Source : `style/pilots/`, rapports `style/rapports/diff_portee_00-*.md`.

| Original | Pilote | Type |
| :--- | :--- | :--- |
| « du moins dans le cas le plus probable » | « dans le cas le plus fréquent » | probabilités |
| « relever la longue série des jours où elle a été émise » | « une longue série de jours comparables » | probabilités, définition |
| « peut être pris en défaut dès que ce facteur change » | « cédera dès que ce facteur bougera » | portée |
| « quatre questions simples qui n’exigent aucune technicité mathématique pour rouvrir le cadre » | « quatre questions simples suffisent, sans technicité mathématique, pour rouvrir le cadre » | portée (suffisance) |
| « son état de vérification (exploratoire ou établie, ce qui a été contrôlé de façon indépendante) et ses hypothèses principales » | « son état de vérification et ses hypothèses » | glose retirée, exigence impossible |
| « assèchement des capacités d’évaluation » | « saturation des capacités d’évaluation » | mécanisme substitué |
| « la plausibilité, et non la vérité, devient l’objectif d’optimisation » | « la plausibilité remplace la vérité comme objectif d’optimisation » | sens (présupposé ajouté) |
| « une réflexion générale sur la décision et sur les contrôles » | « une théorie générale de la décision et des contrôles » | statut |
| « des outils, des arguments et des études de cas » | « des outils, des démonstrations et des cas » | statut |
| « l’un des arguments centraux… développé au @sec:ch07 » | « l’un des résultats centraux… établi au @sec:ch07 » | statut |
| « doutes sur la trajectoire restés sans suite » | « alertes sur la trajectoire restées sans suite » | fait |
| « une frontière en dents de scie » | « un profil de compétence en dents de scie » | terme |
| « des tests de référence » | « des batteries de tests » | terme |
| « la probabilité d’échappement du système de relecture » | « l’échappement du système de relecture » | terme |
| « échappe à la fois au producteur et au contrôleur » | « échappe aux deux voies » | terme |
| « le taux d’erreur du producteur (la proportion d’affirmations fausses qu’il émet) et la probabilité d’échappement (la proportion de ces affirmations fausses qui franchissent les contrôles…) » | « le taux d’erreur du producteur et la probabilité d’échappement des contrôles » | définitions retirées |
| « l’habitude de raisonner à l’envers (chercher quelle variation cachée de l’arrière-plan renverserait la conclusion) » | « l’habitude de raisonner à l’envers » | glose retirée |
| « vis-à-vis de tout facteur omis par le cadre — la corrosion de la ferrure — » | « devant un facteur omis par le cadre » | lien d’exemple retiré |
| « une autorisation, accordée seulement après un contrôle indépendant » | « une autorisation après contrôle indépendant » | portée |
| « comme une ligne budgétaire à part » | « comme une ressource budgétée » | remède affaibli |
| « la théorie de la fiabilité et des contrôles croisés » | « la théorie des contrôles croisés » | énumération amputée |
| « la gouvernance organisationnelle de la vérification » | « le gouvernement de la vérification » | français |
| « la consigne soumise par l’utilisateur transmet déjà son propre cadre à la machine » | « la consigne transmise à la machine lui cède déjà le cadre du problème » | sens ambigu |
| « en écarte une infinité d’autres » (avant-propos) | « en écartant une foule d’autres » | propos central affaibli |
| « le statisticien ou le mathématicien », « le décideur ou le responsable d’institution » (avant-propos) | « le statisticien », « le responsable d’institution » | énumération amputée |
| « le rôle déterminant de la direction et du filtrage humains dans ce processus hybride » (avant-propos) | « la conduite et le filtrage du travail sont restés humains d’un bout à l’autre » | provenance sur-affirmée |
