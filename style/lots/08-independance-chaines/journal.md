# Journal de la passe de style — `08-independance-chaines`

- Appliqué le 2026-11-20T13:26:24 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 7 · appliquées : 4 · rejetées par le juge : 3 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (4)

### 001 — § « L’indépendance est relative, et se paie en comparabilité » (ligne 53) — phrase-longue

Avant :

> La comparabilité est parfaite — les résultats se superposent bit à bit —, mais la capacité à se tromper autrement est nulle : les deux exécutions partagent tout, jusqu’à la moindre omission de cadre, et ne contrôlent rien l’une chez l’autre (tout au plus une panne matérielle fugitive).

Après :

> La comparabilité est parfaite — les résultats se superposent bit à bit —, mais la capacité à se tromper autrement est nulle. Les deux exécutions partagent en effet tout, jusqu’à la moindre omission de cadre, et ne contrôlent rien l’une chez l’autre (tout au plus une panne matérielle fugitive).

*Juge :* Le deux-points explicatif devient un point suivi de « en effet », ce qui allège un paragraphe déjà chargé en deux-points. Le sens, la portée (« nulle », « tout », « rien », « tout au plus ») et la parenthèse sont conservés.

### 003 — § « L’indépendance est relative, et se paie en comparabilité » (ligne 70) — phrase-longue

Avant :

> - Tout en haut du tableau se tient une seconde exécution du même calcul par éléments finis : la comparaison est immédiate, gratuite, et parfaitement aveugle à la corrosion ; un contrôle analytique rapide reposant sur les mêmes idéalisations géométriques (@sec:ch07) demeure, lui aussi, bloqué au niveau des méthodes partageant le même modèle.

Après :

> - Tout en haut du tableau se tient une seconde exécution du même calcul par éléments finis : la comparaison est immédiate, gratuite, et parfaitement aveugle à la corrosion. Un contrôle analytique rapide reposant sur les mêmes idéalisations géométriques (@sec:ch07) demeure, lui aussi, bloqué au niveau des méthodes partageant le même modèle.

*Juge :* Le point-virgule devient un point et sépare deux comparateurs distincts dans un item de liste trop long. « lui aussi », le renvoi et le niveau du tableau sont conservés.

### 004 — § « L’indépendance est relative, et se paie en comparabilité » (ligne 71) — phrase-longue

Avant :

> - Au milieu du tableau figure le modèle d’un collègue appartenant à une autre équipe de mécanique, bâti avec d’autres approximations de géométrie ou d’encastrement : ce comparateur peut repérer une mauvaise hypothèse mécanique dans les variables partagées, mais tant que le cadre demeure purement mécanique, la corrosion lui échappe encore.

Après :

> - Au milieu du tableau figure le modèle d’un collègue appartenant à une autre équipe de mécanique, bâti avec d’autres approximations de géométrie ou d’encastrement. Ce comparateur peut repérer une mauvaise hypothèse mécanique dans les variables partagées, mais tant que le cadre demeure purement mécanique, la corrosion lui échappe encore.

*Juge :* Le deux-points devient un point, ce qui coupe un item long. Le modal « peut », la restriction « dans les variables partagées » et la condition « tant que » restent intacts.

### 005 — § « Chaînes contre contrôles croisés » (ligne 116) — phrase-longue

Avant :

> Dans une chaîne à quatre étapes — par exemple mesure, lissage, calcul thermique, calcul mécanique —, chaque maillon se fie à ce qu’il reçoit pour se concentrer sur sa propre tâche : il suffit qu’un seul maillon laisse passer une cause d’erreur qu’il ne sait pas voir, ou que le passage d’un maillon au suivant introduise une erreur de raccordement, pour que le résultat final soit faussé.

Après :

> Dans une chaîne à quatre étapes — par exemple mesure, lissage, calcul thermique, calcul mécanique —, chaque maillon se fie à ce qu’il reçoit pour se concentrer sur sa propre tâche. Il suffit alors qu’un seul maillon laisse passer une cause d’erreur qu’il ne sait pas voir, ou que le passage d’un maillon au suivant introduise une erreur de raccordement, pour que le résultat final soit faussé.

*Juge :* Le deux-points devient un point suivi de « alors », qui explicite le lien de conséquence que portait le deux-points. La condition « il suffit qu’un seul… ou que… » est intacte, et les deux sources d’erreur sont conservées.

## Rejetées par le juge (3)

### 002 — § « L’indépendance est relative, et se paie en comparabilité » (ligne 55) — francais

*Juge :* « Elles ne parlent pas en effet des mêmes grandeurs » : l’adverbe pris entre « pas » et son complément, sans virgules, est maladroit et peut se lire comme une négation de « en effet ». L’ordre attendu serait « ne parlent en effet pas » ou une incise entre virgules.

Avant :

> Mais précisément parce qu’il partage très peu avec votre représentation, ses objections peinent à mordre sur vos chiffres : elles ne parlent pas des mêmes grandeurs, ne se traduisent pas sans effort dans votre modèle et risquent d’être écartées faute de terrain commun ou de prise en compte (@def:prise-en-compte).

Après (non appliqué) :

> Mais précisément parce qu’il partage très peu avec votre représentation, ses objections peinent à mordre sur vos chiffres. Elles ne parlent pas en effet des mêmes grandeurs, ne se traduisent pas sans effort dans votre modèle et risquent d’être écartées faute de terrain commun ou de prise en compte (@def:prise-en-compte).

### 006 — § « Chaînes contre contrôles croisés » (ligne 118) — francais, registre

*Juge :* « Car » en tête de phrase, après un point, est une construction critiquée en prose académique. La retouche remplace un deux-points par un tic plus visible, sans gain net.

Avant :

> Vis-à-vis de son propre angle mort, c’est en réalité une copie : le contrôleur partage le même cadre, les mêmes variables et les mêmes omissions que le producteur, de sorte que l’intersection de leurs angles morts redonne l’angle mort initial tout entier (@sec:ch07).

Après (non appliqué) :

> Vis-à-vis de son propre angle mort, c’est en réalité une copie. Car le contrôleur partage le même cadre, les mêmes variables et les mêmes omissions que le producteur, de sorte que l’intersection de leurs angles morts redonne l’angle mort initial tout entier (@sec:ch07).

### 007 — § « Le blanchiment aux interfaces » (ligne 185) — argument

*Juge :* « Or » introduit ici la prémisse qui, combinée à l’erreur d’unité, explique pourquoi elle est passée inaperçue. « Mais » pose à la place une opposition avec la phrase précédente, alors qu’il n’y en a pas : le lien logique change.

Avant :

> Or les nombres franchissaient l’interface nus, dépourvus de toute mention d’unité à l’intérieur même du fichier transmis.

Après (non appliqué) :

> Mais les nombres franchissaient l’interface nus, dépourvus de toute mention d’unité à l’intérieur même du fichier transmis.

## Rejetées par les contrôles mécaniques (0)

