# Bilan — P1

## 1. Ce que j'ai compris

La partie I défend que l'on n'agit jamais d'après le monde mais d'après une représentation, et que le monde répond à l'action, non à la représentation. Le chapitre 1 rappelle les outils (déduction et induction, règles à arrière-plan tacite A ∩ (...) → B, probabilité, Bayes en cotes, score logarithmique). Il retient que chacun ne vaut que « pourvu que » des conditions restent tues. Le chapitre 2 en tire la notion de cadre : une spécification finie (variables, catégories, classe de modèles, objectif) choisie avant l'inférence. La rigueur formelle, déductive comme inductive, ne certifie pas ce cadre, et formaliser « un cran plus haut » ne fait que reporter le choix. Le chapitre 3 lit la probabilité comme un poids réparti sur des mondes possibles et recommande de raisonner à l'envers. Il montre qu'une issue isolée juge mal un prévisionniste et que la calibration, mesurée par des règles de score strictement propres, exige la répétition. Le chapitre 4 applique l'utilité espérée de Savage et obtient le seuil p* = 1/(1 + L/ΔU). Ce seuil s'effondre quand les enjeux sont démesurés, et deux décideurs rationnels peuvent diverger selon leur estimation de p. Une décision unique n'est protégée par aucune moyenne, et la question laissée ouverte est : comment décider quand notre cadre a pu manquer l'essentiel ?

## 2. Impression d'ensemble

Forces : un fil très net, des exemples récurrents (ébullition, navigateurs X et Y, soudures) qui aident à retenir, des définitions courtes, une page de partie qui tient ses promesses. Tous les calculs que j'ai refaits sont exacts : tableau 1.1, brouillard 13 %, surprises du tableau 3.1, seuils 1/26 et 1/10 001. Les blocs facultatifs peuvent être sautés sans perdre l'argument. Les points clés sont fidèles, à quelques durcissements près.

Problèmes les plus importants, par ordre :
1. Incohérence de la relation entre représentation et cadre (P1-001), qui sous-tend toute la partie. La notation dérive aussi (P1-019).
2. Exemple de la roulette russe : le joueur « croit l'arme déchargée » (4.3), puis la balle est dite absente de son cadre (4.5) ; les deux mécanismes se confondent (P1-002).
3. Redites lourdes : l'ébullition est déroulée en 1.2 puis en 2.2 (P1-006) ; l'exemple quantitatif de 4.3 refait les calculs de 4.2 et 4.3 (P1-007) ; l'argument du « 5 % » revient de 2.1 à 4.5 (P1-008).
4. Fiabilité du chapitre 2 : renvois répétés à l'article de l'auteur pour des affirmations logiques (P1-003) et étude de cas qui n'est pas un cas documenté (P1-004, P1-005).
5. Durcissements et formules trop fortes : « transporte l'erreur » (P1-009), « seule la répétition » (P1-016), régression à l'infini (P1-010).

## 3. Ce que j'ai dû prendre sur parole

- Le « chapitre 0 » : le navigateur, la dinde inductiviste, les huit parcours de lecture (section 0.8).
- Le chapitre 7 : le problème de Hume et ses « formes contemporaines », la régression à l'infini des méta-procédures, la détection d'un décalage de cadre par observation du monde (renvois en 1.1, 2.4).
- Le chapitre 5 : la dinde « étudiée en détail », la distinction des incertitudes.
- Le chapitre 17 : réponse à la question laissée ouverte, seul traitement annoncé des décisions uniques.
- Les résultats externes cités sans démonstration : théorème de couverture de la prédiction conforme, critères de d-séparation et do-calcul, axiomes de Savage, propriété d'une règle de score strictement propre (le texte démontre seulement le cas logarithmique et le cas quadratique).
- Toutes les références bibliographiques (je ne les ai pas vérifiées) : Hume 1748, Korzybski 1933, Pearl 1988 et 2009, McCarthy et Hayes 1969, Dennett 1984, Shanahan 2016, Vovk et al. 2005, Angelopoulos et Bates 2023, Gneiting et Raftery 2007, Russell et Norvig 2021, Savage 1954. Le contenu de l'article « Fauriat 2026 », cité sept fois dans le chapitre 2, m'est resté inconnu.

## 4. Questions hors périmètre

- Les chapitres 5 et 7 tiennent-ils les promesses faites ici (dinde, Hume, régression des méta-procédures) ?
- L'annexe C (« p introduit au chapitre 4 ») est-elle cohérente avec l'emploi de p dès les chapitres 1 et 3 ? Λ et S manquent-ils vraiment ?
- Le chapitre 17 reprend-il l'exemple de la roulette russe avec la même description du joueur ?
- La bibliographie contient-elle les deux Russell qui motivent « S. J. Russell » ? L'article Fauriat 2026 y est-il décrit comme le disent l'avant-propos et les citations de 2.1 à 2.4 ?
- Le chapitre 0 contient-il bien l'histoire du navigateur et de la dinde reprise en 2.1 et 3.3 ?

## 5. Limites de ma lecture

Lecture intégrale de la partie I et de la référence (avant-propos, glossaire, notation) ; aucun autre fichier ouvert, ni source, ni web. Je n'ai pu juger ni les faits historiques et bibliographiques (seulement la plausibilité), ni la lisibilité des figures (remplacées par « [Figure] » et leur légende). Les constats de gravité A sont absents : je n'ai trouvé ni erreur de calcul ni contresens, et j'ai écarté les simples goûts de style. Les confiances « basse » signalent des remarques discutables.
