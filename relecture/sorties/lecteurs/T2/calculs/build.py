import json
D=open('/home/ai-user/Documents/Sandbox/review_epist_ag/relecture/dossiers/T2_chiffres_modeles.md',encoding='utf-8').read()
C=[]
def add(unite,section,passage,cat,grav,constat,prop,conf):
    C.append(dict(id="T2-%03d"%(len(C)+1),unite=unite,section=section,passage=passage,categorie=cat,gravite=grav,constat=constat,proposition=prop,confiance=conf))

add("ch09","9.5","pour *contrôle franchi*, qui correspond à l'événement noté $D$ au chapitre","terminologie","B",
"L'événement C est défini comme « un contrôle la contredit et l'arrête avant l'action », donc comme une détection suivie d'effet, ce qui correspond bien à D du chapitre 6. La glose « contrôle franchi » dit l'inverse : un contrôle franchi est un contrôle que l'erreur a passé. La suite confirme que C̄ est l'échappement (Pr(C̄|E) = probabilité d'échappement), ce qui rend la glose contradictoire avec la définition. Un lecteur qui lit « franchi » inversera C et C̄ dans les équations (9.3) et au chapitre 16.",
"Remplacer par « (pour *contrôle réussi*, événement noté $D$ au chapitre 6) » ou supprimer la parenthèse.","haute")

add("ch09","Points clés","Le risque réel est le produit du taux d'erreur et de la probabilité d'échappement","terminologie","B",
"Le corps du chapitre 9 nomme R = P(E)(1 − s u) le « risque résiduel » et précise que c'est « au sens de la fiabilité des contrôles ». L'annexe C et le chapitre 17 réservent « risque réel » à p_w = 1 − (1 − p)(1 − z), grandeur différente (risque dans le monde en présence d'un facteur omis). Les points clés du chapitre 9 emploient « risque réel » pour R : le même terme désigne deux grandeurs, et le lecteur qui arrive au chapitre 17 les confondra.",
"Écrire « Le risque résiduel est le produit… ».","haute")

add("annexe-D","","Conformément au principe de source unique posé dans l'avant-propos","dependance","B",
"L'annexe D renvoie à un « principe de source unique » censé être posé dans l'avant-propos. L'avant-propos de la référence ne contient rien de tel : il dit seulement que les paramètres des exemples sont récapitulés dans l'annexe D et qu'ils ont une valeur illustrative. Le renvoi est donc à vide (ou l'avant-propos a perdu la phrase correspondante). Le lecteur ne sait pas ce que ce principe engage (génération mécanique des figures et tableaux, règle de cohérence ?).",
"Énoncer le principe dans l'avant-propos (une phrase), ou reformuler l'annexe D sans renvoi.","haute")

add("annexe-D","D.4","probabilité d'oubli du contrôleur pair lors d'un contrôle croisé à chaque étape","chiffres","C",
"L'annexe D.4 note p = 6 % deux fois, pour deux grandeurs distinctes : l'erreur indépendante par étape et l'oubli du pair. Le chapitre 8 utilise pour le second m (« m = p = 6 % »), qui est la lettre prévue par l'annexe C pour le taux d'oubli. De plus, l'annexe C réserve p à la probabilité d'échec estimée par le décideur (chapitre 4) : p est donc employé avec trois sens (estimation du décideur, erreur par étape, oubli du pair).",
"Écrire m = 6 % pour l'oubli du pair dans D.4 et signaler dans l'annexe C que p désigne aussi l'erreur par étape au chapitre 8.","moyenne")

add("transversal","","remplacer $U$ par $\\alpha\\, U + \\beta$, avec $\\alpha > 0$","chiffres","C",
"Plusieurs lettres changent de sens d'un chapitre à l'autre sans que l'annexe C le signale : α est le niveau d'erreur de la prédiction conforme (ch. 2) puis le facteur d'échelle de l'utilité (ch. 4) ; D est le défaut (ch. 1), l'événement « erreur détectée » (ch. 6), puis « l'état recherché » (9.1) ; A est l'ensemble des conditions énoncées (ch. 1-2) puis l'accord du comparateur (ch. 9) ; E est l'indice observé (ch. 1), l'ensemble des arêtes (ch. 2), puis l'événement « affirmation fausse » (ch. 6-9) ; f est un taux de fausses alertes (ch. 9) mais aussi la prévision f_θ, f_1, f_2 (ch. 5, 7, 13) ; C est un événement de contrôle (ch. 9) et C_j des conditions (ch. 6). Chaque usage est local et lisible, mais l'accumulation gêne le lecteur qui relit l'annexe C.",
"Ajouter à l'annexe C une mention « lettre à usage local » pour ces cas, ou renommer les plus gênants (α du chapitre 4, D de 9.1).","moyenne")

add("ch05","5.4","Tout énoncé quantitatif d'incertitude résume à quel point les membres d'un ensemble spécifié d'alternatives admises sont en désaccord.","argument","B",
"L'énoncé réduit toute incertitude à un désaccord entre alternatives. Or l'équation (5.1) a deux termes : le second est bien un désaccord entre alternatives, mais le premier, E_θ[Var(Y|θ)], est la dispersion interne à chaque alternative (section 5.2 : « la dispersion des issues qu'elle continue de juger possibles »). Même si toutes les alternatives s'accordent, ce terme subsiste. Le titre « n'est qu'un désaccord mesuré » est donc plus fort que la décomposition qui sert de preuve ; ce qui est établi, c'est que l'incertitude est calculée à l'intérieur de Θ.",
"Remplacer « résume à quel point… sont en désaccord » par « résume la dispersion calculée à l'intérieur d'un ensemble spécifié d'alternatives admises (dispersion interne et désaccord entre alternatives) ».","moyenne")

add("ch05","5.4","région de prédiction conforme ou borne au pire cas sur $\\Theta$ --- reste par construction une fonctionnelle définie sur le seul ensemble $\\Theta$ des alternatives admises","argument","B",
"Le noyau formel range la région de prédiction conforme parmi les mesures qui seraient des fonctionnelles définies sur Θ. Mais la section 2.4 présente la prédiction conforme comme valable « sans aucune hypothèse sur la forme de leur loi », sous la seule hypothèse d'échangeabilité : il n'y a pas d'ensemble Θ de modèles pondérés. La cécité de cette méthode vient de l'échangeabilité (qui relève du cadre), non d'un calcul sur Θ. L'affirmation « par construction » est donc invérifiable telle quelle pour cet exemple et contredit la lecture du chapitre 2.",
"Retirer la région conforme de l'énumération, ou écrire qu'elle reste relative à l'hypothèse d'échangeabilité, laquelle fait partie du cadre (section 2.4).","moyenne")

add("ch16","16.1","Seul un comparateur qui se trompe autrement abaisse le plancher.","argument","B",
"Le plancher d'échappement sous examen complet vaut 1 − s = c + (1 − c)m. Il baisse aussi quand le contrôleur devient plus vigilant (m plus petit) à c constant, ce que le texte montre lui-même juste après : dans « Indépendant et précis » le plancher passe de 28,0 % à 19,0 % par la seule baisse de m (de 20 % à 10 %). L'intertitre est donc trop fort : seule la part c du plancher exige un comparateur qui se trompe autrement ; la part (1 − c)m se réduit par la vigilance.",
"« Seul un comparateur qui se trompe autrement abaisse la part incompressible c du plancher. »","haute")

add("ch17","17.1","C'est la seconde voie décrite au chapitre","structure","C",
"L'ordre des deux voies d'entrée d'une pertinence nouvelle n'est pas stable. Le chapitre 17 appelle « seconde voie » la découverte par l'épreuve ; le chapitre 16.2 les cite dans l'ordre inverse (« découvrir par l'épreuve… et être averti ») ; le chapitre 13 écrit « par l'avertissement d'un tiers ou par l'épreuve du réel ». Le lecteur ne peut pas savoir laquelle est la première.",
"Fixer l'ordre (avertissement d'abord, épreuve ensuite, comme au chapitre 13) et l'utiliser partout.","moyenne")

add("ch17","17.1","on obtient quatre issues","clarte","C",
"Le texte annonce quatre issues, puis une phrase ajoutée après la liste en introduit une cinquième étiquette (« renoncement justifié »). Le tableau 17.2 affiche bien cinq issues distinctes, la figure 17.1 parle de « quatre issues » et le noyau formel de quatre quadrants. Ce sont quatre quadrants et cinq étiquettes ; la formulation « quatre issues » induit en erreur à la lecture du tableau.",
"« on obtient quatre cas (quatre quadrants), le troisième portant deux étiquettes : »","haute")

add("ch17","17.1","L'encadré suivant explique pourquoi cette règle, d'apparence rigoureuse, est contradictoire.","structure","B",
"Le texte principal propose de décider sur p_w, annonce que cette règle est contradictoire, et renvoie l'explication à un encadré. Or l'avant-propos pose qu'aucun encadré d'approfondissement ne porte seul une étape indispensable du raisonnement. Si l'encadré en question est facultatif, l'argument qui écarte la règle « décider sur p_w » manque au fil principal ; le lecteur linéaire reste avec une règle plausible et une assertion non justifiée.",
"Donner l'argument en deux phrases dans le texte (p_w dépend de z, que le décideur ne peut pas estimer, hypothèse 2 du modèle M2).","moyenne")

add("ch17","17.1","le deuxième des modèles formels du livre, présentés à la section","terminologie","C",
"Le modèle de décision est utilisé dès le chapitre 4 sans nom, puis nommé M2 au chapitre 17, alors que M3 (chapitre 7) et M1 (chapitre 8) ont déjà été rencontrés. La numérotation M1, M2, M3 ne suit pas l'ordre de lecture (chapitres 8, 4, 7), ce qui surprend le lecteur linéaire. L'annexe D parle de « modèle M2 » dès le chapitre 4.",
"Nommer M2 dès la section 4.2, ou expliquer en une phrase que la numérotation suit la section 0.7 et non l'ordre des chapitres.","basse")

add("ch01","1.5","un signal normal la multiplie par 0,294, ce qui revient à la diviser par moins de 5","chiffres","C",
"Le calcul est juste mais imprécis : 1/0,294 = 3,4. « Moins de 5 » est vrai de tout nombre inférieur à 5 et ne renseigne pas le lecteur ; la comparaison utile est que le signal normal divise la cote par 3,4 là où le signal anormal la multiplie par 5.",
"« ce qui revient à la diviser par 3,4 seulement ».","haute")

add("annexe-D","D.6","6e date","chiffres","C",
"Dans l'annexe D.6, la sixième date de l'exemple est notée « 6e date », alors que le chapitre 12 la nomme « le 5 mars » dans la mise en place et « une autre date » dans le tableau 12.1. Trois libellés pour une même ligne. Les chiffres sont cohérents (22+20+18+16+14+10 = 100 %).",
"Harmoniser : « 5 mars 10 % » dans les deux endroits, ou « autre date 10 % ».","haute")

add("ch06","6.3","quelqu'un prend acte d'un éventuel désaccord et ait l'autorité nécessaire pour suspendre ou corriger l'action.","francais","C",
"Rupture de mode dans la liste des événements : « prend acte » (indicatif) coordonné à « ait » (subjonctif) dépendant de la même proposition, alors que les autres éléments ne comportent pas de subjonctif (« parvient », « existe »).",
"« quelqu'un prend acte d'un éventuel désaccord et a l'autorité nécessaire… ».","haute")

add("ch12","12.4","Mercure (qui, restant plus près du Soleil, est en moyenne dans le temps la planète la plus proche de la Terre (Stockman, Monroe, et Cordner 2019), contrairement à l'idée reçue qui confond distance minimale au rapprochement et distance moyenne)","clarte","C",
"Phrase à trois niveaux de parenthèses. L'idée (Mercure est en moyenne la plus proche de la Terre, Vénus ne l'étant qu'au rapprochement minimal) est déterminante pour tout l'exemple, mais elle est enfouie dans une incise difficile à suivre.",
"Sortir l'explication de la parenthèse dans une phrase séparée, avec la référence.","moyenne")

add("annexe-C","","Notations employées dans l'ouvrage.","autre","C",
"La table des notations omet des symboles employés dans les calculs de façon constante : Λ (rapport de vraisemblance, chapitre 1), S(p) (surprise), VPP (valeur prédictive positive), R (risque résiduel, chapitre 9), 𝔼 et Var (chapitre 5), U_sûr, U_succès, U_échec. L'avant-propos présente pourtant l'annexe C comme le moyen de retrouver chaque notation et le chapitre qui l'introduit. Elle ne mentionne pas non plus que p désigne aussi l'erreur par étape au chapitre 8 et que z est employé de façon informelle dès le chapitre 5.",
"Compléter la table (Λ, S, VPP, R, 𝔼/Var) et ajouter une note sur l'usage de p et de z.","moyenne")

for c in C:
    assert c["passage"] in D, (c["id"], c["passage"][:60])
    assert len(c["passage"])<=300,(c["id"],len(c["passage"]))
json.dump(C,open('/home/ai-user/Documents/Sandbox/review_epist_ag/relecture/sorties/lecteurs/T2/constats.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print(len(C))
