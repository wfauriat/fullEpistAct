# Journal de la passe de style — `00-avant-propos`

- Appliqué le 2026-11-20T13:19:04 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 8 · appliquées : 4 · rejetées par le juge : 4 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (4)

### 001 — § « Pourquoi ce livre » (ligne 9) — phrase-longue

Avant :

> En déplaçant la spécification des règles vers les données d’entraînement, les modèles appris ont franchi un mur de complexité que les règles écrites à la main ne pouvaient pas traverser ; mais ils ont payé cette portée nouvelle en renonçant à la garantie préalable et à l’adresse précise des défaillances.

Après :

> En déplaçant la spécification des règles vers les données d’entraînement, les modèles appris ont franchi un mur de complexité que les règles écrites à la main ne pouvaient pas traverser. Ils ont toutefois payé cette portée nouvelle en renonçant à la garantie préalable et à l’adresse précise des défaillances.

*Juge :* Coupe d'une phrase longue au point-virgule ; « mais » devient « toutefois », la concession est conservée, sens et termes inchangés.

### 004 — § « À qui s’adresse cet ouvrage » (ligne 21) — phrase-longue

Avant :

> Ce livre a été conçu en premier lieu pour des professionnels de culture scientifique et technique — ingénieurs, analystes quantitatifs, praticiens de l’apprentissage automatique, architectes logiciels, responsables de recherche ou d’études — qui ont croisé le calcul des probabilités et la logique au cours de leur formation, mais n’ont pas toujours eu l’occasion de les pratiquer comme un instrument quotidien de raisonnement sur la décision, la fiabilité des contrôles et les modes de défaillance.

Après :

> Ce livre a été conçu en premier lieu pour des professionnels de culture scientifique et technique — ingénieurs, analystes quantitatifs, praticiens de l’apprentissage automatique, architectes logiciels, responsables de recherche ou d’études — qui ont croisé le calcul des probabilités et la logique au cours de leur formation. Ils n’ont toutefois pas toujours eu l’occasion de les pratiquer comme un instrument quotidien de raisonnement sur la décision, la fiabilité des contrôles et les modes de défaillance.

*Juge :* Coupe d'une phrase-tunnel ; « pas toujours » est conservé, « toutefois » garde la concession et « Ils » renvoie sans ambiguïté aux professionnels énumérés.

### 005 — § « La règle du texte principal » (ligne 43) — phrase-longue

Avant :

> Un lecteur qui choisit de passer les encadrés d’approfondissement théorique ou critique (*Boîte à outils*, *Noyau formel*, *Nuance et discussion ouverte*, *Question à se poser*) ne perd aucun maillon du raisonnement : ces blocs éclairent et consolident l’argument, mais n’en portent jamais seuls une étape indispensable.

Après :

> Un lecteur qui choisit de passer les encadrés d’approfondissement théorique ou critique (*Boîte à outils*, *Noyau formel*, *Nuance et discussion ouverte*, *Question à se poser*) ne perd aucun maillon du raisonnement. Ces blocs éclairent et consolident en effet l’argument, mais n’en portent jamais seuls une étape indispensable.

*Juge :* Le deux-points est remplacé par une coupe articulée (« en effet ») ; « jamais seuls » et l'énumération des encadrés sont intacts.

### 006 — § « Les six types d’encadrés » (ligne 51) — italique

Avant :

> Ces exemples ont une valeur strictement *illustrative* : les paramètres retenus (récapitulés dans l’annexe [-@sec:annexe-d]) sont choisis pour mettre une propriété structurelle à nu, non pour fournir l’estimation empirique d’une grandeur réelle.

Après :

> Ces exemples ont une valeur strictement illustrative. Les paramètres retenus (récapitulés dans l’annexe [-@sec:annexe-d]) sont en effet choisis pour mettre une propriété structurelle à nu, non pour fournir l’estimation empirique d’une grandeur réelle.

*Juge :* Coupe articulée par « en effet » et retrait d'une italique d'emphase, conformément à la spécification ; « strictement » et la restriction « non pour… » sont conservés.

## Rejetées par le juge (4)

### 002 — § « Une démarche de travail, non une prescription » (ligne 13) — argument

*Juge :* Le deux-points énonçait le contenu de « l'un des arguments centraux du livre » ; avec « , car », ce contenu devient une simple justification et peut se rattacher à « développé au @sec:ch07 ». La phrase n'identifie plus l'argument, et la longueur ne diminue pas.

Avant :

> Prétendre fournir une méta-procédure formelle garantissant la justesse de nos cadres de pensée contredirait d’ailleurs l’un des arguments centraux du livre, développé au @sec:ch07 : toute procédure chargée d’auditer un cadre repose elle-même sur une spécification finie, et ne fait que reporter le problème un cran plus haut.

Après (non appliqué) :

> Prétendre fournir une méta-procédure formelle garantissant la justesse de nos cadres de pensée contredirait d’ailleurs l’un des arguments centraux du livre, développé au @sec:ch07, car toute procédure chargée d’auditer un cadre repose elle-même sur une spécification finie et ne fait que reporter le problème un cran plus haut.

### 003 — § « Une démarche de travail, non une prescription » (ligne 15) — argument, francais

*Juge :* Le deux-points exposait en quoi consiste la tension ; « Car » en tête de phrase en fait une preuve de son existence et alourdit la phrase (« Car plus…, mieux…, mais plus… »).

Avant :

> Il existe une tension réelle entre l’indépendance d’un contrôle et sa comparabilité avec l’affirmation qu’il vérifie : plus un regard extérieur est éloigné de nos hypothèses, mieux il peut percevoir nos omissions, mais plus il est en général difficile et coûteux de traduire son objection en une comparaison décisive (@sec:ch08).

Après (non appliqué) :

> Il existe une tension réelle entre l’indépendance d’un contrôle et sa comparabilité avec l’affirmation qu’il vérifie. Car plus un regard extérieur est éloigné de nos hypothèses, mieux il peut percevoir nos omissions, mais plus il est en général difficile et coûteux de traduire son objection en une comparaison décisive (@sec:ch08).

### 007 — § « Les six types d’encadrés » (ligne 52) — argument, sens

*Juge :* « ainsi » présente le fait que « les chiffres datés illustrent un mécanisme durable » comme une conséquence de la mention du millésime dans le titre. C'est un lien de conséquence absent de l'original, où le deux-points donnait la raison de cette mention.

Avant :

> Lorsqu’une étude de cas porte sur des systèmes d’intelligence artificielle ou des expériences de terrain dont les mesures dépendent d’une génération particulière de modèles et d’outils, son titre mentionne explicitement son millésime : les chiffres datés illustrent un mécanisme durable, mais l’argument général du livre ne dépend jamais des performances transitoires d’une version donnée.

Après (non appliqué) :

> Lorsqu’une étude de cas porte sur des systèmes d’intelligence artificielle ou des expériences de terrain dont les mesures dépendent d’une génération particulière de modèles et d’outils, son titre mentionne explicitement son millésime. Les chiffres datés illustrent ainsi un mécanisme durable, mais l’argument général du livre ne dépend jamais des performances transitoires d’une version donnée.

### 008 — § « Terminologie, notations et parcours » (ligne 62) — argument

*Juge :* « permettent ainsi » ajoute un lien de conséquence entre la mise en gras du terme et le rôle du glossaire et de la table des notations. L'original juxtaposait deux dispositifs indépendants.

Avant :

> Ce terme est mis en caractères gras et défini lors de sa première introduction formelle dans le corps de l’ouvrage ; le glossaire de l’annexe [-@sec:annexe-b] et la table des notations de l’annexe [-@sec:annexe-c] permettent de retrouver à tout moment sa définition et le chapitre qui l’introduit.

Après (non appliqué) :

> Ce terme est mis en caractères gras et défini lors de sa première introduction formelle dans le corps de l’ouvrage. Le glossaire de l’annexe [-@sec:annexe-b] et la table des notations de l’annexe [-@sec:annexe-c] permettent ainsi de retrouver à tout moment sa définition et le chapitre qui l’introduit.

## Rejetées par les contrôles mécaniques (0)

