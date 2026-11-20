# Audit des calques anglais — Monographie *Agir d’après une représentation du monde*

**État du dépôt vérifié :** branche `main` au commit `c8acb4f` (aucun fichier modifié ; audit strictement en lecture seule).  
**Périmètre audité et vérifié :** `monographie/livre.yaml`, 21 fichiers dans `monographie/chapitres/`, 5 fichiers dans `monographie/parties/`, 15 scripts dans `monographie/scripts/fig_*.py`, 13 tableaux dans `monographie/tableaux/*.md`, 4 annexes dans `monographie/annexes/*.md` (`A`–`D`) et `monographie/commun/registre_termes.md`.  
**Méthode :** 7 auditeurs parallèles (`front`, `part1`–`part5`, `figures`) croisés par 2 vérificateurs (`verifier-prose`, `verifier-fig`) contre `monographie/commun/registre_termes.md` et `authoring_conventions.md` (§ 8).

---

## 1. Synthèse transversale par ordre de priorité

### Priorité 1 — Faux-amis lexicaux et calques syntaxiques altérant le sens ou l’idiome
1. **Faux-amis récurrents dans la prose et les tableaux :**
   - **`tenir`** (*to hold*) au sens de « rester valable / s’appliquer / être vérifié » : omniprésent de l’avant-propos à la conclusion (`00-avant-propos.md:17`, `00-cartographier.md:158`, `01:3,24`, `08:82,192`, `10:46,48`, `12:76,77`, `15:83`, `17:155`, `18:35,136,150`, `99:61,129`).
   - **`attraper` / `rattraper`** (*to catch*) au sens d’« intercepter / déceler / détecter » : `partie-2.md:9`, `partie-4.md:9`, `07:115`, `09:74,160,188`, `12:138`, `13:116`, `16:41,43`, `99:14,28,95,148`, `fig_echappement.py:26`, `tableaux/ch09-echappement.md:9`, `tableaux/ch16-modele-partage.md:9`, `annexes/D-parametres.md:91`.
   - **`manquer`** (*to miss*) au sens de « laisser passer / omettre » : `04:121`, `14:58`, `18:126` (titre).
   - **`délivrer`** (*to deliver*) au sens de « produire / émettre / garantir » : `partie-1.md:5`, `01:3,7,128,173`, `06:133`, `09:15`, `15:103`.
   - **`dérivation`** (*derivation*) au sens de « démonstration / établissement » (en français : différentiation) : `01:105` (titre), `04:46` (titre), `04:52`.
   - **`passer`** un test / un contrôle (*to pass a test*) au sens de « réussir / satisfaire à » : `02:142`, `07:98`, `14:30`, `15:44,90`.
   - **Autres faux-amis ciblés :** `formalité` (*formality* = formalisme, `13:45`), `bruyant` (*noisy* = manifeste/détectable, `12:19`), `calculatoire` (*computational* = informatique/numérique, `17:136`), `former` (*make* = donner, `tableaux/ch09-taux-echappement.md:6`), `casser` (*break* = se rompre / mettre en défaut, `08:163`, `15:90`), `définitionnelle` (*definitional*, `06:57`, `99:146`).
2. **Calques prépositionnels et syntaxiques structurants :**
   - **`décider sur`** (*decide on*) : `04:52`, `17:15,23,57,66,76,90`, `fig_seu.py:79,97,98`, `tableaux/ch17-decisions.md:1,10`, `annexes/A-outils.md:81` — d’autant plus gênant que le titre même de l’ouvrage est *Agir **d’après** une représentation du monde*.
   - **`agir sur une affirmation`** (*act on a claim*) : `partie-5.md:7`, `18:3,148,180` — même contradiction avec « agir d’après ».
   - **`conditionner sur`** (*condition on*) : `02:89,121`, `05:18`, `07:71,74`, `99:19,61,95`, `annexes/A-outils.md:100`.
   - **`sous`** + hypothèse / prévision / condition / appariement / examen (*under*) : omniprésent (`00-avant-propos.md:9,17,50`, `00-cartographier.md:158`, `01:93,97,103,120,139,148,166`, `02:146`, `03:67,88`, `05:71,91`, `09:135,162`, `12:89`, `13:51,120`, `17:155`, `18:150`, `99:129`, `annexes/A-outils.md:136,140`, `annexes/B-glossaire.md:155`, `annexes/D-parametres.md:78`, `registre_termes.md:24`).
   - **`à travers`** (*across / through*) : `00-avant-propos.md:7,29`, `00-cartographier.md:222,234`, `10:58`, `11:31`, `17:121`.
   - **`oubli sur`** (*miss rate on*) : `fig_echappement.py:22`, `tableaux/ch09-echappement.md:5`, `tableaux/ch16-modele-partage.md:5`, `annexes/C-notation.md:19`, `annexes/D-parametres.md:87`, `registre_termes.md:100`.
   - **`par défaut`** hors paramétrage logiciel (*by default*) : `13:72,106,110`, `15:3`.
   - **`vos propres contrôles`** (*your own checks*) en récit à la 3e personne : `partie-3.md:11`, `13:58,63,72,106,108,164`.
   - **Propositions participiales réduites, ruptures de sujet et infinitifs sujets :** « *suppose les alertes suivies* » / « *barres supposent* » (`09:153`, `16:34`), « *Tirées au sort, leurs tâches…* » (`00-cart:14`), « *En supposant…, que prouve…* » (`06:129`), ruptures sous infinitif (`15:59`, `18:152`), infinitifs longs en sujet (`00-cart:63`, `annexes/A-outils.md:23`), « *vos tâches ont pris 19 % de temps de plus* » (`00-cart:14`, `15:35`).

### Priorité 2 — Titres, légendes et ponctuation de rythme anglais
1. **Moule titulaire anglais `X : Y` et empilements nominaux sans articles :**
   - Sous-titre du livre (`livre.yaml:5`), nombreux titres `#`, `##`, `###`, `titre="..."` des blocs `.formel`, `.outils`, `.exemple-quantitatif`, `.cas` et `.proposition` (notamment les titres `Modèle M1/M2/M3 : <liste nominale sans articles>`, `Niveau 1/2/3 — X : Y`, `Où : …`, `Qui : …`, `Quoi : …`, `Combien : …`, les antithèses `X, non Y`, et `17:5` *revisitée*).
2. **Ponctuation anglo-saxonne :**
   - Usage massif d’incises entre tirets cadratins (`— … —`) coupant sujet et verbe, et surtout de la séquence non idiomatique **`—,`** (tiret fermant suivi d’une virgule) dans la quasi-totalité des chapitres et dans `annexes/A-outils.md:100`.
   - Tirets cadratins à l’anglaise dans les titres (`00-cart:61`, `11:61`, `18:126`, `fig_ch00_serie_parallele.py:18,55`) et esperluette `&` dans `fig_ch00_carte_ouvrage.py:62`.

### Priorité 3 — Figures, tableaux, annexes et cohérence terminologique (§ 8)
1. **Textes intégrés aux figures et tableaux :**
   - Libellés télégraphiques omettant articles et prépositions (*error per step*, *alert on right answer*, *loss outside model*, *estimated p*, *crise 2008*, *couche dessous*, *Aléatoire / Épistémique* nus, *Indépendant et précis* nus).
   - Style équation dans des phrases ou annotations (`=`, `+`, `→`, `:`).
   - Légendes et figures partiellement désalignées (`06:53` vs `fig_ch06_cinq_conditions.py:41-42` ; `08:146` vs `14:62` ; `12:123` vs `fig_plausibilite.py:28` ; `D-parametres.md:119` vs `tableaux/ch12-plausibilite.md:5`).
   - Petites erreurs de traduction dans les figures/tableaux : « Alertes qui sont de vraies erreurs (VPP) » (`fig_echappement.py:25`), « Un modèle pour tous » (*One model for all*, `fig_echappement.py:69`), « capacité nommée » (*named capacity*, `fig_ch18_trois_niveaux.py:41`), « vidable à l’avance si spécifié » (`fig_ch13_deux_axes.py:34`), « engendrés mécaniquement » (`D-parametres.md:3`).
2. **Cohérence avec `authoring_conventions.md` § 8 et le registre :**
   - Anglicismes à gloser/italiquer à la première occurrence : *pipelines* (`00-cart:181`), *no free lunch* (`07:109`), *RLHF* dans le texte principal (`11:73`), *RAG* dans `fig_ch18_trois_niveaux.py:38` ; troncation de *frontière en dents de scie* en « frontière et longue traîne » dans `fig_ch00_carte_ouvrage.py:46`.
   - Éviter `calibrer` au ch. 2 (`02:129`) avant la définition de **calibration** au ch. 3.
   - Homogénéiser les couples déjà hésitants entre chapitres : *friction* vs *frottement* (ch. 15), *l’humain / un humain* vs *une personne* (ch. 15), métaphore *acheter / dépenser* (ch. 0, 11, 12, 14), *panneau* vs *volet/graphique* (ch. 9), *exact* pour qualifier un producteur (ch. 9, ch. 16 — choix délibéré au ch. 9 pour distinguer $P(E)$ de $f$, à confirmer).

---

## 2. Faux positifs écartés par les vérificateurs

Les occurrences suivantes, signalées lors du premier balayage, ont été jugées **acceptables ou délibérées** par `verifier-prose` et `verifier-fig` :
- **Prose :**
  - `00-avant-propos.md:21` (« encadrés dédiés ») et `00-cartographier.md:175` (« pesant des mondes possibles ») : acceptables (priorité très faible).
  - `00-cartographier.md:105` (« délibérément *dépensée* pour acheter… ») : métaphore mise en italique par l’auteur (à arbitrer globalement sur ch. 0, 11, 12, 14 plutôt qu’isolément).
  - `01-outils-logique-probabilite.md:9` (« *solide* » pour *sound*) : usage répandu en logique francophone ; `01:52` (« ligne stable ») et `02:52` (« Raffinement progressif ») : termes techniques usuels.
  - `06-detecter-une-erreur.md:44` (« conduire une enquête ») : pleinement idiomatique.
  - `07-cadre-cause-commune.md:3, 117, 121` (« une pertinence nouvelle ») : substantivation défendable en philosophie.
  - `09-severite-echappement.md:56, 74, 151, 162, 190` (« producteur très exact / plus exact ») : choix terminologique voulu au ch. 9 pour opposer *exact* (faible $P(E)$) à *précis* (faible $f$).
  - `14-chaines-qui-agissent.md:45` (« impliqué dans »), `14:60, 99` (« contrainte / règle métier »), `14:116` (« suite de tests »), `10:11` / `11:17` (« opérer ») : passés dans le lexique technique courant (retouche purement facultative).
  - `17-decisions-sans-appel.md:17, 82` / `partie-5.md:5` (« son seul levier ») et `18-remede-trois-niveaux.md:146, 176` (« ne tiennent qu’ensemble », « ne tiennent pas sans appui ») : français idiomatique (contrairement à l’emploi transitif fautif `18:136`).
- **Figures, tableaux et registre :**
  - `fig_ch01_bayes_cotes.py:21-25, 48` et `tableaux/ch01-bayes-cotes.md:3-6` (« Lot courant, signal anormal », « (cote × 5) ») : étiquettes tabulaires abrégées usuelles sur un graphique à barres.
  - `fig_ch05_ferrure_marge.py:32-33` (« Aléatoire (alliage) », « Épistémique (efforts) ») : contrainte de largeur de segments renvoyant aux termes du registre du ch. 5.
  - `fig_chaine.py:16` (« chaque étape contrôlée par un pair ») : tournure nominale standard de légende de courbe.
  - `fig_echappement.py:64` / `tableaux/ch09-echappement.md:16` (« Contrôleur fixe ») : conforme au sens mathématique de paramètre fixé dans `09:68`.
  - `registre_termes.md:65` / `annexes/B-glossaire.md:47` (« au sommet de la pile ») : métaphore technique filée dans toute la partie III (`00-cart:107`, `12:31,82,154,165`, `15:28`, `18:39`).
  - `Taux de faux positifs` (`ch09-depistage.md`), `Relecteur` (`ch09-desaccords.md`) et `P(faux)` (`ch09`/`ch16`) : cohérents avec la prose du ch. 9 (`09:9, 56, 68`).

---

## 3. Oublis notables ajoutés lors de la vérification

### A. Titres `#` / `##` / `###`, `titre="..."` et prose (`verifier-prose`)
- `05-trois-incertitudes.md:82` | `[Titre]` | `titre="Ce que pèse la décomposition de la variance"` (*weighs* / sens flou pour « Ce que mesure… »).
- `06-detecter-une-erreur.md:57` | `[Titre]` | `titre="Une proposition presque définitionnelle dont la portée tient aux cinq conditions"` (*définitionnelle* < *definitional*, *tient aux* < *hinges on*).
- `07-cadre-cause-commune.md:47`, `08-independance-chaines.md:122`, `09-severite-echappement.md:114`, `17-decisions-sans-appel.md:34` | `[Titre]` | Titres des modèles formels sur le moule `Modèle M1/M2/M3 : <liste nominale sans articles>`.
- `08-independance-chaines.md:5`, `10-couches-basses.md:5` | `[Titre]` | `## Boîte à outils : fiabilité en série et en parallèle` / `les contrats logiciels` (moule à deux-points).
- `09-severite-echappement.md:150`, `14-chaines-qui-agissent.md:54`, `16-angles-morts-collectifs.md:26` | `[Titre]` | Titres `.exemple-quantitatif` en empilement nominal sans article initial (`Contrôleur fixe, taux d'erreur décroissant…`, `Trajectoire d'agent…`, `Modèle partagé, précision…`).
- `09-severite-echappement.md:173` | `[Titre]` | `titre="La baisse du taux d'erreur n'érode pas la prise en compte par la seule règle de Bayes"` (*by Bayes' rule alone*).
- `12-autre-regime.md:19` | `[Titre]` | `titre="Définissable ne signifie pas bruyant"` (calque de *noisy* = manifeste/détectable, non acoustique).
- `13-synthese-deux-axes.md:1` (`# Synthèse : deux axes…`) et `13:37, 141` (`titre="Vider la case par avance, non par nature"`, `titre="Simplex déplace la vérification, non la validation"`) | `[Titre]` | Moule `X : Y` et antithèses `X, non Y`.
- `99-conclusion.md:1` (`# Conclusion : la méthode appliquée à elle-même`) et `99-conclusion.md:71` (`### Le sens de variation du produit entre taux d'erreur et échappement reste à mesurer`) | `[Titre]` | « produit *entre* A et B » (au lieu de « produit *du* taux d'erreur *par* la probabilité d'échappement ») + omission d’articles.
- `08-independance-chaines.md:146` et `14-chaines-qui-agissent.md:62` | `[Légende]` | « pour une erreur indépendante par étape $p = 6\,\%$ » (ellipse prépositionnelle devant $p$).
- `12-autre-regime.md:123` | `[Légende]` | « …avec mise en évidence de la réponse juste, sévérité d’un contrôle par 5 tirages et taux d’alerte à tort. » (omission d’articles).
- `13-synthese-deux-axes.md:31` | `[Légende]` | Attaque nominale à deux-points (`Dynamique de la matrice à deux axes : croisement…`).
- `99-conclusion.md:146` | `[Lexique]` | « proposition définitionnelle » (comme `06:57`). *(Coquille grammaticale hors calque relevée au passage : `99-conclusion.md:107` « comment ce livre a été élaboré (…), et on la rappelle ici ».)*

### B. Figures, tableaux, annexes et légendes (`verifier-fig`)
- `fig_ch00_carte_ouvrage.py:46` | `[Figure-Label]` | « frontière et longue traîne » (troncation du terme du registre *frontière en dents de scie*).
- `fig_ch18_trois_niveaux.py:38` | `[Figure-Label]` | « ancrage documentaire (RAG) » (sigle anglais non francisé ni mis en italique dans le schéma).
- `fig_ch18_trois_niveaux.py:41` | `[Figure-Label]` | « capacité nommée » (*named capacity* → « capacité dédiée » ou « poste désigné »).
- `fig_echappement.py:25` (`tableaux/ch09-echappement.md:8`, `ch16-modele-partage.md:8`, `D-parametres.md:90`) | `[Figure-Label | Tableau]` | « Alertes qui sont de vraies erreurs (VPP) » (*Alerts that are true errors* → « Proportion de vraies erreurs parmi les alertes (VPP) »).
- `fig_echappement.py:69` (`parametres.py:98`, `tableaux/ch16-modele-partage.md:1`, `D-parametres.md:83`) | `[Figure-Label | Tableau]` | « Un modèle pour tous » (*One model for all*).
- `tableaux/ch17-scenarios.md:1` (`fig_seu.py:88`) | `[Tableau]` | « Ce que l’on pense p » (« Probabilité estimée $p$ »).
- `annexes/A-outils.md:69` | `[Annexe]` | « échoue avec probabilité estimée $p$ » (omission de l’article → « avec une probabilité estimée $p$ »).
- `annexes/A-outils.md:100` | `[Annexe]` | « — (1) …, (2) …, et (3) … —, » (incise anglo-saxonne `—,`).
- `annexes/A-outils.md:114` | `[Annexe]` | « fait systématiquement défaut sur la classe $E_k$ » (*on class* → « pour la classe $E_k$ »).
- `annexes/A-outils.md:132` | `[Annexe]` | « émet des affirmations fausses au taux d’erreur $P(E)$ » (*at error rate* → « avec un taux d’erreur $P(E)$ »).
- `annexes/D-parametres.md:3` | `[Annexe]` | « engendrés mécaniquement » (*mechanically generated* → « générés automatiquement »).
- `annexes/D-parametres.md:119` | `[Annexe]` | « 6e date 10 % » (discordance mineure avec `tableaux/ch12-plausibilite.md:5` « une autre date 10 % »).
- `06-detecter-une-erreur.md:53` vs `fig_ch06_cinq_conditions.py:41-42` : la légende dit « arrivée à temps » et « prise en compte », mais la figure tronque en « 4. À temps » et abrège en « reçu + droit d’agir ».
- `08-independance-chaines.md:146` vs `14-chaines-qui-agissent.md:62` : calque de participe réduit en légende + divergence entre « un pair » (ch. 8) et « un contrôleur » (ch. 14).
- `09-severite-echappement.md:153` : « le producteur devient plus exact » (*more accurate*).
- `12-autre-regime.md:123` vs `fig_plausibilite.py:28` : légende sans articles, et la figure ne mentionne pas « 5 tirages ».
- `17-decisions-sans-appel.md:66` vs `fig_seu.py:79` : « la grandeur sur laquelle on décide » reprend « décider sur » (*decide on*).

---

## 4. Inventaire détaillé par fichier (prose et titres)

### Liminaires (`livre.yaml`, `00-avant-propos.md`, `00-cartographier.md`)

#### `monographie/livre.yaml`
- `livre.yaml:5` | `[Titre]` | « Cadre, contrôles et décision, de l’informatique classique à l’IA » | empilement nominal sans articles (*Frame, Checks and Decision, from Classical Computing to AI*) | « Le cadre, les contrôles et la décision, de l’informatique classique à l’intelligence artificielle »

#### `monographie/chapitres/00-avant-propos.md`
- `00-avant-propos.md:3` | `[Titre]` | « Pourquoi ce livre » | titre elliptique (*Why This Book*) | « Pourquoi écrire ce livre ? » ou « Objet de l’ouvrage »
- `00-avant-propos.md:7` | `[Syntaxe]` | « agir au mieux sur le monde à travers une représentation finie » | *through* | « au moyen d’une représentation finie »
- `00-avant-propos.md:7` | `[Lexique]` | « portent mieux le propos qu’une équation » | *carry the point* | « éclairent mieux le propos »
- `00-avant-propos.md:9` | `[Ponctuation]` | « La question directrice de l’ouvrage — *qu’est-ce qui peut nous avertir… ?* — est » | incise à tirets séparant sujet et verbe | « L’ouvrage part d’une question directrice : *qu’est-ce qui peut nous avertir…* Cette question est… »
- `00-avant-propos.md:9` | `[Syntaxe]` | « du jugement sous incertitude » | *judgment under uncertainty* | « du jugement dans l’incertitude »
- `00-avant-propos.md:9` | `[Lexique]` | « exige de tenir ensemble les fondements épistémologiques […] et l’architecture concrète » | *hold together* | « exige d’articuler les fondements épistémologiques […] et l’architecture concrète »
- `00-avant-propos.md:11` | `[Titre]` | « Une démarche de travail, non une prescription » | antithèse nominale (*A Working Approach, Not a Prescription*) | « Une démarche de travail plutôt qu’une prescription »
- `00-avant-propos.md:13` | `[Lexique]` | « reporter le problème un cran plus haut » | *one notch up* | « reporter le problème d’un degré »
- `00-avant-propos.md:17` | `[Syntaxe | Lexique]` | « précisant sous quelles hypothèses elle tient » | *under which assumptions it holds* | « précisant à quelles conditions elle demeure valable »
- `00-avant-propos.md:21` | `[Ponctuation | Lexique]` | « de culture scientifique et technique — ingénieurs, […] — qui ont croisé le calcul des probabilités » | incise à tirets + *came across* | « de culture scientifique et technique (ingénieurs, …) qui ont abordé le calcul des probabilités »
- `00-avant-propos.md:29` | `[Lexique | Syntaxe | Ponctuation]` | « à travers des littératures habituellement séparées — philosophie des sciences, […] —, ainsi que pour structurer » | *across* + *literatures* + `—, ` | « dans des disciplines habituellement cloisonnées (philosophie des sciences, …), ainsi que pour structurer »
- `00-avant-propos.md:29` | `[Lexique]` | « rédiger une large part du texte » | *a large part* | « rédiger une grande part du texte »
- `00-avant-propos.md:43` | `[Lexique]` | « n’en portent jamais seuls une étape indispensable » | *carry a step* | « n’en assurent jamais seuls une étape indispensable »
- `00-avant-propos.md:50` | `[Syntaxe]` | « des hypothèses sous lesquelles un résultat est établi » | *under which* | « des hypothèses moyennant lesquelles un résultat est établi »
- `00-avant-propos.md:51` | `[Lexique]` | « mettre une propriété structurelle à nu » | *lay bare* | « mettre en évidence une propriété structurelle »
- `00-avant-propos.md:53` | `[Lexique]` | « un cas frontière » | *borderline/edge case* | « un cas limite »

#### `monographie/chapitres/00-cartographier.md`
- `00-cartographier.md:7` | `[Ponctuation | Lexique]` | « des défaillances d’organisation — anomalies non instruites, absence de recalcul indépendant —, mais sous elles se trouvait » | `—, ` + *beneath them lay* | « (anomalies non instruites, absence de recalcul indépendant), mais à leur racine se trouvait »
- `00-cartographier.md:11` | `[Ponctuation]` | « déplace encore le regard : de la machine vers le jugement de l’expert qui l’utilise. » | deux-points rhétorique | « déplace encore le regard, de la machine vers le jugement de l’expert qui l’utilise. »
- `00-cartographier.md:14` | `[Syntaxe]` | « Tirées au sort, leurs tâches réelles ont pris en moyenne environ 19 % de temps de plus » | *Randomized, their real tasks…* | « Réparties aléatoirement entre les deux conditions, leurs tâches réelles ont demandé environ 19 % de temps supplémentaire »
- `00-cartographier.md:14` | `[Lexique]` | « d’experts opérant dans leur propre domaine » | *operating in their own domain* | « d’experts exerçant dans leur propre domaine »
- `00-cartographier.md:17` | `[Lexique]` | « indiscernable en surface d’une réponse exacte » | *on the surface* | « indiscernable en apparence d’une réponse exacte »
- `00-cartographier.md:41` | `[Syntaxe]` | « ouvert d’exceptions possibles » | *open-ended of possible exceptions* | « ensemble ouvert d’exceptions possibles »
- `00-cartographier.md:61` | `[Titre | Ponctuation]` | « Ce que mesure — et ce que tait — une barre d’erreur » | *What an Error Bar Measures — and What It Hides* | « Ce que mesure une barre d’erreur et ce qu’elle tait »
- `00-cartographier.md:63` | `[Syntaxe]` | « Examiner comment une barre d’erreur est calculée dissipe cette illusion. » | gérondif sujet | « L’examen du mode de calcul d’une barre d’erreur dissipe cette illusion. »
- `00-cartographier.md:63,69` | `[Ponctuation]` | incises entre tirets cadratins séparant sujet et verbe | rythme anglais | parenthèses ou restructuration
- `00-cartographier.md:83,152,154,179` | `[Ponctuation]` | séquences `—, ` | ponctuation anglo-saxonne | parenthèses `(…),`
- `00-cartographier.md:97` | `[Titre | Lexique]` | « L’informatique classique a gagné ses garanties ; les modèles appris les dépensent » | *earn / spend guarantees* | « L’informatique classique fonde ses garanties ; les modèles appris y renoncent pour gagner en portée »
- `00-cartographier.md:105,150,233` | `[Lexique]` | *dépensée / acheter une portée / acheter une garantie* | *spend / buy* (à arbitrer globalement sur ch. 0, 11, 12, 14) | « cédée / acquise au prix de »
- `00-cartographier.md:109` | `[Syntaxe]` | « vérifiable sur chaque appel » | *on every call* | « vérifiable à chaque appel »
- `00-cartographier.md:115` | `[Titre]` | « Ce que l’automatisation fait aux contrôles » | *What Automation Does to Checks* | « Comment l’automatisation transforme les contrôles »
- `00-cartographier.md:117` | `[Lexique]` | « elle retire des contrôles humains implicites » | *removes checks* | « elle supprime des contrôles humains implicites »
- `00-cartographier.md:121` | `[Syntaxe]` | « Structurellement, … Opérationnellement, … » | *Structurally, … Operationally, …* | « Sur le plan structurel, … Dans son fonctionnement, … »
- `00-cartographier.md:135` | `[Lexique]` | « retournent alimenter le Web » | *go back to feed* | « viennent réalimenter le Web »
- `00-cartographier.md:137` | `[Titre]` | « L’énigme arithmétique du producteur plus fiable et du système plus risqué » | empilement nominal anglais | « Comment un producteur plus fiable peut rendre le système plus risqué »
- `00-cartographier.md:141` | `[Syntaxe]` | « avec des chiffres choisis pour l’illustration » | *chosen for illustration* | « avec des chiffres choisis à titre d’illustration »
- `00-cartographier.md:146` | `[Lexique]` | « Bien que son producteur soit dix fois plus exact » | *ten times more accurate* | « Bien que son producteur commette dix fois moins d’erreurs »
- `00-cartographier.md:154` | `[Syntaxe]` | « toucherait le monde réel à fort coût » | *at high cost* | « toucherait le monde réel à grands frais »
- `00-cartographier.md:158` | `[Syntaxe | Lexique]` | « *Sous quelles conditions ce chiffre tient-il ?* » | *Under what conditions does this number hold?* | « *À quelles conditions ce chiffre demeure-t-il valable ?* »
- `00-cartographier.md:166` | `[Lexique | Ponctuation]` | « le niveau situé dessous : le code sous le programme généré, la physique sous le nombre calculé. » | *the level underneath* + chute nominale | « le niveau sous-jacent, qu’il s’agisse du code derrière le programme généré ou de la physique derrière le calcul. »
- `00-cartographier.md:181` | `[Lexique]` | « examine les *pipelines* et les agents autonomes » | terme anglais non glosé à la 1re occurrence (§ 8) | « examine les chaînes de traitement (*pipelines*) et les agents autonomes »
- `00-cartographier.md:196` | `[Lexique]` | « Trois modèles formels portent l’argument » | *carry the argument* | « Trois modèles formels étayent l’argument »
- `00-cartographier.md:222` | `[Légende | Syntaxe]` | « Huit parcours de lecture à travers la monographie » | *through the monograph* | « Huit parcours de lecture dans la monographie »
- `00-cartographier.md:234` | `[Syntaxe]` | « corrèle les erreurs à travers les communautés » | *across communities* | « corrèle les erreurs d’une communauté à l’autre »

---

### Partie I (`partie-1.md`, ch. 1–4)

#### `monographie/parties/partie-1.md`
- `partie-1.md:5` | `[Lexique]` | « aucun ne livre de conclusion sans condition » | *deliver a conclusion* | « aucun n’établit de conclusion sans condition »

#### `monographie/chapitres/01-outils-logique-probabilite.md`
- `01-outils-logique-probabilite.md:1` | `[Titre]` | « # Boîte à outils : logique, conditionnement, probabilité » | liste nominale sans articles ni coordonnant | « # Boîte à outils : la logique, le conditionnement et la probabilité »
- `01-outils-logique-probabilite.md:3,7,173` | `[Lexique]` | « livre de conclusion / ses conclusions » | *deliver conclusions* | « établit / garantit ses conclusions »
- `01-outils-logique-probabilite.md:3,24` | `[Lexique]` | « le « pourvu que » qui le fait tenir » / « qui la font tenir » | *makes it hold* | « dont dépend sa validité » / « qui la rendent valable »
- `01-outils-logique-probabilite.md:18` | `[Lexique]` | « qui gouvernent le phénomène » | *govern* | « qui régissent le phénomène »
- `01-outils-logique-probabilite.md:36,57,83,144` | `[Titre]` | titres à deux-points `X : Y` (« Probabilité : règles et lectures », « Fréquence ou jugement : un débat… », « Réviser un jugement : la règle de Bayes… », « Mesurer la qualité d’une prévision : la surprise ») | moule anglais `X : Y` | « Règles et interprétations de la probabilité », « Un débat ouvert : fréquence ou jugement ? », « Réviser un jugement par la règle de Bayes… », « Mesurer la qualité d’une prévision par la surprise »
- `01-outils-logique-probabilite.md:58` | `[Lexique]` | « à titre de position de travail » | *working position* | « à titre d’hypothèse de travail »
- `01-outils-logique-probabilite.md:71` | `[Syntaxe]` | « lorsque savoir $A$ ne change pas » | *knowing A* | « lorsque la connaissance de $A$ ne change pas »
- `01-outils-logique-probabilite.md:93,97,103,120,139,148,166` | `[Syntaxe]` | « sous chacune des deux hypothèses » / « sous une prévision » (9 occ.) | *under* | « dans chacune des deux hypothèses » / « selon une prévision »
- `01-outils-logique-probabilite.md:105` | `[Titre]` | « Dérivation de la règle de Bayes sous forme de cotes » | faux-ami *derivation* | « Établissement [ou Démonstration] de la règle de Bayes sous forme de cotes »
- `01-outils-logique-probabilite.md:128` | `[Syntaxe | Ponctuation | Lexique]` | « Sur cette zone suspecte » / incise longue à tirets / « délivre elle aussi un signal anormal » | *on this zone* + tirets + *delivers a signal* | « Dans cette zone suspecte » / parenthèses / « émet elle aussi un signal anormal »

#### `monographie/chapitres/02-cadre.md`
- `02-cadre.md:1` | `[Titre]` | « # Le cadre : ce qui compte et ce qu’on tait » | moule `X : Y` | « # Le cadre, ou le partage entre ce qui compte et ce qu’on tait »
- `02-cadre.md:7` | `[Lexique]` | « Toute action menée avec méthode part d’une cible… » | *starts from a target* | « …met en jeu une cible visée, un état du monde et l’écart entre les deux »
- `02-cadre.md:17` | `[Légende]` | « Cible, monde, représentation et action. » | fragment nominal sans verbe | « Relations entre la cible, le monde, la représentation et l’action. »
- `02-cadre.md:64` | `[Lexique]` | « Il gouverne aussi tout modèle… » | *governs* | « Il régit aussi tout modèle… »
- `02-cadre.md:85` | `[Lexique]` | « portent le travail de modélisation » | *carry the modeling work* | « concentrent le travail de modélisation »
- `02-cadre.md:89,121` | `[Titre | Syntaxe]` | « Conditionnement sur les variables du cadre » / « sur lesquelles on conditionne » | *conditioning on* | « Conditionnement par les variables du cadre » / « selon lesquelles on conditionne »
- `02-cadre.md:115,121` | `[Syntaxe]` | « L’idée est séduisante, et elle est fausse » / « la garantie est réelle et conditionnelle. » | *and* adversatif | « … ; elle est pourtant fausse » / « …, mais conditionnelle. »
- `02-cadre.md:125` | `[Titre]` | « Relativité au cadre des garanties déductives et inductives » | empilement nominal (*frame-relativity of…*) | « Dépendance des garanties déductives et inductives à l’égard du cadre »
- `02-cadre.md:128,129` | `[Titre]` | « Une garantie déductive/inductive conditionnelle : le calcul causal sur graphe / la prédiction conforme. » | amorce à deux-points + « sur graphe » sans article | « …sur des graphes » / virgule ou apposition
- `02-cadre.md:129` | `[Lexique | Ponctuation]` | « sert à calibrer le seuil » + séquence `—, ` | *calibrate* (avant ch. 3) + `—, ` | « sert à régler [ou étalonner] le seuil » + `(…),`
- `02-cadre.md:142` | `[Lexique]` | « passer avec succès toutes les épreuves » | *pass all tests* | « réussir toutes les épreuves »
- `02-cadre.md:146` | `[Syntaxe]` | « des hypothèses sous lesquelles ses propres tests fonctionnent » | *under which* | « des hypothèses dans le cadre desquelles ses propres tests sont valables »

#### `monographie/chapitres/03-mondes-possibles.md`
- `03-mondes-possibles.md:1` | `[Titre]` | « # Mondes possibles : la probabilité comme jugement » | moule `X : Y` sans article | « # Les mondes possibles, ou la probabilité comme jugement »
- `03-mondes-possibles.md:37` | `[Titre]` | « ## Prévision et prévisionniste » | absence d’articles | « ## La prévision et le prévisionniste »
- `03-mondes-possibles.md:47` | `[Titre]` | « Ce qu’une seule course dit de deux prévisions » | *what X says about Y* | « Ce qu’une seule course révèle de deux prévisions »
- `03-mondes-possibles.md:67,88` | `[Syntaxe]` | « sous la première hypothèse… » / « sous le jugement $q$ » | *under* | « dans la première hypothèse… » / « selon le jugement $q$ »
- `03-mondes-possibles.md:98` | `[Syntaxe]` | « Et, sur des issues jugées indépendantes, » | *And, on independent outcomes* | « De plus, pour des issues jugées indépendantes, »

#### `monographie/chapitres/04-decider.md`
- `04-decider.md:20` | `[Titre]` | « L’utilité espérée subjective : actes, états et conséquences » | moule `X : A, B et C` | « Actes, états et conséquences dans l’utilité espérée subjective »
- `04-decider.md:46,52` | `[Titre | Lexique]` | « Dérivation du seuil de décision » / « La dérivation ne suppose rien… » | faux-ami *derivation* | « Établissement [ou Démonstration] du seuil de décision » / « La démonstration… »
- `04-decider.md:52` | `[Lexique]` | « *Décision sur la croyance.* » | *decision on belief* | « *Décision fondée sur la croyance.* »
- `04-decider.md:84,119` | `[Ponctuation]` | incises à tirets cadratins | rythme anglais | parenthèses
- `04-decider.md:88` | `[Titre]` | « Seuil de décision et rapport des enjeux : course à la voile et roulette russe » | moule `X : Y` sans articles | « Seuil de décision et rapport des enjeux dans la course à la voile et la roulette russe »
- `04-decider.md:91,100` | `[Légende | Syntaxe]` | « sur deux axes logarithmiques » / « sur les axes logarithmiques » | *on logarithmic axes* | « en échelle doublement logarithmique » / « en coordonnées logarithmiques »
- `04-decider.md:121` | `[Lexique]` | « ce que notre cadre a manqué » | *what our frame missed* | « ce que notre cadre a omis [ou laissé échapper] »

---

### Partie II (`partie-2.md`, ch. 5–9)

#### `monographie/parties/partie-2.md`
- `partie-2.md:9` | `[Lexique]` | « permet de rattraper des fautes d’exécution » | *catch errors* | « permet de déceler [ou d’intercepter] des fautes d’exécution »
- `partie-2.md:9` | `[Lexique]` | « là où l’essai coûte peu et peut être défait » | *can be undone* | « là où l’essai coûte peu et reste réversible »
- `partie-2.md:11` | `[Syntaxe]` | « Il leur faut pourtant partager assez pour pouvoir être comparés » | *share enough* | « Il leur faut pourtant avoir suffisamment d’éléments en commun… »

#### `monographie/chapitres/05-trois-incertitudes.md`
- `05-trois-incertitudes.md:1` | `[Titre]` | « Trois incertitudes, et ce que mesure une barre d’erreur » | virgule avant *et* + absence d’article | « Les trois incertitudes et ce que mesure une barre d’erreur »
- `05-trois-incertitudes.md:18` | `[Syntaxe]` | « En conditionnant d’abord sur $\theta$ » | *conditioning on* | « En conditionnant d’abord par rapport à $\theta$ » (ou « À $\theta$ fixé »)
- `05-trois-incertitudes.md:27,39,118` | `[Titre]` | titres `X : Y` (« Incertitude aléatoire… : un choix de modélisation », « L’incertitude ontologique : quand… », `titre="Challenger : représentation…"`) | moule `X : Y` | reformuler avec prépositions/virgules
- `05-trois-incertitudes.md:54` | `[Lexique]` | « une queue extrême déjà présente dans les barres d’erreur » | *extreme tail* | « un événement extrême [ou une extrémité de distribution] »
- `05-trois-incertitudes.md:57` | `[Lexique]` | « habitent à l’intérieur de l’ensemble $\Theta$ » | *live inside* | « se situent à l’intérieur de l’ensemble $\Theta$ »
- `05-trois-incertitudes.md:71,91` | `[Syntaxe]` | « sous une même loi admise » / « sous hypothèse de moments du second ordre finis » | *under* + ellipse de l’article | « selon une même loi admise » / « sous l’hypothèse de… »
- `05-trois-incertitudes.md:75` | `[Lexique]` | « aide à fixer ce point » | *helps fix this point* | « aide à préciser ce point »
- `05-trois-incertitudes.md:82` | `[Titre]` | `titre="Ce que pèse la décomposition de la variance"` | *weighs* | `titre="Ce que mesure la décomposition de la variance"`
- `05-trois-incertitudes.md:97` | `[Syntaxe]` | « Il ne faut pas lire la @prop:desaccord comme signifiant que » | *read X as meaning* | « Il ne faut pas comprendre la @prop:desaccord comme affirmant que »
- `05-trois-incertitudes.md:104` | `[Lexique]` | « comment la conclusion bouge » | *moves* | « comment la conclusion varie »

#### `monographie/chapitres/06-detecter-une-erreur.md`
- `06-detecter-une-erreur.md:1` | `[Titre]` | « Détecter une erreur : comparateurs et cinq conditions » | `X : Y` sans articles | « Détecter une erreur grâce aux comparateurs et à cinq conditions »
- `06-detecter-une-erreur.md:3` | `[Lexique]` | « relit le cas *Challenger* à cette lumière » | *in this light* | « relit le cas *Challenger* sous cet éclairage »
- `06-detecter-une-erreur.md:26` | `[Lexique]` | « À l’échelle ordinaire… À l’échelle technique… » | *at the ordinary / technical scale* | « Dans la vie courante… Dans la pratique technique… »
- `06-detecter-une-erreur.md:57` | `[Titre]` | `titre="Une proposition presque définitionnelle dont la portée tient aux cinq conditions"` | *definitional* + *hinges on* | reformuler sans « définitionnelle » ni « tient à »
- `06-detecter-une-erreur.md:78` | `[Syntaxe]` | « l’affichent $P(\text{faux})$ » | *display it as* sans préposition | « la notent $P(\text{faux})$ »
- `06-detecter-une-erreur.md:129` | `[Syntaxe]` | « En supposant la comparabilité assurée — les deux côtés… —, que prouve ce désaccord ? » | participe d’ouverture sans coréférence + *both sides* | « Si l’on suppose la comparabilité assurée — les deux termes… —, que prouve ce désaccord ? »
- `06-detecter-une-erreur.md:131,133,135` | `[Lexique]` | « Pris tel quel » (*Taken as is*) / « délivre une signature » (*delivers*) / « un des deux côtés » (*one of the two sides*) | faux-amis | « À lui seul, cet accord… » / « appose une signature » / « l’un des deux termes »

#### `monographie/chapitres/07-cadre-cause-commune.md`
- `07-cadre-cause-commune.md:47` | `[Titre]` | `titre="Modèle M3 : erreur dans le cadre et facteur omis hors du cadre"` | moule `Modèle M3 : <liste nominale sans articles>` | « Modèle M3 : l’erreur dans le cadre et le facteur omis hors du cadre »
- `07-cadre-cause-commune.md:71,74` | `[Titre | Syntaxe]` | « conditionnement sur le cadre » / « conditionnent rarement sur le vecteur $x$ » | *condition on* | « conditionnement par le cadre » / « se restreignent rarement au seul vecteur $x$ »
- `07-cadre-cause-commune.md:98` | `[Lexique]` | « passer ses propres contrôles internes » | *pass checks* | « réussir ses propres contrôles internes »
- `07-cadre-cause-commune.md:109` | `[Lexique]` | « Les théorèmes dits *no free lunch* » | anglicisme non glosé à la 1re occurrence (§ 8) | « …*no free lunch* (*pas de repas gratuit*) »
- `07-cadre-cause-commune.md:115` | `[Lexique]` | « attrapent des défauts bien réels » | *catch defects* | « interceptent [ou décèlent] des défauts bien réels »

#### `monographie/chapitres/08-independance-chaines.md`
- `08-independance-chaines.md:5` | `[Titre]` | `## Boîte à outils : fiabilité en série et en parallèle` | moule à deux-points | « ## Boîte à outils sur la fiabilité en série et en parallèle »
- `08-independance-chaines.md:45,49` | `[Titre | Ponctuation]` | « L’indépendance est relative, et se paie en comparabilité » | virgule anglaise devant *et* | supprimer la virgule
- `08-independance-chaines.md:55,79` | `[Lexique]` | « mordre sur vos chiffres / le dossier » | *have bite on* | « avoir prise sur… »
- `08-independance-chaines.md:57` | `[Tableau]` | `| Comparateur | Partage avec l’affirmation | Peut déceler | Coût indicatif |` | en-têtes télégraphiques | `| Comparateur | Ce qu’il partage avec l’affirmation | Erreurs décelables | Coût indicatif |`
- `08-independance-chaines.md:76` | `[Titre]` | `titre="Une tendance de coût direct, une tension structurelle sur la comparabilité"` | juxtaposition asyndétique | « Une tendance sur le coût direct, mais une tension structurelle sur la comparabilité »
- `08-independance-chaines.md:79` | `[Lexique]` | « bon marché à produire » | *cheap to produce* | « peu coûteux à produire »
- `08-independance-chaines.md:82,192` | `[Lexique]` | « fait tenir cette formule » / « tiennent » | *hold* | « valide cette formule » / « sont assurées »
- `08-independance-chaines.md:86,122` | `[Titre]` | `titre="Vingt-sept versions… : l’expérience de Knight et Leveson"` / `titre="Modèle M1 : …"` | moule `X : Y` sans articles | reformuler en français suivi
- `08-independance-chaines.md:104` | `[Titre | Lexique]` | « Chaînes contre contrôles croisés » | *Chains vs. cross-checks* | « Chaînes et contrôles croisés »
- `08-independance-chaines.md:106` | `[Lexique]` | « câble plusieurs composants entre eux » | *wire together* | « relie plusieurs composants entre eux »
- `08-independance-chaines.md:146` | `[Légende]` | « pour une erreur indépendante par étape $p = 6\,\%$ » | ellipse devant $p$ | « pour une probabilité d’erreur indépendante par étape $p = 6\,\%$ »
- `08-independance-chaines.md:163` | `[Lexique]` | « le dialogue casse » | *dialogue breaks* | « le dialogue se rompt »
- `08-independance-chaines.md:188` | `[Lexique]` | « Dans les termes du modèle M1 » | *In the terms of* | « Selon le modèle M1 »
- `08-independance-chaines.md:201` | `[Lexique]` | « tire structurellement contre la comparabilité » | *pulls against* | « s’oppose structurellement à la comparabilité »

#### `monographie/chapitres/09-severite-echappement.md`
- `09-severite-echappement.md:3` | `[Syntaxe]` | « en taux d’erreur multiplié par probabilité d’échappement » | omission d’articles | « en produit du taux d’erreur par la probabilité d’échappement »
- `09-severite-echappement.md:15` | `[Lexique]` | « le test délivre $9 + 49{,}5 = 58{,}5$ résultats positifs » | *delivers* | « le test produit… »
- `09-severite-echappement.md:42` | `[Lexique]` | « déplace la confiance vers $\bar{E}$ » | *shifts confidence toward* | « renforce la confiance en $\bar{E}$ »
- `09-severite-echappement.md:74,160,188` | `[Lexique]` | « attraper une erreur » / « vraie erreur attrapée » | *catch an error* | « intercepter [ou détecter] »
- `09-severite-echappement.md:88,114,150,173` | `[Titre]` | titre-équation `Risque = taux d’erreur × probabilité d’échappement` (88), `Modèle M1 : …` (114), `Contrôleur fixe, taux d’erreur décroissant…` (150), `…par la seule règle de Bayes` (173) | titres télégraphiques / *by Bayes' rule alone* | reformuler avec articles et syntaxe française
- `09-severite-echappement.md:135,162` | `[Syntaxe]` | « sous examen complet » / « sous appariement des probabilités » | *under* sans article | « lorsque chaque alerte est examinée » / « en cas d’appariement des probabilités »
- `09-severite-echappement.md:153` | `[Légende]` | « sur axe horizontal logarithmique » + « suppose les alertes suivies… / suppose chaque alerte examinée » + « devient plus exact » | ellipse d’article + participe réduit + *more accurate* | « sur un axe… » + « suppose que les alertes sont suivies… » + « commet moins d’erreurs »
- `09-severite-echappement.md:166` | `[Lexique]` | « panneau de gauche / droite » | *panel* | « volet [ou graphique] de gauche / droite »
- `09-severite-echappement.md:176` | `[Lexique]` | « par en dessous » | *from below* | « par valeurs inférieures »
- `09-severite-echappement.md:189` | `[Lexique]` | « qui paie lorsque les enjeux sont élevés » | *pays off* | « avantageuse lorsque les enjeux sont élevés »

---

### Partie III (`partie-3.md`, ch. 10–13)

#### `monographie/parties/partie-3.md`
- `partie-3.md:3` | `[Lexique]` | « l’argument, lui, ne doit dépendre… » | *the argument* | « la démonstration [ou le raisonnement], elle, ne doit dépendre… »
- `partie-3.md:7` | `[Syntaxe]` | « l’ajustement sur des préférences humaines » | *tuning on human preferences* | « l’ajustement à partir de préférences humaines »
- `partie-3.md:9,11` | `[Syntaxe]` | « de l’intérieur d’une conversation / du cadre » | *from inside* | « au fil d’une conversation » / « sans sortir du cadre »
- `partie-3.md:11` | `[Syntaxe | Ponctuation]` | « vos propres contrôles — ceux de la personne… — » | *your own checks* en récit à la 3e personne + tirets | « ses propres contrôles (ceux de la personne…) »

#### `monographie/chapitres/10-couches-basses.md`
- `10-couches-basses.md:5,125` | `[Titre]` | `## Boîte à outils : les contrats logiciels` / `Écrire n’est pas encore vérifier : les trois degrés du contrat` | moule `X : Y` | « ## Boîte à outils sur les contrats logiciels » / « Les trois degrés du contrat, de l’écriture à la vérification »
- `10-couches-basses.md:9,54,55,95,101,132` | `[Ponctuation]` | incises à tirets cadratins (souvent `—,`) | rythme anglais | parenthèses ou virgules
- `10-couches-basses.md:46,48` | `[Lexique]` | « contrats exposés » (*exposed*) / « promesses tiennent » (*hold*) / « interface… tenue » | calques | « contrats publiés [ou offerts] » / « promesses sont tenues » / « interface… respectée »
- `10-couches-basses.md:58` | `[Syntaxe]` | « À travers ces trois exemples » | *Across* | « Dans ces trois exemples »
- `10-couches-basses.md:74,132` | `[Syntaxe]` | « ajuster des paramètres sur des données / exemples » | *fit on* | « ajuster des paramètres d’après des données / à partir d’exemples »
- `10-couches-basses.md:118` | `[Lexique]` | « remontés ni instruits » | *escalated* transitif | « transmis à la hiérarchie [ou signalés] ni instruits »

#### `monographie/chapitres/11-regle-tiree-des-donnees.md`
- `11-regle-tiree-des-donnees.md:3,15,23,100` | `[Lexique]` | *acheter une portée / dépenser la garantie* (à arbitrer globalement) | *buy reach / spend guarantees* | « gagner en portée en cédant [ou sacrifiant] en garantie »
- `11-regle-tiree-des-donnees.md:19,43,89` | `[Ponctuation]` | incises à tirets cadratins (`—,`) | rythme anglais | parenthèses ou virgules
- `11-regle-tiree-des-donnees.md:25,35,41,53,61,75` | `[Titre]` | « Le moteur à prédire le fragment suivant » (25), titres à deux-points (35, 53), fragment adjectival sans article « Fluide et faux… » (41), tiret dans un titre (61), « sur préférences humaines » sans article (75) | *next-token prediction engine*, `X : Y`, titre fragmenté | reformuler en français suivi avec articles
- `11-regle-tiree-des-donnees.md:29` | `[Lexique]` | « un modèle qui les capture » | *captures them* | « un modèle qui les saisit [ou en rend compte] »
- `11-regle-tiree-des-donnees.md:31` | `[Syntaxe]` | « à travers les couches du réseau » | *across the layers* | « d’une couche à l’autre du réseau »
- `11-regle-tiree-des-donnees.md:36` | `[Syntaxe]` | « évaluées environ 40 % plus haut en qualité » | *rated ~40% higher in quality* | « dont la qualité a été jugée supérieure d’environ 40 % »
- `11-regle-tiree-des-donnees.md:57` | `[Lexique]` | « des citations qui sonnent comme du droit » | *sound like law* | « des citations qui ont toute l’allure d’un texte juridique »
- `11-regle-tiree-des-donnees.md:64` | `[Syntaxe]` | « ce que la décision établit bel et bien est d’ordre juridique » | clivée *what… does establish is…* | « la décision établit en revanche un point d’ordre juridique »
- `11-regle-tiree-des-donnees.md:71,73,103` | `[Syntaxe | Lexique]` | « ajustement sur des préférences » + sigle *RLHF* non glosé dans le corps (§ 8) | *tuning on* + sigle anglais | « ajustement à partir de préférences humaines » + gloser *RLHF* à la l. 73

#### `monographie/chapitres/12-autre-regime.md`
- `12-autre-regime.md:3` | `[Lexique]` | « la portée s’achète au prix de la garantie » | *reach is bought* | « la portée s’obtient au prix de la garantie »
- `12-autre-regime.md:3,15,29,38,65,86,154` | `[Ponctuation]` | incises à tirets cadratins (`—,`) | rythme anglais | parenthèses ou virgules
- `12-autre-regime.md:13` | `[Syntaxe]` | « remonter une défaillance » | *trace back a failure* | « remonter à la source d’une défaillance »
- `12-autre-regime.md:15` | `[Lexique]` | « n’est pas l’axe du changement de régime. L’axe décisif est de savoir si » | *the axis … is whether* | « ne définit pas le changement de régime. La question décisive est de savoir si »
- `12-autre-regime.md:19,46,114,149` | `[Titre]` | `Définissable ne signifie pas bruyant` (*noisy* = manifeste), titres à deux-points `X : Y` (46, 114), « Deux sens de calibration, et où s’est logé l’indice d’incertitude » (149) | calques titulaires + faux-ami | reformuler
- `12-autre-regime.md:27` | `[Lexique]` | « l’impact borné de chaque erreur isolée » | *impact* | « la portée bornée [ou l’incidence limitée] »
- `12-autre-regime.md:29` | `[Syntaxe]` | « l’invoquer sur des tâches imprévues » | *invoke on* | « l’appeler pour des tâches imprévues »
- `12-autre-regime.md:38` | `[Lexique]` | « consomme la sortie d’un modèle » | *consumes the output* | « exploite [ou reçoit] la sortie d’un modèle »
- `12-autre-regime.md:49` | `[Lexique | Syntaxe]` | « *juste au-delà* » (*just beyond*) / « ont eu 19 points de pourcentage de moins de chances de parvenir à » (*were 19 pp less likely to*) | calques | « *tout juste au-delà* » / « ont vu leur probabilité de parvenir à une solution correcte reculer de 19 points de pourcentage »
- `12-autre-regime.md:58` | `[Lexique]` | « de chaque côté de la frontière » | *on either side* | « d’un côté comme de l’autre de la frontière »
- `12-autre-regime.md:76,77` | `[Lexique]` | « tient strictement » / « ne tient que pour » | *holds* | « s’applique strictement » / « ne vaut que pour »
- `12-autre-regime.md:86` | `[Lexique]` | « l’ensemble des complétions plausibles » | *completions* | « l’ensemble des prolongements plausibles »
- `12-autre-regime.md:89` | `[Syntaxe]` | « Sous les hypothèses de leur analyse statistique » | *Under the assumptions* | « Dans les hypothèses [ou Moyennant les hypothèses] »
- `12-autre-regime.md:123` | `[Légende]` | « …avec mise en évidence de la réponse juste, sévérité d’un contrôle par 5 tirages et taux d’alerte à tort. » | omission d’articles | ajouter les articles définis + mention « 5 tirages »
- `12-autre-regime.md:138` | `[Lexique]` | « attrape efficacement les erreurs hasardées » | *catches* | « intercepte [ou détecte] efficacement les erreurs hasardées »

#### `monographie/chapitres/13-synthese-deux-axes.md`
- `13-synthese-deux-axes.md:1,37,45,80,106,112,118,141` | `[Titre | Lexique]` | `# Synthèse : deux axes…` (1), `Vider la case par avance, non par nature` (37), `La formalité change la colonne, non la ligne` (*formality* = formalisme, 45), sous-titres `X : Y` (80, 106, 112, 118), `Simplex déplace la vérification, non la validation` (141) | moule `X : Y`, antithèses `X, non Y`, faux-ami *formalité* | reformuler ; remplacer *formalité* par « formalisation » / « formalisme »
- `13-synthese-deux-axes.md:3,15,122,149` | `[Ponctuation]` | tirets cadratins (`—,`) | rythme anglais | deux-points (3), parenthèses ou virgules
- `13-synthese-deux-axes.md:17,31` | `[Tableau | Légende]` | en-têtes à deux-points (`Erreur signalée : …`) ; légende `Dynamique de la matrice à deux axes : croisement…` | style deux-points | parenthèses ou phrase suivie
- `13-synthese-deux-axes.md:49` | `[Syntaxe]` | « Ce que la formalisation modifie, à l’intérieur d’un cadre donné, est la colonne » | clivée *What… changes is…* | « À l’intérieur d’un cadre donné, la formalisation agit sur la colonne »
- `13-synthese-deux-axes.md:51,120` | `[Syntaxe]` | « Sous ces hypothèses » / « sous les conditions de » | *under* | « Dans ces hypothèses » / « aux conditions de »
- `13-synthese-deux-axes.md:58,63,72,106,108,164` | `[Syntaxe]` | « vos propres contrôles » | *your own checks* | « les contrôles personnels [de qui produit ou utilise l’affirmation] »
- `13-synthese-deux-axes.md:72,106,110` | `[Lexique]` | « Effacés par défaut » / « l’effacement par défaut » / « disparaît par défaut » | *by default* | « Effacés d’emblée [ou spontanément] » / « l’effacement spontané » / « disparaît de lui-même »
- `13-synthese-deux-axes.md:99` | `[Lexique]` | « se fondre sans couture » | *blend seamlessly* | « se fondre imperceptiblement [ou sans rupture apparente] »
- `13-synthese-deux-axes.md:116` | `[Lexique]` | « attrape les erreurs hasardées » | *catches* | « intercepte [ou détecte] les erreurs hasardées »
- `13-synthese-deux-axes.md:124` | `[Syntaxe]` | « rien de fondamental n’a accéléré » | ergatif *has sped up* | « rien de fondamental ne s’est accéléré »

---

### Partie IV (`partie-4.md`, ch. 14–16)

#### `monographie/parties/partie-4.md`
- `partie-4.md:3` | `[Syntaxe]` | « elle rend corrélés ceux qui restent » | *makes the remaining ones correlated* | « elle corrèle ceux qui restent »
- `partie-4.md:5` | `[Syntaxe]` | « ne touchent pas un facteur omis » | *do not touch* | « laissent intact un facteur omis »
- `partie-4.md:7` | `[Syntaxe]` | « expose à deux pièges » | *exposes [one] to* | « comporte deux pièges »
- `partie-4.md:9` | `[Lexique | Syntaxe]` | « attrape les erreurs » / « s’entraînent sur elles » | *catches* / *train on them* | « intercepte les fautes » / « sont entraînés à partir d’elles »

#### `monographie/chapitres/14-chaines-qui-agissent.md`
- `14-chaines-qui-agissent.md:3` | `[Lexique]` | « la couche la moins garantie » | *least-guaranteed layer* | « la couche qui offre le moins de garanties »
- `14-chaines-qui-agissent.md:5,20,26,32,42,54` | `[Titre]` | titres à deux-points (`Les agents : quand…`, `Un danger structurel : …`, `Un danger opérationnel : …`, `L’action automatisée… : Knight Capital`), empilements nominaux (`Des pipelines d’IA…`, `Trajectoire d’agent…`) | moule `X : Y` + empilements | reformuler avec prépositions et verbes
- `14-chaines-qui-agissent.md:9..131` | `[Ponctuation]` | 21 tirets cadratins (dont 8 séquences `—,`) | rythme anglais | parenthèses, virgules ou relatives
- `14-chaines-qui-agissent.md:11` | `[Lexique]` | « ce litige client » | *customer dispute* | « ce litige avec un client »
- `14-chaines-qui-agissent.md:16` | `[Lexique]` | « consomme la sortie de la précédente » | *consumes the output* | « reçoit [ou absorbe] la sortie de la précédente »
- `14-chaines-qui-agissent.md:30` | `[Lexique]` | « modifier un test pour qu’il passe » | *so that it passes* | « modifier un test pour qu’il réussisse »
- `14-chaines-qui-agissent.md:36` | `[Syntaxe]` | « d’outils qui écrivent et déclenchent » | *tools that write and trigger* | « d’outils capables d’écrire et de déclencher des opérations »
- `14-chaines-qui-agissent.md:43` | `[Lexique]` | « exécuta ce comportement défectueux » | *executed this faulty behavior* | « exécuta ce code défectueux »
- `14-chaines-qui-agissent.md:58` | `[Lexique]` | « manque chaque erreur locale » | *misses each local error* | « laisse passer chaque erreur locale »
- `14-chaines-qui-agissent.md:62` | `[Légende]` | « en bleu, chaque étape contrôlée en parallèle par un pair » + ellipse devant $p = 6\,\%$ | ellipse sans article ni verbe | « en bleu, la trajectoire dont chaque étape est contrôlée en parallèle par un contrôleur » (harmoniser *pair* / *contrôleur* avec ch. 8)
- `14-chaines-qui-agissent.md:92,94` | `[Lexique]` | « ramène une poignée de passages » (*brings back*) / « ne porte aucune cicatrice » (*bears no scar*) | calques | « extrait quelques passages » / « ne porte aucune trace de son élaboration »
- `14-chaines-qui-agissent.md:110` | `[Lexique]` | « acheté… en *dépensant* ces garanties préalables » | *bought… by spending* | « acquis… au prix de ces garanties préalables »
- `14-chaines-qui-agissent.md:117` | `[Lexique]` | « modifie une base vivante » | *live database* | « modifie une base en production »

#### `monographie/chapitres/15-erosion-verifications.md`
- `15-erosion-verifications.md:3` | `[Lexique]` | « s’effacent par défaut » | *vanish by default* | « s’effacent spontanément [ou d’eux-mêmes] »
- `15-erosion-verifications.md:5,22,90,102` | `[Titre | Lexique]` | « La friction fabriquait des comparateurs » (contre *frottement* l. 9, 30) | *friction* | harmoniser sur « Le frottement »
- `15-erosion-verifications.md:16` | `[Syntaxe]` | « un code fonctionnel » | *working code* | « du code fonctionnel »
- `15-erosion-verifications.md:16..90` | `[Ponctuation]` | 16 tirets cadratins (dont `—,`) | rythme anglais | parenthèses ou virgules
- `15-erosion-verifications.md:32` | `[Titre]` | « Mesure contre impression : l’essai randomisé de METR » | *Measurement vs. Impression: …* | « La mesure contre l’impression dans l’essai randomisé de METR »
- `15-erosion-verifications.md:35` | `[Syntaxe]` | « ont pris en moyenne environ 19 % de temps de plus » | *took 19% more time* | « ont demandé environ 19 % de temps supplémentaire »
- `15-erosion-verifications.md:38` | `[Lexique]` | « contre une ligne de base définie à l’avance » | *against a baseline* | « par rapport à un niveau de référence défini à l’avance »
- `15-erosion-verifications.md:44,90` | `[Lexique]` | « passe quelques cas simples » / « doivent passer ou casser » | *pass or break* | « réussit sur quelques cas simples » / « doivent réussir ou mettre le résultat en défaut »
- `15-erosion-verifications.md:46` | `[Lexique]` | « improvisant le raisonnement métier » | *business reasoning* | « improvisant la logique du domaine »
- `15-erosion-verifications.md:48` | `[Lexique]` | « cessé d’échouer lorsque le fond s’effondre » / « Dans les termes de la @sec:… » | *stopped failing* / *In the terms of* | « cessé de trahir les lacunes » / « Au sens de la @sec:… »
- `15-erosion-verifications.md:59,84,103` | `[Syntaxe]` | rupture de sujet sur infinitive (`sans posséder`, l. 59) ; double `sur` + anacoluthe sur `maintenir` (l. 84) ; participe présent flottant `imposant de mesurer` (l. 103) | syntaxe calquée | rétablir les subordonnées ou sujets explicites
- `15-erosion-verifications.md:75,77,81,106` | `[Lexique]` | « L’humain / un humain » (contre *une personne* l. 3, 88) | *the human / a human* | harmoniser sur « la personne » / « l’opérateur humain »
- `15-erosion-verifications.md:79` | `[Lexique]` | « vis-à-vis de ce que le cadre… » | *vis-à-vis* | « face à ce que le cadre… »
- `15-erosion-verifications.md:83` | `[Lexique]` | « contrôle qu’il tient » | *check that it holds* | « contrôle qu’il reste valable »
- `15-erosion-verifications.md:103` | `[Lexique]` | « En délivrant toutes ses réponses… » | *By delivering* | « En présentant toutes ses réponses… »

#### `monographie/chapitres/16-angles-morts-collectifs.md`
- `16-angles-morts-collectifs.md:3,74` | `[Syntaxe]` | « les mêmes quelques modèles » | *the same few models* | « un même petit nombre de modèles »
- `16-angles-morts-collectifs.md:7` | `[Syntaxe]` | « maintenir nettement séparés les deux facteurs » | *keep separated* | « distinguer nettement les deux facteurs »
- `16-angles-morts-collectifs.md:20..119` | `[Ponctuation]` | 14 tirets cadratins (dont `—,`) | rythme anglais | parenthèses ou virgules
- `16-angles-morts-collectifs.md:26` | `[Titre]` | `Modèle partagé, précision…` | empilement nominal sans article | reformuler avec articles
- `16-angles-morts-collectifs.md:34` | `[Légende]` | « Les barres orange supposent les alertes suivies… ; les barres bleues supposent chaque alerte examinée » + « percer le plancher d’examen complet » | participiale réduite + sujet inanimé | « Les barres orange correspondent à l’hypothèse où les alertes sont suivies… » + « passer sous le plancher de 68,0 % correspondant à l’examen complet »
- `16-angles-morts-collectifs.md:41,43` | `[Lexique]` | « par vraie erreur attrapée » | *true error caught* | « par vraie erreur interceptée [ou détectée] »
- `16-angles-morts-collectifs.md:49` | `[Lexique]` | « Un producteur cinq fois plus exact » | *five times more accurate* | « Un producteur cinq fois plus fiable » (ou « qui commet cinq fois moins d’erreurs »)
- `16-angles-morts-collectifs.md:53` | `[Syntaxe]` | « une part conditionnelle aux erreurs restantes » | *conditional on* | « une part conditionnée aux erreurs restantes »
- `16-angles-morts-collectifs.md:74` | `[Lexique]` | « des corpus largement chevauchants » | *largely overlapping* | « des corpus qui se chevauchent largement »
- `16-angles-morts-collectifs.md:100` | `[Syntaxe | Lexique]` | « coûte ce qu’il a toujours coûté » / « des connaissances de domaine » | *costs what it has always cost* / *domain knowledge* | « coûte toujours autant qu’auparavant » / « des connaissances du domaine »
- `16-angles-morts-collectifs.md:104` | `[Syntaxe]` | « remonter la provenance » | *trace the provenance* | « remonter à la provenance »
- `16-angles-morts-collectifs.md:120` | `[Lexique]` | « les incitations centrées sur le débit » | *throughput-centered* | « les incitations qui récompensent le débit »

---

### Partie V (`partie-5.md`, ch. 17–18) et Conclusion (`99-conclusion.md`)

#### `monographie/parties/partie-5.md`
- `partie-5.md:3` | `[Syntaxe]` | « ce que la @sec:partie-2 a montré impossible » | *showed impossible* | « ce que la @sec:partie-2 a montré être impossible »
- `partie-5.md:7` | `[Lexique]` | « avant d’agir sur une affirmation » | *act on a claim* | « avant d’agir d’après une affirmation »

#### `monographie/chapitres/17-decisions-sans-appel.md` (et `tableaux/ch17-decisions.md`)
- `17-decisions-sans-appel.md:5,34,57,147` | `[Titre]` | « La course à la voile revisitée » (*revisited*, 5), `Modèle M2 : …` (34), « Décider sur ce que l’on croit… » (57), « Recevoir un chiffre assuré : quatre questions » (147) | calques titulaires | « Retour sur la course à la voile », « Décider d’après… », « Quatre questions devant un chiffre assuré »
- `17-decisions-sans-appel.md:15,23,66,76,90` (+ `tableaux/ch17-decisions.md:1,10`) | `[Lexique | Légende]` | « décide sur $p$ » / « prise sur $p + b$ » / « grandeur sur laquelle on décide » | *decide on* | « décide d’après $p$ » / « probabilité retenue $p + b$ »
- `17-decisions-sans-appel.md:64,97` | `[Ponctuation]` | incises à tirets cadratins (dont `—,`) | rythme anglais | parenthèses ou virgules
- `17-decisions-sans-appel.md:113` | `[Lexique]` | « pour *cette* instance » (*this instance*) / « tomber parmi les rares échecs » (*fall among*) | calques | « pour *ce* cas particulier » / « figurer parmi les rares échecs »
- `17-decisions-sans-appel.md:121` | `[Lexique]` | « se lit à travers les cinq conditions » | *is read through* | « s’analyse à la lumière des cinq conditions »
- `17-decisions-sans-appel.md:130` | `[Lexique]` | « tient ensemble deux idées » | *hold two ideas together* | « articule [ou concilie] deux idées »
- `17-decisions-sans-appel.md:136` | `[Lexique]` | « lorsqu’il est lui-même calculatoire » | *computational* | « lorsqu’il est lui-même informatique [ou numérique] »
- `17-decisions-sans-appel.md:140` | `[Lexique]` | « base de données vivante » (*live database*) / « à bas coût » (*at low cost*) | calques | « base de données en production » / « à peu de frais »
- `17-decisions-sans-appel.md:155` | `[Lexique]` | « Sous quelles conditions ce chiffre tient-il ? » | *Under what conditions does it hold?* | « À quelles conditions ce chiffre vaut-il ? »
- `17-decisions-sans-appel.md:160` | `[Lexique]` | « note l’abstention comme une erreur » | *scores… as an error* | « compte l’abstention comme une erreur »
- `17-decisions-sans-appel.md:166` | `[Lexique]` | « soutenir une décision irréversible » | *support a decision* | « fonder [ou étayer] une décision irréversible »

#### `monographie/chapitres/18-remede-trois-niveaux.md`
- `18-remede-trois-niveaux.md:3,148,180` | `[Titre | Lexique]` | « avant d’agir sur une affirmation » | *act on a claim* | « avant d’agir d’après une affirmation »
- `18-remede-trois-niveaux.md:5,37,80` | `[Titre]` | `Niveau 1 — L’attitude : …`, `Niveau 2 — Le placement : où, qui, quoi et combien`, `Niveau 3 — L’organisation : …` | moule `Level N — X: Y` | « Premier / Deuxième / Troisième niveau : … »
- `18-remede-trois-niveaux.md:13` | `[Titre]` | « Se donner une attente… » | *set oneself an expectation* | « Formuler une attente… »
- `18-remede-trois-niveaux.md:35` | `[Lexique]` | « se heurte aussi aux incitations » / « ne tient dans la durée » | *runs into* / *holds over time* | « se heurte au jeu des incitations » / « ne se maintient dans la durée »
- `18-remede-trois-niveaux.md:43,49,57,66` | `[Titre]` | `Où : …`, `Qui : …`, `Quoi : …`, `Combien : …` | fragments à deux-points | « Où placer le contrôle : … », « À qui le confier : … », etc.
- `18-remede-trois-niveaux.md:49,53,55,131,143,177` | `[Lexique]` | « le niveau situé dessous » / « sous cette interface » | *the level below* | « le niveau sous-jacent » (déjà utilisé l. 90, 158)
- `18-remede-trois-niveaux.md:61` | `[Lexique]` | « automatisé autour de la tâche » | *around the task* | « automatisé pour la tâche »
- `18-remede-trois-niveaux.md:70` | `[Syntaxe]` | « une conséquence de flux » | *a flow consequence* | « une conséquence sur les flux »
- `18-remede-trois-niveaux.md:72,116,126` | `[Titre]` | titres à deux-points (72, 116) ; `Ce que mesurent — et ce que manquent — les erreurs injectées` (126) | moule `X : Y` + tirets + *miss* | reformuler sans tirets ni *manquer* (« ce qui leur échappe »)
- `18-remede-trois-niveaux.md:76,156` | `[Lexique]` | « Lue avec les catégories… » / « au point d’usage » | *Read with* / *at the point of use* | « Lue à la lumière des catégories… » / « au moment de la décision »
- `18-remede-trois-niveaux.md:78` | `[Lexique]` | « soutient la phrase à laquelle il est accroché » | *supports… attached to* | « étaye l’énoncé auquel il est associé »
- `18-remede-trois-niveaux.md:131` | `[Lexique]` | « théâtre de conformité » | *compliance theater* | « simulacre de conformité »
- `18-remede-trois-niveaux.md:136,150` | `[Lexique]` | « ne tient à lui seul les cinq conditions » / « sous quelles conditions tient-il » | *hold* | « ne remplit à lui seul… » / « à quelles conditions vaut-il »
- `18-remede-trois-niveaux.md:152` | `[Syntaxe]` | « Avant de transformer une affirmation […], cinq autres questions portent sur… » | rupture de sujet sous l’infinitif | « Avant de transformer une affirmation […], il faut poser cinq autres questions sur… »

#### `monographie/chapitres/99-conclusion.md`
- `99-conclusion.md:1,71` | `[Titre]` | `# Conclusion : la méthode appliquée à elle-même` ; `### Le sens de variation du produit entre taux d’erreur et échappement reste à mesurer` | « produit *entre* A et B » + omission d’articles | « produit *du* taux d’erreur *par* la probabilité d’échappement »
- `99-conclusion.md:14,28,95,148` | `[Lexique]` | « attrapent des défauts » / « attraper les erreurs » | *catch* | « décèlent » / « interceptent »
- `99-conclusion.md:19,61,95` | `[Syntaxe]` | « conditionnent… sur les variables » | *condition on* | « dépendent de… » / « ne sont conditionnés que par… »
- `99-conclusion.md:27,85` | `[Lexique]` | « autour d’une tâche bornée » / « spécifié autour d’un composant appris » | *around* | « pour une tâche bornée » / « qui encadre un composant appris »
- `99-conclusion.md:39,55,146` | `[Ponctuation]` | incises à tirets cadratins (dont `—,`) | rythme anglais | parenthèses ou virgules
- `99-conclusion.md:49` | `[Lexique]` | « l’objection ne mord pas » | *doesn’t bite* | « l’objection reste sans prise »
- `99-conclusion.md:55` | `[Lexique]` | « tire donc contre la comparabilité » | *pulls against* | « joue contre » / « s’oppose à »
- `99-conclusion.md:61,129` | `[Lexique]` | « tient strictement » / « Sous quelles conditions tient-il ? » | *holds* | « vaut strictement » / « À quelles conditions vaut-il ? »
- `99-conclusion.md:107` | `[Syntaxe]` | « objecter aux formulations » (+ coquille « et on la rappelle ici ») | *object to* | « contester les formulations »
- `99-conclusion.md:109` | `[Lexique]` | « aident contre les erreurs » | *help against* | « prémunissent contre »
- `99-conclusion.md:119` | `[Lexique]` | « accrochée à une phrase… la soutienne » | *attached to… supports* | « associée à une phrase… l’étaye »
- `99-conclusion.md:134` | `[Syntaxe]` | « dans ou hors du cadre » | *inside or outside the frame* | « dans le cadre ou hors du cadre »
- `99-conclusion.md:146` | `[Lexique]` | « proposition définitionnelle » | *definitional* | « proposition de nature définitionnelle » (ou « quasi définitionnelle »)

---

## 5. Inventaire détaillé : figures, tableaux, annexes et registre

### A. Scripts de figures (`monographie/scripts/fig_*.py`)

*(Aucun calque repéré dans `fig_ch02_cible_monde_action.py`, `fig_ch05_trois_incertitudes.py`, `fig_ch07_cause_commune.py` et `fig_score_log.py`.)*

- **`scripts/fig_ch00_carte_ouvrage.py` :**
  - `:32` | « 3 incertitudes ; barre = désaccord » → « les 3 incertitudes ; une barre mesure le désaccord »
  - `:33` | « Comparateur et 5 conditions » → « Comparateur et les 5 conditions »
  - `:34` | « Cadre : cause commune » → « Le cadre comme cause commune »
  - `:35` | « Chaînes, croisés, blanchiment » → « Chaînes, contrôles croisés, blanchiment »
  - `:45` | « Composants appris : portée contre garantie » → « Composants appris, la portée au prix de la garantie »
  - `:46` | « frontière et longue traîne » → troncation du terme du registre *frontière en dents de scie*
  - `:55` | « Chaînes et agents : l’erreur passe à l’acte » → « Chaînes et agents, quand l’erreur passe à l’acte »
  - `:62` | « Partie V — Décider et se prémunir (chapitres 17 et 18) & Conclusion » → remplacer `&` par `et`
  - `:65-66` | « Décisions sans appel : … » / « Remède à 3 niveaux : … » → supprimer les deux-points télégraphiques

- **`scripts/fig_ch00_serie_parallele.py` :**
  - `:18,55` | tirets cadratins dans les titres de panneaux `(a) … — …` et `(b) … — …` → virgules
  - `:50` | « Angle mort global = réunion des angles morts de chaque maillon + erreurs nées aux interfaces » → « L’angle mort global réunit les angles morts de chaque maillon et les erreurs nées aux interfaces »
  - `:89` | « Angle mort résiduel = intersection des seuls angles morts partagés (comparaison et prise en compte) » → « L’angle mort résiduel se réduit aux seuls angles morts partagés (sous réserve de comparaison et de prise en compte) »

- **`scripts/fig_ch05_ferrure_marge.py` :**
  - `:45` | « Perte hors modèle : corrosion par piqûres / sous contrainte » → « Perte ignorée par le modèle : corrosion par piqûres ou sous contrainte »

- **`scripts/fig_ch06_cinq_conditions.py` :**
  - `:41` | « 4. À temps » (discordant avec `fig_ch18_trois_niveaux.py:20` et la légende `06:53`) → « 4. Arrivée\nà temps »
  - `:42` | « reçu + droit\nd’agir » → « signal reçu et\nautorité pour agir »
  - `:80` | « l’erreur passe avec échappement = 100 %. » → « l’erreur passe avec une probabilité d’échappement de 100 %. »

- **`scripts/fig_ch13_deux_axes.py` :**
  - `:16,18` | « (un comparateur contredit) » ; « (rien ne contredit — défaillances lourdes) » → « (un comparateur la contredit) » ; « (rien ne la contredit ; défaillances majeures) »
  - `:31` | « réponses dispersées sur devinette » → « réponses dispersées quand le modèle devine »
  - `:34` | « → peuplée par les composants appris ; vidable à l’avance si spécifié » → « → alimentée par les composants appris ; éliminable à l’avance si le composant est spécifié »
  - `:40` | « (crise 2008, …) » → « (crise de 2008, …) »
  - `:55` | « (change la colonne) » → « (ce qui fait changer de colonne) »

- **`scripts/fig_ch18_trois_niveaux.py` :**
  - `:38` | « couche dessous » et « ancrage documentaire (RAG) » → « couche sous-jacente » ; franciser ou mettre en italique *RAG*
  - `:41` | « capacité nommée » (*named capacity*) → « capacité dédiée » ou « poste désigné »
  - `:76` | « Historique et erreurs injectées (niveau 3) : mesurent… » → supprimer les deux-points entre sujet et verbe

- **`scripts/fig_chaine.py` :**
  - `:25` | « N = {n_cle} : facteur partagé = {pct(r["part_q"])} des défaillances restantes » → « À N = {n_cle}, le facteur partagé explique {pct(r["part_q"])} des défaillances restantes »
  - `:35` | « erreur par étape p = … » → « probabilité d’erreur par étape p = … »

- **`scripts/fig_echappement.py` :**
  - `:22` | « Oubli sur les autres erreurs m » → « Taux d’oubli des autres erreurs m »
  - `:25` | « Alertes qui sont de vraies erreurs (VPP) » → « Proportion de vraies erreurs parmi les alertes (VPP) »
  - `:26` | « Alertes par vraie erreur attrapée (1/VPP) » → « Alertes par vraie erreur détectée (1/VPP) »
  - `:51,81` | « risque : erreurs suivies d’effet » → « risque (erreurs suivies d’effet) »
  - `:64` | « …pour comparaison. » → « …à titre de comparaison. »
  - `:69` (`commun/parametres.py:98,100`) | « Un modèle pour tous » (*One model for all*) et « Indépendant et précis » → « Contrôleur indépendant et précis » (et reformuler « Un modèle pour tous »)

- **`scripts/fig_plausibilite.py` :**
  - `:28` | « alerte sur bonne réponse : … » → « fausse alerte si la réponse est juste : … » (et mentionner « 5 tirages » comme dans `12:123`)

- **`scripts/fig_seu.py` :**
  - `:79` | « (p + b) / p∗ : ce sur quoi l’on décide, rapporté au seuil » → « (p + b) / p∗ (probabilité retenue pour décider, rapportée au seuil) »
  - `:80` | « risque réel / p∗ : ce que le monde réserve » → « risque réel / p∗ (ce que le monde réserve) »
  - `:97,98` | « On décide sur p + b » ; « Décider sur ce que l’on croit… » → « Probabilité retenue (p + b) » ; « Décider d’après ce que l’on croit… »

---

### B. Tableaux générés (`monographie/tableaux/*.md`)

*(Aucun calque dans `ch03-score-log.md`.)*

- `tableaux/ch01-bayes-cotes.md:8` : « (normal dans 25 %) » / « (normal dans 85 %) » → « (et un signal normal dans 25 % des cas) »
- `tableaux/ch04-seuil.md:1` : « p estimé » → « Probabilité estimée p »
- `tableaux/ch08-chaine.md:1` et `tableaux/ch14-chaine-agent.md:1` : « Part indépendante (sans → avec contrôle) » → « Part des erreurs indépendantes (sans contrôle → avec contrôle) »
- `tableaux/ch09-echappement.md:1,5,8,9,10-13,16` et `tableaux/ch16-modele-partage.md:1,5,8,9,10-13,16` : « Indépendant et précis », « Oubli sur les autres erreurs m », « Alertes qui sont de vraies erreurs (VPP) », « Alertes par vraie erreur attrapée », « Échappement, alertes suivies… », « Quand producteur et contrôleur… : corrélation et fausses alertes. »
- `tableaux/ch09-taux-echappement.md:6` : « peut former le système le plus risqué » → « peut donner le système le plus risqué »
- `tableaux/ch12-plausibilite.md:1,7` : en-têtes « Réponse fausse », « Alerte à tort » ; légende infinitive « Reposer 5 fois la même question. Sévérité : … ; alerte à tort : … »
- `tableaux/ch17-decisions.md:1,10` : « On décide sur p + b », « Décider sur ce que l’on croit… » → « Probabilité retenue (p + b) », « Décider d’après ce que l’on croit… »
- `tableaux/ch17-scenarios.md:1` : « Ce que l’on pense p » → « Probabilité estimée p »

---

### C. Annexes (`monographie/annexes/*.md`) et registre (`registre_termes.md`)

- **`annexes/A-outils.md` :**
  - `:23` | « observé à la valeur $x$ […] décomposer la prévision […] s’écrit » → « dont la valeur observée est $x$ […], la décomposition de la prévision […] s’écrit »
  - `:43` | « d’occurrence *a priori* » → « de fréquence *a priori* »
  - `:69` | « avec probabilité estimée $p$ » → « avec une probabilité estimée $p$ »
  - `:81` | « décision prise sur $p + b$ » → « décision fondée sur $p + b$ »
  - `:100` | « on conditionne sur la valeur observée » + « — (1)…, (2)…, et (3)… —, » → « on conditionne à la valeur observée » + virgules/parenthèses
  - `:114` | « sur la classe $E_k$ » → « pour la classe $E_k$ »
  - `:132` | « au taux d’erreur $P(E)$ » → « avec un taux d’erreur $P(E)$ »
  - `:136,140` | « sous examen systématique » → « lorsque chaque alerte est examinée systématiquement »

- **`annexes/D-parametres.md` :**
  - `:3` | « engendrés mécaniquement » → « générés automatiquement »
  - `:44,63,78,83,87,90,91,107-108,116` | en-têtes et libellés repris de `parametres.py` et des tableaux (`$p$ estimé`, `Part indépendante`, `sous appariement`, `Indépendant et précis`, `Oubli sur`, `attrapée`, `Désaccords producteur / relecteur`, `Produit taux d’erreur × échappement`, `Réponse fausse` / barre `|` dans la prose).
  - `:119` | « 6e date 10 % » (discordance mineure avec `tableaux/ch12-plausibilite.md:5` « une autre date 10 % »).

- **`commun/registre_termes.md` (répercuté dans `annexes/B-glossaire.md` et `annexes/C-notation.md`) :**
  - `:16,86` | colonne « Introduit » → « Chapitre d’introduction »
  - `:24` (`B-glossaire.md:155`) | « sous la prévision qui lui attribuait la probabilité Pr » → « selon la prévision qui lui attribuait la probabilité Pr »
  - `:100` (`C-notation.md:19`) | « taux d’oubli sur les autres erreurs » → « taux d’oubli des autres erreurs »
