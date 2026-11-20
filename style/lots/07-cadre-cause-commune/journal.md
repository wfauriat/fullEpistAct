# Journal de la passe de style — `07-cadre-cause-commune`

- Appliqué le 2026-11-20T13:26:31 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 6 · appliquées : 2 · rejetées par le juge : 4 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (2)

### 002 — § « Quand les observations révèlent un manque du cadre » (ligne 91) — phrase-longue

Avant :

> Et même s’il agit sur des boîtiers réels où la couleur varie et détermine l’explosion, l’automate continuera d’ignorer qu’il existe des couleurs : à une position donnée, il ne constatera qu’une dispersion inexpliquée entre succès et échecs, sans aucun concept pour attribuer cette variabilité à la teinte du fil.

Après :

> Et même s’il agit sur des boîtiers réels où la couleur varie et détermine l’explosion, l’automate continuera d’ignorer qu’il existe des couleurs. À une position donnée, il ne constatera en effet qu’une dispersion inexpliquée entre succès et échecs, sans aucun concept pour attribuer cette variabilité à la teinte du fil.

*Juge :* La phrase longue est coupée au deux-points. « en effet » garde le lien explicatif de l’original. Le sens, la portée (« ne… qu’ », « sans aucun concept ») et l’exemple de l’automate sont inchangés.

### 005 — § « La régression à l’infini des méta-procédures » (ligne 115) — phrase-longue

Avant :

> Dire qu’aucune méta-procédure n’échappe à la régression à l’infini ne signifie pas que les outils formels soient inutiles, ni que tous les cadres se valent : certains cadres décrivent manifestement le réel bien mieux que d’autres, et les tests de diagnostic à un étage supérieur attrapent des défauts bien réels qu’ils ont été conçus pour chercher.

Après :

> Dire qu’aucune méta-procédure n’échappe à la régression à l’infini ne signifie pas que les outils formels soient inutiles, ni que tous les cadres se valent. Certains cadres décrivent manifestement le réel bien mieux que d’autres, et les tests de diagnostic à un étage supérieur attrapent des défauts bien réels qu’ils ont été conçus pour chercher.

*Juge :* La longue phrase est coupée au deux-points. Juxtaposées, les deux phrases gardent le lien de justification. La double négation, « manifestement » et l’énumération sont intacts.

## Rejetées par le juge (4)

### 001 — § « Le cadre comme cause commune » (ligne 74) — portee, gain

*Juge :* L’ajout de « ainsi » rattache au seul cas de la fiche de chantier une règle que l’original énonce en général (« dès qu’il s’appuie sur un élément absent de $x$ »). La phrase, de longueur modérée, se lisait déjà bien : le gain est faible.

Avant :

> Un ingénieur chargé de relire à la main le calcul de la ferrure peut consulter la fiche de chantier où figure, en marge, l’implantation côtière de l’ouvrage : dès qu’il s’appuie sur un élément absent de $x$, il cesse d’être un comparateur purement interne.

Après (non appliqué) :

> Un ingénieur chargé de relire à la main le calcul de la ferrure peut consulter la fiche de chantier où figure, en marge, l’implantation côtière de l’ouvrage. Dès qu’il s’appuie ainsi sur un élément absent de $x$, il cesse d’être un comparateur purement interne.

### 003 — § « La régression à l’infini des méta-procédures » (ligne 109) — registre, francais

*Juge :* Une phrase ouverte par « Car » est une construction déconseillée dans la prose académique : la retouche remplace un deux-points par un autre tic, sans gain net.

Avant :

> L’objection est juste dans le périmètre strict du théorème, mais elle confirme le propos au lieu de le lever : une procédure ne devient efficace qu’à l’instant où elle renonce à l’universalité en restreignant la classe de problèmes qu’elle vise, et poser cette restriction revient précisément à choisir un cadre [@fauriat2026frame].

Après (non appliqué) :

> L’objection est juste dans le périmètre strict du théorème, mais elle confirme le propos au lieu de le lever. Car une procédure ne devient efficace qu’à l’instant où elle renonce à l’universalité en restreignant la classe de problèmes qu’elle vise, et poser cette restriction revient précisément à choisir un cadre [@fauriat2026frame].

### 004 — § « La régression à l’infini des méta-procédures » (ligne 113) — argument

*Juge :* Dans l’original, « retenir les catégories pertinentes… précède l’inférence » est la leçon tirée de l’exemple « vleu ». Avec « en effet », cette conclusion devient la justification de la phrase qui précède, ce qui inverse le sens de l’argument.

Avant :

> Aucun procédé purement formel appliqué aux données passées ne désigne à lui seul « vert » plutôt que « *vleu* » : retenir les catégories pertinentes — c’est-à-dire choisir les variables et le découpage du cadre — précède l’inférence et ne peut jamais être tiré de rien.

Après (non appliqué) :

> Aucun procédé purement formel appliqué aux données passées ne désigne à lui seul « vert » plutôt que « *vleu* ». Retenir les catégories pertinentes — c’est-à-dire choisir les variables et le découpage du cadre — précède en effet l’inférence et ne peut jamais être tiré de rien.

### 006 — § « Comment une pertinence nouvelle entre dans un cadre » (ligne 124) — argument, francais

*Juge :* Après la coupe, « Il ne découvre en effet » renvoie au « système qui se contenterait d’exploiter », alors que ce système n’essaie justement rien de nouveau. On passe en outre du conditionnel à l’indicatif, et la seconde proposition, parallèle dans l’original, devient une justification qui se détache de ce que la phrase attribue à Sutton et Barto.

Avant :

> 2. *Découvrir par l’épreuve.* En agissant sur le monde et en mettant nos attentes au contact du terrain, nous laissons la réalité non modélisée opposer un démenti concret à nos prévisions (@sec:ch02). En apprentissage par renforcement, Richard Sutton et Andrew Barto placent ainsi l’*exploration* au cœur de toute adaptation [@sutton2018] : un système qui se contenterait d’exploiter ce que sa représentation courante estime optimal resterait enfermé dans ses omissions initiales ; il ne découvre de nouveaux mécanismes qu’en essayant des actions dont il ne maîtrise pas encore l’issue.

Après (non appliqué) :

> 2. *Découvrir par l’épreuve.* En agissant sur le monde et en mettant nos attentes au contact du terrain, nous laissons la réalité non modélisée opposer un démenti concret à nos prévisions (@sec:ch02). En apprentissage par renforcement, Richard Sutton et Andrew Barto placent ainsi l’*exploration* au cœur de toute adaptation [@sutton2018] : un système qui se contenterait d’exploiter ce que sa représentation courante estime optimal resterait enfermé dans ses omissions initiales. Il ne découvre en effet de nouveaux mécanismes qu’en essayant des actions dont il ne maîtrise pas encore l’issue.

## Rejetées par les contrôles mécaniques (0)

