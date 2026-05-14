# FRAMEWORK DE KPIs — Caminhos Estratégicos do ERP GAB
**Versão:** 1.0 | **Data:** 2026-05-14
**Projeto:** PROJ-2026-003 | **GP:** Marcelo Silveira (interino)
**Responsável pelo Framework:** Marcela Métrica — Monitora de Performance

---

> **Princípio-mestre:** Todo KPI tem meta numérica, limite de alerta e frequência de coleta definidos. Nenhuma afirmação sobre saúde do projeto é aceita sem número. Anomalias (desvio > 25% em qualquer KPI crítico) são escaladas imediatamente — nunca no próximo ciclo.

---

## KPIs de Desempenho do Projeto (EVM)

> **BAC Total Fase 1:** R$ 1.010.000 (R$ 930.000 KPMG + R$ 80.000 overhead interno)
> **Duração:** 35 dias corridos (02/04/2026 a 08/05/2026)
> **Data de referência deste framework:** 2026-05-14 (pós encerramento — semana 6)

| KPI | Fórmula | Descrição | Baseline (t=0) | Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|---------|-----------|----------------|------|-----------|-----------|------------|-------------|
| **EV** (Earned Value) | Σ (% conclusão × BAC por entregável) | Valor do trabalho efetivamente concluído, medido por entregáveis aprovados | R$ 0 | R$ 1.010.000 ao M7 | EV < PV em > 10% | EV < PV em > 25% | Semanal (toda sexta) | GP |
| **PV** (Planned Value) | BAC × (% cronograma decorrido) | Valor do trabalho que deveria estar concluído conforme baseline | R$ 0 → R$ 1.010.000 (linear por marco) | Aderência ao PV baseline (ver Seção 4) | — | — | Semanal | GP |
| **AC** (Actual Cost) | Σ horas × tarifa + despesas diretas | Custo real incorrido até a data de medição | R$ 0 | ≤ R$ 1.010.000 | AC > EV (CPI < 1,00) | AC > PV + 20% | Semanal | GP / Financeiro |
| **CPI** (Cost Performance Index) | EV ÷ AC | Eficiência de custo: quanto de valor é gerado por cada real gasto | 1,00 (baseline) | ≥ 1,00 | 0,90 ≤ CPI < 1,00 | CPI < 0,90 | Semanal | GP |
| **SPI** (Schedule Performance Index) | EV ÷ PV | Eficiência de prazo: quanto do trabalho planejado foi concluído | 1,00 (baseline) | ≥ 1,00 | 0,90 ≤ SPI < 1,00 | SPI < 0,90 | Semanal | GP |
| **CV** (Cost Variance) | EV − AC | Variação absoluta de custo (positivo = abaixo do orçamento) | R$ 0 | ≥ R$ 0 | CV entre −R$ 50.500 e R$ 0 (−5% BAC) | CV < −R$ 101.000 (−10% BAC) | Semanal | GP |
| **SV** (Schedule Variance) | EV − PV | Variação absoluta de prazo em valor monetário | R$ 0 | ≥ R$ 0 | SV entre −R$ 50.500 e R$ 0 (−5% BAC) | SV < −R$ 101.000 (−10% BAC) | Semanal | GP |
| **EAC** (Estimate at Completion) | BAC ÷ CPI | Previsão de custo total ao término, dada a eficiência atual | R$ 1.010.000 | ≤ R$ 1.010.000 | R$ 1.010.001 – R$ 1.060.500 (+5%) | > R$ 1.111.000 (+10%) | Semanal | GP |
| **ETC** (Estimate to Complete) | EAC − AC | Custo restante projetado para concluir o projeto | R$ 1.010.000 (t=0) | ≤ BAC − AC | ETC > (BAC − AC) × 1,05 | ETC > (BAC − AC) × 1,10 | Semanal | GP |
| **VAC** (Variance at Completion) | BAC − EAC | Variação total projetada ao encerramento (positivo = dentro do orçamento) | R$ 0 | ≥ R$ 0 | −R$ 50.500 ≤ VAC < R$ 0 | VAC < −R$ 101.000 | Mensal (M5, M7) | GP |
| **TCPI** (To-Complete Performance Index) | (BAC − EV) ÷ (BAC − AC) | CPI necessário para o restante do trabalho atingir o BAC | 1,00 | ≤ 1,10 | 1,10 < TCPI ≤ 1,20 | TCPI > 1,20 | Semanal | GP |

**Regra de Escalonamento EVM:** Se CPI < 0,90 **ou** SPI < 0,90, GP emite alerta imediato ao Comitê Executivo dentro de 24 horas — não aguarda o próximo Flash Report.

---

## KPIs de Resultado (derivados dos critérios de sucesso do TAP)

> Estes KPIs medem se o projeto entregou **valor de negócio**, não apenas esforço. Cada um está rastreado a um critério de sucesso do TAP (CS-1 a CS-6).

### CS-1 — Recomendação de Plataforma ERP com Score Model Documentado

| KPI | Descrição | Método de Medição | Baseline | 🟢 Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|-----------|-------------------|----------|---------|-----------|-----------|------------|-------------|
| **KR-1.1** Entrega da Recomendação no Prazo | Recomendação ERP entregue até 08/05/2026 com Score Model por pilar | Verificação da data de entrega e checklist de conteúdo (pilar a pilar) | Não entregue | Entregue até 08/05/2026 com 100% dos pilares documentados | Entregue até 08/05 porém com < 100% dos pilares | Não entregue até 08/05/2026 | M6 (08/05) e M7 | GP + KPMG |
| **KR-1.2** Completude do Score Model | Número de pilares avaliados no Score Model / total de pilares definidos | Checklist de pilares do Score Model vs. planejado | 0 pilares | 100% dos pilares (meta: ≥ 6 pilares) | 80%–99% dos pilares | < 80% dos pilares | M5 (01/05) | KPMG Lead |
| **KR-1.3** Plataformas na Shortlist | Número de plataformas ERP avaliadas e posicionadas no Score Model | Contagem de registros no Score Model | 0 | ≥ 3 plataformas avaliadas | 2 plataformas | 1 ou nenhuma plataforma | M5 (01/05) | KPMG Lead |

### CS-2 — Cobertura de Workshops (100% das áreas funcionais × 3 entidades)

| KPI | Descrição | Método de Medição | Baseline | 🟢 Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|-----------|-------------------|----------|---------|-----------|-----------|------------|-------------|
| **KR-2.1** Taxa de Cobertura de Workshops | (Nº de workshops realizados + aprovados) ÷ (Nº total planejado de workshops) | Ata de presença + formulário de validação por área/entidade | 0% | 100% (todas as áreas × todas as entidades) | 85%–99% | < 85% | Semanal (M3, M4) | GP |
| **KR-2.2** Cobertura por Entidade | Nº de áreas cobertas por entidade ÷ total de áreas mapeadas para cada entidade | Mapa de cobertura entidade × área (planilha de acompanhamento) | 0% | 100% em cada uma das 3 entidades individualmente | ≥ 85% em todas as 3 | < 85% em qualquer entidade | M3, M4 | GP |
| **KR-2.3** Taxa de Presença nos Workshops | Nº de participantes presentes ÷ Nº de participantes convocados | Lista de presença por workshop | 0% | ≥ 80% de presença por workshop | 60%–79% de presença | < 60% de presença (gatilho R-001) | Por workshop | GP |
| **KR-2.4** Engajamento nos Workshops (R-001) | Workshops encerrados com consenso e ata validada ÷ workshops realizados | Ata assinada vs. não assinada | 0% | 100% das atas validadas no prazo | 85%–99% | < 85% (R-001 ativado) | M3, M4 | GP |

### CS-3 — Aprovação da Recomendação pelos 3 Sponsors

| KPI | Descrição | Método de Medição | Baseline | 🟢 Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|-----------|-------------------|----------|---------|-----------|-----------|------------|-------------|
| **KR-3.1** Aprovação dos Sponsors | Nº de sponsors que aprovaram a recomendação ÷ 3 sponsors | Registro de aprovação formal (ata ou e-mail) na apresentação final | 0/3 | 3/3 sponsors aprovam | 2/3 aprovam (1 pendente) | 1/3 ou 0/3 aprovam (gatilho R-008) | M6 (08/05) | GP |
| **KR-3.2** Presença dos Sponsors na Apresentação Final | Nº de sponsors presentes na apresentação final | Lista de presença da reunião M6 | 0/3 | 3/3 presentes | 2/3 presentes | 1/3 ou menos (R-008 ativado imediatamente) | M6 (08/05) | GP |
| **KR-3.3** Ressalvas Formais Abertas | Nº de ressalvas ou objeções formais não respondidas após a apresentação | Log de decisões / ata de aprovação | 0 | 0 ressalvas em aberto | 1–2 ressalvas com prazo acordado | ≥ 3 ressalvas ou 1 sem prazo | M7 (08/05) | GP + KPMG |

### CS-4 — Score Model com ≥ 70% de Critérios Objetivos

| KPI | Descrição | Método de Medição | Baseline | 🟢 Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|-----------|-------------------|----------|---------|-----------|-----------|------------|-------------|
| **KR-4.1** Taxa de Objetividade do Score Model (R-003) | Nº de critérios derivados de dados objetivos ÷ total de critérios do Score Model | Auditoria de cada critério: fonte = dado verificável (benchmark, demo, requisito técnico) vs. percepção | 0% | ≥ 70% | 60%–69% (pré-alerta R-003) | < 60% (R-003 ativado) | M5 (01/05) | KPMG Lead + GP |
| **KR-4.2** Critérios com Fonte Documentada | Nº de critérios com fonte de evidência registrada ÷ total de critérios | Verificação de campo "fonte" no Score Model | 0% | 100% dos critérios com fonte | 85%–99% | < 85% | M5 (01/05) | KPMG Lead |

### CS-5 — Pacote de Insumos para RFP Entregue em 08/05/2026

| KPI | Descrição | Método de Medição | Baseline | 🟢 Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|-----------|-------------------|----------|---------|-----------|-----------|------------|-------------|
| **KR-5.1** Entrega do Pacote RFP no Prazo | Pacote com shortlist + critérios preliminares de RFP entregue até 08/05/2026 | Verificação do documento no repositório + aceite do cliente | Não entregue | Entregue até 08/05/2026 | Entregue até 09/05 (1 dia de tolerância) | Não entregue até 09/05/2026 | M7 (08/05) | KPMG Lead + GP |
| **KR-5.2** Completude do Pacote RFP | Nº de seções obrigatórias presentes ÷ total definido no escopo KPMG | Checklist contratual: shortlist, critérios técnicos, critérios funcionais, critérios de custo, roadmap de próximos passos | 0% | 100% das seções | 85%–99% | < 85% | M7 (08/05) | KPMG Lead |

### CS-6 — NPS dos Sponsors ≥ 7/10

| KPI | Descrição | Método de Medição | Baseline | 🟢 Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|-----------|-------------------|----------|---------|-----------|-----------|------------|-------------|
| **KR-6.1** NPS dos Sponsors (nota individual) | Nota de satisfação de cada sponsor (0–10) na pesquisa de encerramento | Formulário de pesquisa pós-apresentação final (3 respostas individuais) | N/A (t=0) | ≥ 7,0/10 em todas as 3 notas individuais | Média ≥ 7,0 mas pelo menos 1 nota = 6 | Média < 7,0 ou qualquer nota ≤ 5 | M7 (encerramento) | GP |
| **KR-6.2** NPS Médio dos Sponsors | Média aritmética das 3 notas de satisfação | Cálculo após coleta das 3 notas | N/A | ≥ 7,0 | 6,0–6,9 | < 6,0 | M7 (encerramento) | GP |
| **KR-6.3** Taxa de Resposta à Pesquisa | Nº de sponsors que responderam ÷ 3 | Confirmação de respostas no formulário | 0/3 | 3/3 | 2/3 | 1/3 ou menos | M7 (encerramento) | GP |

---

## KPIs de Processo e Governança

> Estes KPIs monitoram a **qualidade da execução** do projeto — se os processos de gestão estão sendo seguidos. Baixo desempenho de processo é preditor de problemas em resultado.

| KPI | Descrição | Meta | 🟡 Alerta | 🔴 Crítico | Frequência | Responsável |
|-----|-----------|------|-----------|-----------|------------|-------------|
| **KP-1** Flash Report Entregue no Prazo | Flash Reports entregues toda sexta-feira dentro do prazo / total previsto | 100% (5/5 reports) | 1 report atrasado | ≥ 2 reports atrasados ou Flash Report ausente | Semanal (sexta) | GP |
| **KP-2** Comitê Executivo Realizado | Comitês Executivos realizados conforme agenda / total agendado | 100% dos comitês realizados | 1 comitê remarcado com ≤ 48h antecedência | 1 comitê cancelado sem reagendamento | Quinzenal / por marco | GP + Sponsors |
| **KP-3** Riscos Monitorados e Atualizados | Nº de riscos com status atualizado no período / total de riscos ativos no registro | 100% dos riscos ativos atualizados semanalmente | 1–2 riscos sem atualização por semana | ≥ 3 riscos sem atualização ou risco CRÍTICO/ALTO sem atualização | Semanal | GP (Pedro Perigo — input) |
| **KP-4** Ações de Mitigação Executadas | Nº de ações de mitigação executadas / total planejadas para o período | ≥ 90% | 75%–89% | < 75% | Semanal | GP |
| **KP-5** Decisões Formalizadas no Log | Decisões relevantes registradas no Log de Decisões / decisões tomadas estimadas | 100% | 1–2 decisões sem registro | ≥ 3 decisões sem registro ou decisão de sponsor não registrada | Por reunião | GP |
| **KP-6** Entregas Aceitas Formalmente | Nº de entregáveis com aceite formal do cliente / total entregues | 100% | 1 entregável sem aceite até 3 dias | ≥ 2 sem aceite ou entregável final sem aceite | Por entregável | GP + KPMG |
| **KP-7** Atas de Workshop Entregues no Prazo | Atas entregues em até 24h após o workshop / total de workshops | 100% | 1 ata com atraso de 25–48h | ≥ 2 atas com atraso > 48h | Por workshop | KPMG Analista |
| **KP-8** Desvio de Escopo (Change Requests) | Nº de solicitações de mudança de escopo formalizadas vs. absorvidas informalmente | 0 mudanças absorvidas informalmente | 1 mudança informal identificada | ≥ 2 mudanças absorvidas sem CR formal | Semanal | GP |

---

## Configuração EVM

### 4.1 Parâmetros Fundamentais

| Parâmetro | Valor |
|-----------|-------|
| **BAC (Budget at Completion)** | R$ 1.010.000 |
| BAC — Contrato KPMG (escopo externo) | R$ 930.000 |
| BAC — Overhead Interno Estimado | R$ 80.000 |
| **Data de Início** | 02/04/2026 |
| **Data de Término Planejada** | 08/05/2026 |
| **Duração** | 35 dias corridos (5 semanas) |
| **Método de Baseline PV** | Marcos ponderados pelo valor dos entregáveis |
| **Frequência de Medição EV** | Semanal (toda sexta-feira) |
| **Precisão mínima para CPI/SPI** | 2 casas decimais |

### 4.2 PV Baseline por Marco

> O PV é distribuído proporcionalmente ao peso de cada marco no conjunto de entregáveis do assessment. Não é distribuição linear — reflete a concentração de valor nas fases analíticas.

| Marco | Entregáveis Associados | Data Planejada | PV Acumulado | % BAC Acumulado |
|-------|------------------------|----------------|--------------|-----------------|
| **Kick-off / Mobilização** | Plano de projeto, cronograma detalhado, mapa de workshops | 02/04/2026 | R$ 60.600 | 6% |
| **M3 — Entendimento Ciclo 1** | Atas de workshops Ciclo 1 (todas as áreas/entidades), diagnóstico preliminar Ciclo 1 | 10/04/2026 | R$ 252.500 | 25% |
| **M4 — Entendimento Ciclo 2** | Atas de workshops Ciclo 2, diagnóstico consolidado (todas as entidades), mapa de requisitos | 17/04/2026 | R$ 454.500 | 45% |
| **Score Model Draft** | Score Model versão rascunho, critérios objetivos categorizados, primeiro round de avaliação das plataformas | 24/04/2026 | R$ 656.500 | 65% |
| **M5 — Score Model Consolidado** | Score Model final validado, shortlist definitiva, evidências por critério, relatório de análise | 01/05/2026 | R$ 858.500 | 85% |
| **M6 — Aprovação da Recomendação** | Apresentação final aos sponsors, ata de aprovação, pacote RFP | 08/05/2026 | R$ 969.600 | 96% |
| **M7 — Encerramento Fase 1** | Relatório de encerramento, pesquisa NPS, repositório de documentos, handoff | 08/05/2026 | R$ 1.010.000 | 100% |

### 4.3 Método de Medição de EV por Tipo de Entregável

> A escolha do método de medição de EV é crítica em projetos de assessment/consultoria, pois o trabalho intelectual é difícil de mensurar por esforço. As regras abaixo eliminam a subjetividade.

| Tipo de Entregável | Exemplos no Projeto | Método de EV | Regra de Acreditação | Evidência Necessária |
|--------------------|---------------------|-------------|---------------------|----------------------|
| **Workshops** | Workshops de entendimento por área/entidade | **Regra 0/100** | 0% antes do workshop; 100% somente após: (1) workshop realizado, (2) ata gerada, (3) ata validada pelo representante da área | Ata assinada ou e-mail de validação |
| **Diagnósticos e Análises** | Diagnóstico de processos, mapa de requisitos, análise de fit | **Regra 50/50** | 50% ao entregar o draft para revisão interna; 50% adicional após aceite formal do cliente/sponsor | E-mail de submissão do draft + aceite formal |
| **Score Model** | Score Model draft, Score Model final | **Regra 50/50** | 50% ao submeter o draft (todas as plataformas avaliadas em todos os pilares); 50% após validação e aprovação formal | Ata de revisão + aceite formal |
| **Relatórios Periódicos (Flash Reports)** | Flash Reports semanais | **Proporcional ao tempo (linear)** | EV = (semanas decorridas ÷ total de semanas) × BAC do entregável | Relatório publicado no repositório dentro do prazo |
| **Entregáveis Finais únicos** | Recomendação final, Pacote RFP, Relatório de Encerramento | **Regra 0/100** | 0% até entrega formal ao cliente; 100% somente após aceite formal documentado | Aceite formal por escrito (e-mail ou ata) |
| **Atividades de Gestão** | Plano de projeto, risk register, log de decisões | **Regra 0/100** | 0% durante elaboração; 100% após aprovação pelo GP e publicação no repositório | Documento versionado no repositório |
| **Apresentação Final** | Apresentação aos sponsors (M6) | **Regra 0/100** | 0% antes da reunião; 100% após realização da apresentação E aprovação formal pelos sponsors | Ata de aprovação com assinatura dos 3 sponsors |

### 4.4 Cálculo do EV — Exemplo Prático

```
Semana 3 (17/04/2026 — Marco M4):

Entregável: Workshop Área Financeira × Entidade A
  - Status: Realizado + Ata validada = 100% → EV = 100% × R$ 15.000 = R$ 15.000 ✓

Entregável: Score Model Draft
  - Status: Em elaboração (não submetido) = 0% → EV = R$ 0 ✗
  - (Mesmo com 80% do trabalho intelectual feito — sem entrega = sem EV)

Entregável: Flash Reports (semanas 1–3)
  - 3 semanas ÷ 5 semanas = 60% → EV = 60% × R$ 20.000 = R$ 12.000 ✓
```

> **Princípio:** O EV de um entregável intelectual é ZERO enquanto não há entrega verificável. Isso evita inflar o SPI com "trabalho em andamento" que não pode ser validado.

---

## Semáforo de Saúde

> O Semáforo de Saúde é atualizado **a cada Flash Report semanal**. É a síntese executiva do estado do projeto — uma linha por dimensão, sem espaço para ambiguidade. O status consolidado é determinado pela pior dimensão.

### 5.1 Definição das 5 Dimensões

| # | Dimensão | KPIs que a Compõem | Peso na Avaliação |
|---|----------|-------------------|-------------------|
| 1 | **Cronograma** | SPI, SV, marcos atingidos no prazo | 25% |
| 2 | **Custo** | CPI, CV, EAC vs. BAC, VAC | 25% |
| 3 | **Entregáveis** | KR-1 a KR-5 (cobertura, qualidade, pontualidade) | 25% |
| 4 | **Riscos** | KP-3, KP-4; status de R-001, R-003, R-008 | 15% |
| 5 | **Satisfação** | KR-6 (NPS), KR-3 (aprovação sponsors), KP-2 (comitês realizados) | 10% |

### 5.2 Tabela de Thresholds por Dimensão

| Dimensão | 🟢 Verde (Nominal) | 🟡 Amarelo (Atenção) | 🔴 Vermelho (Crítico) | Ação Requerida |
|----------|-------------------|--------------------|-----------------------|----------------|
| **1. Cronograma** | SPI ≥ 1,00 E todos os marcos no prazo | 0,90 ≤ SPI < 1,00 OU 1 marco com atraso ≤ 2 dias | SPI < 0,90 OU qualquer marco com atraso > 2 dias | 🔴: Alerta imediato ao Comitê; plano de recuperação em 24h |
| **2. Custo** | CPI ≥ 1,00 E EAC ≤ BAC | 0,90 ≤ CPI < 1,00 OU EAC até +5% BAC | CPI < 0,90 OU EAC > BAC + 5% | 🔴: Alerta ao Comitê; análise de causa raiz em 24h |
| **3. Entregáveis** | 100% dos entregáveis do período aceitos formalmente E todos os KRs no verde | 1 KR no amarelo OU 1 entregável com aceite pendente (≤ 3 dias) | ≥ 1 KR no vermelho OU entregável final não entregue | 🔴: Escalonamento imediato; mobilização de contingência |
| **4. Riscos** | Todos os riscos CRÍTICOS/ALTOS com mitigação ativa e status atual | R-001 ou R-003 ou R-008 com sinal de materialização parcial | Qualquer risco CRÍTICO/ALTO materializado sem plano de resposta ativo | 🔴: Reunião de crise em 4h; notificação formal aos sponsors |
| **5. Satisfação** | Feedback positivo nos comitês; NPS previsto ≥ 7 (quando disponível) | Feedback misto em comitê; NPS previsto 6–6,9; 1 sponsor ausente | Feedback negativo formal; NPS < 6 ou sponsor recusando aprovação | 🔴: Reunião individual com sponsor afetado em 24h |

### 5.3 Semáforo de Saúde — Template Semanal

```
╔═══════════════════════════════════════════════════════════════════╗
║     SEMÁFORO DE SAÚDE — PROJ-2026-003 | SEMANA: ___/5           ║
║     Data de referência: ___/___/2026                             ║
╠═══════════════════╦══════════╦═══════════════════════════════════╣
║ DIMENSÃO          ║ STATUS   ║ INDICADOR-CHAVE                   ║
╠═══════════════════╬══════════╬═══════════════════════════════════╣
║ 1. CRONOGRAMA     ║  [🟢🟡🔴] ║ SPI = ___ | Marco atual: ___     ║
║ 2. CUSTO          ║  [🟢🟡🔴] ║ CPI = ___ | EAC = R$ ___         ║
║ 3. ENTREGÁVEIS    ║  [🟢🟡🔴] ║ EV acumulado = R$ ___ (___% BAC) ║
║ 4. RISCOS         ║  [🟢🟡🔴] ║ R-001: ___ | R-003: ___ | R-008: ___ ║
║ 5. SATISFAÇÃO     ║  [🟢🟡🔴] ║ NPS: ___ | Aprovações: ___/3    ║
╠═══════════════════╩══════════╩═══════════════════════════════════╣
║ STATUS CONSOLIDADO: [🟢 NOMINAL / 🟡 ATENÇÃO / 🔴 CRÍTICO]      ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 5.4 Regra de Determinação do Status Consolidado

1. Se **qualquer dimensão estiver 🔴**: Status Consolidado = 🔴 CRÍTICO (independente das demais)
2. Se **nenhuma dimensão estiver 🔴 mas ≥ 2 estiverem 🟡**: Status Consolidado = 🟡 ATENÇÃO
3. Se **apenas 1 dimensão estiver 🟡**: Status Consolidado = 🟡 ATENÇÃO (com nota explicativa)
4. Se **todas as dimensões estiverem 🟢**: Status Consolidado = 🟢 NOMINAL

> **Regra de Escalonamento:** Status 🔴 CRÍTICO não pode permanecer por mais de 1 ciclo semanal sem plano de recuperação formal e comunicado documentado ao Comitê Executivo.

---

## Anexo A — Mapa de Rastreabilidade KPI × Critério de Sucesso do TAP

| Critério de Sucesso (TAP) | KPIs de Resultado | KPIs EVM Relacionados | Risco Associado |
|--------------------------|-------------------|-----------------------|-----------------|
| CS-1: Recomendação entregue com Score Model | KR-1.1, KR-1.2, KR-1.3 | EV dos entregáveis finais; SPI semana 5 | R-003 |
| CS-2: 100% cobertura workshops | KR-2.1, KR-2.2, KR-2.3, KR-2.4 | EV dos workshops (0/100); SPI semanas 1–2 | R-001 |
| CS-3: Aprovação pelos 3 sponsors | KR-3.1, KR-3.2, KR-3.3 | EV da Apresentação Final (0/100) | R-008 |
| CS-4: Score Model ≥ 70% objetivo | KR-4.1, KR-4.2 | EV Score Model (50/50); CPI fase analítica | R-003 |
| CS-5: Pacote RFP entregue | KR-5.1, KR-5.2 | EV entregáveis finais; SPI semana 5 | — |
| CS-6: NPS sponsors ≥ 7 | KR-6.1, KR-6.2, KR-6.3 | N/A (resultado de satisfação) | R-008 |

---

## Anexo B — Glossário e Convenções

| Termo | Definição |
|-------|-----------|
| **BAC** | Budget at Completion — orçamento total aprovado para o projeto |
| **EV** | Earned Value — valor do trabalho concluído, medido por entregáveis aceitos |
| **PV** | Planned Value — valor do trabalho que deveria estar concluído na data de medição |
| **AC** | Actual Cost — custo real incorrido até a data de medição |
| **CPI** | Cost Performance Index — EV ÷ AC; valores > 1,00 = abaixo do orçamento |
| **SPI** | Schedule Performance Index — EV ÷ PV; valores > 1,00 = adiantado |
| **EAC** | Estimate at Completion — previsão de custo total dado o CPI atual |
| **VAC** | Variance at Completion — BAC − EAC; negativo = risco de estouro |
| **TCPI** | To-Complete Performance Index — eficiência mínima necessária para concluir no BAC |
| **Regra 0/100** | Nenhum EV é creditado até o entregável ser 100% concluído e aceito |
| **Regra 50/50** | 50% do EV ao submeter o draft; 50% restante após aceite formal |
| **CS** | Critério de Sucesso (do TAP) |
| **KR** | Key Result (KPI de Resultado) |
| **KP** | KPI de Processo/Governança |

---

*Framework elaborado por Marcela Métrica — Monitora de Performance | VMO Autônomo (VMO Consultoria)*
*Aprovação necessária: GP Marcelo Silveira + Patrocinadores antes da primeira medição*
*Próxima revisão planejada: ao final da Semana 1 de medição efetiva*
