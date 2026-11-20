# Étalonnage du juge — résultats

- Date : 2026-11-20 ; juge : claude-opus (juge-style)
- Jeu : dérives réelles des pilotes de première passe, et retouches fidèles tirées des mêmes pilotes (`construire.py`).

| Groupe | Attendu | Résultat |
| :-- | :-- | :-- |
| Dérives nettes (4) | rejet | **4/4 rejetées** |
| Dérives limites (0) | rejet souhaité | 0/0 rejetées |
| Retouches fidèles et utiles (8) | acceptation | **7/8 acceptées** |
| Échanges gratuits de synonymes (0) | l’un ou l’autre | 0 acceptés, 0 rejetés |

## Détail

| Id | Type | Catégorie | Verdict | Raison du juge |
| :-- | :-- | :-- | :-- | :-- |
| E01 | derive | fait durci (doutes → alertes) | rejete | « mit au jour bien des défaillances » devient « révéla bien d’autres défaillances » : « d’autres » ajoute le présupposé que l’erreur d’unités serait elle-même l’une de ces défaillances humaines et organisationnelles. « doutes sur la trajectoire » devient « alertes », ce qui durcit le fait rapporté, et « montrer du doigt » → « désigner du doigt » n’est qu’un échange de synonymes. |
| E02 | controle-utile | « Or » initial retiré, coupe | accepte | Le « Or » initial est retiré et la phrase est coupée au deux-points. La phrase suivante explicite aussitôt le nœud ; sens et termes (« décision unique », « seuil ») inchangés. |
| E03 | derive | probabilités (jugement → fréquence) | rejete | « le cas le plus probable » devient « le cas le plus fréquent » : pour une traversée unique, cela substitue une fréquence à un jugement de probabilité, la confusion même que le passage combat. Le futur « départagera » passe aussi au présent sans aucun gain. |
| E04 | controle-utile | deux-points → « Ainsi » | accepte | La phrase longue est coupée et le deux-points remplacé par « Ainsi », qui introduit explicitement l’exemple. « souvent », « parfois » et le renvoi à Mars Climate Orbiter sont conservés. |
| E05 | controle-utile | deux-points → point, sujet explicite | accepte | Le deux-points suivi d’un infinitif devient une phrase à sujet explicite. La visée et ses deux volets sont intacts. |
| E06 | controle-utile | deux-points → point | rejete ✗ | Une fois la phrase coupée, « Ils puisent tous à la même source et s’accorderont […] tout en se trompant ensemble » devient une affirmation autonome, détachée de la restriction « vis-à-vis de tout facteur omis par le cadre ». Or le paragraphe vient de dire que ces contrôles sont précieux contre les étourderies. La coupe par simple parataxe, sans articulation, apporte en outre un gain faible. |
| E07 | derive | portée (possibilité → certitude) | rejete | « peut être pris en défaut » devient « cédera », qui fait d’une possibilité une certitude. « ne révélera jamais l’effet de » perd « jamais » et « l’effet de », « effectivement » et « statistique » disparaissent. « On parlera alors de dérive de distribution » est rattaché par deux-points au seul second exemple, ce qui change ce que nomme le terme. |
| E08 | derive | terme (frontière en dents de scie) | rejete | Le terme du registre « frontière en dents de scie » est remplacé par « profil de compétence en dents de scie ». La clause « qu’il vient de franchir sa limite » disparaît, alors qu’elle porte l’idée de frontière. « remarquable » est affaibli en « capable ». |
| E09 | controle-utile | deux-points → « alors » | accepte | La coupe au deux-points est assortie d’un « alors » qui garde le lien de conséquence et renvoie au cas défini, et « ces erreurs partagées » maintient la restriction. Les termes « contrôle croisé » et « probabilité d’échappement » sont intacts. |
| E10 | controle-utile | « Or » → « pourtant » | accepte | Le « Or » initial est remplacé par un « pourtant » incident qui conserve l’articulation adversative. Le sens est inchangé. |
| E11 | controle-utile | coupe au point-virgule | accepte | La phrase longue est coupée au point-virgule, et le « Aussi » avec inversion en tête de phrase garde le lien de conséquence. Rien n’est retiré. |
| E12 | controle-utile | italique d’emphase retirée, coupe | accepte | La phrase est coupée au point-virgule et l’italique d’emphase est retiré, ce qui fait partie des objectifs de la passe. « délibérément » porte toujours l’opposition, et le contenu est intact. |
