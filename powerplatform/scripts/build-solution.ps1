<#
.SYNOPSIS
    Gera o arquivo VMO_GAB_Solution.zip pronto para importar no Power Platform.

.DESCRIPTION
    Empacota todos os componentes da solução VMO GAB:
    - solution.xml + customizations.xml + [Content_Types].xml
    - 13 Power Automate Flows (JSON)
    - Canvas App Source (YAML para PAC CLI)
    - Copilot Studio Bot (YAML)

    Requer: Power Platform CLI (PAC)
    Install: https://aka.ms/PowerAppsCLI

.EXAMPLE
    .\build-solution.ps1
    .\build-solution.ps1 -OutputPath "C:\Exports\VMO_GAB_v1.0.zip"
#>

param(
    [string]$OutputPath = "..\VMO_GAB_Solution.zip",
    [string]$SolutionName = "VMO_GAB",
    [switch]$PackCanvasApp = $false
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SrcDir    = Join-Path $ScriptDir ".."
$TempDir   = Join-Path $env:TEMP "VMO_GAB_Build_$(Get-Date -Format 'yyyyMMddHHmm')"

Write-Host "🏗️  VMO GAB — Build Solution Package" -ForegroundColor Cyan
Write-Host "="*50 -ForegroundColor Cyan

# === CRIAR ESTRUTURA TEMPORÁRIA ===
Write-Host "`n📁 Criando estrutura temporária..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $TempDir | Out-Null
New-Item -ItemType Directory -Force -Path "$TempDir\Workflows" | Out-Null
New-Item -ItemType Directory -Force -Path "$TempDir\CanvasApps" | Out-Null
New-Item -ItemType Directory -Force -Path "$TempDir\botcomponents" | Out-Null

# === COPIAR MANIFESTS ===
Write-Host "📄 Copiando manifests da solução..." -ForegroundColor Yellow
Copy-Item "$SrcDir\solution\solution.xml"          "$TempDir\solution.xml"
Copy-Item "$SrcDir\solution\customizations.xml"    "$TempDir\customizations.xml"
Copy-Item "$SrcDir\solution\[Content_Types].xml"   "$TempDir\[Content_Types].xml"

# === COPIAR FLOWS ===
Write-Host "⚡ Copiando flows Power Automate..." -ForegroundColor Yellow
$flows = Get-ChildItem "$SrcDir\flows" -Directory
foreach ($flow in $flows) {
    $defFile = Join-Path $flow.FullName "definition.json"
    if (Test-Path $defFile) {
        $destName = "$($flow.Name).json"
        Copy-Item $defFile "$TempDir\Workflows\$destName"
        Write-Host "   ✅ $($flow.Name)" -ForegroundColor Gray
    }
}

# === COPIAR BOT COPILOT STUDIO ===
Write-Host "🤖 Copiando Copilot Studio Bot..." -ForegroundColor Yellow
$botSrc = "$SrcDir\copilot-studio\VMO_Assistente"
if (Test-Path $botSrc) {
    Copy-Item -Recurse $botSrc "$TempDir\botcomponents\VMO_Assistente"
    Write-Host "   ✅ VMO_Assistente" -ForegroundColor Gray
}

# === CANVAS APP (opcional — requer PAC CLI) ===
if ($PackCanvasApp) {
    Write-Host "🎨 Empacotando Canvas App com PAC CLI..." -ForegroundColor Yellow
    $pacPath = (Get-Command "pac" -ErrorAction SilentlyContinue)?.Source
    if ($pacPath) {
        $canvasSrc = "$SrcDir\canvas-app\VMO_GAB_Dashboard"
        $msappPath = "$TempDir\CanvasApps\VMO_GAB_Dashboard.msapp"
        & pac canvas pack --sources $canvasSrc --msapp $msappPath
        if ($LASTEXITCODE -eq 0) {
            Write-Host "   ✅ Canvas App empacotado em .msapp" -ForegroundColor Green
        } else {
            Write-Host "   ⚠️  Erro ao empacotar Canvas App — copiando fontes YAML" -ForegroundColor Yellow
            Copy-Item -Recurse $canvasSrc "$TempDir\CanvasApps\VMO_GAB_Dashboard"
        }
    } else {
        Write-Host "   ⚠️  PAC CLI não encontrado — copiando fontes YAML" -ForegroundColor Yellow
        Copy-Item -Recurse "$SrcDir\canvas-app\VMO_GAB_Dashboard" "$TempDir\CanvasApps\VMO_GAB_Dashboard"
    }
} else {
    Write-Host "🎨 Copiando Canvas App (YAML source)..." -ForegroundColor Yellow
    Copy-Item -Recurse "$SrcDir\canvas-app\VMO_GAB_Dashboard" "$TempDir\CanvasApps\VMO_GAB_Dashboard"
    Write-Host "   ✅ Canvas App (YAML — use PAC CLI para empacotar como .msapp)" -ForegroundColor Gray
}

# === CRIAR ZIP ===
Write-Host "`n📦 Criando arquivo ZIP..." -ForegroundColor Yellow
$OutputFullPath = if ([System.IO.Path]::IsPathRooted($OutputPath)) {
    $OutputPath
} else {
    Join-Path $ScriptDir $OutputPath
}

if (Test-Path $OutputFullPath) { Remove-Item $OutputFullPath -Force }

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::CreateFromDirectory($TempDir, $OutputFullPath)

# === LIMPEZA ===
Remove-Item -Recurse -Force $TempDir

# === RELATÓRIO ===
$zipInfo = Get-Item $OutputFullPath
Write-Host "`n" + "="*50 -ForegroundColor Green
Write-Host "✅ BUILD CONCLUÍDO!" -ForegroundColor Green
Write-Host "="*50 -ForegroundColor Green
Write-Host "📦 Arquivo: $OutputFullPath" -ForegroundColor White
Write-Host "📏 Tamanho: $([math]::Round($zipInfo.Length/1KB, 1)) KB" -ForegroundColor White
Write-Host "`nConteúdo do pacote:" -ForegroundColor Cyan
Write-Host "  • solution.xml + customizations.xml" -ForegroundColor Gray
Write-Host "  • $($flows.Count) Power Automate Flows (Workflows/)" -ForegroundColor Gray
Write-Host "  • 1 Canvas App (CanvasApps/)" -ForegroundColor Gray
Write-Host "  • 1 Copilot Studio Bot (botcomponents/)" -ForegroundColor Gray
Write-Host "`n🔜 Para importar:" -ForegroundColor Cyan
Write-Host "  Power Platform Admin: https://admin.powerplatform.microsoft.com" -ForegroundColor DarkCyan
Write-Host "  → Solutions → Import Solution → Selecione VMO_GAB_Solution.zip" -ForegroundColor DarkCyan
