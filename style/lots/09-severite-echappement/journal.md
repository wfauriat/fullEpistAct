# Journal de la passe de style — `09-severite-echappement`

- Appliqué le 2026-11-20T13:27:20 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 4 · appliquées : 2 · rejetées par le juge : 2 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (2)

### 001 — § « Sévérité d’un contrôle » (ligne 52) — phrase-longue

Avant :

> Un second calcul mené par un collègue avec les mêmes hypothèses de la résistance des matériaux exerce un contrôle sévère contre les fautes d’algèbre ou d’unité, car il les aurait repérées ; sa sévérité est nulle contre un mécanisme de dégradation absent des deux cadres.

Après :

> Un second calcul mené par un collègue avec les mêmes hypothèses de la résistance des matériaux exerce un contrôle sévère contre les fautes d’algèbre ou d’unité, car il les aurait repérées. Sa sévérité est en revanche nulle contre un mécanisme de dégradation absent des deux cadres.

*Juge :* Coupe au point-virgule ; « en revanche » rend explicite le contraste déjà présent (sévère contre une classe d’erreurs, nulle contre une autre). Sens, portée (« nulle ») et termes inchangés.

### 003 — § « Ce que l’on fait des alertes » (ligne 80) — phrase-longue

Avant :

> James Bliss, Richard Gilson et John Deaton [@bliss1995] ont montré que, placés devant des alarmes dont la fiabilité varie, la plupart des opérateurs ajustent la fréquence à laquelle ils réagissent à la fiabilité perçue du signal : si une alarme ne correspond à un danger réel que dans une fraction modérée des cas, ils ne la vérifient qu’environ à cette fréquence.

Après :

> James Bliss, Richard Gilson et John Deaton [@bliss1995] ont montré que, placés devant des alarmes dont la fiabilité varie, la plupart des opérateurs ajustent la fréquence à laquelle ils réagissent à la fiabilité perçue du signal. Ainsi, si une alarme ne correspond à un danger réel que dans une fraction modérée des cas, ils ne la vérifient qu’environ à cette fréquence.

*Juge :* Coupe d’une phrase longue au deux-points ; « Ainsi » introduit l’instanciation du résultat de [@bliss1995] sans changer le mécanisme ni la portée (« la plupart », « environ », « fraction modérée » conservés).

## Rejetées par le juge (2)

### 002 — § « Le piège des fausses alertes » (ligne 56) — argument, terme

*Juge :* « c’est-à-dire qu’il se trompe » est une glose qui précise une hypothèse (taux d’erreur symétrique) ; « Il se trompe ainsi » en fait une conséquence de « commet une erreur dans 10 % des cas », alors que cette symétrie ne s’en déduit pas.

Avant :

> Imaginons un producteur très fiable qui ne se trompe que dans 1 % des cas, et un relecteur humain ou logiciel qui commet une erreur d’appréciation dans 10 % des cas, indépendamment du producteur — c’est-à-dire qu’il se trompe dans 10 % des cas aussi bien lorsqu’il juge une affirmation juste (10 % de fausses alertes) que lorsqu’il examine une affirmation fausse (10 % d’oubli).

Après (non appliqué) :

> Imaginons un producteur très fiable qui ne se trompe que dans 1 % des cas, et un relecteur humain ou logiciel qui commet une erreur d’appréciation dans 10 % des cas, indépendamment du producteur. Il se trompe ainsi dans 10 % des cas aussi bien lorsqu’il juge une affirmation juste (10 % de fausses alertes) que lorsqu’il examine une affirmation fausse (10 % d’oubli).

### 004 — § « Points clés » (ligne 189) — argument, sens

*Juge :* « pousse ainsi » fait de l’appariement des probabilités une conséquence de ce que fixe la règle de Bayes, alors que le chapitre insiste sur le fait qu’il s’agit d’un comportement qui n’en découle pas ; le deux-points marquait une explicitation, non un lien causal.

Avant :

> - La règle de Bayes fixe la valeur prédictive positive, non la prise en compte : l’appariement des probabilités pousse les opérateurs à négliger des alertes peu fiables, alors que résoudre un désaccord par un tiers est une décision d’utilité espérée qui paie lorsque les enjeux sont élevés (décision unique, perte très supérieure au coût de la contre-expertise).

Après (non appliqué) :

> - La règle de Bayes fixe la valeur prédictive positive, non la prise en compte. L’appariement des probabilités pousse ainsi les opérateurs à négliger des alertes peu fiables, alors que résoudre un désaccord par un tiers est une décision d’utilité espérée qui paie lorsque les enjeux sont élevés (décision unique, perte très supérieure au coût de la contre-expertise).

## Rejetées par les contrôles mécaniques (0)

