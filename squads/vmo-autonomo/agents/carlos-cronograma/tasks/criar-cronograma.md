---
task: "Criar Cronograma Detalhado"
order: 2
input:
  - wbs: "WBS com pacotes de trabalho"
  - tap: "TAP com fases e restrições de prazo"
output:
  - cronograma: "Cronograma detalhado em Markdown com marcos, dependências e caminho crítico"
---

# Criar Cronograma Detalhado

Transforma a WBS em um cronograma detalhado com datas, duração estimada, dependências, responsáveis, marcos e caminho crítico identificado.

## Process

1. **Atribuir duração a cada pacote de trabalho**: Usando o intervalo identificado na WBS, estimar a duração realista (dias ou semanas) de cada pacote, respeitando o limite de 2 semanas por pacote.
2. **Definir dependências**: Identificar relacionamentos entre pacotes de trabalho (Término-Início principalmente; documentar exceções).
3. **Calcular datas de início e fim**: A partir da data de início do projeto (TAP), calcular início e fim de cada atividade respeitando as dependências.
4. **Identificar o caminho crítico**: Sequência de atividades com zero folga que determina a data mínima de conclusão.
5. **Adicionar buffer de contingência**: Reserva explícita de 15% do prazo total como buffer de gestão ao final do cronograma.

## Output Format

```markdown
# CRONOGRAMA — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD
Início do Projeto: YYYY-MM-DD
Conclusão Prevista: YYYY-MM-DD (sem buffer) / YYYY-MM-DD (com buffer 15%)

## Cronograma por Fase

### [Fase 1 — Nome]
| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | Caminho Crítico |
|----|-----------|--------|-----|---------|-------------|-------------|-----------------|
| 1.1 | [atividade] | YYYY-MM-DD | YYYY-MM-DD | Nd | - | [pessoa/área] | ⭐ |

### Marcos Principais
| Marco | Data | Critério |
|-------|------|----------|
| M1 — [nome] | YYYY-MM-DD | [o que precisa estar verdadeiro] |

### Buffer de Contingência
| Item | Prazo | Observação |
|------|-------|------------|
| Buffer de gestão (15%) | +[N] semanas | Reserva centralizada, gerenciada pelo GP |
```

## Output Example

```markdown
# CRONOGRAMA — SRF (Sistema de Rastreamento de Fornecedores)
Versão: 1.0 | Data: 2026-04-15
Início: 2026-05-01 | Conclusão sem buffer: 2026-11-28 | Com buffer (15%): 2026-12-19

## Fase 1 — Requisitos e Arquitetura (01/05 – 31/05)
| ID | Atividade | Início | Fim | Dur. | Dep. | Responsável | ⭐ |
|----|-----------|--------|-----|------|------|-------------|-----|
| 1.2.1.1 | Workshop de requisitos Supply Chain | 01/05 | 07/05 | 5d | - | GP + TI | ⭐ |
| 1.2.1.2 | Especificação técnica integração SAP | 08/05 | 16/05 | 7d | 1.2.1.1 | TI SAP | ⭐ |
| 1.2.1.3 | Revisão e aprovação da ERF | 17/05 | 21/05 | 3d | 1.2.1.2 | GP | ⭐ |
| 1.2.2.1 | Design da arquitetura cloud | 08/05 | 16/05 | 7d | 1.2.1.1 | TI Infra | - |
| 1.2.2.2 | POC de integração API SAP MM | 17/05 | 28/05 | 8d | 1.2.1.2 | TI SAP | ⭐ |
| 1.2.2.3 | Aprovação da arquitetura | 29/05 | 31/05 | 2d | 1.2.2.2 | Sponsor | ⭐ |

## Fase 2 — Desenvolvimento (01/06 – 31/08)
| ID | Atividade | Início | Fim | Dur. | Dep. | Responsável | ⭐ |
|----|-----------|--------|-----|------|------|-------------|-----|
| 1.3.1.1 | Dev: agente de coleta GPS | 01/06 | 14/06 | 10d | 1.2.2.3 | Dev 1 | - |
| 1.3.2.1 | Dev: middleware SAP | 01/06 | 18/06 | 13d | 1.2.2.2 | Dev SAP | ⭐ |
| 1.3.3.1 | Dev: dashboard (mapa + lista) | 15/06 | 05/07 | 15d | 1.3.1.1 | Dev Front | - |
| 1.3.4.1 | Dev: motor de alertas | 01/07 | 15/07 | 11d | 1.3.2.1 | Dev Back | ⭐ |
| 1.3.4.2 | Integração Teams + e-mail | 16/07 | 25/07 | 8d | 1.3.4.1 | Dev Back | ⭐ |
| [Integração e testes internos] | 26/07 | 31/08 | 25d | todos | TI | ⭐ |

## Fase 3 — Testes (01/09 – 30/09)
[formato idêntico]

## Fase 4 — Implantação (01/10 – 31/10)
[formato idêntico]

## Marcos Principais
| Marco | Data | Critério |
|-------|------|----------|
| M1 — Kick-off | 2026-05-01 | TAP assinado e equipe mobilizada |
| M2 — ERF aprovada | 2026-05-21 | ERF assinada pelo solicitante |
| M3 — Arquitetura aprovada | 2026-05-31 | POC bem-sucedida e sponsor aprovada |
| M4 — Dev completo | 2026-08-31 | 100% dos RF Must Have desenvolvidos |
| M5 — UAT aprovado | 2026-09-30 | Todos os casos de teste Must Have aprovados |
| M6 — Go-live | 2026-10-01 | Sistema em produção com 12 fornecedores |
| M7 — Encerramento | 2026-12-31 | Aceite formal do cliente + lições aprendidas |

## Buffer de Contingência
| Item | Prazo | Observação |
|------|-------|------------|
| Buffer de gestão (15%) | +5,5 semanas | Reserva centralizada ao final do projeto |
| Baseline sem buffer: 26/11/2026 | | |
| Deadline máximo: 31/12/2026 | | Buffer consome ao máximo 5 semanas |

## Caminho Crítico
1.2.1.1 → 1.2.1.2 → 1.2.2.2 → 1.2.2.3 → 1.3.2.1 → 1.3.4.1 → 1.3.4.2 → [Integração] → UAT → Go-live
Folga total do caminho crítico: 0 dias
```

## Quality Criteria

- [ ] Todas as atividades têm data de início, fim e duração
- [ ] Dependências documentadas entre atividades do caminho crítico
- [ ] Caminho crítico identificado e marcado com ⭐
- [ ] Todos os marcos principais do TAP aparecem no cronograma
- [ ] Buffer de contingência de ao menos 15% explícito e centralizado
- [ ] Nenhuma atividade individual com duração > 10 dias úteis

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Nenhum caminho crítico identificado no cronograma
2. Buffer de contingência ausente ou embutido nas atividades individuais (deve ser centralizado)
