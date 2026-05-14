---
task: "Analisar Performance"
order: 2
input:
  - kpis_definidos: "Framework de KPIs com baselines e metas"
  - dados_atuais: "Dados de progresso do projeto (informados pelo usuário ou coletados)"
output:
  - analise_performance: "Análise de performance com EVM, semáforo e recomendações"
---

# Analisar Performance

Coleta e interpreta os dados de performance do projeto, calcula os indicadores EVM, atualiza o semáforo de saúde e gera análise com recomendações acionáveis. Usada tanto na iniciação (para estruturar o framework de monitoramento) quanto durante a execução.

## Process

1. **Coletar dados disponíveis**: Ler os dados de progresso fornecidos (% concluído por pacote, custos incorridos, etc.).
2. **Calcular EVM**: Derivar EV, PV e AC para o período; calcular CPI, SPI, EAC e VAC.
3. **Atualizar semáforo**: Comparar cada KPI com os thresholds e atualizar o semáforo por dimensão.
4. **Identificar padrões e anomalias**: Variações > 10% do plano são analisadas; variações > 25% são sinalizadas como críticas.
5. **Formular recomendações**: Para cada dimensão em amarelo ou vermelho, gerar 1-2 recomendações específicas e acionáveis.

## Output Format

```markdown
# ANÁLISE DE PERFORMANCE — [Nome do Projeto]
Período: [início] a [fim] | Data: YYYY-MM-DD | Análise: N/[total]

## STATUS GERAL: [🟢/🟡/🔴]
[1 linha de sumário executivo]

| Dimensão | Status | Indicador |
|----------|--------|-----------|
| Cronograma | 🟢/🟡/🔴 | SPI: [valor] |
| Custo | 🟢/🟡/🔴 | CPI: [valor] |

## Earned Value Management

| Indicador | Valor | Interpretação |
|-----------|-------|---------------|
| PV (Planned Value) | R$ [valor] | [o que deveria estar feito] |
| EV (Earned Value) | R$ [valor] | [o que foi feito de fato] |
| AC (Actual Cost) | R$ [valor] | [o que foi gasto] |
| CPI | [valor] | [interpretação] |
| SPI | [valor] | [interpretação] |
| EAC | R$ [valor] | [previsão de custo final] |
| VAC | R$ [valor] | [desvio previsto] |

## Recomendações

1. [ação específica] — Responsável: [nome] — Prazo: [data]
```

## Output Example

> Ver `pipeline/data/output-examples.md` — Exemplo 3 (Status Report com EVM e semáforo).

## Quality Criteria

- [ ] EVM completo: PV, EV, AC, CPI, SPI, EAC e VAC calculados
- [ ] Semáforo atualizado por dimensão (prazo, custo, escopo, riscos, qualidade)
- [ ] Cada indicador em amarelo ou vermelho tem recomendação acionável
- [ ] Anomalias > 25% sinalizadas explicitamente
- [ ] Interpretação de negócio para cada indicador ("isso significa...")

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. EVM calculado apenas com CPI e SPI sem EAC e VAC (previsão de custo final é obrigatória)
2. Indicadores em vermelho sem nenhuma recomendação de ação associada
