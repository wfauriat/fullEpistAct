# Dossier du juge — lot d’étalonnage

- Chapitres d’origine : `monographie/chapitres/00-avant-propos.md` et `monographie/chapitres/00-cartographier.md` (non modifiés ; les numéros de ligne renvoient à ces fichiers ; les lire pour le contexte).
- Retouches soumises : **38**, issues de plusieurs passes de réécriture, présentées dans le désordre.
- Consignes : `.claude/agents/juge-style.md`. Sortie attendue : `style/lots/_etalonnage/verdicts.json`.
- Les alertes automatiques sont des indices, pas des verdicts.

---

## E01 — `monographie/chapitres/00-cartographier.md`, § « Architecture de l’ouvrage » (ligne 181)

**Avant**

> Le @sec:ch16 passe à l’échelle collective pour montrer comment le recours aux mêmes modèles abaisse le taux d’erreur individuel tout en élevant la probabilité d’échappement par corrélation des angles morts, blanchiment de provenance et assèchement des capacités d’évaluation.

**Après**

> Le @sec:ch16 change d’échelle pour examiner comment l’usage collectif des mêmes modèles abaisse les erreurs individuelles tout en élevant l’échappement par corrélation des angles morts, blanchiment de provenance et saturation des capacités d’évaluation.

**Alertes automatiques :** terme du registre « taux d'erreur » : 1 → 0 ; terme du registre « probabilité d'échappement » : 1 → 0 ; Lecture des probabilités — probable / probabilité : 1 → 0 ; Statut épistémique — montrer : 1 → 0

---

## E02 — `monographie/chapitres/00-cartographier.md`, § « L’informatique classique a gagné ses garanties ; les modèles appris les dépensent » (ligne 99)

**Avant**

> Munis de cette grille de lecture, tournons-nous vers l’informatique.

**Après**

> Munis de cette grille, tournons-nous vers l’informatique.

---

## E03 — `monographie/chapitres/00-cartographier.md`, § « Trois récits pour poser le problème » (ligne 7)

**Avant**

> D’un côté à l’autre de l’interface, les nombres voyageaient nus, sans mention d’unité ; chaque impulsion était ainsi sous-estimée d’un facteur proche de 4,45 [@mco1999].

**Après**

> D’un côté à l’autre de l’interface, les nombres voyageaient nus, sans unité, si bien que chaque impulsion était sous-estimée d’un facteur proche de 4,45 [@mco1999].

---

## E04 — `monographie/chapitres/00-cartographier.md`, § « Cartographier le terrain » (ligne 3)

**Avant**

> Avant d’entrer dans le détail des outils, des arguments et des études de cas, ce chapitre parcourt l’ensemble du trajet à vol d’oiseau.

**Après**

> Ce chapitre parcourt l’ensemble du livre à vol d’oiseau, avant d’entrer dans le détail des outils, des démonstrations et des cas.

**Alertes automatiques :** Statut épistémique — démontrer / prouver : 0 → 1 ; Statut épistémique — argument : 1 → 0

---

## E05 — `monographie/chapitres/00-cartographier.md`, § « La mer ne consulte pas nos probabilités » (ligne 29)

**Avant**

> Que signifie ce 5 % (ou ce 0,1 %) ? Il ne décrit pas une propriété physique de l’océan ni du mât.

**Après**

> Que désigne ce 5 % (ou ce 0,1 %) ? Il ne s’agit ni d’une propriété physique de l’océan ni d’une caractéristique du mât.

---

## E06 — `monographie/chapitres/00-cartographier.md`, § « Architecture de l’ouvrage » (ligne 175)

**Avant**

> Le @sec:ch03 développe la lecture de la probabilité comme jugement pesant des mondes possibles, l’habitude de raisonner à l’envers (chercher quelle variation cachée de l’arrière-plan renverserait la conclusion) et l’impossibilité de juger un prévisionniste sur une seule issue.

**Après**

> Le @sec:ch03 développe la probabilité comme jugement pesant des mondes possibles, l’habitude de raisonner à l’envers et l’impossibilité de juger un prévisionniste sur une issue unique.

**Alertes automatiques :** Quantificateurs absolus — seul(e) / seulement / uniquement : 1 → 0

---

## E07 — `monographie/chapitres/00-cartographier.md`, § « Parcours de lecture » (ligne 206)

**Avant**

> *L’informaticien et le concepteur d’IA* : relie la théorie de la fiabilité et des contrôles croisés au passage des composants spécifiés par contrat aux composants appris, jusqu’aux architectures d’agents, aux bacs à sable et aux verrous.

**Après**

> *L’informaticien et le concepteur d’IA* : relie la théorie des contrôles croisés au passage des composants spécifiés aux composants appris, jusqu’aux architectures d’agents, aux bacs à sable et aux verrous.

**Alertes automatiques :** terme du registre « contrat » : 1 → 0

---

## E08 — `monographie/chapitres/00-cartographier.md`, § « L’informatique classique a gagné ses garanties ; les modèles appris les dépensent » (ligne 109)

**Avant**

> *Ce qui est promis* : on passe d’un contrat vérifiable sur chaque appel à une tendance statistique mesurée en moyenne sur des tests de référence, qui ne garantit aucune réponse particulière.

**Après**

> *Ce qui est promis* : au contrat vérifiable sur chaque appel succède une tendance statistique mesurée en moyenne sur des batteries de tests, sans garantie sur une réponse particulière.

**Alertes automatiques :** terme du registre « test de référence » : 1 → 0 ; Quantificateurs absolus — aucun(e) : 1 → 0 ; Force de l'affirmation — garantir (verbe) : 1 → 0

---

## E09 — `monographie/chapitres/00-cartographier.md`, § « Décider une seule fois face à des enjeux asymétriques » (ligne 53)

**Avant**

> Si la perte en cas de casse vaut vingt-cinq fois le gain d’une victoire, le seuil vaut 1/26, un peu moins de 4 % : M. X, qui évalue le risque à 5 %, choisit rationnellement le voilier renforcé, tandis que M. Y, qui l’évalue à 0,1 %, s’élance non moins rationnellement sur le voilier léger.

**Après**

> Si la casse coûte vingt-cinq fois le gain d’une victoire, le seuil vaut 1/26, soit un peu moins de 4 %. M. X, qui évalue le risque à 5 %, choisit rationnellement le voilier renforcé, tandis que M. Y, à 0,1 %, s’élance non moins rationnellement sur le voilier léger.

---

## E10 — `monographie/chapitres/00-cartographier.md`, § « L’informatique classique a gagné ses garanties ; les modèles appris les dépensent » (ligne 101)

**Avant**

> Une fonction de tri promet que, si on lui fournit une liste d’éléments comparables, elle rendra une permutation ordonnée de cette même liste ; le protocole TCP promet que les octets arriveront dans l’ordre ou qu’une erreur sera signalée.

**Après**

> Une fonction de tri promet de rendre, pour toute liste d’éléments comparables, une permutation ordonnée de cette même liste ; le protocole TCP promet que les octets arriveront dans l’ordre ou qu’une erreur sera signalée.

**Alertes automatiques :** Quantificateurs absolus — tout / tous / toute(s) : 0 → 1

---

## E11 — `monographie/chapitres/00-cartographier.md`, § « Ce que nous pouvons encore faire » (ligne 167)

**Avant**

> mesurer concrètement la probabilité d’échappement du système de relecture en y glissant périodiquement des erreurs injectées

**Après**

> mesurer concrètement l’échappement du système de relecture par des erreurs injectées

**Alertes automatiques :** terme du registre « probabilité d'échappement » : 1 → 0 ; Lecture des probabilités — probable / probabilité : 1 → 0

---

## E12 — `monographie/chapitres/00-cartographier.md`, § « La mer ne consulte pas nos probabilités » (ligne 29)

**Avant**

> Une fois la course terminée, l’issue ne les départagera guère, du moins dans le cas le plus probable.

**Après**

> Une fois la course terminée, l’issue ne les départage guère, du moins dans le cas le plus fréquent.

**Alertes automatiques :** Lecture des probabilités — probable / probabilité : 1 → 0 ; Lecture des probabilités — fréquent / fréquence : 0 → 1

---

## E13 — `monographie/chapitres/00-cartographier.md`, § « Trois récits pour poser le problème » (ligne 19)

**Avant**

> Que s’est-il passé entre la perte de la sonde martienne et ces deux scènes contemporaines ?

**Après**

> Que s’est-il passé entre la perte de la sonde martienne et ces deux épisodes contemporains ?

---

## E14 — `monographie/chapitres/00-cartographier.md`, § « L’énigme arithmétique du producteur plus fiable et du système plus risqué » (ligne 139)

**Avant**

> Puisqu’une affirmation fausse ne cause de dommage que si elle débouche sur une action sans avoir été arrêtée en chemin, le risque résiduel est le produit de deux facteurs : le taux d’erreur du producteur (la proportion d’affirmations fausses qu’il émet) et la probabilité d’échappement (la proportion de ces affirmations fausses qui franchissent les contrôles sans être contredites à temps).

**Après**

> Puisqu’une affirmation fausse ne nuit que si elle atteint l’action sans être arrêtée, le risque résiduel est le produit de deux facteurs : le taux d’erreur du producteur et la probabilité d’échappement des contrôles.

**Alertes automatiques :** terme du registre « affirmation » : 3 → 1

---

## E15 — `monographie/chapitres/00-cartographier.md`, § « L’informatique classique a gagné ses garanties ; les modèles appris les dépensent » (ligne 113)

**Avant**

> En outre, la compétence d’un tel modèle dessine une frontière en dents de scie : remarquable sur une question complexe, il peut échouer sur une variante voisine d’apparence anodine, sans que rien dans le ton de sa réponse ne signale qu’il vient de franchir sa limite.

**Après**

> À cela s’ajoute un profil de compétence en dents de scie : capable sur un problème complexe, le modèle peut échouer sur une variante voisine d’apparence anodine, sans rien laisser paraître dans le ton de sa réponse.

**Alertes automatiques :** terme du registre « frontière en dents de scie » : 1 → 0

---

## E16 — `monographie/chapitres/00-cartographier.md`, § « L’automatisation érode les vérifications humaines » (ligne 131)

**Avant**

> Et même lorsqu’un humain relit le brouillon du modèle, deux pièges referment le contrôle sur lui-même : la consigne soumise par l’utilisateur transmet déjà son propre cadre à la machine, et l’entraînement des modèles à plaire à leur interlocuteur les pousse à la complaisance plutôt qu’à la contradiction.

**Après**

> Et même lorsqu’un humain relit la sortie du modèle, deux pièges referment le contrôle sur lui-même : la consigne transmise à la machine lui cède déjà le cadre du problème, et l’entraînement des modèles à satisfaire l’interlocuteur favorise la complaisance plutôt que la contradiction.

---

## E17 — `monographie/chapitres/00-cartographier.md`, § « L’énigme arithmétique du producteur plus fiable et du système plus risqué » (ligne 141)

**Avant**

> Comparons deux organisations imaginaires, avec des chiffres choisis pour l’illustration :

**Après**

> Comparons deux organisations fictives, avec des chiffres choisis pour l’illustration :

---

## E18 — `monographie/chapitres/00-cartographier.md`, § « Toute règle cache un arrière-plan ouvert » (ligne 43)

**Avant**

> La dinde inductiviste qui note chaque matin l’heure à laquelle le fermier lui apporte son grain dispose, à la veille de Noël, d’une série statistique irréprochable ; la catastrophe qui l’attend ne vient pas d’une faute de calcul, mais d’une variable qui n’a jamais figuré dans son cadre.

**Après**

> La dinde inductiviste qui note chaque matin l’heure à laquelle le fermier lui apporte son grain dispose, à la veille de Noël, d’une série statistique irréprochable. La catastrophe qui l’attend ne vient pas d’une faute de calcul, mais d’une variable absente de son cadre.

**Alertes automatiques :** Quantificateurs absolus — jamais : 1 → 0

---

## E19 — `monographie/chapitres/00-cartographier.md`, § « Toute règle cache un arrière-plan ouvert » (ligne 35)

**Avant**

> Un collègue tente pourtant l’expérience le lendemain, chauffe son récipient à 101 °C et constate que rien ne bout : il a utilisé une eau fortement salée.

**Après**

> Le lendemain, un collègue chauffe son récipient à 101 °C sans voir d’ébullition : il a utilisé une eau fortement salée.

**Alertes automatiques :** Quantificateurs absolus — rien : 1 → 0

---

## E20 — `monographie/chapitres/00-cartographier.md`, § « Ce que nous pouvons encore faire » (ligne 152)

**Avant**

> Deux instruments prennent alors le relais : ajouter délibérément à son estimation du risque une marge d’humilité pour tenir compte de ce que la représentation pourrait omettre — marge qui relève d’un jugement de prudence et non d’une mesure —, et placer devant l’action un verrou, c’est-à-dire un point où elle attend une autorisation, accordée seulement après un contrôle indépendant.

**Après**

> Deux garde-fous prennent alors le relais : ajouter délibérément à son estimation du risque une marge d’humilité (jugement de prudence et non mesure) pour tenir compte de ce que la représentation peut omettre, et placer devant l’action un verrou où elle attend une autorisation après contrôle indépendant.

**Alertes automatiques :** Quantificateurs absolus — seul(e) / seulement / uniquement : 1 → 0

---

## E21 — `monographie/chapitres/00-avant-propos.md`, § « Pourquoi ce livre » (ligne 5)

**Avant**

> Cette représentation assemble des mesures, découpe la réalité en catégories, retient certaines variables, en écarte une infinité d’autres, relie le tout par des règles logiques, des équations ou des distributions de probabilité, puis livre une conclusion ou un chiffre.

**Après**

> Cette représentation assemble des mesures, découpe la réalité en catégories, retient certaines variables en écartant une foule d’autres, puis relie le tout par des règles logiques, des équations ou des distributions de probabilité.

---

## E22 — `monographie/chapitres/00-cartographier.md`, § « Cartographier le terrain » (ligne 3)

**Avant**

> Il pose en langage courant le problème directeur du livre, fait apparaître par le récit les notions qui reviendront de chapitre en chapitre, et montre comment une réflexion générale sur la décision et sur les contrôles éclaire le passage de l’informatique classique à l’intelligence artificielle et à l’automatisation.

**Après**

> Il pose en langage courant la question directrice de l’ouvrage, fait surgir par le récit les notions qui reviendront d’un chapitre à l’autre, et montre comment une théorie générale de la décision et des contrôles éclaire le passage de l’informatique classique à l’intelligence artificielle et à l’automatisation.

**Alertes automatiques :** Statut épistémique — théorie / théorème : 0 → 1

---

## E23 — `monographie/chapitres/00-cartographier.md`, § « Décider une seule fois face à des enjeux asymétriques » (ligne 47)

**Avant**

> Le passage critique a lieu lorsque nous décidons d’agir d’après ce que nous croyons.

**Après**

> Le passage critique a lieu quand nous décidons d’agir d’après ce que nous croyons.

---

## E24 — `monographie/chapitres/00-avant-propos.md`, § « À qui s’adresse cet ouvrage » (ligne 23)

**Avant**

> Le propos touche toutefois des pratiques dont les préoccupations et les défenses naturelles diffèrent sensiblement : l’ingénieur qui chaîne des simulations multiphysiques, le statisticien ou le mathématicien attentif aux hypothèses de ses théorèmes, le concepteur de systèmes d’intelligence artificielle confronté aux frontières irrégulières de ses modèles, le décideur ou le responsable d’institution chargé d’organiser les revues, ou encore le destinataire non spécialiste à qui l’on remet un chiffre assuré pour trancher une décision.

**Après**

> Le propos touche toutefois des métiers dont les contraintes et les défenses naturelles diffèrent sensiblement. Il concerne autant l’ingénieur qui chaîne des simulations multiphysiques que le statisticien attentif aux hypothèses de ses théorèmes, le concepteur de systèmes d’intelligence artificielle confronté aux frontières irrégulières de ses modèles, le responsable d’institution chargé d’organiser les revues, ou encore le destinataire non spécialiste à qui l’on remet un chiffre assuré pour trancher.

---

## E25 — `monographie/chapitres/00-cartographier.md`, § « Chaînes en série et contrôles croisés en parallèle » (ligne 95)

**Avant**

> Sous réserve que la comparaison soit fidèle et que les désaccords soient instruits, une erreur ne passe au travers que si elle échappe à la fois au producteur et au contrôleur : l’angle mort résiduel se réduit à l’intersection de leurs angles morts respectifs.

**Après**

> Sous réserve que la comparaison soit fidèle et les désaccords instruits, une erreur ne passe que si elle échappe aux deux voies : l’angle mort résiduel se réduit à l’intersection de leurs angles morts.

**Alertes automatiques :** terme du registre « producteur » : 1 → 0 ; terme du registre « contrôleur » : 1 → 0

---

## E26 — `monographie/chapitres/00-cartographier.md`, § « Pourquoi l’auto-vérification bute sur le cadre » (ligne 85)

**Avant**

> Encore faut-il que le facteur omis ait effectivement varié pendant la collecte des données, et que ses effets se lisent dans ce que l’on a pris soin d’enregistrer : un essai de charge sur une ferrure neuve dans l’air sec d’un laboratoire ne révélera jamais l’effet de cinq ans de brouillard salin, et un modèle statistique validé tant qu’un facteur caché restait constant peut être pris en défaut dès que ce facteur change en exploitation. On parlera alors de dérive de distribution.

**Après**

> Encore faut-il que le facteur omis ait varié pendant la collecte des données et que ses effets apparaissent dans ce qui a été enregistré. Un essai de charge sur une ferrure neuve en laboratoire sec ne révélera pas cinq ans de brouillard salin, et un modèle validé tant qu’un facteur caché demeurait stable cédera dès que ce facteur bougera en exploitation : on parlera de dérive de distribution.

**Alertes automatiques :** Modaux et atténuateurs — pouvoir (peut, pourrait…) : 1 → 0 ; Quantificateurs absolus — jamais : 1 → 0

---

## E27 — `monographie/chapitres/00-cartographier.md`, § « Trois récits pour poser le problème » (ligne 7)

**Avant**

> Or la spécification d’interface exigeait que ces impulsions soient exprimées dans l’unité du Système international, le newton-seconde, tandis que le programme les écrivait en livres-force-secondes, une unité anglo-saxonne.

**Après**

> La spécification d’interface exigeait des newton-secondes, l’unité du Système international ; le programme écrivait des livres-force-secondes, une unité anglo-saxonne.

---

## E28 — `monographie/chapitres/00-cartographier.md`, § « Trois récits pour poser le problème » (ligne 7)

**Avant**

> La commission d’enquête n’eut aucun mal à désigner la cause technique immédiate de la perte.

**Après**

> La commission d’enquête identifia rapidement la cause technique immédiate de la perte.

**Alertes automatiques :** Quantificateurs absolus — aucun(e) : 1 → 0

---

## E29 — `monographie/chapitres/00-cartographier.md`, § « Pourquoi l’auto-vérification bute sur le cadre » (ligne 83)

**Avant**

> Mais vis-à-vis de tout facteur omis par le cadre — la corrosion de la ferrure —, ces contrôles internes sont des copies les uns des autres : ils puisent tous à la même source et s’accorderont jusqu’à la troisième décimale tout en se trompant ensemble.

**Après**

> Mais devant un facteur omis par le cadre, ces contrôles internes se copient l’un l’autre : ils puisent à la même source et s’accordent jusqu’à la troisième décimale tout en se trompant ensemble.

**Alertes automatiques :** Quantificateurs absolus — tout / tous / toute(s) : 2 → 1

---

## E30 — `monographie/chapitres/00-cartographier.md`, § « La mer ne consulte pas nos probabilités » (ligne 29)

**Avant**

> Pour savoir si une prévision de « 70 % de chances de pluie » mesure bien l’incertitude, il faut relever la longue série des jours où elle a été émise et vérifier s’il a plu environ sept fois sur dix.

**Après**

> Pour savoir si une annonce de « 70 % de chances de pluie » mesure fidèlement l’incertitude, il faut relever une longue série de jours comparables et vérifier s’il a plu environ sept fois sur dix.

---

## E31 — `monographie/chapitres/00-cartographier.md`, § « Ce que nous pouvons encore faire » (ligne 167)

**Avant**

> traiter la capacité d’évaluation indépendante comme une ligne budgétaire à part et ne pas produire plus que ce qu’elle permet de vérifier

**Après**

> traiter la capacité d’évaluation indépendante comme une ressource budgétée et plafonner la production à ce qu’elle permet de vérifier

---

## E32 — `monographie/chapitres/00-avant-propos.md`, § « Une démarche de travail, non une prescription » (ligne 13)

**Avant**

> Prétendre fournir une méta-procédure formelle garantissant la justesse de nos cadres de pensée contredirait d’ailleurs l’un des arguments centraux du livre, développé au @sec:ch07 : toute procédure chargée d’auditer un cadre repose elle-même sur une spécification finie, et ne fait que reporter le problème un cran plus haut.

**Après**

> Fournir une méta-procédure formelle garantissant la justesse de nos cadres de pensée contredirait d’ailleurs l’un des résultats centraux du livre, établi au @sec:ch07 : toute procédure chargée d’auditer un cadre repose elle-même sur une spécification finie, et ne fait que reporter la difficulté un cran plus haut.

**Alertes automatiques :** Statut épistémique — établir : 0 → 1 ; Statut épistémique — argument : 1 → 0 ; Statut épistémique — résultat : 0 → 1

---

## E33 — `monographie/chapitres/00-cartographier.md`, § « Architecture de l’ouvrage » (ligne 179)

**Avant**

> Le @sec:ch11 montre ce qui change lorsque la spécification passe dans les données pour former un composant appris : le gain de portée s’achète au prix de la garantie et de la lisibilité, la plausibilité, et non la vérité, devient l’objectif d’optimisation, et orienter un modèle ne revient jamais à le spécifier.

**Après**

> Le @sec:ch11 suit le passage de la spécification dans les données pour former un composant appris : la portée s’achète au prix de la garantie et de la lisibilité, la plausibilité remplace la vérité comme objectif d’optimisation, et orienter un modèle ne revient jamais à le spécifier.

**Alertes automatiques :** Statut épistémique — montrer : 1 → 0

---

## E34 — `monographie/chapitres/00-cartographier.md`, § « Ce que nous pouvons encore faire » (ligne 167)

**Avant**

> exiger que toute affirmation soumise à la décision affiche son état de vérification (exploratoire ou établie, ce qui a été contrôlé de façon indépendante) et ses hypothèses principales

**Après**

> exiger que toute affirmation soumise à décision affiche son état de vérification et ses hypothèses

**Alertes automatiques :** Statut épistémique — établir : 1 → 0

---

## E35 — `monographie/chapitres/00-cartographier.md`, § « Ce que nous pouvons encore faire » (ligne 156)

**Avant**

> Quant au décideur, au citoyen ou au responsable à qui l’on remet un chiffre assuré sans ses conditions d’obtention — ce qui revient à lui transférer une responsabilité déguisée en information —, il dispose de quatre questions simples qui n’exigent aucune technicité mathématique pour rouvrir le cadre :

**Après**

> Quant au décideur, au citoyen ou au responsable à qui l’on remet un chiffre assuré sans ses conditions d’obtention — transfert de responsabilité déguisé en information —, quatre questions simples suffisent, sans technicité mathématique, pour rouvrir le cadre :

**Alertes automatiques :** Quantificateurs absolus — aucun(e) : 1 → 0 ; Force de l'affirmation — suffire : 0 → 1

---

## E36 — `monographie/chapitres/00-avant-propos.md`, § « Genèse et responsabilité » (ligne 31)

**Avant**

> Il serait tout aussi inexact d’effacer le rôle déterminant de la direction et du filtrage humains dans ce processus hybride.

**Après**

> Pour autant, la conduite et le filtrage du travail sont restés humains d’un bout à l’autre.

**Alertes automatiques :** Quantificateurs absolus — tout / tous / toute(s) : 1 → 0 ; Quantificateurs absolus — d'un bout à l'autre : 0 → 1

---

## E37 — `monographie/chapitres/00-cartographier.md`, § « Trois récits pour poser le problème » (ligne 7)

**Avant**

> L’enquête mit au jour bien des défaillances humaines et organisationnelles (équipes surchargées, doutes sur la trajectoire restés sans suite, absence de recalcul indépendant), mais sous ces facteurs se trouvait un point précis que l’on pouvait montrer du doigt : un fichier de code, et la spécification écrite qu’il enfreignait.

**Après**

> L’enquête révéla bien d’autres défaillances humaines et organisationnelles — équipes surchargées, alertes sur la trajectoire restées sans suite, absence de recalcul indépendant. Sous ces facteurs se trouvait pourtant un point précis que l’on pouvait désigner du doigt : un fichier de code, et la spécification écrite qu’il enfreignait.

**Alertes automatiques :** Statut épistémique — montrer : 1 → 0

---

## E38 — `monographie/chapitres/00-cartographier.md`, § « Parcours de lecture » (ligne 207)

**Avant**

> *Le décideur et l’institution* : se concentre sur l’évaluation des enjeux, la gestion des fausses alertes, l’érosion des relectures humaines, les angles morts collectifs et la gouvernance organisationnelle de la vérification.

**Après**

> *Le décideur et l’institution* : se concentre sur l’évaluation des enjeux, la gestion des fausses alertes, l’érosion des relectures humaines, les angles morts collectifs et le gouvernement de la vérification.

