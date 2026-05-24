# Framework de KPIs e Métricas — PROJ-2026-005

| Campo | Valor |
|---|---|
| **Projeto** | PROJ-2026-005 — Auditor Fiscal NBS (Substituição Fiscal Defender) |
| **Demanda** | DEM-2026-002 |
| **Data de Referência** | 2026-05-15 |
| **Versão** | v6 |
| **Autor** | Marcela Métrica — Especialista em KPIs e Métricas (VMO Autônomo) |
| **Go-live planejado** | 30/10/2026 |
| **BAC** | R$ 35.000 |

---

## 1. EVM — Earned Value Management

### 1.1 Conceitos e Fórmulas Documentadas

| Sigla | Nome | Fórmula | Interpretação |
|---|---|---|---|
| **BAC** | Budget at Completion | Valor total aprovado do orçamento | Orçamento base: R$ 35.000 |
| **PV** | Planned Value | % trabalho planejado × BAC | Valor do trabalho que deveria estar feito até a data |
| **EV** | Earned Value | % trabalho realmente concluído × BAC | Valor do trabalho efetivamente entregue |
| **AC** | Actual Cost | Custo real incorrido até a data | Extraído do controle financeiro do projeto |
| **CV** | Cost Variance | EV − AC | > 0 = abaixo do orçamento; < 0 = estouro |
| **SV** | Schedule Variance | EV − PV | > 0 = adiantado; < 0 = atrasado |
| **CPI** | Cost Performance Index | EV ÷ AC | ≥ 1,0 = eficiente em custo |
| **SPI** | Schedule Performance Index | EV ÷ PV | ≥ 1,0 = no prazo ou adiantado |
| **EAC** | Estimate at Completion | BAC ÷ CPI | Previsão de custo final com performance atual |
| **ETC** | Estimate to Complete | EAC − AC | Quanto ainda falta gastar |
| **VAC** | Variance at Completion | BAC − EAC | Desvio previsto ao final do projeto |
| **TCPI** | To-Complete Performance Index | (BAC − EV) ÷ (BAC − AC) | CPI necessário para terminar dentro do orçamento |

### 1.2 Thresholds de Alerta e Escalada

| Indicador | Verde (Normal) | Amarelo (Alerta) | Vermelho (Escalada) |
|---|---|---|---|
| **CPI** | ≥ 1,0 | 0,80 ≤ CPI < 0,90 | CPI < 0,80 |
| **SPI** | ≥ 1,0 | 0,85 ≤ SPI < 0,95 | SPI < 0,85 |
| **VAC** | VAC ≥ 0 | −R$ 3.500 ≤ VAC < 0 | VAC < −R$ 3.500 (> 10% do BAC) |
| **Desvio de Prazo** | 0–5 dias | 6–14 dias | ≥ 15 dias em fase crítica |

### 1.3 Linha de Base PV por Fase — Curva S

**Critério de distribuição:** ponderação por complexidade e esforço de cada fase sobre o BAC de R$ 35.000.

| Pesos de distribuição por fase |
|---|
| F0 Sanação Bloqueantes: 3% — R$ 1.050 (mobilização, mitigação de riscos críticos) |
| F1 Kick-off + Alinhamento NBS: 5% — R$ 1.750 (alinhamento contratual, governança) |
| F2 Levantamento Detalhado: 12% — R$ 4.200 (análise de requisitos 6 módulos) |
| F3 Desenvolvimento NBS: 50% — R$ 17.500 (núcleo técnico do projeto) |
| F4 Homologação (UAT): 18% — R$ 6.300 (testes, correções, validação) |
| F5 Go-live + Transição: 7% — R$ 2.450 (deploy, treinamento, suporte inicial) |
| F6 Encerramento: 5% — R$ 1.750 (documentação, lições aprendidas, encerramento) |

#### Curva S — Pontos de Controle (PV Acumulado)

| # | Fase | Data de Controle | PV Incremental (R$) | PV Acumulado (R$) | % do BAC |
|---|---|---|---|---|---|
| 1 | F0 — Sanação Bloqueantes | 30/05/2026 | R$ 1.050 | R$ 1.050 | 3,0% |
| 2 | F1 — Kick-off + Alinhamento NBS | 14/06/2026 | R$ 1.750 | R$ 2.800 | 8,0% |
| 3 | F2 — Levantamento Detalhado | 15/07/2026 | R$ 4.200 | R$ 7.000 | 20,0% |
| 4 | F3 — Desenvolvimento NBS | 19/09/2026 | R$ 17.500 | R$ 24.500 | 70,0% |
| 5 | F4 — Homologação (UAT) | 17/10/2026 | R$ 6.300 | R$ 30.800 | 88,0% |
| 6 | F5 — Go-live + Transição | 14/11/2026 | R$ 2.450 | R$ 33.250 | 95,0% |
| 7 | F6 — Encerramento | 16/12/2026 | R$ 1.750 | R$ 35.000 | 100,0% |

> **Nota:** A curva S deve ser atualizada quinzenalmente durante F3 (Desenvolvimento) e semanalmente durante F4 (UAT), por serem fases de maior risco de desvio.

---

## 2. KPIs de Entrega do Projeto (Fase de Execução)

Vigência: 2026-05-15 a 2026-11-14 (F0 → F5)

| ID | Nome do KPI | Fórmula | Unidade | Baseline | Meta | Threshold Mínimo | Frequência | Fonte de Dados | Responsável |
|---|---|---|---|---|---|---|---|---|---|
| **KPI-01** | Índice de Desempenho de Prazo (SPI) | EV ÷ PV | Índice (adimensional) | 1,00 (planejado) | ≥ 1,00 | ≥ 0,85 (alerta < 0,85 = escalada) | Quinzenal | Cronograma + % conclusão declarada | Carlos Cronograma |
| **KPI-02** | Índice de Desempenho de Custo (CPI) | EV ÷ AC | Índice (adimensional) | 1,00 (planejado) | ≥ 1,00 | ≥ 0,90 (alerta < 0,80 = escalada) | Quinzenal | Controle financeiro + notas fiscais | Patrocinador / PMO |
| **KPI-03** | Cobertura de Requisitos Desenvolvidos | (Requisitos entregues ÷ Requisitos baseline) × 100 | % | 0% (início F3) | 100% até 19/09/2026 | ≥ 80% ao fim de F3 | Mensal (F2–F3) | ERF — Backlog de Requisitos | Rafael Requisito |
| **KPI-04** | Taxa de Defeitos em UAT | (Defeitos abertos críticos ÷ Casos de teste executados) × 100 | % | N/D (início UAT) | ≤ 2% ao final de F4 | ≤ 5% na revisão intermediária UAT (08/10/2026) | Semanal (F4) | Sistema de tracking de defeitos (UAT) | Equipe NBS + QA |
| **KPI-05** | Cobertura de Casos de Teste UAT | (Casos executados ÷ Casos planejados) × 100 | % | 0% (início F4) | 100% até 17/10/2026 | ≥ 60% até 08/10/2026 | Semanal (F4) | Plano de testes UAT | Equipe NBS + Usuários Chave |
| **KPI-06** | Taxa de Entrega no Prazo por Fase | (Milestones entregues no prazo ÷ Total de milestones planejados) × 100 | % | 0% (início) | ≥ 85% ao longo do projeto | ≥ 70% até F3 | Por fase (ao encerrar cada fase) | Cronograma mestre | Carlos Cronograma |
| **KPI-07** | Risco Residual Médio (Score) | Média dos scores dos riscos abertos no período | Score (0–25) | Score médio atual: 19 (RSK-01 + RSK-02 críticos) | Score médio ≤ 10 até F3 | Score médio ≤ 15 até F2 | Mensal | Matriz de riscos | Pedro Perigo |
| **KPI-08** | Completude da Documentação de Módulos | (Módulos com documentação técnica aprovada ÷ 6 módulos) × 100 | % | 0% | 100% (todos 6 módulos) até 15/10/2026 | ≥ 50% (3 módulos) até 19/09/2026 | Mensal (F2–F4) | Repositório de documentação | Rafael Requisito |
| **KPI-09** | Velocidade de Resolução de Impedimentos | Tempo médio (dias) entre registro e resolução de impedimento | Dias | Não estabelecido | ≤ 3 dias úteis | ≤ 5 dias úteis | Semanal | Backlog / Log de impedimentos | PMO / Sponsor |
| **KPI-10** | Índice de Comprometimento do Sponsor | Presença nas reuniões de checkpoint ÷ Total de checkpoints convocados | % | 0% (RSK-01 em aberto) | 100% (após identificação do Sponsor — marco F1) | ≥ 80% a partir de F2 | Por checkpoint | Atas de reunião | PMO |

---

## 3. KPIs de Transição (Go-live → 90 dias pós go-live)

Vigência: 18/10/2026 a 16/01/2027

| ID | Nome do KPI | Descrição | Fórmula | Meta de Aceitação (Critério de Sucesso do Go-live) | Prazo de Aferição | Responsável |
|---|---|---|---|---|---|---|
| **KPI-T01** | Taxa de Adoção pelo Usuário | % de usuários da Divisão Comércio que utilizam ativamente o Auditor Fiscal NBS (ao menos 1 operação/semana) | (Usuários ativos na semana ÷ Total de usuários habilitados) × 100 | ≥ 80% até 30 dias pós go-live; ≥ 95% até 90 dias pós go-live | D+30 e D+90 | Equipe NBS + Gestão Divisão Comércio |
| **KPI-T02** | Tempo Médio de Treinamento por Usuário | Horas médias investidas em treinamento para que o usuário atinja proficiência (nota ≥ 7 na avaliação) | Σ horas de treinamento ÷ nº de usuários treinados | ≤ 8 horas por usuário (meta eficiência); 100% dos usuários treinados até D+14 | D+14 pós go-live | Equipe de Treinamento NBS |
| **KPI-T03** | Incidentes Críticos em Produção (Sev. 1 e 2) | Número de incidentes de severidade crítica (falha total ou parcial do módulo de auditoria) registrados nos primeiros 90 dias | Contagem de chamados Sev.1 + Sev.2 abertos | 0 incidentes Sev.1 no período; ≤ 3 incidentes Sev.2 nos primeiros 90 dias | D+30, D+60, D+90 | Equipe NBS (SLA Suporte) |
| **KPI-T04** | Satisfação das Áreas Usuárias (CSAT) | Nota média de satisfação coletada via pesquisa estruturada com usuários-chave da Divisão Comércio | Média das notas em escala de 1 a 10 | ≥ 7,5 / 10,0 até D+30; ≥ 8,0 / 10,0 até D+90 | D+30 e D+90 | PMO + Gestão Divisão Comércio |
| **KPI-T05** | Disponibilidade do Sistema em Produção | Uptime do módulo Auditor Fiscal NBS em ambiente produtivo | (Tempo disponível ÷ Tempo total do período) × 100 | ≥ 99,0% nos primeiros 30 dias; ≥ 99,5% entre D+31 e D+90 | Contínuo (relatório semanal) | Equipe NBS / Infraestrutura |
| **KPI-T06** | Taxa de Cancelamento do Fiscal Defender | Confirmação do cancelamento contratual do Fiscal Defender | Marco binário (Sim/Não) + data do cancelamento efetivo | Cancelamento efetivado até D+30 pós go-live (14/11/2026) | D+30 | Financeiro / Jurídico / PMO |
| **KPI-T07** | Cobertura de Auditoria Fiscal no Período | % das NF-e do período auditadas pelo novo módulo em relação ao total emitido/recebido | (NF-e auditadas pelo NBS ÷ NF-e total do período) × 100 | ≥ 95% até D+30; 100% até D+60 | D+30 e D+60 | Equipe NBS + Fiscal Divisão Comércio |

---

## 4. KRs — Key Results Pós Go-live (3 a 12 meses)

**OKR do Projeto:** *"Consolidar a auditoria fiscal da Divisão Comércio no ERP NBS, eliminando a dependência do Fiscal Defender e gerando eficiência operacional mensurável."*

| ID | Key Result | Descrição | Métrica | Baseline (pré go-live) | Meta | Prazo de Medição |
|---|---|---|---|---|---|---|
| **KR-01** | Saving Realizado vs. Esperado | Confirmar que a economia com cancelamento do Fiscal Defender está sendo capturada conforme planejado | (Custo evitado acumulado ÷ Saving esperado acumulado) × 100 | R$ 0 (contrato Fiscal Defender ainda ativo) | ≥ 100% do saving esperado: R$ 19.500 em 3 meses (3 × R$ 6.500/mês); R$ 78.000 ao final de 12 meses | M+3 (Jan/2027), M+6 (Abr/2027), M+12 (Out/2027) |
| **KR-02** | Cobertura Total da Auditoria Fiscal NBS | Garantir que 100% das operações fiscais da Divisão Comércio passem pelo Auditor Fiscal NBS sem exceções manuais | (Operações auditadas automaticamente ÷ Total de operações fiscais) × 100 | ~0% no NBS (toda auditoria no Fiscal Defender) | ≥ 98% até M+3; 100% até M+6 (sem processos residuais no Fiscal Defender) | M+3 (Jan/2027) e M+6 (Abr/2027) |
| **KR-03** | SLA de Disponibilidade em Operação Estável | Manter alta disponibilidade do Auditor Fiscal NBS após período de estabilização | Uptime mensal do módulo em produção | N/D (sistema ainda não em produção) | ≥ 99,5% / mês a partir de M+3 (Jan/2027) de forma contínua | Mensal a partir de M+3, avaliação consolidada em M+12 |
| **KR-04** | Satisfação Sustentada do Usuário | Demonstrar que os usuários da Divisão Comércio estão satisfeitos com o novo módulo de forma duradoura | CSAT médio trimestral (escala 1–10) | Nota de referência pré-projeto: não coletada (usar D+90 como nova baseline) | ≥ 8,0 / 10,0 em todas as medições trimestrais (M+3, M+6, M+9, M+12) | Trimestral: Jan/2027, Abr/2027, Jul/2027, Out/2027 |
| **KR-05** | Redução de Erros Fiscais com Auditoria Automatizada | Demonstrar que o novo motor de auditoria (M2) reduz a incidência de erros fiscais versus o cenário anterior | (Alertas de erro fiscal gerados pelo NBS no período ÷ Total de NF-e processadas) × 100; comparar com taxa histórica do Fiscal Defender | Taxa histórica a ser coletada em F2 (Levantamento Detalhado) | Redução de ≥ 30% na taxa de erros fiscais não detectados em M+6 vs. baseline histórico | M+6 (Abr/2027) |
| **KR-06** | ROI Realizado | Confirmar que o retorno sobre o investimento está aderente ao planejado | (Benefícios acumulados − Custos totais do projeto) ÷ Custos totais × 100 | ROI = 0% (pré go-live) | ROI ≥ 100% em M+6 (payback completo); ROI ≥ 469% projetado em M+36 | M+6 (Abr/2027) e M+12 (Out/2027) |

---

## 5. Dashboard de Monitoramento

### 5.1 Painel Semanal de Execução (F0 a F5)

**Audiência:** Equipe de projeto, gerente de projeto, equipe NBS
**Cadência:** Toda sexta-feira
**Plataforma sugerida:** Power BI / Planilha compartilhada (Sharepoint)

| Seção | Conteúdo |
|---|---|
| **Status Geral** | Semáforo do projeto (Verde/Amarelo/Vermelho) com justificativa |
| **EVM em Tempo Real** | CPI, SPI, EV, AC, PV da semana; Curva S atualizada |
| **Cronograma** | Gantt sintético com % de conclusão por fase; próximos milestones em 14 dias |
| **Riscos Ativos** | Top 5 riscos por score; novos riscos da semana |
| **Impedimentos** | Lista de impedimentos abertos com dono e prazo de resolução |
| **UAT (apenas F4)** | % de casos executados, taxa de defeitos abertos por severidade |

### 5.2 Painel Mensal de Portfólio (F0 a F6)

**Audiência:** Sponsor, diretoria, PMO, gestores das áreas impactadas
**Cadência:** Toda última sexta-feira do mês
**Plataforma sugerida:** Power BI com camada de dados do projeto

| Seção | Conteúdo |
|---|---|
| **EVM Consolidado** | CPI e SPI histórico (linha do tempo); EAC vs. BAC; VAC projetado |
| **Performance Financeira** | Comprometido vs. realizado vs. planejado; projeção de saving |
| **Cronograma Estratégico** | Fases concluídas vs. planejadas; desvio acumulado em dias |
| **KPIs do Período** | Tabela com todos os KPIs de execução ativos: valor atual vs. meta |
| **Riscos Estratégicos** | Heatmap de riscos; status dos planos de ação dos top 4 riscos |
| **Decisões Pendentes** | Itens que requerem decisão do patrocinador ou diretoria |

### 5.3 Painel Pós Go-live (D+0 a D+90 e além)

**Audiência:** Gestão Divisão Comércio, Financeiro, Compliance Fiscal, PMO
**Cadência:** Semanal nos primeiros 30 dias; mensal a partir de D+31

| Seção | Conteúdo |
|---|---|
| **Adoção e Uso** | KPI-T01: taxa de adoção por semana; curva de adoção acumulada |
| **Qualidade em Produção** | KPI-T03: incidentes por severidade; tempo médio de resolução (MTTR) |
| **Disponibilidade** | KPI-T05: uptime semanal e acumulado vs. SLA 99,5% |
| **Satisfação (CSAT)** | KPI-T04: NPS/CSAT por pesquisa; comentários qualitativos por área |
| **Financeiro** | Saving realizado (KR-01): mês a mês vs. planejado; confirmação de cancelamento Fiscal Defender |
| **Cobertura Fiscal** | KPI-T07 / KR-02: % de NF-e auditadas automaticamente |

---

## 6. Critérios de Encerramento do Projeto

O projeto PROJ-2026-005 será considerado **encerrado com sucesso** quando TODAS as condições abaixo forem atendidas e formalmente verificadas:

| # | Critério de Encerramento | Evidência Exigida | Prazo Limite |
|---|---|---|---|
| **CE-01** | 100% dos módulos (M1–M6) entregues, homologados e em produção | Atas de aceite assinadas por representantes da Divisão Comércio para cada módulo | 14/11/2026 |
| **CE-02** | Taxa de defeitos UAT ≤ 2% na entrega final | Relatório final de UAT com contagem de defeitos abertos / fechados | 17/10/2026 |
| **CE-03** | Cobertura de auditoria fiscal ≥ 95% das NF-e no primeiro mês de produção | Relatório de cobertura extraído do módulo M4 (Relatórios e Dashboards) | 14/11/2026 |
| **CE-04** | Cancelamento formal do contrato do Fiscal Defender efetivado | Comprovante de cancelamento contratual emitido pelo fornecedor / área jurídica | 14/11/2026 |
| **CE-05** | CSAT dos usuários da Divisão Comércio ≥ 7,5/10 em D+30 | Resultado da pesquisa de satisfação D+30 com ≥ 80% de respondentes | 14/11/2026 |
| **CE-06** | Zero incidentes Sev.1 nos primeiros 30 dias de produção | Log de incidentes do período D+0 a D+30 | 14/11/2026 |
| **CE-07** | Documentação técnica e operacional 100% entregue e aprovada | Repositório de documentação completo: manual do usuário, manual técnico, guia de configuração de regras (M5) | 16/12/2026 |
| **CE-08** | Lições aprendidas registradas e compartilhadas com PMO | Documento de lições aprendidas publicado no repositório do VMO | 16/12/2026 |
| **CE-09** | CPI final ≥ 0,90 (custo realizado ≤ 110% do BAC = R$ 38.500) | Relatório financeiro final do projeto | 16/12/2026 |
| **CE-10** | Termo de encerramento assinado pelo Sponsor | Documento formal de aceite e encerramento com assinatura do patrocinador identificado | 16/12/2026 |

> **Nota:** Os critérios CE-01 a CE-06 são **pré-requisitos para o go-live** e devem ser verificados antes da declaração de sucesso da F5. Os critérios CE-07 a CE-10 encerram formalmente o projeto na F6.

---

## 7. Alertas e Gatilhos de Escalada

| # | Condição (Gatilho) | Nível | Ação Imediata | Responsável pela Ação | Prazo para Resposta |
|---|---|---|---|---|---|
| **ALR-01** | SPI < 0,85 em qualquer medição quinzenal | Vermelho — Escalada | Convocar reunião de crise com equipe NBS + PMO; revisar cronograma; acionar plano de contingência de prazo | Carlos Cronograma + PMO | 48 horas após identificação |
| **ALR-02** | CPI < 0,80 em qualquer medição | Vermelho — Escalada | Convocar comitê de portfólio; revisar escopo; levantar causas de estouro; comunicar Sponsor e diretoria | PMO + Sponsor | 48 horas após identificação |
| **ALR-03** | CPI entre 0,80 e 0,90 | Amarelo — Alerta | Investigar causas; apresentar plano de recuperação na próxima reunião de portfólio | Carlos Cronograma + PMO | 5 dias úteis |
| **ALR-04** | RSK-01 (Sponsor) não resolvido até 14/06/2026 (fim F1) | Vermelho — Escalada Estratégica | Escalar para diretoria executiva; projeto entra em stand-by formal até identificação do Sponsor | PMO + Diretoria | Imediato (fim F1) |
| **ALR-05** | RSK-02 (acordo NBS não verificado) persistir em F2 | Vermelho — Bloqueante | Suspender atividades de desenvolvimento até formalização do acordo NBS; comunicar ao Sponsor | PMO + Jurídico | 24 horas após início F2 |
| **ALR-06** | Taxa de defeitos UAT > 5% na revisão intermediária (08/10/2026) | Amarelo — Alerta | Ampliar equipe de correção NBS; revisar cronograma de UAT; avaliar risco de atraso no go-live | Equipe NBS + QA | 3 dias úteis |
| **ALR-07** | Taxa de defeitos UAT > 10% ao final de F4 | Vermelho — Bloqueante de Go-live | Bloquear go-live; estender UAT; acionar cláusula de SLA com NBS; comunicar Sponsor | PMO + Equipe NBS + Sponsor | Imediato |
| **ALR-08** | Incidente Sev.1 em produção (pós go-live) | Vermelho — Incidente Crítico | Ativar bridge de incidente; comunicar gestão Divisão Comércio; acionar suporte NBS P1; avaliar rollback | Equipe NBS (plantão) + PMO | Resposta em 1 hora; resolução em 4 horas |
| **ALR-09** | Taxa de adoção < 60% em D+14 | Amarelo — Alerta | Intensificar treinamento; identificar barreiras de adoção por área; apoio presencial de key users | Equipe de Treinamento + Gestão | 5 dias úteis |
| **ALR-10** | Fiscal Defender não cancelado até D+30 (14/11/2026) | Amarelo — Alerta Financeiro | Escalar para área Financeira e Jurídica; acionar responsável pelo contrato; documentar risco de custo duplo | Financeiro + Jurídico + PMO | 48 horas após D+30 |
| **ALR-11** | CSAT D+30 < 6,0/10 | Vermelho — Escalada | Realizar pesquisa qualitativa aprofundada; plano de ação de melhoria com prazo de 30 dias; comunicar ao Sponsor | PMO + Gestão Divisão Comércio | 5 dias úteis |
| **ALR-12** | Desvio de prazo ≥ 15 dias em fase crítica (F3 ou F4) | Vermelho — Escalada | Análise de impacto no go-live; comunicado formal ao Sponsor; revisão do roadmap com compressão de fases ou ajuste de escopo | Carlos Cronograma + PMO + Sponsor | 48 horas |

---

## Apêndice — Resumo Executivo de Metas

| Dimensão | KPI Principal | Meta de Sucesso |
|---|---|---|
| **Prazo** | SPI ≥ 0,95 na média do projeto | Go-live até 30/10/2026 |
| **Custo** | CPI ≥ 0,95; custo final ≤ R$ 36.750 | BAC R$ 35.000 (tolerância +5%) |
| **Qualidade** | Taxa defeitos UAT ≤ 2% na entrega | 100% módulos aceitos |
| **Adoção** | ≥ 95% usuários ativos em D+90 | CSAT ≥ 8,0/10 em D+90 |
| **Benefício Financeiro** | Saving R$ 78.000/ano realizado | Payback ≤ 6 meses pós go-live |
| **Disponibilidade** | Uptime ≥ 99,5%/mês em operação estável | A partir de Jan/2027 |

---

*Documento gerado por: Marcela Métrica — VMO Autônomo | 2026-05-15 | PROJ-2026-005 v6*
