# Paramètres des exemples quantitatifs {#sec:annexe-d}

Tous les exemples quantitatifs de l’ouvrage ont une vocation strictement illustrative : leurs paramètres sont choisis pour mettre à nu un mécanisme, un seuil ou un changement de régime, et non pour estimer une grandeur empirique réelle. L’ensemble des figures et des tableaux chiffrés des chapitres [-@sec:ch01], [-@sec:ch03], [-@sec:ch04], [-@sec:ch08], [-@sec:ch09], [-@sec:ch12], [-@sec:ch14], [-@sec:ch16] et [-@sec:ch17] sont engendrés mécaniquement à partir des jeux de paramètres canoniques et des fonctions récapitulés ci-dessous.

## Révision bayésienne par cotes (chapitre [-@sec:ch01]) {#sec:annexe-d-bayes}

L’exemple d’examen par ultrasons d’une soudure (@sec:ch01-bayes, @fig:ch01-bayes-cotes, @tbl:ch01-bayes-cotes) repose sur les caractéristiques d’étalonnage suivantes :

- probabilité d’un signal anormal en présence d’un défaut : $\Pr(T^+ \mid D) = 75\,\%$ (signal normal : $\Pr(T^- \mid D) = 25\,\%$) ;
- probabilité d’un signal anormal sur une soudure saine : $\Pr(T^+ \mid \bar{D}) = 15\,\%$ (signal normal : $\Pr(T^- \mid \bar{D}) = 85\,\%$) ;
- rapports de vraisemblance : $\Lambda(T^+) = 0{,}75 / 0{,}15 = 5$ et $\Lambda(T^-) = 0{,}25 / 0{,}85 = 5/17 \approx 0{,}294$ (et $\Lambda = 5^2 = 25$ pour deux signaux anormaux conditionnellement indépendants).

| Situation | Probabilité a priori | Cote a priori | Rapport de vraisemblance $\Lambda$ | Cote a posteriori | Probabilité a posteriori |
| :-- | --: | --: | --: | --: | --: |
| Lot courant, signal anormal | 4 % | $1/24 \approx 0{,}0417$ | 5 | $5/24 \approx 0{,}208$ | 17,2 % |
| Zone suspecte, signal anormal | 20 % | 0,25 | 5 | 1,25 | 55,6 % |
| Zone suspecte, signal normal | 20 % | 0,25 | $5/17 \approx 0{,}294$ | $5/68 \approx 0{,}0735$ | 6,85 % |
| Zone suspecte, deux signaux anormaux indépendants | 20 % | 0,25 | 25 | 6,25 | 86,2 % |

Table: Paramètres et résultats de l’exemple de révision par cotes du @sec:ch01 (@tbl:ch01-bayes-cotes). {#tbl:annexe-d-bayes}

## Score logarithmique de surprise (chapitre [-@sec:ch03]) {#sec:annexe-d-score-log}

L’exemple comparant les deux prévisionnistes M. X et M. Y avant la course à la voile (@sec:ch03-prevision-previsionniste, @fig:ch03-score-log, @tbl:ch03-score-log) évalue la surprise $S(p) = -\ln p$ de chaque prévision selon que le voilier léger casse ou tient.

| Prévision | Probabilité de casse $p$ | Surprise si le bateau casse $-\ln p$ | Surprise s’il tient $-\ln(1-p)$ |
| :-- | --: | --: | --: |
| M. X | 5 % | 3,00 | 0,051 |
| M. Y | 0,1 % | 6,91 | 0,001 |
| Rapport de vraisemblance (X contre Y) | — | 50 | 0,951 |

Table: Paramètres et surprises de l’exemple du score logarithmique du @sec:ch03 (@tbl:ch03-score-log). {#tbl:annexe-d-score-log}

## Seuil de décision, risque omis et marge d’humilité — modèle M2 (chapitres [-@sec:ch04] et [-@sec:ch17]) {#sec:annexe-d-seu}

Les exemples de décision de la course à la voile et des situations à enjeu extrême sont régis par le modèle M2 (@sec:ch04-course-voile, @sec:ch17-course-revisitee) :

- seuil de décision (@eq:ch04-seuil) : $p^\ast = \Delta U / (\Delta U + L) = 1 / (1 + L/\Delta U)$, soit $p^\ast = 1/26 \approx 3{,}85\,\%$ pour $L/\Delta U = 25$, et $p^\ast = 1/10\,001 \approx 0{,}0100\,\%$ pour $L/\Delta U = 10\,000$ ;
- règle de décision avec marge d’humilité $b$ (@eq:ch17-regle-marge) : on part si $p + b < p^\ast$, on renonce si $p + b \ge p^\ast$ ;
- risque réel dans le monde en présence d’une probabilité d’échec omise $z$ indépendante de $p$ (@eq:ch17-risque-reel) : $p_w = 1 - (1 - p)(1 - z)$.

Le @sec:ch04 (@fig:ch04-seuil, @tbl:ch04-seuil) utilise les trois situations de base sans marge ni facteur omis dans le cadre ($b = 0$, $z = 0$ : *M. Y*, *M. X* et *Roulette russe*) ; le @sec:ch17 (@fig:ch17-decisions, @tbl:ch17-scenarios, @tbl:ch17-decisions) déploie les six situations du tableau ci-dessous en remplaçant à $L/\Delta U = 10\,000$ la roulette russe par le *Vol de nuit en montagne*, afin de garder $p$ et $z$ rigoureusement disjoints.

| Situation | $L/\Delta U$ | $p$ | $b$ | $z$ | $p + b$ | $p^\ast$ | Décision | $p_w$ | Issue |
| :------------------ | --------: | -----------: | ----: | --------: | -----------: | ------------: | :------------ | -----------: | :-------------- |
| M. Y | 25 | 0,1 % | 0 % | 0 % | 0,1 % | 3,85 % | on part | 0,100 % | départ justifié |
| M. X | 25 | 5 % | 0 % | 0 % | 5 % | 3,85 % | on renonce | 5,00 % | renoncement justifié |
| M. Y, fissure non repérée | 25 | 0,1 % | 0 % | 8 % | 0,1 % | 3,85 % | on part | 8,09 % | piège silencieux |
| … avec une marge | 25 | 0,1 % | 4 % | 8 % | 4,1 % | 3,85 % | on renonce | 8,09 % | sauvé par la marge |
| Prudence superflue | 25 | 0,1 % | 4 % | 0 % | 4,1 % | 3,85 % | on renonce | 0,100 % | prudence superflue |
| Vol de nuit en montagne | 10 000 | 0,001 % | 0 % | $1/6 \approx 16{,}7\,\%$ | 0,001 % | 0,0100 % | on part | 16,7 % | piège silencieux |

Table: Paramètres et résultats des scénarios de décision des chapitres [-@sec:ch04] (@tbl:ch04-seuil) et [-@sec:ch17] (@tbl:ch17-scenarios et @tbl:ch17-decisions). {#tbl:annexe-d-seu}

*(Légende et précision du @tbl:annexe-d-seu : $p$ désigne la probabilité d’échec estimée par le décideur, $L/\Delta U$ le rapport des enjeux, $b$ et $z$ sont exprimés en points de probabilité — $z$ représente ici une fissure cachée de $8\,\%$ pour « M. Y, fissure non repérée » ou un régime de givrage non modélisé de $1/6$ pour le « Vol de nuit en montagne » — et les résultats calculés $p^\ast$ et $p_w$ sont affichés à trois chiffres significatifs.)*

## Chaînes en série et contrôles croisés — modèle M1 (chapitres [-@sec:ch08] et [-@sec:ch14]) {#sec:annexe-d-chaines}

Les exemples de chaîne à $N = 4$ étapes (@sec:ch08-chaines-controles, @fig:ch08-chaine, @tbl:ch08-chaine) et de trajectoire d’agent en $N = 12$ étapes (@sec:ch14-trajectoire-longue, @fig:ch14-chaine-agent, @tbl:ch14-chaine-agent) partagent les paramètres suivants :

- probabilité d’erreur indépendante par étape : $p = 6\,\%$ ;
- probabilité d’oubli du contrôleur pair lors d’un contrôle croisé à chaque étape : $m = p = 6\,\%$ (d’où une probabilité $p^2 = 0{,}36\,\%$ qu’une erreur indépendante d’une étape échappe à la fois au producteur et au pair) ;
- probabilité d’un facteur omis partagé affectant l’ensemble des étapes : $q = 0\,\%$ (absence de facteur partagé) ou $q = 3\,\%$.

| $N$ | Facteur partagé $q$ | Chaîne sans contrôle | Contrôle croisé à chaque étape | Part indépendante (sans $\rightarrow$ avec contrôle) | Part des défaillances restantes où intervient $q$ |
| --: | --: | --: | --: | --: | --: |
| 4 | 0 % | 21,9 % | 1,43 % | 21,9 % $\rightarrow$ 1,43 % | — |
| 4 | 3 % | 24,3 % | 4,39 % | 21,9 % $\rightarrow$ 1,43 % | 68,3 % |
| 12 | 0 % | 52,4 % | 4,24 % | 52,4 % $\rightarrow$ 4,24 % | — |
| 12 | 3 % | 53,8 % | 7,11 % | 52,4 % $\rightarrow$ 4,24 % | 42,2 % |

Table: Paramètres et résultats du modèle de chaîne et de contrôle croisé aux chapitres [-@sec:ch08] (@tbl:ch08-chaine, $N = 4$) et [-@sec:ch14] (@tbl:ch14-chaine-agent, $N = 12$). {#tbl:annexe-d-chaines}

*(Dans le @tbl:annexe-d-chaines, « Part indépendante » désigne la probabilité d’échec due aux seules erreurs locales lorsque le facteur partagé est nul, $q = 0\,\%$.)*

## Sensibilité, fausses alertes, échappement et modèle partagé — modèle M1 (chapitres [-@sec:ch09] et [-@sec:ch16]) {#sec:annexe-d-echappement}

Le modèle du contrôleur (@sec:ch09-risque-echappement, @fig:ch09-echappement, @tbl:ch09-echappement ; @sec:ch16-taux-echappement, @fig:ch16-modele-partage, @tbl:ch16-modele-partage) compare quatre configurations définies par le taux d’erreur du producteur $P(E)$ (affiché $P(\text{faux})$ dans les tableaux), la part des causes d’erreur partagées $c$, le taux d’oubli sur les autres erreurs $m$ et le taux de fausses alertes $f$ sur les affirmations justes :

- sensibilité : $s = (1 - c)(1 - m)$ (@eq:ch09-sensibilite) ;
- valeur prédictive positive : $\mathrm{VPP} = P(E)s / \bigl[P(E)s + (1 - P(E))f\bigr]$ (@eq:ch09-vpp) ;
- échappement : $1 - s\,u$, avec $u = \mathrm{VPP}$ sous appariement des probabilités et $u = 1$ lorsque chaque alerte est examinée (@eq:ch09-echappement) ;
- risque résiduel : $R = P(E)(1 - s\,u)$ (@eq:ch09-risque).

Le @sec:ch09 met en regard *Contrôle entre pairs* et *Indépendant et précis* (ainsi que la courbe continue en fonction de $P(E)$ à contrôleur fixé $c = 10\,\%$, $m = 20\,\%$, $f = 5\,\%$) ; le @sec:ch16 compare les quatre scénarios.

| Grandeur | Contrôle entre pairs | Un modèle pour tous | Modèle partagé, contrôleur précis | Indépendant et précis |
| :-- | --: | --: | --: | --: |
| Taux d’erreur du producteur $P(\text{faux})$ | 10 % | 2 % | 2 % | 2 % |
| Causes d’erreur partagées $c$ | 10 % | 60 % | 60 % | 10 % |
| Oubli sur les autres erreurs $m$ | 20 % | 20 % | 20 % | 10 % |
| Taux de fausses alertes $f$ | 5 % | 5 % | 0,5 % | 0,5 % |
| Sensibilité $s = (1 - c)(1 - m)$ | 72 % | 32 % | 32 % | 81 % |
| Alertes qui sont de vraies erreurs (VPP) | 61,5 % | 11,6 % | 56,6 % | 76,8 % |
| Alertes par vraie erreur interceptée ($1/\mathrm{VPP}$) | 1,6 | 8,7 | 1,8 | 1,3 |
| Échappement, alertes suivies à hauteur de la VPP | 55,7 % | 96,3 % | 81,9 % | 37,8 % |
| Échappement, chaque alerte examinée ($u = 1$) | 28,0 % | 68,0 % | 68,0 % | 19,0 % |
| Risque, alertes suivies à hauteur de la VPP | 5,57 % | 1,93 % | 1,64 % | 0,756 % |
| Risque, chaque alerte examinée ($u = 1$) | 2,80 % | 1,36 % | 1,36 % | 0,380 % |
| Risque sans contrôleur | 10 % | 2 % | 2 % | 2 % |

Table: Paramètres et résultats des quatre configurations du modèle d’échappement aux chapitres [-@sec:ch09] (@tbl:ch09-echappement) et [-@sec:ch16] (@tbl:ch16-modele-partage). {#tbl:annexe-d-echappement}

### Exemples arithmétiques courts (chapitres [-@sec:ch00] et [-@sec:ch09]) {#sec:annexe-d-arithmetique}

Trois calculs arithmétiques courts complètent le @sec:ch09 (le troisième apparaît également en ouverture à la @sec:ch00-enigme-arithmetique) :

| Exemple | Paramètres d’entrée | Résultat calculé | Tableau |
| :-- | :-- | :-- | :-- |
| Dépistage d’une affection rare | Prévalence $1\,\%$, sensibilité $90\,\%$, faux positifs $5\,\%$ | $\mathrm{VPP} = 2/13 \approx 15{,}4\,\%$ | @tbl:ch09-depistage |
| Désaccords producteur / relecteur (erreurs indépendantes) | Producteur dans l’erreur : $1\,\%$ ; relecteur dans l’erreur : $10\,\%$ | Désaccords où le producteur avait raison : $11/12 \approx 91{,}7\,\%$ | @tbl:ch09-desaccords |
| Produit taux d’erreur $\times$ échappement | Système A : $10\,\% \times 1\,\%$ ; Système B : $1\,\% \times 90\,\%$ | Affirmations fausses suivies d’effet : $0{,}1\,\%$ contre $0{,}9\,\%$ (facteur 9) | @tbl:ch09-taux-echappement |

Table: Paramètres et résultats des trois exemples arithmétiques des chapitres [-@sec:ch00] et [-@sec:ch09]. {#tbl:annexe-d-arithmetique}

## Réinterrogatoire et sévérité sur cinq tirages (chapitre [-@sec:ch12]) {#sec:annexe-d-plausibilite}

L’exemple du @sec:ch12 (@sec:ch12-calibration-longue-traine, @fig:ch12-plausibilite, @tbl:ch12-plausibilite) évalue un contrôle consistant à poser $k = 5$ fois indépendamment la même question à un modèle génératif et à signaler une alerte dès que les cinq réponses ne sont pas toutes identiques.

| Régime | Distribution des réponses ($\checkmark$ = juste) | Réponse fausse $p_{\text{faux}}$ | Sévérité (5 tirages divergent $\mid$ 1re fausse) | Fausse alerte (5 tirages divergent $\mid$ 1re juste) |
| :-- | :-- | --: | --: | --: |
| Fait bien connu (tour Eiffel) | Paris $\checkmark$ 97 %, Lyon 2 %, Marseille 1 % | 3 % | $> 99{,}9\,\%$ | 11,5 % |
| Fait rare et arbitraire (date de naissance) | 14 mai 22 %, 3 août 20 %, 22 nov. $\checkmark$ 18 %, 9 janv. 16 %, 17 oct. 14 %, 5 mars 10 % | 82 % | 99,9 % | 99,9 % |
| Idée reçue répandue (planète la plus proche en moyenne) | Vénus 88 %, Mercure $\checkmark$ 9 %, Mars 3 % | 91 % | 42,0 % | $> 99{,}9\,\%$ |

Table: Distributions et résultats de l’exemple de réinterrogatoire à $k = 5$ tirages du @sec:ch12 (@tbl:ch12-plausibilite). {#tbl:annexe-d-plausibilite}
