"""ch05-ferrure-marge (ch. 5): mechanical bracket safety factor 1.8 vs omitted corrosion.

Outputs: figures/ch05-ferrure-marge.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, MUET, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 3.1))
ax.set_xlim(0, 2.25)
ax.set_ylim(-0.35, 2.35)

# Reference vertical line: nominal load = 1.0
ax.axvline(1.0, color='#4A5A6A', lw=1.3, ls='--')
ax.text(1.0, 2.18, 'Charge nominale (1,0)', fontsize=8.0, fontweight='bold',
        color='#4A5A6A', ha='center', va='bottom')

# Reference vertical line: 1.8 safety factor
ax.axvline(1.8, color='#3A4BC8', lw=1.1, ls=':')
ax.text(1.8, 2.18, 'Dimensionnement × 1,8', fontsize=8.0, fontweight='bold',
        color='#3A4BC8', ha='center', va='bottom')

# Top bar: Inside the frame (dry air mechanical model)
y_top = 1.32
h = 0.48
ax.barh(y_top, 1.0, height=h, color='#eaeef3', edgecolor='#4A5A6A', lw=0.9)
ax.barh(y_top, 0.42, left=1.0, height=h, color='#e8f5f3', edgecolor='#0A8273', lw=0.9)
ax.barh(y_top, 0.38, left=1.42, height=h, color='#eef2fb', edgecolor='#3A4BC8', lw=0.9)

ax.text(0.5, y_top, 'Capacité requise\n(charge nominale)', ha='center', va='center', fontsize=7.2, color=ENCRE)
ax.text(1.21, y_top, 'Aléatoire\n(alliage)', ha='center', va='center', fontsize=6.7, color='#0A8273')
ax.text(1.61, y_top, 'Épistémique\n(efforts)', ha='center', va='center', fontsize=6.7, color='#3A4BC8')

# Bracket / brace text above top bar
ax.annotate('', xy=(1.8, 1.87), xytext=(1.0, 1.87),
            arrowprops=dict(arrowstyle='<->', color='#3A4BC8', lw=1.0))
ax.text(1.4, 1.92, 'marge de sécurité dans le cadre', fontsize=7.2, color='#3A4BC8', ha='center', va='bottom')

# Bottom bar: Reality in corrosive marine atmosphere (omitted mechanism z)
y_bot = 0.35
ax.barh(y_bot, 0.72, height=h, color='#faeef4', edgecolor='#A8336E', lw=1.0)
ax.barh(y_bot, 1.08, left=0.72, height=h, color='#fdf0ea', edgecolor='#A35F00', lw=0.9, ls='--', hatch='///')
ax.text(0.36, y_bot, 'Capacité réelle\nen service', ha='center', va='center', fontsize=7.2, fontweight='bold', color='#A8336E')
ax.text(1.26, y_bot, 'Perte hors modèle :\ncorrosion par piqûres / sous contrainte',
        ha='center', va='center', fontsize=6.9, color='#A35F00',
        bbox=dict(boxstyle='round,pad=0.18', fc='#fdf0ea', ec='none'))

ax.text(1.12, -0.18,
        'La marge de 1,8 protège contre les écarts modélisés ; elle est aveugle à un mécanisme absent du cadre.',
        fontsize=7.3, color=ENCRE2, style='italic', ha='center', va='center')

ax.set_yticks([y_bot, y_top], ['Réalité\n(air marin corrosif)', 'Modèle mécanique\n(air sec, dans le cadre)'], fontsize=8.0)
ax.set_xticks([0, 0.5, 1.0, 1.5, 1.8, 2.0])
ax.set_xticklabels(['0', '0,5', '1,0', '1,5', '1,8', '2,0'], fontsize=7.8)
ax.set_xlabel('résistance rapportée à la charge nominale', fontsize=8.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', visible=False)
ax.tick_params(axis='y', length=0)

fig.tight_layout()
sauver(fig, 'ch05-ferrure-marge')
