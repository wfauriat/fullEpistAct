#!/usr/bin/env python3
"""Phase 0 stylistic profiler for monographie/chapitres/*.md.

Measures rhythm, paragraph variance, scaffolding openers, antithesis markers,
punctuation habits, and italic emphasis on main prose (excluding fenced boxes
such as .formel, .outils, .proposition, .definition, .inclure, tables, and
display math).
"""

from __future__ import annotations

import argparse
import math
import re
import statistics
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "monographie" / "chapitres"

SKIP_DIV_CLASSES = {
    "formel",
    "outils",
    "proposition",
    "definition",
    "inclure",
    "exemple-quantitatif",
    "question",
}

BOILERPLATE_OPENERS = [
    r"^Le @sec:",
    r"^La @sec:",
    r"^Ce chapitre\b",
    r"^Cet avant-propos\b",
    r"^En premier lieu\b",
    r"^En second lieu\b",
    r"^Or[ ,]",
    r"^Toutefois[ ,]",
    r"^En revanche[ ,]",
    r"^Il serait erroné\b",
    r"^Force est de constater\b",
]

ANTITHESIS_PATTERNS = [
    r"\bnon pas\b",
    r"\bnon\s+(?:pas\s+)?un[e]?\b",
    r"\bplutôt que\b",
    r"\bsans jamais\b",
    r"\bni\b[^.;\n]{3,60}\bni\b",
    r",\s+non\s+[àaàld]",
]


@dataclass
class ChapterMetrics:
    filename: str
    words: int
    paragraphs: int
    para_words_mean: float
    para_words_std: float
    sentences: int
    sent_words_mean: float
    sent_words_std: float
    short_sent_pct: float
    long_sent_pct: float
    colons_per_1k: float
    emdash_per_1k: float
    antithesis_per_1k: float
    italic_phrases_per_1k: float
    boilerplate_openers: int
    chapeau_words: int


def extract_main_prose(md_text: str, include_cas_nuance: bool = False) -> tuple[list[str], int]:
    """Return list of main-prose paragraphs and word count of the opening chapeau."""
    lines = md_text.splitlines()
    paragraphs: list[str] = []
    current_para: list[str] = []

    div_stack: list[bool] = []  # True if skipped
    in_display_math = False
    seen_first_h2 = False
    chapeau_words = 0

    def flush_para() -> None:
        nonlocal chapeau_words
        if current_para:
            text = " ".join(current_para).strip()
            if text:
                paragraphs.append(text)
                if not seen_first_h2:
                    chapeau_words += len(re.findall(r"\S+", text))
            current_para.clear()

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if stripped.startswith("$$"):
            flush_para()
            if not in_display_math:
                # Single-line display math: $$ ... $$ (optionally followed by {#eq:...})
                if re.match(r"^\$\$.+\$\$(?:\s*\{#[^}]+\})?\s*$", stripped):
                    continue
                in_display_math = True
            else:
                in_display_math = False
            continue
        if in_display_math:
            continue

        # Fenced div open/close (3 or more colons in pandoc Markdown)
        if re.match(r"^:{3,}", stripped):
            flush_para()
            if re.match(r"^:{3,}$", stripped):
                if div_stack:
                    div_stack.pop()
            else:
                classes = set(re.findall(r"\.([a-zA-Z0-9_-]+)", stripped))
                if classes & SKIP_DIV_CLASSES:
                    div_stack.append(True)
                elif not include_cas_nuance and (classes & {"cas", "nuance"}):
                    div_stack.append(True)
                else:
                    div_stack.append(False)
            continue

        if any(div_stack):
            continue

        # Headings, images, tables, metadata, bullet lists
        if (
            stripped.startswith("#")
            or stripped.startswith("![")
            or stripped.startswith("|")
            or stripped.startswith("Table:")
        ):
            flush_para()
            if stripped.startswith("## "):
                seen_first_h2 = True
            continue

        if not stripped:
            flush_para()
            continue

        # Skip bullet items inside Points cles or lists to focus on running prose
        if re.match(r"^([-*]|\d+\.)\s+", stripped):
            flush_para()
            continue

        current_para.append(stripped)

    flush_para()
    return paragraphs, chapeau_words


def split_sentences(para: str) -> list[str]:
    # Protect decimals, abbreviations like M., et al., etc.
    cleaned = re.sub(r"\bM\.", "M_DOT", para)
    cleaned = re.sub(r"\bet al\.", "et_al_DOT", cleaned)
    cleaned = re.sub(r"\bp\.\s*\d+", "p_NUM", cleaned)
    cleaned = re.sub(r"\[@[^\]]+\]", "", cleaned)  # strip citations from word/sentence length
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÉÈÊÀÂÎÔÛÇ«*])", cleaned)
    return [p.strip() for p in parts if len(re.findall(r"\w+", p)) >= 2]


def count_words(text: str) -> int:
    clean = re.sub(r"\[@[^\]]+\]", "", text)
    clean = re.sub(r"@(?:sec|prop|def|eq|fig|tbl):[a-z0-9-]+", "REF", clean)
    return len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9’'-]+", clean))


def analyze_chapter(path: Path, include_cas_nuance: bool = False) -> ChapterMetrics:
    text = path.read_text(encoding="utf-8")
    paragraphs, chapeau_words = extract_main_prose(text, include_cas_nuance=include_cas_nuance)

    para_lengths = [count_words(p) for p in paragraphs]
    all_sentences: list[str] = []
    opener_hits = 0

    for p in paragraphs:
        for pat in BOILERPLATE_OPENERS:
            if re.search(pat, p):
                opener_hits += 1
                break
        all_sentences.extend(split_sentences(p))

    sent_lengths = [count_words(s) for s in all_sentences if count_words(s) > 0]
    total_words = sum(para_lengths) or 1

    joined = "\n".join(paragraphs)
    colons = len(re.findall(r"\s:\s", joined))
    emdashes = len(re.findall(r"\s—\s", joined))
    italic_phrases = len(re.findall(r"(?<!\*)\*[^*\n]{8,80}\*(?!\*)", joined))

    antithesis_hits = 0
    for pat in ANTITHESIS_PATTERNS:
        antithesis_hits += len(re.findall(pat, joined, flags=re.IGNORECASE))

    short_pct = (
        100.0 * sum(1 for n in sent_lengths if n <= 10) / len(sent_lengths)
        if sent_lengths
        else 0.0
    )
    long_pct = (
        100.0 * sum(1 for n in sent_lengths if n >= 35) / len(sent_lengths)
        if sent_lengths
        else 0.0
    )

    return ChapterMetrics(
        filename=path.name,
        words=total_words if paragraphs else 0,
        paragraphs=len(paragraphs),
        para_words_mean=statistics.mean(para_lengths) if para_lengths else 0.0,
        para_words_std=statistics.pstdev(para_lengths) if len(para_lengths) > 1 else 0.0,
        sentences=len(sent_lengths),
        sent_words_mean=statistics.mean(sent_lengths) if sent_lengths else 0.0,
        sent_words_std=statistics.pstdev(sent_lengths) if len(sent_lengths) > 1 else 0.0,
        short_sent_pct=short_pct,
        long_sent_pct=long_pct,
        colons_per_1k=1000.0 * colons / total_words,
        emdash_per_1k=1000.0 * emdashes / total_words,
        antithesis_per_1k=1000.0 * antithesis_hits / total_words,
        italic_phrases_per_1k=1000.0 * italic_phrases / total_words,
        boilerplate_openers=opener_hits,
        chapeau_words=chapeau_words,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit stylistic metrics of monograph chapters.")
    parser.add_argument("--include-cas", action="store_true", help="Include .cas and .nuance blocks")
    parser.add_argument("--chapter", type=str, default=None, help="Filter by filename substring")
    args = parser.parse_args()

    files = sorted(CHAPTERS_DIR.glob("*.md"))
    if args.chapter:
        files = [f for f in files if args.chapter in f.name]

    metrics = [analyze_chapter(f, include_cas_nuance=args.include_cas) for f in files]

    header = (
        f"{'Fichier':34} {'Mots':>5} {'Para':>4} {'P±σ':>9} "
        f"{'Phr':>4} {'L±σ':>9} {'<=10w':>5} {'>=35w':>5} "
        f"{':/1k':>5} {'—/1k':>5} {'Ant/1k':>6} {'It/1k':>5} {'Opn':>3} {'Chap':>4}"
    )
    print(header)
    print("-" * len(header))

    for m in metrics:
        p_stat = f"{m.para_words_mean:4.0f}±{m.para_words_std:<3.0f}"
        s_stat = f"{m.sent_words_mean:4.1f}±{m.sent_words_std:<4.1f}"
        print(
            f"{m.filename:34} {m.words:5d} {m.paragraphs:4d} {p_stat:>9} "
            f"{m.sentences:4d} {s_stat:>9} {m.short_sent_pct:4.1f}% {m.long_sent_pct:4.1f}% "
            f"{m.colons_per_1k:5.1f} {m.emdash_per_1k:5.1f} {m.antithesis_per_1k:6.1f} "
            f"{m.italic_phrases_per_1k:5.1f} {m.boilerplate_openers:3d} {m.chapeau_words:4d}"
        )

    if len(metrics) > 1:
        tot_words = sum(m.words for m in metrics)
        avg_s_mean = statistics.mean(m.sent_words_mean for m in metrics)
        avg_s_std = statistics.mean(m.sent_words_std for m in metrics)
        avg_short = statistics.mean(m.short_sent_pct for m in metrics)
        avg_colons = statistics.mean(m.colons_per_1k for m in metrics)
        avg_ant = statistics.mean(m.antithesis_per_1k for m in metrics)
        avg_it = statistics.mean(m.italic_phrases_per_1k for m in metrics)
        print("-" * len(header))
        print(
            f"MOYENNE ({len(metrics)} ch., {tot_words} mots) : "
            f"L={avg_s_mean:.1f}±{avg_s_std:.1f} | <=10w={avg_short:.1f}% | "
            f":/1k={avg_colons:.1f} | Ant/1k={avg_ant:.1f} | It/1k={avg_it:.1f}"
        )


if __name__ == "__main__":
    main()
