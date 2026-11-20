"""ch13-deux-axes (ch. 13): two-axis error matrix (cause location vs comparator response).

Outputs: figures/ch13-deux-axes.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, MUET, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 4.35))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.6)
ax.axis('off')

# Column headers
ax.text(3.7, 7.22, 'Erreur signalée\n(un comparateur contredit)',
        fontsize=8.1, fontweight='bold', color='#0A8273', ha='center', va='center')
ax.text(7.65, 7.22, 'Erreur silencieuse\n(rien ne contredit — défaillances lourdes)',
        fontsize=8.1, fontweight='bold', color='#A8336E', ha='center', va='center')

# Row headers (rotated / left column)
ax.text(0.85, 5.15, 'Cause\ndans le cadre',
        fontsize=8.0, fontweight='bold', color='#3A4BC8', ha='center', va='center')
ax.text(0.85, 2.2, 'Cause\nhors du cadre',
        fontsize=8.0, fontweight='bold', color='#A35F00', ha='center', va='center')

# Cells: (x, y, w, h, fc, ec, title, bullets)
cells = [
    (1.85, 3.9, 3.45, 2.48, '#e8f5f3', '#0A8273',
     'Dans le cadre · Signalée',
     '• test qui échoue, violation de contrat\n• plantage net, erreur de type\n• réponses dispersées sur devinette'),
    (6.1, 3.9, 3.7, 2.48, '#faeef4', '#A8336E',
     'Dans le cadre · Silencieuse',
     '• réponse fluide et fausse (Mata v. Avianca)\n• erreur constante, omission de saillance\n• chaîne blanchie (MCO)\n→ peuplée par les composants appris ;\n   vidable à l’avance si spécifié'),
    (1.85, 0.95, 3.45, 2.48, '#eef2fb', '#3A4BC8',
     'Hors du cadre · Signalée',
     '• anomalie remarquée sur le terrain\n• objection d’un tiers (chimiste)\n• eau qui bout vers 85 °C (mont Blanc)\n• alerte de dérive (Google Flu Trends)'),
    (6.1, 0.95, 3.7, 2.48, '#fdf0ea', '#A35F00',
     'Hors du cadre · Silencieuse',
     '• dernier matin de la dinde\n• scénario omis de Θ (crise 2008,\n  corrosion marine avant rupture)'),
]

for x, y, w, h, fc, ec, titre, body in cells:
    b = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05,rounding_size=0.14',
                       fc=fc, ec=ec, lw=1.2)
    ax.add_patch(b)
    ax.text(x + 0.14, y + h - 0.27, titre, fontsize=7.5, fontweight='bold', color=ec, va='center')
    ax.text(x + 0.14, y + h - 0.54, body, fontsize=6.4, color=ENCRE, va='top', linespacing=1.35)

# Horizontal arrows right -> left on both rows (strictly in the gap 5.35 .. 6.05)
for y_arr in (5.14, 2.19):
    ax.annotate('', xy=(5.38, y_arr), xytext=(6.02, y_arr),
                arrowprops=dict(arrowstyle='->', color='#0A8273', lw=2.2))

ax.text(5.82, 6.64, '← Ajouter des comparateurs qui se trompent autrement (change la colonne)',
        fontsize=7.1, fontweight='bold', color='#0A8273', ha='center', va='center')

# Blocked vertical arrow between rows
ax.plot([7.75, 7.75], [3.5, 3.85], color='#A8336E', lw=1.5, ls=':')
ax.plot([7.62, 7.88], [3.57, 3.77], color='#A8336E', lw=1.8)
ax.plot([7.62, 7.88], [3.77, 3.57], color='#A8336E', lw=1.8)

ax.text(5.8, 0.35,
        'Aucune méthode purement interne au cadre ne déplace une cause omise de la ligne du bas vers celle du haut.',
        fontsize=7.1, color='#A35F00', style='italic', ha='center', va='center')

fig.tight_layout()
sauver(fig, 'ch13-deux-axes')
