# STATUS REPORT — Ajustes nos Monitores ZMMR_GSI02/03/04 (SAP ECC Módulo MM)

**Projeto:** PROJ-2026-008 | **Demanda:** DEM-2026-008 (Chamado 6898567 / Work Request 4918651)
**Período coberto:** Pré-execução — Documentação de Iniciação e Planejamento
**Data:** 2026-06-11 | **Report #001**
**Gerente de Projeto:** A designar pelo SQUAD PM/MM (Time de Sustentação ERP) — ver Issue ISS-001
**Sponsor:** Nubia Carla Freitas Santos Souza (Gerente Contábil) — *provisório, aprovação de Diretoria pendente (CB-1)*

---

## STATUS GERAL: 🟡 ATENÇÃO

> **Documentação de Iniciação e Planejamento: 🟢 100% CONCLUÍDA.** Todos os 12 documentos previstos no pipeline de iniciação foram produzidos e validados (TAP, PM Canvas, Plano Geral, ERF, Work Request, Cronograma/WBS, Plano de Riscos, Framework de KPIs).
>
> **Status Geral do Projeto: 🟡 ATENÇÃO** — pela regra do "elo mais fraco" (Marcela Métrica, `kpis.md`), o semáforo consolidado reflete 2 dimensões em 🟡: **Cronograma** (risco de estouro de prazo já identificado na linha de base) e **Riscos** (7 riscos ALTO registrados, nenhum com ação de mitigação iniciada — execução ainda não começou). Nenhum dos dois indica problema materializado; ambos exigem atenção para que a transição da iniciação para a execução não inicie já com desvio.

| Dimensão | Status | KPI Principal |
|----------|--------|---------------|
| Cronograma | 🟡 | SPI: não aplicável (execução não iniciada) — baseline + buffer de 15% (2026-10-10) excede o prazo do TAP (2026-09-30) em ~10 dias |
| Custo | 🟢 | CPI: não aplicável (execução não iniciada) — BAC = R$ 36.000 (R$ 30.000 + 20% contingência) |
| Escopo | 🟢 | Mudanças aprovadas: 0 — escopo de 15 itens em 3 ondas mantido conforme `requisitos.md` (22 RF) |
| Riscos | 🟡 | Riscos ALTO ativos sem mitigação: 7 de 9 (R-001 a R-007) — nenhuma ação iniciada (execução não começou) |
| Qualidade | 🟢 | Documentos de iniciação aprovados internamente: 12/12 — pendente validação formal do solicitante (pesquisa de satisfação, abaixo) |

---

## SUMÁRIO EXECUTIVO

O projeto PROJ-2026-008 concluiu integralmente a fase de **Iniciação e Planejamento** do VMO Autônomo: TAP, PM Canvas, Plano Geral, ERF (22 RF / 9 RNF), Work Request, Cronograma/WBS (3 ondas, M0-M5), Plano de Riscos (9 riscos, R$ 26.800 de valor esperado) e Framework de KPIs foram produzidos e estão prontos para uso na execução.

A demanda foi qualificada como **MELHORIA EVOLUTIVA** (50/100, "APROVADO COM CONDIÇÕES" — Gate G1-G5 com veredicto PASS), a ser executada pelo SQUAD PM/MM (Time de Sustentação ERP), com possibilidade de complemento por consultoria externa SAP ABAP/MM caso a capacidade interna seja insuficiente (Work Request com framing dual-recipient).

**Antes do início da execução, 7 Condições Bloqueantes (CBs) precisam ser resolvidas** — CB-1 a CB-4 com prazo **2026-06-13** (daqui a 2 dias), CB-5 em **2026-06-17** e CB-6 em **2026-06-24**. A mais crítica é a **CB-1 (aprovação formal de Diretoria)**, da qual depende a validade do Sponsor atualmente registrado como provisório. Sem a resolução de CB-1/CB-2, o início formal da execução (Onda 1) fica em risco de atraso.

O planejamento já identificou, de forma proativa, **dois desvios estruturais que precisam de decisão do Sponsor antes do M0 (2026-06-24)**:
1. **Estouro de prazo projetado (~10 dias além do prazo do TAP)** mesmo no cenário com buffer de contingência — caminho crítico com folga zero (item 13, estorno fiscal/contábil).
2. **Reserva de contingência de riscos calculada (R$ 26.800) acima da contingência orçamentária do TAP (R$ 6.000)** — a maior parte do valor esperado é de natureza prazo/esforço (mitigável a custo zero), mas o GP deve estar ciente do gap ao assumir o projeto.

Nenhum dos dois pontos bloqueia o início da execução, mas ambos exigem decisão e comunicação ao solicitante (Tatiane Dias de Moraes / João Henrique) **antes** que expectativas de prazo sejam reforçadas — ver R-006 no Plano de Riscos.

---

## PROGRESSO

**Planejado (fase Iniciação + Planejamento):** 100% | **Realizado:** 100% | **Desvio:** 0%

| Entregável | Status |
|---|---|
| Demanda Coletada / Triagem / Qualificação | ✅ Concluído |
| Gate de Qualificação (G1-G5) | ✅ PASS |
| TAP, PM Canvas, Plano Geral | ✅ Concluído |
| ERF (Especificação de Requisitos Funcionais) | ✅ Concluído (22 RF / 9 RNF) |
| Work Request (Mini-RFP) | ✅ Concluído |
| Cronograma / WBS (3 ondas, M0-M5) | ✅ Concluído |
| Plano de Riscos (Registro + Plano por Risco) | ✅ Concluído (9 riscos) |
| Framework de KPIs (EVM + Semáforo de Saúde) | ✅ Concluído |
| **Próxima fase:** Execução (Onda 1) | ⏳ Aguardando resolução de CB-1 a CB-4 (prazo 2026-06-13) |

---

## ISSUES ABERTAS

| ID | Issue | Impacto | Responsável | Prazo |
|----|-------|---------|-------------|-------|
| ISS-001 (CB-1) | Aprovação formal de Diretoria ainda não confirmada — Sponsor atual (Nubia Carla Freitas Santos Souza) é provisório | Bloqueia validade formal do TAP e início da execução | Diretoria (área solicitante) | 2026-06-13 |
| ISS-002 (CB-2) | Identificação e confirmação do aprovador técnico/orçamentário (Raphael Leitão Sbardelotti, cargo "Gerente de TI" não confirmado) | Bloqueia validação de viabilidade técnica e orçamentária | Sponsor / Diretoria | 2026-06-13 |
| ISS-003 (CB-3) | Destino exato do ajuste no monitor ZMMR_GSI04 e relação com ZMMR_GSI01/item 6 não definidos | Pode gerar retrabalho na Onda 1 (item 6) e Onda 3 | SQUAD PM/MM + Especialista Funcional (Jerfesson Fernandes Helmer) | 2026-06-13 |
| ISS-004 (CB-4) | Priorização entre os itens do escopo ainda ambígua | Pode gerar conflito de alocação do SQUAD PM/MM entre ondas | Sponsor / GP VMO | 2026-06-13 |
| ISS-005 (CB-5/L9) | Estimativa de esforço por fase e indicador quantitativo de eficiência (Critério de Sucesso 4 do TAP) ainda não definidos pelo SQUAD PM/MM | Bloqueia configuração definitiva do EVM (BAC/PV) e do KPI de retrabalho MIRO/GRC | SQUAD PM/MM | 2026-06-17 |
| ISS-006 (CB-6) | Especificação funcional formal e plano de testes dos itens 13/14 (estorno fiscal/contábil) ainda não elaborados | Pré-requisito para início da Onda 3; item 13 está no caminho crítico | SQUAD PM/MM + QA | 2026-06-24 |
| ISS-007 (CB-Orçamento / R-004) | Divergência entre teto declarado como aprovado (R$ 30.000) e BAC com contingência (R$ 36.000) ainda não reconciliada formalmente | Pode gerar necessidade de aditivo orçamentário ou ajuste de escopo (Onda 3) | Sponsor / GP VMO | 2026-06-24 |
| ISS-008 (Cronograma) | Baseline + buffer de 15% (2026-10-10) excede o prazo declarado no TAP (2026-09-30) em ~10 dias | Risco de descumprimento do prazo comprometido ao solicitante (R-006/R-007) | GP VMO | A decidir até M0 (2026-06-24) |
| ISS-009 (GP) | Gerente de Projeto ainda não designado pelo SQUAD PM/MM | Sem ponto focal único para coordenar resolução das CBs acima | SQUAD PM/MM | 2026-06-13 |

---

## PRÓXIMOS PASSOS

1. **Designar o Gerente de Projeto** responsável pela execução, ponto focal único para as CBs — SQUAD PM/MM — até **2026-06-13**.
2. **Obter aprovação formal de Diretoria (CB-1)** e confirmar o aprovador técnico/orçamentário (CB-2), formalizando o Sponsor definitivo do TAP — Diretoria / Sponsor provisório (Nubia Carla Freitas Santos Souza) — até **2026-06-13**.
3. **Resolver CB-3 e CB-4** (destino do ajuste em ZMMR_GSI04 e priorização entre itens) em reunião com o Especialista Funcional (Jerfesson Fernandes Helmer) — SQUAD PM/MM + Sponsor — até **2026-06-13**.
4. **Decidir sobre o desvio de prazo projetado (ISS-008)** — revisar cronograma via CB-5 ou negociar extensão do prazo do TAP para 2026-10-10 — GP VMO + Sponsor — até **2026-06-24 (M0)**.
5. **Enviar a Pesquisa de Satisfação de Iniciação** (anexa abaixo) ao solicitante (Tatiane Dias de Moraes / João Henrique) para validar expectativas antes do início da Onda 1 — Sara Status / GP VMO — até **2026-06-15**.

---

# PESQUISA DE SATISFAÇÃO — Ajustes nos Monitores ZMMR_GSI02/03/04 (SAP ECC Módulo MM)
Tipo: Iniciação (validação das expectativas) | Data: 2026-06-11

## Formulário — A ser enviado a Tatiane Dias de Moraes e João Henrique (solicitantes, Chamado 6898567)

**Pergunta 1 (NPS — Expectativas)**
Em uma escala de 0 a 10, o quanto a documentação de iniciação (escopo dividido em 3 ondas, cronograma e critérios de aceite por item) está alinhada com o que foi solicitado no Chamado 6898567 / Work Request 4918651?

[  ] 0  [  ] 1  [  ] 2  [  ] 3  [  ] 4  [  ] 5  [  ] 6  [  ] 7  [  ] 8  [  ] 9  [  ] 10

**Pergunta 2 (Qualitativa — Priorização das Ondas)**
O planejamento organiza os 15 itens em 3 ondas (Onda 1: itens 2,3,4,6,9,11,15 — até 31/07/2026; Onda 2: itens 1,8,10,12 — até 31/08/2026; Onda 3: itens 5,7,13,14 — até 30/09/2026). Essa priorização atende à urgência do chamado original? Há algum item que precise ser antecipado?

[campo de texto]

**Pergunta 3 (Qualitativa — Prazo)**
O cronograma identificou um risco de que o prazo final possa se estender em até ~10 dias além de 30/09/2026 (até 2026-10-10) caso o buffer de contingência seja necessário. Essa possível extensão é aceitável, ou é necessário priorizar o cumprimento estrito de 30/09/2026 mesmo que isso implique reduzir o escopo da Onda 3?

[campo de texto]

**Pergunta 4 (Comunicação)**
Este é o primeiro de uma série de status reports quinzenais. Há alguma informação adicional, formato ou frequência de comunicação que vocês considerem necessária além do que está previsto?

[campo de texto]

---
**Próxima pesquisa:** Marco M1 (Go-live Onda 1) — previsão 2026-07-15
**Pesquisa final:** 30 dias após go-live da Onda 3 — previsão ~2026-10-12

## Análise dos Resultados

Aguardando respostas — pesquisa recém-criada (Report #001, fase de iniciação). Nenhuma resposta recebida até a data deste report.
