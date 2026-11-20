"""ch06-cinq-conditions (ch. 6): five gates a disagreement signal must pass between claim and action.

Outputs: figures/ch06-cinq-conditions.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 3.7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.4)
ax.axis('off')

# Left box: False claim
claim_box = FancyBboxPatch((0.1, 2.35), 1.25, 1.6, boxstyle='round,pad=0.04,rounding_size=0.12',
                           fc='#fdf0ea', ec='#A35F00', lw=1.2)
ax.add_patch(claim_box)
ax.text(0.72, 3.15, 'Affirmation\nfausse\n(classe $E_k$)', fontsize=7.0, fontweight='bold',
        color='#A35F00', ha='center', va='center')

# Right top box: Error stopped
stop_box = FancyBboxPatch((8.58, 4.25), 1.32, 1.25, boxstyle='round,pad=0.04,rounding_size=0.12',
                          fc='#e8f5f3', ec='#0A8273', lw=1.2)
ax.add_patch(stop_box)
ax.text(9.24, 4.87, 'Erreur\narrêtée\navant l’acte', fontsize=7.1, fontweight='bold',
        color='#0A8273', ha='center', va='center')

# Right bottom box: Action reached unchecked
act_box = FancyBboxPatch((8.58, 0.85), 1.32, 1.25, boxstyle='round,pad=0.04,rounding_size=0.12',
                         fc='#faeef4', ec='#A8336E', lw=1.2)
ax.add_patch(act_box)
ax.text(9.24, 1.47, 'Action\nengagée\n(échappement)', fontsize=7.0, fontweight='bold',
        color='#A8336E', ha='center', va='center')

# Five gates in the middle
gates = [
    ('1. Existence', 'comparateur\ndisponible'),
    ('2. Différence', 'se tromper\nautrement'),
    ('3. Compara-\nbilité', 'grandeurs et\nconditions'),
    ('4. À temps', 'avant l’acte\nirréversible'),
    ('5. Prise en\ncompte', 'reçu + droit\nd’agir'),
]

x_positions = [1.65, 3.02, 4.39, 5.76, 7.13]
w_gate = 1.18

# Top path: all 5 gates open -> green line straight through
ax.plot([1.38, 8.53], [4.87, 4.87], color='#0A8273', lw=1.7, zorder=1)
ax.annotate('', xy=(8.55, 4.87), xytext=(8.25, 4.87),
            arrowprops=dict(arrowstyle='->', color='#0A8273', lw=1.7))
ax.text(4.95, 5.9, 'Toutes les portes sont ouvertes : le signal de désaccord franchit le contrôle',
        fontsize=7.6, fontweight='bold', color='#0A8273', ha='center', va='center')

# Bottom path: blocked at gate 3 (illustrative) -> escapes to action
x_block = x_positions[2] + w_gate / 2
ax.plot([1.38, x_block], [1.9, 1.9], color='#A8336E', lw=1.4, ls='--', zorder=1)
ax.plot([x_block, 8.53], [1.47, 1.47], color='#A8336E', lw=1.7, zorder=1)
ax.annotate('', xy=(8.55, 1.47), xytext=(8.25, 1.47),
            arrowprops=dict(arrowstyle='->', color='#A8336E', lw=1.7))
# Connector from claim to both tracks
ax.plot([1.38, 1.38], [1.9, 4.87], color=ENCRE2, lw=1.0)

for idx, (xg, (titre, sub)) in enumerate(zip(x_positions, gates)):
    col_ec = '#A8336E' if idx == 2 else '#3A4BC8'
    col_fc = '#faeef4' if idx == 2 else '#eef2fb'
    g = FancyBboxPatch((xg, 2.38), w_gate, 1.88, boxstyle='round,pad=0.03,rounding_size=0.1',
                       fc=col_fc, ec=col_ec, lw=1.0, zorder=2)
    ax.add_patch(g)
    ax.text(xg + w_gate / 2, 3.72, titre, fontsize=6.6, fontweight='bold', color=col_ec, ha='center', va='center')
    ax.text(xg + w_gate / 2, 2.86, sub, fontsize=6.2, color=ENCRE2, ha='center', va='center')

    ax.plot([xg + w_gate / 2], [4.87], 'o', color='#0A8273', mec='white', mew=1.0, ms=6, zorder=3)

    if idx == 2:
        ax.plot([xg + w_gate / 2 - 0.16, xg + w_gate / 2 + 0.16], [1.74, 2.06], color='#A8336E', lw=2.0, zorder=4)
        ax.plot([xg + w_gate / 2 - 0.16, xg + w_gate / 2 + 0.16], [2.06, 1.74], color='#A8336E', lw=2.0, zorder=4)

ax.text(4.95, 0.35,
        'Qu’une seule porte reste fermée (ici, à titre d’exemple, la comparabilité) : l’erreur passe avec échappement = 100 %.',
        fontsize=7.2, color='#A8336E', style='italic', ha='center', va='center')

fig.tight_layout()
sauver(fig, 'ch06-cinq-conditions')
