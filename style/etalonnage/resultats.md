# Étalonnage du juge — résultats

- Date : 2026-11-20 ; juge : claude-opus (juge-style)
- Jeu : dérives réelles des pilotes de première passe, et retouches fidèles tirées des mêmes pilotes (`construire.py`).

| Groupe | Attendu | Résultat |
| :-- | :-- | :-- |
| Dérives nettes (24) | rejet | **24/24 rejetées** |
| Dérives limites (2) | rejet souhaité | 2/2 rejetées |
| Retouches fidèles et utiles (8) | acceptation | **1/8 acceptées** |
| Échanges gratuits de synonymes (4) | l’un ou l’autre | 0 acceptés, 4 rejetés |

## Détail

| Id | Type | Catégorie | Verdict | Raison du juge |
| :-- | :-- | :-- | :-- | :-- |
| E01 | derive | mécanisme substitué | rejete | Les termes du registre « taux d’erreur » et « probabilité d’échappement » disparaissent (« les erreurs individuelles », « l’échappement »), « assèchement » devient « saturation », qui nomme un autre mécanisme, et « pour montrer » devient « pour examiner ». |
| E02 | controle-gratuit | mot retiré | rejete | Seuls les mots « de lecture » sont retirés d’une phrase courte qui fonctionnait. Le gain est nul, et « grille de lecture » est l’expression employée ailleurs dans le livre. |
| E03 | controle-utile | connecteur explicite | rejete ✗ | La phrase fonctionnait déjà. « sans mention d’unité » devient « sans unité », ce qui est moins exact puisque les nombres avaient une unité (des livres-force-secondes) qui n’était simplement pas indiquée. |
| E04 | derive | statut (arguments → démonstrations) | rejete | « des arguments » devient « des démonstrations », ce qui promeut le statut des énoncés. « études de cas » est abrégé en « cas » et « le trajet » devient « le livre ». |
| E05 | controle-utile | verbe précisé | rejete ✗ | « signifie » est remplacé par « désigne », un simple synonyme. « propriété physique […] du mât » devient « caractéristique du mât » : l’adjectif « physique » ne porte plus sur le mât et la négation s’élargit. |
| E06 | derive | glose retirée (raisonner à l’envers) | rejete | La glose qui explique « raisonner à l’envers » (« chercher quelle variation cachée de l’arrière-plan renverserait la conclusion ») est supprimée. |
| E07 | derive | énumération amputée (fiabilité) | rejete | « la fiabilité » disparaît de l’énumération des thèmes du parcours, et « par contrat », qui renvoie à un terme du registre, est supprimé de « composants spécifiés par contrat ». |
| E08 | derive | terme (tests de référence) | rejete | « tests de référence », terme du registre, est remplacé par « batteries de tests ». « qui ne garantit aucune réponse particulière » devient « sans garantie sur une réponse particulière », formule plus faible et moins nette sur la portée. |
| E09 | controle-utile | coupe aux deux-points | accepte | Une phrase de plus de cinquante mots est coupée en deux et un deux-points est retiré. Les chiffres, le seuil, les deux évaluations et le double « rationnellement » sont conservés. |
| E10 | controle-utile | tournure allégée | rejete ✗ | La phrase fonctionnait déjà. Le « si on lui fournit […] elle rendra » d’origine épouse la forme précondition-postcondition d’un contrat, et la reformulation n’apporte pas de gain net. |
| E11 | derive | terme (probabilité d’échappement) | rejete | « la probabilité d’échappement », terme du registre, est réduite à « l’échappement », et « en y glissant périodiquement » disparaît. Or la mesure repose justement sur des erreurs glissées dans le flux, à intervalles réguliers. |
| E12 | derive | probabilités (jugement → fréquence) | rejete | « dans le cas le plus probable » devient « le plus fréquent » : un jugement sur une traversée unique devient une fréquence, ce qui contredit le propos du paragraphe. Le futur « départagera » passe en outre au présent. |
| E13 | controle-gratuit | synonyme | rejete | « scènes » est remplacé par « épisodes », un simple synonyme, d’autant que « épisode » est déjà employé juste avant (« Un troisième épisode »). |
| E14 | derive | définitions retirées | rejete | Les deux gloses entre parenthèses qui définissent « taux d’erreur » et « probabilité d’échappement » sont retirées, et la condition « sans être contredites à temps » disparaît. |
| E15 | derive | terme (frontière en dents de scie) | rejete | « frontière en dents de scie », terme du registre, devient « profil de compétence en dents de scie ». « remarquable » est affaibli en « capable », et l’idée que rien ne signale le franchissement de « sa limite » est perdue. |
| E16 | derive-limite | sens ambigu (qui cadre qui) | rejete | « la consigne soumise par l’utilisateur transmet déjà son propre cadre » devient « lui cède déjà le cadre du problème » : le cadre n’est plus celui de l’utilisateur, alors que c’est tout le mécanisme décrit. « les pousse à » est aussi affaibli en « favorise ». |
| E17 | controle-gratuit | synonyme | rejete | « imaginaires » est remplacé par « fictives », un simple synonyme. |
| E18 | controle-utile | coupe à la conjonction | rejete ✗ | La coupe de la phrase en deux est acceptable, mais « qui n’a jamais figuré dans son cadre » devient « absente de son cadre » et perd « jamais ». Or c’est ce mot qui dit que la variable a manqué tout au long de la série. |
| E19 | controle-utile | récit plus direct | rejete ✗ | « pourtant », qui marque la concession après les trois mesures qui confirmaient la règle, disparaît. |
| E20 | derive | portée (« seulement » retiré, modal affaibli) | rejete | « pourrait omettre » devient « peut omettre », alors que le registre donne le conditionnel. La glose qui définit « verrou » (« c’est-à-dire un point où… ») est retirée, et « accordée seulement après » perd « seulement ». |
| E21 | derive | propos central affaibli (infinité → foule) | rejete | « une infinité d’autres » est affaibli en « une foule d’autres ». Surtout, « puis livre une conclusion ou un chiffre » est supprimé, alors que la phrase suivante (« Sur la foi de ce chiffre ») y renvoie. |
| E22 | derive | statut (réflexion → théorie) | rejete | « une réflexion générale » devient « une théorie générale » : une réflexion est promue en théorie. |
| E23 | controle-gratuit | synonyme | rejete | « lorsque » est remplacé par « quand » dans une phrase courte qui fonctionnait : c’est un simple synonyme. |
| E24 | derive | énumération amputée (mathématicien, décideur) | rejete | Deux profils disparaissent de l’énumération, « le mathématicien » et « le décideur », alors qu’ils correspondent aux parcours de lecture. « pratiques » devient « métiers » et « préoccupations » devient « contraintes ». |
| E25 | derive | terme (producteur et contrôleur) | rejete | « au producteur et au contrôleur », termes du registre, est remplacé par « aux deux voies », et « respectifs » est supprimé. |
| E26 | derive | portée (possibilité → certitude) | rejete | « peut être pris en défaut » devient « cédera » : une possibilité devient une certitude. « ne révélera jamais » perd « jamais », et « modèle statistique » perd « statistique ». |
| E27 | controle-utile | « Or » retiré, phrase resserrée | rejete ✗ | Le « Or » initial disparaît, mais l’opposition explicite « tandis que » est remplacée par une juxtaposition après un point-virgule, alors que la spécification demande d’éviter la parataxe. L’objet « ces impulsions » disparaît aussi. |
| E28 | controle-utile | tournure plus directe | rejete ✗ | « n’eut aucun mal à désigner » devient « identifia rapidement » : la facilité devient de la rapidité, ce qui ajoute un détail factuel absent de la source. |
| E29 | derive | lien d’exemple retiré (ferrure) | rejete | « tout facteur omis » devient « un facteur omis » et « tous » disparaît. Le rappel de l’exemple courant « — la corrosion de la ferrure — » est supprimé. Enfin, « se copient l’un l’autre » est inexact pour plusieurs contrôles, qui ne se copient pas mais puisent à la même source. |
| E30 | derive | probabilités (série de calibration) | rejete | La série de référence change : « la longue série des jours où elle a été émise » devient « une longue série de jours comparables ». La calibration se juge sur les jours où la prévision a été émise, non sur des jours comparables. |
| E31 | derive | remède affaibli (ligne budgétaire) | rejete | « une ligne budgétaire à part » devient « une ressource budgétée », ce qui fait perdre l’idée d’un budget séparé et protégé. |
| E32 | derive-limite | statut (arguments développés → résultats établis) | rejete | « l’un des arguments centraux […] développé au » devient « l’un des résultats centraux […] établi au » : un argument est promu en résultat établi. « Prétendre fournir » perd aussi « Prétendre ». |
| E33 | derive | sens (présupposé ajouté) | rejete | « la plausibilité remplace la vérité comme objectif » ajoute le présupposé que la vérité était auparavant l’objectif d’optimisation. « montre ce qui change » devient « suit le passage », ce qui change le rôle du chapitre. |
| E34 | derive | glose retirée + exigence impossible | rejete | La glose « (exploratoire ou établie, ce qui a été contrôlé de façon indépendante) » est supprimée. « ses hypothèses principales » devient « ses hypothèses », ce qui rend l’exigence irréaliste. |
| E35 | derive | portée (suffisance ajoutée) | rejete | « il dispose de quatre questions simples […] pour rouvrir le cadre » devient « quatre questions simples suffisent » : une aide devient une condition suffisante. |
| E36 | derive | provenance sur-affirmée | rejete | Le passage relève de la section verrouillée « Genèse et responsabilité ». De plus, l’ajout de « restés humains d’un bout à l’autre » durcit un fait, « déterminant » disparaît, et le parallèle « tout aussi inexact » avec la phrase précédente est rompu. |
| E37 | derive | fait durci (doutes → alertes) | rejete | « doutes sur la trajectoire » devient « alertes sur la trajectoire », ce qui change ce que rapporte la source. « bien d’autres défaillances » ajoute un présupposé, et « montrer du doigt » est remplacé par « désigner du doigt », un simple synonyme. |
| E38 | derive | français (gouvernance → gouvernement) | rejete | « la gouvernance organisationnelle » devient « le gouvernement » : le sens change (gouvernement n’est pas gouvernance) et la précision « organisationnelle » est perdue. |
