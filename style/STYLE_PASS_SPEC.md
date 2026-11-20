# Plan et spécification — Passe stylistique sur la monographie (2026)

**Objet :** Rendre la prose d’*Agir d’après une représentation du monde* (`monographie/chapitres/*.md`) plus vivante, asymétrique et idiomatiquement française, tout en préservant intégralement sa rigueur conceptuelle, ses statuts épistémiques et son appareil formel.

**Référence d’étalonnage (verrouillée après Phase 1 — profil « Option A : sobre et allégé ») :**
- **À conserver (2026) :** architecture conceptuelle, discipline terminologique (`monographie/commun/registre_termes.md`), séparation texte principal / encadrés, honnêteté épistémique, prudence des énoncés généraux (ne jamais sur-affirmer au-delà de l’appui épistémique), absence de guillemets de précaution superflus.
- **Ce que la passe cherche à corriger :** lourdeur des phrases-tunnels (30–45 mots en série dans les parties III–IV), calques syntaxiques de l’anglais, sujets nominaux abstraits, chapeaux stéréotypés, répétitions inter-chapitres, deux-points aphoristiques en série, italiques d’emphase et tics d’antithèse symétrique.
- **Garde-fou contre la sur-affirmation (leçon d’étalonnage) :** ne pas adopter un ton polémique, provocateur ou péremptoire (types B/C écartés). La brièveté doit servir la **respiration syntaxique** et la **clarté des mécanismes réutilisables**, jamais la formule tranchante qui ferme une porte sans justification ou expose l’argument à un contre-exemple facile.
- **À ne pas importer de 2022 :** mise en scène fictionnelle, dialogues, pronom « je » (sauf éventuellement mention sobre dans l’*Avant-propos* si retenue, sinon maintien de la 3e personne / « nous »), abondance de guillemets distanciateurs, notes de bas de page envahissantes, relâchement orthotypographique.

---

## 1. Périmètre et non-objectifs

- **Dans le périmètre :** le texte principal des chapitres (`monographie/chapitres/*.md`), les chapeaux d’ouverture, les transitions entre sections, et le récit des encadrés `.cas` et `.nuance`.
- **Hors périmètre (intouchés sauf faute matérielle manifeste) :**
  - les encadrés `.formel` et `.outils` (le registre neutre et sec y est adapté) ;
  - le texte des environnements `.proposition` et `.definition` (toute retouche d’énoncé relève d’une passe de fond, pas d’une passe de style) ;
  - les valeurs et tableaux des blocs `.exemple-quantitatif` ;
  - les corrections conceptuelles ou numériques (ex. tensions relevées dans `monographie/notes/REVIEW_PASS_LIVRE_ECRAN.md` sur les chapitres 5, 13, 16, 17), qui doivent faire l’objet de commits séparés.

---

## 2. Invariants stricts (non négociables)

Conformément à `authoring_conventions.md`, aucune retouche stylistique ne doit :
1. modifier une ligne de titre `#` de chapitre, ni aucun identifiant (`#sec:...`, `#prop:...`, `#def:...`, `#eq:...`, `#fig:...`, `#tbl:...`), ni aucun attribut `statut="..."` ;
2. altérer un terme du registre (`monographie/commun/registre_termes.md`), lui substituer un synonyme technique, ou déplacer sa mise en **gras** hors de son chapitre introducteur ;
3. modifier une clé de citation `[@...]` ou détacher une citation d’une donnée empirique ;
4. modifier un nombre dans un bloc `.exemple-quantitatif` ;
5. violer l’ordre des dépendances conceptuelles ou la règle du texte principal (l’argument doit rester lisible en sautant les encadrés `.outils`, `.formel`, `.nuance`, `.question`).

---

## 3. Ce qu’il faut alléger (« détox » LLM et calques de l’anglais)

| Défaut ciblé | Symptôme dans la version actuelle | Règle d’édition |
| :--- | :--- | :--- |
| **1. Tic d’antithèse binaire** | Saturation de formules en `X, non Y`, `ne… pas A ; elle B`, `on achète A, on dépense B`, surtout en fin de paragraphe. | Plafonner à **1 ou 2 antithèses porteuses par section**. Récrire les autres en assertions simples ou causales. |
| **2. Géométrie uniforme des paragraphes** | Paragraphes presque tous calibrés à 5–8 lignes : phrase-thèse → deux développements symétriques → chute aphoristique. | Introduire une vraie variance : paragraphes brefs d’1–2 phrases pour trancher ou relancer ; paragraphes longs (10–12 lignes) quand un raisonnement se déploie. Cesser de boucler chaque paragraphe sur une maxime. |
| **3. Échafaudage mécanique (chapeaux et ponts)** | Chapeaux stéréotypés (*« Le @sec:chXX a montré… Ce chapitre examine… Il montre successivement que A, B, C et D »*) et annonces répétées (*« ce sera l’objet du @sec:chYY »*). | Alléger les chapeaux en une accroche de 2–3 phrases posant le problème réel. Supprimer les tables des matières paraphrasées dans les chapeaux et les ponts redondants en fin de section. |
| **4. Récits répétés entre chapitres** | *Mars Climate Orbiter* raconté en entier 4 fois, *METR (2025)* encadré deux fois à l’identique, *Mata v. Avianca* raconté deux fois. | Garder un récit complet au chapitre d’ancrage ; ailleurs, rappeler l’épisode en 1–2 phrases avec renvoi (`@sec:ch00`, `@sec:ch11`). |
| **5. Italiques d’emphase et deux-points aphoristiques** | Emploi fréquent de `*petites formules en italique*` pour souligner la chute ; enchaînements `A : B` à l’anglaise sans connecteur explicite. | Réserver l’italique aux termes étrangers d’usage (*token*, *fuzzing*) et à de rares contrastes. Remplacer les deux-points systématiques par des liaisons françaises explicites (*car*, *puisque*, *si bien que*, *encore faut-il*). |
| **6. Sujets nominaux abstraits et prudence diplomatique** | Sujets lourds (*« La disparition du frottement et de l’hésitation produit un second effet… »*) et atténuations polies (*« Il serait erroné de voir… »*, *« Ce cas documenté ne prétend pas isoler à lui seul… »*). | Privilégier des sujets concrets et des verbes d’action. Énoncer la position nettement plutôt que d’empiler les dénégations préventives. |

---

## 4. Registre cible — Ce qu’il faut injecter (profil Option A)

1. **Respiration rythmique sans agressivité :** scinder les phrases surchargées (35–50 mots) en deux phrases nettes ; glisser des phrases courtes sobres et factuelles pour marquer un palier, sans chercher le « bon mot » ni la formule polémique.
2. **Précision épistémique intacte :** maintenir les nuances de portée (distinguer ce qui tient sous hypothèses, ce qui est tendance, ce qui reste empiriquement ouvert). Alléger le *ton* diplomatique creux (*« Il serait erroné de voir… »*), **jamais** les réserves épistémiques réelles.
3. **Gradient de ton contenu selon les parties :**
   - *Avant-propos, chapitre 0, Conclusion :* prose claire, directe, débarrassée de la symétrie administrative, mais posée et académique.
   - *Chapitres 1–9 :* prose sobre et fluide, sans échafaudage méta-discursif ; laisser les exemples porter les distinctions génériques.
   - *Chapitres 10–18 :* fermeté analytique, réduction nette des phrases à tiroirs et des italiques décoratifs, accent sur les mécanismes réutilisables plutôt que sur le commentaire d’actualité.
4. **Verbes nets et syntaxe organique :** préférer les articulations causales et concessives du français (*puisque*, *encore faut-il*, *toutefois* en milieu de phrase plutôt qu’en tête systématique, *reste que*) aux séries paratactiques calquées sur l’anglais.

---

## 5. Pipeline d’ingénierie (4 phases)

### Phase 0 — Audit quantitatif de base (`style/audit_style.py`)
Mesurer objectivement la prose principale de chaque chapitre (hors encadrés formels/outils et tableaux) :
- longueur moyenne et écart-type des phrases (mesure de monotonie rythmique) ;
- part des phrases courtes ($\le 10$ mots) et longues ($\ge 35$ mots) ;
- variance de la taille des paragraphes ;
- densité des marqueurs d’antithèse (`non pas`, `plutôt que`, `sans jamais`, `ne… que`), des deux-points, des tirets cadratins, des italiques multi-mots et des ouvertures stéréotypées (`Le @sec:`, `Ce chapitre`, `En premier lieu`, `En second lieu`, `Or `, `Toutefois`).

### Phase 1 — Calibration humaine sur échantillons puis sur 2 chapitres pilotes
1. Valider les choix stylistiques sur des formulations récurrentes de l’ouvrage (voir `style/CALIBRATION_PHASE1.md`).
2. Appliquer la passe à deux chapitres contrastés : `00-avant-propos.md` et `15-erosion-verifications.md` (ou `11-regle-tiree-des-donnees.md`).
3. Revue du `git diff` par l’auteur avec annotations (« gardé », « trop sec », « trop familier », « perte de précision »).
4. Figer ces paires avant/après comme étalon de référence pour la suite.

### Phase 2 — Réécriture par Partie (et non chapitre isolé)
Traiter les chapitres par lots cohérents (`Partie 0`, `Partie I`, `Partie II`, `Partie III`, `Partie IV`, `Partie V + Conclusion`) afin d’harmoniser les transitions entre chapitres voisins et d’éliminer les doublons narratifs.

### Phase 3 — Contrôle mécanique et lecture à l’oreille
1. Exécuter `make verifier` depuis `monographie/`.
2. Vérifier par script de diff que labels, `statut`, citations, nombres des exemples quantitatifs et termes du registre sont intacts.
3. Relancer `style/audit_style.py` pour contrôler l’élargissement effectif de la variance rythmique et la baisse des tics ciblés.
4. Recompiler `livre-ecran.pdf` et effectuer une lecture de contrôle à voix haute / en continu sur les zones clés.

---

## 6. Amendements après revue croisée (2026-11-20)

**Origine :** relecture de cette spécification par Claude (Opus 5.5) en regard de `style/COMPARAISON_2022_2026.md`, du pilote `style/pilots/00-avant-propos.md` et de la sortie de `style/audit_style.py`.
**Statut :** amendements *proposés*, à valider par l’auteur. Les sections 1 à 5 restent valides ; ce qui suit les complète sans les remplacer.

### 6.1 Constats sur le pilote `00-avant-propos.md`

Labels, renvois et clés de citation sont intacts (vérifié par comparaison des identifiants). Les mesures du texte principal (`audit_style.py`) donnent :

| Indicateur | Original | Pilote | Objectif de la spec |
| :--- | ---: | ---: | :--- |
| Mots | 1 887 | 1 695 | — |
| Longueur moyenne des phrases | 32,0 | 26,5 | baisse ✓ |
| Phrases ≥ 35 mots | 39,0 % | 23,4 % | baisse ✓ |
| Phrases ≤ 10 mots | 5,1 % | 9,4 % | hausse ✓ |
| Écart-type de la taille des paragraphes | 54 | 43 | **hausse visée (§3, règle 2) ✗** |
| Antithèses / 1 000 mots | 1,6 | 2,4 | **baisse visée (§3, règle 1) ✗** |
| Italiques / 1 000 mots | 4,8 | 5,3 | **baisse visée (§3, règle 5) ✗** |

Le pilote atteint la cible de longueur mais va contre trois des objectifs qu’il devait servir.

**Glissements de sens relevés (≈ 1 900 mots) :**

| Original | Pilote | Problème | Action proposée |
| :--- | :--- | :--- | :--- |
| « en écarte une infinité d’autres » | « en écartant une foule d’autres » | L’infini est le propos même (cadre fini contre arrière-plan ouvert, @sec:ch02, @sec:ch07). | Rétablir « une infinité ». |
| « le rôle déterminant de la direction et du filtrage humains dans ce processus hybride » | « la conduite et le filtrage du travail sont restés humains d’un bout à l’autre » | Sur-affirmation de la part humaine, dans la section même qui traite de la provenance (cf. blanchiment de provenance, @sec:ch16). | Rétablir l’original ou une formulation rédigée par l’auteur. |
| « le statisticien ou le mathématicien », « le décideur ou le responsable d’institution » | « le statisticien », « le responsable d’institution » | Incohérence avec les parcours du @sec:ch00 (tableau 0.1 : *Le statisticien et le mathématicien*, *Le décideur et l’institution*). | Rétablir les deux profils. |
| « l’un des arguments centraux du livre, développé au @sec:ch07 » | « l’un des résultats centraux du livre, établi au @sec:ch07 » | La conclusion donne à cet énoncé le statut *résultat sous hypothèses* ; « établi » efface la réserve. | À trancher par l’auteur (proposition : « établi sous hypothèses »). |

**Leçon :** aucun des contrôles de la Phase 3 (labels, `statut`, citations, nombres, registre) ne détecte ces glissements. C’est le mécanisme du @sec:ch15 appliqué à la passe elle-même : la version réécrite se lit mieux, donc elle passe. Le pilote ne doit pas être figé comme étalon (Phase 1, point 4) avant correction de ces quatre points.

### 6.2 Invariants supplémentaires (complète §2)

6. **Portée et force des énoncés.** Aucune retouche ne modifie la portée ou la force d’un énoncé : verbes modaux et atténuateurs, quantificateurs, verbes et noms de statut, contenu des énumérations. Toute modification de ces éléments est signalée par le contrôle du §6.3 et validée explicitement par l’auteur.
7. **Énoncés de provenance.** La section « Genèse et responsabilité » (@sec:avant-propos-genese) et le passage « Une provenance déclarée » de la conclusion sont relus et validés ligne à ligne par l’auteur. Aucune reformulation n’augmente la part humaine décrite ni ne réduit la part attribuée aux modèles de langage.

### 6.3 Contrôle de dérive de sens (complète la Phase 3)

`style/diff_portee.py` (écrit le 2026-11-20) compare original et version réécrite **section par section**. L’alignement se fait sur les identifiants `{#sec:...}`, stables par construction (§2, invariant 1). Usage : `python3 style/diff_portee.py ORIGINAL.md REECRIT.md`, puis `--controle RAPPORT` pour la porte de fusion. Pour chaque section, le script rapporte :

- **modaux et atténuateurs** ajoutés ou retirés : *peut, pourrait, tend à, souvent, en général, généralement, rarement, parfois, le plus souvent, en principe, probablement* ;
- **quantificateurs absolus** ajoutés ou retirés : *tout, toute, tous, toutes, aucun, aucune, jamais, toujours, seul, seule, seulement, uniquement, nécessairement, entièrement, d’un bout à l’autre* ;
- **verbes et noms de statut** : *montre, établit, démontre, prouve, suggère, indique, argument, résultat, hypothèse, constat* ;
- **mots pleins perdus** : mots de sept lettres ou plus présents dans la section originale et absents de la version réécrite, ce qui attrape notamment les éléments d’énumération supprimés.

Ajoutés à la mise en œuvre, d’après le pilote du @sec:ch00 :

- **force de l’affirmation** : *suffire, garantir, impossible, forcément, inévitablement, certainement, évidemment* (le pilote avait écrit « quatre questions simples **suffisent** »), et *théorie, théorème, démonstration* dans les mots de statut ;
- **lecture des probabilités** : *probable, probabilité, fréquent, fréquence, vraisemblable* (le pilote avait remplacé « le cas le plus probable » par « le cas le plus fréquent » dans le passage même qui distingue jugement et fréquence) ;
- **termes du registre** dont l’effectif change, avec le contexte de chaque occurrence retirée (le pilote avait remplacé « frontière en dents de scie » et « tests de référence ») ;
- **citations** déplacées ou ajoutées dans une section, **blocs protégés** non identiques, et, sur le fichier entier, identifiants, renvois, attributs `statut` et clés de citation ;
- les mots perdus sont séparés en *sans équivalent dans la section* (à trancher) et *variantes morphologiques probables* (à parcourir).

Le rapport est écrit dans `style/rapports/diff_portee_<chapitre>.md`. Il n’écrase pas un rapport existant sans `--force`, pour préserver les décisions déjà prises.

- **Éléments ⛔ et ⚠ :** une case chacun (*accepté* / *rétabli*).
- **Éléments · :** reformulation à effectif constant, variantes, ajouts. Ils sont listés sans case.

Aucune fusion d’un lot tant que `--controle` ne passe pas, c’est-à-dire tant que toutes les cases ne sont pas cochées par l’auteur.

### 6.4 Cibles chiffrées (font de l’audit une porte d’entrée)

Référence avant passe (`audit_style.py`, texte principal, 2026-11-20) : moyenne 27,4 ± 13,5 mots ; phrases ≤ 10 mots 9,1 %. Les chapitres 0 et 13 à 16 sont les plus lourds (29,5 à 32,1 mots en moyenne, jusqu’à 37 % de phrases ≥ 35 mots). Les chapitres 1 à 3 sont déjà proches de la cible (20,7 à 22,1).

Cibles proposées (à valider par l’auteur) :

| Indicateur | Ch. 0 et 10–16 | Ch. 1–9, 17–18, conclusion |
| :--- | :--- | :--- |
| Longueur moyenne des phrases | ≤ 25 mots | ≤ 24 mots |
| Phrases ≥ 35 mots | ≤ 20 % | ≤ 15 % |
| Phrases ≤ 10 mots | ≥ 10 % | ≥ 12 % |
| Écart-type de la taille des paragraphes | ≥ valeur avant passe | ≥ valeur avant passe |
| Antithèses, italiques, deux-points (/ 1 000 mots) | ≤ valeur avant passe | ≤ valeur avant passe |

- **Plancher.** Ne pas descendre sous ~20 mots de moyenne sur un chapitre : c’est le profil du livre de 2022, et en deçà la prose devient hachée.
- **Écarts justifiés.** Un chapitre qui manque une cible n’est pas rejeté d’office, mais l’écart est justifié dans le message de commit (par exemple, un chapitre à forte densité formelle).
- **Limite.** Atteindre les cibles ne valide rien en soi : le contrôle du §6.3 et la lecture de l’auteur restent décisifs.

### 6.5 Table d’ancrage des récits récurrents (à arrêter avant la Phase 2)

La règle 4 du §3 traverse les Parties. Un traitement par lots (Phase 2) ne peut donc pas la résoudre localement : les ancrages se décident avant.

| Récit | Fichiers où il apparaît | Ancrage proposé | Ailleurs |
| :--- | :--- | :--- | :--- |
| Mars Climate Orbiter | ch. 0, 8, 10, 11, 12, 13, 14, conclusion | Récit au @sec:ch00, analyse au @sec:ch10 | Rappel en 1–2 phrases avec renvoi |
| *Mata v. Avianca* | ch. 0, 11, 13 | Récit au @sec:ch00, analyse au @sec:ch11 | Rappel au @sec:ch13 |
| METR (2025) | ch. 0, 15 | Encadré complet au @sec:ch15 | Une phrase et un renvoi au @sec:ch00 |

Les exemples courants (voiliers, eau bouillante, ferrure, dinde, Challenger, pluie à 70 %) reviennent **par construction** : ils s’enrichissent d’un chapitre à l’autre (@sec:ch00, `commun/exemples_courants.md`). Le dédoublonnage vise les re-narrations de ce qui a déjà été raconté, non la récurrence elle-même.

### 6.6 Chantiers connexes et ordre d’exécution

La spécification exclut à bon droit le fond et la fabrication de son périmètre (§1). Ces chantiers ont toutefois besoin d’un emplacement et d’un ordre.

1. **Vérification des références (prioritaire).** `commun/biblio.bib` ne contient qu’une entrée vérifiée (`fauriat2026frame`) ; `commun/biblio_a_verifier.bib` en contient 60, citées 183 fois dans les chapitres. Ce sont les « ? » orange du PDF ; les plus citées sont `mco1999`, `rogers1986`, `tufte1997`, `mata2023` et `becker2025`. Pour un livre élaboré avec des modèles de langage, et qui ouvre sur *Mata v. Avianca*, c’est le contrôle le plus important. Il précède la passe de fond, puisqu’une source qui ne soutient pas la phrase citée entraîne une correction de fond (cf. @sec:ch18 : le seul contrôle effectif d’une référence consiste à l’ouvrir).
2. **Fabrication (en parallèle).**
   - 10 « Figure à générer » restent à produire.
   - « au section » apparaît deux fois (ch. 7 et 17) : corriger la tournure dans la source, par exemple « à la @sec:… ».
   - Ouverture du ch. 15 : le renvoi produit « de la Vos propres contrôles… ». À reformuler dans la source ; le motif 3 de la calibration traite déjà ce chapeau.
   - L’en-tête courant « 18 Un remède à trois niveaux » persiste sur les pages de la conclusion : à corriger dans le gabarit.
   - Ajouter à la Phase 3 une vérification sur le PDF compilé : recherche de `Figure à générer`, de `au section` et des en-têtes courants. Le bilan de `make verifier` doit afficher 0 référence à vérifier avant publication.
3. **Passe de fond (commits séparés), avant la passe de style.**
   - Les tensions relevées dans `monographie/notes/REVIEW_PASS_LIVRE_ECRAN.md` (ch. 5, 13, 16, 17).
   - Les deux apports issus de `style/COMPARAISON_2022_2026.md` (§2.4 et §5) :
     - l’image de la fève hors du gâteau pour l’incertitude ontologique (@sec:ch05, éventuellement §0.3.1) ;
     - l’exploration comme décision économique (coût de l’information contre gain espéré), aux côtés du cadrage par la sûreté (@sec:ch07, @sec:ch17).

   Raison de l’ordre : la passe de style harmonise ainsi le texte nouveau au lieu de laisser des ajouts d’une autre voix.
4. **Passe de style** (Phases 1 à 3 de cette spécification, amendées par les §6.2 à 6.5), par Partie.
5. **Recompilation et lecture continue** de `livre-ecran.pdf`.

### 6.7 Ajustements de registre (complète §4)

- **Option A confirmée.** La recommandation 3 de `COMPARAISON_2022_2026.md` (« l’énergie du manifeste de 2022 ») se réduit à la netteté de la phrase. Elle n’autorise ni ton péremptoire ni prédiction : les options B et C montrent que cette énergie et la sur-affirmation vont ensemble.
- **« Je ».** Au plus dans « Genèse et responsabilité », où il règle un problème réel (« l’auteur » cinq fois en six phrases). Ailleurs, « nous » ou la troisième personne.
- **Finalité.** La passe vise la lisibilité et la clarté des mécanismes. Elle ne vise pas à rendre le texte moins reconnaissable comme produit avec des modèles. La divulgation de l’avant-propos et de la conclusion reste exacte (invariant 7), conformément à l’argument du @sec:ch15 : la tenue de la forme n’atteste pas le fond.
