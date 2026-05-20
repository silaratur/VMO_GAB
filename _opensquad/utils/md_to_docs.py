#!/usr/bin/env python3
"""
Convert Markdown files to DOCX and/or PDF.
Usage:
  python3 md_to_docs.py <file.md> [--format docx|pdf|both]
  python3 md_to_docs.py <file.md>            # defaults to both
Outputs are saved alongside the source .md file.
"""

import sys
import re
import os
import argparse
from pathlib import Path


# ── DOCX ──────────────────────────────────────────────────────────────────────

def md_to_docx(md_path: Path) -> Path:
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    text = md_path.read_text(encoding="utf-8")
    doc = Document()

    # Page margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.2)
        section.right_margin = Inches(1.2)

    # Default style
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    def add_heading(text_content, level):
        p = doc.add_heading(text_content, level=level)
        run = p.runs[0] if p.runs else p.add_run(text_content)
        if level == 1:
            run.font.size = Pt(18)
            run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
        elif level == 2:
            run.font.size = Pt(14)
            run.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
        else:
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(0x40, 0x40, 0x40)

    def add_inline(para, line):
        # Bold **text** and `code`
        parts = re.split(r'(\*\*[^*]+\*\*|`[^`]+`)', line)
        for part in parts:
            if part.startswith("**") and part.endswith("**"):
                run = para.add_run(part[2:-2])
                run.bold = True
            elif part.startswith("`") and part.endswith("`"):
                run = para.add_run(part[1:-1])
                run.font.name = "Courier New"
                run.font.size = Pt(10)
            else:
                para.add_run(part)

    in_table = False
    table_rows = []
    in_code_block = False

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Code block
        if line.strip().startswith("```"):
            if not in_code_block:
                in_code_block = True
                i += 1
                continue
            else:
                in_code_block = False
                i += 1
                continue
        if in_code_block:
            p = doc.add_paragraph(line)
            p.style.font.name = "Courier New"
            p.style.font.size = Pt(9)
            i += 1
            continue

        # Table rows
        if line.strip().startswith("|"):
            table_rows.append(line)
            i += 1
            continue
        else:
            if table_rows:
                _flush_table(doc, table_rows)
                table_rows = []

        # Headings
        if line.startswith("# "):
            add_heading(line[2:].strip(), 1)
        elif line.startswith("## "):
            add_heading(line[3:].strip(), 2)
        elif line.startswith("### "):
            add_heading(line[4:].strip(), 3)
        elif line.startswith("#### "):
            add_heading(line[5:].strip(), 4)
        # Horizontal rule
        elif re.match(r'^---+$', line.strip()):
            doc.add_paragraph("─" * 60)
        # Blockquote
        elif line.startswith("> "):
            p = doc.add_paragraph(line[2:].strip())
            p.style = doc.styles["Quote"] if "Quote" in doc.styles else doc.styles["Normal"]
        # Bullet list
        elif re.match(r'^[-*•] ', line):
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, line[2:].strip())
        # Numbered list
        elif re.match(r'^\d+\. ', line):
            p = doc.add_paragraph(style="List Number")
            add_inline(p, re.sub(r'^\d+\. ', '', line))
        # Empty line
        elif line.strip() == "":
            doc.add_paragraph("")
        # Normal paragraph
        else:
            p = doc.add_paragraph()
            add_inline(p, line)

        i += 1

    if table_rows:
        _flush_table(doc, table_rows)

    out = md_path.with_suffix(".docx")
    doc.save(out)
    return out


def _flush_table(doc, rows):
    from docx.shared import Pt, RGBColor
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    # Filter separator rows (|---|---|)
    data_rows = [r for r in rows if not re.match(r'^\|[-| :]+\|$', r.strip())]
    if not data_rows:
        return

    parsed = []
    for row in data_rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        parsed.append(cells)

    col_count = max(len(r) for r in parsed)
    table = doc.add_table(rows=len(parsed), cols=col_count)
    table.style = "Table Grid"

    for r_idx, row in enumerate(parsed):
        for c_idx, cell_text in enumerate(row):
            if c_idx >= col_count:
                break
            cell = table.cell(r_idx, c_idx)
            # Strip markdown bold from cell text
            clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', cell_text)
            clean = re.sub(r'`([^`]+)`', r'\1', clean)
            # Emoji status indicators — keep as-is
            p = cell.paragraphs[0]
            run = p.add_run(clean)
            run.font.size = Pt(10)
            if r_idx == 0:
                run.bold = True
                # Header row shading
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:color"), "auto")
                shd.set(qn("w:fill"), "D6E4F0")
                tcPr.append(shd)


# ── PDF ───────────────────────────────────────────────────────────────────────

def md_to_pdf(md_path: Path) -> Path:
    import markdown as md_lib
    from weasyprint import HTML, CSS

    text = md_path.read_text(encoding="utf-8")

    extensions = ["tables", "fenced_code", "nl2br"]
    html_body = md_lib.markdown(text, extensions=extensions)

    css = CSS(string="""
        @page { margin: 2cm 2.5cm; }
        body {
            font-family: 'DejaVu Sans', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.5;
            color: #222;
        }
        h1 { font-size: 18pt; color: #1F497D; border-bottom: 2px solid #1F497D; padding-bottom: 4px; }
        h2 { font-size: 14pt; color: #2E74B5; border-bottom: 1px solid #2E74B5; padding-bottom: 2px; }
        h3 { font-size: 12pt; color: #404040; }
        h4 { font-size: 11pt; color: #404040; font-style: italic; }
        table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 10pt; }
        th { background-color: #D6E4F0; font-weight: bold; padding: 6px 8px; border: 1px solid #aaa; }
        td { padding: 5px 8px; border: 1px solid #ccc; vertical-align: top; }
        tr:nth-child(even) { background-color: #F5F9FF; }
        code { font-family: 'DejaVu Sans Mono', monospace; font-size: 9pt; background: #f4f4f4; padding: 1px 4px; }
        pre { background: #f4f4f4; padding: 10px; font-size: 9pt; overflow-x: auto; }
        blockquote { border-left: 3px solid #2E74B5; margin-left: 0; padding-left: 12px; color: #555; }
        hr { border: none; border-top: 1px solid #ccc; margin: 16px 0; }
        strong { color: #1a1a1a; }
        a { color: #2E74B5; }
    """)

    html_full = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body>{html_body}</body></html>"""

    out = md_path.with_suffix(".pdf")
    HTML(string=html_full, base_url=str(md_path.parent)).write_pdf(str(out), stylesheets=[css])
    return out


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to DOCX/PDF")
    parser.add_argument("input", help="Path to .md file")
    parser.add_argument("--format", choices=["docx", "pdf", "both"], default="both")
    args = parser.parse_args()

    md_path = Path(args.input).resolve()
    if not md_path.exists():
        print(f"ERROR: file not found: {md_path}", file=sys.stderr)
        sys.exit(1)

    outputs = []
    if args.format in ("docx", "both"):
        out = md_to_docx(md_path)
        outputs.append(str(out))
        print(f"DOCX: {out}")

    if args.format in ("pdf", "both"):
        out = md_to_pdf(md_path)
        outputs.append(str(out))
        print(f"PDF:  {out}")

    return outputs


if __name__ == "__main__":
    main()
