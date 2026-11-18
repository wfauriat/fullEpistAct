# Makefile — build of the monograph. Run from monographie/.
#   make pdf | html | docx | tout   whole book
#   make chapitre CH=05             one chapter (PDF + HTML preview, in build/apercu/);
#                                   CH is a file-name prefix: CH=00-a (preface), CH=00-c (chapter 0)
#   make figures                    run every scripts/fig_*.py (figures/ and tableaux/)
#   make verifier                   static checks (statuts, labels, leaks, A-VERIFIER, numbers)
#   make glossaire                  regenerate annexes B (glossary) and C (notation) from commun/registre_termes.md
#   make essai                      toolchain self-test on tests/essai.md
#   make clean
# Owned by the maintainer.

PANDOC  ?= pandoc
LATEXMK ?= latexmk
PY      ?= $(shell test -x /opt/venvs/pyDS/bin/python && echo /opt/venvs/pyDS/bin/python || echo python3)
BUILD   := build
COMMUN  := -d gabarit/commun.yaml
SOURCES := $(shell sed -n 's/^  - \(.*\.md\)$$/\1/p' livre.yaml)
DEPS    := $(SOURCES) livre.yaml gabarit/commun.yaml filtres/monographie.lua commun/biblio.bib commun/biblio_a_verifier.bib
LATEXMK_OPTS := -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(BUILD)

.PHONY: pdf html docx tout chapitre figures verifier glossaire essai clean

pdf: $(BUILD)/livre.pdf
html: $(BUILD)/livre.html
docx: $(BUILD)/livre.docx
tout: pdf html docx

$(BUILD):
	mkdir -p $(BUILD) $(BUILD)/apercu

$(BUILD)/livre.tex: $(DEPS) gabarit/pdf.yaml gabarit/preambule.tex | $(BUILD)
	$(PANDOC) $(COMMUN) -d gabarit/pdf.yaml -d livre.yaml -o $@

$(BUILD)/livre.pdf: $(BUILD)/livre.tex
	$(LATEXMK) $(LATEXMK_OPTS) $<

$(BUILD)/livre.html: $(DEPS) gabarit/html.yaml gabarit/livre.css | $(BUILD)
	$(PANDOC) $(COMMUN) -d gabarit/html.yaml -d livre.yaml -o $@

$(BUILD)/livre.docx: $(DEPS) gabarit/docx.yaml | $(BUILD)
	$(PANDOC) $(COMMUN) -d gabarit/docx.yaml -d livre.yaml -o $@

# Single-chapter preview: references to other chapters show as ?? (expected).
chapitre: | $(BUILD)
	@test -n "$(CH)" || (echo "usage : make chapitre CH=05  (ou CH=00-a, CH=00-c)" && exit 2)
	@f=$$(ls chapitres/$(CH)*.md | head -1); test -n "$$f" || (echo "aucun chapitre $(CH)" && exit 2); \
	echo "aperçu de $$f"; mkdir -p $(BUILD)/apercu; \
	$(PANDOC) $(COMMUN) -d gabarit/html.yaml --metadata title="Aperçu — chapitre $(CH)" --metadata premier-chapitre=$(shell echo $(CH) | cut -c1-2) $$f -o $(BUILD)/apercu/ch-$(CH).html && \
	$(PANDOC) $(COMMUN) -d gabarit/pdf.yaml --metadata title="Aperçu — chapitre $(CH)" --metadata premier-chapitre=$(shell echo $(CH) | cut -c1-2) $$f -o $(BUILD)/apercu/ch-$(CH).tex && \
	$(LATEXMK) -lualatex -interaction=nonstopmode -halt-on-error -outdir=$(BUILD)/apercu $(BUILD)/apercu/ch-$(CH).tex

figures:
	@for s in scripts/fig_*.py; do [ -e "$$s" ] || continue; echo "→ $$s"; $(PY) $$s || exit 1; done

verifier:
	@$(PY) outils/verifier.py

glossaire:
	@$(PY) outils/glossaire.py

essai: | $(BUILD)
	cd tests && $(PY) fig_essai.py
	$(PANDOC) $(COMMUN) -d gabarit/html.yaml tests/essai.md -o $(BUILD)/essai.html
	$(PANDOC) $(COMMUN) -d gabarit/pdf.yaml tests/essai.md -o $(BUILD)/essai.tex
	$(LATEXMK) $(LATEXMK_OPTS) $(BUILD)/essai.tex
	@$(PY) outils/verifier.py tests/essai.md || true

clean:
	$(LATEXMK) -C -outdir=$(BUILD) 2>/dev/null || true
	rm -rf $(BUILD)
