#!/usr/bin/env python3
"""Gera PDF único consolidado com todos os documentos de um projeto VMO."""

import os
import re
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, Preformatted, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus.flowables import BalancedColumns
from datetime import datetime

# ── Paleta ────────────────────────────────────────────────────────────────────
BLUE_DARK   = colors.HexColor("#1E3C78")
BLUE_MID    = colors.HexColor("#1E50A0")
BLUE_LIGHT  = colors.HexColor("#3266CC")
GREY_LINE   = colors.HexColor("#CCCCCC")
GREY_TEXT   = colors.HexColor("#555555")
GREY_BG     = colors.HexColor("#F5F8FC")
CODE_BG     = colors.HexColor("#F0F0F0")
TABLE_HEAD  = colors.HexColor("#DCE6F5")
TABLE_ALT   = colors.HexColor("#F5F8FC")
COVER_BG    = colors.HexColor("#1E3C78")
SECTION_BG  = colors.HexColor("#EEF3FB")

# ── Ordem dos documentos ──────────────────────────────────────────────────────
DOC_ORDER = [
    ("01-qualificacao", "demanda-coletada.md",     "Demanda Coletada"),
    ("01-qualificacao", "gate-intake.md",           "Gate de Governança — Intake"),
    ("01-qualificacao", "qualificacao.md",          "Qualificação da Demanda"),
    ("01-qualificacao", "gate-qualificacao.md",     "Gate de Governança — Qualificação"),
    ("01-qualificacao", "qualificacao-aprovada.md", "Qualificação Aprovada"),
    ("02-iniciacao",    "documentacao-base.md",     "Documentação Base (TAP + PM Canvas)"),
    ("02-iniciacao",    "requisitos.md",             "Especificação de Requisitos (ERF)"),
    ("02-iniciacao",    "work-request.md",           "Work Request — Mini-RFP"),
    ("03-planejamento", "cronograma.md",             "Cronograma do Projeto"),
    ("03-planejamento", "plano-riscos.md",           "Plano de Riscos"),
    ("03-planejamento", "kpis.md",                   "Framework de KPIs"),
    ("04-monitoramento","status-report-2026-05-28.md","Status Report Inicial"),
    ("05-encerramento", "revisao-final.md",          "Revisão de Qualidade"),
    ("05-encerramento", "auditoria-governanca.md",   "Auditoria de Governança"),
    ("05-encerramento", "aprovacao-final.md",        "Aprovação Final"),
]

SECTION_LABELS = {
    "01-qualificacao":  "FASE 01 — QUALIFICAÇÃO",
    "02-iniciacao":     "FASE 02 — INICIAÇÃO",
    "03-planejamento":  "FASE 03 — PLANEJAMENTO",
    "04-monitoramento": "FASE 04 — MONITORAMENTO",
    "05-encerramento":  "FASE 05 — ENCERRAMENTO",
}


def build_styles():
    S = {}
    S["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16,
                              textColor=BLUE_DARK, spaceAfter=5, spaceBefore=4)
    S["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13,
                              textColor=BLUE_MID, spaceAfter=4, spaceBefore=10)
    S["h3"] = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11,
                              textColor=BLUE_LIGHT, spaceAfter=3, spaceBefore=6)
    S["h4"] = ParagraphStyle("h4", fontName="Helvetica-Bold", fontSize=10,
                              textColor=BLUE_LIGHT, spaceAfter=2, spaceBefore=4)
    S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9,
                                leading=13, spaceAfter=3)
    S["bold_body"] = ParagraphStyle("bold_body", fontName="Helvetica-Bold",
                                     fontSize=9, leading=13, spaceAfter=3)
    S["code"] = ParagraphStyle("code", fontName="Courier", fontSize=7.5,
                                leading=10, backColor=CODE_BG,
                                leftIndent=6, rightIndent=6,
                                spaceBefore=2, spaceAfter=2)
    S["quote"] = ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=9,
                                 leading=13, leftIndent=15, textColor=GREY_TEXT)
    S["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9,
                                  leading=13, leftIndent=14, spaceAfter=2)
    S["num"]    = ParagraphStyle("num", fontName="Helvetica", fontSize=9,
                                  leading=13, leftIndent=14, spaceAfter=2)
    S["section_header"] = ParagraphStyle("section_header", fontName="Helvetica-Bold",
                                          fontSize=13, textColor=colors.white,
                                          alignment=TA_LEFT, spaceAfter=0)
    S["doc_title"] = ParagraphStyle("doc_title", fontName="Helvetica-Bold",
                                     fontSize=14, textColor=BLUE_DARK,
                                     spaceAfter=4, spaceBefore=6)
    S["toc_fase"] = ParagraphStyle("toc_fase", fontName="Helvetica-Bold", fontSize=10,
                                    textColor=BLUE_DARK, spaceAfter=2, spaceBefore=6)
    S["toc_item"] = ParagraphStyle("toc_item", fontName="Helvetica", fontSize=9,
                                    textColor=colors.black, leftIndent=12, spaceAfter=1)
    S["cover_title"] = ParagraphStyle("cover_title", fontName="Helvetica-Bold",
                                       fontSize=26, textColor=colors.white,
                                       alignment=TA_CENTER, spaceAfter=8)
    S["cover_sub"]   = ParagraphStyle("cover_sub", fontName="Helvetica", fontSize=14,
                                       textColor=colors.HexColor("#C8D8F0"),
                                       alignment=TA_CENTER, spaceAfter=4)
    S["cover_meta"]  = ParagraphStyle("cover_meta", fontName="Helvetica", fontSize=10,
                                       textColor=colors.HexColor("#A0B8D8"),
                                       alignment=TA_CENTER, spaceAfter=3)
    S["footer"] = ParagraphStyle("footer", fontName="Helvetica", fontSize=8,
                                  textColor=GREY_TEXT, alignment=TA_CENTER)
    return S


def make_header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY_TEXT)
    # header
    canvas.drawString(20*mm, h - 12*mm, "VMO Autônomo — Pacote de Iniciação DEM-2026-008")
    canvas.drawRightString(w - 20*mm, h - 12*mm, "Chamado #6800446 — Integração SGMM03 InterCompany")
    canvas.setStrokeColor(GREY_LINE)
    canvas.line(20*mm, h - 14*mm, w - 20*mm, h - 14*mm)
    # footer
    canvas.line(20*mm, 14*mm, w - 20*mm, 14*mm)
    canvas.drawCentredString(w/2, 10*mm, f"Página {doc.page}")
    canvas.drawString(20*mm, 10*mm, "CONFIDENCIAL — VIX Matriz / Holding DTI")
    canvas.drawRightString(w - 20*mm, 10*mm, "28/05/2026")
    canvas.restoreState()


def make_cover_page(canvas, doc):
    """Capa personalizada — apenas na primeira página."""
    canvas.saveState()
    w, h = A4
    # fundo azul escuro
    canvas.setFillColor(COVER_BG)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    # faixa decorativa
    canvas.setFillColor(colors.HexColor("#2A5298"))
    canvas.rect(0, h * 0.38, w, h * 0.42, fill=1, stroke=0)
    # linha dourada
    canvas.setStrokeColor(colors.HexColor("#F0C040"))
    canvas.setLineWidth(3)
    canvas.line(20*mm, h * 0.38, w - 20*mm, h * 0.38)
    canvas.restoreState()


def clean_inline(text):
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'~~(.+?)~~', r'<strike>\1</strike>', text)
    text = re.sub(r'&(?!#?\w+;)', '&amp;', text)
    return text


def parse_md_to_story(md_path, S):
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
        for row in table_buf:
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if all(re.match(r'^[-: ]+$', c) for c in cells if c):
                continue
            data.append(cells)
        if not data:
            table_buf = []
            return
        ncols = max(len(r) for r in data)
        avail = 170 * mm
        col_widths = [avail / ncols] * ncols
        for r in data:
            while len(r) < ncols:
                r.append("")
        # convert cells to Paragraph for wrapping
        styled_data = []
        for ri, row in enumerate(data):
            styled_row = []
            for ci, cell in enumerate(row):
                cell_clean = clean_inline(cell)
                st = ParagraphStyle("tc", fontName="Helvetica-Bold" if ri == 0 else "Helvetica",
                                    fontSize=8, leading=11, wordWrap='CJK')
                styled_row.append(Paragraph(cell_clean, st))
            styled_data.append(styled_row)
        t = Table(styled_data, colWidths=col_widths, repeatRows=1)
        ts = TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0), TABLE_HEAD),
            ("TEXTCOLOR",     (0, 0), (-1, 0), BLUE_DARK),
            ("FONTSIZE",      (0, 0), (-1, -1), 8),
            ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.white, TABLE_ALT]),
            ("GRID",          (0, 0), (-1, -1), 0.4, GREY_LINE),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ])
        t.setStyle(ts)
        story.append(t)
        story.append(Spacer(1, 3 * mm))
        table_buf = []

    while i < len(lines):
        raw = lines[i].rstrip("\n")

        if raw.strip().startswith("```"):
            if in_code:
                if code_buf:
                    story.append(Preformatted("\n".join(code_buf), S["code"]))
                    story.append(Spacer(1, 2 * mm))
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

        if raw.strip().startswith("|"):
            table_buf.append(raw)
            i += 1
            continue
        else:
            flush_table()

        line = clean_inline(raw)

        if raw.startswith("# ") and not raw.startswith("## "):
            story.append(Paragraph(line[2:], S["h1"]))
            story.append(HRFlowable(width="100%", thickness=1.5, color=BLUE_DARK, spaceAfter=4))
        elif raw.startswith("## "):
            story.append(Spacer(1, 3 * mm))
            story.append(Paragraph(line[3:], S["h2"]))
            story.append(HRFlowable(width="100%", thickness=0.7, color=BLUE_MID, spaceAfter=2))
        elif raw.startswith("### "):
            story.append(Paragraph(line[4:], S["h3"]))
        elif raw.startswith("#### "):
            story.append(Paragraph(line[5:], S["h4"]))
        elif raw.strip() in ("---", "***", "___"):
            story.append(HRFlowable(width="100%", thickness=0.4, color=GREY_LINE, spaceAfter=2))
        elif raw.strip().startswith("> "):
            story.append(Paragraph(line.strip()[2:], S["quote"]))
        elif re.match(r'^\s*- \[[ xX]\]', raw):
            checked = bool(re.match(r'^\s*- \[[xX]\]', raw))
            text = re.sub(r'^\s*- \[.\]\s*', '', line)
            mark = "☑" if checked else "☐"
            story.append(Paragraph(f"{mark} {text}", S["bullet"]))
        elif re.match(r'^\s*[-*+] ', raw):
            text = re.sub(r'^\s*[-*+] ', '', line)
            story.append(Paragraph(f"• {text}", S["bullet"]))
        elif re.match(r'^\s*\d+\.\s', raw):
            num = re.match(r'^\s*(\d+)\.', raw).group(1)
            text = re.sub(r'^\s*\d+\.\s+', '', line)
            story.append(Paragraph(f"{num}. {text}", S["num"]))
        elif raw.strip() == "":
            story.append(Spacer(1, 2 * mm))
        else:
            if re.match(r'^\*\*[^*]+\*\*', raw):
                story.append(Paragraph(line, S["bold_body"]))
            else:
                story.append(Paragraph(line, S["body"]))

        i += 1

    flush_table()
    if in_code and code_buf:
        story.append(Preformatted("\n".join(code_buf), S["code"]))

    return story


def section_divider(label, S):
    """Página separadora de fase."""
    elements = []
    elements.append(PageBreak())
    # tabela com fundo colorido simulando cabeçalho de seção
    data = [[Paragraph(label, S["section_header"])]]
    t = Table(data, colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BLUE_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 6 * mm))
    return elements


def doc_separator(title, S):
    """Separador visual entre documentos."""
    elements = []
    elements.append(Spacer(1, 4 * mm))
    data = [[Paragraph(f"📄  {title}", ParagraphStyle(
        "dh", fontName="Helvetica-Bold", fontSize=11, textColor=BLUE_DARK,
        leftIndent=6))]]
    t = Table(data, colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), SECTION_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("LINEBELOW",     (0, 0), (-1, -1), 1.5, BLUE_MID),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 4 * mm))
    return elements


def build_cover(S):
    """Capa do documento."""
    elements = []
    elements.append(Spacer(1, 35 * mm))
    elements.append(Paragraph("VMO AUTÔNOMO", S["cover_title"]))
    elements.append(Paragraph("PACOTE DE INICIAÇÃO DE PROJETO", S["cover_sub"]))
    elements.append(Spacer(1, 8 * mm))
    elements.append(Paragraph("DEM-2026-008", ParagraphStyle(
        "dem", fontName="Helvetica-Bold", fontSize=20,
        textColor=colors.HexColor("#F0C040"), alignment=TA_CENTER, spaceAfter=4)))
    elements.append(Spacer(1, 6 * mm))
    elements.append(Paragraph("Integração SGMM03 — Campos Empresa e Contrato (InterCompany)", S["cover_sub"]))
    elements.append(Spacer(1, 4 * mm))
    elements.append(Paragraph("Chamado #6800446", S["cover_meta"]))
    elements.append(Paragraph("Sistema: Sistemática ERP — Solicitação de Novas Demandas / Projetos", S["cover_meta"]))
    elements.append(Paragraph("Solicitante: Jenifer dos Santos Carvalho — VIX Matriz", S["cover_meta"]))
    elements.append(Paragraph("Responsável: Mara Rubia Silva Rocha — Holding DTI", S["cover_meta"]))
    elements.append(Spacer(1, 8 * mm))
    elements.append(Paragraph("Data: 28 de maio de 2026", S["cover_meta"]))
    elements.append(Paragraph("Status: APROVADO COM CONDIÇÕES | Score: 50/100", S["cover_meta"]))
    elements.append(Spacer(1, 30 * mm))
    # linha de rodapé da capa
    elements.append(Paragraph("CONFIDENCIAL — VMO Autônomo / Holding DTI", ParagraphStyle(
        "cfoot", fontName="Helvetica", fontSize=9,
        textColor=colors.HexColor("#6080A0"), alignment=TA_CENTER)))
    return elements


def build_toc(S):
    """Sumário."""
    elements = []
    elements.append(PageBreak())
    elements.append(Paragraph("SUMÁRIO", S["h1"]))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=BLUE_DARK, spaceAfter=6))
    elements.append(Spacer(1, 3 * mm))

    current_fase = None
    for fase, fname, title in DOC_ORDER:
        if fase != current_fase:
            current_fase = fase
            elements.append(Paragraph(SECTION_LABELS[fase], S["toc_fase"]))
        elements.append(Paragraph(f"• {title}", S["toc_item"]))

    return elements


def generate(project_dir, output_path):
    S = build_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=22 * mm, bottomMargin=20 * mm,
    )

    story = []

    # ── Capa ──────────────────────────────────────────────────────────────────
    story.extend(build_cover(S))
    story.append(PageBreak())

    # ── Sumário ───────────────────────────────────────────────────────────────
    story.extend(build_toc(S))
    story.append(PageBreak())

    # ── Documentos ────────────────────────────────────────────────────────────
    current_fase = None
    for fase, fname, title in DOC_ORDER:
        md_path = os.path.join(project_dir, fase, fname)
        if not os.path.exists(md_path):
            print(f"  AVISO: não encontrado — {md_path}")
            continue

        # separador de fase
        if fase != current_fase:
            if current_fase is not None:
                story.append(PageBreak())
            story.extend(section_divider(SECTION_LABELS[fase], S))
            current_fase = fase

        # separador de documento
        story.extend(doc_separator(title, S))

        # conteúdo
        doc_story = parse_md_to_story(md_path, S)
        story.extend(doc_story)

        print(f"  ✓  {fase}/{fname}")

    # ── Build ─────────────────────────────────────────────────────────────────
    def first_page(canvas, doc):
        make_cover_page(canvas, doc)

    def later_pages(canvas, doc):
        make_header_footer(canvas, doc)

    doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
    print(f"\n✅  PDF gerado: {output_path}\n")


if __name__ == "__main__":
    project_dir = "/home/user/VMO_GAB/squads/vmo-autonomo/projects/DEM-2026-008"
    output_path = "/home/user/VMO_GAB/squads/vmo-autonomo/projects/DEM-2026-008/DEM-2026-008-pacote-completo.pdf"
    print(f"\nGerando PDF consolidado do projeto DEM-2026-008...\n")
    generate(project_dir, output_path)
