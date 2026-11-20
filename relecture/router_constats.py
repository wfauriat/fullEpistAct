#!/usr/bin/env python3
"""router_constats.py — passage de la vague 1 à la vague 2 de la relecture intégrale.

Rassemble les constats des lecteurs (relecture/sorties/lecteurs/*/constats.json),
les contrôle, et les répartit en lots de vérification par partie du livre.

Usage (depuis la racine du dépôt) :
    python3 relecture/router_constats.py
Sorties :
    relecture/sorties/verification/entrees/V0.json … V5.json, VX.json
    relecture/sorties/verification/entrees/hors_perimetre.md  (§ 3 et § 4 des bilans)
    relecture/sorties/verification/entrees/STATS.md
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ICI = Path(__file__).resolve().parent
LECT = ICI / "sorties/lecteurs"
SORTIE = ICI / "sorties/verification/entrees"

LOTS = {
    "V0": {"avant-propos", "ch00"},
    "V1": {"partie-1", "ch01", "ch02", "ch03", "ch04"},
    "V2": {"partie-2", "ch05", "ch06", "ch07", "ch08", "ch09"},
    "V3": {"partie-3", "ch10", "ch11", "ch12", "ch13"},
    "V4": {"partie-4", "ch14", "ch15", "ch16"},
    "V5": {"partie-5", "ch17", "ch18", "conclusion"},
}
CHAMPS = ["id", "unite", "section", "passage", "categorie", "gravite", "constat", "proposition", "confiance"]


def normaliser_unite(u):
    u = (u or "").strip().lower().replace("chapitre ", "ch").replace("chap. ", "ch")
    m = re.fullmatch(r"ch\.?\s*(\d{1,2})", u)
    if m:
        return f"ch{int(m.group(1)):02d}"
    m = re.fullmatch(r"partie[- ]?(\d)", u)
    if m:
        return f"partie-{m.group(1)}"
    m = re.fullmatch(r"annexe[- ]?([a-d])", u)
    if m:
        return f"annexe-{m.group(1).upper()}"
    return u


def lot_de(unite):
    for lot, unites in LOTS.items():
        if unite in unites:
            return lot
    return "VX"


def main():
    SORTIE.mkdir(parents=True, exist_ok=True)
    lots = defaultdict(list)
    stats, problemes, hors = [], [], []
    for d in sorted(p for p in LECT.iterdir() if p.is_dir()):
        lecteur = d.name
        f = d / "constats.json"
        if not f.exists():
            problemes.append(f"{lecteur} : pas de constats.json")
            continue
        try:
            constats = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            problemes.append(f"{lecteur} : JSON invalide ({e})")
            continue
        grav = Counter()
        for i, c in enumerate(constats, 1):
            manquants = [k for k in CHAMPS if k not in c]
            if manquants:
                problemes.append(f"{lecteur} #{i} : champs manquants {manquants}")
            c = {k: c.get(k, "") for k in CHAMPS}
            if not str(c["id"]).startswith(lecteur):
                c["id"] = f"{lecteur}-{i:03d}"
            c["lecteur"] = lecteur
            c["unite"] = normaliser_unite(c["unite"])
            grav[c["gravite"]] += 1
            lots[lot_de(c["unite"])].append(c)
        stats.append((lecteur, len(constats), grav))
        b = d / "bilan.md"
        if b.exists():
            t = b.read_text(encoding="utf-8")
            m = re.search(r"^## 3\..*?(?=^## 5\.|\Z)", t, re.S | re.M)
            if m:
                hors.append(f"# {lecteur}\n\n{m.group(0).strip()}\n")
        else:
            problemes.append(f"{lecteur} : pas de bilan.md")
    for lot in list(LOTS) + ["VX"]:
        (SORTIE / f"{lot}.json").write_text(json.dumps(lots.get(lot, []), ensure_ascii=False, indent=1), encoding="utf-8")
    (SORTIE / "hors_perimetre.md").write_text(
        "# Ce que les lecteurs ont pris sur parole, et leurs questions hors périmètre\n\n" + "\n".join(hors), encoding="utf-8")
    lignes = ["# Constats de la vague 1", "", "| Lecteur | Constats | A | B | C |", "| :-- | --: | --: | --: | --: |"]
    for lecteur, n, g in stats:
        lignes.append(f"| {lecteur} | {n} | {g.get('A', 0)} | {g.get('B', 0)} | {g.get('C', 0)} |")
    lignes += ["", "| Lot | Constats |", "| :-- | --: |"] + [f"| {l} | {len(lots.get(l, []))} |" for l in list(LOTS) + ["VX"]]
    if problemes:
        lignes += ["", "## Problèmes de format", ""] + [f"- {p}" for p in problemes]
    (SORTIE / "STATS.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("\n".join(lignes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
