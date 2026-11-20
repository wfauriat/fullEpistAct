# Relecture intégrale — consigne de la synthèse (vague 2, étape finale)

Onze lecteurs neufs ont lu le livre *Agir d'après une représentation du monde* (P0 à P5 et PA par portion ; T1, T2, T5 par thème sur des extraits ; C, lecteur cible, de bout en bout). Des vérificateurs ont ensuite contrôlé leurs constats contre la source, lot par lot (V0 à V5 par partie, VX pour les annexes, les constats transversaux et les questions hors périmètre). **Vous rédigez la synthèse destinée à l'auteur.** Vous avez accès à tout le dépôt.

## 1. Entrées

- Les grappes vérifiées : `relecture/sorties/verification/V*.json` et les bilans de lot `relecture/sorties/verification/V*.md`.
- Les bilans des lecteurs : `relecture/sorties/lecteurs/*/bilan.md`, et le journal du lecteur cible `relecture/sorties/lecteurs/C/journal.md`.
- Les chiffres de la vague 1 : `relecture/sorties/verification/entrees/STATS.md`.
- Pour le contexte : `monographie/notes/TODO_ETAT_ACTUEL.md`, `monographie/notes/DECISIONS_SYNTHESE.md`, `monographie/notes/ARBITRAGES_RESTANTS.md`, `monographie/notes/RAPPORT_AUDIT_CALQUES.md`, `content_spec/00_global.md`, `authoring_conventions.md`, et la source du livre (`monographie/chapitres/`, `parties/`, `annexes/`) pour trancher un doute.

Vous pouvez revenir à la source pour contrôler une grappe douteuse ; vous pouvez fusionner des grappes de lots différents qui décrivent le même problème transversal, ou en reclasser une (verdict, gravité, groupe) en le justifiant.

## 2. Sorties

Vous ne modifiez **aucun** fichier du livre.

### `monographie/notes/SYNTHESE_RELECTURE_2026-11-20.md` (en français)

Plan :
1. **Résumé pour l'auteur** (une page au plus) : l'état du livre au regard d'une publication ; les dix problèmes les plus importants, par ordre d'importance, chacun en deux lignes avec renvoi aux grappes.
2. **Ce que les lecteurs ont compris** : rapprochez les § 1 des bilans (« Ce que j'ai compris ») et la « lecture en une page » du lecteur C. Là où les lecteurs ont retenu la même thèse, le texte porte ; là où ils divergent ou se trompent, c'est un problème de clarté à signaler.
3. **Questions de fond (groupe 3)** : pour chacune, le problème, les passages concernés, les options, une recommandation argumentée, et une ligne `Décision :` laissée vide pour l'auteur.
4. **Arbitrages rapides (groupe 2)** : par chapitre ; problème, retouche proposée, ligne `Décision :` vide.
5. **Corrections directes (groupe 1)** : par chapitre, dans l'ordre du livre, avec la retouche exacte (avant / après) ; le détail complet peut rester dans les fichiers JSON si la liste est longue, auquel cas donnez ici le tableau par chapitre et le décompte.
6. **Redites et lecture linéaire** : un plan d'allègement cohérent à l'échelle du livre (quelle occurrence de chaque étude de cas garder en entier, lesquelles réduire à un rappel), à partir des grappes de redite, du lecteur T5 et du journal de C.
7. **Signaux sur les décisions antérieures** : les points tranchés sur lesquels un lecteur neuf bute encore.
8. **Ce qui a été écarté** : décompte des rejets, déjà tranchés et déjà relevés, et leurs motifs récurrents (une ligne chacun, sans détail).
9. **Bilan de la méthode** : nombre de constats par lecteur et taux de confirmation ; part des grappes trouvées par un seul lecteur et par plusieurs ; apport propre des lecteurs par portion, par thème et du lecteur cible ; angles morts probables de cette relecture (ce qu'aucun lecteur n'a pu voir).

Ne mentionnez dans ce document que des identifiants de grappes et de constats, des chemins de fichiers et des citations : il est destiné à l'auteur, pas au livre.

### `relecture/sorties/synthese/corrections.json`

Toutes les corrections exactes des grappes `CONFIRME` des groupes G1 et G2, dans l'ordre du livre, prêtes à être appliquées après décision :

```json
[
  {"grappe": "V2-014", "groupe": "G1", "fichier": "monographie/chapitres/08-independance-chaines.md", "avant": "…", "apres": "…"}
]
```

Vérifiez pour chacune que `avant` figure **une seule fois** dans le fichier (grep -c) ; écartez ou corrigez celles qui ne passent pas, et signalez-les. Validez le JSON avec `python3 -c "import json,sys; print(len(json.load(open(sys.argv[1]))))" relecture/sorties/synthese/corrections.json`.

Terminez en répondant, en dix lignes au plus : le verdict d'ensemble sur l'état du livre, les décomptes par groupe, et les trois questions de fond les plus importantes.
