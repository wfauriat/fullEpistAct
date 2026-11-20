"""bayes-cotes (ch. 1): updating odds with a likelihood ratio (ultrasonic weld inspection).

Outputs: figures/ch01-bayes-cotes.{pdf,svg}, tableaux/ch01-bayes-cotes.md
"""
import numpy as np
from _style import (BLEU, ENCRE, ENCRE2, NEUTRE, LARGEUR, PCT_AXE,
                    debut, pct, pct_in, sig, plt, sauver, tableau)

debut(__file__)

# Probe characteristics on calibration pieces
P_POS_DEFAUT = 0.75   # Pr(T+ | D)
P_NEG_DEFAUT = 0.25   # Pr(T- | D)
P_POS_SAIN = 0.15     # Pr(T+ | ~D)
P_NEG_SAIN = 0.85     # Pr(T- | ~D)

LR_POS = P_POS_DEFAUT / P_POS_SAIN        # 5
LR_NEG = P_NEG_DEFAUT / P_NEG_SAIN        # 5/17 ≈ 0.294

SITUATIONS = [
    ('Lot courant, signal anormal', 'Lot courant,\nsignal anormal', 0.04, LR_POS),
    ('Zone suspecte, signal anormal', 'Zone suspecte,\nsignal anormal', 0.20, LR_POS),
    ('Zone suspecte, signal normal', 'Zone suspecte,\nsignal normal', 0.20, LR_NEG),
    ('Zone suspecte, deux signaux anormaux indépendants',
     'Zone suspecte,\n2 signaux anormaux', 0.20, LR_POS ** 2),
]


def reviser(p_priori, lr):
    cote_priori = p_priori / (1.0 - p_priori)
    cote_post = cote_priori * lr
    p_post = cote_post / (1.0 + cote_post)
    return cote_priori, cote_post, p_post


fig, ax = plt.subplots(figsize=(LARGEUR, 3.2))
y = np.arange(len(SITUATIONS))[::-1]
h = 0.34

for idx, (yi, (_, lab_court, p0, lr)) in enumerate(zip(y, SITUATIONS)):
    c0, c1, p1 = reviser(p0, lr)
    ax.barh(yi + h / 2 + 0.02, 100 * p0, h, color=NEUTRE,
            label='probabilité a priori' if idx == 0 else None)
    ax.barh(yi - h / 2 - 0.02, 100 * p1, h, color=BLEU,
            label='probabilité a posteriori' if idx == 0 else None)
    ax.text(100 * p0 + 1.2, yi + h / 2 + 0.02, pct_in(p0), va='center', fontsize=8, color=ENCRE2)
    lr_str = f'× {sig(lr, 3)}' if lr < 1 else f'× {int(round(lr))}'
    ax.text(100 * p1 + 1.2, yi - h / 2 - 0.02, f'{pct(p1)}  (cote {lr_str})',
            va='center', fontsize=8, color=ENCRE)

ax.axvline(50, color=ENCRE2, lw=0.8, ls=(0, (4, 3)))
ax.text(49.0, y[0] + 0.44, 'une chance sur deux (50 %)', fontsize=7.8, color=ENCRE2, ha='right', va='bottom')

ax.set_yticks(y, [s[1] for s in SITUATIONS], fontsize=8.2)
ax.set_xlim(0, 114)
ax.set_ylim(-0.55, 3.65)
ax.xaxis.set_major_formatter(PCT_AXE)
ax.set_xlabel('probabilité que la soudure présente un défaut')
ax.grid(axis='y', visible=False)
ax.tick_params(axis='y', length=0)
ax.legend(loc='upper right', fontsize=8)
fig.tight_layout()
sauver(fig, 'ch01-bayes-cotes')

rows = []
for lab_long, _, p0, lr in SITUATIONS:
    c0, c1, p1 = reviser(p0, lr)
    c0_str = '0,25' if abs(c0 - 0.25) < 1e-9 else sig(c0, 3)
    lr_str = str(int(round(lr))) if abs(lr - round(lr)) < 1e-9 else sig(lr, 3)
    c1_str = sig(c1, 3)
    rows.append([lab_long, pct_in(p0), c0_str, lr_str, c1_str, pct(p1)])

tableau(
    'ch01-bayes-cotes',
    ['Situation', 'Probabilité a priori', 'Cote a priori', 'Rapport de vraisemblance',
     'Cote a posteriori', 'Probabilité a posteriori'],
    rows,
    'Révision par cotes de la probabilité de défaut d’une soudure. La sonde émet un signal anormal '
    'dans 75 % des cas en présence d’un défaut (normal dans 25 %), et dans 15 % des cas sur une '
    'soudure saine (normal dans 85 %).',
    ['l', 'r', 'r', 'r', 'r', 'r'],
)
