# Boîte à outils : logique, conditionnement, probabilité {#sec:ch01}

Ce chapitre ouvre la @sec:partie-1 immédiatement après la vue d’ensemble du @sec:ch00. Il ne suppose aucun prérequis issu des autres chapitres et peut être lu directement au fil de l’ouvrage ou selon les parcours thématiques indiqués au @sec:ch00-parcours. Il ne constitue ni un cours de logique ni un traité de probabilités : il rassemble de manière unifiée les six instruments formels utilisés dans la suite du livre, chacun introduit par la question pratique à laquelle il répond et formulé dans le vocabulaire exact des chapitres qui viennent.

## Déduction et induction {#sec:ch01-modes-inference}

*Question : que garantit au juste un raisonnement, et à quelles conditions cette garantie tient-elle ?*

Lorsque l’on tire une conclusion à partir d’informations disponibles, deux grands modes d’inférence se partagent l’usage courant et scientifique : la **déduction**, qui est une inférence nécessaire à partir de prémisses posées au départ, et l’**induction**, qui est une généralisation à partir de régularités observées. L’une et l’autre apportent une forme de rigueur bien réelle, mais aucune des deux ne garantit ses conclusions sans condition : l’une comme l’autre ne valent que « pourvu que » leurs conditions d’application soient remplies.

Dans un raisonnement déductif, la conclusion découle nécessairement des prémisses en vertu des règles de la logique : il est impossible que toutes les prémisses soient vraies et que la conclusion soit fausse. On confond pourtant souvent deux propriétés distinctes d’un tel raisonnement : sa *validité* logique et sa *solidité* matérielle. Un argument est valide lorsque son enchaînement ne souffre aucune faille ; il est solide lorsqu’il est à la fois valide et appuyé sur des prémisses effectivement vraies dans le monde. La distinction importe au plus haut point, car la logique protège la validité de la déduction sans jamais pouvoir vérifier la vérité de ses points de départ.

Prenons un raisonnement parfaitement valide dans sa forme : « Tout métal pur conduit le courant électrique ; or ce barreau est en métal pur ; donc ce barreau conduit le courant électrique. » La conclusion suit impeccablement. Imaginons maintenant un raisonnement tout aussi rigoureux en apparence dans un bureau d’études : « Toute poutre en acier homogène dont la contrainte calculée reste sous la limite élastique résiste à la charge ; or la contrainte calculée sur cette poutre reste inférieure à cette limite ; donc cette poutre résistera. » Si la poutre réelle comporte une fissure non répertoriée ou si son alliage s’écarte de l’hypothèse d’homogénéité, l’enchaînement logique demeure irréprochable, mais la prémisse d’homogénéité est fausse et la conclusion peut s’effondrer. La déduction ne crée pas la vérité : elle la *transmet* des prémisses vers la conclusion, pourvu que les définitions, les mesures et les idéalisations de départ correspondent effectivement à la situation visée.

L’induction répond à la question inverse : comment passer d’un nombre fini de cas observés à une règle générale ou à une prévision sur un cas encore jamais vu ? Un laboratoire mesure trois fois la température d’ébullition de l’eau et obtient trois fois 100 °C ; un service hospitalier observe l’efficacité d’un traitement sur cinq cents patients ; un ingénieur relève mille heures de fonctionnement sans panne sur un banc d’essai. De ces observations, l’induction tire une régularité générale. Mais à la différence de la déduction, le passage des cas observés au cas suivant n’est jamais logiquement nécessaire : aucune contradiction logique n’empêche que la mille et unième heure rompe avec les mille précédentes si une circonstance nouvelle intervient.

David Hume a formulé dès le XVIII^e^ siècle la difficulté fondamentale qui s’attache à ce passage [@hume1748] : qu’est-ce qui justifie d’étendre au futur ou à l’inobservé les régularités constatées jusqu’ici ? Tenter de justifier l’induction en faisant valoir que « cette manière de généraliser a toujours bien fonctionné par le passé » reviendrait à employer l’induction pour prouver l’induction, c’est-à-dire à tourner en rond. Nous retrouverons ce problème de l’induction et ses prolongements contemporains au @sec:ch07. Pour l’heure, retenons l’essentiel commun aux deux modes d’inférence :

- la **déduction** garantit sa conclusion *pourvu que* les prémisses et les idéalisations retenues soient exactes ;
- l’**induction** prolonge légitimement les régularités observées *pourvu que* les cas nouveaux ressemblent aux cas observés sous les rapports qui gouvernent le phénomène.

Dans les deux cas, la rigueur interne du calcul ne certifie jamais par elle-même que ces clauses « pourvu que » sont satisfaites.

## Règles conditionnelles et conditions tues {#sec:ch01-regles-conditionnelles}

*Question : comment noter une règle utile lorsque la liste des conditions qui la font tenir ne peut pas être close ?*

En logique élémentaire, une règle conditionnelle s’écrit sous la forme d’une implication directe : « si $A$, alors $B$ », notée $A \rightarrow B$, ou $A_1 \cap A_2 \rightarrow B$ lorsque plusieurs conditions explicites doivent être réunies conjointement. Tant que l’on demeure dans un domaine clos — l’arithmétique, un jeu d’échecs, un circuit logique idéal —, il est possible d’énoncer toutes les hypothèses nécessaires dans $A$ sans rien laisser dans l’ombre.

Il en va tout autrement dès que la règle porte sur le monde matériel. Considérons un premier aperçu d’un exemple qui reviendra sous plusieurs angles dans la suite de l’ouvrage (en particulier au @sec:ch02 et au @sec:ch05) : l’ébullition de l’eau. Chacun connaît l’énoncé court : « si de l’eau est portée à 100 °C, alors elle bout ». Trois mesures rapides au laboratoire semblent le confirmer. Pourtant, l’expérience échoue dès que l’eau est fortement salée, qu’un couvercle étanche élève la pression dans le récipient, ou au contraire que l’on opère en haute altitude où l’ébullition survient bien au-dessous de 100 °C. On peut certes rallonger l’énoncé pour mentionner la pureté de l’eau et la pression atmosphérique normale ; mais même ainsi enrichie, la règle continue de passer sous silence l’absence de surfusion dans un récipient très lisse, la nature des gaz dissous ou l’uniformité de la mesure thermométrique.

Pour rendre visible ce caractère ouvert de toute règle empirique, technique ou décisionnelle, nous écrirons dans cet ouvrage les règles pratiques sous la forme suivante :

$$A \cap (\dots) \rightarrow B$$ {#eq:ch01-regle}

Dans cette écriture, $A$ rassemble les conditions explicitement énoncées, le symbole $\cap$ note la conjonction logique (« et »), $B$ désigne la conséquence attendue, et la parenthèse $(\dots)$ représente l’arrière-plan non énoncé — l’ensemble indéfini des circonstances habituelles que l’on tient tacitement pour acquises lorsque l’on applique la règle.

Cette parenthèse $(\dots)$ ne signale pas une négligence que des auteurs plus scrupuleux pourraient faire disparaître une fois pour toutes. Chercher à tout faire entrer dans $A$ rendrait n’importe quelle règle impraticable par sa longueur et fragile à la moindre exception imprévue ; à l’inverse, n’y presque rien mettre laisse dans l’ombre des conditions décisives. Le @sec:ch02 analysera en détail ce partage entre ce que l’on énonce dans $A$ et ce que l’on tait dans $(\dots)$. Mais un besoin immédiat se fait déjà sentir ici : dès que nous ignorons si toutes les circonstances tapies dans $(\dots)$ sont réunies dans le cas présent, une logique binaire à deux valeurs (« vrai » ou « faux ») ne suffit plus à guider l’esprit. Nous avons besoin d’un instrument pour doser le poids accordé aux différentes issues possibles : c’est le rôle du calcul des probabilités.

## Probabilité : règles et lectures {#sec:ch01-probabilite}

*Question : comment attribuer des poids cohérents à des issues incertaines, et que signifient au juste ces nombres ?*

Soit $\Pr(A)$ la probabilité attribuée à un événement ou à une proposition $A$. Quel que soit le sens philosophique ou pratique que l’on donne à ce nombre, le calcul des probabilités impose avant tout des règles de cohérence interne. Toute probabilité est comprise entre $0$ et $1$ ; l’événement certain qui regroupe toutes les issues envisagées reçoit le poids $1$, et l’événement impossible le poids $0$. Lorsque deux événements s’excluent mutuellement — ils ne peuvent pas se réaliser ensemble —, la probabilité que l’un ou l’autre survienne est égale à la somme de leurs probabilités individuelles. En particulier, comme un événement $A$ et sa négation $\bar{A}$ s’excluent tout en couvrant ensemble toutes les issues possibles, leurs probabilités totalisent $1$, soit $\Pr(\bar{A}) = 1 - \Pr(A)$.

::: {.formel titre="Axiomes du calcul des probabilités"}
On considère un ensemble $\Omega$ regroupant toutes les issues élémentaires retenues dans la description du problème, et une famille de sous-ensembles de $\Omega$ appelés événements (contenant $\Omega$, stable par passage au complémentaire et par réunion dénombrable). Une mesure de probabilité $\Pr(\cdot)$ associe à chaque événement un nombre réel vérifiant les trois axiomes de Kolmogorov :

1. **Positivité :** pour tout événement $A$, $\Pr(A) \ge 0$.
2. **Normalisation :** pour l’événement certain, $\Pr(\Omega) = 1$.
3. **Additivité :** pour deux événements incompatibles ($A \cap B = \emptyset$), $\Pr(A \cup B) = \Pr(A) + \Pr(B)$ ; plus généralement, pour une suite dénombrable d’événements deux à deux incompatibles $A_1, A_2, \dots$, $\Pr\bigl(\bigcup_{i \ge 1} A_i\bigr) = \sum_{i \ge 1} \Pr(A_i)$.

De ces trois axiomes découlent aussitôt les propriétés usuelles du calcul : $\Pr(\emptyset) = 0$, $0 \le \Pr(A) \le 1$, $\Pr(\bar{A}) = 1 - \Pr(A)$, ainsi que la formule générale de la réunion pour deux événements quelconques, $\Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A \cap B)$.
:::

Ces axiomes règlent la syntaxe du calcul sans en fixer l’interprétation. Deux grands systèmes de lecture associent une signification concrète aux mêmes formules :

- **La lecture fréquentiste.** Dans cette perspective, $\Pr(A)$ désigne la fréquence limite avec laquelle l’événement $A$ se réalise lorsqu’une même expérience est répétée un grand nombre de fois dans des conditions jugées identiques. Cette lecture est naturelle pour des tirages en série, des pièces usinées sur une ligne stable ou des lancers de dé ; mais elle devient muette ou artificielle dès que l’on s’interroge sur un événement unique qui ne se répétera pas à l’identique — la réussite d’une intervention chirurgicale demain matin, la tenue d’un ouvrage lors d’une crue exceptionnelle, le lancement d’une sonde interplanétaire.
- **La lecture comme jugement.** Dans cette seconde perspective — développée notamment par de Finetti, Jaynes et Lindley [@definetti1974; @jaynes2003; @lindley2006] —, $\Pr(A)$ mesure le degré de plausibilité ou de confiance qu’un raisonneur rationnel accorde à la proposition $A$ compte tenu de l’information et des hypothèses dont il dispose. Le nombre ne décrit alors pas une propriété physique isolée de l’objet (une soudure n’est pas « cassable à 4 % » en elle-même : elle est fissurée ou intacte), mais l’état de connaissance et de jugement de celui qui l’évalue. Deux analystes qui retiennent des informations ou des hypothèses différentes peuvent dès lors énoncer des probabilités distinctes sans qu’aucun ne viole les axiomes.

Cet ouvrage adopte la lecture comme jugement pour raisonner et décider, sans jamais renier le rôle des fréquences. Pourquoi retenir le jugement comme fil directeur ? Parce que dans l’action réelle, nous devons presque toujours évaluer un risque ou trancher une option *avant* que le monde n’ait répondu, y compris dans des situations qui ne constituent pas des tirages répétés à l’identique. Pourquoi ne pas abandonner les fréquences pour autant ? D’abord parce que, lorsque nous disposons de fréquences stables sur des cas comparables, elles nourrissent directement notre jugement initial. Ensuite et surtout parce que, sur des prévisions répétées, les fréquences observées *a posteriori* restent le banc d’essai qui sanctionne la justesse de nos jugements : vérifier si des événements annoncés à « 70 % » surviennent effectivement environ sept fois sur dix — ce que le @sec:ch03 étudiera sous le nom de calibration — exige de confronter des jugements de probabilité à des fréquences recueillies dans la durée.

## Probabilité conditionnelle et probabilité totale {#sec:ch01-probabilite-conditionnelle}

*Question : comment réajuster le poids d’un événement $B$ lorsque l’on suppose ou apprend qu’une condition $A$ est réalisée, et comment recomposer la probabilité globale d’un phénomène à partir de plusieurs scénarios ?*

La probabilité conditionnelle de $B$ sachant $A$, notée $\Pr(B \mid A)$ et définie dès que $\Pr(A) > 0$, s’écrit :

$$\Pr(B \mid A) = \frac{\Pr(A \cap B)}{\Pr(A)}$$ {#eq:ch01-cond}

Sous cette formule algébrique très simple se cache une image géométrique qui éclaire tout le reste de l’ouvrage. Si l’on se représente $\Omega$ comme l’ensemble des situations ou des mondes compatibles avec ce que l’on envisage, conditionner par $A$ consiste à *restreindre* cet univers aux seuls mondes où $A$ est vérifié, en écartant tous les autres, puis à mesurer dans cette population réduite la part des mondes où $B$ est vérifié lui aussi. Diviser $\Pr(A \cap B)$ par $\Pr(A)$ ne fait rien d’autre que renormaliser les poids sur $A$ de sorte que l’ensemble $A$ devienne le nouvel univers de total $1$.

Cette lecture relie directement la probabilité conditionnelle aux règles à conditions tues de l’@eq:ch01-regle. Lorsqu’une règle affirme $A \cap (\dots) \rightarrow B$, la quantité $\Pr(B \mid A)$ représente précisément la part des situations vérifiant les conditions explicites $A$ dans lesquelles l’arrière-plan tu $(\dots)$ permet à la conséquence $B$ de se réaliser. Le @sec:ch03 reprendra cette image des mondes possibles pour en faire l’armature même du jugement probabiliste.

De l’@eq:ch01-cond découle aussitôt la règle du produit : la probabilité que $A$ et $B$ se réalisent conjointement vaut $\Pr(A \cap B) = \Pr(A)\,\Pr(B \mid A)$. Ce produit offre au passage une définition nette de l’indépendance au sens du calcul des probabilités : deux événements $A$ et $B$ sont probabilistement indépendants lorsque savoir que $A$ est réalisé ne modifie pas la part des mondes où $B$ l’est aussi, autrement dit lorsque $\Pr(B \mid A) = \Pr(B)$, ou de façon équivalente $\Pr(A \cap B) = \Pr(A)\,\Pr(B)$. Dans tous les autres cas, connaître $A$ déplace la probabilité de $B$.

Réciproquement, il est fréquent de connaître plus facilement le comportement d’un événement $B$ à l’intérieur de chaque grand scénario possible que directement dans l’absolu. Imaginons que l’on veuille évaluer la probabilité d’un retard de livraison $B$ selon deux conditions météorologiques exclusives qui recouvrent toutes les possibilités : soit un brouillard dense ($H$), soit un temps dégagé ($\bar{H}$). Si l’on sait estimer la probabilité du retard dans chacun des deux régimes, $\Pr(B \mid H)$ et $\Pr(B \mid \bar{H})$, ainsi que le poids attribué à chaque régime météorologique, $\Pr(H)$ et $\Pr(\bar{H})$, la probabilité globale de retard est simplement la moyenne pondérée des deux :

$$\Pr(B) = \Pr(B \mid H)\,\Pr(H) + \Pr(B \mid \bar{H})\,\Pr(\bar{H}).$$

Par exemple, si le brouillard survient un quart des matins ($\Pr(H) = 25\,\%$) et entraîne alors un retard dans $40\,\%$ des cas, tandis que par temps dégagé ($\Pr(\bar{H}) = 75\,\%$) le retard ne survient que dans $4\,\%$ des cas, la probabilité globale de retard s’établit à $0{,}40 \times 0{,}25 + 0{,}04 \times 0{,}75 = 0{,}10 + 0{,}03 = 13\,\%$. Plus généralement, si $H_1, H_2, \dots, H_k$ forment une partition de $\Omega$ — c’est-à-dire des hypothèses deux à deux incompatibles dont la réunion recouvre tout l’univers ($\sum_{i=1}^k \Pr(H_i) = 1$) —, la **formule des probabilités totales** exprime la probabilité de $B$ par décomposition sur cette partition :

$$\Pr(B) = \sum_{i=1}^{k} \Pr(B \mid H_i)\,\Pr(H_i)$$ {#eq:ch01-totale}

Cette équation joue un rôle conceptuel majeur dès le @sec:ch02 : les probabilités conditionnelles $\Pr(B \mid H_i)$ condensent ce que le modèle décrit à l’intérieur de chaque scénario $H_i$, tandis que les poids $\Pr(H_i)$ portent le jugement sur l’importance relative des scénarios retenus.

## Réviser un jugement : la règle de Bayes sous forme de cotes {#sec:ch01-bayes}

*Question : lorsque l’on observe un résultat nouveau $E$, dans quelle proportion ce constat doit-il déplacer la plausibilité relative d’une hypothèse $H$ par rapport à son contraire $\bar{H}$ ?*

Dans la pratique scientifique et technique, les modèles prédisent généralement le sens direct : étant donné un état supposé du système $H$ (un défaut mécanique, une panne de capteur, une hypothèse climatique), quelle est la probabilité d’observer tel indice $E$ ? C’est $\Pr(E \mid H)$. Mais celui qui examine les données ou reçoit un rapport de mesure se pose la question inverse : sachant que l’indice $E$ vient d’être observé, quelle confiance accorder désormais à $H$ ? C’est $\Pr(H \mid E)$. Confondre ces deux probabilités conditionnelles — prendre $\Pr(E \mid H)$ pour $\Pr(H \mid E)$ — constitue l’une des erreurs de raisonnement les plus répandues. La règle de Bayes assure le passage rigoureux de l’une à l’autre.

Plutôt que d’écrire cette règle directement en probabilités — où l’apparition du dénominateur $\Pr(E)$ masque l’intuition du mécanisme de révision —, il est beaucoup plus parlant de l’exprimer en *cotes*. Pour une hypothèse $H$ et son contraire $\bar{H}$ (avec $\Pr(\bar{H}) > 0$), la cote de $H$ est le rapport de sa probabilité à celle de l’hypothèse opposée :

$$\text{cote}(H) = \frac{\Pr(H)}{\Pr(\bar{H})} = \frac{\Pr(H)}{1 - \Pr(H)}, \qquad \text{et inversement } \Pr(H) = \frac{\text{cote}(H)}{1 + \text{cote}(H)}.$$

Une probabilité de $20\,\%$ correspond ainsi à une cote de $0{,}20 / 0{,}80 = 0{,}25$ (une chance contre quatre) ; une probabilité de $50\,\%$ correspond à une cote de $1$ (à égalité).

Mesurons maintenant la force probante de l’observation $E$ entre les deux hypothèses. On appelle **rapport de vraisemblance** de l’observation $E$ pour l’hypothèse $H$ contre $\bar{H}$ le quotient des probabilités de cette observation sous chacune des deux hypothèses :

$$\Lambda(E) = \frac{\Pr(E \mid H)}{\Pr(E \mid \bar{H})}.$$

Ce rapport exprime combien de fois l’observation $E$ est plus vraisemblable si $H$ est vraie que si $\bar{H}$ est vraie. Si $\Lambda(E) > 1$, l’observation plaide en faveur de $H$ ; si $\Lambda(E) < 1$, elle plaide en faveur de $\bar{H}$ ; si $\Lambda(E) = 1$, l’observation possède exactement la même probabilité sous les deux hypothèses et ne fournit aucune prise pour les départager.

La règle de Bayes prend alors une forme multiplicative d’une clarté immédiate :

$$\text{cote}(H \mid E) = \text{cote}(H) \times \frac{\Pr(E \mid H)}{\Pr(E \mid \bar{H})}$$ {#eq:ch01-bayes-cotes}

En mots : la cote *a posteriori* est égale à la cote *a priori* multipliée par le rapport de vraisemblance. Cette écriture met en évidence deux enseignements décisifs. Premièrement, une observation ne fixe jamais à elle seule la probabilité finale : elle *multiplie* le rapport de plausibilité dont on partait. Deuxièmement, si plusieurs observations successives $E_1, E_2$ sont indépendantes conditionnellement à l’état réel ($H$ et $\bar{H}$), il suffit de multiplier successivement la cote par $\Lambda(E_1)$, puis par $\Lambda(E_2)$.

::: {.formel titre="Dérivation de la règle de Bayes sous forme de cotes"}
Soient deux hypothèses incompatibles $H_1$ et $H_2$, et une observation $E$ telle que $\Pr(E) > 0$, $\Pr(H_2) > 0$ et $\Pr(E \mid H_2) > 0$. En appliquant l’@eq:ch01-cond à $H_1$ et à $H_2$ sachant $E$, on obtient :

$$\Pr(H_1 \mid E) = \frac{\Pr(H_1 \cap E)}{\Pr(E)} = \frac{\Pr(E \mid H_1)\,\Pr(H_1)}{\Pr(E)},$$

$$\Pr(H_2 \mid E) = \frac{\Pr(H_2 \cap E)}{\Pr(E)} = \frac{\Pr(E \mid H_2)\,\Pr(H_2)}{\Pr(E)}.$$

En divisant la première égalité par la seconde, le facteur commun $\Pr(E)$ se simplifie :

$$\frac{\Pr(H_1 \mid E)}{\Pr(H_2 \mid E)} = \frac{\Pr(H_1)}{\Pr(H_2)} \times \frac{\Pr(E \mid H_1)}{\Pr(E \mid H_2)}.$$

En posant $H_1 = H$ et $H_2 = \bar{H}$, on retrouve exactement l’@eq:ch01-bayes-cotes. Lorsqu’on souhaite retrouver la probabilité *a posteriori* $\Pr(H \mid E)$ directement sans passer par la cote, la formule des probabilités totales (@eq:ch01-totale) donne le dénominateur $\Pr(E) = \Pr(E \mid H)\,\Pr(H) + \Pr(E \mid \bar{H})\,\Pr(\bar{H})$, d’où :

$$\Pr(H \mid E) = \frac{\Pr(E \mid H)\,\Pr(H)}{\Pr(E \mid H)\,\Pr(H) + \Pr(E \mid \bar{H})\,\Pr(\bar{H})}.$$

Enfin, pour deux observations $E_1$ et $E_2$ supposées *conditionnellement indépendantes* sous chacune des hypothèses — c’est-à-dire vérifiant $\Pr(E_1 \cap E_2 \mid H) = \Pr(E_1 \mid H)\,\Pr(E_2 \mid H)$ et de même sous $\bar{H}$ —, le rapport de vraisemblance conjoint se factorise : $\Lambda(E_1 \cap E_2) = \Lambda(E_1)\,\Lambda(E_2)$.
:::

Mettons cette formule en œuvre sur un exemple chiffré élémentaire, afin d’observer comment le jugement initial et la force probante du test se combinent.

::: {.exemple-quantitatif titre="Mise à jour par cotes lors d’un contrôle par ultrasons"}
**Mise en place.** Un ingénieur contrôle par ultrasons des soudures critiques sur une canalisation industrielle. Il cherche à évaluer l’hypothèse $D$ (« la soudure présente un défaut interne ») face à $\bar{D}$ (« la soudure est saine »). Les caractéristiques de la sonde sur des pièces d’étalonnage sont les suivantes (les chiffres qui suivent sont purement illustratifs) : lorsque la soudure comporte réellement un défaut ($D$), la sonde émet un signal anormal $T^+$ dans 75 % des cas et reste normale ($T^-$) dans 25 % des cas ; lorsque la soudure est saine ($\bar{D}$), une irrégularité géométrique bénigne déclenche tout de même un signal $T^+$ dans 15 % des cas, tandis que le signal reste normal ($T^-$) dans 85 % des cas.

Le rapport de vraisemblance d’un signal anormal vaut donc $\Lambda(T^+) = 0{,}75 / 0{,}15 = 5$, et celui d’un signal normal vaut $\Lambda(T^-) = 0{,}25 / 0{,}85 = 5/17 \approx 0{,}294$. Nous comparons quatre situations portant sur deux jugements initiaux contrastés avant la mesure : un lot courant où la probabilité *a priori* de défaut est jugée faible (4 %), et une zone suspecte ayant subi des contraintes inhabituelles où cette probabilité initiale est estimée à 20 %.

![Probabilité de défaut avant et après la mesure ultrasonore selon le jugement initial et les signaux observés.](figures/ch01-bayes-cotes.pdf){#fig:ch01-bayes-cotes width=88%}

**Calcul.**

::: {.inclure fichier="tableaux/ch01-bayes-cotes.md"}
:::

En détaillant le calcul sous forme de cotes :

- *Lot courant après un signal $T^+$* : la probabilité *a priori* de 4 % donne une cote *a priori* de $0{,}04 / 0{,}96 = 1/24 \approx 0{,}0417$. Multipliée par 5, elle devient $5/24 \approx 0{,}208$, ce qui correspond à une probabilité *a posteriori* de $(5/24) / (1 + 5/24) = 5/29 \approx 17{,}2\,\%$.
- *Zone suspecte après un signal $T^+$* : la probabilité *a priori* de 20 % correspond à une cote *a priori* de $0{,}20 / 0{,}80 = 0{,}25$. Multipliée par 5, elle atteint 1,25, soit une probabilité *a posteriori* de $1{,}25 / 2{,}25 = 5/9 \approx 55{,}6\,\%$.
- *Zone suspecte après un signal $T^-$* : la même cote *a priori* de 0,25 est multipliée par $5/17 \approx 0{,}294$, tombant à $5/68 \approx 0{,}0735$, soit une probabilité *a posteriori* de $5/73 \approx 6{,}85\,\%$.
- *Zone suspecte après deux signaux $T^+$ indépendants* : si une seconde sonde opérant indépendamment confirme $T^+$, la cote de 0,25 est multipliée par $5 \times 5 = 25$ pour atteindre 6,25, ce qui porte la probabilité *a posteriori* à $6{,}25 / 7{,}25 = 25/29 \approx 86{,}2\,\%$.

**Lecture.** Cet exemple illustre trois mécanismes essentiels de la mise à jour bayésienne. D’abord, une même observation $T^+$ dotée d’un rapport de vraisemblance de 5 ne produit pas la même conclusion selon le point de départ : dans la zone suspecte (20 %), elle fait basculer le défaut au-delà d’une chance sur deux (55,6 %), alors que dans le lot courant (4 %), le défaut reste minoritaire (17,2 %) après la première alerte. Ensuite, le poids d’un signal normal $T^-$ (0,294) n’est pas l’inverse arithmétique exact de celui d’un signal anormal ($1/5 = 0{,}20$) : c’est toujours le rapport des probabilités de l’issue *effectivement observée* sous les deux hypothèses qui gouverne la révision. Enfin, ce résultat repose entièrement sur l’hypothèse que les deux mesures successives sont conditionnellement indépendantes : si la seconde sonde lit simplement le même écho géométrique bénin que la première, multiplier une seconde fois par 5 compterait deux fois la même information.
:::

## Mesurer la qualité d’une prévision : la surprise {#sec:ch01-score-logarithmique}

*Question : comment évaluer après coup une prévision probabiliste lorsque le monde vient de trancher en faveur d’une seule issue ?*

Si un météorologue annonce « il pleuvra demain » et qu’il fait grand soleil, l’énoncé binaire est simplement faux. Mais s’il annonce « 20 % de chances de gel cette nuit », une seule nuit gélive ne prouve pas qu’il avait tort, pas plus qu’une nuit douce ne prouve qu’il avait raison. Pour comparer honnêtement deux prévisions probabilistes face à une issue observée, il faut donc une mesure continue qui évalue à quel point l’événement réel a pris chaque prévision au dépourvu.

C’est le rôle du **score logarithmique**, défini comme la surprise d’une issue sous la prévision qui lui attribuait la probabilité $p = \Pr(\text{issue})$ :

$$S(p) = -\ln p$$ {#eq:ch01-score-log}

Plus la probabilité $p$ accordée à l’issue qui s’est effectivement produite est faible, plus le score logarithmique $S(p)$ est élevé — autrement dit, plus grande est la surprise. Si l’issue avait reçu la probabilité $1$, la surprise est nulle ($-\ln 1 = 0$). À l’inverse, si une issue jugée très improbable ($p$ proche de $0$) finit par se réaliser, la pénalité croît rapidement, et elle devient infinie si la prévision avait posé $p = 0$. Le score logarithmique traduit ainsi une règle d’hygiène intellectuelle élémentaire : n’attribuer une probabilité nulle à un événement que s’il est rigoureusement impossible.

Prenons une illustration simple : deux prévisionnistes évaluent le risque de gel nocturne sur un verger. Le premier estime ce risque à $20\,\%$, le second à $2\,\%$. Si le gel survient effectivement pendant la nuit, le premier subit une surprise de $-\ln(0{,}20) \approx 1{,}61$, tandis que le second encaisse $-\ln(0{,}02) \approx 3{,}91$. La différence de leurs surprises vaut $3{,}91 - 1{,}61 = 2{,}30$, soit exactement $\ln(10)$ : elle correspond à un rapport de vraisemblance de $0{,}20 / 0{,}02 = 10$ en faveur de la première prévision. Si la nuit reste au contraire sans gel, la première prévision avait accordé $80\,\%$ à cette issue (surprise $-\ln 0{,}80 \approx 0{,}223$) et la seconde $98\,\%$ (surprise $-\ln 0{,}98 \approx 0{,}020$) ; l’écart est infime et le rapport de vraisemblance, égal à $0{,}80 / 0{,}98 \approx 0{,}816$, ne tranche guère entre elles.

On aperçoit ainsi le lien exact entre le score logarithmique et le rapport de vraisemblance : *soustraire deux scores logarithmiques revient à prendre le logarithme du rapport de vraisemblance* des deux prévisions sur l’issue observée. Autrement dit, le rapport de vraisemblance est l’exponentielle de l’écart de surprise entre les deux prévisions. Ce double outil — la surprise mesurée par $-\ln \Pr(\text{issue})$ et l’écart traduit en rapport de vraisemblance — servira directement au @sec:ch03 lorsque nous confronterons les estimations de deux navigateurs sur une même course de voiliers et examinerons pourquoi une issue isolée ne suffit presque jamais à départager durablement deux prévisionnistes.

::: {.formel titre="Score logarithmique et rapport de vraisemblance"}
Pour toute issue ayant reçu une probabilité $p \in (0, 1]$, le score logarithmique $S(p) = -\ln p$ est positif ou nul ($S(1) = 0$) et strictement décroissant en $p$.

1. **Additivité sur des épreuves indépendantes.** Si deux issues successives $E_1$ et $E_2$ sont jugées indépendantes et reçoivent les probabilités $p_1$ et $p_2$, la probabilité conjointe est $p_1 p_2$, et la surprise totale est la somme des surprises individuelles :
   $$S(p_1 p_2) = -\ln(p_1 p_2) = -\ln p_1 - \ln p_2 = S(p_1) + S(p_2).$$

2. **Lien avec le rapport de vraisemblance.** Soient deux modèles ou prévisionnistes attribuant à l’issue observée les probabilités $p_1 = \Pr_1(\text{issue})$ et $p_2 = \Pr_2(\text{issue})$ (strictement positives). La différence de leurs surprises vaut :
   $$S(p_2) - S(p_1) = -\ln p_2 - (-\ln p_1) = \ln\left(\frac{p_1}{p_2}\right) = \ln \Lambda,$$ {#eq:ch01-surprise-vraisemblance}
   où $\Lambda = p_1 / p_2$ est le rapport de vraisemblance de l’issue observée sous la première prévision contre la seconde, soit réciproquement $\Lambda = \exp\bigl(S(p_2) - S(p_1)\bigr)$.

3. **Effet d’une probabilité nulle.** Poser $p = 0$ sur une issue qui vient à se produire donne $S(0) = +\infty$. Avec la règle de Bayes (@eq:ch01-bayes-cotes), une probabilité *a priori* nulle correspond à une cote nulle que nul rapport de vraisemblance fini ne pourra jamais relever au-dessus de zéro : c’est pourquoi la cohérence probabiliste interdit d’exclure par un zéro strict toute éventualité qui n’est pas logiquement impossible.
:::

## Points clés {.points-cles}

- La déduction transmet nécessairement la vérité de prémisses posées au départ et l’induction généralise à partir de régularités observées, mais toutes deux ne livrent leurs conclusions que « pourvu que » leurs conditions d’application — exactitude des prémisses ou ressemblance suffisante des contextes — soient satisfaites.
- Toute règle empirique ou technique utilisable cache un arrière-plan ouvert de conditions sous-entendues, ce que l’on note $A \cap (\dots) \rightarrow B$ ; lorsque l’état de $(\dots)$ reste incertain, le calcul des probabilités prend le relais de la logique binaire.
- Les axiomes des probabilités fixent des règles de cohérence compatibles avec deux interprétations : cet ouvrage raisonne selon la lecture comme jugement — le poids accordé aux éventualités compte tenu de ce que l’on sait — tout en conservant les fréquences observées pour éprouver les prévisions dans la durée.
- La probabilité conditionnelle $\Pr(B \mid A) = \Pr(A \cap B) / \Pr(A)$ se lit comme la part des mondes où $A$ est vérifié dans lesquels $B$ l’est aussi, tandis que la formule des probabilités totales recompose $\Pr(B)$ à partir de scénarios disjoints pondérés par leur plausibilité.
- Sous forme de cotes, la règle de Bayes multiplie simplement la cote *a priori* d’une hypothèse par le rapport de vraisemblance $\Pr(E \mid H) / \Pr(E \mid \bar{H})$ de l’observation : une donnée nouvelle révise un jugement initial sans jamais le remplacer à elle seule.
- Le score logarithmique $-\ln \Pr(\text{issue})$ mesure la surprise d’un résultat face à une prévision ; la différence des surprises de deux prévisions égale le logarithme de leur rapport de vraisemblance sur l’issue observée.
