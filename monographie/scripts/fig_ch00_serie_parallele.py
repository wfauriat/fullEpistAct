"""ch00-serie-parallele (ch. 0): series chain vs parallel cross-check conceptual diagram.

Outputs: figures/ch00-serie-parallele.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, LARGEUR, debut, plt, sauver

debut(__file__)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(LARGEUR, 4.0), gridspec_kw={'height_ratios': [1.05, 1.25]})

for ax in (ax1, ax2):
    ax.set_xlim(0, 10)
    ax.axis('off')

# ------------------------------------------------------------------ Panel 1: Series (Chain)
ax1.set_ylim(0, 3.3)
ax1.text(0.15, 3.02, '(a) Composition en série (chaîne) — les angles morts s’additionnent',
         fontsize=8.8, fontweight='bold', color=ENCRE, va='center')

boxes_s = [
    (0.25, 1.05, 1.25, 0.92, 'Entrée', '#f4f4f2', ENCRE2),
    (2.1, 1.05, 1.72, 0.92, 'Maillon 1\n(angle mort 1)', '#fdf0ea', '#A35F00'),
    (4.42, 1.05, 1.72, 0.92, 'Maillon 2\n(angle mort 2)', '#fdf0ea', '#A35F00'),
    (6.74, 1.05, 1.72, 0.92, 'Maillon 3\n(angle mort 3)', '#fdf0ea', '#A35F00'),
    (8.95, 1.05, 0.85, 0.92, 'Action', '#eaeef3', '#4A5A6A'),
]
for x, y, w, h, txt, fc, ec in boxes_s:
    p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05,rounding_size=0.12',
                       fc=fc, ec=ec, lw=1.1)
    ax1.add_patch(p)
    ax1.text(x + w / 2, y + h / 2, txt, ha='center', va='center', fontsize=7.4, color=ENCRE)

arrows_s = [
    (1.55, 2.05, None),
    (3.87, 4.37, 'interface\n(blanchiment)'),
    (6.19, 6.69, 'interface\n(blanchiment)'),
    (8.51, 8.9, None),
]
for x0, x1, lbl in arrows_s:
    ax1.annotate('', xy=(x1, 1.51), xytext=(x0, 1.51),
                 arrowprops=dict(arrowstyle='->', color='#A35F00', lw=1.2))
    if lbl:
        ax1.text((x0 + x1) / 2, 2.12, lbl, ha='center', va='bottom', fontsize=6.7, color='#A35F00', style='italic')

p_sum1 = FancyBboxPatch((0.25, 0.12), 9.55, 0.62, boxstyle='round,pad=0.04,rounding_size=0.1',
                        fc='#fdf0ea', ec='#A35F00', lw=0.8, ls='--')
ax1.add_patch(p_sum1)
ax1.text(5.02, 0.43,
         'Angle mort global = réunion des angles morts de chaque maillon + erreurs nées aux interfaces',
         ha='center', va='center', fontsize=7.1, color='#A35F00')

# ------------------------------------------------------------------ Panel 2: Parallel (Cross-check)
ax2.set_ylim(0, 3.85)
ax2.text(0.15, 3.55, '(b) Composition en parallèle (contrôle croisé) — seul l’angle mort commun subsiste',
         fontsize=8.8, fontweight='bold', color=ENCRE, va='center')

boxes_p = [
    (0.25, 1.55, 1.4, 0.9, 'Même\nquestion', '#f4f4f2', ENCRE2),
    (2.35, 2.25, 2.55, 0.85, 'Producteur\n(angle mort 1)', '#eef2fb', '#3A4BC8'),
    (2.35, 0.95, 2.55, 0.85, 'Contrôleur\n(angle mort 2, différent)', '#e8f5f3', '#0A8273'),
    (5.6, 1.55, 1.75, 0.9, 'Comparaison\ndes réponses', '#f4f4f2', '#4A5A6A'),
    (8.05, 2.25, 1.75, 0.78, 'Accord\n→ Action', '#e8f5f3', '#0A8273'),
    (8.05, 0.98, 1.75, 0.78, 'Désaccord\n→ Arrêt / examen', '#faeef4', '#A8336E'),
]
for x, y, w, h, txt, fc, ec in boxes_p:
    p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05,rounding_size=0.12',
                       fc=fc, ec=ec, lw=1.1)
    ax2.add_patch(p)
    ax2.text(x + w / 2, y + h / 2, txt, ha='center', va='center', fontsize=7.3, color=ENCRE)

ax2.annotate('', xy=(2.3, 2.67), xytext=(1.7, 2.1),
             arrowprops=dict(arrowstyle='->', color='#3A4BC8', lw=1.2))
ax2.annotate('', xy=(2.3, 1.37), xytext=(1.7, 1.9),
             arrowprops=dict(arrowstyle='->', color='#0A8273', lw=1.2))
ax2.annotate('', xy=(5.55, 2.12), xytext=(4.95, 2.65),
             arrowprops=dict(arrowstyle='->', color='#3A4BC8', lw=1.2))
ax2.annotate('', xy=(5.55, 1.88), xytext=(4.95, 1.38),
             arrowprops=dict(arrowstyle='->', color='#0A8273', lw=1.2))
ax2.annotate('', xy=(8.0, 2.62), xytext=(7.4, 2.12),
             arrowprops=dict(arrowstyle='->', color='#0A8273', lw=1.2))
ax2.annotate('', xy=(8.0, 1.38), xytext=(7.4, 1.88),
             arrowprops=dict(arrowstyle='->', color='#A8336E', lw=1.2))

p_sum2 = FancyBboxPatch((0.25, 0.08), 9.55, 0.62, boxstyle='round,pad=0.04,rounding_size=0.1',
                        fc='#e8f5f3', ec='#0A8273', lw=0.8, ls='--')
ax2.add_patch(p_sum2)
ax2.text(5.02, 0.39,
         'Angle mort résiduel = intersection des seuls angles morts partagés (comparaison et prise en compte)',
         ha='center', va='center', fontsize=6.5, color='#0A8273')

fig.tight_layout(h_pad=0.4)
sauver(fig, 'ch00-serie-parallele')
