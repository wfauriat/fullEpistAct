# Dossier du juge — `10-couches-basses`

- Chapitre d'origine, figé au moment de la vérification : `style/lots/10-couches-basses/original.md` (les numéros de ligne renvoient à ce fichier ; le lire pour le contexte).
- Retouches soumises : **7** (sur 7 proposées ; 0 écartées par les contrôles mécaniques).
- Consignes : `.claude/agents/juge-style.md`. Sortie attendue : `style/lots/10-couches-basses/verdicts.json`, un verdict par retouche ci-dessous.
- Les alertes automatiques sont des indices, pas des verdicts.

---

## 001 — § « Des opérations élémentaires à la composition » (ligne 44)

**Avant**

> Or nous avons établi au @sec:ch08 (@prop:chaines) qu’une longue suite d’étapes mises en série risque de cumuler les angles morts de chaque maillon et les malentendus nés aux interfaces.

**Après**

> Nous avons pourtant établi au @sec:ch08 (@prop:chaines) qu’une longue suite d’étapes mises en série risque de cumuler les angles morts de chaque maillon et les malentendus nés aux interfaces.

---

## 002 — § « Chaque couche est une promesse écrite » (ligne 76)

**Avant**

> On reconnaît exactement le mécanisme de blanchiment analysé à la @sec:ch08-blanchiment (@def:blanchiment), par lequel les conditions ou les unités d’un résultat disparaissent au passage d’une frontière : ce que l’interface laisse tomber ou relègue hors du périmètre contrôlé peut traverser les maillons sans alerte, même au cœur d’un logiciel parfaitement déterministe.

**Après**

> On reconnaît exactement le mécanisme de blanchiment analysé à la @sec:ch08-blanchiment (@def:blanchiment), par lequel les conditions ou les unités d’un résultat disparaissent au passage d’une frontière. Ce que l’interface laisse tomber ou relègue hors du périmètre contrôlé peut ainsi traverser les maillons sans alerte, même au cœur d’un logiciel parfaitement déterministe.

---

## 003 — § « Vérifier une fois, avant l’usage » (ligne 86)

**Avant**

> - *Les systèmes de types statiques* : le compilateur vérifie avant toute exécution que les données passées aux fonctions appartiennent aux catégories attendues ; un programme qui tente d’additionner une date et une vitesse, ou de passer une valeur de type `LivreForceSeconde` là où la signature attend un `NewtonSeconde`, est rejeté avant même de pouvoir être exécuté.

**Après**

> - *Les systèmes de types statiques* : le compilateur vérifie avant toute exécution que les données passées aux fonctions appartiennent aux catégories attendues. Un programme qui tente d’additionner une date et une vitesse, ou de passer une valeur de type `LivreForceSeconde` là où la signature attend un `NewtonSeconde`, est ainsi rejeté avant même de pouvoir être exécuté.

---

## 004 — § « Les défaillances ont une adresse » (ligne 107)

**Avant**

> Or la spécification d’interface écrite exigeait que ces grandeurs soient exprimées en unités du Système international, les newton-secondes ($\text{N}\cdot\text{s}$), alors que le programme `SM_FORCES` les écrivait en unités anglo-saxonnes, les livres-force-secondes ($\text{lbf}\cdot\text{s}$).

**Après**

> La spécification d’interface écrite exigeait pourtant que ces grandeurs soient exprimées en unités du Système international, les newton-secondes ($\text{N}\cdot\text{s}$), alors que le programme `SM_FORCES` les écrivait en unités anglo-saxonnes, les livres-force-secondes ($\text{lbf}\cdot\text{s}$).

---

## 005 — § « Les défaillances ont une adresse » (ligne 118)

**Avant**

> Ce sont ces failles humaines et de processus qui ont empêché la prise en compte des indices faibles en cours de vol ; mais elles n’ont pas effacé l’existence d’une règle écrite précise ni celle du programme et du fichier d’interface qui la contredisaient.

**Après**

> Ce sont ces failles humaines et de processus qui ont empêché la prise en compte des indices faibles en cours de vol. Elles n’ont toutefois pas effacé l’existence d’une règle écrite précise ni celle du programme et du fichier d’interface qui la contredisaient.

---

## 006 — § « Les défaillances ont une adresse » (ligne 135)

**Avant**

> Au terme de ce chapitre, la raison pour laquelle nous pouvons légitimement oublier les couches basses de l’informatique est claire : des opérations élémentaires jusqu’aux protocoles réseau et aux systèmes de fichiers, l’édifice est composé de composants spécifiés dont les contrats écrits rendent possible une vérification en amont, une fois pour toutes les exécutions futures, et garantissent qu’en cas d’échec, l’enquête retrouve une adresse.

**Après**

> Au terme de ce chapitre, la raison pour laquelle nous pouvons légitimement oublier les couches basses de l’informatique est claire. Des opérations élémentaires jusqu’aux protocoles réseau et aux systèmes de fichiers, l’édifice est composé de composants spécifiés dont les contrats écrits rendent possible une vérification en amont, une fois pour toutes les exécutions futures, et garantissent qu’en cas d’échec, l’enquête retrouve une adresse.

---

## 007 — § « Points clés » (ligne 146)

**Avant**

> - Écrire un contrat ne suffit pas à le faire appliquer : entre contrat appliqué mécaniquement, contrat seulement écrit en prose et attente formulable sans écrit préalable, seul le premier arrête automatiquement les écarts avant l’usage, faute de quoi des données nues subissent encore un blanchiment aux interfaces.

**Après**

> - Écrire un contrat ne suffit pas à le faire appliquer. Entre contrat appliqué mécaniquement, contrat seulement écrit en prose et attente formulable sans écrit préalable, seul le premier arrête automatiquement les écarts avant l’usage, faute de quoi des données nues subissent encore un blanchiment aux interfaces.

