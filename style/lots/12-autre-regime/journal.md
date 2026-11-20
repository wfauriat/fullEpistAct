# Journal de la passe de style — `12-autre-regime`

- Appliqué le 2026-11-20T13:30:24 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 3 · appliquées : 3 · rejetées par le juge : 0 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (3)

### 001 — § « Trois propriétés basculent ensemble » (ligne 22) — phrase-longue

Avant :

> Ce qui sépare néanmoins ce cas du sommet de la pile tient au fait que la faute demeurait *définissable* : il existait un contrat d’interface écrit, et un comparateur mécanique vérifiant les unités aurait pu être écrit et appliqué une fois pour toutes au composant ou à l’interface.

Après :

> Ce qui sépare néanmoins ce cas du sommet de la pile tient au fait que la faute demeurait *définissable*. Il existait en effet un contrat d’interface écrit, et un comparateur mécanique vérifiant les unités aurait pu être écrit et appliqué une fois pour toutes au composant ou à l’interface.

*Juge :* Le deux-points explicatif devient une coupe articulée par « en effet », qui garde le lien de justification. « demeurait », « aurait pu » et « une fois pour toutes » sont conservés, et la phrase d’environ 50 mots est allégée.

### 002 — § « Vérifier la couche ou contrôler les sorties » (ligne 38) — phrase-longue

Avant :

> Tant que ce déplacement n’est pas opéré — c’est-à-dire tant qu’un système en aval consomme la sortie d’un modèle comme une chaîne de caractères fiable, à la manière d’un résultat issu d’une couche spécifiée —, la chaîne entière (@sec:ch08) hérite d’un angle mort qui n’existait pas au même degré dans les couches inférieures : l’interface demeure aussi lisse qu’avant, mais la garantie qui la soutenait en dessous s’est retirée.

Après :

> Tant que ce déplacement n’est pas opéré — c’est-à-dire tant qu’un système en aval consomme la sortie d’un modèle comme une chaîne de caractères fiable, à la manière d’un résultat issu d’une couche spécifiée —, la chaîne entière (@sec:ch08) hérite d’un angle mort qui n’existait pas au même degré dans les couches inférieures. L’interface demeure en effet aussi lisse qu’avant, mais la garantie qui la soutenait en dessous s’est retirée.

*Juge :* La phrase d’environ 70 mots est coupée au deux-points, et « en effet » garde le lien explicatif. La condition « Tant que » porte toujours sur l’angle mort hérité. La phrase détachée, qui décrit l’interface lisse et la garantie retirée, n’était pas conditionnelle dans l’original, car elle explique cet angle mort.

### 003 — § « Calibration générative, longue traîne et erreurs constantes » (ligne 84) — phrase-longue

Avant :

> Alors que la calibration examinée au @sec:ch03 porte sur l’accord entre les probabilités annoncées et les fréquences observées, on appelle **calibration générative** l’accord entre la distribution des énoncés produits par un modèle et la distribution de ses données d’entraînement ; loin de prémunir contre l’invention, cette propriété entraîne mécaniquement l’invention de faits rares.

Après :

> Alors que la calibration examinée au @sec:ch03 porte sur l’accord entre les probabilités annoncées et les fréquences observées, on appelle **calibration générative** l’accord entre la distribution des énoncés produits par un modèle et la distribution de ses données d’entraînement. Loin de prémunir contre l’invention, cette propriété entraîne mécaniquement l’invention de faits rares.

*Juge :* La coupe au point-virgule sépare la définition de la calibration générative de sa conséquence. Le contraste « Alors que », le terme en gras, « mécaniquement » et « faits rares » sont intacts, et la phrase d’environ 60 mots gagne en lisibilité.

## Rejetées par le juge (0)

## Rejetées par les contrôles mécaniques (0)

