---
execution: inline
agent: vera-veredito
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md
outputFile: squads/vmo-autonomo/projects/{project}/05-encerramento/revisao-final.md
on_reject: 5
---

# Step 11: Revisão de Qualidade

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — TAP + PM Canvas + Plano Geral
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md` — ERF com RFs e RNFs
- `squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md` — WBS + Cronograma detalhado
- `squads/vmo-autonomo/projects/{project}/03-planejamento/plano-riscos.md` — Registro de Riscos + Plano de Resposta
- `squads/vmo-autonomo/projects/{project}/03-planejamento/kpis.md` — Framework de KPIs e semáforo de saúde
- `squads/vmo-autonomo/projects/{project}/04-monitoramento/status-report-{date}.md` — Status Report #001 + Pesquisa de Satisfação
- `squads/vmo-autonomo/pipeline/data/quality-criteria.md` — critérios de qualidade por documento
- `squads/vmo-autonomo/pipeline/data/anti-patterns.md` — anti-padrões e bloqueadores conhecidos

## Instructions

### Process
1. **Executar tarefa `revisar-documentacao.md`**: Revisar cada documento do pacote contra os critérios de qualidade.
2. **Pontuação consolidada**: Calcular score ponderado do pacote completo (mínimo 85/100 para aprovação).
3. **Decisão de veredito**:
   - Score ≥ 85 e nenhum bloqueador CRÍTICO: **APROVADO** → prosseguir para Step 12
   - Score < 85 ou qualquer bloqueador CRÍTICO: **REPROVADO** → retornar ao Step 5 (on_reject: 5)
4. **Se reprovado**: Listar exatamente quais documentos falharam e quais critérios precisam ser corrigidos.
5. **Salvar output**: Escrever relatório completo em `squads/vmo-autonomo/projects/{project}/05-encerramento/revisao-final.md`.

### Rejection Loop
Quando `on_reject: 5` é acionado, o pipeline retorna ao Step 5 (Diana Documento) com:
- Lista dos documentos reprovados
- Critérios específicos que falharam
- Recomendações de correção por documento

## Output Format

```markdown
# Relatório de Revisão de Qualidade — [Nome do Projeto]

## Resultado: [APROVADO ✅ | REPROVADO ❌]

## Pontuação Consolidada: [XX/100]

## Avaliação por Documento

### TAP — [XX/20 pontos]
[Status: ✅ Aprovado | ⚠️ Condicionado | ❌ Reprovado]
[Critérios atendidos e não atendidos]

### PM Canvas — [XX/10 pontos]
[...]

### ERF — [XX/15 pontos]
[...]

### Cronograma — [XX/20 pontos]
[...]

### Plano de Riscos — [XX/15 pontos]
[...]

### Framework de KPIs — [XX/10 pontos]
[...]

### Status Report Inicial — [XX/10 pontos]
[...]

## Bloqueadores Críticos
[Lista de bloqueadores CRÍTICOS encontrados, ou "Nenhum"]

## Recomendações
[Se aprovado: pontos de atenção para execução]
[Se reprovado: instruções específicas de correção para retorno ao Step 5]

## Assinatura do Revisor
- Revisado por: Vera Veredito — Analista de Qualidade VMO
- Data: [data]
- Versão do pacote revisado: v1.0
```

## Output Example

> Ver `pipeline/data/quality-criteria.md` — tabela de pontuação ponderada e critérios por documento.

## Veto Conditions

Reject and redo if ANY are true:
1. Pontuação calculada sem os pesos corretos da tabela em `quality-criteria.md`
2. Decisão de aprovação/reprovação ausente ou ambígua
3. Bloqueadores CRÍTICOS presentes mas decisão marcada como APROVADO
4. Reprovação sem lista específica de critérios que falharam (não é possível corrigir sem saber o quê)

## Quality Criteria

- [ ] Todos os 7 documentos avaliados individualmente
- [ ] Score ponderado calculado corretamente (soma ≤ 100)
- [ ] Veredito claro: APROVADO ou REPROVADO
- [ ] Se reprovado: instruções de correção acionáveis por documento
- [ ] Se aprovado: recomendações para fase de execução documentadas
- [ ] Assinatura do revisor com data presente
