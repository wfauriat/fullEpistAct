#!/usr/bin/env python3
"""Build the judge's calibration lot (sanity check, style/STYLE_PASS_SPEC_v3.md §7).

Items are real edits taken from the first-pass pilots (style/pilots/):
  - 26 known drifts (changes of meaning, scope, status, term, fact…) found when
    reviewing the pilots — the judge should reject them;
  - 8 faithful edits that improve the text — the judge should accept them;
  - 4 faithful but gratuitous synonym swaps — either verdict is acceptable
    (the spec asks the judge to reject edits with no clear gain).

Writes style/lots/_etalonnage/dossier_juge.md in the production format, in a
shuffled order with neutral ids, and the answer key to a path given with
--cle (keep it outside the repository until scoring).

Usage:
  python3 style/etalonnage/construire.py --cle /chemin/hors/depot/cle.json
  python3 style/etalonnage/noter.py --cle /chemin/hors/depot/cle.json
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STYLE = HERE.parent
ROOT = STYLE.parent
sys.path.insert(0, str(STYLE))
import appliquer_edits as ae  # noqa: E402
import diff_portee as dp  # noqa: E402

LOT = STYLE / "lots" / "_etalonnage"
C0, AP = "00-cartographier", "00-avant-propos"

ITEMS = [
    # ---- known drifts (should be rejected) --------------------------------
    ("derive", "probabilités (jugement → fréquence)", C0,
     "Une fois la course terminée, l’issue ne les départagera guère, du moins dans le cas le plus probable.",
     "Une fois la course terminée, l’issue ne les départage guère, du moins dans le cas le plus fréquent."),
    ("derive", "probabilités (série de calibration)", C0,
     "Pour savoir si une prévision de « 70 % de chances de pluie » mesure bien l’incertitude, il faut relever la longue série des jours où elle a été émise et vérifier s’il a plu environ sept fois sur dix.",
     "Pour savoir si une annonce de « 70 % de chances de pluie » mesure fidèlement l’incertitude, il faut relever une longue série de jours comparables et vérifier s’il a plu environ sept fois sur dix."),
    ("derive", "portée (possibilité → certitude)", C0,
     "Encore faut-il que le facteur omis ait effectivement varié pendant la collecte des données, et que ses effets se lisent dans ce que l’on a pris soin d’enregistrer : un essai de charge sur une ferrure neuve dans l’air sec d’un laboratoire ne révélera jamais l’effet de cinq ans de brouillard salin, et un modèle statistique validé tant qu’un facteur caché restait constant peut être pris en défaut dès que ce facteur change en exploitation. On parlera alors de dérive de distribution.",
     "Encore faut-il que le facteur omis ait varié pendant la collecte des données et que ses effets apparaissent dans ce qui a été enregistré. Un essai de charge sur une ferrure neuve en laboratoire sec ne révélera pas cinq ans de brouillard salin, et un modèle validé tant qu’un facteur caché demeurait stable cédera dès que ce facteur bougera en exploitation : on parlera de dérive de distribution."),
    ("derive", "portée (suffisance ajoutée)", C0,
     "Quant au décideur, au citoyen ou au responsable à qui l’on remet un chiffre assuré sans ses conditions d’obtention — ce qui revient à lui transférer une responsabilité déguisée en information —, il dispose de quatre questions simples qui n’exigent aucune technicité mathématique pour rouvrir le cadre :",
     "Quant au décideur, au citoyen ou au responsable à qui l’on remet un chiffre assuré sans ses conditions d’obtention — transfert de responsabilité déguisé en information —, quatre questions simples suffisent, sans technicité mathématique, pour rouvrir le cadre :"),
    ("derive", "glose retirée + exigence impossible", C0,
     "exiger que toute affirmation soumise à la décision affiche son état de vérification (exploratoire ou établie, ce qui a été contrôlé de façon indépendante) et ses hypothèses principales",
     "exiger que toute affirmation soumise à décision affiche son état de vérification et ses hypothèses"),
    ("derive", "mécanisme substitué", C0,
     "Le @sec:ch16 passe à l’échelle collective pour montrer comment le recours aux mêmes modèles abaisse le taux d’erreur individuel tout en élevant la probabilité d’échappement par corrélation des angles morts, blanchiment de provenance et assèchement des capacités d’évaluation.",
     "Le @sec:ch16 change d’échelle pour examiner comment l’usage collectif des mêmes modèles abaisse les erreurs individuelles tout en élevant l’échappement par corrélation des angles morts, blanchiment de provenance et saturation des capacités d’évaluation."),
    ("derive", "sens (présupposé ajouté)", C0,
     "Le @sec:ch11 montre ce qui change lorsque la spécification passe dans les données pour former un composant appris : le gain de portée s’achète au prix de la garantie et de la lisibilité, la plausibilité, et non la vérité, devient l’objectif d’optimisation, et orienter un modèle ne revient jamais à le spécifier.",
     "Le @sec:ch11 suit le passage de la spécification dans les données pour former un composant appris : la portée s’achète au prix de la garantie et de la lisibilité, la plausibilité remplace la vérité comme objectif d’optimisation, et orienter un modèle ne revient jamais à le spécifier."),
    ("derive", "statut (réflexion → théorie)", C0,
     "Il pose en langage courant le problème directeur du livre, fait apparaître par le récit les notions qui reviendront de chapitre en chapitre, et montre comment une réflexion générale sur la décision et sur les contrôles éclaire le passage de l’informatique classique à l’intelligence artificielle et à l’automatisation.",
     "Il pose en langage courant la question directrice de l’ouvrage, fait surgir par le récit les notions qui reviendront d’un chapitre à l’autre, et montre comment une théorie générale de la décision et des contrôles éclaire le passage de l’informatique classique à l’intelligence artificielle et à l’automatisation."),
    ("derive", "statut (arguments → démonstrations)", C0,
     "Avant d’entrer dans le détail des outils, des arguments et des études de cas, ce chapitre parcourt l’ensemble du trajet à vol d’oiseau.",
     "Ce chapitre parcourt l’ensemble du livre à vol d’oiseau, avant d’entrer dans le détail des outils, des démonstrations et des cas."),
    ("derive", "fait durci (doutes → alertes)", C0,
     "L’enquête mit au jour bien des défaillances humaines et organisationnelles (équipes surchargées, doutes sur la trajectoire restés sans suite, absence de recalcul indépendant), mais sous ces facteurs se trouvait un point précis que l’on pouvait montrer du doigt : un fichier de code, et la spécification écrite qu’il enfreignait.",
     "L’enquête révéla bien d’autres défaillances humaines et organisationnelles — équipes surchargées, alertes sur la trajectoire restées sans suite, absence de recalcul indépendant. Sous ces facteurs se trouvait pourtant un point précis que l’on pouvait désigner du doigt : un fichier de code, et la spécification écrite qu’il enfreignait."),
    ("derive", "terme (frontière en dents de scie)", C0,
     "En outre, la compétence d’un tel modèle dessine une frontière en dents de scie : remarquable sur une question complexe, il peut échouer sur une variante voisine d’apparence anodine, sans que rien dans le ton de sa réponse ne signale qu’il vient de franchir sa limite.",
     "À cela s’ajoute un profil de compétence en dents de scie : capable sur un problème complexe, le modèle peut échouer sur une variante voisine d’apparence anodine, sans rien laisser paraître dans le ton de sa réponse."),
    ("derive", "terme (tests de référence)", C0,
     "*Ce qui est promis* : on passe d’un contrat vérifiable sur chaque appel à une tendance statistique mesurée en moyenne sur des tests de référence, qui ne garantit aucune réponse particulière.",
     "*Ce qui est promis* : au contrat vérifiable sur chaque appel succède une tendance statistique mesurée en moyenne sur des batteries de tests, sans garantie sur une réponse particulière."),
    ("derive", "terme (probabilité d’échappement)", C0,
     "mesurer concrètement la probabilité d’échappement du système de relecture en y glissant périodiquement des erreurs injectées",
     "mesurer concrètement l’échappement du système de relecture par des erreurs injectées"),
    ("derive", "terme (producteur et contrôleur)", C0,
     "Sous réserve que la comparaison soit fidèle et que les désaccords soient instruits, une erreur ne passe au travers que si elle échappe à la fois au producteur et au contrôleur : l’angle mort résiduel se réduit à l’intersection de leurs angles morts respectifs.",
     "Sous réserve que la comparaison soit fidèle et les désaccords instruits, une erreur ne passe que si elle échappe aux deux voies : l’angle mort résiduel se réduit à l’intersection de leurs angles morts."),
    ("derive", "définitions retirées", C0,
     "Puisqu’une affirmation fausse ne cause de dommage que si elle débouche sur une action sans avoir été arrêtée en chemin, le risque résiduel est le produit de deux facteurs : le taux d’erreur du producteur (la proportion d’affirmations fausses qu’il émet) et la probabilité d’échappement (la proportion de ces affirmations fausses qui franchissent les contrôles sans être contredites à temps).",
     "Puisqu’une affirmation fausse ne nuit que si elle atteint l’action sans être arrêtée, le risque résiduel est le produit de deux facteurs : le taux d’erreur du producteur et la probabilité d’échappement des contrôles."),
    ("derive", "glose retirée (raisonner à l’envers)", C0,
     "Le @sec:ch03 développe la lecture de la probabilité comme jugement pesant des mondes possibles, l’habitude de raisonner à l’envers (chercher quelle variation cachée de l’arrière-plan renverserait la conclusion) et l’impossibilité de juger un prévisionniste sur une seule issue.",
     "Le @sec:ch03 développe la probabilité comme jugement pesant des mondes possibles, l’habitude de raisonner à l’envers et l’impossibilité de juger un prévisionniste sur une issue unique."),
    ("derive", "lien d’exemple retiré (ferrure)", C0,
     "Mais vis-à-vis de tout facteur omis par le cadre — la corrosion de la ferrure —, ces contrôles internes sont des copies les uns des autres : ils puisent tous à la même source et s’accorderont jusqu’à la troisième décimale tout en se trompant ensemble.",
     "Mais devant un facteur omis par le cadre, ces contrôles internes se copient l’un l’autre : ils puisent à la même source et s’accordent jusqu’à la troisième décimale tout en se trompant ensemble."),
    ("derive", "portée (« seulement » retiré, modal affaibli)", C0,
     "Deux instruments prennent alors le relais : ajouter délibérément à son estimation du risque une marge d’humilité pour tenir compte de ce que la représentation pourrait omettre — marge qui relève d’un jugement de prudence et non d’une mesure —, et placer devant l’action un verrou, c’est-à-dire un point où elle attend une autorisation, accordée seulement après un contrôle indépendant.",
     "Deux garde-fous prennent alors le relais : ajouter délibérément à son estimation du risque une marge d’humilité (jugement de prudence et non mesure) pour tenir compte de ce que la représentation peut omettre, et placer devant l’action un verrou où elle attend une autorisation après contrôle indépendant."),
    ("derive", "remède affaibli (ligne budgétaire)", C0,
     "traiter la capacité d’évaluation indépendante comme une ligne budgétaire à part et ne pas produire plus que ce qu’elle permet de vérifier",
     "traiter la capacité d’évaluation indépendante comme une ressource budgétée et plafonner la production à ce qu’elle permet de vérifier"),
    ("derive", "énumération amputée (fiabilité)", C0,
     "*L’informaticien et le concepteur d’IA* : relie la théorie de la fiabilité et des contrôles croisés au passage des composants spécifiés par contrat aux composants appris, jusqu’aux architectures d’agents, aux bacs à sable et aux verrous.",
     "*L’informaticien et le concepteur d’IA* : relie la théorie des contrôles croisés au passage des composants spécifiés aux composants appris, jusqu’aux architectures d’agents, aux bacs à sable et aux verrous."),
    ("derive", "français (gouvernance → gouvernement)", C0,
     "*Le décideur et l’institution* : se concentre sur l’évaluation des enjeux, la gestion des fausses alertes, l’érosion des relectures humaines, les angles morts collectifs et la gouvernance organisationnelle de la vérification.",
     "*Le décideur et l’institution* : se concentre sur l’évaluation des enjeux, la gestion des fausses alertes, l’érosion des relectures humaines, les angles morts collectifs et le gouvernement de la vérification."),
    ("derive-limite", "sens ambigu (qui cadre qui)", C0,
     "Et même lorsqu’un humain relit le brouillon du modèle, deux pièges referment le contrôle sur lui-même : la consigne soumise par l’utilisateur transmet déjà son propre cadre à la machine, et l’entraînement des modèles à plaire à leur interlocuteur les pousse à la complaisance plutôt qu’à la contradiction.",
     "Et même lorsqu’un humain relit la sortie du modèle, deux pièges referment le contrôle sur lui-même : la consigne transmise à la machine lui cède déjà le cadre du problème, et l’entraînement des modèles à satisfaire l’interlocuteur favorise la complaisance plutôt que la contradiction."),
    ("derive", "propos central affaibli (infinité → foule)", AP,
     "Cette représentation assemble des mesures, découpe la réalité en catégories, retient certaines variables, en écarte une infinité d’autres, relie le tout par des règles logiques, des équations ou des distributions de probabilité, puis livre une conclusion ou un chiffre.",
     "Cette représentation assemble des mesures, découpe la réalité en catégories, retient certaines variables en écartant une foule d’autres, puis relie le tout par des règles logiques, des équations ou des distributions de probabilité."),
    ("derive-limite", "statut (arguments développés → résultats établis)", AP,
     "Prétendre fournir une méta-procédure formelle garantissant la justesse de nos cadres de pensée contredirait d’ailleurs l’un des arguments centraux du livre, développé au @sec:ch07 : toute procédure chargée d’auditer un cadre repose elle-même sur une spécification finie, et ne fait que reporter le problème un cran plus haut.",
     "Fournir une méta-procédure formelle garantissant la justesse de nos cadres de pensée contredirait d’ailleurs l’un des résultats centraux du livre, établi au @sec:ch07 : toute procédure chargée d’auditer un cadre repose elle-même sur une spécification finie, et ne fait que reporter la difficulté un cran plus haut."),
    ("derive", "énumération amputée (mathématicien, décideur)", AP,
     "Le propos touche toutefois des pratiques dont les préoccupations et les défenses naturelles diffèrent sensiblement : l’ingénieur qui chaîne des simulations multiphysiques, le statisticien ou le mathématicien attentif aux hypothèses de ses théorèmes, le concepteur de systèmes d’intelligence artificielle confronté aux frontières irrégulières de ses modèles, le décideur ou le responsable d’institution chargé d’organiser les revues, ou encore le destinataire non spécialiste à qui l’on remet un chiffre assuré pour trancher une décision.",
     "Le propos touche toutefois des métiers dont les contraintes et les défenses naturelles diffèrent sensiblement. Il concerne autant l’ingénieur qui chaîne des simulations multiphysiques que le statisticien attentif aux hypothèses de ses théorèmes, le concepteur de systèmes d’intelligence artificielle confronté aux frontières irrégulières de ses modèles, le responsable d’institution chargé d’organiser les revues, ou encore le destinataire non spécialiste à qui l’on remet un chiffre assuré pour trancher."),
    ("derive", "provenance sur-affirmée", AP,
     "Il serait tout aussi inexact d’effacer le rôle déterminant de la direction et du filtrage humains dans ce processus hybride.",
     "Pour autant, la conduite et le filtrage du travail sont restés humains d’un bout à l’autre."),
    # ---- faithful, useful edits (should be accepted) ----------------------
    ("controle-utile", "coupe à la conjonction", C0,
     "La dinde inductiviste qui note chaque matin l’heure à laquelle le fermier lui apporte son grain dispose, à la veille de Noël, d’une série statistique irréprochable ; la catastrophe qui l’attend ne vient pas d’une faute de calcul, mais d’une variable qui n’a jamais figuré dans son cadre.",
     "La dinde inductiviste qui note chaque matin l’heure à laquelle le fermier lui apporte son grain dispose, à la veille de Noël, d’une série statistique irréprochable. La catastrophe qui l’attend ne vient pas d’une faute de calcul, mais d’une variable absente de son cadre."),
    ("controle-utile", "coupe aux deux-points", C0,
     "Si la perte en cas de casse vaut vingt-cinq fois le gain d’une victoire, le seuil vaut 1/26, un peu moins de 4 % : M. X, qui évalue le risque à 5 %, choisit rationnellement le voilier renforcé, tandis que M. Y, qui l’évalue à 0,1 %, s’élance non moins rationnellement sur le voilier léger.",
     "Si la casse coûte vingt-cinq fois le gain d’une victoire, le seuil vaut 1/26, soit un peu moins de 4 %. M. X, qui évalue le risque à 5 %, choisit rationnellement le voilier renforcé, tandis que M. Y, à 0,1 %, s’élance non moins rationnellement sur le voilier léger."),
    ("controle-utile", "connecteur explicite", C0,
     "D’un côté à l’autre de l’interface, les nombres voyageaient nus, sans mention d’unité ; chaque impulsion était ainsi sous-estimée d’un facteur proche de 4,45 [@mco1999].",
     "D’un côté à l’autre de l’interface, les nombres voyageaient nus, sans unité, si bien que chaque impulsion était sous-estimée d’un facteur proche de 4,45 [@mco1999]."),
    ("controle-utile", "« Or » retiré, phrase resserrée", C0,
     "Or la spécification d’interface exigeait que ces impulsions soient exprimées dans l’unité du Système international, le newton-seconde, tandis que le programme les écrivait en livres-force-secondes, une unité anglo-saxonne.",
     "La spécification d’interface exigeait des newton-secondes, l’unité du Système international ; le programme écrivait des livres-force-secondes, une unité anglo-saxonne."),
    ("controle-utile", "tournure allégée", C0,
     "Une fonction de tri promet que, si on lui fournit une liste d’éléments comparables, elle rendra une permutation ordonnée de cette même liste ; le protocole TCP promet que les octets arriveront dans l’ordre ou qu’une erreur sera signalée.",
     "Une fonction de tri promet de rendre, pour toute liste d’éléments comparables, une permutation ordonnée de cette même liste ; le protocole TCP promet que les octets arriveront dans l’ordre ou qu’une erreur sera signalée."),
    ("controle-utile", "récit plus direct", C0,
     "Un collègue tente pourtant l’expérience le lendemain, chauffe son récipient à 101 °C et constate que rien ne bout : il a utilisé une eau fortement salée.",
     "Le lendemain, un collègue chauffe son récipient à 101 °C sans voir d’ébullition : il a utilisé une eau fortement salée."),
    ("controle-utile", "tournure plus directe", C0,
     "La commission d’enquête n’eut aucun mal à désigner la cause technique immédiate de la perte.",
     "La commission d’enquête identifia rapidement la cause technique immédiate de la perte."),
    ("controle-utile", "verbe précisé", C0,
     "Que signifie ce 5 % (ou ce 0,1 %) ? Il ne décrit pas une propriété physique de l’océan ni du mât.",
     "Que désigne ce 5 % (ou ce 0,1 %) ? Il ne s’agit ni d’une propriété physique de l’océan ni d’une caractéristique du mât."),
    # ---- faithful but gratuitous swaps (either verdict acceptable) --------
    ("controle-gratuit", "synonyme", C0,
     "Comparons deux organisations imaginaires, avec des chiffres choisis pour l’illustration :",
     "Comparons deux organisations fictives, avec des chiffres choisis pour l’illustration :"),
    ("controle-gratuit", "synonyme", C0,
     "Le passage critique a lieu lorsque nous décidons d’agir d’après ce que nous croyons.",
     "Le passage critique a lieu quand nous décidons d’agir d’après ce que nous croyons."),
    ("controle-gratuit", "synonyme", C0,
     "Que s’est-il passé entre la perte de la sonde martienne et ces deux scènes contemporaines ?",
     "Que s’est-il passé entre la perte de la sonde martienne et ces deux épisodes contemporains ?"),
    ("controle-gratuit", "mot retiré", C0,
     "Munis de cette grille de lecture, tournons-nous vers l’informatique.",
     "Munis de cette grille, tournons-nous vers l’informatique."),
]


# Second set: strictly faithful edits written for the check (pure splits, "Or" removed,
# emphasis italics removed, explicit connectives), mixed with four known drifts.
DRIFT_SAMPLE = {"probabilités (jugement → fréquence)", "portée (possibilité → certitude)",
                "terme (frontière en dents de scie)", "fait durci (doutes → alertes)"}
ITEMS_PROPRES = [it for it in ITEMS if it[1] in DRIFT_SAMPLE] + [
    ("controle-utile", "deux-points → point", C0,
     "Mais vis-à-vis de tout facteur omis par le cadre — la corrosion de la ferrure —, ces contrôles internes sont des copies les uns des autres : ils puisent tous à la même source et s’accorderont jusqu’à la troisième décimale tout en se trompant ensemble.",
     "Mais vis-à-vis de tout facteur omis par le cadre — la corrosion de la ferrure —, ces contrôles internes sont des copies les uns des autres. Ils puisent tous à la même source et s’accorderont jusqu’à la troisième décimale tout en se trompant ensemble."),
    ("controle-utile", "« Or » initial retiré, coupe", C0,
     "Or c’est là tout le nœud d’une décision unique, prise une seule fois et dont la réponse ne vient qu’après l’acte : le décideur compare au seuil la probabilité issue de sa propre représentation, tandis que le monde ne consulte pas ce chiffre.",
     "C’est là tout le nœud d’une décision unique, prise une seule fois et dont la réponse ne vient qu’après l’acte. Le décideur compare au seuil la probabilité issue de sa propre représentation, tandis que le monde ne consulte pas ce chiffre."),
    ("controle-utile", "deux-points → « Ainsi »", C0,
     "Ce passage en série est d’autant plus redoutable qu’il s’accompagne souvent d’un blanchiment des conditions : un champ de températures calculé sous dix hypothèses prudentes traverse une interface sous la forme d’un simple tableau de nombres nus, dépouillé de ses réserves, de ses barres d’erreur et parfois de ses unités, comme l’étaient les impulsions transmises à l’équipe de navigation de *Mars Climate Orbiter* [@mco1999].",
     "Ce passage en série est d’autant plus redoutable qu’il s’accompagne souvent d’un blanchiment des conditions. Ainsi, un champ de températures calculé sous dix hypothèses prudentes traverse une interface sous la forme d’un simple tableau de nombres nus, dépouillé de ses réserves, de ses barres d’erreur et parfois de ses unités, comme l’étaient les impulsions transmises à l’équipe de navigation de *Mars Climate Orbiter* [@mco1999]."),
    ("controle-utile", "italique d’emphase retirée, coupe", C0,
     "Dans cette opération, la garantie préalable n’a pas été perdue par négligence ; elle a été délibérément *dépensée* pour acheter une portée nouvelle, précisément sur les tâches rebelles à toute règle explicite.",
     "Dans cette opération, la garantie préalable n’a pas été perdue par négligence. Elle a été délibérément dépensée pour acheter une portée nouvelle, précisément sur les tâches rebelles à toute règle explicite."),
    ("controle-utile", "coupe au point-virgule", C0,
     "Personne n’avait jamais inscrit cette boucle de rétroaction sur les organigrammes ; aussi sa disparition, lorsqu’une réponse complète jaillit en quelques secondes d’une consigne, passe-t-elle inaperçue jusqu’au jour où une énormité traverse tout le processus.",
     "Personne n’avait jamais inscrit cette boucle de rétroaction sur les organigrammes. Aussi sa disparition, lorsqu’une réponse complète jaillit en quelques secondes d’une consigne, passe-t-elle inaperçue jusqu’au jour où une énormité traverse tout le processus."),
    ("controle-utile", "deux-points → « alors »", C0,
     "Mais pour les erreurs qui relèvent de l’angle mort du modèle lui-même, le producteur qui rédige avec l’aide du modèle et le contrôleur qui relit avec l’aide du même modèle puisent désormais à la même source : leur contrôle croisé dégénère en copie, et la probabilité d’échappement de ces erreurs partagées bondit.",
     "Mais pour les erreurs qui relèvent de l’angle mort du modèle lui-même, le producteur qui rédige avec l’aide du modèle et le contrôleur qui relit avec l’aide du même modèle puisent désormais à la même source. Leur contrôle croisé dégénère alors en copie, et la probabilité d’échappement de ces erreurs partagées bondit."),
    ("controle-utile", "deux-points → point, sujet explicite", AP,
     "Ce livre a une visée d’abord pratique : chercher comment agir au mieux sur le monde à travers une représentation finie, et comment bâtir des représentations et des procédures capables d’être démenties à temps lorsque nous nous trompons.",
     "Ce livre a une visée d’abord pratique. Il cherche comment agir au mieux sur le monde à travers une représentation finie, et comment bâtir des représentations et des procédures capables d’être démenties à temps lorsque nous nous trompons."),
    ("controle-utile", "« Or » → « pourtant »", AP,
     "Or le monde ne répond pas à notre représentation ; il répond à notre action.",
     "Le monde, pourtant, ne répond pas à notre représentation ; il répond à notre action."),
]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--cle", type=Path, required=True, help="where to write the answer key (outside the repo)")
    p.add_argument("--graine", type=int, default=7)
    p.add_argument("--jeu", choices=["pilotes", "propres"], default="pilotes",
                   help="pilotes: 38 edits from the pilots; propres: 8 strictly faithful edits + 4 known drifts")
    a = p.parse_args()
    global LOT
    items = ITEMS if a.jeu == "pilotes" else ITEMS_PROPRES
    if a.jeu == "propres":
        LOT = STYLE / "lots" / "_etalonnage2"

    originals = {f: (ROOT / "monographie" / "chapitres" / f"{f}.md").read_text(encoding="utf-8") for f in (C0, AP)}
    pilots = {f: (STYLE / "pilots" / f"{f}.md").read_text(encoding="utf-8") for f in (C0, AP)}
    register = dp.load_register()
    errors = []
    for kind, cat, f, avant, apres in items:
        if originals[f].count(avant) != 1:
            errors.append(f"avant introuvable ou ambigu ({cat}) : {avant[:60]}…")
        if a.jeu == "pilotes" and apres not in pilots[f]:
            errors.append(f"après absent du pilote ({cat}) : {apres[:60]}…")
    if errors:
        sys.exit("\n".join(errors))

    order = list(range(len(items)))
    random.Random(a.graine).shuffle(order)
    key, blocks = {}, []
    for n, idx in enumerate(order, start=1):
        kind, cat, f, avant, apres = items[idx]
        eid = f"E{n:02d}"
        key[eid] = {"type": kind, "categorie": cat, "chapitre": f}
        text = originals[f]
        lines = ae.analyse_lines(text)
        start = text.index(avant)
        line = ae.lines_for_span(lines, start, start + len(avant))[0]
        alerts = ae.soft_alerts(avant, apres, register)
        blocks += ["---", "", f"## {eid} — `monographie/chapitres/{f}.md`, § « {line['titre']} » (ligne {line['n']})", "",
                   "**Avant**", "", ae.quote(avant), "", "**Après**", "", ae.quote(apres), ""]
        if alerts:
            blocks += ["**Alertes automatiques :** " + " ; ".join(alerts), ""]

    LOT.mkdir(parents=True, exist_ok=True)
    head = [
        "# Dossier du juge — lot d’étalonnage",
        "",
        "- Chapitres d’origine : `monographie/chapitres/00-avant-propos.md` et `monographie/chapitres/00-cartographier.md` "
        "(non modifiés ; les numéros de ligne renvoient à ces fichiers ; les lire pour le contexte).",
        f"- Retouches soumises : **{len(items)}**, issues de plusieurs passes de réécriture, présentées dans le désordre.",
        f"- Consignes : `.claude/agents/juge-style.md`. Sortie attendue : `style/lots/{LOT.name}/verdicts.json`.",
        "- Les alertes automatiques sont des indices, pas des verdicts.",
        "",
    ]
    (LOT / "dossier_juge.md").write_text("\n".join(head + blocks) + "\n", encoding="utf-8")
    a.cle.parent.mkdir(parents=True, exist_ok=True)
    a.cle.write_text(json.dumps(key, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {k: sum(1 for v in key.values() if v["type"] == k) for k in ("derive", "derive-limite", "controle-utile", "controle-gratuit")}
    print(f"{LOT / 'dossier_juge.md'} : {len(items)} retouches {counts} ; clé : {a.cle}")


if __name__ == "__main__":
    main()
