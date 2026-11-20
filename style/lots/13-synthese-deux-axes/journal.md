# Journal de la passe de style — `13-synthese-deux-axes`

- Appliqué le 2026-11-20T13:30:57 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 8 · appliquées : 5 · rejetées par le juge : 3 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (5)

### 001 — § « Deux axes plutôt que trois sortes d’incertitude » (ligne 13) — phrase-longue

Avant :

> Une erreur signalée n’est pas encore une erreur arrêtée : pour qu’un désaccord empêche une décision dommageable, il faut encore que le comparateur soit comparable à l’affirmation, que le signal arrive à temps et qu’il fasse l’objet d’une prise en compte effective (@def:prise-en-compte) par quelqu’un ayant l’autorité d’agir (@sec:ch06-cinq-conditions).

Après :

> Une erreur signalée n’est pas encore une erreur arrêtée. Pour qu’un désaccord empêche une décision dommageable, il faut encore que le comparateur soit comparable à l’affirmation, que le signal arrive à temps et qu’il fasse l’objet d’une prise en compte effective (@def:prise-en-compte) par quelqu’un ayant l’autorité d’agir (@sec:ch06-cinq-conditions).

*Juge :* Coupe au deux-points d’une phrase longue ; « il faut encore » garde le lien explicatif, et le sens, la portée et les renvois restent inchangés.

### 004 — § « Deux axes plutôt que trois sortes d’incertitude » (ligne 40) — phrase-longue

Avant :

> Ce qu’un composant spécifié autorise, ce n’est pas l’absence spontanée d’erreurs silencieuses, mais la *possibilité de vider la case à l’avance* : parce qu’une spécification peut être écrite, lue et confrontée au code une fois pour toutes avant la mise en service, on peut déplacer ces erreurs vers la colonne de gauche pour l’ensemble des exécutions futures couvertes par le contrat.

Après :

> Ce qu’un composant spécifié autorise, ce n’est pas l’absence spontanée d’erreurs silencieuses, mais la *possibilité de vider la case à l’avance*. Parce qu’une spécification peut être écrite, lue et confrontée au code une fois pour toutes avant la mise en service, on peut en effet déplacer ces erreurs vers la colonne de gauche pour l’ensemble des exécutions futures couvertes par le contrat.

*Juge :* Coupe d’une phrase longue ; « en effet » restitue le lien justificatif du deux-points, et le modal « peut » ainsi que la restriction « couvertes par le contrat » sont conservés.

### 005 — § « Un énoncé fixé à l’avance : reconstruire un contrôle mécanique autour de la tâche » (ligne 96) — phrase-longue

Avant :

> Dans l’expérience de Knight et Leveson (@sec:ch08) [@knightleveson1986], vingt-sept programmeurs humains travaillant séparément à partir d’une *même spécification* échouaient déjà ensemble sur les entrées difficiles ; lorsqu’un seul et même composant engendre la solution et son comparateur, la communauté de cause est plus étroite encore.

Après :

> Dans l’expérience de Knight et Leveson (@sec:ch08) [@knightleveson1986], vingt-sept programmeurs humains travaillant séparément à partir d’une *même spécification* échouaient déjà ensemble sur les entrées difficiles. Lorsqu’un seul et même composant engendre la solution et son comparateur, la communauté de cause est plus étroite encore.

*Juge :* Coupe au point-virgule ; « déjà » et « plus étroite encore » maintiennent le raisonnement a fortiori, et les faits rapportés de Knight et Leveson sont inchangés.

### 006 — § « Un autre raisonneur : abondance apparente et angles morts partagés » (ligne 116) — phrase-longue

Avant :

> D’abord, comme l’a établi l’étude de la plausibilité au @sec:ch12, réinterroger un même modèle ou des modèles très voisins attrape les erreurs hasardées où le modèle hésite, mais échoue devant les erreurs constantes où il reproduit fidèlement un biais fréquent de ses données d’entraînement : la sévérité (@def:severite) du second avis tombe alors au plus bas.

Après :

> D’abord, comme l’a établi l’étude de la plausibilité au @sec:ch12, réinterroger un même modèle ou des modèles très voisins attrape les erreurs hasardées où le modèle hésite, mais échoue devant les erreurs constantes où il reproduit fidèlement un biais fréquent de ses données d’entraînement. La sévérité (@def:severite) du second avis tombe alors au plus bas.

*Juge :* Coupe au deux-points d’une phrase longue ; « alors » reste rattaché au cas des erreurs constantes, et le renvoi à la sévérité est intact.

### 007 — § « Vérification et validation » (ligne 136) — phrase-longue

Avant :

> Pour les composants spécifiés, la vérification en amont (@sec:ch10) réalise une grande part de ce travail avant la mise en service ; pour les composants appris, la vérification ne subsiste que là où un contrôle mécanique peut être reconstruit autour de la tâche, comme dans Lean [@demoura2021] ou dans le moniteur Simplex [@sha2001].

Après :

> Pour les composants spécifiés, la vérification en amont (@sec:ch10) réalise une grande part de ce travail avant la mise en service. Pour les composants appris, en revanche, la vérification ne subsiste que là où un contrôle mécanique peut être reconstruit autour de la tâche, comme dans Lean [@demoura2021] ou dans le moniteur Simplex [@sha2001].

*Juge :* Coupe au point-virgule ; « en revanche » explicite l’opposition déjà présente entre composants spécifiés et composants appris, et la restriction « ne subsiste que là où » est conservée.

## Rejetées par le juge (3)

### 002 — § « Deux axes plutôt que trois sortes d’incertitude » (ligne 26) — argument

*Juge :* « Or » introduit une nouvelle prémisse ; « pourtant » ajoute une concession, alors que rien dans le paragraphe précédent (concentration des défaillances dans la colonne de droite) n’est contredit par l’opposition des règles de maîtrise.

Avant :

> Or les deux axes de cette matrice obéissent à des règles de maîtrise opposées, représentées sur la @fig:ch13-deux-axes :

Après (non appliqué) :

> Les deux axes de cette matrice obéissent pourtant à des règles de maîtrise opposées, représentées sur la @fig:ch13-deux-axes :

### 003 — § « Deux axes plutôt que trois sortes d’incertitude » (ligne 28) — argument, gain

*Juge :* « ainsi » présente comme une conséquence ce qui précisait le mécanisme en deux temps, et le cumul « ainsi d’abord » alourdit une phrase déjà lisible ; le gain est faible.

Avant :

> Une pertinence nouvelle ne peut entrer que du dehors, par l’avertissement d’un tiers ou par l’épreuve du réel (@sec:ch07-deux-voies) : l’apport extérieur rend d’abord l’omission signalée, et c’est seulement en révisant le cadre qu’on fait entrer sa cause dans la ligne du haut.

Après (non appliqué) :

> Une pertinence nouvelle ne peut entrer que du dehors, par l’avertissement d’un tiers ou par l’épreuve du réel (@sec:ch07-deux-voies). L’apport extérieur rend ainsi d’abord l’omission signalée, et c’est seulement en révisant le cadre qu’on fait entrer sa cause dans la ligne du haut.

### 008 — § « Points clés » (ligne 165) — portee, francais

*Juge :* L’incise « , en revanche, » s’insère entre « ne s’accélère pas » et « par la seule génération automatique » : la restriction se détache et la phrase peut se lire comme une négation absolue (« la validation ne s’accélère pas »). Dans un point clé, ce risque n’est pas acceptable.

Avant :

> - On peut reconstruire une vérification (résoudre correctement le problème posé) autour d’un composant appris là où existe un contrôle mécanique indépendant, mais la validation (poser un problème assez fidèle à la réalité) ne s’accélère pas par la seule génération automatique et reste liée à un apport extérieur au cadre, celui d’une autre discipline ou le contact avec le monde.

Après (non appliqué) :

> - On peut reconstruire une vérification (résoudre correctement le problème posé) autour d’un composant appris là où existe un contrôle mécanique indépendant. La validation (poser un problème assez fidèle à la réalité) ne s’accélère pas, en revanche, par la seule génération automatique et reste liée à un apport extérieur au cadre, celui d’une autre discipline ou le contact avec le monde.

## Rejetées par les contrôles mécaniques (0)

