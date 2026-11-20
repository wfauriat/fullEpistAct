#!/usr/bin/env python3
"""preparer_dossiers.py — vague 0 de la relecture intégrale.

Construit, à partir du livre compilé (monographie/build/livre.html), les dossiers
de lecture de chaque lecteur (texte rendu : renvois résolus, statuts affichés,
tableaux générés inclus, figures remplacées par leur légende), ainsi que des
pistes mécaniques destinées à la vague de vérification.

Usage (depuis la racine du dépôt, après `make html` dans monographie/) :
    python3 relecture/preparer_dossiers.py
Sorties :
    relecture/dossiers/   (régénérable, ignoré par git)
    relecture/pistes/     (pistes mécaniques : répétitions, termes)
"""
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
MONO = RACINE / "monographie"
ICI = RACINE / "relecture"
DOSS = ICI / "dossiers"
PISTES = ICI / "pistes"

FILTRE = """
function Image(el) return pandoc.Str("[Figure]") end
function Link(el) return el.content end
function RawInline(el) return {} end
function RawBlock(el) return {} end
"""

ROMAINS = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}


def rendre():
    filtre = DOSS / "_filtre.lua"
    filtre.write_text(FILTRE, encoding="utf-8")
    sortie = subprocess.run(
        ["pandoc", str(MONO / "build/livre.html"), "-f", "html",
         "-t", "markdown-raw_html-native_divs-native_spans-bracketed_spans-header_attributes-link_attributes",
         "--wrap=none", "--lua-filter", str(filtre)],
        check=True, capture_output=True, text=True).stdout
    return sortie.splitlines()


def cle_unite(titre):
    t = titre[2:].strip()
    if t.startswith("Avant-propos"):
        return "avant-propos"
    if t.startswith("Conclusion"):
        return "conclusion"
    if t.startswith("Bibliographie"):
        return "bibliographie"
    m = re.match(r"Partie (I|II|III|IV|V)\b", t)
    if m:
        return f"partie-{ROMAINS[m.group(1)]}"
    m = re.match(r"Annexe ([A-D])\b", t)
    if m:
        return f"annexe-{m.group(1)}"
    m = re.match(r"(\d+) ", t)
    if m:
        return f"ch{int(m.group(1)):02d}"
    return None


def decouper(lignes):
    unites, cle, cour = {}, None, []
    for l in lignes:
        if l.startswith("# "):
            if cle:
                unites[cle] = cour
            cle, cour = cle_unite(l), [l]
        elif cle:
            cour.append(l)
    if cle:
        unites[cle] = cour
    return unites


FENCE = re.compile(r"^:{3,}")
OUVRE = re.compile(r"^:{3,}\s*(\{[^}]*\}|[\w-]+)\s*:*\s*$")


def vue_lecteur(lignes):
    out = [l for l in lignes if not FENCE.match(l)]
    texte = "\n".join(out)
    texte = re.sub(r"\n{3,}", "\n\n", texte)
    return texte.strip() + "\n"


def classes(attr):
    if attr.startswith("{"):
        return set(re.findall(r"\.([\w-]+)", attr))
    return {attr}


def blocs(lignes):
    """Blocs de premier niveau : liste de (classes, lignes, debut, fin)."""
    res, pile = [], []
    for i, l in enumerate(lignes):
        m = OUVRE.match(l)
        if m:
            pile.append((classes(m.group(1)), i))
        elif FENCE.match(l) and pile:
            cl, debut = pile.pop()
            if not pile:
                res.append((cl, lignes[debut:i + 1], debut, i))
    return res


def hors_blocs(lignes):
    masque = [False] * len(lignes)
    for _, _, d, f in blocs(lignes):
        for k in range(d, f + 1):
            masque[k] = True
    return masque


def paragraphes(lignes, masque=None):
    """Paragraphes (texte courant) hors blocs : liste de (indice, texte)."""
    res, cour, debut = [], [], None
    for i, l in enumerate(lignes):
        dans = masque[i] if masque else False
        if dans or not l.strip() or l.startswith("#"):
            if cour:
                res.append((debut, " ".join(cour)))
            cour, debut = [], None
            continue
        if debut is None:
            debut = i
        cour.append(l.strip())
    if cour:
        res.append((debut, " ".join(cour)))
    return res


def section(lignes, titre_commence):
    for i, l in enumerate(lignes):
        if l.startswith("## ") and l[3:].startswith(titre_commence):
            fin = next((j for j in range(i + 1, len(lignes)) if lignes[j].startswith("## ")), len(lignes))
            return lignes[i:fin]
    return []


def intro(lignes):
    fin = next((j for j in range(1, len(lignes)) if lignes[j].startswith("## ")), len(lignes))
    return lignes[:fin]


def ecrire(nom, morceaux):
    texte = "\n\n".join(m.strip() for m in morceaux if m and m.strip()) + "\n"
    texte = re.sub(r"\n{3,}", "\n\n", texte)
    (DOSS / nom).write_text(texte, encoding="utf-8")
    return nom, len(texte)


def chapitres(u):
    return [k for k in sorted(u) if re.fullmatch(r"ch\d\d", k)]


def extrait_t1(cle, L):
    m = [L[0]]
    m += [l for l in L if l.startswith("## ")]
    m.append("")
    for cl, bl, _, _ in blocs(L):
        if cl & {"definition", "proposition", "nuance"}:
            m.append(vue_lecteur(bl))
    m += section(L, "Points clés")
    return "\n".join(m)


NOMBRE = re.compile(r"\d\s?%|\$")


def extrait_t2(cle, L):
    m = [L[0]]
    masque = hors_blocs(L)
    titres = {i: l for i, l in enumerate(L) if l.startswith("## ")}
    elements = []
    for cl, bl, d, _ in blocs(L):
        if cl & {"formel", "exemple-quantitatif", "outils", "definition", "proposition"}:
            elements.append((d, vue_lecteur(bl)))
    for i, p in paragraphes(L, masque):
        if NOMBRE.search(p):
            elements.append((i, p))
    elements += list(titres.items())
    for _, t in sorted(elements, key=lambda x: x[0]):
        m.append(t)
    return "\n\n".join(m)


def extrait_t5(cle, L):
    m = ["\n".join(intro(L))]
    masque = hors_blocs(L)
    paras = paragraphes(L, masque)
    for i, l in enumerate(L):
        if l.startswith("## ") and not l.startswith("## Points clés"):
            premier = next((p for j, p in paras if j > i), "")
            m.append(l + "\n\n" + premier)
    for cl, bl, _, _ in blocs(L):
        if "cas" in cl:
            m.append(vue_lecteur(bl))
    pc = next((i for i, l in enumerate(L) if l.startswith("## Points clés")), len(L))
    dernier = [p for j, p in paras if j < pc]
    if dernier:
        m.append("[Dernier paragraphe avant les points clés]\n\n" + dernier[-1])
    m.append("\n".join(section(L, "Points clés")))
    return "\n\n".join(m)


def pistes_repetitions(u):
    CAS = {
        "Mars Climate Orbiter": r"Mars Climate Orbiter|SM_FORCES",
        "Mata v. Avianca": r"Mata v\. Avianca|Avianca",
        "Challenger": r"Challenger",
        "METR": r"METR",
        "Knight Capital": r"Knight Capital",
        "Knight et Leveson": r"Knight et Leveson|programmation multiversion",
        "Air Canada / Moffatt": r"Air Canada|Moffatt",
        "Google Flu Trends": r"Google Flu|Flu Trends",
        "ferrure": r"ferrure",
        "course à la voile / régate": r"voilier|régate|course à la voile",
        "roulette russe": r"roulette russe",
        "dinde de Russell": r"dinde",
        "crise de 2008 / hypothécaire": r"hypothécaire|subprime|2008",
        "BCG / frontière en dents de scie": r"BCG|Boston Consulting|dents de scie",
        "Bainbridge": r"Bainbridge",
        "Akerlof": r"Akerlof",
    }
    ordre = ["avant-propos", "ch00"] + [k for k in chapitres(u) if k != "ch00"] + ["conclusion"]
    lignes = ["# Pistes mécaniques — répétitions en lecture linéaire", "",
              "Comptage brut des mentions des études de cas récurrentes par unité (texte rendu), puis paires de paragraphes",
              "de chapitres différents qui partagent une forte proportion de séquences de 6 mots. Ce sont des pistes, pas des constats.", "",
              "## Mentions par unité", "", "| Cas | " + " | ".join(ordre) + " |",
              "|" + " :-- |" * (len(ordre) + 1)]
    for nom, rx in CAS.items():
        r = re.compile(rx)
        cases = [str(len(r.findall("\n".join(u.get(k, []))))) or "0" for k in ordre]
        cases = [c if c != "0" else "·" for c in cases]
        lignes.append(f"| {nom} | " + " | ".join(cases) + " |")
    # Recouvrements de paragraphes
    paras = []
    for k in ordre:
        L = u.get(k, [])
        for i, p in paragraphes(L, hors_blocs(L)) + [(d, vue_lecteur(bl)) for _, bl, d, _ in blocs(L)]:
            mots = re.findall(r"\w+", p.lower())
            if len(mots) < 35:
                continue
            sh = {" ".join(mots[j:j + 6]) for j in range(len(mots) - 5)}
            paras.append((k, i, p, sh))
    index = defaultdict(set)
    for n, (_, _, _, sh) in enumerate(paras):
        for s in sh:
            index[s].add(n)
    paires = defaultdict(int)
    for s, ns in index.items():
        if len(ns) > 6:
            continue
        ns = sorted(ns)
        for a in range(len(ns)):
            for b in range(a + 1, len(ns)):
                if paras[ns[a]][0] != paras[ns[b]][0]:
                    paires[(ns[a], ns[b])] += 1
    trouves = []
    for (a, b), c in paires.items():
        r = c / min(len(paras[a][3]), len(paras[b][3]))
        if c >= 6 and r >= 0.12:
            trouves.append((r, c, a, b))
    trouves.sort(reverse=True)
    lignes += ["", f"## Paragraphes proches entre unités ({len(trouves)} paires, recouvrement ≥ 12 % et ≥ 6 séquences communes)", ""]
    for r, c, a, b in trouves[:80]:
        ka, _, pa, _ = paras[a]
        kb, _, pb, _ = paras[b]
        lignes += [f"### {ka} ↔ {kb} — recouvrement {r:.0%} ({c} séquences)", "",
                   f"- **{ka}** : « {pa[:500]}{'…' if len(pa) > 500 else ''} »",
                   f"- **{kb}** : « {pb[:500]}{'…' if len(pb) > 500 else ''} »", ""]
    (PISTES / "repetitions.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return len(trouves)


def pistes_termes():
    """Termes du registre : gras hors chapitre d'introduction ; emplois avant l'introduction."""
    reg = (MONO / "commun/registre_termes.md").read_text(encoding="utf-8")
    termes = []
    for l in reg.splitlines():
        cols = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cols) >= 4 and re.fullmatch(r"sec:ch\d\d", cols[3] or ""):
            for t in re.split(r",\s*", re.sub(r"\s*\([^)]*\)", "", cols[0])):
                if t:
                    termes.append((t, cols[3][4:]))
    fichiers = sorted((MONO / "chapitres").glob("*.md"))

    def ch_de(f):
        n = f.name
        if n.startswith("00-avant"):
            return "avant-propos"
        if n.startswith("99"):
            return "conclusion"
        return "ch" + n[:2]

    textes = {ch_de(f): (f, f.read_text(encoding="utf-8")) for f in fichiers}
    ordre = ["avant-propos", "ch00"] + sorted(k for k in textes if re.fullmatch(r"ch\d\d", k) and k != "ch00") + ["conclusion"]
    gras, avant = [], []
    for t, intro_ch in termes:
        motif = re.escape(t).replace(r"\ ", r"\s+").replace("’", "[’']")
        rgras = re.compile(r"\*\*" + motif + r"[sx]?\*\*", re.I)
        rmot = re.compile(r"(?<![\w-])" + motif + r"[sx]?(?![\w-])", re.I)
        for k in ordre:
            f, txt = textes[k]
            for m in rgras.finditer(txt):
                if k != intro_ch:
                    ligne = txt.count("\n", 0, m.start()) + 1
                    gras.append(f"- « {t} » (introduit au {intro_ch}) en gras dans `{f.name}:{ligne}`")
        if len(t.split()) < 2 and t.lower() in {"cadre", "contrôle", "historique", "calibration", "affirmation", "chaîne",
                                                 "comparateur", "représentation", "induction", "déduction", "sévérité",
                                                 "validation", "vérification", "blanchiment"}:
            mots_courants = True
        else:
            mots_courants = False
        for k in ordre:
            if k in ("avant-propos", "ch00") or k == intro_ch:
                continue
            if ordre.index(k) >= ordre.index(intro_ch):
                break
            f, txt = textes[k]
            occ = [txt.count("\n", 0, m.start()) + 1 for m in rmot.finditer(txt)]
            if occ:
                avant.append(f"- « {t} » (introduit au {intro_ch}){' [mot courant]' if mots_courants else ''} : "
                             f"`{f.name}` l. {', '.join(map(str, occ[:8]))}{' …' if len(occ) > 8 else ''}")
    lignes = ["# Pistes mécaniques — termes du registre", "",
              "Repérage automatique sur les sources. Pistes à confirmer : un mot courant employé dans son sens ordinaire n'est pas une faute.", "",
              f"## Termes en gras hors de leur chapitre d'introduction ({len(gras)})", ""] + (gras or ["(aucun)"]) + [
              "", f"## Emplois avant le chapitre d'introduction, hors avant-propos et ch. 0 ({len(avant)})", ""] + (avant or ["(aucun)"])
    (PISTES / "termes.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return len(gras), len(avant)


def main():
    DOSS.mkdir(parents=True, exist_ok=True)
    PISTES.mkdir(parents=True, exist_ok=True)
    u = decouper(rendre())
    manquants = [k for k in ["avant-propos", "ch00", "conclusion", "annexe-A", "annexe-B", "annexe-C", "annexe-D"]
                 + [f"partie-{i}" for i in range(1, 6)] + [f"ch{i:02d}" for i in range(19)] if k not in u]
    if manquants:
        sys.exit(f"unités introuvables : {manquants}")
    V = {k: vue_lecteur(L) for k, L in u.items()}
    tailles = []
    tailles.append(ecrire("reference_lecteur.md", [V["avant-propos"], V["annexe-B"], V["annexe-C"]]))
    groupes = {
        "P0_avant-propos_ch00.md": ["avant-propos", "ch00"],
        "P1_partie1.md": ["partie-1", "ch01", "ch02", "ch03", "ch04"],
        "P2_partie2.md": ["partie-2", "ch05", "ch06", "ch07", "ch08", "ch09"],
        "P3_partie3.md": ["partie-3", "ch10", "ch11", "ch12", "ch13"],
        "P4_partie4.md": ["partie-4", "ch14", "ch15", "ch16"],
        "P5_partie5_conclusion.md": ["partie-5", "ch17", "ch18", "conclusion"],
        "PA_annexes_A_D.md": ["annexe-A", "annexe-D"],
    }
    for nom, cles in groupes.items():
        tailles.append(ecrire(nom, [V[k] for k in cles]))
    chs = [k for k in chapitres(u) if k != "ch00"]
    parties = {int(k[-1]): V[k] for k in u if k.startswith("partie-")}
    debut_partie = {"ch01": 1, "ch05": 2, "ch10": 3, "ch14": 4, "ch17": 5}
    t1 = [V["ch00"]]
    t2 = [V["annexe-C"], V["annexe-D"]]
    t5 = [V["ch00"]]
    for k in chs:
        if k in debut_partie:
            t1.append(parties[debut_partie[k]])
            t5.append(parties[debut_partie[k]])
        t1.append(extrait_t1(k, u[k]))
        t2.append(extrait_t2(k, u[k]))
        t5.append(extrait_t5(k, u[k]))
    t1.append(V["conclusion"])
    t2.append(extrait_t2("conclusion", u["conclusion"]))
    t5.append(V["conclusion"])
    tailles.append(ecrire("T1_argument_statuts.md", t1))
    tailles.append(ecrire("T2_chiffres_modeles.md", t2))
    tailles.append(ecrire("T5_repetitions_lineaire.md", t5))
    # Lecteur cible : le livre entier, une unité par fichier, dans l'ordre de lecture.
    C = DOSS / "C_livre"
    C.mkdir(exist_ok=True)
    ordre_c = ["avant-propos", "ch00"]
    for k in chs:
        if k in debut_partie:
            ordre_c.append(f"partie-{debut_partie[k]}")
        ordre_c.append(k)
    ordre_c.append("conclusion")
    total_c = 0
    for n, k in enumerate(ordre_c):
        (C / f"{n:02d}_{k}.md").write_text(V[k], encoding="utf-8")
        total_c += len(V[k])
    tailles.append(("C_livre/ (" + str(len(ordre_c)) + " fichiers)", total_c))
    nrep = pistes_repetitions(u)
    ng, na = pistes_termes()
    print("Dossiers (caractères ; ≈ jetons à 3,5 car./jeton) :")
    for nom, n in tailles:
        print(f"  {nom:40s} {n:>8d}  ≈ {n / 3.5 / 1000:5.0f} k")
    print(f"Pistes : {nrep} paires de paragraphes proches ; termes : {ng} gras hors chapitre, {na} emplois anticipés")


if __name__ == "__main__":
    main()
