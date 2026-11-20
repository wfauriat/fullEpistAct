# Bilan — C

*Lecteur cible, lecture intégrale et linéaire de l'avant-propos à la conclusion (26 fichiers), journal tenu fichier par fichier (`journal.md`), 59 constats (`constats.json` : 2 A, 21 B, 36 C).*

## 1. Ce que j'ai compris

Nous agissons toujours d'après une représentation finie, construite dans un cadre (variables, catégories, classe de modèles, objectif) qui laisse un arrière-plan tacite ouvert. Le monde, lui, répond à l'action. Aucune rigueur interne ne certifie ce cadre. Une barre d'erreur ne mesure que le désaccord entre alternatives admises, et tous les contrôles calculés dans le cadre partagent avec lui une cause commune. Une erreur n'est arrêtée que par un comparateur qui existe, se trompe autrement, reste comparable, arrive à temps et trouve quelqu'un qui l'écoute et a l'autorité d'agir. Une chaîne cumule les angles morts, un contrôle croisé ne garde que les angles morts communs, et le blanchiment aux interfaces ramène l'un à l'autre. Le risque se décompose en taux d'erreur × probabilité d'échappement, et les évaluations courantes ne mesurent que le premier facteur. L'informatique classique a gagné sa fiabilité par des contrats vérifiables en amont, qui donnent une adresse aux défaillances. Les modèles appris dépensent cette garantie pour gagner en portée : leurs erreurs sont fluides, sans adresse, « dans le cadre et silencieuses ». L'automatisation chaîne les étapes jusqu'à l'action, efface les contrôles implicites (friction, signe révélateur, signal coûteux) et corrèle les angles morts via un « prêteur unique ». Réponse du livre : marge d'humilité et verrou pour les décisions uniques, bac à sable pour explorer, quatre questions devant tout chiffre assuré, et trois niveaux de défense (attitude, placement, organisation) dont la capacité d'évaluation est la ressource rare, à mesurer par erreurs injectées.

## 2. Impression d'ensemble

### Ma lecture en une page

La thèse m'a largement convaincu, et c'est un livre dont je retiendrai des outils. Le tableau 8.1 (échelle des comparateurs), la grille des cinq conditions, la matrice à deux axes du ch. 13 (« la formalité change la colonne, non la ligne »), la distinction vérification/validation appliquée à ce que l'IA accélère ou non, les deux conditions d'un contrôle croisé humain-modèle (ch. 15), le critère « quelle erreur cette étape peut-elle arrêter que le producteur n'aurait pas pu arrêter lui-même ? » (ch. 18) : tout cela est utilisable demain matin. La prose est claire, les exemples bien choisis, les calculs justes (je les ai tous refaits : tableaux 1.1, 3.1, 4.1, 8.2, 9.1-9.4, 12.1, 14.1, 16.1, 17.2). L'honnêteté épistémique est remarquable : Nuances qui corrigent les raccourcis (Challenger, Moffatt, « la règle de Bayes ne fixe pas la prise en compte »), conclusion qui expose les points faibles.

Ce qui m'a laissé sceptique tient en trois points.
(1) L'« énigme » qui ouvre le livre, « producteur plus fiable, système plus risqué » (0.5.4), m'a été vendue comme l'idée-force. Le seul modèle formel qui la traite (ch. 16) donne pourtant, avec ses propres paramètres, l'effet inverse : le risque baisse avec le modèle partagé. Le livre finit par le reconnaître (ch. 9 Nuance, conclusion), mais trop tard (C-003).
(2) La distinction centrale entre erreur *dans* le cadre et facteur *omis* est brouillée par l'exemple même qui doit l'illustrer, la roulette russe (C-001). Elle devient de plus floue pour les composants appris, faute de dire de quel cadre on parle (C-015).
(3) Le livre est long parce qu'il redit. Le ch. 0 expose presque toute la thèse, avec les mêmes exemples et souvent les mêmes phrases. Puis chaque cas (ébullition, ferrure, Mars Climate Orbiter, M. X / M. Y, METR, Mata, Challenger) est raconté de nouveau en détail, et chaque chapitre s'ouvre et se ferme sur des récapitulatifs, en plus des Points clés et des introductions de partie (C-019 à C-022).

### Les chapitres les plus forts et les plus faibles

- **Les plus forts :** le ch. 13 (synthèse : matrice, quatre sources, Lean, Simplex, vérification/validation), le ch. 12 (changement de régime, omission de saillance, calibration générative, répétition), le ch. 15 (friction, signe révélateur, signal coûteux, Bainbridge, deux pièges de la consigne), le ch. 8 (tableau 8.1, Knight et Leveson, blanchiment) et le ch. 18 (placement, RAG comme outil de placement, erreurs injectées « venues d'un autre cadre »). Le ch. 4 est le plus pédagogique.
- **Les plus faibles :** le ch. 14 (une grande part de 14.1 et de l'exemple 14.2.3 duplique 8.4 et 8.2 ; seuls 14.2.2, 14.3 et 14.4 sont neufs), le ch. 2 (quatrième récit de l'ébullition, étude de cas imaginaire, huit autocitations), le ch. 10 (Mars Climate Orbiter raconté deux fois de suite) et le ch. 7, dont le volet (a) de la proposition 3 est presque tautologique une fois M3 posé, et dont le volet (b) n'est pas démontré (C-014).

### Ce que je couperais et ce qui m'a manqué

- **Je couperais :** les récits répétés (garder un seul récit complet de chaque cas et des renvois d'une ligne ailleurs) ; au ch. 0, les encadrés METR et le détail de Mata, qui seront développés plus loin ; 14.1 (renvoi à 8.4) et la moitié de 14.2.3 ; le récit de Mars Climate Orbiter en 10.5 ; la Nuance Challenger du ch. 5 ; la reprise de la Genèse dans la conclusion ; plusieurs Noyaux formels qui redisent le texte qui les précède (M1 au ch. 9, M2 au ch. 17) ; la moitié des récapitulatifs d'ouverture et de fermeture de chapitre.
- **Il m'a manqué :** (a) une colonne du tableau 16.1 où le risque monte vraiment ; (b) la discussion de la parade classique de l'hypothèse « fourre-tout » dans Θ, que la marge d'humilité rappelle beaucoup (C-013) ; (c) l'entraînement par renforcement sur récompenses vérifiables, qui place un comparateur mécanique dans l'objectif même du modèle (C-044) ; (d) un vrai cas documenté de dérive de modèle clinique (C-011) ; (e) un exemple de facteur omis qui soit réellement hors du cadre pour la roulette ; (f) une seule mesure, même modeste, d'échappement par erreurs injectées dans un flux de relecture, puisque tout le dispositif final en dépend.

### La conclusion est-elle méritée ?

Oui, largement. C'est la meilleure partie du livre du point de vue de la méthode. Elle classe chaque affirmation par statut et point faible, nomme six tensions, liste des observations qui affaibliraient l'argument, admet que l'exemple du ch. 16 contredit l'énigme du ch. 0 et que l'axe « dans/hors du cadre » devient « une affaire de degré » pour les composants appris. Deux réserves. Elle affirme une cohérence interne (« termes fixés, renvois tenus ») que ma lecture dément sur des points précis (C-058). Et elle reconnaît en dernier ce que le ch. 0 aurait dû dire en premier : l'énigme est une possibilité, non une fréquence.

### Les dix améliorations les plus importantes

1. **Mettre en accord le ch. 0 et le ch. 16 sur l'énigme du producteur plus fiable** : une phrase en 0.5.4 (« possibilité, non fréquence ») et une configuration du tableau 16.1 où le risque monte (C-003).
2. **Refaire l'exemple de la roulette russe** pour que le facteur omis soit vraiment hors du cadre et indépendant de p, ou le présenter comme une erreur d'estimation (C-001, ch. 4 et 17).
3. **Couper les redites de cas** : ébullition, ferrure, Mars Climate Orbiter, M. X / M. Y, METR, Mata, Challenger, 8.4 → 14.1, 8.2 → 14.2.3. Un récit complet par cas, des renvois ailleurs (C-019 à C-022).
4. **Aligner les statuts** : proposition 4 (trois statuts différents), proposition 1 (hypothèses absentes de l'énoncé), proposition 3(b) (aucune dérivation), cinq conditions (« qui en découlent »), définition 1 (contient une thèse) (C-002, C-012, C-014, C-023, C-046).
5. **Stabiliser les notations** : z variable / z probabilité ; D, C, A, E qui changent de sens ; P(E) / Pr(E) / P(faux) ; numéroter M1-M3 dans l'ordre d'apparition (C-006, C-009, C-027).
6. **Tenir la règle du terme unique** : dérive de distribution (sens restreint non signalé), sévérité = sensibilité, vérification vs contrôle, « chaîne de contrôles » au lieu de chaîne d'étapes, « calibrer » un seuil, « Indépendant et précis » à c constant (C-007, C-008, C-018, C-026, C-047, C-024).
7. **Préciser de quel cadre on parle pour un composant appris** dans la matrice du ch. 13 (C-015).
8. **Corriger les renvois et les attributions** : 10.2 → 10.1 ; « chapitre 3, proposition 3 » ; « inférence inductive (chapitre 2) » ; R comparé à p* (ch. 9 → 17) ; pré-mortem sans source ; V&V attribuée à l'auteur ; vérifier logit lens et Google Flu Trends ; nuancer 2008 (C-010, C-029, C-030, C-031, C-039, C-040, C-042, C-043, C-017).
9. **Corriger les deux erreurs de raisonnement des modèles** : la Nuance de 8.5, qui contredit M1 (« le producteur la voit et ne l'émet pas »), et la lecture de la répétition à 99,9 % de sévérité, qui oublie les fausses alertes (C-004, C-005).
10. **Revoir les parcours de lecture** : ajouter le ch. 8 (et 9, 4, 17) à « L'argument principal » ; compléter la liste des Nuances du parcours critique ; ne pas appeler « Boîte à outils » un chapitre et des sections qui définissent des termes indispensables (C-016, C-051, C-052).

## 3. Ce que j'ai dû prendre sur parole

- **Les faits des études de cas :** Mars Climate Orbiter (rapport du Mishap Investigation Board), Mata v. Avianca, Moffatt v. Air Canada, Challenger (7 vols avec dommages / 16 sans, d'après Tufte et la Commission présidentielle), Knight et Leveson (27 versions), Google Flu Trends (Lazer et al. 2014), BCG (758 consultants, +12,2 % de tâches, +25,1 % de vitesse, +40 % de qualité, −19 points hors frontière), METR (+19 % de temps contre −20 % ressentis), Knight Capital (45 min, plus de 460 M$), effondrement de modèle (Shumailov et al. 2024), complaisance (Sharma et al. 2024), appariement des probabilités (Bliss et al. 1995). Ces chiffres sont cohérents avec ce que j'en savais, mais je n'ai rien vérifié.
- **Les résultats techniques invoqués sans démonstration :** la borne de Kalai et Vempala, donnée « schématiquement » (12.1) ; l'effet des barèmes d'évaluation (Kalai et al. 2025) ; l'entropie sémantique (Farquhar et al.) ; les théorèmes no free lunch ; la garantie de la prédiction conforme sous échangeabilité ; le do-calcul ; le test par mutation ; la réglementation européenne sur la projection d'images de menaces fictives (TIP).
- **L'article de l'auteur (Fauriat 2026)**, cité 36 fois comme source de la thèse, des pratiques (quatre questions, marge d'humilité, transfert de responsabilité) et parfois de faits (2008). Je n'y ai pas accès. La conclusion dit que le livre l'a corrigé sur deux points.
- **Les figures** (0.1, 0.2, 2.1, 3.1, 4.1, 5.1, 5.2, 6.1, 7.1, 8.1, 9.1, 12.1, 13.1, 14.1, 16.1, 17.1, 18.1) : je n'en ai lu que la légende et la description dans le texte.
- **Les annexes A (aide-mémoire) et D (paramètres des exemples)**, citées par l'avant-propos et la conclusion, ne figuraient pas dans mon dossier.

## 4. Questions hors périmètre

- Vérifier dans les sources primaires : l'exemple « tour Eiffel, pays puis ville » attribué au billet sur le logit lens (nostalgebraist 2020) ; la formule « la même méthode » pour Google Flu Trends ; le caractère structurel (et non paramétrique) de la corrélation dans les modèles hypothécaires d'avant 2008 ; le graphique de Challenger effectivement examiné *pendant* la téléconférence (Tufte distingue les planches de Thiokol et le graphique de la Commission).
- Vérifier dans l'annexe C : les notations q (ch. 8 : une probabilité, « facteur omis partagé ») et z (variable/probabilité), et l'absence de P(faux), A et D.
- Vérifier si l'annexe D récapitule bien tous les paramètres illustratifs (en particulier m = p = 6 % aux ch. 8 et 14, et la configuration du ch. 16).
- Vérifier que le glossaire et le texte concordent sur « dérive de distribution », « sévérité » et « vérification ».
- Il serait utile qu'un lecteur spécialiste de l'apprentissage automatique juge la description du post-entraînement (ch. 11), qui omet le renforcement sur récompenses vérifiables, et le sens restreint de « dérive de distribution ».
- Il serait utile qu'un statisticien juge l'absence de discussion de l'hypothèse « fourre-tout » (ch. 5 et 17) et le statut de « résultat sous hypothèses » de la proposition 3(b).

## 5. Limites de ma lecture

- J'ai lu les 26 fichiers en entier, dans l'ordre, ainsi que le fichier de référence. Mais je les ai lus comme un lecteur cible : j'ai survolé certains Noyaux formels (dérivations des ch. 1, 3, 5, 7), sans en contrôler chaque étape algébrique. J'ai en revanche refait tous les calculs des exemples quantitatifs.
- Les figures n'étaient pas visibles. Je ne peux juger ni leur lisibilité ni leur accord exact avec les tableaux.
- Je n'avais ni les annexes A et D, ni la bibliographie complète : les références n'ont été jugées que sur leur plausibilité, de mémoire, sans vérification.
- Ma sensibilité aux redites tient en partie à la lecture d'une traite. Un lecteur qui suit un parcours sélectif (tableau 0.1) souffrira moins des répétitions, mais davantage des lacunes du parcours « argument principal ».
- Mes constats de terminologie et de notation s'appuient sur le glossaire et la table des notations fournis. Les constats sur le style (redites, longueur des phrases) relèvent en partie du jugement.
