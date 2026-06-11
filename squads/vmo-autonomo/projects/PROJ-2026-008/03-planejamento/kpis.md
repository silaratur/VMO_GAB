# FRAMEWORK DE KPIs — Ajustes nos Monitores ZMMR_GSI02/03/04 (SAP ECC Módulo MM)
Versão: 1.0 | Data: 2026-06-11 | Elaborado por: Marcela Métrica (VMO Autônomo) | Projeto: PROJ-2026-008

---

## Nota de Abertura

Este framework estabelece os indicadores que habilitam decisões objetivas de gestão ao longo das 3 ondas do projeto (Onda 1: 2026-06-17 a 2026-07-15; Onda 2: 2026-07-16 a 2026-08-12; Onda 3: 2026-08-13 a 2026-09-11; Encerramento: até 2026-09-25). CPI e SPI são os indicadores primários — qualquer leitura de saúde do projeto começa por eles. Anomalias com variação > 25% em qualquer KPI (ex.: SPI cair de 1,00 para < 0,75 entre dois ciclos) são escaladas imediatamente ao Sponsor, sem aguardar o próximo status report quinzenal.

⚠️ **Dado a confirmar (não tratado como informação até resolução):** o indicador quantitativo de eficiência (Critério de Sucesso 4 do TAP — redução do tempo de fechamento mensal e/ou retrabalhos de conciliação MIRO/GRC) está formalmente pendente de definição até 2026-06-17 (CB-5/lacuna L9). O KPI "Redução de Retrabalho de Conciliação MIRO/GRC" abaixo é proposto como a operacionalização desse critério, com baseline a ser medida antes do go-live de cada onda — **a meta numérica de 20% já está definida no TAP**, mas a métrica-base de coleta (ex.: nº de conciliações manuais/mês) ainda precisa ser instrumentada pelo SQUAD PM/MM.

---

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|---------|----------|------|-----------|------------|-------|-------------|
| CPI (Cost Performance Index) | EV / AC | 1,00 | ≥ 1,00 | 0,85–0,99 | < 0,85 | Quinzenal | GP VMO |
| SPI (Schedule Performance Index) | EV / PV | 1,00 | ≥ 1,00 | 0,85–0,99 | < 0,85 | Quinzenal | GP VMO |
| EAC (Estimate at Completion) | BAC / CPI | R$ 36.000 | ≤ R$ 36.000 | R$ 36.000–R$ 42.350 | > R$ 42.350 | Quinzenal | GP VMO |
| VAC (Variance at Completion) | BAC – EAC | R$ 0 | ≥ R$ 0 | -R$ 6.350 a R$ 0 | < -R$ 6.350 | Quinzenal | GP VMO |

**Implicação dos limites:**
- **CPI < 0,85**: o projeto está consumindo recursos a um ritmo que, projetado para o BAC de R$ 36.000, resultaria em estouro superior a ~R$ 6.350 — patamar que já aproxima ou ultrapassa a folga entre o teto declarado como aprovado (R$ 30.000) e o BAC com contingência (R$ 36.000). Acima desse ponto, o risco R-004 (Estouro de Orçamento) passa de "ALTO" para "MATERIALIZADO" e exige acionamento imediato do plano de contingência (priorizar Ondas 1 e 2, submeter Onda 3 como aditivo).
- **SPI < 0,85**: considerando que o caminho crítico tem **folga zero** (cronograma.md), um SPI abaixo de 0,85 em qualquer ponto após o início da Onda 1 indica que o atraso acumulado já compromete a data de Go-live da onda seguinte — não é mais um desvio absorvível pelo buffer de gestão de 15% (que cobre apenas ~2,2 semanas sobre ~14,5 semanas de baseline).
- **VAC < -R$ 6.350**: o desvio de custo previsto já supera a contingência de 20% (R$ 6.000) embutida no BAC — qualquer valor abaixo deste threshold exige comunicação formal ao Sponsor sobre necessidade de aditivo orçamentário (vinculado a CB-Orçamento/R-004).

---

## KPIs de Resultado do Projeto

| KPI | Descrição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|-----------|----------|------|-----------|------------|-------|-------------|
| Cobertura de Itens por Onda — Onda 1 | % dos 7 itens da Onda 1 (2,3,4,6,9,11,15) implementados e validados (UAT aprovado) em produção | 0% | 100% até 2026-07-31 | 70–99% até 2026-07-31 | < 70% até 2026-07-31 | Quinzenal | GP VMO |
| Cobertura de Itens por Onda — Onda 2 | % dos 4 itens da Onda 2 (1,8,10,12) implementados e validados em produção | 0% | 100% até 2026-08-31 | 70–99% até 2026-08-31 | < 70% até 2026-08-31 | Quinzenal | GP VMO |
| Cobertura de Itens por Onda — Onda 3 | % dos 4 itens da Onda 3 (5,7,13,14) implementados, testados (incl. especificação funcional formal e plano de testes dos itens 13/14 — CB-6) e validados em produção | 0% | 100% até 2026-09-30 | 70–99% até 2026-09-30 | < 70% até 2026-09-30 | Quinzenal | GP VMO |
| Definição Formal do Indicador de Eficiência (CB-5/L9) | Status de definição formal do indicador quantitativo de eficiência (Critério de Sucesso 4 do TAP) pelo SQUAD PM/MM | Não definido | Definido e baseline medida até 2026-06-17 | Definido até 2026-06-24 (atraso ≤ 1 semana) | Não definido até 2026-06-24 | Única medição (gate), depois mensal | SQUAD PM/MM + GP VMO |
| Redução de Retrabalho de Conciliação MIRO/GRC | % de redução do nº de retrabalhos manuais de conciliação MIRO/GRC vs. baseline pré-Onda 1 (instrumento de medição a ser definido via CB-5/L9) | 0% (a confirmar — ⚠️ dado a confirmar) | ≥ 20% em até 60 dias após go-live da Onda 3 (até ~2026-11-11) | 10–19% | < 10% | Mensal (a partir da baseline) | SQUAD PM/MM |
| Incidentes Críticos Fiscais/Contábeis (Itens 13/14) | Nº de incidentes críticos de divergência fiscal/contábil decorrentes dos itens 13 e 14 nos 30 dias após go-live da Onda 3 | 0 | 0 incidentes | 1 incidente (não-crítico/contornado) | ≥ 1 incidente crítico | Diário (janela de 30d pós go-live Onda 3), depois encerrado | SQUAD PM/MM (QA) + Especialista Funcional |
| Gestão de Riscos — Riscos ALTO Ativos sem Mitigação | Nº de riscos classificados ALTO (R-001 a R-007) sem ao menos 1 ação de resposta em andamento ou concluída no prazo definido | 7 (todos ALTO no registro inicial) | 0 riscos ALTO sem ação em andamento | 1 risco ALTO sem ação em andamento | ≥ 2 riscos ALTO sem ação em andamento, ou qualquer risco ALTO com gatilho disparado sem resposta | Quinzenal (alinhado ao status report) | Pedro Perigo / GP VMO |
| Gestão de Riscos — Cobertura de Gatilhos Monitorados | % dos 9 riscos do registro (R-001 a R-009) com gatilho explicitamente verificado no ciclo de status report | 0% (registro recém-criado) | 100% dos gatilhos verificados a cada ciclo | 80–99% | < 80% | Quinzenal | Pedro Perigo / GP VMO |

**Rastreabilidade aos Critérios de Sucesso do TAP:**
1. Critério 1 (100% Onda 1 até 31/07/2026) → KPI "Cobertura de Itens por Onda — Onda 1"
2. Critério 2 (100% Onda 2 até 31/08/2026) → KPI "Cobertura de Itens por Onda — Onda 2"
3. Critério 3 (100% Onda 3 até 30/09/2026, incl. especificação e plano de testes 13/14) → KPI "Cobertura de Itens por Onda — Onda 3"
4. Critério 4 (indicador de eficiência definido até 17/06/2026, meta de melhoria ≥ 20% em 60 dias pós Onda 3) → KPIs "Definição Formal do Indicador de Eficiência (CB-5/L9)" e "Redução de Retrabalho de Conciliação MIRO/GRC"
5. Critério 5 (zero incidentes críticos fiscais/contábeis nos 30 dias pós go-live Onda 3, itens 13/14) → KPI "Incidentes Críticos Fiscais/Contábeis (Itens 13/14)"

**Implicação dos KPIs de Riscos:**
- Com 7 dos 9 riscos do registro classificados como ALTO (R-001 a R-007, scores 9–15), o threshold de "Riscos ALTO Ativos sem Mitigação" é deliberadamente apertado (🟡 a partir de 1 risco sem ação em andamento) — refletindo o princípio de Pedro Perigo de que riscos ALTO geram notificação imediata ao Sponsor quando o gatilho é disparado.
- O KPI "Cobertura de Gatilhos Monitorados" é o indicador de **disciplina de processo**: um valor abaixo de 80% sinaliza que o registro de riscos está sendo atualizado pro forma, sem revisão real dos gatilhos — condição que historicamente precede a materialização não detectada de riscos ALTO (ex.: R-001/governança, R-005/disponibilidade do squad).

---

## Configuração EVM

- **BAC (Budget at Completion):** R$ 36.000 (R$ 30.000 de estimativa base + R$ 6.000 de contingência de 20%, conforme TAP). ⚠️ Nota: o BAC adotado para EVM (R$ 36.000) é o **total estimado com contingência**, não o teto declarado como aprovado (R$ 30.000) — essa diferença de R$ 6.000 é monitorada separadamente pelo risco R-004/CB-Orçamento e não deve ser confundida com VAC negativo por estouro real.

- **PV Baseline (Planned Value):** Curva S definida pelo cronograma.md, com marcos M0 (2026-06-24, CBs resolvidas), M1 (2026-07-15, Go-live Onda 1), M2 (2026-08-12, Go-live Onda 2), M3 (2026-06-24, especificações 13/14 aprovadas), M4 (2026-09-12, Go-live Onda 3) e M5 (2026-09-25, encerramento). PV é calculado proporcionalmente ao custo planejado de cada pacote de trabalho da WBS, distribuído ao longo de sua duração planejada.

- **Método de Medição de EV:** Porcentagem física concluída por pacote de trabalho (entregáveis aprovados, não esforço gasto), aplicando a seguinte regra de medição por tipo de entregável:

  | Tipo de Entregável | Regra de EV | Exemplos na WBS |
  |---|---|---|
  | Documentação (especificações funcionais, planos de testes, registros, lições aprendidas) | **0/100**: 0% até aprovação formal do documento, 100% após aprovação | 1.2.1.2, 1.3.1.1, 1.4.1.1, 1.4.1.2, 1.4.1.3, 1.5.1 |
  | Desenvolvimento/customização ABAP | **50/50**: 50% ao início efetivo do desenvolvimento, 50% ao teste unitário aprovado | 1.2.2.1, 1.2.2.2, 1.2.2.3, 1.3.2.1, 1.3.2.2, 1.3.2.3, 1.4.2.1, 1.4.2.2, 1.4.2.3, 1.4.2.4 |
  | Testes/Homologação (unitários, integração, UAT) | **Por entregável aprovado**: EV = (nº de itens/cenários com resultado PASS aprovado) / (nº total de itens/cenários do pacote) × 100% do valor do pacote | 1.2.3.1, 1.2.3.2, 1.3.3.1, 1.3.3.2, 1.4.3.1, 1.4.3.2, 1.4.3.3 |
  | Gerenciamento (status reports, gestão de riscos, resolução de CBs, encerramento) | **Proporcional ao tempo decorrido**: EV = (dias úteis decorridos / dias úteis planejados do pacote) × valor do pacote, até o limite de 100% | 1.1.1, 1.1.2, 1.1.3, 1.5.2, 1.5.3 |

- **Frequência de Atualização do EVM:** Quinzenal, alinhada aos status reports (Sara Status), com checkpoint adicional ao final de cada onda (Go-live Onda 1/2/3 — M1/M2/M4).

---

## Semáforo de Saúde

| Dimensão | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|----------|----------|-----------|------------|
| Cronograma (SPI) | SPI ≥ 1,00 | 0,85 ≤ SPI < 1,00 | SPI < 0,85 |
| Custo (CPI) | CPI ≥ 1,00 | 0,85 ≤ CPI < 1,00 | CPI < 0,85 |
| Escopo | Sem mudanças de escopo aprovadas, ou mudanças sem impacto em prazo/custo total | 1–2 mudanças aprovadas com impacto em onda(s), sem alteração do prazo final (30/09/2026) | > 2 mudanças aprovadas, ou qualquer mudança que altere o prazo final ou o BAC além do VAC crítico |
| Riscos | Todos os riscos ALTO (R-001 a R-007) com ação de resposta em andamento ou concluída; nenhum gatilho disparado sem resposta | 1 risco ALTO ativo sem ação em andamento, ou cobertura de gatilhos monitorados entre 80–99% | ≥ 2 riscos ALTO ativos sem ação, qualquer risco com gatilho disparado sem resposta acionada, ou cobertura de gatilhos < 80% |
| Satisfação Cliente | NPS ≥ 8/10 (pesquisa pós-onda) ou ausência de escalonamento via R-006 (expectativa de prazo) | NPS 6–7/10, ou 1 manifestação formal de insatisfação/cobrança de SLA (chamado 6898567) sem resolução em até 5 dias úteis | NPS < 6/10, ou reabertura formal do chamado 6898567 com escalonamento ao Sponsor, ou recusa de UAT em qualquer onda |

**Implicação do Semáforo Consolidado:**
- O semáforo de saúde do projeto é definido pela **pior dimensão** (regra "elo mais fraco") — um único 🔴 em qualquer dimensão classifica o projeto como 🔴 no status report, independentemente das demais.
- Dado o caminho crítico com folga zero e o risco R-006 (expectativa de prazo do solicitante via chamado de SLA "1 semana"), as dimensões **Cronograma** e **Satisfação Cliente** têm correlação direta neste projeto: um SPI 🟡 não comunicado proativamente à Tatiane Dias de Moraes/João Henrique tende a rebaixar também a dimensão Satisfação Cliente para 🟡 ou 🔴, mesmo sem atraso real na entrega.
- A dimensão **Riscos** funciona como indicador antecedente (leading indicator): um rebaixamento para 🟡 ou 🔴 nesta dimensão tipicamente precede, em 1–2 ciclos quinzenais, um rebaixamento em Cronograma ou Custo — deve ser tratada como sinal de alerta precoce, não apenas como registro histórico.

---

## Resumo de Frequências e Responsáveis

| Frequência | KPIs |
|---|---|
| Quinzenal | CPI, SPI, EAC, VAC, Cobertura de Itens por Onda (1/2/3), Gestão de Riscos — Riscos ALTO Ativos sem Mitigação, Gestão de Riscos — Cobertura de Gatilhos Monitorados |
| Diária (janela específica) | Incidentes Críticos Fiscais/Contábeis (Itens 13/14) — durante os 30 dias pós go-live da Onda 3 |
| Mensal (a partir de baseline) | Redução de Retrabalho de Conciliação MIRO/GRC |
| Gate único + acompanhamento mensal | Definição Formal do Indicador de Eficiência (CB-5/L9) |

| Responsável | KPIs sob sua coleta/cálculo |
|---|---|
| GP VMO | CPI, SPI, EAC, VAC, Cobertura de Itens por Onda (1/2/3) |
| SQUAD PM/MM | Definição Formal do Indicador de Eficiência (CB-5/L9), Redução de Retrabalho de Conciliação MIRO/GRC |
| SQUAD PM/MM (QA) + Especialista Funcional | Incidentes Críticos Fiscais/Contábeis (Itens 13/14) |
| Pedro Perigo / GP VMO | Gestão de Riscos — Riscos ALTO Ativos sem Mitigação, Gestão de Riscos — Cobertura de Gatilhos Monitorados |
