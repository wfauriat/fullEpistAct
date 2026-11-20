"""ch02-cible-monde-action (ch. 2): target, world, picture inside a finite frame, and action.

Outputs: figures/ch02-cible-monde-action.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, MUET, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 3.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.axis('off')

# Left side: The World (open, with hatched unrepresented background)
monde_outer = FancyBboxPatch((0.2, 0.45), 3.3, 5.2, boxstyle='round,pad=0.06,rounding_size=0.18',
                             fc='#f7f6f2', ec='#4A5A6A', lw=1.2)
ax.add_patch(monde_outer)
ax.text(1.85, 5.32, 'MONDE RÉEL', fontsize=8.6, fontweight='bold', color='#4A5A6A', ha='center', va='center')

# Measured / observed portion inside the world
monde_obs = FancyBboxPatch((0.42, 3.25), 2.86, 1.65, boxstyle='round,pad=0.04,rounding_size=0.12',
                           fc='white', ec='#4A5A6A', lw=0.9)
ax.add_patch(monde_obs)
ax.text(1.85, 4.07, 'Aspects observés et mesurés\n(grandeurs retenues X)',
        fontsize=7.3, color=ENCRE, ha='center', va='center')

# Unrepresented / tacit background inside the world (hatched)
monde_hors = FancyBboxPatch((0.42, 0.72), 2.86, 2.2, boxstyle='round,pad=0.04,rounding_size=0.12',
                            fc='#fdf0ea', ec='#A35F00', lw=0.9, ls='--', hatch='///')
monde_hors.set_edgecolor('#d8b08c')
ax.add_patch(monde_hors)
monde_hors_lbl = FancyBboxPatch((0.56, 1.05), 2.58, 1.54, boxstyle='round,pad=0.04,rounding_size=0.08',
                                fc='#fdf0ea', ec='#A35F00', lw=0.8)
ax.add_patch(monde_hors_lbl)
ax.text(1.85, 1.82, 'Hors du cadre\n(arrière-plan tacite (…) :\nfacteurs omis, couplages)',
        fontsize=7.0, color='#A35F00', ha='center', va='center')

# Top-right: Cible (Target)
cible_box = FancyBboxPatch((6.15, 4.75), 3.6, 0.9, boxstyle='round,pad=0.05,rounding_size=0.14',
                           fc='#e8f5f3', ec='#0A8273', lw=1.1)
ax.add_patch(cible_box)
ax.text(7.95, 5.2, 'CIBLE (état visé par celui qui agit)',
        fontsize=7.6, fontweight='bold', color='#0A8273', ha='center', va='center')

# Middle-right: Finite Frame containing the Representation
cadre_box = FancyBboxPatch((5.85, 2.35), 3.9, 1.95, boxstyle='round,pad=0.05,rounding_size=0.15',
                           fc='#eef2fb', ec='#3A4BC8', lw=1.3, ls='-')
ax.add_patch(cadre_box)
ax.text(7.8, 4.03, 'CADRE FINI (spécification choisie)',
        fontsize=7.6, fontweight='bold', color='#3A4BC8', ha='center', va='center')

repr_box = FancyBboxPatch((6.1, 2.55), 3.4, 1.22, boxstyle='round,pad=0.04,rounding_size=0.1',
                          fc='white', ec='#3A4BC8', lw=0.9)
ax.add_patch(repr_box)
ax.text(7.8, 3.16, 'REPRÉSENTATION\n(catégories, équations, probabilités)\nd’après laquelle on décide',
        fontsize=7.2, color=ENCRE, ha='center', va='center')

# Bottom-right: Action
action_box = FancyBboxPatch((6.15, 0.55), 3.6, 1.05, boxstyle='round,pad=0.05,rounding_size=0.14',
                            fc='#faeef4', ec='#A8336E', lw=1.2)
ax.add_patch(action_box)
ax.text(7.95, 1.07, 'ACTION ENGAGÉE\n(cap, dimensionnement, mise en service)',
        fontsize=7.1, fontweight='bold', color='#A8336E', ha='center', va='center')

# Arrows
# 1. Partial observations: Monde (observed) -> Représentation
ax.annotate('', xy=(5.8, 3.55), xytext=(3.35, 4.05),
            arrowprops=dict(arrowstyle='->', color='#3A4BC8', lw=1.3))
ax.text(4.65, 4.1, 'observations\npartielles', fontsize=7.2, color='#3A4BC8', ha='center', va='bottom')

# 2. Cible -> Cadre/Représentation (écart à réduire)
ax.annotate('', xy=(7.95, 4.33), xytext=(7.95, 4.72),
            arrowprops=dict(arrowstyle='->', color='#0A8273', lw=1.1))
ax.text(8.1, 4.52, 'objectif retenu', fontsize=7.0, color='#0A8273', ha='left', va='center')

# 3. Decision: Représentation -> Action
ax.annotate('', xy=(7.95, 1.65), xytext=(7.95, 2.32),
            arrowprops=dict(arrowstyle='->', color='#3A4BC8', lw=1.3))
ax.text(8.1, 1.98, 'décision', fontsize=7.4, color='#3A4BC8', ha='left', va='center', fontweight='bold')

# 4. Action -> Monde & Réponse du monde
ax.annotate('', xy=(3.55, 1.0), xytext=(6.1, 1.0),
            arrowprops=dict(arrowstyle='<->', color='#A8336E', lw=1.4))
ax.text(4.82, 1.16, 'le monde répond\nà l’action seule',
        fontsize=7.1, fontweight='bold', color='#A8336E', ha='center', va='bottom')

# 5. Blocked arrow: Représentation -x-> Réponse du monde
ax.annotate('', xy=(4.45, 2.32), xytext=(5.8, 2.85),
            arrowprops=dict(arrowstyle='->', color=MUET, lw=0.9, ls=':'))
ax.text(4.82, 2.75, 'aucune prise directe', fontsize=6.7, color=ENCRE2, style='italic', ha='center')

fig.tight_layout()
sauver(fig, 'ch02-cible-monde-action')
