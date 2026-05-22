#!/usr/bin/env python3
"""Convert markdown files to PDF using reportlab."""

import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, ListFlowable, ListItem, Preformatted
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT_DIR = "/home/user/VMO_GAB/squads/vmo-autonomo/projects/_pdf_exports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Colour palette ────────────────────────────────────────────────────────────
BLUE_DARK  = colors.HexColor("#1E3C78")
BLUE_MID   = colors.HexColor("#1E50A0")
BLUE_LIGHT = colors.HexColor("#3266CC")
GREY_LINE  = colors.HexColor("#CCCCCC")
GREY_TEXT  = colors.HexColor("#555555")
CODE_BG    = colors.HexColor("#F0F0F0")
TABLE_HEAD = colors.HexColor("#DCE6F5")
TABLE_ALT  = colors.HexColor("#F5F8FC")


def build_styles():
    base = getSampleStyleSheet()
    S = {}

    S["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=18,
                              textColor=BLUE_DARK, spaceAfter=6, spaceBefore=4)
    S["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=14,
                              textColor=BLUE_MID, spaceAfter=4, spaceBefore=10,
                              borderPadding=(0, 0, 2, 0))
    S["h3"] = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11,
                              textColor=BLUE_LIGHT, spaceAfter=3, spaceBefore=7)
    S["h4"] = ParagraphStyle("h4", fontName="Helvetica-Bold", fontSize=10,
                              textColor=BLUE_LIGHT, spaceAfter=2, spaceBefore=5)
    S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                               leading=14, spaceAfter=3, textColor=colors.black)
    S["bold_body"] = ParagraphStyle("bold_body", fontName="Helvetica-Bold",
                                    fontSize=10, leading=14, spaceAfter=3)
    S["code"] = ParagraphStyle("code", fontName="Courier", fontSize=8,
                               leading=11, backColor=CODE_BG,
                               leftIndent=6, rightIndent=6,
                               spaceBefore=2, spaceAfter=2)
    S["quote"] = ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=10,
                                leading=14, leftIndent=15, textColor=GREY_TEXT)
    S["footer"] = ParagraphStyle("footer", fontName="Helvetica", fontSize=8,
                                 textColor=GREY_TEXT, alignment=TA_CENTER)
    return S


def clean_inline(text):
    """Convert markdown inline to reportlab XML."""
    # bold+italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # inline code
    text = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', text)
    # links → just label
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # strikethrough
    text = re.sub(r'~~(.+?)~~', r'<strike>\1</strike>', text)
    # escape bare & not already entity
    text = re.sub(r'&(?!#?\w+;)', '&amp;', text)
    return text


def make_header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY_TEXT)
    canvas.drawString(20*mm, h - 12*mm, f"VMO Autônomo — {doc.vmo_title}")
    canvas.setStrokeColor(GREY_LINE)
    canvas.line(20*mm, h - 14*mm, w - 20*mm, h - 14*mm)
    canvas.drawCentredString(w/2, 10*mm, f"Página {doc.page}")
    canvas.restoreState()


def md_to_pdf(md_path, pdf_path, title):
    S = build_styles()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=22*mm, bottomMargin=18*mm,
    )
    doc.vmo_title = title

    story = []

    with open(md_path, encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    in_code = False
    code_buf = []
    table_buf = []

    def flush_table():
        nonlocal table_buf
        if not table_buf:
            return
        data = []
        col_widths = None
        header_done = False
        for row in table_buf:
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if all(re.match(r'^[-: ]+$', c) for c in cells if c):
                header_done = True
                continue
            data.append(cells)
        if not data:
            table_buf = []
            return
        ncols = max(len(r) for r in data)
        avail = 170*mm
        # Narrow first column when it contains short IDs (#, P-1, R-01, CS-01…)
        first_col_max = max(len(r[0]) for r in data if r) if data else 0
        if ncols >= 2 and first_col_max <= 8:
            first_w   = min(18*mm, avail * 0.12)
            rest_w    = (avail - first_w) / (ncols - 1)
            col_widths = [first_w] + [rest_w] * (ncols - 1)
        else:
            col_widths = [avail / ncols] * ncols
        # pad rows
        for r in data:
            while len(r) < ncols:
                r.append("")
        t = Table(data, colWidths=col_widths, repeatRows=1)
        ts = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD),
            ("TEXTCOLOR",  (0, 0), (-1, 0), BLUE_DARK),
            ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE",   (0, 0), (-1, -1), 9),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, TABLE_ALT]),
            ("GRID",       (0, 0), (-1, -1), 0.5, GREY_LINE),
            ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING",  (0, 0), (-1, -1), 5),
        ])
        t.setStyle(ts)
        story.append(t)
        story.append(Spacer(1, 4*mm))
        table_buf = []

    while i < len(lines):
        raw = lines[i].rstrip("\n")

        # ── code block ──────────────────────────────────────────────────────
        if raw.strip().startswith("```"):
            if in_code:
                # end block
                if code_buf:
                    story.append(Preformatted("\n".join(code_buf), S["code"]))
                    story.append(Spacer(1, 2*mm))
                code_buf = []
                in_code = False
            else:
                flush_table()
                in_code = True
            i += 1
            continue

        if in_code:
            code_buf.append(raw)
            i += 1
            continue

        # ── table ───────────────────────────────────────────────────────────
        if raw.strip().startswith("|"):
            table_buf.append(raw)
            i += 1
            continue
        else:
            flush_table()

        line = clean_inline(raw)

        # ── headings ────────────────────────────────────────────────────────
        if raw.startswith("# ") and not raw.startswith("## "):
            story.append(Paragraph(line[2:], S["h1"]))
            story.append(HRFlowable(width="100%", thickness=1.5,
                                    color=BLUE_DARK, spaceAfter=4))

        elif raw.startswith("## "):
            story.append(Spacer(1, 3*mm))
            story.append(Paragraph(line[3:], S["h2"]))
            story.append(HRFlowable(width="100%", thickness=0.8,
                                    color=BLUE_MID, spaceAfter=2))

        elif raw.startswith("### "):
            story.append(Paragraph(line[4:], S["h3"]))

        elif raw.startswith("#### "):
            story.append(Paragraph(line[5:], S["h4"]))

        # ── HR ──────────────────────────────────────────────────────────────
        elif raw.strip() in ("---", "***", "___"):
            story.append(HRFlowable(width="100%", thickness=0.5,
                                    color=GREY_LINE, spaceAfter=3))

        # ── blockquote ──────────────────────────────────────────────────────
        elif raw.strip().startswith("> "):
            story.append(Paragraph(line.strip()[2:], S["quote"]))

        # ── checkbox ────────────────────────────────────────────────────────
        elif re.match(r'^\s*- \[[ xX]\]', raw):
            checked = bool(re.match(r'^\s*- \[[xX]\]', raw))
            text = re.sub(r'^\s*- \[.\]\s*', '', line)
            mark = "☑" if checked else "☐"
            story.append(Paragraph(f"{mark} {text}", S["body"]))

        # ── bullet list ─────────────────────────────────────────────────────
        elif re.match(r'^\s*[-*+] ', raw):
            text = re.sub(r'^\s*[-*+] ', '', line)
            story.append(Paragraph(f"• {text}", ParagraphStyle(
                "bullet", parent=S["body"], leftIndent=12, firstLineIndent=0,
                bulletIndent=0)))

        # ── numbered list ───────────────────────────────────────────────────
        elif re.match(r'^\s*\d+\.\s', raw):
            num = re.match(r'^\s*(\d+)\.', raw).group(1)
            text = re.sub(r'^\s*\d+\.\s+', '', line)
            story.append(Paragraph(f"{num}. {text}", ParagraphStyle(
                "num", parent=S["body"], leftIndent=12)))

        # ── empty line ──────────────────────────────────────────────────────
        elif raw.strip() == "":
            story.append(Spacer(1, 2*mm))

        # ── normal paragraph ────────────────────────────────────────────────
        else:
            # detect all-bold line
            if re.match(r'^\*\*[^*]+\*\*', raw):
                story.append(Paragraph(line, S["bold_body"]))
            else:
                story.append(Paragraph(line, S["body"]))

        i += 1

    flush_table()
    if in_code and code_buf:
        story.append(Preformatted("\n".join(code_buf), S["code"]))

    doc.build(story, onFirstPage=make_header_footer, onLaterPages=make_header_footer)
    print(f"  OK  {os.path.basename(pdf_path)}")


def main():
    base = "/home/user/VMO_GAB/squads/vmo-autonomo/projects"
    files = []
    for root, dirs, fnames in os.walk(base):
        dirs[:] = [d for d in dirs if d != "_pdf_exports"]
        for fn in sorted(fnames):
            if fn.endswith(".md"):
                files.append(os.path.join(root, fn))

    print(f"\nConvertendo {len(files)} arquivo(s) para PDF...\n")
    for md_path in files:
        rel = os.path.relpath(md_path, base)
        pdf_name = rel.replace("/", "__").replace(".md", ".pdf")
        pdf_path = os.path.join(OUTPUT_DIR, pdf_name)
        title_raw = os.path.basename(md_path).replace(".md", "").replace("-", " ")
        title = " ".join(w.capitalize() for w in title_raw.split())
        try:
            md_to_pdf(md_path, pdf_path, title)
        except Exception as e:
            print(f"  ERRO {os.path.basename(md_path)}: {e}")

    print(f"\n{len(files)} PDFs exportados em:\n{OUTPUT_DIR}\n")


if __name__ == "__main__":
    main()
