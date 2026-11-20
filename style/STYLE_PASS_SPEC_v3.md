# Spécification v3 — Passe de style automatisée (retenue)

**Objet :** rendre la prose d’*Agir d’après une représentation du monde* (`monographie/chapitres/*.md`) plus lisible, plus rythmée et plus idiomatiquement française, sans changer ce qu’elle dit.

**Statut :** v3 du 2026-11-20, retenue par l’auteur. Elle remplace :
- `STYLE_PASS_SPEC.md` (v1 et amendements), conservée comme trace ;
- `STYLE_PASS_SPEC_v2.md` (variante stricte avec décisions de l’auteur), non retenue.

Le fonctionnement pratique (fichiers, états, commandes) est décrit dans `style/PROTOCOLE.md`.

---

## 1. Principe

1. **Le rédacteur** (une instance Gemini) propose des **retouches** : chacune remplace un passage exact du chapitre par une nouvelle version. Il ne produit jamais un chapitre réécrit.
2. **Des contrôles mécaniques** écartent les retouches qui touchent à ce qui ne doit jamais changer (§4).
3. **Le juge** (un agent Claude Opus, neuf à chaque chapitre, d’une autre famille que le rédacteur) accepte ou rejette chaque retouche restante, sur le sens, la portée, la ligne argumentative et le registre (§5).
4. **Un script** applique les retouches acceptées. Une retouche rejetée laisse le texte d’origine en place.
5. **Un commit par chapitre** sur la branche `style-pass`. L’auteur reste hors de la boucle jusqu’à sa relecture intégrale du livre.

Chaque chapitre laisse dans `style/lots/<chapitre>/` un **journal** pour cette relecture :
- les retouches appliquées (avant et après) ;
- les retouches rejetées, avec la raison du juge ;
- un rapport des changements les plus sensibles (`rapport_portee.md`).

**Ce que vise la passe :** une lecture plus aisée, pas une transformation. La voix, l’argument et la prudence du texte restent ceux de l’auteur.

---

## 2. Objectifs de style (une orientation, pas une porte)

**À corriger :**
- phrases-tunnels de 35 à 50 mots, surtout en série ;
- deux-points aphoristiques en série et « Or » en tête de phrase ;
- italiques d’emphase ;
- antithèses symétriques qui ne portent rien (« X, non Y » en fin de paragraphe, à répétition) ;
- chapeaux qui paraphrasent la table des matières du chapitre ;
- ponts d’annonce redondants (« ce sera l’objet du @sec:… ») ;
- sujets nominaux abstraits (« La disparition du frottement produit un second effet… ») ;
- formules diplomatiques creuses (« Il serait erroné de voir… ») ;
- calques de l’anglais ;
- paragraphes tous calibrés sur le même gabarit.

**Gradient de ton :**
- avant-propos, chapitre 0 et conclusion : clair, direct, posé ;
- chapitres 1 à 9 : sobre et fluide, les exemples portent les distinctions ;
- chapitres 10 à 18 : fermeté analytique, accent sur les mécanismes réutilisables.

**Repères chiffrés,** mesurés par `style/audit_style.py` : à titre indicatif seulement. Aucun chapitre n’est bloqué sur ces chiffres.

| Indicateur | Avant passe | Direction |
| :--- | :--- | :--- |
| Longueur moyenne des phrases | 27 mots (29 à 32 aux ch. 0 et 13–16) | vers 22 à 25 mots |
| Phrases ≥ 35 mots | jusqu’à 37 % | nettement moins |
| Phrases ≤ 10 mots | 9 % | un peu plus |
| Taille des paragraphes | gabarit uniforme | plus variée |

Ne pas descendre sous ~20 mots de moyenne : en deçà, la prose devient hachée.

---

## 3. Règle de retenue

C’est la règle la plus importante. Le premier pilote a réécrit 82 % des phrases, y compris des phrases courtes qu’aucun objectif ne visait, et a ainsi changé le sens d’une vingtaine de passages sur un seul chapitre.

- **Ne retoucher que ce qui gagne nettement.** Une phrase qui fonctionne reste telle quelle.
- **Pas d’échange de synonymes**, pas de « reformulation plus élégante » sans défaut à corriger. Le juge rejette toute retouche sans gain net.
- **Ne jamais retoucher le contenu :** un exemple, un fait, un chiffre, un acteur, une date, ce que dit une source.
- **Retouches petites et autonomes :** idéalement une à trois phrases, jamais plus d’un paragraphe. Chaque retouche doit pouvoir être acceptée ou rejetée seule. Deux retouches ne se chevauchent pas.
- **Termes du registre** (`monographie/commun/registre_termes.md`) : les garder exacts, même répétés. Un pronom ne remplace un terme que s’il n’y a aucune ambiguïté.
- **Conserver la prudence** : modaux, quantificateurs, conditions et restrictions (*peut, tend à, souvent, tout, aucun, seulement, si, tant que, ne… que*) restent présents et portent sur le même segment. Couper une phrase ne doit jamais rendre inconditionnel ce qui était conditionnel.

`style/DERIVES_A_EVITER.md` donne les dérives relevées sur le premier pilote, à éviter.

---

## 4. Ce qui ne change jamais (contrôlé automatiquement)

Une retouche qui enfreint l’un de ces points est rejetée sans passer au juge (`style/appliquer_edits.py verifier`).

- Le passage `avant` apparaît **exactement une fois** dans le chapitre. Il faut le copier à l’identique, apostrophes typographiques ’ comprises.
- Il couvre **au plus un paragraphe** et se trouve entièrement dans de la prose modifiable (§6).
- Restent identiques entre avant et après :
  - renvois (`@sec:`, `@prop:`, `@def:`, `@eq:`, `@fig:`, `@tbl:`, y compris la forme `[-@…]`) ;
  - clés de citation (`[@…]`) ;
  - identifiants `{#…}` ;
  - mises en **gras** ;
  - formules en ligne `$…$` ;
  - code en ligne ;
  - appels de note ;
  - nombres.
- L’après n’introduit ni titre, ni balise de bloc `:::`, ni tableau, ni figure, ni formule centrée.

---

## 5. Ce que le juge vérifie

Le juge accepte une retouche seulement si :

1. **sens** — elle dit la même chose, ni plus ni moins, sans présupposé ajouté ;
2. **portée** — modaux, quantificateurs, négations, conditions et restrictions sont intacts et portent sur le même segment ;
3. **statut** — rien n’est promu ni rétrogradé (hypothèse, résultat, argument, preuve, réflexion, théorie) ;
4. **probabilités** — jugement et fréquence restent distincts, ainsi que les séries de référence ;
5. **terme** — aucun terme du registre n’est remplacé, aucune définition ni glose n’est retirée ;
6. **fait** — aucun détail factuel n’est ajouté, durci, adouci ou retiré ;
7. **argument** — la phrase garde son rôle, ses liens logiques, ses renvois aux exemples courants, tous les éléments de ses énumérations, et nomme le même mécanisme ;
8. **registre** — le ton reste sobre (§7) ;
9. **français** — la phrase est correcte et idiomatique ;
10. **gain** — la lecture s’améliore nettement.

En cas de doute, il rejette. Ses consignes complètes sont dans `.claude/agents/juge-style.md`.

---

## 6. Zones hors passe

**Ne pas proposer de retouche dans :**
- les titres ;
- les balises de bloc `:::` et le contenu des blocs `.formel`, `.outils`, `.proposition`, `.definition` et `.exemple-quantitatif` ;
- les tableaux et leurs légendes ;
- les figures ;
- les formules centrées ;
- les commentaires.

**Sections verrouillées,** réservées à l’auteur (rejet automatique) :
- « Genèse et responsabilité » (`sec:avant-propos-genese`) ;
- « Une provenance déclarée » (`sec:conclusion-provenance`).

**Restent dans la passe :**
- le texte des encadrés `.cas`, `.nuance` et `.question` ;
- les listes ;
- les « Points clés ».

---

## 7. Registre (profil « Option A »)

- **Sobre et académique.** Pas de ton péremptoire, pas de formule-choc, pas d’adresse familière au lecteur, pas de prédiction.
- **Aucune importation du livre de 2022 :** pas de fiction ni de dialogue, pas de guillemets distanciateurs, pas de « je ».
- **La brièveté sert la respiration et la clarté des mécanismes,** jamais la formule tranchante qui ferme une porte sans justification.
- **Articulations françaises explicites** (*car, puisque, si bien que, encore faut-il que, reste que, de même*) plutôt que les deux-points et la parataxe calqués sur l’anglais. Un deux-points qui introduit une liste ou une définition reste.

---

## 8. Retouches particulières permises

- **Chapeau d’ouverture :** une accroche de 2 ou 3 phrases qui pose le problème du chapitre, au lieu de la liste de son contenu. Les notions préalables nommées avec leur renvoi restent présentes. Une seule retouche par chapitre.
- **Antithèses :** au plus deux antithèses symétriques par section. Les autres deviennent des assertions simples ou causales, sans rien perdre de leur contenu.
- **Formules diplomatiques :** une formule creuse peut céder la place à une position nette. Jamais une réserve épistémique réelle, c’est-à-dire tout ce qui porte un statut, une condition ou une limite.
- **Récits répétés :** un récit déjà fait ailleurs peut être ramené à un rappel d’une ou deux phrases avec renvoi, selon la table ci-dessous. Les exemples courants (voiliers, eau bouillante, ferrure, dinde, Challenger, pluie à 70 %) reviennent par construction : seules les re-narrations sont visées.

| Récit | Récit complet | Ailleurs |
| :--- | :--- | :--- |
| *Mars Climate Orbiter* | ch. 0 (récit), ch. 10 (analyse) | rappel bref avec renvoi |
| *Mata v. Avianca* | ch. 0 (récit), ch. 11 (analyse) | rappel bref au ch. 13 |
| METR (2025) | encadré du ch. 15 | une phrase et un renvoi au ch. 0 |

Un rappel retire du texte, mais ne doit retirer ni une citation (§4) ni un élément sur lequel l’argument local s’appuie.

---

## 9. Motifs

Chaque retouche déclare un motif :

| Motif | Défaut corrigé |
| :--- | :--- |
| `phrase-longue` | phrase trop longue |
| `rythme` | rythme du passage |
| `paragraphe` | découpage des paragraphes |
| `deux-points` | deux-points en série |
| `or-initial` | « Or » en tête de phrase |
| `italique` | italique d’emphase |
| `antithese` | antithèse symétrique |
| `chapeau` | chapeau d’ouverture |
| `recit-repete` | récit déjà fait ailleurs |
| `formule-creuse` | formule diplomatique creuse |
| `sujet-abstrait` | sujet nominal abstrait |
| `calque` | calque de l’anglais |
| `pont-redondant` | pont d’annonce redondant |
| `autre` | autre défaut (à expliquer dans la note) |

Le motif et la note éventuelle ne sont pas montrés au juge, qui juge le texte seul. Ils figurent dans le journal.

---

## 10. Étalonnage du juge

Avant la production, le juge est testé une fois sur un lot d’étalonnage :
- les dérives réelles du premier pilote ;
- des retouches fidèles tirées du même pilote.

Voir `style/etalonnage/`. Le résultat est dans `style/etalonnage/BILAN.md` : 30 dérives sur 30 rejetées, et 7 retouches strictement fidèles sur 8 acceptées.

**Conséquences pour le rédacteur :**
- préférer les coupes articulées (« alors », « ainsi », « car », « de même ») aux simples juxtapositions ;
- ne jamais retirer un connecteur logique (« pourtant », « tandis que ») ni un mot de portée (« jamais », « effectivement ») ;
- éviter les échanges de synonymes : le juge les rejette.
