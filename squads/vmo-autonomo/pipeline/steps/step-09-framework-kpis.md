---
execution: subagent
agent: marcela-metrica
inputFile: squads/vmo-autonomo/output/documentacao-base.md
outputFile: squads/vmo-autonomo/output/kpis.md
model_tier: fast
---

# Step 09: Framework de KPIs

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/output/documentacao-base.md` — TAP com critérios de sucesso e plano com baseline de custo
- `squads/vmo-autonomo/output/cronograma.md` — baseline de prazo para EVM
- `squads/vmo-autonomo/output/plano-riscos.md` — riscos para KPIs de gestão de riscos
- `squads/vmo-autonomo/pipeline/data/quality-criteria.md` — critérios de qualidade para calibrar thresholds

## Instructions

### Process
1. **Executar tarefa `definir-kpis.md`**: Definir todos os KPIs com metas, thresholds e responsáveis.
2. **Configurar EVM**: Definir BAC, método de medição de EV e regras por tipo de entregável.
3. **Criar semáforo de saúde**: Tabela de thresholds verde/amarelo/vermelho por dimensão.
4. **Salvar output**: Escrever framework completo em `squads/vmo-autonomo/output/kpis.md`.

## Output Format

```markdown
# Framework de KPIs — [Nome do Projeto]

## KPIs de Desempenho do Projeto (EVM)
[tabela CPI, SPI, EAC, VAC]

## KPIs de Resultado
[tabela derivada dos critérios de sucesso do TAP]

## Configuração EVM
[BAC, método de medição de EV, regras por tipo]

## Semáforo de Saúde
[tabela de thresholds por dimensão]
```

## Output Example

> Ver o exemplo completo no `definir-kpis.md` — Projeto SRF com KPIs de EVM e resultado.

## Veto Conditions

Reject and redo if ANY are true:
1. CPI e SPI ausentes do framework
2. Nenhum KPI derivado dos critérios de sucesso do TAP

## Quality Criteria

- [ ] KPIs EVM obrigatórios (CPI, SPI, EAC, VAC)
- [ ] KPIs de resultado vinculados aos critérios de sucesso do TAP
- [ ] Thresholds verde/amarelo/vermelho por KPI
- [ ] Configuração EVM com BAC e método de medição
