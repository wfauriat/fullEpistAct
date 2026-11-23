# Ce qui peut nous détromper à temps : synthèse d’une recherche en deux livres

22 novembre 2026

## En bref

Deux livres, à quatre ans d’intervalle, poursuivent une même question. Nous n’agissons jamais sur le monde tel qu’il est, mais d’après une représentation construite : mesures, équations, programmes, et désormais modèles appris. Qu’est-ce qui peut nous avertir à temps que cette représentation fait fausse route ?

*Un discours de la méthode au XXIe siècle* (2022) y répond en pédagogue, sous la forme d’un dialogue entre un professeur de statistique et six étudiants de disciplines différentes. Il reconstruit la logique, les probabilités, la statistique et la théorie de la décision, défend le caractère « nécessairement subjectif » de la rationalité et conclut par un manifeste pour une rationalité « humble, critique et humaine », méfiant envers les promesses de l’intelligence artificielle.

*Agir d’après une représentation du monde* (2026) en donne la forme mûre et technique. Sa devise : **une erreur n’est arrêtée que par ce qui peut se tromper autrement.** Il en tire une théorie des contrôles, l’applique au logiciel classique, aux modèles appris, aux agents automatisés et aux institutions, puis propose des parades concrètes.

La trajectoire est nette : d’un avertissement philosophique sur les limites de la rationalité à une discipline d’ingénieur sur l’architecture des contrôles. Le contraste vaut aussi pour leur fabrication : le premier livre a été écrit seul en plus de 700 heures, le second bâti en trois jours avec des modèles de langage. Cette synthèse présente les idées, leur place dans la littérature, leurs usages et leurs limites, puis ce qu’enseigne la comparaison des deux manières de faire.

## Les idées centrales

L’édifice repose sur quelques notions, introduites sans référence à l’intelligence artificielle, puis appliquées à elle.

**Le cadre et son arrière-plan tacite.** Toute règle portant sur le monde vaut « pourvu que » tout un arrière-plan reste dans son état habituel : l’eau bout à 100 °C si elle est pure, à l’air libre, à basse altitude, et ainsi de suite sans fin. Choisir ce que l’on énonce et ce que l’on tait, c’est choisir un *cadre* (variables, catégories, modèles, objectif), avant tout calcul. La rigueur exercée dans un cadre, déductive ou inductive, ne certifie jamais le cadre : la dinde qui note chaque matin l’heure du grain dispose, la veille de Noël, d’une série statistique irréprochable, et son malheur tient à une variable absente de son cadre.

**Ce que tait une barre d’erreur.** Une incertitude chiffrée mesure toujours un désaccord entre des alternatives admises d’avance ; ce qu’aucune ne contient ne produit aucun désaccord. L’ingénieur qui calcule une ferrure avec un coefficient de sécurité de 1,8 a exploré la dispersion de l’alliage et l’incertitude sur les efforts ; si la corrosion en air salin ne figure dans aucune équation, la note reste muette, et dix relecteurs fidèles à la même note tomberont d’accord. Marges, analyses de sensibilité et moyennes de modèles restent précieuses, mais elles travaillent à l’intérieur du cadre.

**La probabilité comme jugement, mis à l’épreuve.** Une probabilité répartit un poids sur les « mondes possibles » compatibles avec ce que l’on sait ; relative à une information, elle n’est pas arbitraire pour autant. Une issue isolée départage mal deux prévisions ; seule la répétition, consignée et notée par des règles de score, permet de juger un prévisionniste et sa calibration. Pour décider, l’option risquée ne se justifie que si la probabilité d’échec reste sous le seuil gain / (gain + perte), qui tend vers zéro quand la perte devient démesurée. Deux navigateurs qui estiment à 5 % et à 0,1 % le risque de démâter peuvent ainsi choisir différemment, et tous deux rationnellement ; mais le monde répond selon ce qui est, fissure invisible du mât comprise.

**Les cinq conditions d’un contrôle.** Une erreur n’est arrêtée avant l’action que si l’affirmation est confrontée à un *comparateur* et que le désaccord est pris en compte. Cinq conditions doivent être réunies :

1. un comparateur **existe** (second calcul, règle écrite, avis d’un pair, mesure sur le terrain) ;
2. il peut **se tromper autrement** à l’égard de la cause d’erreur visée ;
3. les deux sont **comparables** : mêmes grandeurs, mêmes unités, conditions explicites ;
4. le désaccord arrive **à temps**, avant l’irréversible ;
5. quelqu’un le **prend en compte** et a l’autorité d’agir.

Qu’une seule manque, et toute une famille d’erreurs passe : sa probabilité d’échappement vaut 100 %. L’accident de la navette Challenger se relit ainsi comme une combinaison de ruptures : un graphique qui omettait les vols sans dommage, puis des objections techniques écartées en séance.

**Le cadre comme cause commune.** Deux pompes de secours branchées sur la même alimentation ne protègent pas d’une coupure de courant. De même, face à un facteur omis, tous les contrôles calculés dans un même cadre sont des copies : ils s’accordent en se trompant ensemble. Le monde échappe à ce cercle, à condition que le facteur omis ait varié et qu’on en ait enregistré les effets. Aucune « méta-procédure » ne détecte automatiquement les cadres incomplets, puisqu’elle devrait fixer d’avance ce qu’elle surveille : une pertinence nouvelle n’entre que du dehors, par un tiers qui voit autrement ou par l’épreuve du monde.

**Chaînes, contrôles croisés, blanchiment.** Dans une *chaîne*, chaque maillon tient pour acquis ce qu’il reçoit, et les angles morts s’additionnent ; dans un *contrôle croisé*, seul subsiste l’angle mort partagé. Mais l’indépendance se paie en comparabilité : plus le contrôleur est éloigné du producteur, mieux il voit ses omissions, mais plus son objection est difficile à traduire. Le *blanchiment*, perte des unités, hypothèses ou réserves d’un résultat lorsqu’il change de mains, a coûté la sonde Mars Climate Orbiter en 1999.

**Risque = taux d’erreur × probabilité d’échappement.** Un contrôle passé sans alerte ne prouve rien s’il n’aurait pas pu alerter : c’est la notion de *sévérité*. Les évaluations des outils mesurent le premier facteur ; l’architecture des contrôles décide du second, et la part des causes d’erreur partagées entre producteur et contrôleur y forme un plancher qu’aucune vigilance ne perce.

**Une matrice à deux axes.** Les erreurs se rangent selon que leur cause est dans ou hors du cadre, et selon qu’elles sont signalées ou silencieuses.

| | Erreur signalée (un comparateur la contredit) | Erreur silencieuse (rien ne la contredit) |
| --- | --- | --- |
| **Cause dans le cadre** (faute de calcul, bogue, paramètre) | *Faute rattrapée* : un test ou un contre-calcul la contredit avant l’usage (ex. : bogue arrêté par un test) | *Faute muette* : rien ne la contredit à temps ; case que peuplent les modèles appris (ex. : réponse fluide et fausse) |
| **Cause hors du cadre** (facteur absent du modèle) | *Omission révélée* : un regard extérieur ou une mesure de terrain la fait apparaître (ex. : corrosion signalée par un tiers) | *Omission ignorée* : aucun contrôle calculé dans le cadre ne peut la voir (ex. : la ferrure corrodée) |

*Sur la ligne du haut, formaliser (contrat, test, preuve) fait passer une faute de la colonne silencieuse à la colonne signalée ; sur la ligne du bas, seul un tiers ou l’épreuve du monde le peut. La ligne est fixée par le cadre : aucun formalisme ne l’inspecte de l’intérieur.*

D’où la formule : **la formalité change la colonne, non la ligne.** Un contrat, un test ou une preuve rendent une faute interne détectable ; ils ne certifient jamais l’adéquation du cadre. Ils servent la *vérification* (résoudre correctement le problème posé), non la *validation* (poser un problème fidèle au réel).

Le livre de 2022 posait déjà certaines de ces pierres sous d’autres noms : trois limites de la rationalité (mathématique, épistémique, économique), un arbitrage entre le coût et le bénéfice d’en savoir plus, qu’il nommait « exploration statistique », et la thèse selon laquelle « formaliser, c’est déjà choisir ».

## Le diagnostic sur l’IA et l’automatisation

Appliquée à l’informatique, la grille produit un diagnostic précis : le danger tient moins à la fréquence des erreurs des machines qu’à la disparition silencieuse de ce qui permettait de les arrêter.

**Des garanties gagnées, puis dépensées.** Le logiciel classique repose sur des contrats écrits : chaque couche promet ce qu’elle fait, on la vérifie une fois pour toutes avant l’usage, et la panne a une adresse. L’apprentissage automatique a franchi le mur que les règles écrites ne pouvaient pas traverser (personne ne savait spécifier ce qui distingue un chat d’un chien sur une grille de pixels), mais en dépensant cette garantie : la spécification a migré dans les données et la fonction d’objectif, où nul ne la lit. Avec les grands modèles de langage, trois choses basculent ensemble : la promesse devient une tendance statistique mesurée en moyenne, l’échec prend la forme d’un texte fluide et assuré, et l’enquête n’aboutit à aucune ligne à corriger.

En 2023, dans l’affaire Mata contre Avianca, des avocats ont cité six décisions de justice inventées par un assistant conversationnel, sans qu’aucune règle ait été enfreinte. Les consignes et l’ajustement sur des préférences humaines déplacent les fréquences d’erreur, mais « orienter n’est pas spécifier ». S’y ajoutent une compétence « en dents de scie », brillante sur une question difficile et défaillante sur une variante anodine, et des erreurs constantes que reposer la question ne débusque pas.

**Trois effets de l’automatisation.**

- **Elle enchaîne les étapes jusqu’à l’acte.** Un agent qui planifie et appelle des outils est une chaîne à N maillons qui modifie des bases de données, publie ou engage des transactions : le pouvoir d’agir revient à la couche la moins garantie.
- **Elle érode les contrôles humains implicites.** La lenteur du travail fournissait des ordres de grandeur attendus, l’hésitation d’un collègue signalait sa limite, une forme soignée témoignait d’un fond travaillé. Un modèle s’exprime de la même voix assurée qu’il ait raison ou tort, et la forme parfaite devient gratuite. Un essai randomisé de 2025 a trouvé des développeurs expérimentés ralentis d’environ 19 % par leurs outils, alors qu’ils se croyaient accélérés d’environ 20 %. Et relire le brouillon d’un modèle sans s’être formé d’abord son propre jugement revient à lire deux fois la même représentation.
- **Elle corrèle les angles morts.** Quand producteurs et relecteurs s’appuient sur les mêmes modèles, ceux-ci corrigent les étourderies de chacun mais rendent leurs propres omissions communes à tous : c’est le « prêteur unique ». Vingt journalistes qui reprennent la même dépêche ne sont pas vingt témoins. Au même moment, la pression du volume pousse à rogner l’évaluation indépendante, devenue le véritable goulet d’étranglement.

D’où un avertissement contre-intuitif : un outil plus fiable peut composer un système plus risqué. Un producteur qui se trompe dans 10 % des cas, mais dont 1 % seulement des erreurs échappent au contrôle, laisse passer 0,1 % d’affirmations fausses ; un producteur à 1 % d’erreurs dont 90 % échappent en laisse passer 0,9 %. Le livre présente ce cas comme une possibilité, non comme une fréquence.

**Les parades proposées.**

- **Distinguer ce qui se répète de ce qui ne se joue qu’une fois.** On calibre le répétitif. Pour la décision unique, on ajoute à l’estimation une *marge d’humilité* (jugement de prudence, non mesure), on place un *verrou* où l’action attend un contrôle indépendant, et l’on explore dans des *bacs à sable* où l’erreur coûte peu et se défait.
- **Interroger tout chiffre assuré.** Sous quelles conditions tient-il ? Qu’est-ce qui le ferait changer ? Comment pourrait-il être faux ? Qu’a-t-on choisi de ne pas modéliser ?
- **Organiser les contrôles sur trois niveaux.** L’*attitude* : écrire son attente avant de lire le résultat, pratiquer le pré-mortem, élargir les mondes possibles envisagés. Le *placement* : contrôler là où une sortie devient un acte, par quelqu’un qui sait lire le niveau sous-jacent. L’*organisation* : budgéter la capacité d’évaluation et y plafonner la production, afficher l’état de vérification de chaque résultat, tenir un historique, et mesurer l’échappement par des erreurs injectées, comme la sûreté aéroportuaire projette des menaces fictives sur les écrans de contrôle des bagages.

Ce diagnostic ne conduit ni au scepticisme paralysant ni au rejet de l’automatisation : là où l’on ne peut plus acheter une garantie une fois pour toutes sur l’outil, il faut organiser lucidement ses contrôles.

## Situer l’œuvre

L’œuvre ne relève d’aucune école unique : elle fait dialoguer des disciplines d’ordinaire cloisonnées autour d’une seule question, celle de savoir ce qui peut contredire une affirmation fausse avant qu’elle ne devienne un acte.

| Tradition | Ce que l’œuvre en retient | Repères |
| --- | --- | --- |
| Philosophie des sciences | Problème de l’induction, arrière-plan tacite des lois, problème du cadre, faillibilisme | Hume, Russell, Goodman, Hempel, Cartwright ; McCarthy et Hayes, Dennett ; un esprit proche de Popper, Duhem et Quine |
| Probabilités et statistique | Probabilité comme jugement, calibration, sévérité d’un test, modèles mal spécifiés | Ramsey, de Finetti, Savage ; Deborah Mayo ; George Box |
| Théorie de la décision | Utilité espérée subjective, décisions uniques, valeur de l’information | von Neumann et Morgenstern, Savage ; Knight, Ellsberg, Simon ; Raiffa et Schlaifer ; Taleb |
| Sûreté de fonctionnement | Défaillances de mode commun, redondance, analyse d’accidents | Knight et Leveson ; voisinage de Perrow, Reason, Vaughan |
| Génie logiciel | Contrats, preuve de programmes, vérification et validation | Hoare, Dijkstra, Meyer |
| Apprentissage automatique | Compétence irrégulière, hallucinations, complaisance, dégradation des modèles entraînés sur leurs propres productions | Littérature récente sur la fiabilité des grands modèles de langage |
| Économie de l’information | Signal coûteux, sélection adverse, mesure devenue cible | Spence, Akerlof, Goodhart |
| Facteurs humains | Ironie de l’automatisation, lassitude face aux alarmes, pré-mortem | Bainbridge, Klein |
| Critique de l’IA (livre de 2022) | Refus de l’anthropomorphisme, défense de l’intuition humaine | Objection de Lady Lovelace, Dreyfus ; en France, Ganascia, Sadin |

Le patronage de Descartes, affiché par le titre de 2022, est celui de la « morale par provision » : quand l’action ne souffre pas de délai, suivre les opinions les plus probables. Tout le projet tient dans ce glissement, de la certitude comme idéal à la décision raisonnée sous incertitude.

Aucune pièce n’est inédite, et l’œuvre le reconnaît. Ce qui l’est davantage, c’est un vocabulaire commun, applicable aussi bien à une note de calcul qu’à un rapport d’expertise ou à une chaîne d’agents logiciels : comparateur, cinq conditions, probabilité d’échappement, blanchiment, cadre comme cause commune. Plusieurs formulations sont nettes et, semble-t-il, originales : « la formalité change la colonne, non la ligne » ; la distinction entre l’omission structurelle (le facteur est absent du modèle) et l’omission de saillance (il y figure sans être mobilisé) ; le « prêteur unique » ; l’exigence de se former son jugement avant de consulter un modèle. Le livre de 2026 change aussi de registre par rapport à celui de 2022 : il ne dit plus ce que les machines ne pourraient pas faire, mais quelles garanties elles offrent ou n’offrent pas, ce qui le rapproche des approches de sûreté de l’IA fondées sur la surveillance et la défense en profondeur.

Plusieurs voisins naturels restent peu ou pas convoqués : Popper et Kuhn, pourtant proches de la thèse ; les « petits mondes » de Savage, qui posaient déjà le problème ; les théories de la décision sous ambiguïté et de la robustesse ; la sociologie des accidents (Perrow, Reason, Vaughan) ; et une tradition française qui aurait offert des interlocuteurs évidents, d’Alain Desrosières à René Amalberti, et *Agir dans un monde incertain* de Callon, Lascoumes et Barthe.

## Usages possibles

La grille vaut partout où l’on agit d’après un résultat que l’on n’a pas produit soi-même, ou produit trop vite pour l’avoir vraiment contrôlé.

- **Ingénierie et simulation.** Exiger que chaque résultat voyage avec ses unités, ses hypothèses et ses réserves, et rappeler qu’une barre d’erreur ne couvre que les alternatives admises.
- **Sûreté, qualité et audit.** Utiliser les cinq conditions comme liste de contrôle d’une procédure de revue, avec une question simple : quelle erreur cette étape peut-elle arrêter, que le producteur n’aurait pas arrêtée lui-même ? Mesurer l’échappement par erreurs injectées dans la relecture de rapports ou de code.
- **Déploiement de l’IA dans les organisations.** Explorer dans des bacs à sable, verrouiller les points où un agent toucherait le monde réel, confier la relecture à qui sait lire le niveau sous-jacent, afficher l’état de vérification, plafonner la production à la capacité de contrôle ; et, individuellement, se faire une idée avant d’interroger le modèle, puis lui soumettre le problème nu plutôt que la réponse espérée.
- **Recherche et édition scientifique.** Quand auteurs et relecteurs utilisent les mêmes outils, l’évaluation par les pairs risque de devenir une copie : traçabilité de la provenance, distinction entre résultat exploratoire et résultat établi, déclaration de l’usage d’outils génératifs y trouvent une justification de fond.
- **Décision publique et gouvernance.** Les quatre questions conviennent à un élu devant une étude d’impact comme à un dirigeant devant un tableau de bord. Pour un régulateur, une profession entière adossée à deux ou trois modèles présente un risque de mode commun que les évaluations outil par outil ne voient pas.
- **Formation.** Le livre de 2022 reste une initiation accessible aux probabilités et à la décision ; celui de 2026 plaide pour préserver, contre l’ironie de l’automatisation, les compétences que l’exception exigera.

Dans tous les cas, l’apport principal est un déplacement du regard : de la question « cet outil se trompe-t-il souvent ? » à la question « quand il se trompe, qu’est-ce qui nous en avertira, et à temps ? »

## Limites et tensions

Le livre de 2026 a le mérite rare de dresser lui-même l’inventaire de ses faiblesses : statut de chaque énoncé, tensions laissées ouvertes, observations qui l’affaibliraient. Les réserves qui suivent prolongent cet inventaire plus qu’elles ne le contredisent.

**Le premier livre : une thèse qui oscille, un argument daté.** Au sens modeste, la subjectivité de la rationalité est juste mais classique : c’est le point de départ de la théorie bayésienne de la décision. Poussée jusqu’à nier qu’une anticipation puisse être « plus juste » qu’une autre, elle devient excessive, puisque la calibration et les règles de score permettent de comparer des prévisionnistes ; le second livre corrige ce glissement. L’argument contre l’« intelligence » des machines passe du niveau matériel (des électrons, des instructions) au niveau des capacités, et ses affirmations d’impossibilité « par nature » ont été fragilisées par l’auto-apprentissage, puis par les modèles généralistes et les agents. Manquent aussi Simon, Kahneman et Tversky, la causalité et une relecture éditoriale. La partie pédagogique garde sa valeur.

**Le second livre : des distinctions plus que des théorèmes.** Les calculs sont exacts, mais les « résultats sous hypothèses » reformulent largement leurs hypothèses. La force de l’argument tient aux distinctions qu’il organise et aux ponts vers la pratique (coût croissant de l’indépendance, corrélation sous modèle partagé, érosion des contrôles humains), que le livre classe lui-même parmi les hypothèses de travail. La base empirique est mince et datée, souvent une étude unique ; d’autres essais ont d’ailleurs mesuré des gains nets de productivité sur des tâches de programmation délimitées.

**Une frontière poreuse.** La critique statistique des modèles (analyse des résidus, contrôles prédictifs) détecte souvent une inadéquation sans modèle concurrent ; en simulation, la « discordance de modèle » prend en charge une part de l’incertitude structurelle. Pour les modèles de langage, reformuler, décomposer ou faire débattre peut réveiller une connaissance latente sans apport extérieur, ce que la notion d’omission de saillance admet sans le mesurer. Le contraste entre logiciel classique et modèles appris est lui aussi de degré plutôt que de nature : les couches basses ont leurs arrière-plans tacites, et l’interprétabilité commence à fournir des « adresses » partielles.

**La marge d’humilité.** Sans règle pour la fixer, elle risque d’être choisie après coup ; aux enjeux extrêmes, une marge additive conduit à l’abstention universelle. Or l’aviation ou le nucléaire réduisent le facteur omis lui-même (défense en profondeur, retour d’expérience) et pèsent le coût de l’inaction, que le modèle ignore. Les théories de la décision sous ambiguïté offrent des voies intermédiaires, laissées de côté.

**L’énigme du producteur plus fiable.** Avec les paramètres que le livre retient plus loin, son propre modèle montre au contraire une baisse du risque sous modèle partagé. L’avertissement serait plus solide s’il était formulé en termes de risque extrême : un modèle partagé peut réduire l’erreur moyenne tout en concentrant le risque sur des défaillances rares, silencieuses et simultanées.

**L’économie politique des contrôles.** Plafonner la production ou sanctuariser l’évaluation suppose résolu un problème d’action collective : qui rationnera son débit sous la pression de la concurrence ? Le droit de la responsabilité, l’assurance et les normes de sûreté, leviers naturels, restent peu étudiés, de même que le risque de voir les procédures tourner au rituel.

**La méthode appliquée à elle-même.** Élaboré avec des modèles de langage, le livre de 2026 le déclare et en tire la leçon : ce sont des « comparateurs empruntés », utiles contre les erreurs de l’auteur, non contre leurs propres angles morts. Ses absences ont d’ailleurs un air de famille, et le recours répété à un article antérieur non évalué par des pairs illustre le risque de corroboration circulaire qu’il décrit. Sa prose, soignée mais redondante, appelle sa propre règle : la tenue du texte ne prouve rien sur son fond.

## La fabrique des deux livres

Les deux ouvrages ont été fabriqués de manières presque opposées, ce qui offre une rare expérience naturelle. Le premier a été écrit seul, sans modèle de langage ; le second a été bâti en trois jours par des agents de deux fournisseurs, à partir d’idées déjà mûres et sous la direction de l’auteur. Un journal d’heures tenu à la main pour 2022 et le relevé des sessions d’agents pour 2026 permettent de chiffrer l’écart.

|  | Livre de 2022 | Livre de 2026 |
| --- | --- | --- |
| Mode de production | Écrit seul, sans modèle de langage | Rédigé par des agents de deux fournisseurs, sous supervision |
| Durée calendaire | Environ 10 mois, 145 jours de travail | 3 jours, 73 h écoulées |
| Heures de travail | ≈ 723 h de travail propre, déclarées (borne basse) | ≈ 29 h d’activité d’agents journalisée ; supervision estimée à 30–40 h, environ 132 consignes |
| Texte final | Environ 65 000 à 75 000 mots | Environ 102 000 mots, 277 pages |
| Volume engendré | Le texte lui-même | ≈ 6,3 millions de jetons produits (35 à 40 fois le texte final) |
| Coût en calcul | Aucun | ≈ 260 à 360 $ au tarif public des API |
| Relecture | 84 h de correction, plus 43 h pour le manifeste | Passes automatisées ; relecture humaine complète encore à faire |

**Ce que mesurent les chiffres.** L’écart est d’environ vingt fois en heures humaines et d’une centaine de fois en temps calendaire, pour un texte plus long. Un premier jet complet de tous les chapitres a été obtenu en un peu plus de sept heures, pour un coût de calcul inférieur à un dollar par page (environ 1 960 $ sans la mise en cache des contextes). En pratique, le travail s’est fait sur abonnement, et la contrainte ressentie a été le quota plutôt que l’argent.

La comparaison mesure pourtant la mise en livre d’idées arrêtées, non leur production. Le livre de 2026 repose sur un article, deux essais, une conférence et une carte des idées issus d’environ une année de recherche elle-même assistée par des modèles, et surtout sur le livre de 2022, où se trouvent déjà l’essentiel de sa première partie et le noyau de la deuxième. Compté honnêtement, il s’appuie sur au moins les mêmes 723 heures, augmentées d’une centaine d’heures de recherche, puis du chantier. La relecture humaine complète, estimée entre 40 et 120 heures, reste à faire : elle porterait le coût humain à 70 à 160 heures, encore 4,5 à 10 fois moins qu’en 2022. Les relevés, enfin, sont incomplets de part et d’autre.

**Un chantier qui applique sa propre thèse.** Le plus frappant n’est pas la vitesse, mais l’organisation, conçue comme une architecture de contrôles :

- des spécifications verrouillées d’abord (terminologie, statut de chaque proposition, nombres engendrés par programme, vérificateur automatique), qui ont permis à une dizaine d’agents de rédiger en parallèle sans que le livre se disperse ;
- un fournisseur qui rédige, l’autre qui relit : la diversité des modèles servait de comparateur qui se trompe autrement ;
- des lecteurs neufs et isolés, sans communication entre eux : onze lecteurs ont relevé 328 constats en seize minutes ;
- un juge étalonné avant usage : après qu’un essai de reprise stylistique libre eut réécrit 82 % des phrases d’un chapitre et changé le sens une vingtaine de fois, le juge automatique a dû rejeter les 30 dérives connues qu’on lui soumettait avant d’être employé ;
- des modèles qui proposent et des scripts qui appliquent, chapitre par chapitre, sous le contrôle du vérificateur.

L’auteur n’a presque rien écrit de la prose. Son temps est passé dans la décision : fixer la direction, trancher entre des options, arbitrer, choisir ce qu’il ne fallait pas automatiser (la relecture finale notamment) et surveiller les quotas.

**Ce que la comparaison enseigne.** Le chantier confirme d’abord le déplacement du goulet d’étranglement que décrit le livre : produire est devenu presque gratuit, les notes de travail représentant à elles seules plus de trois fois le livre, tandis que l’évaluation reste rare et lente. Il illustre ensuite la perte du signal coûteux : le texte de 2026 est très correct et d’une terminologie cohérente, mais sa prose est plus uniforme que celle de 2022 et se répète. Il suggère enfin où se loge désormais la valeur : non dans la rédaction, mais dans la maturation des idées, qui a pris des années, et dans la vérification indépendante, qui reste à achever et pourrait bien devenir la part la plus longue du travail.

## Bilan

Ce qui s’énonçait en 2022 comme un appel à l’humilité du jugement humain devant les algorithmes devient, en 2026, une question d’architecture : comment disposer nos instruments, nos interfaces et nos institutions pour que nos représentations restent exposées à la contradiction du réel ? L’apport le plus durable de l’œuvre est ce déplacement de la question. Le péril qu’elle décrit n’est ni une intelligence étrangère ni une impuissance des méthodes, mais un déplacement silencieux de nos garanties : des composants sans contrat écrit au cœur de nos chaînes d’action, une aisance qui endort les signaux du doute, des angles morts alignés entre ceux qui produisent et ceux qui vérifient.

Sa principale faiblesse en est le revers : une synthèse conceptuelle encore en attente d’étalonnage, dont les modèles sont des épures et les remèdes n’ont pas été mesurés. Le programme qu’elle ouvre est pourtant clair : mesurer l’échappement des erreurs par injection dans des relectures mixtes, humaines et automatiques ; estimer la part des causes partagées quand une profession adopte les mêmes modèles ; éprouver les parades ; relier la marge d’humilité aux théories de la décision sous ambiguïté et aux normes de sûreté. Le second livre demande à être lu comme il se lit lui-même, comme une démarche de travail exposée à la contradiction ; son meilleur comparateur, dit-il, est la pratique du lecteur, seule capable d’apporter le contre-exemple qui se trompe autrement.

### Sources

- *Un discours de la méthode au XXIe siècle. Risques et limites de l’« intelligence artificielle »*, 2022.
- *Agir d’après une représentation du monde. Cadre, contrôles et décision, de l’informatique classique à l’IA*, version de travail, novembre 2026.
- Revue de littérature interdisciplinaire en neuf volets accompagnant le livre de 2026, recensions des deux livres et lectures croisées.
- Relevé du processus de construction du livre de 2026 et journal d’heures du livre de 2022, compilés à partir de l’historique git et des journaux de sessions d’agents.
