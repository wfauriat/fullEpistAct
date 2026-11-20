# Journal de la passe de style — `05-trois-incertitudes`

- Appliqué le 2026-11-20T13:25:33 ; rédacteur : gemini ; juge : claude-opus (juge-style) ; tour None
- Proposées : 6 · appliquées : 4 · rejetées par le juge : 2 · rejetées par les contrôles : 0 · sans verdict : 0
- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).
- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.

## Retouches appliquées (4)

### 001 — § « Trois incertitudes, et ce que mesure une barre d’erreur » (ligne 3) — autre

Avant :

> Ce chapitre s’appuie sur les règles de la forme $A \cap (\dots) \rightarrow B$, dont l’arrière-plan tacite $\mathcal{T}$ reste ouvert et la formule des probabilités totales (@sec:ch01), sur les notions de représentation (@def:representation) et de cadre (@def:cadre) introduites au @sec:ch02, ainsi que sur la lecture de la probabilité comme jugement pesant des mondes possibles (@sec:ch03).

Après :

> Ce chapitre s’appuie sur les règles de la forme $A \cap (\dots) \rightarrow B$ — dont l’arrière-plan tacite $\mathcal{T}$ reste ouvert — et sur la formule des probabilités totales (@sec:ch01), sur les notions de représentation (@def:representation) et de cadre (@def:cadre) introduites au @sec:ch02, ainsi que sur la lecture de la probabilité comme jugement pesant des mondes possibles (@sec:ch03).

*Juge :* Les tirets et le « et sur » lèvent l’ambiguïté qui laissait lire « la formule des probabilités totales » dans la relative ; prérequis, renvois et sens inchangés.

### 002 — § « Une barre d’erreur mesure un désaccord » (ligne 73) — italique

Avant :

> Il en découle une conséquence souvent méconnue : *l’incertitude ontologique n’est pas une troisième quantité numérique qui attendrait encore une formule plus savante*.

Après :

> Il en découle une conséquence souvent méconnue : l’incertitude ontologique n’est pas une troisième quantité numérique qui attendrait encore une formule plus savante.

*Juge :* Retrait d’une italique d’emphase portant sur toute une proposition ; le texte, la portée de la négation et le statut de l’énoncé sont inchangés.

### 003 — § « Une barre d’erreur mesure un désaccord » (ligne 99) — phrase-longue

Avant :

> Dire d’un facteur omis qu’il reste muet signifie donc qu’il demeure *non attribué*, et non qu’il est toujours numériquement absent : seul un facteur demeuré constant pendant la collecte des données (ou maintenu identique par le protocole d’essai) ne laisse littéralement aucune trace dans la barre d’erreur calculée.

Après :

> Dire d’un facteur omis qu’il reste muet signifie donc qu’il demeure *non attribué*, et non qu’il est toujours numériquement absent. Seul un facteur demeuré constant pendant la collecte des données (ou maintenu identique par le protocole d’essai) ne laisse en effet littéralement aucune trace dans la barre d’erreur calculée.

*Juge :* La phrase longue est coupée au deux-points. « En effet » rend explicite le lien de justification que portait déjà le deux-points ; « seul », « toujours » et la parenthèse sur le protocole sont conservés.

### 006 — § « Pourquoi les outils de robustesse restent à l’intérieur du cadre » (ligne 121) — phrase-longue

Avant :

> Des ingénieurs qui connaissaient les propulseurs se sont opposés au lancement par le froid annoncé, en faisant valoir que les températures prévues sortaient du domaine observé sans dommage ; la direction du programme a passé outre à leurs objections dans la décision finale de lancement [@rogers1986].

Après :

> Des ingénieurs qui connaissaient les propulseurs se sont opposés au lancement par le froid annoncé, en faisant valoir que les températures prévues sortaient du domaine observé sans dommage. La direction du programme a pourtant passé outre à leurs objections dans la décision finale de lancement [@rogers1986].

*Juge :* La phrase d’environ 45 mots est coupée au point-virgule. « Pourtant » explicite une concession déjà contenue dans « passer outre » ; acteurs, faits et source sont inchangés.

## Rejetées par le juge (2)

### 004 — § « Une barre d’erreur mesure un désaccord » (ligne 99) — francais, gain

*Juge :* Une fois la retouche 003 acceptée, « en effet » reviendrait deux phrases plus loin dans ce court paragraphe (« ne laisse en effet… », « sous-estimera en effet… ») : on remplacerait un tic par un autre. Dans la phrase d’origine, le deux-points introduisait clairement la précision.

Avant :

> De plus, même lorsque ses fluctuations passées ont gonflé le terme aléatoire, cette barre d’erreur ne protège pas contre un changement durable de ce facteur : si le système entre ensuite dans des conditions où ce facteur prend une valeur nouvelle et systématique, la dispersion aléatoire mesurée auparavant sous-estimera le décalage réel.

Après (non appliqué) :

> De plus, même lorsque ses fluctuations passées ont gonflé le terme aléatoire, cette barre d’erreur ne protège pas contre un changement durable de ce facteur. Si le système entre ensuite dans des conditions où ce facteur prend une valeur nouvelle et systématique, la dispersion aléatoire mesurée auparavant sous-estimera en effet le décalage réel.

### 005 — § « Pourquoi les outils de robustesse restent à l’intérieur du cadre » (ligne 110) — francais, registre

*Juge :* Une phrase autonome ouverte par « Car » après un point est maladroite en prose académique. La coupe isole la justification de l’affirmation qu’elle fonde, et le deux-points d’origine faisait déjà ce travail sans heurt.

Avant :

> Ni un balayage plus large des paramètres mécaniques ni le coefficient de sécurité de 1,8 ne traitent la corrosion : la corrosion par piqûres et la fissuration par corrosion sous contrainte modifient le mécanisme de défaillance d’une façon qu’une marge sur la charge statique ne mesure pas (@fig:ch05-ferrure-marge).

Après (non appliqué) :

> Ni un balayage plus large des paramètres mécaniques ni le coefficient de sécurité de 1,8 ne traitent la corrosion. Car la corrosion par piqûres et la fissuration par corrosion sous contrainte modifient le mécanisme de défaillance d’une façon qu’une marge sur la charge statique ne mesure pas (@fig:ch05-ferrure-marge).

## Rejetées par les contrôles mécaniques (0)

