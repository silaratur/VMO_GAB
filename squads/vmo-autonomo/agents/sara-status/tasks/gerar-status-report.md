---
task: "Gerar Status Report"
order: 1
input:
  - documentacao_base: "TAP e Plano Geral com critérios de sucesso e baseline"
  - kpis: "Framework de KPIs com valores atuais (se execução) ou baseline (se iniciação)"
  - plano_riscos: "Registro de riscos atualizado"
output:
  - status_report: "Status Report completo com semáforo, progresso, issues e próximos passos"
---

# Gerar Status Report

Produz o Status Report do projeto — documento de comunicação periódica que informa todos os stakeholders sobre o status atual, desvios do plano, issues abertas e próximos passos. Para a fase de iniciação, gera o primeiro status report (template do projeto).

## Process

1. **Definir período coberto**: Para o primeiro report (iniciação), o período é "pré-execução — documentação de iniciação".
2. **Calcular o status por dimensão**: Com base nos KPIs disponíveis (ou placeholders para execução futura), definir o semáforo de cada dimensão.
3. **Documentar progresso**: Listar entregas completadas, em andamento e pendentes.
4. **Registrar issues abertas**: Todos os problemas identificados com responsável, prazo e próximo passo.
5. **Definir próximos passos**: 3-5 ações concretas para o próximo período, com responsável e data.

## Output Format

```markdown
STATUS REPORT — [Nome do Projeto]
Período: [início] a [fim] | Data: YYYY-MM-DD | Report #[N]
Gerente de Projeto: [nome]

STATUS GERAL: [🟢 NORMAL / 🟡 ATENÇÃO / 🔴 ALERTA]

| Dimensão | Status | KPI Principal |
|----------|--------|---------------|
| Cronograma | 🟢/🟡/🔴 | SPI: [valor] |
| Custo | 🟢/🟡/🔴 | CPI: [valor] |
| Escopo | 🟢/🟡/🔴 | Mudanças: [N] |
| Riscos | 🟢/🟡/🔴 | Riscos altos: [N] |
| Qualidade | 🟢/🟡/🔴 | [indicador] |

PROGRESSO
  Planejado: [%] | Realizado: [%] | Desvio: [%]

ISSUES ABERTAS
  | ID | Issue | Impacto | Responsável | Prazo |

PRÓXIMOS PASSOS
  1. [ação] — [responsável] — [data]
```

## Output Example

> Ver `pipeline/data/output-examples.md` — Exemplo 3 (Status Report completo para projeto SRF).

## Quality Criteria

- [ ] Semáforo consolidado presente no topo
- [ ] Semáforo por dimensão (5 dimensões mínimas)
- [ ] Progresso em percentual com comparação ao baseline
- [ ] Issues abertas com responsável e prazo
- [ ] Mínimo 3 próximos passos com responsável e data
- [ ] Sumário executivo legível em menos de 2 minutos

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Semáforo geral ausente ou não baseado em thresholds documentados no framework de KPIs
2. Issues listadas sem responsável ou sem prazo de resolução
