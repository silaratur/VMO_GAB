# FRAMEWORK DE KPIs — PROJ-2026-001
Inclusão de Aprovador SAP FI Lançamentos Pré-Editados | Versão: 1.0 | Data: 2026-04-03

---

## Semáforo de Saúde do Projeto

| Dimensão | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|
| **Prazo** | SPI ≥ 0,95 | 0,85 ≤ SPI < 0,95 | SPI < 0,85 |
| **Custo** | CPI ≥ 0,95 | 0,85 ≤ CPI < 0,95 | CPI < 0,85 |
| **Escopo** | 100% dos critérios de aceitação atendidos, zero desvios abertos | 1 desvio aberto ou critério pendente de verificação | 2+ desvios abertos ou critério de aceitação reprovado |
| **Riscos** | Nenhum risco ALTO ativo materializado; todos com plano de resposta documentado | 1 risco ALTO ativo sem plano de resposta concluído ou com gatilho iminente | Risco ALTO materializado (R01, R02 ou R03) impactando prazo ou custo |
| **Satisfação** | Aprovador confirma treinamento e aceita sistema antes do go-live; zero reclamações de bypass | Aprovador confirma treinamento mas levanta ressalvas de usabilidade | Aprovador não confirma treinamento até Du 50 ou rejeita aceite do sistema |

---

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|---|---|---|---|---|---|---|---|
| **CPI** — Cost Performance Index | CPI = EV / AC | 1,00 (Du 0) | CPI ≥ 1,00 ao longo do projeto | 0,85 ≤ CPI < 0,95 | CPI < 0,85 | Semanal (toda 2ª feira) | Marcela Métrica |
| **SPI** — Schedule Performance Index | SPI = EV / PV | 1,00 (Du 0) | SPI ≥ 1,00 ao longo do projeto | 0,85 ≤ SPI < 0,95 | SPI < 0,85 | Semanal (toda 2ª feira) | Marcela Métrica |
| **EV** — Earned Value | Soma dos valores planejados das atividades concluídas (método 0/100 para entregáveis discretos; % concluída para atividades contínuas) | R$ 0,00 (Du 0) | EV = PV em cada ponto de medição | EV < 90% do PV acumulado | EV < 80% do PV acumulado | Semanal (toda 2ª feira) | Marcela Métrica |
| **PV** — Planned Value | Valor orçado do trabalho agendado até a data de medição (curva S baseline) | R$ 0,00 (Du 0) | Seguir baseline aprovado | — | — | Semanal | Marcela Métrica |
| **AC** — Actual Cost | Soma dos custos reais incorridos até a data de medição | R$ 0,00 (Du 0) | AC ≤ EV em cada ponto | AC > EV (CPI < 1) | AC > 115% do EV acumulado | Semanal (toda 2ª feira) | Gerente do Projeto |
| **EAC** — Estimate at Completion | EAC = BAC / CPI | R$ 8.640 (Du 0) | EAC ≤ R$ 8.640 | R$ 8.640 < EAC ≤ R$ 9.500 | EAC > R$ 9.500 | Semanal (toda 2ª feira) | Marcela Métrica |
| **VAC** — Variance at Completion | VAC = BAC − EAC | R$ 0,00 (Du 0) | VAC ≥ R$ 0 (dentro do orçamento) | −R$ 860 ≤ VAC < R$ 0 | VAC < −R$ 860 | Semanal (toda 2ª feira) | Marcela Métrica |
| **CV** — Cost Variance | CV = EV − AC | R$ 0,00 (Du 0) | CV ≥ 0 | −R$ 500 ≤ CV < 0 | CV < −R$ 500 | Semanal (toda 2ª feira) | Marcela Métrica |
| **SV** — Schedule Variance | SV = EV − PV | R$ 0,00 (Du 0) | SV ≥ 0 | −10% do PV acumulado | < −15% do PV acumulado | Semanal (toda 2ª feira) | Marcela Métrica |

---

## KPIs de Resultado do Projeto

(Derivados dos 5 Critérios de Sucesso do TAP)

| KPI | Descrição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|---|---|---|---|---|---|---|---|
| **KR-1 — Taxa de Cobertura de Aprovação Pós Go-Live** | % dos lançamentos pré-editados que passaram pelo fluxo de aprovação do Diretor Financeiro, medido via relatório SBWP na 1ª semana após go-live | 0% (pré-go-live) | 100% na semana 1 pós go-live | 90% ≤ taxa < 100% (investigar lacuna) | < 90% (critério de sucesso não atingido) | Diária na semana pós go-live; semanal após | Consultor SAP FI |
| **KR-2 — Taxa de Bypass Zero (Auditoria 30 dias)** | Número de lançamentos contabilizados sem aprovação do Diretor nos 30 dias pós go-live | 0 bypass (baseline ideal) | 0 bypass nos 30 dias | 1 bypass identificado (ação corretiva imediata) | ≥ 2 bypasses ou 1 bypass não corrigido em 48h | Diária (auditoria automática via SBWP) | Auditor / Gerente do Projeto |
| **KR-3 — Prazo de Entrega em Produção** | Dia útil de go-live efetivo (entrada em produção) em relação ao baseline de Du 60 | Du 60 (baseline) | Go-live até Du 60 | Go-live entre Du 55–60 com risco de atraso identificado | Go-live após Du 60 (critério de sucesso violado) | Acompanhamento semanal; confirmação no marco M6 | Gerente do Projeto |
| **KR-4 — Aderência ao Teto de Custo** | Custo total do projeto (AC final) versus teto aprovado de R$ 8.640 | R$ 0,00 (Du 0) | AC final ≤ R$ 8.640 | R$ 8.000 ≤ AC final ≤ R$ 8.640 (consumo de contingência) | AC final > R$ 8.640 (estourou teto aprovado) | Semanal e ao encerramento | Gerente do Projeto / Financeiro |
| **KR-5 — Confirmação de Treinamento do Aprovador** | Confirmação formal (e-mail ou assinatura de lista de presença) do Diretor Financeiro de que recebeu e concluiu o treinamento antes do go-live | Não realizado (Du 0) | Confirmação obtida até Du 52 (marco M6) | Confirmação obtida entre Du 46–52 com pendência de assinatura | Diretor não confirma treinamento até Du 52 ou recusa participação | Uma vez (marco M5/M6 — Du 46–52) | Gerente do Projeto |

---

## Configuração EVM

### Parâmetros Base

- **BAC (Budget at Completion):** R$ 8.640 (teto aprovado, inclui 20% de contingência)
- **Prazo Baseline:** Du 60 a partir da assinatura do TAP
- **Moeda:** BRL (R$)
- **Unidade de tempo:** Dias úteis (Du)

### Método de Medição de EV por Tipo de Atividade

| Tipo de Atividade | Método EV | Justificativa |
|---|---|---|
| Entregáveis discretos com critério de aceite claro (ex.: TAP assinado, Requisitos aprovados, Plano de riscos entregue, Cronograma baseline, Documentação técnica, Resultados de teste aprovados, Treinamento concluído) | **0/100** — 0% até início, 100% apenas quando entregável aceito formalmente | Elimina subjetividade; EV só é creditado com aceite comprovado |
| Atividades de configuração SAP com etapas intermediárias verificáveis (ex.: configuração QAS, testes integrados) | **Marcos Ponderados (milestones)** — % por etapa concluída e verificada (ex.: 30% config iniciada, 70% config validada QAS, 100% aprovada para transporte) | Permite medição objetiva de progresso sem "síndrome dos 90%" |
| Atividades de gestão contínua (reuniões de status, monitoramento, comunicação) | **% Duração Decorrida** — proporcional ao tempo transcorrido dentro do período planejado | Adequado para esforço distribuído sem entregável pontual |
| Treinamento do Diretor Financeiro | **0/100** — 0% até realização, 100% após confirmação formal (lista de presença / e-mail) | Critério de sucesso binário; não admite parcial |
| Validação e auditoria pós go-live | **Marcos Ponderados** — 50% após relatório SBWP gerado na semana 1; 100% após auditoria de 30 dias sem bypass | Reflete as duas etapas de verificação do TAP |

### Marcos EVM e PV Planejado

| Marco | Du | Entregável Principal | % BAC Planejado (PV Acumulado) |
|---|---|---|---|
| M0 — TAP Assinado | Du 2 | TAP aprovado e assinado | 5% — R$ 432 |
| M1 — Requisitos Aprovados | Du 5 | Documento de requisitos aceito | 12% — R$ 1.037 |
| M2 — Baseline Estabelecido | Du 10 | Cronograma, riscos e KPIs aprovados | 20% — R$ 1.728 |
| M3 — Config. QAS Aprovada | Du 28 | Configuração SAP FI em QAS validada | 55% — R$ 4.752 |
| M4 — Testes Integrados OK | Du 40 | Resultados de testes aprovados | 75% — R$ 6.480 |
| M5 — Treinamento Concluído | Du 46 | Confirmação formal do Diretor | 88% — R$ 7.603 |
| M6 — Go-Live / Produção | Du 52 | Sistema em produção + aceite | 96% — R$ 8.294 |
| M7 — Encerramento | Du 60 | Auditoria 30 dias + lições aprendidas | 100% — R$ 8.640 |

### Regras de Controle de Contingência

- Reserva de contingência: R$ 1.440 (20% do orçamento base R$ 7.200)
- Uso da contingência requer aprovação do Patrocinador
- Se EAC ultrapassar R$ 8.640, acionar análise de impacto de R01 (risco ZFI0057)
- Qualquer liberação de reserva deve ser registrada como mudança de baseline de custo

---

## Frequência de Reporting

| Relatório | Conteúdo | Frequência | Audiência |
|---|---|---|---|
| Dashboard Semanal de KPIs | Semáforo de saúde + CPI + SPI + EV/PV/AC + VAC | Toda segunda-feira | Gerente do Projeto + Patrocinador |
| Relatório de Marco | Status completo EVM + KRs + riscos ativos + próximos passos | A cada marco (M0–M7) | Patrocinador + Comitê |
| Alerta de Threshold | Notificação imediata quando qualquer KPI entra em zona 🔴 | Ad hoc (imediato) | Gerente do Projeto + Patrocinador |
| Relatório de Encerramento | EAC final + VAC final + todos os KRs verificados + lições aprendidas | Du 60 (encerramento) | Todos os stakeholders |

---

*Documento gerado por Marcela Métrica — Monitora de Performance | PROJ-2026-001 | v1.0 | 2026-04-03*
