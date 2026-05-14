---
task: "Revisar Documentação do Projeto"
order: 1
input:
  - documentacao_base: "TAP, PM Canvas e Plano Geral (output/documentacao-base.md)"
  - requisitos: "Especificação de Requisitos Funcionais (output/requisitos.md)"
  - cronograma: "WBS e Cronograma detalhado (output/cronograma.md)"
  - plano_riscos: "Registro de Riscos e Plano de Resposta (output/plano-riscos.md)"
  - kpis: "Framework de KPIs (output/kpis.md)"
  - status_report: "Status Report inicial (output/status-report-inicial.md)"
  - quality_criteria: "pipeline/data/quality-criteria.md"
output:
  - revisao_final: "Veredicto consolidado com pontuação por documento e plano de correção"
---

# Revisar Documentação do Projeto

Avalia toda a documentação de iniciação gerada pelo squad contra os critérios de qualidade VMO/PMBOK. Emite veredicto com pontuação ponderada e plano de correção específico para cada não-conformidade.

## Process

1. **Carregar critérios de qualidade**: Ler completamente `pipeline/data/quality-criteria.md` antes de iniciar qualquer avaliação.
2. **Verificar consistência cross-documentos**: Checar se prazo, custo, escopo e stakeholders são idênticos em TAP, PM Canvas e Cronograma. Inconsistências são flagradas antes de avaliar documentos individuais.
3. **Avaliar cada documento contra critérios BLOCKING**: Se qualquer critério BLOCKING não for atendido, o documento recebe REPROVADO imediatamente.
4. **Pontuar critérios de qualidade (1-10)**: Para cada critério não-BLOCKING, atribuir nota com justificativa de ao menos 1 linha.
5. **Calcular pontuação ponderada**: TAP 25%, ERF 15%, Cronograma 20%, Riscos 15%, PM Canvas 10%, KPIs 10%, Status Report 5%.
6. **Emitir veredicto e plano de correção**: Listar todas as correções requeridas com localização exata, problema e ação corretiva.

## Output Format

```markdown
REVISÃO DE QUALIDADE — VMO AUTÔNOMO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Projeto: [nome]
Data da Revisão: YYYY-MM-DD
Revisão: N de 3

VEREDICTO: [🟢 APROVADO / 🟡 APROVADO COM CONDIÇÕES / 🔴 REPROVADO]

PONTUAÇÃO CONSOLIDADA

| Documento | Peso | Pontuação | Status |
|-----------|------|-----------|--------|
| TAP | 25% | X.X/10 | [status] |
| PM Canvas | 10% | X.X/10 | [status] |
| ERF | 15% | X.X/10 | [status] |
| Cronograma | 20% | X.X/10 | [status] |
| Plano de Riscos | 15% | X.X/10 | [status] |
| KPIs | 10% | X.X/10 | [status] |
| Status Report | 5% | X.X/10 | [status] |
| CONSOLIDADO | 100% | X.X/10 | [VEREDICTO] |

PONTOS FORTES
  ✅ [ponto forte 1]
  ✅ [ponto forte 2]
  ✅ [ponto forte 3]

CONDIÇÕES REQUERIDAS (corrigir antes de avançar)
  1. [Documento] — [Seção] — [problema + ação corretiva específica]

SUGESTÕES (não bloqueantes)
  - [sugestão de melhoria]

PRÓXIMO PASSO
  [instrução clara para o time]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Output Example

> Ver `pipeline/data/output-examples.md` — Seção "Vera Veredito" com exemplo completo de revisão.

## Quality Criteria

- [ ] Todos os 7 documentos avaliados
- [ ] Critérios BLOCKING verificados para cada documento
- [ ] Pontuação ponderada calculada corretamente (soma dos pesos = 100%)
- [ ] Ao menos 3 pontos fortes documentados
- [ ] Cada condição requerida tem: documento, seção, problema, ação corretiva
- [ ] Veredicto coerente com as pontuações calculadas
- [ ] Número da revisão rastreado (N de 3)

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. O veredicto é "APROVADO" mas há critérios BLOCKING não atendidos em qualquer documento
2. Algum documento dos 7 não foi avaliado e a revisão foi emitida mesmo assim
