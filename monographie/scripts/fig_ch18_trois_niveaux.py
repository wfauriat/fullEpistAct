"""ch18-trois-niveaux (ch. 18): how the three remedy levels cover the five detection conditions.

Outputs: figures/ch18-trois-niveaux.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, MUET, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 3.9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.8)
ax.axis('off')

# Columns: 5 detection conditions
cols = [
    (3.35, '1. Existence'),
    (4.65, '2. Différence'),
    (5.95, '3. Compara-\nbilité'),
    (7.25, '4. Arrivée\nà temps'),
    (8.55, '5. Prise en\ncompte'),
]
w_col = 1.2

for xc, titre in cols:
    hdr = FancyBboxPatch((xc, 5.75), w_col, 0.78, boxstyle='round,pad=0.03,rounding_size=0.1',
                         fc='#eaeef3', ec='#4A5A6A', lw=1.0)
    ax.add_patch(hdr)
    ax.text(xc + w_col / 2, 6.14, titre, fontsize=6.9, fontweight='bold',
            color='#4A5A6A', ha='center', va='center')

# Rows: 3 levels
rows = [
    (4.25, 'Niveau 1 — Attitude\nindividuelle',
     'attente préalable, pré-mortem,\nmondes élargis', '#3A4BC8', '#eef2fb',
     ['direct', 'direct', 'partiel', 'none', 'none']),
    (2.75, 'Niveau 2 — Placement\ndes contrôles',
     'points de passage, couche dessous,\nancrage documentaire (RAG)', '#0A8273', '#e8f5f3',
     ['none', 'direct', 'direct', 'direct', 'partiel']),
    (1.25, 'Niveau 3 — Organisation\ncollective',
     'capacité nommée, statut affiché,\nhistorique, erreurs injectées', '#A8336E', '#faeef4',
     ['direct', 'direct', 'direct', 'none', 'direct']),
]

h_row = 1.18
for yr, titre, sub, col_ec, col_fc, cov in rows:
    # Row label box
    rb = FancyBboxPatch((0.15, yr), 3.0, h_row, boxstyle='round,pad=0.04,rounding_size=0.1',
                        fc=col_fc, ec=col_ec, lw=1.1)
    ax.add_patch(rb)
    ax.text(1.65, yr + h_row - 0.34, titre, fontsize=7.2, fontweight='bold',
            color=col_ec, ha='center', va='center')
    ax.text(1.65, yr + 0.28, sub, fontsize=6.1, color=ENCRE2, ha='center', va='center')

    # Coverage cells
    for (xc, _), status in zip(cols, cov):
        cell_fc = col_fc if status == 'direct' else ('#f7f6f2' if status == 'partiel' else 'white')
        cell_ec = col_ec if status == 'direct' else (MUET if status == 'partiel' else '#e4e3df')
        cb = FancyBboxPatch((xc, yr), w_col, h_row, boxstyle='round,pad=0.03,rounding_size=0.08',
                            fc=cell_fc, ec=cell_ec, lw=0.9)
        ax.add_patch(cb)
        if status == 'direct':
            ax.text(xc + w_col / 2, yr + h_row / 2 + 0.12, '●', fontsize=12, color=col_ec, ha='center', va='center')
            ax.text(xc + w_col / 2, yr + 0.26, 'appui direct', fontsize=6.0, color=col_ec, ha='center', va='center')
        elif status == 'partiel':
            ax.text(xc + w_col / 2, yr + h_row / 2 + 0.12, '◐', fontsize=11, color=ENCRE2, ha='center', va='center')
            ax.text(xc + w_col / 2, yr + 0.26, 'appui partiel', fontsize=6.0, color=ENCRE2, ha='center', va='center')
        else:
            ax.text(xc + w_col / 2, yr + h_row / 2, '—', fontsize=10, color=MUET, ha='center', va='center')

# Bottom transverse bar: Historical track record & seeded errors measure the whole chain
trans = FancyBboxPatch((3.35, 0.15), 6.4, 0.82, boxstyle='round,pad=0.04,rounding_size=0.1',
                       fc='#fdf0ea', ec='#A35F00', lw=1.0, ls='--')
ax.add_patch(trans)
ax.text(6.55, 0.56,
        'Historique et erreurs injectées (niveau 3) :\nmesurent l’échappement effectif de l’ensemble des cinq portes',
        fontsize=6.7, fontweight='bold', color='#A35F00', ha='center', va='center', linespacing=1.3)

ax.text(1.65, 0.58, 'Aucun niveau isolé ne\ncouvre les cinq conditions.',
        fontsize=6.9, color=ENCRE2, style='italic', ha='center', va='center')

fig.tight_layout()
sauver(fig, 'ch18-trois-niveaux')
