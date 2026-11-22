# Lecture croisée des rapports Claude et Gemini

Rapport de lecture croisée sur deux séries indépendantes de comptes rendus consacrés à trois sources : W. Fauriat, *Un discours de la méthode au XXIe siècle* (2022) ; W. Fauriat, *Agir d'après une représentation du monde* (2026) ; la revue de littérature en anglais du dossier `literature_review/`.

---

## 1. Objet, corpus et méthode

### 1.1 Le corpus

Chacune des trois sources a fait l'objet d'un rapport rédigé par des agents Claude et d'un rapport rédigé par Gemini. Les six textes ont été lus intégralement.

| Source | Rapport Claude (`report_claude/`) | Rapport Gemini (`report_gemini/`) |
| :--- | :--- | :--- |
| *Un discours de la méthode au XXIe siècle* (2022), `ManuscritPDFpub.pdf` | `recension_un_discours_de_la_methode_au_XXIe_siecle.md` (10 643 mots) | `rapport_ManuscritPDFpub.md` (4 084 mots) |
| *Agir d'après une représentation du monde* (2026), `livre-ecran.pdf` | `recension_agir_d_apres_une_representation_du_monde.md` (9 227 mots) | `rapport_livre_ecran.md` (4 490 mots) |
| Revue de littérature (neuf champs et trois passes de raffinement, 34 453 mots) | `rapport_revue_de_litterature.md` (10 398 mots) | `rapport_literature_review.md` (5 733 mots) |

Dans la suite, on désigne ces rapports par C1, C2, C3 (Claude) et G1, G2, G3 (Gemini), dans l'ordre du tableau. Les renvois de page suivent la pagination imprimée des livres ; pour le livre de 2022, la page du PDF s'obtient en ajoutant deux, pour celui de 2026 en ajoutant douze (décalage contrôlé sur plusieurs pages : p. 1 = PDF 13, p. 118 = PDF 130, p. 265 = PDF 277).

### 1.2 Conditions de production

Les conditions dans lesquelles les deux séries ont été rédigées ne sont pas symétriques, et il faut le dire d'emblée. Les agents Claude avaient reçu pour consigne de lire la source en entier, de viser environ 4 000 à 8 000 mots, d'écrire principalement en prose argumentée avec une annexe d'errata et de respecter des règles strictes de français idiomatique. Les instructions données à Gemini sont inconnues. On notera que les trois rapports Claude dépassent la fourchette demandée (9 227 à 10 643 mots) : c'est un manquement à la consigne, d'autant plus visible que leurs annexes représentent une part notable du volume. La longueur, en revanche, n'est ni récompensée ni pénalisée ici en tant que telle ; seules comptent la densité, la précision et l'exactitude.

Pendant la rédaction du présent rapport, un fichier `cross_read_report.md` est apparu dans le dossier `report_gemini/`. Il ne fait pas partie du corpus et n'a pas été consulté au-delà de son en-tête, afin de préserver l'indépendance de la présente lecture.

### 1.3 Le risque d'autocomplaisance et la manière de le contenir

Le présent rapport est écrit par un modèle Claude qui juge des textes produits par des modèles Claude face à ceux d'un concurrent. Le risque de complaisance envers soi-même est évident : préférence pour un style familier, indulgence pour des erreurs que l'on aurait pu commettre. Une déclaration de bonne foi ne suffit pas ; on a donc cherché à contenir ce biais par la méthode.

Premièrement, aucun jugement de fond ne repose sur une impression : chaque affirmation de fait qui sépare les deux rapports, et chaque affirmation importante d'un seul rapport (renvoi de page, citation, erreur reprochée à l'auteur, chiffre recalculé, attribution bibliographique), a été confrontée à la source. Deuxièmement, les mêmes critères ont été appliqués aux deux séries. Troisièmement, on a cherché les erreurs des rapports Claude avec au moins autant d'insistance que celles des rapports Gemini : les affirmations les plus tranchées de Claude, qui sont aussi les plus exposées, ont été vérifiées en priorité. L'annexe recense les 134 vérifications effectuées ; elle fait apparaître des erreurs dans les deux séries.

### 1.4 Protocole de vérification

Les vérifications ont porté sur les textes extraits des deux livres, munis de repères de page, interrogés par recherche ciblée ; lorsque l'extraction perdait une formule ou un exposant, la page du PDF a été examinée en image (pages 74, 119, 170 et 171 du livre de 2022). Pour la revue de littérature, les douze fichiers ont été interrogés ligne par ligne. Les calculs cités par les rapports ont été refaits (valeur prédictive positive, risques résiduels, seuils de bascule, mise à jour bayésienne, calculs élémentaires du livre de 2022). Les faits extérieurs aux sources (dates, attributions bibliographiques) n'ont été tenus pour exacts que lorsqu'ils relèvent d'une connaissance bibliographique établie ; les faits très récents (prépublications de 2026, annonces de projets logiciels) sont classés « non vérifiables » lorsqu'ils sont décisifs.

### 1.5 Critères

Six critères ont été retenus pour chaque paire : la couverture de la source ; l'exactitude factuelle (renvois, citations, chiffres) ; la justesse des critiques adressées à l'auteur ; l'indépendance du jugement, c'est-à-dire la capacité à ne pas se contenter de reformuler l'autoprésentation de l'ouvrage ; l'utilité pour l'auteur ; la qualité de la langue et de la typographie.

---

## 2. *Un discours de la méthode au XXIe siècle* (2022)

### 2.1 Couverture

Les deux rapports couvrent l'ouvrage en entier, mais selon des partis pris différents. G1 en donne la description la plus complète et la plus régulière : chacun des vingt et un chapitres est résumé avec ses bornes de pages, de la préface (p. 7-12) à l'épilogue (p. 279-280), avec les épigraphes latines, l'index et la bibliographie. Pour savoir ce que contient le livre et où, G1 est plus commode que C1 ; il ajoute une section sur l'appareil formel et une autre sur le positionnement de l'auteur.

C1 résume plus vite la deuxième partie et consacre l'essentiel de son volume à l'analyse critique (thèse centrale, exactitude technique discipline par discipline, position dans la littérature, épreuve des années postérieures à 2022, forme), puis à une annexe d'environ cent corrections. Ni l'un ni l'autre n'omet de partie de l'ouvrage. C1 examine en revanche ce que G1 ne fait qu'énumérer : les notes de bas de page (cent vingt et une, nombre exact), l'index (dépourvu de noms propres) et le lien, absent, entre la bibliographie et le texte.

### 2.2 Convergences

Les points sur lesquels les deux rapports s'accordent sont les plus sûrs, et tous ceux qui suivent ont été vérifiés dans le livre. Le dispositif narratif s'essouffle et s'efface dans la troisième partie, à partir de la page 215 ; l'enveloppe du prologue (p. 15-16) n'est jamais ouverte ni reprise. Le qualificatif « structuraliste » revendiqué par le manifeste (p. 264) n'est expliqué nulle part, et G1 relève à juste titre qu'il ne figure pas à l'index. La note 96 (p. 233) affirme que « le réel n'est pas intrinsèquement aléatoire » et engage un déterminisme que l'auteur ne justifie pas. Le traitement de l'apprentissage automatique reste générique : les réseaux de neurones ne sont nommés qu'une fois (p. 150), l'apprentissage par renforcement et l'apprentissage profond jamais. La troisième partie est redondante. Le texte n'a pas fait l'objet d'une relecture éditoriale : les deux rapports relèvent les mêmes fautes (de « UN DISOURS » au faux-titre à « garder le contrôler », p. 259) et la même erreur latine dans *Amicus Plato, sed magis amica verum* (p. 278). Enfin, les deux rapports reconnaissent la valeur pédagogique de la deuxième partie.

### 2.3 Divergences et arbitrages

Sur le fond, les deux rapports divergent moins par des affirmations contradictoires que par le degré de sévérité. G1 juge la thèse centrale « tenue avec rigueur et unité » ; C1 la juge « soit triviale, soit excessive » : triviale si elle se borne à dire que la rationalité d'un choix s'apprécie au regard de l'information de l'agent, ce qui est le point de départ de la théorie bayésienne depuis Ramsey, de Finetti et Savage ; excessive lorsqu'elle conclut qu'aucune anticipation n'est « plus juste qu'une autre » (p. 218-219). Les citations de C1 sont exactes, et l'autocontradiction qu'il relève est réelle : le livre écrit à la page 224 que « celui qui comprend mieux le réel et qui possède une vision “plus juste” […] obtiendra généralement de meilleurs résultats ». Sur ce point, C1 a raison et G1 ne voit pas la difficulté. On doit toutefois nuancer C1 : le livre ne réserve pas entièrement la calibration aux décisions répétées, puisqu'il écrit aussi, page 223, que des anticipations sont « bien calibrées » lorsque l'utilité moyenne observée rejoint l'utilité espérée.

Les divergences factuelles portent sur trois points. Pour le seuil d'indifférence du chapitre « Décider, c'est anticiper », G1 écrit $p^* = (u_2 - u_3)/(u_1 - u_3)$, C1 écrit $p_e = (u_s - u_0)/(u_1 - u_0)$. L'examen de la page 169 en image donne raison à C1 : la formule de G1 est mathématiquement équivalente, mais la notation n'est pas celle de l'auteur, alors que G1 la donne pour celle du livre. Pour la formule des probabilités totales, G1 la situe dans le chapitre « Probabilités : mondes possibles et raisonnements imparfaits » (p. 115-129), C1 dans le chapitre « Statistique, “régularité du réel” et prédictions » (p. 131-143) ; l'index renvoie aux pages 141 et 155, ce qui donne raison à C1. Pour le jeu de go, enfin, G1 affirme en note que l'extraction a perdu les exposants « $10^{43}$ et $10^{170}$ à la p. 72 » : la page, examinée en image, porte $10^{100}$ pour le go. G1 a donc comblé une lacune de l'extraction par une valeur qu'il n'a pas lue, ce qui est plus grave qu'une simple coquille.

### 2.4 Apports propres

G1 apporte un argument que C1 n'a pas : la note 53 (p. 164) restreint l'analyse au cas d'un agent unique et écarte les choix collectifs, alors que le récit repose sur une négociation collective, que Pauline définit la science politique par les questions « Qui décide ? Dans l'intérêt de qui ? » (p. 44) et que le manifeste vise les « décideurs industriels, économiques ou politiques » (p. 274). Les trois renvois sont exacts, et la critique est juste : elle met au jour une tension interne que C1, qui cite la même note 53 pour une remarque de vocabulaire (théorie des jeux ou théorie du choix social), n'exploite pas. G1 relève aussi, avec justesse, le glissement entre une rationalité purement formelle (la dinde est déclarée « rationnelle », p. 183) et l'appel final à une rationalité « humble, critique et humaine ».

Les apports propres de C1 sont beaucoup plus nombreux et, pour l'essentiel, ils tiennent (le détail figure à l'annexe, n° 1 à 34). Ont notamment été vérifiés : l'inégalité stricte $\Pr(E) > 0$ (p. 117), qui contredit la note 17 ; Socrate « né […] au VIe siècle avant J.C. » (p. 94) ; l'épigraphe de Descartes privée de « souvent » (p. 5) ; la note 85 (p. 221) qui juge dépourvue de sens une « probabilité sur une probabilité », alors que le livre place lui-même une loi *a priori* sur un paramètre ; les notes 30, 77 et 80 (empirisme tiré de « l'empire », « validation croisée » réduite à un découpage, Saint-Pétersbourg et Allais rattachés à l'« aversion au risque ») ; les $10^{43}$ « candidats » des échecs (p. 72), qui sont des positions selon Shannon ; la causalité remplacée par la « régularité » (p. 234) ; une bibliographie dont un seul titre est appelé dans le texte (p. 134) ; la valeur de l'information de Raiffa et Schlaifer reprise sans être nommée. C1 a également refait les petits calculs des saynètes initiales (trois œufs pour six convives, 58 cm pour la tangente de 30°, 16 % de spectateurs supplémentaires, soit 80 billets sur 500) : ils sont justes, et C1 le dit. Le rapprochement avec l'objection de Lady Lovelace est bien choisi.

### 2.5 Erreurs et faiblesses de chaque rapport

C1 commet trois erreurs nettes. La première touche l'exemple du trajet vers l'aéroport. C1 affirme que, « si les durées et les coûts s'additionnent d'un segment à l'autre, le problème se résout en temps linéaire par programmation dynamique ». Or l'énoncé du livre (p. 69-71) combine un délai à respecter et un coût à minimiser : avec deux options par segment, c'est un problème de sac à dos à choix multiples, difficile au sens faible, que la programmation dynamique résout en temps pseudo-polynomial, non linéaire. L'idée générale de C1 reste juste (la taille de l'espace des candidats ne mesure pas la difficulté d'un problème), mais l'exemple choisi pour réfuter l'auteur est lui-même inexact. La deuxième erreur porte sur la note 42 (p. 146). C1 écrit qu'elle « assimile l'histogramme » à un diagramme en secteurs ; le texte dit en réalité que les proportions « pourraient être présentées différemment, sous la forme du gâteau découpé », la note précisant qu'on parle alors de « camemberts ». Il n'y a pas de confusion chez l'auteur. La troisième est mineure : la note 107 est située page 245 alors qu'elle figure page 243.

À ces erreurs s'ajoutent des excès. La prémisse « Socrate est un homme », dont C1 dit que « seule la note 1 » la rétablit, figure en fait dans le corps du texte, une ligne plus bas, dans la « formulation plus classique » du syllogisme. La note 45 (p. 149), qui donne à « numérique » le sens de valeurs « qui évoluent de façon continue », vise l'« espace numérique des candidats » d'une optimisation continue : l'emploi est spécialisé, non « contraire à l'usage ». Sur la définition du risque (p. 174), C1 reproche à l'auteur de ne pas dire que le risque combine probabilité et gravité ; or le livre écrit, juste avant sa définition, qu'« on retrouve toujours deux éléments : un certain degré “d'incertitude” […] et des “conséquences” ». Ces excès dessinent un trait : dans sa recherche d'erreurs, C1 force parfois le texte. En revanche, la confrontation du livre aux grands modèles de langage, postérieurs à sa rédaction, est loyale : C1 admet qu'on ne saurait reprocher à l'auteur de les ignorer et ne vise que les affirmations d'impossibilité « par essence » (p. 199).

Les faiblesses de G1 sont d'une autre nature. Outre les trois inexactitudes signalées plus haut ($10^{170}$, notation du seuil, place de la formule des probabilités totales) et une approximation sur l'étymologie (*Statista* n'apparaît qu'à la page 131, non dans le chapitre des pages 33-38, qui parle du « préfixe Stat »), G1 ne voit aucune des erreurs techniques du livre : ni l'axiome de positivité, ni la date de Socrate, ni les notes 30, 77, 80 ou 85. Il présente la bibliographie comme une « filiation intellectuelle cohérente » qui « éclaire les appuis » de l'auteur, sans remarquer que vingt-deux titres sur vingt-trois ne sont jamais appelés. Sa critique est juste mais générale ; sa liste de coquilles, exacte, n'en compte qu'une dizaine.

### 2.6 Qualité critique et rédactionnelle

C1 est un compte rendu d'expert : il discute la thèse avec des outils précis (règles de score propres, convergence des opinions de Blackwell et Dubins, théorème d'Aumann), situe le livre dans la littérature et formule des recommandations de réédition ordonnées. Le ton est sévère, mais argumenté, et l'appréciation finale reconnaît les mérites du livre. Le français est d'une grande correction ; la typographie respecte les espaces insécables (près de sept cents occurrences) et les guillemets français.

G1 est une bonne note de lecture analytique, équilibrée, bien composée, plus agréable à lire que C1 pour qui cherche une vue d'ensemble. Sa langue est correcte, mais moins surveillée : « vingt-et-un chapitres », « modèles non-paramétriques », « sur-apprentissage » reproduisent précisément les traits d'union superflus que C1 relève comme fautes dans le livre ; aucune espace insécable n'est employée devant les deux-points ni à l'intérieur des guillemets.

---

## 3. *Agir d'après une représentation du monde* (2026)

### 3.1 Couverture

Les deux rapports couvrent l'ensemble de l'ouvrage : avant-propos et mode d'emploi, chapitre 0, cinq parties, conclusion, annexes et bibliographie. G2 en donne un exposé structuré et très précis, qui reconstitue les cinq thèses, les trois modèles formels et les principaux énoncés. Ses renvois sont d'une exactitude remarquable : sur une trentaine d'équations, de définitions, de propositions (avec leurs statuts) et de tableaux contrôlés, aucun n'est faux. C2 couvre la même matière plus brièvement dans sa partie descriptive, mais il examine aussi l'appareil (dénombrement des encadrés, quatorze définitions, cinq propositions), la notation, la mise en page et la bibliographie, et il recalcule tous les exemples chiffrés.

### 3.2 Convergences

Les deux rapports s'accordent sur les qualités du livre : une grille des contrôles féconde, une probité méthodologique rare, une langue soignée. Ils s'accordent aussi sur ses limites principales, toutes vérifiées : la marge d'humilité $b$ n'a pas de règle de fixation et conduit à l'abstention lorsque $p^*$ devient très petit, ce que le livre reconnaît lui-même (« lorsque $p^*$ devient inférieur à toute marge plausible, la règle revient simplement à s'abstenir », p. 208) ; la « distance optimale » entre producteur et contrôleur reste indéterminée ; la base empirique est mince, faite d'études uniques et datées, ce que la conclusion admet (p. 232) ; les paramètres des exemples sont illustratifs ; la genèse du livre l'expose au risque du « prêteur unique » qu'il décrit. Les deux rapports relèvent enfin la même tension chiffrée : l'énigme du producteur plus fiable (tableau 9.3, où le risque passe de 0,1 % à 0,9 %) n'est pas reproduite par l'exemple du chapitre 16, où le risque baisse de 5,57 % à 1,93 % (tableau 16.1, p. 193).

### 3.3 Divergences et arbitrages

La divergence principale tient au degré d'indépendance du jugement. G2 reprend largement l'autoévaluation de l'auteur : ses six « limites » recoupent pour l'essentiel les six tensions que la conclusion du livre recense elle-même, ce que G2 reconnaît d'ailleurs (« dont certaines sont reconnues dans la Conclusion »). C2 va au-delà et examine le livre à l'aune de ses propres exigences.

Plusieurs points de fait séparent les deux rapports, et ils ont été tranchés. G2 présente l'ouvrage comme rédigé « dans un français soutenu, limpide et idiomatique » ; C2 relève des calques de *deliver* (« le test délivre 9 + 49,5 = 58,5 résultats positifs », p. 109 ; « En délivrant toutes ses réponses », p. 188). C2 a raison, et il est même incomplet : le verbe revient aux pages 26 (« délivre elle aussi un signal anormal ») et 81 (« délivre une signature »). G2 inscrit sans réserve l'ouvrage dans « la tradition bayésienne subjective (de Finetti, Savage, Jaynes, Lindley) » ; C2 objecte que Jaynes défendait une lecture objective. L'objection est fondée sur le fond, mais C2 l'exagère en écrivant que le livre « gomme » la différence : la page 45 parle d'une conception défendue « sous des formes diverses » par ces quatre auteurs.

### 3.4 Apports propres

C2 a refait l'ensemble des calculs, et c'est l'apport le plus solide de toute la série. Ses recalculs (soudure, course au large, seuils, modèle M2, tableaux 9.4 et 16.1) ont été refaits ici : tous sont justes. C2 découvre surtout la seule erreur chiffrée du livre : page 118, la valeur prédictive positive annoncée « ≈ 25 % » pour un taux d'erreur de 2 % face au contrôleur fixe vaut en réalité $0{,}02 \times 0{,}72 / (0{,}02 \times 0{,}72 + 0{,}98 \times 0{,}05) = 22{,}7$ %. G2 n'a fait aucun calcul.

Sont également vérifiés et propres à C2 (annexe, n° 56 à 85) : le statut incohérent de la proposition 2, « définition » page 74, « résultat sous hypothèses de réalisabilité » page 75 ; le modèle M3 présenté comme « le troisième » alors que le lecteur le rencontre en premier (p. 85) ; la double définition de la « prudence superflue » (p. 203 et 245) ; l'emploi de ∩ pour la conjonction (p. 21) ; l'effectif de l'étude de METR passé sous silence ; l'absence de Perrow, Reason, Vaughan, Parasuraman, Box, Kennedy et O'Hagan, Gilboa et Schmeidler ou Hansen et Sargent ; l'article de l'auteur, document de travail, cité trente-deux fois. L'objection selon laquelle les modèles M2 et la marge additive conduiraient à l'abstention universelle dans les activités à enjeux extrêmes, alors que la sûreté industrielle réduit le facteur omis au lieu de le couvrir par une prime, est un apport de fond qui dépasse la réserve formulée par l'auteur.

G2 a lui aussi un apport propre : l'insuffisante analyse des conditions juridiques, économiques et réglementaires (responsabilité, assurance, normes sectorielles) qui pourraient imposer les verrous du niveau 3 là où la concurrence pousse à les contourner. La critique est juste et C2 ne la formule pas. G2 relève aussi avec exactitude que le modèle M2 suppose l'indépendance du facteur omis et des causes modélisées (p. 204), mais il s'agit là d'une réserve de l'auteur lui-même. Enfin, G2 qualifie l'affaire *Moffatt v. Air Canada* de « brève mention » (p. 137) : c'est en réalité un encadré entier, dont C2 rend mieux la portée (le livre y établit que la décision ne prouve rien sur les modèles de langage).

### 3.5 Erreurs et faiblesses de chaque rapport

C2 commet une erreur nette et plusieurs excès. L'erreur porte sur un exemple extérieur au livre : C2 range « le défaut de division du Pentium (1994) » parmi les défaillances où « le contrat de l'architecture était respecté tandis que le comportement réel s'en écartait ». C'est vrai des attaques par exécution spéculative, non du défaut de division, qui violait la norme IEEE 754 qu'il devait implémenter. Le second seuil de bascule calculé par C2 (« environ 4,2 % ») vaut en réalité 4,1 % ($0{,}028 / 0{,}68 = 4{,}12$ %) ; le premier (6,2 %) est juste. C2 compte dix-neuf encadrés « Question à se poser » ; on n'en retrouve que dix-sept, alors que ses cinq autres dénombrements sont exacts. Il estime la bibliographie du livre à « environ soixante-quinze titres », quand on en compte soixante-neuf, et C3 écrit pour sa part « environ soixante-dix » : les deux rapports Claude se contredisent.

Les excès sont plus significatifs, car ils dessinent un défaut récurrent. C2 écrit que « Le chapitre 0 devrait le dire d'emblée », à propos du caractère seulement possible de l'énigme ; or le chapitre 0 écrit déjà, page 11, que « ce calcul montre une possibilité, dont le chapitre 16 précisera à quelles conditions elle se réalise ». C2 estime que l'étiquette « Indépendant et précis », qui conserve la même part de causes partagées, « induit en erreur » ; le livre précise qu'elle est « nommée ainsi par contraste avec les scénarios corrélés du chapitre 16 » (p. 117). Il juge « curieuse » l'attribution des mondes possibles à Russell et Norvig (p. 43) ; le livre écrit seulement que ces auteurs « proposent une manière simple de dire ce que désigne alors le nombre », c'est-à-dire précisément une présentation de manuel. Dans ces trois cas, C2 reproche à l'auteur une omission que l'auteur a déjà réparée.

La faiblesse de G2 est inverse : un éloge peu discriminant (« essai d'une tenue intellectuelle peu commune », « honnêteté épistémique exemplaire », « crédibilité rare »), l'absence de toute vérification des calculs, la reprise du cadrage de l'auteur. On n'a pourtant relevé dans G2 aucune erreur de fait au sens strict ; sa fidélité à la lettre du livre est irréprochable.

### 3.6 Qualité critique et rédactionnelle

C2 est l'un des meilleurs textes du corpus : il sépare nettement ce qui est vérifié de ce qui est jugé, distingue la rigueur des calculs de la profondeur des résultats (« Les propositions présentées comme des “résultats sous hypothèses” sont pour l'essentiel des reformulations de leurs hypothèses »), et ses six recommandations finales sont directement utilisables. Sa langue est précise et sa typographie soignée.

G2 est un résumé raisonné de grande qualité, qui pourrait servir de présentation de l'ouvrage. Sa langue est correcte et souvent élégante ; on y relève quelques lourdeurs (« Fait notable de probité intellectuelle, le livre rectifie… ») et une typographie qui ignore les espaces insécables. Pour l'auteur, G2 est utile comme miroir fidèle de son propre propos ; C2 l'est comme contradicteur.

---

## 4. La revue de littérature

### 4.1 Couverture

Les deux rapports examinent les douze fichiers. G3 procède volet par volet, selon une grille constante (contenu, forces, limites), puis traite de la rigueur, de la cohérence, des lacunes et de recommandations éditoriales ; il ne confronte pas la revue au livre qu'elle accompagne. C3 procède aussi champ par champ, mais il annonce une méthode explicite (« ce que j'ai vérifié », « probablement erroné », « pas pu vérifier »), confronte les renvois de la revue au texte du livre, recalcule les formules de la passe des ponts formels et termine par une annexe de soixante et une références douteuses ou erronées. C3 couvre mieux les passes de raffinement, dont il examine la fidélité au livre ; G3 décrit mieux la structure formelle de chaque volet.

### 4.2 Convergences

Les deux rapports s'accordent sur des constats tous vérifiés : l'appareil bibliographique est lacunaire et hétérogène (auteurs cités sans date ni titre aux champs 1, 2 et 4) ; la passe de vérification empirique est la plus honnête et la plus utile ; ses corrections (Kim et al., Steyvers et al., Doshi et Hauser, corpus de Liang et al. 2024) n'ont pas été reportées dans les champs 8 et 9 ; les sections d'interfaces sont redondantes ; la typologie des facteurs omis invisibles du champ 3 (constantes de régime, colinéarité, seuils non activés) est l'apport le plus original de la revue.

Une convergence, pourtant, est fausse, et elle montre qu'un accord entre deux rapports ne vaut pas preuve. G3 et C3 reprochent tous deux au champ 8 d'attribuer à Liang et al. (2024) le biais des détecteurs contre les auteurs non anglophones, qui est un résultat de Liang et al. (2023). Le fichier actuel du champ 8 ne contient pas cette attribution : la ligne 20 et la ligne 68 évoquent le biais sans citation. L'erreur se trouve dans la passe de falsification (ligne 99), que C3 cite d'ailleurs correctement ailleurs. Les deux rapports ont reproduit l'audit de la passe 2, qui renvoie à un état antérieur du fichier, sans le contrôler.

### 4.3 Divergences et arbitrages

Trois divergences de fait ont été tranchées.

La première concerne les listes de références. G3 écrit que six des neuf volets (02, 03, 04, 05, 06, 08) n'en possèdent pas, à la différence des volets 01, 07 et 09 ; C3 écrit que « sept des neuf champs n'ont pas de liste de références » et que le champ 9 est « le seul champ thématique, avec le septième, à disposer d'une liste ». Le fichier 01 comporte une section `## References` (lignes 145 à 171) : G3 a raison, C3 a tort, et il se contredit puisque son propre examen du champ 1 traite de ses références.

La deuxième concerne la passe des ponts formels. G3 écrit que les passerelles formelles sont « mathématiquement justes » et que la dérivation de $c_{\text{eff}}$ est « rigoureuse » ; C3 y trouve trois erreurs. Deux ont été confirmées par calcul. L'e-processus $E_t = \prod_i [1 + \lambda_i(X_i/p_0 - 1)]$ avec $\lambda_i \in [0, 1/p_0)$ (ligne 65) n'est pas positif : pour $X_i = 0$, le facteur vaut $1 - \lambda_i$, négatif dès que $\lambda_i > 1$, ce que l'intervalle autorise puisque $1/p_0 > 1$ ; l'inégalité de Ville ne s'applique plus. La formule de la valeur de quasi-option (ligne 38), $\mathbb{E}[\max_{a_1} U] - \max_{a_1} \mathbb{E}[U]$, est celle de la valeur espérée de l'information parfaite. Le troisième point (copule posée entre deux fonctions d'un même stress scalaire, donc comonotones) est un raisonnement valable sous l'hypothèse, que C3 explicite, d'un stress unidimensionnel. C3 relève enfin, à juste titre, que $c_{\text{eff}}$ peut devenir négatif (ligne 82), hors du domaine $c \in [0, 1]$ que le livre fixe à l'équation 9.4 (p. 115). Sur ce point, C3 l'emporte nettement.

La troisième porte sur la formule d'échappement corrélé du champ 8 (lignes 46-48), que G3 tient pour « un outil analytique précieux » et C3 pour « l'erreur formelle la plus nette des neuf champs ». L'arbitrage est partagé. C3 a raison de dire qu'une corrélation unitaire ($\rho \to 1$) est impossible entre deux événements de probabilités différentes, en vertu des bornes de Fréchet ; G3 ne le voit pas. Mais C3 affirme que $q$ « est défini comme » une probabilité conditionnelle, alors que le fichier parle d'un taux d'omission « marginal » : si l'on prend cette définition au mot, l'identité $P = pq + \rho\sqrt{p(1-p)q(1-q)}$ est correcte. La formule est donc mal définie plutôt que fausse.

Une dernière divergence est mineure : G3 compte quatorze études dans la passe empirique, C3 quinze ; le tableau principal en recense quatorze. G3, en revanche, estime le corpus à « environ 284 Ko », alors que les douze fichiers totalisent 266 613 octets.

### 4.4 Apports propres

Les apports propres de C3 ont été contrôlés dans les fichiers chaque fois que c'était possible (annexe, n° 98 à 122). Le champ 4 réduit bien le théorème de Savage à trois axiomes (ligne 12), range Buchak parmi les critiques des probabilités ponctuelles (ligne 21) et assimile l'incertitude knightienne à l'ambiguïté (ligne 15) ; le champ 5 crédite Littlewood et Miller d'une idée qui est le cœur du modèle d'Eckhardt et Lee (ligne 13) ; le champ 6 prête à DeMillo, Lipton et Perlis une thèse qui n'est pas la leur (ligne 18) ; le champ 2 attribue le théorème *No Free Lunch* en apprentissage à Wolpert et Macready (1997), erreur que la bibliographie du livre contient aussi. C3 montre en outre que la revue ignore des auteurs que le livre cite (Wynne, Goodman, Hume, Pearl, Dijkstra : aucune occurrence dans la revue) et des pans entiers de la sûreté (Reason, Parasuraman, normes de sûreté fonctionnelle : aucune occurrence). Sa critique de la passe de falsification est l'apport le plus original : la passe combat des thèses que le livre ne soutient pas ; or le livre écrit bien que les chiffres de METR « reflètent une génération particulière d'outils » (p. 183) et que, dans l'illustration du chapitre 16, « le risque sous appariement baisse même (1,93 % contre 5,57 %) » (p. 235). Les citations sont exactes. Enfin, C3 observe que la revue, en lisant tous les travaux à travers les catégories du livre, perd sa valeur de contrôle indépendant : c'est appliquer à la revue la leçon du chapitre 16, et l'observation vaut aussi, toutes proportions gardées, pour le présent exercice.

Deux apports de C3 sont moins sûrs. La lecture de MacKenzie et Spears comme réfutant le récit de la copule « qui a tué Wall Street » est fondée, mais la revue (ligne 72) ne dit pas exactement le contraire : elle en tire une thèse d'enfermement organisationnel que ces auteurs défendent aussi en partie. Le doute sur la date de 1999 attribuée à Ben-Haim n'est pas probant, Ben-Haim ayant publié sur la théorie de l'écart d'information avant la première édition de son livre.

G3 a trois apports propres, tous pertinents : l'angle mort juridique, réglementaire et assurantiel ; la sous-estimation des coûts de calcul, d'énergie et de latence des remèdes proposés (le surcoût de cinq à dix fois de l'entropie sémantique est bien mentionné au champ 7, ligne 46) ; la faible couverture de l'interprétabilité mécaniste et des interactions entre agents multiples. C3 ne formule pas ces critiques.

### 4.5 Erreurs et faiblesses de chaque rapport

Les erreurs de C3 sont celles déjà relevées : le décompte des listes de références (« sept des neuf »), contredit par le fichier 01 ; le nombre d'études de la passe 2 ; l'attribution de l'erreur sur Liang et al. au champ 8. Elles touchent l'inventaire, non l'analyse, mais elles sont fâcheuses dans un rapport qui reproche à la revue son manque de soin. On relève aussi une phrase dont le ton détonne dans un rapport d'expertise : « Je ne demande pas une revue patriotique ».

Les erreurs de G3 sont moins nombreuses en valeur absolue, mais plus graves dans leurs conséquences : déclarer « mathématiquement justes » des ponts formels qui contiennent au moins deux erreurs, et recommander comme « outil analytique précieux » une formule mal définie, revient à donner à l'auteur une assurance qu'il ne doit pas avoir. G3 n'a trouvé lui-même aucune erreur de fond dans la revue : toutes celles qu'il signale viennent de la passe 2. Son jugement d'ensemble (« revue de littérature interdisciplinaire de très haut niveau », dont l'analyse est « excellente ») n'est pas étayé par une vérification propre.

### 4.6 Qualité critique et rédactionnelle

C3 est un rapport de contrôle, plus que de présentation ; il est exigeant, souvent juste, parfois excessif dans son inventaire d'absences (la liste des travaux français manquants revient d'un rapport Claude à l'autre et prend l'allure d'une préférence du recenseur). Sa langue est précise ; il traduit les citations et signale les originaux.

G3 est clair et bien ordonné, mais sa langue est plus relâchée que celle de G1 et G2 : « pistes de recherche à fort levier », « délocalisation sub-symbolique », « frontières dentelées » (le livre dit « en dents de scie »), « tampon d'humilité » (le livre dit « marge d'humilité »), « basculement exponentiel » pour *exponential tilting* (on attend « inclinaison exponentielle »), « inférence sûre valide à tout moment ». Les liens `file:///` insérés dans le corps du texte sont inutilisables hors de la machine de rédaction.

---

## 5. Comparaison transversale

**Rapport à l'autoprésentation de l'auteur.** Le trait le plus constant de la série Gemini est la reprise du cadrage de la source : G2 reprend les tensions que la conclusion du livre se reconnaît, G3 les corrections que la revue s'applique à elle-même, G1 la filiation que la bibliographie suggère. Cette fidélité garantit la justesse descriptive, mais les rapports Gemini apprennent peu à l'auteur qu'il ne sache déjà. La série Claude, à l'inverse, juge les sources à l'aune de leurs propres exigences et de la littérature extérieure. Son défaut symétrique, vérifié trois fois dans C2 et deux fois dans C1, est de reprocher à l'auteur des omissions que celui-ci a déjà réparées, ou de forcer un passage pour en faire une erreur.

**Vérification des calculs.** C'est la différence la plus nette. Les rapports Claude ont refait les calculs des sources et trouvé la seule erreur chiffrée du livre de 2026 ainsi que les deux erreurs formelles de la passe des ponts formels. Les rapports Gemini n'ont refait aucun calcul ; G3 a même certifié exactes des formules qui ne le sont pas. En sens contraire, les recalculs de Claude ne sont pas infaillibles (trajet de l'aéroport, seuil de 4,2 %).

**Exactitude des renvois.** Les rapports Gemini sont, sur ce point, au moins aussi bons que les rapports Claude : G2 n'a commis aucune erreur sur une trentaine de renvois précis, et G3 a mieux compté que C3 les listes de références et les études. Les erreurs de Gemini se concentrent sur des reconstructions non vérifiées ($10^{170}$, notation du seuil) ; celles de Claude, sur des inventaires (décomptes, pagination d'une note) et sur des critiques trop appuyées.

**Exactitude bibliographique.** Les rapports Claude mobilisent une culture bibliographique étendue et, pour les références contrôlables (Blackwell et Dubins 1962, Aumann 1976, Shannon 1950, Kennedy et O'Hagan 2001, Earman et Roberts 1999, Henry 1974, entre autres), exacte. Les rapports Gemini en mobilisent peu, sans erreur.

**Ton.** Les rapports Gemini sont laudatifs, parfois sans discernement (G2, G3) ; les rapports Claude sont sévères, parfois à l'excès (C1 sur l'aéroport et l'histogramme, C2 sur le chapitre 0), mais toujours argumentés.

**Langue et typographie.** Les rapports Claude respectent les règles de la typographie française (espaces insécables, guillemets) et évitent les calques ; ils ne sont pas parfaitement homogènes entre eux (apostrophes typographiques dans C2, droites dans C1 et C3). Les rapports Gemini sont correctement écrits, mais n'emploient aucune espace insécable et laissent passer des calques et des traits d'union fautifs, surtout dans G3.

**Conformité aux consignes.** Les rapports Claude dépassent tous la longueur demandée et leurs annexes sont volumineuses. On ne peut juger Gemini sur ce point.

Le tableau suivant résume ces appréciations ; chacune est justifiée dans les sections 2 à 4.

| Critère | C1 | G1 | C2 | G2 | C3 | G3 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Couverture descriptive | bonne | très bonne | bonne | très bonne | bonne | bonne |
| Exactitude des renvois et citations | très bonne | bonne | très bonne | excellente | bonne | bonne |
| Justesse des critiques | bonne, avec deux erreurs notables | bonne mais limitée | très bonne, avec excès | moyenne (reprise de l'auteur) | très bonne, avec erreurs d'inventaire | faible (formules certifiées à tort) |
| Vérification des calculs | bonne | absente | excellente | absente | très bonne | absente, jugement erroné |
| Indépendance du jugement | très bonne | moyenne | très bonne | faible | très bonne | faible |
| Utilité pour l'auteur | très bonne | moyenne | très bonne | moyenne | très bonne | moyenne |
| Langue | très bonne | bonne | très bonne | bonne | très bonne | moyenne |
| Typographie française | très bonne | faible | très bonne | faible | très bonne | faible |
| Concision | faible (au-delà de la consigne) | bonne | moyenne | bonne | moyenne | bonne |

---

## 6. Synthèse consolidée pour l'auteur

On distingue quatre catégories : (A) critique confirmée par les deux rapports et par la vérification ; (B) critique propre à un rapport et vérifiée ; (C) critique propre à un rapport, non vérifiable ou douteuse ; (D) critique réfutée. À l'intérieur de chaque catégorie, les critiques sont rangées par ordre d'importance décroissante.

### 6.1 *Un discours de la méthode au XXIe siècle*

- **A.** La troisième partie s'essouffle et se répète, et le dialogue s'y efface (p. 215 et suivantes) ; le qualificatif « structuraliste » (p. 264) n'est pas expliqué ; la note 96 (p. 233) engage un déterminisme non justifié ; l'apprentissage automatique est traité de façon trop générique (réseaux de neurones à la seule page 150) ; le texte exige une relecture professionnelle (coquilles relevées par les deux rapports, faute latine de la page 278) ; l'enveloppe du prologue reste sans fonction.
- **B.** La thèse centrale glisse du caractère subjectif de la probabilité à son caractère arbitraire, et le livre se contredit (p. 218-219 contre p. 224) ; les règles de score propres et la calibration offrent les critères que le livre dit introuvables (C1). La note 53 écarte les choix collectifs, en tension avec le récit et le manifeste (G1). Erreurs techniques établies par C1 : axiome de positivité (p. 117), date de Socrate (p. 94), notes 30, 77, 80 et 85, $10^{43}$ « suites de coups » (p. 72), épigraphe de Descartes. Défauts de positionnement établis par C1 : bibliographie non reliée au texte, Knight, Raiffa et Schlaifer non discutés, valeur de l'information réinventée, causalité écartée en une note (p. 234), stratégies de jeu dites « conçues par l'homme » (p. 72) alors qu'AlphaZero les contredisait déjà.
- **C.** La note 22 sur Laplace et le subjectivisme (critique défendable, mais affaire d'interprétation historique) ; l'objection des « niveaux de description » contre l'argument sur l'intelligence des machines (C1 : thèse philosophique discutable, non erreur de fait) ; l'absence de l'exemple de la dinde dans l'*History of Western Philosophy* de Russell (non vérifiable ici).
- **D.** La note 42 ne confond pas histogramme et diagramme en secteurs (C1 réfuté). L'exemple du trajet vers l'aéroport ne se résout pas en temps linéaire (C1 réfuté sur ce point, non sur l'idée générale). La définition du risque, page 174, mentionne bien incertitude et conséquences (reproche de C1 excessif). La valeur de $10^{170}$ pour le go n'est pas dans le livre, qui écrit $10^{100}$ (G1 réfuté).

### 6.2 *Agir d'après une représentation du monde*

- **A.** La marge d'humilité $b$ manque de règle de fixation et conduit à l'abstention aux enjeux extrêmes ; la distance optimale du contrôleur reste indéterminée ; la base empirique est étroite et datée ; les paramètres des modèles sont illustratifs ; l'énigme du producteur plus fiable n'est pas reproduite par l'exemple du chapitre 16 ; la genèse assistée expose le livre au risque du prêteur unique.
- **B.** Établis par C2 : la valeur prédictive positive de la page 118 vaut 22,7 %, non 25 % ; les « résultats sous hypothèses » reformulent largement leurs hypothèses ; statuts incohérents (proposition 2, tableau 1), numérotation M1-M3, double définition de la « prudence superflue », notations surchargées ; absence des littératures sur l'ambiguïté, la critique et la discordance de modèle, les accidents organisationnels et le biais d'automatisation ; effectif de METR omis ; quatre calques de « délivrer » (relevé complété). Établi par G2 : les conditions juridiques, assurantielles et réglementaires des remèdes ne sont pas analysées.
- **C.** Le reproche fait au livre de ne pas citer Savage sur les « petits mondes » ou Vaughan sur Challenger est fondé (absences vérifiées), mais son poids relève de l'appréciation ; le rapprochement de Jaynes avec la tradition subjective est discutable, sans être une erreur, puisque le livre écrit « sous des formes diverses ».
- **D.** Le chapitre 0 présente déjà l'énigme comme « une possibilité » (p. 11) ; l'étiquette « Indépendant et précis » est expliquée (p. 117) ; Russell et Norvig ne sont pas crédités de l'invention des mondes possibles (p. 43) : sur ces trois points, les reproches de C2 sont réfutés. Le défaut de division du Pentium n'illustre pas un contrat respecté (exemple de C2 erroné, sans effet sur le livre). Le jugement d'une langue « limpide et idiomatique » sans calque (G2) est démenti par les quatre emplois de « délivrer ».

### 6.3 La revue de littérature

- **A.** Six champs sur neuf n'ont pas de liste de références, et beaucoup d'auteurs sont cités sans date ni titre ; les corrections de la passe 2 (Kim et al., Steyvers et al., Liang et al. 2024 et son corpus, « pénalité de propriété ») ne sont pas reportées dans les champs 8 et 9 ni dans la passe 1 ; les sections d'interfaces sont redondantes.
- **B.** La passe 3 contient deux erreurs formelles (contrainte sur $\lambda_i$, formule de la valeur de quasi-option), un usage douteux de la copule et un $c_{\text{eff}}$ négatif hors du domaine du modèle (C3). La formule d'échappement du champ 8 admet une corrélation unitaire impossible et définit mal $q$ (C3, en partie). Plusieurs attributions sont inexactes : Savage réduit à trois axiomes, Buchak, Knight et Ellsberg, Littlewood et Miller, DeMillo, Lipton et Perlis, Wolpert et Macready (C3). La passe de falsification vise des thèses que le livre ne soutient pas (C3, vérifié dans le livre p. 183 et p. 235). La revue ignore des auteurs centraux du livre (Wynne, Goodman, Hume, Pearl, Dijkstra) et les fondateurs de la sûreté et des facteurs humains (C3). Les coûts de calcul des remèdes, le droit et l'assurance, les systèmes multi-agents sont des angles morts (G3).
- **C.** La lecture de MacKenzie et Spears (critique fondée, mais la revue ne dit pas exactement l'inverse) ; les attributions d'expressions à Mayo (*fallacy of non-exhaustive alternatives*) et à Manski (*assumption-dodging*), présentes dans la revue mais dont l'origine n'a pu être contrôlée ; la date de Ben-Haim ; l'existence des travaux très récents cités par C3 comme vérifiés (Leanstral, FormalRx, prépublication de Bauer, annonce de curl), hors de portée de la présente vérification.
- **D.** Le champ 8 n'attribue pas, dans son état actuel, le biais des détecteurs à Liang et al. (2024) : la critique commune aux deux rapports porte sur la passe 1. Le champ 1 possède une liste de références (C3 réfuté). La passe 3 n'est pas « mathématiquement juste » dans son ensemble (G3 réfuté).

---

## 7. Conclusion

Les deux séries ne sont pas du même genre. Les rapports Gemini sont des notes de lecture fidèles, bien composées, exactes dans leurs renvois, d'une concision qui rend service ; ils décrivent mieux qu'ils ne jugent, et leur jugement tend à épouser l'autoprésentation des sources. Les rapports Claude sont des expertises : ils vérifient, recalculent, situent dans la littérature et discutent ; leur valeur critique est nettement supérieure, et c'est chez eux que se trouvent les découvertes les plus importantes de tout le corpus (l'autocontradiction de la thèse du livre de 2022, l'erreur chiffrée de la page 118 du livre de 2026, les erreurs formelles de la revue).

L'exactitude doit être appréciée au regard du nombre et de la difficulté des affirmations. Sur 89 affirmations des rapports Claude contrôlées, 7 se sont révélées inexactes, 14 partiellement exactes et 1 non vérifiable ; sur 45 affirmations des rapports Gemini, 5 inexactes et 6 partiellement exactes. Les taux sont voisins (environ 8 % et 11 % d'inexactitudes), mais les erreurs ne pèsent pas de la même manière : celles de Claude touchent des inventaires et des critiques trop appuyées, celles de Gemini des reconstructions non vérifiées et, surtout, deux certificats d'exactitude accordés à des formules erronées ou mal définies. On se gardera pourtant d'en conclure que les rapports Claude sont exempts de défauts : ils reprochent à trois reprises à l'auteur de 2026 des omissions que celui-ci a réparées, et l'un d'eux contredit l'autre sur la taille d'une bibliographie.

Ce qu'un lecteur trouvera dans les rapports Gemini et non dans les rapports Claude : une description chapitre par chapitre, paginée, du livre de 2022 ; un exposé très exact de l'architecture formelle du livre de 2026 ; quelques critiques originales et justes (les décisions collectives écartées par la note 53, les conditions juridiques et assurantielles des remèdes, les coûts de calcul et les systèmes multi-agents dans la revue) ; un décompte plus exact des listes de références de la revue. Ce qu'il trouvera dans les rapports Claude et non dans les rapports Gemini : une discussion de la validité des thèses, des calculs refaits, des erreurs de l'auteur établies page par page, une confrontation de la revue au livre, des errata utilisables tels quels, et une langue conforme aux règles de la typographie française. Pour un auteur qui prépare une nouvelle version, les rapports Claude sont les plus utiles, à condition d'en retrancher les points réfutés à la section 6 ; les rapports Gemini leur sont complémentaires, et parfois plus justes sur les faits d'inventaire.

---

## Annexe : table des vérifications

Légende : C1-C3 et G1-G3 comme à la section 1.1 ; « p. » renvoie à la pagination imprimée ; « l. » à la ligne d'un fichier de la revue. Verdicts : exact, inexact, partiellement exact, non vérifiable.

### A. *Un discours de la méthode au XXIe siècle* (2022)

| N° | Rapport | Affirmation | Lieu | Verdict | Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | C1 | L'épigraphe omet « souvent » | p. 5 | exact | Le livre : « ne souffrant aucun délai » ; Descartes : « ne souffrant souvent aucun délai » |
| 2 | C1 | « conférence de Darmouth » | p. 61 | exact | Graphie relevée |
| 3 | C1 | Socrate né « au VIe siècle », deux fois | p. 94 | exact | Deux occurrences |
| 4 | C1 | Prémisse « Socrate est un homme » rétablie seulement par la note 1 | p. 94 | partiellement exact | Elle figure aussi dans le corps du texte, forme « plus classique » |
| 5 | C1 | « Pr(E) > 0 », contradiction avec la note 17 | p. 117 | exact | Vérifié en image (PDF 119) |
| 6 | C1 | « probabilité sur une probabilité » sans sens | p. 221, n. 85 | exact | Citation exacte |
| 7 | C1 | Aucune anticipation « plus juste qu'une autre » | p. 218-219 | exact | Citation exacte |
| 8 | C1 | 95 % « pas plus juste » que 96 % | p. 223, n. 89 | exact | Citation exacte |
| 9 | C1 | Autocontradiction : « obtiendra généralement de meilleurs résultats » | p. 224 | exact | Citation exacte |
| 10 | C1 | Calibration réservée à la décision répétée | p. 185, n. 68 | exact | Mais le livre en parle aussi p. 223 |
| 11 | C1 | Laplace, « fondements de l'interprétation subjectiviste » | p. 123, n. 22 | exact | Citation exacte ; critique défendable |
| 12 | C1 | « une statistique » = « un estimateur » | p. 131, n. 29 | exact | Citation exacte |
| 13 | C1 | Étymologie par « l'empire » | p. 133, n. 30 | exact | Citation exacte |
| 14 | C1 | La note 42 assimile histogramme et camembert | p. 146 | inexact | Le texte dit que les proportions « pourraient être présentées différemment » |
| 15 | C1 | « numérique » au sens contraire à l'usage | p. 149, n. 45 | partiellement exact | Usage spécialisé (optimisation continue) |
| 16 | C1 | « validation croisée » = découpage unique | p. 194, n. 77 | exact | Citation exacte |
| 17 | C1 | $10^{43}$ « suites de coups » = positions | p. 72 | exact | Vérifié en image (PDF 74) |
| 18 | C1 | « milliards de possibilités » sous-estime | p. 74 | exact | $2^{1\,000\,000}$ pour un million de segments |
| 19 | C1 | Trajet résoluble en temps linéaire | p. 69-74 | inexact | Délai et coût : sac à dos à choix multiples, pseudo-polynomial |
| 20 | C1 | $p_e = (u_s - u_0)/(u_1 - u_0)$ | p. 169 | exact | Vérifié en image (PDF 171) |
| 21 | C1 | Saint-Pétersbourg et Allais rattachés à l'aversion au risque | p. 216, n. 80 | exact | Citation exacte |
| 22 | C1 | Risque défini par la seule probabilité ; « il ne le dit pas » | p. 174-175 | partiellement exact | Le livre cite incertitude et conséquences juste avant |
| 23 | C1 | Causalité remplacée par la « régularité » | p. 234, n. 98 | exact | Citation exacte |
| 24 | C1 | « par construction, par nature, par essence » | p. 199 | exact | Citation exacte |
| 25 | C1 | « indéniablement hors de portée des machines » | p. 265 | exact | Citation exacte |
| 26 | C1 | Division des difficultés = « réductionnisme » | p. 243, n. 105 | exact | Citation exacte |
| 27 | C1 | Note 107 située p. 245 | p. 243 | inexact | La note est p. 243 |
| 28 | C1 | 23 références, seul Savage appelé | p. 134, 285-286 | exact | Décompte et recherche |
| 29 | C1 | Ramsey, de Finetti, Popper, Simon, Kahneman, Turing absents ; Knight, Pearl en bibliographie seulement | passim | exact | Aucune occurrence dans le texte |
| 30 | C1 | Descartes absent hors épigraphe, préface, p. 54 et 243 | passim | partiellement exact | Oublie l'épigraphe transformée p. 200 |
| 31 | C1 | Calculs des saynètes exacts | p. 26-28 | exact | 3 œufs ; 58 cm ; 80/500 = 16 % |
| 32 | C1 | Cent vingt et une notes | passim | exact | Dernière note : 121 |
| 33 | C1 | « écran digital », « conservative », « en charge de » | p. 25, 207, 28 | exact | Occurrences relevées |
| 34 | C1 | Poulet chez Russell (1912), dinde chez Chalmers | externe | exact | Connaissance établie |
| 35 | G1 (et C1) | Coquille « DISOURS » | p. 3 (PDF 5) | exact | Faux-titre |
| 36 | G1 (et C1) | Paraphrase d'Einstein | p. 11 | exact | Citation exacte |
| 37 | G1 (et C1) | Enveloppe jamais reprise | p. 15-16 | exact | Aucune occurrence ultérieure |
| 38 | G1 | 21 chapitres, dont 3 signalés par astérisque ; 23 références | table, p. 285-286 | exact | Décompte |
| 39 | G1 (et C1) | Note 53 : agent unique, théorie des jeux écartée | p. 164 | exact | Citation exacte |
| 40 | G1 | « Qui décide ? Dans l'intérêt de qui ? » | p. 44 | exact | Citation exacte |
| 41 | G1 | « décideurs industriels, économiques ou politiques » | p. 274 | exact | Citation exacte |
| 42 | G1 (et C1) | Réseaux de neurones mentionnés p. 150 seulement | p. 150 | exact | Seule occurrence |
| 43 | G1 (et C1) | « structuraliste » non défini, absent de l'index | p. 264, 281-284 | exact | Aucune entrée d'index |
| 44 | G1 (et C1) | « le réel n'est pas intrinsèquement aléatoire » | p. 233, n. 96 | exact | Citation exacte |
| 45 | G1 | La dinde déclarée « rationnelle » | p. 183 | exact | Citation exacte |
| 46 | G1 | « ne sont objectives que les observations » | p. 258 | exact | Guillemets internes omis |
| 47 | G1 | Biais-variance, n. 113 ; validation croisée, n. 77 | p. 255, 194 | exact | Notes repérées |
| 48 | G1 (et C1) | Mise à jour de 0,5 à 0,826 | p. 155 | exact | 0,475/0,575 = 0,826 |
| 49 | G1 | $p^* = (u_2 - u_3)/(u_1 - u_3)$ | p. 169 | partiellement exact | Équivalent, notation non conforme |
| 50 | G1 | Probabilités totales dans le chapitre p. 115-129 | index | inexact | Index : p. 141 et 155 |
| 51 | G1 | *Statista* dans le chapitre p. 33-38 | p. 38, 131 | partiellement exact | p. 38 : « préfixe Stat » ; *Statista* p. 131 |
| 52 | G1 | Exposant « $10^{170}$ » pour le go | p. 72 | inexact | Image : $10^{100}$ |
| 53 | G1 (et C1) | Coquilles p. 8, 33, 59, 82, 187, 259, 260 | id. | exact | Toutes repérées |
| 54 | G1 | $\Pr(400 < Y < 600 \mid c, m)$ | p. 138 | exact | Formule repérée |
| 55 | G1 | PIB prévu à 1,6 % | p. 84 | exact | Repéré |

### B. *Agir d'après une représentation du monde* (2026)

| N° | Rapport | Affirmation | Lieu | Verdict | Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 56 | C2 | xii + 265 p., 277 p. PDF, décalage de 12 | passim | exact | Contrôlé p. 1, 118, 265 |
| 57 | C2 | Encadrés : 10, 15, 9, 12, 21 et 19 | passim | partiellement exact | Cinq décomptes exacts ; 17 « Question à se poser » |
| 58 | C2 | 14 définitions, 5 propositions | passim | exact | Décompte |
| 59 | C2 | Calculs de la soudure, de la course, des seuils, de M2 | p. 27-28, 47, 55-57, 207 | exact | Recalculés |
| 60 | C2 | VPP « ≈ 25 % » vaut 22,7 % | p. 118 | exact | 0,0144/0,0634 = 22,7 % |
| 61 | C2 | Risque 5,57 → 1,93 % et 2,80 → 1,36 % | p. 193 | exact | Tableau 16.1 et recalcul |
| 62 | C2 | Seuils de bascule 6,2 % et 4,2 % | calcul | partiellement exact | 6,15 % juste ; 4,12 % pour le second |
| 63 | C2 | Le chapitre 0 devrait qualifier l'énigme | p. 11 | partiellement exact | « ce calcul montre une possibilité » est déjà écrit |
| 64 | C2 | Proposition 2 : « définition » puis « résultat sous hypothèses » | p. 74-75 | exact | Citations exactes |
| 65 | C2 | Tableau 1 : thèse substantielle classée « définition » | p. 229 | exact | Ligne 1 du tableau |
| 66 | C2 | M3, « le troisième des modèles formels » | p. 85 | exact | Citation exacte |
| 67 | C2 | « Prudence superflue » définie deux fois | p. 203, 245 | exact | Conditions différentes |
| 68 | C2 | Étiquette « Indépendant et précis » trompeuse | p. 117 | partiellement exact | Le livre justifie le nom |
| 69 | C2 | ∩ pour la conjonction | p. 21 | exact | « le symbole ∩ note la conjonction » |
| 70 | C2 | Jaynes rangé « sous une même conception subjective » | p. 45 | partiellement exact | Le livre dit « sous des formes diverses » |
| 71 | C2 | Mondes possibles attribués à Russell et Norvig | p. 43 | partiellement exact | Présentés comme une « manière simple de dire » |
| 72 | C2 | Dinde : « version ultérieure » non attribuée | p. 66 | exact | Chalmers et Taleb absents |
| 73 | C2 | « mêmes hypothèses de comportement élastique » sans renvoi précis | p. 80 | exact | Renvoi global à la commission |
| 74 | C2 | Condition f/s approximative | p. 110 | exact | Condition exacte sur la cote |
| 75 | C2 | « masquer le token suivant » | p. 134 | exact | Citation exacte |
| 76 | C2 | METR cité sans effectif | p. 1, 182-183 | exact | Aucune mention de seize développeurs |
| 77 | C2 | « toute marge plausible » ; encadré sans référence | p. 208-209 | exact | Gilboa, Klibanoff, Hansen absents |
| 78 | C2 | Perrow, Reason, Vaughan, Box, Kennedy et O'Hagan, Parasuraman, Amalberti, Callon, Cartwright, Duhem, Quine, Lakatos absents | passim | exact | Aucune occurrence (homonymes écartés) |
| 79 | C2 | Bibliographie d'environ 75 titres | p. 262-265 | partiellement exact | Environ 69 entrées |
| 80 | C2 | Article de l'auteur cité 32 fois | passim | exact | 32 occurrences |
| 81 | C2 | Seuls calques : « délivrer » p. 109 et 188 | passim | partiellement exact | Aussi p. 26 et 81 |
| 82 | C2 | Eau pure : 99,97 °C selon l'EIT-90 | p. 34 | exact | Le livre écrit 100 °C |
| 83 | C2 | Pentium : contrat respecté | externe | inexact | Le défaut violait IEEE 754 |
| 84 | C2 | « Williams; Norgate » ; « (Finetti 1974) » | p. 264, 23, 45 | exact | Repérés |
| 85 | C2 | « sont engendrés » ; « réinterrogatoire » | p. 255, 247 | exact | Repérés |
| 86 | G2 | Une trentaine de renvois (équations, définitions, propositions, tableaux) | passim | exact | Tous contrôlés |
| 87 | G2 | Statuts des propositions 1 à 5 | p. 67-101 | exact | Conformes |
| 88 | G2 | Challenger : seize vols sans dommage omis | p. 79-80 | exact | Citation exacte |
| 89 | G2 | Deux rectifications de l'article fondateur | p. 238 | exact | Sections 5.5, 6.4, 13.1 |
| 90 | G2 | Risque en baisse (16.1), en hausse (9.3) | p. 115, 193 | exact | 0,1 → 0,9 % ; 5,57 → 1,93 % |
| 91 | G2 | M2 : indépendance de $z$ ; fissure et rafales | p. 204 | exact | Réserve de l'auteur |
| 92 | G2 | *Moffatt* : « brève mention » | p. 137 | partiellement exact | Encadré entier |
| 93 | G2 | « ponts » au statut d'hypothèse de travail | p. 232 | exact | Citation exacte |
| 94 | G2 | « une démarche de travail, non une prescription » | p. ix | exact | Citation exacte |
| 95 | G2 | $p^* = \Delta U/(\Delta U + L)$, éq. 4.1 | p. 54 | exact | Repéré |
| 96 | G2 | Français « limpide et idiomatique » | passim | partiellement exact | Quatre calques de « délivrer » |
| 97 | G2 | Tradition subjective : de Finetti, Savage, Jaynes, Lindley | p. ix, 45 | partiellement exact | Reprise sans réserve sur Jaynes |

### C. Revue de littérature

| N° | Rapport | Affirmation | Lieu | Verdict | Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 98 | C3 | Douze fichiers, environ 34 500 mots | dossier | exact | 34 453 mots |
| 99 | C3 | Sept champs sur neuf sans liste ; champ 9 seul avec le 7e | 01, l. 145 | inexact | Le champ 1 a une liste |
| 100 | C3 | Earman et Roberts non datés, renvoi à la SEP | 01, l. 150 | exact | Entrée repérée |
| 101 | C3 | « training conventions » ; guillemets sur *intersection of falsehoods* | 01, l. 84 | exact | Texte repéré |
| 102 | C3 | NFL attribué à Wolpert et Macready, erreur héritée du livre | 02, l. 71 ; livre p. 265 | exact | Les deux repérés |
| 103 | C3 | Savage réduit à trois axiomes | 04, l. 12 | exact | Texte repéré |
| 104 | C3 | Buchak parmi les critiques des a priori ponctuels | 04, l. 21 | exact | Texte repéré |
| 105 | C3 | Incertitude knightienne = ambiguïté | 04, l. 15 | exact | Texte repéré |
| 106 | C3 | Population commune attribuée à Littlewood et Miller | 05, l. 13 | exact | Texte repéré |
| 107 | C3 | DeMillo, Lipton et Perlis : thèse de la traduction | 06, l. 18 | exact | Texte repéré ; critique fondée |
| 108 | C3 | MacKenzie et Spears enrôlés contre leur thèse | 03, l. 72 | partiellement exact | La revue en tire une thèse organisationnelle qu'ils soutiennent en partie |
| 109 | C3 | Date de 1999 pour Ben-Haim douteuse | 03, l. 41 | non vérifiable | Publications antérieures à 2001 probables |
| 110 | C3 | Formule d'échappement erronée | 08, l. 46-48 | partiellement exact | $\rho \to 1$ impossible si $p \ne q$ ; $q$ dit « marginal » |
| 111 | C3 (et G3) | Liang 2024 cité pour le biais des détecteurs dans le champ 8 | 08, l. 20, 68 | inexact | Absent du champ 8 ; présent en R1, l. 99 |
| 112 | C3 (et G3) | Corpus « ICLR, ICML » de Liang 2024 | 08, l. 67 | exact | Texte repéré |
| 113 | C3 (et G3) | Kim et al. à CHI ; titre de Steyvers et al. | 09, l. 137, 150 | exact | Références repérées |
| 114 | C3 | R1 : Bastani et les « workers under deadline » ; « CFF-style ancrage » | R1, l. 86, 83 | exact | Textes repérés |
| 115 | C3 | R2 : quinze études | R2, tableau | inexact | Quatorze lignes |
| 116 | C3 | R2 : METR situé au « Ch. 1 » | R2, l. 18 ; livre p. 1 | exact | Première mention au chapitre 0 |
| 117 | C3 | R3 : $\lambda_i \in [0, 1/p_0)$ rend l'e-processus négatif | R3, l. 65 | exact | $1 - \lambda_i < 0$ si $\lambda_i > 1$ |
| 118 | C3 | R3 : formule de la quasi-option = valeur de l'information parfaite | R3, l. 38 | exact | Formule classique de la valeur espérée de l'information parfaite |
| 119 | C3 | R3 : $c_{\text{eff}} \le 0$ hors du domaine de M1 | R3, l. 82 ; livre p. 115 | exact | $c \in [0, 1]$ (éq. 9.4) |
| 120 | C3 | Wynne, Goodman, Hume, Pearl, Dijkstra, Reason, Parasuraman, normes absents | dossier | exact | Aucune occurrence |
| 121 | C3 | Citations du livre p. 183 et p. 235 ; Gerstgrasser absent du livre | livre | exact | Citations exactes |
| 122 | C3 | Bibliographie du livre d'environ soixante-dix entrées | livre p. 262-265 | exact | Environ 69 |
| 123 | G3 | Corpus d'environ 284 Ko | dossier | inexact | 266 613 octets |
| 124 | G3 | Six volets sans liste ; 01, l. 145-171 | dossier | exact | Repéré |
| 125 | G3 (et C3) | Belkin non daté, l. 72 | 02, l. 72 | exact | Repéré |
| 126 | G3 | Volet 03 : trois sections thématiques ; *identifiability leakage* l. 24 | 03 | exact | Structure repérée |
| 127 | G3 | Volet 07 : *Core Verified References* ; surcoût de 5 à 10 fois, l. 46 ; l. 112 | 07 | exact | Repéré |
| 128 | G3 | Confusion Liang 2023/2024 dans le volet 08 | 08 | inexact | Voir n° 111 |
| 129 | G3 | GitHub l. 66 ; AI Act art. 50 l. 28 | 08 | exact | Repéré |
| 130 | G3 | Volet 09 : +127 % omis ; caractère observationnel, l. 20 | 09 | exact | Aucune occurrence de 127 ; l. 20 repérée |
| 131 | G3 | Quatorze études dans la passe 2 | R2 | exact | Quatorze lignes |
| 132 | G3 | Passerelles « mathématiquement justes » ; $c_{\text{eff}}$ « rigoureuse » | R3 | inexact | Voir n° 117-119 |
| 133 | G3 | Formule d'échappement : « outil analytique précieux » | 08, l. 46-48 | partiellement exact | Défaut de Fréchet non vu |
| 134 | G3 (et C3) | *Safety clutter* sans année, datée de 2018 en R1 | 04, l. 86 ; R1 | exact | Repéré |

**Récapitulatif.** Rapports Claude : 89 affirmations contrôlées, dont 67 exactes, 14 partiellement exactes, 7 inexactes, 1 non vérifiable. Rapports Gemini : 45 affirmations contrôlées, dont 34 exactes, 6 partiellement exactes, 5 inexactes. Lorsque les deux séries font la même affirmation, la ligne est attribuée au rapport indiqué en premier.
