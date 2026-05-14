# Plano de Gestão de Riscos — Caminhos Estratégicos do ERP GAB

**ID Projeto:** PROJ-2026-003
**Versão:** 1.0
**Data:** 05/04/2026
**Elaborado por:** Pedro Perigo — Analista de Riscos (VMO Autônomo)
**Run ID:** 2026-04-05-173000

---

## 1. Metodologia de Análise de Riscos

### Escalas de Avaliação

**Probabilidade (P):**

| Valor | Nível | Descrição |
|---|---|---|
| 1 | Muito Baixa | < 10% de probabilidade de ocorrência |
| 2 | Baixa | 10–30% |
| 3 | Média | 30–50% |
| 4 | Alta | 50–70% |
| 5 | Muito Alta | > 70% |

**Impacto (I):**

| Valor | Nível | Descrição |
|---|---|---|
| 1 | Muito Baixo | Atraso < 1 dia ou custo adicional < R$5K; impacto irrelevante na entrega |
| 2 | Baixo | Atraso de 1–3 dias ou custo adicional R$5K–R$30K; entrega com ajuste menor |
| 3 | Médio | Atraso de 3–7 dias ou custo adicional R$30K–R$100K; entrega comprometida parcialmente |
| 4 | Alto | Atraso de 1–2 semanas ou custo adicional R$100K–R$300K; entrega final em risco |
| 5 | Crítico | Atraso > 2 semanas ou custo adicional > R$300K; entrega impossível sem replanning |

**Nível de Risco (Score = P × I):**

| Score | Nível | Cor |
|---|---|---|
| 1–4 | BAIXO | 🟢 |
| 5–9 | MÉDIO | 🟡 |
| 10–14 | ALTO | 🟠 |
| 15–25 | CRÍTICO | 🔴 |

---

## 2. Registro de Riscos

| ID | Categoria | Descrição do Risco | P | I | Score | Nível |
|---|---|---|---|---|---|---|
| R-001 | Prazo | Workshops da Semana 1 atrasam ou são cancelados por falta de agenda confirmada e participantes não designados | 4 | 5 | 20 | 🔴 CRÍTICO |
| R-002 | Stakeholders | Baixo engajamento das áreas de negócio nos workshops — participantes enviam substitutos sem autoridade ou cancelam sessões | 4 | 4 | 16 | 🔴 CRÍTICO |
| R-003 | Qualidade | Avaliação do Score Model influenciada por percepções individuais dos avaliadores em vez de dados objetivos, comprometendo a credibilidade da recomendação final | 3 | 5 | 15 | 🔴 CRÍTICO |
| R-004 | Governança | GP Interno (Marcelo Silveira) deixa o papel interino sem substituto designado durante a execução do projeto | 2 | 5 | 10 | 🟠 ALTO |
| R-005 | Qualidade | Foco excessivo na escolha da ferramenta (plataforma ERP) sem prévia definição do cenário-alvo de processos, gerando seleção desalinhada com a estratégia futura do GAB | 3 | 4 | 12 | 🟠 ALTO |
| R-006 | Comunicação | Comunicação insuficiente sobre o projeto para stakeholders internos não envolvidos diretamente, gerando resistência à futura implementação | 3 | 3 | 9 | 🟡 MÉDIO |
| R-007 | Prazo | Feriado de 01/05/2026 (Dia do Trabalho) reduz a Semana 4 para 4 dias úteis, comprimindo as atividades de análise de aderências | 5 | 2 | 10 | 🟠 ALTO |
| R-008 | Financeiro | Escopo da Fase 1 cresce além do contratado (novas áreas ou entidades solicitam inclusão), gerando necessidade de aditivo contratual com KPMG | 2 | 4 | 8 | 🟡 MÉDIO |
| R-009 | Técnico | As três plataformas candidatas (SAP, Oracle, TOTVS) obtêm scores muito próximos, impossibilitando uma recomendação clara e objetiva sem critérios de desempate definidos | 2 | 4 | 8 | 🟡 MÉDIO |
| R-010 | Decisão | O Comitê Executivo não aprova a recomendação da KPMG na apresentação final, requerendo nova rodada de análises ou revisão da metodologia | 2 | 5 | 10 | 🟠 ALTO |
| R-011 | Prazo | Início da Fase 2 (RFP) é postergado aguardando aprovação da decisão de plataforma, atrasando o cronograma de seleção de fornecedor | 3 | 3 | 9 | 🟡 MÉDIO |
| R-012 | Qualidade | Documentação de processos AS-IS gerada nos workshops é superficial ou incompleta por limitação de tempo das sessões (1–2 dias por área) | 3 | 3 | 9 | 🟡 MÉDIO |
| R-013 | Stakeholders | Conflito entre os três sponsors sobre qual plataforma priorizar, baseado em interesses específicos de cada divisão (Holding vs. VixPar vs. VAB) | 2 | 4 | 8 | 🟡 MÉDIO |
| R-014 | Financeiro | Fornecedores das plataformas candidatas exercem pressão comercial sobre os tomadores de decisão GAB fora do processo formal de assessment | 2 | 3 | 6 | 🟡 MÉDIO |
| R-015 | Técnico | Inconsistência na metodologia Score Model (5 vs. 6 pilares — LAC-007) não é esclarecida antes da aplicação, gerando questionamento posterior da validade do score | 3 | 3 | 9 | 🟡 MÉDIO |

---

## 3. Matriz de Probabilidade × Impacto

```
         │  I=1   │  I=2   │  I=3   │  I=4   │  I=5
─────────┼────────┼────────┼────────┼────────┼────────
P=5      │   🟢   │  🟠    │  🔴    │  🔴    │  🔴
(M.Alta) │        │  R-007 │        │        │
─────────┼────────┼────────┼────────┼────────┼────────
P=4      │   🟢   │  🟡    │  🟡    │  🔴    │  🔴
(Alta)   │        │        │        │  R-002 │  R-001
─────────┼────────┼────────┼────────┼────────┼────────
P=3      │   🟢   │  🟡    │  🟡    │  🟠    │  🔴
(Média)  │        │        │R-006   │  R-005 │  R-003
         │        │        │R-012   │        │
         │        │        │R-015   │        │
─────────┼────────┼────────┼────────┼────────┼────────
P=2      │   🟢   │  🟡    │  🟡    │  🟡    │  🟠
(Baixa)  │        │        │R-014   │R-008   │  R-004
         │        │        │        │R-009   │  R-010
         │        │        │        │R-013   │
─────────┼────────┼────────┼────────┼────────┼────────
P=1      │   🟢   │  🟢    │  🟡    │  🟡    │  🟠
(M.Baixa)│        │        │        │        │
─────────┴────────┴────────┴────────┴────────┴────────
```

**Riscos por nível:**
- 🔴 CRÍTICO: R-001, R-002, R-003
- 🟠 ALTO: R-004, R-005, R-007, R-010
- 🟡 MÉDIO: R-006, R-008, R-009, R-011, R-012, R-013, R-014, R-015
- 🟢 BAIXO: nenhum

---

## 4. Plano de Resposta por Risco

---

### R-001 — Atraso ou cancelamento dos workshops da Semana 1
**Nível:** 🔴 CRÍTICO (Score 20)
**Categoria:** Prazo
**Estratégia:** MITIGAR

**Gatilho (Trigger):** Até o final do dia 05/04/2026 (hoje), a agenda detalhada da Semana 1 não foi confirmada por Wallacy Lima (KPMG) ou Marcelo Silveira (GP). Qualquer sessão da Semana 1 for cancelada sem remarcação confirmada.

**Ações de Mitigação:**
| Ação | Responsável | Prazo |
|---|---|---|
| Contatar Wallacy Lima (KPMG) imediatamente para obter agenda completa da Semana 1 (datas, horários, temas, facilitadores) | Marcelo Silveira | 05/04/2026 (hoje) |
| Designar participantes internos GAB para cada sessão com reservas (backup) nomeadas | Marcelo Silveira + Líderes de área | 05/04/2026 (hoje) |
| Confirmar salas, videoconferência e acesso aos sistemas necessários para as sessões | Marcelo Silveira / DTI | 05/04/2026 (hoje) |
| Estabelecer protocolo de remarcação: qualquer cancelamento deve ser remarcado dentro da mesma semana | Marcelo Silveira + Wallacy Lima | 05/04/2026 (hoje) |

**Plano de Contingência:** Se a Semana 1 iniciar sem agenda confirmada, GP Interno deve acionar os Sponsors imediatamente para autorizar a KPMG a conduzir sessões em formato remoto/emergencial com quaisquer participantes disponíveis, documentando quais áreas não foram cobertas adequadamente para retomada na Semana 2. Impacto esperado: compressão das análises das Semanas 3-4.

---

### R-002 — Baixo engajamento das áreas de negócio nos workshops
**Nível:** 🔴 CRÍTICO (Score 16)
**Categoria:** Stakeholders
**Estratégia:** MITIGAR

**Gatilho:** Mais de 1 sessão de workshop com ausência de participante-chave (sem substituto com conhecimento equivalente) OU participante que não consegue responder ≥ 30% das perguntas da KPMG na sessão.

**Ações de Mitigação:**
| Ação | Responsável | Prazo |
|---|---|---|
| Cada Sponsor comunica formalmente às suas áreas a obrigatoriedade de participação nos workshops — prioridade executiva | Décio Chieppe, Paula Barcelos, Patrícia Chieppe | Antes de 06/04/2026 |
| Desbloquear participantes do calendário para toda a duração do workshop (não apenas "quando puder") | Líderes de área + Marcelo Silveira | 05/04/2026 |
| Preparar briefing de 1 página por área explicando o que será discutido e qual preparação é necessária | KPMG / Marcelo Silveira | 05/04/2026 |
| Registrar e reportar no Flash Report diário o nível de participação de cada sessão | Marcelo Silveira | Contínuo |

**Plano de Contingência:** Para sessões com baixo engajamento documentado, KPMG conduz sessão complementar de validação com o GP Interno e materiais de referência existentes. O risco de distorção no score é registrado no relatório final com flag de limitação.

---

### R-003 — Avaliação influenciada por percepções individuais
**Nível:** 🔴 CRÍTICO (Score 15)
**Categoria:** Qualidade
**Estratégia:** MITIGAR

**Gatilho:** Divergência > 2 pontos no score de qualquer pilar entre dois avaliadores distintos para a mesma plataforma, sem justificativa documentada baseada em evidência objetiva.

**Ações de Mitigação:**
| Ação | Responsável | Prazo |
|---|---|---|
| Exigir da KPMG que o Score Model seja baseado em evidências documentadas (telas, demos, benchmarks) — não apenas opiniões das sessões | Marcelo Silveira | Semana 3 início |
| Solicitar à KPMG sessões de calibração de score com múltiplos avaliadores para cada plataforma | Wallacy Lima (KPMG) | Semanas 3-4 |
| Incluir no Status Report semanal a indicação de quais critérios foram avaliados por evidência vs. percepção | KPMG + VMO | Semanal |
| VMO solicita matriz de rastreabilidade: score → evidência → fonte | Marcelo Silveira | Semana 4 (na revisão das matrizes) |

**Plano de Contingência:** Se o score final tiver baixa base empírica, o relatório KPMG deve incluir seção de "limitações metodológicas" explicitando quais critérios foram avaliados por percepção e com que nível de confiança. O Comitê Executivo decide se aceita a recomendação com essa ressalva ou solicita complementação.

---

### R-004 — Saída do GP Interno (Marcelo Silveira) sem sucessor designado
**Nível:** 🟠 ALTO (Score 10)
**Categoria:** Governança
**Estratégia:** MITIGAR

**Gatilho:** Marcelo Silveira comunica saída ou afastamento prolongado do papel de GP sem substituto designado com no mínimo 5 dias de antecedência.

**Ações de Mitigação:**
| Ação | Responsável | Prazo |
|---|---|---|
| Confirmar com a Diretoria GAB se há previsão de titularização ou se há um backup identificado para o cargo | Sponsors / RH GAB | 07/04/2026 (CB-01 do parecer de qualificação) |
| Produzir e manter atualizado Knowledge Base do projeto no VMO Autônomo para facilitar onboarding de qualquer sucessor | VMO Autônomo | Contínuo |
| GP Interno deve documentar todas as decisões e reuniões no sistema de registro do projeto | Marcelo Silveira | Contínuo |

**Plano de Contingência:** Em caso de saída abrupta, o Sponsor Décio Luiz Chieppe assume temporariamente o papel de GP até designação de substituto. VMO Autônomo produz briefing de transição com status atualizado do projeto.

---

### R-005 — Foco em ferramenta sem definição do cenário-alvo de processos
**Nível:** 🟠 ALTO (Score 12)
**Categoria:** Qualidade
**Estratégia:** MITIGAR

**Gatilho:** Ao final da Semana 2, os workshops não produziram definição de "cenário-alvo" (TO-BE) para as principais áreas de processo — apenas mapeamento do estado atual (AS-IS).

**Ações de Mitigação:**
| Ação | Responsável | Prazo |
|---|---|---|
| Solicitar à KPMG esclarecimento sobre como o cenário-alvo de processos será capturado nos workshops das Semanas 1-2 | Marcelo Silveira | Semana 1 |
| Incluir pauta explícita sobre "processo futuro desejado" em cada workshop, não apenas "processo atual" | Wallacy Lima (KPMG) | Semanas 1-2 |

**Plano de Contingência:** Se o cenário-alvo não for capturado adequadamente nas Semanas 1-2, incluir sessão adicional de validação de processo futuro na Semana 3 antes do início do scoring.

---

### R-007 — Feriado 01/05/2026 comprime a Semana 4
**Nível:** 🟠 ALTO (Score 10)
**Categoria:** Prazo
**Estratégia:** ACEITAR (risco certo, impacto baixo com planejamento)

**Gatilho:** Este risco é de materialização CERTA (01/05 é feriado nacional). O impacto depende de como a Semana 4 for planejada.

**Ações de Contingência (ativação imediata):**
| Ação | Responsável | Prazo |
|---|---|---|
| Informar KPMG que a Semana 4 tem 4 dias úteis (27/04 a 30/04) + retorno 04/05 (início da Semana 5) | Marcelo Silveira | 06/04/2026 |
| Planejar as atividades de maior densidade da Semana 4 para os dias 27–28/04 | Wallacy Lima (KPMG) | Semana 1 |
| Verificar se 30/04 (véspera do feriado) terá disponibilidade reduzida das áreas | Marcelo Silveira | Semana 1 |

---

### R-010 — Comitê Executivo não aprova recomendação KPMG
**Nível:** 🟠 ALTO (Score 10)
**Categoria:** Decisão
**Estratégia:** MITIGAR

**Gatilho:** No Comitê Executivo da Semana 3 (mid-point review), algum Sponsor expressa discordância fundamental com a metodologia ou com os candidatos em análise.

**Ações de Mitigação:**
| Ação | Responsável | Prazo |
|---|---|---|
| Realizar Kick Off Executivo com apresentação da metodologia Score Model para alinhamento de expectativas ANTES da apresentação final | Rodrigo Figaro (KPMG) | Abril/2026 |
| Conduzir mid-point review na Semana 3 com os Sponsors para validar o andamento e resolver discordâncias cedo | Rodrigo Figaro + Marcelo Silveira | 24/04/2026 |
| Documentar explicitamente os critérios de avaliação (Score Model) aprovados pelos Sponsors desde o início | Wallacy Lima / Marcelo Silveira | Semana 1 |

**Plano de Contingência:** Se o Comitê Executivo não aprovar na apresentação final: (1) documentar os pontos de discordância; (2) KPMG realiza sessão de revisão focada nos critérios contestados; (3) nova apresentação em até 5 dias úteis.

---

### Riscos Médios — Planos Resumidos

| ID | Risco | Estratégia | Ação Principal | Responsável | Prazo |
|---|---|---|---|---|---|
| R-006 | Comunicação insuficiente com stakeholders internos | MITIGAR | Produzir newsletter/comunicado interno sobre o projeto até Semana 2; incluir no plano de comunicação | Marcelo Silveira | Semana 2 |
| R-008 | Expansão de escopo | EVITAR | Registrar formalmente que qualquer inclusão de área/entidade requer aprovação dos Sponsors + aditivo KPMG | Marcelo Silveira | Semana 1 |
| R-009 | Scores muito próximos sem critério de desempate | MITIGAR | Confirmar com KPMG o procedimento de desempate (LAC-008) antes da Semana 3 | Marcelo Silveira | Semana 1-2 |
| R-011 | Atraso no início da Fase 2 | ACEITAR | Buffer de 1 semana já previsto no cronograma; monitorar decisão de aprovação ao final da Semana 5 | VMO Autônomo | Contínuo |
| R-012 | Documentação AS-IS superficial | MITIGAR | Solicitar à KPMG template mínimo de documentação por workshop antes da Semana 1 | Wallacy Lima | 05/04/2026 |
| R-013 | Conflito entre Sponsors sobre plataforma | MITIGAR | Estabelecer critérios ponderados (Score Model) como árbitro objetivo ANTES da avaliação; mid-point review na S3 | Rodrigo Figaro | Kick Off Executivo |
| R-014 | Pressão comercial de fornecedores | MITIGAR | GP orienta todos os participantes a não aceitar reuniões individuais com fornecedores durante o assessment | Marcelo Silveira | Semana 1 |
| R-015 | Inconsistência no número de pilares (5 vs. 6) | EVITAR | Confirmar com KPMG o número correto de pilares (LAC-007) antes da Semana 3 | Marcelo Silveira | Semana 1 |

---

## 5. Reserva de Contingência — Cálculo de Valor Esperado

| ID | Risco | Impacto Financeiro Estimado | P (decimal) | Valor Esperado |
|---|---|---|---|---|
| R-001 | Atraso workshops Semana 1 | R$ 200.000 (1 semana de atraso na entrega final = adicional KPMG estimado) | 0,40 | R$ 80.000 |
| R-002 | Baixo engajamento áreas | R$ 150.000 (sessões complementares + risco de decisão inadequada) | 0,40 | R$ 60.000 |
| R-003 | Score por percepção individual | R$ 100.000 (revisão complementar da metodologia) | 0,30 | R$ 30.000 |
| R-004 | Saída do GP Interno | R$ 80.000 (onboarding de novo GP + perda de contexto) | 0,20 | R$ 16.000 |
| R-005 | Foco em ferramenta vs. cenário alvo | R$ 120.000 (sessões adicionais de mapeamento de processo futuro) | 0,30 | R$ 36.000 |
| R-006 | Comunicação insuficiente | R$ 30.000 (ações de comunicação e engajamento) | 0,30 | R$ 9.000 |
| R-007 | Feriado 01/05 | R$ 20.000 (compressão de sessões) | 1,00 (certo) | R$ 20.000 |
| R-008 | Expansão de escopo | R$ 200.000 (aditivo contratual KPMG estimado) | 0,20 | R$ 40.000 |
| R-009 | Scores próximos | R$ 50.000 (análise complementar de desempate) | 0,20 | R$ 10.000 |
| R-010 | Não aprovação pelo Comitê | R$ 100.000 (revisão da análise + nova apresentação) | 0,20 | R$ 20.000 |
| R-011 | Atraso Fase 2 | R$ 50.000 (custo de espera da equipe KPMG) | 0,30 | R$ 15.000 |
| R-012 | Documentação AS-IS superficial | R$ 60.000 (sessões complementares) | 0,30 | R$ 18.000 |
| R-013 | Conflito entre Sponsors | R$ 80.000 (mediação e nova rodada de análise) | 0,20 | R$ 16.000 |
| R-014 | Pressão comercial fornecedores | R$ 30.000 (impacto na qualidade da decisão) | 0,20 | R$ 6.000 |
| R-015 | Inconsistência pilares Score Model | R$ 40.000 (revisão do score já calculado) | 0,30 | R$ 12.000 |
| | | | **VALOR ESPERADO TOTAL** | **R$ 388.000** |

**Recomendação de Reserva de Contingência:**

| Tipo | Valor | Finalidade |
|---|---|---|
| Reserva de Contingência (riscos identificados) | R$ 388.000 | Cobertura do valor esperado dos riscos listados |
| Reserva de Gerenciamento (riscos não identificados) | R$ 110.000 (~10% do investimento Fase 1) | Riscos emergentes não previstos na iniciação |
| **Reserva Total Recomendada** | **R$ 498.000** | A ser negociada com área financeira e Sponsors |

> **Nota importante:** O contrato com a KPMG de R$ 930.000 é o valor base da Fase 1. As reservas acima representam orçamento adicional potencial necessário para gestão de riscos, não incluído no contrato atual. Recomenda-se revisão com a área financeira da Holding sobre disponibilidade desta reserva.

---

## 6. Calendário de Revisão de Riscos

| Momento | Atividade | Responsável |
|---|---|---|
| Semana 1 (10/04/2026) | Primeira revisão do Risk Register — validar R-001 (materializado?) e atualizar probabilidades | Pedro Perigo / GP Interno |
| Semanalmente (quinta-feira) | Revisão do Risk Register no Comitê Executivo — riscos CRÍTICOS e ALTOS em destaque | Marcelo Silveira |
| Semana 3 — mid-point review (24/04/2026) | Revisão completa do Risk Register com atualização de status de todos os riscos | VMO Autônomo + GP Interno |
| Semana 5 — antes da apresentação final (07/05/2026) | Revisão final dos riscos ativos para inclusão no relatório de encerramento da Fase 1 | VMO Autônomo + GP Interno |
| Início da Fase 2 (~11/05/2026) | Abertura de novo ciclo de identificação de riscos específicos da fase RFP | Pedro Perigo (novo ciclo VMO) |

---

## 7. Riscos Materializados (Issues) — Situação Atual (05/04/2026)

Os itens abaixo deixaram de ser riscos e tornaram-se **problemas ativos (issues)**, pois sua condição de gatilho já se confirmou:

| ID Issue | Descrição | Origem | Impacto | Ação Imediata | Responsável |
|---|---|---|---|---|---|
| I-001 | Agenda da Semana 1 não confirmada em 05/04/2026 (dia anterior ao início) | Materialização do R-001 | CRÍTICO — workshops iniciam amanhã | Contato imediato com Wallacy Lima e Marcelo Silveira | Marcelo Silveira |
| I-002 | Participantes internos GAB para os workshops não foram designados | Materialização do R-002 (parcial) | ALTO — sem designação, workshops ocorrem sem representação adequada | Escalada para Sponsors hoje | Sponsors + Marcelo Silveira |
| I-003 | GP Interno atua de forma interina sem previsão de titularização | Materialização do R-004 (parcial) | MÉDIO — risco de continuidade | Confirmar até 07/04/2026 (CB-01) | Diretoria GAB |

---

*Documento elaborado por Pedro Perigo — Analista de Riscos, VMO Autônomo*
*Run ID: 2026-04-05-173000 | Etapa: 8/12 — Plano de Riscos | ID Projeto: PROJ-2026-003*
