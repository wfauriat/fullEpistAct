# Journal de la passe de style — `06-detecter-une-erreur`

- Appliqué le 2026-11-20T13:26:12 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 6 · appliquées : 5 · rejetées par le juge : 1 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (5)

### 001 — § « Détecter une erreur : comparateurs et cinq conditions » (ligne 3) — phrase-longue

Avant :

> Le @sec:ch05 a distingué trois sortes d’incertitudes — aléatoire, épistémique et ontologique — et montré qu’une barre d’erreur ne mesure jamais que l’ampleur du désaccord à l’intérieur d’un ensemble d’alternatives admises à l’avance (@prop:desaccord) : ce que le cadre omet, et sur quoi toutes les alternatives admises gardent donc le silence, ne laisse aucune trace chiffrée.

Après :

> Le @sec:ch05 a distingué trois sortes d’incertitudes — aléatoire, épistémique et ontologique — et montré qu’une barre d’erreur ne mesure jamais que l’ampleur du désaccord à l’intérieur d’un ensemble d’alternatives admises à l’avance (@prop:desaccord). Ce que le cadre omet, et sur quoi toutes les alternatives admises gardent donc le silence, ne laisse aucune trace chiffrée.

*Juge :* Coupe au deux-points d’une phrase d’ouverture d’une soixantaine de mots ; « jamais que », « donc » et le renvoi à @prop:desaccord sont conservés, et le lien de conséquence reste lisible, d’autant que la phrase suivante reprend par « donc ».

### 003 — § « Taux d’erreur et probabilité d’échappement » (ligne 67) — phrase-longue

Avant :

> Une équipe ou un système dont le taux d’erreur est modeste peut néanmoins causer de graves dommages si ses erreurs franchissent tous les contrôles sans être arrêtées ; à l’inverse, un outil sujet à des erreurs fréquentes, mais aussitôt interceptées avant la décision, expose à moins de risque qu’un outil plus exact dont les fautes passent sans contradiction.

Après :

> Une équipe ou un système dont le taux d’erreur est modeste peut néanmoins causer de graves dommages si ses erreurs franchissent tous les contrôles sans être arrêtées. À l’inverse, un outil sujet à des erreurs fréquentes, mais aussitôt interceptées avant la décision, expose à moins de risque qu’un outil plus exact dont les fautes passent sans contradiction.

*Juge :* Coupe au point-virgule d’une longue phrase ; « À l’inverse » maintient le parallèle, et le modal « peut », la condition « si » et la comparaison restent intacts.

### 004 — § « Taux d’erreur et probabilité d’échappement » (ligne 73) — phrase-longue

Avant :

> Si l’une quelconque des cinq conditions fait défaut pour cette classe d’erreurs, le contrôle n’a aucune chance d’arrêter les erreurs de cette famille avant qu’elles ne se traduisent en acte : devant lui, leur probabilité d’échappement est égale à $1$, soit 100 %.

Après :

> Si l’une quelconque des cinq conditions fait défaut pour cette classe d’erreurs, le contrôle n’a aucune chance d’arrêter les erreurs de cette famille avant qu’elles ne se traduisent en acte. Devant lui, leur probabilité d’échappement est alors égale à $1$, soit 100 %.

*Juge :* Coupe au deux-points, qui réduit les deux-points en série du paragraphe ; l’ajout de « alors » conserve la portée conditionnelle (« Si l’une quelconque… ») dans la seconde phrase. La répétition de « alors » dans la phrase suivante (« Peu importe alors ») reste une gêne mineure.

### 005 — § « Ce que montrent un désaccord et un accord » (ligne 131) — italique

Avant :

> Pris tel quel, *il ne prouve rien*, à moins que le comparateur n’ait eu une véritable possibilité de contredire l’affirmation si celle-ci avait été fausse.

Après :

> Pris tel quel, il ne prouve rien, à moins que le comparateur n’ait eu une véritable possibilité de contredire l’affirmation si celle-ci avait été fausse.

*Juge :* Retrait d’une italique d’emphase, l’un des défauts visés ; le sens, la négation et la condition « à moins que » sont inchangés.

### 006 — § « Ce que montrent un désaccord et un accord » (ligne 135) — phrase-longue

Avant :

> Un désaccord établi entre grandeurs comparables oblige à chercher l’erreur, puisqu’il démontre qu’un des deux côtés au moins est erroné ; un accord, lui, n’apporte un véritable appui à l’affirmation que dans la mesure où le contrôle courait réellement le risque d’échouer si l’affirmation avait été fausse.

Après :

> Un désaccord établi entre grandeurs comparables oblige à chercher l’erreur, puisqu’il démontre qu’un des deux côtés au moins est erroné. Un accord, lui, n’apporte un véritable appui à l’affirmation que dans la mesure où le contrôle courait réellement le risque d’échouer si l’affirmation avait été fausse.

*Juge :* Coupe au point-virgule d’une phrase d’environ 55 mots ; « lui » maintient l’opposition annoncée par « L’asymétrie est nette », et « puisque », « au moins », « ne… que dans la mesure où » restent en place.

## Rejetées par le juge (1)

### 002 — § « Cinq conditions pour qu’un contrôle arrête une erreur » (ligne 39) — argument

*Juge :* « Or » marque ici une étape du raisonnement (les conditions doivent être réunies ensemble ; or chacune peut céder seule, d’où la fragilité du contrôle). « pourtant » en fait une concession et suggère une contradiction avec la phrase précédente, ce que le texte n’affirme pas.

Avant :

> Or chacune de ces cinq conditions obéit à des mécanismes qui lui sont propres, et elles peuvent céder séparément.

Après (non appliqué) :

> Chacune de ces cinq conditions obéit pourtant à des mécanismes qui lui sont propres, et elles peuvent céder séparément.

## Rejetées par les contrôles mécaniques (0)

