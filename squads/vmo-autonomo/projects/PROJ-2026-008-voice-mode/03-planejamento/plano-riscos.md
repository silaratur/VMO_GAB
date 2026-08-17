# Plano de Riscos — Estudo de Viabilidade Voice Mode

**Projeto:** PROJ-2026-008-voice-mode
**Data:** 17/08/2026
**Analista:** Pedro Perigo
**Versão:** 1.0

---

## Registro de Riscos

### RISCO 1 — Prazo insuficiente para análise completa
| Campo | Valor |
|---|---|
| **ID** | RSK-001 |
| **Categoria** | Prazo |
| **Descrição** | O prazo de 1 dia útil pode ser insuficiente para análise profunda das 3 soluções nos 7 critérios, resultando em estudo superficial |
| **Probabilidade** | Alta (4/5) |
| **Impacto** | Alto (4/5) |
| **Severidade** | 16/25 — CRÍTICO |
| **Estratégia** | MITIGAR — priorizar critérios mais relevantes; focar em dados disponíveis; aceitar análise de alto nível onde dados profundos não estiverem acessíveis |
| **Trigger** | Ao final do dia 17/08 sem levantamento técnico concluído |
| **Responsável** | Neemias Buceli |
| **Prazo da ação** | 17/08/2026 17:00 |

### RISCO 2 — Dados de custo indisponíveis
| Campo | Valor |
|---|---|
| **ID** | RSK-002 |
| **Categoria** | Financeiro |
| **Descrição** | Informações de custo (licenciamento, infra, operação) das 3 soluções podem não estar disponíveis publicamente, impossibilitando análise de TCO |
| **Probabilidade** | Média (3/5) |
| **Impacto** | Médio (3/5) |
| **Severidade** | 9/25 — MODERADO |
| **Estratégia** | ACEITAR — documentar que TCO não pôde ser calculado por indisponibilidade de dados; recomendar levantamento específico como próximo passo |
| **Trigger** | Pesquisa de custos retorna dados incompletos ou indisponíveis |
| **Responsável** | Analista Data AI |
| **Prazo da ação** | 17/08/2026 |

### RISCO 3 — Roadmap Microsoft incerto
| Campo | Valor |
|---|---|
| **ID** | RSK-003 |
| **Categoria** | Técnico |
| **Descrição** | O prazo de disponibilidade de Voice Mode no Microsoft Teams/Copilot Studio é incerto (1-3 meses estimados), tornando análise de prazo da solução 2 inconclusiva |
| **Probabilidade** | Alta (4/5) |
| **Impacto** | Médio (3/5) |
| **Severidade** | 12/25 — ALTO |
| **Estratégia** | MITIGAR — documentar cenários (otimista: 1 mês, pessimista: 3+ meses); recomendar monitoramento do roadmap Microsoft; avaliar alternativa interim |
| **Trigger** | Documentação Microsoft não fornece data de GA (General Availability) para Voice Mode |
| **Responsável** | Analista Data AI |
| **Prazo da ação** | 17/08/2026 |

### RISCO 4 — Sponsor não confirmado
| Campo | Valor |
|---|---|
| **ID** | RSK-004 |
| **Categoria** | Stakeholders |
| **Descrição** | Ausência de sponsor formal pode comprometer a autoridade da recomendação e a implementação da decisão resultante do estudo |
| **Probabilidade** | Média (3/5) |
| **Impacto** | Alto (4/5) |
| **Severidade** | 12/25 — ALTO |
| **Estratégia** | MITIGAR — entregar o estudo mesmo sem sponsor formal; escalar a necessidade de sponsor para a fase de implementação |
| **Trigger** | 18/08/2026 sem confirmação de sponsor |
| **Responsável** | Neemias Buceli |
| **Prazo da ação** | 18/08/2026 |

### RISCO 5 — Solução Fireflies descontinuada antes da decisão
| Campo | Valor |
|---|---|
| **ID** | RSK-005 |
| **Categoria** | Técnico |
| **Descrição** | A solução Fireflies, atualmente funcional mas não homologada, pode ser bloqueada pela TI antes que a decisão formal seja tomada, eliminando a referência operacional |
| **Probabilidade** | Baixa (2/5) |
| **Impacto** | Médio (3/5) |
| **Severidade** | 6/25 — BAIXO |
| **Estratégia** | ACEITAR — documentar funcionalidades da Fireflies no estudo como referência, independente de disponibilidade futura |
| **Trigger** | TI emite comunicação de bloqueio de Fireflies |
| **Responsável** | Neemias Buceli / ITeam |
| **Prazo da ação** | Contínuo |

### RISCO 6 — Viés do solicitante na recomendação
| Campo | Valor |
|---|---|
| **ID** | RSK-006 |
| **Categoria** | Stakeholders |
| **Descrição** | O solicitante pode ter preferência por uma solução específica, influenciando a objetividade da análise comparativa |
| **Probabilidade** | Média (3/5) |
| **Impacto** | Médio (3/5) |
| **Severidade** | 9/25 — MODERADO |
| **Estratégia** | MITIGAR — usar critérios objetivos e pontuação ponderada; documentar evidência para cada avaliação; submeter a revisão independente |
| **Trigger** | Recomendação favorece solução sem justificativa proporcional à pontuação |
| **Responsável** | Pipeline VMO (revisão de qualidade) |
| **Prazo da ação** | 18/08/2026 |

---

## Matriz de Riscos

|  | Impacto Baixo (1-2) | Impacto Médio (3) | Impacto Alto (4-5) |
|---|---|---|---|
| **Prob. Alta (4-5)** | — | RSK-003 | **RSK-001** |
| **Prob. Média (3)** | — | RSK-002, RSK-006 | RSK-004 |
| **Prob. Baixa (1-2)** | — | RSK-005 | — |

---

## Reserva de Contingência

| Dimensão | Reserva |
|---|---|
| **Prazo** | 0 dias — sem margem (prazo fixo 18/08) |
| **Esforço** | 32h adicionais (diferença entre cenário otimista 64h e pessimista 96h) |
| **Custo** | R$ 0 — sem CAPEX/OPEX adicional previsto |

**Observação:** A ausência de reserva de prazo é o principal risco do projeto. A mitigação é aceitar análise de alto nível onde dados profundos não estiverem acessíveis, priorizando entrega dentro do prazo.
