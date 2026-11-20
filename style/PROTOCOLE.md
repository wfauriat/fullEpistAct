# Protocole — passe de style automatisée

Fonctionnement pratique de `STYLE_PASS_SPEC_v3.md`. Deux instances travaillent dans **le même dossier**, sur la branche **`style-pass`** :

| Rôle | Qui | Fait | Ne fait jamais |
| :--- | :--- | :--- | :--- |
| **Rédacteur** | instance Gemini | propose les retouches, chapitre par chapitre, dans `style/lots/<chapitre>/` | modifier `monographie/`, appliquer, committer, changer de branche |
| **Orchestrateur** | instance Claude Code | veille, revérifie, lance le juge, applique, contrôle, committe | réécrire le texte |
| **Juge** | agent Claude Opus (effort élevé), neuf à chaque chapitre | accepte ou rejette chaque retouche, écrit `verdicts.json` | modifier un autre fichier, proposer une variante |
| **Auteur** | — | relecture intégrale à la fin, à l’aide des journaux | — (hors de la boucle pendant la passe) |

Le chapitre n’est modifié que par `style/appliquer_edits.py appliquer`, lancé par l’orchestrateur.

---

## 1. Fichiers d’un lot (`style/lots/<chapitre>/`)

| Fichier | Écrit par | Rôle |
| :--- | :--- | :--- |
| `propositions.yaml` | rédacteur | les retouches proposées (§3) |
| `PRET` | rédacteur, via `veilleur.py declarer` | marqueur « prêt pour le juge » : tour et empreinte SHA-256 de `propositions.yaml` |
| `ETAT` | orchestrateur | `en_revue`, puis `applique` (ou `erreur`) ; un lot qui a un `ETAT` est fermé au rédacteur |
| `verification.json`, `dossier_juge.md`, `original.md` | `appliquer_edits.py verifier` | résultat des contrôles, dossier lu par le juge, copie figée du chapitre |
| `verdicts.json` | juge | un verdict par retouche soumise |
| `journal.md`, `rapport_portee.md` | `appliquer_edits.py appliquer` | pour la relecture de l’auteur |

**Ordre des chapitres** (celui de `monographie/livre.yaml`) : `00-avant-propos`, `00-cartographier`, `01-outils-logique-probabilite`, `02-cadre`, `03-mondes-possibles`, `04-decider`, `05-trois-incertitudes`, `06-detecter-une-erreur`, `07-cadre-cause-commune`, `08-independance-chaines`, `09-severite-echappement`, `10-couches-basses`, `11-regle-tiree-des-donnees`, `12-autre-regime`, `13-synthese-deux-axes`, `14-chaines-qui-agissent`, `15-erosion-verifications`, `16-angles-morts-collectifs`, `17-decisions-sans-appel`, `18-remede-trois-niveaux`, `99-conclusion`.

Le nom du dossier de lot est le nom du fichier du chapitre sans `.md`.

---

## 2. Côté rédacteur (Gemini)

1. **Lire une fois :**
   - `style/STYLE_PASS_SPEC_v3.md` (objectifs, règle de retenue, interdits) ;
   - `style/DERIVES_A_EVITER.md` (pièges relevés) ;
   - `monographie/commun/registre_termes.md` (termes à garder exacts) ;
   - ce protocole.
2. **Pour chaque chapitre, dans l’ordre :**
   1. Lire le chapitre en entier (`monographie/chapitres/<chapitre>.md`). Facultatif : `python3 style/audit_style.py --chapter <chapitre>` indique où la prose est la plus lourde.
   2. Écrire `style/lots/<chapitre>/propositions.yaml` (format au §3).
   3. Auto-vérifier : `python3 style/appliquer_edits.py verifier style/lots/<chapitre>`. Corriger ou retirer chaque retouche rejetée par les contrôles (texte introuvable, chevauchement, zone non modifiable, renvoi ou nombre modifié…), puis relancer jusqu’à ce qu’il n’y ait plus de rejet.
   4. Déclarer le lot prêt : `python3 style/veilleur.py declarer style/lots/<chapitre>`.
   5. Passer au chapitre suivant sans attendre le juge.
3. **Réviser un lot déjà déclaré :** c’est possible tant que l’orchestrateur ne l’a pas pris, c’est-à-dire tant qu’il n’a pas de fichier `ETAT`. Modifier `propositions.yaml`, relancer `verifier`, puis `declarer` à nouveau (le tour augmente). Une fois l’`ETAT` présent, le lot est fermé.
4. **Ne jamais :**
   - modifier un fichier hors de `style/lots/<chapitre>/`, et en particulier rien sous `monographie/` ;
   - lancer `appliquer_edits.py appliquer` ;
   - faire une opération git (commit, checkout, stash, reset, switch…) ;
   - toucher à un lot qui a un `ETAT`.

   Les fichiers `verification.json`, `dossier_juge.md` et `original.md` produits par l’auto-vérification seront réécrits par l’orchestrateur : c’est normal.

---

## 3. Format de `propositions.yaml`

Utiliser des **blocs littéraux** (`|`) pour `avant` et `apres` : le texte contient des deux-points, des dièses et des guillemets qui casseraient une chaîne YAML simple. L’indentation doit être régulière.

```yaml
chapitre: 00-cartographier
redacteur: gemini-<modèle et version>
modifications:
  - id: "001"
    motif: phrase-longue
    avant: |
      La dinde inductiviste qui note chaque matin l’heure à laquelle le fermier lui apporte son grain dispose, à la veille de Noël, d’une série statistique irréprochable ; la catastrophe qui l’attend ne vient pas d’une faute de calcul, mais d’une variable qui n’a jamais figuré dans son cadre.
    apres: |
      La dinde inductiviste qui note chaque matin l’heure à laquelle le fermier lui apporte son grain dispose, à la veille de Noël, d’une série statistique irréprochable. La catastrophe qui l’attend ne vient pas d’une faute de calcul, mais d’une variable qui n’a jamais figuré dans son cadre.
    note: "Coupe au point-virgule."
  - id: "002"
    motif: or-initial
    avant: |
      …
    apres: |
      …
```

- **`id`** : unique dans le lot, entre guillemets.
- **`avant`** : copie **exacte** d’un passage du chapitre, apostrophes typographiques ’ comprises. Il doit apparaître une seule fois ; sinon, l’allonger. Au plus un paragraphe.
- **`apres`** : la nouvelle version. Elle peut couper le paragraphe en deux, par une ligne vide.
- **`motif`** : une valeur du §9 de la spécification.
- **`note`** : facultative, jamais montrée au juge, reprise dans le journal.

---

## 4. Côté orchestrateur (Claude Code)

### 4.1 Boucle de veille

1. Lancer le veilleur **en arrière-plan** : `python3 style/veilleur.py attendre`. Il prend le premier lot prêt dans l’ordre du livre, écrit `ETAT: en_revue`, affiche `LOT_PRET style/lots/<chapitre> tour=<n>` et s’arrête, ce qui réveille l’orchestrateur.
2. **Revérifier**, sans se fier à l’auto-vérification du rédacteur : `python3 style/appliquer_edits.py verifier style/lots/<chapitre>`.
3. **Si aucune retouche n’est soumise au juge :** écrire `{"juge": "aucun", "verdicts": []}` dans `verdicts.json` et passer à l’étape 6.
4. **Lancer le juge** : un agent neuf, Opus, effort élevé, en premier plan.
   - Type `juge-style` (`.claude/agents/juge-style.md`).
   - Si ce type n’est pas chargé dans la session, type `general-purpose` avec l’instruction de lire et suivre `.claude/agents/juge-style.md`.
   - Message de mission :

     > Mission : juger le lot `style/lots/<chapitre>/`. Dossier : `style/lots/<chapitre>/dossier_juge.md`. Chapitre d’origine : `style/lots/<chapitre>/original.md` (lis-le en entier avant de juger). Au besoin : `monographie/commun/registre_termes.md`, `style/STYLE_PASS_SPEC_v3.md`. Écris `style/lots/<chapitre>/verdicts.json`, un verdict par retouche, dans l’ordre du dossier. Ne lis aucun autre fichier du dépôt, n’exécute aucune commande, ne modifie aucun autre fichier.
5. **Contrôler le passage du juge :**
   - `git status --porcelain` ne montre, en dehors des lots, aucun fichier modifié ;
   - `verdicts.json` est un JSON valide avec un verdict par retouche soumise.

   Sinon, restaurer ce qui a été touché et relancer un juge neuf.
6. **Appliquer** : `python3 style/appliquer_edits.py appliquer style/lots/<chapitre>`.
7. **Vérifier la compilation** : `cd monographie && make verifier`. Il doit sortir sans erreur nouvelle.

   En cas d’échec :
   - restaurer le chapitre depuis `style/lots/<chapitre>/original.md` ;
   - écrire `etat: erreur` et la raison dans `ETAT` ;
   - ne pas committer le chapitre, et le signaler dans le compte rendu.
8. **Committer** le chapitre et son lot, rien d’autre :

   `git add monographie/chapitres/<chapitre>.md style/lots/<chapitre>`

   Message : `style(<chapitre>): <n> retouches appliquées (<m> rejetées par le juge, <k> par les contrôles)`, avec en corps « Rédacteur : <modèle> ; juge : Claude Opus (juge-style) » et les lignes d’attribution habituelles.
9. **Relancer le veilleur** (étape 1).

### 4.2 Fin de passe et incidents

- **Fin de passe :** après `99-conclusion`, faire un bilan par chapitre (`python3 style/veilleur.py etat`), mesurer avec `python3 style/audit_style.py`, et le communiquer à l’auteur.
- **Interruption :** si la session s’arrête pendant qu’un lot est `en_revue`, au redémarrage :
  - lancer `python3 style/veilleur.py liberer style/lots/<chapitre>` (le lot redevient disponible), puis relancer le veilleur ;
  - les lots déjà `applique` sont committés et ne sont pas repris.
- **État de la passe à tout moment :** `python3 style/veilleur.py etat`.

---

## 5. Pour la relecture finale de l’auteur

- **Vue d’ensemble :** `git diff main..style-pass -- monographie/chapitres/`.
- **Par chapitre :**
  - `style/lots/<chapitre>/journal.md` : retouches appliquées (avant, après) et retouches rejetées avec la raison du juge ;
  - `style/lots/<chapitre>/rapport_portee.md` : les changements les plus susceptibles d’avoir déplacé le sens (modaux, quantificateurs, termes du registre, mots pleins disparus). C’est le premier endroit à regarder si un passage sonne faux.
- **Revenir au texte d’origine d’un chapitre :** `git checkout main -- monographie/chapitres/<chapitre>.md`. Une retouche isolée se retrouve dans le journal pour la défaire à la main.

---

## 6. Message de lancement pour l’instance Gemini

À coller tel quel :

> Tu es le rédacteur d’une passe de style sur la monographie de ce dépôt, sur la branche `style-pass` (ne change pas de branche et ne fais aucune opération git). Lis d’abord, en entier : `style/PROTOCOLE.md` (ton rôle et le format à produire), `style/STYLE_PASS_SPEC_v3.md` (objectifs, règle de retenue, interdits), `style/DERIVES_A_EVITER.md` (pièges relevés sur une première tentative) et `monographie/commun/registre_termes.md`. Puis traite les chapitres un par un, dans l’ordre du protocole, en commençant par `00-avant-propos` :
> 1. écris `style/lots/<chapitre>/propositions.yaml` ;
> 2. lance `python3 style/appliquer_edits.py verifier style/lots/<chapitre>` et corrige jusqu’à ce qu’aucune retouche ne soit rejetée par les contrôles ;
> 3. lance `python3 style/veilleur.py declarer style/lots/<chapitre>` ;
> 4. passe au chapitre suivant sans attendre.
>
> Tu ne modifies jamais rien sous `monographie/` : un autre agent juge tes retouches et un script les applique. Respecte la règle de retenue : ne retouche que ce qui gagne nettement, garde intactes les phrases qui fonctionnent, ne change jamais un terme du registre, un fait, un modal ou une restriction. Préfère dix retouches nettes à cinquante discutables. Quand le dernier chapitre (`99-conclusion`) est déclaré, arrête-toi et fais un bref compte rendu.
