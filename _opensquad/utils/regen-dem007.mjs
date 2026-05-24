import { execSync } from "child_process";
import { readFileSync, writeFileSync, existsSync, mkdirSync, copyFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dir = dirname(fileURLToPath(import.meta.url));
const BASE  = join(__dir, "..", "..");
const PROJ  = join(BASE, "squads", "vmo-autonomo", "projects", "DEM-2026-007");
const DOCS  = join(BASE, "squads", "vmo-web-publisher", "output", "site", "projetos", "docs", "DEM-2026-007");
const TMP   = join(__dir, "_tmp3");
const PRINT = join(__dir, "_print.cjs");
try { mkdirSync(TMP, { recursive: true }); } catch {}

const CSS = [
  "*{box-sizing:border-box;margin:0;padding:0;}",
  "body{font-family:'Segoe UI',Arial,sans-serif;font-size:11pt;line-height:1.65;color:#1e293b;background:#fff;padding:0 8mm;}",
  ".hdr{background:#1e3a5f;color:#fff;padding:14pt 18pt;margin:0 -8mm 18pt;display:flex;justify-content:space-between;align-items:flex-start;}",
  ".hdr-l{flex:1;}.hdr-co{font-size:8pt;letter-spacing:1px;text-transform:uppercase;opacity:.75;margin-bottom:3pt;}",
  ".hdr-t{font-size:16pt;font-weight:800;line-height:1.2;}.hdr-sub{font-size:10.5pt;opacity:.85;margin-top:3pt;}",
  ".hdr-r{text-align:right;font-size:8.5pt;opacity:.85;}.hdr-id{font-size:11pt;font-weight:700;color:#93c5fd;}",
  "h1{font-size:15pt;font-weight:800;color:#1e3a5f;margin:22pt 0 9pt;padding-bottom:5pt;border-bottom:2.5pt solid #1e3a5f;page-break-before:always;page-break-after:avoid;}",
  "h1:first-of-type{page-break-before:avoid;}",
  "h2{font-size:12.5pt;font-weight:700;color:#1e3a5f;margin:18pt 0 7pt;padding:5pt 0 5pt 9pt;border-left:4pt solid #3b82f6;background:#f0f7ff;page-break-after:avoid;}",
  "h3{font-size:11pt;font-weight:700;color:#334155;margin:14pt 0 5pt;padding-bottom:3pt;border-bottom:1pt solid #e2e8f0;page-break-after:avoid;}",
  "h4{font-size:11pt;font-weight:600;color:#475569;margin:10pt 0 4pt;}",
  "p{margin:0 0 7pt;}strong{font-weight:700;color:#0f172a;}em{font-style:italic;color:#475569;}",
  "table{width:100%;border-collapse:collapse;margin:9pt 0 14pt;font-size:9.5pt;page-break-inside:avoid;}",
  "thead tr{background:#1e3a5f;color:#fff;}",
  "thead th{padding:7pt 9pt;text-align:left;font-weight:700;font-size:9pt;}",
  "tbody tr:nth-child(even){background:#f8fafc;}tbody tr:nth-child(odd){background:#fff;}",
  "td{padding:6pt 9pt;border-bottom:.75pt solid #e2e8f0;vertical-align:top;line-height:1.5;}",
  "ul,ol{margin:3pt 0 9pt 17pt;}li{margin:2pt 0;line-height:1.5;}",
  "blockquote{margin:7pt 0;padding:7pt 11pt;background:#f0f7ff;border-left:4pt solid #3b82f6;color:#475569;font-size:10pt;border-radius:0 3pt 3pt 0;}",
  "pre{background:#0f172a;color:#e2e8f0;padding:9pt 13pt;border-radius:4pt;font-family:Consolas,monospace;font-size:8pt;margin:7pt 0 12pt;page-break-inside:avoid;white-space:pre-wrap;word-break:break-all;}",
  "code{font-family:Consolas,monospace;font-size:8.5pt;background:#f1f5f9;color:#1e3a5f;padding:1pt 4pt;border-radius:2pt;}",
  "pre code{background:transparent;color:inherit;padding:0;font-size:inherit;}",
  "hr{border:none;border-top:1pt solid #e2e8f0;margin:14pt 0;}",
  ".ftr{margin-top:20pt;padding-top:8pt;border-top:1pt solid #e2e8f0;font-size:8pt;color:#94a3b8;font-style:italic;}",
].join("\n");

function buildHtml(raw, label) {
  const tmpMd  = join(TMP, "in.md");
  const tmpHtm = join(TMP, "out.html");
  writeFileSync(tmpMd, raw, "utf-8");
  execSync(`npx marked -i "${tmpMd}" -o "${tmpHtm}"`, { stdio: "pipe" });
  const body = readFileSync(tmpHtm, "utf-8");

  let title = label, sub = "";
  for (const l of raw.split("\n")) {
    const s = l.trim();
    if (s.startsWith("# ") && title === label) { title = s.slice(2); continue; }
    if (s.startsWith("## ") && title !== label && !sub) { sub = s.slice(3); break; }
  }

  const today = new Date().toLocaleDateString("pt-BR");
  return [
    "<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'>",
    "<style>" + CSS + "</style></head><body>",
    "<div class='hdr'>",
    "  <div class='hdr-l'>",
    "    <div class='hdr-co'>VMO Consultoria</div>",
    "    <div class='hdr-t'>" + title + "</div>",
    sub ? "    <div class='hdr-sub'>" + sub + "</div>" : "",
    "  </div>",
    "  <div class='hdr-r'>",
    "    <div class='hdr-id'>DEM-2026-007</div>",
    "    <div>" + today + " · Confidencial</div>",
    "  </div>",
    "</div>",
    body,
    "<div class='ftr'>VMO Autônomo — DEM-2026-007 — " + label + " — " + today + "</div>",
    "</body></html>",
  ].join("\n");
}

function toPdf(html, pdfPath) {
  const tmpHtml = join(TMP, "page.html");
  writeFileSync(tmpHtml, html, "utf-8");
  execSync(`node "${PRINT}" "${tmpHtml}" "${pdfPath}"`, {
    stdio: "pipe", timeout: 60000, cwd: BASE,
  });
}

const FILES = [
  { md: "01-qualificacao/demanda-coletada.md",          label: "Demanda Coletada",        dst: "02-demanda-coletada.pdf" },
  { md: "01-qualificacao/gate-intake.md",               label: "Gate Intake",             dst: null },
  { md: "01-qualificacao/gate-qualificacao.md",         label: "Gate Qualificacao",       dst: null },
  { md: "01-qualificacao/qualificacao.md",              label: "Qualificacao",            dst: "01-qualificacao.pdf" },
  { md: "01-qualificacao/qualificacao-aprovada.md",     label: "Qualificacao Aprovada",   dst: null },
  { md: "02-iniciacao/documentacao-base.md",            label: "TAP + PM Canvas",         dst: "03-tap-canvas-plano-geral.pdf" },
  { md: "02-iniciacao/requisitos.md",                   label: "ERF Requisitos",          dst: "04-erf-requisitos.pdf" },
  { md: "02-iniciacao/work-request.md",                 label: "Work Request",            dst: null },
  { md: "03-planejamento/cronograma.md",                label: "Cronograma",              dst: "05-cronograma.pdf" },
  { md: "03-planejamento/kpis.md",                      label: "Framework de KPIs",       dst: "07-kpis.pdf" },
  { md: "03-planejamento/plano-riscos.md",              label: "Plano de Riscos",         dst: "06-plano-riscos.pdf" },
  { md: "04-monitoramento/status-report-2026-05-20.md", label: "Status Report SR-001",    dst: "08-status-report.pdf" },
  { md: "05-encerramento/auditoria-governanca.md",      label: "Auditoria de Governanca", dst: "11-auditoria-governanca.pdf" },
  { md: "05-encerramento/revisao-final.md",             label: "Revisao de Qualidade",    dst: "09-revisao-final.pdf" },
];

console.log("Gerando PDFs — DEM-2026-007\n");
let ok = 0, fail = 0;

for (const { md, label, dst } of FILES) {
  const mdPath  = join(PROJ, md);
  const pdfPath = mdPath.replace(".md", ".pdf");
  process.stdout.write("  " + label.padEnd(28) + " ");

  try {
    const raw  = readFileSync(mdPath, "utf-8");
    const html = buildHtml(raw, label);
    toPdf(html, pdfPath);
    if (dst && existsSync(pdfPath)) copyFileSync(pdfPath, join(DOCS, dst));
    const sz = Math.round(readFileSync(pdfPath).length / 1024);
    console.log("OK  " + sz + " KB");
    ok++;
  } catch (e) {
    console.log("ERRO  " + (e.message || "").slice(0, 70));
    fail++;
  }
}

console.log("\n" + ok + " gerados | " + fail + " erros");
