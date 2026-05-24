# Framework de KPIs e Métricas de Desempenho
## PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação
## Grupo Águia Branca

**Versão:** 1.0
**Data:** 2026-05-14
**Responsável:** Marcela Métrica — Especialista em Métricas e Desempenho, VMO Autônomo
**Referências:** `v2/documentacao-base.md` | `v3/requisitos.md` | `v4/cronograma.md` | `v5/plano-riscos.md`

---

## 1. Estrutura do Framework

O framework de métricas do PROJ-2026-004 é organizado em três camadas:

| Camada | Ferramenta | Foco |
|---|---|---|
| **EVM — Earned Value Management** | Valor Planejado, Valor Agregado, Custo Real, CPI, SPI | Controle de prazo e custo em execução |
| **KPIs de Entrega** | Indicadores por módulo e fase | Qualidade, cobertura e velocidade de desenvolvimento |
| **KRs — Key Results** | Resultados-chave do objetivo do projeto | Sucesso do produto entregue (pós go-live) |

---

## 2. EVM — Earned Value Management

### 2.1 Definições

| Sigla | Nome | Definição |
|---|---|---|
| **BAC** | Budget at Completion | Orçamento total aprovado: **R$ 75.000,00** *(sem contingência)* |
| **PV** | Planned Value (Valor Planejado) | Trabalho que deveria estar concluído até a data de referência, em valor |
| **EV** | Earned Value (Valor Agregado) | Trabalho efetivamente concluído até a data de referência, em valor |
| **AC** | Actual Cost (Custo Real) | Custo real incorrido até a data de referência |
| **CPI** | Cost Performance Index | EV / AC — eficiência de custo (>1: abaixo do orçamento; <1: acima) |
| **SPI** | Schedule Performance Index | EV / PV — eficiência de prazo (>1: adiantado; <1: atrasado) |
| **CV** | Cost Variance | EV − AC (positivo: economia; negativo: estouro) |
| **SV** | Schedule Variance | EV − PV (positivo: adiantado; negativo: atrasado) |
| **EAC** | Estimate at Completion | Estimativa revisada de custo total ao final do projeto |
| **ETC** | Estimate to Complete | Custo estimado para concluir o trabalho restante |
| **VAC** | Variance at Completion | BAC − EAC (positivo: economia esperada; negativo: estouro esperado) |

### 2.2 Curva S — Distribuição do Valor Planejado por Fase

> BAC = R$ 75.000,00 | Início: 16/06/2026 | Go-live: 30/11/2026

| Fase | Período | PV da Fase | PV Acumulado | % do BAC Acumulado |
|---|---|---|---|---|
| Planejamento Detalhado | 16/06 – 30/06 | R$ 6.000 | R$ 6.000 | 8% |
| Sprint 1 — M1 + M2 (MVP) | 01/07 – 11/08 | R$ 22.500 | R$ 28.500 | 38% |
| Sprint 2 — M3 + M4 | 13/08 – 12/09 | R$ 15.000 | R$ 43.500 | 58% |
| Sprint 3 — M5 + M6 | 16/09 – 27/10 | R$ 15.000 | R$ 58.500 | 78% |
| Integração + Testes Sistêmicos | 29/10 – 07/11 | R$ 6.000 | R$ 64.500 | 86% |
| UAT | 10/11 – 14/11 | R$ 4.500 | R$ 69.000 | 92% |
| Implantação + Go-live | 17/11 – 28/11 | R$ 6.000 | R$ 75.000 | 100% |

### 2.3 Pontos de Controle EVM

A medição do EVM será feita quinzenalmente, integrada ao relatório de status. Os valores abaixo representam as metas de controle em cada marco:

| Data de Controle | Marco Referência | PV Acumulado | CPI Mínimo Aceitável | SPI Mínimo Aceitável |
|---|---|---|---|---|
| 30/06/2026 | Planejamento concluído | R$ 6.000 | ≥ 0,90 | ≥ 0,90 |
| 11/08/2026 | MVP em homologação | R$ 28.500 | ≥ 0,90 | ≥ 0,85 |
| 12/09/2026 | Sprint 2 concluído | R$ 43.500 | ≥ 0,90 | ≥ 0,85 |
| 27/10/2026 | Sprint 3 concluído | R$ 58.500 | ≥ 0,90 | ≥ 0,85 |
| 07/11/2026 | Liberação para UAT | R$ 64.500 | ≥ 0,90 | ≥ 0,90 |
| 14/11/2026 | UAT aprovado | R$ 69.000 | ≥ 0,90 | ≥ 0,95 |
| 28/11/2026 | Go-live | R$ 75.000 | ≥ 0,90 | ≥ 1,00 |

### 2.4 Thresholds de Alerta EVM

| Indicador | Verde (Normal) | Amarelo (Atenção) | Vermelho (Alerta) | Ação no Vermelho |
|---|---|---|---|---|
| CPI | ≥ 0,95 | 0,85–0,94 | < 0,85 | Reunião de contingência com sponsor; revisão de escopo |
| SPI | ≥ 0,90 | 0,80–0,89 | < 0,80 | Análise de caminho crítico; acionar plano de resposta RSK-04 |
| CV | ≥ 0 | -R$ 5.000 a 0 | < -R$ 5.000 | Acionar reserva de contingência; comunicar sponsor |
| SV | ≥ 0 | -5 a 0 d.u. | < -5 d.u. | Revisar cronograma; avaliar horas extras ou restrição de escopo |

---

## 3. KPIs de Entrega por Fase

### 3.1 Fase de Planejamento (até 30/06/2026)

| KPI | Descrição | Meta | Como Medir |
|---|---|---|---|
| KPI-P01 | Backlog 100% priorizado e estimado | 100% dos 37 RFs com estimativa em story points | Contagem no backlog |
| KPI-P02 | Wireframes aprovados pelo solicitante | ≥ 80% dos wireframes aprovados por Jadson | Ata de validação |
| KPI-P03 | Ambiente de desenvolvimento configurado | CI/CD funcional e ambiente dev disponível | Teste de deploy bem-sucedido |
| KPI-P04 | Arquitetura técnica documentada e aprovada pelo tech lead | 100% dos componentes documentados | Documento de arquitetura |

### 3.2 KPIs de Desenvolvimento por Sprint

| KPI | Descrição | Meta | Como Medir |
|---|---|---|---|
| KPI-D01 | Velocidade de entrega por sprint | ≥ 80% do planejado em story points | Burndown chart por sprint |
| KPI-D02 | Cobertura de testes unitários | ≥ 70% do código coberto por testes | Relatório de cobertura (ferramenta de CI) |
| KPI-D03 | Taxa de defeitos encontrados internamente (antes do UAT) | ≥ 90% dos defeitos encontrados pela equipe (não pelo cliente) | Registro de defeitos |
| KPI-D04 | Taxa de defeitos P1 em produção | 0 defeitos P1 abertos no go-live | Registro de defeitos |
| KPI-D05 | Taxa de defeitos P2 em produção | ≤ 5 defeitos P2 abertos no go-live | Registro de defeitos |
| KPI-D06 | Review de sprint aprovado pelo solicitante | 100% dos reviews de sprint com validação de Jadson | Ata de review assinada |

### 3.3 KPIs de Performance Técnica

| KPI | Descrição | Meta | Como Medir |
|---|---|---|---|
| KPI-T01 | Tempo de resposta sob carga | < 3 segundos para 95% das requisições com 500 usuários simultâneos | Teste de carga (JMeter ou equivalente) |
| KPI-T02 | Disponibilidade pós-go-live | ≥ 99% em horário comercial (07h–20h) | Monitoramento de uptime |
| KPI-T03 | Escalabilidade de usuários | Suportar 10.000 usuários cadastrados sem degradação | Teste de volume |
| KPI-T04 | Segurança — OWASP Top 10 | Zero vulnerabilidades críticas nos testes de segurança | Relatório de teste de segurança |

### 3.4 KPIs de UAT

| KPI | Descrição | Meta | Como Medir |
|---|---|---|---|
| KPI-U01 | Taxa de aprovação do UAT | ≥ 80% dos casos de teste aprovados | Relatório de UAT assinado |
| KPI-U02 | Taxa de aprovação dos casos críticos | 100% dos casos críticos aprovados | Relatório de UAT assinado |
| KPI-U03 | Satisfação do time de inovação no UAT | Nota ≥ 4,0/5,0 na pesquisa de satisfação pós-UAT | Formulário de avaliação |
| KPI-U04 | Prazo de execução do UAT | UAT concluído até 14/11/2026 | Data de conclusão |

---

## 4. KRs — Key Results (Pós-Entrega)

> Os Key Results medem o sucesso do produto entregue e são apurados nos 30 e 90 dias após o go-live.

### OKR do Projeto

**Objetivo:** Substituir a plataforma terceirizada de gestão de ideias de inovação por uma solução proprietária que democratize a participação de todos os colaboradores do Grupo Águia Branca, reduza custos e suporte o Prêmio Inovação 2027.

---

### KR-01 — Entrega dentro do prazo e orçamento

| Campo | Detalhe |
|---|---|
| **Key Result** | Plataforma em produção até 30/11/2026 com custo total ≤ R$ 90.000 |
| **Baseline** | Projeto não iniciado (custo 0; prazo 0%) |
| **Meta** | Go-live até 30/11/2026; custo final ≤ R$ 90.000 |
| **Apuração** | Na data do go-live |
| **Status inicial** | ⚪ A iniciar |

---

### KR-02 — Adoção pelos colaboradores (30 dias pós-go-live)

| Campo | Detalhe |
|---|---|
| **Key Result** | ≥ 50% dos usuários ativos da plataforma anterior acessaram a nova plataforma nos primeiros 30 dias |
| **Baseline** | Taxa de adoção pré-go-live: 0% (nova plataforma) |
| **Meta** | ≥ 50% de taxa de acesso nos primeiros 30 dias; ≥ 30 ideias submetidas no primeiro mês |
| **Apuração** | 30 dias após go-live (até 28/12/2026) |
| **Status inicial** | ⚪ A iniciar |

---

### KR-03 — Eliminação do custo recorrente (90 dias pós-go-live)

| Campo | Detalhe |
|---|---|
| **Key Result** | Contrato com a plataforma terceirizada rescindido, eliminando R$ 80.000–90.000/ano de custo recorrente |
| **Baseline** | Custo anual com plataforma terceirizada: R$ 80.000–90.000 |
| **Meta** | Rescisão formal confirmada por escrito até 28/02/2027 |
| **Apuração** | 90 dias após go-live (até 28/02/2027) |
| **Status inicial** | ⚪ A iniciar |

---

### KR-04 — Satisfação do usuário-chave (Prêmio Inovação 2027)

| Campo | Detalhe |
|---|---|
| **Key Result** | Nota de satisfação ≥ 4,0/5,0 atribuída por Jadson e time de inovação após o Prêmio Inovação de janeiro/2027 |
| **Baseline** | Sem avaliação anterior (nova plataforma) |
| **Meta** | Nota ≥ 4,0/5,0 na pesquisa de satisfação pós-Prêmio |
| **Apuração** | Até 31/01/2027 (após o Prêmio Inovação) |
| **Status inicial** | ⚪ A iniciar |

---

### KR-05 — Cobertura funcional operacional

| Campo | Detalhe |
|---|---|
| **Key Result** | ≥ 95% dos 37 requisitos funcionais operando sem defeitos críticos 30 dias após o go-live |
| **Baseline** | 0% (pré-go-live) |
| **Meta** | ≥ 95% dos RFs operacionais; 0 defeitos P1 abertos após 30 dias |
| **Apuração** | 30 dias após go-live (até 28/12/2026) |
| **Status inicial** | ⚪ A iniciar |

---

## 5. Dashboard de Controle — Resumo dos Indicadores

### 5.1 Painel de Controle de Projeto (em execução)

| Indicador | Frequência | Responsável | Threshold Verde | Threshold Amarelo | Threshold Vermelho |
|---|---|---|---|---|---|
| CPI | Quinzenal | GP | ≥ 0,95 | 0,85–0,94 | < 0,85 |
| SPI | Quinzenal | GP | ≥ 0,90 | 0,80–0,89 | < 0,80 |
| % Backlog concluído | Quinzenal | Tech Lead | ≥ meta do sprint | ±10% da meta | < 70% da meta |
| Cobertura de testes | Semanal | QA | ≥ 70% | 60%–69% | < 60% |
| Defeitos P1 abertos | Semanal | QA | 0 | 1–2 | ≥ 3 |
| Riscos em vermelho | Quinzenal | GP | 0 | 1 | ≥ 2 |
| Satisfação no review de sprint | Por sprint | GP | ≥ 4,0/5,0 | 3,0–3,9 | < 3,0 |

### 5.2 Painel de Resultados (pós-entrega)

| KR | Prazo de Apuração | Meta | Status |
|---|---|---|---|
| KR-01 — Prazo e orçamento | 30/11/2026 | Go-live + custo ≤ R$90K | ⚪ |
| KR-02 — Adoção 30 dias | 28/12/2026 | ≥ 50% acesso + ≥ 30 ideias | ⚪ |
| KR-03 — Rescisão contrato | 28/02/2027 | Confirmação escrita | ⚪ |
| KR-04 — Satisfação Prêmio | 31/01/2027 | ≥ 4,0/5,0 | ⚪ |
| KR-05 — Cobertura funcional | 28/12/2026 | ≥ 95% RFs sem P1 | ⚪ |

---

## 6. Responsabilidades de Medição

| Indicador | Quem Mede | Quem Recebe | Ferramenta |
|---|---|---|---|
| EVM (PV, EV, AC, CPI, SPI) | GP | Sponsor, PMO, Jadson | Planilha de controle do projeto |
| Cobertura de testes | QA + CI/CD pipeline | GP, Tech Lead | Relatório automático de CI |
| Defeitos | QA | GP, Jadson | Ferramenta de issue tracking |
| Velocidade de sprint | Tech Lead | GP | Burndown chart |
| KRs pós-entrega | GP + Jadson | Sponsor, PMO | Pesquisa de satisfação + dados da plataforma |
| Uptime pós-go-live | TI do Grupo | GP, Jadson | Monitoramento de infraestrutura |

---

## 7. Baseline de Métricas de Referência

| Métrica | Valor de Baseline (plataforma atual) | Fonte |
|---|---|---|
| Custo anual da plataforma | R$ 80.000–90.000/ano | Declarado por Jadson |
| Nº de usuários licenciados atuais | Não informado (LACUNA) | Levantamento necessário no kick-off |
| Nº de ideias submetidas por mês (média) | Não informado (LACUNA) | Levantamento necessário no kick-off |
| Tempo médio de aprovação de ideias | Não informado (LACUNA) | Levantamento necessário no kick-off |
| Satisfação dos usuários com a plataforma atual | Não informado (LACUNA) | Pesquisa pré-implantação (opcional) |

> **Nota:** As lacunas de baseline devem ser preenchidas por Jadson no kick-off para que os KRs pós-entrega possam ser calculados com precisão. Sem o baseline, os KR-02 e KR-04 serão avaliados em termos absolutos (não comparativos).

---

*Documento gerado por Marcela Métrica — Especialista em Métricas e Desempenho | VMO Autônomo v1.0 | 2026-05-14*
*PROJ-2026-004 | Versão 1.0 | 2026-05-14*
