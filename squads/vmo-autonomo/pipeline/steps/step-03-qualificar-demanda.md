---
execution: inline
agent: felipe-filtro
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-validada.md
outputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao.md
---

# Step 03: Qualificar Demanda

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-validada.md` — demanda validada pelo usuário no checkpoint
- `squads/vmo-autonomo/pipeline/data/domain-framework.md` — critérios de qualificação VMO
- `squads/vmo-autonomo/pipeline/data/quality-criteria.md` — padrões de qualidade

## Instructions

### Process
1. **Executar tarefa `qualificar-demanda.md`**: Avaliar os 6 critérios de qualificação com pontuação justificada.
2. **Executar tarefa `analise-comercial.md`**: Aprofundar análise de ROI e criar proposta de valor.
3. **Compilar parecer completo**: Combinar as duas análises em documento único com decisão clara.
4. **Salvar output**: Escrever em `squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao.md`.

## Output Format

```markdown
# Parecer de Qualificação — [Nome da Demanda]
[output combinado das tasks qualificar-demanda e analise-comercial]
[incluir: 6 critérios, pontuação, decisão, análise de ROI, próximos passos]
```

## Output Example

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-047 | Data: 2026-04-11

CRITÉRIOS DE QUALIFICAÇÃO
1. Alinhamento Estratégico    4/5 — OKR Q1/2026: redução de falhas de fornecimento
2. Viabilidade Técnica        3/5 — API SAP disponível; integração requer POC
3. ROI                        4/5 — Payback estimado 23 meses com contingência
4. Urgência                   5/5 — 3 incidentes Q1/2026, reunião fornecedores jul/2026
5. Maturidade                 3/5 — Problema claro; sponsor e orçamento pendentes
6. Recursos                   3/5 — Orçamento sinalizado; TI com conflito SAP

PONTUAÇÃO: 22/30 (73%)
DECISÃO: APROVADO COM CONDIÇÕES

CONDIÇÕES BLOQUEANTES:
1. Designar sponsor executivo
2. Formalizar orçamento CAPEX
3. Validar disponibilidade TI

PROPOSTA DE VALOR:
"O projeto SRF, com investimento de R$ 336.000, entregará visibilidade em
tempo real sobre os 12 fornecedores Tier 1, prevenindo rupturas que custaram
R$ 135.000 em Q1/2026, com payback estimado de 23 meses."

PRÓXIMOS PASSOS: [ações com responsável e prazo]
```

## Veto Conditions

Reject and redo if ANY are true:
1. A decisão de qualificação não está explicitamente declarada
2. Algum dos 6 critérios está sem pontuação ou justificativa

## Quality Criteria

- [ ] Todos os 6 critérios avaliados com pontuação e justificativa
- [ ] ROI calculado com payback em meses
- [ ] Decisão emitida e coerente com a pontuação
- [ ] Condições bloqueantes listadas (se houver)
- [ ] Próximos passos com responsável e prazo
