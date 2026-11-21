# Lookback 2022–2026

Material produced on 21 Nov 2026, looking back on how *Agir d'après une représentation du monde* was built and where its ideas come from, set against the 2022 book *Un discours de la méthode au XXIe siècle*.

## Reports

| File | What it covers |
| :-- | :-- |
| `rapport_processus_construction.md` | The build process, 18–21 Nov 2026: timeline by phase, agent sessions and swarms, tokens, cost in USD at public API prices, and human hours in 2022 against 2026 |
| `rapport_genealogie_idees.md` | The lineage of ideas: what is surely the author's (2022 book, Nov 2025 notes, Dec 2025 talk), what is mixed, and what came from LLM-written texts. It also checks `style/COMPARAISON_2022_2026.md`. Section 0 adds the provenance records and claude.ai export metadata from `miscMD/November_GH_housekeeping/` |

## Pages

Standalone copies of the published pages; they open in any browser.

| File | Published page (private) |
| :-- | :-- |
| `monograph-build-lookback.html` | https://claude.ai/artifact/PN8wpd27aXmMGQurS7ZnJX |
| `monograph-idea-lineage.html` | https://claude.ai/artifact/PqndnS1EbH9u8tr6RyWAYL |

## Scripts and data

The scripts that produced the figures. They read the local agent stores, `~/.claude/projects/` and `~/.gemini/antigravity-cli/`.

| File | Role |
| :-- | :-- |
| `scripts/agg_claude.py` | Totals Claude Code usage per session and subagent: calls, input, cache reads and writes, output |
| `scripts/pb.py` | Minimal protobuf decoder for Antigravity's `gen_metadata` records |
| `scripts/gem_all.py`, `scripts/gem_usage.py` | Gemini and Antigravity usage per conversation and per call |
| `scripts/find.py` | Full-text search with page numbers, used on the `pdftotext` output of the two books |
| `scripts/terms*.txt`, `scripts/t3.txt` | The search terms used for the 2022 book |
| `data/claude_rows.json`, `data/gem_rows.json` | Per-session usage tables, as computed on 21 Nov 2026 (prompt text removed) |

Usage: `python3 scripts/agg_claude.py out.json` and `python3 scripts/gem_all.py out.json`. `find.py` takes a text file, a terms file and the number of snippets to show per term.

## Not included

- The extracted text of the two books and of the sources. Regenerate it with `pdftotext`.
- The time log `TimeUnemployment.xlsx`, kept by the author outside the repository.
