# Diapositives du cours — *Agir d’après une représentation du monde*

Ce dossier contient les supports de présentation construits avec **Marp** (Markdown + MathJax SVG hors ligne + figures vectorielles de `../monographie/figures/`).

## Contenu

- `slides_courts.md` / `.html` / `.pdf` / `.pptx` — **Format « message » (35 min, 18 diapositives)** : la thèse centrale, les cinq conditions, le basculement IA/automatisation, le paradoxe $P(E) \times \text{échappement}$ et les trois niveaux de remède.
- `slides_3h.md` / `.html` / `.pdf` / `.pptx` — **Format « panorama complet » (3 h, 3 × 55 min, 45 diapositives)** : les 5 parties, les 5 propositions (**P1–P5**), les 3 modèles (**M1–M3**), les 18 figures, les études de cas, deux ateliers pratiques et le bilan épistémique final.
- `themes/monographie.css` — thème reprenant la palette (`#2a78d6`, `#eb6834`, `#1baf7a`, `#1d232b`) et la typographie de la monographie.
- `Makefile` — compilation HTML, PDF (avec signets et notes) et PPTX.

## Compiler et présenter

Depuis `slides/` :

```bash
make short     # HTML5 autonome (35 min)
make 3h        # HTML5 autonome (3 h)
make pdf       # PDF 35 min avec signets et notes de l'orateur
make 3h-pdf    # PDF 3 h avec signets et notes de l'orateur
make pptx      # PowerPoint 35 min
make 3h-pptx   # PowerPoint 3 h
make all       # Tout compiler
```

*(Les cibles PDF et PPTX utilisent `chrome-headless-shell` installé localement dans `~/.cache/puppeteer`.)*

Ouvrir `slides_courts.html` ou `slides_3h.html` dans un navigateur :
- **`P`** : vue présentateur (affiche les notes orales, le minutage et la diapositive suivante)
- **`F`** : plein écran
- **`O`** : vue d’ensemble des diapositives
