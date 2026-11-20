# Rapport de vérification bibliographique et factuelle

**Objet :** Passe de vérification bibliographique et factuelle (Priorité `P5.1` de `monographie/notes/TODO_ETAT_ACTUEL.md` et § 5 de `monographie/notes/SYNTHESE_A_TRANCHER.md`).  
**Périmètre :** 3 balises `[@A-VERIFIER: ...]` en texte libre, 7 ensembles de vérifications factuelles (§ 5), et audit complet des 60 entrées candidates de `monographie/commun/biblio_a_verifier.bib` citées dans `monographie/chapitres/*.md` (ainsi que des citations transversales de `NOTES_*.md`).  
**Note :** Conformément au mandat, aucun fichier de chapitre ni aucun fichier `.bib` n’a été modifié directement ; le présent rapport fournit les entrées BibTeX prêtes à copier et les retouches textuelles exactes à appliquer.

---

## Synthèse exécutive

- **Balises `[@A-VERIFIER: ...]` (3/3 résolues) :**
  1. **Ch. 2 (`02-cadre.md:150`) :** résolue par `shanahan2016frame` (*Stanford Encyclopedia of Philosophy*, révision printemps 2016) ; affirmation exacte.
  2. **Ch. 5 (`05-trois-incertitudes.md:52`) :** résolue par `fcic2011` (*Financial Crisis Inquiry Report*, 2011) et `coval2009` (Coval, Jurek & Stafford, *JEP* 2009), avec `gerardi2008` en appui complémentaire ; le fond historique est exact, avec une recommandation mineure d’alignement entre la l. 49 et la l. 52 (point `S5`).
  3. **Ch. 11 (`11-regle-tiree-des-donnees.md:64`) :** **`[@moffatt2024]` ne peut pas remplacer directement** la balise pour l’incise sur la « déclaration ultérieure d’Air Canada », car la décision `2024 BCCRT 149` constate seulement l’absence de preuve technique au dossier (et non les commentaires ultérieurs de la compagnie dans la presse). Recommandation : supprimer l’incise non sourcée de presse ou l’étayer explicitement sur une source secondaire, et s’en tenir à ce qu’établit `[@moffatt2024]`.
- **Vérifications factuelles § 5 (7/7 vérifiées) :**
  - Des retouches textuelles ciblées et exactes sont recommandées sur **6 points** :
    1. *Mata v. Avianca* (ch. 0, ch. 11) : préciser que les sanctions ont visé **les avocats et leur cabinet** (`Levidow, Levidow & Oberman P.C.`).
    2. *Challenger* (ch. 5, ch. 6) : rectifier le décompte (**24** vols antérieurs au total, dont **23** documentés — **7** avec dommages et **16**, non 17, sans dommage — et **1** vol aux propulseurs non repêchés, STS-4) et distinguer **direction de la NASA** et **direction de Morton Thiokol**.
    3. *Mars Climate Orbiter* (ch. 8) : expliciter en une phrase la chaîne causale entre sous-estimation des impulsions d’un facteur 4,45 et trajectoire finale trop basse (~57 km).
    4. *Knight Capital* (ch. 14) : préciser l’oubli sur **1 des 8 serveurs** et la **réactivation du code dormant *Power Peg* par un indicateur réutilisé** pour harmoniser les l. 43 et 45.
    5. *Vénus vs. Mercure* (ch. 12) : remplacer « en moyenne *géométrique* » par « en moyenne *temporelle* » (l. 119) et ajouter la référence `stockman2019` (*Physics Today*, 2019).
    6. *Lean 4 / autoformalisation* (ch. 13) : distinguer *autoformalisation* (traduction formelle) et recherche d’ébauches de preuve, et adjoindre `wu2022` (Wu et al., NeurIPS 2022) à `demoura2021` (qui ne porte que sur Lean 4 et son noyau de confiance).
  - Pour l’étude *BCG* (`dellacqua2023`, ch. 11 et ch. 12), tous les chiffres sont conformes à la source primaire (avec nuance mineure possible « plus de 40 % » au lieu de « environ 40 % »).
- **Audit de `biblio_a_verifier.bib` (60 entrées, toutes citées) :**
  - **39** entrées **Verified Ready** (métadonnées exactes et affirmation conforme, sous réserve d’élargir certains champs `averifier` aux chapitres transversaux).
  - **17** entrées **Minor BibTeX metadata fix needed** (auteurs `and others` à développer pour `ouyang2022`, `sharma2023`, `lewis2020`, pagination manquante ou à affiner pour `christiano2017`, `hoare1969`, `dennett1984`, sous-titres/URL/dates/notes pour `korzybski1933`, `rogers1986`, `tufte1997`, `mayo2018`, `hume1748`, `savage1954`, `mco1999`, `nostalgebraist2020`, `ue2015tip`, prénom `McFowland III` dans `dellacqua2023`, année/ISBN pour `russell2021`).
  - **4** entrées **Claim mismatch / nuance requise** :
    - `pearl1988` : l’image littérale du « champ de mines » attribuée à Pearl au ch. 2 (`02-cadre.md:56`) n’a pas pu être attestée mot pour mot dans l’ouvrage original de 1988 par recherche documentaire ; à vérifier directement dans le texte imprimé ou à reformuler sans attribution littérale de la métaphore à Pearl.
    - `demoura2021` : cité au ch. 13 pour l’*autoformalisation* alors que l’article ne décrit que Lean 4 et son noyau (ajouter `wu2022`).
    - `mata2023` : les chapitres 0 et 11 omettent le cabinet d’avocats dans les sanctions.
    - `sec2013knight` : léger décalage rédactionnel au ch. 14 l. 43 (« laissa actif » vs l. 45 « code dormant réactivé »).

---

## Partie A — Résolution des 3 balises `[@A-VERIFIER: ...]`

### A.1. Chapitre 2 (`monographie/chapitres/02-cadre.md:150`) — Shanahan, « The Frame Problem », SEP

- **Passage actuel (`02-cadre.md:150`) :**
  > « Sous cette forme logique, la difficulté a reçu des réponses techniques `[@A-VERIFIER: Shanahan, « The Frame Problem », SEP]`. »
- **Vérification de l’affirmation :** Conforme. L’article de Murray Shanahan dans la *Stanford Encyclopedia of Philosophy* (publié le 23 février 2004, révision substantielle du 17 février 2016) retrace précisément les solutions logiques apportées au problème du cadre au sens étroit posé par McCarthy et Hayes (1969) — logiques non monotones, circonscription, calcul des situations et axiomes d’état successeur — tout en le distinguant du problème épistémologique plus large de la pertinence (Dennett, Fodor). Cette référence figure d’ailleurs déjà dans la bibliographie de l’article source de l’auteur (`source/frame_problem_article_WF.tex:1442`, `Shanahan2016`).
- **Remplacement dans le texte :** remplacer `[@A-VERIFIER: Shanahan, « The Frame Problem », SEP]` par `[@shanahan2016frame]`.
- **Entrée BibTeX prête à copier (dans `biblio.bib`) :**

```bibtex
@incollection{shanahan2016frame,
  author    = {Shanahan, Murray},
  title     = {The Frame Problem},
  booktitle = {The Stanford Encyclopedia of Philosophy},
  editor    = {Zalta, Edward N.},
  edition   = {Spring 2016},
  publisher = {Metaphysics Research Lab, Stanford University},
  year      = {2016},
  url       = {https://plato.stanford.edu/archives/spr2016/entries/frame-problem/}
}
```

---

### A.2. Chapitre 5 (`monographie/chapitres/05-trois-incertitudes.md:52`) — Modèles de risque hypothécaire et corrélation des défauts avant 2008

- **Passage actuel (`05-trois-incertitudes.md:49, 52–54`) :**
  - L. 49 : « Parce que le couplage généralisé entre marchés immobiliers régionaux ne figurait pas dans la structure retenue, un effondrement simultané n’apparaissait pas comme un scénario incertain : il n’apparaissait pas du tout. »
  - L. 52 (encadré `.cas`) : « Dans les années qui ont précédé la crise financière de 2008, les modèles statistiques chargés d’évaluer des portefeuilles de prêts hypothécaires titrisés reposaient sur les régularités observées au cours des décennies antérieures `[@A-VERIFIER: rapport ou étude sur les modèles de risque hypothécaire et la corrélation des défauts avant 2008]`. Dans ces séries passées, les baisses régionales des prix immobiliers étaient restées faiblement corrélées d’un État à l’autre, faute de baisse nationale dans la période observée. Tirée de cette histoire sans retournement généralisé, la quasi-indépendance avait été figée dans la structure même des modèles de portefeuille, au lieu d’y figurer comme un paramètre incertain. »
- **Vérification factuelle de l’encadré :** Exacte sur le fond historique et technique.
  - Le rapport final de la *Financial Crisis Inquiry Commission* (`fcic2011`, janvier 2011) documente explicitement que les modèles utilisés par les agences de notation et les banques pour noter les MBS et CDO reposaient sur des séries historiques récentes sans baisse nationale simultanée des prix immobiliers depuis la Grande Dépression ; ils présupposaient la diversification géographique (des pertes régionales devant être compensées par d’autres régions) et assignaient une probabilité quasi nulle à des défauts simultanés à l’échelle nationale.
  - Coval, Jurek & Stafford (`coval2009`, *Journal of Economic Perspectives*, 23(1), 2009) démontrent mathématiquement que la notation des tranches seniors (AAA) de produits structurés dépend de manière critique de deux paramètres traités comme connus avec précision : la probabilité de défaut et la **corrélation des défauts** entre actifs sous-jacents ; le tranchage amplifie considérablement l’erreur d’estimation dès que la corrélation réelle (liée à un choc macroéconomique national) dépasse l’hypothèse figée dans le modèle.
  - En complément, Gerardi, Lehnert, Sherlund & Willen (`gerardi2008`, *Brookings Papers on Economic Activity*, 39(2), 2008) confirment que les analystes connaissaient le lien mécanique entre chute des prix immobiliers et défauts, mais attribuaient une probabilité négligeable à une baisse nationale des prix au vu des séries récentes.
- **Vérification de la formulation (tension `S5` de `SYNTHESE_A_TRANCHER.md`) :**
  - La formulation actuelle de l’encadré (« la quasi-indépendance avait été figée dans la structure même des modèles de portefeuille, au lieu d’y figurer comme un paramètre incertain ») est fidèle aux sources. Pour éviter qu’un lecteur ne voie une contradiction entre « faiblement corrélées » (l. 52) et « le couplage généralisé [...] ne figurait pas dans la structure retenue » (l. 49), la l. 52 peut préciser que la corrélation régionale a été *calibrée à un niveau faible et figée sans facteur commun de retournement national*.
- **Remplacement dans le texte :** remplacer la balise `[@A-VERIFIER: ...]` à la l. 52 par `[@fcic2011; @coval2009]` (et optionnellement `@gerardi2008`), et reprendre `[@fcic2011; @coval2009]` dans les mentions rapides du cas aux chapitres 13 (l. 20 et 137) et 17 (l. 111) si l’on souhaite y conserver la citation directe.
- **Entrées BibTeX prêtes à copier (dans `biblio.bib`) :**

```bibtex
@techreport{fcic2011,
  author      = {{Financial Crisis Inquiry Commission}},
  title       = {The Financial Crisis Inquiry Report: Final Report of the National Commission on the Causes of the Financial and Economic Crisis in the United States},
  institution = {U.S. Government Printing Office},
  address     = {Washington, D.C.},
  year        = {2011},
  month       = jan,
  isbn        = {978-0-16-087983-8}
}

@article{coval2009,
  author  = {Coval, Joshua D. and Jurek, Jakub W. and Stafford, Erik},
  title   = {The Economics of Structured Finance},
  journal = {Journal of Economic Perspectives},
  volume  = {23},
  number  = {1},
  pages   = {3--25},
  year    = {2009},
  doi     = {10.1257/jep.23.1.3}
}
```

*(Entrée complémentaire optionnelle :)*
```bibtex
@article{gerardi2008,
  author  = {Gerardi, Kristopher and Lehnert, Andreas and Sherlund, Shane M. and Willen, Paul S.},
  title   = {Making Sense of the Subprime Crisis},
  journal = {Brookings Papers on Economic Activity},
  volume  = {39},
  number  = {2},
  pages   = {69--159},
  year    = {2008}
}
```

---

### A.3. Chapitre 11 (`monographie/chapitres/11-regle-tiree-des-donnees.md:64`) — Déclaration d’Air Canada (*Moffatt v. Air Canada*)

- **Passage actuel (`11-regle-tiree-des-donnees.md:64`) :**
  > « D’une part, aucune preuve technique relative au fonctionnement ou à l’architecture de cet assistant n’a été versée au dossier devant le tribunal `[@moffatt2024]` ; selon des déclarations ultérieures attribuées à la compagnie, l’outil aurait même été antérieur aux modèles génératifs actuels `[@A-VERIFIER: déclaration d’Air Canada (technologie antérieure)]`. »
- **Vérification par rapport à `moffatt2024` (`2024 BCCRT 149`, 14 février 2024) :**
  - **Est-ce que `[@moffatt2024]` peut remplacer directement la balise `[@A-VERIFIER: ...]` ? NON.**
  - La décision *Moffatt v. Air Canada*, 2024 BCCRT 149 (rendue par Christopher C. Rivers au Civil Resolution Tribunal de Colombie-Britannique le 14 février 2024) établit :
    1. qu’Air Canada n’a versé **aucune preuve technique** sur la nature, la programmation ou le fonctionnement de son agent conversationnel (`"no evidence"` sur son fonctionnement) ;
    2. que la compagnie a soutenu (en vain) que le chatbot était une entité juridique distincte et que le client aurait dû vérifier la page statique ;
    3. que l’entreprise est juridiquement responsable des informations affichées sur son site web, qu’elles proviennent d’une page statique ou d’un assistant interactif.
  - En revanche, l’affirmation selon laquelle l’assistant était basé sur des règles ou antérieur à l’IA générative provient uniquement de **commentaires de presse et d’analyses postérieurs au jugement** (février 2024, rapportés notamment dans des revues juridiques et médias spécialisés tels que *Best Lawyers* ou *National Magazine*), et non du texte même de `2024 BCCRT 149` — et aucune déclaration officielle datée et signée d’un porte-parole d’Air Canada citant ce point précis n’a pu être retracée directement dans une source primaire publique vérifiable.
- **Recommandation textuelle exacte (option propre et autosuffisante, conforme à `NOTES_11.md`) :**
  Supprimer la proposition secondaire non étayée sur les déclarations ultérieures, car la seule absence de preuve technique au dossier dans `[@moffatt2024]` suffit déjà pleinement à interdire de faire de l’affaire un témoignage sur les grands modèles de langage :
  - *Remplacement proposé à `11-regle-tiree-des-donnees.md:64` :*
    > « D’une part, aucune preuve technique relative au fonctionnement ou à l’architecture de cet assistant n’a été versée au dossier devant le tribunal `[@moffatt2024]`, de sorte que rien dans la décision n’établit qu’il se soit agi d’un grand modèle de langage génératif. L’épisode ne saurait donc servir de preuve sur le comportement d’un tel modèle ; à cet égard, *Mata v. Avianca* reste le cas documenté. »

---

## Partie B — Vérifications factuelles de `SYNTHESE_A_TRANCHER.md` § 5

### B.1. *Mata v. Avianca* (`mata2023`, ch. 0 et ch. 11)

- **Question :** Les sanctions visaient-elles les avocats, le cabinet, ou les deux ?
- **Constat vérifié :** Dans l’ordonnance de sanctions rendue le **22 juin 2023** par le juge P. Kevin Castel (*Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC), S.D.N.Y., 678 F. Supp. 3d 443), le tribunal a sanctionné **à la fois les deux avocats et leur cabinet** en vertu de la règle 11 (*Federal Rules of Civil Procedure*) :
  - **Steven A. Schwartz** (qui a utilisé ChatGPT pour la recherche et rédigé le mémoire),
  - **Peter LoDuca** (qui a signé et déposé le mémoire),
  - **Levidow, Levidow & Oberman P.C.** (leur cabinet), tous trois condamnés *solidairement* (*jointly and severally*) à une amende de 5 000 $, ainsi qu’à l’obligation d’adresser l’ordonnance et les faux arrêts au client Roberto Mata et aux juges fédéraux dont les noms avaient été utilisés.
- **Écart dans les chapitres :**
  - `00-cartographier.md:9` écrit : « ce qui valut **aux conseils** une amende et des sanctions en juin 2023 `[@mata2023]`. »
  - `11-regle-tiree-des-donnees.md:54` écrit : « En juin 2023, le tribunal prononça une amende et d’autres sanctions **contre les avocats concernés** `[@mata2023]`. »
- **Retouches recommandées :**
  - `00-cartographier.md:9` : remplacer « aux conseils » par « aux avocats et à leur cabinet ».
  - `11-regle-tiree-des-donnees.md:54` : remplacer « contre les avocats concernés » par « contre les avocats concernés et leur cabinet ».

---

### B.2. *Challenger* (`rogers1986`, `tufte1997`, ch. 5 et ch. 6)

- **Questions :** (1) Que désigne « la direction » (NASA vs Morton Thiokol) ? (2) Quel est le décompte exact des vols (7 vs 23/24) ?
- **Constats vérifiés :**
  1. **Direction NASA vs Morton Thiokol (`rogers1986`, vol. 1, ch. 5) :**
     - Lors de la téléconférence du 27 janvier 1986 au soir, les ingénieurs de Morton Thiokol (notamment Roger Boisjoly et Arnie Thompson) ont recommandé de ne pas lancer en dessous de 53 °F.
     - Ce sont d’abord les responsables de la **NASA** (notamment Lawrence Mulloy et George Hardy au Marshall Space Flight Center) qui ont contesté cette recommandation et inversé la charge de la preuve (« When do you want me to launch, next April? »).
     - Puis, lors d’une suspension de séance hors ligne (*caucus*), la **direction de Morton Thiokol** (Jerald Mason demandant au vice-président de l’ingénierie Robert Lund de « quitter sa casquette d’ingénieur pour mettre sa casquette de dirigeant ») a désavoué ses propres ingénieurs et émis un avis favorable au lancement, sur lequel la **direction de la NASA** a maintenu le tir.
  2. **Décompte des vols (`tufte1997`, ch. 2, « Visual and Statistical Thinking ») :**
     - Le vol *Challenger* (STS-51-L) était la 25^e^ mission de la navette : il y avait donc **24 vols antérieurs** au total.
     - Sur ces 24 vols antérieurs, **7** avaient présenté des dommages ou indices thermiques sur les joints toriques ; **16** vols documentés n’en présentaient pas ; et **1** vol (**STS-4**) avait eu ses propulseurs d’appoint perdus en mer sans récupération, si bien que l’état de ses joints était inconnu — soit **23 vols antérieurs documentés** (et non 17 vols « sans incident » documentés ; Tufte critique précisément que les tableaux d’origine aient parfois traité STS-4 comme indemne ou omis les vols sains).
- **Écarts dans les chapitres :**
  - `05-trois-incertitudes.md:119` et `06-detecter-une-erreur.md:112` écrivent tous deux : « ne montrait que les **sept** vols antérieurs [...] en laissant de côté les **dix-sept** vols [antérieurs] sans incident » (ce qui suppose 17 vols documentés sans dommage alors que l’un de ces 17 vols, STS-4, n’a pas permis de récupérer les propulseurs : seuls **16** vols sont documentés sans dommage, pour **23** vols documentés au total sur 24 lancements précédents). De même, `06-detecter-une-erreur.md:117` mentionne « les données des vingt-quatre vols antérieurs », alors que les données d’état des joints ne portent que sur **23** vols documentés (24 lancements antérieurs dont 1 aux propulseurs non repêchés).
  - `06-detecter-une-erreur.md:112` écrit : « **la direction** demanda aux ingénieurs de prouver que le lancement serait dangereux » sans distinguer NASA et Morton Thiokol alors que la l. 110 mentionne les responsables de la NASA et les ingénieurs de Morton Thiokol.
- **Retouches recommandées :**
  - `05-trois-incertitudes.md:119` et `06-detecter-une-erreur.md:112` : remplacer « les dix-sept vols [antérieurs] sans incident » par « les seize vols documentés sans dommage (un vingt-quatrième vol antérieur ayant perdu ses propulseurs en mer) », et écrire « l’ensemble des 23 vols antérieurs documentés ».
  - `06-detecter-une-erreur.md:117` : écrire « Les relevés de 23 des 24 vols antérieurs (les propulseurs d’un vol n’ayant pas été repêchés) et des essais existaient dans les archives `[@tufte1997]` ».
  - `06-detecter-une-erreur.md:112` : préciser « les responsables de la NASA contestèrent cette recommandation et demandèrent aux ingénieurs de prouver que le lancement serait dangereux ; après un aparté, la direction de Morton Thiokol écarta l’avis de ses propres ingénieurs, et le lancement fut maintenu par la NASA `[@rogers1986]`. »

---

### B.3. *Mars Climate Orbiter* (`mco1999`, ch. 0, ch. 8, ch. 10, ch. 12)

- **Questions (`SYNTHESE_A_TRANCHER.md` § 5) :**
  1. Le facteur 4,45 porte-t-il sur les impulsions du fichier `SM_FORCES` (`lbf·s` vs `N·s`) et non sur la trajectoire ?
  2. Les fichiers fautifs ont-ils été produits pendant le transit ?
  3. Des anomalies ont-elles été observées sans être formellement remontées, et convient-il de reformuler « sans alarme décisive » ?
  4. La chaîne causale entre l’erreur d’unités et la trajectoire trop basse est-elle dite au ch. 8 ?
- **Constats vérifiés (`Mars Climate Orbiter Mishap Investigation Board, Phase I Report`, 10 novembre 1999) :**
  1. **Objet du facteur 4,45 :** Le programme au sol `SM_FORCES` (Lockheed Martin) calculait l’impulsion ($\Delta V$ / impulsion totale) des poussées de désaturation de moment cinétique (*Angular Momentum Desaturation*, AMD) et l’écrivait dans des fichiers AMD en **livres-force-secondes** ($\text{lbf}\cdot\text{s}$) au lieu des **newton-secondes** ($\text{N}\cdot\text{s}$) imposés par le document d’interface (*Software Interface Specification*). Comme $1\;\text{lbf} \approx 4{,}448\;\text{N}$ (facteur $\approx 4{,}45$), le logiciel de navigation du JPL sous-estimait d’un facteur 4,45 **chaque impulsion** transmise dans ces fichiers.
  2. **Moment de production :** Le logiciel `SM_FORCES` avait été écrit avant le vol, mais les **fichiers de données AMD** étaient générés et transmis régulièrement **pendant les neuf mois et demi du transit** vers Mars (d’autant plus fréquemment que l’asymétrie des panneaux solaires imposait 10 à 14 fois plus d’événements AMD que prévu).
  3. **Anomalies non remontées :** L’équipe de navigation a bel et bien observé des écarts et une dérive inattendue de trajectoire en cours de transit, mais ces doutes ont été échangés de façon informelle (courriels) sans faire l’objet de fiches formelles d’anomalie (*Incident/Surprise/Anomaly*, ISA) ni d’escalade institutionnelle.
  4. **Chaîne causale vers la trajectoire trop basse :** Comme chaque poussée de désaturation était sous-estimée d’un facteur 4,45 dans le calcul de trajectoire, les écarts accumulés (et les manœuvres de correction fondées sur ces modèles erronés) ont fait dériver la trajectoire estimée par rapport à la trajectoire réelle : à l’arrivée, le 23 septembre 1999, la sonde a abordé Mars à une altitude d’environ 57 km au lieu des ~140–150 km sûrs (périapse initialement visé vers 226 km), et a été perdue dans l’atmosphère martienne.
- **Évaluation des chapitres actuels :**
  - `00-cartographier.md:7`, `10-couches-basses.md:107, 116, 118` et `12-autre-regime.md:22` sont déjà **exacts** sur les trois premiers points (facteur 4,45 sur les impulsions, production pendant le vol/transit, anomalies non instruites formellement, et `12-autre-regime.md:22` a déjà corrigé « sans alarme décisive » en « Aucune alarme n’a interrompu la mission »).
  - En revanche, **`08-independance-chaines.md:183–185` omet effectivement le chaînon causal** entre l’écart d’un facteur 4,45 sur les impulsions (l. 185) et la trajectoire trop basse (l. 183).
- **Retouche recommandée :**
  - Dans `08-independance-chaines.md:185`, ajouter après « d’un facteur proche de 4,45 `[@mco1999]`. » :
    > « En sous-estimant ainsi d’un facteur 4,45 l’effet réel de chaque petite poussée pendant tout le transit, le modèle de navigation laissa la trajectoire dériver progressivement jusqu’à engager la sonde trop bas dans l’atmosphère martienne `[@mco1999]`. »

---

### B.4. *Knight Capital* (`sec2013knight`, ch. 14)

- **Question :** Harmoniser « laissa actif en production un code dormant » (`14-chaines-qui-agissent.md:43`) et « le code dormant réactivé » (`14-chaines-qui-agissent.md:45`).
- **Constat vérifié (SEC Release No. 34-70694, 16 octobre 2013) :** Le 1^er^ août 2012, lors du déploiement du nouveau code RLP (*Retail Liquidity Program*) sur les huit serveurs de routage SMARS de Knight Capital, le technicien n’a copié la mise à jour que sur **sept des huit serveurs**, laissant l’ancien code sur le huitième. La mise à jour réutilisait un indicateur (*flag*) qui servait autrefois à une ancienne fonction de routage inutilisée depuis 2003 (*Power Peg*, code dormant dont le compteur d’arrêt avait été déplacé). Lorsque des ordres porteurs de cet indicateur réutilisé ont atteint le huitième serveur non mis à jour, ils ont **réactivé ce code dormant**, déclenchant en environ **45 minutes** plus de 4 millions d’exécutions sur 154 titres et une perte avant impôts supérieure à **460 millions de dollars** (~461,1 M$).
- **Retouche recommandée (`14-chaines-qui-agissent.md:43`) :**
  > « En 2012, lors du déploiement d’une mise à jour logicielle sur huit serveurs de routage d’ordres chez la société financière Knight Capital, une omission laissa l’ancienne version en production sur l’un des serveurs, où un indicateur réutilisé réactiva un code dormant `[@sec2013knight]`. »

---

### B.5. Étude du BCG (`dellacqua2023`, ch. 11 et ch. 12)

- **Question :** Vérifier les chiffres avancés (`+12,2 %` de tâches, `25,1 %` plus vite, `≈ 40 %` de qualité en plus dans la frontière ; `−19 points de pourcentage` hors frontière).
- **Constat vérifié (Dell’Acqua et al., Harvard Business School Working Paper 24-013, septembre 2023) :**
  - **758** consultants individuels du Boston Consulting Group (BCG) ont participé à l’expérience contrôlée randomisée avec GPT-4.
  - **À l’intérieur de la frontière technologique :** les consultants assistés par l’IA ont achevé **12,2 %** de tâches en plus, travaillé **25,1 %** plus vite, et produit des résultats jugés **de plus de 40 % supérieurs en qualité** (*more than 40% higher quality*) par rapport au groupe témoin.
  - **Au-delà de la frontière technologique :** sur la tâche conçue pour se situer juste hors de la frontière de compétence du modèle, les consultants assistés ont eu **19 points de pourcentage de moins** de chances de produire une solution correcte que ceux travaillant sans IA.
- **Évaluation des chapitres :** Exacte (`11-regle-tiree-des-donnees.md:36` et `12-autre-regime.md:47–49`). Ajustement cosmétique optionnel à `11-regle-tiree-des-donnees.md:36` : « plus de 40 % plus haut en qualité » au lieu de « environ 40 % plus haut en qualité » (la source écrit *over 40%* / *more than 40%*).

---

### B.6. Vénus vs. Mercure (`12-autre-regime.md:119, 134`)

- **Question (`SYNTHESE_A_TRANCHER.md` § 5 & `S8`) :** Vérifier l’affirmation selon laquelle Mercure est en moyenne la planète la plus proche de la Terre, et fournir une entrée BibTeX si utile.
- **Constat vérifié :** Tom Stockman, Gabriel Monroe et Samuel Cordner ont publié en mars 2019 dans *Physics Today* (« Venus is not Earth’s closest neighbor », vol. 72, n^o^ 3, p. 30–31, DOI `10.1063/PT.6.3.20190312a`) la démonstration par la méthode point-cercle (*point-circle method*) que **Mercure** — et non Vénus — est en **moyenne temporelle** (sur l’ensemble des configurations orbitales supposées circulaires, coplanaires et concentriques) la planète la plus proche de la Terre (et même de chacune des autres planètes du Système solaire). L’idée reçue vient de la confusion entre distance minimale au rapprochement (conjonction inférieure de Vénus) et distance moyenne dans le temps.
- **Défaut repéré à `12-autre-regime.md:119` :** Le texte actuel écrit :
  > « seulement 9 % à Mercure (qui, restant plus près du Soleil, demeure **en moyenne géométrique** sur l’ensemble des orbites la plus proche de la Terre, contrairement à l’idée reçue qui confond distance minimale au rapprochement et distance moyenne) »
  - En français mathématique, « moyenne géométrique » désigne $(\prod x_i)^{1/n}$, alors que Stockman et al. (2019) calculent une **moyenne temporelle** (ou simplement « en moyenne sur le temps et sur l’ensemble des orbites »).
- **Retouche recommandée (`12-autre-regime.md:119`) :**
  > « seulement 9 % à Mercure (qui, restant plus près du Soleil, demeure en moyenne temporelle sur l’ensemble des orbites la plus proche de la Terre `[@stockman2019]`, contrairement à l’idée reçue qui confond distance minimale au rapprochement et distance moyenne) »
- **Entrée BibTeX prête à copier (dans `biblio.bib`) :**

```bibtex
@article{stockman2019,
  author  = {Stockman, Tom and Monroe, Gabriel and Cordner, Samuel},
  title   = {Venus is not {Earth}'s closest neighbor},
  journal = {Physics Today},
  volume  = {72},
  number  = {3},
  pages   = {30--31},
  year    = {2019},
  month   = mar,
  doi     = {10.1063/PT.6.3.20190312a}
}
```

---

### B.7. Lean 4 et autoformalisation (`demoura2021`, `13-synthese-deux-axes.md:89, 101, 136`)

- **Question (`SYNTHESE_A_TRANCHER.md` § 5) :** Vérifier comment `demoura2021` est cité et si l’autoformalisation en Lean s’entend comme traduction d’une preuve ou comme recherche d’une preuve (ou nécessite une référence dédiée).
- **Constat vérifié :**
  1. **Portée de `demoura2021` :** L’article de Leonardo de Moura et Sebastian Ullrich (CADE 28, 2021, p. 625–635) décrit le langage et l’assistant de preuve **Lean 4**, son architecture extensible et son petit noyau de confiance fondé sur la théorie des types. Il **ne traite pas** de l’autoformalisation par grands modèles de langage.
  2. **Sens exact de l’*autoformalisation* :** Dans la littérature de référence — inaugurée pour les LLM par **Wu et al. (2022)**, « Autoformalization with Large Language Models », *Advances in Neural Information Processing Systems 35* (NeurIPS 2022), p. 32353–32368 —, l’*autoformalisation* désigne précisément la **traduction automatique** d’énoncés et de preuves en langue naturelle vers un langage formel vérifiable par un assistant de preuve (Isabelle/HOL, Lean, etc.), ce qui est distinct de la **recherche neuronale de preuves** (*neural theorem proving* / génération d’ébauches de démonstration), même si les deux s’enchaînent souvent en pratique.
  3. **Usage actuel au ch. 13 :**
     - L. 89 : « comme l’illustre ci-dessous la traduction automatique de preuves dans Lean `[@demoura2021]`. » -> `demoura2021` seul ne documente pas la traduction automatique.
     - L. 101 : « La traduction automatique d’un énoncé et d’une preuve vers un langage formel — ce que l’on nomme l’*autoformalisation* — dans un assistant de preuve tel que Lean 4 déplace radicalement ce point d’appui `[@demoura2021]`. L’architecture de Lean sépare l’outil qui cherche ou rédige la démonstration d’un *noyau de confiance* volontairement réduit [...] `[@demoura2021]`. » -> La 2^e^ phrase est parfaitement couverte par `demoura2021`, mais la 1^re^ mélange implicitement traduction formelle et recherche de preuves et cite `demoura2021` pour l’autoformalisation.
- **Retouches recommandées :**
  - Ajouter `wu2022` dans `biblio.bib` et le citer aux l. 89 et 101 pour l’autoformalisation, en conservant `[@demoura2021]` pour Lean 4 et le noyau de confiance :
    - L. 89 : « comme l’illustre ci-dessous l’autoformalisation et le contrôle de preuves dans Lean `[@wu2022; @demoura2021]`. »
    - L. 101 : « La traduction automatique d’un énoncé ou d’une preuve informelle vers un langage formel — l’*autoformalisation* `[@wu2022]` —, associée à la génération de tentatives de démonstration dans un assistant de preuve tel que Lean 4 `[@demoura2021]`, déplace radicalement ce point d’appui. »
- **Entrée BibTeX prête à copier (dans `biblio.bib`) :**

```bibtex
@inproceedings{wu2022,
  author    = {Wu, Yuhuai and Jiang, Albert Q. and Li, Wenda and Rabe, Markus N. and Staats, Charles and Jamnik, Mateja and Szegedy, Christian},
  title     = {Autoformalization with Large Language Models},
  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS 2022)},
  pages     = {32353--32368},
  year      = {2022}
}
```

---

## Partie C — Audit complet de `monographie/commun/biblio_a_verifier.bib`

Toutes les **60** clés de `biblio_a_verifier.bib` sont effectivement citées dans `monographie/chapitres/*.md` (aucune clé orpheline). Le tableau ci-dessous audite chaque entrée sur deux axes : **exactitude des métadonnées BibTeX** (auteurs, titre, revue/éditeur, année, pages) et **adéquation de l’affirmation** dans les chapitres citant la clé.

**Légende des statuts :**
- **Verified Ready** : métadonnées exactes (ou complètes pour l’usage bibliographique) et toutes les citations dans les chapitres correspondent à la source. *(Note : pour plusieurs clés citées dans de nouveaux chapitres ou dans la conclusion, penser à mettre à jour le champ interne `averifier` ou à le retirer lors du transfert vers `biblio.bib`.)*
- **Minor BibTeX metadata fix needed** : source et affirmation vérifiées, mais l’entrée BibTeX demande un complément ou une correction (auteurs complets, pagination, sous-titre, édition, URL, n° de décision).
- **Claim mismatch** : écart ou imprécision relevé entre le texte du chapitre et la source primaire (détaillé en Partie B ou dans la colonne *Observations*).

| Clé | Chapitres citant | Statut | Observations et corrections requises |
| :--- | :--- | :--- | :--- |
| `mccarthy1969` | ch. 2, 12 | **Verified Ready** | McCarthy & Hayes (1969), *Machine Intelligence 4*, pp. 463–502 : exact. Origine du problème du cadre (ch. 2, 12) conforme. |
| `dennett1984` | ch. 2, 12 | **Minor BibTeX metadata fix needed** | Cambridge University Press 1984 : pagination parfois référencée `129--150` (`frame_problem_article_WF.tex`), `129--151` (`biblio_a_verifier.bib`) ou `129--152` selon l’édition/notice CUP ; vérifier l’exemplaire retenu. Les trois robots (R1, R1D1, R2D1) et la bombe sur le chariot sont conformes. |
| `korzybski1933` | ch. 2 | **Minor BibTeX metadata fix needed** | Compléter le titre : *Science and Sanity: An Introduction to Non-Aristotelian Systems and General Semantics* (p. 58 : « A map is not the territory it represents... »). Usage ch. 2 conforme. |
| `pearl1988` | ch. 2 | **Claim mismatch** | Métadonnée : compléter le sous-titre (*Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*). **Point d’attention sur l’affirmation (`02-cadre.md:56`) :** Pearl (1988, ch. 10) analyse les règles par défaut à exceptions (*birds fly*, *smoke suggests fire*), mais l’expression littérale du « champ de mines » attribuée nommément à Pearl n’a pas pu être attestée dans le texte original de 1988 par recherche documentaire. Vérifier la page exacte dans l’ouvrage imprimé ou reformuler « comme l’analyse Judea Pearl `[@pearl1988]`, raisonner en présence d’exceptions revient à traverser un champ de mines ». |
| `pearl2009` | ch. 2 | **Verified Ready** | *Causality* (2^e^ éd., CUP, 2009). Calcul causal (*d*-séparation, *do*-calcul, identifiabilité relative au graphe) conforme à ch. 2 l. 123 et 128. |
| `vovk2005` | ch. 2 | **Verified Ready** | Vovk, Gammerman & Shafer (2005), *Algorithmic Learning in a Random World*, Springer. Garantie à échantillon fini sous échangeabilité conforme à ch. 2 l. 123 et 131. |
| `angelopoulos2023` | ch. 2 | **Verified Ready** | Angelopoulos & Bates (2023), *Foundations and Trends in Machine Learning*, 16(4), 494–591. Couvre bien la prédiction conforme standard sous échangeabilité ET les variantes pondérées sous dérive de covariables (*weighted conformal prediction*, mentionnée à ch. 2 l. 131). |
| `russell2021` | ch. 3 | **Minor BibTeX metadata fix needed** | Russell & Norvig, *AIMA*, 4^e^ éd., Pearson (copyright US 2020, éd. globale 2021 — préciser `2020` ou conserver `2021` selon le tirage). L’exposé des mondes possibles pour les probabilités figure au **chapitre 12** (*Quantifying Uncertainty*, ch. 13 dans la 3^e^ éd.). Affirmation ch. 3 l. 9 conforme. |
| `definetti1974` | ch. 1, 3 | **Verified Ready** | de Finetti (1974), *Theory of Probability*, vol. 1, Wiley. Affirmations ch. 1 et ch. 3 conformes (ajouter ch. 1 dans `averifier` si conservé). |
| `savage1954` | ch. 3, 4, 17 | **Minor BibTeX metadata fix needed** | Métadonnées exactes (Wiley, 1954 ; théorème de représentation ch. 2–5, probabilité personnelle ch. 3, utilité espérée ch. 5). Note : ch. 4 l. 18 et ch. 17 l. 35, 95 conformes ; le champ `averifier` peut mentionner explicitement la probabilité personnelle pour le ch. 3. |
| `jaynes2003` | ch. 1, 3 | **Verified Ready** | Jaynes (2003), *Probability Theory: The Logic of Science*, CUP (éd. G. L. Bretthorst). Affirmations ch. 1 et ch. 3 conformes. |
| `lindley2006` | ch. 1, 3 | **Verified Ready** | Lindley (2006), *Understanding Uncertainty*, Wiley. Affirmations ch. 1 et ch. 3 conformes. |
| `gneiting2007` | ch. 3, 17, 99 | **Verified Ready** | Gneiting & Raftery (2007), *JASA*, 102(477), 359–378. Règles propres / strictement propres, score log et Brier, et principe « maximizing sharpness subject to calibration » conformes aux ch. 3, 17 et Conclusion. |
| `knight1921` | ch. 5 | **Verified Ready** | Knight (1921), *Risk, Uncertainty and Profit*, Houghton Mifflin. Distinction risque / incertitude non mesurable conforme à ch. 5 l. 43. |
| `wynne1992` | ch. 5 | **Verified Ready** | Wynne (1992), *Global Environmental Change*, 2(2), 111–127. Typologie risque / incertitude / ignorance / indétermination conforme à ch. 5 l. 43. |
| `walker2003` | ch. 5 | **Verified Ready** | Walker et al. (7 auteurs exacts), *Integrated Assessment*, 4(1), 5–17 (2003). Conforme à ch. 5 l. 43. |
| `lempert2003` | ch. 5 | **Verified Ready** | Lempert, Popper & Bankes (2003), RAND (*MR-1626-RPC*). Incertitude profonde (*deep uncertainty*) conforme à ch. 5 l. 43. |
| `russell1912` | ch. 5, 13 | **Verified Ready** | Russell (1912), *The Problems of Philosophy*, Williams and Norgate, ch. VI « On Induction » (« The man who has fed the chicken every day throughout its life at last wrings its neck instead... »). Conforme à ch. 5 l. 45 et ch. 13. |
| `hume1748` | ch. 1, 7 | **Minor BibTeX metadata fix needed** | Ajouter l’éditeur d’origine (`London: A. Millar`) ou l’édition critique utilisée ; noter que le titre de 1748 était *Philosophical Essays Concerning Human Understanding* (retitré *An Enquiry...* en 1758). Problème de l’induction conforme aux ch. 1 et 7. |
| `goodman1955` | ch. 7 | **Verified Ready** | Goodman (1955), *Fact, Fiction, and Forecast*, Harvard University Press (ch. III « The New Riddle of Induction », prédicat *grue* / « vleu »). Conforme à ch. 7 l. 113. |
| `wolpert1997` | ch. 7 | **Verified Ready** | Wolpert & Macready (1997), *IEEE Trans. Evol. Comput.*, 1(1), 67–82. Théorèmes *no free lunch* pour l’optimisation conformes à ch. 7 l. 109. |
| `sutton2018` | ch. 7, 17 | **Verified Ready** | Sutton & Barto (2018), *Reinforcement Learning: An Introduction* (2^e^ éd.), MIT Press. Rôle de l’exploration conforme à ch. 7 l. 124 et ch. 17 l. 127. |
| `lazer2014` | ch. 7, 13, 99 | **Verified Ready** | Lazer, Kennedy, King & Vespignani (2014), *Science*, 343(6176), 1203–1205. Chronologie et mécanismes de dérive de Google Flu Trends (sans chiffres précis non vérifiés) conformes aux ch. 7, 13 et Conclusion. |
| `rogers1986` | ch. 5, 6 | **Minor BibTeX metadata fix needed** | Compléter titre et éditeur : *Report of the Presidential Commission on the Space Shuttle Challenger Accident*, U.S. Government Printing Office, Washington, D.C., June 6, 1986. Pour le texte, voir **Partie B.2** (distinguer direction NASA et direction Morton Thiokol au ch. 6 l. 112). |
| `tufte1997` | ch. 5, 6 | **Minor BibTeX metadata fix needed** | Compléter le sous-titre : *Visual Explanations: Images and Quantities, Evidence and Narrative*, Graphics Press, 1997. Pour le texte, voir **Partie B.2** (harmoniser 7 + 16 + 1 = 24 vols, soit 23 documentés, entre ch. 5 l. 119 et ch. 6 l. 112). |
| `knightleveson1986` | ch. 8, 13, 99 | **Verified Ready** | Knight & Leveson (1986), *IEEE Trans. Softw. Eng.*, SE-12(1), 96–109. 27 versions indépendantes, échecs corrélés sur entrées difficiles : conforme aux ch. 8, 13 et Conclusion. |
| `levins1966` | ch. 8 | **Verified Ready** | Levins (1966), *American Scientist*, 54(4), 421–431. Citation exacte p. 423 : « Hence our truth is the intersection of independent lies. » Conforme à ch. 8 l. 82. |
| `orzack1993` | ch. 8 | **Verified Ready** | Orzack & Sober (1993), *Quarterly Review of Biology*, 68(4), 533–546. Critique de l’analyse de robustesse de Levins conforme à ch. 8 l. 82. |
| `wimsatt1981` | ch. 8 | **Verified Ready** | Wimsatt (1981), *Scientific Inquiry and the Social Sciences*, Jossey-Bass, pp. 124–163. Analyse de robustesse conforme à ch. 8 l. 82. |
| `mayo1996` | ch. 9 | **Verified Ready** | Mayo (1996), *Error and the Growth of Experimental Knowledge*, University of Chicago Press. Critère de sévérité conforme à ch. 9 l. 42, 45. |
| `mayo2018` | ch. 9 | **Minor BibTeX metadata fix needed** | Compléter le sous-titre : *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*, CUP, 2018. Affirmation conforme à ch. 9. |
| `bliss1995` | ch. 9, 16, 99 | **Verified Ready** | Bliss, Gilson & Deaton (1995), *Ergonomics*, 38(11), 2300–2312. Appariement des probabilités (*probability matching*) face aux alarmes de fiabilité variable conforme aux ch. 9, 16 et Conclusion. |
| `hoare1969` | ch. 10 | **Minor BibTeX metadata fix needed** | Corriger la pagination : l’article de Hoare dans *Comm. ACM* 12(10) couvre les pages `576--580` et `583` (ACM DL : `576--583`). Triplet de Hoare (avec note de `NOTES_10.md` sur la notation usuelle `{P} C {Q}`) conforme à ch. 10 l. 11, 14. |
| `meyer1992` | ch. 10 | **Verified Ready** | Meyer (1992), *Computer*, 25(10), 40–51. Programmation par contrat (préconditions, postconditions, invariants) conforme à ch. 10 l. 9, 33. |
| `dijkstra1972` | ch. 10 | **Verified Ready** | Dijkstra (1972), « The humble programmer », *Comm. ACM*, 15(10), 859–866 (formulation explicite dans la conférence Turing ; également présent dans EWD249, 1969/1970). Paraphrase sans guillemets à ch. 10 l. 93 tout à fait conforme. |
| `mco1999` | ch. 0, 8, 10, 12, 13, 14, 99 | **Minor BibTeX metadata fix needed** | Ajouter la date exacte (`month = nov`, 10 nov. 1999) dans l’entrée. Pour la chaîne causale manquante au ch. 8 l. 185, voir **Partie B.3**. |
| `sculley2015` | ch. 11 | **Verified Ready** | Sculley et al. (10 auteurs exacts), *Advances in Neural Information Processing Systems 28*, 2015, pp. 2503–2511. Conforme à ch. 11 l. 21. |
| `dellacqua2023` | ch. 11, 12, 99 | **Minor BibTeX metadata fix needed** | Préciser `McFowland III, Edward` et `month = sep` (HBS Working Paper 24-013, 2023). Tous les chiffres des ch. 11 et 12 sont vérifiés (**Partie B.5**). |
| `nostalgebraist2020` | ch. 11 | **Minor BibTeX metadata fix needed** | Ajouter la date (`31 août 2020`) et l’URL (`https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens`). Si une référence publiée/arXiv complémentaire est souhaitée pour le *tuned lens*, Belrose et al. (2023, arXiv:2303.08112) existe ; `nostalgebraist2020` demeure toutefois la référence d’origine exacte du *logit lens*. |
| `mata2023` | ch. 0, 11, 13 | **Claim mismatch** | Métadonnée : ajouter le recueil `678 F. Supp. 3d 443`, le juge `(PKC)`, et la date `June 22, 2023`. **Écart dans le texte (Partie B.1) :** ch. 0 l. 9 et ch. 11 l. 54 omettent que le **cabinet** (`Levidow, Levidow & Oberman P.C.`) a été sanctionné avec les deux avocats. |
| `moffatt2024` | ch. 11 | **Verified Ready** | *Moffatt v. Air Canada*, 2024 BCCRT 149 (14 fév. 2024). Conforme pour les faits et l’absence de preuve technique au dossier ; voir **Partie A.3** pour le retrait de l’incise sur la déclaration ultérieure. |
| `goodhart1975` | ch. 11 | **Verified Ready** | Goodhart (1975), *Papers in Monetary Economics*, vol. 1, Reserve Bank of Australia. Conforme à ch. 11 l. 84. |
| `strathern1997` | ch. 11 | **Verified Ready** | Strathern (1997), *European Review*, 5(3), 305–321. Conforme à ch. 11 l. 84. |
| `christiano2017` | ch. 11 | **Minor BibTeX metadata fix needed** | Compléter `Brown, Tom B.` et ajouter `pages = {4299--4307}` (NeurIPS 30, 2017). Affirmation RLHF conforme à ch. 11 l. 76. |
| `ouyang2022` | ch. 11 | **Minor BibTeX metadata fix needed** | Développer `Ouyang, Long and others` vers les **20 auteurs complets** et ajouter `pages = {27730--27744}` (NeurIPS 35, 2022). Affirmation conforme à ch. 11 l. 76. |
| `kalai2024` | ch. 12 | **Verified Ready** | Kalai & Vempala (2024), STOC ’24, pp. 160–171. Borne inférieure par taux de *singletons* (*monofacts*) et argument de type Good-Turing conformes à ch. 12 l. 86, 89, 102, 152. |
| `kalai2025` | ch. 12, 17 | **Verified Ready** | Kalai, Nachum, Vempala & Zhang (2025), arXiv:2509.04664 (sept. 2025). Notation binaire des bancs d’épreuve pénalisant l’abstention conforme aux ch. 12 et 17. |
| `farquhar2024` | ch. 12 | **Verified Ready** | Farquhar, Kossen, Kuhn & Gal (2024), *Nature*, 630, 625–630. Entropie sémantique pour confabulations vs erreurs constantes conforme à ch. 12 l. 109, 110, 142, 154. |
| `sha2001` | ch. 13 | **Verified Ready** | Sha (2001), *IEEE Software*, 18(4), 20–28. Architecture Simplex conforme à ch. 13 l. 90, 136, 142. |
| `demoura2021` | ch. 13 | **Claim mismatch** | Métadonnées exactes (CADE 28, LNCS 12699, pp. 625–635, 2021). **Écart d’attribution (Partie B.7) :** cité au ch. 13 l. 89 et 101 pour l’*autoformalisation*, que `demoura2021` ne couvre pas (il couvre Lean 4 et son noyau de confiance) ; adjoindre `wu2022`. |
| `sec2013knight` | ch. 14, 17 | **Claim mismatch** | Métadonnée : préciser `Release No. 34-70694` et la date `October 16, 2013`. **Écart rédactionnel (Partie B.4) :** harmoniser ch. 14 l. 43 (« laissa actif ») et l. 45 (« code dormant réactivé ») en mentionnant 1 des 8 serveurs et l’indicateur réutilisé. |
| `bainbridge1983` | ch. 15 | **Verified Ready** | Bainbridge (1983), *Automatica*, 19(6), 775–779. Ironie de l’automatisation conforme à ch. 15 l. 73, 75. |
| `becker2025` | ch. 0, 15, 99 | **Verified Ready** | Becker, Rush, Barnes & Rein (2025), arXiv:2507.09089. Essai METR (+19 % temps mesuré vs ~20 % plus rapide perçu, outils début 2025) conforme aux ch. 0, 15 et Conclusion. |
| `spence1973` | ch. 15 | **Verified Ready** | Spence (1973), *QJE*, 87(3), 355–374. Signal coûteux et équilibre séparateur conformes à ch. 15 l. 50, 59. |
| `akerlof1970` | ch. 15 | **Verified Ready** | Akerlof (1970), *QJE*, 84(3), 488–500. Marché des *lemons* et sélection adverse conformes à ch. 15 l. 52, 60. |
| `sharma2023` | ch. 15 | **Minor BibTeX metadata fix needed** | Développer `Sharma, Mrinank and others` vers les **19 auteurs complets** ; la version publiée étant acceptée à **ICLR 2024**, basculer ou mentionner `ICLR 2024` (en gardant `arXiv:2310.13548` si l’on conserve la clé `sharma2023`). Affirmation sur la complaisance (*sycophancy*) sous RLHF conforme à ch. 15 l. 84. |
| `shumailov2024` | ch. 16 | **Verified Ready** | Shumailov et al. (6 auteurs exacts), *Nature*, 631, 755–759 (2024). Effondrement des modèles sur données récursives conforme à ch. 16 l. 90. |
| `ue2015tip` | ch. 0, 18, 99 | **Minor BibTeX metadata fix needed** | Ajouter date et pagination au *JOUE* (`14 novembre 2015, p. 1--142`) et préciser en note/annexe les points `11.4` (formation continue) et `12.5` (TIP : CTI/FTI) de l’Annexe. Affirmations conformes aux ch. 0, 18 et Conclusion. |
| `demillo1978` | ch. 18, 99 | **Verified Ready** | DeMillo, Lipton & Sayward (1978), *Computer*, 11(4), 34–41. Test par mutation conforme à ch. 18 l. 119 et Conclusion. |
| `lewis2020` | ch. 18, 99 | **Minor BibTeX metadata fix needed** | Développer `Lewis, Patrick and others` vers les **12 auteurs complets** et ajouter `pages = {9459--9474}` (NeurIPS 33, 2020). Description fonctionnelle du RAG conforme à ch. 18 l. 72 et Conclusion. |

---

## Annexe — Blocs BibTeX corrigés prêts à copier pour `biblio.bib`

Les blocs ci-dessous fournissent les versions corrigées des entrées de `biblio_a_verifier.bib` demandant une mise à jour de métadonnées (15 entrées *Minor BibTeX metadata fix needed* hors `savage1954` dont seul `averifier` change et `russell2021`/`hume1748` inclus, plus `pearl1988`, `mata2023` et `sec2013knight` ; les 6 nouvelles entrées `shanahan2016frame`, `fcic2011`, `coval2009`, `gerardi2008`, `stockman2019` et `wu2022` figurent en Parties A et B) :

```bibtex
@incollection{dennett1984,
  author    = {Dennett, Daniel C.},
  title     = {Cognitive wheels: the frame problem of {AI}},
  booktitle = {Minds, Machines and Evolution: Philosophical Studies},
  editor    = {Hookway, Christopher},
  publisher = {Cambridge University Press},
  year      = {1984},
  pages     = {129--151}
}

@book{korzybski1933,
  author    = {Korzybski, Alfred},
  title     = {Science and Sanity: An Introduction to Non-Aristotelian Systems and General Semantics},
  publisher = {International Non-Aristotelian Library Publishing Company},
  year      = {1933}
}

@book{pearl1988,
  author    = {Pearl, Judea},
  title     = {Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference},
  publisher = {Morgan Kaufmann},
  year      = {1988}
}

@book{russell2021,
  author    = {Russell, Stuart J. and Norvig, Peter},
  title     = {Artificial Intelligence: A Modern Approach},
  edition   = {4},
  publisher = {Pearson},
  year      = {2021},
  isbn      = {978-0-13-461099-3}
}

@book{hume1748,
  author    = {Hume, David},
  title     = {An Enquiry Concerning Human Understanding},
  publisher = {A. Millar},
  address   = {London},
  year      = {1748}
}

@techreport{rogers1986,
  author      = {{Presidential Commission on the Space Shuttle Challenger Accident}},
  title       = {Report of the Presidential Commission on the Space Shuttle Challenger Accident},
  institution = {U.S. Government Printing Office},
  address     = {Washington, D.C.},
  year        = {1986},
  month       = jun
}

@book{tufte1997,
  author    = {Tufte, Edward R.},
  title     = {Visual Explanations: Images and Quantities, Evidence and Narrative},
  publisher = {Graphics Press},
  year      = {1997}
}

@book{mayo2018,
  author    = {Mayo, Deborah G.},
  title     = {Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars},
  publisher = {Cambridge University Press},
  year      = {2018}
}

@article{hoare1969,
  author  = {Hoare, C. A. R.},
  title   = {An axiomatic basis for computer programming},
  journal = {Communications of the ACM},
  volume  = {12},
  number  = {10},
  pages   = {576--583},
  year    = {1969},
  doi     = {10.1145/363235.363259}
}

@techreport{mco1999,
  author      = {{Mars Climate Orbiter Mishap Investigation Board}},
  title       = {Phase {I} Report},
  institution = {NASA},
  year        = {1999},
  month       = nov
}

@techreport{dellacqua2023,
  author      = {Dell'Acqua, Fabrizio and McFowland III, Edward and Mollick, Ethan R. and Lifshitz-Assaf, Hila and Kellogg, Katherine C. and Rajendran, Saran and Krayer, Lisa and Candelon, Fran\c{c}ois and Lakhani, Karim R.},
  title       = {Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of {AI} on Knowledge Worker Productivity and Quality},
  institution = {Harvard Business School},
  type        = {Working Paper},
  number      = {24-013},
  year        = {2023},
  month       = sep
}

@misc{nostalgebraist2020,
  author       = {{nostalgebraist}},
  title        = {interpreting {GPT}: the logit lens},
  howpublished = {LessWrong},
  year         = {2020},
  month        = aug,
  url          = {https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens}
}

@misc{mata2023,
  title        = {Mata v. Avianca, Inc.},
  howpublished = {No. 22-cv-1461 (PKC), 678 F. Supp. 3d 443 (S.D.N.Y. June 22, 2023)},
  year         = {2023}
}

@inproceedings{christiano2017,
  author    = {Christiano, Paul F. and Leike, Jan and Brown, Tom B. and Martic, Miljan and Legg, Shane and Amodei, Dario},
  title     = {Deep reinforcement learning from human preferences},
  booktitle = {Advances in Neural Information Processing Systems 30},
  pages     = {4299--4307},
  year      = {2017}
}

@inproceedings{ouyang2022,
  author    = {Ouyang, Long and Wu, Jeffrey and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll L. and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and Schulman, John and Hilton, Jacob and Kelton, Fraser and Miller, Luke and Simens, Maddie and Askell, Amanda and Welinder, Peter and Christiano, Paul and Leike, Jan and Lowe, Ryan},
  title     = {Training language models to follow instructions with human feedback},
  booktitle = {Advances in Neural Information Processing Systems 35},
  pages     = {27730--27744},
  year      = {2022}
}

@misc{sec2013knight,
  author       = {{U.S. Securities and Exchange Commission}},
  title        = {In the Matter of Knight Capital Americas {LLC}},
  howpublished = {Exchange Act Release No. 34-70694, Administrative Proceeding File No. 3-15570},
  year         = {2013},
  month        = oct
}

@inproceedings{sharma2023,
  author    = {Sharma, Mrinank and Tong, Meg and Korbak, Tomasz and Duvenaud, David and Askell, Amanda and Bowman, Samuel R. and Cheng, Newton and Durmus, Esin and Hatfield-Dodds, Zac and Johnston, Scott R. and Kravec, Shauna and Maxwell, Timothy and McCandlish, Sam and Ndousse, Kamal and Rausch, Oliver and Schiefer, Nicholas and Yan, Da and Zhang, Miranda and Perez, Ethan},
  title     = {Towards Understanding Sycophancy in Language Models},
  booktitle = {International Conference on Learning Representations (ICLR 2024)},
  note      = {arXiv:2310.13548 (2023)},
  year      = {2024}
}

@misc{ue2015tip,
  author       = {{Commission europ\'eenne}},
  title        = {R\`eglement d'ex\'ecution ({UE}) 2015/1998 de la Commission du 5 novembre 2015 fixant des mesures d\'etaill\'ees pour la mise en {\oe}uvre des normes de base communes dans le domaine de la s\^uret\'e de l'aviation civile},
  howpublished = {Journal officiel de l'Union europ\'eenne, L 299, 14 novembre 2015, p. 1--142 (Annexe, points 11.4 et 12.5)},
  year         = {2015}
}

@inproceedings{lewis2020,
  author    = {Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and K\"uttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rockt\"aschel, Tim and Riedel, Sebastian and Kiela, Douwe},
  title     = {Retrieval-augmented generation for knowledge-intensive {NLP} tasks},
  booktitle = {Advances in Neural Information Processing Systems 33},
  pages     = {9459--9474},
  year      = {2020}
}
```
