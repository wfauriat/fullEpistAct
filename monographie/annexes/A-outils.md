# Outils de référence {#sec:annexe-a .annexes}

Cette annexe rassemble sous forme d’aide-mémoire les outils formels et les trois modèles (M1, M2, M3) mobilisés au fil de l’ouvrage. Elle reprend, sans élément nouveau, les définitions, les formules et les hypothèses exposées au @sec:ch01 et dans les encadrés *Boîte à outils* et *Noyau formel* des chapitres suivants. Les termes techniques sont définis dans le glossaire (annexe [-@sec:annexe-b]) et les symboles sont récapitulés dans la table des notations (annexe [-@sec:annexe-c]).

## Logique et règles à arrière-plan tacite {#sec:annexe-a-logique}

Une déduction est *valide* lorsque sa forme interdit que ses prémisses soient vraies et sa conclusion fausse ; elle est *solide* lorsqu’elle est valide et que ses prémisses sont vraies (@sec:ch01-modes-inference). Une induction généralise une régularité observée sur un échantillon fini à des cas non encore observés. Ni la déduction ni l’induction ne certifient par elles-mêmes le cadre dans lequel leurs prémisses ou leurs observations sont formulées (@sec:ch02-rigueur-formelle).

Dès qu’une règle conditionnelle porte sur le monde matériel ou social, la liste des circonstances nécessaires à sa vérité ne peut pas être close (@sec:ch01-regles-conditionnelles, @sec:ch02-pertinence-exceptions). On l’écrit :

$$A \cap (\dots) \rightarrow B,$$

où $A$ rassemble les conditions explicitement énoncées, $B$ la conséquence attendue et $(\dots)$ l’arrière-plan tacite (noté $\mathcal{T}$ dans le texte, @eq:ch01-regle). Faire passer une condition de $(\dots)$ dans $A$ précise la règle mais ne vide jamais la parenthèse.

## Probabilités, conditionnement et révision bayésienne {#sec:annexe-a-probabilites}

Sur un ensemble $\Omega$ d’issues élémentaires (ou de mondes possibles, @sec:ch03), une mesure de probabilité $\Pr(\cdot)$ vérifie les trois axiomes de Kolmogorov (@sec:ch01-probabilite) : positivité ($\Pr(A) \ge 0$), normalisation ($\Pr(\Omega) = 1$) et additivité sur les événements deux à deux incompatibles ($\Pr(A \cup B) = \Pr(A) + \Pr(B)$ lorsque $A \cap B = \emptyset$). On en tire $\Pr(\bar{A}) = 1 - \Pr(A)$.

Lorsque $\Pr(A) > 0$, la probabilité conditionnelle de $B$ sachant $A$ (@eq:ch01-cond) et la formule des probabilités totales sur une partition $H_1, \dots, H_k$ de $\Omega$ (@eq:ch01-totale) s’écrivent :

$$\Pr(B \mid A) = \frac{\Pr(A \cap B)}{\Pr(A)}, \qquad \Pr(B) = \sum_{i=1}^{k} \Pr(B \mid H_i)\,\Pr(H_i).$$

Dans un cadre retenant un vecteur de variables représentées $X = (X_1, \dots, X_k)$ observé à la valeur $x$ (@def:cadre, @sec:ch02-cadre-specification), décomposer la prévision d’une grandeur $Y$ selon des hypothèses $H_i$ conditionnellement à $X = x$ s’écrit (@eq:ch02-cond-cadre) :

$$\Pr(Y \mid X = x) = \sum_{i=1}^{m} \Pr(Y \mid X = x, H_i)\,\Pr(H_i \mid X = x).$$

### Règle de Bayes sous forme de cotes et rapport de vraisemblance {#sec:annexe-a-bayes}

Pour une hypothèse $H$ de probabilité $\Pr(H) < 1$, sa cote contre l’hypothèse complémentaire $\bar{H}$ vaut $\text{cote}(H) = \Pr(H)/\Pr(\bar{H}) = \Pr(H)/\bigl(1 - \Pr(H)\bigr)$, et inversement $\Pr(H) = \text{cote}(H)/\bigl(1 + \text{cote}(H)\bigr)$ (@sec:ch01-bayes).

Devant une observation $E$ telle que $\Pr(E \mid \bar{H}) > 0$, le rapport de vraisemblance de $E$ en faveur de $H$ contre $\bar{H}$ est :

$$\Lambda(E) = \frac{\Pr(E \mid H)}{\Pr(E \mid \bar{H})}.$$

La règle de Bayes prend alors la forme multiplicative (@eq:ch01-bayes-cotes) :

$$\text{cote}(H \mid E) = \text{cote}(H) \times \Lambda(E).$$

Si deux observations $E_1$ et $E_2$ sont conditionnellement indépendantes tant sous $H$ que sous $\bar{H}$, le rapport de vraisemblance conjoint se factorise : $\Lambda(E_1 \cap E_2) = \Lambda(E_1)\,\Lambda(E_2)$. Lorsqu’une observation a même probabilité sous les deux hypothèses ($\Lambda(E) = 1$), elle laisse la cote inchangée.

### Taux de base, sensibilité et valeur prédictive positive {#sec:annexe-a-vpp}

Pour un contrôle ou un test de dépistage (@sec:ch09-taux-base-vpp) portant sur un état ou une erreur d’occurrence *a priori* (taux de base) $P(E) = \Pr(E)$, de sensibilité $s = \Pr(\text{alerte} \mid E)$ et de taux de fausses alertes $f = \Pr(\text{alerte} \mid \bar{E})$, la valeur prédictive positive (proportion des alertes qui correspondent à de vraies erreurs) vaut :

$$\mathrm{VPP} = \Pr(E \mid \text{alerte}) = \frac{P(E)\,s}{P(E)\,s + \bigl(1 - P(E)\bigr)\,f}.$$

En cotes, $\text{cote}(E \mid \text{alerte}) = \text{cote}(E) \times (s / f)$. À sensibilité $s$ et taux de fausses alertes $f > 0$ fixés, lorsque le taux d’erreur $P(E)$ tend vers $0$, la valeur prédictive positive tend vers $0$ : dès que $P(E)$ devient petit devant $f/s$, la majorité des alertes émises sont des fausses alertes.

Symétriquement, l’absence d’alerte (l’accord $A$ du comparateur avec l’affirmation, @sec:ch09-severite) multiplie la cote de justesse $\bar{E}$ par $(1 - f)/(1 - s)$ (@eq:ch09-accord-cotes). Un contrôle passé sans alerte n’est sévère (@def:severite) que si sa sensibilité $s$ à l’erreur redoutée est élevée, ce qui rend $1 - s$ petit.

## Score logarithmique de surprise {#sec:annexe-a-score-log}

Lorsqu’une prévision attribuait la probabilité $p \in \left]0, 1\right]$ à l’issue qui s’est effectivement produite, sa surprise (score logarithmique, @sec:ch01-score-logarithmique, @sec:ch03-prevision-previsionniste) vaut (@eq:ch01-score-log) :

$$S(p) = -\ln p.$$

La surprise est nulle pour une issue annoncée comme certaine ($S(1) = 0$), strictement décroissante en $p$, et tend vers $+\infty$ lorsque $p \to 0$. Sur des épreuves indépendantes, les surprises s’additionnent : $S(p_1 p_2) = S(p_1) + S(p_2)$.

Si deux prévisions attribuent respectivement les probabilités $p_1$ et $p_2$ à l’issue observée, la différence de leurs surprises est le logarithme du rapport de vraisemblance $\Lambda = p_1 / p_2$ de la première prévision contre la seconde sur cette issue (@eq:ch01-surprise-vraisemblance) :

$$S(p_2) - S(p_1) = \ln\left(\frac{p_1}{p_2}\right) = \ln \Lambda.$$

## Utilité espérée subjective, seuil de décision et modèle M2 {#sec:annexe-a-seu}

Dans le formalisme de Savage (@sec:ch04-ues), un décideur choisit parmi des actes $a \in \mathcal{A}$ celui qui maximise l’utilité espérée $\mathrm{UE}(a) = \sum_{\omega \in \Omega} \Pr(\omega)\,U\bigl(c(a, \omega)\bigr)$ calculée avec ses propres probabilités $\Pr(\omega)$ à l’intérieur de son cadre.

### Seuil de décision de base {#sec:annexe-a-seuil}

Face au choix entre une option sûre d’utilité $U_{\text{sûr}}$ et une option risquée qui réussit avec probabilité $1 - p$ (gain $\Delta U = U_{\text{succès}} - U_{\text{sûr}} > 0$) ou échoue avec probabilité estimée $p$ (perte $L = U_{\text{sûr}} - U_{\text{échec}} > 0$), l’option risquée a une utilité espérée supérieure à l’option sûre si et seulement si $(1 - p)\,\Delta U > p\,L$, soit $p < p^\ast$ (@sec:ch04-course-voile, @eq:ch04-seuil) :

$$p^\ast = \frac{\Delta U}{\Delta U + L} = \frac{1}{1 + L/\Delta U}.$$

Le seuil $p^\ast$ ne dépend que du rapport des enjeux $L/\Delta U$ et tend vers $0$ comme $\Delta U / L$ lorsque la perte en cas d’échec domine le gain en cas de succès.

### Modèle M2 : risque réel et marge d’humilité {#sec:annexe-a-modele-m2}

Le modèle M2 (@sec:ch17-course-revisitee) prolonge ce schéma lorsqu’un facteur omis par le cadre ajoute une probabilité d’échec propre $z \in [0, 1]$, supposée indépendante du risque modélisé $p$. Le risque réel auquel l’action est exposée dans le monde vaut alors (@eq:ch17-risque-reel) :

$$p_w = 1 - (1 - p)(1 - z) = p + z - pz \ge \max(p, z).$$

Le décideur n’a pas accès à $z$. S’il applique une marge d’humilité délibérée $b \ge 0$ relevant d’un jugement de prudence hors du calcul d’utilité espérée interne au cadre, sa règle de départ devient $p + b < p^\ast$ (@eq:ch17-regle-marge). Croiser la décision prise sur $p + b$ et la position du risque réel $p_w$ par rapport au seuil $p^\ast$ fait apparaître quatre régimes :

1. *Départ justifié* : $p + b < p^\ast$ et $p_w < p^\ast$.
2. *Piège silencieux* : $p + b < p^\ast$ mais $p_w \ge p^\ast$ (le facteur omis $z$ fait basculer le risque réel au-dessus du seuil sans que la représentation en avertisse).
3. *Sauvé par la marge* : $p < p^\ast \le p + b$ et $p_w \ge p^\ast$ (la marge $b$ retient une action que le risque réel rendait perdante en espérance).
4. *Prudence superflue* (ou renoncement justifié si $p \ge p^\ast$) : $p < p^\ast \le p + b$ et $p_w < p^\ast$ (prix de la marge lorsque $z$ est nul ou bénin : le gain $\Delta U$ est délaissé au profit de l’option sûre).

## Décomposition de la variance sur un ensemble d’alternatives admises {#sec:annexe-a-variance}

Soit $\Theta$ l’ensemble des alternatives admises (paramètres ou modèles $\theta$) muni d’une loi de probabilité, et soit $Y$ une grandeur réelle de moments du second ordre finis. La loi de la variance totale décompose la variance prédictive de $Y$ en deux termes (@sec:ch05-variance-totale, @eq:ch05-variance-totale) :

$$\mathrm{Var}(Y) = \mathbb{E}_\theta\bigl[\mathrm{Var}(Y \mid \theta)\bigr] + \mathrm{Var}_\theta\bigl(\mathbb{E}[Y \mid \theta]\bigr).$$

Le premier terme (moyenne des variances conditionnelles internes à chaque alternative $\theta$) représente la part traitée comme incertitude aléatoire ; le second terme (variance des prévisions moyennes $f_\theta(x) = \mathbb{E}[Y \mid X = x, \theta]$ entre les alternatives $\theta \in \Theta$) représente l’incertitude épistémique. Les deux termes étant des fonctionnelles définies sur le seul ensemble $\Theta$, toute alternative $\theta' \notin \Theta$ reçoit un poids nul et ne produit aucun désaccord mesuré (@prop:desaccord).

## Modèle M3 : le cadre comme cause commune {#sec:annexe-a-modele-m3}

Dans le modèle M3 (@sec:ch07-cause-commune, @prop:cause-commune), l’issue réelle produite par le monde s’écrit $Y = g(x, z)$, où $x$ est la valeur des variables représentées $X$ et $z$ un facteur extérieur omis. Une affirmation $f_1(x)$ et un comparateur interne $f_2(x)$ sont tous deux calculés à partir du seul contenu du cadre.

Sous les trois hypothèses du modèle — (1) $f_1$ et $f_2$ ne dépendent que de $x$ et d’éventuels tirages internes indépendants de $z$ sachant $X = x$, (2) $z$ n’est pas enregistré dans $X$, et (3) on conditionne sur la valeur observée $X = x$ —, l’événement $A$ (« $f_1(x)$ et $f_2(x)$ concordent ») est conditionnellement indépendant de $z$ sachant $X = x$, donc indépendant de l’erreur $e(x, z) = g(x, z) - f_1(x)$. Pour deux hypothèses $H_{\text{grand}}$ et $H_{\text{petit}}$ portant sur l’ampleur de $|e(x, z)|$, le rapport de vraisemblance de l’accord interne vaut (@eq:ch07-vraisemblance) :

$$\Lambda(A \mid X = x) = \frac{\Pr(A \mid X = x, H_{\text{grand}})}{\Pr(A \mid X = x, H_{\text{petit}})} = 1.$$

Un contrôle purement interne au cadre ne modifie donc pas la cote d’une erreur causée par un facteur que ce cadre omet.

## Modèle M1 : angles morts, chaînes, contrôles croisés et échappement {#sec:annexe-a-modele-m1}

### Cinq conditions nécessaires de détection {#sec:annexe-a-cinq-conditions}

Pour une classe d’erreurs $E_k \subseteq E$, l’événement $D$ (« l’erreur est détectée et prise en compte avant l’action », @sec:ch06-echappement, noté $C$ au @sec:ch09) implique la réalisation conjointe des cinq conditions $C_1$ (existence d’un comparateur), $C_2$ (différence : se tromper autrement), $C_3$ (comparabilité), $C_4$ (arrivée à temps) et $C_5$ (prise en compte) :

$$D \subseteq \bigcap_{j=1}^{5} C_j, \qquad \Pr(D \mid E_k) \le \min_{1 \le j \le 5} \Pr(C_j \mid E_k).$$

Si l’une des cinq conditions fait systématiquement défaut sur la classe $E_k$ ($\Pr(C_j \mid E_k) = 0$), la probabilité de détection est nulle et la probabilité d’échappement $\Pr(\bar{D} \mid E_k) = 1 - \Pr(D \mid E_k)$ vaut $1$ pour ce contrôle (@eq:ch06-echappement-un).

### Composition en série (chaîne) et en parallèle (contrôle croisé) {#sec:annexe-a-serie-parallele}

En notant $B_i$ l’angle mort structurel du composant $i$ (@def:angle-mort), $B_{\text{interfaces}}$ les causes d’erreur nées aux interfaces (notamment par blanchiment des conditions, @def:blanchiment) et $B_{\text{cmp}}$ l’angle mort de l’opération de comparaison (@sec:ch08-chaines-controles, @prop:chaines) :

$$B_{\text{chaîne}} \supseteq \left(\bigcup_{i=1}^{N} B_i\right) \cup B_{\text{interfaces}}, \qquad B_{\text{croisé}} = B_1 \cap (B_2 \cup B_{\text{cmp}}) = (B_1 \cap B_2) \cup (B_1 \cap B_{\text{cmp}}).$$

Dans une chaîne de $N$ étapes ayant chacune une probabilité d’erreur indépendante $p$ et exposées ensemble à un facteur omis partagé de probabilité $q$ (@sec:ch08-chaines-controles, @sec:ch14-trajectoire-longue), la probabilité d’échec sans contrôle et la probabilité d’échec lorsque chaque étape est doublée d’un contrôleur indépendant de même taux d’oubli $p$ valent :

$$\Pr(\text{échec, chaîne non contrôlée}) = 1 - (1 - p)^N (1 - q),$$

$$\Pr(\text{échec, chaîne contrôlée à chaque étape}) = 1 - (1 - p^2)^N (1 - q) \ge q.$$

La part des défaillances résiduelles de la chaîne contrôlée dans lesquelles intervient le facteur partagé $q$ vaut $q / \Pr(\text{échec, chaîne contrôlée})$.

### Sensibilité, prise en compte, échappement et risque résiduel {#sec:annexe-a-echappement}

Dans le modèle du contrôleur du @sec:ch09 (@sec:ch09-risque-echappement) et du @sec:ch16 (@sec:ch16-taux-echappement), un producteur émet des affirmations fausses au taux d’erreur $P(E)$. Une fraction $c \in [0, 1]$ des causes d’erreur du producteur est partagée avec le contrôleur (toujours manquée) ; sur la fraction complémentaire $1 - c$, le contrôleur commet un oubli indépendant avec probabilité $m \in [0, 1]$. Sa sensibilité effective vaut (@eq:ch09-sensibilite) :

$$s = (1 - c)(1 - m).$$

Lorsque l’affirmation est juste, le contrôleur déclenche une fausse alerte avec probabilité $f$. La proportion d’alertes suivies d’un examen effectif est la prise en compte $u \in [0, 1]$ : sous examen systématique de chaque alerte, $u = 1$ ; sous l’hypothèse comportementale d’appariement des probabilités (@sec:ch09-fausses-alertes), $u = \mathrm{VPP}$. La probabilité d’échappement et le risque résiduel (probabilité qu’une affirmation fausse atteigne l’action sans être arrêtée) s’écrivent (@eq:ch09-echappement, @eq:ch09-risque) :

$$\Pr(\text{échappement}) = 1 - s\,u, \qquad R = P(E)\,(1 - s\,u).$$

Même sous examen systématique de toutes les alertes ($u = 1$), l’échappement ne descend pas au-dessous du plancher $1 - s = c + (1 - c)m \ge c$.

### Réinterrogatoire et sévérité sur cinq tirages {#sec:annexe-a-reinterrogatoire}

Lorsqu’on interroge $k$ fois indépendamment une distribution générative qui attribue les probabilités $p_1, \dots, p_r$ aux réponses possibles et que l’on déclenche une alerte dès que les $k$ réponses ne sont pas toutes identiques (@sec:ch12-calibration-longue-traine), en notant $J$ l’ensemble des réponses justes (de probabilité totale $p_{\text{juste}} = \sum_{i \in J} p_i$) et $F$ l’ensemble des réponses fausses ($p_{\text{faux}} = \sum_{j \in F} p_j = 1 - p_{\text{juste}}$), la sévérité du contrôle par concordance et son taux d’alerte à tort sur une première réponse juste valent :

$$\text{sévérité} = \Pr(\text{au moins un désaccord} \mid \text{1re réponse fausse}) = 1 - \frac{\sum_{j \in F} p_j^k}{p_{\text{faux}}},$$

$$\Pr(\text{alerte} \mid \text{1re réponse juste}) = 1 - \frac{\sum_{i \in J} p_i^k}{p_{\text{juste}}}.$$

La sévérité est proche de $1$ lorsque l’erreur se disperse sur plusieurs réponses fausses peu probables (erreurs où le modèle devine), mais chute dès qu’une erreur unique concentre la masse de probabilité (idée reçue ou biais constant).

## Contrats logiciels et triplets de Hoare {#sec:annexe-a-hoare}

Pour un composant spécifié $C$, une précondition $P$ et une postcondition $Q$ (@sec:ch10-boite-outils), le triplet de Hoare :

$$\{P\}\; C \;\{Q\}$$

affirme que si l’état d’entrée vérifie l’assertion $P$ avant l’exécution de $C$, alors l’état de sortie vérifie l’assertion $Q$ après son exécution (en correction partielle : sous réserve que $C$ se termine ; en correction totale : avec terminaison garantie). La composition séquentielle repose sur l’enchaînement des garanties à l’interface :

$$\frac{\{P\}\; C_1 \;\{R\} \qquad \{R\}\; C_2 \;\{Q\}}{\{P\}\; C_1 \,;\, C_2 \;\{Q\}}.$$

Ce mécanisme permet la vérification en amont : établir la conformité de $C$ à son contrat $\{P\}\; C \;\{Q\}$ une fois pour toutes couvre l’ensemble de ses exécutions futures satisfaisant $P$, et localise toute défaillance à l’adresse du composant dont la postcondition est violée alors que sa précondition était remplie.

## Signalisation coûteuse et équilibre mélangeant {#sec:annexe-a-signalisation}

En économie de l’information asymétrique (@sec:ch15-effondrement-signal), un attribut observable (tel que la tenue formelle d’un texte ou d’un code) ne sépare les productions de haute qualité (type $H$) des productions non contrôlées (type $B$) que si le coût $c(\text{signal} \mid \text{type})$ d’émission de ce signal vérifie la condition de croisement de Spence :

$$c(\text{signal} \mid H) < \text{bénéfice du crédit accordé} < c(\text{signal} \mid B).$$

Lorsque l’automatisation abaisse le coût de mise en forme $c(\text{signal} \mid B)$ à près de zéro tandis que le coût du contrôle de fond reste élevé, tous les producteurs émettent le même signal formel : l’équilibre séparateur fait place à un équilibre mélangeant (au sens d’Akerlof), dans lequel la forme cesse de constituer un comparateur sévère de la solidité du fond.
