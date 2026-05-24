# gerar-pdfs-docs.ps1
# Converte todos os .md da pasta docs/ em PDF usando md_to_docs.py
# Uso: ! powershell -ExecutionPolicy Bypass -File squads\vmo-web-publisher\tools\gerar-pdfs-docs.ps1

$base = Split-Path $PSScriptRoot -Parent | Split-Path -Parent | Split-Path -Parent
$docs = "$base\squads\vmo-web-publisher\output\site\projetos\docs"
$util = "$base\_opensquad\utils\md_to_docs.py"

$python = @("python3", "python", "py") | Where-Object {
  try { & $_ --version 2>&1 | Out-Null; $true } catch { $false }
} | Select-Object -First 1

if (-not $python) {
  Write-Error "Python nao encontrado. Instale Python 3 e tente novamente."
  exit 1
}

Write-Host "Usando: $python"

$files = Get-ChildItem $docs -Recurse -Filter "*.md" | Where-Object {
  $_.Directory.Name -match "^(PROJ|DEM)-"
}

Write-Host "Convertendo $($files.Count) arquivos para PDF..."
$ok = 0; $fail = 0

foreach ($f in $files) {
  $pdfPath = [System.IO.Path]::ChangeExtension($f.FullName, ".pdf")
  if (Test-Path $pdfPath) {
    Write-Host "  SKIP (ja existe): $($f.Name)"
    $ok++
    continue
  }
  Write-Host "  -> $($f.FullName.Replace($base,''))"
  $out = & $python $util $f.FullName --format pdf 2>&1
  if ($LASTEXITCODE -eq 0) { $ok++ }
  else { Write-Host "  ERRO: $out"; $fail++ }
}

Write-Host ""
Write-Host "Resultado: $ok OK | $fail erros"
