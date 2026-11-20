---
marp: true
theme: monographie
paginate: true
math: mathjax
title: Agir d’après une représentation du monde — Synthèse (35 min)
footer: Agir d’après une représentation du monde · Synthèse (35 min)
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="eyebrow">Conférence de synthèse · 35 minutes</div>

# Agir d’après une représentation du monde

<div class="subtitle">Ce qui peut encore nous détromper à temps — de l’ingénierie classique aux systèmes d’IA</div>

<div class="meta">

D’après la monographie *Agir d’après une représentation du monde* (18 chapitres · 5 propositions · 3 modèles formels)
**Fil directeur :** forger les clés (théorie générale des contrôles) avant d’aborder les serrures (IA et automatisation)

</div>

<!--
Minutage indicatif : 1 min (total 1/35).
Posez le cadre de l’exposé : nous n’allons pas parler d’IA pendant les quinze premières minutes, à dessein.
Si l’on commence par les LLM et les agents, on prend pour des bizarreries de l’IA des lois générales qui gouvernent toute représentation finie.
-->

---

<div class="eyebrow">Ouverture · Chapitre 0</div>

# Trois récits pour poser le problème

<div class="cols-3">

<div class="card blue">

<div class="card-title">1. Mars Climate Orbiter (1999)</div>

`SM_FORCES` envoie des livres-force-secondes sans unité là où l’interface attend des newton-secondes (facteur 4,45).

**Trace :** une règle écrite a été enfreinte — la défaillance a une *adresse*.

</div>

<div class="card orange">

<div class="card-title">2. Mata v. Avianca (2023)</div>

Six arrêts de justice inventés de toutes pièces dans un mémoire rédigé avec un modèle de langage.

**Trace :** prose fluide, assurée — *aucun contrat écrit violé*.

</div>

<div class="card aqua">

<div class="card-title">3. Essai METR (2025)</div>

Développeurs expérimentés sur leurs propres dépôts avec assistance IA.

**Mesuré :** +19 % de temps.
**Ressenti :** −20 % (inversion de signe).

</div>

</div>

<div class="card" style="margin-top: 14px;">

**Question directrice :** quand nous agissons à travers des modèles, du code et des chaînes automatisées, *qu’est-ce qui peut encore nous avertir à temps que nous faisons fausse route ?*

</div>

<!--
Minutage : 2,5 min (total 3,5/35).
Soulignez la progression entre les trois scènes :
1) échec d’interface silencieusement propagé, mais localisable après coup ;
2) échec indiscernable en surface, sans règle violée ;
3) perte du repère interne chez l’expert lui-même.
-->

---

<div class="eyebrow">Partie I · Agir d’après une représentation (Ch. 1–4)</div>

# L’asymétrie fondamentale : représentation vs action

<div class="cols-40-60">

<div>

- Nous ne manipulons jamais le monde directement : nous raisonnons sur une **représentation** finie.
- Mais **le monde répond à l’action**, jamais à notre représentation.
- Exemple des voiliers : M. X estime le risque de démâter à 5 %, M. Y à 0,1 %. La mer ne consulte aucun de ces deux chiffres.
- Une issue unique ne juge guère un prévisionniste : seule la répétition permet la **calibration**.

</div>

<div class="fig">

![Le monde répond à l'action, non à la représentation](../monographie/figures/ch02-cible-monde-action.svg)

<div class="caption">

Figure 2.1 — Ce sur quoi l’on calcule (la représentation) et ce qui répond (le monde, via l’action).

</div>

</div>

</div>

<!--
Minutage : 2 min (total 5,5/35).
Insistez sur le fait qu’une probabilité de 5 % ou 0,1 % n’est pas une propriété physique du mât : c’est un poids sur des mondes possibles. Le problème critique survient lors d’une décision unique, où la réponse du monde arrive après l’acte.
-->

---

<div class="eyebrow">Partie I · Chapitres 1–2</div>

# Le cadre et l’arrière-plan tacite

<div class="cols">

<div>

## « L’eau bout à 100 °C »…

- Eau salée → ne bout pas à 101 °C.
- Autocuiseur fermé → pas à 104 °C.
- Sommet du mont Blanc → bout à ~85 °C.

<div class="card blue">

$$A \cap (\dots) \rightarrow B$$

<span class="small">Toute règle empirique suppose un **arrière-plan tacite** $\mathcal{T}$ ouvert d’exceptions.</span>

</div>

</div>

<div>

## Quatre choix avant tout calcul

Un **cadre** est une spécification finie choisie *en amont* de l’inférence :

1. variables retenues ;
2. catégories ;
3. classe de modèles ;
4. objectif poursuivi.

<span class="small">Déduction et induction ne certifient leur conclusion que *« pourvu que »* le cadre convienne (la dinde inductiviste à la veille de Noël).</span>

</div>

</div>

<!--
Minutage : 2 min (total 7,5/35).
Point clé : la rigueur formelle (déductive ou statistique) reste relative au cadre. On ne peut pas énumérer toutes les conditions de (...) sans rendre la règle inutilisable.
-->

---

<div class="eyebrow">Partie II · Ce qui peut nous détromper (Ch. 5)</div>

# Ce que mesure — et ce que tait — une barre d’erreur

<div class="cols-40-60">

<div>

<div class="card">

<div class="card-title">Proposition 1 <span class="statut">résultat sous hypothèses</span></div>

<span class="small">Une mesure quantitative d’incertitude résume le **désaccord à l’intérieur d’un ensemble d’alternatives admises** $\Theta$.</span>

</div>

<div class="small tight">

- Un facteur omis $z$ absent de $\Theta$ reçoit un poids nul.
- Constant lors de la collecte : **aucune trace** (coefficient de sécurité 1,8 sur une ferrure vs brouillard salin ; modèles hypothécaires d’avant 2008).
- Variable non enregistré : gonfle le bruit aléatoire sans nommer la cause.

</div>

</div>

<div class="fig">

![Trois incertitudes : aléatoire, épistémique, ontologique](../monographie/figures/ch05-trois-incertitudes.svg)

<div class="caption">

Figure 5.1 — Décomposition de la variance dans $\Theta$ vs incertitude ontologique hors du cadre.

</div>

</div>

</div>

<!--
Minutage : 2 min (total 9,5/35).
Faites sentir l’image de la note d’hypothèses dont il manque la page 2 : dix relecteurs qui lisent la même note tombent d’accord, mais leur accord ne mesure que la cohérence de la page 1.
-->

---

<div class="eyebrow">Partie II · Chapitre 6</div>

# Pas de détection sans comparateur — et cinq conditions

<div class="cols-45-55">

<div>

<div class="card blue">

**Proposition 2** <span class="statut def">définition</span>
Une erreur n’est détectée que lorsqu’une affirmation est confrontée à un **comparateur** censé concorder avec elle, que la comparaison fait apparaître un désaccord et que quelqu’un en prend acte.

</div>

<div class="small tight" style="margin-top: 10px;">

- **Cinq portes en série :** $D \subseteq C_1 \cap C_2 \cap C_3 \cap C_4 \cap C_5$. Qu’une seule manque systématiquement ⇒ **probabilité d’échappement = 100 %**.
- **Cas *Challenger* (1986) :** l’alerte existait, mais la comparabilité (16 vols sans dommage omis) et la **prise en compte** (autorité) ont cédé.

</div>

</div>

<div class="fig">

![Les cinq portes : existence, différence, comparabilité, arrivée à temps, prise en compte](../monographie/figures/ch06-cinq-conditions.svg)

<div class="caption">

Figure 6.1 — Cinq conditions simultanées : si une porte reste fermée, l’erreur passe à 100 %.

</div>

</div>

</div>

<!--
Minutage : 2 min (total 11,5/35).
Notez l’asymétrie logique (section 6.5) : un désaccord prouve qu’au moins un des deux côtés se trompe ; un accord ne prouve rien tant qu’on ne sait pas si le contrôle pouvait échouer (sévérité).
-->

---

<div class="eyebrow">Partie II · Chapitre 7</div>

# Le cadre comme cause commune de nos contrôles

<div class="cols-45-55">

<div>

<div class="card">

<div class="card-title">Proposition 3 (modèle M3) <span class="statut">résultat sous hypothèses</span></div>

<div class="small">

**(a)** Tout comparateur calculé depuis les seules variables $x$ du cadre a $\Lambda = 1$ vis-à-vis d’un facteur omis $z$.
**(b)** Les observations du monde ne révèlent $z$ que s’il a varié durant la collecte et affecte ce qui est enregistré.

</div>

</div>

<div class="small tight">

- **Défaillance de mode commun :** deux pompes sur une même prise ↔ éléments finis et calcul manuel sans corrosion.
- **Régression :** auditer un cadre exige… un autre cadre.
- **Deux seules entrées :** *être averti* (tiers) ou *découvrir par l’épreuve* (monde).

</div>

</div>

<div class="fig">

![Le cadre comme cause commune](../monographie/figures/ch07-cause-commune.svg)

<div class="caption">

Figure 7.1 — Deux contrôles internes partageant les variables $X$ restent aveugles à $z$.

</div>

</div>

</div>

<!--
Minutage : 2 min (total 13,5/35).
C’est le cœur théorique du livre : l’auto-vérification corrige des fautes de calcul ou d’étourderie à l’intérieur du cadre, jamais les omissions du cadre lui-même.
-->

---

<div class="eyebrow">Partie II · Chapitres 8–9</div>

# Chaînes en série, contrôles croisés et blanchiment

<div class="cols-45-55">

<div>

<div class="card">

<div class="card-title">Propositions 4 & 5 (modèle M1) <span class="statut">résultat</span> <span class="statut hyp">hypothèse</span></div>

<div class="small tight">

- **Chaîne :** <span class="math"><i>B</i><sub>chaîne</sub> ⊇ ⋃ <i>B</i><sub><i>i</i></sub> ∪ <i>B</i><sub>interfaces</sub></span> — les angles morts s’additionnent.
- **Contrôle croisé :** <span class="math"><i>B</i><sub>croisé</sub> = <i>B</i><sub>1</sub> ∩ (<i>B</i><sub>2</sub> ∪ <i>B</i><sub>cmp</sub>)</span> — l’indépendance se paie en effort de comparabilité.

</div>

</div>

<div class="card orange" style="margin-top: 10px;">

<div class="card-title">Blanchiment aux interfaces</div>

<span class="small">Quand les hypothèses, unités ou réserves disparaissent d’une étape à l’autre (tableau nu, unités perdues de *Mars Climate Orbiter*), un résultat conditionnel arrive en aval comme un fait établi.</span>

</div>

</div>

<div class="fig tall">

![Chaîne en série vs contrôle croisé en parallèle](../monographie/figures/ch00-serie-parallele.svg)

<div class="caption">

Figure 0.1 — En série, les angles morts s’additionnent ; en parallèle, seul l’angle mort commun subsiste.

</div>

</div>

</div>

<!--
Minutage : 2 min (total 15,5/35).
Transition vers la Partie III : nous avons maintenant forgé toutes nos clés générales — sans avoir prononcé le mot « LLM » une seule fois depuis l’ouverture. Voyons comment ces clés ouvrent la pile informatique.
-->

---

<div class="eyebrow">Partie III · De l’informatique classique à l’IA (Ch. 10–11)</div>

# Informatique classique vs composants appris

<div class="cols">

<div class="card blue">

<div class="card-title">Couches basses : composant spécifié</div>

<div class="small tight">

- Règles écrites + **contrat** opposable ($\{P\}\,C\,\{Q\}$).
- **Vérification en amont :** types, tests, analyse statique, preuve — établie *une fois* pour toutes les exécutions futures.
- Quand il échoue, l’erreur garde une **adresse** (ligne, module, interface).

</div>

</div>

<div class="card orange">

<div class="card-title">Sommet de pile : composant appris</div>

<div class="small tight">

- On **dépense** la garantie préalable pour acheter de la *portée* sur des tâches impossibles à spécifier.
- La spécification migre dans les données, le coût et l’alignement.
- **Orienter** (consignes, RLHF) s’apparente au dressage plutôt qu’au câblage d’un disjoncteur (loi de Goodhart).

</div>

</div>

</div>

<div class="card" style="margin-top: 8px;">

**Objectif statistique :** un modèle de langage optimise la *plausibilité* du fragment suivant, non la vérité ni le respect d’un contrat — d’où des faux fluides et assurés (*Mata v. Avianca*).

</div>

<!--
Minutage : 2 min (total 17,5/35).
Rappelez que l’informatique classique n’est pas exempte d’erreurs silencieuses (Orbiter l’a prouvé), mais elle permet de vider la case silencieuse à l’avance par un contrat appliqué.
-->

---

<div class="eyebrow">Partie III · Chapitre 12</div>

# Un changement de régime au sommet de la pile

<div class="cols-3">

<div class="card">

<div class="card-title">1. Trois bascules simultanées</div>

<div class="small tight">

- **Promesse :** statistique en moyenne, pas par sortie.
- **Échec :** prose lisse indiscernable du vrai.
- **Enquête :** pas d’adresse pour une rustine locale.

</div>

</div>

<div class="card orange">

<div class="card-title">2. Frontière en dents de scie</div>

<div class="small">

Étude BCG : +40 % de qualité *dans* la frontière, mais **−19 points** sur des tâches voisines *hors* frontière — sans aucun changement de ton.

Apparaît aussi l’**omission de saillance** (facteur présent mais non mobilisé).

</div>

</div>

<div class="card blue">

<div class="card-title">3. Calibration générative</div>

<div class="small">

Invention forcée sur les faits rares de la longue traîne (Kalai–Vempala) + pénalisation de l’abstention.

Répéter 5 tirages trahit les *erreurs hasardées*, jamais les *erreurs constantes*.

</div>

</div>

</div>

<div class="card" style="margin-top: 10px;">

**Conséquence pratique :** faute de vérifier la couche en amont, il faut reporter le contrôle *sortie par sortie*, ou reconstruire un comparateur mécanique autour d’une tâche bornée.

</div>

<!--
Minutage : 2 min (total 19,5/35).
Insistez sur la distinction entre erreurs hasardées (détectables par entropie sémantique / tirages répétés) et erreurs constantes (idées reçues, oublis systématiques : sévérité nulle de la répétition).
-->

---

<div class="eyebrow">Partie III · Chapitre 13</div>

# Synthèse : deux axes et quatre sources de comparateurs

<div class="cols-38-62">

<div class="small tight">

- **Ligne (dans / hors cadre) :** fixée par le cadre ; aucun procédé interne ne remonte d’une ligne.
- **Colonne (signalée / silencieuse) :** dépend des comparateurs ; *la formalité déplace la colonne, non la ligne*.
- Les modèles appris peuplent la case **dans le cadre · silencieuse**.
- **4 sources :** énoncé fixé d’avance (compilateur, Lean, Simplex), contrôles personnels, autre raisonneur, le monde.

</div>

<div class="fig tall">

![Matrice à deux axes : lieu de la cause et réaction des comparateurs](../monographie/figures/ch13-deux-axes.svg)

<div class="caption">

Figure 13.1 — Ajouter des comparateurs déplace vers la gauche ; seul le dehors touche la ligne du bas.

</div>

</div>

</div>

<!--
Minutage : 2 min (total 21,5/35).
C’est aussi le lien classique entre vérification (résoudre correctement le problème posé : colonne) et validation (poser un problème fidèle au réel : ligne).
-->

---

<div class="eyebrow">Partie IV · L’automatisation et ses angles morts (Ch. 14–16)</div>

# Ce que l’automatisation fait aux contrôles

<div class="cols-3">

<div class="card">

<div class="card-title">1. Chaîner jusqu’à l’acte (Ch. 14)</div>

<div class="small">

**Agents** = chaînes à $N$ étapes où chaque maillon blanchit le précédent en texte libre.

Passage des *réponses* aux *actions* : l’autorité d’agir passe à la couche la moins garantie (Knight Capital : 460 millions de dollars perdus en 45 min).

À $N=12$ avec $q=3\,\%$, le contrôle par pairs réduit l’échec ($53{,}8\,\% \to 7{,}11\,\%$), mais $q$ cause $42{,}2\,\%$ du reste.

</div>

</div>

<div class="card orange">

<div class="card-title">2. Éroder l’humain (Ch. 15)</div>

<div class="small">

Disparition de la **friction** qui créait nos repères internes.

Disparition du **signe révélateur** du doute ; effondrement du **signal coûteux** de la forme (→ *équilibre mélangeant*).

Ironie de Bainbridge + 2 pièges de la consigne : transmission du cadre et **complaisance**.

</div>

</div>

<div class="card blue">

<div class="card-title">3. Corréler à grande échelle (Ch. 16)</div>

<div class="small">

Un **prêteur unique** de savoir : aide contre les fautes de l’emprunteur, jamais contre celles du prêteur.

**Blanchiment de provenance :** 20 copies d’une dépêche simulent 20 témoins ; récursion vers l’*effondrement de modèle*.

Le débit d’output explose pendant qu’on comprime l’évaluation.

</div>

</div>

</div>

<!--
Minutage : 2,5 min (total 24/35).
Soulignez que ces trois mécanismes (enchaînement, érosion, corrélation) agissent ensemble dans les organisations qui déploient l’IA pour « gagner du temps ».
-->

---

<div class="eyebrow">Partie IV · Chapitres 9 & 16</div>

# L’énigme arithmétique : taux d’erreur vs risque résiduel

<div class="cols-55-45">

<div class="card orange small">

**Risque résiduel :** $R = P(E) \times \Pr(\bar{C} \mid E) = P(E)\,(1 - s\,u)$
• Outil A : $10\,\% \times 1\,\% = \mathbf{0{,}1\,\%}$ · Outil B : $1\,\% \times 90\,\% = \mathbf{0{,}9\,\%}$
*10× moins d’erreurs à la source, 9× plus de risque à l’action.*

</div>

<div class="card blue small">

**Modèle M1 (modèle partagé) :** $P(\text{faux}) : 10\,\% \to 2\,\%$, $c : 10\,\% \to 60\,\%$.
Sensibilité $32\,\%$, VPP $11{,}6\,\%$, échappement **$96{,}3\,\%$** sous appariement (plancher **$68{,}0\,\%$** sous examen complet).

</div>

</div>

<div class="fig fig-wide" style="margin-top: 8px;">

![Échappement et risque résiduel avec un modèle partagé](../monographie/figures/ch16-modele-partage.svg)

<div class="caption">

Figure 16.1 — Réduire les fausses alertes répare la VPP, mais ne perce jamais le plancher $c$ des causes partagées.

</div>

</div>

<!--
Minutage : 2,5 min (total 26,5/35).
C’est l’image la plus frappante à laisser à un public technique ou dirigeant : les benchmarks ne mesurent que le premier facteur, P(E). Toute l’architecture des contrôles gouverne le second facteur, l’échappement.
-->

---

<div class="eyebrow">Partie V · Décider et se prémunir (Ch. 17)</div>

# Décisions sans appel : calibrer ou verrouiller

<div class="cols-40-60">

<div class="small tight">

Seuil de Savage : $p^\ast = \Delta U / (\Delta U + L)$ (voilier : $3{,}85\,\%$ ; vol de nuit : $0{,}0100\,\%$).

Modèle **M2** : $p_w = 1 - (1-p)(1-z)$ ; règle de décision : $p + b < p^\ast$.

- **Calibrer ce qui se répète** en milieu stable (historique + score propre).
- **Verrouiller ce qui ne se joue qu’une fois :** ajouter une **marge d’humilité** $b$ (jugement, non mesure) + poser un **verrou** devant l’acte irréversible.
- **Bac à sable :** explorer librement là où le monde répond vite et à bas coût (compilateur, tests).

</div>

<div class="fig">

![Quatre quadrants de décision M2 avec marge d'humilité](../monographie/figures/ch17-decisions.svg)

<div class="caption">

Figure 17.1 — Sans marge ni verrou, une fissure non repérée ($z$) fait basculer dans le piège silencieux.

</div>

</div>

</div>

<!--
Minutage : 2 min (total 28,5/35).
Rappelez les deux garde-fous de cette architecture : un bac à sable ne révèle que ce qu’il modélise (l’agent ne doit pas pouvoir réécrire ses propres tests), et multiplier les verrous sur des actes bénins transforme l’humain en automate qui clique « Accepter ».
-->

---

<div class="eyebrow">Partie V · Chapitre 18</div>

# Un remède à trois niveaux

<div class="cols-40-60">

<div>

<div class="card blue small">

**Niveau 1 · Attitude (soi-même)**
Attente écrite *avant* de consulter ; **pré-mortem** ; élargir $\Theta$.
*Limite :* ne déborde pas son propre cadre.

</div>

<div class="card aqua small">

**Niveau 2 · Placement (le flux)**
*Où* (passages vers l’action) · *Qui* (partage l’interface & lit dessous) · *Quoi* (sortie + représentation) · *Combien* (plafonné par la capacité ; RAG comme outil de placement).

</div>

<div class="card orange small">

**Niveau 3 · Organisation**
Budget indépendant protégé · état de vérification obligatoire · **historique** · mesure directe par **erreurs injectées** (TIP aérien, test par mutation).

</div>

</div>

<div class="fig">

![Correspondance entre les trois niveaux et les cinq conditions](../monographie/figures/ch18-trois-niveaux.svg)

<div class="caption">

Figure 18.1 — Aucun niveau ne couvre seul les cinq conditions ; ensemble, ils se soutiennent.

</div>

</div>

</div>

<!--
Minutage : 2,5 min (total 31/35).
Insistez sur le critère test d’une revue au niveau 3 : « Quelle erreur cette étape peut-elle arrêter que le producteur n’aurait pas pu arrêter lui-même ? » Sinon, elle fabrique une signature.
-->

---

<div class="eyebrow">Boîte à outils pratique · Chapitres 17 & 18</div>

# Deux grilles de questions à emporter

<div class="cols">

<div class="card blue">

<div class="card-title">Devant un chiffre assuré (4 questions, Ch. 17)</div>

<span class="small">*À adresser à l’**institution** si le chiffre sort d’un système automatisé :*</span>

1. **Sous quelles conditions** ce chiffre tient-il ?
2. **Qu’est-ce qui le ferait changer** sensiblement ?
3. **Quelle est la manière la plus vraisemblable** dont il pourrait être faux ?
4. **Qu’a-t-on délibérément choisi** de ne pas modéliser ?

</div>

<div class="card aqua">

<div class="card-title">Avant d’agir sur une affirmation (5 questions, Ch. 18)</div>

1. **Existence :** quel est le comparateur ?
2. **Différence :** comment peut-il se tromper *autrement* ?
3. **Comparabilité :** les conditions et la provenance sont-elles conservées ?
4. **À temps :** la confrontation a-t-elle lieu *avant* l’acte (verrou) ?
5. **Prise en compte :** qui écoute le désaccord et peut arrêter ?

</div>

</div>

<!--
Minutage : 2 min (total 33/35).
Ces deux listes opérationnalisent tout le livre sans aucun prérequis mathématique. Accepter « nous ne savons pas » ou « nous n’avons pas modélisé ce facteur » comme réponse informative est la condition de possibilité de la première liste.
-->

---

<div class="eyebrow">Conclusion · La méthode appliquée à elle-même</div>

# Ce que vaut ce cadre — et ses propres limites

<div class="cols">

<div>

## Transparence épistémique

- **Propositions P1–P5 :** chaque thèse affiche son statut (*définition*, *résultat sous hypothèses*, *hypothèse de travail*, *constat empirique*).
- **Parties III–V :** diagnostic appuyé sur un petit nombre d’études datées (BCG 2023, METR 2025, Knight Capital, *Mata*) ; les remèdes restent une **démarche de travail** à éprouver.
- **Co-élaboration :** rédaction itérative assistée par LLM assumée et soumise aux comparateurs du livre.

</div>

<div>

## Six tensions laissées ouvertes

- Distance optimale entre producteur et contrôleur.
- Coût vs indépendance (comparateurs peu coûteux mais oubliés).
- Omission de saillance vs omission structurelle.
- Prise en compte comportementale réelle des alertes.
- Signe net du risque sous modèles partagés ($P(E)\!\downarrow$ vs $c\!\uparrow$).
- Efficacité non encore mesurée des remèdes sur flux IA.

</div>

</div>

<!--
Minutage : 1 min (total 34/35).
Il est rare qu’un ouvrage s’applique ses propres critères d’audit jusqu’à formuler ce qui le réfuterait empiriquement.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="eyebrow">À retenir · En une phrase</div>

# Ne jugez pas un outil à son taux d’erreur moyen, mais à ce qui peut vous contredire avant l’acte.

<div class="subtitle" style="margin-top: 12px;">

*Agir d’après une représentation du monde* · 8 parcours de lecture · Cours complet en 3 heures disponible

</div>

<div class="meta">

**Pour aller plus loin :** Table 0.1 de la monographie (parcours *Ingénieur*, *Informaticien / IA*, *Décideur*, *Destinataire d’un chiffre*, *Parcours critique*) et Annexes A–D.

</div>

<!--
Minutage : 1 min (total 35/35).
Ouvrez la discussion / les questions avec l’auditoire.
-->
