# Framework de KPIs — PROJ-2026-006
## Plataforma Própria de Gestão de Ideias e Inovação

**Elaborado por:** Marcela Métrica — Monitora de Performance (VMO Consultoria)
**Data de elaboração:** 2026-05-16
**Revisão:** 1.0
**Status:** Baseline Aprovado

---

## Parâmetros-Base do Projeto

| Parâmetro | Valor |
|---|---|
| BAC (Budget at Completion) | R$ 100.000 |
| Início planejado | 2026-06-24 |
| Go-live planejado | 2026-12-07 |
| Prazo contratual máximo | 2026-12-31 |
| Duração total planejada | 28 semanas |
| Módulos no escopo | M1, M2, M3, M4, M5, M6 |
| Gerente de Projeto | Marcelo Silveira |

---

## TASK 1 — KPIs DEFINIDOS

---

### BLOCO A — KPIs de Desempenho do Projeto (EVM Obrigatórios)

> **EVM (Earned Value Management)** é metodologia mandatória em todos os projetos VMO. Os quatro indicadores abaixo devem ser calculados mensalmente a partir do relatório de progresso físico e custos acumulados.

---

#### KPI-EVM-01 — CPI (Cost Performance Index)

| Campo | Valor |
|---|---|
| **Definição** | Eficiência do gasto em relação ao valor entregue. CPI = EV / AC |
| **BAC** | R$ 100.000 |
| **Baseline** | 1,00 (eficiência perfeita — cada R$1,00 gasto gera R$1,00 de valor) |
| **Meta** | CPI ≥ 1,00 durante todo o projeto |
| **Threshold Verde** | CPI ≥ 0,95 |
| **Threshold Amarelo** | 0,85 ≤ CPI < 0,95 — atenção, análise de causa requerida |
| **Threshold Vermelho** | CPI < 0,85 — intervenção imediata, escalada ao Sponsor |
| **Frequência de aferição** | Mensal (última sexta-feira útil do mês) |
| **Responsável pela aferição** | Marcelo Silveira — GP VMO |
| **Fonte de dados** | Relatório de custos acumulados vs. progresso físico (% concluído por pacote) |
| **Ação em vermelho** | Análise de desvio de causa-raiz em até 48h; plano de recuperação apresentado ao Sponsor em até 5 dias úteis |

---

#### KPI-EVM-02 — SPI (Schedule Performance Index)

| Campo | Valor |
|---|---|
| **Definição** | Eficiência do progresso em relação ao cronograma. SPI = EV / PV |
| **BAC** | R$ 100.000 |
| **Baseline** | 1,00 (progresso na velocidade planejada) |
| **Meta** | SPI ≥ 1,00 durante todo o projeto |
| **Threshold Verde** | SPI ≥ 0,95 |
| **Threshold Amarelo** | 0,85 ≤ SPI < 0,95 — alerta de atraso, revisão de cronograma requerida |
| **Threshold Vermelho** | SPI < 0,85 — atraso crítico, escalada imediata ao Sponsor |
| **Frequência de aferição** | Mensal (última sexta-feira útil do mês) |
| **Responsável pela aferição** | Marcelo Silveira — GP VMO |
| **Fonte de dados** | Cronograma baseline (Parte 2 — cronograma.md) vs. % físico concluído por atividade |
| **Ação em vermelho** | Plano de recuperação de cronograma em até 48h; avaliação de compressão (crashing/fast-tracking) de atividades no caminho crítico |

---

#### KPI-EVM-03 — EAC (Estimate at Completion)

| Campo | Valor |
|---|---|
| **Definição** | Projeção do custo total do projeto ao término, dado o desempenho atual. EAC = BAC / CPI |
| **BAC** | R$ 100.000 |
| **Baseline** | R$ 100.000 (cenário de eficiência perfeita) |
| **Meta** | EAC ≤ R$ 100.000 |
| **Threshold Verde** | EAC ≤ R$ 100.000 |
| **Threshold Amarelo** | R$ 100.001 ≤ EAC ≤ R$ 110.000 (uso parcial da contingência — dentro do teto com reserva) |
| **Threshold Vermelho** | EAC > R$ 110.000 — projeção de extrapolação do teto; requer decisão formal do Sponsor |
| **Frequência de aferição** | Mensal — calculado automaticamente a partir do CPI apurado |
| **Responsável pela aferição** | Marcelo Silveira — GP VMO |
| **Fonte de dados** | CPI do período × BAC; tabela de EAC atualizada no relatório mensal |
| **Nota** | A contingência de R$17.000 integra o BAC. EAC > R$100k indica uso parcial da contingência; EAC > R$117k indica rompimento total do orçamento aprovado |

---

#### KPI-EVM-04 — VAC (Variance at Completion)

| Campo | Valor |
|---|---|
| **Definição** | Desvio projetado entre orçamento e custo final estimado. VAC = BAC − EAC |
| **BAC** | R$ 100.000 |
| **Baseline** | R$ 0,00 (zero desvio projetado) |
| **Meta** | VAC ≥ R$ 0,00 (custo final igual ou inferior ao BAC) |
| **Threshold Verde** | VAC ≥ R$ 0 (dentro do orçamento) |
| **Threshold Amarelo** | −R$ 10.000 ≤ VAC < R$ 0 (desvio negativo de até 10%) |
| **Threshold Vermelho** | VAC < −R$ 10.000 (desvio negativo superior a 10% do BAC) |
| **Frequência de aferição** | Mensal — derivado do EAC apurado |
| **Responsável pela aferição** | Marcelo Silveira — GP VMO |
| **Fonte de dados** | EAC do período |

---

### BLOCO B — KPIs de Resultado (Derivados dos Critérios de Sucesso)

> Cada KPI de resultado é rastreável a um Critério de Sucesso (CS) do TAP. Sem meta mensurável, não é KPI.

---

#### KPI-R-01 — Entrega de Módulos no Prazo *(vinculado a CS-02)*

| Campo | Valor |
|---|---|
| **Critério de sucesso** | CS-02: Plataforma entregue com 100% dos módulos M1-M6 operacionais até 31/12/2026 |
| **Definição** | Percentual de módulos entregues dentro da data-alvo de cada marco de projeto (M2 a M8) |
| **Fórmula** | (Módulos entregues no prazo / Total de módulos planejados) × 100 |
| **Baseline** | 0% (projeto não iniciado) |
| **Meta** | 100% dos módulos M1-M6 em produção até 07/12/2026 (go-live planejado); deadline máximo 31/12/2026 |
| **Threshold Verde** | 100% dos módulos no prazo; go-live em 07/12/2026 |
| **Threshold Amarelo** | Go-live entre 08/12/2026 e 24/12/2026 — dentro da janela de folga residual |
| **Threshold Vermelho** | Go-live após 25/12/2026 ou qualquer módulo incompleto em 31/12/2026 |
| **Frequência de aferição** | A cada marco de projeto (M0 a M8); relatório mensal entre marcos |
| **Responsável** | Marcelo Silveira — GP VMO |
| **Fonte de dados** | Ata de aceite por marco (cronograma.md); registro de deploy em produção |

---

#### KPI-R-02 — Rescisão do Contrato SaaS *(vinculado a CS-01 - aspecto de prazo de rescisão)*

| Campo | Valor |
|---|---|
| **Critério de sucesso** | CS-01: Contrato da plataforma SaaS atual rescindido em até 30 dias após go-live |
| **Definição** | Número de dias entre o go-live da plataforma própria e a rescisão formal do contrato SaaS |
| **Fórmula** | Data de rescisão formal SaaS − Data do go-live (em dias corridos) |
| **Baseline** | Contrato SaaS ativo (antes do go-live) |
| **Meta** | Rescisão em até 30 dias corridos após go-live |
| **Threshold Verde** | Rescisão em ≤ 30 dias pós go-live |
| **Threshold Amarelo** | Rescisão entre 31 e 45 dias pós go-live — risco de custo duplo; pressionar Jurídico |
| **Threshold Vermelho** | Rescisão após 45 dias pós go-live — custo duplo de licença e licença própria confirmado; escalada ao Sponsor |
| **Frequência de aferição** | Aferição única pós go-live; monitoramento semanal após go-live até confirmação da rescisão |
| **Responsável** | Marcelo Silveira — GP VMO + Jurídico/Compliance |
| **Fonte de dados** | Termo de rescisão contratual assinado; notificação ao fornecedor SaaS |

---

#### KPI-R-03 — Economia de Licenciamento Confirmada *(vinculado a CS-03)*

| Campo | Valor |
|---|---|
| **Critério de sucesso** | CS-03: Economia anual de R$85.000 em licenciamento confirmada no 1º ano pós go-live |
| **Definição** | Economia anual efetiva gerada pela eliminação da licença SaaS no primeiro ano após go-live |
| **Fórmula** | Custo anual SaaS (2026) − Custo anual plataforma própria (infraestrutura + sustentação 2027) |
| **Baseline** | Custo SaaS atual: R$ 80.000 a R$ 90.000/ano (referência TAP) |
| **Meta** | Economia ≥ R$ 85.000 no 1º ano completo pós go-live (jan–dez/2027) |
| **Threshold Verde** | Economia ≥ R$ 85.000/ano |
| **Threshold Amarelo** | R$ 70.000 ≤ Economia < R$ 85.000/ano — abaixo da meta; analisar custos de sustentação |
| **Threshold Vermelho** | Economia < R$ 70.000/ano — desvio superior a 17,6%; reavaliação do business case; escalada ao Sponsor |
| **Frequência de aferição** | Trimestral no 1º ano pós go-live; consolidação anual em dez/2027 |
| **Responsável** | Marcelo Silveira — GP VMO + Controller Financeiro |
| **Fonte de dados** | Comparativo de despesas: notas fiscais SaaS 2026 vs. custos de infraestrutura própria 2027 |

---

#### KPI-R-04 — Taxa de Adoção de Usuários *(vinculado a CS-04)*

| Campo | Valor |
|---|---|
| **Critério de sucesso** | CS-04: Taxa de adoção ≥ 80% dos usuários ativos da plataforma anterior migrados em 60 dias pós go-live |
| **Definição** | Percentual de usuários ativos na plataforma SaaS anterior que realizaram ao menos 1 login ativo na nova plataforma nos primeiros 60 dias pós go-live |
| **Fórmula** | (Usuários com ≥ 1 login na nova plataforma em 60 dias / Total de usuários ativos na plataforma SaaS anterior) × 100 |
| **Baseline** | 0% no dia do go-live |
| **Meta** | ≥ 80% em 60 dias corridos pós go-live |
| **Threshold Verde** | Adoção ≥ 80% em 60 dias |
| **Threshold Amarelo** | 60% ≤ Adoção < 80% em 60 dias — plano de ação de engajamento ativo |
| **Threshold Vermelho** | Adoção < 60% em 60 dias — risco de baixo retorno do investimento; acionar Plano de Comunicação de Crise |
| **Frequência de aferição** | Semanal nas primeiras 8 semanas pós go-live; consolidação final no D+60 |
| **Responsável** | Jadson — Gestor de Inovação + GP VMO |
| **Fonte de dados** | Relatório de logins exportado do sistema (log de acesso por usuário); base de usuários ativos SaaS como denominador |

---

#### KPI-R-05 — Satisfação dos Usuários *(vinculado a CS-05)*

| Campo | Valor |
|---|---|
| **Critério de sucesso** | CS-05: Satisfação dos usuários ≥ 7,5/10 na pesquisa pós-lançamento |
| **Definição** | Score médio de satisfação dos usuários na pesquisa aplicada após o go-live |
| **Fórmula** | Média aritmética dos scores individuais da pesquisa de satisfação (escala 0–10) |
| **Baseline** | Score da plataforma SaaS atual (a levantar antes do go-live como benchmark de comparação) |
| **Meta** | Score médio ≥ 7,5 / 10,0 |
| **Threshold Verde** | Score ≥ 7,5 |
| **Threshold Amarelo** | 6,0 ≤ Score < 7,5 — identificar pontos críticos; plano de melhoria em até 30 dias |
| **Threshold Vermelho** | Score < 6,0 — insatisfação estrutural; análise qualitativa obrigatória; plano de correção emergencial |
| **Frequência de aferição** | Pesquisa aplicada no D+30 pós go-live; reaplicação opcional no D+90 |
| **Responsável** | Jadson — Gestor de Inovação |
| **Fonte de dados** | Formulário digital de pesquisa (Google Forms / ferramenta interna); mínimo de 60% de taxa de resposta para validade estatística |
| **Nota** | Pesquisa dirigida a gestores de área e colaboradores ativos. Critério de aceitação: mínimo 60% de taxa de resposta sobre a base de usuários migrados |

---

## TASK 2 — SEMÁFORO DE SAÚDE DO PROJETO

> O semáforo de saúde é emitido mensalmente pelo GP VMO no Relatório de Status. Cada dimensão recebe uma cor independente. A cor mais crítica entre as 5 dimensões define a cor geral do projeto no período.

---

### Dimensão 1 — CRONOGRAMA (SPI)

| Cor | Threshold | Ação |
|---|---|---|
| VERDE | SPI ≥ 0,95 | Monitoramento padrão |
| AMARELO | 0,85 ≤ SPI < 0,95 | Revisar cronograma; identificar atividades críticas em risco; reunião de emergência com fornecedor em até 3 dias úteis |
| VERMELHO | SPI < 0,85 | Escalada imediata ao Sponsor; acionar plano de recuperação (crashing/fast-tracking); avaliar impacto no go-live de 07/12/2026 |

**Indicador complementar:** Desvio em semanas do marco mais próximo. Alerta automático se desvio > 2 semanas em qualquer marco do caminho crítico.

---

### Dimensão 2 — CUSTO (CPI)

| Cor | Threshold | Ação |
|---|---|---|
| VERDE | CPI ≥ 0,95 | Monitoramento padrão |
| AMARELO | 0,85 ≤ CPI < 0,95 | Auditoria de custos acumulados; identificar categoria de desvio; reunião com Sponsor em até 5 dias úteis; avaliar uso da reserva de contingência |
| VERMELHO | CPI < 0,85 (EAC > R$117.000) | Paralisação de gastos não essenciais; aprovação do Sponsor para qualquer gasto adicional; renegociação com fornecedor se custo for externo |

**Indicador complementar:** % da contingência consumida. Alerta amarelo se >50% da contingência (R$8.500) consumida antes de 50% do prazo decorrido.

---

### Dimensão 3 — ESCOPO (Mudanças de Escopo)

| Cor | Threshold | Ação |
|---|---|---|
| VERDE | 0 mudanças aprovadas no período; nenhuma solicitação de mudança de impacto pendente | Monitoramento padrão |
| AMARELO | 1–2 mudanças de escopo aprovadas com impacto controlado (sem comprometer prazo ou orçamento); ou 1 solicitação de impacto alto em análise | Acionar processo formal de controle de mudanças (PG-10); análise de impacto em cronograma e custo antes de qualquer aprovação |
| VERMELHO | ≥ 3 mudanças aprovadas no período; ou qualquer mudança que impacte prazo de 31/12/2026 ou extrapole o BAC de R$100.000 | Congelar escopo; nenhuma nova solicitação admitida sem aprovação do Sponsor; revisão do TAP se necessário |

**Indicador complementar:** Volume acumulado de solicitações de mudança (log de mudanças — PG-10). Benchmark de alerta: > 5 solicitações acumuladas ao longo do projeto.

---

### Dimensão 4 — RISCOS (Nível do Risco Aberto Mais Alto)

| Cor | Threshold | Ação |
|---|---|---|
| VERDE | Nenhum risco ativo com classificação "Crítico" ou "Alto"; todos os riscos em monitoramento ou mitigados | Monitoramento padrão do registro de riscos (atualização mensal) |
| AMARELO | 1 ou mais riscos com classificação "Alto" ativos (probabilidade × impacto = Alto); plano de resposta definido e em execução | Reunião de revisão de riscos com GP VMO e equipe; atualizar plano de resposta; comunicar Sponsor se risco tiver potencial de escalar para Crítico |
| VERMELHO | Qualquer risco com classificação "Crítico" ativo (ex: RI-01 sem resolução após data-limite; RI-03 com impacto confirmado no prazo de go-live) | Escalada imediata ao Sponsor; convocação de reunião de crise em 24h; ativar plano de contingência específico do risco |

**Indicador complementar:** Quantidade de riscos com resposta "Aceitar passivamente" — não devem exceder 1 risco de impacto Alto sem mitigação ativa documentada.

---

### Dimensão 5 — SATISFAÇÃO (Score de Pesquisa Pós-Lançamento)

| Cor | Threshold | Ação |
|---|---|---|
| VERDE | Score médio ≥ 7,5 / 10,0 (meta atingida — KPI-R-05) | Registrar aprendizados positivos; comunicar resultado ao Sponsor |
| AMARELO | 6,0 ≤ Score < 7,5 | Análise qualitativa dos comentários abertos; identificação dos top 3 pontos de insatisfação; plano de melhoria apresentado à Área de Inovação em até 30 dias |
| VERMELHO | Score < 6,0 | Diagnóstico de usabilidade com usuários-chave; avaliar retrabalho de UX/UI nos módulos com menor score; relatório ao Sponsor em até 10 dias úteis pós-resultado |

**Nota de aplicação:** Esta dimensão permanece em "Cinza — Não Aplicável" durante todo o período de desenvolvimento (pré go-live). Ativa no D+30 pós go-live com resultado da pesquisa.

---

## Painel Consolidado — Semáforo de Saúde (Template Mensal)

| Dimensão | KPI Referência | Meta | Realizado | Cor | Ação |
|---|---|---|---|---|---|
| Cronograma | SPI | ≥ 0,95 | __ | __ | __ |
| Custo | CPI | ≥ 0,95 | __ | __ | __ |
| Escopo | Mudanças aprovadas no período | 0 mudanças de impacto | __ | __ | __ |
| Riscos | Nível do risco aberto mais alto | Nenhum Crítico ativo | __ | __ | __ |
| Satisfação | Score pesquisa (D+30) | ≥ 7,5 / 10 | __ | __ | __ |
| **SAÚDE GERAL** | Pior cor das 5 dimensões | Verde | __ | __ | __ |

> **Legenda:** VERDE = dentro das metas | AMARELO = atenção — ação requerida | VERMELHO = crítico — escalada obrigatória | CINZA = não aplicável no período

---

## Calendário de Aferição

| KPI | Frequência | Próxima aferição | Responsável |
|---|---|---|---|
| CPI (KPI-EVM-01) | Mensal | Julho/2026 (D+30 do início) | Marcelo Silveira |
| SPI (KPI-EVM-02) | Mensal | Julho/2026 (D+30 do início) | Marcelo Silveira |
| EAC (KPI-EVM-03) | Mensal | Julho/2026 | Marcelo Silveira |
| VAC (KPI-EVM-04) | Mensal | Julho/2026 | Marcelo Silveira |
| Entrega de Módulos (KPI-R-01) | Por marco (M0–M8) | Marco M0: 2026-06-24 | Marcelo Silveira |
| Rescisão SaaS (KPI-R-02) | Pós go-live (D+30) | Jan/2027 (após go-live de dez/2026) | Marcelo Silveira + Jurídico |
| Economia de Licenciamento (KPI-R-03) | Trimestral pós go-live | Mar/2027 (T1 pós go-live) | Marcelo Silveira + Controller |
| Taxa de Adoção (KPI-R-04) | Semanal D+1 a D+60 | Jan/2027 (início pós go-live) | Jadson + GP VMO |
| Satisfação (KPI-R-05) | Pesquisa D+30 | Jan/2027 (30 dias pós go-live) | Jadson |

---

## Veto Conditions — Checklist de Qualidade

- [x] KPIs EVM obrigatórios presentes: CPI (KPI-EVM-01), SPI (KPI-EVM-02), EAC (KPI-EVM-03) e VAC (KPI-EVM-04)
- [x] BAC = R$ 100.000 definido e explicitado em todos os KPIs EVM
- [x] KPIs de resultado vinculados a CS-01 (KPI-R-02), CS-02 (KPI-R-01), CS-03 (KPI-R-03), CS-04 (KPI-R-04) e CS-05 (KPI-R-05)
- [x] Thresholds verde/amarelo/vermelho definidos por KPI com limites numéricos precisos
- [x] Frequência de aferição e responsável definidos para cada KPI
- [x] Semáforo de saúde com 5 dimensões: Cronograma, Custo, Escopo, Riscos e Satisfação
- [x] Nenhum KPI sem meta mensurável
- [x] Nenhum EVM sem BAC definido
- [x] Nenhum threshold subjetivo — todos com limite numérico explícito

---

*Framework elaborado por: Marcela Métrica — Monitora de Performance | VMO Consultoria*
*Versão 1.0 — 2026-05-16 | PROJ-2026-006*
*Próxima revisão: Julho/2026 (D+30 do início do projeto)*
