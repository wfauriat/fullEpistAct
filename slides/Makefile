MARP = npx --yes @marp-team/marp-cli
THEME = themes/monographie.css
CHROME ?= $(shell find $(HOME)/.cache/puppeteer -name chrome-headless-shell -type f 2>/dev/null | head -n 1)
BROWSER_FLAGS = CHROME_NO_SANDBOX=1 $(MARP) --browser chrome --browser-path "$(CHROME)"

.PHONY: all short 3h pdf pptx 3h-pdf 3h-pptx clean

all: short 3h pdf 3h-pdf pptx 3h-pptx

short: slides_courts.html

3h: slides_3h.html

pdf: slides_courts.pdf

3h-pdf: slides_3h.pdf

pptx: slides_courts.pptx

3h-pptx: slides_3h.pptx

%.html: %.md $(THEME)
	$(MARP) --html --allow-local-files --theme $(THEME) $< -o $@

%.pdf: %.md $(THEME)
	@test -n "$(CHROME)" || (echo "Chrome introuvable dans ~/.cache/puppeteer ; lancez : npx --yes @puppeteer/browsers install chrome-headless-shell@stable --path ~/.cache/puppeteer" && exit 1)
	$(BROWSER_FLAGS) --pdf --pdf-notes --pdf-outlines --html --allow-local-files --theme $(THEME) $< -o $@

%.pptx: %.md $(THEME)
	@test -n "$(CHROME)" || (echo "Chrome introuvable dans ~/.cache/puppeteer ; lancez : npx --yes @puppeteer/browsers install chrome-headless-shell@stable --path ~/.cache/puppeteer" && exit 1)
	$(BROWSER_FLAGS) --pptx --html --allow-local-files --theme $(THEME) $< -o $@

clean:
	rm -f slides_courts.html slides_courts.pdf slides_courts.pptx slides_3h.html slides_3h.pdf slides_3h.pptx
