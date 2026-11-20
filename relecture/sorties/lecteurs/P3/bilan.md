# Bilan — P3

## 1. Ce que j'ai compris

La partie III applique la théorie des contrôles à la pile informatique. En informatique classique, chaque couche est une promesse écrite (contrat, pré/postconditions). On peut donc vérifier un composant une fois en amont, et toute défaillance a une « adresse », y compris celles qui passent longtemps inaperçues (Mars Climate Orbiter). L'apprentissage automatique déplace la spécification vers les données et l'objectif : on gagne en portée, on perd la garantie préalable et la lisibilité. Un modèle de langage optimisé pour la plausibilité peut être fluide et faux sans enfreindre de contrat (Mata v. Avianca), et l'on ne fait qu'« orienter » le modèle, jamais le spécifier. Au sommet de la pile, trois choses basculent ensemble : la promesse, la forme de l'échec et le lieu de l'enquête. La compétence suit une frontière en dents de scie. La calibration générative force l'invention de faits rares (borne de Kalai et Vempala). Reposer la question démasque les erreurs hasardées mais pas les erreurs constantes. Le chapitre 13 croise lieu de la cause (dans/hors du cadre) et présence d'un comparateur (signalée/silencieuse). Il distingue quatre sources de comparateurs et la vérification (bien résoudre) de la validation (bien poser). Les composants appris peuplent la case « dans le cadre et silencieuse », que les composants spécifiés permettent de vider à l'avance.

## 2. Impression d'ensemble

Forces : construction très lisible, annonces tenues, exemple de Mars Climate Orbiter bien choisi, lien constant avec la partie II, et calculs de l'exemple quantitatif du chapitre 12 que j'ai refaits et trouvés exacts (11,5 % ; 99,9 % ; 42,0 %). Le texte principal se suit sans les encadrés, hors le point signalé ci-dessous.

Principaux problèmes, par ordre d'importance :
1. Les redites : Mars Climate Orbiter revient sur l'ensemble de la partie, avec deux encadrés qui redisent le texte principal (P3-006, P3-007, P3-024), et BCG est raconté deux fois (P3-015).
2. L'extension du « cadre » aux modèles de langage (« le domaine courant, la consigne ») sur laquelle repose la matrice du chapitre 13, et le flou sur le terme « omission » appliqué à la saillance (P3-023, P3-017).
3. La page d'ouverture durcit les chapitres : erreurs « d'un type nouveau » et composants spécifiés qui « excluent » ces erreurs (P3-001, P3-002), alors que le chapitre 13 nuance. S'y ajoute l'axe du changement de régime, dont la formulation (absence de spécification) ne distingue pas les modèles de langage des filtres antipourriels cités en 12.2 (P3-013).
4. Définition 11 et adresse : « spécifié » oscille entre « écrit à l'avance » et « formulable après coup », ce qui rend l'adresse presque non réfutable (P3-003, P3-004). Le tableau 13.2 idéalise ensuite la colonne des composants spécifiés (P3-027).
5. Statut des résultats : la borne de Kalai et Vempala est durcie dans le point clé (P3-019) et l'exemple illustratif est cité comme « établi » au chapitre 13 (P3-022). L'interprétation de l'exemple (« la répétition attrape efficacement ») ignore que l'alerte sonne presque toujours (P3-020).

## 3. Ce que j'ai dû prendre sur parole

- Les propositions 2, 3, 4, 5 et les définitions 2, 5, 6, 7, 8, 9, 10 des chapitres 2 à 9, y compris la fermeture du cadre (proposition 3, volet (a)), le « modèle M3 » et le tableau 8.1.
- Les chiffres et l'épisode de la ferrure (facteur 1,8), la corrélation hypothécaire d'avant 2008 et la fissure du mât du voilier, évoqués dans le tableau 13.1.
- Les sources externes citées (Kalai et Vempala, Farquhar, Dell'Acqua, Stockman et al., Sha, Moura et Ullrich, nostalgebraist) : je n'ai pas pu les consulter.
- Le contenu des chapitres 14 à 16 annoncés en fin de partie.

## 4. Questions hors périmètre

- Les chapitres 6 et 8 disent-ils bien que « comparateur » compte trois familles ? Le chapitre 13 prétend les avoir « annoncées » en quatre.
- Les glossaires situent « arrière-plan tacite » au chapitre 1 : le chapitre 11 renvoie au chapitre 2.
- La proposition 3 (volet a) est-elle formulée en termes de facteur absent du cadre ? Dans l'affirmative, la saillance relève de la nuance du chapitre 7 « annoncée » en 12.3.
- Le chapitre 9 établit-il bien que « un producteur dont le taux d'erreur diminue mais dont les erreurs échappent aux contrôles peut former un système plus risqué » (invoqué en 12.1) ?
- Les chapitres 8 et 7 contiennent-ils les récits déjà annoncés de Mars Climate Orbiter, de la ferrure et de Google Flu Trends ? S'ils les détaillent, la redite se confirme.

## 5. Limites de ma lecture

Je n'ai lu que la partie III et le fichier de référence. Les renvois aux chapitres antérieurs ou postérieurs n'ont donc pu être vérifiés que par le glossaire et la notation. Mes remarques sur les sources externes (Russell, McCarthy et Hayes, billet de blog sur le logit lens) reposent sur ma mémoire et sont de confiance basse. Je n'ai pas vu les figures (12.1 et 13.1) : je n'ai jugé que leurs légendes. Les calculs du tableau 12.1 ont été refaits ; je n'ai pas contrôlé les autres chiffres cités.
