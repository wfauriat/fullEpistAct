"""ch05-trois-incertitudes (ch. 5): aleatory, epistemic, and ontological uncertainty vs frame and Theta.

Outputs: figures/ch05-trois-incertitudes.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 3.7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.4)
ax.axis('off')

# Outer open region: Ontological uncertainty (outside the frame)
outer = FancyBboxPatch((0.2, 0.25), 9.6, 5.9, boxstyle='round,pad=0.06,rounding_size=0.18',
                       fc='#fdf0ea', ec='#A35F00', lw=1.1, ls='--')
ax.add_patch(outer)
ax.text(5.0, 5.88, 'HORS DU CADRE — INCERTITUDE ONTOLOGIQUE',
        fontsize=8.3, fontweight='bold', color='#A35F00', ha='center', va='center')
ax.text(5.0, 5.48, 'Arrière-plan tacite (…) : variables non retenues, catégories absentes, mécanismes omis (z)',
        fontsize=7.3, color='#A35F00', ha='center', va='center')
ax.text(5.0, 0.52, 'Une alternative absente de Θ reçoit un poids nul : elle ne produit aucun désaccord dans les barres d’erreur.',
        fontsize=7.2, color='#A35F00', ha='center', va='center', style='italic')

# Middle box: The Frame (Cadre)
cadre = FancyBboxPatch((0.65, 0.95), 8.7, 4.18, boxstyle='round,pad=0.05,rounding_size=0.15',
                       fc='#eef2fb', ec='#3A4BC8', lw=1.3)
ax.add_patch(cadre)
ax.text(5.0, 4.86, 'CADRE CHOISI (variables X, catégories, classe de modèles, objectif)',
        fontsize=8.0, fontweight='bold', color='#3A4BC8', ha='center', va='center')

# Inner box: Admitted set Theta
theta_box = FancyBboxPatch((1.0, 1.2), 8.0, 3.35, boxstyle='round,pad=0.05,rounding_size=0.12',
                           fc='white', ec='#4A5A6A', lw=1.0)
ax.add_patch(theta_box)
ax.text(5.0, 4.28, 'Ensemble des alternatives admises Θ',
        fontsize=8.0, fontweight='bold', color='#4A5A6A', ha='center', va='center')

# Three admitted alternatives theta_1, theta_2, theta_3
alts = [
    (1.3, 1.9, 'Alternative θ₁', 'dispersion\naléatoire'),
    (3.9, 1.9, 'Alternative θ₂', 'dispersion\naléatoire'),
    (6.5, 1.9, 'Alternative θ₃', 'dispersion\naléatoire'),
]
for x0, y0, title, sub in alts:
    b = FancyBboxPatch((x0, y0), 2.2, 1.55, boxstyle='round,pad=0.04,rounding_size=0.1',
                       fc='#e8f5f3', ec='#0A8273', lw=1.0)
    ax.add_patch(b)
    ax.text(x0 + 1.1, y0 + 1.24, title, fontsize=7.6, fontweight='bold', color='#0A8273', ha='center', va='center')
    # Small bell-like / spread bar inside each theta
    ax.plot([x0 + 0.35, x0 + 1.85], [y0 + 0.72, y0 + 0.72], color='#0A8273', lw=1.8)
    ax.plot([x0 + 1.1], [y0 + 0.72], 'o', color='#0A8273', ms=5)
    ax.text(x0 + 1.1, y0 + 0.32, sub, fontsize=6.9, color=ENCRE2, ha='center', va='center')

# Epistemic uncertainty arrow between alternatives
ax.annotate('', xy=(6.4, 3.72), xytext=(3.6, 3.72),
            arrowprops=dict(arrowstyle='<->', color='#3A4BC8', lw=1.2))
ax.text(5.0, 3.84, r'Incertitude épistémique : désaccord entre $\theta \in \Theta$   $\mathrm{Var}_\theta(\mathbb{E}[Y \mid \theta])$',
        fontsize=7.3, fontweight='bold', color='#3A4BC8', ha='center', va='bottom')

# Aleatory uncertainty caption at bottom of Theta
ax.text(5.0, 1.46, r'Incertitude aléatoire : variabilité irréductible à l’intérieur de chaque $\theta$   $\mathbb{E}_\theta[\mathrm{Var}(Y \mid \theta)]$',
        fontsize=7.3, fontweight='bold', color='#0A8273', ha='center', va='center')

fig.tight_layout()
sauver(fig, 'ch05-trois-incertitudes')
