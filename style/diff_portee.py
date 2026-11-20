#!/usr/bin/env python3
"""Meaning-drift check for the style pass (style/STYLE_PASS_SPEC.md, §6.3).

Compares an original chapter with its rewritten version, section by section
(aligned on the {#sec:...} identifiers, which the style pass may not change),
and writes a Markdown report for the author. It lists:

  - hedges and modals, absolute quantifiers and epistemic-status words that were
    added, removed or reworded around (§6.2, invariant 6);
  - numbers changed in the prose;
  - register terms (monographie/commun/registre_termes.md) and bold spans whose
    counts changed (§2, invariant 2);
  - content words (>= 7 letters) lost, and those added;
  - citation keys moved between sections (§2, invariant 3);
  - protected blocks (.formel, .outils, .proposition, .definition,
    .exemple-quantitatif) that are not identical (§1);
  - structural invariants for the whole file: identifiers, cross-references,
    citation keys, statut attributes, sections (§2, invariant 1).

Every flagged item gets a task-list checkbox followed by "décision :". The author
ticks it and writes "accepté" or "rétabli". `--controle RAPPORT` exits with
status 1 while any box is unticked, so it can gate a merge.

The script cannot read meaning: it points at the places where meaning is most
likely to have moved. A clean report is necessary, not sufficient.

Usage:
  python3 style/diff_portee.py ORIGINAL.md REECRIT.md            # writes style/rapports/diff_portee_<nom>.md
  python3 style/diff_portee.py ORIGINAL.md REECRIT.md --stdout
  python3 style/diff_portee.py ORIGINAL.md REECRIT.md --out R.md --force
  python3 style/diff_portee.py --controle style/rapports/diff_portee_00-cartographier.md
"""

from __future__ import annotations

import argparse
import bisect
import datetime
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRE = ROOT / "monographie" / "commun" / "registre_termes.md"
RAPPORTS = Path(__file__).resolve().parent / "rapports"

PROTECTED = {"formel", "outils", "proposition", "definition", "exemple-quantitatif"}
CROSSREF_PREFIXES = ("sec", "prop", "def", "eq", "fig", "tbl")

# Marker families (§6.3). Patterns are applied case-insensitively to cleaned prose.
FAMILIES: dict[str, dict[str, str]] = {
    "Modaux et atténuateurs": {
        "pouvoir (peut, pourrait…)": r"\b(?:peut|peuvent|pourrait|pourraient|puisse|puissent|pouvait|pouvaient|pourra|pourront)\b",
        "tendre à": r"\btend(?:ent|ait|aient|re)?\s+à\b",
        "souvent / le plus souvent": r"\bsouvent\b",
        "en général / généralement": r"\ben général\b|\bgénéralement\b",
        "rarement": r"\brarement\b",
        "parfois": r"\bparfois\b",
        "en principe": r"\ben principe\b",
        "probablement / sans doute": r"\bprobablement\b|\bsans doute\b",
        "presque / quasi / à peu près / environ": r"\bpresque\b|\bquasi\b|\bà peu près\b|\benviron\b",
        "guère": r"\bguère\b",
        "en partie / partiellement": r"\ben partie\b|\bpartiellement\b",
    },
    "Quantificateurs absolus": {
        "tout / tous / toute(s)": r"\btout(?:e|es|s)?\b",
        "aucun(e)": r"\baucun(?:e|s|es)?\b",
        "jamais": r"\bjamais\b",
        "toujours": r"\btoujours\b",
        "rien": r"\brien\b",
        "nul(le)": r"\bnul(?:le|s|les)?\b",
        "seul(e) / seulement / uniquement": r"\bseul(?:e|s|es|ement)?\b|\buniquement\b",
        "nécessairement / strictement / absolument": r"\bnécessairement\b|\bstrictement\b|\babsolument\b",
        "entièrement / totalement / complètement / intégralement": r"\bentièrement\b|\btotalement\b|\bcomplètement\b|\bintégralement\b",
        "d'un bout à l'autre": r"\bd'un bout à l'autre\b",
    },
    "Force de l'affirmation": {
        "suffire": r"\b(?:in)?suffi(?:t|re|ra|ront|rait|raient|s(?:e|es|ent|ait|aient|ant|ante|antes|ants)?)\b",
        "garantir (verbe)": r"\bgaranti(?:t|r|ssent|ra|ront|rait|raient|ssait)\b",
        "impossible / impossibilité": r"\bimpossib\w*",
        "forcément / inévitablement / certainement / évidemment": r"\bforcément\b|\binévitablement\b|\bcertainement\b|\bévidemment\b|\bindéniablement\b",
    },
    "Lecture des probabilités": {
        "probable / probabilité": r"\bprobab(?:le|les|ilité|ilités|ilistes?)\b",
        "fréquent / fréquence": r"\bfréquen\w*",
        "vraisemblable / vraisemblance": r"\bvraisembl\w*",
    },
    "Statut épistémique": {
        "montrer": r"\bmontr(?:e|ent|er|é|ée|és|ées|ait|aient|ons)\b",
        "établir": r"\bétabli(?:t|r|e|s|es|ssent|ssons|ssait)?\b",
        "démontrer / prouver": r"\bdémon(?:tr|str)\w*|\bprouv\w*|\bpreuves?\b",
        "suggérer / indiquer": r"\bsugg[èé]r\w*|\bindiqu\w*",
        "argument": r"\bargument(?:s|e|ent|é)?\b",
        "résultat": r"\brésultats?\b",
        "hypothèse": r"\bhypothèses?\b",
        "constat": r"\bconstats?\b",
        "théorie / théorème": r"\bthéori\w*|\bthéorèmes?\b",
    },
}
COMPILED = {
    fam: {item: re.compile(pat, re.IGNORECASE) for item, pat in items.items()}
    for fam, items in FAMILIES.items()
}
ALL_MARKERS = [rx for items in COMPILED.values() for rx in items.values()]

# Connectives and other long function words: their loss is a style matter.
STOPWORDS = {
    "lorsque", "lorsqu", "puisque", "puisqu", "pourtant", "toutefois", "désormais",
    "ensuite", "quelques", "quelque", "plusieurs", "beaucoup", "simplement",
    "également", "notamment", "cependant", "néanmoins", "ailleurs", "encore",
    "pourquoi", "comment", "jusqu", "jusque", "quoique", "dorénavant", "aussitôt",
    "autrement", "davantage", "d'ailleurs", "c'est-à-dire", "celle-ci", "celui-ci",
    "ceux-ci", "celles-ci", "lui-même", "elle-même", "eux-mêmes", "elles-mêmes",
    "lesquels", "lesquelles", "laquelle", "auxquels", "desquels", "chacune",
}

LETTER = "A-Za-zÀ-ÖØ-öø-ÿŒœÆæ"
WORD_RE = re.compile(rf"[{LETTER}]+(?:[-'][{LETTER}]+)*")
NUM_RE = re.compile(r"\d+(?:[  ]\d{3})*(?:,\d+)?")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*(\{[^}]*\})?\s*$")
DIV_OPEN_RE = re.compile(r"^(:{3,})\s*(?:\{([^}]*)\}|([\w-]+))\s*$")
DIV_CLOSE_RE = re.compile(r"^:{3,}\s*$")
CITE_KEY_RE = re.compile(r"@([A-Za-z][\w-]*)(?![\w:-])")
CROSSREF_RE = re.compile(r"@((?:%s):[\w.-]+)" % "|".join(CROSSREF_PREFIXES))
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
SUFFIXES = ("aient", "èrent", "ions", "iez", "ent", "ait", "ais", "ées", "ée", "és", "es", "s", "x", "e")


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

@dataclass
class Section:
    key: str
    title: str
    prose: list[str] = field(default_factory=list)
    blocks: list[tuple[str, str]] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n".join(self.prose)


def _norm_block(lines: list[str]) -> str:
    return " ".join("\n".join(lines).split())


def parse(path: Path) -> dict[str, Section]:
    """Split a chapter into sections keyed by heading identifier.

    Lines inside protected blocks are kept apart (compared verbatim); all other
    lines, including the text of .cas, .nuance and .question blocks and the
    titre="…" of block openings, count as prose.
    """
    cur = Section("(début)", "avant le premier titre")
    sections: dict[str, Section] = {cur.key: cur}
    stack: list[set[str]] = []
    prot: tuple[str, list[str]] | None = None
    in_code = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if not in_code:
            if not stack:
                m = HEADING_RE.match(line)
                if m:
                    title = m.group(2).strip()
                    idm = re.search(r"#([^\s}]+)", m.group(3) or "")
                    key = idm.group(1) if idm else "titre:" + title
                    base, n = key, 2
                    while key in sections:
                        key, n = f"{base} ({n})", n + 1
                    cur = Section(key, title)
                    sections[key] = cur
                    continue
            mo = DIV_OPEN_RE.match(line)
            if mo:
                attrs = mo.group(2) or ""
                classes = set(re.findall(r"\.([\w-]+)", attrs)) if mo.group(2) is not None else {mo.group(3)}
                stack.append(classes)
                if prot is not None:
                    prot[1].append(line)
                elif classes & PROTECTED:
                    prot = (sorted(classes & PROTECTED)[0], [line])
                else:
                    titre = re.search(r'titre="([^"]*)"', attrs)
                    if titre:
                        cur.prose.append(titre.group(1))
                continue
            if DIV_CLOSE_RE.match(line) and stack:
                stack.pop()
                if prot is not None:
                    prot[1].append(line)
                    if not any(c & PROTECTED for c in stack):
                        cur.blocks.append((prot[0], _norm_block(prot[1])))
                        prot = None
                continue
        if prot is not None:
            prot[1].append(line)
        else:
            cur.prose.append(line)
    return {k: s for k, s in sections.items() if k != "(début)" or any(l.strip() for l in s.prose) or s.blocks}


# --------------------------------------------------------------------------
# Text helpers
# --------------------------------------------------------------------------

def _strip_markup(text: str) -> str:
    t = text.replace("’", "'")
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)(\{[^}]*\})?", r"\1", t)
    t = re.sub(r"\[[^\]]*@[^\]]*\]", " ", t)
    t = re.sub(r"-?@[\w:.-]+", " ", t)
    t = re.sub(r"\{[^}]*\}", " ", t)
    t = re.sub(r"`[^`]*`", " ", t)
    return t


def clean_words(text: str) -> str:
    """Prose without math, references, attributes or Markdown punctuation."""
    t = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    t = re.sub(r"\$[^$\n]*\$", " ", t)
    t = _strip_markup(t)
    t = re.sub(r"[*_|#>]", " ", t)
    return t


def clean_numbers(text: str) -> str:
    """Prose with math kept (normalised) so numbers in formulas are compared."""
    t = text.replace("{,}", ",").replace("\\,", "").replace("\\%", "%")
    return _strip_markup(t)


def words_with_pos(text: str) -> list[tuple[int, int, str]]:
    return [(m.start(), m.end(), m.group(0).lower()) for m in WORD_RE.finditer(text)]


def stem(w: str) -> str:
    for suf in SUFFIXES:
        if w.endswith(suf) and len(w) - len(suf) >= 5:
            return w[: -len(suf)]
    return w


def snippet(text: str, start: int, end: int, span: int = 10) -> str:
    """About `span` words either side of [start, end), with the match in bold."""
    before = WORD_RE.findall(text[:start])[-span:]
    after = WORD_RE.findall(text[end:])[:span]
    lead = "… " if len(WORD_RE.findall(text[:start])) > span else ""
    tail = " …" if len(WORD_RE.findall(text[end:])) > span else ""
    match = " ".join(text[start:end].split())
    return f"{lead}{' '.join(before)} **{match}** {' '.join(after)}{tail}".strip()


# --------------------------------------------------------------------------
# Comparisons
# --------------------------------------------------------------------------

def marker_windows(text: str, rx: re.Pattern) -> list[tuple[str, int, int]]:
    """Each occurrence with its neighbouring words, as a comparable key."""
    words = words_with_pos(text)
    starts = [w[0] for w in words]
    out = []
    for m in rx.finditer(text):
        i = bisect.bisect_left(starts, m.start())
        prev = words[i - 1][2] if i > 0 else ""
        j = bisect.bisect_left(starts, m.end())
        nxt = words[j][2] if j < len(words) else ""
        out.append((f"{prev}|{m.group(0).lower()}|{nxt}", m.start(), m.end()))
    return out


def multiset_diff(a: list, b: list) -> tuple[list, list]:
    ca, cb = Counter(a), Counter(b)
    return list((ca - cb).elements()), list((cb - ca).elements())


def load_register() -> list[tuple[str, re.Pattern]]:
    if not REGISTRE.exists():
        return []
    terms: list[tuple[str, re.Pattern]] = []
    in_terms = False
    for line in REGISTRE.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_terms = "terme" in line.lower()
            continue
        if not in_terms or not line.startswith("|") or line.startswith("| :") or line.startswith("| Terme"):
            continue
        cell = line.split("|")[1].strip()
        cell = re.sub(r"\([^)]*\)", "", cell)
        for variant in (v.strip() for v in cell.split(",")):
            words = WORD_RE.findall(variant.replace("’", "'"))
            if not words:
                continue
            parts = [re.escape(w) + ("" if w[-1] in "sx" else "(?:s|x)?") for w in words]
            terms.append((" ".join(words), re.compile(r"\b" + r"\s+".join(parts) + r"\b", re.IGNORECASE)))
    return terms


@dataclass
class Item:
    severity: str  # "⛔", "⚠", "·"
    label: str
    lines: list[str] = field(default_factory=list)


def compare_section(o: Section | None, n: Section | None, register) -> list[Item]:
    items: list[Item] = []
    if o is None or n is None:
        which = "absente de l'original" if o is None else "absente de la réécriture"
        items.append(Item("⛔", f"Section {which} (invariant 1)"))
        return items

    ow, nw = clean_words(o.text), clean_words(n.text)

    # 1. Marker families
    for fam, rxs in COMPILED.items():
        for label, rx in rxs.items():
            ow_list, nw_list = marker_windows(ow, rx), marker_windows(nw, rx)
            removed, added = multiset_diff([k for k, _, _ in ow_list], [k for k, _, _ in nw_list])
            if not removed and not added:
                continue
            count_changed = len(ow_list) != len(nw_list)
            sev = "⚠" if count_changed else "·"
            what = "effectif modifié" if count_changed else "reformulé autour"
            it = Item(sev, f"{fam} — *{label}* : {len(ow_list)} → {len(nw_list)} ({what})")
            used: Counter = Counter()
            for key in removed:
                for k, s, e in ow_list:
                    if k == key and used[("o", s)] == 0:
                        used[("o", s)] = 1
                        it.lines.append(f"retiré : « {snippet(ow, s, e)} »")
                        break
            for key in added:
                for k, s, e in nw_list:
                    if k == key and used[("n", s)] == 0:
                        used[("n", s)] = 1
                        it.lines.append(f"ajouté : « {snippet(nw, s, e)} »")
                        break
            items.append(it)

    # 2. Numbers
    on, nn = NUM_RE.findall(clean_numbers(o.text)), NUM_RE.findall(clean_numbers(n.text))
    removed, added = multiset_diff(on, nn)
    if removed or added:
        it = Item("⚠", "Nombres modifiés dans la prose")
        if removed:
            it.lines.append("retirés : " + ", ".join(removed))
        if added:
            it.lines.append("ajoutés : " + ", ".join(added))
        items.append(it)

    # 3. Register terms and bold spans
    reg_lines = []
    for name, rx in register:
        ow_list, nw_list = marker_windows(ow, rx), marker_windows(nw, rx)
        if len(ow_list) == len(nw_list):
            continue
        reg_lines.append(f"*{name}* : {len(ow_list)} → {len(nw_list)}")
        removed, added = multiset_diff([k for k, _, _ in ow_list], [k for k, _, _ in nw_list])
        for key in removed[:3]:
            s, e = next((s, e) for k, s, e in ow_list if k == key)
            reg_lines.append(f"    retiré : « {snippet(ow, s, e)} »")
        for key in added[:3]:
            s, e = next((s, e) for k, s, e in nw_list if k == key)
            reg_lines.append(f"    ajouté : « {snippet(nw, s, e)} »")
    if reg_lines:
        it = Item("⚠", "Termes du registre : effectifs modifiés (invariant 2 — vérifier qu'aucun synonyme n'a remplacé le terme)")
        it.lines.extend(reg_lines)
        items.append(it)
    removed, added = multiset_diff(BOLD_RE.findall(o.text), BOLD_RE.findall(n.text))
    if removed or added:
        it = Item("⚠", "Mises en gras modifiées (invariant 2)")
        if removed:
            it.lines.append("retirées : " + ", ".join(f"**{x}**" for x in removed))
        if added:
            it.lines.append("ajoutées : " + ", ".join(f"**{x}**" for x in added))
        items.append(it)

    # 4. Citation keys in this section
    oc = CITE_KEY_RE.findall(re.sub(r"`[^`]*`", " ", o.text))
    nc = CITE_KEY_RE.findall(re.sub(r"`[^`]*`", " ", n.text))
    removed, added = multiset_diff(oc, nc)
    if removed or added:
        sev = "⛔" if removed else "⚠"
        it = Item(sev, "Citations modifiées dans la section (invariant 3)")
        if removed:
            it.lines.append("retirées : " + ", ".join(f"@{x}" for x in removed))
        if added:
            it.lines.append("ajoutées : " + ", ".join(f"@{x}" for x in added) + " (vérifier qu'elles soutiennent la phrase où elles sont placées)")
        items.append(it)

    # 5. Content words lost / added
    def content(text: str) -> dict[str, tuple[str, int, int]]:
        out: dict[str, tuple[str, int, int]] = {}
        for s, e, w in words_with_pos(text):
            if len(w.replace("-", "").replace("'", "")) < 7 or w in STOPWORDS:
                continue
            if "'" in w:
                w = w.split("'", 1)[1]
                if len(w) < 7:
                    continue
            if any(rx.fullmatch(w) for rx in ALL_MARKERS):
                continue
            out.setdefault(stem(w), (w, s, e))
        return out

    oc_words, nc_words = content(ow), content(nw)
    lost = [v for k, v in oc_words.items() if k not in nc_words]
    gained = [v for k, v in nc_words.items() if k not in oc_words]

    def variant_of(w: str, pool: list[str]) -> str | None:
        """A word of `pool` that looks like an inflection of `w` (shared prefix up to the last two letters)."""
        for p in pool:
            shorter = min(len(w), len(p))
            common = 0
            while common < shorter and w[common] == p[common]:
                common += 1
            if common >= max(5, shorter - 2):
                return p
        return None

    gained_words = [w for w, _, _ in gained]
    truly_lost, variants = [], []
    for w, s, e in lost:
        v = variant_of(w, gained_words)
        if v:
            variants.append(f"{w} → {v}")
        else:
            truly_lost.append((w, s, e))
    matched = {v.split(" → ")[1] for v in variants}
    gained = [g for g in gained if g[0] not in matched]

    if truly_lost:
        it = Item("⚠", f"Mots pleins perdus sans équivalent dans la section ({len(truly_lost)})")
        it.lines.extend(f"*{w}* : « {snippet(ow, s, e, 6)} »" for w, s, e in truly_lost)
        items.append(it)
    if variants or gained:
        lines = []
        if variants:
            lines.append("variantes probables : " + ", ".join(variants))
        if gained:
            lines.append("ajoutés : " + ", ".join(w for w, _, _ in gained))
        items.append(Item("·", f"Mots pleins : {len(variants)} variante(s), {len(gained)} ajout(s)", lines))

    # 6. Protected blocks
    if o.blocks != n.blocks:
        it = Item("⛔", "Bloc protégé modifié (§1 : .formel, .outils, .proposition, .definition, .exemple-quantitatif)")
        it.lines.append(f"original : {', '.join(c for c, _ in o.blocks) or 'aucun'} ; réécriture : {', '.join(c for c, _ in n.blocks) or 'aucun'}")
        for i, (a, b) in enumerate(zip(o.blocks, n.blocks)):
            if a != b:
                it.lines.append(f"bloc n° {i + 1} (.{a[0]}) différent")
        items.append(it)
    return items


def global_invariants(otext: str, ntext: str) -> list[Item]:
    items: list[Item] = []
    checks = [
        ("Identifiants {#…}", lambda t: re.findall(r"\{[^}]*?#([^\s}]+)", t), "⛔"),
        ("Renvois @sec:/@prop:/@def:/@eq:/@fig:/@tbl:", lambda t: CROSSREF_RE.findall(t), "⛔"),
        ("Attributs statut=\"…\"", lambda t: re.findall(r'statut="([^"]*)"', t), "⛔"),
        ("Clés de citation", lambda t: CITE_KEY_RE.findall(re.sub(r"`[^`]*`", " ", t)), None),
    ]
    for label, fn, sev in checks:
        removed, added = multiset_diff(fn(otext), fn(ntext))
        if not removed and not added:
            continue
        s = sev or ("⛔" if removed else "⚠")
        it = Item(s, f"{label} (fichier entier)")
        if removed:
            it.lines.append("retirés : " + ", ".join(sorted(set(removed))) + f" ({len(removed)} occurrence(s))")
        if added:
            it.lines.append("ajoutés : " + ", ".join(sorted(set(added))) + f" ({len(added)} occurrence(s))")
        items.append(it)
    return items


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def render(orig: Path, new: Path) -> tuple[str, int, Counter]:
    osec, nsec = parse(orig), parse(new)
    register = load_register()
    keys = list(osec) + [k for k in nsec if k not in osec]
    per_section = [(k, (osec.get(k) or nsec.get(k)).title, compare_section(osec.get(k), nsec.get(k), register)) for k in keys]
    glob = global_invariants(orig.read_text(encoding="utf-8"), new.read_text(encoding="utf-8"))

    sev_count: Counter = Counter()
    for it in glob:
        sev_count[it.severity] += 1
    for _, _, its in per_section:
        for it in its:
            sev_count[it.severity] += 1
    n_boxes = sev_count["⛔"] + sev_count["⚠"]

    out = [
        f"# Contrôle de portée — `{new.stem}`",
        "",
        f"- Original : `{orig}`",
        f"- Réécriture : `{new}`",
        f"- Généré le {datetime.date.today().isoformat()} par `style/diff_portee.py` (STYLE_PASS_SPEC.md, §6.3)",
        "",
        "**Mode d'emploi.** Pour chaque case : la cocher et écrire après « décision : » *accepté* ou *rétabli* "
        "(avec, au besoin, la formulation retenue). `python3 style/diff_portee.py --controle <ce fichier>` échoue tant qu'une case reste vide. "
        "⛔ = invariant de la spec touché ; ⚠ = portée ou contenu possiblement modifié. "
        "Les éléments · (reformulation à effectif constant, variantes morphologiques, mots ajoutés) sont à parcourir et ne demandent pas de décision.",
        "",
        f"**Bilan :** {n_boxes} décision(s) à prendre — ⛔ {sev_count['⛔']} · ⚠ {sev_count['⚠']} ; {sev_count['·']} élément(s) · à parcourir",
        "",
        "## Synthèse par section",
        "",
        "| Section | ⛔ | ⚠ | · |",
        "| :-- | --: | --: | --: |",
    ]
    for k, title, its in per_section:
        c = Counter(it.severity for it in its)
        out.append(f"| `{k}` {title} | {c['⛔'] or ''} | {c['⚠'] or ''} | {c['·'] or ''} |")
    out.append("")

    def emit(its: list[Item]) -> None:
        for it in sorted(its, key=lambda i: "⛔⚠·".index(i.severity)):
            if it.severity == "·":
                out.append(f"- · {it.label}")
            else:
                out.append(f"- [ ] {it.severity} {it.label} — décision : ")
            for l in it.lines:
                out.append(f"    - {l}")

    out += ["## Invariants structurels (fichier entier)", ""]
    if glob:
        emit(glob)
    else:
        out.append("Aucune différence : identifiants, renvois, attributs `statut` et clés de citation identiques.")
    out.append("")

    for k, title, its in per_section:
        if not its:
            continue
        out += [f"## `{k}` — {title}", ""]
        emit(its)
        out.append("")
    return "\n".join(out), n_boxes, sev_count


def controle(report: Path) -> int:
    text = report.read_text(encoding="utf-8")
    open_boxes = re.findall(r"^- \[ \].*$", text, flags=re.M)
    undecided = [l for l in re.findall(r"^- \[[xX]\].*$", text, flags=re.M) if not re.search(r"décision\s*:\s*\S", l)]
    if open_boxes or undecided:
        print(f"{report} : {len(open_boxes)} case(s) non cochée(s), {len(undecided)} cochée(s) sans décision écrite.")
        return 1
    print(f"{report} : toutes les décisions sont prises.")
    return 0


def main() -> None:
    p = argparse.ArgumentParser(description="Contrôle de dérive de sens d'une passe de style (STYLE_PASS_SPEC.md §6.3).")
    p.add_argument("original", nargs="?", type=Path)
    p.add_argument("reecrit", nargs="?", type=Path)
    p.add_argument("--out", type=Path, help="chemin du rapport (défaut : style/rapports/diff_portee_<nom>.md)")
    p.add_argument("--force", action="store_true", help="écraser un rapport existant (et les décisions qu'il contient)")
    p.add_argument("--stdout", action="store_true", help="afficher le rapport au lieu de l'écrire")
    p.add_argument("--controle", type=Path, metavar="RAPPORT", help="vérifier qu'un rapport a toutes ses décisions")
    a = p.parse_args()

    if a.controle:
        sys.exit(controle(a.controle))
    if not a.original or not a.reecrit:
        p.error("donner ORIGINAL et REECRIT, ou --controle RAPPORT")

    report, n_boxes, sev = render(a.original, a.reecrit)
    if a.stdout:
        print(report)
        return
    out = a.out or RAPPORTS / f"diff_portee_{a.reecrit.stem}.md"
    if out.exists() and not a.force:
        sys.exit(f"{out} existe déjà (il peut contenir des décisions) ; utiliser --force pour l'écraser ou --out.")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report + "\n", encoding="utf-8")
    print(f"{out} : {n_boxes} décision(s) — ⛔ {sev['⛔']} · ⚠ {sev['⚠']} ; {sev['·']} élément(s) · à parcourir")


if __name__ == "__main__":
    main()
