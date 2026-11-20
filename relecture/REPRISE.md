# Relecture intégrale — état et reprise

**Branche :** `relecture-livre` · **Texte figé :** tag `relecture-2026-11-20-base` (après les corrections P5.1b) · **État au 2026-11-20 soir :** vague 1 terminée, **en pause** avant la vague 2.

## Ce qui est fait

| Étape | Fichiers | État |
| :-- | :-- | :-- |
| P5.1b (corrections factuelles, bibliographie) | chapitres, `commun/biblio*.bib` | ✔ commité et tagué |
| Vague 0 — dossiers de lecture et pistes | `preparer_dossiers.py` → `dossiers/` (ignoré par git, régénérable), `pistes/` | ✔ |
| Vague 1 — 11 lecteurs isolés | consignes : `consignes/00_commun.md` + `P0…P5, PA, T1, T2, T5, C` ; sorties : `sorties/lecteurs/<ID>/{constats.json, bilan.md}` (+ `C/journal.md`) | ✔ 328 constats (3 A, 159 B, 166 C) |
| Routage vers la vérification | `router_constats.py` → `sorties/verification/entrees/{V0…V5, VX}.json`, `hors_perimetre.md`, `STATS.md` | ✔ |
| Vague 2 — vérification et synthèse | consignes prêtes : `consignes/V_verificateur.md`, `consignes/S_synthese.md` | ✘ **à lancer** |

Modèles utilisés en vague 1 : lecteurs P* et T* en Sonnet (effort medium), lecteur C en Opus (effort high).

## Reprendre

1. Se placer sur la branche : `git switch relecture-livre`.
2. Si `relecture/dossiers/` a disparu (inutile pour la vague 2, sauf pour relancer un lecteur) : `git checkout relecture-2026-11-20-base -- monographie && (cd monographie && make html) && python3 relecture/preparer_dossiers.py`, puis revenir à la tête de branche.
3. Choisir l'ampleur de la vague 2 (décision de l'auteur, non prise) :
   - **légère** : filtrer les constats A/B (162) et confier vérification et synthèse à un seul agent Opus (effort high) ;
   - **moyenne** : 7 vérificateurs Sonnet (medium), un par lot, puis une synthèse Opus (high) ;
   - **complète** : 7 vérificateurs Opus (high), puis une synthèse Opus (high).
4. Lancer chaque vérificateur avec : « Lisez `relecture/consignes/V_verificateur.md` et exécutez-la pour le lot `VID` » (V0…V5, VX). Sorties : `sorties/verification/VID.{json,md}`.
5. Lancer la synthèse avec : « Lisez `relecture/consignes/S_synthese.md` et exécutez-la ». Sorties : `monographie/notes/SYNTHESE_RELECTURE_2026-11-20.md`, `relecture/sorties/synthese/corrections.json`.
6. Pour la variante légère, adapter l'étape 4 : un fichier d'entrée unique ne contenant que les A/B (filtre à écrire sur `entrees/*.json`), et un seul agent qui enchaîne vérification et synthèse.

## Thèmes déjà visibles dans les retours des lecteurs (non vérifiés)

- Résumés plus affirmatifs que les chapitres : ch. 0, pages de partie, points clés (T1, P3, P4, P5, C).
- « Producteur plus fiable, système plus risqué » contredit par le tableau 16.1 (P4, T1, C).
- Redites : récapitulatifs à chaque seuil de partie, études de cas racontées plusieurs fois (T5, P1, P3, C).
- Points déjà tranchés sur lesquels des lecteurs neufs butent encore : cadre/représentation (P1.2), ch. 16 (P1.1), statuts des propositions 2 et 4 (P1.6), roulette russe (S6).
- Parcours « L'argument principal » sans les ch. 8 et 9 (P0, T5).
- Aucune erreur de calcul trouvée (T2, PA et tous les lecteurs de partie).
