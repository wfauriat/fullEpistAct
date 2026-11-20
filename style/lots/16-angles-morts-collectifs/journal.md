# Journal de la passe de style — `16-angles-morts-collectifs`

- Appliqué le 2026-11-20T13:32:19 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 9 · appliquées : 6 · rejetées par le juge : 3 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (6)

### 001 — § « Le taux d’erreur baisse, la probabilité d’échappement monte » (ligne 12) — or-initial

Avant :

> Or, comme l’a souligné le @sec:ch09, les tests de référence notent le producteur seul et ne mesurent donc que le premier facteur ; un tableau de bord qui s’en tient à ces scores laisse dans l’ombre l’évolution du second.

Après :

> Comme l’a souligné le @sec:ch09, les tests de référence notent pourtant le producteur seul et ne mesurent donc que le premier facteur. Un tableau de bord qui s’en tient à ces scores laisse ainsi dans l’ombre l’évolution du second.

*Juge :* « Or » initial retiré au profit de « pourtant », qui rend le contraste attendu (deux facteurs distingués, un seul mesuré) ; coupe au point-virgule articulée par « ainsi » ; sens, portée et renvois inchangés.

### 002 — § « Le taux d’erreur baisse, la probabilité d’échappement monte » (ligne 59) — phrase-longue

Avant :

> Le premier, déjà isolé au @sec:ch09, tient à la chute de la VPP face à un contrôleur fixe : la plupart des alertes deviennent fausses (@eq:ch09-vpp) et, si les opérateurs réagissent par appariement des probabilités [@bliss1995], leur prise en compte $u$ recule jusqu’à rendre le contrôleur pratiquement décoratif.

Après :

> Le premier, déjà isolé au @sec:ch09, tient à la chute de la VPP face à un contrôleur fixe. La plupart des alertes deviennent ainsi fausses (@eq:ch09-vpp) et, si les opérateurs réagissent par appariement des probabilités [@bliss1995], leur prise en compte $u$ recule jusqu’à rendre le contrôleur pratiquement décoratif.

*Juge :* Coupe au deux-points articulée par « ainsi » ; la condition « si les opérateurs réagissent par appariement des probabilités » reste dans la même phrase et porte sur le même segment.

### 005 — § « Un même prêteur pour tous les emprunteurs » (ligne 76) — phrase-longue

Avant :

> Une scène familière du journalisme résume ce trompe-l’œil collectif : imaginons vingt journalistes qui, pour vérifier la solidité de leur article avant publication, s’appellent consciencieusement les uns les autres afin de confronter leurs chiffres et leurs citations — alors que tous les vingt se sont appuyés, sans le savoir ni le mentionner, sur la même dépêche d’agence non vérifiée.

Après :

> Une scène familière du journalisme résume ce trompe-l’œil collectif. Imaginons vingt journalistes qui, pour vérifier la solidité de leur article avant publication, s’appellent consciencieusement les uns les autres afin de confronter leurs chiffres et leurs citations — alors que tous les vingt se sont appuyés, sans le savoir ni le mentionner, sur la même dépêche d’agence non vérifiée.

*Juge :* Coupe au deux-points d’une phrase longue qui introduit la scène ; contenu, exemple et incise intacts.

### 007 — § « L’étranglement institutionnel de l’évaluation » (ligne 102) — or-initial

Avant :

> Or les structures d’incitation de la plupart des organisations n’ont pas suivi ce basculement.

Après :

> Mais les structures d’incitation de la plupart des organisations n’ont pas suivi ce basculement.

*Juge :* « Or » initial remplacé par « Mais », qui rend fidèlement le contraste entre le basculement décrit et l’inertie des incitations ; « la plupart des » conservé.

### 008 — § « L’étranglement institutionnel de l’évaluation » (ligne 104) — phrase-longue

Avant :

> Les évaluateurs restants, submergés par le flux, n’ont plus le temps de remonter la provenance de chaque pièce, de reproduire un calcul par une voie indépendante ni d’enquêter sur des alertes dont la VPP baisse — ce qui referme sur eux le piège de l’appariement des probabilités et les ramène à une vigilance purement formelle, tandis que la prise en compte (@def:prise-en-compte) cède sous la pression des délais.

Après :

> Les évaluateurs restants, submergés par le flux, n’ont plus le temps de remonter la provenance de chaque pièce, de reproduire un calcul par une voie indépendante ni d’enquêter sur des alertes dont la VPP baisse. Cette situation referme alors sur eux le piège de l’appariement des probabilités et les ramène à une vigilance purement formelle, tandis que la prise en compte (@def:prise-en-compte) cède sous la pression des délais.

*Juge :* Coupe d’une phrase très longue ; « Cette situation » reprend sans ambiguïté l’ensemble de ce que les évaluateurs n’ont plus le temps de faire, et « tandis que » ainsi que le terme « prise en compte » avec son renvoi sont conservés.

### 009 — § « L’étranglement institutionnel de l’évaluation » (ligne 110) — phrase-longue

Avant :

> L’automatisation les *enchaîne* d’abord dans des suites d’étapes et des boucles d’agents dont les erreurs s’exécutent plus vite que la reprise en main humaine (@sec:ch14) ; elle *retire* ensuite les contrôles implicites que fabriquaient la friction, les marques visibles du doute et le coût de la forme (@sec:ch15) ; elle *corrèle* enfin les contrôles restants par le partage d’un même prêteur, efface la provenance dans le patrimoine commun et comprime la capacité d’évaluation sous la pression du débit (@sec:ch16).

Après :

> L’automatisation les *enchaîne* d’abord dans des suites d’étapes et des boucles d’agents dont les erreurs s’exécutent plus vite que la reprise en main humaine (@sec:ch14). Elle *retire* ensuite les contrôles implicites que fabriquaient la friction, les marques visibles du doute et le coût de la forme (@sec:ch15). Elle *corrèle* enfin les contrôles restants par le partage d’un même prêteur, efface la provenance dans le patrimoine commun et comprime la capacité d’évaluation sous la pression du débit (@sec:ch16).

*Juge :* Coupe aux points-virgules d’une phrase de plus de soixante-dix mots ; les trois verbes en italique, l’ordre « d’abord, ensuite, enfin », tous les éléments de l’énumération et les renvois sont conservés.

## Rejetées par le juge (3)

### 003 — § « Le taux d’erreur baisse, la probabilité d’échappement monte » (ligne 59) — portee, argument

*Juge :* La coupe fait sortir « le contrôleur ne sert presque plus, mais le risque total continue de suivre la baisse du taux d’erreur » de la portée de « tant que les paramètres du contrôleur ($c$, $m$, $f$) restent inchangés » ; le paragraphe suivant montre justement que cette conclusion tombe quand $c$ bouge.

Avant :

> Et tant que les paramètres du contrôleur ($c$, $m$, $f$) restent inchangés, ce premier mécanisme rapproche le risque résiduel du risque sans contrôleur, $P(E)$, sans le faire monter : le contrôleur ne sert presque plus, mais le risque total continue de suivre la baisse du taux d’erreur.

Après (non appliqué) :

> Et tant que les paramètres du contrôleur ($c$, $m$, $f$) restent inchangés, ce premier mécanisme rapproche le risque résiduel du risque sans contrôleur, $P(E)$, sans le faire monter. Le contrôleur ne sert presque plus, mais le risque total continue de suivre la baisse du taux d’erreur.

### 004 — § « Un même prêteur pour tous les emprunteurs » (ligne 68) — argument

*Juge :* « pourtant » introduit une opposition absente : le grand modèle de langage prolonge et industrialise le mécanisme de la phrase précédente (réutiliser un contact avec le monde payé par d’autres), il ne le contredit pas. Le lien logique change.

Avant :

> Or un grand modèle de langage entraîné sur l’immense archive écrite industrialise la voie qui consiste à *être averti* en la concentrant dans un réservoir unique : il condense en un seul jeu de paramètres ce que des millions d’auteurs, d’ingénieurs et d’observateurs ont découvert au contact du monde, et le met à la disposition de quiconque l’interroge (@sec:ch11).

Après (non appliqué) :

> Un grand modèle de langage entraîné sur l’immense archive écrite industrialise pourtant la voie qui consiste à *être averti* en la concentrant dans un réservoir unique. Il condense en effet en un seul jeu de paramètres ce que des millions d’auteurs, d’ingénieurs et d’observateurs ont découvert au contact du monde, et le met à la disposition de quiconque l’interroge (@sec:ch11).

### 006 — § « Blanchiment de provenance et biens communs épistémiques » (ligne 88) — argument, gain

*Juge :* Le deux-points introduisait la glose de $\Pr(A \mid E)$ voisine de $1$ ; « en effet » la présente comme une justification de la phrase précédente, ce qui inverse le rapport entre énoncé formel et lecture. Le gain reste faible pour une phrase de longueur raisonnable.

Avant :

> Dans l’@eq:ch09-accord-cotes, dès lors que la première copie reproduit une erreur $E$ du modèle source, les neuf autres copies dérivées de la même lignée ont une probabilité $\Pr(A \mid E)$ voisine de $1$ de concorder avec elle : l’accord n’avait pratiquement aucune chance d’échouer si l’affirmation était fausse.

Après (non appliqué) :

> Dans l’@eq:ch09-accord-cotes, dès lors que la première copie reproduit une erreur $E$ du modèle source, les neuf autres copies dérivées de la même lignée ont une probabilité $\Pr(A \mid E)$ voisine de $1$ de concorder avec elle. L’accord n’avait en effet pratiquement aucune chance d’échouer si l’affirmation était fausse.

## Rejetées par les contrôles mécaniques (0)

