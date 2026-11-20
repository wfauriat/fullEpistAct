# Document d’aide à l’arbitrage — Points ouverts (Priorités 1 et 2)

**Horodatage :** `2026-11-20T14:10:10+01:00`  
**Base textuelle examinée :** branche `style-pass` (`098ca4d`, incluant l’ensemble des corrections de `7afa571` consignées dans `EDITS_SYNTHESE.md`).

Ce document regroupe **tous les points de fond, de structure et de terminologie encore ouverts** à l’issue du croisement entre :
1. les points laissés ouverts dans `SYNTHESE_A_TRANCHER.md` et `DECISIONS_SYNTHESE.md` (listés en fin de `EDITS_SYNTHESE.md`) ;
2. la relecture intégrale sur le PDF compilé (`REVIEW_PASS_LIVRE_ECRAN.md`) ;
3. les deux micro-points signalés par les juges de la passe de style (`style/BILAN_PASSE.md`).

Pour chaque point figurent : sa **lignée**, les **chapitres et fichiers impactés**, la **tension ou lecture alternative** qu’il engendre dans l’état actuel du texte, les **options** et une **recommandation**, ainsi qu’une ligne `Décision :` pour noter votre arbitrage.

---

# PARTIE I — PRIORITÉ 1 : Tensions conceptuelles, formelles et quantitatives

---

## P1.1 — Modèle M1 : indépendance ($c, m, s$), plancher de 68,0 % et baisse du risque net au chapitre 16
- **Lignée :** `[SYN-D1]` (ch. 8 T8, ch. 9 T1–T2, ch. 16 T1–T3, p4) + `[REV-4A.1]` (`REVIEW_PASS_LIVRE_ECRAN.md` § 4A.1) + `[SYN-S13]` (ch. 16 T3, T4, T6).
- **Chapitres et fichiers impactés :**
  - `chapitres/08-independance-chaines.md`
  - `chapitres/09-severite-echappement.md`
  - `chapitres/16-angles-morts-collectifs.md` (légende Fig. 16.1, lecture Table 16.1, encadré *Nuance*, Points clés)
  - `parties/partie-4.md`
  - *(Optionnel : `commun/parametres.py` si l’on modifie ou renomme un scénario)*
- **Tension ou lecture alternative engendrée :**
  1. **Flottement sur « indépendance » et sur le « plancher » ($c$ vs. $1-s$) :** Dans M1, la sensibilité du contrôleur vaut $s = (1-c)(1-m)$ et l’échappement sous examen complet ($u = 1$) vaut $1 - s = c + (1-c)m$. Or le texte appelle « indépendance » tantôt un $c$ faible, tantôt un $s$ élevé (ch. 9), tantôt une baisse de $m$. De plus, au ch. 16 (légende de la Fig. 16.1 p. 193 et encadré *Nuance* p. 195), le plancher d’échappement de **68,0 %** est décrit comme *« imposé par les 60 % de causes partagées »* ou fixé par *« la seule corrélation, à 60 % »*, alors que $68{,}0\,\% = 1 - (1 - 0{,}60)(1 - 0{,}20)$ additionne les **60 %** de causes partagées ($c$) et les **8 %** d’oublis indépendants ($(1-c)m$).
  2. **Scénario *Indépendant et précis* :** Ce scénario baisse à la fois $c$ (de 60 % à 10 %) et $m$ (de 20 % à 10 %), mais le texte du ch. 16 attribue toute la baisse du plancher (de 68,0 % à 19,0 %) à la seule chute de $c$, alors que le tableau contient déjà la comparaison à $m = 20\,\%$ constant (*Un modèle pour tous* à 68,0 % vs. *Contrôle entre pairs* à 28,0 %).
  3. **Tension avec l’avertissement sur le risque net (Table 16.1) :** Les sections 0.5.4 et 9.5 montrent qu’un producteur 10 fois plus exact peut former un système 9 fois plus risqué ($0{,}1\,\% \to 0{,}9\,\%$). Or, dans la Table 16.1 du ch. 16, passer de *Contrôle entre pairs* ($P(\text{faux}) = 10\,\%, c = 10\,\%$) à *Un modèle pour tous* ($P(\text{faux}) = 2\,\%, c = 60\,\%$) **fait baisser** le risque résiduel de **5,57 % à 1,93 %** sous appariement (et de **2,80 % à 1,36 %** sous examen complet). Le ch. 16 le signale brièvement en fin d’encadré (l. 53), mais un lecteur linéaire peut trouver que le tableau émousse le titre de la section (*« Le taux d'erreur baisse, la probabilité d'échappement monte »*). En outre, comme $c = \Pr(\text{cause partagée} \mid E)$ est une part *conditionnelle* aux erreurs restantes, éliminer 80 % des erreurs idiosyncrasiques (passer de 10 % à 2 % d’erreurs) fait mécaniquement grimper $c$ de 10 % à 50 % même si le taux absolu d’erreurs de cause commune ($P(E)\times c$) restait constant à 1,0 % (dans la Table 16.1, il passe seulement de $10\,\% \times 10\,\% = 1{,}0\,\%$ à $2\,\% \times 60\,\% = 1{,}2\,\%$).
- **Options :**
  - **(a) Clarification purement textuelle (sans toucher à `parametres.py` ni aux figures/tableaux) :**
    1. Réserver partout « indépendance » à un $c$ faible, et appeler $s = (1-c)(1-m)$ la « sensibilité » (qui combine indépendance $1-c$ et vigilance sur les autres causes $1-m$).
    2. Préciser au ch. 9 et au ch. 16 que le plancher d’échappement sous examen complet vaut $1 - s = c + (1-c)m$ (soit $60\,\% + 8\,\% = 68{,}0\,\%$), dont $c = 60\,\%$ constitue la part incompressible due à la corrélation.
    3. Au ch. 16, illustrer l’effet pur de $c$ à $m = 20\,\%$ constant par l’écart entre 68,0 % (*Un modèle pour tous*, $c = 60\,\%$) et 28,0 % (*Contrôle entre pairs*, $c = 10\,\%$), puis mentionner que *Indépendant et précis* ($19{,}0\,\%$) abaisse en outre $m$ de 20 % à 10 %.
    4. Ajouter 2 phrases dans la lecture du ch. 16 expliquant que : (i) le tableau illustre un cas où le gain brut sur les erreurs idiosyncrasiques ($10\,\% \to 2\,\%$) fait baisser le risque global *toutes erreurs confondues* ($5{,}57\,\% \to 1{,}93\,\%$), tout en rendant le contrôle croisé quasi inopérant (1,93 % contre 2,00 % sans contrôleur) ; (ii) sur le sous-ensemble des erreurs du modèle lui-même (qui passent de $1{,}0\,\%$ à $1{,}2\,\%$ en fréquence absolue et deviennent souvent des erreurs à fort enjeu ou systémiques), le filet de sécurité a disparu.
  - **(b) Modification des paramètres générés (`parametres.py`) :** Fixer $m = 20\,\%$ dans *Indépendant et précis* ou choisir un taux d’erreur $P(\text{faux})$ intermédiaire (ex. 6 % ou 7 %) où le risque résiduel total augmente en valeur absolue. *(Plus lourd : oblige à régénérer figures et tableaux des ch. 9 et 16 et à retoucher la Conclusion.)*
- **Recommandation :** **Option (a)**. Elle ne casse aucun artefact généré, conserve la cohérence avec la Conclusion (qui discute déjà la baisse de 5,57 % à 1,93 %), rectifie l’arithmétique du plancher de 68,0 % ($60\,\% + 8\,\%$) et éclaire de façon très pédagogique la différence entre la baisse des étourderies individuelles et la perte du filet de sécurité sur les erreurs partagées.
- **Décision :** 

---

## P1.2 — *Cadre* et *représentation* : définitions emboîtées ou disjointes ?
- **Lignée :** `[SYN-D2]` (ch. 2 T1, liste transversale p1 n° 7).
- **Chapitres et fichiers impactés :**
  - `chapitres/02-cadre.md` (§ 2.3 et Points clés)
  - `commun/registre_termes.md` (entrées *représentation* et *cadre*)
- **Tension ou lecture alternative engendrée :**
  - Dans le registre et au ch. 2, la **représentation** (Déf. 1) est composée de *« mesures, catégories, équations, probabilités »*, tandis que le **cadre** (Déf. 2) est fixé par le choix des *« variables, catégories, classe de modèles et objectif »*. Les deux listes se chevauchent (notamment sur *catégories*).
  - Puis le § 2.3 écrit que la représentation est *« ce que l’on construit à l’intérieur de ce cadre »* (lecture disjointe : le cadre est le contenant, la représentation le contenu), alors que le premier Point clé du ch. 2 range la redéfinition d’une catégorie du côté du cadre.
- **Options :**
  - **(a) Lecture emboîtée (le cadre fait partie de la représentation) :** La représentation est l’ensemble de la construction mentale ou formelle, et le cadre en est la spécification finie préalable (les fondations sur lesquelles le reste de la représentation est ajusté). Il suffit alors de retoucher une phrase au § 2.3 du ch. 2 : *« la représentation comprend ce cadre et les relations ou estimations que l’on construit à l’intérieur de lui »* (le registre reste intact).
  - **(b) Lecture disjointe (le cadre précède la représentation) :** Retirer *« catégories »* de la définition de la représentation dans le registre et au ch. 2 pour ne garder dans la représentation que les valeurs, paramètres et estimations construits une fois le cadre fixé.
- **Recommandation :** **Option (a)**. Elle est fidèle à l’article arXiv (*« a constructed picture of what matters and how the matters connect »*), ne touche pas au registre et demande une retouche d’une seule ligne au ch. 2.
- **Décision :** 

---

## P1.3 — Sens de « Cause dans le cadre » dans la Table 13.1 face à la Définition 2 du cadre
- **Lignée :** `[REV-4A.3]` (`REVIEW_PASS_LIVRE_ECRAN.md` § 4A.3).
- **Chapitres et fichiers impactés :**
  - `chapitres/13-synthese-deux-axes.md` (§ 13.1, introduction de la Table 13.1)
- **Tension ou lecture alternative engendrée :**
  - Au ch. 2 (Déf. 2), un *cadre* est défini par quatre choix explicites : variables $X$, catégories, classe de modèles $\Theta$ et **objectif**.
  - Au ch. 13, la **Table 13.1** range les inventions d’un modèle de langage (*Mata v. Avianca*), les erreurs constantes et les *omissions de saillance* sur la première ligne : **« Cause dans le cadre »**.
  - Or, pour un composant appris entraîné à prédire le prochain jeton plausible, il n’y a pas de liste explicite de variables du domaine $X$, et son *objectif* d’entraînement (la plausibilité statistique) diverge de l’objectif de l’utilisateur (l’exactitude factuelle ou juridique) — ce qui, au sens strict de la Déf. 2, mettrait en cause le cadre lui-même. La Conclusion reconnaît d’ailleurs (p. 233 et p. 236) que le classement d’une omission de saillance hésite à la frontière.
- **Options :**
  - **(a) Expliciter au § 13.1 ce que désigne « dans le cadre » pour une tâche confiée à un modèle appris :** Ajouter un court paragraphe avant la Table 13.1 précisant que, dans cette matrice, la ligne du haut (*Cause dans le cadre*) s’entend par rapport au **cadre du problème posé par l’utilisateur** (les faits, règles ou données qui figurent déjà dans le domaine courant ou dans la consigne fournie, sans intervention d’un facteur physique extérieur omis $z$), même lorsque le composant appris substitue son propre objectif de plausibilité à une spécification explicite.
  - **(b) Laisser le texte en l’état**, en laissant la nuance à la seule Conclusion.
- **Recommandation :** **Option (a)**. Une précision de deux phrases au § 13.1 désamorce immédiatement l’objection d’un lecteur attentif à la Définition 2 et prépare la discussion de la Conclusion.
- **Décision :** 

---

## P1.4 — Portée du terme *blanchiment* (conditions seules, unités/définitions, provenance)
- **Lignée :** `[SYN-D3]` (ch. 8 T2, T5, T17 ; ch. 14 T5 ; ch. 15 T12 ; ch. 16 T7 ; p2 T4).
- **Chapitres et fichiers impactés :**
  - `commun/registre_termes.md` (entrée *blanchiment*)
  - `chapitres/08-independance-chaines.md` (§ 8.6 et Points clés)
  - `parties/partie-2.md`
  - `chapitres/14-chaines-qui-agissent.md` (§ 14.3)
  - `chapitres/16-angles-morts-collectifs.md` (§ 16.3)
- **Tension ou lecture alternative engendrée :**
  - La Définition 9 (`@def:blanchiment`, ch. 8) définit le blanchiment uniquement comme la perte des **conditions** d’un résultat lorsqu’il change de mains.
  - Le texte du ch. 8 lui associe ensuite *« deux proches cousins »* : la perte des **unités/définitions** et la perte de la **provenance**. Pourtant, *Mars Climate Orbiter* (une perte d’unités) sert d’exemple principal pour illustrer le blanchiment au ch. 8, et le Point clé du ch. 8 englobe *« conditions, unités ou provenance »* sous le mot blanchiment.
  - Enfin, le ch. 16 rappelle que l’effacement de la provenance est l’un des deux cousins vus au ch. 8, puis introduit en gras **blanchiment de provenance** comme un nouveau terme du registre.
- **Options :**
  - **(a) Sens strict :** Le blanchiment ne porte que sur les conditions (hypothèses, domaine de validité). Les unités et la provenance restent deux cousins, et *Mars Climate Orbiter* est présenté explicitement comme l’illustration du premier cousin.
  - **(b) Sens intermédiaire (conditions incluant unités et définitions) :** Préciser dès la Déf. 9 au ch. 8 que les conditions de validité d’un résultat incluent ses hypothèses, ses unités et ses définitions. *Mars Climate Orbiter* illustre alors directement le blanchiment ; il ne reste qu’un seul cousin, touchant à l’origine de l’affirmation, que le ch. 16 baptise et développe sous le nom de **blanchiment de provenance**.
  - **(c) Sens large :** Inclure conditions, unités et provenance dès la Déf. 9 et supprimer la métaphore des « cousins ».
- **Recommandation :** **Option (b)**. Elle conserve *Mars Climate Orbiter* comme exemple phare du blanchiment aux interfaces (ch. 8 et 14), supprime le flottement entre le corps et les Points clés du ch. 8, et donne au *blanchiment de provenance* du ch. 16 une place nette (le pendant, sur l’origine, du blanchiment des conditions).
- **Décision :** 

---

## P1.5 — *Challenger* lu à travers les cinq conditions de détection
- **Lignée :** `[SYN-D4]` (ch. 6 T4–T6 ; ch. 5 T13–T14).
- **Chapitres et fichiers impactés :**
  - `chapitres/06-detecter-une-erreur.md` (§ 6.3, étude du cas *Challenger*)
  - `chapitres/05-trois-incertitudes.md` (encadré *Nuance* sur *Challenger*)
- **Tension ou lecture alternative engendrée :**
  - *Challenger* est le cas vitrine qui illustre les cinq conditions de détection au ch. 6. Or, dans la rédaction actuelle :
    1. Le fait de n’avoir retenu sur le graphique que les 7 vols présentant un dommage (en omettant les 17 vols sans dommage) est invoqué à la fois sous la condition de **différence** et sous celle de **comparabilité** (et effleuré sous **existence**). Le lecteur ne voit pas clairement ce qui distingue ici le défaut de *différence* du défaut de *comparabilité*.
    2. Sous **existence**, le texte hésite entre dire que le comparateur *existait* (les relevés des 24 vols étaient disponibles dans les dossiers) ou qu’il *manquait* (le graphique complet n’avait pas été tracé).
    3. Sous **prise en compte**, deux défaillances distinctes sont fondues en une seule : le fait que la hiérarchie n’ait pas pris acte de l’objection des ingénieurs, et le fait que les ingénieurs qui prenaient acte du danger n’avaient pas l’autorité d’arrêter le tir.
- **Options :**
  - **(a) Clarifier la répartition entre les cinq puces au ch. 6 (et aligner la phrase du ch. 5) :**
    - *Existence :* les données des 24 vols et les essais existaient dans les archives, mais le comparateur pertinent (la série complète confrontant température et présence *ou absence* d’incident) n’a pas été assemblé sur la table de décision.
    - *Différence :* l’examen des seuls vols endommagés partageait le cadrage même de l’affirmation à contrôler (chercher une tendance interne aux cas d’incident), si bien qu’il ne pouvait pas contredire l’illusion d’absence de lien.
    - *Comparabilité :* faute de mettre en regard les 7 vols avec incident et les 17 vols sans incident sur la même échelle de température, la présentation rompait la comparabilité nécessaire pour faire ressortir le seuil thermique.
    - *Arrivée à temps :* l’alerte orale des ingénieurs de Thiokol est bien arrivée la veille du tir (condition remplie).
    - *Prise en compte :* double rupture disjointe — ceux qui mesuraient le péril (les ingénieurs) n’avaient pas l’autorité d’interrompre le lancement, et ceux qui détenaient cette autorité ont renversé la charge de la preuve en demandant de prouver que la navette ne pouvait pas voler.
  - **(b) Ramener la sélection des 7 vols uniquement à la *comparabilité***, et utiliser pour la *différence* le fait que les calculs officiels partageaient les mêmes hypothèses de qualification initiale des joints.
- **Recommandation :** **Option (a)** (ou **(b)** si vous préférez que chaque fait empirique du dossier *Challenger* ne serve qu’à une seule puce — **(b)** est encore plus nette pédagogiquement).
- **Décision :** 

---

## P1.6 — Proposition 4 : ce que « coûte » l’indépendance (structure vs. tendance)
- **Lignée :** `[SYN-D5]` (ch. 8 T3 ; p2 T3 ; Conclusion : tableau, § « La tension entre coût et indépendance », PC 2).
- **Chapitres et fichiers impactés :**
  - `chapitres/08-independance-chaines.md` (`@prop:independance`, corps § 8.2 et Points clés)
  - `parties/partie-2.md`
  - `chapitres/99-conclusion.md` (Tableau des statuts l. 22, § 2.2 l. 53–57, Point clé 2)
- **Tension ou lecture alternative engendrée :**
  - Au ch. 8, la Proposition 4 énonce que l’indépendance *« tend à se payer en comparabilité — donc en coût de mise en correspondance »*.
  - Dans la Conclusion, la section sur les limites de P4 s’intitule *« La tension entre coût et indépendance n’est qu’une tendance »* et cite comme contre-exemples des comparateurs indépendants et bon marché (analyse dimensionnelle, question naïve d’un tiers, test de fumée) dont *« le prix se reporte sur la comparabilité et sur la prise en compte »*.
  - Comme l’a relevé la relecture à froid (Opus A1), si ces exceptions reportent leur prix sur la comparabilité, elles **confirment** l’énoncé du ch. 8 (*se payer en comparabilité*) au lieu d’en être des exceptions ! La confusion vient du fait que la spec (`00_global.md` § 3, P4) et l’essai *Failing Differently* distinguent deux volets :
    1. **La tension structurelle :** ce que l’affirmation et le comparateur partagent, aucun des deux ne peut le contrôler chez l’autre ; or il leur faut partager un langage commun pour être comparés. L’indépendance (la *différence*) tire donc structurellement contre la *comparabilité*.
    2. **La tendance pratique (hypothèse de travail) :** le coût direct de production d’un contrôle (effort, délai, compétence) tend à croître avec son indépendance. Les contre-exemples bon marché à produire font exception à cette tendance de coût direct, mais confirment la tension structurelle en reportant l’effort sur la traduction (*comparabilité*) et l’autorité (*prise en compte*).
- **Options :**
  - **(a) Expliciter la distinction entre (i) la tension structurelle (différence vs. comparabilité) et (ii) la tendance de coût direct (effort/délai vs. indépendance)** au ch. 8 (autour de P4 et dans les PC) ainsi que dans le tableau et le § 2.2 de la Conclusion (et remplacer le calque *« aider contre »* au ch. 8).
  - **(b) Garder le texte actuel.**
- **Recommandation :** **Option (a)**. Elle aligne parfaitement le ch. 8, la Conclusion et la spec `00_global.md`, et rend l’analyse des vérifications « bon marché mais difficiles à faire écouter » (comme le chimiste de la corrosion) beaucoup plus pénétrante.
- **Décision :** 

---

## P1.7 — Marge d’humilité $b$ face aux axiomes de Savage (UES) au chapitre 17
- **Lignée :** `[REV-4A.2]` (`REVIEW_PASS_LIVRE_ECRAN.md` § 4A.2).
- **Chapitres et fichiers impactés :**
  - `chapitres/17-decisions-sans-appel.md` (§ 17.1, Modèle M2 et encadré *Nuance*)
- **Tension ou lecture alternative engendrée :**
  - Dans le modèle M2, le seuil de décision de Savage $p^\ast = 1/(1 + L/\Delta U)$ encode déjà intégralement l’asymétrie des enjeux $L/\Delta U$.
  - Or le texte dit à la fois que $b$ *« n’est ni une mesure ni un estimateur de $z$ »*, qu’il s’ajoute à $p$ en unités de probabilité ($p + b < p^\ast$, Éq. 17.2) et que ce jugement de prudence *« s’appuie sur le rapport des enjeux $L/\Delta U$ »* (l. 21, l. 52, l. 97).
  - Un lecteur formé à la théorie de la décision (Savage) objectera : (1) si $L/\Delta U$ fixe déjà $p^\ast$, dimensionner $b$ d’après $L/\Delta U$ semble compter les enjeux deux fois ; (2) ajouter $b$ à $p$ équivaut formellement soit à réviser sa probabilité subjective d’échec à la hausse, soit à sortir des axiomes de Savage (aversion à l’ambiguïté / robustesse à la mauvaise spécification du cadre).
- **Options :**
  - **(a) Ajouter 3 phrases dans l’encadré *Nuance* du § 17.1 :** Expliquer explicitement que dans l’UES de Savage stricte — qui suppose le cadre complet —, les enjeux $L/\Delta U$ sont déjà entièrement absorbés par $p^\ast$ et toute croyance est résumée dans $p$. La marge $b$ constitue donc un **écart délibéré par rapport à l’UES interne au cadre** (apparenté aux approches d’aversion à l’ambiguïté ou de robustesse à la mauvaise spécification) : le rapport $L/\Delta U$ n’y est pas compté deux fois dans l’utilité, il commande par $p^\ast - p$ l’étroitesse de la brèche qu’une omission du cadre suffirait à ouvrir.
  - **(b) Laisser l’encadré *Nuance* en l’état.**
- **Recommandation :** **Option (a)**. Cela pare d’avance une objection classique des théoriciens de la décision sans alourdir le texte principal.
- **Décision :** 

---

## P1.8 — Portée universelle de la Proposition 1 face à sa preuve par la variance (chapitre 5)
- **Lignée :** `[REV-4A.4]` (`REVIEW_PASS_LIVRE_ECRAN.md` § 4A.4).
- **Chapitres et fichiers impactés :**
  - `chapitres/05-trois-incertitudes.md` (§ 5.2, encadré *Noyau formel*)
- **Tension ou lecture alternative engendrée :**
  - La Proposition 1 (`@prop:desaccord`) porte le statut *résultat sous hypothèses* et énonce universellement : *« Tout énoncé quantitatif d’incertitude résume à quel point les membres d’un ensemble spécifié d’alternatives admises sont en désaccord. »*
  - L’encadré *Noyau formel* qui suit immédiatement ne démontre la propriété que pour la **variance prédictive** $\operatorname{Var}(Y \mid X=x)$ via la loi de la variance totale (Éq. 5.1, sous hypothèse de moments d’ordre 2 finis).
- **Options :**
  - **(a) Ajouter une phrase en fin de *Noyau formel* au ch. 5 :** Préciser que si l’Éq. (5.1) écrit la décomposition pour la variance (sous hypothèse de moments finis), toute autre mesure quantitative d’incertitude (intervalle inter-quantiles, entropie prédictive, région de prédiction conforme ou borne au pire cas sur $\Theta$) reste par construction une fonctionnelle définie sur le seul ensemble $\Theta$ des alternatives admises, et partage donc la même cécité envers ce qui n’appartient pas à $\Theta$.
  - **(b) Laisser l’encadré en l’état.**
- **Recommandation :** **Option (a)**. Une seule phrase suffit à aligner exactement l’universalité de la Proposition 1 et son encadré formel.
- **Décision :** 

---

## P1.9 — Double acception du mot *risque* entre les Parties I/V et les Parties II/IV
- **Lignée :** `[REV-4A.5]` (`REVIEW_PASS_LIVRE_ECRAN.md` § 4A.5).
- **Chapitres et fichiers impactés :**
  - `chapitres/09-severite-echappement.md` (§ 9.5, introduction de l’Éq. 9.3)
- **Tension ou lecture alternative engendrée :**
  - Aux ch. 4 et 17, le risque d’échec ($p$ ou $p_w$) est systématiquement mis en regard du rapport des enjeux $L/\Delta U$ via le seuil $p^\ast$.
  - Aux ch. 9 et 16, l’Éq. (9.3) appelle **risque résiduel** la quantité $R = P(E)(1 - su)$, c’est-à-dire la probabilité *non pondérée par les enjeux* qu’une affirmation fausse franchisse le contrôle et conduise à l’action.
- **Options :**
  - **(a) Ajouter une incise au ch. 9 (§ 9.5) :** Préciser que l’on appelle ici *risque résiduel* (au sens de la fiabilité des contrôles) la probabilité qu’une affirmation fausse atteigne l’action ; dans une décision unique (@sec:ch04, @sec:ch17), c’est cette probabilité d’erreur non arrêtée qui devra être comparée au seuil de tolérance $p^\ast$ fixé par les enjeux $L/\Delta U$.
  - **(b) Ne rien changer.**
- **Recommandation :** **Option (a)**. Elle relie proprement les modèles M1 (ch. 9, 16) et M2 (ch. 4, 17).
- **Décision :** 

---

## P1.10 — Six précisions formelles et mathématiques locales (`REV-4B.1` à `REV-4B.6`)
- **Lignée :** `[REV-4B.1]` à `[REV-4B.6]` (`REVIEW_PASS_LIVRE_ECRAN.md` § 4B).
- **Détail des 6 sous-points :**
  1. **`[REV-4B.1]` En-tête de colonne des Tables 8.2 et 14.1 (`tableaux/ch08-chaine.md`, `tableaux/ch14-pipeline-agent.md` et script de génération) :**
     - *Problème :* La dernière colonne est intitulée *« Part des défaillances restantes **due à** $q$ »*, alors que le ratio calculé $q / P(\text{échec})$ ($68{,}3\,\%$ pour $N=4$ et $42{,}2\,\%$ pour $N=12$) donne la proportion des défaillances restantes **dans lesquelles intervient $q$** ($\Pr(Q \mid Q \cup I)$, ce que disent d’ailleurs correctement le texte courant et la légende de la figure : *« dans lesquelles intervient le facteur partagé »*). Les défaillances causées *exclusivement* par $q$ vaudraient $q(1 - p_{\text{ind}})/P(\text{échec})$.
     - *Recommandation :* Remplacer *« due à $q$ »* par *« où intervient $q$ »* dans l’en-tête du tableau généré.
  2. **`[REV-4B.2]` Calcul de collision à 5 tirages au ch. 12 (`chapitres/12-autre-regime.md`, l. 118 et 132) :**
     - *Problème :* Dans le régime 2 (*Fait rare et arbitraire*), la 6e issue de la distribution est libellée *« 10 % sur une autre date »*, mais le calcul de la probabilité que les 5 tirages répètent exactement la même erreur élève $0{,}10$ à la puissance 5 ($0{,}10^5$) comme s’il s’agissait d’une seule date précise et non d’un panier résiduel de nombreuses dates.
     - *Recommandation :* Remplacer *« 10 % sur une autre date »* par une sixième date explicite, par exemple *« 10 % sur le 5 mars »* (aux l. 118 et 132). Le calcul $0{,}10^5$ et la table générée deviennent alors mathématiquement irréprochables sans modifier un seul chiffre !
  3. **`[REV-4B.3]` Écho circulaire entre la Proposition 2 et la Définition 6 au ch. 6 (`chapitres/06-detecter-une-erreur.md`) :**
     - *Problème :* La Proposition 2 dit *« que quelqu’un ayant l’autorité d’agir en prenne acte »* et la Définition 6 définit la *prise en compte* par *« le fait qu’un désaccord parvienne à quelqu’un qui à la fois en prend acte et a l’autorité pour agir en conséquence »*.
     - *Recommandation :* Gloser légèrement la Définition 6 (*« en reconnaisse la portée — en prenne acte — et ait l’autorité… »*) ou laisser tel quel si l’écho verbal est jugé volontaire (rappel du terme de la proposition).
  4. **`[REV-4B.4]` Lettre de l’événement « erreur arrêtée à temps » : $D$ au ch. 6 vs. $C$ au ch. 9 (`chapitres/06-detecter-une-erreur.md`, `chapitres/09-severite-echappement.md`) :**
     - *Problème :* L’encadré formel du ch. 6 note $D$ (*détection suivie d’effet*) l’événement qu’une erreur soit détectée et prise en compte avant l’action (et $\Pr(\overline{D} \mid E)$ l’échappement), tandis que le ch. 9 (Éq. 9.3) et le ch. 16 notent ce même événement $C$ ($\Pr(\bar{C} \mid E)$, à côté de $c$ minuscule pour les causes partagées).
     - *Recommandation :* Soit remplacer $D$ par $C$ dans l’encadré du ch. 6 (puisque les cinq conditions y sont déjà notées $C_1, \dots, C_5$, ou garder $D$ au ch. 6 et rappeler d’un mot au ch. 9 *« noté ici $C$, pour contrôle franchi, comme $D$ au @sec:ch06 »*). Гарder $D$ avec une note d’équivalence au ch. 9 évite toute collision avec $C_1,\dots,C_5$ au ch. 6 et avec $c$ au ch. 9.
  5. **`[REV-4B.5]` Redondance dans l’Hypothèse 2 du Modèle M3 au ch. 7 (`chapitres/07-cadre-cause-commune.md`) :**
     - *Problème :* L’Hypothèse 2 énonce : *« $z$ n’est pas enregistré dans $x$, et aucune variable retenue dans $X$ ne varie avec $z$ au-delà de ce que $x$ fixe déjà »*. Dès lors que l’Hypothèse 3 conditionne sur la valeur observée $X = x$, toute variation de $z$ à $X = x$ fixé laisse $x$ invariant par définition.
     - *Recommandation :* Resserrer l’Hypothèse 2 en : *« $z$ n’est pas enregistré dans $X$, de sorte que fixer les variables retenues à la valeur observée $X = x$ laisse $z$ libre de varier »*.
  6. **`[REV-4B.6]` Rappel de la condition d’*existence* au niveau 3 du ch. 18 (`chapitres/18-remede-trois-niveaux.md`, § 18.4) :**
     - *Problème :* La synthèse du § 18.4 rattache le niveau 3 aux conditions de *différence*, *comparabilité* et *prise en compte*, en omettant que sanctuariser une capacité d’évaluation indépendante assure d’abord l’*existence* même d’un comparateur.
     - *Recommandation :* Ajouter *« l’existence, »* en tête de la liste des conditions soutenues par le niveau 3 au § 18.4.
- **Décision (pour P1.10.1 à P1.10.6) :** 

---

## P1.11 — Trois alignements avec les sources internes (`E1`, `E2`, `E3`)
- **Lignée :** `[SYN-E1]` (ch. 13 T1, conclusion l. 123), `[SYN-E2]` (ch. 0 T3), `[SYN-E3]` (ch. 15 T1, T2, T5 ; p4 T4).
- **Détail des 3 sous-points :**
  1. **`[SYN-E1]` Le monde présenté comme « seule source » d’une pertinence nouvelle (`chapitres/13-synthese-deux-axes.md` l. 120, `chapitres/99-conclusion.md` l. 123) :**
     - *Tension :* Le ch. 13 écrit : *« C’est la seule source capable, sous les conditions de la @prop:cause-commune, de démentir un cadre tout entier et de forcer l’entrée d’une pertinence nouvelle (@sec:ch07-deux-voies). »* Or la section du ch. 7 à laquelle il renvoie établit **deux** voies d’entrée d’une pertinence nouvelle : *être averti* (par un autre raisonneur) et *découvrir par l’épreuve* (le monde).
     - *Recommandation :* Écrire au ch. 13 (et harmoniser la l. 123 de la Conclusion) : *« C’est le seul comparateur qui ne soit pas lui-même une représentation, et donc le seul qui n’ait pas de cadre propre. Directement, par l’épreuve, ou indirectement, par l’intermédiaire de celui qui nous avertit après l’avoir éprouvé (@sec:ch07-deux-voies), il demeure la source ultime de toute pertinence nouvelle. »*
  2. **`[SYN-E2]` Les « deux pièges » rattachés au mauvais scénario au ch. 0 (`chapitres/00-cartographier.md`) :**
     - *Tension :* Le ch. 0 écrit : *« Et même lorsqu’un humain relit le brouillon du modèle, deux pièges referment le contrôle sur lui-même : la consigne […] transmet déjà son propre cadre à la machine, et l’entraînement des modèles à plaire… »* Or, au ch. 15 (comme dans *Failing Differently* § 9.2), ces deux pièges décrivent le scénario inverse : lorsque l’humain demande au *modèle* de contrôler le travail *humain*. Quand l’humain relit le brouillon du modèle sans s’être formé d’avis préalable, le piège est qu’il *« lit deux fois la même représentation »*.
     - *Recommandation :* Aligner le ch. 0 sur le ch. 15 : *« Relire le brouillon d’un modèle sans s’être formé d’abord son propre jugement revient à lire deux fois la même représentation. Et lorsqu’on inverse les rôles en demandant au modèle de contrôler un travail humain, deux pièges referment encore le contrôle sur lui-même : la consigne transmet déjà au modèle le cadre de l’utilisateur, et l’entraînement à plaire le pousse à la complaisance plutôt qu’à la contradiction. »*
  3. **`[SYN-E3]` Soumettre un texte « déjà rédigé » au modèle au ch. 15 (`chapitres/15-erosion-verifications.md`, `parties/partie-4.md`) :**
     - *Tension :* Pour la seconde condition d’un contrôle croisé humain–modèle, le corps du ch. 15 autorise de soumettre un texte déjà rédigé en demandant d’en chercher les failles sans indiquer la conclusion privilégiée, alors que le premier piège vient d’expliquer qu’un texte déjà rédigé transmet son cadre, et que les Points clés ne retiennent que la soumission du *problème nu*. De plus, le chapeau du ch. 15 et la page de la Partie 4 annoncent *« une condition »* au singulier alors que le texte en énonce *deux*.
     - *Recommandation :* Présenter explicitement le texte déjà rédigé comme un pis-aller au ch. 15 (*« ou, à défaut et au prix d’une neutralité moindre puisque le texte transmet déjà son découpage, lui demander de rechercher les failles… »*), et mettre *« deux conditions »* au pluriel dans le chapeau du ch. 15 et sur la page de la Partie 4 (avec les deux micro-retouches associées : *« éclaire aussi pourquoi »* et *« de cette analyse »*).
- **Décision (pour P1.11.1 à P1.11.3) :** 

---

# PARTIE II — PRIORITÉ 2 : Arbitrages rapides restants (Groupe 2), répétitions et style

---

## P2.1 — Trois points de vocabulaire transversal restés « Ouverts » dans `DECISIONS_SYNTHESE.md` (`R5`, `V1`, `V21`)
- **Lignée :** `[DEC-R5]`, `[DEC-V1]`, `[DEC-V21]`.
- **Détail des 3 sous-points :**
  1. **`[DEC-R5]` Comparateur : « un texte fixé à l’avance » vs. « un énoncé fixé à l’avance »**
     - *Où :* `commun/registre_termes.md` (entrée *comparateur*), `chapitres/06-detecter-une-erreur.md`, `chapitres/13-synthese-deux-axes.md`, `parties/partie-2.md`, `parties/partie-3.md` (avec T5 de p3 sur l’alignement des intitulés des quatre sources).
     - *Tension :* Le registre et le ch. 6 disent *« un texte fixé à l’avance »* (qui évoque un document en prose plutôt qu’un type, un contrat formel ou une loi de conservation), tandis que le ch. 13 intitule la première source *« Un énoncé fixé à l’avance »* (traduction directe de *a statement fixed in advance* dans FD).
     - *Recommandation :* Adopter **« un énoncé fixé à l’avance »** partout (registre, ch. 6, ch. 13, pages des parties 2 et 3) et aligner les intitulés des quatre sources sur la page de la partie 3.
  2. **`[DEC-V1]` « exact », « précis », « dix fois plus précis » et « 5 % de fausses alertes »**
     - *Où :* `chapitres/09-severite-echappement.md`, `chapitres/16-angles-morts-collectifs.md`, `parties/partie-2.md`.
     - *Tension :* (i) « précis » qualifie tantôt le producteur qui fait peu d’erreurs ($P(E)$ bas), tantôt le contrôleur qui fait peu de fausses alertes ($f$ bas) ; (ii) quand $f$ passe de 5 % à 0,5 %, le texte dit que le contrôleur est *« dix fois plus précis »*, alors que sa VPP ne fait que quintupler ; (iii) *« 5 % de fausses alertes »* peut être lu à tort comme $\text{FDR} = 5\,\%$ (5 % des alertes émises sont fausses) au lieu de $f = \Pr(A \mid \bar E) = 5\,\%$ (une fausse alerte sur 5 % des affirmations correctes).
     - *Recommandation :* Réserver **« exact »** au producteur ($P(E)$ bas) et **« précis »** au contrôleur ($f$ bas, comme dans le nom du scénario généré *Contrôleur précis*) ; remplacer *« dix fois plus précis »* par *« qui émet dix fois moins de fausses alertes »* ; et gloser à la première mention de $f$ au ch. 9 et au ch. 16 : *« un taux de fausses alertes $f = 5\,\%$ (c’est-à-dire une alerte déclenchée à tort sur 5 % des affirmations correctes) »*.
  3. **`[DEC-V21]` « comparabilité », « lisibilité », « comparaison fidèle » et $B_{\text{cmp}}$**
     - *Où :* `chapitres/08-independance-chaines.md`, `chapitres/14-chaines-qui-agissent.md`, `chapitres/16-angles-morts-collectifs.md`, `parties/partie-4.md`.
     - *Tension :* La troisième condition de détection s’appelle désormais partout *comparabilité* (`V20`), mais $B_{\text{cmp}}$ est appelé tantôt *« défauts de la comparaison »*, tantôt *« angle mort de la comparaison »*, et la condition $B_{\text{cmp}} = \emptyset$ est appelée *« comparaison fidèle »* ou *« lisibilité »*.
     - *Recommandation :* Utiliser **« comparabilité »** pour la propriété générale, gloser $B_{\text{cmp}}$ une fois par chapitre où il apparaît comme *« l’angle mort de la comparaison elle-même, noté $B_{\text{cmp}}$ »*, et garder *« comparaison fidèle ($B_{\text{cmp}} = \emptyset$) »* pour l’hypothèse formelle du modèle M1.
- **Décision (pour P2.1.1 à P2.1.3) :** 

---

## P2.2 — Arbitrages structurels et locaux par chapitre (`S1`, `S6` à `S9`, `S11` à `S13`, `S15`)
- **Lignée :** `[SYN-S1]`, `[DEC-S6]`, `[SYN-S7..S9]`, `[SYN-S11..S13]`, `[SYN-S15]`.
- **Détail des 9 sous-points :**
  1. **`[SYN-S1]` & `[SYN-S1b]` Chapitre 18 (`chapitres/18-remede-trois-niveaux.md`) :**
     - *Problème :* (i) Le titre du § 18.3 annonce *« Niveau 3 — L’organisation : indépendance, état de vérification, historique et mesure »*, mais la 1re sous-section porte sur la capacité d’évaluation comme budget qui plafonne la production ; (ii) le § 18.4 attribue au niveau 3 *« éviter de dépendre d’un prêteur unique »* et *« protéger l’autorité de celui qui alerte »*, qui ne font pas l’objet de sous-sections propres au § 18.3 ; (iii) au Niveau 1 (§ 18.1), la 3e pratique (*Élargir délibérément l’ensemble des mondes considérés*) n’a pas de paragraphe final énonçant sa **limite**, alors que le chapeau du chapitre promet une limite explicite pour chacune des pratiques.
     - *Recommandation :* (i) Intituler le § 18.3 *« Niveau 3 — L’organisation : capacité indépendante, état de vérification, historique et mesure »* ; (ii) dans la première sous-section du § 18.3, mentionner en une phrase que protéger une capacité d’évaluation indépendante implique aussi de préserver la diversité des sources (éviter le prêteur unique du ch. 16) et l’autorité de refus de l’évaluateur (*prise en compte*) ; (iii) ajouter à la fin de la 3e pratique du § 18.1 sa limite (issue de FD § 11.1 et du ch. 3 : les mondes ajoutés par l’imagination ne débordent jamais le cadre propre de celui qui les forme, et allonger la liste sans hiérarchie finit par diluer l’attention).
  2. **`[DEC-S6]` La roulette russe aux chapitres 4 et 17 (`chapitres/04-decider.md`, `chapitres/17-decisions-sans-appel.md`) :**
     - *Problème :* Au ch. 4 § 4.3 (et au ch. 17 l. 64), le joueur est dit *« à peu près certain que la chambre placée face au percuteur est vide ($p = 0{,}001\,\%$) »*, ce qui laisse entendre qu’il sait qu’une balle est dans le barillet mais croit connaître la position de la chambre. Puis le § 4.5 dit que sa conviction venait d’*« un cadre où une chambre chargée n’avait pas sa place »* (il croyait l’arme déchargée). En outre, au § 4.3, le premier des « deux cas » où la règle autorise à presser la détente (« s’il est quasi certain que le coup ne partira pas ») supprime le risque de 1/6 de la roulette russe classique.
     - *Recommandation :* Harmoniser aux ch. 4 et 17 sur l’exposé oral (`EXP`) : le joueur *« croit l’arme déchargée (il estime à $p = 0{,}001\,\%$ le risque résiduel qu’une balle ait été oubliée dans la chambre) »*, tandis qu’en réalité une balle a été engagée dans l’une des six chambres du barillet ($z = 1/6 \approx 16{,}7\,\%$, facteur omis par son cadre). Au ch. 4 § 4.3, écrire : *« Face à une mort possible, la règle de l’UES n’autorise à presser la détente que dans deux cas »*.
  3. **`[SYN-S7]` Chapitre 0 — Quatre petits points de construction (`chapitres/00-cartographier.md`) :**
     - *Détail :* (i) T12 : la phrase sur l’étude METR 2025 au § 0.5.2 arrive juste après l’érosion de la friction ; ajouter deux mots de transition (*« De même, lorsque l’effort visible s’efface, le ressenti cesse d’être un comparateur fiable : dans une étude… »*) ; (ii) T20 : le § 0.6 annonce que le lecteur *« retrouvera »* *Challenger* (qui n’a pas encore été cité au ch. 0) et mentionne *« la grille des quatre ou cinq questions »* comme s’il s’agissait d’une seule grille au nombre flottant : écrire *« retrouvera ou découvrira au fil des chapitres »* et *« les deux grilles de questions pratiques (quatre questions devant un chiffre assuré au @sec:ch17, cinq questions avant d’engager l’action au @sec:ch18) »*.
     - *Recommandation :* Appliquer ces deux clarifications légères au ch. 0.
  4. **`[SYN-S8]` Chapitre 12 — Mercure et Vénus (`chapitres/12-autre-regime.md`, l. 119) :**
     - *Problème :* Les deux lecteurs à froid ont cru à une erreur factuelle de l’auteur en lisant que Mercure (et non Vénus) est en moyenne la planète la plus proche de la Terre.
     - *Recommandation :* Préciser d’une courte incise à la l. 119 : *« seulement 9 % à Mercure (qui, restant plus près du Soleil, demeure en moyenne géométrique sur l’ensemble des orbites la plus proche de la Terre, contrairement à l’idée reçue qui confond distance minimale au rapprochement et distance moyenne) »*.
  5. **`[SYN-S9]` Chapitre 13 — Typologie des quatre sources de comparateurs (`chapitres/13-synthese-deux-axes.md`) :**
     - *Détail :* (i) T5 : l’exécution d’un test automatisé ou d’un noyau de preuve figure à la fois dans la source 1 (*Un énoncé fixé à l’avance*) et dans la source 4 (*Le monde : environnement informatique*) — préciser d’une phrase au § 13.2.4 que dans le monde calculatoire, confronter le code au monde (l’exécuter) revient à l’éprouver contre les énoncés formels (compilateur, tests) qui constituent cet environnement ; (ii) T6 : dans la Table 13.1, la ferrure corrodée figure dans la colonne de gauche (quand le chimiste l’inspecte avant rupture) et dans celle de droite (sans chimiste, avant rupture) — préciser *« en l’absence d’inspection chimique »* dans la case inférieure droite ; (iii) T10 : préciser dès la présentation de *« Vos propres contrôles »* qu’il s’agit des contrôles personnels **de celui qui produit ou utilise l’affirmation** (et aligner `parties/partie-3.md`). *(Note : T14 « loi de commande » pour Simplex est déjà appliqué dans le texte !)*
     - *Recommandation :* Appliquer ces trois précisions locales au ch. 13.
  6. **`[SYN-S11]` Chapitre 2 — Points locaux (`chapitres/02-cadre.md`) :**
     - *Détail :* (i) T7 : préciser en deux mots dans l’encadré sur la prédiction conforme que l’échantillon est scindé entre un jeu d’apprentissage (qui ajuste le modèle) et un jeu d’étalonnage (qui calibre le seuil de non-conformité) ; (ii) T11 : lors de la première mention des *« habitudes de codage d’un dossier »* avant l’encadré clinique, écrire *« les habitudes de saisie des dossiers médicaux »* pour que l’allusion soit immédiatement claire ; (iii) T12 : remplacer *« si sa barre casse »* (qui dans l’article est un aléa modélisé et non hors cadre) par *« si une fissure cachée sous le pont rompt son mât »* (cohérent avec le ch. 17).
     - *Recommandation :* Appliquer ces trois retouches de précision au ch. 2.
  7. **`[SYN-S12]` Chapitre 8 — Précisions de notation autour du Modèle M1 (`chapitres/08-independance-chaines.md`) :**
     - *Détail :* (i) T4/T11 : distinguer d’une phrase dans l’encadré M1 l’angle mort structurel $B_i$ (les causes manquées systématiquement, qui donneront la fraction $c$ au ch. 9) et l’oubli ponctuel de probabilité $m$ sur les autres causes ; (ii) T13 : écrire explicitement l’égalité $B_1 \cap (B_2 \cup B_{\text{cmp}}) = (B_1 \cap B_2) \cup (B_1 \cap B_{\text{cmp}})$ dans le *Noyau formel* pour justifier la phrase de prose qui énonce directement la réunion des deux termes ; (iii) T14 : au § 8.6 (blanchiment), le résultat transmis entre les maillons est noté $A \to B \to C$, où la lettre $B$ entre en collision avec l’angle mort $B_i$ du même chapitre — remplacer les étapes du pipeline au § 8.6 par $R_1 \to R_2 \to R_3$ (ou $E_1 \to E_2 \to E_3$).
     - *Recommandation :* Appliquer (i), (ii) et (iii) au ch. 8.
  8. **`[SYN-S15]` Chapitre 1 — Sonde à ultrasons et score logarithmique (`chapitres/01-outils-logique-probabilite.md`) :**
     - *Détail :* (i) T2 : préciser dans la mise en place de l’exemple de la soudure que les taux de détection (90 %) et de fausse alarme (5 %) sont connus par un étalonnage préalable de la sonde, tandis que la prévalence (1 %) vient de l’historique de fabrication ; (ii) T3 : préciser qu’il s’agit d’une *seconde sonde indépendante* (ou d’une seconde mesure dont les erreurs sont supposées conditionnellement indépendantes de la première sachant l’état de la soudure) dès la mise en place ; (iii) T4 : après la définition de la surprise $S(p) = -\ln p$, préciser en une demi-phrase le sens de lecture (*« nulle pour un événement certain ($p=1$) et d’autant plus élevée que l’événement observé avait reçu une probabilité faible »*).
     - *Recommandation :* Appliquer (i), (ii) et (iii) au ch. 1.
- **Décision (pour P2.2.1 à P2.2.8) :** 

---

## P2.3 — Arbitrages propres à la Conclusion (`C-1` à `C-7` et question éditoriale `§ 6.3.2`)
- **Lignée :** `[SYN-C1]` à `[SYN-C7]` et `[SYN-6.3]` (`SYNTHESE_A_TRANCHER.md` § 6.2–6.3).
- **Chapitres et fichiers impactés :**
  - `chapitres/99-conclusion.md` (et `chapitres/00-avant-propos.md` pour `C-3`)
- **Détail des 7 sous-points :**
  1. **`[SYN-C1]` Statut épistémique de « le monde répond à l’action » (Tableau l. 13) :**
     - *Problème :* La première ligne du tableau de la Conclusion énonce : *« Nous agissons d’après une représentation construite dans un cadre fini ; le monde répond à l’action, non à la représentation »*, et ne donne un statut (*définition*) qu’à la première moitié.
     - *Recommandation :* Étendre le statut de **définition** aux deux moitiés (l’asymétrie entre la représentation et l’action découle de la définition même de ce qu’est une représentation face au monde).
  2. **`[SYN-C2]` Rôle des constats empiriques (corps vs. tableau vs. Point clé 1) :**
     - *Problème :* Le corps de la Conclusion dit que l’argument *« a été construit pour ne dépendre d’aucun »* constat empirique, alors que le tableau attribue le statut de *constat empirique* au gain de portée (ch. 11) et à la frontière en dents de scie (ch. 12), et que le Point clé 1 dit que le poids pratique de l’ouvrage *« repose »* en partie sur eux.
     - *Recommandation :* Nuancer dans le corps : *« le noyau formel de l’argument (les cinq propositions) ne dépend d’aucun d’eux ; l’ampleur pratique des effets décrits aux parties III et IV s’appuie en revanche sur des hypothèses de travail qu’illustrent ces constats empiriques »*, et aligner le Point clé 1.
  3. **`[SYN-C3]` « Hypothèse de travail » au sens large vs. statut épistémique :**
     - *Problème :* L’ouvrage utilise *« hypothèse de travail »* à la fois pour l’un des 4 statuts épistémiques précis définis dans l’Avant-propos et pour qualifier l’ensemble du livre (*« la meilleure hypothèse de travail disponible »*, Avant-propos et Conclusion). En outre, le § 2.6 de la Conclusion dit que les remèdes de la Partie V *« ne sont pas écrits comme des hypothèses »*, alors que le tableau leur donne le statut d’*hypothèse de travail*.
     - *Recommandation :* Garder *« hypothèse de travail »* dans le tableau (en précisant au § 2.6 qu’ils ont le statut d’hypothèses de travail quant à leur efficacité empirique, bien qu’ils s’énoncent sous la forme de pratiques), et parler de *« démarche de travail »* (comme le titre de la dernière section de la Conclusion) lorsqu’on désigne la posture globale de l’ouvrage en fin de Conclusion.
  4. **`[SYN-C5]` Point faible de la ligne du ch. 11 dans le tableau de la Conclusion :**
     - *Problème :* La colonne « Point le plus faible » de la ligne du ch. 11 indique que des *« architectures mixtes rebâtissent un contrôle mécanique autour de la tâche »*. Est-ce une vraie limite de l’affirmation ou une nuance ?
     - *Recommandation :* Reformuler légèrement pour en faire une vraie limite de frontière : *« La frontière entre composant spécifié et composant appris se brouille dès qu’une architecture mixte enveloppe le modèle dans un contrôle mécanique autour d’une tâche bornée (@sec:ch13). »*
  5. **`[SYN-C6]` « dériver / dérivation » (ch. 8 et Conclusion) :**
     - *Problème :* Utilisé au sens mathématique/logique (*« n’est pas dérivée d’un modèle »*, *« erreur de dérivation »*). Admis en français scientifique, mais signalé comme calque possible de *derive* (au profit de *déduire / calcul*).
     - *Recommandation :* Remplacer *« erreur de dérivation »* par *« erreur de déduction ou de calcul »* et *« n’est pas dérivée »* par *« ne se déduit pas »* (plus idiomatique et évite toute collision avec *dérive de distribution*).
  6. **`[SYN-C7]` Liste des constats empiriques (Conclusion l. 39) :**
     - *Problème :* La phrase énumère quelques constats empiriques du livre en omettant *Challenger*, *Mata v. Avianca*, Knight Capital, la complaisance et l’appariement des probabilités.
     - *Recommandation :* Introduire la liste par *« notamment »* (solution la plus sobre).
  7. **`[SYN-6.3.2]` Mentionner ou non que le livre corrige l’article arXiv `[@fauriat2026frame]` sur deux points :**
     - *Contexte :* L’ouvrage rectifie l’article arXiv sur *Challenger* (classé comme défaut de mise en forme et de prise en compte plutôt que pur défaut de cadre) et sur la place des défaillances lourdes (placées dans la colonne *erreur silencieuse* de la matrice à deux axes plutôt que dans la seule *incertitude ontologique*).
     - *Question :* Souhaitez-vous ajouter 2 phrases dans la section *« Une provenance déclarée »* de la Conclusion pour citer ces deux rectifications de `[@fauriat2026frame]` comme exemple concret de la méthode appliquée à elle-même, ou préféreriez-vous ne pas attirer l’attention sur les écarts avec l’article ?
     - *Recommandation :* L’ajouter en 2 phrases sobres : c’est une démonstration très élégante que l’ouvrage ne traite pas son propre article fondateur comme un cadre intouchable.
- **Décision (pour P2.3.1 à P2.3.7) :** 

---

## P2.4 — Répétitions en lecture linéaire et numérotation des modèles M1–M3
- **Lignée :** `[REV-3.1]` et `[REV-3.2]` (`REVIEW_PASS_LIVRE_ECRAN.md` § 3).
- **Chapitres et fichiers impactés :**
  - *Mars Climate Orbiter* : `chapitres/00-cartographier.md`, `chapitres/08-independance-chaines.md`, `chapitres/10-couches-basses.md`, `chapitres/12-autre-regime.md`.
  - *METR 2025* : `chapitres/00-cartographier.md` (encadré *Étude de cas* p. 2) et `chapitres/15-erosion-verifications.md` (encadré *Étude de cas* p. 183–184).
  - *Mata v. Avianca* : `chapitres/00-cartographier.md` (p. 1–2) et `chapitres/11-regle-tiree-des-donnees.md` (p. 137).
- **Tension ou lecture alternative engendrée :**
  1. Conçu pour permettre les 8 parcours de lecture sélectifs de la Table 0.1, le livre raconte certains cas plusieurs fois avec un niveau de détail très proche : en particulier, l’encadré *Étude de cas* sur **METR (2025)** au ch. 0.1 et celui du ch. 15.2 reprennent presque les mêmes phrases, et l’histoire de **Mars Climate Orbiter** est déroulée quatre fois (ch. 0, ch. 8, ch. 10, ch. 12).
  2. La numérotation des modèles formels apparaît dans l’ordre **M3** (ch. 7) $\to$ **M1** (ch. 8–9) $\to$ **M2** (ch. 17). La décision `N3` a déjà ajouté une présentation de la série au ch. 0.7 et un rappel descriptif à chaque première mention, mais les étiquettes restent `M3, M1, M2`.
- **Options :**
  - **(a) Conservation de l’autonomie des chapitres + allègement ciblé des deux doublons les plus visibles :**
    - Garder la structure autonome pour les parcours de lecture (et garder `M1, M2, M3` tels que clarifiés par `N3`).
    - Au ch. 0.1, condenser légèrement les trois vignettes d’ouverture (*Mars Climate Orbiter*, *Mata v. Avianca*, *METR 2025*) pour qu’elles posent l’énigme en quelques lignes vives sans déflorer mot pour mot les encadrés *Étude de cas* détaillés des ch. 10, 11 et 15 ; et au ch. 12.1, remplacer le 4e récit de *Mars Climate Orbiter* par un rappel d’une phrase renvoyant aux ch. 8 et 10.
  - **(b) Resserrement plus fort dans tous les chapitres** (transformer ch. 10, 11, 12, 15 en simples rappels du ch. 0 — *déconseillé* car un lecteur qui suit un parcours sélectif sautant le ch. 0 perdrait l’étude de cas).
  - **(c) Ne rien changer aux études de cas** et renuméroter ou non `M3, M1, M2` en `M1, M2, M3` selon l’ordre des chapitres.
- **Recommandation :** **Option (a)** (et garder la numérotation `M1–M3` de la spec déjà expliquée par `N3`). Condenser légèrement l’ouverture du ch. 0.1 et le 4e rappel de *MCO* au ch. 12 supprime l’impression de copier-coller pour le lecteur linéaire tout en laissant les chapitres 8, 10, 11 et 15 pleinement autonomes pour les parcours sélectifs.
- **Décision :** 

---

## P2.5 — Deux micro-points signalés par les juges de la passe de style
- **Lignée :** `[STY-1]` et `[STY-2]` (`style/BILAN_PASSE.md` § « Pour la relecture finale »).
- **Chapitres et fichiers impactés :**
  - `chapitres/06-detecter-une-erreur.md` (l. 129)
  - `chapitres/14-chaines-qui-agissent.md` (l. 52)
- **Détail des 2 sous-points :**
  1. **`[STY-1]` Ch. 6, l. 129 (`chapitres/06-detecter-une-erreur.md`) :**
     - *Texte actuel après `style-pass` :* Dans le parallélisme entre désaccord et accord, l’italique a été retirée sur le second membre (*« il ne prouve rien »*) mais conservée sur le premier (*« au moins l’un des deux termes est faux »*), ce qui crée une dissymétrie typographique.
     - *Recommandation :* Retirer aussi l’italique sur « au moins l’un des deux termes est faux » (conformément à la règle de réserve des italiques de `authoring_conventions.md`).
  2. **`[STY-2]` Ch. 14, l. 52 (`chapitres/14-chaines-qui-agissent.md`) :**
     - *Texte actuel après `style-pass` :* Le retrait de la formule creuse *« Il serait toutefois inexact d’affirmer que… »* a donné *« Tout pipeline n’est toutefois pas condamné à cet empilement aveugle. »*
     - *Recommandation :* La phrase raccourcie est claire, sobre et idiomatique ; je recommande de la **valider telle quelle**.
- **Décision (pour P2.5.1 et P2.5.2) :** 
