# Notes — Chapitre 01

## Références à ajouter ou à vérifier
- `[@hume1748]` (clé candidate dans `commun/biblio_a_verifier.bib`) — annonce du problème de l’induction de David Hume au `#sec:ch01-modes-inference` (repris au chapitre 7).
- `[@definetti1974]`, `[@jaynes2003]`, `[@lindley2006]` (clés candidates dans `commun/biblio_a_verifier.bib`) — lecture de la probabilité comme jugement et degré de plausibilité sous information au `#sec:ch01-probabilite` (les entrées actuelles ne mentionnent que le chapitre 3 ; à vérifier pour les chapitres 1 et 3).
- Aucun marqueur `[@A-VERIFIER: …]` en texte libre n’a été nécessaire : le chapitre ne cite pas de donnée empirique chiffrée et présente uniquement des outils logiques et probabilistes classiques accompagnés d’illustrations arithmétiques.

## Termes proposés (absents du registre)
- Aucun terme nouveau proposé. Tous les termes prévus pour le chapitre 1 dans `commun/registre_termes.md` ont été introduits en gras et définis : **déduction**, **induction**, **rapport de vraisemblance**, **score logarithmique**, ainsi que les notations $\Pr(\cdot)$, $\Pr(B \mid A)$ et $A \cap (\dots) \rightarrow B$.
- Précaution de terminologie respectée : conformément à la règle d’ordre des dépendances, *cadre*, *représentation*, *mondes possibles*, *calibration*, *taux de base*, *sensibilité*, *taux de fausses alertes* et *valeur prédictive positive (VPP)* ne sont ni définis ni employés dans leur sens technique (seules des annonces explicites renvoient vers les chapitres 2 et 3 là où la spécification le prévoit).

## Paramètres / figures demandés
- **`ch01-bayes-cotes`** — `#sec:ch01-bayes`, bloc `.exemple-quantitatif` (« Mise à jour par cotes lors d’un contrôle par ultrasons ») :
  - **Paramètres canoniques proposés pour `commun/parametres.py` :**
    - Caractéristiques du test (choisies distinctes du dépistage du chapitre 9 : $1\,\%$, $90\,\%$, $5\,\%$) : $\Pr(T^+ \mid D) = 0{,}75$, $\Pr(T^- \mid D) = 0{,}25$, $\Pr(T^+ \mid \bar{D}) = 0{,}15$, $\Pr(T^- \mid \bar{D}) = 0{,}85$, donnant $\Lambda(T^+) = 5$ et $\Lambda(T^-) = 5/17 \approx 0{,}294$.
    - Quatre scénarios :
      1. `Lot courant, signal T+` : $\Pr(D) = 4\,\%$, cote a priori $1/24 \approx 0{,}0417$, $\Lambda = 5$, cote a posteriori $5/24 \approx 0{,}208$, $\Pr(D \mid T^+) = 5/29 \approx 17{,}2\,\%$.
      2. `Zone suspecte, signal T+` : $\Pr(D) = 20\,\%$, cote a priori $0{,}25$, $\Lambda = 5$, cote a posteriori $1{,}25$, $\Pr(D \mid T^+) = 5/9 \approx 55{,}6\,\%$.
      3. `Zone suspecte, signal T-` : $\Pr(D) = 20\,\%$, cote a priori $0{,}25$, $\Lambda = 5/17 \approx 0{,}294$, cote a posteriori $5/68 \approx 0{,}0735$, $\Pr(D \mid T^-) = 5/73 \approx 6{,}85\,\%$.
      4. `Zone suspecte, deux signaux T+` : $\Pr(D) = 20\,\%$, cote a priori $0{,}25$, $\Lambda = 25$, cote a posteriori $6{,}25$, $\Pr(D \mid T^+, T^+) = 25/29 \approx 86{,}2\,\%$.
  - **Tableau demandé (`tableaux/ch01-bayes-cotes.md`, étiquette `{#tbl:ch01-bayes-cotes}`) :** colonnes `Situation | Probabilité a priori | Cote a priori | Rapport de vraisemblance | Cote a posteriori | Probabilité a posteriori`, et légende reprenant explicitement les quatre paramètres du test (`75 %`, `25 %`, `15 %`, `85 %`) pour satisfaire le contrôle automatique de cohérence numérique dans `outils/verifier.py`. Une fois ce tableau généré, on pourra ajouter un renvoi explicite à `@tbl:ch01-bayes-cotes` dans le paragraphe *Calcul* (omis provisoirement pour ne pas déclencher d’erreur d’étiquette non définie).
  - **Figure demandée (`figures/ch01-bayes-cotes.pdf` et `.svg`, étiquette `{#fig:ch01-bayes-cotes}`) :** graphique horizontal ou diagramme de pente (*slopegraph* / barres groupées) montrant le passage de la probabilité *a priori* à la probabilité *a posteriori* dans les quatre situations, afin de rendre visible que le même facteur multiplicatif $\Lambda = 5$ laisse le lot courant sous $20\,\%$ mais porte la zone suspecte au-dessus de $50\,\%$, et que l’absence de signal ($T^-$) abaisse la probabilité à $6{,}85\,\%$.

## Écarts par rapport à la spec
- **Formule reliant score logarithmique et rapport de vraisemblance :** `content_spec/part1.md` (section 6) évoquait « *the likelihood ratio as the ratio of surprises* ». Or, avec $S(p) = -\ln p$, la différence des surprises $S(p_2) - S(p_1) = \ln(p_1 / p_2)$ égale le *logarithme* du rapport de vraisemblance $\Lambda = p_1 / p_2$, soit $\Lambda = \exp(S(p_2) - S(p_1))$, et non le rapport des surprises $S(p_2) / S(p_1)$. Le chapitre rétablit la relation mathématique exacte dans le texte et le bloc `.formel`.

## Incohérences repérées ailleurs
- `content_spec/part1.md` (ligne 24) : remplacer « *the likelihood ratio as the ratio of surprises* » par « *the log likelihood ratio as the difference of surprises (and the likelihood ratio as the exponential of that difference)* », en cohérence avec `monographie/tableaux/ch03-score-log.md` ($S_X = 3{,}00$, $S_Y = 6{,}91$, $\Lambda = \exp(6{,}91 - 3{,}00) = 50$).
- `content_spec/part1.md` (ligne 28) et `content_spec/00_global.md` (§7) : `part1.md` demande un bloc `.exemple-quantitatif` avec tableau pour le chapitre 1, mais aucun jeu de paramètres n’était encore défini pour le chapitre 1 dans `00_global.md` §7 ni dans `commun/parametres.py`.
- `monographie/commun/biblio_a_verifier.bib` (lignes 58–76) : ajouter la mention du chapitre 1 dans le champ `averifier` de `definetti1974`, `jaynes2003` et `lindley2006`.
