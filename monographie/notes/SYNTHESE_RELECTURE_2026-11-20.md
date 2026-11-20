# Synthèse de la relecture intégrale — *Agir d’après une représentation du monde*

**Date :** 2026-11-20  
**Base textuelle examinée :** dépôt `/home/ai-user/Documents/Sandbox/review_epist_ag`, branche `relecture-livre`, tag `relecture-2026-11-20-base` (avant-propos, chapitres 0 à 18, conclusion, pages de partie I–V, annexes A–D, `monographie/commun/registre_termes.md`, tableaux générés).  
**Corpus analysé :** 328 constats émis par 11 lecteurs neufs (`C`, `P0`–`P5`, `PA`, `T1`, `T2`, `T5`) et 20 pistes mécaniques ou hors périmètre, regroupés en 273 grappes dans les lots `V0`–`V5` et `VX`, puis ramenés à **260 grappes consolidées** après 8 fusions transversales et 1 reclassement documentés ci-dessous.

---

## 1. Résumé pour l’auteur

**Verdict d’ensemble.** Le livre est **proche d’un état publiable sur le fond**, avec une réserve nette : il faut solder **6 défauts critiques (gravité A)**, trancher une douzaine de **questions de fond (groupe 3)** et exécuter une **passe d’allègement des redites** avant le bon à tirer. La thèse, l’architecture des cinq propositions et l’honnêteté épistémique (notamment les encadrés *Nuance* et la Conclusion) emportent l’adhésion des onze lecteurs. Tous les calculs et tableaux quantitatifs ont été recalculés à la main par plusieurs lecteurs indépendants (`C`, `PA`, `T2`, `P1`–`P5`) sans qu’aucune erreur arithmétique soit relevée. En revanche, la lecture linéaire souffre d’un fort empilement de résumés et d’études de cas répétées *in extenso*, et les passes d’édition antérieures ont laissé ou introduit quelques contresens locaux et tensions de statut.

**Décomptes consolidés (260 grappes).**
- **Par verdict :** `CONFIRME` **181** · `PLAUSIBLE` **50** · `DEJA_TRANCHE` **5** · `DEJA_RELEVE` **4** · `REJETE` **20**.
- **Par groupe (sur les 231 grappes actives `CONFIRME` + `PLAUSIBLE`) :** **G1** (corrections directes) **124** (112 `CONFIRME`, 12 `PLAUSIBLE`) · **G2** (arbitrages rapides) **89** (56 `CONFIRME`, 33 `PLAUSIBLE`) · **G3** (questions de fond) **18** (13 `CONFIRME`, 5 `PLAUSIBLE`). Hors actives : 29 grappes (`DEJA_TRANCHE`, `DEJA_RELEVE`, `REJETE`).
- **Par gravité (sur 260 grappes) :** **A** (bloquant) **6** · **B** (important) **98** · **C** (mineur) **156**.

**Les dix problèmes les plus importants :**

1. **Contradiction de la roulette russe dans M2 (`V5-001` fusionnée avec `V1-002`, grav. A, G3).** Le joueur estime $p = 0{,}001\,\%$ pour une balle oubliée dans la chambre, puis la balle dans le barillet ($z = 1/6$) est présentée comme un facteur omis indépendant de $p$ (ch. 4 et 17).
2. **Contresens « contrôle franchi » sur $C$ et statut de la sévérité (`V2-039`, grav. A, G1 ; `V2-040`, grav. B, G3).** Au ch. 9 (`ARBITRAGES P1.10.4`), $C$ désigne l’arrêt de l’erreur mais est glosé « *contrôle franchi* » ($\bar C$) ; de plus, mesurer la sévérité par $\Pr(\bar A \mid E)$ (`R4`) la confond avec la sensibilité $s$.
3. **Triple contradiction sur le statut de la Proposition 4 (`V2-029`, grav. A, G3).** L’en-tête du ch. 8 affiche *hypothèse de travail*, la note interne la dit *composite* (*définition* pour la tension structurelle), et le Tableau 1 de la Conclusion classe cette tension en *résultat sous hypothèses*.
4. **Faille mathématique dans la preuve du modèle M3 (`V2-021`, grav. A, G2 ; `VX-013`, grav. B, G1).** Au ch. 7 et en A.6, $f_1$ admet des tirages aléatoires internes, ce qui brise l’indépendance entre l’accord $A$ et l’erreur $e(x,z) = g(x,z) - f_1(x)$ sachant $X=x$.
5. **Sur-affirmation sur les « erreurs d’un type nouveau » en partie III (`V3-001`, grav. A, G1 ; `V3-002`, grav. B, G1).** `monographie/parties/partie-3.md` qualifie les erreurs internes au cadre et silencieuses de « type nouveau » propre aux composants appris, contre *Mars Climate Orbiter* (ch. 10 et 13).
6. **Fausse lecture de la sévérité à 99,9 % au chapitre 12 (`V3-030`, grav. A, G1).** La puce de lecture vante une sévérité de 99,9 % sur le fait rare comme un succès alors que le taux de fausses alertes vaut aussi 99,9 % ($s/f \approx 1$), contredisant la leçon du ch. 9.
7. **Écart entre l’énigme d’ouverture (0.5.4) et la baisse du risque au ch. 16 (`VX-001` fusionnée avec `V0-025`, `V4-019`, grav. B, G2 ; `V4-020`, grav. B, G1).** Le lecteur linéaire attend que le modèle partagé fasse monter le risque global, alors que le Tableau 16.1 le fait baisser ($5{,}57\,\% \to 1{,}93\,\%$) et que les titres 16.1 et `partie-4.md` durcissent une hypothèse conditionnelle.
8. **Hypothèses et statuts incomplets des Propositions 1, 2 et 3(b) (`V2-005`, `V2-014`, `V2-022`, grav. B, G3).** P1 omet ses hypothèses dans l’énoncé et réduit l’éq. (5.1) au seul désaccord ; P2 (« définition » à 3 éléments) prétend faire « découler » 5 conditions sans statut propre ; P3(b) reste sans dérivation formelle.
9. **Glissement du terme « cadre » pour les composants appris et instabilité *cadre* / *représentation* (`V3-033`, grav. B, G2 ; `V1-001`, grav. B, G3).** La matrice 13.1 entend *cadre* au sens du « problème posé par l’utilisateur » malgré la Déf. 2, et l’inclusion *représentation* $\supset$ *cadre* ajoutée en 2.3 reste contredite deux lignes plus bas et aux ch. 3–4.
10. **Redites structurelles et lacunes du parcours « L’argument principal » (`VX-005`, `VX-034`, `V0-001`, `V0-008`, `V3-008`, `V4-002`, grav. B, G2/G3).** Quatre cas sont narrés *in extenso* plusieurs fois, les pages de partie et 0.7 répètent les chapitres, et le parcours principal saute les ch. 4, 8, 9 et 17 dont dépendent 13, 16 et 18.

*(Note de traçabilité des fusions : 13 grappes redondantes entre lots ont été fusionnées dans les grappes porteuses correspondantes — `VX-035` $\to$ `V0-002` ; `V0-031` + `VX-036` $\to$ `V5-034` ; `V1-002` $\to$ `V5-001` ; `V1-007` + `V2-010` + `V3-041` $\to$ `VX-011` ; `V0-025` $\to$ `VX-001` [reclassée `CONFIRME`] ; `V5-016` $\to$ `V0-012` ; `V0-011` + `V3-016` + `V4-027` $\to$ `VX-005` ; `V2-004` $\to$ `VX-034`. Ces fusions expliquent le passage de 273 grappes brutes à 260 grappes consolidées sans perte d’aucun constat.)*

---

## 2. Ce que les lecteurs ont compris

Le rapprochement des onze bilans (« Ce que j’ai compris ») et de la « lecture en une page » de `C` montre une convergence remarquable sur la colonne vertébrale de l’ouvrage, y compris chez les lecteurs qui n’avaient que des extraits (`T1`, `T2`, `T5`).

### Ce que le texte porte sans ambiguïté

- **Le socle épistémologique (Parties I et II).** Tous les lecteurs (`C`, `P0`, `P1`, `P2`, `T1`, `T2`, `T5`) restituent exactement l’asymétrie fondatrice (*on agit d’après une représentation construite dans un cadre fini ; le monde répond à l’action*), l’arrière-plan tacite ouvert des règles, l’impossibilité de certifier le cadre de l’intérieur (déduction comme induction), la barre d’erreur comme mesure du désaccord au sein d’un ensemble admis $\Theta$, les cinq conditions de détection, le cadre comme cause commune des contrôles internes, l’opposition chaîne / contrôle croisé et le blanchiment aux interfaces, la sévérité (Mayo), l’effondrement de la VPP quand les erreurs deviennent rares, l’appariement comportemental des probabilités et la factorisation $R = P(E)\times\text{échappement}$.
- **Le basculement informatique et l’automatisation (Parties III et IV).** `C`, `P0`, `P3`, `P4`, `T1` et `T5` restituent fidèlement le contraste entre composants spécifiés (contrats, vérification en amont, adresse des défaillances) et composants appris (« garantie dépensée contre portée », plausibilité plutôt que vérité, orienter sans spécifier, frontière en dents de scie, calibration générative), la matrice à deux axes du ch. 13 (« la formalité change la colonne, non la ligne ») et la distinction vérification / validation, ainsi que les trois effets de l’automatisation (enchaînement jusqu’à l’action, érosion des contrôles implicites par perte de friction/signe révélateur/signal coûteux et complaisance, corrélation des angles morts via un prêteur unique et blanchiment de provenance).
- **L’atelier pratique et la posture réflexive (Partie V et Conclusion).** `C`, `P0`, `P5`, `PA`, `T1` et `T5` retiennent tous le duo marge d’humilité $b$ / verrou sur les décisions uniques, le rôle des bacs à sable, les quatre questions devant un chiffre assuré, l’organisation à trois niveaux (attitude, placement, organisation mesurée par erreurs injectées) et le caractère *faute de mieux* d’une conclusion jugée honnête et rigoureuse.

### Là où les lecteurs divergent, hésitent ou se trompent (signaux de clarté)

1. **L’énigme d’ouverture (« producteur plus fiable, système plus risqué »).** `P0` et `T1` la prennent en ouverture pour une loi générale annoncée par le livre ; `C` (qui lit tout d’une traite) y voit son principal motif de scepticisme lorsqu’il découvre au ch. 16 que le modèle M1 fait *baisser* le risque global avec les paramètres choisis (`VX-001`, `V4-019`).
2. **La frontière *dans le cadre* / *hors du cadre* (roulette russe et composants appris).** `P1`, `P5` et `C` butent sur l’exemple de la roulette russe, où $p$ couvre une balle oubliée dans la chambre tandis que la balle dans le barillet est appelée « facteur omis » $z$ (`V5-001`). En partie III, `P3` et `C` ne savent plus de quel cadre on parle pour les composants appris (« domaine courant », « consigne », ou « cadre du modèle » : `V3-033`), et `T1` reste gêné par « erreurs d’un type nouveau » en `partie-3.md` (`V3-001`).
3. **L’inclusion *représentation* $\leftrightarrow$ *cadre* et le mot *vérification*.** `P1` relève que la retouche 2.3 (*comprend ce cadre*) cohabite avec *à l’intérieur du cadre* (`V1-001`). `C` note la coexistence de *vérification* (résoudre correctement le problème posé, ch. 13), *vérification en amont* (ch. 10), *état de vérification* (ch. 18) et *vérifications humaines* (ch. 15 : `VX-003`).
4. **Les « chaînes de contrôles ».** `C` et `P0` relèvent dans plusieurs seuils (`00-cartographier.md`, `partie-2.md`, `partie-4.md`, `partie-5.md`, `99-conclusion.md`) le glissement « contrôles en chaîne », qui contredit le ch. 8 où la chaîne assemble des *composants* de production (`V0-004`, `VX-007`).
5. **Le statut et la portée des cinq propositions et de la réponse finale.** `C`, `P2` et `T1` divergent de l’affichage sur P1 (hypothèses absentes de l’énoncé), P2 (cinq conditions présentées comme « découlant » d’une définition à trois termes), P3(b) (sans dérivation), P4 (trois statuts affichés) et la phrase finale de la conclusion (qui donne aux cinq conditions l’allure d’une condition suffisante : `V5-039`).
6. **Lecture sur extraits vs lecture linéaire.** `T1` (privé du corps) et `T2` (privé des paragraphes sans chiffres) perçoivent parfois des durcissements entre résumés et corps ou ignorent un renvoi interne (`V1-030`, `V2-020`, `V3-018`, `V5-031`), mais leurs constats confirment un fait réel pour un lecteur pressé qui ne lit que les cartes et *Points clés* : les résumés (ch. 0, pages de partie, *Points clés*) sont souvent plus catégoriques que les chapitres qu’ils synthétisent.

---

## 3. Questions de fond (groupe 3)

Les 18 grappes actives de groupe 3 (13 `CONFIRME`, 5 `PLAUSIBLE`) sont regroupées ci-dessous dans l’ordre du livre. *(Les 2 grappes `DEJA_TRANCHE` de groupe 3 — `V1-029` et `V2-009` — sont recensées en § 8.)*

### 1. `V0-001` (`CONFIRME`, grav. B) — Parcours « L’argument principal » incomplet
- **Passages concernés :** `monographie/chapitres/00-cartographier.md` l. 213 (Table 0.1).
- **Problème :** Signalé par 4 lecteurs (`C-016`, `P0-002`, `T1-016`, `T5-025`). Le parcours « L’argument principal » retient les ch. 0, 2, 5, 6, 7, 10, 11, 13, 16, 18 et Conclusion, omettant les ch. 8 et 9 (qui portent les Propositions 4 et 5, *angle mort*, *blanchiment*, *sévérité* et le modèle M1) ainsi que les ch. 4 et 17 (seuil $p^\ast$, décision unique, marge $b$, verrou), alors que les ch. 13, 16 et 18 s’appuient directement sur eux.
- **Options :** *(a)* Inclure les ch. 8 et 9 (et idéalement 4 et 17) dans « L’argument principal » (12 ou 14 chapitres sur 19) ; *(b)* renommer ce parcours en « Traversée rapide » (ou « Vue d’ensemble courte ») et avertir que les Propositions 4–5 et la décision unique sont laissées de côté.
- **Recommandation :** **Option (a)** avec ajout minimal de **4, 8, 9 et 17** (ou au strict minimum **8 et 9** si l’on veut préserver une variante courte, en renommant alors le titre pour ne plus promettre « l’argument complet du choix du cadre jusqu’à l’organisation des contrôles »). Un parcours qui revendique « l’argument principal » ne peut pas sauter deux des cinq propositions sur lesquelles reposent le ch. 13 et le ch. 16.
- **Décision :** 

### 2. `V0-008` (`CONFIRME`, grav. B) — Longueur et redondance de la section 0.7
- **Passages concernés :** `monographie/chapitres/00-cartographier.md` l. 175–196 (§ 0.7).
- **Problème :** Signalé par `P0-012` et `T5-007`. La section 0.7 résume chapitre par chapitre (~980 mots) ce que 0.2–0.6 viennent d’exposer et ce que les pages de partie et introductions de chapitre répètent aussitôt, tout en introduisant des termes techniques non encore définis (`V0-010`).
- **Options :** *(a)* Condenser 0.7 en un tableau ou en cinq brefs paragraphes de 3–4 lignes par partie (renvoyant aux pages de partie sans jargon non défini) ; *(b)* conserver 0.7 détaillée pour les lecteurs qui choisissent leur parcours dans la Table 0.1, en retirant seulement les termes techniques anticipés.
- **Recommandation :** **Option (a)** (un tableau synthétique `Chapitre | Question centrale | Ce qu'il établit` de ~250 mots, ou 5 paragraphes de 3 lignes par partie). Cela allège le ch. 0 d’environ 700 mots sans nuire au choix des parcours. À articuler avec `VX-034`.
- **Décision :** 

### 3. `V1-001` (`CONFIRME`, grav. B) — Direction d’inclusion entre *représentation* et *cadre*
- **Passages concernés :** `monographie/chapitres/02-cadre.md` l. 77 ; `monographie/chapitres/03-mondes-possibles.md` l. 3 ; `monographie/chapitres/04-decider.md` l. 117 ; `monographie/commun/registre_termes.md` l. 18–19.
- **Problème :** Malgré `ARBITRAGES P1.2` (`SYN-D2`, qui a ajouté « La représentation comprend ce cadre… » en 2.3), `P1-001` relève que la même section 2.3 écrit deux lignes plus bas « ajuster une représentation *à l’intérieur du cadre* » et que les ch. 3 et 4 écrivent « une représentation construite *dans* un cadre ».
- **Options :** *(a)* Maintenir la lecture **emboîtée** ($\text{représentation} \supset \text{cadre}$) et remplacer partout « à l’intérieur du cadre » / « construite dans un cadre » (lorsqu’il s’agit de la représentation complète) par « à partir de ce cadre » ou « sur la base de ce cadre » (2.3, 3.1, 4.5, Conclusion) ; *(b)* revenir à la lecture **disjointe** (cadre = contenant, représentation = contenu ajusté) en retirant « comprend ce cadre » en 2.3 et « catégories » de la Déf. 1.
- **Recommandation :** **Option (a)** (maintenir l’emboîtement voulu par `P1.2` et nettoyer les 4–5 formulations résiduelles « dans le cadre / à l’intérieur du cadre » appliquées à la représentation entière). L’option (a) préserve l’unité avec la Déf. 1 et la Déf. 2 du registre sans réouvrir le glossaire.
- **Décision :** 

### 4. `V1-003` (`CONFIRME`, grav. B) — Bloc `.cas` fictif au chapitre 2
- **Passages concernés :** `monographie/chapitres/02-cadre.md` l. 136–142 ; `monographie/chapitres/07-cadre-cause-commune.md` l. 85.
- **Problème :** Signalé par `C-011` et `P1-004`. L’encadré « Un modèle clinique face à un changement de population » est balisé `.cas` (*Étude de cas*), alors que `00-avant-propos.md` l. 52 réserve ce bloc aux épisodes historiques, industriels ou juridiques documentés et datés. Or le bloc décrit un scénario générique (« Considérons… ») sans autre source que `[@fauriat2026frame]`, et le § 7.3 y renvoie ensuite comme à un fait avéré.
- **Options :** *(a)* Requalifier l’encadré en exemple illustratif en texte courant (ou `.nuance` / `.outils`) et ajuster le renvoi du § 7.3 (« comme dans l’exemple du modèle clinique… ») ; *(b)* remplacer le scénario générique par une étude de cas clinique réellement publiée et datée sur la dérive de population (ex. réadmission hospitalière ou score de septicémie Epic/EHR documenté dans la littérature).
- **Recommandation :** **Option (a)** si l’auteur souhaite éviter d’introduire une nouvelle recherche bibliographique à ce stade ; **Option (b)** est encore préférable qualitativement (et comble un manque signalé par `C` dans son bilan) s’il dispose déjà d’un cas publié vérifié. Dans les deux cas, ne pas conserver un scénario inventé sous l’étiquette `.cas`.
- **Décision :** 

### 5. `VX-034` (`CONFIRME`, grav. B) — Redondance structurelle des 5 pages de partie et des ponts de frontière
- **Passages concernés :** `monographie/parties/partie-1.md` à `partie-5.md` (3 831 mots au total), transitions de fin et d’ouverture de chapitres (fusionne `V2-004`, constats `T5-001`, `T5-002`, `T5-005`, `T5-006`).
- **Problème :** En lecture linéaire, les 5 pages de partie résument en détail chaque chapitre (523 à 1 038 mots chacune), doublonnant 0.7, les chapeaux de chapitre et les *Points clés*, et chaque frontière entre parties répète trois fois le même pont (fin de chapitre $k$, fin de page de partie, ouverture de chapitre $k+1$).
- **Options :** *(a)* Réduire chaque page de partie à un texte court (150–250 mots : question directrice de la partie + une phrase par chapitre situant sa place, sans résumer les résultats ni annoncer la partie suivante en dernier paragraphe), sur le modèle déjà rédigé dans `V5-017` pour `partie-5.md` ; *(b)* conserver les pages de partie détaillées comme cartes autonomes pour les parcours sélectifs et alléger uniquement les introductions/clôtures de chapitres.
- **Recommandation :** **Option (a)**. Les chapitres ont déjà chacun un chapeau et des *Points clés*, et les parcours sélectifs s’appuient sur la Table 0.1. Condenser les pages de partie (et supprimer leurs annonces redondantes de la partie suivante) allège le livre d’environ 2 500 mots tout en améliorant nettement le rythme de lecture.
- **Décision :** 

### 6. `V2-005` (`CONFIRME`, grav. B) — Hypothèses absentes et sens de « désaccord » dans la Proposition 1
- **Passages concernés :** `monographie/chapitres/05-trois-incertitudes.md` l. 65 (`@prop:desaccord`) et l. 82–91 (*Noyau formel*) ; `monographie/chapitres/99-conclusion.md` Tableau 1.
- **Problème :** Signalé par 4 lecteurs (`C-012`, `P2-003`, `T1-032`, `T2-006`). (1) La Proposition 1 porte le statut *résultat sous hypothèses*, mais son énoncé encadré est universel et relègue les hypothèses (mesure définie sur un ensemble $\Theta$, moments finis pour la variance, facteur omis constant ou non attribué) dans un bloc `.formel` facultatif, contraire à la règle du texte principal ; (2) le mot « désaccord » ne couvre littéralement que le second terme de l’éq. (5.1) ($\mathrm{Var}_\theta(\mathbb{E}[Y\mid\theta])$), le premier terme mesurant la dispersion interne $\mathbb{E}_\theta[\mathrm{Var}(Y\mid\theta)]$.
- **Options :** *(a)* Reformuler l’énoncé de P1 pour intégrer ses conditions et les deux termes : « Sous les hypothèses retenues pour le calcul (moments finis, pondération sur l’ensemble spécifié $\Theta$), toute mesure quantitative d’incertitude résume la dispersion calculée au sein de $\Theta$ — dispersion interne à chaque alternative et désaccord entre alternatives. Une alternative qui n’a jamais été admise n’y contribue en rien. » ; *(b)* garder le titre et le mot « désaccord » en ajoutant uniquement la clause « calculé sur un ensemble spécifié $\Theta$ sous des hypothèses données » dans l’énoncé encadré, et gloser les deux termes de (5.1) juste en dessous dans le texte principal.
- **Recommandation :** **Option (a)** (ou **(b)** si l’auteur tient à garder la formule concise « désaccord » dans l’énoncé canonique de P1, à condition d’expliciter dans la phrase encadrée qu’il s’agit d’une quantité *calculée sur un ensemble spécifié $\Theta$ sous ses hypothèses* et que le premier terme de (5.1) représente la dispersion interne).
- **Décision :** 

### 7. `V2-008` (`PLAUSIBLE`, grav. B) — Réponse à l’objection de l’hypothèse « fourre-tout » dans $\Theta$
- **Passages concernés :** `monographie/chapitres/05-trois-incertitudes.md` l. 73–77 (ou `monographie/chapitres/17-decisions-sans-appel.md` § 17.1).
- **Problème :** Relevé par `C-013`. Le livre ne discute pas l’objection bayésienne classique consistant à ajouter dans $\Theta$ une hypothèse résiduelle « autre chose que nos modèles » dotée d’un poids *a priori* non nul (qui rappelle la marge $b$ du ch. 17).
- **Options :** *(a)* Ajouter un court paragraphe (en *Nuance* au ch. 5 ou au ch. 17) expliquant qu’une hypothèse « fourre-tout » n’a pas de vraisemblance prédictive définie sur les observables, de sorte qu’elle ne peut ni produire un désaccord calculable dans $\Theta$ ni être révisée par les données (ce qui la distingue précisément d’une marge de décision $b$ prise au niveau de l’acte au ch. 17) ; *(b)* laisser en l’état.
- **Recommandation :** **Option (a)**. Trois phrases suffisent et désamorcent une objection très attendue des statisticiens bayésiens.
- **Décision :** 

### 8. `V2-012` (`PLAUSIBLE`, grav. C) — Place de la *Nuance* sur *Challenger* au chapitre 5
- **Passages concernés :** `monographie/chapitres/05-trois-incertitudes.md` l. 116–122 ; `monographie/chapitres/06-detecter-une-erreur.md` § 6.3.
- **Problème :** `T5-015` relève que la *Nuance* de fin du ch. 5 raconte *Challenger* (7 vols vs 16 vols, autorité des ingénieurs, renversement de la charge de la preuve) juste avant l’étude de cas du ch. 6.
- **Options :** *(a)* Conserver au ch. 5 un garde-fou de 3 lignes (pour éviter que le lecteur du ch. 5 ou d’un parcours sautant le ch. 6 ne classe *Challenger* comme pur défaut de cadre) avec renvoi au § 6.3 pour le récit factuel ; *(b)* garder la *Nuance* du ch. 5 telle quelle ; *(c)* la supprimer au ch. 5.
- **Recommandation :** **Option (a)**. Maintenir l’avertissement conceptuel au ch. 5 sans déflorer le récit chiffré réservé au § 6.3 (cohérent avec le plan d’allègement en § 6).
- **Décision :** 

### 9. `V2-014` (`CONFIRME`, grav. B) — Statut « définition » de la Proposition 2 face aux cinq conditions
- **Passages concernés :** `monographie/chapitres/06-detecter-une-erreur.md` l. 35–46, 57–62, 88 ; `monographie/chapitres/99-conclusion.md` Tableau 1.
- **Problème :** Signalé par 3 lecteurs (`C-023`, `P2-008`, `T1-003`). La Proposition 2 porte le statut *définition* et ne nomme que trois éléments (comparateur, désaccord, prise d’acte). Pourtant le texte (l. 39, l. 88) affirme qu’il en « découle » cinq conditions — dont *se tromper autrement*, *comparabilité* et *arrivée à temps* qui n’y figurent pas — et ajoute la conséquence « si une condition manque, l’échappement vaut 1 » sans statut affiché.
- **Options :** *(a)* Conserver P2 comme *définition* à 3 termes et présenter explicitement le déploiement en cinq conditions (et l’énoncé d’échappement égal à 1) comme une *décomposition analytique* / *résultat sous hypothèses* (dès qu’un désaccord probant exige différence, comparabilité et antériorité) ; *(b)* intégrer les cinq conditions dans l’énoncé même de P2 en affichant un statut *composite*.
- **Recommandation :** **Option (a)**. Elle respecte `00_global.md` § 3 (`P2` *définition*), évite de gonfler l’encadré P2 et donne un statut clair au passage des trois termes de la définition aux cinq conditions opérationnelles.
- **Décision :** 

### 10. `V2-016` (`CONFIRME`, grav. B) — Relecture de *Challenger* à travers les cinq conditions
- **Passages concernés :** `monographie/chapitres/06-detecter-une-erreur.md` l. 111–121 (§ 6.3).
- **Problème :** Signal sur `ARBITRAGES P1.5` (`C-037`, `P2-011`, `P2-012`). Trois lecteurs/constats trouvent la répartition actuelle confuse : déclarer *existence* remplie tout en disant que le comparateur complet n’a pas été assemblé paraît contradictoire, et ranger l’omission des 16 vols sans incident sous *différence* (« partageait le cadrage même de l’affirmation ») paraît forcé alors qu’il s’agit d’une sélection biaisée des données (*comparabilité*).
- **Options :** *(a)* Suivre l’option (b) déjà envisagée dans `ARBITRAGES P1.5` : fixer un seul fait par condition — *existence* : les relevés des 23 vols existaient dans les dossiers, mais le graphique complet n’était pas assemblé en séance ; *différence* : les calculs de qualification initiaux de la NASA et de Thiokol partageaient les mêmes hypothèses de comportement du joint à froid ; *comparabilité* : les planches de séance ne montraient que les 7 vols endommagés sans les 16 vols intacts ; *arrivée à temps* : alerte la veille (remplie) ; *prise en compte* : double rupture (ingénieurs sans autorité / direction renversant la charge de la preuve) ; *(b)* ramener explicitement la non-présentation des 16 vols à la seule *comparabilité* et indiquer que l’*existence* était satisfaite en puissance dans les archives.
- **Recommandation :** **Option (a)** (correspondant à l’option (b) de `ARBITRAGES P1.5`), qui donne à chaque condition un fait propre sans double emploi entre *existence*, *différence* et *comparabilité*.
- **Décision :** 

### 11. `V2-022` (`CONFIRME`, grav. B) — Statut du volet (b) de la Proposition 3
- **Passages concernés :** `monographie/chapitres/07-cadre-cause-commune.md` l. 35–42 ; `monographie/chapitres/99-conclusion.md` Tableau 1.
- **Problème :** Signal sur `DECISIONS_SYNTHESE S4` (`C-014`, `P2-016`). Le volet (b) (« des observations du monde peuvent révéler un facteur omis… ») affiche le statut *résultat sous hypothèses*, alors que le modèle M3 ne démontre que (a) et que la phrase ajoutée par `S4` pour (b) reprend la conclusion dans les hypothèses sans dérivation formelle.
- **Options :** *(a)* Reclasser le volet (b) en *hypothèse de travail* (ou en *remarque structurelle illustrée par des constats empiriques*, en réservant *résultat sous hypothèses* au seul volet (a)) au ch. 7 et dans le Tableau 1 de la Conclusion ; *(b)* ajouter dans l’encadré M3 (ou juste après la proposition) une dérivation courte reliant (b) à l’équation (5.1) de la variance totale (un $z$ qui varie engendre une variance conditionnelle $\mathbb{E}[\mathrm{Var}(Y\mid X, z)] + \mathrm{Var}(\mathbb{E}[Y\mid X, z])$ non expliquée par $X$, tandis qu’un $z$ constant s’absorbe dans la moyenne sans dispersion supplémentaire).
- **Recommandation :** **Option (b)** est mathématiquement très propre (4 lignes suffisent, appuyées sur l’éq. (5.1) déjà démontrée) ; à défaut d’ajouter cette dérivation, **Option (a)** est indispensable pour ne pas afficher un statut non prouvé.
- **Décision :** 

### 12. `V2-023` (`CONFIRME`, grav. B) — Définition restrictive de « dérive de distribution »
- **Passages concernés :** `monographie/chapitres/07-cadre-cause-commune.md` l. 85 ; `monographie/commun/registre_termes.md` l. 45.
- **Problème :** Relevé par `C-007`. Le ch. 7 et le registre définissent **dérive de distribution** uniquement comme « le changement, en exploitation, d’un facteur resté constant pendant la collecte des données ». Or, en apprentissage automatique, *distribution shift* recouvre tout changement entre entraînement et exploitation, y compris sur des variables *enregistrées* (que les détecteurs hors distribution mentionnés au ch. 5 savent repérer).
- **Options :** *(a)* Renommer le terme du registre en **dérive d’un facteur omis** (ou **dérive hors cadre**) ; *(b)* conserver **dérive de distribution** mais préciser explicitement dès la définition au § 7.3 et dans le registre qu’on vise ici le cas particulier (« au sens restreint retenu ici… ») d’un changement sur un facteur *omis* resté constant pendant la collecte, par opposition aux dérives sur variables enregistrées.
- **Recommandation :** **Option (b)** (ou **(a)** si l’auteur préfère éviter toute collision avec le lexique ML). L’option (b) préserve le lien avec l’anglais *distribution shift* dans le glossaire tout en levant l’ambiguïté pour les praticiens de l’apprentissage automatique.
- **Décision :** 

### 13. `V2-029` (`CONFIRME`, grav. A) — Contradiction de statut sur la Proposition 4
- **Passages concernés :** `monographie/chapitres/08-independance-chaines.md` l. 49–53 ; `monographie/chapitres/99-conclusion.md` Tableau 1 (l. 22) et § 2.2 (l. 53–57).
- **Problème :** Signalé par 3 lecteurs (`C-002`, `P2-023`, `T1-002`). L’en-tête de P4 affiche `statut="hypothèse de travail"`, la parenthèse juste en dessous la déclare *composite* (en classant la tension structurelle comme *définition*), et le Tableau 1 de la Conclusion classe cette même tension structurelle en *résultat sous hypothèses*. De plus, le § 8.2 fait doublon avec la note.
- **Options :** *(a)* Mettre `statut="composite"` sur l’en-tête de P4 (en vérifiant que `filtres/monographie.lua` l’accepte — ou sinon afficher deux propositions P4a/P4b) et harmoniser la répartition entre ch. 8 et Conclusion : *définition* (relativité à une classe d’erreurs), *résultat sous hypothèses* (tension structurelle : ce qui est partagé ne peut être contrôlé, or la comparaison exige un partage minimal, issu des conditions 2 et 3 de P2) et *hypothèse de travail* (tendance empirique de coût croissant avec l’indépendance) ; *(b)* scinder P4 en deux propositions numérotées.
- **Recommandation :** **Option (a)** (à condition de vérifier que le filtre accepte `composite` ou de modifier l’étiquette autorisée dans `outils/verifier.py`/`filtres/monographie.lua` si nécessaire ; sinon indiquer `hypothèse de travail` uniquement pour le second volet en scindant proprement les deux phrases). L’alignement exact entre ch. 8 et Tableau 1 de la Conclusion est impératif.
- **Décision :** 

### 14. `V2-040` (`CONFIRME`, grav. B) — Sévérité mesurée par $\Pr(\bar A \mid E)$ (collision avec la sensibilité $s$)
- **Passages concernés :** `monographie/chapitres/09-severite-echappement.md` l. 48–50.
- **Problème :** Signal sur `DECISIONS_SYNTHESE R4` (`C-008`, `P2-028`). La phrase ajoutée par `R4` (« On la mesure par $\Pr(\bar A \mid E)$, la probabilité que le contrôle donne l’alerte quand l’affirmation est fausse ») rend la sévérité numériquement identique à la sensibilité $s = \Pr(\bar A \mid E)$ introduite à la section précédente et rappelée deux lignes plus bas — créant deux termes du registre pour la même quantité et réduisant le critère de Mayo (qui compare $\Pr(A\mid \bar E)$ à $\Pr(A\mid E)$, ou le rapport de vraisemblance $(1-f)/(1-s)$) sans le dire.
- **Options :** *(a)* Clarifier dans une phrase au § 9.2 : « Dans le modèle binaire à alerte franche ($A$ ou $\bar A$), la sévérité d’un contrôle à l’égard d’une classe d’erreurs $E$ se ramène à sa sensibilité $s = \Pr(\bar A \mid E)$, tandis que la valeur probante d’un accord ($A$) dépend du rapport $(1 - f)/(1 - s)$. » ; *(b)* supprimer la phrase ajoutée par `R4` et ne garder comme mesure quantitative de la valeur probante d’un accord que le facteur $(1-f)/(1-s)$ de l’éq. (9.2).
- **Recommandation :** **Option (a)**. Elle explique explicitement le lien entre le concept général de Mayo (*sévérité*), le paramètre du contrôleur (*sensibilité* $s$) et le facteur d’un contrôle passé sans alerte ($(1-f)/(1-s)$), supprimant l’impression de doublon terminologique.
- **Décision :** 

### 15. `V3-003` (`PLAUSIBLE`, grav. C) — Statut de « changement de régime » dans la Conclusion
- **Passages concernés :** `monographie/parties/partie-3.md` l. 9 ; `monographie/chapitres/12-autre-regime.md` ; `monographie/chapitres/99-conclusion.md` l. 28 (Tableau 1).
- **Problème :** `T1-014` relève que le Tableau 1 de la Conclusion classe le « changement de régime » au ch. 12 comme *définition*, alors que l’énoncé recouvre deux choses : la dénomination du basculement simultané des trois propriétés (définition) et l’affirmation qu’elles basculent ensemble sous l’effet de l’absence de spécification écrite (thèse structurelle / empirique).
- **Options :** *(a)* Préciser dans le Tableau 1 de la Conclusion : *définition* pour la désignation des trois bascules au sommet de la pile ; *hypothèse de travail* (illustrée par des *constats empiriques*) pour leur lien avec l’absence de spécification vérifiable ; *(b)* laisser en l’état (terme défini au registre).
- **Recommandation :** **Option (a)**, retouche d’une ligne dans le Tableau 1 qui le met à l’abri de toute critique de statut.
- **Décision :** 

### 16. `V5-001` (`CONFIRME`, grav. A, fusionnée avec `V1-002`) — Contradiction de la roulette russe dans le modèle M2
- **Passages concernés :** `monographie/chapitres/04-decider.md` l. 84 et 119 ; `monographie/chapitres/17-decisions-sans-appel.md` l. 64 ; `monographie/commun/parametres.py` et `tableaux/ch04-seuil.md`, `ch17-scenarios.md`, `ch17-decisions.md` (si scénario modifié).
- **Problème :** Signal sur `ARBITRAGES P2.2.2` (`DEC-S6`) confirmé par 3 lecteurs (`C-001`, `P1-002`, `P5-005`). Aux ch. 4 et 17, le joueur « croit l’arme déchargée et estime à $p = 0{,}001\,\%$ le risque résiduel qu’une balle ait été oubliée dans la chambre », puis la balle engagée dans l’une des six chambres ($z = 1/6 \approx 16{,}7\,\%$) est traitée comme un facteur *omis par son cadre* et *indépendant de $p$*. Or si l’éventualité d’une balle est dans $p$, une balle dans le barillet n’est ni hors du cadre ni indépendante de $p$ : c’est une erreur d’estimation *dans* le cadre.
- **Options :** *(a)* Maintenir les chiffres ($L/\Delta U = 10\,000$, $p = 0{,}001\,\%$, $z = 1/6$) mais changer le récit pour que $p$ et $z$ portent sur des mécanismes distincts : soit le joueur évalue uniquement un risque générique d’incident mécanique / d’amorce sur un pistolet à un coup qu’il croit neutralisé, et ignore qu’un barillet rotatif a été réarmé ($z = 1/6$) — mais cela reste artificiel ; soit *(b)* conserver la roulette russe uniquement au ch. 4 (comme exemple d’enjeu extrême $L/\Delta U = 10\,000$ où le joueur commet une erreur d’estimation $p$ ou croit l’arme vide avec $p=0{,}001\,\%$, sans l’invoquer en 4.5 comme facteur omis), et la remplacer dans le modèle M2 du ch. 17 (lignes 5–6 du Tableau 17.2) par un exemple physique net où $p$ et $z$ sont réellement disjoints (par exemple : traversée d’un pont ou vol en montagne à fort enjeu $L/\Delta U = 10\,000$, où $p = 0{,}001\,\%$ est la probabilité de panne mécanique connue et $z = 16{,}7\,\%$ un défaut d’entretien ignoré du cadre — ou bien garder les 5 lignes sans roulette dans M2 et consacrer un bref paragraphe à l’écart entre $p^\ast = 0{,}0100\,\%$ et toute marge plausible).
- **Recommandation :** **Option (b)** (ou, si l’auteur souhaite garder la roulette russe sans régénérer `parametres.py`, préciser explicitement au ch. 4 § 4.3 et au ch. 17 que le joueur croit participer à un simulacre avec arme neutralisée où $p = 0{,}001\,\%$ couvre un aléa d’armement, tandis qu’une arme chargée à balles réelles — $z = 1/6$ — relève d’une substitution non envisagée par son cadre ; toutefois, même ainsi, la roulette russe reste moins convaincante que l’avarie cachée du mât de M. Y). Remplacer la ligne 6 de M2 au ch. 17 par un cas sans collision (ou limiter la roulette russe au ch. 4 § 4.3 comme illustration de $L/\Delta U = 10\,000$ en la retirant de § 4.5 et de M2) règle le problème à la racine.
- **Décision :** 

### 17. `V5-011` (`PLAUSIBLE`, grav. C) — Critère des environnements `.definition` numérotés
- **Passages concernés :** `monographie/chapitres/17-decisions-sans-appel.md` l. 17 ; `monographie/commun/registre_termes.md` ; `monographie/chapitres/00-avant-propos.md`.
- **Problème :** `T1-018` note que certains concepts majeurs (*marge d’humilité*, *changement de régime*, *omission structurelle* / *de saillance*, *erreur signalée* / *silencieuse*) sont définis en gras dans le fil du texte sans bloc `.definition` numéroté, à la différence de *verrou* et *bac à sable* (14 étiquettes `def:` seulement sur ~64 termes du registre).
- **Options :** *(a)* Conserver la sélection actuelle des 14 définitions formelles et préciser d’une phrase dans l’avant-propos que les blocs `Définition` ne concernent que les briques des modèles et propositions, les autres termes du glossaire étant introduits en gras dans le texte ; *(b)* promouvoir les 4–5 notions clés restantes (dont *marge d’humilité*) en blocs `.definition`.
- **Recommandation :** **Option (a)** (un mot dans l’avant-propos), pour ne pas alourdir la mise en page par des dizaines de boîtes numérotées.
- **Décision :** 

### 18. `V5-044` (`PLAUSIBLE`, grav. B) — Longueur et redondance de la Conclusion
- **Passages concernés :** `monographie/chapitres/99-conclusion.md` (~5 900 mots, § 2 l. 53–95 et *Points clés* l. 146–154).
- **Problème :** `T5-024` et `piste-rep-04` signalent que la Conclusion réexpose au fond des développements déjà faits aux ch. 8, 9 et 16 (tension P4, exemple de la ferrure, calcul 10 %×1 % vs 1 %×90 %, lassitude face aux alertes) et clôt sur cinq *Points clés* très longs, au lieu de renvoyer brièvement au texte pour ne retenir que ce qui reste ouvert.
- **Options :** *(a)* Conserver l’autonomie actuelle de la § 2 pour les lecteurs qui ne lisent que l’avant-propos et la conclusion (en appliquant uniquement la coupe de la « Genèse » `V5-034`), tout en resserrant les 5 *Points clés* à une phrase chacun ; *(b)* resserrer également les sous-sections § 2.1–2.6 de moitié en renvoyant aux chapitres concernés.
- **Recommandation :** **Option (a)** (plus **Option (b)** ciblée sur la seule réexposition de la ferrure et du calcul 10 %×1 % en § 2.2–2.3). Cela garde l’intérêt d’une conclusion auto-suffisante sans répéter les exemples chiffrés déjà vus trois fois.
- **Décision :** 

---

## 4. Arbitrages rapides (groupe 2)

Les **89 grappes actives de groupe 2** (56 `CONFIRME`, 33 `PLAUSIBLE`) sont classées ci-dessous **dans l’ordre des fichiers du livre**. Les 23 grappes `CONFIRME` déjà munies d’une retouche exacte dans `relecture/sorties/synthese/corrections.json` sont marquées `[JSON]`.

### `monographie/chapitres/00-avant-propos.md`
- **`V0-006` (`CONFIRME`, grav. B, `P0-005`)** — *Problème :* « hypothèse de travail » est employé en l. 15 au sens courant de conjecture provisoire avant d’être défini en l. 58 comme statut épistémique précis. *Retouche proposée :* remplacer en l. 15 par « la meilleure conjecture disponible » (ou « la meilleure représentation provisoire »).
  `Décision :` 
- **`V0-027` (`PLAUSIBLE`, grav. C, `P0-016`)** — *Problème :* la section « Genèse et responsabilité » (5 §) paraît un peu longue et défensive sur le témoignage de l’article antérieur. *Retouche proposée :* resserrer éventuellement d’un paragraphe ou laisser en l’état (choix d’auteur).
  `Décision :` 

### `monographie/chapitres/00-cartographier.md`
- **`V0-003` (`CONFIRME`, grav. B, `P0-007`, `T1-010`)** — *Problème :* l’essai METR (Becker et al. 2025) est présenté en 0.1 comme un « enseignement durable » et en 0.5.2 (l. 127) comme une loi causale générale. *Retouche proposée :* formuler en 0.1 et 0.5.2 comme une possibilité illustrée par un cas daté (« le ressenti d’experts *peut* s’inverser / cesser d’être un comparateur fiable »).
  `Décision :` 
- **`VX-032` (`PLAUSIBLE`, grav. B, `T1-007`)** — *Problème :* la « frontière en dents de scie » est présentée comme un trait général en § 0.4 et au Point clé 2 du ch. 12, alors que le Tableau 1 de la Conclusion la classe en *constat empirique daté* (BCG). *Retouche proposée :* ajouter une incise « observée notamment sur des modèles récents » en 0.4 et au Point clé du ch. 12.
  `Décision :` 
- **`VX-001` (`CONFIRME`, grav. B, `C-003`, `T5-029` — fusionne `V0-025`) `[JSON]`** — *Problème :* l’énigme 0.5.4 (10 %×1 % vs 1 %×90 %) est perçue comme la thèse typique du livre, alors que la Table 16.1 montre une baisse du risque global et que la Conclusion dit qu’il s’agit d’une possibilité. *Retouche proposée :* patch exact en `corrections.json` remplaçant « dix fois plus exact » (`V0-009`) et précisant « montre une possibilité, dont le @sec:ch16 précisera à quelles conditions elle se réalise » (en outre, examiner en lien avec `V4-019` l’ajout éventuel d’une colonne au Tableau 16.1 où le risque monte).
  `Décision :` 
- **`V0-022` (`CONFIRME`, grav. C, `P0-021`)** — *Problème :* malgré `DECISIONS_SYNTHESE V4`, « partagent l’interface avec le producteur » et « le niveau situé dessous » en 0.6 restent obscurs avant le ch. 18 (aussi signalé en `RAPPORT_AUDIT_CALQUES.md` l. 159). *Retouche proposée :* « des relecteurs qui maîtrisent le domaine du producteur et le niveau technique sous-jacent : le code… ».
  `Décision :` 
- **`V0-024` (`CONFIRME`, grav. C, `T1-030`, `T5-027`)** — *Problème :* la liste des exemples récurrents en 0.7 omet des chapitres notables (voiliers ch. 2 ; ferrure ch. 6, 13, 17 ; MCO ch. 11, 13, 14 ; Challenger ch. 13, 18). *Retouche proposée :* remplacer les listes fermées par « notamment aux chapitres… » (ou compléter).
  `Décision :` 
- **`V0-012` (`CONFIRME`, grav. C, `C-027`, `P0-011`, `T2-012`, `T5-008` — fusionne `V5-016`)** — *Problème :* malgré `N3`, 4 lecteurs butent sur l’ordre M3 (ch. 7) $\to$ M1 (ch. 8–9) $\to$ M2 (ch. 17) et sur ces sigles en 0.7. *Retouche proposée :* soit renuméroter M1 (ch. 7), M2 (ch. 8–9), M3 (ch. 17) dans tout le livre (lourd sur les renvois internes/annexes), soit retirer les sigles `M1–M3` du ch. 0.7 (en gardant la description des trois modèles dans l’ordre d’apparition : ch. 7, ch. 8–9, ch. 17) et expliquer brièvement au ch. 8 pourquoi M1 est numéroté en tête (modèle central).
  `Décision :` 
- **`V0-014` (`CONFIRME`, grav. C, `C-051`, `T1-017`, `T5-026`)** — *Problème :* le « Parcours critique » de la Table 0.1 omet 8 chapitres qui possèdent un bloc `.nuance` (1, 2, 4, 6, 10, 11, 15, 18). *Retouche proposée :* compléter la liste (au moins avec 4, 6, 10, 11, 15, 18) ou préciser « sélection de blocs *Nuance*… ».
  `Décision :` 
- **`V0-023` (`CONFIRME`, grav. C, `T1-029`)** — *Problème :* les six *Points clés* du ch. 0 omettent la probabilité comme jugement et le seuil de décision unique face aux enjeux asymétriques. *Retouche proposée :* compléter le 1er point clé ou en ajouter un 7e en une phrase.
  `Décision :` 

### `monographie/chapitres/01-outils-logique-probabilite.md`
- **`V1-021` (`CONFIRME`, grav. C, `C-052`) `[JSON]`** — *Problème :* le titre `# Boîte à outils : …` reprend le nom d’un type d’encadré facultatif alors que le ch. 1 définit des termes obligatoires du registre (même ambiguïté sur 8.1 et 10.1, cf. `V3-004`). *Retouche proposée :* `# Outils de logique et de probabilité {#sec:ch01}` (patch en `corrections.json`) et harmoniser 8.1 / 10.1.
  `Décision :` 
- **`V1-005` (`CONFIRME`, grav. B, `P1-006`, `T5-016`, `PISTE-REP-01`) `[JSON]`** — *Problème :* la section 1.2 détaille déjà toutes les exceptions de l’ébullition que le ch. 2 (2.2) va redérouler juste après. *Retouche proposée :* alléger 1.2 au sel et à l’altitude en renvoyant au ch. 2 (patch en `corrections.json`).
  `Décision :` 

### `monographie/chapitres/02-cadre.md`
- **`V1-013` (`CONFIRME`, grav. C, `C-046`) `[JSON]`** — *Problème :* malgré `ARBITRAGES P2.3.1` (`SYN-C1`), la 2e phrase de la Déf. 1 (« Le monde, lui, répond à l’action, non à la représentation ») reste perçue comme une thèse hors définition. *Retouche proposée :* sortir cette seconde phrase juste sous l’encadré `.definition` (patch en `corrections.json` ; laisser ou ajuster le Tableau 1 en conséquence).
  `Décision :` 
- **`V1-026` (`PLAUSIBLE`, grav. C, `P1-011`)** — *Problème :* la Déf. 2 dit « choisi avant toute inférence » alors que la l. 87 reconnaît qu’il procède d’un savoir antérieur. *Retouche proposée :* « choisi en amont de l’inférence qu’il encadre » (au ch. 2 l. 67 et dans `registre_termes.md` l. 19).
  `Décision :` 

### `monographie/chapitres/03-mondes-possibles.md`
- **`V1-022` (`CONFIRME`, grav. C, `T5-017`, `PISTE-REP-02`) `[JSON]`** — *Problème :* la l. 9 du ch. 3 répète mot pour mot trois formules de 2.1 sur le 5 % du mât. *Retouche proposée :* condenser en une phrase de rappel (patch en `corrections.json`).
  `Décision :` 
- **`V1-011` (`CONFIRME`, grav. C, `C-048`) `[JSON]`** — *Problème :* l’événement passe de « démâter » (ch. 0, 2) à « démâte ou subisse une avarie » en 3.3 avec les mêmes chiffres. *Retouche proposée :* aligner 3.3 sur « casse (démâte) » (patch en `corrections.json`).
  `Décision :` 
- **`VX-008` (`PLAUSIBLE`, grav. C, `P1-019`)** — *Problème :* $p$ change de sens entre 1.6, 3.4 et 4.2 ; $T$ (intervention au ch. 2) reste proche de $\mathcal{T}$. *Retouche proposée :* rappeler le sens local de $p$ en 1.6/3.4 et renvoyer les omissions de l’annexe C ($\Lambda, S$) à `VX-021`.
  `Décision :` 

### `monographie/chapitres/04-decider.md`
- **`V1-027` (`PLAUSIBLE`, grav. C, `P1-020`)** — *Problème :* la 4e « hypothèse » du noyau formel (l. 52) mêle hypothèse de décision sur $p$ et remarque de portée. *Retouche proposée :* isoler la seconde phrase en remarque après la liste numérotée.
  `Décision :` 
- **`V1-006` (`CONFIRME`, grav. B, `P1-007`) `[JSON]`** — *Problème :* l’exemple quantitatif de 4.3 refait mot pour mot les calculs faits deux fois en 4.2 et au début de 4.3. *Retouche proposée :* condenser le paragraphe de calcul en renvoyant au tableau et à la figure (patch en `corrections.json`).
  `Décision :` 

### `monographie/parties/partie-2.md`
- **`V2-001` (`CONFIRME`, grav. B, `P2-001`) `[JSON]`** — *Problème :* `partie-2.md` promet des exemples choisis hors IA mais les ch. 7 et 9 citent Sutton & Barto, Google Flu Trends, les modèles statistiques et des relecteurs logiciels. *Retouche proposée :* écrire « ses *principaux* exemples » (patch en `corrections.json`).
  `Décision :` 
- **`V2-002` (`CONFIRME`, grav. B, `T1-005`) `[JSON]`** — *Problème :* `partie-2.md` l. 9 énonce P3(a) sans réserve (« jamais de découvrir un facteur que le cadre a omis »). *Retouche proposée :* ajouter « tant qu’ils restent dans le même cadre » (patch en `corrections.json`).
  `Décision :` 
- **`V2-003` (`PLAUSIBLE`, grav. C, `C-054`)** — *Problème :* la fin de phrase l. 11 (issue de `P1.6`) reste elliptique avant le ch. 8. *Retouche proposée :* « et l’indépendance se paie toujours, soit en coût direct de production, soit en effort de traduction et de prise en compte ».
  `Décision :` 

### `monographie/chapitres/05-trois-incertitudes.md`
- **`VX-011` (`CONFIRME`, grav. B, `C-039`, `P1-003`, `P2-002`, `P3-031`, `P5-012`, `T5-031` — fusionne `V1-007`, `V2-010`, `V3-041`)** — *Problème :* l’autocitation `[@fauriat2026frame]` apparaît 36 fois (7 en ch. 2, 7 en ch. 5, 5 en ch. 17, 7 en ch. 18, etc.), y compris pour des distinctions classiques (aléatoire/épistémique en 5.2, V&V en 13.3) ou des faits documentés ailleurs (2008 en 5.3). *Retouche proposée :* ajouter des références primaires reconnues pour aléatoire/épistémique (ex. Der Kiureghian & Ditlevsen 2009 / Hora 1996) et V&V (ASME / IEEE / Oberkampf & Roy), et réduire les occurrences redondantes de `[@fauriat2026frame]` aux seuls apports spécifiques de l’article.
  `Décision :` 
- **`V2-011` (`PLAUSIBLE`, grav. C, `P2-006`)** — *Problème :* « encore calme à 101 °C » (l. 79) est elliptique si le lecteur a oublié la Table 2.1. *Retouche proposée :* « qui ne bout pas encore à 101 °C ».
  `Décision :` 
- **`VX-004` (`PLAUSIBLE`, grav. B, `C-020`, `P1-008`)** — *Problème :* plusieurs exemples récurrents (ébullition en 5.4, navigateur à 5 % doublé du téléphone satellite en 2.1, ferrure à 1,8) sont réexposés avec les mêmes détails. *Retouche proposée :* voir le plan d’allègement global en § 6.
  `Décision :` 

### `monographie/chapitres/06-detecter-une-erreur.md`
- **`V2-018` (`PLAUSIBLE`, grav. C, `P2-009`)** — *Problème :* l’ouverture de la *Nuance* l. 58 répète presque mot pour mot l’explication de la l. 39 sur le statut presque définitionnel de P2. *Retouche proposée :* ouvrir la *Nuance* directement sur son apport (« Aucune expérience empirique ne saurait la démentir… »).
  `Décision :` 

### `monographie/chapitres/07-cadre-cause-commune.md`
- **`V2-021` (`CONFIRME`, grav. A, `P2-015`) `[JSON]`** — *Problème :* dans la preuve du modèle M3 (l. 56), si $f_1$ comporte des tirages aléatoires internes (permis par l’hyp. 1), l’accord $A$ dépend de $f_1(x)$ et donc de l’erreur $e(x,z) = g(x,z) - f_1(x)$, invalidant la conclusion $A \perp e \mid X=x$. *Retouche proposée :* stipuler $f_1$ déterministe sachant $x$ dans l’hypothèse 1 (patch en `corrections.json` ; harmonisé avec `VX-013` en annexe A).
  `Décision :` 
- **`V2-024` (`CONFIRME`, grav. C, `C-043`, `P2-019`) `[JSON]`** — *Problème :* Google Flu Trends a été révisé après 2009 et en 2013 (il n’appliquait donc pas « la même méthode ») et la remarque sur ses contrôles internes n’est pas sourcée. *Retouche proposée :* recentrer sur le surajustement aux requêtes selon `[@lazer2014]` (patch en `corrections.json`).
  `Décision :` 
- **`V2-027` (`PLAUSIBLE`, grav. B, `P2-020`)** — *Problème :* les théorèmes *no free lunch* (l. 109) sont présentés comme « une expression mathématique précise » de la régression des méta-procédures alors qu’ils portent sur l’optimisation moyenne sans a priori. *Retouche proposée :* qualifier le rapprochement d’« analogie précise dans le domaine de l’optimisation ».
  `Décision :` 
- **`V2-028` (`PLAUSIBLE`, grav. B, `P2-021`)** — *Problème :* « les deux seules voies » (l. 121 et Point clé 5) semble exclure la réflexion théorique ou l’expérience de pensée. *Retouche proposée :* « les deux voies principales par lesquelles… ».
  `Décision :` 

### `monographie/chapitres/08-independance-chaines.md`
- **`V2-034` (`CONFIRME`, grav. B, `P2-022`)** — *Problème :* la section 8.1 répète l’exemple des deux pompes et de la borne $q$ du § 7.1, puis redit en boîte à outils ce que la prose vient d’exposer. *Retouche proposée :* renvoyer au § 7.1 pour les pompes et centrer la § 8.1 sur série/parallèle (et harmoniser le titre `Boîte à outils :` avec `V1-021` / `V3-004`).
  `Décision :` 
- **`V2-036` (`PLAUSIBLE`, grav. C, `P2-025`)** — *Problème :* l’interprétation de Knight & Leveson (1986) (« Parce que les 27 développeurs partageaient l’énoncé… ») est donnée comme un fait établi, et `partie-2.md` parle d’« équipes » au lieu de « programmeurs ». *Retouche proposée :* « Les auteurs attribuent cette convergence au fait que… » et uniformiser « programmeurs ».
  `Décision :` 
- **`V2-033` (`PLAUSIBLE`, grav. C, `C-036`)** — *Problème :* justifier $m = p = 6\,\%$ par « la même compétence que le producteur » (l. 144) confond taux d’erreur à la production et taux d’oubli en relecture. *Retouche proposée :* « un pair qui, pour l’illustration, laisse échapper chaque erreur indépendante avec la même probabilité $m = p = 6\,\%$ ».
  `Décision :` 
- **`V2-030` (`CONFIRME`, grav. B, `C-004`, `P2-027`) `[JSON]`** — *Problème :* la *Nuance* l. 161 écrit « Si une erreur n’appartient pas à $B_1$, le producteur la voit et ne l’émet pas », contredisant M1 et l’exemple chiffré ($p = 6\,\%$ d’erreurs ponctuelles hors $B_1$). *Retouche proposée :* limiter explicitement l’énoncé aux causes structurelles de l’éq. (8.2) (patch en `corrections.json`).
  `Décision :` 
- **`V2-038` (`PLAUSIBLE`, grav. C, `T5-012`)** — *Problème :* l’encadré `.cas` de 8.6 répète les données de *Mars Climate Orbiter* déjà données en 0.1 avant d’introduire le blanchiment. *Retouche proposée :* voir plan d’allègement en § 6.
  `Décision :` 

### `monographie/chapitres/09-severite-echappement.md`
- **`V2-052` (`CONFIRME`, grav. B, `T5-018`)** — *Problème :* les cinq conditions de détection sont réénumérées *in extenso* dans les chapeaux des ch. 8 (l. 3) et 9 (l. 3) après 0.3.2, `partie-2.md` et ch. 6. *Retouche proposée :* renvoyer à « les cinq conditions de détection du @sec:ch06 » dans les chapeaux des ch. 8 et 9.
  `Décision :` 
- **`V2-044` (`PLAUSIBLE`, grav. C, `P2-031`)** — *Problème :* « prise en compte » désigne à la fois la condition qualitative (Déf. 6) et la proportion quantitative $u$. *Retouche proposée :* gloser en l. 82 « ou taux de prise en compte, noté $u$ ».
  `Décision :` 
- **`V2-050` (`PLAUSIBLE`, grav. B, `T1-009`)** — *Problème :* « Les batteries d’évaluations comparatives… notent, par construction, le producteur seul » (l. 98) généralise sans nuance ni référence. *Retouche proposée :* écrire « Les batteries d’évaluations comparatives usuelles notent… ».
  `Décision :` 
- **`V2-042` (`CONFIRME`, grav. C, `C-031`) `[JSON]`** — *Problème :* l’incise l. 112 (issue de `ARBITRAGES P1.9`) promet à tort que $R$ sera comparé à $p^\ast$ au ch. 17, où il n’est question que de $p+b$. *Retouche proposée :* supprimer la parenthèse fautive (patch en `corrections.json`).
  `Décision :` 
- **`V2-043` (`PLAUSIBLE`, grav. C, `C-024`)** — *Problème :* au ch. 9, le scénario « *Indépendant et précis* » a le même $c = 10\,\%$ que « *Contrôle entre pairs* », rendant son nom opaque avant le ch. 16. *Retouche proposée :* ajouter l’incise « (nommé ainsi par contraste avec les scénarios corrélés du @sec:ch16) ».
  `Décision :` 
- **`V2-048` (`PLAUSIBLE`, grav. C, `P2-035`)** — *Problème :* dans la Table 9.4, le second scénario change simultanément $P(\text{faux})$, $m$ et $f$, empêchant le tableau seul d’isoler le levier $f$. *Retouche proposée :* renvoyer explicitement à la lecture à $P(\text{faux}) = 2\,\%$ sur la courbe de la Fig. 9.1 ($\mathrm{VPP} \approx 25\,\%$).
  `Décision :` 

### `monographie/chapitres/10-couches-basses.md`
- **`V3-004` (`PLAUSIBLE`, grav. C, `P3-009`)** — *Problème :* titre `## Boîte à outils : les contrats logiciels` (même ambiguïté que ch. 1 et 8.1) et triplet de Hoare exposé en texte puis aussitôt dans l’encadré `.outils`. *Retouche proposée :* renommer la section en `## Les contrats logiciels {#sec:ch10-boite-outils}` (patch prêt si validé) et alléger l’ouverture de l’encadré `.outils`.
  `Décision :` 
- **`V3-006` (`CONFIRME`, grav. B, `P3-003`) `[JSON]`** — *Problème :* contradiction entre le 3e degré du contrat (formulable après coup, l. 72) et la l. 74 / le Point clé 2 qui exigent un texte écrit *avant* l’exécution. *Retouche proposée :* distinguer le code (écrit avant l’usage) du contrat (écrit d’avance ou formulable après coup) (patch en `corrections.json`).
  `Décision :` 
- **`V3-008` (`CONFIRME`, grav. B, `C-019`, `T5-011`) `[JSON]`** — *Problème :* *Mars Climate Orbiter* est raconté deux fois de suite en § 10.5 (prose l. 107–109 puis `.cas` l. 113–119) après ch. 0 et ch. 8. *Retouche proposée :* condenser la prose en un bref rappel technique renvoyant au ch. 8 et conserver l’encadré `.cas` pour l’adresse et l’organisation (patch en `corrections.json`).
  `Décision :` 
- **`V3-009` (`PLAUSIBLE`, grav. C, `P3-004`)** — *Problème :* « Les analyses après incident convergent vers une adresse » (l. 121) paraît trop absolu pour les bogues de concurrence ou d’interaction. *Retouche proposée :* « convergent le plus souvent vers une adresse — une ligne, une interface ou une interaction précise entre tâches — ».
  `Décision :` 
- **`V3-010` (`CONFIRME`, grav. B, `P3-006`)** — *Problème :* les trois degrés du contrat sont exposés en prose (l. 123) puis repris quasi à l’identique dans l’encadré `.nuance` qui suit (l. 125–133). *Retouche proposée :* alléger la `.nuance` pour n’y garder que le classement explicite de `SM_FORCES` au 2e degré et la transition vers le ch. 11.
  `Décision :` 

### `monographie/chapitres/11-regle-tiree-des-donnees.md`
- **`V3-013` (`CONFIRME`, grav. C, `T5-030`)** — *Problème :* le motif « personne ne savait écrire la règle » est répété fin ch. 10, chapeau ch. 11 et § 11.1 (en plus du ch. 0 et de `partie-3.md`). *Retouche proposée :* alléger la fin du ch. 10 (sans liste d’exemples) et le chapeau du ch. 11, garder le développement en 11.1.
  `Décision :` 
- **`V3-015` (`CONFIRME`, grav. C, `C-044`)** — *Problème :* la § 11.4 range tout le post-entraînement sous l’ajustement sur préférences humaines et omet le renforcement sur récompenses vérifiables (code, maths), qui introduit pourtant un comparateur mécanique dans l’objectif et prépare le ch. 12. *Retouche proposée :* ajouter deux phrases en 11.4 précisant que le renforcement contre un comparateur mécanique améliore les tâches vérifiables sans doter le modèle d’un contrat général.
  `Décision :` 

### `monographie/chapitres/12-autre-regime.md`
- **`V3-020` (`CONFIRME`, grav. B, `P3-013`)** — *Problème :* 12.1 et le Point clé 2 font de la seule absence de spécification vérifiable le critère du changement de régime, alors que 12.2 montre que les anciens filtres statistiques n’étaient pas spécifiés non plus mais restaient cantonnés (non généralistes/composables). *Retouche proposée :* mentionner explicitement la conjonction « absence de spécification + emploi généraliste et composable » en 12.1, au Point clé 2 et en `partie-3.md`.
  `Décision :` 
- **`V3-024` (`PLAUSIBLE`, grav. C, `P3-017`)** — *Problème :* *omission de saillance* utilise « omission » pour un facteur présent dans la représentation (et classé en « Cause dans le cadre » au ch. 13), et dit « affine » la P3 alors qu’elle en restreint le volet (a). *Retouche proposée :* gloser en 12.3 qu’il s’agit d’une omission *de mobilisation* (d’usage) et non d’une absence du cadre.
  `Décision :` 
- **`V3-029` (`CONFIRME`, grav. C, `P3-021`)** — *Problème :* 12.4 (6 occurrences) et `tableaux/ch12-plausibilite.md` emploient « alerte à tort » au lieu du terme du registre « taux de fausses alertes » (voir aussi `VX-024`). *Retouche proposée :* harmoniser sur « fausse alerte » (ou expliquer explicitement que la divergence sur une 1re réponse juste du fait rare mesure l’incertitude épistémique du modèle).
  `Décision :` 

### `monographie/chapitres/13-synthese-deux-axes.md`
- **`V3-031` (`CONFIRME`, grav. B, `T5-019`)** — *Problème :* la phrase d’ouverture du ch. 13 (~220 mots) aligne douze renvois numérotés sans rappel lisible. *Retouche proposée :* scinder en 3 phrases courtes et retirer les numéros de définitions superflus.
  `Décision :` 
- **`V3-033` (`CONFIRME`, grav. B, `C-015`, `P3-023`)** — *Problème :* malgré `ARBITRAGES P1.3` (`REV-4A.3`), la l. 15 fait glisser « cadre » de la Déf. 2 au « cadre du problème posé par l’utilisateur », l’encadré formel l. 51 traite appris et spécifiés à parité, et le caractère graduel de cet axe pour les composants appris (reconnu en Conclusion l. 63) n’est pas annoncé en 13.1. *Retouche proposée :* assumer explicitement en 13.1 l’extension à « cadre de la tâche » et annoncer dès 13.1 que la frontière entre les deux lignes devient une affaire de degré pour les composants appris.
  `Décision :` 
- **`V3-035` (`CONFIRME`, grav. B, `P3-024`)** — *Problème :* le paragraphe principal (l. 35) et la `.nuance` qui suit (l. 37–41) répètent l’idée « vider cette case à l’avance » avec MCO. *Retouche proposée :* garder l. 35 et resserrer la `.nuance` sur ses apports propres (préconditions tacites, cas limites, contrats non exécutés).
  `Décision :` 
- **`V3-038` (`CONFIRME`, grav. B, `P3-028`) `[JSON]`** — *Problème :* le bloc « Autoformalisation et noyau de confiance en Lean » est balisé `.cas` alors qu’il ouvre sur un scénario hypothétique (« Considérons un problème mathématique… ») sans épisode daté. *Retouche proposée :* changer `.cas` en `.outils` (patch en `corrections.json`).
  `Décision :` 
- **`V3-039` (`CONFIRME`, grav. B, `P3-029`)** — *Problème :* 13.2.4 affirme d’abord que le monde est « le seul comparateur qui n’ait pas de cadre propre » (l. 120), puis y range les environnements informatiques (compilateur, tests) qui « rejoignent la première source » et reposent sur des cadres formels (l. 122). *Retouche proposée :* distinguer dès l’ouverture de 13.2.4 le monde physique/clinique/institutionnel (sans cadre propre) de l’environnement informatique d’exécution (confrontation réelle au sein d’un cadre formel).
  `Décision :` 

### `monographie/parties/partie-4.md`
- **`V4-026` (`CONFIRME`, grav. B, `P4-015`, `T5-003`)** — *Problème :* `partie-4.md` l. 3 dit que tous les épisodes cités sont en `.cas` (faux : seuls Knight Capital et METR le sont) et résume longuement chaque chapitre en l. 5–9. *Retouche proposée :* corriger « deux études de cas » en l. 3 et condenser l. 5–9 (en coordination avec `VX-034`).
  `Décision :` 
- **`VX-007` (`CONFIRME`, grav. C, `C-026`)** — *Problème :* malgré `DECISIONS_SYNTHESE V16`, la locution « contrôles en chaîne » subsiste (`partie-4.md`, `partie-5.md`, `ch18`, `99-conclusion.md`, `partie-2.md` « assembler des contrôles ») en contradiction avec le ch. 8 (chaîne de *composants* vs contrôle croisé). *Retouche proposée :* harmoniser sur « met nos étapes en chaîne » / « place des composants en chaîne sans contrôle » (comme déjà fait en ch. 0.5.1).
  `Décision :` 

### `monographie/chapitres/14-chaines-qui-agissent.md`
- **`V4-002` (`CONFIRME`, grav. B, `C-022`, `T5-022`)** — *Problème :* 14.1 (l. 11–13) duplique presque mot pour mot 8.4 (hiérarchie des finalités, chaîne automobile), et les mises en place des exemples quantitatifs 14.2.3 et 16.1 refont longuement celles des ch. 8 et 9. *Retouche proposée :* remplacer la duplication 14.1 par un rappel bref renvoyant à 8.4, et alléger la mise en place de 14.2.3 (garder le tableau à $N=12$) et de 16.1.
  `Décision :` 

### `monographie/chapitres/15-erosion-verifications.md`
- **`VX-003` (`PLAUSIBLE`, grav. C, `C-018`)** — *Problème :* « vérifications humaines » (titre ch. 15, ch. 0, `partie-4.md`) emploie *vérification* au sens courant de *contrôle* avant/après sa définition technique au ch. 13. *Retouche proposée :* soit conserver l’emploi idiomatique « vérifications humaines » en le glosant d’un mot, soit renommer en « L’érosion des contrôles humains » (plus conforme à la règle du terme unique).
  `Décision :` 
- **`VX-005` (`CONFIRME`, grav. B, `C-021`, `P2-013`, `P3-007`, `T5-010`, `T5-013`, `piste-rep-01` — fusionne `V0-011`, `V3-016`, `V4-027`)** — *Problème :* quatre études de cas (*METR 2025*, *Mata v. Avianca*, *Challenger*, *Mars Climate Orbiter*) sont racontées *in extenso* à plusieurs reprises en lecture linéaire (`TODO P2.4` / `REV-3.1` non appliqué). *Retouche proposée :* appliquer le plan d’allègement détaillé en § 6 (un seul récit complet par cas, rappels d’une phrase ailleurs).
  `Décision :` 
- **`V4-013` (`CONFIRME`, grav. B, `P4-003`)** — *Problème :* le corps (l. 52) attribue « équilibre mélangeant » à Akerlof 1970 et l’encadré (l. 60) confond le mélange initial (prix unique) avec la sélection adverse dynamique qui finit par *détruire* le mélange. *Retouche proposée :* garder le terme du registre en l. 52 sans l’attribuer à Akerlof, et distinguer dans l’encadré le mélange initial (Spence) de l’éviction dynamique des bons véhicules (Akerlof 1970), comme fait par `VX-025` en annexe A.
  `Décision :` 
- **`V4-011` (`CONFIRME`, grav. B, `P4-001`)** — *Problème :* malgré `ARBITRAGES P1.11.3` (`SYN-E3`), `partie-4.md`, le chapeau du ch. 15 et les *Points clés* exigent un « problème nu sans transmettre son cadre », tandis que la l. 92 tolère encore un texte déjà rédigé qui transmet le découpage. *Retouche proposée :* soit retirer la tolérance du texte déjà rédigé en 15.4, soit mentionner dès les *Points clés* et l’introduction qu’un texte déjà rédigé n’est qu’un pis-aller dégradé.
  `Décision :` 

### `monographie/chapitres/16-angles-morts-collectifs.md`
- **`V4-019` (`CONFIRME`, grav. B, `P4-010`, `T1-006`)** — *Problème :* malgré `ARBITRAGES P1.1`, le titre de 16.1 (« Le taux d’erreur baisse, la probabilité d’échappement monte »), le 1er *Point clé* (l. 116) et `partie-4.md` (l. 9) affirment sans condition que l’usage d’un modèle partagé fait monter l’échappement, alors que la hausse de $c$ est une hypothèse de travail et que le risque global baisse dans le Tableau 16.1 ($5{,}57\,\% \to 1{,}93\,\%$). *Retouche proposée :* reformuler le titre (en conservant `#sec:ch16-taux-echappement`), le Point clé et `partie-4.md` pour marquer le caractère conditionnel (« Quand le taux d’erreur baisse mais que les causes partagées dominent… »), et décider s’il faut ajouter une colonne au Tableau 16.1 (ex. $P(\text{faux}) = 6{,}5\,\%$) où le risque net augmente.
  `Décision :` 
- **`V4-021` (`CONFIRME`, grav. B, `P4-013`) `[JSON]`** — *Problème :* le plancher de 68,0 % ($60\,\% + 8\,\%$) est répété cinq fois dans la § 16.1. *Retouche proposée :* alléger la répétition dans l’encadré *Nuance* l. 61 (patch en `corrections.json`).
  `Décision :` 
- **`V4-023` (`CONFIRME`, grav. B, `P4-012`, `T1-011`)** — *Problème :* la § 16.4 et `partie-4.md` l. 9 énoncent sans source ni statut une dynamique institutionnelle (organisations continuant à récompenser le volume), alors que la Conclusion dit que l’érosion des contrôles repose sur peu de mesures. *Retouche proposée :* marquer explicitement 16.4 comme *hypothèse de travail* (et nuancer `partie-4.md` l. 9 en « risquent de continuer »), ou appuyer sur une source documentée.
  `Décision :` 
- **`V4-025` (`CONFIRME`, grav. C, `P4-014`)** — *Problème :* la transition finale du ch. 16 (l. 110–112) répète presque mot pour mot `partie-4.md` l. 11 et est placée *après* le bloc `.question` (à l’inverse des ch. 14 et 15). *Retouche proposée :* replacer la transition avant `.question` et alléger l’une des deux occurrences.
  `Décision :` 

### `monographie/parties/partie-5.md`
- **`V5-018` (`PLAUSIBLE`, grav. C, `P5-031`)** — *Problème :* « ce que la @sec:partie-2 a montré impossible » omet que c’est sous hypothèses (et calque *shown impossible*). *Retouche proposée :* « ce que la @sec:partie-2 a montré être hors de portée sous ses hypothèses ».
  `Décision :` 
- **`V5-017` (`CONFIRME`, grav. B, `P5-019`, `T5-004`) `[JSON]`** — *Problème :* deux longs paragraphes résument en détail les ch. 17 et 18 juste avant leurs introductions (et contiennent « seul levier » signalé par `V5-002`). *Retouche proposée :* condenser chaque paragraphe à 3 lignes (patch exact en `corrections.json`, qui supprime du même coup « seul levier »).
  `Décision :` 

### `monographie/chapitres/17-decisions-sans-appel.md`
- **`VX-010` (`PLAUSIBLE`, grav. B, `P5-003`)** — *Problème :* `partie-5.md`, ch. 17 et ch. 18 invoquent P3(a) sans rappeler ses hypothèses (M3, omissions structurelles). *Retouche proposée :* ajouter « sous les hypothèses du modèle M3 » à la première occurrence au ch. 17 (l. 3).
  `Décision :` 
- **`VX-002` (`CONFIRME`, grav. B, `C-006`)** — *Problème :* $z$ désigne une variable physique aux ch. 5 et 7 ($Y = g(x,z)$) puis une probabilité dans $[0,1]$ au ch. 17, en A.4.2 et en annexe C ($p_w = 1-(1-p)(1-z)$), sans mention dans la Table C. *Retouche proposée :* soit renommer la probabilité en $p_z$ (ch. 17, A.4.2, D.3, scripts de figures), soit conserver $z$ et expliciter les deux usages dès le ch. 17 et en annexe C (`registre_termes.md`).
  `Décision :` 
- **`V5-004` (`PLAUSIBLE`, grav. C, `P5-006`)** — *Problème :* aucun repère pratique additionnel n’aide à fixer $b$ (hormis $p^\ast - p$ et $L/\Delta U$). *Retouche proposée :* ajouter une phrase de méthode (ex. fixer $b$ *avant* de regarder si $p + b$ franchit $p^\ast$).
  `Décision :` 
- **`V5-005` (`CONFIRME`, grav. B, `P5-007`) `[JSON]`** — *Problème :* quand $L/\Delta U$ est très élevé ($p^\ast = 0{,}0100\,\%$), toute marge $b$ usuelle transforme $p + b < p^\ast$ en interdiction systématique. *Retouche proposée :* ajouter cette précision en l. 85 (patch en `corrections.json`).
  `Décision :` 
- **`V5-009` (`PLAUSIBLE`, grav. C, `P5-011`)** — *Problème :* les limites des quatre questions ne mentionnent pas qu’une réponse fluide ne prouve pas que le chiffre soit juste. *Retouche proposée :* ajouter deux phrases en fin de § 17.4 (l. 160).
  `Décision :` 

### `monographie/chapitres/18-remede-trois-niveaux.md`
- **`V5-023` (`CONFIRME`, grav. B, `P5-014`)** — *Problème :* contrairement aux niveaux 1 et 3, le niveau 2 (18.2.1–18.2.4) omet d’afficher son appui (*proposition*) et les limites de « qui » (18.2.2) et « quoi » (18.2.3). *Retouche proposée :* ajouter une phrase d’appui en 18.2 (l. 41) et deux lignes de limites en fin de 18.2.2 et 18.2.3.
  `Décision :` 
- **`V5-029` (`PLAUSIBLE`, grav. C, `P5-029`)** — *Problème :* l. 7 qualifie l’humilité épistémique (une attitude) de « première source de comparateurs », alors que la source est le savoir du praticien. *Retouche proposée :* « ouvre l’accès à la première source de comparateurs » (ou laisser tel quel, la l. 9 précisant aussitôt).
  `Décision :` 
- **`V5-020` (`CONFIRME`, grav. C, `C-040`) `[JSON]`** — *Problème :* le *pré-mortem* (l. 21) est attribuable à Gary Klein (2007) mais présenté sans référence. *Retouche proposée :* insérer la balise `[@A-VERIFIER: Klein 2007…]` (patch en `corrections.json`, et ajouter l’entrée vérifiée dans `commun/biblio.bib`).
  `Décision :` 
- **`V5-024` (`CONFIRME`, grav. B, `P5-015`)** — *Problème :* le plafonnement de la production par la capacité de contrôle est répété presque à l’identique en 18.2.4 (l. 70), 18.3.1 (l. 90) et 18.4 (l. 144). *Retouche proposée :* alléger 18.3.1 par un renvoi net à 18.2.4 en y gardant uniquement le volet budgétaire et organisationnel.
  `Décision :` 
- **`V5-021` (`PLAUSIBLE`, grav. C, `C-041`)** — *Problème :* ranger la 3e pratique du niveau 3 (historique confronté aux issues) parmi les « propositions » (l. 86) la sous-estime face au ch. 17 qui la dit éprouvée. *Retouche proposée :* « les deux premières sont des propositions… la troisième étend à la vie d’une organisation une pratique déjà éprouvée en prévision ».
  `Décision :` 
- **`V5-026` (`PLAUSIBLE`, grav. B, `P5-017`)** — *Problème :* « les trois niveaux ne tiennent qu’ensemble » (l. 146) paraît trop absolu : la Fig. 18.1 montre qu’aucun niveau ne couvre *toutes* les conditions, non qu’un contrôle mécanique isolé soit sans effet. *Retouche proposée :* « Aucun niveau ne couvre à lui seul les cinq conditions ; c’est ensemble qu’ils se soutiennent ».
  `Décision :` 

### `monographie/chapitres/99-conclusion.md`
- **`V5-043` (`PLAUSIBLE`, grav. C, `T1-028`)** — *Problème :* la liste des constats empiriques (l. 39) mêle observations et techniques de mesure (TIP, test par mutation) tout en omettant *Challenger*. *Retouche proposée :* citer *Challenger* parmi les constats et séparer en fin de phrase « auxquels s’ajoutent deux dispositifs documentés d’injection de défauts ».
  `Décision :` 
- **`V5-037` (`CONFIRME`, grav. B, `P5-023`) `[JSON]`** — *Problème :* la liste des observations qui affaibliraient l’argument (l. 99) couvre ch. 6, 9, 12, 15 et 18 mais omet le ch. 17. *Retouche proposée :* ajouter une clause sur les décisions uniques (marge d’humilité et verrous dégénérant en formalité) (patch en `corrections.json`).
  `Décision :` 
- **`V5-041` (`PLAUSIBLE`, grav. C, `P5-027`)** — *Problème :* « erreurs constantes » et « erreurs hasardées » reviennent en l. 99 sans rappel ni entrée au glossaire. *Retouche proposée :* glose brève entre parenthèses en l. 99 (ou entrée au registre).
  `Décision :` 
- **`V5-038` (`PLAUSIBLE`, grav. C, `P5-024`)** — *Problème :* la § « Ce qui affaiblirait l’argument » gagnerait à préciser explicitement qu’aucune de ces mesures empiriques n’a encore été conduite sur le livre lui-même. *Retouche proposée :* ajouter « et aucune n’a encore été conduite sur cet ouvrage » en l. 101.
  `Décision :` 
- **`V5-036` (`CONFIRME`, grav. B, `P5-022`) `[JSON]`** — *Problème :* la § « Une provenance déclarée » (l. 109) omet la *complaisance* (ch. 15) parmi les limites des modèles objecteurs et ne mentionne pas d’éventuels relecteurs humains externes. *Retouche proposée :* ajouter la complaisance en `corrections.json` (`[JSON]`), et indiquer le cas échéant la relecture humaine.
  `Décision :` 
- **`V5-046` (`PLAUSIBLE`, grav. C, `piste-rep-02`)** — *Problème :* la l. 123 sur le monde comme comparateur sans cadre propre reprend presque mot pour mot 13.2.4 (suite à `SYN-E1`). *Retouche proposée :* conserver pour l’autonomie de la conclusion ou condenser en un renvoi d’une ligne à `@sec:ch13-le-monde`.
  `Décision :` 
- **`V5-039` (`CONFIRME`, grav. B, `P5-025`, `T1-004`) `[JSON]`** — *Problème :* la phrase finale de la conclusion (l. 142) paraît exclure absolument toute détection interne (malgré la saillance l. 61) et présenter les cinq conditions comme suffisantes. *Retouche proposée :* ajouter « en principe » et « au minimum » (patch en `corrections.json`).
  `Décision :` 

### `monographie/annexes/A-outils.md` et `monographie/annexes/C-notation.md`
- **`VX-018` (`CONFIRME`, grav. B, `PA-007`, `T2-005`)** — *Problème :* plusieurs lettres ($E, A, D, B, H, c, f, m, \alpha$) changent de sens d’un chapitre à l’autre et au sein même de l’annexe A (l. 31). *Retouche proposée :* ajouter une note de portée locale en tête de l’annexe A et en annexe C (ou renommer les collisions les plus gênantes comme $c(a,\omega)$ en $u(a,\omega)$ dans A.4).
  `Décision :` 
- **`VX-021` (`CONFIRME`, grav. C, `PA-010`, `T2-017`)** — *Problème :* la Table C (générée depuis `registre_termes.md`) ne comporte que 15 lignes et omet des symboles constants dans les calculs ($\Lambda$, $S(p)$, $\mathrm{VPP}$, $R$, $P(\text{faux})$, $C/\bar C$, $D$, $U_{\text{sûr}}$) ainsi que les premiers emplois de $p$ (ch. 1, 3) et $z$ (ch. 5), alors que A.1 dit que « tous les symboles » y figurent. *Retouche proposée :* compléter `registre_termes.md` (notamment $C/\bar C$, $\mathrm{VPP}$, $R$, $P(\text{faux})$) et écrire « les principaux symboles » en A.1.
  `Décision :` 

---

## 5. Corrections directes (groupe 1)

Le groupe 1 rassemble **124 grappes actives** (112 `CONFIRME` et 12 `PLAUSIBLE`). Les retouches exactes de **107 grappes `CONFIRME` de G1** (135 opérations `avant`/`apres`) — accompagnées de **23 grappes `CONFIRME` de G2** (25 opérations) — figurent dans **`relecture/sorties/synthese/corrections.json`**, soit **160 retouches prêtes à appliquer**, rangées dans l’ordre de `monographie/livre.yaml` et vérifiées à **occurrence unique (`1`)** et sans chevauchement dans chaque fichier cible.

**Contrôle des anomalies signalées lors du pré-contrôle :**
- `V1-004` (`03-mondes-possibles.md`), `VX-006` (`09-severite-echappement.md`) et `VX-019` (`annexes/A-outils.md`) contenaient chacun une liste multi-fichiers dépourvue de clé `"fichier"` sur les items secondaires : corrigé d’après la source vers `04-decider.md` (l. 138), `16-angles-morts-collectifs.md` (l. 5), `99-conclusion.md` (l. 71) et `annexes/D-parametres.md` (l. 60), tous vérifiés `count == 1`.
- Le chemin réel de l’annexe A dans le dépôt est **`monographie/annexes/A-outils.md`** (il n’existe pas de fichier `A-outils-reference.md`) : toutes les corrections correspondantes (`VX-012`, `VX-013`, `VX-019`, `VX-020`, `VX-023`, `VX-025`, `VX-027`, `VX-028`, `VX-029`) ciblent `monographie/annexes/A-outils.md` et ont été vérifiées `count == 1`.
- `V2-041` : le report sur `monographie/parties/partie-2.md` (l. 13, « risque réel » $\to$ « risque résiduel »), indiqué dans la justification de `V2.json`, a été ajouté dans `corrections.json`. En revanche, le report de `V5-002` sur `monographie/parties/partie-5.md` (l. 5) n’a pas été dupliqué dans `corrections.json` car `V5-017` (G2) réécrit déjà ce paragraphe entier (à reporter manuellement sur `partie-5.md` l. 5 si `V5-017` n’était pas retenu).
- **5 grappes `CONFIRME` de G1 n’ont pas de patch JSON dans `corrections.json`** :
  - **2 portent sur des tableaux générés** (à corriger dans le script puis régénérer par `make figures`) : `V1-012` (`monographie/scripts/fig_seu.py` l. 43 $\to$ `tableaux/ch04-seuil.md`, retirer « (sans facteur omis) ») et `V3-028` (`monographie/commun/parametres.py` l. 128 $\to$ `tableaux/ch12-plausibilite.md`, remplacer `'une autre date'` par `'5 mars'`).
  - **3 portent sur des ajouts ou harmonisations tabulaires en annexe D** (`monographie/annexes/D-parametres.md`) laissés à rédiger au moment de l’application : `VX-017` (rappeler sous la Table D.3 le sens de $p$, $L/\Delta U$, « fissure non repérée » et les unités de $b$ et $z$), `VX-030` (définir « Part indépendante » = $q = 0\,\%$ sous la Table D.4), `VX-031` (note ou harmonisation des décimales en Table D.3).
- Les **12 grappes `PLAUSIBLE` de G1** (`V0-026`, `V0-028`, `V1-024`, `V1-025`, `V1-028`, `V3-014`, `V3-023`, `V4-010`, `V5-010`, `V5-030`, `VX-009`, `VX-024`) conservent leurs propositions optionnelles dans les fichiers `V*.json` correspondants (11 d’entre elles disposent d’un patch `avant`/`apres` prêt à l’emploi, seule `VX-024` étant sans patch).

### Tableau récapitulatif des corrections directes (`CONFIRME` G1) par fichier

| Fichier cible (ordre du livre) | Grappes `CONFIRME` G1 | Nb retouches JSON | Objet principal des retouches |
| :--- | :--- | --: | :--- |
| `chapitres/00-avant-propos.md` | `V0-015`, `V0-019` | 2 | « limiter les prérequis » ; 8 parcours / 5 profils |
| `chapitres/00-cartographier.md` | `V0-002` (+`VX-035`), `V0-004`, `V0-005`, `V0-007`, `V0-013`, `V0-016`, `V0-017`, `V0-018`, `V0-020`, `V0-021` | 14 | Arrière-plan tacite au ch. 1 ; composants en chaîne ; réserve P5 ; R6 ; erreur d’unités ; « vis-à-vis » ; `$p^*$` absent de (0.2) |
| `chapitres/01-outils-logique-probabilite.md` | `V1-008`, `V1-014`, `V1-015`, `V1-017` | 5 | Déduction à prémisse fausse ; convention de travail ; relevés de fabrication ; diviser par 3,4 |
| `chapitres/02-cadre.md` | `V1-009`, `V1-018` | 2 | Mesures *effectuées* sur cohortes ; Table 2.1 cumulative (« à l’air libre ») |
| `chapitres/03-mondes-possibles.md` | `V1-004`, `V1-019`, `V1-023` | 3 | PC « Une issue isolée… » ; citation `[@gneiting2007]` ; `[-@russell2021]` |
| `chapitres/04-decider.md` | (`V1-004`), `V1-010`, `V1-020` | 3 | PC ch. 4 ; incise « remporte la course » ; « utilité espérée » au lieu de « gains » |
| `tableaux/ch04-seuil.md` *(script)* | `V1-012` | 0 *(script)* | Retirer « (sans facteur omis) » dans `scripts/fig_seu.py` l. 43 |
| `parties/partie-2.md` | (`V2-041`) | 1 | « risque réel » $\to$ « risque résiduel » (l. 13) |
| `chapitres/05-trois-incertitudes.md` | `V2-006`, `V2-007` | 2 | Prédiction conforme sur échangeabilité (hors $\Theta$) ; « Trois conséquences » |
| `chapitres/06-detecter-une-erreur.md` | `V2-013`, `V2-015`, `V2-017` | 3 | Trace d’un facteur omis variable ; concordance « prend acte… et a » ; « double rupture » |
| `chapitres/07-cadre-cause-commune.md` | `V2-025`, `V2-026` | 2 | Accord « à quelques pour cent près » ; notation $z$ minuscule uniforme |
| `chapitres/08-independance-chaines.md` | `V2-031`, `V2-032`, `V2-035` | 3 | Point clé 3 aligné sur $B_1 \cap (B_2 \cup B_{\text{cmp}})$ ; suppression incise vitesse ; coût « globalement » croissant |
| `chapitres/09-severite-echappement.md` | `V2-039` (**A**), `V2-041`, `V2-046`, `V2-047`, `V2-049`, `VX-006` | 9 | **« contrôle réussi »** au lieu de « contrôle franchi » ; « risque résiduel » ; étude au singulier ; « moins d’erreurs » |
| `parties/partie-3.md` | `V3-001` (**A**), `V3-002` | 2 | **Supprimer « d’un type nouveau »** ; « contrat écrit lorsqu’il est effectivement appliqué » |
| `chapitres/10-couches-basses.md` | `V3-005`, `V3-007`, `V3-011` | 3 | Déterminisme à architecture/ordonnancement donnés ; alarme *automatique* ; « demande » avant ch. 11 |
| `chapitres/11-regle-tiree-des-donnees.md` | `V3-012`, `V3-017` | 3 | Renvois ch. 1 et 2 (arrière-plan tacite, induction) ; « cette affaire, l’année suivante » |
| `chapitres/12-autre-regime.md` | `V3-019`, `V3-021`, `V3-022`, `V3-025`, `V3-026`, `V3-027`, `V3-030` (**A**) | 8 | **Sévérité 99,9 % / fausses alertes 99,9 %** ; borne de Kalai-Vempala conditionnelle ; Dennett ; BCG abrégé ; parenthèse Mercure |
| `tableaux/ch12-plausibilite.md` *(script)* | `V3-028` | 0 *(script)* | `'une autre date'` $\to$ `'5 mars'` dans `commun/parametres.py` l. 128 |
| `chapitres/13-synthese-deux-axes.md` | (`V3-001`), `V3-032`, `V3-034`, `V3-036`, `V3-037`, `V3-040`, `V3-042`, `V3-045` | 11 | Tableau 13.2 et PC3 nuancés ; « poulet » de Russell ; environnement isolé ; `[@farquhar2024]` ; échappement 1 |
| `parties/partie-4.md` | `V4-014` | 1 | « peut tromper jusqu’aux experts » |
| `chapitres/14-chaines-qui-agissent.md` | `V4-001`, `V4-003`, `V4-004`, `V4-005`, `V4-006`, `V4-007`, `V4-008`, `V4-009` | 10 | Renvoi `@sec:ch10-boite-outils` (10.1) ; pyramide classique ; « suite d’actions » ; hypothèse indépendance contrôleur ; part relative de $q$ |
| `chapitres/15-erosion-verifications.md` | `V4-012`, `V4-014`, `V4-015`, `V4-016`, `V4-017` | 7 | Transition Bainbridge + chapeau ; METR « illustre » ; définitions locales $A$, $E$ |
| `chapitres/16-angles-morts-collectifs.md` | `V4-018`, `V4-020`, `V4-022`, `V4-024`, (`VX-006`) | 6 | Intertitre « part incompressible $c$ du plancher » ; coupe définition blanchiment ; Shumailov « risquent » ; « moins d’erreurs » |
| `chapitres/17-decisions-sans-appel.md` | `V5-002`, `V5-003`, `V5-007`, `V5-008`, `V5-012`, `V5-014`, `V5-015` | 9 | « côté estimation » ; facteur constant (P1) ; « seul moyen statistique » ; Knight Capital dissocié des LLM ; 4 quadrants / 5 libellés |
| `chapitres/18-remede-trois-niveaux.md` | `V5-019`, `V5-025`, `V5-027`, `V5-028`, `V5-032` | 5 | Renvoi `@prop:cause-commune` au ch. 7 ; glose $\bar C$ ; suppression liste répétée des 4 et 5 questions |
| `chapitres/99-conclusion.md` | `V5-033`, `V5-034` (+`V0-031`, `VX-036`), `V5-035`, `V5-040`, `V5-042`, (`VX-006`) | 7 | Coupe 15 lignes Genèse + « on la rappelle » ; alignement Tableau 1 / l. 81 ; P4 dans noyau ; « moins d’erreurs » |
| `annexes/A-outils.md` | `VX-012`, `VX-013`, `VX-019`, `VX-020`, `VX-023`, `VX-025`, `VX-027`, `VX-028`, `VX-029` | 9 | Régime 4 M2 ; $f_1$ déterministe M3 ; $m=p$ ; conditionnel/joint $R$ ; $\mathrm{UES}$ ; Spence/Akerlof ; ordre M2, M3, M1 |
| `annexes/D-parametres.md` | `VX-014`, `VX-016`, `VX-017`, (`VX-019`), `VX-026`, `VX-030`, `VX-031` | 4 *(+3 à rédiger)* | Supprimer « source unique » ; D.3 ($z=0$ dans le cadre) ; $m=p=6\,\%$ ; « 5 mars » (+ notes D.3/D.4) |
| `commun/registre_termes.md` | `VX-022` | 1 | « ensemble des alternatives admises » |
| **Total `CONFIRME` G1** | **112 grappes** *(107 en JSON + 2 scripts + 3 ann. D)* | **135** *(+ 25 G2 = 160)* | |

---

## 6. Redites et lecture linéaire — Plan d’allègement cohérent

L’analyse croisée des grappes de redite, du bilan de `T5`, du journal de `C` et des comptages mécaniques de `relecture/pistes/repetitions.md` montre que la gêne ressentie en lecture linéaire ne vient pas de la spirale pédagogique elle-même (que `C` et `T5` apprécient lorsque le rappel sert un nouveau point, comme M. X/M. Y du ch. 4 au ch. 17), mais de **quatre foyers de duplication littérale**. Voici le plan d’allègement recommandé, qui préserve l’autonomie minimale des chapitres pour les parcours sélectifs :

### A. Études de cas et exemples récurrents : où garder le récit complet, où réduire à un rappel

| Cas / Exemple | Garder en entier | Réduire à un rappel bref (1–3 lignes + renvoi) | Grappes associées |
| :--- | :--- | :--- | :--- |
| **METR (Becker et al. 2025)** | **§ 15.2** (où il fonde la perte de friction et l’inversion ressenti/mesure) | **§ 0.1** : vignette d’accroche de 4 lignes posant l’énigme (+19 % mesuré vs −20 % ressenti), sans dupliquer les 38 séquences communes avec 15.2 | `VX-005` (+`V0-011`, `V4-027`) |
| **Mata v. Avianca (2023)** | **§ 11.3** (avec le rapprochement détaillé avec `SM_FORCES`) | **§ 0.1** : vignette d’ouverture de 4 lignes (jurisprudences inventées, pas de ligne fautive à pointer) | `VX-005` (+`V3-016`) |
| **Mars Climate Orbiter (1999)** | **§ 8.6** (blanchiment `SM_FORCES` / unités) et bloc `.cas` du **§ 10.5** (adresse et organisation) | **§ 0.1** (vignette brève) ; **§ 10.5 texte courant** (1 phrase renvoyant au ch. 8, `V3-008`) ; **§ 12.1 Nuance** et **§ 14.3** (rappel d’une ligne) | `VX-005`, `V3-008`, `V2-038` |
| **Challenger (1986)** | **§ 6.3** (étude de cas complète sur les 5 conditions) | **§ 5.5 Nuance** : garder uniquement le garde-fou conceptuel (3 lignes : cas mixte combinant mise en forme des données et objection écartée, voir § 6.3) sans redéployer les 7/16 vols | `VX-005`, `V2-012` |
| **BCG (Dell’Acqua et al. 2023)** | **§ 11.2** (protocole et gains) + **§ 12.3** (résultat hors frontière −19 pts) | **§ 12.3** : supprimer la répétition du protocole (patch `V3-022`) | `V3-022` |
| **Ébullition de l’eau** | **§ 2.2** (Table 2.1 progressive) | **§ 1.2** : ne garder que sel et altitude (patch `V1-005`) ; **§ 5.4** : rappel d’une demi-phrase | `V1-005`, `VX-004` |
| **Course à la voile (M. X / M. Y)** | **§ 2.1** (représentation), **§ 3.3** (score log), **§ 4.2** (seuil $p^\ast$), **§ 17.1** (M2 avec $z, b$) | **§ 3.1** (condenser l’écho de 2.1, patch `V1-022`) ; **§ 4.3** (condenser le triple calcul, patch `V1-006`) ; **§ 2.1** (éviter le doublet navigateur/téléphone satellite) | `V1-006`, `V1-022`, `VX-004` |
| **Ferrure métallique (1,8)** | **§ 5.4** (incertitudes) et **§ 8.2** (Table 8.1) | **§ 0.3**, **§ 6.2/6.5**, **§ 7.2/7.3/7.5**, **§ 13.1**, **Conclusion** : mentions d’une phrase sans réexposer le scénario à neuf | `VX-004`, `V5-044` |

### B. Répétitions structurelles et doublons entre sections voisines
1. **Pages d’ouverture de partie (`partie-1.md` à `partie-5.md`) et § 0.7 (`V0-008`, `VX-034`, `V4-026`, `V5-017`) :** ramener § 0.7 à un tableau ou cinq paragraphes courts, condenser chaque page de partie à ~150–250 mots (sur le modèle de `V5-017`), et supprimer les derniers paragraphes de page de partie qui annoncent la partie suivante.
2. **Transitions et rappels internes de chapitres :** supprimer la réénumération *in extenso* des cinq conditions en tête des ch. 8 et 9 (`V2-052`), le motif répété de l’apprentissage (« personne ne savait écrire la règle ») en fin de ch. 10 et en chapeau du ch. 11 (`V3-013`), la duplication `8.4` $\to$ `14.1` et `8.2` $\to$ `14.2.3` (`V4-002`), la réexposition de la définition du blanchiment en `16.3` (`V4-024`), la répétition du plancher de 68,0 % en `16.1` (`V4-021`), le doublon `18.2.4` / `18.3.1` sur le plafonnement (`V5-024`), et les listes répétées des 4 et 5 questions au ch. 18 (`V5-032`, `V5-027`).
3. **Doublons texte / encadré immédiat et Conclusion :** alléger l’encadré `.nuance` du § 10.5 (`V3-010`) et du § 13.1 (`V3-035`), réduire la « Genèse » en Conclusion l. 107 à 3 lignes avec renvoi à l’avant-propos (`V5-034`), et resserrer les *Points clés* de la Conclusion (`V5-044`).

---

## 7. Signaux sur les décisions antérieures

Les lecteurs neufs et vérificateurs montrent que **21 points déjà tranchés** dans `DECISIONS_SYNTHESE.md`, `ARBITRAGES_RESTANTS.md` ou `TODO_ETAT_ACTUEL.md` soit **ne suffisent pas** à empêcher un lecteur neuf de buter, soit ont été **incomplètement appliqués**, soit ont **introduit un défaut local** :

### A. Décisions insuffisantes sur le fond (lecteurs neufs qui butent encore)
- **`ARBITRAGES P2.2.2` (`DEC-S6`, roulette russe, `V5-001` + `V1-002`, grav. A) :** l’alignement sur « croit l’arme déchargée / estime à $0{,}001\,\%$ le risque qu’une balle ait été oubliée » a rendu plus visible la contradiction entre erreur estimée dans $p$ et facteur omis indépendant $z = 1/6$.
- **`DECISIONS_SYNTHESE R4` (sévérité $\Pr(\bar A \mid E)$, `V2-040`, grav. B) :** mesurer la sévérité par $\Pr(\bar A \mid E)$ la confond numériquement avec la sensibilité $s$.
- **`DECISIONS_SYNTHESE S4` (statut de P3(b), `V2-022`, grav. B) :** deux lecteurs contestent toujours le statut *résultat sous hypothèses* faute de dérivation dans M3.
- **`ARBITRAGES P1.2` (`SYN-D2`, *représentation* vs *cadre*, `V1-001`, grav. B) :** l’ajout « comprend ce cadre » en 2.3 reste contredit par « à l’intérieur du cadre » deux lignes plus bas et aux ch. 3–4.
- **`ARBITRAGES P1.3` (`REV-4A.3`, « Cause dans le cadre » au ch. 13, `V3-033`, grav. B) :** la phrase ajoutée en 13.1 n’empêche pas `C` et `P3` de relever le glissement face à la Déf. 2 et l’absence de l’aveu d’ambiguïté de la Conclusion.
- **`ARBITRAGES P1.5` (`SYN-D4`, *Challenger* dans les 5 conditions, `V2-016`, grav. B) :** `C` et `P2` trouvent toujours flottante la répartition entre *existence*, *différence* et *comparabilité* (et `V2-017` critique « double rupture disjointe »).
- **`ARBITRAGES P1.11.3` (`SYN-E3`, variante « texte déjà rédigé » au § 15.4, `V4-011`, grav. B) :** l’incise « à défaut et au prix d’une neutralité moindre » laisse subsister une tension avec l’énoncé strict des résumés.
- **`ARBITRAGES P2.3.1` (`SYN-C1`, Déf. 1 au ch. 2, `V1-013`, grav. C) :** `C` voit encore la 2e phrase de la Déf. 1 (« Le monde répond à l’action… ») comme une thèse hors définition.
- **`DECISIONS_SYNTHESE N3` (ordre M3 $\to$ M1 $\to$ M2, `V0-012` + `V5-016`, grav. C) :** 4 lecteurs (`C`, `P0`, `T2`, `T5`) butent encore sur la numérotation non chronologique.
- **`DECISIONS_SYNTHESE V4` (« niveau situé dessous », `V0-022`, grav. C) :** obscur pour `P0` en 0.6.
- **`DECISIONS_SYNTHESE V16` (« contrôles en chaîne », `VX-007`, `V0-004`, grav. B/C) :** contradiction avec le ch. 8 entre *chaîne de composants* et *contrôles en chaîne* (`partie-4.md`, `partie-5.md`, `99-conclusion.md`, `00-cartographier.md`).
- **`DECISIONS_SYNTHESE V2` (« vérifications humaines », `VX-003`, grav. C) :** recouvrement léger avec le terme *vérification* du ch. 13.

### B. Défauts introduits ou reports oubliés lors des applications antérieures
- **`ARBITRAGES P1.10.4` (`V2-039`, grav. A) :** l’ajout « *contrôle franchi* » pour $C$ au ch. 9 l. 92 dit le contraire de la définition de $C$ (contresens critique).
- **`ARBITRAGES P1.8` (`V2-006`, `V2-007`, grav. B/C) :** la phrase ajoutée en 5.2 range à tort la prédiction conforme sur $\Theta$ et laisse « Deux propriétés » annoncer trois points.
- **`DECISIONS_SYNTHESE R11` (`V2-015`, grav. C) :** « quelqu’un prend acte… et ait l’autorité » (faute de mode en 6.2).
- **`ARBITRAGES P1.9` (`V2-041`, `V2-042`, grav. B/C) :** « risque réel » subsiste en 9.3, PC 4 et `partie-2.md:13`, et l’incise ajoutée en 9.5 promet une comparaison $R$ vs $p^\ast$ absente du ch. 17.
- **`ARBITRAGES P1.1` (`V4-019`, `V4-020`, `VX-001`, grav. B) :** l’explication de la baisse du risque et du plancher $c + (1-c)m$ en 16.1 n’a pas été reportée sur le titre 16.1, l’intertitre l. 51, le PC 1, `partie-4.md` ni 0.5.4.
- **`ARBITRAGES P1.4` (`SYN-D3`, `V4-024`, grav. C) :** l’harmonisation de *blanchiment* a créé une répétition mot pour mot entre 14.3 et 16.3.
- **`ARBITRAGES P1.10.2` (`REV-4B.2`, `V3-028`, `VX-026`, grav. C) :** « 5 mars » appliqué au ch. 12 n’a pas été reporté dans `parametres.py`, `ch12-plausibilite.md` ni `D-parametres.md` (« 6e date »).
- **`DECISIONS_SYNTHESE R6` (`V0-017`, grav. C) :** la réserve « ce qu’il établit » n’a pas été reportée en 0.4.
- **`ARBITRAGES P2.3.6` (`SYN-C7`, `V5-043`, grav. C) & `P2.4` (`REV-3.1`, `VX-005`) :** liste des constats en Conclusion à affiner (`Challenger` omis, dispositifs mêlés aux constats), et plan d’allègement des 4 études de cas encore non appliqué.

---

## 8. Ce qui a été écarté

Au total, **29 grappes consolidées** ont été écartées du plan d’action : **20 `REJETE`**, **5 `DEJA_TRANCHE`** et **4 `DEJA_RELEVE`** *(après fusion de `V5-016` dans `V0-012` et de `V0-011` dans `VX-005`, et traitement de `V0-009` conjointement avec `VX-001`)*.

### Motifs des `REJETE` (20 grappes)
- **Faux positifs des pistes mécaniques (`V1-031`, `V1-032`, `V2-053`, `V3-043`, `V3-044`, `V5-045`, `V5-047`) :** annonces explicites en italique, verbe courant (*adresser*), terme distinct (*vérification en amont*), ou reprises structurelles voulues (4 questions, spirale quantitative ch. 4 $\to$ ch. 17, alignement `SYN-E1`).
- **Lecture sur extraits partiels ou erreur de conversion (`V1-030`, `V2-020`, `V3-018`, `V5-031`, `VX-033`) :** `T1` manquait les développements du corps (ch. 4 $\to$ 17, 6 $\to$ 13, 11.2, 18.1.3) ou subissait un artefact de son dossier d’extraits (`Points clés` doublé).
- **Inattention de lecture ou faux écart (`V0-030`, `V5-013`, `V5-022`, `VX-015`) :** précision déjà présente à la phrase suivante (« Pour lui… »), ordre conforme au ch. 7, glose déjà présente (« prêteur unique » en ch. 18), ou absence effective de figure générée depuis `parametres.py` au ch. 0.
- **Conventions éditoriales assumées du livre (`V0-029`, `V0-032`, `V0-033`, `V2-045`) :** autocitation prévue en avant-propos/ch. 0 (`00_global.md` § 8), amorces intentionnelles du ch. 0, et termes médicaux glosés du Tableau 9.1.

### Motifs des `DEJA_TRANCHE` (5 grappes)
- **`V1-029`** (*Cromwell / « logiquement impossible »*, `S14`), **`V2-009`** (*2008 / incertitude ontologique*, `S5`), **`V2-019`** (*différence / se tromper autrement*, `V20`), **`V2-051`** (*exact / précis*, `DEC-V1`), **`V5-006`** (*écart à Savage placé en Nuance au ch. 17*, `P1.7`).

### Motifs des `DEJA_RELEVE` (4 grappes)
- **`V0-009`** (*dix fois plus exact* en 0.5.4, `RAPPORT_AUDIT_CALQUES` — résolu de fait par le patch `VX-001`), **`V0-010`** (*jargon en 0.7*, `TODO P2.2 [SYN-S7]`), **`V1-016`** (*calibrer* au ch. 2, `RAPPORT_AUDIT_CALQUES` § 3.2/4), **`V2-037`** (*tire contre* au ch. 8, `RAPPORT_AUDIT_CALQUES` l. 201).

---

## 9. Bilan de la méthode

### Rendement et taux de confirmation par lecteur (sur les 260 grappes consolidées)

| Lecteur | Rôle | Constats émis | `CONFIRME` | `PLAUSIBLE` | `DEJA_*` | `REJETE` | Taux `CONFIRME` | Taux `CONFIRME + PLAUSIBLE` |
| :--- | :--- | --: | --: | --: | --: | --: | --: | --: |
| `C` | Lecteur cible (intégral) | 59 | 49 | 8 | 2 | 0 | **83,1 %** | **96,6 %** |
| `P0` | Avant-propos, ch. 0 | 23 | 16 | 3 | 2 | 2 | 69,6 % | 82,6 % |
| `P1` | Partie I (ch. 1–4) | 22 | 15 | 6 | 1 | 0 | 68,2 % | 95,5 % |
| `P2` | Partie II (ch. 5–9) | 37 | 28 | 7 | 1 | 1 | 75,7 % | 94,6 % |
| `P3` | Partie III (ch. 10–13) | 33 | 28 | 5 | 0 | 0 | 84,8 % | 100,0 % |
| `P4` | Partie IV (ch. 14–16) | 20 | 18 | 2 | 0 | 0 | 90,0 % | 100,0 % |
| `P5` | Partie V et Conclusion | 32 | 20 | 10 | 1 | 1 | 62,5 % | 93,8 % |
| `PA` | Annexes A et D | 20 | 18 | 1 | 0 | 1 | 90,0 % | 95,0 % |
| `T1` | Thème : charpente & statuts | 34 | 21 | 6 | 2 | 5 | 61,8 % | 79,4 % |
| `T2` | Thème : maths & calculs | 17 | 16 | 0 | 0 | 1 | **94,1 %** | 94,1 % |
| `T5` | Thème : redites & rythme | 31 | 28 | 3 | 0 | 0 | **90,3 %** | **100,0 %** |
| **Total** | **11 lecteurs** | **328** | — | — | — | — | — | — |

*(Note : la somme des colonnes de lecteurs dépasse le nombre de grappes parce qu’une même grappe regroupe souvent plusieurs constats ; une piste mécanique pure sans constat de lecteur, `V3-011`, porte les `CONFIRME` à 181.)*

### Convergence entre lecteurs et apport propre de chaque profil
- **Grappe trouvée par un seul lecteur vs plusieurs :** sur les **180 grappes `CONFIRME` issues de lecteurs** (hors `V3-011` piste pure), **127 (70,6 %)** ont été repérées par **1 seul lecteur** et **53 (29,4 %)** par **au moins 2 lecteurs** (41 par 2 lecteurs, 7 par 3, 4 par 4, et 1 — `VX-011` — par 6 lecteurs). Sur l’ensemble des 249 grappes consolidées contenant au moins un constat de lecteur, 194 (77,9 %) viennent d’un seul lecteur et 55 (22,1 %) convergent entre plusieurs.
- **Complémentarité des trois profils (sur les 180 grappes `CONFIRME` de lecteurs ; entre parenthèses, gravités A + B = 92) :**
  - **Apport propre des lecteurs par portion (`P0`–`P5`, `PA`) :** **91** grappes `CONFIRME` trouvées uniquement par eux (dont **43 A/B**, parmi lesquelles la faille de preuve `V2-021` [A] et la grande majorité des défauts factuels, d’exemples et de logique locale de section).
  - **Apport propre du lecteur cible (`C`) :** **19** grappes `CONFIRME` trouvées uniquement par lui (dont **3 A/B** : `V2-023` sur *dérive de distribution*, `V4-001` sur le renvoi faux à 10.2, `VX-002` sur la surcharge de $z$), plus un rôle décisif de **ciment transversal** (présent dans **30** des 53 grappes multi-lecteurs, dont `V5-001` [A], `V2-029` [A], `V2-039` [A], `V3-030` [A]).
  - **Apport propre des lecteurs thématiques (`T1`, `T2`, `T5`) :** **18** grappes `CONFIRME` trouvées uniquement par eux (dont **8 A/B** : `V4-020` sur l’intertitre du plancher de 68 %, `VX-034` sur les 5 pages de partie, `V2-002`, `V2-031`, `V2-052`, `V3-031`, `V4-024`, `V5-042`), et une forte convergence transversale avec `C` et `P*` (32 grappes multi-lecteurs impliquent au moins un `T*`).

### Angles morts probables de cette relecture (ce qu’aucun lecteur n’a pu voir)
1. **Les figures graphiques compilées (`figures/*.pdf`) :** tous les lecteurs (y compris `C`, `T2` et `PA`) n’ont lu que le Markdown et les légendes ; la lisibilité visuelle, les chevauchements d’étiquettes et l’adéquation exacte entre tracés visuels et tableaux (`fig_ch00_*`, `fig_ch06_*`, `fig_ch13_*`, `fig_ch18_*`, courbes et barres) n’ont pas été vérifiés par cette passe.
2. **Les sources primaires externes et l’article `[@fauriat2026frame]` :** comme le note `C` (§ 3–4 de son bilan), aucun lecteur n’avait accès au texte de `fauriat2026frame` ni aux sources primaires (hormis l’audit préalable `RAPPORT_VERIFICATION_BIBLIO.md`), laissant quelques points de détail à vérifier à la source (l’exemple « pays puis ville » de *logit lens* `V3-014`, la citation d’ingénierie pour V&V `V3-041`, Gary Klein 2007 `V5-020`).
3. **L’expérience du lecteur réel sur épreuve PDF/HTML et les 8 parcours sélectifs :** sauf `C`, aucun lecteur n’a testé les parcours partiels du Tableau 0.1 de bout en bout (par exemple le parcours « Décideur » ou « Ingénieur ») pour vérifier les dépendances de renvois internes sur l’épreuve finale.
4. **Le regard d’un praticien ou chercheur spécialiste sur deux points frontières :** l’absence du renforcement sur récompenses vérifiables (RLVR) en 11.4 (`V3-015`) et l’absence de discussion de l’hypothèse « fourre-tout » bayésienne (`V2-008`) ont été relevées par `C`, mais un spécialiste externe de l’alignement ou des statistiques décisionnelles pourrait encore relever d’autres angles morts techniques ou bibliographiques récents.
5. **Le rendu typographique et LaTeX final :** césures, sauts de page, veuves/orphelines, rendu des encadrés et tableaux larges (notamment le Tableau 1 de la Conclusion et les tableaux transposés) relèvent du contrôle sur PDF compilé, hors périmètre d’une relecture sur Markdown.
