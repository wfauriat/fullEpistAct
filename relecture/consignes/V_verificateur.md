# Relecture intégrale — consigne des vérificateurs (vague 2)

Onze lecteurs neufs ont lu le livre *Agir d'après une représentation du monde* sans rien connaître de son histoire : sept par portion (P0 à P5, PA), trois par thème sur des extraits (T1 argument et statuts, T2 chiffres et modèles, T5 redites et lecture linéaire) et un lecteur cible de bout en bout (C). Leurs constats ont été répartis en lots. **Vous vérifiez un lot.** Contrairement aux lecteurs, vous n'êtes pas tenu à l'isolement : vous avez accès à tout le dépôt.

Votre lot est indiqué dans le message qui vous lance (`VID` : V0 à V5 ou VX).

## 1. Entrées

- **Votre lot :** `relecture/sorties/verification/entrees/VID.json` — un tableau de constats (`id`, `lecteur`, `unite`, `section`, `passage`, `categorie`, `gravite`, `constat`, `proposition`, `confiance`).
- **Le texte source** (seule référence pour localiser et juger) : `monographie/chapitres/*.md`, `monographie/parties/partie-N.md`, `monographie/annexes/*.md`, `monographie/tableaux/*.md`, `monographie/commun/parametres.py`. Le livre compilé `monographie/build/livre.html` peut servir à voir un rendu.
- **Les règles :** `authoring_conventions.md` (surtout § 8 pour le français et la typographie, § 11 pour la grille de relecture), `monographie/commun/registre_termes.md` (termes, chapitre d'introduction), `content_spec/00_global.md` (§ 3 : statuts canoniques des propositions ; § 7 : valeurs canoniques ; § 9 : affirmations interdites), `BUILDER_START_HERE.md` § 2 (règles dures).
- **Les décisions déjà prises par l'auteur :** `monographie/notes/DECISIONS_SYNTHESE.md`, `monographie/notes/ARBITRAGES_RESTANTS.md` (lignes « Décision : »), `monographie/notes/TODO_ETAT_ACTUEL.md`. Au besoin, cherchez (grep) un point ancien dans `monographie/notes/SYNTHESE_A_TRANCHER.md`.
- **Les points déjà relevés et encore ouverts :** `monographie/notes/RAPPORT_AUDIT_CALQUES.md` (audit des calques de l'anglais, non appliqué).
- **Pistes mécaniques :** `relecture/pistes/termes.md` (emplois de termes avant leur chapitre d'introduction) et `relecture/pistes/repetitions.md`. Traitez les pistes qui touchent les unités de votre lot comme des constats supplémentaires (lecteur `piste`).
- **Lot VX seulement :** `relecture/sorties/verification/entrees/hors_perimetre.md` — ce que chaque lecteur a dû prendre sur parole et ses questions hors périmètre. Examinez chaque point : soit le livre y répond (notez-le brièvement dans votre `VX.md`), soit il révèle un défaut (créez une grappe).

## 2. Localiser un passage

Les lecteurs citent le **texte rendu**, pas la source. Dans la source : apostrophes et guillemets courbes (’ « »), espaces insécables, renvois sous forme d'étiquettes (`@sec:ch08`, `@prop:…`, `@def:…`, `[-@sec:ch05]`), citations sous forme de clés (`[@mco1999]`), blocs entre `:::`. Cherchez un fragment distinctif de quelques mots, avec `.` à la place des apostrophes. Les tableaux des exemples quantitatifs viennent de `monographie/tableaux/` (générés : ne jamais proposer de les modifier à la main ; signaler plutôt le script en cause).

## 3. Juger chaque constat

Lisez le passage **dans son contexte complet**. Attention : T1, T2 et T5 n'ont vu que des extraits ; un « chaînon manquant » ou une « notion non définie » peut figurer dans le texte courant qu'ils n'avaient pas.

**Verdicts :**
- `CONFIRME` — le défaut est réel tel que décrit (éventuellement après reformulation).
- `PLAUSIBLE` — défendable mais affaire de jugement ; l'auteur tranchera.
- `REJETE` — erreur de lecture, texte qui dit autre chose ailleurs, artefact de conversion, ou reproche fait à une convention assumée du livre. Une ligne de justification suffit.
- `DEJA_TRANCHE` — le constat demande l'inverse d'une décision prise par l'auteur (citez-la : « DECISIONS_SYNTHESE N1 », « ARBITRAGES P1.2 »…). **Exception importante :** si la décision visait précisément ce problème et qu'un lecteur neuf bute encore dessus, mettez `CONFIRME` et écrivez dans `justification` : « la correction décidée (réf.) ne suffit pas ». C'est un signal précieux.
- `DEJA_RELEVE` — déjà listé comme ouvert dans `RAPPORT_AUDIT_CALQUES.md` ou dans le TODO (citez la référence) ; inutile de le détailler.

**Regroupement :** réunissez en une seule **grappe** les constats qui portent sur le même problème (même passage, ou même cause dans plusieurs passages de votre lot). Le nombre de lecteurs **distincts** qui ont relevé un problème est une information : conservez tous les identifiants.

**Gravité** (réévaluez-la) : `A` contresens, erreur de fond, de calcul ou de fait, contradiction ; `B` gêne réelle ; `C` mineur.

**Rang** (ordre de priorité de `BUILDER_START_HERE.md` § 4) : `1` fuite d'argument ou dépendance (et erreurs de chiffres ou de faits) ; `2` fuite de provenance ; `3` statut ; `4` terminologie ; `5` qualité du français (clarté, redites comprises) ; `6` typographie.

**Groupe d'action :**
- `G1` — correction directe, sans arbitrage : erreur factuelle ou de calcul, faute nette, retouche de français évidente, conforme aux décisions et aux règles ;
- `G2` — arbitrage rapide : choix entre deux formulations, petite retouche de structure, coupe locale ;
- `G3` — question de fond : argument, statut, structure, coupe importante ; exposez les options.

**Correction proposée :** pour chaque grappe `G1`, et pour les `G2` quand c'est possible, donnez une retouche **exacte** : `avant` = chaîne copiée de la source, présente **une seule fois** dans le fichier (vérifiez-le avec grep -c), `apres` = son remplacement. Respectez les termes du registre, les règles de français et de typographie (§ 8 des conventions : espaces insécables, guillemets « », etc.), ne tapez jamais à la main un nombre d'un exemple quantitatif, n'introduisez aucune référence interne. Une retouche doit rester minimale.

## 4. Sorties

Vous ne modifiez **aucun** fichier du livre. Vous écrivez deux fichiers dans `relecture/sorties/verification/` :

### `VID.json`

```json
[
  {
    "grappe": "VID-001",
    "constats": ["P2-004", "T2-017", "C-033"],
    "lecteurs_distincts": 3,
    "fichier": "monographie/chapitres/08-independance-chaines.md",
    "ligne": 185,
    "passage": "extrait exact de la source",
    "verdict": "CONFIRME",
    "reference": "",
    "categorie": "chiffres",
    "gravite": "A",
    "rang": 1,
    "groupe": "G1",
    "probleme": "énoncé net du défaut, en une à trois phrases",
    "correction": {"avant": "…", "apres": "…"},
    "justification": "pourquoi ce verdict ; pour G3 : les options"
  }
]
```

`correction` vaut `null` quand aucune retouche exacte n'est proposée ; une grappe peut porter une liste de corrections (`"correction": [{…}, {…}]`) si le même défaut touche plusieurs passages. **Chaque constat de votre lot doit figurer dans exactement une grappe** (les rejetés aussi). Validez le fichier :
`python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(len(d), 'grappes')" relecture/sorties/verification/VID.json`

### `VID.md`

```markdown
# Vérification — lot VID

## Bilan chiffré
(constats reçus ; grappes ; répartition par verdict, gravité, groupe)

## Les problèmes les plus importants du lot
(5 à 10, par ordre d'importance, avec renvoi aux grappes)

## Signaux sur des décisions antérieures
(points tranchés sur lesquels un lecteur neuf bute encore)

## Rejets : motifs récurrents
(par exemple : extrait incomplet, artefact de conversion, convention mal comprise ; et par lecteur si un profil se dégage)

## Remarques pour la synthèse
(problèmes qui débordent votre lot et doivent être rapprochés d'autres lots)
```

Terminez en répondant, en cinq lignes au plus : nombre de grappes par verdict et par groupe, et les deux problèmes les plus graves.
