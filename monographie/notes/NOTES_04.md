# Notes — Chapitre 04

## Références à ajouter ou à vérifier
- `[@savage1954]` (clé candidate dans `commun/biblio_a_verifier.bib`) — formulation de l’utilité espérée subjective (actes, états du monde, conséquences, utilités, probabilités personnelles et théorème de représentation) à la `#sec:ch04-ues` et dans l’encadré `.outils`. Conforme au champ `averifier` (« utilité espérée subjective (ch. 3, 4, 17) »).
- Aucun marqueur `[@A-VERIFIER: …]` en texte libre n’a été laissé dans le chapitre.
- Aucune donnée empirique chiffrée : toutes les valeurs numériques (course à la voile à $L/\Delta U = 25$, M. X à 5 %, M. Y à 0,1 %, roulette russe à $L/\Delta U = 10\,000$ avec $p = 0{,}001\,\%$) sont explicitement présentées comme illustratives, conformément à l’exemple `seu-a` de `00_global.md` §7 et de `commun/parametres.py`.

## Termes proposés (absents du registre)
- Aucun terme nouveau proposé. Les quatre termes prévus pour le chapitre 4 dans `commun/registre_termes.md` — **utilité espérée subjective (UES)**, **rapport des enjeux**, **seuil $p^\ast$** et **décision unique** — ainsi que les notations $p$, $L$, $\Delta U$ et $p^\ast$ ont été introduits en gras (strictement une seule fois à leur définition) et définis dans le texte.
- Précaution d’ordre des dépendances respectée : aucun recours au facteur omis $z$ (ch. 5 et 7), à la marge d’humilité $b$ (ch. 17), au risque réel $p_w$ (ch. 17), ni aux termes techniques introduits à partir du chapitre 5 (*incertitude aléatoire / épistémique / ontologique*, *ensemble des alternatives admises*, *affirmation*, *contrôle*, *comparateur*, *prise en compte*, *taux d’erreur*, *probabilité d’échappement*, *angle mort*, *sévérité*, *vérification*, *validation*, *agent*, *marge d’humilité*, *verrou*, *bac à sable*). Le mot *marge* a été évité au profit d’*écart*, *agent* a été remplacé par *décideur* (ou *chacun*), et *gravité* remplace *sévérité*.
- Renvois prospectifs limités au `#sec:ch17`, conformément à `content_spec/part1.md` et à `course_outline.md`.

## Paramètres / figures demandés
- Aucun paramètre ni figure supplémentaire demandés. La figure `figures/ch04-seuil.pdf` / `.svg` (`{#fig:ch04-seuil}`) et le tableau `tableaux/ch04-seuil.md` (`{#tbl:ch04-seuil}`) existent déjà et reproduisent les valeurs canoniques du scénario `seu-a` (`commun/parametres.py` et `00_global.md` §7).

## Écarts par rapport à la spec
- **Placement de l’exemple quantitatif `seu-a` :** la figure `#fig:ch04-seuil` et le tableau `#tbl:ch04-seuil` réunissent la course à la voile ($L/\Delta U = 25$) et la roulette russe ($L/\Delta U = 10\,000$). Le bloc `.exemple-quantitatif` est donc placé en fin de section 3 (`#sec:ch04-roulette-russe`), après l’introduction des deux situations dans le texte principal.
- **Règle du texte principal (`authoring_conventions.md` §4) :** la définition et le sens de l’UES figurent dans le texte principal de la section 1 (`#sec:ch04-ues`), le bloc `.outils` donnant la notation générale ($\mathcal{A}$, $\Omega$, $c(a, \omega)$, $U$, $\mathrm{UE}(a)$) et la propriété d’invariance affine. De même, l’`@eq:ch04-seuil` apparaît dans le texte principal de la section 2 (`#sec:ch04-course-voile`), tandis que le bloc `.formel` en expose la dérivation algébrique détaillée et les quatre hypothèses explicites.
- **Titre du bloc `.formel` :** le titre retenu est `Dérivation du seuil de décision` sans formule LaTeX dans l’attribut `titre="…"`, car la fonction `esc` de `filtres/monographie.lua` échappe les délimiteurs `$` et accolades dans les titres de blocs.

## Incohérences repérées ailleurs
- Confirmation dans `make chapitre CH=04` du comportement déjà signalé dans `NOTES_03.md` : comme l’unique figure du chapitre est placée à l’intérieur d’un bloc (`.exemple-quantitatif`), pandoc omet `\setkeys{Gin}{keepaspectratio}` dans le `.tex` de l’aperçu isolé, si bien que `figures/ch04-seuil.pdf` est étirée sur `\textheight` (`Package tcolorbox Warning: The upper box part has become overfull`). Ce défaut n’affecte pas le livre complet (où d’autres chapitres ont des figures hors blocs), mais gagnerait à être corrigé dans `gabarit/preambule.tex` ou `filtres/monographie.lua` (`figure_fixe`).
- `monographie/commun/exemples_courants.md` : toujours au stade de gabarit vide ; l’apparition du chapitre 4 pour l’exemple courant « Voiliers, M. X et M. Y » (seuil $p^\ast$ et décisions opposées sous UES à $L/\Delta U = 25$) reste à y consigner lors de la mise à jour par le mainteneur.
