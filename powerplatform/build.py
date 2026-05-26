#!/usr/bin/env python3
"""
Build script: empacota a solução VMO GAB como ZIP importável no Power Platform.
Uso: python build.py
"""

import os
import zipfile
import shutil
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent
OUT  = BASE / "VMO_GAB_Solution.zip"

# Mapeamento: (source_path, dest_in_zip)
FILES = [
    # Manifests
    (BASE / "solution" / "solution.xml",         "solution.xml"),
    (BASE / "solution" / "customizations.xml",   "customizations.xml"),
    (BASE / "solution" / "[Content_Types].xml",  "[Content_Types].xml"),
]

# Flows
flows_dir = BASE / "flows"
for flow_dir in sorted(flows_dir.iterdir()):
    def_file = flow_dir / "definition.json"
    if def_file.exists():
        FILES.append((def_file, f"Workflows/{flow_dir.name}.json"))

# Canvas App
canvas_dir = BASE / "canvas-app" / "VMO_GAB_Dashboard"
for f in canvas_dir.rglob("*"):
    if f.is_file():
        rel = f.relative_to(canvas_dir)
        FILES.append((f, f"CanvasApps/VMO_GAB_Dashboard/{rel}"))

# Copilot Studio Bot
bot_dir = BASE / "copilot-studio" / "VMO_Assistente"
for f in bot_dir.rglob("*"):
    if f.is_file():
        rel = f.relative_to(bot_dir)
        FILES.append((f, f"botcomponents/VMO_Assistente/{rel}"))

print(f"\n🏗️  VMO GAB — Build Solution Package")
print("="*50)
print(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M')}")

if OUT.exists():
    OUT.unlink()
    print(f"🗑️  Removido ZIP anterior")

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
    for src, dst in FILES:
        if src.exists():
            zf.write(src, dst)
            print(f"   ✅ {dst}")
        else:
            print(f"   ⚠️  FALTANDO: {src}")

size_kb = OUT.stat().st_size / 1024
print(f"\n{'='*50}")
print(f"✅ BUILD CONCLUÍDO!")
print(f"📦 {OUT}")
print(f"📏 {size_kb:.1f} KB  |  {len(FILES)} arquivos")
print(f"\n🔜 Para importar:")
print(f"   Power Platform Admin Center → Solutions → Import Solution")
print(f"   Selecione: {OUT.name}")
