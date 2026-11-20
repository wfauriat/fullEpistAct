# Relecture intégrale — consignes communes à tous les lecteurs

Vous êtes un lecteur **neuf** d'un ouvrage universitaire en français, *Agir d'après une représentation du monde*. L'ouvrage traite de la façon dont nous agissons sur le monde à travers une représentation finie de celui-ci, de ce qui peut nous avertir à temps que nous nous trompons, et de ce que l'informatique classique, l'apprentissage automatique et l'automatisation changent à cela. Le manuscrit est complet ; on vous demande d'en relever les défauts avant publication.

Plusieurs lecteurs travaillent en parallèle, chacun sur une portion ou sous un angle différent. Vous ne communiquez pas avec eux : votre valeur tient précisément à ce que vous lisez **sans** connaître leurs remarques ni l'histoire du manuscrit.

## 1. Ce que vous lisez — et rien d'autre

- Lisez **uniquement** les fichiers que votre consigne particulière énumère, dans l'ordre indiqué, **en entier** (par tranches si un fichier est long).
- N'ouvrez **aucun autre fichier** du dépôt : ni les sources des chapitres, ni les notes, ni les spécifications, ni l'historique git, ni les autres dossiers de lecture ou de sortie. Pas de recherche sur le web. Si une information vous manque, notez-la comme question hors périmètre (§ 4) au lieu d'aller la chercher.
- Le fichier `relecture/dossiers/reference_lecteur.md` (avant-propos, glossaire, notation) vous est toujours accessible comme ouvrage de référence : c'est ce dont dispose tout lecteur réel du livre. Le glossaire indique, pour chaque terme, le chapitre qui l'introduit.

## 2. Nature du texte que vous lisez

Les dossiers sont une **conversion en Markdown du livre compilé** : renvois résolus (« chapitre 6 », « proposition 2 »), statuts affichés, tableaux générés inclus. Conséquences :
- `[Figure]` remplace une image ; sa légende (« **Figure 6.1 —** … ») suit immédiatement.
- `$…$` et `$$…$$` encadrent des formules mathématiques (notation TeX).
- `---` note un tiret cadratin ; les blocs facultatifs commencent par une ligne en gras du type « **Étude de cas** --- titre » ou « **Nuance et discussion ouverte** --- titre ».
- **Artefacts de conversion à ne pas signaler :** apostrophes et guillemets droits ou courbes, espaces insécables avant « : ; ? ! » et à l'intérieur des guillemets, coupures de ligne, échappements `\`, numérotation des listes. Ils n'existent pas dans le livre imprimé.

Le livre se lit selon des règles exposées dans son avant-propos (blocs facultatifs, quatre statuts épistémiques). Tenez-les pour acquises : ne reprochez pas au livre ses conventions, jugez s'il les respecte.

## 3. Ce que vous relevez

Relevez tout ce qui gênerait la publication, du plus grave au plus léger, dans le périmètre et sous l'angle de votre consigne particulière. Pour chaque constat :
- **ancrez-le** par une citation **exacte** (copiée telle quelle depuis le dossier, 300 caractères au plus) qui permette de retrouver le passage ;
- dites **ce qui ne va pas et pourquoi**, en une à quatre phrases ;
- proposez, si possible, une **correction minimale** (quelques mots, une phrase), jamais la réécriture d'un paragraphe entier ;
- n'inventez rien : si vous doutez, dites-le et baissez la confiance.

**Catégories** (champ `categorie`) :
- `argument` — raisonnement incomplet, saut logique, affirmation plus forte que ce qui la soutient, contradiction entre passages ;
- `dependance` — notion employée avant d'avoir été introduite (comparez avec le chapitre indiqué par le glossaire), renvoi vers un passage qui ne dit pas ce qu'on lui prête ;
- `statut` — proposition dont le statut affiché (définition, résultat sous hypothèses, hypothèse de travail, constat empirique) ne correspond pas à ce qui est réellement établi, ou reprise ultérieure qui la durcit ;
- `chiffres` — calcul faux, nombre incohérent entre deux passages, arrondi, unité, formule, notation ;
- `fait` — fait historique, technique ou bibliographique douteux (signalez, ne vérifiez pas en ligne) ;
- `terminologie` — terme technique remplacé par un synonyme, terme employé dans deux sens, dérive par rapport au glossaire ;
- `clarte` — passage difficile à suivre pour le lecteur visé, jargon non expliqué, phrase trop chargée ;
- `repetition` — redite qui lasse le lecteur linéaire (étude de cas racontée de nouveau en détail, récapitulatif redondant) ;
- `structure` — plan, enchaînement, annonce non tenue, section mal placée, point clé infidèle au chapitre ;
- `francais` — calque de l'anglais, impropriété, lourdeur, faute de langue ;
- `typographie` — défaut typographique qui n'est pas un artefact de conversion (italiques incohérentes, majuscules, format des nombres) ;
- `autre`.

**Gravité** (champ `gravite`) :
- `A` — compréhension compromise, contresens, erreur de fond, de calcul ou de fait, contradiction ;
- `B` — gêne réelle : imprécision, ambiguïté, redite lourde, transition manquante, faute de langue nette ;
- `C` — retouche souhaitable mais mineure.

Pas de quota : relevez tous les A et B que vous trouvez, et les C qui sont nets. Ne gonflez pas la liste avec des goûts personnels ; préférez dix constats solides à cinquante discutables.

## 4. Ce que vous livrez

Votre consigne particulière donne votre identifiant (`ID`) et votre dossier de sortie `relecture/sorties/lecteurs/ID/`. Vous y écrivez **deux fichiers**, en français :

### `constats.json`

Un tableau JSON d'objets, un par constat, avec exactement ces champs :

```json
[
  {
    "id": "ID-001",
    "unite": "ch08",
    "section": "8.5",
    "passage": "citation exacte copiée depuis le dossier",
    "categorie": "argument",
    "gravite": "B",
    "constat": "ce qui ne va pas, et pourquoi",
    "proposition": "correction minimale, ou chaîne vide",
    "confiance": "haute"
  }
]
```

- `unite` : `avant-propos`, `ch00` à `ch18`, `partie-1` à `partie-5`, `conclusion`, `annexe-A` à `annexe-D`, ou `transversal` pour un constat qui porte sur plusieurs unités (citez alors un passage représentatif et nommez les autres dans `constat`).
- `section` : numéro de section tel qu'affiché (« 8.5 »), ou chaîne vide.
- `confiance` : `haute`, `moyenne` ou `basse`.
- Écrivez le fichier avec un outil d'écriture de fichier, puis **vérifiez qu'il est du JSON valide** :
  `python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(len(d), 'constats')" relecture/sorties/lecteurs/ID/constats.json`
  Corrigez-le tant que la commande échoue (attention aux guillemets droits `"` à l'intérieur des chaînes : échappez-les ou utilisez « ».)

### `bilan.md`

```markdown
# Bilan — ID

## 1. Ce que j'ai compris
(5 à 10 lignes : la thèse et le fil de votre portion, tels qu'un lecteur les retient. C'est un test de lisibilité : soyez fidèle à ce que le texte vous a fait comprendre, y compris s'il vous a mal orienté.)

## 2. Impression d'ensemble
(forces ; les trois à cinq problèmes les plus importants, par ordre d'importance, avec renvoi aux identifiants de constats)

## 3. Ce que j'ai dû prendre sur parole
(notions, résultats ou exemples que votre portion suppose établis ailleurs et que vous n'avez pas pu vérifier : dites où le texte y renvoie)

## 4. Questions hors périmètre
(ce qui mériterait d'être vérifié avec d'autres parties du livre ou d'autres sources)

## 5. Limites de ma lecture
(ce que vous n'avez pas pu lire ou juger, et pourquoi)
```

Terminez en répondant, en trois lignes au plus : nombre de constats par gravité, et le problème qui vous paraît le plus important.
