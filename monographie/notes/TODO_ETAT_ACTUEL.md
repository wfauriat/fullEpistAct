# État d’avancement et liste des tâches (avec traçabilité)

**Horodatage :** `2026-11-20T14:10:10+01:00`  
**Branche courante lors de l’état des lieux :** `style-pass` (HEAD `098ca4d`, issue de `main` `163884f`)

---

## 1. Généalogie et traçabilité des passes de relecture (*Lineage*)

| Étape | Commit / Date | Artefacts produits | Contenu et statut actuel |
| :--- | :--- | :--- | :--- |
| **1. Rédaction initiale & relectures croisées** | Jusqu’à `fddee93` (18–19 nov. 2026) | `chapitres/*.md`, `NOTES_*.md`, `RELECTURE_partie1..5.md` | Rédaction complète des chapitres 0 à 18 et de la conclusion, vérification mécanique initiale (`make verifier`). **Terminé.** |
| **2. Relectures « à froid » & synthèse des arbitrages** | `7afa571` (19 nov. 2026, 16:57) | `LECTURE_FRAICHE_Opus_*.md`, `LECTURE_FRAICHE_Sonnet_*.md`, `A_TRANCHER_*.md`, `SYNTHESE_A_TRANCHER.md` | 408 points compilés et classés en Groupe 1 (corrections directes), Groupe 2 (arbitrages rapides) et Groupe 3 (questions de fond `D1–D5`, écarts sources `E1–E3`). **Synthétisé.** |
| **3. Arbitrages auteur (lot 1) & application des corrections** | `7afa571` (19 nov. 2026, 16:57) | `DECISIONS_SYNTHESE.md`, `EDITS_SYNTHESE.md`, `EDITS_*.md` | **Note de fraîcheur :** l’en-tête de `DECISIONS_SYNTHESE.md` (*« Aucune décision n'est encore appliquée »*) est **obsolète**. Tous les points du **Groupe 1** (`G1-1` à `G1-22`, alignement des *Points clés*, lot § 4.3) et tous les points marqués ***Adopté*** dans `DECISIONS_SYNTHESE.md` (`N1–N4`, `R1–R4`, `R6–R11`, `V2–V18`, `V20`, `S2–S5`, `S10`, `S14`) ont été **appliqués** dans `7afa571`. Seuls les points listés en fin de `EDITS_SYNTHESE.md` (l. 991–1014) restent ouverts. |
| **4. Relecture intégrale sur épreuve PDF compilée** | `163884f` (`main`, 20 nov. 2026, 12:45) | `REVIEW_PASS_LIVRE_ECRAN.md` (sur `build/livre-ecran.pdf`, 264 p.) | Lecture de bout en bout après application de `7afa571`. Ses constats sont **actifs** : recoupe certains points ouverts du Groupe 3 (`D1`) et identifie des tensions propres à la lecture linéaire (§ 3 et § 4), des défauts de compilation LaTeX/Lua (§ 5.1–5.3) et les éléments de complétude manquants (§ 5.4–5.5). |
| **5. Passe de style automatisée (rédacteur + juge Opus)** | `8270e8d..098ca4d` (`style-pass`, 20 nov. 2026) | `style/BILAN_PASSE.md`, `style/lots/*/journal.md` | 83 retouches conservatrices appliquées sur 19 fichiers (coupes de phrases longues, retrait de « Or » initiaux et d’italiques d’emphase ; `make verifier` : 0 erreur). Signale 2 micro-points locaux à relire (ch. 6 et ch. 14). **Prêt à fusionner dans `main`.** |

---

## 2. Feuille de route priorisée des points restants

Les identifiants entre crochets indiquent la lignée de chaque point :
- `[SYN-*]` : issu de `SYNTHESE_A_TRANCHER.md` / `EDITS_SYNTHESE.md` (points laissés ouverts) ;
- `[DEC-*]` : laissé `Ouvert` dans `DECISIONS_SYNTHESE.md` ;
- `[REV-*]` : issu de `REVIEW_PASS_LIVRE_ECRAN.md` ;
- `[STY-*]` : signalé dans `style/BILAN_PASSE.md`.

*(Le détail complet des options et recommandations pour les Priorités 1 et 2 figure dans le document compagnon `monographie/notes/ARBITRAGES_RESTANTS.md`.)*

---

### Priorité 1 — Tensions conceptuelles, formelles et quantitatives (Arbitrages auteur + retouches texte)

- [ ] **P1.1 — `[SYN-D1]` + `[REV-4A.1]` : Modèle M1, indépendance ($c, m, s$), plancher de 68,0 % et baisse du risque net au ch. 16**
  - *Fichiers :* `chapitres/08-independance-chaines.md`, `chapitres/09-severite-echappement.md`, `chapitres/16-angles-morts-collectifs.md`, `parties/partie-4.md` (et éventuellement `commun/parametres.py` si renommage/modification de scénario).
  - *Objet :* Distinguer « indépendance » ($c$ faible) et « sensibilité » ($s = (1-c)(1-m)$) ; ne pas attribuer le plancher d’échappement de 68,0 % au seul $c = 60\,\%$ ($1 - s = c + (1-c)m = 68{,}0\,\%$) ; expliquer dès le ch. 16 pourquoi le risque résiduel de la Table 16.1 baisse de 5,57 % à 1,93 % malgré la corrélation (et en quoi $c$ est une part conditionnelle des erreurs restantes).
- [ ] **P1.2 — `[SYN-D2]` : Définition du *cadre* et de la *représentation* (emboîtés ou disjoints ?)**
  - *Fichiers :* `chapitres/02-cadre.md`, `commun/registre_termes.md`, `chapitres/99-conclusion.md`.
  - *Objet :* Lever le recouvrement entre les deux définitions (lecture emboîtée recommandée : la représentation comprend le cadre et ce que l’on construit à l’intérieur de lui).
- [ ] **P1.3 — `[REV-4A.3]` : Sens de « Cause dans le cadre » dans la matrice à deux axes (Table 13.1) face à la Définition 2**
  - *Fichiers :* `chapitres/13-synthese-deux-axes.md`.
  - *Objet :* Préciser pourquoi les inventions d’un modèle de langage (*Mata v. Avianca*) et les omissions de saillance figurent dans la ligne « Cause dans le cadre » de la Table 13.1 (cadre de la tâche ou du domaine, alors que le composant appris n’a pas de liste explicite de variables $X$ et optimise la plausibilité plutôt que la vérité factuelle).
- [ ] **P1.4 — `[SYN-D3]` : Portée du terme *blanchiment* (conditions seules, unités/définitions, provenance)**
  - *Fichiers :* `chapitres/08-independance-chaines.md`, `chapitres/14-chaines-qui-agissent.md`, `chapitres/15-erosion-verifications.md`, `chapitres/16-angles-morts-collectifs.md`, `parties/partie-2.md`, `commun/registre_termes.md`.
  - *Objet :* Harmoniser la définition du ch. 8, ses « cousins » et le *blanchiment de provenance* du ch. 16 (recommandation : inclure unités et définitions dans les conditions au ch. 8 pour garder *Mars Climate Orbiter* comme exemple central, et faire du blanchiment de provenance le cousin développé au ch. 16).
- [ ] **P1.5 — `[SYN-D4]` : *Challenger* lu à travers les cinq conditions de détection**
  - *Fichiers :* `chapitres/06-detecter-une-erreur.md`, `chapitres/05-trois-incertitudes.md`.
  - *Objet :* Clarifier le partage entre *existence* (relevés des 23 vols disponibles), *différence* (mise en forme dans le cadrage même de l’affirmation) et *comparabilité* (7 vols retenus sur 24), et scinder les deux défaillances de la *prise en compte* (décideurs vs. autorité des ingénieurs).
- [ ] **P1.6 — `[SYN-D5]` : Proposition 4 — ce que « coûte » l’indépendance (structure vs. tendance)**
  - *Fichiers :* `chapitres/08-independance-chaines.md`, `parties/partie-2.md`, `chapitres/99-conclusion.md`.
  - *Objet :* Séparer le volet structurel (l’indépendance se paie en comparabilité) de la tendance empirique / hypothèse de travail (le coût d’un contrôle tend à croître avec son indépendance ; les comparateurs bon marché reportent ce prix sur la mise en correspondance et la prise en compte).
- [ ] **P1.7 — `[REV-4A.2]` : Marge d’humilité $b$ face aux axiomes de Savage (UES) au ch. 17**
  - *Fichiers :* `chapitres/17-decisions-sans-appel.md`.
  - *Objet :* Préciser dans l’encadré *Nuance* comment l’ajout de $b$ à $p$ ($p + b < p^\ast$) et son calibrage qualitatif au vu de $L/\Delta U$ se situent par rapport à l’UES de Savage (où $L/\Delta U$ fixe déjà $p^\ast$ : retenue délibérée hors UES stricte contre la mauvaise spécification du cadre, et non double comptage des enjeux).
- [ ] **P1.8 — `[REV-4A.4]` : Portée universelle de la Proposition 1 face à sa preuve par la variance**
  - *Fichiers :* `chapitres/05-trois-incertitudes.md`.
  - *Objet :* Ajouter une phrase dans le *Noyau formel* précisant que l’équation (5.1) démontre la proposition pour la variance prédictive, tandis que les autres mesures (intervalles quantiles, pire cas, prédiction conforme) obéissent à la même restriction structurelle à $\Theta$.
- [ ] **P1.9 — `[REV-4A.5]` : Double acception du mot *risque* ($p, p_w$ avec enjeux vs. $R = P(E)(1-su)$ sans enjeux)**
  - *Fichiers :* `chapitres/09-severite-echappement.md`, `chapitres/17-decisions-sans-appel.md`.
  - *Objet :* Gloser d’une phrase au ch. 9 (ou ch. 17) que le « risque résiduel » $R$ du modèle M1 désigne la probabilité qu’une affirmation fausse atteigne l’action, avant pondération par l’asymétrie des enjeux $L/\Delta U$ des ch. 4 et 17.
- [ ] **P1.10 — `[REV-4B.1]` à `[REV-4B.6]` : Précisions formelles et mathématiques locales**
  - `[REV-4B.1]` En-tête de la dernière colonne des Tables 8.2 et 14.1 (`tableaux/ch08-chaine.md`, `tableaux/ch14-pipeline-agent.md` / script générateur) : « Part des défaillances restantes *où intervient* $q$ » (au lieu de « *due à* $q$ »).
  - `[REV-4B.2]` Ch. 12 (`chapitres/12-autre-regime.md`, exemple à 5 tirages) : remplacer « une autre date 10 % » par une 6e date explicite (ex. « 10 % sur le 5 mars ») pour que le terme $0{,}10^5$ soit mathématiquement exact sans changer aucun chiffre généré.
  - `[REV-4B.3]` Ch. 6 (`chapitres/06-detecter-une-erreur.md`) : alléger l’écho circulaire « en prend acte » entre la Proposition 2 et la Définition 6.
  - `[REV-4B.4]` Ch. 6 et Ch. 9 (`chapitres/06-detecter-une-erreur.md`, `chapitres/09-severite-echappement.md`) : harmoniser ou signaler la lettre de l’événement « erreur arrêtée à temps » ($D$ au ch. 6 vs. $C$ au ch. 9).
  - `[REV-4B.5]` Ch. 7 (`chapitres/07-cadre-cause-commune.md`, Modèle M3, Hypothèse 2) : simplifier la redondance avec le conditionnement par $X = x$ de l’Hypothèse 3.
  - `[REV-4B.6]` Ch. 18 (`chapitres/18-remede-trois-niveaux.md`, § 18.4, niveau 3) : mentionner l’*existence* aux côtés de *différence*, *comparabilité* et *prise en compte*.
- [ ] **P1.11 — `[SYN-E1]`, `[SYN-E2]`, `[SYN-E3]` : Alignements avec les sources internes**
  - `[SYN-E1]` Ch. 13 et Conclusion : le monde comme seul comparateur qui ne soit pas une représentation (source ultime, directe ou par l’intermédiaire d’un tiers qui avertit, en accord avec les deux voies du ch. 7).
  - `[SYN-E2]` Ch. 0 : rattacher les « deux pièges » (cadrage de la consigne et complaisance) au contrôle du travail humain par le modèle, et la lecture « deux fois de la même représentation » à la relecture humaine du brouillon du modèle (en accord avec le ch. 15).
  - `[SYN-E3]` Ch. 15 et `parties/partie-4.md` : présenter la soumission d’un texte déjà rédigé comme un pis-aller explicite et harmoniser l’annonce des *deux* conditions dans le chapeau du ch. 15 et la page de la partie 4.

---

### Priorité 2 — Arbitrages rapides restants (Groupe 2), répétitions inter-chapitres et micro-points de style

- [ ] **P2.1 — `[DEC-R5]`, `[DEC-V1]`, `[DEC-V21]` : Vocabulaire transversal et registre restés ouverts**
  - `[DEC-R5]` « un texte fixé à l’avance » vs. « un énoncé fixé à l’avance » (registre, ch. 6, ch. 13, pages des parties 2 et 3).
  - `[DEC-V1]` « exact » (producteur) vs. « précis » (contrôleur à faible $f$) ; formulation de « dix fois moins de fausses alertes » et « fausses alertes sur 5 % des affirmations correctes » (ch. 9, ch. 16, partie 2).
  - `[DEC-V21]` Harmonisation de « comparabilité », « lisibilité », « comparaison fidèle » et glose de $B_{\text{cmp}}$ (ch. 14, ch. 16, partie 4).
- [ ] **P2.2 — `[SYN-S1]`, `[SYN-S1b]`, `[DEC-S6]`, `[SYN-S7..S9]`, `[SYN-S11..S13]`, `[SYN-S15]` : Points structurels et locaux par chapitre**
  - `[SYN-S1]` & `[SYN-S1b]` Ch. 18 : titre et synthèse du niveau 3 ; ajout de la limite manquante sur la 3e pratique du niveau 1.
  - `[DEC-S6]` Ch. 4 et Ch. 17 : formulation de la conviction du joueur de roulette russe (barillet cru vide vs. chambre face au percuteur).
  - `[SYN-S7]` Ch. 0 : niveau de jargon technique, rattachement de la phrase METR, annonce de *Challenger* et distinction des grilles à 4 et 5 questions.
  - `[SYN-S8]` Ch. 12 : incise justificative sur Mercure vs. Vénus comme planète en moyenne la plus proche de la Terre.
  - `[SYN-S9]` Ch. 13 : précisions sur les quatre sources de comparateurs (recouvrement sources 1/4, ferrure, « loi de commande » pour Simplex, référent de « vos propres contrôles »).
  - `[SYN-S11]` Ch. 2 : points locaux (jeu d’étalonnage, jargon de l’encadré causal/conforme, barre qui casse).
  - `[SYN-S12]` Ch. 8 : précisions sur le modèle M1 (angle mort de probabilité 1 vs. oubli $m$, notation $B$ vs. $B_i$, distributivité de $B_1 \cap (B_2 \cup B_{\text{cmp}})$).
  - `[SYN-S13]` Ch. 16 : précisions de lecture du calcul (« à corrélation égale », borne $P(\text{faux})$).
  - `[SYN-S15]` Ch. 1 : origine des chiffres de la sonde à ultrasons, second passage vs. seconde sonde, sens de lecture du score logarithmique.
- [ ] **P2.3 — `[SYN-C1..C7]` & `[SYN-6.3]` : Arbitrages propres à la Conclusion**
  - Statut de « le monde répond à l’action » (`C-1`) ; rôle des constats empiriques entre corps, tableau et PC (`C-2`) ; « hypothèse de travail » vs. « démarche de travail » (`C-3`) ; point faible du ch. 11 dans le tableau (`C-5`) ; « dériver / dérivation » (`C-6`) ; liste des constats empiriques (`C-7`) ; mention éventuelle des deux auto-corrections par rapport à l’article arXiv (`§ 6.3.2`).
- [ ] **P2.4 — `[REV-3.1]` & `[REV-3.2]` : Répétitions en lecture linéaire et numérotation M1–M3**
  - Arbitrer le degré d’allègement des études de cas racontées plusieurs fois in extenso : *Mars Climate Orbiter* (ch. 0, 8, 10, 12), *METR 2025* (doublon quasi identique entre ch. 0 et ch. 15), *Mata v. Avianca* (ch. 0 et ch. 11).
  - Confirmer le maintien de la numérotation `M3` (ch. 7) $\to$ `M1` (ch. 8–9) $\to$ `M2` (ch. 17) (déjà contextualisée par `N3`), ou décider d’un renommage.
- [ ] **P2.5 — `[STY-1]` & `[STY-2]` : Micro-retouches issues du bilan de la passe de style**
  - Ch. 6, l. 129 : rétablir la symétrie d’italique sur « *au moins l’un des deux termes est faux* » / « il ne prouve rien ».
  - Ch. 14, l. 52 : vérifier la tournure « Tout pipeline n’est toutefois pas condamné… ».

---

### Priorité 3 — Corrections techniques de compilation, renvois `@sec:` et gabarit LaTeX/Lua

*(Terminé sur `main` après la fusion de `style-pass` ; vérifié sur `build/livre-ecran.pdf` et `build/livre.html`.)*

- [x] **P3.1 — `[REV-5.1]` : Réparation des renvois de sections (`@sec:` / `\nameref`) en français**
  - Corrigé l’accord « au section 0.7 » $\to$ « à la section 0.7 » (`chapitres/07-cadre-cause-commune.md`, `chapitres/17-decisions-sans-appel.md`).
  - Numéroté les sous-sections de niveau 3 (`h.level == 3`, `chap.sect.subsect`) dans `filtres/monographie.lua` pour les aligner sur la numérotation LaTeX (`section 13.2.1`, `section 13.2.4`, `section 14.2.1`, `section 18.1.4`, etc.) et préfixé les renvois aux sections non numérotées (Avant-propos, Conclusion) par `section « … »`.
- [x] **P3.2 — `[REV-5.2]` : En-têtes courants (`\markboth`) et coupure visuelle de la Conclusion**
  - Ajouté `\markboth` explicite pour les chapitres non numérotés (*Avant-propos*, *Conclusion : la méthode appliquée à elle-même*, *Bibliographie*) et `\clorepartie` (espacement de table des matières + remise à la racine des signets PDF via `bookmark`) avant la Conclusion, les Annexes et la Bibliographie (`filtres/monographie.lua`, `gabarit/preambule.tex`).
- [x] **P3.3 — `[REV-5.3]` : Glyphe manquant (`□`) pour $\mathcal{T}$ dans les annexes B et C**
  - Déclaré `\newunicodechar{𝒯}{\ensuremath{\mathcal{T}}}` dans `gabarit/preambule.tex` (0 caractère manquant dans `build/livre-ecran.log`).

---

### Priorité 4 — Génération des artefacts manquants et rédaction des annexes A et D

- [ ] **P4.1 — `[REV-5.5b]` : Tableau généré manquant au chapitre 1**
  - Générer ou raccorder `monographie/tableaux/ch01-bayes-cotes.md` (actuellement affiché `[Contenu généré manquant : tableaux/ch01-bayes-cotes.md]` p. 27).
- [ ] **P4.2 — `[REV-5.5c]` : Rédaction des Annexes A et D**
  - `monographie/annexes/A-outils-reference.md` (*Outils de référence*).
  - `monographie/annexes/D-parametres.md` (*Paramètres des exemples quantitatifs*, à partir de `commun/parametres.py`).
- [ ] **P4.3 — `[REV-5.5a]` : Génération des 9 figures conceptuelles (*Figure à générer*)**
  - `figures/ch00-serie-parallele.pdf` (ch. 0, p. 7)
  - `figures/ch00-carte-ouvrage.pdf` (ch. 0, p. 13)
  - `figures/ch02-cible-monde-action.pdf` (ch. 2, p. 31)
  - `figures/ch05-trois-incertitudes.pdf` (ch. 5, p. 67)
  - `figures/ch05-ferrure-marge.pdf` (ch. 5, p. 71)
  - `figures/ch06-cinq-conditions.pdf` (ch. 6, p. 76)
  - `figures/ch07-cause-commune.pdf` (ch. 7, p. 86)
  - `figures/ch13-deux-axes.pdf` (ch. 13, p. 156)
  - `figures/ch18-trois-niveaux.pdf` (ch. 18, p. 226)

---

### Priorité 5 — Passe de vérification bibliographique et seconde passe de style (optionnelle)

- [ ] **P5.1 — `[REV-5.4]` & `[SYN-5]` : Vérification bibliographique et factuelle**
  - Résoudre les 3 balises `[à vérifier : ...]` dans le texte :
    1. Ch. 2 (p. 40) : Shanahan, « The Frame Problem », *Stanford Encyclopedia of Philosophy*.
    2. Ch. 5 (p. 66) : rapport ou étude sur les modèles de risque hypothécaire et la corrélation des défauts avant 2008.
    3. Ch. 11 (p. 137) : déclaration d’Air Canada (*Moffatt v. Air Canada*).
  - Vérifier les points factuels listés dans `SYNTHESE_A_TRANCHER.md` § 5 (*Mata v. Avianca* sanctions, *Challenger* direction NASA vs. Thiokol, *Mars Climate Orbiter* chaîne causale, Knight Capital code dormant/réactivé, chiffres exacts BCG, Lean autoformalisation).
  - Valider et basculer les ~60 entrées de `commun/biblio_a_verifier.bib` vers `commun/biblio.bib` pour faire disparaître le marqueur orange « ? » après chaque citation.
- [ ] **P5.2 — `[STY-P2]` : Seconde passe de style ciblée (optionnelle, après stabilisation du fond)**
  - Cible : chapitres encore denses (ch. 0, 13, 14, 15 et 16 ; moyenne actuelle 29–31 mots/phrase), avec les trois consignes issues de `style/BILAN_PASSE.md`.
