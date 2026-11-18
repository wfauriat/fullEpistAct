# Notes — Avant-propos et Chapitre 00

## Références à ajouter ou à vérifier
- `[@fauriat2026frame]` (déjà vérifiée dans `commun/biblio.bib`) — thèse générale sur le problème du cadre, l'incertitude ontologique et la genèse hybride de la démarche (`#sec:avant-propos-objet`, `#sec:avant-propos-genese`, `#sec:ch00-representation`).
- `[@mco1999]` (clé candidate dans `commun/biblio_a_verifier.bib`) — perte de la sonde *Mars Climate Orbiter* le 23 septembre 1999, fichier `SM_FORCES`, impulsions en livres-force-secondes au lieu de newtons-secondes, facteur proche de 4,45, causes organisationnelles et existence d'une adresse de défaillance (`#sec:ch00-trois-recits`, `#sec:ch00-chaines-croises`).
- `[@mata2023]` (clé candidate dans `commun/biblio_a_verifier.bib`) — affaire *Mata v. Avianca* (S.D.N.Y., 2023), mémoire citant des décisions judiciaires inexistantes engendrées par un modèle de langage conversationnel, sanctions prononcées (`#sec:ch00-trois-recits`, `#sec:ch00-contrats-donnees`).
- `[@becker2025]` (clé candidate dans `commun/biblio_a_verifier.bib`) — essai contrôlé randomisé METR (début 2025) auprès de développeurs expérimentés de logiciels libres : ralentissement mesuré d'environ 19 % avec l'assistance d'outils d'IA contre gain de vitesse estimé après coup d'environ 20 % (`#sec:ch00-trois-recits`, encadré `.cas`, `#sec:ch00-auto-erosion`).

## Termes proposés (absents du registre)
- Aucun terme nouveau proposé. Les 64 entrées de `commun/registre_termes.md` couvrent l'ensemble des notions présentées de façon narrative au chapitre 0. Conformément aux règles de rédaction, aucun terme du registre n'est mis en gras ni défini formellement dans l'avant-propos ou au chapitre 0.

## Paramètres / figures demandés
- `ch00-serie-parallele` — schéma conceptuel — `figures/ch00-serie-parallele.pdf` (`#fig:ch00-serie-parallele`, section `#sec:ch00-chaines-croises`) : pictogramme opposant la composition en série (chaîne où les angles morts s'additionnent avec les erreurs d'interface) et la composition en parallèle (contrôle croisé où seul subsiste l'angle mort commun).
- `ch00-carte-ouvrage` — schéma synoptique — `figures/ch00-carte-ouvrage.pdf` (`#fig:ch00-carte-ouvrage`, section `#sec:ch00-architecture`) : carte d'une page représentant l'enchaînement des cinq parties et des étapes de l'argumentation (des fondements de la représentation et de la décision jusqu'au remède à trois niveaux).

## Écarts par rapport à la spec
- Aucun écart sur le fond ni sur l'organisation des sections. Pour éviter toute collision d'étiquette avec le chapitre 9 (voir ci-dessous), l'énigme arithmétique de la section `#sec:ch00-enigme-arithmetique` ($1\,\% \times 90\,\% = 0{,}9\,\%$ contre $10\,\% \times 1\,\% = 0{,}1\,\%$) est exposée directement dans le texte courant avec les valeurs exactes de `00_global.md` §7, sans inclure le fichier `tableaux/ch09-taux-echappement.md`.

## Incohérences repérées ailleurs
- `content_spec/00_global.md` (§7, ligne 290) et `monographie/tableaux/ch09-taux-echappement.md` : la note de `00_global.md` indique que `ch09-taux-echappement` peut également servir à l'aperçu du chapitre 0, mais `tableaux/ch09-taux-echappement.md` porte en dur l'étiquette `{#tbl:ch09-taux-echappement}`. Une double inclusion de ce fichier aux chapitres 0 et 9 déclencherait un avertissement d'étiquette en double dans `filtres/monographie.lua` lors de la compilation complète. Laisser l'inclusion du tableau au seul chapitre 9 (comme le suggère son préfixe `ch09`) évite ce conflit.
