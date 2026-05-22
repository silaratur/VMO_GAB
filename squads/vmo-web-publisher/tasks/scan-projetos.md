---
task: "Escanear Projetos"
agent: lucas-layout
order: 1
---

# Escanear Projetos

## Objetivo

Identificar todos os projetos presentes em `squads/vmo-autonomo/projects/` e construir a lista de projetos para processamento nos steps seguintes.

## Processo

1. Listar todas as subpastas de `squads/vmo-autonomo/projects/` — cada subpasta é um projeto ou demanda
2. Para cada pasta encontrada, registrar:
   - **ID**: nome da pasta (ex: `PROJ-2026-001`, `DEM-2026-007`)
   - **Tipo**: PROJ = projeto formal; DEM = demanda em instrução
   - **Arquivos presentes**: quais fases existem (01 a 05)
   - **Status report mais recente**: nome do arquivo em `04-monitoramento/`
   - **state.json**: se existe, qual o status registrado
3. Comparar com a lista da última run (memories.md) para identificar projetos novos
4. Registrar projetos novos como `🔵 NOVO` no index

## Output

Lista estruturada de projetos para os steps 2, 3 e 4:
```
[
  { id: "PROJ-2026-001", tipo: "PROJ", fases: [1,2,3,4,5], status_report: "status-report-inicial.md" },
  { id: "DEM-2026-007", tipo: "DEM", fases: [1,2,3,5], status_report: null },
  ...
]
```
