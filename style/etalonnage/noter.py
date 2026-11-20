#!/usr/bin/env python3
"""Score the judge's verdicts on the calibration lot against the answer key.

Usage:
  python3 style/etalonnage/noter.py --cle /chemin/hors/depot/cle.json [--sortie style/etalonnage/resultats.md]
"""

from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOT = HERE.parent / "lots" / "_etalonnage"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--cle", type=Path, required=True)
    p.add_argument("--sortie", type=Path, default=HERE / "resultats.md")
    p.add_argument("--lot", default="_etalonnage")
    a = p.parse_args()
    global LOT
    LOT = HERE.parent / "lots" / a.lot
    key = json.loads(a.cle.read_text(encoding="utf-8"))
    doc = json.loads((LOT / "verdicts.json").read_text(encoding="utf-8"))
    verdicts = {str(v["id"]): v for v in doc.get("verdicts", [])}

    def verdict(eid: str) -> str:
        v = (verdicts.get(eid, {}).get("verdict") or "?").lower().replace("é", "e")
        return "accepte" if v.startswith("accept") else "rejete" if v.startswith("rejet") else "?"

    groups = {"derive": [], "derive-limite": [], "controle-utile": [], "controle-gratuit": []}
    for eid, info in key.items():
        groups[info["type"]].append((eid, info, verdict(eid), verdicts.get(eid, {})))

    def count(items, want):
        return sum(1 for _, _, v, _ in items if v == want)

    d, dl, cu, cg = groups["derive"], groups["derive-limite"], groups["controle-utile"], groups["controle-gratuit"]
    lines = [
        "# Étalonnage du juge — résultats",
        "",
        f"- Date : {datetime.date.today().isoformat()} ; juge : {doc.get('juge')}",
        "- Jeu : dérives réelles des pilotes de première passe, et retouches fidèles tirées des mêmes pilotes (`construire.py`).",
        "",
        "| Groupe | Attendu | Résultat |",
        "| :-- | :-- | :-- |",
        f"| Dérives nettes ({len(d)}) | rejet | **{count(d, 'rejete')}/{len(d)} rejetées** |",
        f"| Dérives limites ({len(dl)}) | rejet souhaité | {count(dl, 'rejete')}/{len(dl)} rejetées |",
        f"| Retouches fidèles et utiles ({len(cu)}) | acceptation | **{count(cu, 'accepte')}/{len(cu)} acceptées** |",
        f"| Échanges gratuits de synonymes ({len(cg)}) | l’un ou l’autre | {count(cg, 'accepte')} acceptés, {count(cg, 'rejete')} rejetés |",
        "",
        "## Détail",
        "",
        "| Id | Type | Catégorie | Verdict | Raison du juge |",
        "| :-- | :-- | :-- | :-- | :-- |",
    ]
    for eid in sorted(key):
        info = key[eid]
        v = verdict(eid)
        expected_reject = info["type"].startswith("derive")
        miss = (expected_reject and v != "rejete") or (info["type"] == "controle-utile" and v != "accepte")
        mark = " ✗" if miss else ""
        raison = (verdicts.get(eid, {}).get("raison") or "").replace("|", "/").replace("\n", " ")
        lines.append(f"| {eid} | {info['type']} | {info['categorie']} | {v}{mark} | {raison} |")
    a.sortie.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[5:11]))
    misses = [l for l in lines if l.endswith("|") and " ✗ |" in l]
    if misses:
        print("\nÉcarts :")
        print("\n".join(misses))
    print(f"\n→ {a.sortie}")


if __name__ == "__main__":
    main()
