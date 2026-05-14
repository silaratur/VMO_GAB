---
task: "Definir Framework de KPIs"
order: 1
input:
  - tap: "TAP com critérios de sucesso e objetivos"
  - cronograma: "Cronograma com baseline de prazo"
  - plano_geral: "Plano geral com baseline de custo"
output:
  - framework_kpis: "Definição completa dos KPIs do projeto com metas, alertas e responsáveis"
---

# Definir Framework de KPIs

Estabelece o framework completo de indicadores de performance do projeto, definindo quais KPIs serão monitorados, como serão calculados, qual a meta e os limites de alerta, quem é responsável por cada um e com que frequência serão atualizados.

## Process

1. **Derivar KPIs dos critérios de sucesso do TAP**: Cada critério de sucesso deve ter ao menos 1 KPI que mede seu progresso.
2. **Definir KPIs obrigatórios de EVM**: CPI, SPI, EAC e VAC são sempre obrigatórios.
3. **Estabelecer baselines**: Definir o valor baseline de cada KPI (ponto de partida ou meta) para permitir comparação.
4. **Definir thresholds**: Para cada KPI, definir limites verde/amarelo/vermelho.
5. **Atribuir responsável e frequência**: Quem coleta, calcula e reporta cada KPI, e com que frequência.

## Output Format

```markdown
# FRAMEWORK DE KPIs — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|---------|----------|------|-----------|------------|-------|-------------|
| CPI | EV / AC | 1,00 | ≥ 1,00 | 0,85-0,95 | < 0,85 | Quinzenal | GP |
| SPI | EV / PV | 1,00 | ≥ 1,00 | 0,85-0,95 | < 0,85 | Quinzenal | GP |

## KPIs de Resultado do Projeto

| KPI | Descrição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|-----------|----------|------|-----------|------------|-------|-------------|
| [KPI] | [como é medido] | [valor inicial] | [meta] | [limiar] | [limiar] | [freq.] | [resp.] |

## Semáforo de Saúde

| Dimensão | Verde | Amarelo | Vermelho |
|----------|-------|---------|----------|
| Cronograma | SPI ≥ 0,95 | 0,85–0,95 | < 0,85 |
| Custo | CPI ≥ 0,95 | 0,85–0,95 | < 0,85 |
```

## Output Example

```markdown
# FRAMEWORK DE KPIs — SRF
Versão: 1.0 | Data: 2026-04-16

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|---------|----------|------|-----------|------------|-------|-------------|
| CPI (Cost Performance Index) | EV / AC | 1,00 | ≥ 1,00 | 0,85–0,95 | < 0,85 | Quinzenal | GP |
| SPI (Schedule Performance Index) | EV / PV | 1,00 | ≥ 1,00 | 0,85–0,95 | < 0,85 | Quinzenal | GP |
| EAC (Estimate at Completion) | BAC / CPI | R$ 336.000 | ≤ R$ 336.000 | R$ 336k–370k | > R$ 370k | Quinzenal | GP |
| VAC (Variance at Completion) | BAC – EAC | R$ 0 | ≥ R$ 0 | R$ -34k a R$ 0 | < -R$ 34k | Quinzenal | GP |

## KPIs de Resultado do Projeto

| KPI | Descrição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|-----------|----------|------|-----------|------------|-------|-------------|
| Cobertura Tier 1 | % dos 12 fornecedores integrados ao sistema | 0% | 100% até 30/09 | < 80% em 30/09 | < 50% em 30/09 | Mensal | TI |
| Redução de Rupturas | % de redução de incidentes vs. Q1/2026 | 0% | ≥ 40% em H2/2026 | 20-39% | < 20% | Trimestral | Supply Chain |
| Disponibilidade do Sistema | % de uptime do sistema | 0% | ≥ 99,5% | 98–99,5% | < 98% | Semanal (pós-go-live) | TI |
| Adoção Supply Chain | % de usuários ativos após 60 dias do go-live | 0% | ≥ 90% | 70–89% | < 70% | Mensal (pós-go-live) | GP |
| Satisfação do Cliente Interno | NPS (0-10) — pesquisa pós-go-live | - | ≥ 8/10 | 6–7/10 | < 6/10 | Pós-go-live (30d) | GP |
| Alertas com Falso Positivo | % de alertas enviados sem atraso real | 0% | ≤ 5% | 5–10% | > 10% | Mensal (pós-go-live) | TI |

## Configuração EVM

- **BAC (Budget at Completion):** R$ 336.000
- **Método de Medição de EV:** Porcentagem física concluída por pacote de trabalho (baseada em entregáveis aprovados)
- **Regra de EV por tipo de atividade:**
  - Entregáveis de documentação: 0/100 (0% até aprovação, 100% após)
  - Entregáveis de desenvolvimento: 50/50 (50% ao início do desenvolvimento, 50% ao teste aprovado)
  - Atividades de gerenciamento: proporcional ao tempo decorrido

## Semáforo de Saúde

| Dimensão | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|----------|----------|-----------|------------|
| Cronograma | SPI ≥ 0,95 | 0,85–0,95 | < 0,85 |
| Custo | CPI ≥ 0,95 | 0,85–0,95 | < 0,85 |
| Escopo | Sem mudanças de escopo | 1–2 mudanças aprovadas | > 2 mudanças |
| Riscos | Todos os riscos sob controle | 1 risco ALTO ativo sem mitigação | Risco CRÍTICO ativo |
| Satisfação Cliente | ≥ 8/10 | 6–7/10 | < 6/10 |
```

## Quality Criteria

- [ ] KPIs de EVM (CPI, SPI, EAC, VAC) presentes com baselines e metas
- [ ] KPIs de resultado derivados dos critérios de sucesso do TAP
- [ ] Todos os KPIs com threshold verde/amarelo/vermelho
- [ ] Responsável e frequência de medição definidos por KPI
- [ ] Configuração EVM com BAC e método de medição de EV
- [ ] Semáforo de saúde com 5 dimensões (prazo, custo, escopo, riscos, satisfação)

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. KPIs de EVM (CPI e SPI) ausentes — são sempre obrigatórios em projetos com orçamento definido
2. Nenhum KPI derivado dos critérios de sucesso do TAP (os KPIs devem medir o que o projeto prometeu entregar)
