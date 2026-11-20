#!/usr/bin/env python3
"""Check and apply the style edits of one lot (see style/PROTOCOLE.md).

A lot is a folder style/lots/<chapitre>/ holding propositions.yaml, written by
the rewriter. Two subcommands:

  verifier  LOT   mechanical checks on every proposed edit; writes
                  verification.json, dossier_juge.md (what the judge reads) and
                  original.md (a frozen copy of the chapter). The rewriter may
                  run it to pre-check its own proposals.
  appliquer LOT   applies the edits accepted in verdicts.json to the chapter,
                  writes journal.md, rapport_portee.md (diff_portee.py) and ETAT.
                  Run by the orchestrator only. No model touches the chapter.

Hard checks (an edit failing one is rejected and never shown to the judge):
  - `avant` occurs exactly once in the chapter, spans at most one paragraph,
    and lies entirely in editable prose (not a heading, block fence, protected
    block, table, figure, display formula, comment or locked section);
  - no overlap with another edit; `apres` differs from `avant` and adds no
    structural line (heading, fence, table, figure, display formula);
  - identical cross-references, citation keys, identifiers, bold spans,
    inline formulas, inline code, footnote markers and numbers.
Soft alerts (passed to the judge as pointers, not verdicts): changes in counts
of register terms and of the word families tracked by diff_portee.py.

Usage:
  python3 style/appliquer_edits.py verifier  style/lots/00-cartographier
  python3 style/appliquer_edits.py appliquer style/lots/00-cartographier
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHAPITRES = ROOT / "monographie" / "chapitres"
sys.path.insert(0, str(HERE))
import diff_portee as dp  # noqa: E402

LOCKED_SECTIONS = {"sec:avant-propos-genese", "sec:conclusion-provenance"}
MOTIFS = {
    "phrase-longue", "rythme", "paragraphe", "deux-points", "or-initial", "italique",
    "antithese", "chapeau", "recit-repete", "formule-creuse", "sujet-abstrait",
    "calque", "pont-redondant", "autre",
}
STRUCT_LINE_RE = re.compile(r"^\s*(#|:::|\||!\[|\$\$|Table:|<!--)")
CROSSREF_TOKEN_RE = re.compile(r"(\[-)?@((?:%s):[\w.-]+)" % "|".join(dp.CROSSREF_PREFIXES))


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def now() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def write_etat(lot: Path, data: dict) -> None:
    write_atomic(lot / "ETAT", yaml.safe_dump(data, allow_unicode=True, sort_keys=False))


def read_etat(lot: Path) -> dict:
    p = lot / "ETAT"
    return read_yaml(p) if p.exists() else {}


def quote(text: str) -> str:
    return "\n".join("> " + l if l.strip() else ">" for l in text.split("\n"))


def norm_typo(s: str) -> str:
    return " ".join(s.replace("’", "'").replace(" ", " ").replace(" ", " ").split())


# --------------------------------------------------------------------------
# Which lines may be edited
# --------------------------------------------------------------------------

def analyse_lines(text: str) -> list[dict]:
    """For each line: offsets, reason it is not editable (None if editable), section."""
    out = []
    offset = 0
    stack: list[set[str]] = []
    locked_level: int | None = None
    in_math = in_code = False
    sec_key, sec_title = "(début)", "avant le premier titre"
    for n, line in enumerate(text.split("\n"), start=1):
        why = None
        s = line.strip()
        if s.startswith("```"):
            in_code, why = not in_code, "bloc de code"
        elif in_code:
            why = "bloc de code"
        elif not stack and line.startswith("#") and (m := dp.HEADING_RE.match(line)):
            level, title = len(m.group(1)), m.group(2).strip()
            idm = re.search(r"#([^\s}]+)", m.group(3) or "")
            key = idm.group(1) if idm else "titre:" + title
            if locked_level is not None and level <= locked_level:
                locked_level = None
            if key in LOCKED_SECTIONS:
                locked_level = level
            sec_key, sec_title, why = key, title, "titre"
        elif mo := dp.DIV_OPEN_RE.match(line):
            classes = set(re.findall(r"\.([\w-]+)", mo.group(2) or "")) if mo.group(2) is not None else {mo.group(3)}
            stack.append(classes)
            why = "balise de bloc"
        elif dp.DIV_CLOSE_RE.match(line) and stack:
            stack.pop()
            why = "balise de bloc"
        elif in_math:
            # a display formula may close on a line that does not start with $$,
            # e.g. "\end{aligned}$$ {#eq:…}"
            if "$$" in s:
                in_math = False
            why = "formule centrée"
        elif s.startswith("$$"):
            if s.count("$$") == 1:
                in_math = True
            why = "formule centrée"
        elif any(c & dp.PROTECTED for c in stack):
            why = "bloc protégé (" + ", ".join(sorted(set().union(*stack) & dp.PROTECTED)) + ")"
        elif s.startswith("|"):
            why = "tableau"
        elif s.startswith("Table:"):
            why = "légende de tableau"
        elif s.startswith("!["):
            why = "figure"
        elif s.startswith("<!--"):
            why = "commentaire"
        elif locked_level is not None:
            why = "section verrouillée (provenance, réservée à l'auteur)"
        out.append({"n": n, "start": offset, "end": offset + len(line), "why": why,
                    "sec": sec_key, "titre": sec_title})
        offset += len(line) + 1
    return out


def lines_for_span(lines: list[dict], start: int, end: int) -> list[dict]:
    return [l for l in lines if l["end"] >= start and l["start"] < end]


# --------------------------------------------------------------------------
# Invariants
# --------------------------------------------------------------------------

def _strip_code(x: str) -> str:
    return re.sub(r"`[^`]*`", " ", x)


EXTRACTORS = {
    "renvois": lambda x: [(bool(a), b) for a, b in CROSSREF_TOKEN_RE.findall(x)],
    "clés de citation": lambda x: dp.CITE_KEY_RE.findall(_strip_code(x)),
    "identifiants": lambda x: re.findall(r"\{[^}]*?#([^\s}]+)", x),
    "mises en gras": lambda x: dp.BOLD_RE.findall(x),
    "formules en ligne": lambda x: [" ".join(m.split()) for m in re.findall(r"\$([^$\n]+)\$", x)],
    "code en ligne": lambda x: re.findall(r"`[^`]*`", x),
    "appels de note": lambda x: re.findall(r"\[\^[^\]]+\]", x),
    "nombres": lambda x: dp.NUM_RE.findall(dp.clean_numbers(x)),
}


def _fmt(items: list) -> str:
    return ", ".join(f"{'[-' if isinstance(i, tuple) and i[0] else ''}{i[1] if isinstance(i, tuple) else i}" for i in items)


def hard_invariants(avant: str, apres: str) -> list[str]:
    reasons = []
    for label, fn in EXTRACTORS.items():
        removed, added = dp.multiset_diff(fn(avant), fn(apres))
        if removed or added:
            parts = []
            if removed:
                parts.append("retirés : " + _fmt(removed))
            if added:
                parts.append("ajoutés : " + _fmt(added))
            reasons.append(f"{label} modifiés ({' ; '.join(parts)})")
    if any(STRUCT_LINE_RE.match(l) for l in apres.split("\n")):
        reasons.append("l'après introduit une ligne de structure (titre, bloc, tableau, figure, formule centrée)")
    return reasons


def soft_alerts(avant: str, apres: str, register) -> list[str]:
    alerts = []
    ow, nw = dp.clean_words(avant), dp.clean_words(apres)
    for name, rx in register:
        a, b = len(rx.findall(ow)), len(rx.findall(nw))
        if a != b:
            alerts.append(f"terme du registre « {name} » : {a} → {b}")
    for fam, rxs in dp.COMPILED.items():
        for label, rx in rxs.items():
            a, b = len(rx.findall(ow)), len(rx.findall(nw))
            if a != b:
                alerts.append(f"{fam} — {label} : {a} → {b}")
    return alerts


# --------------------------------------------------------------------------
# verifier
# --------------------------------------------------------------------------

def load_lot(lot: Path) -> tuple[dict, Path]:
    prop_path = lot / "propositions.yaml"
    if not prop_path.exists():
        sys.exit(f"{prop_path} introuvable")
    try:
        props = read_yaml(prop_path)
    except yaml.YAMLError as e:
        sys.exit(f"propositions.yaml illisible (YAML) : {e}")
    ch = str(props.get("chapitre", "")).strip()
    if not ch:
        sys.exit("propositions.yaml : champ « chapitre » manquant")
    chap = CHAPITRES / f"{ch.removesuffix('.md')}.md"
    if not chap.exists():
        sys.exit(f"chapitre introuvable : {chap}")
    if not isinstance(props.get("modifications"), list):
        sys.exit("propositions.yaml : « modifications » doit être une liste")
    return props, chap


def verifier(lot: Path) -> dict:
    etat = read_etat(lot)
    if etat.get("etat") == "applique":
        sys.exit(f"{lot} : lot déjà appliqué, vérification refusée (original.md serait écrasé)")
    props, chap = load_lot(lot)
    text = chap.read_text(encoding="utf-8")
    lines = analyse_lines(text)
    register = dp.load_register()
    results, spans, seen_ids = [], [], set()

    for i, m in enumerate(props["modifications"], start=1):
        mid = str(m.get("id") or f"{i:03d}")
        avant = str(m.get("avant") or "").strip()
        apres = str(m.get("apres") or "").strip()
        motif = str(m.get("motif") or "").strip()
        r = {"id": mid, "statut": "ok", "raisons": [], "alertes": [], "motif": motif,
             "avant": avant, "apres": apres}
        if mid in seen_ids:
            r["raisons"].append("identifiant en double")
        seen_ids.add(mid)
        if not avant or not apres:
            r["raisons"].append("« avant » ou « apres » vide")
        elif avant == apres:
            r["raisons"].append("aucun changement")
        if motif and motif not in MOTIFS:
            r["alertes"].append(f"motif non répertorié : {motif}")
        if avant:
            count = text.count(avant)
            if count == 0:
                hint = ""
                if norm_typo(avant) and norm_typo(avant) in norm_typo(text):
                    hint = " (le texte existe à la typographie près : copier exactement apostrophes ’ et espaces)"
                r["raisons"].append("« avant » introuvable dans le chapitre" + hint)
            elif count > 1:
                r["raisons"].append(f"« avant » apparaît {count} fois : l'étendre pour qu'il soit unique")
            else:
                start = text.index(avant)
                end = start + len(avant)
                r["debut"], r["fin"] = start, end
                touched = lines_for_span(lines, start, end)
                r["ligne"] = touched[0]["n"]
                r["section"], r["titre_section"] = touched[0]["sec"], touched[0]["titre"]
                if re.search(r"\n[ \t]*\n", avant):
                    r["raisons"].append("« avant » couvre plus d'un paragraphe")
                bad = [l for l in touched if l["why"]]
                if bad:
                    r["raisons"].append(f"zone non modifiable : {bad[0]['why']} (ligne {bad[0]['n']})")
                for other_id, s, e in spans:
                    if start < e and s < end:
                        r["raisons"].append(f"chevauche la retouche {other_id}")
                        break
                if not r["raisons"]:
                    spans.append((mid, start, end))
        if avant and apres and avant != apres:
            r["raisons"].extend(hard_invariants(avant, apres))
            r["alertes"].extend(soft_alerts(avant, apres, register))
        if r["raisons"]:
            r["statut"] = "rejete"
            spans[:] = [s for s in spans if s[0] != mid]
        results.append(r)

    ok = [r for r in results if r["statut"] == "ok"]
    rel = lot.relative_to(ROOT) if lot.is_relative_to(ROOT) else lot
    report = {
        "lot": str(rel),
        "chapitre": chap.stem,
        "fichier": str(chap.relative_to(ROOT)),
        "tour": props.get("tour"),
        "redacteur": props.get("redacteur"),
        "date": now(),
        "sha256_chapitre": sha256_bytes(text.encode("utf-8")),
        "sha256_propositions": sha256_bytes((lot / "propositions.yaml").read_bytes()),
        "modifications": results,
    }
    write_atomic(lot / "verification.json", json.dumps(report, ensure_ascii=False, indent=2))
    write_atomic(lot / "original.md", text)
    write_atomic(lot / "dossier_juge.md", dossier(rel, chap, ok, len(results)))
    print(f"{rel} : {len(results)} retouche(s) proposée(s), {len(ok)} soumise(s) au juge, "
          f"{len(results) - len(ok)} rejetée(s) par les contrôles.")
    for r in results:
        if r["statut"] == "rejete":
            print(f"  ✗ {r['id']} : " + " ; ".join(r["raisons"]))
    return report


def dossier(lot: Path, chap: Path, ok: list[dict], total: int) -> str:
    out = [
        f"# Dossier du juge — `{chap.stem}`",
        "",
        f"- Chapitre d'origine, figé au moment de la vérification : `{lot}/original.md` "
        "(les numéros de ligne renvoient à ce fichier ; le lire pour le contexte).",
        f"- Retouches soumises : **{len(ok)}** (sur {total} proposées ; "
        f"{total - len(ok)} écartées par les contrôles mécaniques).",
        "- Consignes : `.claude/agents/juge-style.md`. Sortie attendue : "
        f"`{lot}/verdicts.json`, un verdict par retouche ci-dessous.",
        "- Les alertes automatiques sont des indices, pas des verdicts.",
        "",
    ]
    for r in ok:
        out += [
            "---",
            "",
            f"## {r['id']} — § « {r['titre_section']} » (ligne {r['ligne']})",
            "",
            "**Avant**",
            "",
            quote(r["avant"]),
            "",
            "**Après**",
            "",
            quote(r["apres"]),
            "",
        ]
        if r["alertes"]:
            out.append("**Alertes automatiques :** " + " ; ".join(r["alertes"]))
            out.append("")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# appliquer
# --------------------------------------------------------------------------

def norm_verdict(v: str) -> str:
    v = (v or "").strip().lower().replace("é", "e")
    if v.startswith("accept"):
        return "accepte"
    if v.startswith("rejet") or v.startswith("refus"):
        return "rejete"
    return "?"


def appliquer(lot: Path) -> None:
    etat = read_etat(lot)
    if etat.get("etat") == "applique":
        sys.exit(f"{lot} : déjà appliqué")
    ver_path, verd_path = lot / "verification.json", lot / "verdicts.json"
    if not ver_path.exists() or not verd_path.exists():
        sys.exit("verification.json et verdicts.json sont requis")
    ver = json.loads(ver_path.read_text(encoding="utf-8"))
    if sha256_bytes((lot / "propositions.yaml").read_bytes()) != ver["sha256_propositions"]:
        sys.exit("propositions.yaml a changé depuis la vérification : relancer « verifier » puis le juge")
    chap = ROOT / ver["fichier"]
    text = chap.read_text(encoding="utf-8")
    if sha256_bytes(text.encode("utf-8")) != ver["sha256_chapitre"]:
        sys.exit(f"{chap} a changé depuis la vérification : relancer « verifier » puis le juge")
    try:
        verdicts_doc = json.loads(verd_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"verdicts.json illisible : {e}")
    verdicts = {str(v.get("id")): v for v in verdicts_doc.get("verdicts", [])}

    applied, judge_rejected, no_verdict = [], [], []
    for r in ver["modifications"]:
        if r["statut"] != "ok":
            continue
        v = verdicts.get(r["id"])
        if v is None or norm_verdict(v.get("verdict")) == "?":
            no_verdict.append(r)
        elif norm_verdict(v.get("verdict")) == "accepte":
            assert text[r["debut"]:r["fin"]] == r["avant"], f"position incohérente pour {r['id']}"
            applied.append((r, v))
        else:
            judge_rejected.append((r, v))

    new = text
    for r, _ in sorted(applied, key=lambda x: x[0]["debut"], reverse=True):
        new = new[: r["debut"]] + r["apres"] + new[r["fin"]:]
    write_atomic(chap, new)

    mech_rejected = [r for r in ver["modifications"] if r["statut"] != "ok"]
    write_atomic(lot / "journal.md", journal(ver, verdicts_doc, applied, judge_rejected, no_verdict, mech_rejected))
    report, _, sev = dp.render(lot / "original.md", chap)
    write_atomic(lot / "rapport_portee.md", report + "\n")
    write_etat(lot, {
        "etat": "applique",
        "tour": ver.get("tour"),
        "date": now(),
        "proposees": len(ver["modifications"]),
        "rejetees_controles": len(mech_rejected),
        "acceptees": len(applied),
        "rejetees_juge": len(judge_rejected),
        "sans_verdict": len(no_verdict),
        "sha256_chapitre_apres": sha256_bytes(new.encode("utf-8")),
    })
    print(f"{chap.relative_to(ROOT)} : {len(applied)} retouche(s) appliquée(s), {len(judge_rejected)} rejetée(s) par le juge, "
          f"{len(mech_rejected)} par les contrôles, {len(no_verdict)} sans verdict. "
          f"Rapport de portée : {sev['⛔']} ⛔, {sev['⚠']} ⚠.")


def journal(ver, verdicts_doc, applied, judge_rejected, no_verdict, mech_rejected) -> str:
    out = [
        f"# Journal de la passe de style — `{ver['chapitre']}`",
        "",
        f"- Appliqué le {now()} ; rédacteur : {ver.get('redacteur') or '?'} ; juge : {verdicts_doc.get('juge') or '?'} ; tour {ver.get('tour')}",
        f"- Proposées : {len(ver['modifications'])} · appliquées : {len(applied)} · rejetées par le juge : {len(judge_rejected)} "
        f"· rejetées par les contrôles : {len(mech_rejected)} · sans verdict : {len(no_verdict)}",
        "- Original figé : `original.md` ; rapport de portée : `rapport_portee.md` (indices pour la relecture).",
        "- Revenir au texte d'origine d'un chapitre : `git checkout main -- <fichier du chapitre>`.",
        "",
        f"## Retouches appliquées ({len(applied)})",
        "",
    ]
    for r, v in applied:
        out += [f"### {r['id']} — § « {r['titre_section']} » (ligne {r['ligne']}) — {r.get('motif') or 'motif ?'}", "",
                "Avant :", "", quote(r["avant"]), "", "Après :", "", quote(r["apres"]), ""]
        if v.get("raison"):
            out += [f"*Juge :* {v['raison']}", ""]
    out += [f"## Rejetées par le juge ({len(judge_rejected)})", ""]
    for r, v in judge_rejected:
        dims = ", ".join(v.get("dimensions") or [])
        out += [f"### {r['id']} — § « {r['titre_section']} » (ligne {r['ligne']}) — {dims or 'dimension ?'}", "",
                f"*Juge :* {v.get('raison') or '(sans raison)'}", "",
                "Avant :", "", quote(r["avant"]), "", "Après (non appliqué) :", "", quote(r["apres"]), ""]
    if no_verdict:
        out += [f"## Sans verdict, non appliquées ({len(no_verdict)})", ""]
        out += [f"- {r['id']} (ligne {r['ligne']})" for r in no_verdict] + [""]
    out += [f"## Rejetées par les contrôles mécaniques ({len(mech_rejected)})", ""]
    for r in mech_rejected:
        out.append(f"- **{r['id']}** : " + " ; ".join(r["raisons"]))
    return "\n".join(out) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(description="Vérifie et applique les retouches d'un lot de la passe de style.")
    p.add_argument("action", choices=["verifier", "appliquer"])
    p.add_argument("lot", type=Path, help="dossier style/lots/<chapitre>")
    a = p.parse_args()
    lot = a.lot.resolve()
    if a.action == "verifier":
        verifier(lot)
    else:
        appliquer(lot)


if __name__ == "__main__":
    main()
