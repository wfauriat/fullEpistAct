# Cartographier le terrain {#sec:ch00 .corps}

Ce chapitre parcourt l’ensemble du livre à vol d’oiseau, avant d’entrer dans le détail des outils, des démonstrations et des cas. Il pose en langage courant la question directrice de l’ouvrage, fait surgir par le récit les notions qui reviendront d’un chapitre à l’autre, et montre comment une théorie générale de la décision et des contrôles éclaire le passage de l’informatique classique à l’intelligence artificielle et à l’automatisation. Aucun terme n’y est encore défini formellement : chacun recevra sa définition précise dans le chapitre qui l’introduit. Le parcours se referme sur l’architecture détaillée des cinq parties et sur huit itinéraires de lecture.

## Trois récits pour poser le problème {#sec:ch00-trois-recits}

Le 23 septembre 1999, la sonde *Mars Climate Orbiter* entamait la manœuvre qui devait la placer en orbite autour de Mars. Elle passa derrière la planète comme prévu, puis l’on n’en reçut plus aucun signal : sa trajectoire l’avait amenée trop près de la surface, dans une atmosphère qu’elle ne pouvait pas traverser intacte [@mco1999]. La commission d’enquête identifia rapidement la cause technique immédiate de la perte. Tout au long du vol, un programme au sol, `SM_FORCES`, calculait l’effet des petites poussées de correction et transmettait ses résultats par fichier à l’équipe de navigation. La spécification d’interface exigeait des newton-secondes, l’unité du Système international ; le programme écrivait des livres-force-secondes, une unité anglo-saxonne. D’un côté à l’autre de l’interface, les nombres voyageaient nus, sans unité, si bien que chaque impulsion était sous-estimée d’un facteur proche de 4,45 [@mco1999]. L’enquête révéla bien d’autres défaillances humaines et organisationnelles — équipes surchargées, alertes sur la trajectoire restées sans suite, absence de recalcul indépendant. Sous ces facteurs se trouvait pourtant un point précis que l’on pouvait désigner du doigt : un fichier de code, et la spécification écrite qu’il enfreignait. La défaillance avait une adresse.

Vingt-quatre ans plus tard, au début de 2023, les avocats du demandeur dans l’affaire *Mata v. Avianca*, devant le tribunal fédéral du district sud de New York, déposèrent un mémoire en réponse à la demande de rejet de la compagnie aérienne [@mata2023]. Le texte était rédigé dans une langue juridique irréprochable et citait une demi-douzaine de décisions de justice avec intitulés, références et extraits entre guillemets. Quand la partie adverse et le juge cherchèrent ces arrêts dans les recueils de jurisprudence, aucun n’existait. L’un des avocats avait consulté un modèle de langage conversationnel, qui avait composé des précédents plausibles de toutes pièces avant d’assurer que ces décisions figuraient bien dans les bases juridiques [@mata2023]. Ici encore, une affirmation fausse avait franchi toutes les étapes jusqu’à un acte officiel, et le tribunal prononça en juin 2023 des sanctions contre les conseils. Mais si l’on cherchait après coup l’équivalent du fichier `SM_FORCES`, on ne trouvait rien. Aucun module n’avait enfreint une spécification écrite, pour la simple raison qu’aucune spécification ne fixe ce qu’un tel modèle doit répondre à une question de droit. Le programme avait fonctionné selon sa construction : il avait prolongé le texte soumis par une suite de mots plausible.

Un troisième épisode, deux ans plus tard, déplace encore l’attention. En 2025, l’institut de recherche METR a conduit un essai contrôlé randomisé auprès de développeurs chevronnés de logiciels libres travaillant sur leurs propres dépôts de code — des projets complexes qu’ils pratiquaient intimement depuis des années [@becker2025]. Chaque tâche réelle de développement ou de correction était tirée au sort pour être réalisée soit avec l’assistance d’outils d’intelligence artificielle récents, soit sans eux.

::: {.cas titre="Productivité mesurée et productivité ressentie chez des développeurs expérimentés" date="2025"}
Dans cette étude, les tâches réalisées avec l’aide d’outils d’intelligence artificielle du début de 2025 ont pris en moyenne environ 19 % de temps de plus que les tâches accomplies sans eux [@becker2025]. Interrogés après coup, les participants estimaient pourtant que ces mêmes outils les avaient rendus environ 20 % plus rapides. Ces chiffres décrivent des outils et des pratiques d’un moment donné ; l’enseignement durable tient à l’inversion de signe entre la mesure et l’impression d’experts travaillant dans leur propre domaine.
:::

Ces trois histoires jalonnent le terrain du livre. Dans la première, une erreur de calcul traverse des mois d’opérations parce que les unités se perdent à l’interface et qu’aucun contrôle indépendant ne recoupe les chiffres ; après l’accident, une règle écrite permet du moins de localiser la faute. Dans la deuxième, l’erreur revêt une prose fluide et assurée, indiscernable en surface d’une réponse exacte, sans violation de règle écrite. Dans la troisième, des experts se méprennent sur le signe même de l’effet de leur outil, prenant un ralentissement mesuré pour un gain de vitesse.

Que s’est-il passé entre la perte de la sonde martienne et ces deux épisodes contemporains ? Et surtout, lorsque nous agissons sur le monde par l’entremise de mesures, de modèles mathématiques, de logiciels et de chaînes automatisées, qu’est-ce qui peut encore nous avertir à temps que nous faisons fausse route ?

## Nous agissons d’après une représentation {#sec:ch00-representation}

Pour répondre à cette question, il faut revenir à la situation élémentaire de tout agent — individu, équipe d’ingénieurs ou institution — qui cherche à modifier le cours des choses. Nous poursuivons un but dans le monde réel, mais nous ne manipulons jamais le monde lui-même au moment de préparer une décision. Nous raisonnons sur une représentation construite pour la circonstance [@fauriat2026frame].

### La mer ne consulte pas nos probabilités {#sec:ch00-mer-probabilites}

Imaginons un navigateur, M. X, qui prépare une course au large et hésite entre deux bateaux : un voilier léger, rapide mais sollicité près de ses limites mécaniques, et un voilier renforcé, plus lourd et moins véloce, mais presque incassable. M. X rassemble ce qu’il sait de la météo, du gréement, de la houle annoncée et de son expérience passée, puis résume son jugement par un chiffre : il estime à 5 % la probabilité de démâter sur le voilier léger. Un second navigateur, M. Y, examine le même bateau et le même bulletin météorologique, mais retient d’autres hypothèses sur la fatigue des matériaux et évalue ce risque à 0,1 %.

Que désigne ce 5 % (ou ce 0,1 %) ? Il ne s’agit ni d’une propriété physique de l’océan ni d’une caractéristique du mât. La traversée à venir ne sera pas « une traversée à 5 % » : le mât tiendra jusqu’à l’arrivée, ou il se brisera. La probabilité énoncée par M. X traduit son jugement, c’est-à-dire le poids qu’il accorde, d’après ce qu’il sait, aux différents mondes possibles compatibles avec ses observations.

Qui avait raison avant le départ ? Ni l’un ni l’autre : chacun a traduit honnêtement les conséquences de ses hypothèses. Une fois la course terminée, l’issue ne les départage guère, du moins dans le cas le plus fréquent. Si le voilier léger arrive intact, chacun voit se réaliser l’issue qu’il jugeait de loin la plus probable, et rien ne distingue vraiment leurs prévisions. Si le mât casse, M. Y sera bien plus surpris que M. X, et l’événement plaidera contre lui ; mais une traversée isolée renseigne sur une prévision, guère sur le prévisionniste. Pour savoir si une annonce de « 70 % de chances de pluie » mesure fidèlement l’incertitude, il faut relever une longue série de jours comparables et vérifier s’il a plu environ sept fois sur dix. Seule la répétition permet d’évaluer ainsi celui qui prévoit : on parlera de calibration.

### Toute règle cache un arrière-plan ouvert {#sec:ch00-regle-cadre}

Pourquoi deux raisonneurs attentifs peuvent-ils diverger ainsi, et pourquoi nos modèles les plus éprouvés restent-ils exposés aux surprises ? Parce qu’aucune règle utilisable ne peut énoncer toutes les conditions nécessaires à sa vérité.

Prenons l’énoncé scolaire par excellence : l’eau bout à 100 °C. Trois mesures au laboratoire le confirment, et nous en tirons une règle générale. Le lendemain, un collègue chauffe son récipient à 101 °C sans voir d’ébullition : il a utilisé une eau fortement salée. Nous précisons donc la règle : l’eau *pure* bout à 100 °C. Un deuxième essai échoue à 104 °C avec de l’eau distillée : le récipient était fermé hermétiquement, comme un autocuiseur. Nous allongeons encore l’énoncé : l’eau pure, *portée à l’air libre*, bout à 100 °C. Mais transporté au sommet du mont Blanc, le même récipient ouvert bout aux alentours de 85 °C.

Chaque fois qu’une règle affirme que des conditions explicites $A$ entraînent une conséquence $B$, elle sous-entend en réalité : « si $A$ est vérifié, *et pourvu que tout un arrière-plan non précisé reste dans son état habituel*, alors $B$ s’ensuit ». C’est le premier des deux repères symboliques utiles dans ce chapitre :

$$ A \cap (\dots) \rightarrow B $$ {#eq:ch00-regle}

La parenthèse $(\dots)$ désigne cet arrière-plan tacite, ouvert d’exceptions possibles — salinité, confinement, altitude, impuretés, nature des parois — qu’aucun manuel ne peut énumérer jusqu’au bout sans rendre la règle inutilisable. Choisir ce qui figure explicitement dans $A$ et ce que l’on relègue en silence dans l’arrière-plan tacite, c’est arrêter un cadre : un ensemble fini de variables, de catégories, de modèles envisageables et d’objectifs à l’intérieur duquel le raisonnement va opérer.

Ce choix précède tout calcul, et aucune rigueur formelle ne permet de s’en affranchir. Qu’un raisonnement procède par déduction à partir d’axiomes ou par induction à partir de données observées, sa garantie demeure strictement conditionnelle. La déduction certifie la conclusion *pourvu que* la description initiale soit fidèle ; l’induction la certifie *pourvu que* le contexte futur ressemble au contexte passé sur les points retenus. La dinde inductiviste qui note chaque matin l’heure à laquelle le fermier lui apporte son grain dispose, à la veille de Noël, d’une série statistique irréprochable. La catastrophe qui l’attend ne vient pas d’une faute de calcul, mais d’une variable absente de son cadre.

### Décider une seule fois face à des enjeux asymétriques {#sec:ch00-decider-enjeux}

Tant qu’une représentation reste sur le papier, ses omissions ne tirent pas à conséquence. Le passage critique a lieu quand nous décidons d’agir d’après ce que nous croyons.

Revenons à nos deux navigateurs devant le voilier léger. Gagner la course sur ce bateau rapide procure un avantage appréciable par rapport au voilier renforcé, mais démâter en pleine mer impose un remorquage coûteux qui dépasse largement le gain espéré. Dans la théorie classique de l’utilité espérée subjective, il devient rationnel de renoncer à l’option risquée dès que la probabilité d’échec retenue dépasse un seuil. Ce seuil s’abaisse à mesure que la perte encourue pèse lourd devant le gain espéré, tous deux mesurés par rapport à l’option sûre :

$$ \text{seuil} = \frac{\text{gain}}{\text{gain} + \text{perte}} $$ {#eq:ch00-seuil}

Si la casse coûte vingt-cinq fois le gain d’une victoire, le seuil vaut 1/26, soit un peu moins de 4 %. M. X, qui évalue le risque à 5 %, choisit rationnellement le voilier renforcé, tandis que M. Y, à 0,1 %, s’élance non moins rationnellement sur le voilier léger. Poussons l’asymétrie à l’extrême : à la roulette russe, où la perte est sans commune mesure avec un gain ordinaire, le seuil s’approche de zéro ; on n’accepterait d’appuyer sur la détente qu’en étant à peu près certain que la chambre est vide.

C’est là tout le nœud d’une décision unique, prise une seule fois et dont la réponse vient après l’acte. Le décideur compare au seuil la probabilité issue de sa représentation, tandis que le monde ne consulte pas ce chiffre. Le monde répond d’après ce qui est, y compris tout ce que le cadre a laissé dans l’arrière-plan tacite. Si le mât cache une fissure interne, ou si une chambre du barillet a été chargée à l’insu du joueur, aucune cohérence interne du calcul n’empêche de franchir le pas.

## Une erreur n’est arrêtée que par ce qui peut se tromper autrement {#sec:ch00-detromper}

On pourrait espérer que la quantification des incertitudes suffise à prévenir ce piège : un modèle sérieux n’accompagne-t-il pas ses prévisions d’un intervalle de confiance ou d’une barre d’erreur ?

### Ce que mesure — et ce que tait — une barre d’erreur {#sec:ch00-barre-erreur}

Examiner comment une barre d’erreur est calculée dissipe vite cette illusion. Qu’on l’obtienne en faisant varier des paramètres, en rééchantillonnant des données ou en comparant plusieurs sous-modèles, une incertitude chiffrée mesure toujours le désaccord à l’intérieur d’un ensemble d’alternatives admises d’avance dans le calcul. Ce sur quoi toutes les variantes admises s’accordent par construction — parce qu’aucune ne contient la variable correspondante — ne produit aucun désaccord et n’élargit pas la barre d’erreur. Tout au plus un facteur omis qui aurait varié durant la collecte des données se glisse-t-il dans la dispersion attribuée au hasard ; s’il est resté constant, il ne laisse aucune trace.

Prenons un ingénieur qui calcule la tenue d’une ferrure métallique et conclut qu’elle supporte sa charge nominale avec un coefficient de sécurité de 1,8. En faisant varier ses paramètres, il explore l’incertitude aléatoire (la dispersion de l’alliage d’une coulée à l’autre) et l’incertitude épistémique (la connaissance imparfaite des efforts appliqués). Mais si la ferrure doit travailler dans un air marin chargé de sel et que la corrosion électrochimique ne figure dans aucune équation, cette troisième incertitude — l’incertitude ontologique, qui touche à l’adéquation du cadre lui-même — reste muette dans le rapport de calcul. Dix relecteurs qui étudient la même note d’hypothèses incomplète tomberont d’accord : leur accord mesure la cohérence de la note, non la présence de la page qui manque.

### Les cinq conditions d’un contrôle {#sec:ch00-cinq-conditions}

Comment une erreur — qu’elle naisse d’une faute interne au cadre ou d’un facteur oublié au dehors — peut-elle alors être repérée avant l’acte ? Uniquement en confrontant l’affirmation produite à un comparateur censé concorder avec elle, et en prenant acte de leur désaccord.

Cette idée simple tire sa portée pratique de cinq conditions qu’elle réclame ensemble. Pour qu’un contrôle arrête une erreur, il faut :

1. qu’un comparateur *existe* (un second calcul, une règle écrite d’avance, l’avis d’un pair, une mesure de terrain) ;
2. qu’il puisse *se tromper autrement* que l’affirmation initiale sur la cause d’erreur visée, sans quoi la même cause les faussera de concert ;
3. que l’affirmation et le comparateur soient *comparables*, exprimés dans les mêmes grandeurs avec leurs conditions et leurs unités ;
4. que le désaccord apparaisse *à temps*, avant que l’action ne devienne irréversible ;
5. qu’il donne lieu à une *prise en compte* effective, c’est-à-dire qu’il parvienne à quelqu’un qui l’entende et ait autorité pour suspendre ou modifier la décision.

Qu’une seule de ces cinq conditions manque pour une famille d’erreurs, et le contrôle les laisse toutes passer. Leur probabilité d’échappement — la probabilité qu’elles atteignent l’action sans contradiction à temps — vaut alors 100 %.

### Pourquoi l’auto-vérification bute sur le cadre {#sec:ch00-auto-verification}

La deuxième condition — pouvoir se tromper autrement — explique pourquoi un système de raisonnement ne peut pas auditer son propre cadre de l’intérieur. En sûreté de fonctionnement, deux pompes de secours branchées sur la même alimentation électrique ne forment pas deux protections indépendantes contre une panne de courant : elles partagent une cause commune de défaillance. Il en va de même pour le raisonnement. Relire son propre code, relancer une simulation avec un autre tirage aléatoire ou recouper un calcul par éléments finis avec une formule analytique fondée sur les mêmes idéalisations géométriques aide à débusquer une étourderie ou un bogue. Mais devant un facteur omis par le cadre, ces contrôles internes se copient l’un l’autre : ils puisent à la même source et s’accordent jusqu’à la troisième décimale tout en se trompant ensemble.

Les observations tirées du monde réel échappent en principe à ce cercle, puisque la réalité n’est pas calculée d’après notre cadre. Encore faut-il que le facteur omis ait varié pendant la collecte des données et que ses effets apparaissent dans ce qui a été enregistré. Un essai de charge sur une ferrure neuve en laboratoire sec ne révélera pas cinq ans de brouillard salin, et un modèle validé tant qu’un facteur caché demeurait stable cédera dès que ce facteur bougera en exploitation : on parlera de dérive de distribution. Quant au projet d’une « méta-procédure » formelle chargée de détecter automatiquement les cadres incomplets, il ouvre une régression sans fin, car cette procédure devrait elle-même fixer la liste finie des tests et des anomalies à surveiller, donc adopter un cadre. Ce qui est neuf n’entre dans un cadre que du dehors : par l’avertissement d’un tiers doté d’un autre point de vue, ou par un démenti concret du monde.

### Chaînes en série et contrôles croisés en parallèle {#sec:ch00-chaines-croises}

Tout composant — personne, équipe, programme, modèle — possède ainsi un angle mort : les causes d’erreur qu’il ne peut pas percevoir. Lorsqu’on assemble plusieurs composants dans un flux de travail, la géométrie de l’assemblage détermine si leurs angles morts s’additionnent ou se réduisent (figure [-@fig:ch00-serie-parallele]).

![Composition en série (chaîne) et composition en parallèle (contrôle croisé) : la chaîne cumule les angles morts de chaque maillon et ceux des interfaces, tandis que le contrôle croisé ne laisse passer que les causes d’erreur communes aux deux voies.](figures/ch00-serie-parallele.pdf){#fig:ch00-serie-parallele width=85%}

Dans une chaîne en série, chaque maillon reçoit le résultat du précédent et le tient pour acquis afin de produire l’étape suivante. Si une erreur survient à un maillon, ou si un malentendu naît à une interface, le résultat final en hérite. Ce passage en série devient d’autant plus fragile qu’il s’accompagne souvent d’un blanchiment des conditions. Un champ de températures calculé sous dix hypothèses prudentes traverse une interface sous la forme d’un tableau de nombres nus, dépouillé de ses réserves, de ses barres d’erreur et parfois de ses unités — comme les impulsions transmises à l’équipe de navigation de *Mars Climate Orbiter* [@mco1999]. Le maillon suivant n’a plus rien à comparer ; il incorpore le chiffre comme un fait accompli.

Dans un contrôle croisé en parallèle, au contraire, un producteur et un contrôleur examinent la même question et l’on confronte leurs réponses. Sous réserve que la comparaison soit fidèle et les désaccords instruits, une erreur ne passe que si elle échappe aux deux voies : l’angle mort résiduel se réduit à l’intersection de leurs angles morts. Ce gain a toutefois un coût fréquent : plus le contrôleur est indépendant par ses méthodes, sa discipline ou ses données, moins il partage spontanément le même langage et les mêmes définitions, et plus il faut travailler pour rendre les résultats comparables. À l’inverse, demander à un modèle de relire sa propre sortie dessine un contrôle croisé sur l’organigramme, mais ne forme qu’un miroir devant son propre angle mort.

## L’informatique classique a gagné ses garanties ; les modèles appris les dépensent {#sec:ch00-contrats-donnees}

Munis de cette grille, tournons-nous vers l’informatique. Pourquoi pouvons-nous empiler des milliards d’opérations élémentaires dans un processeur, un système de fichiers, un protocole réseau ou une base de données sans devoir contrôler une à une chacune des réponses produites à chaque seconde ?

L’informatique classique repose sur des composants spécifiés : des briques logicielles dont quelqu’un a rédigé les règles et qui s’engagent envers le reste du système par un contrat explicite. Une fonction de tri promet de rendre, pour toute liste d’éléments comparables, une permutation ordonnée de cette même liste ; le protocole TCP promet que les octets arriveront dans l’ordre ou qu’une erreur sera signalée. Parce que cette promesse est écrite d’avance, lisible par un tiers et opposable au code, elle sert de comparateur permanent. Elle autorise la vérification en amont : typage, tests, analyse statique ou preuve formelle confrontent le composant à son contrat avant sa mise en service, en un contrôle fait une fois pour toutes les exécutions futures. Les tests ne prouvent pas l’absence d’erreur, mais le principe demeure : on vérifie d’avance. Et quand le logiciel échoue malgré tout en exploitation, le contrat — ou la clause qu’on aurait dû écrire — donne une adresse où corriger : telle ligne, tel module, telle interface.

La portée de cette informatique s’arrêtait pourtant là où s’arrêtait notre capacité à rédiger des règles. Personne ne savait écrire la spécification formelle qui distingue un chat d’un chien sur une grille de pixels, résume fidèlement un dossier touffu ou traduit un texte avec naturel. L’apprentissage automatique a franchi cette limite en inversant la démarche : au lieu de formuler la règle, on rassemble une multitude d’exemples et l’on ajuste par optimisation des millions ou des milliards de paramètres numériques pour former un composant appris.

Dans cet échange, la garantie préalable n’a pas été perdue par négligence. Elle a été délibérément dépensée pour acquérir une portée nouvelle sur des tâches rebelles aux règles écrites. La spécification n’a pas disparu pour autant : elle a migré vers le choix des données d’entraînement, la fonction objectif et les préférences d’évaluation, où personne ne peut plus la lire comme un texte de loi.

Au sommet de la pile logicielle, avec les grands modèles de langage entraînés à prédire de proche en proche le fragment suivant, ce déplacement provoque un changement de régime où trois propriétés basculent ensemble :

1. *Ce qui est promis* : au contrat vérifiable sur chaque appel succède une tendance statistique mesurée en moyenne sur des batteries de tests, sans garantie sur une réponse particulière.
2. *La façon dont l’échec se présente* : dans les couches basses, une erreur contredit une règle écrite, même quand elle passe longtemps inaperçue comme l’erreur d’unité de *Mars Climate Orbiter* ; au sommet, elle prend l’allure d’un texte fluide, poli et assuré, indiscernable en surface d’une réponse exacte, comme dans l’affaire *Mata v. Avianca* [@mata2023].
3. *Le lieu où aboutit l’enquête après coup* : il n’y a plus d’adresse pour un correctif local ; on ne répare pas une distribution de probabilité par une rustine à la ligne 42.

À cela s’ajoute un profil de compétence en dents de scie : capable sur un problème complexe, le modèle peut échouer sur une variante voisine d’apparence anodine, sans rien laisser paraître dans le ton de sa réponse. L’interroger plusieurs fois et comparer les réponses trahit les erreurs où il devine, mais non celles qu’il répète avec constance. L’orienter par des consignes soignées ou par un ajustement sur des préférences humaines déplace utilement ses fréquences d’erreur, mais s’apparente au dressage plutôt qu’au câblage d’un disjoncteur : cela ne rétablit aucun contrat. Faute de vérification en amont, le contrôle doit se reporter sur les sorties, avant qu’elles ne se changent en actes.

## Ce que l’automatisation fait aux contrôles {#sec:ch00-automatisation}

Que se passe-t-il lorsque ces composants appris ne servent plus seulement à répondre à un lecteur attentif, mais s’intègrent au cœur des flux de travail ? L’automatisation agit simultanément sur trois leviers : elle enchaîne les étapes, elle retire des contrôles humains implicites, et elle corrèle les contrôles restants.

### L’automatisation met les étapes en chaîne et fait passer les erreurs à l’acte {#sec:ch00-auto-chaines}

Pour accomplir des tâches ambitieuses — remanier un dépôt de code, instruire un dossier client, piloter une suite d’opérations —, on assemble des chaînes où un modèle extrait des données, résume, planifie et appelle des outils externes : c’est l’agent autonome. Sur le plan structurel, une séquence de douze étapes où chacune repose sur le texte produit par la précédente forme une chaîne à douze maillons, le long de laquelle les hypothèses tacites risquent d’être blanchies à chaque passage tandis que les angles morts s’additionnent. Sur le plan opérationnel, le système passe de la production de réponses, soumises à un lecteur, à l’exécution d’actions qui modifient une base de données, publient un document ou engagent une transaction sans relecture. Le pouvoir d’agir directement revient ainsi à la couche de l’édifice informatique qui offre le moins de garanties préalables.

### L’automatisation érode les vérifications humaines {#sec:ch00-auto-erosion}

Dans le travail analytique ordinaire, la lenteur remplissait une fonction discrète : la friction fabriquait des comparateurs. En nettoyant des tableaux, en posant des équations à la main ou en écrivant un programme pas à pas, l’analyste se formait une attente d’ordre de grandeur et croisait des résultats intermédiaires capables de se contredire. Comme personne n’avait inscrit cette boucle de rétroaction sur les organigrammes, sa disparition devant une réponse instantanée passe inaperçue — jusqu’au jour où une erreur grossière traverse tout le circuit sans alerte interne.

En même temps s’efface un indice courant de la coopération humaine : le signe révélateur du doute. Lorsqu’un collègue s’avance aux bornes de ce qu’il maîtrise, son hésitation, ses réserves ou le caractère inachevé de son brouillon alertent le destinataire. Un modèle génératif adopte la même voix posée qu’il restitue un fait solide ou qu’il invente une référence ; rien dans le grain du texte ne trahit plus l’incertitude. L’essai de METR cité plus haut montre aussi à quel point l’impression de vitesse peut s’écarter du temps mesuré, même chez des spécialistes travaillant sur leur propre terrain [@becker2025].

Plus largement, tant que rédiger une prose claire ou un code qui compile exigeait d’avoir travaillé le fond, la tenue formelle constituait un signal coûteux, donc crédible, de solidité. Dès lors que la belle forme devient presque gratuite tandis que la vérification de fond reste lente et onéreuse, les travaux contrôlés et les textes superficiels deviennent indiscernables au premier regard. Et même lorsqu’un humain relit la sortie du modèle, deux pièges referment le contrôle sur lui-même : la consigne transmise à la machine lui cède déjà le cadre du problème, et l’entraînement des modèles à satisfaire l’interlocuteur favorise la complaisance plutôt que la contradiction.

### L’automatisation corrèle les angles morts à l’échelle collective {#sec:ch00-auto-correlation}

Enfin, à mesure qu’une communauté entière d’auteurs, d’ingénieurs et de relecteurs adopte le même petit nombre de modèles de fondation, un effet d’échelle apparaît. Contre les étourderies propres à chaque individu, le modèle joue le rôle d’un vrai comparateur et abaisse le taux d’erreur individuel. Mais pour les erreurs qui appartiennent à l’angle mort du modèle lui-même, producteur et contrôleur puisent désormais à la même source : leur contrôle croisé tend à se réduire à une copie, et la probabilité d’échappement de ces erreurs partagées monte.

Cette corrélation s’accentue lorsque les textes et les codes produits par les modèles reviennent alimenter le Web, les dépôts logiciels et la littérature sans mention d’origine. Par ce blanchiment de provenance, dix reprises issues d’un même modèle finissent par ressembler à dix témoins indépendants. Dans le même temps, la hausse du volume produit incite les organisations à comprimer le temps et les moyens alloués à ce qui est devenu le véritable goulet d’étranglement : l’évaluation indépendante.

### L’énigme arithmétique du producteur plus fiable et du système plus risqué {#sec:ch00-enigme-arithmetique}

Un calcul élémentaire montre pourquoi l’amélioration moyenne d’un outil ne garantit pas à elle seule la sûreté d’un système. Puisqu’une affirmation fausse ne nuit que si elle atteint l’action sans être arrêtée, le risque résiduel est le produit de deux facteurs : le taux d’erreur du producteur et la probabilité d’échappement des contrôles.

Comparons deux organisations fictives, avec des chiffres choisis pour l’illustration :

- dans la première, le producteur se trompe dans 10 % des cas, mais ses sorties passent par un contrôle qui se trompe autrement que lui et ne laisse passer que 1 % des erreurs ; la part des affirmations fausses qui atteignent l’action vaut alors $10\,\% \times 1\,\% = 0{,}1\,\%$ ;
- dans la seconde, le producteur, assisté d’un modèle, ne se trompe plus que dans 1 % des cas, mais ses erreurs ont la même aisance que ses réussites, n’ont pas d’adresse, et les relecteurs s’appuient sur le même modèle ; 90 % d’entre elles franchissent le filtre, portant la part des erreurs suivies d’effet à $1\,\% \times 90\,\% = 0{,}9\,\%$.

Bien que le second producteur soit dix fois plus exact, le système laisse passer neuf fois plus d’erreurs jusqu’à l’action. Les tests de référence ne mesurent que le premier facteur ; toute la question du cadre et de l’architecture des contrôles porte sur le second. De plus, à mesure que les vraies erreurs du producteur deviennent plus rares, un contrôleur au taux de fausses alertes constant émet une proportion croissante d’alertes infondées. Si les opérateurs finissent par moins les écouter — phénomène comportemental et non arithmétique —, la probabilité d’échappement augmente encore.

## Ce que nous pouvons encore faire {#sec:ch00-remedes}

Ce diagnostic ne mène ni au scepticisme paralysant ni au rejet de l’automatisation. Il invite à déplacer l’effort : là où l’on ne peut plus acheter une garantie une fois pour toutes sur l’outil, il faut organiser lucidement les décisions et les contrôles.

Du côté de la décision, tout commence par le partage entre ce qui se répète et ce qui ne se joue qu’une fois. Lorsqu’une décision se répète des milliers de fois en milieu stable — filtrer des messages, prévoir la pluie du lendemain, trier des demandes courantes —, le suivi des fréquences permet de calibrer le système et d’ajuster ses seuils. Face à une décision unique aux conséquences lourdes ou irréversibles — lancer une sonde, opérer un patient, engager une architecture critique, laisser un agent exécuter une commande destructive —, aucune moyenne statistique ne protège le cas singulier. Deux garde-fous prennent alors le relais : ajouter délibérément à son estimation du risque une marge d’humilité (jugement de prudence et non mesure) pour tenir compte de ce que la représentation peut omettre, et placer devant l’action un verrou où elle attend une autorisation après contrôle indépendant.

La même distinction éclaire la conduite de l’exploration. Puisque toute action est aussi une question posée au monde, mieux vaut la poser là où la réponse coûte peu et peut être annulée : laisser les modèles et les agents explorer librement dans un bac à sable — environnement isolé où compilateur, simulateur et tests répondent vite, à faible coût et sans dégât extérieur —, tout en maintenant des verrous stricts aux frontières qui touchent le monde réel à coût élevé.

Quant au décideur, au citoyen ou au responsable à qui l’on remet un chiffre assuré sans ses conditions d’obtention — transfert de responsabilité déguisé en information —, quatre questions simples suffisent, sans technicité mathématique, pour rouvrir le cadre :

1. *Sous quelles conditions ce chiffre tient-il ?*
2. *Qu’est-ce qui le ferait changer sensiblement ?*
3. *Quelle est la manière la plus vraisemblable dont il pourrait être faux ?*
4. *Qu’a-t-on délibérément choisi de ne pas modéliser ?*

Du côté de l’organisation des contrôles, enfin, la défense s’appuie sur trois niveaux complémentaires, dont aucun ne suffit isolément :

- *L’attitude individuelle* : notre expérience du monde déborde souvent le cadre du modèle consulté, sans jamais déborder le nôtre. L’humilité épistémique consiste alors à produire ses propres comparateurs *avant* de regarder l’outil : noter un ordre de grandeur attendu, pratiquer un pré-mortem en imaginant l’échec du projet six mois plus tard, et élargir à dessein les mondes possibles envisagés.
- *Le placement des contrôles* : plutôt que de disperser une attention limitée ou de multiplier les approbations machinales, placer les vérifications aux points de passage vers l’action, là où une sortie cesse d’être un brouillon pour devenir un acte ou une référence. Ces points demandent des relecteurs qui partagent l’interface avec le producteur et comprennent par eux-mêmes le niveau situé dessous : le code sous le programme généré, la physique sous le nombre calculé.
- *L’organisation collective* : traiter la capacité d’évaluation indépendante comme une ressource budgétée et plafonner la production à ce qu’elle permet de vérifier ; exiger que toute affirmation soumise à décision affiche son état de vérification et ses hypothèses ; tenir un historique confrontant prévisions et issues réelles ; mesurer concrètement l’échappement du système de relecture par des erreurs injectées, sur le modèle des menaces fictives projetées sur les écrans de sûreté aéroportuaire [@ue2015tip].

## Architecture de l’ouvrage {#sec:ch00-architecture}

Pour établir ces thèses sans pétition de principe, le livre suit une règle d’ordre : forger les clés avant d’aborder les serrures. Commencer par les modèles de langage et les agents logiciels exposerait à prendre pour des singularités passagères de l’intelligence artificielle des mécanismes qui valent pour toute représentation finie et tout dispositif de contrôle. L’argument se déploie donc en cinq parties (figure [-@fig:ch00-carte-ouvrage]).

![Architecture de l’ouvrage : les cinq parties et l’enchaînement des étapes de l’argument, des fondements de la décision dans un cadre jusqu’à l’organisation des contrôles.](figures/ch00-carte-ouvrage.pdf){#fig:ch00-carte-ouvrage width=95%}

La @sec:partie-1 (*Agir d’après une représentation*, chapitres [-@sec:ch01] à [-@sec:ch04]) met en place les instruments de base pour un décideur isolé. Le @sec:ch01 unifie les outils de logique et de probabilité employés dans la suite : conditionnement, règle de Bayes en cotes, rapport de vraisemblance et score logarithmique de surprise. Le @sec:ch02 sépare le monde de la représentation, formalise les règles à conditions cachées et définit le cadre ainsi que le problème du cadre, en montrant pourquoi la rigueur déductive ou inductive demeure relative au cadre choisi. Le @sec:ch03 développe la probabilité comme jugement pesant des mondes possibles, l’habitude de raisonner à l’envers et l’impossibilité de juger un prévisionniste sur une issue unique. Le @sec:ch04 relie enfin croyance et action par l’utilité espérée subjective et dégage le seuil de décision $p^\ast$ (@eq:ch00-seuil) devant une décision unique.

La @sec:partie-2 (*Ce qui peut nous détromper*, chapitres [-@sec:ch05] à [-@sec:ch09]) forme le cœur théorique et formel de la monographie. Pour en éprouver la généralité, ses exemples restent pris hors de l’intelligence artificielle : mécanique, accidents industriels, finance, dépistage médical, programmation multiversion, calculs multiphysiques. Le @sec:ch05 distingue les incertitudes aléatoire, épistémique et ontologique et établit la première proposition : une barre d’erreur ne mesure que le désaccord entre alternatives admises. Le @sec:ch06 définit l’affirmation, le contrôle et le comparateur, puis déploie les cinq conditions nécessaires à la détection d’une erreur (deuxième proposition). Le @sec:ch07 montre pourquoi le cadre agit comme une cause commune qui aveugle les contrôles internes aux facteurs omis, précise quand les observations du monde peuvent révéler un tel facteur (troisième proposition), et explique pourquoi aucune méta-procédure n’échappe à la régression. Le @sec:ch08 analyse le compromis entre indépendance et comparabilité (quatrième proposition), oppose les chaînes aux contrôles croisés (cinquième proposition) et caractérise le blanchiment aux interfaces. Le @sec:ch09 introduit la sévérité d’un test, le piège des fausses alertes quand le taux de base recule, et la décomposition du risque en taux d’erreur multiplié par la probabilité d’échappement.

La @sec:partie-3 (*De l’informatique classique à l’IA*, chapitres [-@sec:ch10] à [-@sec:ch13]) applique cette théorie des contrôles à l’empilement des couches logicielles. Le @sec:ch10 explique sur quoi repose la fiabilité des composants spécifiés : contrats écrits, vérification en amont et adresse localisable des défaillances. Le @sec:ch11 suit le passage de la spécification dans les données pour former un composant appris : la portée s’achète au prix de la garantie et de la lisibilité, la plausibilité remplace la vérité comme objectif d’optimisation, et orienter un modèle ne revient jamais à le spécifier. Le @sec:ch12 étudie le changement de régime au sommet de la pile — basculement conjoint de la promesse, de l’apparence de l’échec et de l’enquête après coup —, la frontière en dents de scie des compétences et le lien mathématique entre calibration générative et invention sur faits rares. Le @sec:ch13 croise enfin les deux axes qui synthétisent les parties [-@sec:partie-2] et [-@sec:partie-3] — lieu de la cause d’erreur (dans ou hors du cadre) et réponse des contrôles (erreur signalée ou silencieuse) —, passe en revue les quatre sources de comparateurs et situe vérification et validation sur cette matrice.

La @sec:partie-4 (*L’automatisation et ses angles morts*, chapitres [-@sec:ch14] à [-@sec:ch16]) étudie la dynamique opérationnelle de l’automatisation à l’aide des modèles formels de la @sec:partie-2. Le @sec:ch14 analyse les *pipelines* et les agents autonomes comme des chaînes dont les erreurs passent directement à l’acte. Le @sec:ch15 détaille l’érosion des vérifications humaines : perte de la friction génératrice de repères, disparition du signe révélateur d’hésitation, effondrement du signal par la forme et pièges de la consigne. Le @sec:ch16 change d’échelle pour examiner comment l’usage collectif des mêmes modèles abaisse les erreurs individuelles tout en élevant l’échappement par corrélation des angles morts, blanchiment de provenance et saturation des capacités d’évaluation.

La @sec:partie-5 (*Décider et se prémunir*, chapitres [-@sec:ch17] et [-@sec:ch18]) traduit ce diagnostic en principes pratiques. Le @sec:ch17 reprend le modèle de décision du @sec:ch04 avec un risque omis par le cadre et une marge d’humilité, sépare ce qui relève de la calibration de ce qui réclame un verrou, articule bacs à sable et verrous pour l’exploration, et détaille les quatre questions à poser devant tout chiffre assuré. Le @sec:ch18 organise le remède sur trois niveaux — attitude, placement, organisation, y compris la mesure expérimentale de l’échappement par erreurs injectées — et se ferme sur cinq questions avant d’agir. La conclusion soumet enfin l’ouvrage lui-même à ses propres critères (@sec:conclusion).

D’une partie à l’autre, un petit nombre d’exemples récurrents reviennent à mesure que l’appareil conceptuel s’enrichit :

- la course de voiliers de M. X et M. Y (chapitres [-@sec:ch03], [-@sec:ch04] et [-@sec:ch17]) ;
- l’ébullition de l’eau et ses conditions tacites (chapitres [-@sec:ch01], [-@sec:ch02] et [-@sec:ch05]) ;
- la ferrure mécanique exposée à la corrosion (chapitres [-@sec:ch05], [-@sec:ch07], [-@sec:ch08] et [-@sec:ch18]) ;
- la sonde *Mars Climate Orbiter* (chapitres [-@sec:ch08], [-@sec:ch10] et [-@sec:ch12]) ;
- la dinde inductiviste (chapitres [-@sec:ch03], [-@sec:ch05] et [-@sec:ch13]) ;
- l’accident de la navette *Challenger* (chapitres [-@sec:ch05] et [-@sec:ch06]) ;
- la prévision de pluie à 70 % (chapitres [-@sec:ch03] et [-@sec:ch17]) ;
- et les cas documentés sur l’usage contemporain des modèles de langage (chapitres [-@sec:ch11], [-@sec:ch12] et [-@sec:ch15]).

Comme l’annonce l’avant-propos, chacune des cinq propositions structurantes de la @sec:partie-2 affiche explicitement son statut épistémique (*définition*, *résultat sous hypothèses*, *hypothèse de travail* ou *constat empirique*) et fait l’objet d’une discussion critique de sa robustesse. Trois modèles formels soutiennent l’ensemble : le modèle M1, des angles morts et de l’échappement (chapitres [-@sec:ch08] et [-@sec:ch09]) ; le modèle M2, de la décision avec facteur omis (@sec:ch17) ; le modèle M3, du cadre comme cause commune (@sec:ch07).

## Parcours de lecture {#sec:ch00-parcours}

La monographie est conçue pour une lecture continue, mais chaque lecteur l’aborde avec les questions et les contraintes de son métier. Huit parcours sélectifs mènent plus directement aux développements liés à un profil donné (@tbl:ch00-parcours). L’ouverture de chaque chapitre rappelle d’ailleurs brièvement les notions d’amont mobilisées, avec renvoi vers le chapitre qui les introduit.

- *L’argument principal* : suit l’épine dorsale logique du livre au plus court, du choix du cadre jusqu’à l’organisation des contrôles, en laissant de côté les rappels d’outils et les développements techniques intermédiaires.
- *Voiliers, eau bouillante et mondes possibles* : privilégie une entrée concrète par la philosophie pratique des probabilités, le jugement sous incertitude et la décision unique face au risque.
- *L’ingénieur* : met l’accent sur les marges de sécurité, les défaillances de mode commun, le chaînage de modèles multiphysiques, les contrats d’interface et l’architecture de vérification et de validation.
- *Le statisticien et le mathématicien* : s’attache aux fondements du conditionnement, aux règles de score, à la décomposition de la variance, aux limites formelles de l’auto-vérification, à la sévérité des tests et aux bornes théoriques sur la génération calibrée.
- *L’informaticien et le concepteur d’IA* : relie la théorie des contrôles croisés au passage des composants spécifiés aux composants appris, jusqu’aux architectures d’agents, aux bacs à sable et aux verrous.
- *Le décideur et l’institution* : se concentre sur l’évaluation des enjeux, la gestion des fausses alertes, l’érosion des relectures humaines, les angles morts collectifs et le gouvernement de la vérification.
- *Le destinataire d’un chiffre sûr de lui* : donne à celui qui reçoit une prévision, un score ou un rapport sans en avoir bâti le modèle les moyens d’en interroger les conditions de validité avant d’agir.
- *Parcours critique (tensions et limites)* : permet au lecteur déjà familier de la thèse générale de traverser les encadrés *Nuance et discussion ouverte* où sont examinées les objections, les hypothèses fragiles et les questions laissées ouvertes jusqu’au bilan final.

| Parcours | Chapitres recommandés |
| :-- | :-- |
| L’argument principal | Chapitres [-@sec:ch00], [-@sec:ch02], [-@sec:ch05], [-@sec:ch06], [-@sec:ch07], [-@sec:ch10], [-@sec:ch11], [-@sec:ch13], [-@sec:ch16], [-@sec:ch18] et @sec:conclusion |
| Voiliers, eau bouillante et mondes possibles | Chapitres [-@sec:ch00], [-@sec:ch01], [-@sec:ch02], [-@sec:ch03], [-@sec:ch04], [-@sec:ch05] et [-@sec:ch17] |
| L’ingénieur | Chapitres [-@sec:ch00], [-@sec:ch02], [-@sec:ch05], [-@sec:ch07], [-@sec:ch08], [-@sec:ch10], [-@sec:ch13] et [-@sec:ch18] |
| Le statisticien et le mathématicien | Chapitres [-@sec:ch00], [-@sec:ch01], [-@sec:ch03], [-@sec:ch05], [-@sec:ch07], [-@sec:ch09] et [-@sec:ch12] |
| L’informaticien et le concepteur d’IA | Chapitres [-@sec:ch00], [-@sec:ch08], [-@sec:ch09], [-@sec:ch10], [-@sec:ch11], [-@sec:ch12], [-@sec:ch13], [-@sec:ch14] et [-@sec:ch17] |
| Le décideur et l’institution | Chapitres [-@sec:ch00], [-@sec:ch04], [-@sec:ch09], [-@sec:ch15], [-@sec:ch16], [-@sec:ch17] et [-@sec:ch18] |
| Le destinataire d’un chiffre sûr de lui | Chapitres [-@sec:ch00], [-@sec:ch03], [-@sec:ch04], [-@sec:ch11], [-@sec:ch15] et [-@sec:ch17] |
| Parcours critique (tensions et limites) | Chapitre [-@sec:ch00], blocs *Nuance et discussion ouverte* des chapitres [-@sec:ch05], [-@sec:ch07], [-@sec:ch08], [-@sec:ch09], [-@sec:ch12], [-@sec:ch13], [-@sec:ch16] et [-@sec:ch17], et @sec:conclusion |

Table: Huit parcours de lecture à travers la monographie selon le profil et les préoccupations du lecteur. {#tbl:ch00-parcours}

::: {.question}
Dans votre activité récente, quel est le dernier chiffre d’après lequel vous avez agi, et quel était son comparateur ?
:::

## Points clés {.points-cles}

- Nous n’agissons jamais sur le monde directement, mais d’après une représentation bâtie à l’intérieur d’un cadre fini qui laisse toujours un arrière-plan de conditions sous-entendues, alors que le monde répond à notre action et non à nos hypothèses.
- Une barre d’erreur ne mesure que le désaccord entre les alternatives admises dans le cadre ; une erreur — interne ou issue d’un facteur omis — n’est arrêtée à temps que si elle rencontre un comparateur capable de se tromper autrement, comparable, disponible avant l’acte et effectivement pris en compte.
- Les contrôles placés en chaîne additionnent leurs angles morts à mesure que les conditions sont blanchies aux interfaces, tandis que les contrôles croisés en parallèle ne laissent subsister que les causes d’erreur communes aux deux voies.
- L’informatique classique a fondé sa fiabilité sur des contrats écrits vérifiables en amont et dotés d’une adresse en cas de défaillance ; l’apprentissage automatique achète sa portée sur des tâches rebelles aux règles écrites au prix de cette garantie préalable, si bien que ses erreurs n’ont plus d’adresse et prennent la même aisance que ses réussites.
- L’automatisation met les étapes en chaîne jusqu’à l’action, érode les vérifications humaines nées de la friction ou des signes d’hésitation, et corrèle les erreurs dans les communautés qui partagent les mêmes modèles, ce qui peut accroître le risque global même quand le taux d’erreur individuel baisse.
- Face à ce déplacement, la maîtrise du risque repose sur des verrous et une marge d’humilité devant les décisions uniques, sur le cantonnement de l’exploration libre dans des bacs à sable réversibles, et sur une défense organisée aux trois niveaux de l’attitude individuelle, du placement des contrôles aux points de passage vers l’action et de la mesure collective de l’échappement.
