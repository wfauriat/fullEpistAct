# Dossier du juge — lot d’étalonnage

- Chapitres d’origine : `monographie/chapitres/00-avant-propos.md` et `monographie/chapitres/00-cartographier.md` (non modifiés ; les numéros de ligne renvoient à ces fichiers ; les lire pour le contexte).
- Retouches soumises : **12**, issues de plusieurs passes de réécriture, présentées dans le désordre.
- Consignes : `.claude/agents/juge-style.md`. Sortie attendue : `style/lots/_etalonnage2/verdicts.json`.
- Les alertes automatiques sont des indices, pas des verdicts.

---

## E01 — `monographie/chapitres/00-cartographier.md`, § « Trois récits pour poser le problème » (ligne 7)

**Avant**

> L’enquête mit au jour bien des défaillances humaines et organisationnelles (équipes surchargées, doutes sur la trajectoire restés sans suite, absence de recalcul indépendant), mais sous ces facteurs se trouvait un point précis que l’on pouvait montrer du doigt : un fichier de code, et la spécification écrite qu’il enfreignait.

**Après**

> L’enquête révéla bien d’autres défaillances humaines et organisationnelles — équipes surchargées, alertes sur la trajectoire restées sans suite, absence de recalcul indépendant. Sous ces facteurs se trouvait pourtant un point précis que l’on pouvait désigner du doigt : un fichier de code, et la spécification écrite qu’il enfreignait.

**Alertes automatiques :** Statut épistémique — montrer : 1 → 0

---

## E02 — `monographie/chapitres/00-cartographier.md`, § « Décider une seule fois face à des enjeux asymétriques » (ligne 55)

**Avant**

> Or c’est là tout le nœud d’une décision unique, prise une seule fois et dont la réponse ne vient qu’après l’acte : le décideur compare au seuil la probabilité issue de sa propre représentation, tandis que le monde ne consulte pas ce chiffre.

**Après**

> C’est là tout le nœud d’une décision unique, prise une seule fois et dont la réponse ne vient qu’après l’acte. Le décideur compare au seuil la probabilité issue de sa propre représentation, tandis que le monde ne consulte pas ce chiffre.

---

## E03 — `monographie/chapitres/00-cartographier.md`, § « La mer ne consulte pas nos probabilités » (ligne 29)

**Avant**

> Une fois la course terminée, l’issue ne les départagera guère, du moins dans le cas le plus probable.

**Après**

> Une fois la course terminée, l’issue ne les départage guère, du moins dans le cas le plus fréquent.

**Alertes automatiques :** Lecture des probabilités — probable / probabilité : 1 → 0 ; Lecture des probabilités — fréquent / fréquence : 0 → 1

---

## E04 — `monographie/chapitres/00-cartographier.md`, § « Chaînes en série et contrôles croisés en parallèle » (ligne 93)

**Avant**

> Ce passage en série est d’autant plus redoutable qu’il s’accompagne souvent d’un blanchiment des conditions : un champ de températures calculé sous dix hypothèses prudentes traverse une interface sous la forme d’un simple tableau de nombres nus, dépouillé de ses réserves, de ses barres d’erreur et parfois de ses unités, comme l’étaient les impulsions transmises à l’équipe de navigation de *Mars Climate Orbiter* [@mco1999].

**Après**

> Ce passage en série est d’autant plus redoutable qu’il s’accompagne souvent d’un blanchiment des conditions. Ainsi, un champ de températures calculé sous dix hypothèses prudentes traverse une interface sous la forme d’un simple tableau de nombres nus, dépouillé de ses réserves, de ses barres d’erreur et parfois de ses unités, comme l’étaient les impulsions transmises à l’équipe de navigation de *Mars Climate Orbiter* [@mco1999].

---

## E05 — `monographie/chapitres/00-avant-propos.md`, § « Pourquoi ce livre » (ligne 7)

**Avant**

> Ce livre a une visée d’abord pratique : chercher comment agir au mieux sur le monde à travers une représentation finie, et comment bâtir des représentations et des procédures capables d’être démenties à temps lorsque nous nous trompons.

**Après**

> Ce livre a une visée d’abord pratique. Il cherche comment agir au mieux sur le monde à travers une représentation finie, et comment bâtir des représentations et des procédures capables d’être démenties à temps lorsque nous nous trompons.

---

## E06 — `monographie/chapitres/00-cartographier.md`, § « Pourquoi l’auto-vérification bute sur le cadre » (ligne 83)

**Avant**

> Mais vis-à-vis de tout facteur omis par le cadre — la corrosion de la ferrure —, ces contrôles internes sont des copies les uns des autres : ils puisent tous à la même source et s’accorderont jusqu’à la troisième décimale tout en se trompant ensemble.

**Après**

> Mais vis-à-vis de tout facteur omis par le cadre — la corrosion de la ferrure —, ces contrôles internes sont des copies les uns des autres. Ils puisent tous à la même source et s’accorderont jusqu’à la troisième décimale tout en se trompant ensemble.

---

## E07 — `monographie/chapitres/00-cartographier.md`, § « Pourquoi l’auto-vérification bute sur le cadre » (ligne 85)

**Avant**

> Encore faut-il que le facteur omis ait effectivement varié pendant la collecte des données, et que ses effets se lisent dans ce que l’on a pris soin d’enregistrer : un essai de charge sur une ferrure neuve dans l’air sec d’un laboratoire ne révélera jamais l’effet de cinq ans de brouillard salin, et un modèle statistique validé tant qu’un facteur caché restait constant peut être pris en défaut dès que ce facteur change en exploitation. On parlera alors de dérive de distribution.

**Après**

> Encore faut-il que le facteur omis ait varié pendant la collecte des données et que ses effets apparaissent dans ce qui a été enregistré. Un essai de charge sur une ferrure neuve en laboratoire sec ne révélera pas cinq ans de brouillard salin, et un modèle validé tant qu’un facteur caché demeurait stable cédera dès que ce facteur bougera en exploitation : on parlera de dérive de distribution.

**Alertes automatiques :** Modaux et atténuateurs — pouvoir (peut, pourrait…) : 1 → 0 ; Quantificateurs absolus — jamais : 1 → 0

---

## E08 — `monographie/chapitres/00-cartographier.md`, § « L’informatique classique a gagné ses garanties ; les modèles appris les dépensent » (ligne 113)

**Avant**

> En outre, la compétence d’un tel modèle dessine une frontière en dents de scie : remarquable sur une question complexe, il peut échouer sur une variante voisine d’apparence anodine, sans que rien dans le ton de sa réponse ne signale qu’il vient de franchir sa limite.

**Après**

> À cela s’ajoute un profil de compétence en dents de scie : capable sur un problème complexe, le modèle peut échouer sur une variante voisine d’apparence anodine, sans rien laisser paraître dans le ton de sa réponse.

**Alertes automatiques :** terme du registre « frontière en dents de scie » : 1 → 0

---

## E09 — `monographie/chapitres/00-cartographier.md`, § « L’automatisation corrèle les angles morts à l’échelle collective » (ligne 135)

**Avant**

> Mais pour les erreurs qui relèvent de l’angle mort du modèle lui-même, le producteur qui rédige avec l’aide du modèle et le contrôleur qui relit avec l’aide du même modèle puisent désormais à la même source : leur contrôle croisé dégénère en copie, et la probabilité d’échappement de ces erreurs partagées bondit.

**Après**

> Mais pour les erreurs qui relèvent de l’angle mort du modèle lui-même, le producteur qui rédige avec l’aide du modèle et le contrôleur qui relit avec l’aide du même modèle puisent désormais à la même source. Leur contrôle croisé dégénère alors en copie, et la probabilité d’échappement de ces erreurs partagées bondit.

---

## E10 — `monographie/chapitres/00-avant-propos.md`, § « Pourquoi ce livre » (ligne 5)

**Avant**

> Or le monde ne répond pas à notre représentation ; il répond à notre action.

**Après**

> Le monde, pourtant, ne répond pas à notre représentation ; il répond à notre action.

---

## E11 — `monographie/chapitres/00-cartographier.md`, § « L’automatisation érode les vérifications humaines » (ligne 125)

**Avant**

> Personne n’avait jamais inscrit cette boucle de rétroaction sur les organigrammes ; aussi sa disparition, lorsqu’une réponse complète jaillit en quelques secondes d’une consigne, passe-t-elle inaperçue jusqu’au jour où une énormité traverse tout le processus.

**Après**

> Personne n’avait jamais inscrit cette boucle de rétroaction sur les organigrammes. Aussi sa disparition, lorsqu’une réponse complète jaillit en quelques secondes d’une consigne, passe-t-elle inaperçue jusqu’au jour où une énormité traverse tout le processus.

---

## E12 — `monographie/chapitres/00-cartographier.md`, § « L’informatique classique a gagné ses garanties ; les modèles appris les dépensent » (ligne 105)

**Avant**

> Dans cette opération, la garantie préalable n’a pas été perdue par négligence ; elle a été délibérément *dépensée* pour acheter une portée nouvelle, précisément sur les tâches rebelles à toute règle explicite.

**Après**

> Dans cette opération, la garantie préalable n’a pas été perdue par négligence. Elle a été délibérément dépensée pour acheter une portée nouvelle, précisément sur les tâches rebelles à toute règle explicite.

