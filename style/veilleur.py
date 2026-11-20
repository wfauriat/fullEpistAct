#!/usr/bin/env python3
"""Hand-off between the rewriter (Gemini) and the orchestrator (Claude) — see style/PROTOCOLE.md.

Subcommands:
  declarer LOT     (rewriter) mark style/lots/<chapitre>/ as ready for review: checks that
                   propositions.yaml parses, then writes the PRET marker atomically with
                   the round number and the SHA-256 of propositions.yaml.
  attendre         (orchestrator, run in the background) wait until a lot is ready, claim
                   it (ETAT: en_revue), print "LOT_PRET <lot> tour=<n>" and exit 0.
  etat             status of every chapter's lot.
  liberer LOT      (orchestrator) release a lot claimed by mistake or after an incident
                   (removes ETAT if it says en_revue), so it can be picked up again.

A lot is picked up when PRET exists, its hash matches propositions.yaml (so a file
still being written is ignored) and it is not already claimed or applied. A lot in
state "erreur" is picked up again only once the rewriter declares a higher round.
Lots are taken in the book's order (monographie/livre.yaml).
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import re
import sys
import time
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LOTS = HERE / "lots"
LIVRE = ROOT / "monographie" / "livre.yaml"


def now() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read_yaml(p: Path) -> dict:
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return {}


def write_atomic(p: Path, data: dict) -> None:
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    tmp.replace(p)


def chapter_order() -> list[str]:
    return re.findall(r"chapitres/([\w.-]+)\.md", LIVRE.read_text(encoding="utf-8"))


def lots_in_order() -> list[Path]:
    order = chapter_order()
    rank = {name: i for i, name in enumerate(order)}
    found = [p for p in LOTS.iterdir() if p.is_dir()] if LOTS.exists() else []
    return sorted(found, key=lambda p: (rank.get(p.name, 999), p.name))


def ready_round(lot: Path) -> int | None:
    """Round number if the lot is declared ready and intact, else None."""
    pret, props = lot / "PRET", lot / "propositions.yaml"
    if not pret.exists() or not props.exists():
        return None
    marker = read_yaml(pret)
    if marker.get("sha256") != sha256_file(props):
        return None
    try:
        return int(marker.get("tour", 1))
    except (TypeError, ValueError):
        return None


def claimable(lot: Path) -> int | None:
    tour = ready_round(lot)
    if tour is None:
        return None
    etat = read_yaml(lot / "ETAT") if (lot / "ETAT").exists() else {}
    state = etat.get("etat")
    if state is None:
        return tour
    if state == "erreur" and tour > int(etat.get("tour") or 0):
        return tour
    return None


def cmd_declarer(lot: Path) -> None:
    props = lot / "propositions.yaml"
    if not props.exists():
        sys.exit(f"{props} introuvable")
    try:
        data = yaml.safe_load(props.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        sys.exit(f"propositions.yaml illisible : {e}")
    if not data.get("chapitre") or not isinstance(data.get("modifications"), list):
        sys.exit("propositions.yaml doit contenir « chapitre » et une liste « modifications »")
    etat = read_yaml(lot / "ETAT") if (lot / "ETAT").exists() else {}
    if etat.get("etat") in ("en_revue", "applique"):
        sys.exit(f"{lot.name} : lot déjà pris par l'orchestrateur (état {etat['etat']}) ; ne plus le modifier")
    previous = read_yaml(lot / "PRET").get("tour", 0) if (lot / "PRET").exists() else 0
    tour = max(int(previous or 0), int(etat.get("tour") or 0)) + 1
    write_atomic(lot / "PRET", {"chapitre": data["chapitre"], "tour": tour,
                                "sha256": sha256_file(props), "date": now(),
                                "modifications": len(data["modifications"])})
    print(f"{lot.name} : déclaré prêt pour la revue (tour {tour}, {len(data['modifications'])} retouche(s)).")


def cmd_attendre(interval: float) -> None:
    while True:
        for lot in lots_in_order():
            tour = claimable(lot)
            if tour is not None:
                write_atomic(lot / "ETAT", {"etat": "en_revue", "tour": tour, "date": now()})
                print(f"LOT_PRET {lot.relative_to(ROOT)} tour={tour}", flush=True)
                return
        time.sleep(interval)


def cmd_etat() -> None:
    lots = {p.name: p for p in lots_in_order()}
    print(f"{'chapitre':34} {'prêt':>6}  état")
    for name in chapter_order():
        lot = lots.get(name)
        if lot is None:
            print(f"{name:34} {'—':>6}  (pas de lot)")
            continue
        tour = ready_round(lot)
        etat = read_yaml(lot / "ETAT") if (lot / "ETAT").exists() else {}
        detail = etat.get("etat", "en attente du juge" if tour else "en rédaction")
        if etat.get("etat") == "applique":
            detail += f" — {etat.get('acceptees')} acceptée(s), {etat.get('rejetees_juge')} rejetée(s) par le juge, {etat.get('rejetees_controles')} par les contrôles"
        print(f"{name:34} {('t' + str(tour)) if tour else '—':>6}  {detail}")


def cmd_liberer(lot: Path) -> None:
    etat_p = lot / "ETAT"
    etat = read_yaml(etat_p) if etat_p.exists() else {}
    if etat.get("etat") != "en_revue":
        sys.exit(f"{lot.name} : rien à libérer (état {etat.get('etat')})")
    etat_p.unlink()
    print(f"{lot.name} : libéré.")


def main() -> None:
    p = argparse.ArgumentParser(description="Passage de relais entre rédacteur et orchestrateur (style/PROTOCOLE.md).")
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("declarer"); d.add_argument("lot", type=Path)
    a = sub.add_parser("attendre"); a.add_argument("--intervalle", type=float, default=20.0)
    sub.add_parser("etat")
    l = sub.add_parser("liberer"); l.add_argument("lot", type=Path)
    args = p.parse_args()
    if args.cmd == "declarer":
        cmd_declarer(args.lot.resolve())
    elif args.cmd == "attendre":
        cmd_attendre(args.intervalle)
    elif args.cmd == "etat":
        cmd_etat()
    else:
        cmd_liberer(args.lot.resolve())


if __name__ == "__main__":
    main()
