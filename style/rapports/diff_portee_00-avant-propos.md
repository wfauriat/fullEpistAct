# Contrôle de portée — `00-avant-propos`

- Original : `monographie/chapitres/00-avant-propos.md`
- Réécriture : `style/pilots/00-avant-propos.md`
- Généré le 2026-11-20 par `style/diff_portee.py` (STYLE_PASS_SPEC.md, §6.3)

**Mode d'emploi.** Pour chaque case : la cocher et écrire après « décision : » *accepté* ou *rétabli* (avec, au besoin, la formulation retenue). `python3 style/diff_portee.py --controle <ce fichier>` échoue tant qu'une case reste vide. ⛔ = invariant de la spec touché ; ⚠ = portée ou contenu possiblement modifié. Les éléments · (reformulation à effectif constant, variantes morphologiques, mots ajoutés) sont à parcourir et ne demandent pas de décision.

**Bilan :** 28 décision(s) à prendre — ⛔ 0 · ⚠ 28 ; 22 élément(s) · à parcourir

## Synthèse par section

| Section | ⛔ | ⚠ | · |
| :-- | --: | --: | --: |
| `sec:avant-propos` Avant-propos |  |  |  |
| `sec:avant-propos-objet` Pourquoi ce livre |  | 6 | 2 |
| `sec:avant-propos-posture` Une démarche de travail, non une prescription |  | 8 | 2 |
| `sec:avant-propos-public` À qui s’adresse cet ouvrage |  | 3 | 4 |
| `sec:avant-propos-genese` Genèse et responsabilité |  | 5 | 6 |
| `sec:avant-propos-lecture` Mode d’emploi |  | 1 |  |
| `sec:avant-propos-regle` La règle du texte principal |  | 2 | 4 |
| `sec:avant-propos-encadres` Les six types d’encadrés |  | 1 | 1 |
| `sec:avant-propos-statuts` Énoncés et statuts épistémiques |  | 1 | 1 |
| `sec:avant-propos-terminologie` Terminologie, notations et parcours |  | 1 | 2 |

## Invariants structurels (fichier entier)

Aucune différence : identifiants, renvois, attributs `statut` et clés de citation identiques.

## `sec:avant-propos-objet` — Pourquoi ce livre

- [ ] ⚠ Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 3 → 2 (effectif modifié) — décision : 
    - retiré : « … de complexité que les règles écrites à la main ne **pouvaient** pas traverser mais ils ont payé cette portée nouvelle en … »
- [ ] ⚠ Modaux et atténuateurs — *tendre à* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … lent les signes visibles de l'hésitation humaine l'indépendance des relectures **tendent à** s'éroder ou à se corréler en silence Comprendre ce basculement … »
- [ ] ⚠ Quantificateurs absolus — *tout / tous / toute(s)* : 4 → 3 (effectif modifié) — décision : 
    - retiré : « … sont enchaînés dans des flux automatisés ou sollicités simultanément par **toute** une communauté professionnelle les mécanismes mêmes qui permettaient de détecter … »
- [ ] ⚠ Quantificateurs absolus — *jamais* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … fiabilité des systèmes et du génie logiciel cette formalisation n'est **jamais** une fin en soi Elle sert d'instrument de méthode et … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *chaîne* : 1 → 0
    -     retiré : « … sous l'effet conjugué de l'apprentissage automatique et de l'automatisation des **chaînes** de traitement Pendant des décennies l'informatique classique a construit sa … »
    - *composant appris* : 1 → 0
    -     retiré : « … garantie préalable et à l'adresse précise des défaillances Lorsque ces **composants appris** sont enchaînés dans des flux automatisés ou sollicités simultanément par … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (18) — décision : 
    - *infinité* : « … retient certaines variables en écarte une **infinité** d'autres relie le tout par des … »
    - *ouvrage* : « … temps lorsque nous nous trompons Si **l'ouvrage** mobilise en chemin le vocabulaire de … »
    - *hygiène* : « … Elle sert d'instrument de méthode et **d'hygiène** intellectuelle énoncer les hypothèses là où … »
    - *intellectuelle* : « … sert d'instrument de méthode et d'hygiène **intellectuelle** énoncer les hypothèses là où elles … »
    - *assurer* : « … hypothèses là où elles sont posées **assurer** la cohérence de l'enchaînement d'un bout … »
    - *cohérence* : « … où elles sont posées assurer la **cohérence** de l'enchaînement d'un bout à l'autre … »
    - *portent* : « … exemple concret ou une analyse opérationnelle **portent** mieux le propos qu'une équation c'est … »
    - *singulièrement* : « … est à la fois ancienne et **singulièrement** actuelle Elle est ancienne dans sa … »
    - *actuelle* : « … à la fois ancienne et singulièrement **actuelle** Elle est ancienne dans sa structure … »
    - *conjugué* : « … aujourd'hui un relief inédit sous l'effet **conjugué** de l'apprentissage automatique et de l'automatisation … »
    - *chaînes* : « … l'apprentissage automatique et de l'automatisation des **chaînes** de traitement Pendant des décennies l'informatique … »
    - *traitement* : « … et de l'automatisation des chaînes de **traitement** Pendant des décennies l'informatique classique a … »
    - *renonçant* : « … ont payé cette portée nouvelle en **renonçant** à la garantie préalable et à … »
    - *sollicités* : « … enchaînés dans des flux automatisés ou **sollicités** simultanément par toute une communauté professionnelle … »
    - *simultanément* : « … dans des flux automatisés ou sollicités **simultanément** par toute une communauté professionnelle les … »
    - *permettaient* : « … communauté professionnelle les mécanismes mêmes qui **permettaient** de détecter nos erreurs la friction … »
    - *érodent* : « … de l'hésitation humaine l'indépendance des relectures **s'érodent** ou se corrèlent en silence Comprendre … »
    - *corrèlent* : « … l'indépendance des relectures s'érodent ou se **corrèlent** en silence Comprendre ce basculement exige … »
- · Lecture des probabilités — *probable / probabilité* : 3 → 3 (reformulé autour)
    - retiré : « … par des règles logiques des équations ou des distributions de **probabilité** puis livre une conclusion ou un chiffre Sur la foi … »
    - ajouté : « … par des règles logiques des équations ou des distributions de **probabilité** Sur la foi du chiffre ou de la conclusion qui … »
- · Mots pleins : 3 variante(s), 10 ajout(s)
    - variantes probables : chercher → cherche, traverser → traverse, détecter → détection
    - ajoutés : écartant, constitue, empêcher, éclaire, entière, ressorts, ordinaires, tendent, corréler, demande

## `sec:avant-propos-posture` — Une démarche de travail, non une prescription

- [ ] ⚠ Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … recenser les questions laissées ouvertes et indiquer quelles observations empiriques **pourraient** mettre l'argument en défaut »
- [ ] ⚠ Modaux et atténuateurs — *tendre à* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … quantitative fait partie intégrante du projet Ainsi l'indépendance d'un contrôle **tend à** entrer en tension avec sa comparabilité plus un regard extérieur … »
- [ ] ⚠ Modaux et atténuateurs — *en général / généralement* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … mieux il peut percevoir nos omissions mais plus il est **en général** difficile et coûteux de traduire son objection en une comparaison … »
- [ ] ⚠ Statut épistémique — *établir* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … de pensée contredirait d'ailleurs l'un des résultats centraux du livre **établi** au toute procédure chargée d'auditer un cadre repose elle-même sur … »
- [ ] ⚠ Statut épistémique — *argument* : 2 → 1 (effectif modifié) — décision : 
    - retiré : « … justesse de nos cadres de pensée contredirait d'ailleurs l'un des **arguments** centraux du livre développé au toute procédure chargée d'auditer un … »
- [ ] ⚠ Statut épistémique — *résultat* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … justesse de nos cadres de pensée contredirait d'ailleurs l'un des **résultats** centraux du livre établi au toute procédure chargée d'auditer un … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *affirmation* : 1 → 0
    -     retiré : « … réelle entre l'indépendance d'un contrôle et sa comparabilité avec l **affirmation** qu'il vérifie plus un regard extérieur est éloigné de nos … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (19) — décision : 
    - *développé* : « … l'un des arguments centraux du livre **développé** au toute procédure chargée d'auditer un … »
    - *adoptée* : « … un cran plus haut La posture **adoptée** ici est celle d'une démarche de … »
    - *constitue* : « … irréductibles de la pratique quantitative ne **constitue** pas un aveu d'impuissance mais l'un … »
    - *impuissance* : « … quantitative ne constitue pas un aveu **d'impuissance** mais l'un des objectifs mêmes du … »
    - *objectifs* : « … un aveu d'impuissance mais l'un des **objectifs** mêmes du livre Il existe une … »
    - *affirmation* : « … d'un contrôle et sa comparabilité avec **l'affirmation** qu'il vérifie plus un regard extérieur … »
    - *vérifie* : « … et sa comparabilité avec l'affirmation qu'il **vérifie** plus un regard extérieur est éloigné … »
    - *général* : « … omissions mais plus il est en **général** difficile et coûteux de traduire son … »
    - *difficile* : « … mais plus il est en général **difficile** et coûteux de traduire son objection … »
    - *permanente* : « … Il existe de même une tension **permanente** entre la nécessité d'explorer le monde … »
    - *nécessité* : « … même une tension permanente entre la **nécessité** d'explorer le monde pour découvrir ce … »
    - *sécurité* : « … les dissimuler sous des marges de **sécurité** de façade ou des procédures de … »
    - *purement* : « … façade ou des procédures de validation **purement** rituelles est la première condition pour … »
    - *méthode* : « … gouverner Par souci de cohérence cette **méthode** est appliquée à l'ouvrage lui-même Chacune … »
    - *jalonnent* : « … lui-même Chacune des propositions structurantes qui **jalonnent** le texte est accompagnée de son … »
    - *robustesse* : « … et d'une discussion critique de sa **robustesse** précisant sous quelles hypothèses elle tient … »
    - *situations* : « … hypothèses elle tient et dans quelles **situations** elle s'affaiblit La conclusion reprend l'ensemble … »
    - *ensemble* : « … situations elle s'affaiblit La conclusion reprend **l'ensemble** de cet échafaudage pour en dresser … »
    - *laissées* : « … le bilan critique recenser les questions **laissées** ouvertes et indiquer quelles observations empiriques … »
- · Statut épistémique — *hypothèse* : 3 → 3 (reformulé autour)
    - retiré : « … la tradition bayésienne subjective entend le jugement rationnel la meilleure **hypothèse** de travail disponible compte tenu de ce que l'on sait … »
    - ajouté : « … la tradition bayésienne subjective entend le jugement rationnel la meilleure **hypothèse** disponible compte tenu de ce que l'on sait retenue faute … »
- · Mots pleins : 4 variante(s), 10 ajout(s)
    - variantes probables : propose → proposition, éloigné → éloigne, validation → validations, propositions → proposition
    - ajoutés : trouvera, difficulté, évidence, intégrante, devient, analogue, exigence, affiche, restées, mettraient

## `sec:avant-propos-public` — À qui s’adresse cet ouvrage

- [ ] ⚠ Statut épistémique — *argument* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … mobilisé dans les termes mêmes où la suite de l **argument** l'emploie Le propos touche toutefois des pratiques dont les préoccupations … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *adresse* : 0 → 1
    -     ajouté : « Ce livre s **adresse** d'abord aux professionnels de culture scientifique et technique ingénieurs analystes … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (10) — décision : 
    - *premier* : « Ce livre a été conçu en **premier** lieu pour des professionnels de culture … »
    - *occasion* : « … formation mais n'ont pas toujours eu **l'occasion** de les pratiquer comme un instrument … »
    - *instrument* : « … l'occasion de les pratiquer comme un **instrument** quotidien de raisonnement sur la décision … »
    - *épargner* : « … les modes de défaillance Pour leur **épargner** tout prérequis implicite le et des … »
    - *pratiques* : « … l'emploie Le propos touche toutefois des **pratiques** dont les préoccupations et les défenses … »
    - *préoccupations* : « … touche toutefois des pratiques dont les **préoccupations** et les défenses naturelles diffèrent sensiblement … »
    - *mathématicien* : « … simulations multiphysiques le statisticien ou le **mathématicien** attentif aux hypothèses de ses théorèmes … »
    - *décideur* : « … frontières irrégulières de ses modèles le **décideur** ou le responsable d'institution chargé d'organiser … »
    - *ouvrage* : « … Afin que chacun puisse entrer dans **l'ouvrage** selon ses propres questions la fin … »
    - *propres* : « … puisse entrer dans l'ouvrage selon ses **propres** questions la fin du propose huit … »
- · Quantificateurs absolus — *tout / tous / toute(s)* : 1 → 1 (reformulé autour)
    - retiré : « … des contrôles et les modes de défaillance Pour leur épargner **tout** prérequis implicite le et des encadrés dédiés rappellent chaque outil … »
    - ajouté : « … fiabilité des contrôles et les modes de défaillance Pour éviter **tout** prérequis implicite le et des encadrés dédiés rappellent chaque outil … »
- · Quantificateurs absolus — *toujours* : 1 → 1 (reformulé autour)
    - retiré : « … la logique au cours de leur formation mais n'ont pas **toujours** eu l'occasion de les pratiquer comme un instrument quotidien de … »
    - ajouté : « … croisé les probabilités et la logique durant leur formation sans **toujours** les pratiquer au quotidien pour raisonner sur la décision la … »
- · Lecture des probabilités — *probable / probabilité* : 1 → 1 (reformulé autour)
    - retiré : « … de recherche ou d'études qui ont croisé le calcul des **probabilités** et la logique au cours de leur formation mais n'ont … »
    - ajouté : « … logiciels responsables de recherche ou d'études qui ont croisé les **probabilités** et la logique durant leur formation sans toujours les pratiquer … »
- · Mots pleins : 1 variante(s), 4 ajout(s)
    - variantes probables : raisonnement → raisonner
    - ajoutés : adresse, métiers, contraintes, concerne

## `sec:avant-propos-genese` — Genèse et responsabilité

- [ ] ⚠ Modaux et atténuateurs — *pouvoir (peut, pourrait…)* : 3 → 1 (effectif modifié) — décision : 
    - retiré : « … définitions et des analyses présentées dans ces pages L'article cité **peut** être lu à cet égard comme le témoin d'un travail … »
    - retiré : « … humaine la manière dont un texte a été construit ne **peut** certifier son propre cadre Comme dans toute entreprise scientifique et … »
- [ ] ⚠ Quantificateurs absolus — *tout / tous / toute(s)* : 5 → 4 (effectif modifié) — décision : 
    - retiré : « … de grands modèles de langage Ces outils ont été mobilisés **tout** au long du travail comme instruments d'exploration documentaire à travers … »
    - retiré : « … beaucoup aux travaux cités au fil des chapitres Il serait **tout** aussi inexact d'effacer le rôle déterminant de la direction et … »
    - retiré : « … Le paradoxe n'est pourtant qu'apparent il illustre la posture défendue **tout** au long du livre Il ne s'agit ni de récuser … »
    - retiré : « … été construit ne peut certifier son propre cadre Comme dans **toute** entreprise scientifique et technique soumise à l'examen critique de ses … »
    - ajouté : « … avec de grands modèles de langage Ces outils ont servi **tout** au long du travail à explorer des littératures habituellement séparées … »
    - ajouté : « … paradoxe n'est qu'apparent car il illustre la posture défendue dans **tout** l'ouvrage ne pas récuser par principe des instruments d'une portée … »
    - ajouté : « … texte a été construit ne certifie son propre cadre Comme **tout** travail scientifique et technique soumis à l'examen des pairs cet … »
- [ ] ⚠ Quantificateurs absolus — *d'un bout à l'autre* : 0 → 1 (effectif modifié) — décision : 
    - ajouté : « … la conduite et le filtrage du travail sont restés humains **d'un bout à l'autre** La thèse centrale prolonge une réflexion engagée avant le recours … »
- [ ] ⚠ Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme) — décision : 
    - *cadre* : 2 → 1
    -     retiré : « … la rédaction de cette monographie ont été développées dans le **cadre** d'un dialogue itératif avec de grands modèles de langage Ces … »
    - *vérification* : 0 → 1
    -     ajouté : « … l'élimination des rapprochements fragiles la révision des arguments et la **vérification** logique ont relevé d'une décision humaine L'auteur assume seul la … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (27) — décision : 
    - *développements* : « Un ouvrage qui consacre des **développements** détaillés à la traçabilité des affirmations … »
    - *détaillés* : « Un ouvrage qui consacre des développements **détaillés** à la traçabilité des affirmations et … »
    - *manière* : « … se doit d'être transparent sur la **manière** dont il a lui-même été élaboré … »
    - *élaboré* : « … manière dont il a lui-même été **élaboré** L'architecture argumentative et la rédaction de … »
    - *développées* : « … rédaction de cette monographie ont été **développées** dans le cadre d'un dialogue itératif … »
    - *mobilisés* : « … de langage Ces outils ont été **mobilisés** tout au long du travail comme … »
    - *documentaire* : « … long du travail comme instruments d'exploration **documentaire** à travers des littératures habituellement séparées … »
    - *travers* : « … travail comme instruments d'exploration documentaire à **travers** des littératures habituellement séparées philosophie des … »
    - *épreuve* : « … les raisonnements mettre les formulations à **l'épreuve** d'objections croisées et rédiger une large … »
    - *inexact* : « … part du texte lui-même Il serait **inexact** de minimiser cet apport l'ampleur de … »
    - *minimiser* : « … texte lui-même Il serait inexact de **minimiser** cet apport l'ampleur de la synthèse … »
    - *effacer* : « … chapitres Il serait tout aussi inexact **d'effacer** le rôle déterminant de la direction … »
    - *déterminant* : « … tout aussi inexact d'effacer le rôle **déterminant** de la direction et du filtrage … »
    - *direction* : « … d'effacer le rôle déterminant de la **direction** et du filtrage humains dans ce … »
    - *processus* : « … et du filtrage humains dans ce **processus** hybride La thèse centrale de l'ouvrage … »
    - *hybride* : « … du filtrage humains dans ce processus **hybride** La thèse centrale de l'ouvrage prolonge … »
    - *synthétique* : « … d'abord été exposée sous une forme **synthétique** dans un article seule référence de … »
    - *propres* : « … seule référence de l'auteur à ses **propres** travaux dans ce livre D'une étape … »
    - *sélectionné* : « … l'auteur a fixé les orientations théoriques **sélectionné** les exemples écarté les rapprochements fragiles … »
    - *articulation* : « … révisé les arguments et vérifié leur **articulation** logique L'auteur assume l'entière responsabilité de … »
    - *entière* : « … vérifié leur articulation logique L'auteur assume **l'entière** responsabilité de chacune des propositions des … »
    - *lecteur* : « … mais non une garantie absolue Le **lecteur** relèvera peut-être l'ironie qu'il y a … »
    - *soi-même* : « … de l'inférence automatisée tout en recourant **soi-même** aux outils les plus récents de … »
    - *automatisation* : « … outils les plus récents de cette **automatisation** Le paradoxe n'est pourtant qu'apparent il … »
    - *entreprise* : « … son propre cadre Comme dans toute **entreprise** scientifique et technique soumise à l'examen … »
    - *soumise* : « … dans toute entreprise scientifique et technique **soumise** à l'examen critique de ses pairs … »
    - *critique* : « … scientifique et technique soumise à l'examen **critique** de ses pairs ce livre demande … »
- · Quantificateurs absolus — *aucun(e)* : 2 → 2 (reformulé autour)
    - retiré : « … été produit Surtout ce mode d'élaboration ne confère à l'ouvrage **aucune** autorité particulière ni aucune validation de principe Pas plus qu'un … »
    - ajouté : « … d'un résultat Surtout ce mode d'élaboration ne confère au livre **aucune** autorité particulière ni aucune validation de principe Pas plus qu'un … »
- · Quantificateurs absolus — *seul(e) / seulement / uniquement* : 3 → 3 (reformulé autour)
    - retiré : « … synthèse transdisciplinaire réunie ici n'aurait pas été accessible à l'auteur **seul** sous cette forme et dans ce délai Le fond de … »
    - ajouté : « … la vérification logique ont relevé d'une décision humaine L'auteur assume **seul** la responsabilité des propositions des définitions et des analyses présentées … »
- · Statut épistémique — *argument* : 2 → 2 (reformulé autour)
    - retiré : « … cette forme et dans ce délai Le fond de l **argument** quant à lui doit beaucoup aux travaux cités au fil … »
    - retiré : « … théoriques sélectionné les exemples écarté les rapprochements fragiles révisé les **arguments** et vérifié leur articulation logique L'auteur assume l'entière responsabilité de … »
    - ajouté : « … forme ni dans ce délai Quant au fond de l **argument** il doit beaucoup aux travaux cités au fil des chapitres … »
    - ajouté : « … choix des exemples l'élimination des rapprochements fragiles la révision des **arguments** et la vérification logique ont relevé d'une décision humaine L'auteur … »
- · Statut épistémique — *résultat* : 1 → 1 (reformulé autour)
    - retiré : « … jamais masquer les conditions dans lesquelles un texte ou un **résultat** a été produit Surtout ce mode d'élaboration ne confère à … »
    - ajouté : « … jamais masquer les conditions de production d'un texte ou d'un **résultat** Surtout ce mode d'élaboration ne confère au livre aucune autorité … »
- · Statut épistémique — *théorie / théorème* : 1 → 1 (reformulé autour)
    - retiré : « … livre D'une étape à l'autre l'auteur a fixé les orientations **théoriques** sélectionné les exemples écarté les rapprochements fragiles révisé les arguments … »
    - ajouté : « … seule référence personnelle du volume À chaque étape les orientations **théoriques** le choix des exemples l'élimination des rapprochements fragiles la révision … »
- · Mots pleins : 6 variante(s), 11 ajout(s)
    - variantes probables : exploration → explorer, recourir → recours, vérifié → vérification, recourant → recours, produit → production, certifier → certifie
    - ajoutés : soumettre, resserrée, personnelle, élimination, révision, décision, témoigne, antérieur, constitue, utilisant, propose

## `sec:avant-propos-lecture` — Mode d’emploi

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (3) — décision : 
    - *organisé* : « L'ouvrage est **organisé** de manière à séparer nettement le … »
    - *manière* : « L'ouvrage est organisé de **manière** à séparer nettement le fil conducteur … »
    - *séparer* : « L'ouvrage est organisé de manière à **séparer** nettement le fil conducteur de l'argument … »

## `sec:avant-propos-regle` — La règle du texte principal

- [ ] ⚠ Statut épistémique — *argument* : 1 → 0 (effectif modifié) — décision : 
    - retiré : « … aucun maillon du raisonnement ces blocs éclairent et consolident l **argument** mais n'en portent jamais seuls une étape indispensable Les exemples … »
- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (4) — décision : 
    - *viennent* : « … seul tenant Six types d'encadrés balisés **viennent** ponctuer les chapitres pour rappeler un … »
    - *choisit* : « … question de diagnostic Un lecteur qui **choisit** de passer les encadrés d'approfondissement théorique … »
    - *approfondissement* : « … qui choisit de passer les encadrés **d'approfondissement** théorique ou critique Boîte à outils … »
    - *portent* : « … éclairent et consolident l'argument mais n'en **portent** jamais seuls une étape indispensable Les … »
- · Quantificateurs absolus — *jamais* : 1 → 1 (reformulé autour)
    - retiré : « … raisonnement ces blocs éclairent et consolident l'argument mais n'en portent **jamais** seuls une étape indispensable Les exemples quantitatifs et les études … »
    - ajouté : « … aucun maillon du raisonnement ils l'éclairent et le consolident sans **jamais** en porter seuls une étape indispensable Les exemples quantitatifs et … »
- · Quantificateurs absolus — *seul(e) / seulement / uniquement* : 2 → 2 (reformulé autour)
    - retiré : « … ces blocs éclairent et consolident l'argument mais n'en portent jamais **seuls** une étape indispensable Les exemples quantitatifs et les études de … »
    - ajouté : « … raisonnement ils l'éclairent et le consolident sans jamais en porter **seuls** une étape indispensable Les exemples quantitatifs et les études de … »
- · Statut épistémique — *théorie / théorème* : 1 → 1 (reformulé autour)
    - retiré : « … diagnostic Un lecteur qui choisit de passer les encadrés d'approfondissement **théorique** ou critique Boîte à outils Noyau formel Nuance et discussion … »
    - ajouté : « … une question de diagnostic Un lecteur qui saute les encadrés **théoriques** ou critiques Boîte à outils Noyau formel Nuance et discussion … »
- · Mots pleins : 1 variante(s), 0 ajout(s)
    - variantes probables : ponctuer → ponctuent

## `sec:avant-propos-encadres` — Les six types d’encadrés

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (9) — décision : 
    - *chapitres* : « Tout au long des **chapitres** ces encadrés obéissent à un code … »
    - *utilisée* : « … et de fixer la formulation exacte **utilisée** dans le livre L'annexe regroupe l'ensemble … »
    - *ensemble* : « … utilisée dans le livre L'annexe regroupe **l'ensemble** de ces rappels sous forme d'aide-mémoire … »
    - *choisis* : « … paramètres retenus récapitulés dans l'annexe sont **choisis** pour mettre une propriété structurelle à … »
    - *fournir* : « … propriété structurelle à nu non pour **fournir** l'estimation empirique d'une grandeur réelle Étude … »
    - *empirique* : « … à nu non pour fournir l'estimation **empirique** d'une grandeur réelle Étude de cas … »
    - *mesures* : « … des expériences de terrain dont les **mesures** dépendent d'une génération particulière de modèles … »
    - *dépendent* : « … expériences de terrain dont les mesures **dépendent** d'une génération particulière de modèles et … »
    - *directement* : « … de développement une question de diagnostic **directement** transposable à ses propres modèles à … »
- · Mots pleins : 2 variante(s), 1 ajout(s)
    - variantes probables : estimation → estimer, organisation → organisations
    - ajoutés : servent

## `sec:avant-propos-statuts` — Énoncés et statuts épistémiques

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (2) — décision : 
    - *ouvrage* : « … et les cinq propositions principales de **l'ouvrage** sont mises en évidence dans des … »
    - *évidence* : « … principales de l'ouvrage sont mises en **évidence** dans des environnements numérotés Conformément à … »
- · Mots pleins : 0 variante(s), 1 ajout(s)
    - ajoutés : apparaissent

## `sec:avant-propos-terminologie` — Terminologie, notations et parcours

- [ ] ⚠ Mots pleins perdus sans équivalent dans la section (3) — décision : 
    - *associé* : « … flottement sémantique chaque concept technique est **associé** à un terme français unique Ce … »
    - *caractères* : « … unique Ce terme est mis en **caractères** gras et défini lors de sa … »
    - *conclut* : « … formel réduit au minimum et se **conclut** par les parcours de lecture thématiques »
- · Quantificateurs absolus — *tout / tous / toute(s)* : 2 → 2 (reformulé autour)
    - retiré : « Afin d'éviter **tout** flottement sémantique chaque concept technique est associé à un terme … »
    - ajouté : « Pour éviter **tout** flottement sémantique chaque concept technique correspond à un terme français … »
- · Mots pleins : 0 variante(s), 2 ajout(s)
    - ajoutés : correspond, présenter

