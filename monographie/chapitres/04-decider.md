# Décider d’après ce que l’on croit {#sec:ch04}

Les chapitres précédents ont séparé ce que nous construisons pour comprendre le réel de la réponse que celui-ci oppose à nos actes. Au @sec:ch01, nous avons rappelé le calcul des probabilités conditionnelles et la révision bayésienne ; au @sec:ch02, nous avons établi que chacun agit d’après une représentation (@def:representation) bâtie dans un cadre fini (@def:cadre), alors que le monde répond à l’action ; au @sec:ch03, nous avons montré qu’une probabilité répartit un poids sur des mondes possibles et que la calibration suppose la répétition. Les lecteurs qui suivent l’un des parcours sélectifs de la @sec:ch00-parcours pourront se reporter aux développements correspondants au besoin. Nous examinons maintenant le passage du jugement à la décision : comment l’utilité espérée subjective relie la croyance au rapport des enjeux par un seuil critique, pourquoi deux décideurs rationnels peuvent trancher à l’opposé, comment ce seuil s’effondre lorsque les pertes deviennent extrêmes, ce qui distingue une décision unique d’une série d’essais, et quelle question reste ouverte jusqu’au @sec:ch17.

## L’utilité espérée subjective de Savage {#sec:ch04-ues}

Une fois posés des poids sur des mondes possibles, comment transformer cette évaluation en choix concret avant que l’événement ne se produise ? Une règle fondée sur les fréquences observées exige des séries déjà recueillies, alors qu’une décision est toujours prise *avant* que le monde ne réponde, et souvent dans des situations qui ne se répéteront pas. Au moment de trancher, le décideur ne dispose ni de l’issue future ni d’une fréquence sur cette épreuve singulière : il doit composer ce qu’il juge plausible avec ce qu’il risque de gagner ou de perdre.

La théorie classique de la décision apporte une réponse précise à cette question sous le nom d’**utilité espérée subjective (UES)** : il s’agit de la règle de décision formulée par Leonard Savage [-@savage1954], qui consiste à choisir l’acte dont l’utilité espérée est la plus élevée, calculée avec ses propres probabilités.

Quatre éléments suffisent à dresser la scène d’une décision dans ce cadre :

- *les actes*, c’est-à-dire les options effectivement ouvertes à l’instant présent (appareiller sur un voilier allégé ou sur un voilier renforcé, engager une mise en production ou la suspendre) ;
- *les états du monde*, c’est-à-dire les configurations de l’événement qui échappent au décideur une fois son choix arrêté (le mât résiste ou se brise, la chambre sous le percuteur est vide ou chargée) — ces états correspondent directement aux mondes possibles envisagés à la @sec:ch03-mondes-possibles ;
- *les conséquences*, qui résultent de la rencontre entre l’acte retenu et l’état réel du monde (victoire, démâtage et remorquage coûteux, traversée sans histoire mais plus lente) ;
- *les probabilités personnelles et les utilités*, c’est-à-dire le poids que le décideur accorde à chacun des états envisagés d’après sa représentation (@def:representation), et la valeur — l’*utilité* — qu’il attache à chaque conséquence.

Deux précisions évitent d’emblée les contresens habituels. D’une part, le mot *utilité* ne se réduit pas à une somme d’argent comptée linéairement : perdre dix mille euros lorsque cette somme ruine une entreprise ou compromet une traversée pèse bien plus lourd en utilité que gagner la même somme comme un simple bonus, et perdre la vie ou la santé n’a pas d’équivalent monétaire immédiat. L’utilité traduit précisément cette appréciation de la gravité des conséquences par celui qui s’y expose. D’autre part, *subjectif* conserve exactement le sens rigoureux établi à la @sec:ch03-raisonner-envers : il ne signifie ni capricieux ni arbitraire, mais relatif aux informations, aux préférences et au cadre du décideur. Savage [-@savage1954] a démontré que dès lors que les préférences d’un décideur devant l’incertain respectent des axiomes élémentaires de cohérence interne, ce décideur se comporte *comme s’il* attribuait une probabilité personnelle cohérente aux états du monde, une utilité aux conséquences, et retenait l’acte de plus grande utilité espérée. La cohérence lie ainsi ce que l’on croit à ce que l’on fait ; elle ne dispense jamais de s’interroger sur ce qui fonde cette croyance.

::: {.outils titre="L’utilité espérée subjective : actes, états et conséquences"}
Soit un ensemble d’actes envisageables $\mathcal{A}$ et un ensemble d’états du monde retenus $\Omega$, jouant le rôle de l’univers des issues élémentaires introduit à la @sec:ch01-probabilite. Choisir l’acte $a \in \mathcal{A}$ lorsque l’état $\omega \in \Omega$ se réalise produit la conséquence $c(a, \omega)$, à laquelle le décideur attache l’utilité $U\bigl(c(a, \omega)\bigr)$.

Si le décideur répartit ses poids de plausibilité sur $\Omega$ selon une loi de probabilité personnelle $\Pr(\cdot)$ (avec $\sum_{\omega \in \Omega} \Pr(\omega) = 1$ dans le cas fini, ou une intégrale dans le cas continu), l’utilité espérée subjective de l’acte $a$ vaut :

$$\mathrm{UE}(a) = \sum_{\omega \in \Omega} \Pr(\omega)\,U\bigl(c(a, \omega)\bigr).$$

La règle de Savage prescrit de choisir un acte $a^\star \in \arg\max_{a \in \mathcal{A}} \mathrm{UE}(a)$ [@savage1954]. Notons deux propriétés essentielles pour la suite. Premièrement, toute transformation affine croissante $\tilde{U}(c) = \alpha\,U(c) + \beta$ ($\alpha > 0$) laisse inchangé l’ordre des actes : seule importe la comparaison relative des écarts d’utilité. Deuxièmement, la somme ne porte jamais que sur les états $\omega$ figurant dans $\Omega$, pondérés par les probabilités $\Pr(\omega)$ que le décideur leur accorde à l’intérieur de son cadre.
:::

Cette règle donne une forme mathématique limpide à l’articulation entre croyance et enjeu : elle permet de calculer exactement jusqu’à quel niveau de risque perçu une option risquée reste préférable à une alternative sûre.

## La course à la voile {#sec:ch04-course-voile}

Revenons sur le ponton où nous avions laissé M. X et M. Y à la @sec:ch03-prevision-previsionniste. Avant le départ de la course au large, chaque navigateur doit choisir entre deux embarcations : un *voilier léger*, très rapide mais sollicité près de ses limites mécaniques, et un *voilier renforcé*, plus lent mais quasi incassable. Prendre la mer sur le voilier léger donne une chance appréciable de devancer la flotte ; mais si le gréement cède au large, il faudra demander un remorquage qui coûtera bien plus cher que le prix promis au vainqueur.

Traitons le voilier renforcé comme une référence sûre, procurant l’utilité de base $U_{\text{sûr}}$. Face à lui, le voilier léger expose à deux issues : s’il tient jusqu’à l’arrivée (*succès*), le navigateur obtient une utilité $U_{\text{succès}} > U_{\text{sûr}}$ ; s’il casse (*échec*), il subit une utilité $U_{\text{échec}} < U_{\text{sûr}}$. Notons alors deux grandeurs positives mesurées à partir de cette référence : le *gain en cas de succès* $\Delta U = U_{\text{succès}} - U_{\text{sûr}}$ et la *perte en cas d’échec* $L = U_{\text{sûr}} - U_{\text{échec}}$. On appelle **rapport des enjeux** le quotient $L / \Delta U$ de la perte en cas d’échec au gain en cas de succès, tous deux mesurés par rapport à l’option sûre.

Désignons par $p$ la probabilité d’échec estimée par le décideur pour le voilier léger (et donc $1 - p$ la probabilité qu’il attribue à une traversée intacte). Selon la règle de l’UES, partir sur le voilier léger procure une utilité espérée égale à $(1 - p)\,U_{\text{succès}} + p\,U_{\text{échec}}$, qui ne dépasse la référence sûre $U_{\text{sûr}}$ que si le gain espéré $(1 - p)\,\Delta U$ l’emporte sur la perte espérée $p\,L$. L’option risquée cesse donc d’être préférable dès que $p$ atteint le **seuil $p^\ast$**, défini par :

$$p^\ast = \frac{\Delta U}{\Delta U + L} = \frac{1}{1 + L/\Delta U}$$ {#eq:ch04-seuil}

Autrement dit, il est rationnel, au sens de Savage, de prendre le voilier léger si et seulement si $p < p^\ast$, et de se replier sur le bateau renforcé dès que $p \ge p^\ast$.

Cette formule admet une lecture très parlante sous la forme des cotes rappelée à la @sec:ch01-bayes : l’inégalité $(1 - p)\,\Delta U > p\,L$ s’écrit aussi $(1 - p)/p > L/\Delta U$. Pour que l’option risquée paie en espérance, il faut que la cote du succès contre l’échec soit supérieure au rapport des enjeux : si la casse coûte vingt-cinq fois ce que rapporte la victoire, le navigateur doit juger la traversée réussie plus de vingt-cinq fois plus plausible que la casse. Lorsque la perte équivaut au gain ($L/\Delta U = 1$), le seuil vaut $1/2$, soit 50 % : on accepte le risque tant que le succès paraît plus plausible que l’échec. Dès que la perte pèse beaucoup plus lourd que le gain ($L \gg \Delta U$), le seuil tombe bien au-dessous de 50 % et exige une confiance d’autant plus ferme que l’asymétrie des conséquences est prononcée. La seconde écriture de l’@eq:ch04-seuil montre en outre que ni les valeurs absolues du prix ou du remorquage prises isolément, ni l’échelle choisie pour mesurer l’utilité n’interviennent : seul compte le rapport sans dimension $L/\Delta U$.

::: {.formel titre="Dérivation du seuil de décision"}
Posons les hypothèses explicites du modèle de base :

1. *Issue binaire de l’option risquée* : le voilier léger réussit la traversée avec la probabilité personnelle $1 - p$ (utilité $U_{\text{succès}}$) ou subit une rupture avec la probabilité $p \in [0, 1]$ (utilité $U_{\text{échec}}$).
2. *Référence sûre* : le voilier renforcé procure une utilité certaine $U_{\text{sûr}}$ (ou, de façon équivalente, son éventuel risque résiduel infime est déjà absorbé dans sa propre utilité espérée de référence $U_{\text{sûr}}$).
3. *Enjeux non triviaux* : $U_{\text{échec}} < U_{\text{sûr}} < U_{\text{succès}}$, de sorte que $\Delta U = U_{\text{succès}} - U_{\text{sûr}} > 0$ et $L = U_{\text{sûr}} - U_{\text{échec}} > 0$.
4. *Règle interne* : le choix repose uniquement sur la probabilité $p$ formée dans la représentation du décideur, sans facteur omis.

D’après la règle d’UES, l’option risquée est strictement préférée à l’option sûre si et seulement si :

$$(1 - p)\,U_{\text{succès}} + p\,U_{\text{échec}} > U_{\text{sûr}}.$$

En écrivant $U_{\text{sûr}} = (1 - p)\,U_{\text{sûr}} + p\,U_{\text{sûr}}$ et en retranchant ce terme des deux membres, on fait apparaître directement $\Delta U$ et $L$ :

$$(1 - p)(U_{\text{succès}} - U_{\text{sûr}}) - p(U_{\text{sûr}} - U_{\text{échec}}) > 0,$$

soit $(1 - p)\,\Delta U - p\,L > 0$, ou encore $\Delta U > p\,(\Delta U + L)$. Comme $\Delta U + L > 0$, on divise sans changer le sens de l’inégalité pour obtenir :

$$p < \frac{\Delta U}{\Delta U + L} = \frac{1}{1 + L/\Delta U} = p^\ast,$$

ce qui établit l’@eq:ch04-seuil. On voit aussitôt deux propriétés limites : si $L/\Delta U \to 0$ (perte négligeable devant le gain), $p^\ast \to 1$ ; si $L/\Delta U \to +\infty$ (perte écrasante devant le gain), $p^\ast \to 0$. Par ailleurs, multiplier $U$ par $\alpha > 0$ et lui ajouter une constante $\beta$ multiplie $\Delta U$ et $L$ par $\alpha$, laissant $L/\Delta U$ et $p^\ast$ rigoureusement invariants.
:::

Munis de l’@eq:ch04-seuil, revenons sur le quai auprès de M. X et de M. Y. Tous deux préparent la même traversée, lisent le même bulletin météorologique, examinent le même voilier léger et affrontent exactement le même rapport des enjeux : supposons pour fixer les idées que la perte liée au démâtage et au remorquage pèse vingt-cinq fois le gain de la victoire, soit $L/\Delta U = 25$. Le seuil critique vaut alors $p^\ast = 1 / (1 + 25) = 1/26 \approx 3{,}85\,\%$.

Or nous avons vu à la @sec:ch03-prevision-previsionniste que devant les mêmes faits publics, deux prévisionnistes également cohérents peuvent pondérer différemment l’arrière-plan tu $(\dots)$ : M. X évalue le risque de casse à $p = 5\,\%$, tandis que M. Y l’évalue à $p = 0{,}1\,\%$. Sur le quai, aucune règle de probabilité ne permettait de déclarer l’un juste et l’autre faux. L’@eq:ch04-seuil livre pourtant deux décisions opposées :

- M. Y compare $0{,}1\,\%$ à $3{,}85\,\%$ : il reste largement au-dessous du seuil et prend rationnellement le départ sur le voilier léger ;
- M. X compare $5\,\%$ à $3{,}85\,\%$ : il dépasse le seuil et choisit tout aussi rationnellement le voilier renforcé.

Ainsi, deux décideurs qui poursuivent le même objectif, partagent les mêmes enjeux et appliquent la même règle de rationalité peuvent aboutir à des actes contraires dès lors que leurs estimations $p$ encadrent le seuil $p^\ast$. Le désaccord dans l’action ne trahit ici ni erreur d’arithmétique ni divergence d’intérêts : il résulte mécaniquement du fait que les deux représentations placent le curseur de part et d’autre du même point de bascule. Réciproquement, toute modification de l’un des deux termes fait pivoter le choix. Si un élément nouveau révise à la hausse l’estimation de M. Y par la règle de Bayes (@eq:ch01-bayes-cotes) au-delà de $3{,}85\,\%$, son choix bascule aussitôt vers le bateau renforcé ; si, à estimation constante ($p = 5\,\%$), une baisse des frais de remorquage ou une hausse du prix ramenait $L/\Delta U$ au-dessous de $19$ (portant le seuil au-delà de $5\,\%$), c’est M. X qui changerait de quai. La théorie de la décision ne tranche pas à la place de la représentation ni à la place des valeurs : elle traduit fidèlement en acte leur confrontation.

## La roulette russe et l’effondrement du seuil {#sec:ch04-roulette-russe}

Que devient ce mécanisme lorsque l’asymétrie des enjeux s’accentue de plusieurs ordres de grandeur ? Dès que $L/\Delta U$ est grand devant $1$, l’@eq:ch04-seuil montre que le seuil $p^\ast$ se comporte comme l’inverse du rapport des enjeux : $p^\ast \approx \Delta U / L$. Multiplier la gravité relative de l’échec par dix divise par dix la probabilité d’échec tolérable ; quand $L/\Delta U$ tend vers l’infini, $p^\ast$ tend vers zéro.

L’image limite de la *roulette russe* rend cette géométrie immédiatement sensible. Imaginons qu’on propose à un joueur d’appuyer une fois sur la détente d’un revolver contre une somme d’argent. Si l’échec signifie la mort ($L$) et le succès une récompense financière ordinaire ($\Delta U$), le rapport des enjeux $L/\Delta U$ atteint des ordres de grandeur considérables — disons, à titre d’illustration, $L/\Delta U = 10\,000$. L’@eq:ch04-seuil ramène alors le seuil tolérable à $p^\ast = 1 / 10\,001 \approx 0{,}0100\,\%$, soit moins d’une chance sur dix mille.

Pour un barillet ordinaire contenant une cartouche sur six chambres, personne de sensé ne joue à ce tarif. À un tel rapport des enjeux, la règle de l’UES ne permet d’appuyer sur la détente que dans deux situations extrêmes : soit la récompense $\Delta U$ est si colossale au regard de la perte $L$ — par exemple sauver une vie ou échapper à une perte presque aussi certaine — que le rapport $L/\Delta U$ cesse d’être démesuré ; soit le décideur est *quasi absolument convaincu* que la chambre est vide, au point d’estimer la probabilité d’accident bien en dessous du seuil — par exemple à $0{,}001\,\%$, soit une chance sur cent mille.

L’exemple quantitatif suivant réunit sur une même courbe les deux régimes, celui de la course à la voile et celui de la roulette russe, afin de montrer comment le seuil chute avec le rapport des enjeux.

::: {.exemple-quantitatif titre="Seuil de décision face aux enjeux : course à la voile et roulette russe"}
**Mise en place.** Les grandeurs ci-dessous sont purement illustratives et choisies pour mettre en évidence le comportement du seuil $p^\ast$ selon l’@eq:ch04-seuil. On compare d’abord nos deux navigateurs — M. Y avec une probabilité d’échec estimée $p$ de 0,1 % et M. X avec une estimation de 5 % — placés devant un même rapport des enjeux $L/\Delta U$ égal à 25, en prenant le voilier renforcé pour option sûre de référence. On ajoute ensuite le cas extrême de la roulette russe, avec un rapport des enjeux de 10 000 et un décideur convaincu que le risque d’échec n’est que de 0,001 %. Dans les trois situations, on suppose une issue binaire (réussite ou échec grave, démâtage ou tir mortel), une référence sûre bien définie et un choix guidé uniquement par l’estimation $p$ du décideur, sans facteur omis.

![Seuil de décision $p^\ast$ en fonction du rapport des enjeux $L/\Delta U$ en échelle logarithmique : positions de M. X (5 %) et de M. Y (0,1 %) face au seuil de 3,85 % pour un rapport de 25, et effondrement du seuil à 0,0100 % dans le cas de la roulette russe pour un rapport de 10 000.](figures/ch04-seuil.pdf){#fig:ch04-seuil width=90%}

**Calcul.**

::: {.inclure fichier="tableaux/ch04-seuil.md"}
:::

Le @tbl:ch04-seuil et la @fig:ch04-seuil résument ces trois situations. Pour un rapport des enjeux de 25, l’@eq:ch04-seuil donne $p^\ast = 1 / (1 + 25) = 1/26$, soit un seuil de 3,85 % : avec 0,1 %, M. Y reste très au-dessous du seuil et choisit le voilier léger (« on part »), tandis qu’avec 5 %, M. X le dépasse et préfère le bateau renforcé (« on renonce »). Lorsque le rapport des enjeux grimpe à 10 000 dans le cas de la roulette russe, le seuil s’effondre à $p^\ast = 1 / (1 + 10\,000)$, soit 0,0100 % : seul un décideur qui estime la probabilité d’échec encore au-dessous — ici 0,001 % — accepte de s’engager.

**Lecture.** L’exemple fait ressortir deux mécanismes complémentaires. En premier lieu, pour un rapport des enjeux identique de 25, la même règle de rationalité sépare M. X et M. Y de part et d’autre du seuil de 3,85 % sans que l’un des deux raisonne de travers. En second lieu, sur les axes logarithmiques de la @fig:ch04-seuil, dès que le rapport des enjeux dépasse quelques dizaines, la courbe du seuil suit une droite descendante de pente $-1$ : chaque facteur dix sur la lourdeur de la perte relative divise par dix le risque maximal tolérable. Ce que cet exemple ne montre pas, en revanche, c’est ce qui garantirait que l’estimation de 0,1 % ou de 0,001 % couvre réellement tous les modes d’échec possibles : le tableau compare le seuil à l’estimation retenue dans la représentation, sous l’hypothèse explicite qu’aucun facteur oublié n’altère la réalité de l’épreuve.
:::

## Décider une seule fois ou à répétition {#sec:ch04-decision-unique}

Arrivé à ce point, un lecteur habitué aux applications statistiques de la théorie de la décision pourrait se rassurer : si M. Y choisit le voilier léger chaque fois que $p < p^\ast$, son gain moyen sur l’ensemble de ses choix l’emportera, à la longue, sur l’option sûre. Cette consolation repose pourtant sur une confusion décisive entre deux régimes d’action.

Dans une suite de décisions répétées dans des conditions stables — le citadin qui consulte chaque matin une prévision de pluie à 70 % pour décider d’emporter ou non son parapluie (@sec:ch03-calibration-historique), un organisme de crédit qui traite chaque mois des milliers de dossiers comparables selon les mêmes règles, un service de tri qui oriente un flux quotidien de demandes —, l’espérance mathématique prend littéralement corps dans la moyenne empirique. La répétition crée une population d’épreuves semblables. Une erreur sur un dossier isolé s’absorbe dans le bilan global ; si les probabilités annoncées se révèlent systématiquement optimistes ou si le seuil est mal réglé, l’écart entre les fréquences observées et les prévisions consignées finit par apparaître dans l’historique, et l’on peut recalibrer la règle pour les milliers de cas suivants.

Il en va tout autrement devant ce que nous appellerons une **décision unique** : une décision prise une seule fois, sans série d’essais comparables, et dont la réponse du monde n’arrive qu’après l’acte. Lancer un voilier léger dans une course transatlantique, engager une intervention chirurgicale exceptionnelle, figer l’architecture d’un grand système d’information ou déployer une opération irréversible ne forment pas un échantillon tiré d’une urne stationnaire. Ici, aucune loi des grands nombres ne vient amortir un mauvais coup du sort : le bateau casse ou franchit la ligne, une seule fois, et la perte $L$ s’encaisse tout entière sur cette unique traversée. Dire que $p = 0{,}1\,\%$ reste inférieur à $p^\ast = 3{,}85\,\%$ signifie seulement que, compte tenu de la représentation de M. Y, le pari l’emporte en utilité espérée ; ce chiffre ne constitue en rien une promesse fréquentiste que *cette* traversée se passera bien.

De plus, comme nous l’avons démontré à la @sec:ch03-prevision-previsionniste, la réponse du monde n’arrive pas seulement *après* le point de non-retour ; une issue isolée ne permet même pas aisément de départager les estimations qui ont dicté le choix. Si le bateau revient entier, M. Y ne saura jamais s’il devait ce succès à un gréement irréprochable ou à la bonne fortune d’avoir évité le grain qui aurait brisé un mât fragile à 5 %. Et s’il démâte, la facture du remorquage est déjà due avant toute réévaluation. La calibration aide là où les décisions se répètent et où l’expérience passée instruit les essais à venir ; les décisions uniques exigent d’autres garde-fous, que construira le @sec:ch17.

## La question laissée ouverte {#sec:ch04-question-ouverte}

Rassemblons maintenant la thèse établie au @sec:ch02 et la règle de décision établie ici. L’UES montre comment décider de façon cohérente *à l’intérieur* d’une représentation : elle fixe le seuil $p^\ast$ imposé par le rapport des enjeux et garantit que l’option retenue est optimale au regard des probabilités $p$ que le décideur accorde aux mondes possibles envisagés.

Mais d’où vient ce nombre $p$ ? Il sort d’une représentation (@def:representation) bâtie à l’intérieur d’un cadre fini (@def:cadre), qui n’a retenu que certaines grandeurs, certaines catégories et certains scénarios d’échec, en laissant tout le reste dans l’arrière-plan tu $(\dots)$. Tant que les seules incertitudes en jeu portent sur des événements explicitement envisagés — un coup de vent prévu dans le bulletin météo, une fatigue ordinaire des matériaux déjà chiffrée dans les abaques —, l’@eq:ch04-seuil règle proprement le compromis entre prudence et gain.

Supposez à présent que la quasi-certitude de 0,001 % qui décide le joueur de roulette russe à presser la détente provienne d’un cadre qui a omis d’inspecter une chambre chargée du barillet — ou que l’estimation de 0,1 % de M. Y repose sur des fiches nominales qui taisent un défaut interne caché dans la structure du mât. Rien, dans le calcul de l’utilité espérée ni dans l’@eq:ch04-seuil, ne déclenche la moindre alarme : la formule compare sagement le nombre $p$ inscrit dans la représentation au seuil $p^\ast$, constate $p < p^\ast$ et autorise le départ sans broncher.

Or le monde, une fois l’acte engagé, ne consulte pas nos probabilités (@sec:ch02-monde-action). La détente libère le percuteur face à ce qui se trouve réellement dans la chambre, et la houle sollicite le mât tel qu’il est, avec tout ce que le cadre avait relégué dans la parenthèse $(\dots)$. Nous touchons ici la question centrale que ce chapitre laisse délibérément ouverte : *comment décider devant des enjeux sans appel quand notre propre calcul ne peut rien dire de ce que notre cadre a manqué ?* Pour y répondre, il nous faudra d’abord comprendre ce que mesurent au juste nos chiffres d’incertitude et ce qui peut nous détromper à temps avant l’acte, puis nous reviendrons directement aux décisions uniques et aux moyens de s’y prémunir au @sec:ch17.

::: {.nuance titre="Le monde ne consulte pas nos probabilités"}
Une tentation fréquente consiste à vouloir corriger sur-le-champ l’@eq:ch04-seuil en modifiant simplement sa consigne : « ne partir que si le *véritable* risque d’échec dans le monde est inférieur à $p^\ast$ ». Sous la règle de l’UES, cette échappatoire s’effondre aussitôt. Une règle de décision ne peut opérer que sur ce qui figure dans la représentation du décideur ; ce que le cadre a omis est précisément ce qu’aucune coordonnée du calcul ne nomme et qu’on ne saurait donc lire sur un cadran pour le comparer au seuil.

À défaut de mesurer ce qui échappe au cadre, l’habitude de raisonner à l’envers (@sec:ch03-raisonner-envers) rend déjà un premier service précieux : elle oblige à regarder l’écart qui sépare $p$ de $p^\ast$. Lorsque $L/\Delta U = 25$, il suffit d’un péril caché de moins de quatre points de pourcentage pour faire basculer la décision de M. Y ; lorsque $L/\Delta U = 10\,000$, l’écart admissible se réduit à moins d’un centième de pour cent. Savoir à quel point la frontière est étroite ne fait toutefois pas surgir de soi-même la chambre oubliée du barillet : comment traduire cette conscience en règle pratique de décision sans prétendre mesurer l’inconnu fera l’objet du @sec:ch17.
:::

::: {.question}
Pour votre prochain déploiement irréversible ou votre prochaine décision sans retour en arrière, quel est le rapport des enjeux $L/\Delta U$, et quel seuil $p^\ast$ impose-t-il ?
:::

## Points clés {.points-cles}

- Devant un choix incertain qui précède la réponse du monde, l’utilité espérée subjective (UES) prescrit de décider en pondérant l’utilité des conséquences par ses propres probabilités, plutôt que d’attendre des fréquences observées.
- Face à une référence sûre, une option risquée ne paie que tant que la probabilité d’échec estimée $p$ reste inférieure au seuil $p^\ast = 1 / (1 + L/\Delta U)$, qui tend vers zéro à mesure que croît le rapport des enjeux $L/\Delta U$.
- Deux décideurs également rationnels, confrontés au même problème et aux mêmes enjeux, peuvent donc prendre des décisions opposées dès lors que leurs représentations situent $p$ de part et d’autre du seuil $p^\ast$.
- À l’inverse des séries répétées où la calibration corrige les écarts dans la durée, une décision unique ne bénéficie d’aucune moyenne protectrice : le monde livre une seule issue après l’acte, sans consulter nos estimations.
- Si la conviction qui place $p$ au-dessous de $p^\ast$ provient d’un cadre qui a omis un facteur décisif dans $(\dots)$, rien dans la cohérence du calcul d’utilité espérée ne donne l’alerte — question ouverte que reprendra le @sec:ch17.
