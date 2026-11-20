# Journal de la passe de style — `11-regle-tiree-des-donnees`

- Appliqué le 2026-11-20T13:29:33 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 4 · appliquées : 3 · rejetées par le juge : 1 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (3)

### 002 — § « La spécification passe dans les données » (ligne 23) — formule-creuse

Avant :

> Il serait erroné de voir dans ce déplacement une négligence ou un abandon de rigueur.

Après :

> Ce déplacement ne relève ni d’une négligence ni d’un abandon de rigueur.

*Juge :* La formule impersonnelle « Il serait erroné de voir » est retirée. La négation porte sur les deux mêmes termes, le sens est conservé et l'enchaînement avec la phrase suivante reste intact.

### 003 — § « Le moteur à prédire le fragment suivant » (ligne 31) — phrase-longue

Avant :

> Personne n’a programmé cet escalier de représentations, ni posé entre ces couches des contrats comparables à ceux qui séparent un système de fichiers d’un programme utilisateur (@sec:ch10) : cette organisation a été retenue par l’optimisation uniquement parce qu’elle réduisait l’erreur de prédiction.

Après :

> Personne n’a programmé cet escalier de représentations, ni posé entre ces couches des contrats comparables à ceux qui séparent un système de fichiers d’un programme utilisateur (@sec:ch10). Cette organisation a été retenue par l’optimisation uniquement parce qu’elle réduisait l’erreur de prédiction.

*Juge :* La longue phrase est coupée au deux-points. « Uniquement » et le lien de contraste restent lisibles grâce à la reprise « Cette organisation » ; sens et portée inchangés.

### 004 — § « Fluide et faux sans enfreindre aucune règle » (ligne 51) — phrase-longue

Avant :

> Une réponse prise isolément ne porte en surface aucune marque indiquant que le modèle vient de sortir de son domaine de maîtrise — le @sec:ch12 montrera dans quelles limites la comparaison de plusieurs tirages répétés (plusieurs réponses obtenues pour la même consigne) permet, pour certaines erreurs mais non pour toutes, de repérer une réponse hasardeuse.

Après :

> Une réponse prise isolément ne porte en surface aucune marque indiquant que le modèle vient de sortir de son domaine de maîtrise. Le @sec:ch12 montrera dans quelles limites la comparaison de plusieurs tirages répétés (plusieurs réponses obtenues pour la même consigne) permet, pour certaines erreurs mais non pour toutes, de repérer une réponse hasardeuse.

*Juge :* La phrase est coupée au tiret. La première proposition était déjà absolue, et la seconde garde toutes ses restrictions (« dans quelles limites », « pour certaines erreurs mais non pour toutes ») ainsi que la glose entre parenthèses.

## Rejetées par le juge (1)

### 001 — § « La spécification passe dans les données » (ligne 19) — gain, argument

*Juge :* Remplacer le deux-points par « car » n'apporte qu'un gain marginal sur une phrase qui fonctionnait déjà. La retouche rompt en outre le parallèle voulu entre « En premier lieu disparaît… : » et « En second lieu disparaît la lisibilité : », qui structure les deux volets du prix payé.

Avant :

> En premier lieu disparaît la garantie préalable qu’offrait un composant conforme à la @def:composant-specifie : l’ajustement numérique contraint les paramètres à s’accorder aux exemples d’entraînement — que l’on contrôle ensuite sur des échantillons d’essai tirés d’une source semblable —, et non à satisfaire un invariant démontré pour toute entrée concevable.

Après (non appliqué) :

> En premier lieu disparaît la garantie préalable qu’offrait un composant conforme à la @def:composant-specifie, car l’ajustement numérique contraint les paramètres à s’accorder aux exemples d’entraînement — que l’on contrôle ensuite sur des échantillons d’essai tirés d’une source semblable —, et non à satisfaire un invariant démontré pour toute entrée concevable.

## Rejetées par les contrôles mécaniques (0)

