# Ce qui peut nous détromper à temps : panorama d’une recherche en deux livres

22 novembre 2026

## Une question, deux livres

Les deux ouvrages poursuivent, à quatre ans d’intervalle, une même interrogation. Nous n’agissons jamais sur le monde tel qu’il est, mais d’après une représentation que nous en avons construite : des mesures, des catégories, des équations, des programmes, et désormais des modèles appris. Qu’est-ce qui peut alors nous avertir, avant qu’il ne soit trop tard, que cette représentation fait fausse route ?

Le premier livre, *Un discours de la méthode au XXIe siècle* (2022), aborde la question en pédagogue. Il prend la forme d’un récit : un vieux professeur de statistique accompagne six étudiants venus de disciplines différentes (économie, ingénierie, informatique, mathématiques, science politique, philosophie), chargés de conseiller leur université sur le partage d’un supercalculateur flambant neuf. Chemin faisant, ils reconstruisent la logique, les probabilités, la statistique et la théorie de la décision, puis concluent par un manifeste pour une rationalité « humble, critique et humaine » et une mise en garde contre les espoirs placés dans le raisonnement automatisé.

Le second, *Agir d’après une représentation du monde* (2026), donne au même projet sa forme mûre et technique. Il abandonne la fiction et resserre la question : à quelles conditions un contrôle peut-il réellement arrêter une erreur ? La réponse tient en une phrase, qui sert de devise à l’ensemble : **une erreur n’est arrêtée que par ce qui peut se tromper autrement.** Sur ce socle, l’ouvrage bâtit une théorie des contrôles qu’il applique tour à tour au logiciel classique, à l’apprentissage automatique, aux grands modèles de langage, aux agents automatisés et aux institutions.

Lus ensemble, les deux livres dessinent une trajectoire nette. Le premier soutient surtout que la rationalité est nécessairement subjective et que les machines ne sauraient nous fournir le recul critique qui nous fait défaut. Le second conserve ce point de départ, mais convertit un avertissement philosophique en discipline d’ingénieur : que contrôler, où, par qui, et comment savoir si les contrôles fonctionnent.

Ce panorama suit les idées plutôt que l’ordre des chapitres. Il expose les notions centrales en termes simples, les situe parmi les penseurs et les écoles dont elles procèdent, puis examine sans complaisance ni sévérité gratuite ce que l’œuvre apporte, où elle reste fragile et où elle peut servir. Il s’appuie aussi sur les recensions et sur la revue de littérature qui accompagnent les deux ouvrages.

## Les questions directrices et les messages principaux

La question directrice s’énonce simplement et ne s’épuise pas : comment agir au mieux à travers une représentation forcément incomplète, et comment organiser nos raisonnements pour qu’ils puissent être démentis à temps lorsqu’ils se trompent ? Six messages structurent la réponse.

1. **Nous agissons d’après une représentation, et le monde répond à nos actes, non à nos modèles.** Une règle aussi familière que « l’eau bout à 100 °C » ne vaut que si tout un arrière-plan reste dans son état habituel : eau pure, récipient ouvert, altitude ordinaire, et ainsi de suite sans fin. Choisir ce que l’on énonce et ce que l’on tait, c’est choisir un *cadre* : un ensemble fini de variables, de catégories, de modèles et d’objectifs, fixé avant tout calcul.
2. **La rigueur exercée dans un cadre ne garantit pas le cadre.** La déduction transporte la vérité des prémisses sans la créer ; l’induction généralise, pourvu que l’avenir ressemble au passé sur les points retenus. La dinde qui note chaque matin l’heure du grain dispose, la veille de Noël, d’une série statistique irréprochable : son malheur ne vient pas d’une faute de calcul, mais d’une variable absente de son cadre.
3. **Une probabilité est un jugement, non une propriété des choses, mais un jugement qui se met à l’épreuve.** Deux navigateurs qui estiment l’un à 5 %, l’autre à 0,1 % le risque de démâter peuvent décider aussi rationnellement l’un que l’autre, chacun d’après ce qu’il croit. Une traversée isolée les départage mal ; seule la répétition, consignée et notée, permet de juger un prévisionniste.
4. **Une erreur n’est arrêtée que par ce qui peut se tromper autrement.** Relire son propre calcul, relancer une simulation ou demander à un modèle de vérifier sa propre réponse débusque les étourderies, mais jamais ce que tous ces contrôles omettent ensemble. Un contrôle n’arrête une erreur que s’il réunit cinq conditions précises, détaillées plus bas.
5. **Les modèles appris ont acheté une portée nouvelle en dépensant les garanties de l’informatique classique.** Le logiciel traditionnel repose sur des promesses écrites, vérifiables d’avance, dont la violation laisse une trace localisable. L’apprentissage automatique sait faire ce qu’aucune règle écrite ne savait faire, mais au prix de cette garantie : l’erreur d’un grand modèle de langage a la même aisance qu’une réponse juste, et aucune ligne de code à corriger.
6. **L’automatisation transforme nos contrôles autant que nos outils.** Elle enchaîne les étapes jusqu’à l’action, efface les contrôles humains implicites qu’engendrait la lenteur du travail, et aligne les angles morts lorsque producteurs et relecteurs s’appuient sur les mêmes modèles. D’où un avertissement contre-intuitif : un outil plus fiable peut composer un système plus risqué, si ses erreurs échappent davantage aux contrôles.

De ces constats découle une conduite plutôt qu’une doctrine : calibrer ce qui se répète, verrouiller ce qui ne se joue qu’une fois, explorer là où l’erreur coûte peu, et faire de l’évaluation indépendante une ressource que l’on protège. Le premier livre en tirait une leçon plus générale et plus polémique, qui tenait en une formule : investir dans l’intelligence humaine plutôt que dans la puissance de calcul. Le second la traduit en architecture de contrôles.

## Les notions clés et le cadre théorique

L’édifice repose sur un petit nombre de notions, introduites sans aucune référence à l’intelligence artificielle, puis appliquées à elle. Cette séparation est voulue : l’argument entend valoir indépendamment des générations d’outils.

### Représentation, cadre et arrière-plan tacite

Toute règle portant sur le monde a la forme « si A, et pourvu que tout l’arrière-plan reste dans son état habituel, alors B ». Ajouter des conditions déplace cet arrière-plan sans jamais l’épuiser. Énoncer davantage rend la règle lourde et fragile, énoncer moins laisse des exceptions muettes, et aucun réglage ne supprime les deux risques à la fois.

Le *cadre* est le choix qui sépare l’énoncé du tacite : variables retenues, catégories, classe de modèles, objectif. Il précède tout calcul, et aucune rigueur formelle ne l’abolit : un graphe causal ou une hypothèse d’échangeabilité, si élaborés soient-ils, sont eux-mêmes des cadres. Le célèbre « problème du cadre » de l’intelligence artificielle symbolique n’est, dans cette lecture, qu’un cas particulier d’une limite générale : on ne peut spécifier d’avance tout ce qui sera pertinent.

### Trois incertitudes, et ce que tait une barre d’erreur

La distinction usuelle entre incertitude *aléatoire* (la variabilité des choses, comme la dispersion des propriétés d’un alliage d’une coulée à l’autre) et incertitude *épistémique* (l’imperfection de notre savoir, comme la méconnaissance des efforts appliqués) est présentée comme un choix de modélisation : elle marque l’endroit où l’analyste cesse d’affiner. Une troisième, l’incertitude *ontologique*, porte sur le cadre lui-même, c’est-à-dire sur la pertinence des variables et des modèles retenus.

D’où une proposition simple mais lourde de conséquences : une incertitude chiffrée mesure toujours un désaccord au sein d’un ensemble d’alternatives admises d’avance. Ce sur quoi toutes les variantes s’accordent, parce qu’aucune ne le contient, ne produit aucun désaccord, donc aucune barre d’erreur. L’ingénieur qui conclut qu’une ferrure supporte sa charge avec un coefficient de sécurité de 1,8 a exploré la dispersion de l’alliage et l’incertitude sur les efforts ; si la corrosion en air salin ne figure dans aucune équation, la note de calcul reste muette. Dix relecteurs fidèles à la même note d’hypothèses tomberont d’accord : leur accord mesure la cohérence de la note, non la présence de la page qui manque.

La nuance compte : un facteur omis qui a varié pendant la collecte des données se glisse dans la dispersion, que l’on impute au hasard sans pouvoir le nommer ; seul un facteur resté constant ne laisse aucune trace. Coefficients de sécurité, analyses de sensibilité, moyennes de modèles ou détecteurs de données atypiques restent indispensables, mais ils travaillent à l’intérieur du cadre.

### Probabilité, surprise et calibration

Les deux livres lisent la probabilité comme un jugement : elle répartit un poids sur les « mondes possibles » compatibles avec ce que l’on sait. Le second précise ce que le premier laissait parfois glisser : relative à une information et à un cadre, une probabilité n’est pas arbitraire pour autant. Elle obéit aux règles du calcul et se confronte aux faits.

Cette confrontation a une forme précise. Une issue isolée départage mal deux prévisions, surtout lorsque c’est l’issue la plus probable qui se réalise : une matinée paisible ne dit presque rien. La répétition, elle, permet de juger le prévisionniste, à condition de consigner ses prévisions, de les noter par une règle de score « strictement propre » (qui récompense celui qui annonce ses vraies probabilités) et d’en vérifier la calibration : il doit pleuvoir environ sept fois sur dix les jours où l’on annonce 70 % de risque de pluie. Ce recours fait défaut, précisément, devant ce qui n’arrive qu’une fois. D’où un conseil de méthode : « raisonner à l’envers », c’est-à-dire chercher quelle variation plausible de l’arrière-plan renverserait la conclusion, plutôt que de défendre une réponse unique.

### Décider d’après ce que l’on croit

La théorie de la décision retenue est celle de l’utilité espérée subjective : on pondère la valeur des conséquences par ses propres probabilités, parce que la décision se prend avant que le monde réponde. Face à une option sûre, l’option risquée ne se justifie que si la probabilité d’échec estimée reste sous un seuil, où ΔU désigne le gain espéré et L la perte encourue, tous deux mesurés par rapport à l’option sûre :

```latex
p^{*} = \frac{\Delta U}{\Delta U + L}
```

Si la casse coûte vingt-cinq fois ce que rapporte la victoire, le seuil vaut 1/26, un peu moins de 4 %. Le navigateur qui estime le risque à 5 % choisit le bateau renforcé, celui qui l’estime à 0,1 % s’élance sur le bateau léger, et tous deux sont rationnels. Lorsque la perte devient démesurée, comme à la roulette russe, le seuil tend vers zéro. C’est le nœud des décisions uniques : le décideur compare au seuil un chiffre issu de sa représentation, tandis que le monde répond selon ce qui est, fissure invisible du mât comprise.

### Le contrôle et ses cinq conditions

Le cœur théorique du second livre est une définition : une erreur n’est détectée avant l’action que si une affirmation est confrontée à un *comparateur* censé concorder avec elle, que la confrontation fait apparaître un désaccord et que quelqu’un en prend acte. Cette évidence apparente se déplie en cinq conditions simultanées :

1. **Existence** : un comparateur existe (second calcul, règle écrite d’avance, avis d’un pair, mesure sur le terrain).
2. **Différence** : il peut se tromper autrement que l’affirmation à l’égard de la cause d’erreur considérée.
3. **Comparabilité** : les deux s’expriment dans les mêmes grandeurs, avec leurs unités et leurs conditions.
4. **Arrivée à temps** : le désaccord apparaît avant que l’action ne soit engagée de façon irréversible.
5. **Prise en compte** : quelqu’un entend l’alerte et a l’autorité de suspendre ou de modifier la décision.

Qu’une seule condition manque pour une famille d’erreurs, et toutes ces erreurs passent : leur probabilité d’échappement vaut 100 %. La grille sert d’abord à distinguer l’existence nominale d’un contrôle de sa capacité réelle d’arrêter une erreur. Relu ainsi, l’accident de la navette Challenger combine plusieurs ruptures : le graphique examiné la veille, qui omettait les vols sans dommage, a fait céder la différence et la comparabilité, et le rejet des objections techniques en séance a rompu la prise en compte.

### Le cadre comme cause commune

La sûreté de fonctionnement sait depuis longtemps que deux pompes de secours branchées sur la même alimentation ne protègent pas contre une coupure de courant : elles partagent une cause commune de défaillance. Les livres transposent cette idée au raisonnement. Face à un facteur que le cadre omet, tous les contrôles calculés dans ce cadre sont des copies les uns des autres : ils s’accorderont à la troisième décimale tout en se trompant ensemble.

Les observations du monde échappent en principe à ce cercle, puisque le monde n’est pas calculé à partir de notre cadre. Encore faut-il que le facteur omis ait varié pendant la collecte et que ses effets se lisent dans ce que l’on a enregistré : un essai de charge dans l’air sec d’un laboratoire ne révélera jamais cinq ans de brouillard salin. Quant à une « méta-procédure » qui détecterait automatiquement les cadres incomplets, elle devrait elle-même fixer d’avance la liste de ce qu’elle surveille, et le problème remonte d’un cran. Une pertinence nouvelle n’entre donc dans un cadre que du dehors : par un tiers qui voit autrement, ou par l’épreuve du monde.

### Chaînes, contrôles croisés et blanchiment

Tout composant (personne, équipe, programme, modèle) a un *angle mort* : les causes d’erreur qu’il ne peut percevoir. La façon de les assembler décide si ces angles morts s’additionnent ou se réduisent. Dans une *chaîne*, chaque maillon tient pour acquis ce qu’il reçoit, et le résultat hérite de toutes les erreurs, y compris celles qui naissent aux interfaces. Dans un *contrôle croisé*, producteur et contrôleur traitent la même question et l’on compare leurs réponses : seul subsiste l’angle mort qu’ils partagent.

Ce gain a un prix. L’indépendance est toujours relative à une classe d’erreurs, et elle tire contre la comparabilité : plus le contrôleur est éloigné du producteur par ses méthodes ou sa discipline, mieux il voit ses omissions, mais plus il est difficile de traduire son objection en désaccord décisif. Il existe sans doute une bonne distance, entre le jumeau qui ne voit rien de neuf et l’étranger dont l’objection ne porte pas, mais elle ne se calcule pas. Le *blanchiment*, enfin, désigne la perte des conditions d’un résultat (hypothèses, unités, définitions) quand il change de mains : c’est ainsi que des impulsions exprimées en livres-force-secondes, transmises sans unité là où l’on attendait des newtons-secondes, ont coûté la sonde Mars Climate Orbiter en 1999.

### Sévérité, fausses alertes et probabilité d’échappement

Un contrôle passé sans alerte ne prouve quelque chose que s’il aurait donné l’alerte en cas d’erreur : c’est la notion de *sévérité*, empruntée à la philosophie des statistiques. Inversement, quand les erreurs se raréfient devant un contrôleur dont le taux de fausses alertes ne bouge pas, la plupart de ses alertes deviennent fausses, et ceux qui les reçoivent finissent par les écouter moins.

Le risque se décompose alors en deux facteurs : **risque résiduel = taux d’erreur du producteur × probabilité que ces erreurs échappent aux contrôles.** Les évaluations comparatives notent le producteur seul et ne mesurent que le premier facteur ; toute la question de l’architecture des contrôles porte sur le second. Dans le modèle du livre, la part des causes d’erreur que le contrôleur partage avec le producteur forme un plancher incompressible : aucune vigilance ne le perce, seul un comparateur qui se trompe autrement l’abaisse.

### Une matrice à deux axes

La synthèse range les erreurs selon deux questions. Leur cause est-elle *dans* le cadre (faute de calcul, bogue, paramètre erroné) ou *hors* du cadre (facteur omis) ? L’erreur est-elle *signalée*, parce qu’un comparateur la contredit, ou *silencieuse*, parce que rien ne la contredit ? Le premier axe est fixé par le cadre et ne s’inspecte pas de l’intérieur ; le second dépend des comparateurs disponibles et peut se construire.

| | Erreur signalée (un comparateur la contredit) | Erreur silencieuse (rien ne la contredit) |
| --- | --- | --- |
| **Cause dans le cadre** (faute de calcul, bogue, paramètre) | *Faute rattrapée* : un test ou un contre-calcul la contredit avant l’usage (ex. : bogue arrêté par un test) | *Faute muette* : rien ne la contredit à temps ; case que peuplent les modèles appris (ex. : réponse fluide et fausse) |
| **Cause hors du cadre** (facteur absent du modèle) | *Omission révélée* : un regard extérieur ou une mesure de terrain la fait apparaître (ex. : corrosion signalée par un tiers) | *Omission ignorée* : aucun contrôle calculé dans le cadre ne peut la voir (ex. : la ferrure corrodée) |

*Sur la ligne du haut, formaliser (contrat, test, preuve) fait passer une faute de la colonne silencieuse à la colonne signalée ; sur la ligne du bas, seul un tiers ou l’épreuve du monde le peut. La ligne est fixée par le cadre : aucun formalisme ne l’inspecte de l’intérieur.*

D’où une formule frappante : **la formalité change la colonne, non la ligne.** Écrire un contrat, une spécification ou une preuve rend une erreur interne détectable ; cela ne certifie jamais l’adéquation du cadre. Les composants appris tendent à peupler la case la plus inconfortable, celle des erreurs internes au cadre mais silencieuses.

Quatre sources de comparateurs restent disponibles : un énoncé fixé d’avance (test, spécification, preuve), les contrôles personnels de celui qui produit ou utilise, un autre raisonneur (humain ou machine) et le monde. L’automatisation les transforme inégalement. Elle peut reconstruire une *vérification* (résoudre correctement le problème posé) autour d’un composant appris, là où existe un contrôle mécanique ; elle n’accélère guère la *validation* (poser un problème assez fidèle au réel), qui reste tributaire d’un apport extérieur.

### Les notions propres au premier livre

Le livre de 2022 posait déjà plusieurs de ces pierres sous d’autres noms. Il défendait le caractère « nécessairement subjectif » de la rationalité : nul agent, humain ou machine, ne peut savoir a priori quelle décision est la bonne, puisqu’il décide d’après ce qu’il croit et non d’après ce qui adviendra. Il distinguait trois limites : une limite *mathématique* (hors du monde idéal des mathématiques, aucune conclusion ne s’impose avec certitude), une limite *épistémique* (toute prédiction repose sur une « régularité du réel » décrite avec une précision finie) et une limite *économique* (chercher à en savoir plus a un coût, qu’il faut mettre en balance avec le bénéfice attendu).

Ce dernier arbitrage, qu’il nommait « exploration statistique », correspond à ce que la théorie de la décision appelle la valeur de l’information. Le livre formulait enfin une thèse que le second reprend sous forme technique : « formaliser, c’est déjà choisir ». Les machines, qui appliquent un cadre formel que nous leur avons donné, héritent de nos limites sans pouvoir regarder au-delà.

## Les domaines couverts et leurs liens

L’œuvre traverse au moins neuf disciplines d’ordinaire cloisonnées, et c’est là l’une de ses singularités. Une seule question leur sert de dénominateur commun : qu’est-ce qui, dans un dispositif donné, peut contredire une affirmation fausse avant qu’elle ne devienne un acte ? Chaque discipline fournit une pièce de la réponse.

| Domaine | Ce que l’œuvre en retient | Rôle dans l’argument |
| --- | --- | --- |
| Philosophie des sciences | Problème de l’induction, dinde inductiviste, lois « toutes choses égales par ailleurs », problème du cadre | Montrer que la rigueur interne ne certifie pas le cadre |
| Probabilités et statistique bayésienne | Probabilité comme jugement, révision par la règle de Bayes, surprise, calibration, règles de score | Juger une prévision et un prévisionniste |
| Quantification des incertitudes | Incertitudes aléatoire, épistémique et ontologique, coefficients de sécurité, vérification et validation | Dire ce que mesure, et ce que tait, une barre d’erreur |
| Théorie de la décision | Utilité espérée subjective, seuil de décision, décisions uniques ou répétées, valeur de l’information | Décider d’après ce que l’on croit, et savoir quand s’abstenir |
| Sûreté de fonctionnement | Défaillance de mode commun, fiabilité en série et en parallèle, programmation multiversion, retours d’accidents | Penser les contrôles comme une architecture |
| Génie logiciel et vérification formelle | Contrats, préconditions et postconditions, tests, preuve, moniteurs de sûreté, test par mutation | Décrire les garanties « gagnées » par l’informatique classique |
| Apprentissage automatique et grands modèles de langage | Prédiction du fragment suivant, compétence irrégulière, hallucinations, complaisance, effondrement des modèles | Décrire les garanties « dépensées » par les modèles appris |
| Économie de l’information | Signal coûteux, sélection adverse, loi de Goodhart, monoculture | Expliquer pourquoi la forme ne témoigne plus du fond |
| Facteurs humains et organisations | Ironies de l’automatisation, lassitude face aux alarmes, pré-mortem, capacité d’évaluation | Expliquer l’érosion des contrôles humains et les remèdes |

Le livre de 2022 couvrait déjà une partie de ce terrain, en le distribuant entre ses six personnages : l’économiste, l’ingénieur, l’informaticienne, la mathématicienne, la politiste et le philosophe. Il s’en tenait toutefois à la logique, aux probabilités, à la statistique, à l’apprentissage automatique dans ses formes classiques et à la théorie de la décision. La sûreté de fonctionnement, le génie logiciel, l’économie de l’information et les facteurs humains n’entrent véritablement en scène qu’en 2026, et ce sont eux qui donnent au second livre sa portée pratique.

L’intérêt de ce croisement tient moins à la nouveauté de chaque pièce qu’à leur assemblage. La défaillance de mode commun de l’ingénieur de sûreté, la sévérité du philosophe des statistiques, la valeur prédictive de l’épidémiologiste et le signal coûteux de l’économiste décrivent, chacun dans sa langue, un même phénomène : un contrôle ne vaut que par ce qu’il ne partage pas avec ce qu’il contrôle.

## Situer l’œuvre : penseurs de référence et écoles de pensée

L’œuvre ne se rattache pas à une école unique ; elle se tient au carrefour de plusieurs traditions qu’elle fait dialoguer. Son originalité tient à ce dialogue plus qu’à une rupture avec l’une d’elles.

### Descartes, ou la morale par provision

Le titre du premier livre et son épigraphe se réclament de Descartes, non du Descartes du doute méthodique mais de celui de la « morale par provision » : lorsque l’action ne souffre pas de délai et qu’on ne peut discerner les opinions les plus vraies, il faut suivre les plus probables. Tout le projet est contenu dans ce glissement, de la certitude comme idéal à la décision raisonnée sous incertitude. Le dialogue avec Descartes reste cependant, dans le livre de 2022, davantage un clin d’œil qu’une confrontation suivie.

### L’empirisme critique et le faillibilisme

La filiation la plus profonde est celle de l’empirisme critique. Le problème de l’induction de Hume, le poulet de Bertrand Russell devenu « dinde inductiviste », la « nouvelle énigme » de Goodman fondent l’idée qu’aucune série d’observations ne garantit l’avenir. L’arrière-plan tacite rejoint les clauses « toutes choses égales par ailleurs » discutées par Hempel et Nancy Cartwright, et la connaissance tacite de Polanyi.

La devise du second livre, selon laquelle une erreur n’est arrêtée que par ce qui peut se tromper autrement, est d’esprit très poppérien : une connaissance ne progresse qu’en s’exposant à ce qui peut la contredire. L’idée qu’un cadre ne se révise que du dehors évoque aussi le holisme de Duhem et de Quine, et les révolutions de cadre décrites par Kuhn ou Lakatos. Ces auteurs sont pourtant peu ou pas cités, ce qui prive le lecteur de repères qu’il aurait reconnus.

### Le bayésianisme subjectif, tempéré par la statistique de l’erreur

Pour les probabilités, l’ancrage est la tradition subjective de Ramsey, de Finetti et Savage : la probabilité mesure un degré de croyance cohérent, relatif à un état d’information. Le second livre l’adosse à deux exigences venues d’ailleurs. La première est la mise à l’épreuve des prévisions par la calibration et les règles de score, tradition de la météorologie et de la statistique de la prévision. La seconde est la notion de sévérité, forgée par Deborah Mayo au sein de la statistique de l’erreur, école rivale du bayésianisme, et transposée ici en langage bayésien. On reconnaît enfin le mot de George Box, « tous les modèles sont faux, certains sont utiles », et les travaux sur les modèles mal spécifiés, où le vrai processus n’appartient à aucune des hypothèses envisagées.

### La théorie de la décision et ses limites

Le cadre de décision est celui de von Neumann, Morgenstern et Savage. Savage lui-même distinguait les « petits mondes », où sa théorie s’applique, du « grand monde » dont ils ne sont qu’une coupe : c’est exactement le sujet des deux livres, qui ne l’exploitent pourtant guère. La distinction de Frank Knight entre risque probabilisable et incertitude radicale, le paradoxe d’Ellsberg sur l’aversion à l’ambiguïté, la rationalité limitée d’Herbert Simon et la valeur de l’information de Raiffa et Schlaifer forment le voisinage immédiat. L’œuvre en retrouve les intuitions, parfois sous d’autres noms ; elle laisse de côté les théories formelles de la décision sous ambiguïté et de la robustesse, qui occupent précisément l’espace entre le calcul bayésien et le jugement nu. On pense aussi à Nassim Nicholas Taleb, dont *Le Cygne noir* met en scène la même dinde et la même méfiance envers l’extrapolation.

### La sûreté de fonctionnement et la sociologie des accidents

Le second livre est le plus neuf lorsqu’il transporte en épistémologie les outils de la sûreté : défaillances de mode commun, redondance, défense en profondeur, analyse d’accidents. Il retrouve l’expérience célèbre de Knight et Leveson, qui montra que des programmes écrits indépendamment à partir d’une même spécification se trompaient sur les mêmes cas difficiles. Il dialogue moins avec la sociologie des organisations, alors qu’il en est proche : les « accidents normaux » de Charles Perrow, le modèle des barrières de James Reason, la « normalisation de la déviance » que Diane Vaughan a dégagée à propos de Challenger, ou l’approche systémique de Nancy Leveson.

### Le génie logiciel et la vérification

Du côté de l’informatique, la référence est la tradition des contrats et de la preuve de programmes : Hoare, Dijkstra (pour qui les tests montrent la présence des erreurs, jamais leur absence), Bertrand Meyer et la programmation par contrat. La distinction entre vérification et validation vient de la simulation numérique, où l’on sépare « résoudre correctement les équations » de « résoudre les bonnes équations ».

### L’économie de l’information et les facteurs humains

L’idée que la forme cesse de signaler le fond emprunte à Michael Spence (le signal n’est crédible que s’il coûte) et à George Akerlof (quand on ne distingue plus la qualité, le marché se dégrade). La loi de Goodhart, selon laquelle une mesure devenue cible cesse d’être une bonne mesure, éclaire l’entraînement des modèles sur les préférences humaines. Du côté des facteurs humains, l’« ironie de l’automatisation » de Lisanne Bainbridge est centrale : plus on automatise le courant, plus on confie à l’humain l’exception, pour laquelle il est de moins en moins entraîné.

### La critique de l’intelligence artificielle

Le livre de 2022 appartient à la tradition critique qui va de l’objection de Lady Lovelace (la machine ne fait que ce que nous savons lui ordonner) à Hubert Dreyfus (*What Computers Can’t Do*), et, en France, à des essais comme ceux de Jean-Gabriel Ganascia ou d’Éric Sadin. Il partage avec eux le refus de l’anthropomorphisme et la défense de l’intuition humaine, mais aussi leur point faible : des affirmations d’impossibilité « par nature », auxquelles Turing répondait déjà en 1950.

Le livre de 2026 change de registre. Il ne se prononce plus sur ce que les machines peuvent ou ne peuvent pas faire, mais sur les garanties qu’elles offrent ou n’offrent pas. Il rejoint ainsi la littérature récente sur la fiabilité des grands modèles de langage (compétence irrégulière, hallucinations inévitables, complaisance, dégradation des modèles entraînés sur leurs propres productions) et les approches de sûreté de l’IA qui raisonnent en termes de surveillance et de défense en profondeur plutôt que de confiance.

### Ce qui est propre à l’œuvre

Aucune des pièces n’est inédite, et l’œuvre le reconnaît. Ce qui l’est davantage, c’est un vocabulaire commun, applicable avec un égal profit à une note de calcul, à un rapport d’expertise ou à une chaîne d’agents logiciels : comparateur, cinq conditions, probabilité d’échappement, blanchiment, cadre comme cause commune. Plusieurs formulations sont, à notre connaissance, originales ou d’une netteté rare : « la formalité change la colonne, non la ligne », la distinction entre omission structurelle et omission de saillance, le « prêteur unique » dont tous empruntent le regard, ou l’idée que relire le brouillon d’un modèle sans s’être formé d’abord son propre jugement revient à lire deux fois la même représentation.

Une tradition française aurait enfin offert des interlocuteurs naturels, presque absents des deux livres : l’histoire de la statistique d’Alain Desrosières, la sécurité des systèmes de René Amalberti, et *Agir dans un monde incertain* de Callon, Lascoumes et Barthe, dont le titre fait presque écho au second ouvrage et qui étudie précisément comment des tiers rouvrent les cadres des experts.

## Le diagnostic : risques nouveaux et parades proposées

Appliquée à l’informatique et à l’automatisation, la grille des contrôles produit un diagnostic précis : le danger ne tient pas d’abord à la fréquence des erreurs des machines, mais à la disparition silencieuse de ce qui permettait de les arrêter.

### Le changement de régime au sommet de la pile logicielle

Si l’on peut empiler des milliards d’opérations dans un processeur, un système de fichiers ou une base de données sans vérifier chaque résultat, c’est que chaque couche promet par écrit ce qu’elle fait. Une fonction de tri s’engage à rendre une permutation ordonnée de sa liste ; ce contrat sert de comparateur permanent, permet de tout vérifier une fois pour toutes avant l’usage, et donne une adresse à la panne : telle ligne, tel module.

L’apprentissage automatique a franchi le mur que les règles écrites ne pouvaient pas traverser : personne ne savait spécifier ce qui distingue un chat d’un chien sur une grille de pixels. Mais la garantie préalable n’a pas été perdue par négligence : elle a été dépensée pour acheter cette portée. La spécification a migré dans le choix des données, de la fonction d’objectif et des préférences d’évaluation, où nul ne peut plus la lire. Au sommet de la pile, avec les grands modèles de langage, trois choses basculent ensemble : ce qui est promis (une tendance statistique mesurée en moyenne, non plus un contrat sur chaque appel), la forme de l’échec (un texte fluide et assuré, identique en surface à une réponse juste) et le lieu où aboutit l’enquête (aucune ligne fautive à corriger).

L’affaire Mata contre Avianca, où des avocats déposèrent en 2023 un mémoire citant six décisions inventées par un assistant conversationnel, en est l’illustration : aucune règle n’avait été enfreinte, le programme avait simplement prolongé la demande par une suite de mots plausible. Les consignes et l’ajustement sur des préférences humaines déplacent utilement les fréquences d’erreur, mais « orienter n’est pas spécifier » : cela tient du dressage plutôt que du câblage d’un disjoncteur.

Trois phénomènes aggravent la situation. La compétence de ces modèles dessine une frontière « en dents de scie » : remarquable sur une question difficile, elle peut céder sur une variante anodine sans que rien dans le ton ne le signale. Un modèle peut aussi posséder une information sans la mobiliser : c’est l’*omission de saillance*, distincte de l’omission structurelle d’un facteur absent. Enfin, des travaux récents montrent qu’un modèle bien calibré sur son corpus doit inventer, avec une fréquence minimale, des faits rares et arbitraires. Reposer plusieurs fois la même question débusque les réponses hasardées, qui varient d’un tirage à l’autre, mais non les erreurs constantes, répétées d’une même voix.

### Ce que l’automatisation fait aux contrôles

L’automatisation agit sur trois leviers à la fois.

- **Elle enchaîne les étapes et fait passer les erreurs à l’acte.** Un agent qui extrait, résume, planifie et appelle des outils sur douze étapes est une chaîne à douze maillons, où les hypothèses sont blanchies à chaque passage. Et il ne produit plus des réponses qui attendent un lecteur, mais des actions qui modifient une base, publient un document ou engagent une transaction. On confie ainsi le pouvoir d’agir à la couche qui offre le moins de garanties : c’est l’« inversion des garanties ».
- **Elle érode les contrôles humains implicites.** La lenteur du travail analytique avait une vertu cachée : en posant ses équations à la main, l’analyste se formait une idée de l’ordre de grandeur attendu. Cette boucle, absente des organigrammes, disparaît sans bruit. Disparaît aussi le signe révélateur du doute : un collègue qui s’aventure hors de sa compétence hésite, un modèle s’exprime de la même voix posée qu’il restitue un fait ou invente une référence. Et lorsque la mise en forme devient presque gratuite tandis que la vérification du fond reste coûteuse, la qualité de la forme cesse d’être un signal crédible. Un essai randomisé de 2025 a montré des développeurs expérimentés ralentis d’environ 19 % par leurs outils, alors qu’ils s’estimaient accélérés d’environ 20 %.
- **Elle corrèle les angles morts à l’échelle collective.** Quand toute une profession rédige et relit avec les mêmes modèles, ceux-ci corrigent les étourderies propres à chacun, mais leurs propres angles morts deviennent communs aux producteurs et aux relecteurs. C’est l’image du « prêteur unique » : un comparateur emprunté aide contre les erreurs de l’emprunteur, jamais contre celles du prêteur. Le blanchiment de provenance achève le tableau : vingt journalistes qui reprennent la même dépêche ne sont pas vingt témoins concordants, mais une seule dépêche relue vingt fois. Au même moment, la pression du volume pousse les institutions à comprimer la ressource devenue le véritable goulet d’étranglement : l’évaluation indépendante.

Un calcul élémentaire résume l’enjeu. Un producteur qui se trompe dans 10 % des cas, contrôlé par un relecteur qui ne laisse passer que 1 % de ses erreurs, laisse arriver 0,1 % d’affirmations fausses jusqu’à l’action. Un producteur assisté qui ne se trompe plus que dans 1 % des cas, mais dont 90 % des erreurs passent parce que ses relecteurs consultent le même modèle, en laisse passer 0,9 %, soit neuf fois plus. Le second livre prend soin de présenter ce cas comme une possibilité, non comme une fréquence : le sens réel de l’effet dépend du domaine et reste à mesurer.

Un piège supplémentaire guette la collaboration entre l’humain et la machine. Demander à un modèle de contrôler un travail humain le referme sur lui-même : la consigne lui transmet déjà le cadre de l’utilisateur, et son entraînement à plaire le pousse à la complaisance plutôt qu’à la contradiction. Un humain et un modèle ne forment un véritable contrôle croisé que si la personne se forme d’abord son propre jugement, puis soumet le problème nu, sans laisser deviner la réponse qu’elle attend.

### Décider et se prémunir

Le point de départ des parades est une distinction : ce qui se répète des milliers de fois dans un environnement stable (filtrer des messages, prévoir la pluie) se calibre au fil de l’eau ; ce qui ne se joue qu’une fois (lancer une sonde, opérer un patient, laisser un agent exécuter une commande destructrice) ne bénéficie d’aucune moyenne protectrice. Pour ces décisions, le second livre propose un petit modèle : au risque p estimé dans le cadre s’ajoute un risque z que le cadre ne voit pas, et le risque réel devient :

```latex
p_w = 1 - (1 - p)(1 - z)
```

Puisque z est invisible, il propose de décider d’après p augmenté d’une *marge d’humilité*, qui relève d’un jugement de prudence et non d’une mesure. Quatre issues sont alors possibles : le départ justifié, le piège silencieux, le sauvetage par la marge et la prudence superflue. À la marge s’ajoutent deux dispositifs empruntés à l’ingénierie : le *verrou*, point où l’action attend une autorisation accordée après un contrôle indépendant, et le *bac à sable*, environnement isolé où l’on explore librement parce que l’erreur y coûte peu et se défait. Toute action étant aussi une question posée au monde, mieux vaut la poser là où la réponse est bon marché, sans confondre pour autant le bac à sable avec le monde.

Au destinataire d’un chiffre assuré (décideur, citoyen, responsable), le livre offre quatre questions qui n’exigent aucune technicité :

1. Sous quelles conditions ce chiffre tient-il ?
2. Qu’est-ce qui le ferait changer sensiblement ?
3. Quelle est la manière la plus vraisemblable dont il pourrait être faux ?
4. Qu’a-t-on délibérément choisi de ne pas modéliser ?

Remettre un chiffre sans ses conditions revient, selon une formule du livre, à transférer une responsabilité déguisée en information. Annoncer « il pleuvra demain » est une injonction déguisée ; annoncer « 70 % de risque de pluie » laisse à chacun le soin de peser ses propres enjeux.

### Un remède à trois niveaux

Les contrôles eux-mêmes s’organisent sur trois niveaux, dont aucun ne suffit seul.

- **L’attitude.** Produire ses propres comparateurs avant de consulter l’outil : écrire l’ordre de grandeur attendu avant de lire le résultat, pratiquer le pré-mortem (supposer que le projet a échoué et en imaginer les causes), élargir à dessein l’éventail des mondes possibles. Cette discipline déborde le cadre de l’outil, jamais celui de la personne, et ne tient pas sans appui collectif.
- **Le placement.** Décider où contrôler (là où une sortie cesse d’être un brouillon pour devenir un acte ou une référence), par qui (quelqu’un qui partage l’interface et sait lire le niveau situé dessous : le code sous le programme généré, la physique sous le nombre calculé), sur quoi (la sortie, mais aussi la représentation) et avec quel effort, proportionné aux enjeux. L’ancrage des réponses dans des documents consultables aide, sans dispenser de les ouvrir.
- **L’organisation.** Traiter la capacité d’évaluation indépendante comme une ligne budgétaire à part et ne pas produire plus qu’elle ne peut vérifier ; exiger que toute affirmation soumise à décision affiche son état de vérification ; tenir un historique qui confronte les prévisions aux issues ; mesurer enfin la probabilité d’échappement en glissant périodiquement des erreurs injectées dans le flux, comme la sûreté aéroportuaire projette des images de menaces fictives sur les écrans des opérateurs de contrôle des bagages.

Avant d’agir d’après une affirmation, cinq questions reprennent les cinq conditions : y a-t-il un comparateur, peut-il se tromper autrement, est-il comparable, arrivera-t-il à temps, et quelqu’un prendra-t-il son alerte en compte ? Ce diagnostic ne conduit ni au scepticisme paralysant ni au rejet nostalgique de l’automatisation : là où l’on ne peut plus acheter une garantie une fois pour toutes sur l’outil, il faut organiser lucidement ses décisions et ses contrôles.

## Où ces idées peuvent servir

La grille vaut partout où l’on agit d’après un résultat que l’on n’a pas produit soi-même, ou que l’on a produit trop vite pour l’avoir véritablement contrôlé. Plusieurs terrains s’y prêtent particulièrement.

- **Ingénierie et simulation numérique.** Les chaînes de calcul multiphysiques, où un champ de températures calculé sous dix hypothèses prudentes devient à l’étape suivante un simple tableau de nombres nus, sont le terrain naturel du blanchiment. Exiger que chaque résultat voyage avec ses conditions, ses unités et ses barres d’erreur, et rappeler que la barre d’erreur ne couvre que les alternatives admises, sont des règles directement applicables.
- **Sûreté, qualité et audit.** Les cinq conditions forment une liste de contrôle efficace pour juger une procédure de revue. Une question en résume l’esprit : quelle erreur cette étape peut-elle arrêter, que le producteur n’aurait pas pu arrêter lui-même ? La mesure de l’échappement par erreurs injectées, déjà pratiquée en sûreté aéroportuaire et en test logiciel, se transpose à la relecture de rapports, de code ou de synthèses.
- **Déploiement de l’IA dans les organisations.** C’est le terrain le plus immédiat : réserver l’exploration aux bacs à sable et placer des verrous là où un agent toucherait le monde réel ; confier la relecture à des personnes qui savent lire le niveau sous-jacent ; afficher l’état de vérification de chaque production ; plafonner le volume produit à la capacité de contrôle. Le livre réhabilite aussi un geste simple : se faire une idée avant d’interroger le modèle, et lui soumettre le problème nu plutôt que la réponse espérée.
- **Recherche scientifique et édition.** Quand auteurs, relecteurs et éditeurs s’appuient sur les mêmes outils, l’évaluation par les pairs risque de devenir une copie plutôt qu’un contrôle. La traçabilité de la provenance, la distinction entre résultat exploratoire et résultat établi, et la déclaration de l’usage d’outils génératifs y trouvent une justification de fond. Le second livre s’y soumet d’ailleurs lui-même, en déclarant avoir été élaboré en dialogue avec de grands modèles de langage et en analysant ce que cela implique.
- **Décision publique et culture du chiffre.** Les quatre questions face à un chiffre assuré conviennent aussi bien à un élu devant une étude d’impact qu’à un dirigeant devant un tableau de bord ou à un patient devant un pronostic. Elles supposent seulement d’accepter « nous ne savons pas » comme une réponse recevable.
- **Gouvernance et régulation.** L’idée que la corrélation des angles morts peut croître alors même que chaque outil s’améliore intéresse directement les régulateurs : une profession entière qui s’appuie sur deux ou trois modèles de fondation présente un risque de mode commun que les évaluations outil par outil ne voient pas.
- **Formation.** Le premier livre garde ici toute sa valeur : il initie un lecteur non spécialiste aux probabilités conditionnelles, à l’inférence et à la décision rationnelle, avec des images efficaces. Le second plaide pour former des analystes capables de lire le niveau situé sous les outils, et pour préserver, contre l’ironie de l’automatisation, les compétences que l’exception exigera.

Dans tous ces cas, l’apport principal est un déplacement du regard : de la performance moyenne de l’outil vers l’architecture des contrôles qui l’entourent. La question n’est plus seulement « cet outil se trompe-t-il souvent ? », mais « quand il se trompe, qu’est-ce qui nous en avertira, et à temps ? »

## Limites et tensions

Les deux livres n’appellent pas le même jugement, et il serait injuste de lire le premier à l’aune du second. Le livre de 2026 a d’ailleurs le mérite rare de dresser lui-même l’inventaire de ses faiblesses : statut de chaque énoncé, tensions laissées ouvertes, observations qui affaibliraient l’argument. Les réserves qui suivent prolongent souvent cet inventaire plus qu’elles ne le contredisent.

### Le premier livre : une thèse qui oscille

La thèse centrale de 2022, le caractère subjectif de la rationalité, hésite entre deux lectures. Au sens modeste (nul ne connaît d’avance l’issue d’une décision, et deux agents aux croyances différentes peuvent choisir différemment sans faute de raisonnement), elle est juste, mais c’est le point de départ de la théorie bayésienne de la décision plutôt qu’une découverte. Poussée jusqu’à affirmer qu’aucune anticipation n’est « plus juste » qu’une autre, elle devient excessive : les règles de score et la calibration permettent précisément de comparer des prévisionnistes, et le livre se contredit lorsqu’il ajoute que celui qui comprend mieux le réel obtiendra généralement de meilleurs résultats. Le second ouvrage corrige ce glissement en distinguant explicitement le subjectif de l’arbitraire.

L’argumentaire contre l’« intelligence » des machines est le point le plus daté. Il passe du niveau matériel (une machine manipule des électrons et applique des instructions) au niveau des capacités, ce qui ne va pas de soi : décrire l’électrochimie des neurones ne dit rien de l’intelligence d’une personne. Les affirmations d’impossibilité « par nature » (pas d’intuition, pas d’initiative, pas d’exploration spontanée) étaient déjà fragilisées en 2022 par des programmes de jeu devenus surhumains par auto-apprentissage, et l’ont été davantage par les modèles généralistes et les agents apparus depuis. La prédiction finale, selon laquelle ceux qui attendent beaucoup de l’IA « finiront par se retrouver déçus », est formulée de telle sorte qu’elle ne peut guère être réfutée.

Plusieurs repères manquent enfin : Herbert Simon, dont l’expression « rationalité procédurale » est reprise dans un autre sens ; la psychologie de la décision de Kahneman et Tversky ; la causalité, c’est-à-dire la différence entre observer et intervenir, pourtant essentielle à un livre sur l’action ; la discussion de Knight, cité sans être examiné. Le texte souffre aussi de redites et d’un défaut de relecture. Sa deuxième partie n’en reste pas moins une initiation accessible et cohérente au raisonnement probabiliste et décisionnel.

### Le second livre : des distinctions plus que des théorèmes

L’appareil formel du livre de 2026 est exact : les calculs, refaits par un relecteur, se vérifient à une imprécision près. Mais les propositions présentées comme des « résultats sous hypothèses » reformulent pour l’essentiel leurs hypothèses : une moyenne calculée sur un ensemble d’alternatives ne contient rien de ce qui n’y figure pas, un événement soumis à cinq conditions nécessaires est impossible si l’une manque. Ce sont des vérités solides, mais élémentaires. La force de l’argument tient aux distinctions qu’il organise et aux « ponts » qui relient ces schémas aux situations réelles : la tendance du coût d’un contrôle à croître avec son indépendance, la hausse de la corrélation sous modèle partagé, l’érosion des contrôles humains. Or tous ces ponts ont, le livre le reconnaît, le statut d’hypothèses de travail.

La base empirique est étroite et datée : une poignée de cas emblématiques et quelques études souvent uniques, comme l’essai de 2025 portant sur seize développeurs, dont la taille n’est pas rappelée. D’autres essais contrôlés ont mesuré au contraire des gains nets sur des tâches de programmation bien délimitées, et une méta-analyse récente trouve la collaboration entre humains et machines plus fructueuse pour la création de contenus que pour la décision. Le diagnostic gagnerait à préciser ses conditions de validité plutôt qu’à généraliser.

### Une frontière plus poreuse qu’il n’y paraît

Toute la construction repose sur une coupure nette entre ce qui est dans le cadre et ce qui lui échappe. En pratique, la frontière est plus poreuse. La critique statistique des modèles, de Box aux contrôles prédictifs a posteriori, sait déceler l’inadéquation d’un modèle sans avoir spécifié son concurrent : des résidus ordonnés selon le temps, le lot ou l’opérateur révèlent souvent une structure qui met sur la piste du facteur manquant. En simulation numérique, les termes de « discordance de modèle » prennent en charge une part de l’incertitude structurelle à l’intérieur même de la pratique quantitative.

Pour les modèles de langage, l’omission de saillance que le livre a lui-même mise au jour brouille sa propre règle : reformuler, décomposer un raisonnement, faire débattre deux instances ou consacrer davantage de calcul à la vérification peut réveiller une connaissance latente sans apport extérieur. Le livre l’admet, mais sans dire comment situer un contrôle donné entre la copie et le regard extérieur.

Le contraste entre informatique classique et modèles appris est, de même, plus net que la réalité. Les couches basses reposent elles aussi sur des arrière-plans tacites : les failles d’exécution spéculative des processeurs ont montré un contrat fonctionnel respecté pendant que le comportement physique trahissait des secrets. À l’inverse, l’interprétabilité et l’édition ciblée des modèles commencent à dessiner des « adresses » partielles. La différence est de degré et de lisibilité plutôt que de nature : la thèse n’en est pas ruinée, mais sa formulation en sort tempérée.

### La marge d’humilité et le coût de la prudence

La marge d’humilité est le maillon le plus fragile des parades. Faute de règle pour la fixer, elle risque d’être choisie après coup pour justifier la décision souhaitée. Et aux enjeux extrêmes (aviation, nucléaire, chirurgie), où le seuil de décision est minuscule, toute marge additive plausible conduit mécaniquement à l’abstention universelle.

Or ces activités ne se gouvernent pas en ajoutant une prime d’ignorance à une estimation. Elles réduisent le facteur omis lui-même, par la défense en profondeur, la qualification des matériaux et le retour d’expérience, et elles pèsent le coût de l’inaction, que le modèle ne représente pas. Entre le calcul bayésien ponctuel et le jugement nu, un demi-siècle de travaux sur la décision sous ambiguïté et sur la robustesse offre des voies intermédiaires disciplinées, que l’œuvre laisse de côté.

### L’énigme du producteur plus fiable

L’exemple du chapitre d’ouverture, où un outil dix fois plus fiable compose un système neuf fois plus risqué, frappe les esprits. Mais avec les paramètres illustratifs que le livre retient plus loin, son propre modèle montre l’inverse : le passage à un modèle partagé y fait baisser le risque résiduel. Le livre le reconnaît honnêtement et parle d’une possibilité, non d’une fréquence. La leçon la plus robuste est sans doute ailleurs : un modèle partagé peut faire baisser l’erreur moyenne tout en concentrant le risque résiduel sur des défaillances rares, silencieuses et simultanées. Formulé en termes de risque extrême plutôt que de moyenne, l’avertissement serait plus solide.

### L’économie politique des contrôles

Les remèdes organisationnels (plafonner la production à la capacité de contrôle, sanctuariser l’évaluation, injecter des erreurs) sont de bonnes règles d’hygiène. Ils supposent pourtant résolu le problème d’action collective qu’ils affrontent : pourquoi une entreprise en concurrence sur les délais rationnerait-elle de son plein gré son débit ? Le droit de la responsabilité, l’assurance du risque algorithmique corrélé et les normes de sûreté fonctionnelle, qui imposent déjà l’indépendance des vérificateurs dans l’aéronautique ou l’automobile, sont les leviers qui pourraient imposer ces verrous de l’extérieur ; ils restent peu étudiés. S’y ajoute un risque bien connu en sûreté : que les procédures de vérification se muent en rituels cochés machinalement, ou qu’elles poussent les opérateurs pressés à les contourner.

### La méthode appliquée à elle-même

Le second livre déclare avoir été élaboré en dialogue avec de grands modèles de langage et en tire lui-même la leçon : ces modèles sont des comparateurs empruntés, utiles contre les erreurs de l’auteur, non contre leurs propres angles morts. Les absences relevées plus haut ont d’ailleurs un air de famille : des pans entiers de disciplines voisines (sociologie des accidents, théorie de l’ambiguïté, critique des modèles, tradition francophone), comme si la synthèse s’était construite autour d’un noyau d’auteurs canoniques. Le recours répété à un article antérieur non évalué par des pairs illustre, à rebours, le risque de corroboration circulaire que l’ouvrage décrit si bien.

La prose, enfin, est très soignée mais redondante : exemples racontés trois ou quatre fois, rappels et résumés qui se répètent. Le livre fournit lui-même la règle de lecture qui convient : lorsque la mise en forme devient presque gratuite, la tenue du texte ne prouve rien sur son fond.

## En marge : la fabrique des deux livres

Les deux ouvrages ne diffèrent pas seulement par leur contenu : ils ont été fabriqués de deux manières presque opposées, ce qui offre une rare expérience naturelle. Le premier a été écrit seul, sans modèle de langage. Le second a été bâti en trois jours par des agents de deux fournisseurs, à partir d’idées déjà mûres et sous la direction de l’auteur. Un journal d’heures tenu à la main pour 2022 et le relevé des sessions d’agents pour 2026 permettent de chiffrer l’écart.

|  | Livre de 2022 | Livre de 2026 |
| --- | --- | --- |
| Mode de production | Écrit seul, sans modèle de langage | Rédigé par des agents de deux fournisseurs, sous supervision |
| Durée calendaire | Environ 10 mois (oct. 2020 – juil. 2021), 145 jours de travail | 3 jours (18–21 nov. 2026), 73 h écoulées |
| Heures de travail | ≈ 723 h de travail propre, déclarées (borne basse) | ≈ 29 h d’activité d’agents journalisée ; supervision estimée à 30–40 h, environ 132 consignes |
| Texte final | Environ 65 000 à 75 000 mots | Environ 102 000 mots, 277 pages |
| Rythme d’écriture | Environ 100 mots par heure | Environ 2 500 à 3 500 mots par heure supervisée |
| Volume engendré | Le texte lui-même | ≈ 6,3 millions de jetons produits (35 à 40 fois le texte final) et 350 000 mots de notes de travail |
| Coût en calcul | Aucun | ≈ 260 $ au tarif public des API (260 à 360 $ avec une session non journalisée) |
| Relecture | 84 h de correction, plus 43 h pour le manifeste | Passes automatisées ; relecture humaine complète encore à faire |

### Ce que les chiffres mesurent, et ce qu’ils taisent

L’écart est spectaculaire : environ vingt fois moins d’heures humaines et une centaine de fois moins de temps calendaire, pour un texte plus long. Un premier jet complet des vingt et un fichiers de chapitres a été obtenu en un peu plus de sept heures. Le coût en calcul, évalué au tarif public des API, reste de l’ordre de quelques centaines de dollars, soit moins d’un dollar par page ; sans la mise en cache des contextes, la même quantité de calcul aurait coûté environ 1 960 $. En pratique, le travail s’est fait sur abonnement, et la contrainte ressentie a été le quota plutôt que l’argent : consultations répétées de la consommation, efforts abaissés en cours de route, et même un passage d’un fournisseur à l’autre au milieu d’une relecture.

La comparaison ne porte pourtant pas sur la même chose. Elle mesure la mise en livre d’idées arrêtées, non leur production. Le livre de 2026 repose sur un article préalable, deux essais, une conférence et une carte interactive des idées, issus d’environ une année de recherche elle-même assistée par des modèles (une centaine d’heures recensées). Il repose surtout sur le livre de 2022, où se trouvent déjà l’essentiel de sa première partie et le noyau de la deuxième. Compté honnêtement, l’ouvrage de 2026 s’appuie donc sur au moins les mêmes 723 heures, augmentées de ce travail de recherche, puis du chantier de trois jours.

Deux autres réserves s’imposent. La relecture humaine complète, délibérément réservée pour la fin, reste à faire : estimée entre 40 et 120 heures, elle porterait le coût humain du livre à 70 à 160 heures, soit encore 4,5 à 10 fois moins qu’en 2022. Et les relevés eux-mêmes sont incomplets : une session de relecture menée dans un environnement distant n’a laissé aucune trace locale, les heures de 2022 s’arrêtent sept mois avant le dépôt légal, et une partie des compteurs de 2026 a dû être décodée à la main.

### Un chantier qui applique sa propre thèse

Le plus frappant n’est pas la vitesse, mais l’organisation. Le chantier a été conçu comme une architecture de contrôles, au sens même du livre qu’il produisait.

- **Des spécifications verrouillées d’abord.** Un ensemble de documents fixait la hiérarchie des sources, la terminologie (chaque terme rattaché à un chapitre), le statut de chaque proposition et des nombres engendrés par programme, sous le contrôle d’un vérificateur automatique. C’est ce qui a permis à une dizaine d’agents de rédiger en parallèle sans que le livre se disperse.
- **Un fournisseur produit, l’autre relit.** Les modèles de l’un rédigeaient, ceux de l’autre relisaient ; plus tard, l’un proposait des corrections de style et l’autre les jugeait. La diversité des fournisseurs servait de comparateur qui se trompe autrement, et non de simple capacité supplémentaire.
- **Des lecteurs neufs et isolés.** Relectures à froid, lecteurs thématiques et lecteur du seul PDF recevaient chacun un contexte vierge, sans communication entre eux, pour que leurs angles morts ne se corrèlent pas. Une première vague de onze lecteurs a relevé 328 constats en seize minutes.
- **Étalonner le juge avant de s’y fier.** Un premier essai de reprise stylistique libre avait réécrit 82 % des phrases d’un chapitre et changé le sens une vingtaine de fois. Le juge automatique a donc été testé avant usage : il a rejeté les 30 dérives de sens connues qu’on lui a soumises et accepté 7 des 8 corrections fidèles.
- **Les modèles proposent, des scripts appliquent.** Après l’échec de l’essai libre, chaque correction passait par un lot écrit, une application déterministe, le vérificateur et un enregistrement par chapitre.

L’auteur, de son côté, n’a presque rien écrit de la prose. Son temps est passé dans la décision : fixer la direction et les règles de provenance, trancher entre des options, arbitrer les désaccords, choisir ce qu’il ne fallait pas automatiser (les corrections d’anglicismes, les erreurs injectées, la relecture finale) et surveiller les quotas.

### Ce que la comparaison enseigne

Le chantier confirme d’abord le diagnostic du livre sur le déplacement du goulet d’étranglement. Produire est devenu presque gratuit : les modèles ont engendré trente-cinq à quarante fois la longueur du texte final, et les notes de travail représentent plus de trois fois le livre. Ce qui reste rare et lent, c’est l’évaluation : les vagues de relecture, l’arbitrage des constats et surtout la relecture humaine, que le relevé désigne lui-même comme le comparateur qu’aucun agent n’a remplacé.

Il illustre ensuite la perte du signal coûteux. Le texte de 2026 est d’une grande correction et d’une terminologie très cohérente, mais sa prose est plus uniforme que celle de 2022, il se répète à la lecture suivie, et l’audit des anglicismes attend encore la relecture humaine. La netteté de la forme n’y garantit pas plus qu’ailleurs la solidité du fond.

Il pose enfin une question de méthode qui dépasse ce cas. Si un livre de près de trois cents pages peut être bâti en trois jours à partir d’idées mûres, la valeur ne réside plus dans la rédaction, mais dans deux choses que la machine ne fournit pas seule : la maturation des idées, qui a pris ici des années, et la vérification indépendante, qui reste à achever. Le contraste entre les deux livres en donne une mesure grossière mais parlante : plus de 700 heures pour penser et écrire seul en 2022, une trentaine d’heures pour faire écrire en 2026, et une relecture humaine qui pourrait bien devenir, à elle seule, la part la plus longue du travail.

## Bilan

Au terme du parcours, l’unité de l’œuvre apparaît nettement. Ce qui s’énonçait en 2022 comme un appel moral à l’humilité du jugement humain devant la mécanique des algorithmes devient, en 2026, une question d’architecture : comment disposer nos instruments, nos interfaces et nos institutions pour que nos représentations restent exposées à la contradiction du réel ?

Son apport le plus durable est sans doute ce déplacement de la question. Devant les modèles appris, on demande d’ordinaire s’ils se trompent souvent ; l’œuvre demande ce qui nous avertira quand ils se tromperont. Elle se garde à la fois de l’enchantement et de la panique. Le péril qu’elle décrit n’est ni une volonté étrangère qui nous dépasserait, ni une impuissance des méthodes statistiques, mais un déplacement silencieux de nos garanties : nous insérons au cœur de nos chaînes d’action des composants sans contrat écrit, dont l’aisance endort les signaux habituels du doute, et nous alignons sans le voir les angles morts de ceux qui produisent et de ceux qui vérifient.

Sa principale faiblesse est le revers de cette force : c’est une synthèse conceptuelle encore en attente d’étalonnage. Ses modèles sont des épures, ses paramètres sont illustratifs, et l’efficacité de ses remèdes n’a été mesurée nulle part. Le programme de recherche qu’elle ouvre est pourtant clair. Une partie en est formulée par l’œuvre elle-même : mesurer l’échappement des erreurs par injection dans des relectures mixtes, humaines et automatiques ; estimer la part des causes partagées lorsqu’une profession adopte les mêmes modèles ; éprouver l’effet réel des parades proposées. Une autre partie est suggérée par ses lecteurs : relier la marge d’humilité aux théories de la décision sous ambiguïté, intégrer la critique statistique des modèles, et penser les conditions juridiques, assurantielles et normatives qui rendraient les verrous effectifs.

Les deux livres demandent à être lus comme ils se lisent eux-mêmes : comme une démarche de travail, retenue faute de mieux et exposée à la contradiction. Le second a le mérite, rare dans les essais consacrés à l’intelligence artificielle, de nommer ses points faibles et les observations qui le démentiraient. Son meilleur comparateur, comme il le dit lui-même, n’est ni son auteur ni les outils qui l’ont aidé, mais la pratique du lecteur : c’est à celle-ci d’apporter le contre-exemple qui se trompe autrement.

### Sources consultées

- *Un discours de la méthode au XXIe siècle. Risques et limites de l’« intelligence artificielle »*, 2022 (fichier `ManuscritPDFpub.pdf`).
- *Agir d’après une représentation du monde. Cadre, contrôles et décision, de l’informatique classique à l’IA*, version de travail, novembre 2026 (fichier `livre-ecran.pdf`).
- Revue de littérature interdisciplinaire en neuf volets et trois notes d’approfondissement (dossier `literature_review`).
- Recensions des deux livres, rapport sur la revue de littérature et lectures croisées (dossiers `report_claude` et `report_gemini`).
- Relevé du processus de construction du livre de 2026 et journal d’heures du livre de 2022, compilés à partir de l’historique git et des journaux de sessions d’agents (fichier `monograph-build-lookback.html`).
