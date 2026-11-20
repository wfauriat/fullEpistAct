# Journal de la passe de style — `10-couches-basses`

- Appliqué le 2026-11-20T13:28:24 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 7 · appliquées : 6 · rejetées par le juge : 1 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (6)

### 001 — § « Des opérations élémentaires à la composition » (ligne 44) — or-initial

Avant :

> Or nous avons établi au @sec:ch08 (@prop:chaines) qu’une longue suite d’étapes mises en série risque de cumuler les angles morts de chaque maillon et les malentendus nés aux interfaces.

Après :

> Nous avons pourtant établi au @sec:ch08 (@prop:chaines) qu’une longue suite d’étapes mises en série risque de cumuler les angles morts de chaque maillon et les malentendus nés aux interfaces.

*Juge :* « Or » initial remplacé par « pourtant » ; la tension entre « aucun ingrédient mystérieux » et le risque des chaînes (@prop:chaines) est réelle, et la phrase garde son rôle : poser la difficulté que reprend la question suivante.

### 002 — § « Chaque couche est une promesse écrite » (ligne 76) — phrase-longue

Avant :

> On reconnaît exactement le mécanisme de blanchiment analysé à la @sec:ch08-blanchiment (@def:blanchiment), par lequel les conditions ou les unités d’un résultat disparaissent au passage d’une frontière : ce que l’interface laisse tomber ou relègue hors du périmètre contrôlé peut traverser les maillons sans alerte, même au cœur d’un logiciel parfaitement déterministe.

Après :

> On reconnaît exactement le mécanisme de blanchiment analysé à la @sec:ch08-blanchiment (@def:blanchiment), par lequel les conditions ou les unités d’un résultat disparaissent au passage d’une frontière. Ce que l’interface laisse tomber ou relègue hors du périmètre contrôlé peut ainsi traverser les maillons sans alerte, même au cœur d’un logiciel parfaitement déterministe.

*Juge :* Longue phrase coupée au deux-points ; « ainsi » rend le lien de conséquence implicite, et « peut », « sans alerte » et « même au cœur d’un logiciel parfaitement déterministe » sont conservés.

### 003 — § « Vérifier une fois, avant l’usage » (ligne 86) — phrase-longue

Avant :

> - *Les systèmes de types statiques* : le compilateur vérifie avant toute exécution que les données passées aux fonctions appartiennent aux catégories attendues ; un programme qui tente d’additionner une date et une vitesse, ou de passer une valeur de type `LivreForceSeconde` là où la signature attend un `NewtonSeconde`, est rejeté avant même de pouvoir être exécuté.

Après :

> - *Les systèmes de types statiques* : le compilateur vérifie avant toute exécution que les données passées aux fonctions appartiennent aux catégories attendues. Un programme qui tente d’additionner une date et une vitesse, ou de passer une valeur de type `LivreForceSeconde` là où la signature attend un `NewtonSeconde`, est ainsi rejeté avant même de pouvoir être exécuté.

*Juge :* Coupe au point-virgule d’un item très long ; l’exemple de rejet reste rattaché à la vérification du compilateur, et les modalités (« avant toute exécution », « avant même de pouvoir être exécuté ») sont intactes.

### 005 — § « Les défaillances ont une adresse » (ligne 118) — phrase-longue

Avant :

> Ce sont ces failles humaines et de processus qui ont empêché la prise en compte des indices faibles en cours de vol ; mais elles n’ont pas effacé l’existence d’une règle écrite précise ni celle du programme et du fichier d’interface qui la contredisaient.

Après :

> Ce sont ces failles humaines et de processus qui ont empêché la prise en compte des indices faibles en cours de vol. Elles n’ont toutefois pas effacé l’existence d’une règle écrite précise ni celle du programme et du fichier d’interface qui la contredisaient.

*Juge :* « ; mais » devient « . Elles n’ont toutefois pas » : la concession est conservée, et le contenu factuel du rapport reste inchangé.

### 006 — § « Les défaillances ont une adresse » (ligne 135) — phrase-longue

Avant :

> Au terme de ce chapitre, la raison pour laquelle nous pouvons légitimement oublier les couches basses de l’informatique est claire : des opérations élémentaires jusqu’aux protocoles réseau et aux systèmes de fichiers, l’édifice est composé de composants spécifiés dont les contrats écrits rendent possible une vérification en amont, une fois pour toutes les exécutions futures, et garantissent qu’en cas d’échec, l’enquête retrouve une adresse.

Après :

> Au terme de ce chapitre, la raison pour laquelle nous pouvons légitimement oublier les couches basses de l’informatique est claire. Des opérations élémentaires jusqu’aux protocoles réseau et aux systèmes de fichiers, l’édifice est composé de composants spécifiés dont les contrats écrits rendent possible une vérification en amont, une fois pour toutes les exécutions futures, et garantissent qu’en cas d’échec, l’enquête retrouve une adresse.

*Juge :* Coupe au deux-points d’une phrase de bilan très longue, dans un paragraphe qui contient déjà un autre deux-points ; « rendent possible » et « garantissent » sont conservés tels quels.

### 007 — § « Points clés » (ligne 146) — phrase-longue

Avant :

> - Écrire un contrat ne suffit pas à le faire appliquer : entre contrat appliqué mécaniquement, contrat seulement écrit en prose et attente formulable sans écrit préalable, seul le premier arrête automatiquement les écarts avant l’usage, faute de quoi des données nues subissent encore un blanchiment aux interfaces.

Après :

> - Écrire un contrat ne suffit pas à le faire appliquer. Entre contrat appliqué mécaniquement, contrat seulement écrit en prose et attente formulable sans écrit préalable, seul le premier arrête automatiquement les écarts avant l’usage, faute de quoi des données nues subissent encore un blanchiment aux interfaces.

*Juge :* Coupe au deux-points dans un point clé chargé ; les trois degrés, « seul le premier » et « faute de quoi » sont intacts.

## Rejetées par le juge (1)

### 004 — § « Les défaillances ont une adresse » (ligne 107) — argument, francais

*Juge :* « pourtant » oppose l’exigence de la spécification à la phrase précédente, qui ne dit rien des unités : aucune opposition n’y existe. De plus, il double l’opposition déjà portée par « alors que » dans la même phrase (« exigeait pourtant… alors que »). « Or », qui introduit ici le fait décisif du récit, était plus juste.

Avant :

> Or la spécification d’interface écrite exigeait que ces grandeurs soient exprimées en unités du Système international, les newton-secondes ($\text{N}\cdot\text{s}$), alors que le programme `SM_FORCES` les écrivait en unités anglo-saxonnes, les livres-force-secondes ($\text{lbf}\cdot\text{s}$).

Après (non appliqué) :

> La spécification d’interface écrite exigeait pourtant que ces grandeurs soient exprimées en unités du Système international, les newton-secondes ($\text{N}\cdot\text{s}$), alors que le programme `SM_FORCES` les écrivait en unités anglo-saxonnes, les livres-force-secondes ($\text{lbf}\cdot\text{s}$).

## Rejetées par les contrôles mécaniques (0)

