# Contrôle de portée — `00-cartographier`

- Original : `monographie/chapitres/00-cartographier.md`
- Réécriture : `style/pilots/00-cartographier.md`
- Généré le 2026-11-20 par `style/diff_portee.py` (STYLE_PASS_SPEC.md, §6.3)

**Mode d'emploi.** Pour chaque case : la cocher et écrire après « décision : » *accepté* ou *rétabli* (avec, au besoin, la formulation retenue). `python3 style/diff_portee.py --controle <ce fichier>` échoue tant qu'une case reste vide. ⛔ = invariant de la spec touché ; ⚠ = portée ou contenu possiblement modifié. Les éléments · (reformulation à effectif constant, variantes morphologiques, mots ajoutés) sont à parcourir et ne demandent pas de décision.

**Bilan :** 83 décision(s) à prendre — ⛔ 0 · ⚠ 83 ; 50 élément(s) · à parcourir

## Synthèse par section

| Section | ⛔ | ⚠ | · |
| :-- | --: | --: | --: |
| `sec:ch00` Cartographier le terrain |  | 5 | 1 |
| `sec:ch00-trois-recits` Trois récits pour poser le problème |  | 5 | 3 |
| `sec:ch00-representation` Nous agissons d’après une représentation |  | 1 | 1 |
| `sec:ch00-mer-probabilites` La mer ne consulte pas nos probabilités |  | 3 | 3 |
| `sec:ch00-regle-cadre` Toute règle cache un arrière-plan ouvert |  | 5 | 2 |
| `sec:ch00-decider-enjeux` Décider une seule fois face à des enjeux asymétriques |  | 3 | 2 |
| `sec:ch00-detromper` Une erreur n’est arrêtée que par ce qui peut se tromper autrement |  | 1 | 2 |
| `sec:ch00-barre-erreur` Ce que mesure — et ce que tait — une barre d’erreur |  | 2 | 3 |
| `sec:ch00-cinq-conditions` Les cinq conditions d’un contrôle |  | 3 | 3 |
| `sec:ch00-auto-verification` Pourquoi l’auto-vérification bute sur le cadre |  | 4 | 1 |
| `sec:ch00-chaines-croises` Chaînes en série et contrôles croisés en parallèle |  | 5 | 2 |
| `sec:ch00-contrats-donnees` L’informatique classique a gagné ses garanties ; les modèles appris les dépensent |  | 5 | 6 |
| `sec:ch00-automatisation` Ce que l’automatisation fait aux contrôles |  | 2 | 2 |
| `sec:ch00-auto-chaines` L’automatisation met les étapes en chaîne et fait passer les erreurs à l’acte |  | 1 | 1 |
| `sec:ch00-auto-erosion` L’automatisation érode les vérifications humaines |  | 5 | 4 |
| `sec:ch00-auto-correlation` L’automatisation corrèle les angles morts à l’échelle collective |  | 2 | 1 |
| `sec:ch00-enigme-arithmetique` L’énigme arithmétique du producteur plus fiable et du système plus risqué |  | 7 | 2 |
| `sec:ch00-remedes` Ce que nous pouvons encore faire |  | 9 | 4 |
| `sec:ch00-architecture` Architecture de l’ouvrage |  | 8 | 4 |
| `sec:ch00-parcours` Parcours de lecture |  | 3 | 2 |
| `titre:Points clés` Points clés |  | 3 | 1 |

## Invariants structurels (fichier entier)

- [ ] ⚠ Clés de citation (fichier entier) — décision : 
    - ajoutés : becker2025, mata2023 (2 occurrence(s))

## `sec:ch00` — Cartographier le terrain

- [ ] ⚠ Quantificateurs absolus — *aucun(e)* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … passage de l'informatique classique à l'intelligence artificielle et à l'automatisation **Aucun** terme n'y est encore défini formellement chacun recevra sa définition … »
- [ ] ⚠ Statut épistémique — *démontrer / prouver* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … vol d'oiseau avant d'entrer dans le détail des outils des **démonstrations** et des cas Il pose en langage courant la question … »
- [ ] ⚠ Statut épistémique — *argument* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « Avant d'entrer dans le détail des outils des **arguments** et des études de cas ce chapitre parcourt l'ensemble du … »
- [ ] ⚠ Statut épistémique — *théorie / théorème* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … qui reviendront d'un chapitre à l'autre et montre comment une **théorie** générale de la décision et des contrôles éclaire le passage … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (6) — décision : 
    - *problème* : « … Il pose en langage courant le **problème** directeur du livre fait apparaître par … »
    - *directeur* : « … pose en langage courant le problème **directeur** du livre fait apparaître par le … »
    - *apparaître* : « … le problème directeur du livre fait **apparaître** par le récit les notions qui … »
    - *réflexion* : « … en chapitre et montre comment une **réflexion** générale sur la décision et sur … »
    - *emploie* : « … et à l'automatisation Les mots qu'il **emploie** ne sont pas encore définis chacun … »
    - *adaptés* : « … et sur des parcours de lecture **adaptés** à chaque profil »
- · Mots pleins : 2 variante(s), 7 ajout(s)
    - variantes probables : définis → définition, précision → précise
    - ajoutés : question, directrice, ouvrage, formellement, recevra, détaillée, itinéraires

## `sec:ch00-trois-recits` — Trois récits pour poser le problème

- [ ] ⚠ Quantificateurs absolus — *aucun(e)* : 6 → 5 (effectif modifié) — décision : 
    - retiré : « … ne pouvait pas traverser sans dommage La commission d'enquête n'eut **aucun** mal à désigner la cause technique immédiate de la perte … »
    - retiré : « … le juge cherchèrent ces décisions dans les recueils de jurisprudence **aucune** n'existait L'un des avocats avait interrogé un modèle de langage … »
    - retiré : « … cherchait après coup l'équivalent du fichier on ne trouvait rien **Aucun** composant n'avait enfreint de spécification écrite pour la simple raison … »
    - retiré : « … et assurée indiscernable en surface d'une réponse exacte sans qu **aucune** règle écrite ait été violée Dans la troisième des experts … »
    - ajouté : « … derrière la planète comme prévu puis l'on n'en reçut plus **aucun** signal sa trajectoire l'avait amenée trop près de la surface … »
    - ajouté : « … le juge cherchèrent ces arrêts dans les recueils de jurisprudence **aucun** n'existait L'un des avocats avait consulté un modèle de langage … »
    - ajouté : « … cherchait après coup l'équivalent du fichier on ne trouvait rien **Aucun** module n'avait enfreint une spécification écrite pour la simple raison … »
- [ ] ⚠ Quantificateurs absolus — *jamais* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … derrière la planète comme prévu mais l'on n'en reçut plus **jamais** le moindre signal sa trajectoire l'avait amenée beaucoup trop près … »
- [ ] ⚠ Statut épistémique — *montrer* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … ces facteurs se trouvait un point précis que l'on pouvait **montrer** du doigt un fichier de code et la spécification écrite … »
- [ ] ⚠ Citations modifiées dans la section (invariant 3) — décision : 
    - ajoutées : @mata2023 (vérifier qu'elles soutiennent la phrase où elles sont placées)
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (25) — décision : 
    - *moindre* : « … l'on n'en reçut plus jamais le **moindre** signal sa trajectoire l'avait amenée beaucoup … »
    - *dommage* : « … qu'elle ne pouvait pas traverser sans **dommage** La commission d'enquête n'eut aucun mal … »
    - *propulseurs* : « … de petites poussées de correction des **propulseurs** et ses résultats étaient transmis sous … »
    - *étaient* : « … correction des propulseurs et ses résultats **étaient** transmis sous forme de fichier à … »
    - *chargée* : « … de fichier à l'équipe de navigation **chargée** de calculer la trajectoire Or la … »
    - *impulsions* : « … la spécification d'interface exigeait que ces **impulsions** soient exprimées dans l'unité du Système … »
    - *exprimées* : « … d'interface exigeait que ces impulsions soient **exprimées** dans l'unité du Système international le … »
    - *mention* : « … l'interface les nombres voyageaient nus sans **mention** d'unité chaque impulsion était ainsi sous-estimée … »
    - *opposer* : « … New York déposèrent un mémoire pour **s'opposer** à la demande de rejet présentée … »
    - *présentée* : « … s'opposer à la demande de rejet **présentée** par la compagnie aérienne Le texte … »
    - *appuyait* : « … dans une langue juridique irréprochable et **s'appuyait** sur une demi-douzaine de décisions de … »
    - *interrogé* : « … aucune n'existait L'un des avocats avait **interrogé** un modèle de langage conversationnel qui … »
    - *données* : « … figuraient bien dans les bases de **données** juridiques Ici encore une affirmation fausse … »
    - *composant* : « … fichier on ne trouvait rien Aucun **composant** n'avait enfreint de spécification écrite pour … »
    - *travaillaient* : « … développeurs chevronnés de logiciels libres qui **travaillaient** sur leurs propres dépôts de code … »
    - *connaissaient* : « … de code des projets complexes qu'ils **connaissaient** intimement depuis des années Chaque tâche … »
    - *propose* : « … le terrain que ce livre se **propose** de cartographier Dans la première une … »
    - *cartographier* : « … que ce livre se propose de **cartographier** Dans la première une erreur de … »
    - *perdues* : « … parce que ses unités ont été **perdues** en chemin et qu'aucun contrôle indépendant … »
    - *survenu* : « … la recoupe mais une fois l'accident **survenu** une spécification écrite permet de localiser … »
    - *ambiguïté* : « … permet de localiser la faute sans **ambiguïté** Dans la deuxième l'erreur se présente … »
    - *trompent* : « … Dans la troisième des experts se **trompent** sur le signe même de l'effet … »
    - *prennent* : « … de l'effet de leur outil ils **prennent** un ralentissement mesuré pour un gain … »
    - *intermédiaire* : « … nous agissons sur le monde par **l'intermédiaire** de mesures de modèles mathématiques de … »
    - *informatiques* : « … mesures de modèles mathématiques de programmes **informatiques** et désormais de chaînes automatisées qu'est-ce … »
- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 3 → 3 (reformulé autour)
    - retiré : « … sous ces facteurs se trouvait un point précis que l'on **pouvait** montrer du doigt un fichier de code et la spécification … »
    - ajouté : « … ces facteurs se trouvait pourtant un point précis que l'on **pouvait** désigner du doigt un fichier de code et la spécification … »
- · Statut épistémique — *résultat* : 1 → 1 (reformulé autour)
    - retiré : « … l'effet de petites poussées de correction des propulseurs et ses **résultats** étaient transmis sous forme de fichier à l'équipe de navigation … »
    - ajouté : « … calculait l'effet des petites poussées de correction et transmettait ses **résultats** par fichier à l'équipe de navigation La spécification d'interface exigeait … »
- · Mots pleins : 4 variante(s), 14 ajout(s)
    - variantes probables : calculé → calculait, transmis → transmettait, calculer → calculait, construit → construction
    - ajoutés : intacte, identifia, rapidement, alertes, restées, consulté, assurer, conseils, attention, perdent, violation, méprennent, prenant, entremise

## `sec:ch00-representation` — Nous agissons d’après une représentation

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (2) — décision : 
    - *seconde* : « Pour répondre à cette **seconde** question il faut repartir de la … »
    - *repartir* : « … à cette seconde question il faut **repartir** de la situation élémentaire de tout … »
- · Mots pleins : 0 variante(s), 1 ajout(s)
    - ajoutés : revenir

## `sec:ch00-mer-probabilites` — La mer ne consulte pas nos probabilités

- [ ] ⚠ Lecture des probabilités — *probable / probabilité* : 4 → 3 (effectif modifié) — décision : 
    - retiré : « … les départagera guère du moins dans le cas le plus **probable** Si le voilier léger arrive intact chacun verra simplement se … »
- [ ] ⚠ Lecture des probabilités — *fréquent / fréquence* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … les départage guère du moins dans le cas le plus **fréquent** Si le voilier léger arrive intact chacun voit se réaliser … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (7) — décision : 
    - *apprête* : « Imaginons un navigateur M X qui **s'apprête** à prendre le départ d'une course … »
    - *prendre* : « … navigateur M X qui s'apprête à **prendre** le départ d'une course au large … »
    - *choisir* : « … d'une course au large et doit **choisir** entre deux embarcations un voilier léger … »
    - *embarcations* : « … large et doit choisir entre deux **embarcations** un voilier léger rapide mais sollicité … »
    - *éclairer* : « … moins véloce mais quasi incassable Pour **éclairer** son choix le marin rassemble ce … »
    - *signifie* : « … et évalue ce risque à Que **signifie** ce ou ce Il ne décrit … »
    - *nettement* : « … que M X et l'issue plaidera **nettement** contre lui mais même alors une … »
- · Modaux et atténuateurs — *presque / quasi / à peu près / environ* : 2 → 2 (reformulé autour)
    - retiré : « … et un voilier renforcé plus lourd et moins véloce mais **quasi** incassable Pour éclairer son choix le marin rassemble ce qu'il … »
    - ajouté : « … et un voilier renforcé plus lourd et moins véloce mais **presque** incassable M X rassemble ce qu'il sait de la météo … »
- · Modaux et atténuateurs — *guère* : 2 → 2 (reformulé autour)
    - retiré : « … hypothèses Une fois la course terminée l'issue ne les départagera **guère** du moins dans le cas le plus probable Si le … »
    - ajouté : « … hypothèses Une fois la course terminée l'issue ne les départage **guère** du moins dans le cas le plus fréquent Si le … »
- · Mots pleins : 2 variante(s), 7 ajout(s)
    - variantes probables : départagera → départage, distinguera → distingue
    - ajoutés : prépare, bateaux, désigne, caractéristique, fidèlement, comparables, évaluer

## `sec:ch00-regle-cadre` — Toute règle cache un arrière-plan ouvert

- [ ] ⚠ Quantificateurs absolus — *tout / tous / toute(s)* : 2 → 3 (effectif modifié) — décision : 
    - ajouté : « … exposés aux surprises Parce qu'aucune règle utilisable ne peut énoncer **toutes** les conditions nécessaires à sa vérité Prenons l'énoncé scolaire par … »
- [ ] ⚠ Quantificateurs absolus — *jamais* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … pas d'une faute de calcul mais d'une variable qui n'a **jamais** figuré dans son cadre »
- [ ] ⚠ Quantificateurs absolus — *rien* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … le lendemain chauffe son récipient à C et constate que **rien** ne bout il a utilisé une eau fortement salée Nous … »
- [ ] ⚠ Quantificateurs absolus — *seul(e) / seulement / uniquement* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … son état habituel alors s'ensuit C'est le premier des deux **seuls** repères symboliques dont nous aurons besoin dans ce chapitre La … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (7) — décision : 
    - *totalité* : « … règle utilisable ne peut énoncer la **totalité** des conditions nécessaires à sa vérité … »
    - *expérience* : « … règle générale Un collègue tente pourtant **l'expérience** le lendemain chauffe son récipient à … »
    - *constate* : « … chauffe son récipient à C et **constate** que rien ne bout il a … »
    - *présence* : « … ouvert d'exceptions possibles salinité confinement altitude **présence** d'impuretés nature des parois qu'aucun manuel … »
    - *figurer* : « … inutilisable Choisir ce que l'on fait **figurer** explicitement dans et ce que l'on … »
    - *appellerons* : « … tacite c'est choisir ce que nous **appellerons** un cadre un ensemble fini de … »
    - *mathématique* : « … affranchir Qu'un raisonnement procède par déduction **mathématique** à partir d'axiomes ou par induction … »
- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 3 → 3 (reformulé autour)
    - retiré : « Pourquoi deux raisonneurs attentifs **peuvent** ils ainsi diverger et pourquoi nos modèles les plus éprouvés … »
    - ajouté : « Pourquoi deux raisonneurs attentifs **peuvent** ils diverger ainsi et pourquoi nos modèles les plus éprouvés … »
- · Mots pleins : 1 variante(s), 4 ajout(s)
    - variantes probables : transporte → transporté
    - ajoutés : ébullition, deuxième, arrêter, absente

## `sec:ch00-decider-enjeux` — Décider une seule fois face à des enjeux asymétriques

- [ ] ⚠ Quantificateurs absolus — *aucun(e)* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … chambre du barillet a été chargée à l'insu du joueur **aucune** cohérence interne du calcul n'empêche de franchir le pas »
- [ ] ⚠ Quantificateurs absolus — *rien* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … chambre du barillet a été chargée à l'insu du joueur **rien** dans la cohérence interne du calcul n'empêchera de franchir le … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (4) — décision : 
    - *demander* : « … démâter en pleine mer oblige à **demander** un remorquage coûteux et fait perdre … »
    - *retient* : « … que la probabilité d'échec que l'on **retient** dépasse un certain seuil Ce seuil … »
    - *comporte* : « … dans l'arrière-plan tacite Si le mât **comporte** une fissure interne invisible ou si … »
    - *invisible* : « … le mât comporte une fissure interne **invisible** ou si une chambre du barillet … »
- · Modaux et atténuateurs — *presque / quasi / à peu près / environ* : 1 → 1 (reformulé autour)
    - retiré : « … on n'accepterait d'appuyer sur la détente que si l'on était **à peu près** certain que la chambre est vide Or c'est là tout … »
    - ajouté : « … de zéro on n'accepterait d'appuyer sur la détente qu'en étant **à peu près** certain que la chambre est vide C'est là tout le … »
- · Mots pleins : 1 variante(s), 4 ajout(s)
    - variantes probables : empêchera → empêche
    - ajoutés : largement, retenue, abaisse, ordinaire

## `sec:ch00-detromper` — Une erreur n’est arrêtée que par ce qui peut se tromper autrement

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (2) — décision : 
    - *méthodes* : « On pourrait espérer que nos **méthodes** de quantification des incertitudes suffisent à … »
    - *prémunir* : « … quantification des incertitudes suffisent à nous **prémunir** contre ce piège un modèle sérieux … »
- · Force de l'affirmation — *suffire* : 1 → 1 (reformulé autour)
    - retiré : « On pourrait espérer que nos méthodes de quantification des incertitudes **suffisent** à nous prémunir contre ce piège un modèle sérieux n'accompagne-t-il … »
    - ajouté : « On pourrait espérer que la quantification des incertitudes **suffise** à prévenir ce piège un modèle sérieux n'accompagne-t-il pas ses … »
- · Mots pleins : 0 variante(s), 1 ajout(s)
    - ajoutés : prévenir

## `sec:ch00-barre-erreur` — Ce que mesure — et ce que tait — une barre d’erreur

- [ ] ⚠ Quantificateurs absolus — *entièrement / totalement / complètement / intégralement* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … ontologique celle qui porte sur l'adéquation du cadre lui-même reste **totalement** muette dans le rapport de calcul Dix relecteurs qui s'en … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (7) — décision : 
    - *confrontant* : « … en rééchantillonnant les données ou en **confrontant** plusieurs sous-modèles une incertitude chiffrée mesure … »
    - *ampleur* : « … sous-modèles une incertitude chiffrée mesure toujours **l'ampleur** du désaccord à l'intérieur d'un ensemble … »
    - *pendant* : « … un facteur omis qui aurait varié **pendant** la collecte des données s'y glisse-t-il … »
    - *mécanique* : « … trace Lorsqu'un ingénieur calcule la tenue **mécanique** d'une ferrure métallique et conclut qu'elle … »
    - *systématiquement* : « … de il explore en faisant varier **systématiquement** ses paramètres l'incertitude aléatoire la dispersion … »
    - *propriétés* : « … paramètres l'incertitude aléatoire la dispersion des **propriétés** de l'alliage d'une coulée à l'autre … »
    - *tiennent* : « … de calcul Dix relecteurs qui s'en **tiennent** à la même note d'hypothèses incomplète … »
- · Quantificateurs absolus — *aucun(e)* : 4 → 4 (reformulé autour)
    - retiré : « … quoi toutes les variantes admises s'accordent par construction parce qu **aucune** d'elles ne contient la variable correspondante ne produit aucun désaccord … »
    - ajouté : « … quoi toutes les variantes admises s'accordent par construction parce qu **aucune** ne contient la variable correspondante ne produit aucun désaccord et … »
- · Quantificateurs absolus — *toujours* : 1 → 1 (reformulé autour)
    - retiré : « … données ou en confrontant plusieurs sous-modèles une incertitude chiffrée mesure **toujours** l'ampleur du désaccord à l'intérieur d'un ensemble d'alternatives admises à … »
    - ajouté : « … données ou en comparant plusieurs sous-modèles une incertitude chiffrée mesure **toujours** le désaccord à l'intérieur d'un ensemble d'alternatives admises d'avance dans … »
- · Mots pleins : 0 variante(s), 4 ajout(s)
    - ajoutés : comparant, prenons, travailler, étudient

## `sec:ch00-cinq-conditions` — Les cinq conditions d’un contrôle

- [ ] ⚠ Quantificateurs absolus — *tout / tous / toute(s)* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … en prenant acte de leur désaccord Cette évidence apparente tire **toute** sa force pratique des cinq conditions qu'elle exige simultanément Pour … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *comparateur* : 4 → 3
    -     retiré : « … une mesure sur le terrain il faut ensuite que ce **comparateur** puisse se tromper autrement que l'affirmation initiale vis-à-vis de la … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (14) — décision : 
    - *intérieur* : « … vienne d'une faute de calcul à **l'intérieur** du cadre ou d'un facteur oublié … »
    - *détectée* : « … facteur oublié au dehors peut-elle être **détectée** avant de se traduire en acte … »
    - *traduire* : « … peut-elle être détectée avant de se **traduire** en acte Uniquement en confrontant l'affirmation … »
    - *évidence* : « … prenant acte de leur désaccord Cette **évidence** apparente tire toute sa force pratique … »
    - *apparente* : « … acte de leur désaccord Cette évidence **apparente** tire toute sa force pratique des … »
    - *simultanément* : « … pratique des cinq conditions qu'elle exige **simultanément** Pour qu'un contrôle arrête une erreur … »
    - *vis-à-vis* : « … se tromper autrement que l'affirmation initiale **vis-à-vis** de la cause d'erreur considérée sans … »
    - *considérée* : « … initiale vis-à-vis de la cause d'erreur **considérée** sans quoi la même cause faussera … »
    - *accompagnés* : « … exprimés dans les mêmes grandeurs et **accompagnés** de leurs conditions et de leurs … »
    - *engagée* : « … temps avant que l'action ne soit **engagée** de façon irréversible il faut enfin … »
    - *dispose* : « … c'est-à-dire quelqu'un qui entende l'alerte et **dispose** de l'autorité nécessaire pour suspendre ou … »
    - *nécessaire* : « … entende l'alerte et dispose de l'autorité **nécessaire** pour suspendre ou modifier la décision … »
    - *manquer* : « … de ces cinq conditions vienne à **manquer** pour une famille d'erreurs et ce … »
    - *contredites* : « … qu'elles atteignent l'action sans avoir été **contredites** à temps est de »
- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 2 → 2 (reformulé autour)
    - retiré : « … à l'intérieur du cadre ou d'un facteur oublié au dehors **peut** elle être détectée avant de se traduire en acte Uniquement … »
    - retiré : « … mesure sur le terrain il faut ensuite que ce comparateur **puisse** se tromper autrement que l'affirmation initiale vis-à-vis de la cause … »
    - ajouté : « … faute interne au cadre ou d'un facteur oublié au dehors **peut** elle alors être repérée avant l'acte Uniquement en confrontant l'affirmation … »
    - ajouté : « … écrite d'avance l'avis d'un pair une mesure de terrain qu'il **puisse** se tromper autrement que l'affirmation initiale sur la cause d'erreur … »
- · Quantificateurs absolus — *seul(e) / seulement / uniquement* : 2 → 2 (reformulé autour)
    - retiré : « … dehors peut-elle être détectée avant de se traduire en acte **Uniquement** en confrontant l'affirmation produite à un comparateur censé concorder avec … »
    - ajouté : « … facteur oublié au dehors peut-elle alors être repérée avant l'acte **Uniquement** en confrontant l'affirmation produite à un comparateur censé concorder avec … »
- · Mots pleins : 0 variante(s), 8 ajout(s)
    - ajoutés : interne, repérée, réclame, ensemble, concert, devienne, parvienne, contradiction

## `sec:ch00-auto-verification` — Pourquoi l’auto-vérification bute sur le cadre

- [ ] ⚠ Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … un modèle statistique validé tant qu'un facteur caché restait constant **peut** être pris en défaut dès que ce facteur change en … »
- [ ] ⚠ Quantificateurs absolus — *tout / tous / toute(s)* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … une étourderie ou un bogue de programmation Mais vis-à-vis de **tout** facteur omis par le cadre la corrosion de la ferrure … »
- [ ] ⚠ Quantificateurs absolus — *jamais* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … une ferrure neuve dans l'air sec d'un laboratoire ne révélera **jamais** l'effet de cinq ans de brouillard salin et un modèle … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (17) — décision : 
    - *constituent* : « … sur la même alimentation électrique ne **constituent** pas deux protections indépendantes contre une … »
    - *refaire* : « … le raisonnement Relire son propre code **refaire** tourner une simulation avec un autre … »
    - *tourner* : « … raisonnement Relire son propre code refaire **tourner** une simulation avec un autre tirage … »
    - *vérifier* : « … avec un autre tirage aléatoire ou **vérifier** un calcul par éléments finis à … »
    - *réflexes* : « … les mêmes idéalisations géométriques sont des **réflexes** précieux pour débusquer une étourderie ou … »
    - *précieux* : « … mêmes idéalisations géométriques sont des réflexes **précieux** pour débusquer une étourderie ou un … »
    - *programmation* : « … une étourderie ou un bogue de **programmation** Mais vis-à-vis de tout facteur omis … »
    - *vis-à-vis* : « … ou un bogue de programmation Mais **vis-à-vis** de tout facteur omis par le … »
    - *corrosion* : « … facteur omis par le cadre la **corrosion** de la ferrure ces contrôles internes … »
    - *effectivement* : « … faut-il que le facteur omis ait **effectivement** varié pendant la collecte des données … »
    - *statistique* : « … de brouillard salin et un modèle **statistique** validé tant qu'un facteur caché restait … »
    - *restait* : « … statistique validé tant qu'un facteur caché **restait** constant peut être pris en défaut … »
    - *constant* : « … validé tant qu'un facteur caché restait **constant** peut être pris en défaut dès … »
    - *construire* : « … de distribution Quant à l'espoir de **construire** une méta-procédure formelle chargée de détecter … »
    - *vraiment* : « … adopter un cadre Ce qui est **vraiment** nouveau n'entre dans un cadre que … »
    - *nouveau* : « … un cadre Ce qui est vraiment **nouveau** n'entre dans un cadre que du … »
    - *épreuve* : « … parce que le monde mis à **l'épreuve** oppose un démenti à nos essais »
- · Mots pleins : 3 variante(s), 8 ajout(s)
    - variantes probables : accorderont → accordent, enregistrer → enregistré, avertit → avertissement
    - ajoutés : forment, relancer, recouper, copient, apparaissent, demeurait, bougera, concret

## `sec:ch00-chaines-croises` — Chaînes en série et contrôles croisés en parallèle

- [ ] ⚠ Modaux et atténuateurs — *souvent / le plus souvent* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … leurs angles morts respectifs Mais ce gain a le plus **souvent** un prix plus le contrôleur est indépendant du producteur par … »
- [ ] ⚠ Lecture des probabilités — *fréquent / fréquence* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … de leurs angles morts Ce gain a toutefois un coût **fréquent** plus le contrôleur est indépendant par ses méthodes sa discipline … »
- [ ] ⚠ Statut épistémique — *résultat* : 2 → 3 (effectif modifié) — décision : 
    - ajouté : « … mêmes définitions et plus il faut travailler pour rendre les **résultats** comparables À l'inverse demander à un modèle de relire sa … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *producteur* : 3 → 1
    -     retiré : « … au travers que si elle échappe à la fois au **producteur** et au contrôleur l'angle mort résiduel se réduit à l'intersection … »
    -     retiré : « … plus souvent un prix plus le contrôleur est indépendant du **producteur** par ses méthodes sa discipline ou ses données moins il … »
    - *contrôleur* : 3 → 2
    -     retiré : « … si elle échappe à la fois au producteur et au **contrôleur** l'angle mort résiduel se réduit à l'intersection de leurs angles … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (13) — décision : 
    - *appellerons* : « … modèle a ainsi ce que nous **appellerons** un angle mort les causes d'erreur … »
    - *incapable* : « … mort les causes d'erreur qu'il est **incapable** de percevoir Lorsque plusieurs composants sont … »
    - *processus* : « … plusieurs composants sont assemblés dans un **processus** de travail l'architecture de leur assemblage … »
    - *architecture* : « … assemblés dans un processus de travail **l'architecture** de leur assemblage détermine si leurs … »
    - *quelconque* : « … Si une erreur survient à l'un **quelconque** des maillons ou si une incompréhension … »
    - *incompréhension* : « … quelconque des maillons ou si une **incompréhension** naît à l'interface entre deux étapes … »
    - *redoutable* : « … passage en série est d'autant plus **redoutable** qu'il s'accompagne souvent d'un blanchiment des … »
    - *étaient* : « … et parfois de ses unités comme **l'étaient** les impulsions transmises à l'équipe de … »
    - *compare* : « … examinent la même question et l'on **compare** leurs réponses Sous réserve que la … »
    - *travers* : « … instruits une erreur ne passe au **travers** que si elle échappe à la … »
    - *respectifs* : « … à l'intersection de leurs angles morts **respectifs** Mais ce gain a le plus … »
    - *conclusions* : « … il faut travailler pour rendre leurs **conclusions** comparables Un modèle à qui l'on … »
    - *vis-à-vis* : « … dessine un contrôle croisé sur l'organigramme **vis-à-vis** de son propre angle mort ce … »
- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 1 → 1 (reformulé autour)
    - retiré : « … plus rien à quoi comparer ce qu'il reçoit il ne **peut** que l'incorporer comme un fait accompli À l'inverse dans un … »
    - ajouté : « … possède ainsi un angle mort les causes d'erreur qu'il ne **peut** pas percevoir Lorsqu'on assemble plusieurs composants dans un flux de … »
- · Mots pleins : 2 variante(s), 8 ajout(s)
    - variantes probables : incorporer → incorpore, demande → demander
    - ajoutés : possède, géométrie, malentendu, devient, fragile, chiffre, contraire, confronte

## `sec:ch00-contrats-donnees` — L’informatique classique a gagné ses garanties ; les modèles appris les dépensent

- [ ] ⚠ Quantificateurs absolus — *jamais* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … vaut pour toutes ses exécutions futures Les tests ne prouvent **jamais** l'absence d'erreur mais le geste reste le même on vérifie … »
- [ ] ⚠ Quantificateurs absolus — *seul(e) / seulement / uniquement* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … mais le geste reste le même on vérifie d'avance une **seule** fois pour toutes les exécutions Et lorsque le logiciel échoue … »
- [ ] ⚠ Force de l'affirmation — *garantir (verbe)* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … mesurée en moyenne sur des tests de référence qui ne **garantit** aucune réponse particulière La façon dont l'échec se présente dans … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *contrat* : 4 → 5
    -     retiré : « … propriétés basculent simultanément Ce qui est promis on passe d'un **contrat** vérifiable sur chaque appel à une tendance statistique mesurée en … »
    -     retiré : « … plutôt qu'au câblage d'un disjoncteur cela ne rétablit pas un **contrat** Faute de pouvoir vérifier en amont un tel composant il … »
    -     ajouté : « … analyse statique ou preuve formelle confrontent le composant à son **contrat** avant sa mise en service en un contrôle fait une … »
    -     ajouté : « … où trois propriétés basculent ensemble Ce qui est promis au **contrat** vérifiable sur chaque appel succède une tendance statistique mesurée en … »
    -     ajouté : « … dressage plutôt qu'au câblage d'un disjoncteur cela ne rétablit aucun **contrat** Faute de vérification en amont le contrôle doit se reporter … »
    - *vérification en amont* : 1 → 2
    -     retiré : « … au code elle sert de comparateur permanent Elle autorise une **vérification en amont** typage tests analyse statique ou preuve formelle confrontent le composant … »
    -     ajouté : « … au code elle sert de comparateur permanent Elle autorise la **vérification en amont** typage tests analyse statique ou preuve formelle confrontent le composant … »
    -     ajouté : « … câblage d'un disjoncteur cela ne rétablit aucun contrat Faute de **vérification en amont** le contrôle doit se reporter sur les sorties avant qu'elles … »
    - *test de référence* : 1 → 0
    -     retiré : « … appel à une tendance statistique mesurée en moyenne sur des **tests de référence** qui ne garantit aucune réponse particulière La façon dont l'échec … »
    - *frontière en dents de scie* : 1 → 0
    -     retiré : « … ligne En outre la compétence d'un tel modèle dessine une **frontière en dents de scie** remarquable sur une question complexe il peut échouer sur une … »
    - *vérification* : 1 → 2
    -     retiré : « … au code elle sert de comparateur permanent Elle autorise une **vérification** en amont typage tests analyse statique ou preuve formelle confrontent … »
    -     ajouté : « … au code elle sert de comparateur permanent Elle autorise la **vérification** en amont typage tests analyse statique ou preuve formelle confrontent … »
    -     ajouté : « … câblage d'un disjoncteur cela ne rétablit aucun contrat Faute de **vérification** en amont le contrôle doit se reporter sur les sorties … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (25) — décision : 
    - *lecture* : « Munis de cette grille de **lecture** tournons-nous vers l'informatique Pourquoi pouvons-nous empiler … »
    - *vérifier* : « … de base de données sans devoir **vérifier** une à une chacune des réponses … »
    - *fournit* : « … tri promet que si on lui **fournit** une liste d'éléments comparables elle rendra … »
    - *obstacle* : « … naturel L'apprentissage automatique a franchi cet **obstacle** en inversant la démarche au lieu … »
    - *opération* : « … former un composant appris Dans cette **opération** la garantie préalable n'a pas été … »
    - *acheter* : « … elle a été délibérément dépensée pour **acheter** une portée nouvelle précisément sur les … »
    - *précisément* : « … dépensée pour acheter une portée nouvelle **précisément** sur les tâches rebelles à toute … »
    - *cherche* : « … fonction de coût ce que l'optimisation **cherche** à réduire et des préférences d'évaluation … »
    - *réduire* : « … coût ce que l'optimisation cherche à **réduire** et des préférences d'évaluation où personne … »
    - *simultanément* : « … de régime où trois propriétés basculent **simultanément** Ce qui est promis on passe … »
    - *référence* : « … en moyenne sur des tests de **référence** qui ne garantit aucune réponse particulière … »
    - *définissable* : « … basses une erreur est un écart **définissable** par rapport à une règle écrite … »
    - *rapport* : « … erreur est un écart définissable par **rapport** à une règle écrite même lorsqu'elle … »
    - *martienne* : « … celle des unités de la sonde **martienne** au sommet elle prend la forme … »
    - *identique* : « … d'un texte fluide poli et assuré **identique** en surface à une réponse juste … »
    - *avocats* : « … l'ont appris à leurs dépens les **avocats** de l'affaire Mata v Avianca Le … »
    - *atterrit* : « … Mata v Avianca Le lieu où **atterrit** l'enquête après coup il n'y a … »
    - *insérer* : « … il n'y a plus d'adresse où **insérer** un correctif local on ne répare … »
    - *dessine* : « … outre la compétence d'un tel modèle **dessine** une frontière en dents de scie … »
    - *frontière* : « … compétence d'un tel modèle dessine une **frontière** en dents de scie remarquable sur … »
    - *remarquable* : « … une frontière en dents de scie **remarquable** sur une question complexe il peut … »
    - *question* : « … dents de scie remarquable sur une **question** complexe il peut échouer sur une … »
    - *franchir* : « … réponse ne signale qu'il vient de **franchir** sa limite L'interroger plusieurs fois et … »
    - *pouvoir* : « … rétablit pas un contrat Faute de **pouvoir** vérifier en amont un tel composant … »
    - *deviennent* : « … une à une avant qu'elles ne **deviennent** des actes »
- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 2 → 2 (reformulé autour)
    - retiré : « … en dents de scie remarquable sur une question complexe il **peut** échouer sur une variante voisine d'apparence anodine sans que rien … »
    - ajouté : « … dents de scie capable sur un problème complexe le modèle **peut** échouer sur une variante voisine d'apparence anodine sans rien laisser … »
- · Quantificateurs absolus — *tout / tous / toute(s)* : 3 → 3 (reformulé autour)
    - retiré : « … en service et ce contrôle fait une fois vaut pour **toutes** ses exécutions futures Les tests ne prouvent jamais l'absence d'erreur … »
    - retiré : « … acheter une portée nouvelle précisément sur les tâches rebelles à **toute** règle explicite La spécification n'a pas disparu mais elle a … »
    - ajouté : « … contrat explicite Une fonction de tri promet de rendre pour **toute** liste d'éléments comparables une permutation ordonnée de cette même liste … »
    - ajouté : « … demeure on vérifie d'avance Et quand le logiciel échoue malgré **tout** en exploitation le contrat ou la clause qu'on aurait dû … »
- · Quantificateurs absolus — *aucun(e)* : 1 → 1 (reformulé autour)
    - retiré : « … en moyenne sur des tests de référence qui ne garantit **aucune** réponse particulière La façon dont l'échec se présente dans les … »
    - ajouté : « … au dressage plutôt qu'au câblage d'un disjoncteur cela ne rétablit **aucun** contrat Faute de vérification en amont le contrôle doit se … »
- · Quantificateurs absolus — *rien* : 1 → 1 (reformulé autour)
    - retiré : « … peut échouer sur une variante voisine d'apparence anodine sans que **rien** dans le ton de sa réponse ne signale qu'il vient … »
    - ajouté : « … modèle peut échouer sur une variante voisine d'apparence anodine sans **rien** laisser paraître dans le ton de sa réponse L'interroger plusieurs … »
- · Statut épistémique — *démontrer / prouver* : 2 → 2 (reformulé autour)
    - retiré : « … fois vaut pour toutes ses exécutions futures Les tests ne **prouvent** jamais l'absence d'erreur mais le geste reste le même on … »
    - ajouté : « … une fois pour toutes les exécutions futures Les tests ne **prouvent** pas l'absence d'erreur mais le principe demeure on vérifie d'avance … »
- · Mots pleins : 0 variante(s), 23 ajout(s)
    - ajoutés : contrôler, principe, demeure, corriger, rédiger, formuler, échange, acquérir, écrites, objectif, ensemble, succède, batteries, contredit, climate, orbiter, indiscernable, aboutit, capable, problème, laisser, paraître, changent

## `sec:ch00-automatisation` — Ce que l’automatisation fait aux contrôles

- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *chaîne* : 1 → 0
    -     retiré : « … agit simultanément sur trois leviers elle met les étapes en **chaîne** elle retire des contrôles humains implicites et elle corrèle les … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (5) — décision : 
    - *interrogés* : « … composants appris ne sont plus seulement **interrogés** isolément par un lecteur prudent mais … »
    - *isolément* : « … appris ne sont plus seulement interrogés **isolément** par un lecteur prudent mais intégrés … »
    - *prudent* : « … seulement interrogés isolément par un lecteur **prudent** mais intégrés au cœur des flux … »
    - *intégrés* : « … isolément par un lecteur prudent mais **intégrés** au cœur des flux de travail … »
    - *organisations* : « … des flux de travail et des **organisations** L'automatisation agit simultanément sur trois leviers … »
- · Quantificateurs absolus — *seul(e) / seulement / uniquement* : 1 → 1 (reformulé autour)
    - retiré : « Que se passe-t-il lorsque ces composants appris ne sont plus **seulement** interrogés isolément par un lecteur prudent mais intégrés au cœur … »
    - ajouté : « Que se passe-t-il lorsque ces composants appris ne servent plus **seulement** à répondre à un lecteur attentif mais s'intègrent au cœur … »
- · Mots pleins : 0 variante(s), 5 ajout(s)
    - ajoutés : servent, répondre, attentif, intègrent, enchaîne

## `sec:ch00-auto-chaines` — L’automatisation met les étapes en chaîne et fait passer les erreurs à l’acte

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (4) — décision : 
    - *traitement* : « … on assemble désormais des chaînes de **traitement** où un modèle extrait des informations … »
    - *informations* : « … traitement où un modèle extrait des **informations** les résume planifie une suite d'étapes … »
    - *attendent* : « … de la production de réponses qui **attendent** un lecteur à l'exécution d actions … »
    - *quiconque* : « … ou engagent une transaction avant que **quiconque** ait pu les relire On confie … »
- · Mots pleins : 2 variante(s), 3 ajout(s)
    - variantes probables : structurellement → structurel, opérationnellement → opérationnel
    - ajoutés : soumises, relecture, revient

## `sec:ch00-auto-erosion` — L’automatisation érode les vérifications humaines

- [ ] ⚠ Quantificateurs absolus — *jamais* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … chemin des résultats intermédiaires susceptibles de se contredire Personne n'avait **jamais** inscrit cette boucle de rétroaction sur les organigrammes aussi sa … »
- [ ] ⚠ Statut épistémique — *établir* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … s'exprime de la même voix posée lorsqu'il restitue un fait **établi** et lorsqu'il invente une référence rien dans la forme ne … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *consigne* : 2 → 1
    -     retiré : « … sa disparition lorsqu'une réponse complète jaillit en quelques secondes d'une **consigne** passe-t-elle inaperçue jusqu'au jour où une énormité traverse tout le … »
    -     retiré : « … du modèle deux pièges referment le contrôle sur lui-même la **consigne** soumise par l'utilisateur transmet déjà son propre cadre à la … »
    -     ajouté : « … du modèle deux pièges referment le contrôle sur lui-même la **consigne** transmise à la machine lui cède déjà le cadre du … »
- [ ] ⚠ Citations modifiées dans la section (invariant 3) — décision : 
    - ajoutées : @becker2025 (vérifier qu'elles soutiennent la phrase où elles sont placées)
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (32) — décision : 
    - *traditionnel* : « Dans le travail analytique **traditionnel** la lenteur avait une vertu cachée … »
    - *engendrait* : « … avait une vertu cachée la friction **engendrait** des comparateurs En nettoyant ses données … »
    - *données* : « … engendrait des comparateurs En nettoyant ses **données** en posant ses équations à la … »
    - *susceptibles* : « … croisait en chemin des résultats intermédiaires **susceptibles** de se contredire Personne n'avait jamais … »
    - *complète* : « … organigrammes aussi sa disparition lorsqu'une réponse **complète** jaillit en quelques secondes d'une consigne … »
    - *jaillit* : « … aussi sa disparition lorsqu'une réponse complète **jaillit** en quelques secondes d'une consigne passe-t-elle … »
    - *secondes* : « … lorsqu'une réponse complète jaillit en quelques **secondes** d'une consigne passe-t-elle inaperçue jusqu'au jour … »
    - *passe-t-elle* : « … jaillit en quelques secondes d'une consigne **passe-t-elle** inaperçue jusqu'au jour où une énormité … »
    - *énormité* : « … passe-t-elle inaperçue jusqu'au jour où une **énormité** traverse tout le processus En même … »
    - *processus* : « … où une énormité traverse tout le **processus** En même temps disparaît un indice … »
    - *disparaît* : « … tout le processus En même temps **disparaît** un indice précieux de la vie … »
    - *précieux* : « … En même temps disparaît un indice **précieux** de la vie ordinaire le signe … »
    - *aventure* : « … signe révélateur du doute Lorsqu'un collègue **s'aventure** hors de son domaine de compétence … »
    - *domaine* : « … Lorsqu'un collègue s'aventure hors de son **domaine** de compétence son hésitation ses précautions … »
    - *compétence* : « … s'aventure hors de son domaine de **compétence** son hésitation ses précautions de langage … »
    - *précautions* : « … domaine de compétence son hésitation ses **précautions** de langage ou le caractère brouillon … »
    - *langage* : « … compétence son hésitation ses précautions de **langage** ou le caractère brouillon de son … »
    - *éveillent* : « … de son texte nous alertent et **éveillent** notre vigilance Un modèle génératif s'exprime … »
    - *vigilance* : « … texte nous alertent et éveillent notre **vigilance** Un modèle génératif s'exprime de la … »
    - *exprime* : « … éveillent notre vigilance Un modèle génératif **s'exprime** de la même voix posée lorsqu'il … »
    - *évoquée* : « … trahit plus l'erreur L'étude de METR **évoquée** plus haut montre d'ailleurs combien l'impression … »
    - *combien* : « … METR évoquée plus haut montre d'ailleurs **combien** l'impression d'efficacité peut s'écarter de la … »
    - *efficacité* : « … plus haut montre d'ailleurs combien l'impression **d'efficacité** peut s'écarter de la mesure même … »
    - *experts* : « … de la mesure même chez des **experts** de leur propre domaine Plus largement … »
    - *compris* : « … un code qui compile exigeait d'avoir **compris** le fond du problème la qualité … »
    - *qualité* : « … compris le fond du problème la **qualité** de la forme constituait un signal … »
    - *parfaite* : « … lors que la mise en forme **parfaite** devient quasi gratuite tandis que la … »
    - *coûteuse* : « … sur le fond reste lente et **coûteuse** les travaux vérifiés et les productions … »
    - *vérifiés* : « … reste lente et coûteuse les travaux **vérifiés** et les productions superficielles deviennent indiscernables … »
    - *productions* : « … coûteuse les travaux vérifiés et les **productions** superficielles deviennent indiscernables au premier coup … »
    - *soumise* : « … le contrôle sur lui-même la consigne **soumise** par l'utilisateur transmet déjà son propre … »
    - *utilisateur* : « … sur lui-même la consigne soumise par **l'utilisateur** transmet déjà son propre cadre à … »
- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 1 → 1 (reformulé autour)
    - retiré : « … de METR évoquée plus haut montre d'ailleurs combien l'impression d'efficacité **peut** s'écarter de la mesure même chez des experts de leur … »
    - ajouté : « … plus haut montre aussi à quel point l'impression de vitesse **peut** s'écarter du temps mesuré même chez des spécialistes travaillant sur … »
- · Modaux et atténuateurs — *presque / quasi / à peu près / environ* : 1 → 1 (reformulé autour)
    - retiré : « … fond Dès lors que la mise en forme parfaite devient **quasi** gratuite tandis que la vérification sur le fond reste lente … »
    - ajouté : « … crédible de solidité Dès lors que la belle forme devient **presque** gratuite tandis que la vérification de fond reste lente et … »
- · Statut épistémique — *montrer* : 1 → 1 (reformulé autour)
    - retiré : « … ne trahit plus l'erreur L'étude de METR évoquée plus haut **montre** d'ailleurs combien l'impression d'efficacité peut s'écarter de la mesure même … »
    - ajouté : « … ne trahit plus l'incertitude L'essai de METR cité plus haut **montre** aussi à quel point l'impression de vitesse peut s'écarter du … »
- · Mots pleins : 3 variante(s), 28 ajout(s)
    - variantes probables : attendu → attente, superficielles → superficiels, transmet → transmise
    - ajoutés : remplissait, fonction, discrète, fabriquait, tableaux, programme, capables, instantanée, grossière, circuit, interne, courant, coopération, humaine, maîtrise, réserves, inachevé, destinataire, incertitude, vitesse, spécialistes, travaillant, terrain, travaillé, formelle, onéreuse, satisfaire, favorise

## `sec:ch00-auto-correlation` — L’automatisation corrèle les angles morts à l’échelle collective

- [ ] ⚠ Modaux et atténuateurs — *tendre à* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … contrôleur puisent désormais à la même source leur contrôle croisé **tend à** se réduire à une copie et la probabilité d'échappement de … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (17) — décision : 
    - *phénomène* : « … nombre de modèles de fondation un **phénomène** subtil se produit Vis-à-vis des étourderies … »
    - *vis-à-vis* : « … fondation un phénomène subtil se produit **Vis-à-vis** des étourderies propres à chaque individu … »
    - *constitue* : « … propres à chaque individu le modèle **constitue** un comparateur réel le taux d'erreur … »
    - *diminue* : « … comparateur réel le taux d'erreur individuel **diminue** Mais pour les erreurs qui relèvent … »
    - *relèvent* : « … diminue Mais pour les erreurs qui **relèvent** de l'angle mort du modèle lui-même … »
    - *dégénère* : « … la même source leur contrôle croisé **dégénère** en copie et la probabilité d'échappement … »
    - *aggrave* : « … ces erreurs partagées bondit Ce phénomène **s'aggrave** lorsque les textes et les codes … »
    - *engendrés* : « … lorsque les textes et les codes **engendrés** par les modèles retournent alimenter le … »
    - *retournent* : « … les codes engendrés par les modèles **retournent** alimenter le Web les dépôts logiciels … »
    - *pression* : « … indépendants Au même moment sous la **pression** du volume de production que ces … »
    - *production* : « … sous la pression du volume de **production** que ces outils rendent possible la … »
    - *rendent* : « … volume de production que ces outils **rendent** possible la tentation est forte pour … »
    - *possible* : « … de production que ces outils rendent **possible** la tentation est forte pour les … »
    - *tentation* : « … que ces outils rendent possible la **tentation** est forte pour les institutions de … »
    - *institutions* : « … la tentation est forte pour les **institutions** de comprimer le budget et le … »
    - *ressource* : « … et le temps alloués à la **ressource** pourtant devenue le véritable goulet d'étranglement … »
    - *devenue* : « … temps alloués à la ressource pourtant **devenue** le véritable goulet d'étranglement l'évaluation indépendante »
- · Mots pleins : 0 variante(s), 10 ajout(s)
    - ajoutés : échelle, apparaît, abaisse, appartiennent, réduire, corrélation, accentue, reviennent, reprises, organisations

## `sec:ch00-enigme-arithmetique` — L’énigme arithmétique du producteur plus fiable et du système plus risqué

- [ ] ⚠ Quantificateurs absolus — *jamais* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … résume pourquoi l'amélioration des performances moyennes d'un outil ne suffit **jamais** à elle seule à garantir la sécurité d'un système Puisqu'une … »
- [ ] ⚠ Quantificateurs absolus — *seul(e) / seulement / uniquement* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … des performances moyennes d'un outil ne suffit jamais à elle **seule** à garantir la sécurité d'un système Puisqu'une affirmation fausse ne … »
    - retiré : « … de référence et les courbes de performance notent le producteur **seul** ils ne mesurent que le premier facteur toute la question … »
    - ajouté : « … pourquoi l'amélioration moyenne d'un outil ne garantit pas à elle **seule** la sûreté d'un système Puisqu'une affirmation fausse ne nuit que … »
- [ ] ⚠ Force de l'affirmation — *suffire* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … élémentaire résume pourquoi l'amélioration des performances moyennes d'un outil ne **suffit** jamais à elle seule à garantir la sécurité d'un système … »
- [ ] ⚠ Statut épistémique — *montrer* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « Un calcul élémentaire **montre** pourquoi l'amélioration moyenne d'un outil ne garantit pas à elle … »
- [ ] ⚠ Statut épistémique — *résultat* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … première le producteur se trompe dans des cas mais ses **résultats** passent par un contrôle qui se trompe autrement que lui … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *affirmation* : 5 → 2
    -     retiré : « … deux facteurs le taux d'erreur du producteur la proportion d **affirmations** fausses qu'il émet et la probabilité d'échappement la proportion de … »
    -     retiré : « … qu'il émet et la probabilité d'échappement la proportion de ces **affirmations** fausses qui franchissent les contrôles sans être contredites à temps … »
    -     retiré : « … et ne laisse échapper que des erreurs la part des **affirmations** qui parviennent fausses jusqu'à l'action vaut alors dans la seconde … »
    - *taux d'erreur* : 2 → 1
    -     retiré : « … porte sur le second De surcroît à mesure que le **taux d'erreur** d'un producteur baisse les vraies erreurs se raréfient alors que … »
    - *producteur* : 6 → 5
    -     retiré : « … est le produit de deux facteurs le taux d'erreur du **producteur** la proportion d'affirmations fausses qu'il émet et la probabilité d'échappement … »
    -     retiré : « … parviennent fausses jusqu'à l'action vaut alors dans la seconde le **producteur** désormais assisté d'un modèle ne se trompe plus que dans … »
    -     retiré : « … part des affirmations fausses suivies d'effet atteint Bien que son **producteur** soit dix fois plus exact la seconde organisation laisse passer … »
    -     ajouté : « … est le produit de deux facteurs le taux d'erreur du **producteur** et la probabilité d'échappement des contrôles Comparons deux organisations fictives … »
    -     ajouté : « … fausses qui atteignent l'action vaut alors dans la seconde le **producteur** assisté d'un modèle ne se trompe plus que dans des … »
    -     ajouté : « … part des erreurs suivies d'effet à Bien que le second **producteur** soit dix fois plus exact le système laisse passer neuf … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (17) — décision : 
    - *performances* : « … calcul élémentaire résume pourquoi l'amélioration des **performances** moyennes d'un outil ne suffit jamais … »
    - *sécurité* : « … à elle seule à garantir la **sécurité** d'un système Puisqu'une affirmation fausse ne … »
    - *dommage* : « … Puisqu'une affirmation fausse ne cause de **dommage** que si elle débouche sur une … »
    - *débouche* : « … cause de dommage que si elle **débouche** sur une action sans avoir été … »
    - *contredites* : « … qui franchissent les contrôles sans être **contredites** à temps Comparons deux organisations imaginaires … »
    - *imaginaires* : « … contredites à temps Comparons deux organisations **imaginaires** avec des chiffres choisis pour l'illustration … »
    - *échapper* : « … autrement que lui et ne laisse **échapper** que des erreurs la part des … »
    - *parviennent* : « … erreurs la part des affirmations qui **parviennent** fausses jusqu'à l'action vaut alors dans … »
    - *présentent* : « … des cas mais ses erreurs se **présentent** avec la même aisance que ses … »
    - *relisent* : « … pas d'adresse et ceux qui le **relisent** consultent le même modèle d'entre elles … »
    - *consultent* : « … d'adresse et ceux qui le relisent **consultent** le même modèle d'entre elles passent … »
    - *organisation* : « … dix fois plus exact la seconde **organisation** laisse passer neuf fois plus d'erreurs … »
    - *courbes* : « … les tests de référence et les **courbes** de performance notent le producteur seul … »
    - *surcroît* : « … contrôles porte sur le second De **surcroît** à mesure que le taux d'erreur … »
    - *raréfient* : « … producteur baisse les vraies erreurs se **raréfient** alors que le taux de fausses … »
    - *imparfait* : « … taux de fausses alertes d'un contrôleur **imparfait** reste le même une part croissante … »
    - *reçoivent* : « … fausses alertes Si ceux qui les **reçoivent** finissent par moins les écouter ce … »
- · Force de l'affirmation — *garantir (verbe)* : 1 → 1 (reformulé autour)
    - retiré : « … moyennes d'un outil ne suffit jamais à elle seule à **garantir** la sécurité d'un système Puisqu'une affirmation fausse ne cause de … »
    - ajouté : « Un calcul élémentaire montre pourquoi l'amélioration moyenne d'un outil ne **garantit** pas à elle seule la sûreté d'un système Puisqu'une affirmation … »
- · Mots pleins : 1 variante(s), 13 ajout(s)
    - variantes probables : comportement → comportemental
    - ajoutés : fictives, sorties, atteignent, relecteurs, appuient, portant, deviennent, constant, infondées, opérateurs, phénomène, arithmétique, augmente

## `sec:ch00-remedes` — Ce que nous pouvons encore faire

- [ ] ⚠ Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 3 → 4 (effectif modifié) — décision : 
    - retiré : « … marge d'humilité pour tenir compte de ce que la représentation **pourrait** omettre marge qui relève d'un jugement de prudence et non … »
    - ajouté : « … l'automatisation Il invite à déplacer l'effort là où l'on ne **peut** plus acheter une garantie une fois pour toutes sur l'outil … »
    - ajouté : « … non mesure pour tenir compte de ce que la représentation **peut** omettre et placer devant l'action un verrou où elle attend … »
- [ ] ⚠ Modaux et atténuateurs — *presque / quasi / à peu près / environ* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … compilateur le simulateur ou la suite de tests répondent instantanément **presque** gratuitement et sans effet extérieur irréversible tout en maintenant des … »
- [ ] ⚠ Quantificateurs absolus — *aucun(e)* : 3 → 2 (effectif modifié) — décision : 
    - retiré : « … en information il dispose de quatre questions simples qui n'exigent **aucune** technicité mathématique pour rouvrir le cadre Sous quelles conditions ce … »
- [ ] ⚠ Quantificateurs absolus — *seul(e) / seulement / uniquement* : 2 → 0 (effectif modifié) — décision : 
    - retiré : « … verrou c'est-à-dire un point où elle attend une autorisation accordée **seulement** après un contrôle indépendant Cette distinction éclaire aussi le rôle … »
    - retiré : « … sur trois niveaux complémentaires dont aucun ne suffit à lui **seul** L'attitude individuelle notre expérience du monde déborde souvent le cadre … »
- [ ] ⚠ Force de l'affirmation — *suffire* : 1 → 2 (effectif modifié) — décision : 
    - retiré : « … la défense s'articule sur trois niveaux complémentaires dont aucun ne **suffit** à lui seul L'attitude individuelle notre expérience du monde déborde … »
    - ajouté : « … d'obtention transfert de responsabilité déguisé en information quatre questions simples **suffisent** sans technicité mathématique pour rouvrir le cadre Sous quelles conditions … »
    - ajouté : « … la défense s'appuie sur trois niveaux complémentaires dont aucun ne **suffit** isolément L'attitude individuelle notre expérience du monde déborde souvent le … »
- [ ] ⚠ Lecture des probabilités — *probable / probabilité* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … coup les prévisions aux issues réelles et mesurer concrètement la **probabilité** d'échappement du système de relecture en y glissant périodiquement des … »
- [ ] ⚠ Statut épistémique — *établir* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … à la décision affiche son état de vérification exploratoire ou **établie** ce qui a été contrôlé de façon indépendante et ses … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *contrôle* : 5 → 4
    -     retiré : « … sur l'outil nous devons organiser lucidement nos décisions et nos **contrôles** Du côté de la décision tout commence par la distinction … »
    -     retiré : « … point où elle attend une autorisation accordée seulement après un **contrôle** indépendant Cette distinction éclaire aussi le rôle de l'exploration Puisque … »
    -     retiré : « … images de menaces fictives sur les écrans des opérateurs de **contrôle** des bagages »
    -     ajouté : « … sur l'outil il faut organiser lucidement les décisions et les **contrôles** Du côté de la décision tout commence par le partage … »
    -     ajouté : « … devant l'action un verrou où elle attend une autorisation après **contrôle** indépendant La même distinction éclaire la conduite de l'exploration Puisque … »
    - *probabilité d'échappement* : 1 → 0
    -     retiré : « … coup les prévisions aux issues réelles et mesurer concrètement la **probabilité d'échappement** du système de relecture en y glissant périodiquement des erreurs … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (31) — décision : 
    - *nostalgique* : « … au scepticisme paralysant ni au rejet **nostalgique** de l'automatisation Il invite à déplacer … »
    - *pouvons* : « … notre effort là où nous ne **pouvons** plus acheter une garantie une fois … »
    - *observation* : « … du lendemain trier des demandes courantes **l'observation** des fréquences permet de calibrer le … »
    - *corriger* : « … de calibrer le système et de **corriger** ses seuils au fil de l'eau … »
    - *particulier* : « … moyenne statistique ne protège le cas **particulier** Deux instruments prennent alors le relais … »
    - *instruments* : « … ne protège le cas particulier Deux **instruments** prennent alors le relais ajouter délibérément … »
    - *accordée* : « … point où elle attend une autorisation **accordée** seulement après un contrôle indépendant Cette … »
    - *défaite* : « … réponse coûte peu et peut être **défaite** il est fécond de laisser les … »
    - *intérieur* : « … et les agents explorer librement à **l'intérieur** d'un bac à sable un environnement … »
    - *instantanément* : « … ou la suite de tests répondent **instantanément** presque gratuitement et sans effet extérieur … »
    - *gratuitement* : « … suite de tests répondent instantanément presque **gratuitement** et sans effet extérieur irréversible tout … »
    - *revient* : « … sans ses conditions d'obtention ce qui **revient** à lui transférer une responsabilité déguisée … »
    - *transférer* : « … d'obtention ce qui revient à lui **transférer** une responsabilité déguisée en information il … »
    - *dispose* : « … une responsabilité déguisée en information il **dispose** de quatre questions simples qui n'exigent … »
    - *exigent* : « … dispose de quatre questions simples qui **n'exigent** aucune technicité mathématique pour rouvrir le … »
    - *articule* : « … l'organisation des contrôles enfin la défense **s'articule** sur trois niveaux complémentaires dont aucun … »
    - *exercice* : « … avant de lire la sortie pratiquer **l'exercice** du pré-mortem en supposant que le … »
    - *supposant* : « … sortie pratiquer l'exercice du pré-mortem en **supposant** que le projet a échoué six … »
    - *éventail* : « … les causes et élargir à dessein **l'éventail** des mondes possibles envisagés Le placement … »
    - *humaine* : « … plutôt que de disperser une attention **humaine** limitée ou de se contenter d'un … »
    - *contenter* : « … attention humaine limitée ou de se **contenter** d'un clic d'approbation machinal il faut … »
    - *confier* : « … acte ou une référence et les **confier** à des relecteurs qui partagent l'interface … »
    - *exploratoire* : « … décision affiche son état de vérification **exploratoire** ou établie ce qui a été … »
    - *contrôlé* : « … ou établie ce qui a été **contrôlé** de façon indépendante et ses hypothèses … »
    - *principales* : « … de façon indépendante et ses hypothèses **principales** tenir un historique permettant de confronter … »
    - *permettant* : « … ses hypothèses principales tenir un historique **permettant** de confronter après coup les prévisions … »
    - *glissant* : « … du système de relecture en y **glissant** périodiquement des erreurs injectées à la … »
    - *périodiquement* : « … système de relecture en y glissant **périodiquement** des erreurs injectées à la manière … »
    - *aérienne* : « … à la manière dont la sûreté **aérienne** projette des images de menaces fictives … »
    - *opérateurs* : « … menaces fictives sur les écrans des **opérateurs** de contrôle des bagages »
    - *bagages* : « … écrans des opérateurs de contrôle des **bagages** »
- · Quantificateurs absolus — *tout / tous / toute(s)* : 5 → 5 (reformulé autour)
    - retiré : « … tests répondent instantanément presque gratuitement et sans effet extérieur irréversible **tout** en maintenant des verrous stricts à chaque frontière où l'action … »
    - ajouté : « … tests répondent vite à faible coût et sans dégât extérieur **tout** en maintenant des verrous stricts aux frontières qui touchent le … »
- · Quantificateurs absolus — *jamais* : 1 → 1 (reformulé autour)
    - retiré : « … du modèle que nous consultons même si elle ne déborde **jamais** le nôtre l'humilité épistémique consiste alors à produire ses propres … »
    - ajouté : « … du monde déborde souvent le cadre du modèle consulté sans **jamais** déborder le nôtre L'humilité épistémique consiste alors à produire ses … »
- · Statut épistémique — *hypothèse* : 1 → 1 (reformulé autour)
    - retiré : « … ce qui a été contrôlé de façon indépendante et ses **hypothèses** principales tenir un historique permettant de confronter après coup les … »
    - ajouté : « … soumise à décision affiche son état de vérification et ses **hypothèses** tenir un historique confrontant prévisions et issues réelles mesurer concrètement … »
- · Mots pleins : 9 variante(s), 13 ajout(s)
    - variantes probables : toucherait → touchent, déguisée → déguisé, consultons → consulté, consulter → consulté, imaginer → imaginant, approbation → approbations, budgétaire → budgétée, confronter → confrontant, projette → projetées
    - ajoutés : ajuster, singulier, garde-fous, annulée, transfert, isolément, déborder, regarder, multiplier, ressource, plafonner, production, aéroportuaire

## `sec:ch00-architecture` — Architecture de l’ouvrage

- [ ] ⚠ Quantificateurs absolus — *tout / tous / toute(s)* : 6 → 4 (effectif modifié) — décision : 
    - retiré : « … qui valent en réalité pour toute représentation finie et pour **tout** dispositif de contrôle Le parcours s'organise donc en cinq parties … »
    - retiré : « … outils de logique et de calcul des probabilités utilisés dans **tout** le livre conditionnement règle de Bayes sous forme de cotes … »
    - retiré : « … le recours aux mêmes modèles abaisse le taux d'erreur individuel **tout** en élevant la probabilité d'échappement par corrélation des angles morts … »
    - retiré : « … l'action Enfin la conclusion soumet l'ouvrage à ses propres critères **Tout** au long de ces cinq parties le lecteur retrouvera d'un … »
    - ajouté : « … artificielle des mécanismes qui valent pour toute représentation finie et **tout** dispositif de contrôle L'argument se déploie donc en cinq parties … »
    - ajouté : « … comment l'usage collectif des mêmes modèles abaisse les erreurs individuelles **tout** en élevant l'échappement par corrélation des angles morts blanchiment de … »
- [ ] ⚠ Quantificateurs absolus — *toujours* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … cadre en montrant pourquoi la rigueur déductive ou inductive reste **toujours** relative au cadre choisi Le développe la lecture de la … »
- [ ] ⚠ Quantificateurs absolus — *seul(e) / seulement / uniquement* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … la conclusion et l'impossibilité de juger un prévisionniste sur une **seule** issue Le relie enfin croyance et action par l'utilité espérée … »
- [ ] ⚠ Lecture des probabilités — *probable / probabilité* : 5 → 3 (effectif modifié) — décision : 
    - retiré : « … manière unifiée les outils de logique et de calcul des **probabilités** utilisés dans tout le livre conditionnement règle de Bayes sous … »
    - retiré : « … la décomposition du risque en taux d'erreur multiplié par la **probabilité** d'échappement La De l'informatique classique à l'IA chapitres à applique … »
    - retiré : « … modèles abaisse le taux d'erreur individuel tout en élevant la **probabilité** d'échappement par corrélation des angles morts blanchiment de provenance et … »
    - ajouté : « … décideur isolé Le unifie les outils de logique et de **probabilité** employés dans la suite conditionnement règle de Bayes en cotes … »
- [ ] ⚠ Statut épistémique — *montrer* : 3 → 1 (effectif modifié) — décision : 
    - retiré : « … amont et à l'existence d'une adresse pour chaque défaillance Le **montre** ce qui change lorsque la spécification passe dans les données … »
    - retiré : « … pièges de la consigne Le passe à l'échelle collective pour **montrer** comment le recours aux mêmes modèles abaisse le taux d'erreur … »
- [ ] ⚠ Statut épistémique — *établir* : 3 → 2 (effectif modifié) — décision : 
    - retiré : « Pour **établir** chacune de ces thèses sans pétition de principe l'ouvrage suit … »
    - retiré : « … relie enfin croyance et action par l'utilité espérée subjective et **établit** le seuil de décision noté face à une décision unique … »
    - retiré : « … multiphysiques Le distingue les incertitudes aléatoire épistémique et ontologique et **établit** notre première proposition une barre d'erreur ne mesure que le … »
    - ajouté : « Pour **établir** ces thèses sans pétition de principe le livre suit une … »
    - ajouté : « … multiphysiques Le distingue les incertitudes aléatoire épistémique et ontologique et **établit** la première proposition une barre d'erreur ne mesure que le … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *cadre* : 9 → 8
    -     retiré : « … deux axes le lieu de la cause d'erreur dans le **cadre** ou hors du cadre et le comportement des contrôles erreur … »
    - *contrôle* : 9 → 7
    -     retiré : « … réalité pour toute représentation finie et pour tout dispositif de **contrôle** Le parcours s'organise donc en cinq parties figure Architecture de … »
    -     retiré : « … l'érosion des vérifications humaines disparition de la friction génératrice de **contrôles** perte du signe révélateur de l'incertitude effondrement du signal par … »
    -     retiré : « … par erreurs injectées et se clôt sur cinq questions de **contrôle** avant l'action Enfin la conclusion soumet l'ouvrage à ses propres … »
    -     ajouté : « … qui valent pour toute représentation finie et tout dispositif de **contrôle** L'argument se déploie donc en cinq parties figure Architecture de … »
    - *comparateur* : 3 → 2
    -     retiré : « … ensemble d'alternatives admises Le définit l'affirmation le contrôle et le **comparateur** et déploie les cinq conditions nécessaires à la détection d'une … »
    -     retiré : « … à la régression Le analyse le compromis entre l'indépendance d'un **comparateur** et sa comparabilité quatrième proposition oppose les chaînes aux contrôles … »
    -     retiré : « … silencieuse puis passe en revue les quatre sources possibles de **comparateurs** ainsi que la distinction entre vérification et validation La L'automatisation … »
    -     ajouté : « … entre alternatives admises Le définit l'affirmation le contrôle et le **comparateur** puis déploie les cinq conditions nécessaires à la détection d'une … »
    -     ajouté : « … signalée ou silencieuse passe en revue les quatre sources de **comparateurs** et situe vérification et validation sur cette matrice La L'automatisation … »
    - *taux d'erreur* : 2 → 1
    -     retiré : « … pour montrer comment le recours aux mêmes modèles abaisse le **taux d'erreur** individuel tout en élevant la probabilité d'échappement par corrélation des … »
    - *probabilité d'échappement* : 3 → 1
    -     retiré : « … modèles abaisse le taux d'erreur individuel tout en élevant la **probabilité d'échappement** par corrélation des angles morts blanchiment de provenance et assèchement … »
    -     retiré : « … modèles abaisse le taux d'erreur individuel tout en élevant la **probabilité d'échappement** par corrélation des angles morts blanchiment de provenance et assèchement … »
    - *chaîne* : 3 → 2
    -     retiré : « … artificielle ingénierie mécanique accidents industriels finance dépistage médical programmation multiversion **chaînes** de calcul multiphysiques Le distingue les incertitudes aléatoire épistémique et … »
    - *erreur silencieuse* : 1 → 0
    -     retiré : « … du cadre et le comportement des contrôles erreur signalée ou **erreur silencieuse** puis passe en revue les quatre sources possibles de comparateurs … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (44) — décision : 
    - *commençait* : « … avant d'aborder les serrures Si l'on **commençait** par décrire les modèles de langage … »
    - *décrire* : « … les serrures Si l'on commençait par **décrire** les modèles de langage et les … »
    - *risquerait* : « … langage et les agents logiciels on **risquerait** de prendre pour des curiosités passagères … »
    - *curiosités* : « … on risquerait de prendre pour des **curiosités** passagères de l'intelligence artificielle des mécanismes … »
    - *réalité* : « … artificielle des mécanismes qui valent en **réalité** pour toute représentation finie et pour … »
    - *parcours* : « … pour tout dispositif de contrôle Le **parcours** s'organise donc en cinq parties figure … »
    - *rappelle* : « … base pour un décideur isolé Le **rappelle** de manière unifiée les outils de … »
    - *manière* : « … un décideur isolé Le rappelle de **manière** unifiée les outils de logique et … »
    - *unifiée* : « … décideur isolé Le rappelle de manière **unifiée** les outils de logique et de … »
    - *utilisés* : « … logique et de calcul des probabilités **utilisés** dans tout le livre conditionnement règle … »
    - *distinction* : « … logarithmique de surprise Le introduit la **distinction** entre le monde et la représentation … »
    - *explicite* : « … entre le monde et la représentation **explicite** le schéma des règles à conditions … »
    - *lecture* : « … au cadre choisi Le développe la **lecture** de la probabilité comme jugement pesant … »
    - *chercher* : « … possibles l'habitude de raisonner à l'envers **chercher** quelle variation cachée de l'arrière-plan renverserait … »
    - *variation* : « … de raisonner à l'envers chercher quelle **variation** cachée de l'arrière-plan renverserait la conclusion … »
    - *arrière-plan* : « … l'envers chercher quelle variation cachée de **l'arrière-plan** renverserait la conclusion et l'impossibilité de … »
    - *renverserait* : « … chercher quelle variation cachée de l'arrière-plan **renverserait** la conclusion et l'impossibilité de juger … »
    - *constitue* : « … qui peut nous détromper chapitres à **constitue** le cœur théorique et formel de … »
    - *délibérément* : « … éprouver la généralité ses exemples sont **délibérément** pris hors de l'intelligence artificielle ingénierie … »
    - *ingénierie* : « … délibérément pris hors de l'intelligence artificielle **ingénierie** mécanique accidents industriels finance dépistage médical … »
    - *quelles* : « … aveugles aux facteurs omis précise à **quelles** conditions les données d'observation peuvent révéler … »
    - *diminue* : « … le taux de base des erreurs **diminue** et la décomposition du risque en … »
    - *conquis* : « … composants spécifiés de l'informatique classique ont **conquis** leur fiabilité grâce aux contrats écrits … »
    - *existence* : « … la vérification en amont et à **l'existence** d'une adresse pour chaque défaillance Le … »
    - *devient* : « … la plausibilité et non la vérité **devient** l'objectif d'optimisation et orienter un modèle … »
    - *simultané* : « … au sommet de la pile basculement **simultané** de la promesse de la forme … »
    - *rassemble* : « … et l'invention de faits rares Le **rassemble** les fils des parties et en … »
    - *croisant* : « … les fils des parties et en **croisant** deux axes le lieu de la … »
    - *comportement* : « … ou hors du cadre et le **comportement** des contrôles erreur signalée ou erreur … »
    - *réutilisant* : « … la dynamique opérationnelle de l'automatisation en **réutilisant** les modèles formels de la Le … »
    - *exécutent* : « … comme des chaînes dont les erreurs **s'exécutent** directement dans le monde Le analyse … »
    - *recours* : « … l'échelle collective pour montrer comment le **recours** aux mêmes modèles abaisse le taux … »
    - *assèchement* : « … angles morts blanchiment de provenance et **assèchement** des capacités d'évaluation La Décider et … »
    - *introduisant* : « … modèle de décision du en y **introduisant** un risque omis par le cadre … »
    - *domaines* : « … et une marge d'humilité distingue les **domaines** qui relèvent de la calibration et … »
    - *relèvent* : « … marge d'humilité distingue les domaines qui **relèvent** de la calibration et ceux qui … »
    - *exigent* : « … de la calibration et ceux qui **exigent** un verrou articule bacs à sable … »
    - *lecteur* : « … long de ces cinq parties le **lecteur** retrouvera d'un chapitre à l'autre un … »
    - *retrouvera* : « … de ces cinq parties le lecteur **retrouvera** d'un chapitre à l'autre un petit … »
    - *progresse* : « … s'enrichissent à mesure que l'appareil conceptuel **progresse** la course de voiliers de M … »
    - *portant* : « … et ainsi que les cas documentés **portant** sur l'usage contemporain des modèles de … »
    - *portera* : « … des cinq propositions structurantes de la **portera** explicitement son statut épistémique définition résultat … »
    - *limites* : « … sera suivie d'un examen de ses **limites** de robustesse Trois modèles formels portent … »
    - *portent* : « … limites de robustesse Trois modèles formels **portent** l'argument le modèle M des angles … »
- · Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 2 → 2 (reformulé autour)
    - retiré : « … aux facteurs omis précise à quelles conditions les données d'observation **peuvent** révéler un tel facteur troisième proposition et explique pourquoi aucune … »
    - ajouté : « … internes aux facteurs omis précise quand les observations du monde **peuvent** révéler un tel facteur troisième proposition et explique pourquoi aucune … »
- · Lecture des probabilités — *vraisemblable / vraisemblance* : 1 → 1 (reformulé autour)
    - retiré : « … conditionnement règle de Bayes sous forme de cotes rapport de **vraisemblance** score logarithmique de surprise Le introduit la distinction entre le … »
    - ajouté : « … la suite conditionnement règle de Bayes en cotes rapport de **vraisemblance** et score logarithmique de surprise Le sépare le monde de … »
- · Statut épistémique — *argument* : 2 → 2 (reformulé autour)
    - retiré : « … de ses limites de robustesse Trois modèles formels portent l **argument** le modèle M des angles morts et de l'échappement chapitres … »
    - ajouté : « … pour toute représentation finie et tout dispositif de contrôle L **argument** se déploie donc en cinq parties figure Architecture de l'ouvrage … »
- · Mots pleins : 6 variante(s), 27 ajout(s)
    - variantes probables : observation → observations, examine → examiner, collective → collectif, individuel → individuelles, enrichissent → enrichit, annoncé → annonce
    - ajoutés : commencer, exposerait, singularités, employés, formalise, demeure, restent, calculs, localisable, passage, remplace, conjoint, apparence, synthétisent, réponse, matrice, passent, repères, hésitation, saturation, pratiques, réclame, reviennent, affiche, discussion, critique, soutiennent

## `sec:ch00-parcours` — Parcours de lecture

- [ ] ⚠ Statut épistémique — *établir* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … l'ouverture de chaque chapitre rappelle en quelques lignes les notions **établies** en amont sur lesquelles il s'appuie avec un renvoi vers … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *contrat* : 2 → 1
    -     retiré : « … et des contrôles croisés au passage des composants spécifiés par **contrat** aux composants appris jusqu'aux architectures d'agents aux bacs à sable … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (15) — décision : 
    - *habitudes* : « … lecteur aborde ces questions avec les **habitudes** les outils et les urgences de … »
    - *urgences* : « … les habitudes les outils et les **urgences** de son métier Huit parcours sélectifs … »
    - *permettent* : « … de son métier Huit parcours sélectifs **permettent** d'aller droit aux développements les plus … »
    - *préoccupation* : « … les plus directement reliés à une **préoccupation** donnée Afin de rendre ces lectures … »
    - *transversales* : « … donnée Afin de rendre ces lectures **transversales** aisées l'ouverture de chaque chapitre rappelle … »
    - *intuitive* : « … possibles privilégie une entrée concrète et **intuitive** par la philosophie pratique des probabilités … »
    - *fiabilité* : « … d'IA relie la théorie de la **fiabilité** et des contrôles croisés au passage … »
    - *gouvernance* : « … les angles morts collectifs et la **gouvernance** organisationnelle de la vérification Le destinataire … »
    - *organisationnelle* : « … angles morts collectifs et la gouvernance **organisationnelle** de la vérification Le destinataire d'un … »
    - *fournit* : « … destinataire d'un chiffre sûr de lui **fournit** à celui qui reçoit une prévision … »
    - *expertise* : « … prévision un score ou un rapport **d'expertise** sans en avoir bâti le modèle … »
    - *nécessaires* : « … avoir bâti le modèle les clés **nécessaires** pour interroger ses conditions de validité … »
    - *débattues* : « … Nuance et discussion ouverte où sont **débattues** les objections les hypothèses fragiles et … »
    - *ouvrage* : « … fragiles et les questions ouvertes de **l'ouvrage** jusqu'à l'auto-examen final Parcours Chapitres recommandés … »
    - *auto-examen* : « … les questions ouvertes de l'ouvrage jusqu'à **l'auto-examen** final Parcours Chapitres recommandés L'argument principal … »
- · Statut épistémique — *théorie / théorème* : 2 → 2 (reformulé autour)
    - retiré : « … la génération calibrée L'informaticien et le concepteur d'IA relie la **théorie** de la fiabilité et des contrôles croisés au passage des … »
    - ajouté : « … la génération calibrée L'informaticien et le concepteur d'IA relie la **théorie** des contrôles croisés au passage des composants spécifiés aux composants … »
- · Mots pleins : 0 variante(s), 7 ajout(s)
    - ajoutés : continue, contraintes, brièvement, mobilisées, gouvernement, examinées, laissées

## `titre:Points clés` — Points clés

- [ ] ⚠ Quantificateurs absolus — *tout / tous / toute(s)* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … l'apprentissage automatique achète sa portée sur des tâches rebelles à **toute** règle écrite en dépensant cette garantie préalable ses erreurs n'ont … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *affirmation* : 1 → 0
    -     retiré : « … d'un facteur omis n'est détectée à temps que si l **affirmation** rencontre un comparateur capable de se tromper autrement comparable disponible … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (7) — décision : 
    - *construite* : « … monde directement mais d'après une représentation **construite** à l'intérieur d'un cadre fini qui … »
    - *détectée* : « … ou issue d'un facteur omis n'est **détectée** à temps que si l'affirmation rencontre … »
    - *affirmation* : « … n'est détectée à temps que si **l'affirmation** rencontre un comparateur capable de se … »
    - *dépensant* : « … rebelles à toute règle écrite en **dépensant** cette garantie préalable ses erreurs n'ont … »
    - *présentent* : « … erreurs n'ont plus d'adresse et se **présentent** avec la même aisance que ses … »
    - *travers* : « … d'hésitation et corrèle les erreurs à **travers** les communautés qui partagent les mêmes … »
    - *diminue* : « … même lorsque le taux d'erreur individuel **diminue** Face à ce déplacement la maîtrise … »
- · Mots pleins : 0 variante(s), 3 ajout(s)
    - ajoutés : arrêtée, écrites, prennent

