#!/usr/bin/env python3
"""Build a natively editable PowerPoint (.pptx) from a Marp slide deck.

Every heading, card, bullet list, table, caption, and speaker note becomes
native PPTX shapes/text boxes (editable in PowerPoint and Canva), and SVG
figures are paired with 300-DPI PNG renders from monographie/figures/*.pdf.
"""
from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

# Palette matching monographie/scripts/_style.py and slides/themes/monographie.css
C_BLEU = RGBColor(0x2A, 0x78, 0xD6)
C_ORANGE = RGBColor(0xEB, 0x68, 0x34)
C_AQUA = RGBColor(0x1B, 0xAF, 0x7A)
C_ENCRE = RGBColor(0x1D, 0x23, 0x2B)
C_ENCRE2 = RGBColor(0x52, 0x51, 0x4E)
C_MUET = RGBColor(0x8A, 0x89, 0x84)
C_GRILLE = RGBColor(0xE4, 0xE3, 0xDF)
C_PAPIER = RGBColor(0xFA, 0xF9, 0xF6)
C_BLEU_FOND = RGBColor(0xF0, 0xF5, 0xFC)
C_ORANGE_FOND = RGBColor(0xFD, 0xF3, 0xEE)
C_AQUA_FOND = RGBColor(0xEE, 0xF9, 0xF4)
C_BLANC = RGBColor(0xFF, 0xFF, 0xFF)

FONT_SERIF = 'Georgia'
FONT_SANS = 'Liberation Sans'

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

SUB_MAP = str.maketrans('0123456789ijkn', '₀₁₂₃₄₅₆₇₈₉ᵢⱼₖₙ')


def latex_to_unicode(expr: str) -> str:
    """Convert common LaTeX math snippets from the monograph to clean Unicode."""
    s = expr.strip()
    replacements = [
        (r'\mathcal{T}', '𝒯'),
        (r'\mathbb{E}', '𝔼'),
        (r'\operatorname{Var}', 'Var'),
        (r'\mathrm{VPP}', 'VPP'),
        (r'\mathrm{Pr}', 'Pr'),
        (r'\Pr', 'Pr'),
        (r'\bar{C}', 'C̄'),
        (r'\bar{H}', 'H̄'),
        (r'^\ast', '*'),
        (r'\ast', '*'),
        (r'\Theta', 'Θ'),
        (r'\theta', 'θ'),
        (r'\Delta', 'Δ'),
        (r'\Lambda', 'Λ'),
        (r'\alpha', 'α'),
        (r'\bigcup', '⋃'),
        (r'\subseteq', '⊆'),
        (r'\supseteq', '⊇'),
        (r'\cap', '∩'),
        (r'\cup', '∪'),
        (r'\in', '∈'),
        (r'\rightarrow', '→'),
        (r'\to', '→'),
        (r'\Rightarrow', '⇒'),
        (r'\times', '×'),
        (r'\mid', '|'),
        (r'\dots', '…'),
        (r'\ln', 'ln'),
        (r'\{', '{'),
        (r'\}', '}'),
        (r'\%', '%'),
        (r'\,', ' '),
        (r'\!', ''),
        (r'\;', ' '),
        (r'\quad', '  '),
        (r'\approx', '≈'),
        (r'\le', '≤'),
        (r'\ge', '≥'),
        (r'\downarrow', '↓'),
        (r'\uparrow', '↑'),
    ]
    for old, new in replacements:
        s = s.replace(old, new)
    s = s.replace('{,}', ',')
    # Handle nested braces cleanly in \text / \mathbf / \mathrm and fractions
    for _ in range(3):
        s = re.sub(r'\\(text|mathbf|mathrm)\{([^{}]+)\}', r'\2', s)
        s = re.sub(r'\\d?frac\{([^{}]+)\}\{([^{}]+)\}', r'\1 / (\2)', s)
    # _{...} and _x
    s = re.sub(r'_\{([^{}]+)\}', lambda m: '_' + m.group(1), s)
    s = re.sub(r'_([0-9ijkn])\b', lambda m: m.group(1).translate(SUB_MAP), s)
    s = re.sub(r'[{}]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def clean_inline_html(text: str) -> str:
    """Normalize inline HTML and LaTeX into clean text with markdown emphasis markers."""
    s = text.strip()
    s = re.sub(r'<span class="statut[^"]*">([^<]+)</span>', r'[\1]', s)
    s = re.sub(r'<span class="math"[^>]*>(.*?)</span>',
               lambda m: re.sub(r'</?i>', '', m.group(1)).replace('<sub>', '_').replace('</sub>', ''),
               s, flags=re.S)
    s = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', s, flags=re.S)
    s = re.sub(r'<em>(.*?)</em>', r'*\1*', s, flags=re.S)
    s = re.sub(r'<strong>(.*?)</strong>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'\$\$(.*?)\$\$', lambda m: latex_to_unicode(m.group(1)), s, flags=re.S)
    s = re.sub(r'\$([^$\n]+)\$', lambda m: latex_to_unicode(m.group(1)), s)
    s = s.replace('&amp;', '&')
    return s


def add_formatted_runs(p, text: str, font_size: int, color: RGBColor, font_name: str = FONT_SANS,
                       base_bold: bool = False, base_italic: bool = False):
    """Add runs to a python-pptx paragraph supporting **bold** (with nested *italic*), *italic*, `code`."""
    tokens = re.split(r'(\*\*.*?\*\*|`[^`]+`)', text)
    for tok in tokens:
        if not tok:
            continue
        if tok.startswith('**') and tok.endswith('**'):
            add_formatted_runs_inner(p, tok[2:-2], font_size, color, font_name, True, base_italic)
        elif tok.startswith('`') and tok.endswith('`'):
            r = p.add_run()
            r.text = tok[1:-1]
            r.font.size = Pt(font_size)
            r.font.name = 'DejaVu Sans Mono'
            r.font.bold = base_bold
            r.font.italic = base_italic
            r.font.color.rgb = color
        else:
            add_formatted_runs_inner(p, tok, font_size, color, font_name, base_bold, base_italic)


def add_formatted_runs_inner(p, text: str, font_size: int, color: RGBColor, font_name: str,
                             base_bold: bool, base_italic: bool):
    for tok in re.split(r'(\*[^*]+\*)', text):
        if not tok:
            continue
        italic = base_italic
        val = tok
        if tok.startswith('*') and tok.endswith('*'):
            val = tok[1:-1]
            italic = True
        for part in re.split(r'(_[A-Za-zÀ-ÿ0-9]+)', val):
            if not part:
                continue
            r = p.add_run()
            if part.startswith('_') and len(part) > 1:
                r.text = part[1:]
                r.font.size = Pt(max(10, int(font_size * 0.78)))
            else:
                r.text = part
                r.font.size = Pt(font_size)
            r.font.name = font_name
            r.font.bold = base_bold
            r.font.italic = italic
            r.font.color.rgb = color


@dataclass
class Block:
    kind: str  # 'card', 'text', 'fig'
    variant: str = ''
    title: str = ''
    lines: list[str] = field(default_factory=list)
    img_path: str = ''
    caption: str = ''


def strip_outer_div(chunk: str) -> tuple[str, str]:
    """If chunk starts with <div class="..."> and ends with </div>, return (classes, inner)."""
    m = re.match(r'^\s*<div([^>]*)>(.*)</div>\s*$', chunk.strip(), flags=re.S)
    if not m:
        return '', chunk.strip()
    attrs, inner = m.group(1), m.group(2).strip()
    cm = re.search(r'class="([^"]+)"', attrs)
    return (cm.group(1) if cm else ''), inner


def split_top_divs(html_text: str) -> list[str]:
    """Split a container's inner text into top-level blocks (<div>...</div> or plain markdown)."""
    blocks: list[str] = []
    pos = 0
    n = len(html_text)
    tag_re = re.compile(r'<div\b[^>]*>|</div>')
    while pos < n:
        while pos < n and html_text[pos].isspace():
            pos += 1
        if pos >= n:
            break
        if html_text[pos:].startswith('<div'):
            depth = 0
            start = pos
            for m in tag_re.finditer(html_text, pos):
                if m.group(0).startswith('<div'):
                    depth += 1
                else:
                    depth -= 1
                    if depth == 0:
                        blocks.append(html_text[start:m.end()].strip())
                        pos = m.end()
                        break
            else:
                blocks.append(html_text[start:].strip())
                break
        else:
            nxt = html_text.find('<div', pos)
            if nxt == -1:
                blocks.append(html_text[pos:].strip())
                break
            blocks.append(html_text[pos:nxt].strip())
            pos = nxt
    return [b for b in blocks if b]


def parse_block(raw: str) -> Block:
    cls, inner = strip_outer_div(raw)
    classes = cls.split()
    if 'fig' in classes:
        im = re.search(r'!\[[^\]]*\]\(([^)]+)\)', inner)
        img_path = im.group(1) if im else ''
        cap = ''
        cm = re.search(r'<div class="caption">(.*?)</div>', inner, flags=re.S)
        if cm:
            cap = clean_inline_html(cm.group(1))
        return Block(kind='fig', variant=' '.join(classes), img_path=img_path, caption=cap)

    if 'card' in classes:
        title = ''
        tm = re.search(r'<div class="card-title">(.*?)</div>', inner, flags=re.S)
        if tm:
            title = clean_inline_html(tm.group(1))
            inner = inner.replace(tm.group(0), '', 1).strip()
        # Unwrap inner <div class="small..."> wrappers
        inner = re.sub(r'</?div[^>]*>', '', inner)
        lines = [clean_inline_html(ln) for ln in inner.splitlines() if ln.strip()]
        variant = next((c for c in classes if c in ('blue', 'orange', 'aqua')), 'neutral')
        return Block(kind='card', variant=variant, title=title, lines=lines)

    # Plain text / markdown block (possibly wrapped in a generic <div>)
    inner = re.sub(r'</?div[^>]*>', '', inner)
    lines = [clean_inline_html(ln) for ln in inner.splitlines() if ln.strip()]
    return Block(kind='text', lines=lines)


def render_pdf_to_png(rel_svg: str, slides_dir: Path, cache_dir: Path) -> Path:
    """Render monographie/figures/<name>.pdf at 300 DPI for crisp PPTX/Canva import."""
    svg_path = (slides_dir / rel_svg).resolve()
    pdf_path = svg_path.with_suffix('.pdf')
    cache_dir.mkdir(parents=True, exist_ok=True)
    out_base = cache_dir / pdf_path.stem
    out_png = out_base.with_suffix('.png')
    if not out_png.exists() or out_png.stat().st_mtime < pdf_path.stat().st_mtime:
        subprocess.run(
            ['pdftoppm', '-png', '-r', '300', '-singlefile', str(pdf_path), str(out_base)],
            check=True,
        )
    return out_png


def add_textbox(slide, left, top, width, height, lines: list[str], font_size: int = 16,
                color: RGBColor = C_ENCRE, font_name: str = FONT_SANS,
                align=PP_ALIGN.LEFT, line_spacing: float = 1.2):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.06)
    tf.margin_right = Inches(0.06)
    tf.margin_top = Inches(0.04)
    tf.margin_bottom = Inches(0.04)
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        p.space_after = Pt(5)
        if ln.startswith('## '):
            add_formatted_runs(p, ln[3:].strip(), font_size + 3, C_BLEU, FONT_SERIF, base_bold=True)
            p.space_before = Pt(4)
        elif ln.startswith('- '):
            add_formatted_runs(p, '•  ' + ln[2:].strip(), font_size, color, font_name)
        elif re.match(r'^\d+\.\s+', ln):
            add_formatted_runs(p, ln, font_size, color, font_name)
        else:
            add_formatted_runs(p, ln, font_size, color, font_name)
    return tb


def add_card(slide, left, top, width, height, block: Block, font_size: int = 15):
    bg_map = {
        'blue': (C_BLEU_FOND, C_BLEU),
        'orange': (C_ORANGE_FOND, C_ORANGE),
        'aqua': (C_AQUA_FOND, C_AQUA),
        'neutral': (C_PAPIER, C_BLEU),
    }
    bg_col, accent_col = bg_map.get(block.variant, (C_PAPIER, C_BLEU))
    bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    bg.adjustments[0] = 0.03
    bg.fill.solid()
    bg.fill.fore_color.rgb = bg_col
    bg.line.color.rgb = C_GRILLE
    bg.line.width = Pt(1)

    stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, Inches(0.08), height)
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = accent_col
    stripe.line.fill.background()

    tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.10),
                                  width - Inches(0.28), height - Inches(0.18))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    first = True
    if block.title:
        p = tf.paragraphs[0]
        first = False
        p.space_after = Pt(5)
        add_formatted_runs(p, block.title, font_size + 1, C_ENCRE, FONT_SANS, base_bold=True)
    for ln in block.lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.line_spacing = 1.18
        p.space_after = Pt(4)
        if ln.startswith('- '):
            add_formatted_runs(p, '•  ' + ln[2:].strip(), font_size, C_ENCRE, FONT_SANS)
        else:
            add_formatted_runs(p, ln, font_size, C_ENCRE, FONT_SANS)


def add_picture_fit(slide, img_path: Path, left, top, max_w, max_h, caption: str = ''):
    cap_h = Inches(0.45) if caption else Inches(0)
    avail_h = max_h - cap_h
    with Image.open(img_path) as im:
        iw, ih = im.size
    ratio = iw / ih
    w = max_w
    h = w / ratio
    if h > avail_h:
        h = avail_h
        w = h * ratio
    x = left + (max_w - w) / 2
    y = top + (avail_h - h) / 2
    slide.shapes.add_picture(str(img_path), x, y, width=w, height=h)
    if caption:
        add_textbox(slide, left, top + avail_h + Inches(0.04), max_w, cap_h,
                    [caption], font_size=12, color=C_ENCRE2, align=PP_ALIGN.CENTER, line_spacing=1.1)


def render_column_blocks(slide, raw_col: str, left, top, width, height, slides_dir: Path, cache_dir: Path):
    """Render a column that may contain multiple stacked cards or text blocks."""
    cls, inner = strip_outer_div(raw_col)
    if 'fig' in cls.split():
        b = parse_block(raw_col)
        png = render_pdf_to_png(b.img_path, slides_dir, cache_dir)
        add_picture_fit(slide, png, left, top, width, height, b.caption)
        return
    if 'card' in cls.split():
        b = parse_block(raw_col)
        add_card(slide, left, top, width, height, b, font_size=15)
        return
    parts = split_top_divs(inner)
    blocks = [parse_block(p) for p in parts]
    if not blocks:
        return
    n = len(blocks)
    gap = Inches(0.14)
    # Allocate vertical space proportional to wrapped line count
    weights = [sum(max(1, (len(ln) + 34) // 35) for ln in b.lines) + (1.5 if b.title else 0) + 0.8
               for b in blocks]
    tot = sum(weights)
    avail = height - gap * (n - 1)
    y = top
    for b, w in zip(blocks, weights):
        bh = avail * (w / tot)
        if b.kind == 'card':
            add_card(slide, left, y, width, bh, b, font_size=14 if n >= 3 else 15)
        else:
            add_textbox(slide, left, y, width, bh, b.lines, font_size=16)
        y += bh + gap


def build_deck(md_path: Path, out_pptx: Path):
    text = md_path.read_text(encoding='utf-8')
    if text.startswith('---'):
        _, _, text = text.split('---', 2)
    raw_slides = [s.strip() for s in re.split(r'\n---\n', text) if s.strip()]

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank_layout = prs.slide_layouts[6]

    slides_dir = md_path.parent
    cache_dir = slides_dir / '.cache' / 'figs'
    footer_label = 'Agir d’après une représentation du monde · Synthèse (35 min)'

    for idx, raw in enumerate(raw_slides, 1):
        slide = prs.slides.add_slide(blank_layout)

        # Extract speaker notes (comments that are not Marp directives)
        notes: list[str] = []
        is_lead = False
        for cm in re.finditer(r'<!--(.*?)-->', raw, flags=re.S):
            body = cm.group(1).strip()
            if body.startswith('_class: lead'):
                is_lead = True
            elif body.startswith('_'):
                continue
            else:
                notes.append(body)
        if notes:
            slide.notes_slide.notes_text_frame.text = '\n'.join(notes)
        raw = re.sub(r'<!--.*?-->', '', raw, flags=re.S).strip()

        # Eyebrow
        eyebrow = ''
        em = re.search(r'<div class="eyebrow[^"]*">(.*?)</div>', raw, flags=re.S)
        if em:
            eyebrow = clean_inline_html(em.group(1)).upper()
            raw = raw.replace(em.group(0), '', 1).strip()

        # Heading (# ...)
        title = ''
        hm = re.search(r'^#\s+(.+)$', raw, flags=re.M)
        if hm:
            title = clean_inline_html(hm.group(1))
            raw = raw.replace(hm.group(0), '', 1).strip()

        if is_lead:
            # Left accent bar
            bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.14), SLIDE_H)
            bar.fill.solid()
            bar.fill.fore_color.rgb = C_BLEU
            bar.line.fill.background()

            sub = ''
            sm = re.search(r'<div class="subtitle"[^>]*>(.*?)</div>', raw, flags=re.S)
            if sm:
                sub = clean_inline_html(sm.group(1))
                raw = raw.replace(sm.group(0), '', 1).strip()
            meta = ''
            mm = re.search(r'<div class="meta"[^>]*>(.*?)</div>', raw, flags=re.S)
            if mm:
                meta = clean_inline_html(mm.group(1))

            y = Inches(1.85)
            if eyebrow:
                add_textbox(slide, Inches(0.9), y, Inches(11.4), Inches(0.4), [eyebrow],
                            font_size=13, color=C_BLEU, font_name=FONT_SANS)
                y += Inches(0.42)
            add_textbox(slide, Inches(0.9), y, Inches(11.4), Inches(1.6), [title],
                        font_size=36, color=C_ENCRE, font_name=FONT_SERIF)
            if sub:
                add_textbox(slide, Inches(0.9), y + Inches(1.5), Inches(11.2), Inches(0.8), [sub],
                            font_size=20, color=C_ENCRE2, font_name=FONT_SANS)
            if meta:
                rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(4.85),
                                              Inches(11.4), Pt(1))
                rule.fill.solid()
                rule.fill.fore_color.rgb = C_GRILLE
                rule.line.fill.background()
                meta_lines = [ln.strip() for ln in meta.splitlines() if ln.strip()]
                add_textbox(slide, Inches(0.9), Inches(5.05), Inches(11.4), Inches(1.1),
                            meta_lines, font_size=14, color=C_MUET)
            continue

        # Standard slide header + rule + footer
        if eyebrow:
            add_textbox(slide, Inches(0.75), Inches(0.32), Inches(11.8), Inches(0.32),
                        [eyebrow], font_size=12, color=C_BLEU, font_name=FONT_SANS)
        add_textbox(slide, Inches(0.75), Inches(0.62), Inches(11.8), Inches(0.65),
                    [title], font_size=26, color=C_ENCRE, font_name=FONT_SERIF)
        hrule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), Inches(1.30),
                                       Inches(11.83), Pt(1.2))
        hrule.fill.solid()
        hrule.fill.fore_color.rgb = C_GRILLE
        hrule.line.fill.background()

        add_textbox(slide, Inches(0.75), Inches(7.02), Inches(9.5), Inches(0.32),
                    [footer_label], font_size=11, color=C_MUET)
        add_textbox(slide, Inches(11.3), Inches(7.02), Inches(1.28), Inches(0.32),
                    [str(idx)], font_size=11, color=C_MUET, align=PP_ALIGN.RIGHT)

        # Body area: y = 1.48 .. 6.86 (height = 5.38 in)
        top_blocks = split_top_divs(raw)
        y_cur = Inches(1.48)
        y_end = Inches(6.88)
        avail_h = y_end - y_cur
        n_top = len(top_blocks)

        for bi, tb_raw in enumerate(top_blocks):
            cls, inner = strip_outer_div(tb_raw)
            classes = cls.split()
            is_last = (bi == n_top - 1)
            # Determine block height when multiple stacked rows exist
            if n_top == 1:
                bh = avail_h
            elif 'fig-wide' in classes:
                bh = y_end - y_cur
            elif any(c in classes for c in ('cols', 'cols-3', 'cols-55-45')):
                # Top row above another card or wide figure
                bh = Inches(2.1) if any('fig-wide' in strip_outer_div(x)[0] for x in top_blocks) else Inches(3.85)
            else:
                bh = (y_end - y_cur) if is_last else Inches(1.3)

            if 'cols-3' in classes:
                items = split_top_divs(inner)
                gap = Inches(0.22)
                col_w = (Inches(11.83) - gap * 2) / 3
                for ci, item in enumerate(items[:3]):
                    render_column_blocks(slide, item, Inches(0.75) + (col_w + gap) * ci,
                                         y_cur, col_w, bh, slides_dir, cache_dir)
            elif any(c in classes for c in ('cols', 'cols-40-60', 'cols-45-55', 'cols-38-62', 'cols-55-45')):
                items = split_top_divs(inner)
                gap = Inches(0.30)
                total_w = Inches(11.83) - gap
                if 'cols-40-60' in classes:
                    r_left = 0.41
                elif 'cols-45-55' in classes:
                    r_left = 0.45
                elif 'cols-38-62' in classes:
                    r_left = 0.38
                elif 'cols-55-45' in classes:
                    r_left = 0.53
                else:
                    r_left = 0.50
                w1 = total_w * r_left
                w2 = total_w - w1
                if len(items) >= 1:
                    render_column_blocks(slide, items[0], Inches(0.75), y_cur, w1, bh, slides_dir, cache_dir)
                if len(items) >= 2:
                    render_column_blocks(slide, items[1], Inches(0.75) + w1 + gap, y_cur, w2, bh, slides_dir, cache_dir)
            elif 'fig' in classes:
                b = parse_block(tb_raw)
                png = render_pdf_to_png(b.img_path, slides_dir, cache_dir)
                add_picture_fit(slide, png, Inches(0.75), y_cur, Inches(11.83), bh, b.caption)
            elif 'card' in classes:
                b = parse_block(tb_raw)
                add_card(slide, Inches(0.75), y_cur, Inches(11.83), bh, b, font_size=15)
            else:
                b = parse_block(tb_raw)
                add_textbox(slide, Inches(0.75), y_cur, Inches(11.83), bh, b.lines, font_size=16)

            y_cur += bh + Inches(0.16)

    prs.save(str(out_pptx))
    print(f'Wrote {out_pptx} ({len(prs.slides)} slides)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_md', type=Path)
    parser.add_argument('output_pptx', type=Path)
    args = parser.parse_args()
    build_deck(args.input_md, args.output_pptx)
