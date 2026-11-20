"""ch00-carte-ouvrage (ch. 0): synoptic map of the five parts and the argument steps.

Outputs: figures/ch00-carte-ouvrage.{pdf,svg}
"""
from matplotlib.patches import FancyBboxPatch
from _style import ENCRE, ENCRE2, LARGEUR, debut, plt, sauver

debut(__file__)

fig, ax = plt.subplots(figsize=(LARGEUR, 5.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10.6)
ax.axis('off')

PARTIES = [
    (
        8.6, 1.75,
        'Partie I — Agir d’après une représentation (chapitres 1 à 4)',
        '#4A5A6A', '#eaeef3',
        [
            ('Ch. 1', 'Logique, conditionnement,\ncotes de Bayes, surprise'),
            ('Ch. 2', 'Monde et représentation,\ncadre et arrière-plan (…)'),
            ('Ch. 3', 'Mondes possibles,\nraisonner à l’envers'),
            ('Ch. 4', 'Décision unique (UES)\net seuil p∗'),
        ],
    ),
    (
        6.5, 1.8,
        'Partie II — Ce qui peut nous détromper (chapitres 5 à 9, propositions 1 à 5)',
        '#3A4BC8', '#eef2fb',
        [
            ('Ch. 5 (P1)', '3 incertitudes ;\nbarre = désaccord'),
            ('Ch. 6 (P2)', 'Comparateur et\n5 conditions'),
            ('Ch. 7 (P3, M3)', 'Cadre : cause\ncommune'),
            ('Ch. 8 (P4–5, M1)', 'Chaînes, croisés,\nblanchiment'),
            ('Ch. 9 (M1)', 'Sévérité, VPP,\néchappement'),
        ],
    ),
    (
        4.45, 1.75,
        'Partie III — De l’informatique classique à l’IA (chapitres 10 à 13)',
        '#0A8273', '#e8f5f3',
        [
            ('Ch. 10', 'Composants spécifiés,\ncontrats et adresse'),
            ('Ch. 11', 'Composants appris :\nportée contre garantie'),
            ('Ch. 12', 'Changement de régime,\nfrontière et longue traîne'),
            ('Ch. 13', 'Synthèse : deux axes\net quatre sources'),
        ],
    ),
    (
        2.45, 1.7,
        'Partie IV — L’automatisation et ses angles morts (chapitres 14 à 16)',
        '#A35F00', '#fdf0ea',
        [
            ('Ch. 14 (M1)', 'Chaînes et agents :\nl’erreur passe à l’acte'),
            ('Ch. 15', 'Érosion des contrôles humains,\nsignal coûteux et consigne'),
            ('Ch. 16 (M1)', 'Angles morts collectifs,\nmodèle partagé et provenance'),
        ],
    ),
    (
        0.35, 1.8,
        'Partie V — Décider et se prémunir (chapitres 17 et 18) & Conclusion',
        '#A8336E', '#faeef4',
        [
            ('Ch. 17 (M2)', 'Décisions sans appel : marge b,\nbacs à sable, verrous, 4 questions'),
            ('Ch. 18', 'Remède à 3 niveaux : attitude,\nplacement, organisation, 5 questions'),
            ('Conclusion', 'La méthode appliquée\nà l’ouvrage lui-même'),
        ],
    ),
]

for idx, (y0, h, titre, col_ec, col_fc, chaps) in enumerate(PARTIES):
    # Outer band
    band = FancyBboxPatch((0.15, y0), 9.7, h, boxstyle='round,pad=0.05,rounding_size=0.14',
                          fc=col_fc, ec=col_ec, lw=1.15)
    ax.add_patch(band)
    ax.text(0.35, y0 + h - 0.22, titre, fontsize=8.1, fontweight='bold', color=col_ec, va='center')

    n = len(chaps)
    margin_x = 0.3
    gap = 0.14
    avail_w = 9.7 - 2 * (margin_x - 0.15) - (n - 1) * gap
    w_box = avail_w / n
    y_box = y0 + 0.13
    h_box = h - 0.62

    for j, (ch_lbl, ch_txt) in enumerate(chaps):
        xb = margin_x + j * (w_box + gap)
        cb = FancyBboxPatch((xb, y_box), w_box, h_box, boxstyle='round,pad=0.04,rounding_size=0.09',
                            fc='white', ec=col_ec, lw=0.8)
        ax.add_patch(cb)
        ax.text(xb + w_box / 2, y_box + h_box - 0.22, ch_lbl,
                fontsize=7.3, fontweight='bold', color=col_ec, ha='center', va='center')
        ax.text(xb + w_box / 2, y_box + (h_box - 0.28) / 2, ch_txt,
                fontsize=6.8, color=ENCRE, ha='center', va='center')

    # Vertical arrow to next part
    if idx < len(PARTIES) - 1:
        y_next_top = PARTIES[idx + 1][0] + PARTIES[idx + 1][1]
        ax.annotate('', xy=(5.0, y_next_top + 0.04), xytext=(5.0, y0 - 0.04),
                    arrowprops=dict(arrowstyle='->', color=ENCRE2, lw=1.2))

fig.tight_layout()
sauver(fig, 'ch00-carte-ouvrage')
