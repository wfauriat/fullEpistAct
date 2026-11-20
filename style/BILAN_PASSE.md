# Bilan de la passe de style automatisée (2026-11-20)

**Fonctionnement :** Gemini a proposé les retouches. Chaque chapitre a ensuite été jugé par un agent Claude Opus neuf (`juge-style`, effort élevé), puis les retouches acceptées ont été appliquées par script. Un commit par chapitre sur la branche `style-pass`.

## Chiffres

| | Nombre |
| :--- | ---: |
| Retouches proposées et soumises au juge | 122 |
| **Appliquées** | **83** (68 %) |
| Rejetées par le juge (texte d’origine conservé) | 39 |
| Rejetées par les contrôles mécaniques | 0 |
| Retirées par le rédacteur (après un faux rejet dû à un défaut de l’outil, corrigé en `3940101`) | 2 |
| Rapports de portée : alertes ⛔ / ⚠ | 0 / 1 (ch. 14, retrait d’une formule creuse vérifié par le juge) |
| `make verifier` après chaque chapitre | 0 erreur |

Le diff complet tient en **81 lignes modifiées** sur 19 fichiers (`git diff main..style-pass -- monographie/chapitres/`). Deux chapitres n’ont pas changé :
- ch. 1 : aucune retouche proposée ;
- conclusion : son unique retouche a été rejetée.

## Effet mesuré (`style/audit_style.py`, texte principal)

| | Avant | Après |
| :--- | ---: | ---: |
| Longueur moyenne des phrases | 27,4 mots | 26,7 mots |
| Deux-points / 1 000 mots | 10,3 | 9,7 |
| Phrases ≤ 10 mots | 9,1 % | 9,2 % |

**Part des phrases de 35 mots ou plus,** sur les chapitres les plus touchés :

| Chapitre | Avant | Après |
| :--- | ---: | ---: |
| Ch. 6 | 30,8 % | 23,2 % |
| Ch. 15 | 37,6 % | 30,3 % |
| Ch. 16 | 37,5 % | 33,3 % |
| Avant-propos | 39,0 % | 33,9 % |
| Ch. 0 | 36,0 % | 32,0 % |

**Une passe conservatrice, comme prévu.** Les retouches sont presque toutes des coupes de phrases longues, des « Or » initiaux retirés et des italiques d’emphase supprimées. Les repères indicatifs de la spécification (22 à 25 mots de moyenne) ne sont pas atteints : le rédacteur a peu proposé, environ deux retouches pour mille mots, et le juge a écarté un tiers des propositions.

## Ce que le juge a rejeté

Aucun rejet ne concernait un fait, un chiffre ou un terme du registre. Le rédacteur n’en a d’ailleurs presque pas touché. Les rejets se répartissent ainsi :

1. **Connecteur ajouté qui change le lien logique** (« ainsi », « en effet », « car », « pourtant », « dès lors ») : environ la moitié des rejets. Un deux-points qui introduisait une conclusion devient une justification ; une précision devient une conséquence.
2. **« Or » de raisonnement remplacé par « Mais » ou « pourtant »** : environ un quart des rejets. Dans ces passages, « Or » introduisait une prémisse, pas une opposition.
3. **Coupe qui fait sortir une phrase de sa condition :** ch. 13 (point clé) et ch. 16 (« tant que les paramètres du contrôleur restent inchangés »).
4. **Français :** « Car » en tête de phrase, « mais » répétés, adverbe mal placé.

## Pour la relecture finale

- **Par chapitre :** `style/lots/<chapitre>/journal.md` donne les retouches appliquées (avant et après) et les rejets motivés. `rapport_portee.md` relève les changements les plus sensibles.
- **Points signalés par les juges :**
  - ch. 6, ligne 129 : l’italique de « *au moins l’un des deux termes est faux* » n’a plus son pendant, l’italique ayant été retirée de « il ne prouve rien » ;
  - ch. 14 : retrait de « Il serait toutefois inexact d’affirmer que… », devenu « Tout pipeline n’est toutefois pas condamné… », à relire.
- **Revenir au texte d’origine d’un chapitre :** `git checkout main -- monographie/chapitres/<chapitre>.md`.

## Si une seconde passe est envisagée

Le pipeline peut être relancé sur le texte retouché. Il faudrait alors :

1. nommer les lots d’une seconde passe à part, par exemple `style/lots/p2-<chapitre>/`, ce qui demande une petite adaptation de `veilleur.py` ;
2. donner au rédacteur trois consignes tirées des rejets :
   - garder « Or » quand il introduit une prémisse ;
   - ne jamais commencer une phrase par « Car » ;
   - n’ajouter un connecteur que si l’original exprime déjà cette relation ;
3. viser en priorité les chapitres encore lourds : 0, 13, 14, 15 et 16 (29 à 31 mots de moyenne).
