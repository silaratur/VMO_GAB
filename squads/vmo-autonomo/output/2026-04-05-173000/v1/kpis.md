# Framework de KPIs — Caminhos Estratégicos do ERP GAB

**ID Projeto:** PROJ-2026-003
**Versão:** 1.0
**Data:** 05/04/2026
**Elaborado por:** Marcela Métrica — Monitora de Performance (VMO Autônomo)
**Run ID:** 2026-04-05-173000

---

> **Nota de Autoria:** Este framework foi elaborado pela Marcela Métrica, Monitora de Performance do VMO Autônomo, com base na análise completa dos documentos de iniciação do projeto (TAP, Cronograma e Plano de Riscos). Todos os índices EVM são calculados com base em entregáveis formalmente aceitos — percentuais subjetivos de conclusão não são aceitos como medida de progresso neste framework.

---

## 1. Configuração EVM — Earned Value Management

### 1.1 Parâmetros Fundamentais

| Parâmetro | Valor | Observação |
|---|---|---|
| **BAC — Budget at Completion (Fase 1)** | R$ 930.000,00 | Contrato KPMG — valor fechado, sem cláusula de aditivo |
| **BAC — Budget at Completion (Fase 2)** | R$ 170.000,00 | RFP — valor contratado, execução a partir de ~05/05/2026 |
| **BAC Total do Contrato** | R$ 1.100.000,00 | Aprovado via DocuSign em 13–17/03/2026 |
| **Data de Início (Fase 1)** | 02/04/2026 | Kick Off Operacional |
| **Data de Início EVM** | 06/04/2026 | Início dos entregáveis mensuráveis (Semana 1) |
| **Data de Fim (Fase 1)** | 08/05/2026 | Entrega final do relatório de recomendação |
| **Duração (Fase 1)** | 25 dias úteis | 5 semanas de 5 dias (Semana 4 tem 4 dias úteis — feriado 01/05) |
| **Data de Referência (hoje)** | 05/04/2026 | Semana 0 — documentação de iniciação VMO |

### 1.2 Regra de Medição de Valor Agregado (EV)

**Regra principal: 0/100 por entregável contratual**

O contrato KPMG remunera por marcos de entregável, não por hora trabalhada. Portanto:

- Um entregável vale **0%** até ser formalmente aceito pelo GP Interno (Marcelo Silveira)
- Um entregável vale **100%** a partir do momento em que o GP emite aceite formal (e-mail ou assinatura de ata)
- Aceite parcial NÃO é reconhecido — o entregável só entra no cálculo do EV quando 100% aprovado
- Em caso de disputa sobre o aceite, prevalece o critério do GP Interno com respaldo dos Sponsors

**Regra complementar: 50/50 para deliverables em andamento**

Para entregáveis que abrangem múltiplas semanas (ex.: consolidação de matrizes de aderência nas Semanas 3 e 4), aplica-se a regra 50/50:
- 50% do valor reconhecido quando o entregável é iniciado e a 1ª metade entregue para revisão
- 50% restante reconhecido com o aceite formal do produto completo

**Para atividades VMO (não faturadas):** Uso de **SPI somente** — EV medido por documentos VMO concluídos vs. planejados. Sem controle de custo (AC) para atividades internas.

### 1.3 Baseline de Valor Planejado (PV) — Curva S por Semana

Distribuição linear do BAC da Fase 1 (R$ 930.000) pelas 5 semanas de execução:

| Semana | Período | Dias Úteis | PV Semanal | PV Acumulado | % PV |
|---|---|---|---|---|---|
| **Semana 0** | 02–05/04/2026 | 3 dias (iniciação) | R$ 0,00 | R$ 0,00 | 0% |
| **Semana 1** | 06–10/04/2026 | 5 dias | R$ 186.000,00 | R$ 186.000,00 | 20% |
| **Semana 2** | 13–17/04/2026 | 5 dias | R$ 186.000,00 | R$ 372.000,00 | 40% |
| **Semana 3** | 20–24/04/2026 | 5 dias | R$ 186.000,00 | R$ 558.000,00 | 60% |
| **Semana 4** | 27–30/04/2026 | 4 dias* | R$ 186.000,00 | R$ 744.000,00 | 80% |
| **Semana 5** | 04–08/05/2026 | 5 dias | R$ 186.000,00 | R$ 930.000,00 | 100% |

*01/05/2026 é feriado nacional — Semana 4 tem 4 dias úteis efetivos.

**Nota sobre a distribuição:** A distribuição linear (R$ 186.000/semana) é o baseline de referência. Caso a KPMG apresente um cronograma de faturamento com marcos contratuais específicos por semana, a curva S deverá ser atualizada para refletir os marcos reais. Esta atualização requer aprovação formal como mudança de baseline.

### 1.4 Estrutura de Entregáveis KPMG e Seus Valores EV

| ID | Entregável | Semana | Regra EV | Valor EV (R$) | % do BAC |
|---|---|---|---|---|---|
| D01 | Documentação AS-IS — Manutenção/Frotas (VixPar) | S1 | 0/100 | R$ 66.000 | 7,1% |
| D02 | Documentação AS-IS — Suprimentos (VixPar + Holding) | S1 | 0/100 | R$ 66.000 | 7,1% |
| D03 | Documentação AS-IS — Finanças Parte 1 (3 entidades) | S1 | 0/100 | R$ 66.000 | 7,1% |
| D04 | Documentação AS-IS — Fiscal Parte 1 (3 entidades) | S1 | 0/100 | R$ 66.000 | 7,1% |
| D05 | Documentação AS-IS — RH/DP/SESMT (VAB + VixPar) | S2 | 0/100 | R$ 66.000 | 7,1% |
| D06 | Complemento AS-IS — Finanças (continuação) | S2 | 0/100 | R$ 66.000 | 7,1% |
| D07 | Documentação AS-IS — Tecnologia (todas entidades) | S2 | 0/100 | R$ 66.000 | 7,1% |
| D08 | AS-IS consolidados (todas as 7 áreas) | S3 | 50/50 | R$ 60.000 | 6,5% |
| D09 | Requisitos de aderência por plataforma | S3 | 0/100 | R$ 60.000 | 6,5% |
| D10 | Score Model — Pilares 1 e 2 (Estratégico + Produto) | S3 | 50/50 | R$ 66.000 | 7,1% |
| D11 | Score Model — Pilares 3 a 6 (Tecnologia+Cliente+Fin+Op) | S4 | 50/50 | R$ 66.000 | 7,1% |
| D12 | Matrizes de aderência consolidadas (3 × 7) | S4 | 0/100 | R$ 60.000 | 6,5% |
| D13 | Ranking preliminar das plataformas | S4 | 0/100 | R$ 60.000 | 6,5% |
| D14 | Relatório Final de Recomendação (revisado) | S5 | 0/100 | R$ 60.000 | 6,5% |
| D15 | Apresentação Executiva Final + Aprovação do Comitê | S5 | 0/100 | R$ 120.000 | 12,9% |
| | **TOTAL** | | | **R$ 930.000** | **100%** |

---

## 2. KPIs de Performance do Projeto (EVM)

### 2.1 Índices EVM — Definições e Fórmulas

| KPI | Código | Fórmula | O que mede |
|---|---|---|---|
| Valor Planejado | PV | BAC × % planejado no período | Quanto deveria ter sido realizado até hoje |
| Valor Agregado | EV | Σ (valor de entregáveis aceitos) | Quanto foi efetivamente realizado e aceito |
| Custo Real | AC | Σ faturas KPMG aprovadas pela finanças GAB | Quanto foi efetivamente pago/comprometido |
| Variação de Prazo | SV | EV − PV | Positivo = adiantado; negativo = atrasado |
| Variação de Custo | CV | EV − AC | Positivo = abaixo do orçamento; negativo = acima |
| Índice de Performance de Prazo | SPI | EV ÷ PV | < 1,0 = atrasado; > 1,0 = adiantado |
| Índice de Performance de Custo | CPI | EV ÷ AC | < 1,0 = acima do custo; > 1,0 = abaixo do custo |
| Estimativa para Conclusão | ETC | (BAC − EV) ÷ CPI | Custo estimado para concluir o restante |
| Estimativa ao Fim | EAC | AC + ETC | Custo total estimado ao fim do projeto |
| Variação ao Fim | VAC | BAC − EAC | Positivo = projeto ficará abaixo do orçamento |
| Índice de Performance para Completar | TCPI | (BAC − EV) ÷ (BAC − AC) | CPI que precisa ser mantido para terminar no orçamento |

### 2.2 Tabela de KPIs EVM — Thresholds e Responsabilidades

| KPI | Baseline | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho | Frequência | Responsável |
|---|---|---|---|---|---|---|---|
| **CPI** | 1,00 | ≥ 1,00 | ≥ 0,95 | 0,85–0,94 | < 0,85 | Semanal | Marcela Métrica / GP |
| **SPI** | 1,00 | ≥ 1,00 | ≥ 0,95 | 0,85–0,94 | < 0,85 | Semanal | Marcela Métrica / GP |
| **CV (R$)** | R$ 0 | ≥ R$ 0 | ≥ −R$ 46.500 (−5%) | −R$ 46.500 a −R$ 139.500 | < −R$ 139.500 (−15%) | Semanal | GP Interno |
| **SV (R$)** | R$ 0 | ≥ R$ 0 | ≥ −R$ 9.300 (−5% PV) | −R$ 9.300 a −R$ 27.900 | < −R$ 27.900 (−15% PV) | Semanal | GP Interno |
| **EAC** | R$ 930.000 | = R$ 930.000 | ≤ R$ 976.500 | R$ 976.501–R$ 1.069.500 | > R$ 1.069.500 | Semanal | GP Interno + Sponsors |
| **VAC** | R$ 0 | ≥ R$ 0 | ≥ −R$ 46.500 | −R$ 46.500 a −R$ 139.500 | < −R$ 139.500 | Semanal | GP Interno + Sponsors |
| **TCPI** | 1,00 | ≤ 1,05 | ≤ 1,05 | 1,06–1,18 | > 1,18 | Semanal | Marcela Métrica |

### 2.3 Regras de Cálculo do EAC

Para este projeto (contrato de valor fechado com KPMG), o EAC deve ser calculado usando **dois métodos em paralelo**, tomando o mais conservador:

**Método 1 — Baseado no CPI atual:**
> EAC = BAC ÷ CPI

**Método 2 — Estimativa bottom-up:**
> EAC = AC + ETC (onde ETC é a estimativa revisada das atividades restantes)

**Nota crítica:** Como o contrato KPMG é de valor fechado (R$ 930.000), o AC não deve exceder o BAC salvo em caso de aditivo contratual formalmente aprovado. O CPI < 1,0 neste contexto indica risco de necessidade de aditivo ou de entregáveis não aceitos que precisem ser refeitos com custo adicional.

---

## 3. KPIs de Entregáveis e Milestones

### 3.1 Taxa de Entregáveis no Prazo

| KPI | Definição | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho | Frequência |
|---|---|---|---|---|---|---|
| **Taxa de Entregáveis no Prazo** | Nº de entregáveis aceitos na semana prevista ÷ Nº de entregáveis previstos na semana | 100% | ≥ 95% | 85–94% | < 85% | Semanal |
| **Entregáveis Aceitos Acumulados** | Total de entregáveis com aceite formal do GP ÷ Total esperado até a data | 100% | ≥ 95% | 85–94% | < 85% | Semanal |
| **Entregáveis em Revisão (backlog)** | Nº de entregáveis enviados pela KPMG aguardando aceite do GP | 0 | ≤ 1 | 2–3 | ≥ 4 | Semanal |
| **Tempo Médio de Aceite** | Média de dias entre submissão pela KPMG e aceite formal pelo GP | 2 dias | ≤ 2 dias úteis | 3–4 dias úteis | > 4 dias úteis | Semanal |

### 3.2 Tracker de Milestones — Fase 1

| ID | Marco | Data Planejada | Status Inicial | Critério de Conclusão |
|---|---|---|---|---|
| **M01** | Kick Off Operacional KPMG | 02/04/2026 | ✅ REALIZADO | Ata de Kick Off assinada |
| **M02** | Documentação VMO de Iniciação concluída | 05/04/2026 | 🔄 EM ANDAMENTO | Todos os 8 artefatos VMO aprovados por Vera Veredito |
| **M03** | Kick Off Executivo | Abril/2026 (TBD) | ⏳ PENDENTE | Apresentação executiva realizada; Sponsors presentes |
| **M04** | Conclusão dos Workshops — Semana 1 | 10/04/2026 | ⏳ PREVISTO | 4 documentações AS-IS aceitas pelo GP (D01–D04) |
| **M05** | Conclusão dos Workshops — Semana 2 | 17/04/2026 | ⏳ PREVISTO | 3 documentações AS-IS aceitas pelo GP (D05–D07) |
| **M06** | Mid-Point Review com Sponsors | 24/04/2026 | ⏳ PREVISTO | Ata de validação assinada pelos Sponsors |
| **M07** | Consolidação das Matrizes de Aderência | 30/04/2026 | ⏳ PREVISTO | Matrizes 3×7 aceitas + ranking preliminar emitido (D08–D13) |
| **M08** | **Entrega Final — Relatório Software Selection** | **08/05/2026** | ⏳ PREVISTO | Relatório entregue + aprovado pelo Comitê Executivo |
| **M09** | Aprovação formal da recomendação | 08–15/05/2026 | ⏳ PREVISTO | Ata de aprovação assinada pelos 3 Sponsors |
| **M10** | Início da Fase 2 (RFP) | ~05/05/2026 | ⏳ PREVISTO | Documento RFP draft iniciado |
| **M11** | Entrega Final — RFP | ~06/06/2026 | ⏳ PREVISTO | Relatório RFP entregue + decisão formal de fornecedor |

### 3.3 KPI de Cobertura dos Workshops

| KPI | Meta | Critério de Medição | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|---|---|
| **Áreas cobertas por workshops** (ao fim S2) | 7/7 áreas | Nº de áreas com sessão realizada e documentada | 7/7 (100%) | 6/7 (86%) | ≤ 5/7 (< 72%) |
| **Entidades representadas por área** | 3/3 entidades | Nº médio de entidades com representante presente por workshop | 3/3 (100%) | 2/3 (67%) | 1/3 ou nenhuma |
| **Workshops realizados conforme agenda** | 100% | Nº de workshops na data prevista ÷ Nº planejado | 100% | 85–99% | < 85% |
| **Workshops com representante de autoridade** | 100% | Nº de workshops com participante que tem autoridade decisória ÷ total | 100% | 80–99% | < 80% |

---

## 4. KPIs de Resultado (vinculados aos Critérios de Sucesso do TAP)

Cada critério de sucesso formal do TAP se traduz em um KPI mensurável com método de verificação objetivo:

| CS | Critério de Sucesso (TAP) | KPI Derivado | Meta | Método de Verificação | Prazo |
|---|---|---|---|---|---|
| **CS-01** | Entrega do relatório de recomendação com scores comparativos | Relatório entregue E aceito pelo Comitê Executivo | 1 relatório com aceite formal | Ata de aprovação assinada pelos Sponsors | 08/05/2026 |
| **CS-02** | Cobertura completa das 7 áreas nas 3 entidades | % de áreas cobertas com pelo menos 1 workshop realizado | 100% (7/7 áreas) | Lista de presença de cada workshop + aceite do AS-IS pelo GP | 17/04/2026 |
| **CS-03** | Scoring completo das 3 plataformas nos 6 pilares | Células preenchidas na matriz de score (3×6 = 18 células) | 18/18 células (100%) | Revisão da matriz final pelo GP antes da apresentação | 01/05/2026 |
| **CS-04** | Participação dos Sponsors no Comitê Executivo | % de quórum (≥ 2 de 3 Sponsors) nas reuniões semanais | 100% das reuniões com quórum | Lista de presença das atas do Comitê Executivo | Toda quinta-feira |
| **CS-05** | Aderência ao orçamento contratado (CPI ≥ 1,0) | CPI final ao encerramento da Fase 1 | CPI = 1,00 (sem aditivos) | Confronto de faturas KPMG aprovadas vs. BAC | 08/05/2026 |
| **CS-06** | Aprovação formal da recomendação com ata assinada | Ata de aprovação com as 3 assinaturas dos Sponsors | Ata assinada pelos 3 Sponsors | Documento físico ou eletrônico com assinaturas | 15/05/2026 |
| **CS-07** | Início da Fase 2 conforme cronograma | Data real de início da Fase 2 vs. data planejada (~05/05) | Desvio ≤ 3 dias úteis | Verificação da emissão do documento RFP draft | 05/05/2026 |

---

## 5. KPIs de Governança e Processo

### 5.1 Cadência de Relatórios VMO

| KPI | Definição | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho | Frequência |
|---|---|---|---|---|---|---|
| **Taxa de Flash Reports entregues** | Flash Reports emitidos no prazo (até 17h do dia) ÷ Flash Reports devidos | 100% | 100% | 90–99% | < 90% | Diário |
| **Taxa de Status Reports entregues** | Status Reports emitidos na quarta-feira prevista ÷ Status Reports devidos | 100% | 100% | 80–99% | < 80% | Semanal |
| **Pontualidade do Status Report** | Status Report entregue até 18h da quarta-feira | 100% | Entregue até 18h | Entregue com atraso de 1 dia | Entregue com ≥ 2 dias de atraso | Semanal |
| **Tempo de Resolução de Issues** | Média de dias entre abertura e fechamento de um issue | ≤ 5 dias úteis | ≤ 3 dias | 4–7 dias | > 7 dias | Semanal |
| **Issues em aberto > 5 dias úteis** | Nº de issues sem resolução há mais de 5 dias úteis | 0 | 0 | 1 | ≥ 2 | Semanal |

### 5.2 Participação no Comitê Executivo

| KPI | Definição | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|---|---|
| **Quórum do Comitê Executivo** | Nº de Sponsors presentes ÷ 3 (total de Sponsors) | ≥ 2/3 | 3/3 Sponsors | 2/3 Sponsors | 1/3 ou 0/3 Sponsors |
| **Pontualidade do Comitê** | Reunião inicia até 10 min após horário marcado | 100% | 100% | 80–99% | < 80% |
| **Acumulado de Comitês realizados** | Comitês realizados ÷ Comitês planejados (1/semana) | 5/5 ao fim da Fase 1 | 100% | 80–99% | < 80% |
| **Decisões pendentes no Comitê** | Nº de pontos de pauta sem decisão registrada na ata | 0 | 0 | 1–2 | ≥ 3 |

### 5.3 Controle de Mudanças de Escopo

| KPI | Definição | Meta | Threshold de Alerta |
|---|---|---|---|
| **Solicitações de Mudança recebidas** | Total de SCMs formalizadas no período | 0 (contrato fechado) | ≥ 1 SCM exige análise de impacto imediata |
| **SCMs aprovadas pelos Sponsors** | SCMs aprovadas ÷ SCMs recebidas | 100% das que impactam escopo/prazo/custo | Qualquer SCM aprovada sem análise de CPI/SPI é anomalia |
| **SCMs incorporadas ao baseline** | SCMs aprovadas e refletidas no baseline atualizado | 100% dentro de 3 dias da aprovação | SCM aprovada sem atualização de baseline > 3 dias = 🔴 RED |

---

## 6. KPIs de Qualidade das Entregas KPMG

### 6.1 Qualidade dos Workshops

| KPI | Definição | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|---|---|
| **Completude da documentação AS-IS** | Nº de seções preenchidas ÷ Nº de seções obrigatórias do template por workshop | 100% | ≥ 95% | 80–94% | < 80% |
| **Workshops com documentação entregue na semana seguinte** | Nº de workshops com AS-IS entregue até a sexta da semana seguinte ÷ total | 100% | 100% | 80–99% | < 80% |
| **Áreas de processo cobertas** | Nº de áreas com mapeamento de processo atual (AS-IS) documentado | 7/7 | 7/7 | 6/7 | ≤ 5/7 |
| **Nível de detalhe das sessões (avaliação GP)** | GP avalia cada AS-IS em escala 1–5: ≥ 4 = aprovado | ≥ 4/5 | ≥ 4 | 3 | ≤ 2 |

### 6.2 Qualidade do Score Model

| KPI | Definição | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|---|---|
| **Critérios do Score Model validados pelos Sponsors** | Nº de critérios/pilares formalmente aprovados pelos Sponsors ÷ total de critérios | 100% | 100% | 85–99% | < 85% |
| **Scores baseados em evidência documentada** | Nº de critérios com evidência (demo, benchmark, documento) ÷ total de critérios avaliados | ≥ 80% | ≥ 80% | 60–79% | < 60% |
| **Divergência de score entre avaliadores** | Nº de critérios com divergência > 2 pontos entre avaliadores distintos (sem justificativa) | 0 | 0 | 1–2 | ≥ 3 |
| **Células da matriz sem pontuação** | Nº de células em branco na matriz 3×6 (ou 3×7) | 0 | 0 | 1–2 | ≥ 3 |
| **Pilares do Score Model confirmados** | Resolução da inconsistência 5 vs. 6 pilares (LAC-007) | Confirmado antes da Semana 3 | Confirmado na Semana 1 | Confirmado na Semana 2 | Não confirmado até início da Semana 3 |

### 6.3 Aprovação dos Entregáveis KPMG pelo GP

| KPI | Definição | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|---|---|
| **Taxa de aceite de primeira revisão** | Nº de entregáveis aceitos na 1ª submissão ÷ total de entregáveis | ≥ 80% | ≥ 80% | 60–79% | < 60% |
| **Nº de ciclos de revisão por entregável** | Média de idas e vindas entre KPMG e GP para aceite | ≤ 2 ciclos | ≤ 2 | 3 | ≥ 4 |
| **Entregável rejeitado sem plano de correção** | Nº de entregas recusadas sem prazo de reentrega definido | 0 | 0 | 1 | ≥ 2 |

---

## 7. KPIs de Gestão de Riscos

### 7.1 Indicadores do Registro de Riscos

| KPI | Definição | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho | Frequência |
|---|---|---|---|---|---|---|
| **Riscos CRÍTICOS ativos** | Nº de riscos com score ≥ 15 no registro de riscos vigente | 0 | 0 | 1 (com plano de mitigação ativo) | ≥ 2 OU qualquer risco crítico sem plano | Semanal |
| **Riscos ALTOS ativos** | Nº de riscos com score 10–14 ativos | ≤ 2 | ≤ 2 | 3–4 | ≥ 5 | Semanal |
| **Riscos sem plano de resposta** | Nº de riscos sem ação de mitigação ou contingência definida | 0 | 0 | 1 | ≥ 2 | Semanal |
| **Ações de mitigação executadas no prazo** | Nº de ações de mitigação realizadas na data prevista ÷ total de ações devidas | 100% | ≥ 95% | 80–94% | < 80% | Semanal |
| **Novos riscos identificados por semana** | Nº de novos riscos adicionados ao registro por semana | Monitorar | 0–2 novos | 3–4 novos | ≥ 5 novos (surto de riscos) | Semanal |
| **Issues abertos (riscos materializados)** | Nº de issues ativos no registro de issues | ≤ 1 | 0–1 | 2–3 | ≥ 4 | Diário |
| **Valor Esperado de Riscos Ativos (EMV)** | Σ (probabilidade × impacto financeiro) dos riscos ativos | < R$ 200.000 | < R$ 200.000 | R$ 200–350.000 | > R$ 350.000 | Quinzenal |

### 7.2 Status Inicial dos Riscos (05/04/2026)

| Nível | Riscos | IDs | Situação |
|---|---|---|---|
| 🔴 CRÍTICO | 3 riscos | R-001, R-002, R-003 | R-001 e R-002 JÁ MATERIALIZADOS (I-001 e I-002) |
| 🟠 ALTO | 4 riscos | R-004, R-005, R-007, R-010 | R-004 parcialmente materializado (I-003) |
| 🟡 MÉDIO | 8 riscos | R-006, R-008, R-009, R-011, R-012, R-013, R-014, R-015 | Em monitoramento |
| **EMV Total** | | | **R$ 388.000** — acima do limite amarelo |

> **Alerta:** O projeto inicia com EMV de R$ 388.000 e 2 riscos críticos já materializados como issues. O indicador de Riscos CRÍTICOS está em 🔴 VERMELHO no Dia 3 do projeto.

---

## 8. KPIs de Satisfação de Stakeholders

### 8.1 Pesquisa de Satisfação — Cadência e Método

A satisfação dos stakeholders é avaliada em **três momentos formais** da Fase 1:
- **Semana 2 (17/04):** Pesquisa rápida pós-workshops (Semanas 1 e 2) — formulário digital, 5 perguntas
- **Semana 3 (24/04 — mid-point review):** Avaliação de satisfação com o andamento pelo Comitê Executivo
- **Semana 5 (08/05):** Pesquisa de encerramento da Fase 1 — avaliação completa

### 8.2 Indicadores de Satisfação

| KPI | Público | Meta | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho | Momento |
|---|---|---|---|---|---|---|
| **NPS dos Sponsors com o projeto** | Décio, Paula, Patrícia | NPS ≥ 50 | NPS ≥ 50 | NPS 0–49 | NPS < 0 (detratores) | S2, S3, S5 |
| **Satisfação do GP com entregas KPMG** | Marcelo Silveira | ≥ 4/5 | ≥ 4/5 | 3/5 | ≤ 2/5 | S2, S3, S5 |
| **Satisfação das áreas com os workshops** | Gestores de área GAB | ≥ 4/5 | ≥ 4/5 | 3/5 | ≤ 2/5 | Após cada workshop |
| **Satisfação dos Sponsors com a metodologia** | Décio, Paula, Patrícia | ≥ 4/5 | ≥ 4/5 | 3/5 | ≤ 2/5 | S3 (mid-point) |
| **Confiança na recomendação final** | Comitê Executivo | ≥ 4/5 | ≥ 4/5 | 3/5 | ≤ 2/5 | S5 (apresentação final) |
| **Avaliação da governança VMO** | GP Interno | ≥ 4/5 | ≥ 4/5 | 3/5 | ≤ 2/5 | S5 (encerramento Fase 1) |

### 8.3 Escala de Avaliação de Satisfação

- **5 — Excelente:** Supera expectativas
- **4 — Bom:** Atende expectativas plenamente
- **3 — Regular:** Atende parcialmente; há pontos de melhoria
- **2 — Insatisfatório:** Abaixo das expectativas; requer ação imediata
- **1 — Crítico:** Não atende expectativas; escalada imediata necessária

---

## 9. Semáforo de Saúde do Projeto

### 9.1 Tabela-Resumo do Semáforo

| Dimensão | Indicador-Síntese | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|---|
| ⏱️ **Prazo (SPI)** | SPI acumulado | SPI ≥ 0,95 | SPI 0,85–0,94 | SPI < 0,85 |
| 💰 **Custo (CPI)** | CPI acumulado | CPI ≥ 0,95 | CPI 0,85–0,94 | CPI < 0,85 |
| 📋 **Escopo** | % entregáveis aceitos vs. planejados | ≥ 95% no prazo | 85–94% | < 85% |
| ⚠️ **Riscos** | Nº de riscos CRÍTICOS ativos | 0 críticos | 1 crítico (com plano) | ≥ 2 críticos OU sem plano |
| 📦 **Entregáveis** | Taxa de aceite acumulada | ≥ 95% | 85–94% | < 85% |
| 👥 **Stakeholders** | Quórum Comitê Executivo + satisfação | 3/3 sponsors + NPS ≥ 50 | 2/3 sponsors OU NPS 0–49 | 1/3 sponsors OU NPS < 0 |
| 📊 **Governança** | Flash + Status Reports no prazo | 100% | 90–99% | < 90% |
| 🔍 **Qualidade** | Score Model baseado em evidência | ≥ 80% evidenciado | 60–79% evidenciado | < 60% evidenciado |

### 9.2 Regra de Consolidação do Semáforo Geral

| Situação | Cor Geral | Ação Requerida |
|---|---|---|
| Todos os indicadores VERDE | 🟢 VERDE | Manter o ritmo; reportar normalidade |
| 1 ou 2 indicadores AMARELO (sem VERMELHO) | 🟡 AMARELO | GP aciona plano de recuperação; informar Sponsors no Status Report |
| Qualquer indicador VERMELHO | 🔴 VERMELHO | Escalada imediata ao Comitê Executivo; reunião de emergência em até 24h |
| Desvio > 25% em qualquer indicador EVM | 🔴 VERMELHO | Escalada automática — ver Seção 11 (Protocolo de Escalada) |

### 9.3 Semáforo de Abertura — Situação em 05/04/2026

| Dimensão | Status Atual | Cor | Observação |
|---|---|---|---|
| ⏱️ Prazo | SPI = 1,00 (baseline) | 🟢 | Projeto sem desvio de prazo na data de abertura |
| 💰 Custo | CPI indisponível (Semana 0 — sem faturas) | ⚪ | Aguardando 1ª fatura KPMG |
| 📋 Escopo | Documentação VMO em andamento | 🟡 | LAC-005 e LAC-006 em aberto (workshops sem agenda/participantes) |
| ⚠️ Riscos | 2 riscos CRÍTICOS materializados (I-001, I-002) | 🔴 | Issues ativos exigem ação imediata em 05/04/2026 |
| 📦 Entregáveis | 0/15 entregáveis KPMG aceitos (Semana 0) | ⚪ | Nenhum entregável KPMG venceu ainda |
| 👥 Stakeholders | Quórum S0 não mensurado ainda | ⚪ | Primeiro Comitê na Semana 1 (10/04) |
| 📊 Governança | Flash Reports S0 iniciando | 🟡 | Status Report Inicial previsto para hoje (S0) |
| 🔍 Qualidade | Score Model — inconsistência LAC-007 em aberto | 🟡 | Confirmar 5 vs. 6 pilares até Semana 1 |

> **Cor Geral de Abertura: 🔴 VERMELHO** — Pelo menos 1 indicador em VERMELHO (Riscos). Issues I-001 e I-002 exigem ação imediata nesta data.

---

## 10. Dashboard de Acompanhamento Semanal

### Template de Preenchimento — Preencher toda Segunda-feira

---

```
╔══════════════════════════════════════════════════════════════════════╗
║  DASHBOARD SEMANAL — CAMINHOS ESTRATÉGICOS DO ERP GAB               ║
║  PROJ-2026-003 | Semana: ____ | Período: ___/___/2026 a ___/___/2026 ║
║  Preenchido por: Marcela Métrica — VMO Autônomo                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

### 10.1 Dados EVM da Semana

| Indicador | Valor Acumulado | Status |
|---|---|---|
| **PV (Valor Planejado)** | R$ ___________ | — |
| **EV (Valor Agregado)** | R$ ___________ | — |
| **AC (Custo Real)** | R$ ___________ | — |
| **SV (Variação de Prazo)** | R$ ___________ (EV−PV) | 🟢/🟡/🔴 |
| **CV (Variação de Custo)** | R$ ___________ (EV−AC) | 🟢/🟡/🔴 |
| **SPI** | ___________ (EV÷PV) | 🟢/🟡/🔴 |
| **CPI** | ___________ (EV÷AC) | 🟢/🟡/🔴 |
| **EAC (Estimativa ao Fim)** | R$ ___________ | 🟢/🟡/🔴 |
| **VAC (Variação ao Fim)** | R$ ___________ | 🟢/🟡/🔴 |
| **TCPI** | ___________ | 🟢/🟡/🔴 |

### 10.2 Entregáveis da Semana

| Entregável | Previsto para esta semana | Aceite? | Data do Aceite | Observação |
|---|---|---|---|---|
| ___________ | Sim / Não | Sim / Não / Pendente | ___/___/2026 | ___________ |
| ___________ | Sim / Não | Sim / Não / Pendente | ___/___/2026 | ___________ |
| ___________ | Sim / Não | Sim / Não / Pendente | ___/___/2026 | ___________ |

**Total de entregáveis aceitos (acumulado):** _____ / 15
**Taxa de entregáveis no prazo:** _____%

### 10.3 Milestones

| Marco | Planejado | Real | Desvio (dias) | Status |
|---|---|---|---|---|
| ___________ | ___/___/2026 | ___/___/2026 | ___ dias | 🟢/🟡/🔴 |

### 10.4 Workshops da Semana

| Workshop | Área | Entidades | Realizado? | Participação (1–5) | Obs. |
|---|---|---|---|---|---|
| ___________ | ___________ | ___________ | Sim/Não | ____ | ___________ |
| ___________ | ___________ | ___________ | Sim/Não | ____ | ___________ |

**Cobertura acumulada de áreas:** _____ / 7

### 10.5 Semáforo da Semana

| Dimensão | Cor | Tendência | Comentário |
|---|---|---|---|
| ⏱️ Prazo (SPI) | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| 💰 Custo (CPI) | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| 📋 Escopo | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| ⚠️ Riscos | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| 📦 Entregáveis | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| 👥 Stakeholders | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| 📊 Governança | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| 🔍 Qualidade | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |
| **COR GERAL** | 🟢/🟡/🔴 | ↑/→/↓ | ___________ |

### 10.6 Riscos — Atualização da Semana

| ID | Risco | Nível Anterior | Nível Atual | Mudança | Ação da Semana |
|---|---|---|---|---|---|
| R-001 | ___________ | 🔴 | 🟢/🟡/🔴 | ↑/=/↓ | ___________ |
| R-002 | ___________ | 🔴 | 🟢/🟡/🔴 | ↑/=/↓ | ___________ |
| Novos | ___________ | — | 🟢/🟡/🔴 | Novo | ___________ |

**Riscos CRÍTICOS ativos:** _____ | **Riscos ALTOS ativos:** _____ | **EMV estimado:** R$ ___________

### 10.7 Issues Ativos

| ID Issue | Descrição | Abertura | Responsável | Prazo de Resolução | Status |
|---|---|---|---|---|---|
| ___________ | ___________ | ___/___/2026 | ___________ | ___/___/2026 | 🟢/🟡/🔴 |

### 10.8 Governança — Cadência Cumprida

| Atividade | Planejado | Realizado | Status |
|---|---|---|---|
| Flash Reports (qtd) | _____ | _____ | 🟢/🟡/🔴 |
| Status Report | ___/___/2026 | ___/___/2026 | 🟢/🟡/🔴 |
| Comitê Executivo | ___/___/2026 | ___/___/2026 | 🟢/🟡/🔴 |
| Quórum do Comitê | ___/3 Sponsors | ___/3 Sponsors | 🟢/🟡/🔴 |
| Atualização Registro de Riscos | ___/___/2026 | ___/___/2026 | 🟢/🟡/🔴 |

### 10.9 Principais Issues e Decisões da Semana

**Issues registrados esta semana:**
1. ___________________________________________________________
2. ___________________________________________________________

**Decisões tomadas no Comitê Executivo:**
1. ___________________________________________________________
2. ___________________________________________________________

**Ações pendentes para a próxima semana:**
1. ___________________________________________________________
2. ___________________________________________________________

---

## 11. Protocolo de Escalada

### 11.1 Matriz de Escalada por Nível de Desvio

| Gatilho | Quem detecta | Quem notifica | Para quem | Prazo | Canal | Ação |
|---|---|---|---|---|---|---|
| SPI ou CPI < 0,95 (Amarelo) | Marcela Métrica (VMO) | GP Interno (Marcelo Silveira) | Sponsors (e-mail) | Até o próximo Status Report (quarta-feira) | Status Report + e-mail direto | GP aciona plano de recuperação; comunicar impacto no prazo/custo |
| SPI ou CPI < 0,85 (Vermelho) | Marcela Métrica (VMO) | GP Interno → Sponsors | Décio, Paula, Patrícia | Em até 24 horas | E-mail urgente + convocação de Comitê Emergencial | Comitê Executivo Emergencial em até 48h para decidir ação corretiva |
| Desvio > 25% em qualquer KPI EVM | Marcela Métrica (VMO) | GP Interno | Sponsors + Rodrigo Figaro (KPMG) | Imediato (mesmo dia) | Ligação + e-mail urgente | Revisão formal do baseline; possível replanejamento |
| 2 ou mais riscos CRÍTICOS ativos | Pedro Perigo (VMO) | GP Interno | Sponsors | Em até 24 horas | Status Report + e-mail urgente | Reunião de gerenciamento de riscos com todos os Sponsors |
| Issue sem resolução > 5 dias úteis | Marcela Métrica (VMO) | GP Interno | Sponsors responsáveis | No próximo Comitê Executivo | Pauta de Comitê | Issue colocado em pauta como bloqueio de alta prioridade |
| Entregável KPMG atrasado ≥ 1 semana | GP Interno | GP Interno | Wallacy Lima (KPMG) + Rodrigo Figaro + Sponsors | Em até 24h após constatação | E-mail formal + registro no Status Report | Reunião com KPMG para plano de recuperação; avaliar impacto no caminho crítico |
| Workshop cancelado sem remarcação | GP Interno | GP Interno | Sponsors da entidade impactada | No mesmo dia | Ligação imediata + e-mail | Acionar Sponsor para autorizar sessão emergencial; registrar impacto em SPI |
| Comitê Executivo sem quórum (< 2/3 Sponsors) | VMO Autônomo | GP Interno | Sponsor ausente | Até 2h após a reunião | E-mail direto ao Sponsor | Decisões adiadas registradas em ata; nova convocação em até 5 dias |
| Solicitação de mudança de escopo recebida | GP Interno | GP Interno | Todos os Sponsors | Em até 24h da solicitação | E-mail formal com análise de impacto | Avaliar impacto em CPI/SPI/escopo; decisão formal dos Sponsors antes de qualquer ação |

### 11.2 Fluxo de Escalada — Desvio EVM Crítico

```
Desvio identificado na medição semanal
            │
            ▼
    Marcela Métrica registra o desvio no Dashboard
            │
            ▼
    Desvio < 5% (normal)  →  Registrar no Status Report. Sem ação adicional.
            │
    Desvio 5–15% (amarelo) → GP notifica Sponsors no Status Report.
            │                 GP aciona plano de recuperação.
    Desvio > 15% (vermelho) → GP notifica Sponsors IMEDIATAMENTE (24h).
            │                  Convocar Comitê Executivo Emergencial.
    Desvio > 25% (crítico)  → GP + VMO notificam Sponsors + KPMG.
                               Revisar baseline formalmente.
                               Decisão: aceitar desvio OU replanejamento.
```

### 11.3 Contatos de Escalada

| Papel | Nome | Contato | Disponibilidade |
|---|---|---|---|
| GP Interno | Marcelo Silveira | marcelov@aguiabranca.com.br | Dias úteis — resposta em até 4h |
| Sponsor Principal | Décio Luiz Chieppe | (via secretaria Holding GAB) | Disponível para Comitê Executivo (quinta) |
| Sponsor VAB | Paula Barcelos T. Corrêa | (via secretaria VAB) | Disponível para Comitê Executivo (quinta) |
| Sponsor VixPar | Patrícia Poubel Chieppe | (via secretaria VixPar) | Disponível para Comitê Executivo (quinta) |
| Sócio KPMG | Rodrigo Figaro | (via Wallacy Lima) | Escalada KPMG — decisões contratuais |
| Gerente KPMG | Wallacy Lima | (via GP Interno) | Operacional — resposta em até 2h |
| Monitora VMO | Marcela Métrica | VMO Autônomo | Medição semanal — toda segunda-feira |

### 11.4 Critérios de Escalada Automática (Sem Necessidade de Análise)

Os seguintes eventos disparam escalada automática, sem necessidade de avaliação adicional:

1. **CPI < 0,85 em qualquer semana** → Escalada imediata para Sponsors (risco de aditivo contratual)
2. **SPI < 0,85 em qualquer semana** → Escalada imediata; avaliar impacto na data de 08/05/2026
3. **Qualquer desvio > 25% em relação ao baseline** → Comitê Emergencial obrigatório
4. **2 ou mais issues críticos abertos simultaneamente** → Reunião de crise em 24h
5. **Workshop cancelado na Semana 1 sem remarcação no mesmo dia** → Escalada imediata para Sponsors (caminho crítico impactado)
6. **KPMG sinaliza impossibilidade de cumprir data de 08/05/2026** → Escalada para Sponsors com análise de impacto financeiro e de prazo da Fase 2

---

## Apêndice A — Histórico de Medições EVM

| Semana | Data Medição | PV (R$) | EV (R$) | AC (R$) | SPI | CPI | EAC (R$) | VAC (R$) | Cor Geral |
|---|---|---|---|---|---|---|---|---|---|
| S0 | 05/04/2026 | R$ 0 | R$ 0 | R$ 0 | N/A | N/A | R$ 930.000 | R$ 0 | 🔴* |
| S1 | 13/04/2026 | R$ 186.000 | — | — | — | — | — | — | — |
| S2 | 20/04/2026 | R$ 372.000 | — | — | — | — | — | — | — |
| S3 | 27/04/2026 | R$ 558.000 | — | — | — | — | — | — | — |
| S4 | 04/05/2026 | R$ 744.000 | — | — | — | — | — | — | — |
| S5 | 11/05/2026 | R$ 930.000 | — | — | — | — | — | — | — |

*Cor Geral S0 = 🔴 devido a issues críticos ativos (I-001, I-002) — não por desvio EVM.

---

## Apêndice B — Glossário EVM

| Sigla | Nome | Definição |
|---|---|---|
| BAC | Budget at Completion | Orçamento total aprovado para o projeto |
| PV | Planned Value | Valor que deveria ter sido realizado até a data de medição |
| EV | Earned Value | Valor dos trabalhos efetivamente concluídos e aceitos |
| AC | Actual Cost | Custos efetivamente incorridos (faturas aprovadas) |
| SV | Schedule Variance | EV − PV: variação de prazo em valor financeiro |
| CV | Cost Variance | EV − AC: variação de custo |
| SPI | Schedule Performance Index | EV ÷ PV: índice de performance de prazo |
| CPI | Cost Performance Index | EV ÷ AC: índice de performance de custo |
| ETC | Estimate to Complete | Estimativa do custo para concluir o restante do projeto |
| EAC | Estimate at Completion | AC + ETC: estimativa do custo total ao término |
| VAC | Variance at Completion | BAC − EAC: variação esperada ao término (positivo = economia) |
| TCPI | To Complete Performance Index | (BAC−EV) ÷ (BAC−AC): CPI necessário para terminar no orçamento |

---

*Documento elaborado por Marcela Métrica — Monitora de Performance, VMO Autônomo*
*Run ID: 2026-04-05-173000 | Etapa: 9/12 — Framework de KPIs | ID Projeto: PROJ-2026-003*
*Todos os valores em Reais (BRL). Thresholds EVM revisáveis ao final de cada fase mediante aprovação formal do GP e Sponsors.*
