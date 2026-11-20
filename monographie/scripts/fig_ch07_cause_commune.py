"""ch07-cause-commune (ch. 7): causal DAG showing the frame as a common cause (model M3).

Outputs: figures/ch07-cause-commune.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, MUET, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 3.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.axis('off')

# Frame box (common cause container)
cadre = FancyBboxPatch((0.25, 2.25), 9.5, 3.7, boxstyle='round,pad=0.06,rounding_size=0.16',
                       fc='#eef2fb', ec='#3A4BC8', lw=1.25)
ax.add_patch(cadre)
ax.text(0.5, 5.65, 'À L’INTÉRIEUR DU CADRE (cause commune des contrôles internes)',
        fontsize=8.0, fontweight='bold', color='#3A4BC8', va='center')

# Node x: represented variables
nx = FancyBboxPatch((0.65, 3.2), 2.15, 1.4, boxstyle='round,pad=0.05,rounding_size=0.12',
                    fc='white', ec='#3A4BC8', lw=1.1)
ax.add_patch(nx)
ax.text(1.72, 3.9, 'Variables\nreprésentées $x$', fontsize=8.0, fontweight='bold',
        color='#3A4BC8', ha='center', va='center')

# Node f1(x): Claim
nf1 = FancyBboxPatch((3.85, 4.15), 2.15, 1.05, boxstyle='round,pad=0.05,rounding_size=0.12',
                     fc='white', ec='#4A5A6A', lw=1.1)
ax.add_patch(nf1)
ax.text(4.92, 4.67, 'Affirmation\n$f_1(x)$', fontsize=7.8, fontweight='bold',
        color=ENCRE, ha='center', va='center')

# Node f2(x): Internal comparator
nf2 = FancyBboxPatch((3.85, 2.6), 2.15, 1.05, boxstyle='round,pad=0.05,rounding_size=0.12',
                     fc='white', ec='#4A5A6A', lw=1.1)
ax.add_patch(nf2)
ax.text(4.92, 3.12, 'Comparateur interne\n$f_2(x)$', fontsize=7.8, fontweight='bold',
        color=ENCRE, ha='center', va='center')

# Agreement A
na = FancyBboxPatch((6.95, 3.35), 2.45, 1.15, boxstyle='round,pad=0.05,rounding_size=0.12',
                    fc='#e8f5f3', ec='#0A8273', lw=1.1)
ax.add_patch(na)
ax.text(8.17, 3.92, 'Accord interne $A$\n($f_1(x) \\approx f_2(x)$)', fontsize=7.6, fontweight='bold',
        color='#0A8273', ha='center', va='center')

# Outside the frame: omitted factor z and real outcome g(x, z)
nz = FancyBboxPatch((0.65, 0.4), 2.15, 1.2, boxstyle='round,pad=0.05,rounding_size=0.12',
                    fc='#fdf0ea', ec='#A35F00', lw=1.2, ls='--')
ax.add_patch(nz)
ax.text(1.72, 1.0, 'Facteur omis $z$\n(hors du cadre)', fontsize=7.8, fontweight='bold',
        color='#A35F00', ha='center', va='center')

ng = FancyBboxPatch((3.85, 0.4), 2.15, 1.2, boxstyle='round,pad=0.05,rounding_size=0.12',
                    fc='#faeef4', ec='#A8336E', lw=1.2)
ax.add_patch(ng)
ax.text(4.92, 1.0, 'Issue réelle\n$g(x, z)$', fontsize=7.8, fontweight='bold',
        color='#A8336E', ha='center', va='center')

ne = FancyBboxPatch((6.95, 0.4), 2.45, 1.2, boxstyle='round,pad=0.05,rounding_size=0.12',
                    fc='#faeef4', ec='#A8336E', lw=1.1)
ax.add_patch(ne)
ax.text(8.17, 1.0, 'Erreur réelle\n$e(x,z) = g(x,z) - f_1(x)$', fontsize=7.3, fontweight='bold',
        color='#A8336E', ha='center', va='center')

# Arrows inside frame
ax.annotate('', xy=(3.8, 4.65), xytext=(2.85, 4.15),
            arrowprops=dict(arrowstyle='->', color='#3A4BC8', lw=1.3))
ax.annotate('', xy=(3.8, 3.15), xytext=(2.85, 3.65),
            arrowprops=dict(arrowstyle='->', color='#3A4BC8', lw=1.3))
ax.annotate('', xy=(6.9, 4.1), xytext=(6.05, 4.6),
            arrowprops=dict(arrowstyle='->', color='#0A8273', lw=1.2))
ax.annotate('', xy=(6.9, 3.75), xytext=(6.05, 3.18),
            arrowprops=dict(arrowstyle='->', color='#0A8273', lw=1.2))

# Arrow x -> g(x, z)
ax.annotate('', xy=(3.82, 1.25), xytext=(2.4, 3.15),
            arrowprops=dict(arrowstyle='->', color='#3A4BC8', lw=1.2))

# Arrow z -> g(x, z) ONLY
ax.annotate('', xy=(3.8, 1.0), xytext=(2.85, 1.0),
            arrowprops=dict(arrowstyle='->', color='#A35F00', lw=1.4))

# Arrow g(x, z) -> e(x, z)
ax.annotate('', xy=(6.9, 1.0), xytext=(6.05, 1.0),
            arrowprops=dict(arrowstyle='->', color='#A8336E', lw=1.2))

# Dashed independence separator between A and e(x, z)
ax.plot([8.17, 8.17], [1.68, 3.28], color=MUET, lw=1.0, ls=':')
ax.text(8.17, 2.02, r'sachant $x$, $A \perp z$' + '\n' + r'$\Lambda(A \mid X = x) = 1$',
        fontsize=7.0, color=ENCRE2, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.18', fc='white', ec=MUET, lw=0.7))

fig.tight_layout()
sauver(fig, 'ch07-cause-commune')
