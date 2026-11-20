# Bilan — T2

## 1. Ce que j'ai compris

Le livre soutient que l'on agit toujours d'après une représentation finie (un cadre) et que le monde répond à l'action, non à la représentation. Les nombres produits dans un cadre (probabilités, barres d'erreur) sont des jugements relatifs à ce cadre. La règle de décision de Savage donne un seuil p* = 1/(1 + L/ΔU) qui s'effondre quand les enjeux sont démesurés. Les barres d'erreur ne mesurent que la dispersion à l'intérieur de l'ensemble des alternatives admises, donc rien de ce que le cadre omet (facteur z). Tous les contrôles calculés dans le cadre en sont des copies : cause commune. Le modèle M1 quantifie cela. Une chaîne en série cumule les angles morts. Un contrôle croisé les réduit au produit des oublis, mais il laisse intact un facteur omis partagé (q). Le modèle du contrôleur (ch. 9 et 16) combine sensibilité s = (1 − c)(1 − m), fausses alertes f, VPP et prise en compte u, avec risque = taux d'erreur × échappement. Il montre qu'un producteur plus exact peut accompagner un contrôle devenu décoratif quand les angles morts se corrèlent (modèle partagé). Le modèle M2 ajoute le risque réel p_w = 1 − (1 − p)(1 − z) et une marge d'humilité b, avec quatre quadrants de décision. Le fil est cohérent et les exemples chiffrés servent bien le propos.

## 2. Impression d'ensemble

Forces : les chiffres sont d'une exactitude remarquable. J'ai recalculé toute la matière quantitative disponible (tableaux 1.1, 3.1, 4.1, 8.2, 9.1-9.4, 12.1, 14.1, 16.1, 17.2, annexe D, formules du texte courant) sans trouver une seule erreur de calcul ni d'arrondi, ni d'écart entre un chapitre, l'annexe D et la conclusion. Les valeurs reprises (1,93 % contre 5,57 %, 0,9 % contre 0,1 %, 68,3 % et 42,2 %, 8,09 %, etc.) concordent partout. Les dérivations (Bayes par cotes, score logarithmique, seuil p*, loi de la variance totale) sont justes. Les hypothèses des modèles sont énoncées avant usage et les limites des exemples sont dites.

Problèmes, par ordre d'importance (aucun n'est une erreur de calcul) :
1. Termes quantitatifs qui dérivent : « risque réel » désigne R au chapitre 9 (points clés) et p_w au chapitre 17 et dans l'annexe C (T2-002) ; la glose « contrôle franchi » inverse le sens de l'événement C (T2-001).
2. Énoncés plus forts que leur preuve : la proposition 1 réduit l'incertitude à un désaccord alors que le terme aléatoire de (5.1) n'en est pas un (T2-006) ; la région conforme est classée comme fonctionnelle sur Θ, contre le chapitre 2 (T2-007) ; l'intertitre « Seul un comparateur… abaisse le plancher » ignore l'effet de m, que le texte montre lui-même (T2-008).
3. Renvoi à vide vers un « principe de source unique » de l'avant-propos (T2-003) ; explication essentielle renvoyée à un encadré au chapitre 17 (T2-011).
4. Lettres à plusieurs sens et annexe C incomplète : p, α, D, A, E, f ; Λ, VPP, R, S absents (T2-004, T2-005, T2-017).
5. Retouches de lisibilité : quatre issues, cinq étiquettes (T2-010) ; ordre des deux voies d'entrée de la pertinence (T2-009).

## 3. Ce que j'ai dû prendre sur parole

- L'exemple de la ferrure et son coefficient de sécurité de 1,8 (ch. 5), repris aux chapitres 7 et 13 : je n'ai pas le texte du chapitre 5 qui l'introduit, seulement les reprises concordantes.
- Le « modèle clinique examiné à la section 2.4 » (renvoi du chapitre 7.3) : la section 2.4 de mon dossier ne contient que le noyau formel.
- Le chapitre 0, dont l'annexe D dit que le calcul « produit taux d'erreur × échappement » apparaît en ouverture (section 0.5.4) : absent de mon dossier, je n'ai pu vérifier la concordance qu'avec le chapitre 9.
- Les paragraphes sans nombre ni formule, filtrés de mon dossier (cas Challenger, sections 7.5, 8.4, 10.2 à 10.4, etc.), dont dépendent plusieurs renvois (section 6.5, 7.5, 13.2.2).
- Les références bibliographiques (Kalai et Vempala, Stockman et al., Mayo, Bliss et al., etc.) et les faits historiques (Mars Climate Orbiter, facteur 4,45 ; date du 23 septembre 1999 ; ébullition vers 85 °C au mont Blanc) : plausibles, non vérifiés.

## 4. Questions hors périmètre

- La section 0.7 présente-t-elle M1, M2, M3 dans cet ordre, et la section 0.5.4 le calcul du dépistage ou du produit des taux ? (T2-012)
- Quel est l'encadré qui explique la contradiction de la règle « décider sur p_w » (ch. 17), et est-il facultatif ? (T2-011)
- L'avant-propos complet de la version imprimée contient-il le « principe de source unique » ? (T2-003)
- Le chapitre 5 définit-il la ferrure et son coefficient de 1,8 comme les chapitres 7 et 13 le supposent ?
- Les sections 13.2 et 13.2.2 existent-elles telles que le chapitre 15 les cite ?

## 5. Limites de ma lecture

Mon dossier est un extrait : seuls les paragraphes contenant un nombre ou une formule, les blocs formels et les tableaux y figurent. Je n'ai donc pas lu les transitions ni les argumentations littéraires (chapitres 6, 10, 11, 13, 15, 18 pour l'essentiel), et je ne juge pas la clarté globale des chapitres. Mes constats de langue et de structure sont incidents. Un défaut qui tiendrait à un paragraphe sans nombre m'a échappé par construction. Les figures ne sont pas visibles (seulement leurs légendes) ; je n'ai pas pu contrôler que les courbes ou les barres correspondent aux tableaux.
