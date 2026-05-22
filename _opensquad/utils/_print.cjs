// Playwright print-to-PDF helper — chamado pelo regen-dem007.mjs
// Uso: node _print.cjs <htmlPath> <pdfPath>
const { chromium } = require('playwright');
const [,, htmlPath, pdfPath] = process.argv;
const url = 'file:///' + htmlPath.replace(/\\/g, '/');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '8mm', right: '10mm', bottom: '14mm', left: '10mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:7pt;color:#94a3b8;text-align:center;width:100%;padding:0 10mm;">VMO Consultoria — DEM-2026-007 — Pág <span class="pageNumber"></span>/<span class="totalPages"></span> — Confidencial</div>',
  });
  await browser.close();
  process.exit(0);
})().catch(e => { console.error(e.message); process.exit(1); });
