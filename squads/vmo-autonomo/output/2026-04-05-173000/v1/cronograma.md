# Planejamento de Prazo — Caminhos Estratégicos do ERP GAB

**ID Projeto:** PROJ-2026-003
**Versão:** 1.0
**Data:** 05/04/2026
**Elaborado por:** Carlos Cronograma — Planejador de Prazo (VMO Autônomo)
**Run ID:** 2026-04-05-173000
**Baseline de Prazo:** v1.0 — 05/04/2026

---

## 1. Premissas de Estimativa

| # | Premissa | Impacto no Cronograma |
|---|---|---|
| P01 | O cronograma da Fase 1 (Software Selection, 5 semanas) foi definido em contrato KPMG e é fixo — o VMO o adota como baseline sem alteração | Fase 1 não pode ser renegociada unilateralmente pelo GAB |
| P02 | A Fase 2 (RFP) inicia em paralelo à Semana 5 da Fase 1, conforme proposta KPMG | Sobreposição de 1 semana entre as fases |
| P03 | Dias úteis considerados: segunda a sexta, exceto feriados nacionais — não foram identificados feriados nacionais no período 06/04 a 08/05/2026 | Sem impacto na Fase 1; verificar 01/05 (Dia do Trabalho — feriado nacional) na Semana 4/5 |
| P04 | A participação das áreas internas do GAB nos workshops (Semanas 1 e 2) é pressuposta como confirmada — sem confirmação de participantes até 05/04/2026 (LAC-005 e LAC-006 em aberto) | Risco de atraso nos workshops caso áreas não estejam disponíveis |
| P05 | O Kick Off Executivo ocorrerá em Abril/2026 — data exata não confirmada; estimado para Semana 1 ou 2 | Buffer de 1 semana incluído antes da entrega final para acomodar eventual realinhamento executivo |
| P06 | Duração estimada das atividades VMO (documentação de iniciação): 2 dias úteis por artefato principal | Estimativa por analogia com projetos similares de nível de complexidade ALTA no portfólio VMO |
| P07 | A data 01/05/2026 (Semana 4) é feriado nacional. A Semana 4 tem 4 dias úteis efetivos (27/04 a 30/04 + retorno 04/05) | Os workshops da Semana 4 devem ser planejados para 27–30/04, com 04/05 como início da Semana 5 |

---

## 2. WBS — Estrutura Analítica do Projeto

### Nível 1 — Projeto Caminhos Estratégicos do ERP GAB

```
PROJ-2026-003 Caminhos Estratégicos do ERP GAB
│
├── 1. GESTÃO DO PROJETO (VMO Autônomo)
│   ├── 1.1 Iniciação do Projeto
│   │   ├── 1.1.1 Coleta e estruturação da demanda (Iara Inbound)
│   │   ├── 1.1.2 Qualificação da demanda (Felipe Filtro)
│   │   ├── 1.1.3 Elaboração do TAP e PM Canvas (Diana Documento)
│   │   ├── 1.1.4 Especificação de Requisitos PMO / ERF (Rafael Requisito)
│   │   ├── 1.1.5 Planejamento de Prazo / WBS e Cronograma (Carlos Cronograma)
│   │   ├── 1.1.6 Plano de Riscos (Pedro Perigo)
│   │   ├── 1.1.7 Framework de KPIs (Marcela Métrica)
│   │   └── 1.1.8 Status Report Inicial (Sara Status)
│   │
│   ├── 1.2 Monitoramento e Controle (durante toda a Fase 1)
│   │   ├── 1.2.1 Flash Reports diários (S0 a S5) — 25 entregas
│   │   ├── 1.2.2 Status Reports semanais (S1 a S5) — 5 entregas (quarta-feira)
│   │   ├── 1.2.3 Atualização do Registro de Riscos (semanal)
│   │   ├── 1.2.4 Controle de Issues (contínuo)
│   │   ├── 1.2.5 Controle de Mudanças de Escopo (demanda)
│   │   └── 1.2.6 Comitê Executivo — preparação de insumos (quinta-feira semanal)
│   │
│   ├── 1.3 Gestão de Fornecedores (KPMG)
│   │   ├── 1.3.1 Gestão do contrato KPMG — acompanhamento de entregas
│   │   ├── 1.3.2 Revisão e aceite de entregáveis KPMG por semana
│   │   ├── 1.3.3 Aprovação de faturas KPMG (conforme marcos contratuais)
│   │   └── 1.3.4 Planejamento e contratação da Fase 2 (RFP)
│   │
│   └── 1.4 Encerramento da Fase 1
│       ├── 1.4.1 Apresentação Final ao Comitê Executivo
│       ├── 1.4.2 Aprovação da recomendação de plataforma
│       ├── 1.4.3 Lições aprendidas e atualização de memória VMO
│       └── 1.4.4 Transição para Fase 2 (RFP)
│
├── 2. ASSESSMENT DE SELEÇÃO DE ERP — FASE 1 (KPMG + GAB)
│   ├── 2.1 Preparação e Kick Off
│   │   ├── 2.1.1 Kick Off Operacional (realizado 02/04/2026) ✓
│   │   ├── 2.1.2 Kick Off Executivo (Abril/2026 — data a confirmar)
│   │   └── 2.1.3 Setup do ambiente de trabalho e ferramentas KPMG
│   │
│   ├── 2.2 Entendimento de Processos — Semana 1 (06–10/04/2026)
│   │   ├── 2.2.1 Workshop: Manutenção / Frotas (VixPar)
│   │   ├── 2.2.2 Workshop: Suprimentos (VixPar + Holding)
│   │   ├── 2.2.3 Workshop: Finanças — parte 1 (Holding + VAB + VixPar)
│   │   └── 2.2.4 Workshop: Fiscal — parte 1 (Holding + VAB + VixPar)
│   │
│   ├── 2.3 Entendimento de Processos — Semana 2 (13–17/04/2026)
│   │   ├── 2.3.1 Workshop: RH / Departamento Pessoal / SESMT (VAB + VixPar)
│   │   ├── 2.3.2 Workshop: Finanças — continuação
│   │   └── 2.3.3 Workshop: Tecnologia (todas as entidades)
│   │
│   ├── 2.4 Análise e Definição de Aderências — Semana 3 (20–24/04/2026)
│   │   ├── 2.4.1 Consolidação dos mapeamentos AS-IS por área
│   │   ├── 2.4.2 Definição dos requisitos de aderência por plataforma (SAP, Oracle, TOTVS)
│   │   ├── 2.4.3 Aplicação do Score Model — pilares Estratégico e Produto
│   │   └── 2.4.4 Sessão de validação com GP e áreas (mid-point review)
│   │
│   ├── 2.5 Análise e Definição de Aderências — Semana 4 (27/04–01/05/2026*)
│   │   ├── 2.5.1 Aplicação do Score Model — pilares Tecnologia, Cliente, Financeiro, Operação
│   │   ├── 2.5.2 Consolidação das matrizes de aderência (3 plataformas × 7 áreas)
│   │   └── 2.5.3 Análise comparativa e ranking preliminar das plataformas
│   │
│   └── 2.6 Revisão Final e Apresentação — Semana 5 (04–08/05/2026)
│       ├── 2.6.1 Revisão do relatório final de recomendação
│       ├── 2.6.2 Preparação da apresentação executiva
│       ├── 2.6.3 Apresentação ao Comitê Executivo (data a confirmar na Semana 5)
│       └── 2.6.4 Entrega formal do relatório final à GAB
│
└── 3. RFP — FASE 2 (início em paralelo à Semana 5)
    ├── 3.1 Preparação do RFP (04–08/05/2026 — em paralelo à Semana 5)
    │   ├── 3.1.1 Definição dos fornecedores a convidar (baseado na recomendação Fase 1)
    │   └── 3.1.2 Elaboração do documento RFP
    │
    ├── 3.2 Condução do RFP (11/05–22/05/2026)
    │   ├── 3.2.1 Envio e briefing dos fornecedores
    │   ├── 3.2.2 Sessões de dúvidas com fornecedores
    │   └── 3.2.3 Recebimento e análise das propostas
    │
    └── 3.3 Análise, Decisão e Encerramento (25/05–06/06/2026)
        ├── 3.3.1 Avaliação das propostas recebidas
        ├── 3.3.2 Apresentação final ao Comitê Executivo
        └── 3.3.3 Decisão de seleção do fornecedor ERP

* Nota: 01/05/2026 é feriado nacional (Dia do Trabalho) — Semana 4 tem 4 dias úteis efetivos.
```

---

## 3. Cronograma Detalhado — Fase 1: Software Selection

### 3.1 Atividades VMO — Iniciação (já em execução)

| ID | Atividade | Início | Fim | Dur. | Resp. | Dep. | Status |
|---|---|---|---|---|---|---|---|
| VMO-01 | Coleta e estruturação da demanda | 05/04/2026 | 05/04/2026 | 1d | Iara Inbound | — | CONCLUÍDO ✓ |
| VMO-02 | Qualificação da demanda | 05/04/2026 | 05/04/2026 | 1d | Felipe Filtro | VMO-01 | CONCLUÍDO ✓ |
| VMO-03 | TAP + PM Canvas + Plano Geral | 05/04/2026 | 05/04/2026 | 1d | Diana Documento | VMO-02 | CONCLUÍDO ✓ |
| VMO-04 | ERF — Especificação de Requisitos | 05/04/2026 | 05/04/2026 | 1d | Rafael Requisito | VMO-02 | CONCLUÍDO ✓ |
| VMO-05 | WBS + Cronograma | 05/04/2026 | 05/04/2026 | 1d | Carlos Cronograma | VMO-03/04 | EM ANDAMENTO |
| VMO-06 | Plano de Riscos | 05/04/2026 | 05/04/2026 | 1d | Pedro Perigo | VMO-05 | PREVISTO |
| VMO-07 | Framework de KPIs | 05/04/2026 | 05/04/2026 | 1d | Marcela Métrica | VMO-05 | PREVISTO |
| VMO-08 | Status Report Inicial (Semana 0) | 05/04/2026 | 05/04/2026 | 1d | Sara Status | VMO-06/07 | PREVISTO |
| VMO-09 | Revisão de Qualidade (Vera Veredito) | 05/04/2026 | 05/04/2026 | 1d | Vera Veredito | VMO-08 | PREVISTO |
| VMO-10 | Checkpoint Final — Aprovar Documentação | 05/04/2026 | 05/04/2026 | 1d | GP Interno | VMO-09 | PREVISTO |

### 3.2 Atividades VMO — Monitoramento Semanal

| Semana | Flash Reports | Status Report | Comitê Executivo | Atualização Riscos |
|---|---|---|---|---|
| **Semana 1** (06–10/04) | 5 reports (seg–sex) | 09/04/2026 (quarta) | 10/04/2026 (quinta) | 10/04/2026 |
| **Semana 2** (13–17/04) | 5 reports | 16/04/2026 (quarta) | 17/04/2026 (quinta) | 17/04/2026 |
| **Semana 3** (20–24/04) | 5 reports | 23/04/2026 (quarta) | 24/04/2026 (quinta) | 24/04/2026 |
| **Semana 4** (27–30/04) | 4 reports (seg–qui) | 29/04/2026 (quarta) | 30/04/2026 (quinta) | 30/04/2026 |
| **Semana 5** (04–08/05) | 5 reports | 06/05/2026 (quarta) | 07 ou 08/05/2026 | 08/05/2026 |

### 3.3 Atividades KPMG + GAB — Assessment

| ID | Atividade | Período | Dur. | Facilitador | Participantes GAB | Entregável |
|---|---|---|---|---|---|---|
| KMP-01 | Kick Off Operacional | 02/04/2026 | 1d | Wallacy Lima | Marcelo Silveira + Áreas | Ata de Kick Off |
| KMP-02 | Kick Off Executivo | Abr/2026 (a confirmar) | 1d | Rodrigo Figaro | Sponsors + GP | Apresentação executiva |
| KMP-03 | Workshop: Manutenção/Frotas | S1 (06–10/04) | 1–2d | KPMG Especialista | VixPar — TBD (LAC-005) | Documentação AS-IS Manutenção |
| KMP-04 | Workshop: Suprimentos | S1 (06–10/04) | 1–2d | KPMG Especialista | VixPar + Holding — TBD | Documentação AS-IS Suprimentos |
| KMP-05 | Workshop: Finanças — Parte 1 | S1 (06–10/04) | 2d | KPMG Especialista | Holding + VAB + VixPar — TBD | Documentação AS-IS Finanças |
| KMP-06 | Workshop: Fiscal — Parte 1 | S1 (06–10/04) | 1–2d | KPMG Especialista | Holding + VAB + VixPar — TBD | Documentação AS-IS Fiscal |
| KMP-07 | Workshop: RH/DP/SESMT | S2 (13–17/04) | 2d | KPMG Especialista | VAB + VixPar — TBD | Documentação AS-IS RH/DP/SESMT |
| KMP-08 | Workshop: Finanças — Continuação | S2 (13–17/04) | 1d | KPMG Especialista | Holding + VAB + VixPar — TBD | Complemento AS-IS Finanças |
| KMP-09 | Workshop: Tecnologia | S2 (13–17/04) | 1–2d | KPMG Especialista | DTI GAB — TBD | Documentação AS-IS Tecnologia |
| KMP-10 | Consolidação dos mapeamentos AS-IS | S3 (20–24/04) | 3d | KPMG Equipe | Marcelo Silveira (revisão) | Documentos AS-IS consolidados |
| KMP-11 | Definição de requisitos de aderência | S3 (20–24/04) | 2d | KPMG Equipe | GP + Áreas-chave | Requisitos de aderência por plataforma |
| KMP-12 | Aplicação Score Model — Pilares 1-2 | S3 (20–24/04) | 2d | KPMG Equipe | — | Score parcial: Estratégico + Produto |
| KMP-13 | Mid-point review com GP + Sponsors | S3 (24/04) | 1d | Wallacy Lima | Sponsors + GP | Validação do andamento — Semana 3 |
| KMP-14 | Aplicação Score Model — Pilares 3-6 | S4 (27–30/04) | 3d | KPMG Equipe | — | Score completo: Tecnologia+Cliente+Financeiro+Operação |
| KMP-15 | Consolidação matrizes de aderência | S4 (27–30/04) | 2d | KPMG Equipe | Marcelo Silveira (revisão) | Matrizes: 3 plataformas × 7 áreas |
| KMP-16 | Análise comparativa e ranking | S4 (30/04) | 1d | KPMG Equipe | — | Ranking preliminar das plataformas |
| KMP-17 | Revisão do relatório final | S5 (04–06/05) | 2d | KPMG + GP | Marcelo Silveira | Relatório final revisado |
| KMP-18 | Preparação da apresentação executiva | S5 (04–07/05) | 2d | Rodrigo Figaro + Wallacy | GP + Sponsors | Apresentação para Comitê |
| KMP-19 | **Apresentação Final ao Comitê Executivo** | S5 (07 ou 08/05) | 1d | Rodrigo Figaro | Sponsors + GP | Recomendação de plataforma |
| KMP-20 | Entrega formal do relatório final | S5 (08/05/2026) | 1d | KPMG | Marcelo Silveira | Relatório Final — ENTREGÁVEL PRINCIPAL |

---

## 4. Cronograma Macro — Fases 1 e 2

```
ABR/2026                                                    MAI/2026        JUN/2026
W0       W1           W2           W3           W4          W5          W6-W8
30/03    06/04        13/04        20/04        27/04        04/05       11/05-06/06

[==Iniciação VMO==]
[== S1: Workshops ==]     [== S2: Workshops ==]
                          [== S3: Aderências ==][== S4: Aderências ==]
                                                             [== S5: Revisão+Apres. ==]
                                                             [===== Fase 2 RFP ====================================]

Marcos:
▼ 02/04  Kick Off Operacional (✓)
▽ Abr    Kick Off Executivo (data a confirmar)
▼ 05/04  Documentação Iniciação VMO (hoje)
▼ 09/04  1º Status Report
▼ 08/05  Entrega Final Software Selection ← MARCO PRINCIPAL FASE 1
▼ ~08/05 Início Fase 2 (RFP)
▼ ~06/06 Entrega Final RFP ← MARCO PRINCIPAL FASE 2
```

---

## 5. Marcos Principais

| ID | Marco | Data | Tipo | Status |
|---|---|---|---|---|
| M01 | Kick Off Operacional KPMG | 02/04/2026 | Fase | REALIZADO ✓ |
| M02 | Documentação de Iniciação VMO concluída | 05/04/2026 | Gestão | EM ANDAMENTO |
| M03 | Kick Off Executivo | Abril/2026 (TBD) | Governança | PENDENTE |
| M04 | Conclusão dos Workshops Semana 1 | 10/04/2026 | Fase | PREVISTO |
| M05 | Conclusão dos Workshops Semana 2 | 17/04/2026 | Fase | PREVISTO |
| M06 | Mid-Point Review (Semana 3) | 24/04/2026 | Revisão | PREVISTO |
| M07 | Consolidação das Matrizes de Aderência | 30/04/2026 | Entregável | PREVISTO |
| M08 | **Entrega Final — Relatório Software Selection** | **08/05/2026** | **Entregável Principal** | PREVISTO |
| M09 | Aprovação da Recomendação pelo Comitê Executivo | 07 ou 08/05/2026 | Decisão | PREVISTO |
| M10 | Início da Fase 2 (RFP) | ~05/05/2026 | Fase | PREVISTO |
| M11 | **Entrega Final — RFP** | **~06/06/2026** | **Entregável Principal Fase 2** | PREVISTO |

---

## 6. Caminho Crítico

O caminho crítico da Fase 1 é determinado pela sequência de workshops e entregas KPMG — todas as atividades desta sequência têm folga zero:

```
Kick Off Op. (02/04)
    → Workshop S1: Manutenção (06–07/04)
    → Workshop S1: Suprimentos (07–08/04)
    → Workshop S1: Finanças P1 (08–09/04)
    → Workshop S1: Fiscal P1 (09–10/04)
    → Workshop S2: RH/DP/SESMT (13–14/04)
    → Workshop S2: Finanças (cont.) (15/04)
    → Workshop S2: Tecnologia (16–17/04)
    → Consolidação AS-IS (20–22/04)
    → Definição requisitos aderência (23–24/04)
    → Score Model Pilares 1-2 (22–24/04)
    → Score Model Pilares 3-6 (27–29/04)
    → Consolidação matrizes (28–30/04)
    → Análise comparativa (30/04)
    → Revisão relatório final (04–06/05)
    → Apresentação executiva (07–08/05)
    → ENTREGA FINAL (08/05/2026) ← FIM CAMINHO CRÍTICO
```

**Fator de risco crítico:** Qualquer atraso nos workshops da Semana 1 (LAC-006 — agenda não confirmada; LAC-005 — participantes não designados) propaga diretamente para a data de entrega final de 08/05/2026. Não há folga disponível no caminho crítico.

**Atividades com folga (fora do caminho crítico):**
- Kick Off Executivo (data flexível em Abril — não impacta entrega da Fase 1)
- Atividades VMO de monitoramento (podem ser recuperadas sem impacto na entrega KPMG)
- Início da Fase 2 (pode atrasar 1–2 dias sem comprometer o planejamento de 4 semanas)

---

## 7. Cronograma Fase 2 — RFP (Planejamento Preliminar)

| Semana | Período | Atividade | Entregável |
|---|---|---|---|
| RFP S0 | 04–08/05/2026 | Preparação do RFP + seleção de fornecedores convidados | Documento RFP draft |
| RFP S1 | 11–15/05/2026 | Envio do RFP aos fornecedores + briefing | RFP enviado + ata de briefing |
| RFP S2 | 18–22/05/2026 | Sessões de dúvidas + prazo para recebimento de propostas | Propostas recebidas |
| RFP S3 | 25–29/05/2026 | Análise e avaliação das propostas recebidas | Matriz de avaliação RFP |
| RFP S4 | 01–06/06/2026 | Apresentação final + decisão + encerramento | Relatório final RFP + decisão formal |

**Marco:** Entrega final RFP e decisão de fornecedor → ~06/06/2026

---

## 8. Buffer de Contingência

**Buffer explícito calculado:**

| Fase | Prazo Total (dias úteis) | Buffer 15% | Buffer em Dias | Uso |
|---|---|---|---|---|
| Fase 1 — Software Selection | ~25 dias úteis (06/04 a 08/05) | 15% | ~4 dias | Reserva de gestão para recuperação de atrasos em workshops |
| Fase 2 — RFP | ~20 dias úteis (11/05 a 06/06) | 15% | ~3 dias | Reserva para atrasos em respostas de fornecedores |

**Política de uso do buffer:**
- O buffer NÃO está distribuído nas atividades individuais
- O buffer É gerenciado centralmente pelo GP Interno (Marcelo Silveira)
- Uso do buffer deve ser formalmente registrado no Status Report da semana em que ocorrer
- Uso de mais de 50% do buffer ativa alerta amarelo no semáforo de cronograma
- Uso de 100% do buffer ativa alerta vermelho e requer revisão do baseline com Sponsors

**Nota:** Dado que a Fase 1 tem prazo fixo em contrato (5 semanas terminando ~08/05/2026) e o caminho crítico tem folga zero, o buffer de contingência neste projeto funciona principalmente como reserva para as atividades VMO de monitoramento e documentação — não como folga para os workshops KPMG, que seguem cronograma da consultoria.

---

## 9. Disponibilidade da Equipe — Premissas

| Recurso | Disponibilidade Assumida | Observação |
|---|---|---|
| Marcelo Silveira (GP Interno) | 60–80% — dedicação parcial ao projeto | Atua de forma interina; pode ter outras demandas do PMO |
| Equipe KPMG (22 pessoas) | 100% alocados no projeto conforme contrato | Confirmado em contrato |
| Sponsors (3 executivos) | Disponíveis para Comitê Executivo semanal (quinta) | ~2h/semana por Sponsor |
| Áreas internas GAB (workshops) | A confirmar por área — LAC-005 em aberto | Risco de conflito com operação cotidiana |
| VMO Autônomo | Execução dos artefatos de gestão conforme pipeline | Já em execução |

---

## 10. Desvios do Cronograma — Situação Atual (05/04/2026)

| Situação | Avaliação |
|---|---|
| O projeto iniciou em 02/04/2026 (Kick Off Operacional) conforme planejado | ✓ SEM DESVIO |
| A documentação VMO de iniciação está sendo produzida em 05/04/2026 — 3 dias após o Kick Off | ✓ DENTRO DO ESPERADO — iniciação VMO retroativa ao Kick Off |
| Semana 1 de workshops inicia em 06/04/2026 — amanhã | ⚠️ AGENDA NÃO CONFIRMADA (LAC-006) — risco de impacto nos workshops |
| Participantes internos GAB para workshops não foram designados | ⚠️ LAC-005 EM ABERTO — ação urgente requerida |
| Data do Kick Off Executivo não confirmada | ⚠️ LAC-001 EM ABERTO — não está no caminho crítico, mas deve ser confirmado |

**SPI Atual (Schedule Performance Index):** 1,0 (no baseline) — projeto sem desvio de prazo na data de 05/04/2026.

---

*Documento elaborado por Carlos Cronograma — VMO Autônomo*
*Run ID: 2026-04-05-173000 | Etapa: 7/12 — Criar Cronograma | ID Projeto: PROJ-2026-003*
