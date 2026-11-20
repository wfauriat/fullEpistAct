# Journal de la passe de style — `14-chaines-qui-agissent`

- Appliqué le 2026-11-20T13:31:47 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 9 · appliquées : 5 · rejetées par le juge : 4 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (5)

### 001 — § « Des *pipelines* d’IA comme chaînes orchestrées » (ligne 11) — phrase-longue

Avant :

> Mais cette division du travail se heurte immédiatement à la même tension que celle observée dans les grands ensembles d’ingénierie (@sec:ch08-composer), portée ici à un degré supérieur : plus l’objectif assigné au *pipeline* se situe haut dans la hiérarchie des finalités — « refactoriser ce dépôt logiciel », « instruire et régler ce litige client », « préparer ce dossier réglementaire à partir d’une liasse de pièces » —, moins cet objectif se laisse enfermer dans un énoncé formel vérifiable d’avance.

Après :

> Mais cette division du travail se heurte immédiatement à la même tension que celle observée dans les grands ensembles d’ingénierie (@sec:ch08-composer), portée ici à un degré supérieur. Plus l’objectif assigné au *pipeline* se situe haut dans la hiérarchie des finalités — « refactoriser ce dépôt logiciel », « instruire et régler ce litige client », « préparer ce dossier réglementaire à partir d’une liasse de pièces » —, moins cet objectif se laisse en effet enfermer dans un énoncé formel vérifiable d’avance.

*Juge :* Coupe au deux-points d’une phrase longue chargée d’une énumération entre tirets ; « en effet » rend explicite le lien explicatif que portait le deux-points ; corrélation « plus… moins » et renvoi intacts.

### 003 — § « Des *pipelines* d’IA comme chaînes orchestrées » (ligne 18) — formule-creuse

Avant :

> Il serait toutefois inexact d’affirmer que tout *pipeline* est condamné par nature à demeurer une chaîne aveugle.

Après :

> Tout *pipeline* n’est toutefois pas condamné par nature à demeurer une chaîne aveugle.

*Juge :* Retire la formule creuse « Il serait inexact d’affirmer que » ; la négation partielle « Tout pipeline n’est pas » conserve la portée, et « toutefois » maintient la concession.

### 006 — § « Le blanchiment dans les chaînes d’IA » (ligne 88) — phrase-longue

Avant :

> Dans les *pipelines* et les boucles d’agents fondés sur des modèles de langage, le blanchiment change de matière première et devient presque systématique : ce ne sont plus seulement des tableaux de flottants qui traversent les frontières sans étiquettes, mais des *chaînes de caractères nues* — des paragraphes de texte libre, des résumés ou des champs textuels — qui voyagent d’une étape à l’autre dépouillés de leurs hypothèses, de leur origine et de leur incertitude.

Après :

> Dans les *pipelines* et les boucles d’agents fondés sur des modèles de langage, le blanchiment change de matière première et devient presque systématique. Ce ne sont plus seulement des tableaux de flottants qui traversent les frontières sans étiquettes, mais des *chaînes de caractères nues* — des paragraphes de texte libre, des résumés ou des champs textuels — qui voyagent d’une étape à l’autre dépouillés de leurs hypothèses, de leur origine et de leur incertitude.

*Juge :* Coupe au deux-points d’une phrase longue ; « presque systématique », « seulement » et la triade « hypothèses, origine, incertitude » sont conservés.

### 007 — § « Le blanchiment dans les chaînes d’IA » (ligne 93) — phrase-longue

Avant :

> Entraîné à produire une prose fluide, cohérente et plausible (@sec:ch11), le modèle lisse les aspérités : il gomme les réserves (« valable uniquement avant la version 3 », « sous réserve de vérification comptable »), efface les désaccords entre deux pièces en choisissant une formulation médiane qui paraît consensuelle, et omet d’indiquer si telle affirmation était directement écrite dans la source ou reconstruite par conjecture (@sec:ch12).

Après :

> Entraîné à produire une prose fluide, cohérente et plausible (@sec:ch11), le modèle lisse les aspérités. Il gomme ainsi les réserves (« valable uniquement avant la version 3 », « sous réserve de vérification comptable »), efface les désaccords entre deux pièces en choisissant une formulation médiane qui paraît consensuelle, et omet d’indiquer si telle affirmation était directement écrite dans la source ou reconstruite par conjecture (@sec:ch12).

*Juge :* Coupe au deux-points ; « ainsi » marque la manière dont le modèle « lisse les aspérités » sans ajouter de cause ; les trois effets énumérés et les renvois sont intacts.

### 009 — § « Points clés » (ligne 130) — phrase-longue

Avant :

> - Même lorsque des contrôles croisés indépendants à chaque étape réduisent fortement les erreurs locales le long d’une longue trajectoire, ils laissent intact tout facteur omis que partagent l’agent et ses contrôleurs, et qui pèse sur toute la trajectoire, qui finit par intervenir dans une large part des défaillances restantes.

Après :

> - Même lorsque des contrôles croisés indépendants à chaque étape réduisent fortement les erreurs locales le long d’une longue trajectoire, ils laissent intact tout facteur omis que partagent l’agent et ses contrôleurs et qui pèse sur toute la trajectoire ; ce facteur finit alors par intervenir dans une large part des défaillances restantes.

*Juge :* Corrige la double relative fautive (« et qui pèse…, qui finit par ») ; « alors » renvoie à la condition « Même lorsque… réduisent fortement », et « tout », « large part » et « défaillances restantes » sont conservés.

## Rejetées par le juge (4)

### 002 — § « Des *pipelines* d’IA comme chaînes orchestrées » (ligne 15) — argument, gain

*Juge :* « Le premier module livre ainsi un texte plausible » présente la plausibilité de la sortie comme une conséquence de l’absence de spécification, alors qu’elle tient à la nature du composant appris (@sec:ch11) ; la phrase d’origine, de longueur raisonnable, fonctionnait déjà.

Avant :

> Entre deux étapes d’un *pipeline* d’intelligence artificielle, aucune spécification formelle n’encadre le sens de la sortie produite par l’étape qui extrait ou par celle qui résume : le premier module livre un texte plausible (@sec:ch11), et le second l’accepte tant qu’il paraît grammaticalement et syntaxiquement bien formé.

Après (non appliqué) :

> Entre deux étapes d’un *pipeline* d’intelligence artificielle, aucune spécification formelle n’encadre le sens de la sortie produite par l’étape qui extrait ou par celle qui résume. Le premier module livre ainsi un texte plausible (@sec:ch11), et le second l’accepte tant qu’il paraît grammaticalement et syntaxiquement bien formé.

### 004 — § « Un danger structurel : la chaîne à $N$ maillons » (ligne 28) — argument

*Juge :* « Or » introduit ici la prémisse qui applique l’@eq:ch08-chaine-angle-mort à l’agent ; « Mais » en fait une objection au fait que l’agent allonge la chaîne, ce qui change le lien logique pour un simple échange de connecteur.

Avant :

> Or, d’après l’@eq:ch08-chaine-angle-mort, l’angle mort d’une chaîne contient la réunion des angles morts de toutes ses étapes, augmentée des défauts qui naissent aux interfaces.

Après (non appliqué) :

> Mais, d’après l’@eq:ch08-chaine-angle-mort, l’angle mort d’une chaîne contient la réunion des angles morts de toutes ses étapes, augmentée des défauts qui naissent aux interfaces.

### 005 — § « Un danger opérationnel : des réponses aux actions » (ligne 45) — argument

*Juge :* Le deux-points énonçait le mécanisme lui-même ; avec « suffit en effet », la phrase suivante devient la justification de « L’épisode isole… », ce qui déplace son rôle, pour un gain de lecture faible.

Avant :

> L’épisode isole néanmoins dans toute sa pureté le mécanisme opérationnel à l’œuvre ici : dès qu’un logiciel agit directement à la vitesse de la machine sur un environnement réel, le décalage entre la cadence d’exécution et le délai de prise en compte humaine suffit à rendre les dégâts massifs avant qu’un contrôle extérieur n’intervienne.

Après (non appliqué) :

> L’épisode isole néanmoins dans toute sa pureté le mécanisme opérationnel à l’œuvre ici. Dès qu’un logiciel agit directement à la vitesse de la machine sur un environnement réel, le décalage entre la cadence d’exécution et le délai de prise en compte humaine suffit en effet à rendre les dégâts massifs avant qu’un contrôle extérieur n’intervienne.

### 008 — § « Le blanchiment dans les chaînes d’IA » (ligne 104) — argument

*Juge :* « pourtant » introduit une opposition absente : une interface permissive qui laisse tout passer et la destruction de la comparabilité vont dans le même sens, la seconde prolongeant la première.

Avant :

> Or ce passage en texte nu détruit la *comparabilité* entre étapes.

Après (non appliqué) :

> Ce passage en texte nu détruit pourtant la *comparabilité* entre étapes.

## Rejetées par les contrôles mécaniques (0)

