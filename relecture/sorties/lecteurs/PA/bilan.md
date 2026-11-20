# Bilan — PA

## 1. Ce que j'ai compris
Les annexes A et D forment l'aide-mémoire formel du livre. L'annexe A rassemble la logique (déduction, induction, règles à arrière-plan tacite), la révision bayésienne par cotes et rapports de vraisemblance, le taux de base et la valeur prédictive positive, le score logarithmique de surprise, le seuil de décision p* et le modèle M2 (risque réel et marge d'humilité), la décomposition de la variance, le modèle M3 (un contrôle interne au cadre ne dit rien d'une erreur due à un facteur omis, Λ = 1), le modèle M1 (cinq conditions de détection, chaînes et contrôles croisés, échappement et risque résiduel, réinterrogatoire), les triplets de Hoare et la signalisation coûteuse. Le fil : une représentation finie ne peut pas se contrôler de l'intérieur ; seuls des contrôles qui se trompent autrement, qui arrivent à temps et qui sont pris en compte réduisent le risque. L'annexe D donne les paramètres des exemples chiffrés, illustratifs, et leurs résultats.

## 2. Impression d'ensemble
Forces : toutes les formules que j'ai refaites sont justes (cotes, VPP, loi de la variance totale, seuil p*, p_w, chaînes en série, sévérité sur k tirages). Je n'ai trouvé aucune erreur de calcul dans les tableaux D.1 à D.7 (tous recalculés : 17,2 %, 55,6 %, 6,85 %, 86,2 % ; 3,00 / 6,91 ; 21,9 / 1,43 / 4,39 / 24,3 / 4,24 / 7,11 / 68,3 / 42,2 ; les douze lignes du tableau D.5 ; 2/13 ; 11/12 ; 99,9 / 42,0 / 11,5 %). Le style est sobre et les renvois aux sections et équations sont nombreux.
Problèmes, par importance :
1. Classification des régimes de M2 incomplète et incohérente avec D.3 (PA-001).
2. Collisions de notation et de terminologie sur plusieurs symboles, fragilisant l'autosuffisance (PA-007, PA-008, PA-010, PA-011, PA-012, PA-013).
3. Paramètres de D.3 non décrits et contradiction sur « les trois situations » du chapitre 4 (PA-005, PA-006).
4. Indépendance de l'accord A et de l'erreur e en M3 non établie si f1 comporte un tirage (PA-002).
5. Renvoi à un « principe de source unique » absent de l'avant-propos (PA-003) ; ambiguïté échappement / risque résiduel (PA-009).

## 3. Ce que j'ai dû prendre sur parole
- Les définitions numérotées (définitions 2, 8, 9, 10 ; propositions 1, 3, 5) et les numéros d'équations (1.1 à 17.2) auxquels l'annexe renvoie.
- Le contenu des sections 9.1 à 9.5, 12.4, 14.2.3, 15.3, 16.1, 17.1 et des tableaux 4.1, 8.2, 9.1 à 9.4, 12.1, 14.1, 16.1, 17.1, 17.2.
- La correspondance des intitulés « Contrôle entre pairs », « Un modèle pour tous », etc., avec les chapitres 9 et 16.
- Le contenu de la proposition 3 telle que l'énonce le chapitre 7 (A.6 en est un résumé).

## 4. Questions hors périmètre
- Quelles sont les trois situations du chapitre 4 (tableau 4.1) ? (PA-005)
- L'avant-propos complet ou un autre chapitre énonce-t-il le « principe de source unique » ? (PA-003)
- Le chapitre 7 définit-il f1 comme déterministe sachant x ? (PA-002)
- Y a-t-il des exemples chiffrés aux chapitres 5, 7, 13 ou 18 dont les paramètres devraient figurer en D ?
- Les chapitres 4 et 17 emploient-ils la même liste de régimes que A.4.2 ?
- L'attribution à Akerlof de l'équilibre mélangeant au chapitre 15 (PA-014).

## 5. Limites de ma lecture
Je n'ai lu que les annexes A et D et le dossier de référence (avant-propos, glossaire, notation). Je n'ai pas pu vérifier les renvois aux chapitres ni les tableaux d'origine. La typographie TeX a été jugée sur la conversion Markdown, donc sans le rendu final. Les contrôles numériques ont été faits par calcul direct et ne portent que sur les valeurs affichées.
