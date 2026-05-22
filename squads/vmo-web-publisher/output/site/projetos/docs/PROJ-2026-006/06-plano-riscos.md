# Plano de Riscos — PROJ-2026-006
## Plataforma Própria de Gestão de Ideias e Inovação

**Elaborado por:** Pedro Perigo — Analista de Riscos (VMO Consultoria)
**Data de elaboração:** 2026-05-16
**Revisão:** 1.0
**Status:** Aprovação pendente de Sponsor (condição bloqueante CB-01)

---

## Sumário Executivo de Riscos

| Parâmetro | Valor |
|---|---|
| Total de riscos identificados | 12 riscos |
| Riscos CRÍTICOS (P×I ≥ 16) | 4 riscos |
| Riscos ALTOS (P×I 9–15) | 5 riscos |
| Riscos MÉDIOS (P×I 5–8) | 2 riscos |
| Riscos BAIXOS (P×I 1–4) | 1 risco |
| Categorias cobertas | 6 categorias |
| VME total (CRÍTICOS + ALTOS) | **R$ 260.000** (exposição bruta agregada) |
| Reserva de contingência recomendada | **R$ 17.000** (conforme TAP, calibrada para absorção realista) |
| Reserva de contingência adicional sugerida | **+R$ 10.000** (gap de cobertura — ver seção 5) |

> **Nota metodológica:** O VME bruto agregado (R$ 260.000) é a soma dos valores monetários esperados de todos os riscos CRÍTICOS e ALTOS calculados individualmente. Riscos não se materializam simultaneamente e possuem correlação parcial entre si. A reserva de contingência de R$ 17.000 aprovada no TAP é insuficiente para cobrir os cenários de maior exposição. Recomenda-se aprovação de reserva adicional de R$ 10.000 (total R$ 27.000 = 27% do orçamento base de R$ 83.000).

---

## 1. Escala de Avaliação

### 1.1 Probabilidade (P)

| Valor | Classificação | Definição |
|---|---|---|
| 1 | Muito Baixa | < 10% de chance de ocorrer neste projeto |
| 2 | Baixa | 10–30% de chance |
| 3 | Média | 31–60% de chance |
| 4 | Alta | 61–80% de chance |
| 5 | Muito Alta | > 80% de chance |

### 1.2 Impacto (I)

| Valor | Classificação | Impacto em Prazo | Impacto em Custo | Impacto em Escopo/Qualidade |
|---|---|---|---|---|
| 1 | Muito Baixo | < 1 semana | < R$ 2.000 | Ajuste menor sem impacto funcional |
| 2 | Baixo | 1–2 semanas | R$ 2.000–5.000 | Funcionalidade reduzida sem impacto em adoção |
| 3 | Médio | 2–4 semanas | R$ 5.000–15.000 | Módulo entregue com funcionalidade parcial |
| 4 | Alto | 1–2 meses | R$ 15.000–30.000 | Módulo crítico impactado ou prazo do go-live ameaçado |
| 5 | Muito Alto | > 2 meses ou inviabilização | > R$ 30.000 | Projeto cancelado ou prazo estratégico perdido |

### 1.3 Nível de Risco (Score P×I)

| Faixa | Nível | Cor de referência |
|---|---|---|
| 16–25 | CRÍTICO | Vermelho |
| 9–15 | ALTO | Laranja |
| 5–8 | MÉDIO | Amarelo |
| 1–4 | BAIXO | Verde |

---

## 2. Registro de Riscos — Task 1: Identificação

### Tabela de Riscos Identificados

| ID | Categoria | Descrição do Risco | P | I | Score | Nível |
|---|---|---|---|---|---|---|
| RSK-001 | Governança / Sponsor | Sponsor de nível Diretor ou superior não identificado até a data de kick-off (CB-01 aberta), bloqueando a autorização formal do TAP, aprovação de orçamento e todas as decisões de escopo ao longo do projeto | 4 | 5 | **20** | **CRÍTICO** |
| RSK-002 | Financeiro | Orçamento de R$ 100.000 insuficiente para o escopo real de 6 módulos web com UAT, migração de dados e infraestrutura, resultando em necessidade de aporte adicional não previsto ou corte de escopo | 4 | 4 | **16** | **CRÍTICO** |
| RSK-003 | Prazo | Atraso acumulado no caminho crítico (desenvolvimento sequencial M1→M6) que consome o buffer de 3,5 semanas e ameaça o go-live de 07/12/2026, comprometendo o Prêmio Inovação de janeiro/2027 | 4 | 5 | **20** | **CRÍTICO** |
| RSK-004 | Técnico | Complexidade do M3 (Motor de Fluxo de Aprovação) subestimada na estimativa — regras de aprovação por gestor de área e aprovação de investimento requerem motor de workflow mais elaborado que o estimado, gerando atraso de 2–4 semanas no caminho crítico | 4 | 4 | **16** | **CRÍTICO** |
| RSK-005 | Fornecimento | Modelo de desenvolvimento não definido (interno / externo / misto) — ausência de decisão atrasa contratação ou alocação de equipe, impactando diretamente o início das fases de desenvolvimento | 3 | 4 | **12** | **ALTO** |
| RSK-006 | Escopo | Scope creep — requisitos adicionais inseridos sem aprovação formal (novos campos de ideia, integrações informais, dashboards não previstos no ERF v2) consumindo orçamento e prazo sem contrapartida aprovada | 3 | 4 | **12** | **ALTO** |
| RSK-007 | Técnico | Dados históricos da plataforma SaaS atual não exportáveis no formato esperado ou com volume/qualidade incompatível para migração automatizada, exigindo migração manual parcial ou perda de dados históricos | 3 | 3 | **9** | **ALTO** |
| RSK-008 | Adoção | Baixa adoção pelos gestores de área no fluxo de aprovação de ideias (M3) — resistência ao novo processo, não utilização da plataforma após o go-live, comprometendo o retorno esperado do programa de inovação e o critério CS-03 | 3 | 4 | **12** | **ALTO** |
| RSK-009 | Qualidade | Retrabalho intenso no UAT — não-conformidades identificadas com volume ou severidade superior ao previsto, consumindo parte significativa do buffer de 3,5 semanas e pressionando o prazo de go-live | 3 | 4 | **12** | **ALTO** |
| RSK-010 | Governança | Processo de inovação do grupo não está documentado (premissa P-04 falha) — critérios de aprovação de ideias, responsáveis por nível e fluxo completo precisam ser construídos durante o projeto, gerando retrabalho na especificação do M3 e M4 | 3 | 3 | **9** | **ALTO** |
| RSK-011 | Conformidade | Falha de conformidade com LGPD — dados pessoais de colaboradores (ideias vinculadas a autores identificáveis) tratados sem adequação à política de privacidade do grupo, gerando risco regulatório e retrabalho de arquitetura | 2 | 4 | **8** | **MÉDIO** |
| RSK-012 | Fornecimento | Fornecedor SaaS atual interrompe ou degrada o serviço antes do go-live da plataforma própria — o contrato vigente pode ser encerrado prematuramente ou sofrer aumento de preço/mudança de condições durante o período de desenvolvimento | 2 | 4 | **8** | **MÉDIO** |

---

## 3. Heatmap de Riscos

```
IMPACTO →
         1-Muito Baixo  2-Baixo  3-Médio  4-Alto  5-Muito Alto
5-M.Alta |             |        |        |        |            |
4-Alta   |             |        |        | RSK-002| RSK-001    |
         |             |        |        | RSK-004| RSK-003    |
3-Média  |             |        | RSK-007| RSK-005| RSK-006    |
         |             |        | RSK-010| RSK-008|            |
         |             |        |        | RSK-009|            |
2-Baixa  |             |        |        | RSK-011|            |
         |             |        |        | RSK-012|            |
1-M.Baixa|             |        |        |        |            |
```

**Zona CRÍTICA (≥16):** RSK-001, RSK-002, RSK-003, RSK-004
**Zona ALTA (9–15):** RSK-005, RSK-006, RSK-007, RSK-008, RSK-009, RSK-010
**Zona MÉDIA (5–8):** RSK-011, RSK-012

---

## 4. Plano de Resposta aos Riscos — Task 2

---

### RSK-001 — Sponsor Não Identificado (CRÍTICO | P×I = 20)

**Categoria:** Governança / Sponsor
**Estratégia:** Evitar — criar condição estrutural para que o risco não se materialize antes do prazo de impacto

**Gatilho de ativação:** Ausência de sponsor identificado até 2026-05-31 (D-24 do kick-off previsto) — qualquer dia sem confirmação formal após essa data ativa o plano de contingência

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-01.1 | Elaborar comunicação formal de escalada para a alta direção, assinada por Marcelo Silveira (GP VMO), apresentando os riscos financeiros e estratégicos de manter o TAP sem sponsor e sem assinatura — incluir cálculo de impacto diário de atraso no Prêmio Inovação jan/2027 | Marcelo Silveira (GP VMO) | 2026-05-23 |
| AP-01.2 | Solicitar a Jadson (Gestor de Inovação) que identifique e apresente formalmente três candidatos a sponsor de nível Diretor ou superior, com indicação da área de maior interesse na plataforma (inovação, TI, RH) | Jadson (Gestor de Inovação) | 2026-05-28 |
| AP-01.3 | Agendar reunião executiva entre Marcelo Silveira e o candidato a sponsor com maior aderência, apresentando resumo executivo do projeto (benefício R$85k/ano, payback 14 meses, ROI +70%) para facilitar a decisão | Marcelo Silveira (GP VMO) + Jadson | 2026-06-05 |
| AP-01.4 | Monitorar semanalmente o status de CB-01 e reportar ao comitê de portfólio (caso exista) até a resolução | Marcelo Silveira (GP VMO) | Semanal até resolução |

**Plano de Contingência:** Se sponsor não for identificado até 2026-06-15 (D-9 do kick-off), Marcelo Silveira solicita ao solicitante Jadson autorização para propor redesenho do projeto como piloto interno de menor escopo (3 módulos M1-M3) com orçamento reduzido de R$ 40.000, permitindo início com aprovação de nível gerencial enquanto o sponsor é identificado para a fase completa. Em paralelo, considera-se a possibilidade de adiamento do kick-off para setembro/2026, aceitando a perda do Prêmio Inovação jan/2027 como impacto documentado e aprovado formalmente.

---

### RSK-002 — Orçamento Insuficiente (CRÍTICO | P×I = 16)

**Categoria:** Financeiro
**Estratégia:** Mitigar — estruturar o orçamento com visibilidade de custo real antes do início, não durante

**Gatilho de ativação:** Qualquer proposta de fornecedor de desenvolvimento acima de R$ 65.000 para os 6 módulos, ou variância acumulada de custo superior a 10% do orçamento base (R$ 83.000) em qualquer fase do projeto

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-02.1 | Realizar processo formal de cotação com no mínimo 3 fornecedores de desenvolvimento antes do kick-off, utilizando o escopo do ERF como base — validar se R$ 65.000 é suficiente para 6 módulos com as funcionalidades especificadas | Marcelo Silveira (GP VMO) + Jadson | 2026-06-10 |
| AP-02.2 | Estabelecer controle mensal de custos acumulados vs. orçamento aprovado, com alerta automático ao sponsor quando variância atingir 5% | Marcelo Silveira (GP VMO) | A partir do kick-off |
| AP-02.3 | Mapear, antes da contratação do fornecedor, os itens de custo variável (licenças de terceiros, serviços de cloud, ferramentas de teste) que podem crescer durante o projeto e incluir teto explícito no contrato | ARQ (a designar) + GP VMO | 2026-06-20 |
| AP-02.4 | Negociar contrato de desenvolvimento com cláusula de preço fixo por módulo, com aprovação de aditivo obrigatória para qualquer escopo adicional | Marcelo Silveira (GP VMO) + Jurídico | 2026-06-20 |

**Plano de Contingência:** Se o orçamento projetado no final da Fase 2 (Especificação) ultrapassar R$ 95.000, acionar reunião de emergência com sponsor para: (a) aprovação de aporte adicional de até R$ 20.000 — decisão documentada em ata — ou (b) corte de escopo da versão 1 priorizando M1, M2, M3 e M6 (dashboard), adiando M4 e M5 para versão 1.1, ou (c) substituição de funcionalidades complexas por soluções de menor custo de desenvolvimento.

---

### RSK-003 — Atraso Acumulado no Caminho Crítico (CRÍTICO | P×I = 20)

**Categoria:** Prazo
**Estratégia:** Mitigar — estabelecer pontos de controle intermediários com ação corretiva automática

**Gatilho de ativação:** Qualquer marco intermediário (M2 a M5) com atraso superior a 5 dias úteis em relação ao baseline do cronograma, ou consumo de mais de 50% do buffer de 3,5 semanas antes de 2026-11-07

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-03.1 | Implementar reunião semanal de acompanhamento de prazo com a equipe de desenvolvimento — revisão do caminho crítico e atualização do % de conclusão de cada pacote de trabalho | Marcelo Silveira (GP VMO) | A partir do kick-off |
| AP-03.2 | Estabelecer "semáforo de prazo" mensal: verde (0–5d de variância), amarelo (6–10d), vermelho (>10d) — em amarelo, GP elabora plano de recuperação; em vermelho, aciona sponsor para decisão de escopo ou prazo | Marcelo Silveira (GP VMO) | A partir do kick-off |
| AP-03.3 | Fixar marcos intermediários como pontos de go/no-go formais: M2 (04/set), M3 (09/out), M4 (13/nov) — atraso em qualquer marco acima de 10 dias ativa revisão de cronograma com sponsor | Marcelo Silveira (GP VMO) + Sponsor | Definido no kick-off |
| AP-03.4 | Incluir no contrato com o fornecedor cláusulas de entrega parcial por módulo com datas e critérios de aceite claros — penalidades progressivas por atraso nos marcos contratualmente definidos | GP VMO + Jurídico | Na contratação |

**Plano de Contingência:** Se o atraso acumulado ultrapassar 10 dias úteis no Marco M3 (09/out) ou M4 (13/nov), acionar o plano de fast-track: (a) paralelizar desenvolvimento de M5 e M6 com alocação de desenvolvedor adicional (custo estimado R$ 8.000–12.000 da reserva de contingência), ou (b) reduzir escopo do M6 (Dashboard) eliminando funcionalidades de exportação PDF/Excel para versão 1.1, ou (c) formalmente revisar a data de go-live para 31/12/2026 (prazo máximo contratual) e comunicar o impacto ao Prêmio Inovação jan/2027.

---

### RSK-004 — Complexidade do M3 Subestimada (CRÍTICO | P×I = 16)

**Categoria:** Técnico
**Estratégia:** Mitigar — investigar a complexidade real antes do início do desenvolvimento

**Gatilho de ativação:** Arquiteto de Solução (ARQ) identifica durante a fase de especificação (Fase 2) que o motor de aprovação requer mais de 2 estados de fluxo por nível hierárquico, ou que a regra de aprovação de investimento varia por divisão, ou que o volume de notificações exige arquitetura de filas

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-04.1 | Incluir no Workshop de Requisitos M3 (tarefa 2.1.2, semana 2 de jul/2026) sessão específica de mapeamento de todos os estados possíveis do fluxo de aprovação, com o Gestor de Inovação (Jadson) e pelo menos 2 gestores de área — documentar: níveis de aprovação, regras de exceção, aprovações paralelas ou sequenciais | ARQ (a designar) + Jadson | 2026-07-15 |
| AP-04.2 | Realizar spike técnico de 3 dias (protótipo de motor de workflow) durante a Fase 2, antes do sign-off do ERF v2, para validar a viabilidade técnica dentro do prazo e custo estimados | ARQ (a designar) | 2026-07-18 |
| AP-04.3 | Avaliar uso de biblioteca de workflow open-source comprovada (ex: ativiti, temporalio, ou equivalente) em vez de desenvolvimento do motor do zero, reduzindo risco técnico de M3 | ARQ (a designar) | 2026-07-20 |

**Plano de Contingência:** Se o spike técnico (AP-04.2) confirmar que o motor de aprovação requer mais de 4 semanas de desenvolvimento (acima do estimado de 2,5 semanas para a fase 5), acionar revisão do cronograma com as seguintes opções: (a) realocar 1 desenvolvedor adicional exclusivamente para M3 (+R$ 5.000–8.000) aprovado pelo sponsor, ou (b) simplificar o fluxo de aprovação para versão 1 — aprovação em 1 único nível (gestor de inovação) — e implementar fluxo multinível em versão 1.1 pós go-live.

---

### RSK-005 — Modelo de Desenvolvimento Não Definido (ALTO | P×I = 12)

**Categoria:** Fornecimento
**Estratégia:** Evitar — decidir o modelo antes do kick-off para eliminar o risco

**Gatilho de ativação:** Ausência de decisão formal sobre o modelo de desenvolvimento (interno/externo/misto) até 2026-06-10 (D-14 do kick-off)

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-05.1 | Elaborar análise comparativa de 3 modelos (interno, externo com preço fixo, squad misto) com estimativa de custo, risco e prazo para cada um — apresentar ao sponsor como subsídio para decisão | Marcelo Silveira (GP VMO) | 2026-06-03 |
| AP-05.2 | Se modelo externo for escolhido, iniciar processo de seleção e cotação imediatamente após a aprovação do TAP (CB-01/CB-02 resolvidas), com prazo máximo de contratação até 2026-06-17 | GP VMO + Jurídico | 2026-06-17 |

**Plano de Contingência:** Se a decisão de modelo não ocorrer até 2026-06-10, o GP VMO adota provisoriamente o modelo externo (fornecedor único com preço fixo por módulo) e inicia o processo de cotação em paralelo à resolução das CBs, para não perder tempo assim que o sponsor for identificado.

---

### RSK-006 — Scope Creep (ALTO | P×I = 12)

**Categoria:** Escopo
**Estratégia:** Evitar + Mitigar — controle rigoroso de mudanças estruturado desde o início

**Gatilho de ativação:** Qualquer solicitação de funcionalidade não prevista no ERF v2 aprovado, ou qualquer "ajuste" informal acordado entre o time de inovação e o fornecedor sem registro e aprovação do GP VMO

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-06.1 | Implantar processo formal de controle de mudanças com formulário de solicitação de mudança (RFC — Request for Change), análise de impacto em prazo e custo, e aprovação obrigatória do sponsor para mudanças de impacto ≥ R$ 2.000 ou ≥ 3 dias de prazo | Marcelo Silveira (GP VMO) | Kick-off |
| AP-06.2 | Comunicar formalmente a todos os stakeholders (incluindo Jadson e gestores de área) que o escopo está congelado após o sign-off do ERF v2 — novas solicitações entram no backlog para versão 1.1 | GP VMO | 2026-07-24 (sign-off ERF) |
| AP-06.3 | Incluir cláusula anti-scope-creep no contrato com o fornecedor: qualquer funcionalidade não prevista no ERF v2 requer ordem de serviço adicional com aprovação escrita do GP VMO | GP VMO + Jurídico | Na contratação |

**Plano de Contingência:** Se scope creep identificado com impacto acumulado > R$ 10.000 ou > 15 dias de prazo, acionar reunião de revisão de escopo com sponsor para decidir entre: (a) aprovação de aditivo de orçamento e/ou prazo, ou (b) remoção de funcionalidades originais de menor prioridade para acomodar as novas, mantendo custo e prazo.

---

### RSK-007 — Migração de Dados Históricos com Falha (ALTO | P×I = 9)

**Categoria:** Técnico
**Estratégia:** Mitigar — levantar a situação real antes de assumir viabilidade

**Gatilho de ativação:** Fornecedor SaaS confirma que os dados históricos não estão disponíveis em formato CSV/JSON (premissa P-06 falha), ou o volume de dados é superior a 10.000 registros sem estrutura mapeada

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-07.1 | Contatar o fornecedor SaaS atual imediatamente após o kick-off para validar: (a) formatos disponíveis de exportação, (b) volume estimado de dados históricos, (c) estrutura dos dados (campos e relações) | Jadson + GP VMO | 2026-07-03 |
| AP-07.2 | Incluir no ERF v2 (Workshop M1/M2) o mapeamento de campos da plataforma SaaS vs. campos da nova plataforma, definindo regras de transformação e identificando dados sem correspondência | ARQ + Jadson | 2026-07-15 |
| AP-07.3 | Definir, antes do início do desenvolvimento, se a migração será automatizada (script) ou manual parcial — e alocar esforço/custo correspondente no plano de projeto | ARQ + GP VMO | 2026-07-31 |

**Plano de Contingência:** Se os dados históricos não forem exportáveis ou forem de qualidade insuficiente, adotar a abordagem de "migração seletiva": importar apenas os dados críticos para o Prêmio Inovação (ideias aprovadas dos últimos 2 anos com status e ganhos registrados) via processo manual controlado, e manter o restante na plataforma SaaS em modo de leitura por 12 meses pós go-live antes do encerramento definitivo do contrato.

---

### RSK-008 — Baixa Adoção pelos Gestores de Área (ALTO | P×I = 12)

**Categoria:** Adoção
**Estratégia:** Mitigar — engajar gestores de área como co-criadores antes do go-live

**Gatilho de ativação:** Menos de 50% dos gestores de área convidados para o UAT comparecendo, ou feedback negativo generalizado (NPS < 5) na validação do protótipo com usuários-chave (tarefa 2.2.4)

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-08.1 | Incluir pelo menos 2 gestores de área (diferentes divisões) na validação do protótipo de alta fidelidade (tarefa 2.2.4 — jul/2026) para garantir que o fluxo de aprovação atende à realidade operacional deles antes do desenvolvimento | Jadson + GP VMO | 2026-07-31 |
| AP-08.2 | Elaborar plano de comunicação e engajamento de mudança: comunicado executivo do sponsor apresentando a plataforma, vídeo de 3 minutos demonstrando o fluxo de aprovação, e FAQ para gestores de área — publicar 2 semanas antes do go-live | GP VMO + Jadson | 2026-11-23 |
| AP-08.3 | Realizar treinamento presencial ou ao vivo (não apenas documentação) com gestores de área antes do go-live — mínimo 1 hora de treinamento com simulação do fluxo real de aprovação | GP VMO + Jadson | 2026-11-24 a 2026-12-03 |
| AP-08.4 | Designar "campeões de inovação" por divisão (1 por área, indicado pelo gestor de inovação) para servir de referência e multiplicador do uso da plataforma nos primeiros 60 dias | Jadson | 2026-12-07 (go-live) |

**Plano de Contingência:** Se 30 dias após o go-live a taxa de adoção de aprovações pelos gestores de área for inferior a 40% (abaixo da meta de 70% do CS-03), acionar plano de adoção emergencial: (a) comunicação direta do sponsor cobrando o uso da plataforma como processo obrigatório do programa de inovação, com prazo definido, e (b) round adicional de treinamentos personalizados por divisão.

---

### RSK-009 — Retrabalho Intenso no UAT (ALTO | P×I = 12)

**Categoria:** Qualidade
**Estratégia:** Mitigar — prevenir via qualidade contínua no desenvolvimento

**Gatilho de ativação:** Mais de 20 não-conformidades identificadas na execução do UAT (tarefa 9.2.2), ou qualquer não-conformidade classificada como "crítica" (bloqueio de funcionalidade principal do fluxo M1→M3→M6) no UAT

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-09.1 | Exigir cobertura de testes unitários e integração ≥ 80% como critério de aceite de cada módulo (M1 a M6) antes de avançar para o módulo seguinte — sem esta cobertura, o módulo não é considerado entregue | QA (a designar) | Por módulo entregue |
| AP-09.2 | Realizar mini-UAT ao final de cada marco de módulo (M2, M3, M4) com pelo menos 2 usuários representativos, antecipando a detecção de não-conformidades antes do UAT formal | Jadson + QA | Ao final de M2, M3 e M4 |
| AP-09.3 | Preparar ambiente e dados de UAT realistas (amostra dos dados da plataforma SaaS atual) — UAT com dados fictícios tende a não refletir os problemas reais do fluxo | QA + INF | 2026-11-16 |

**Plano de Contingência:** Se o volume de não-conformidades no UAT ultrapassar a capacidade de correção na janela de 2 dias (tarefa 9.2.3), utilizar o buffer de 3,5 semanas (2026-11-23 a 2026-12-04) como janela de correção e reteste — este é exatamente o cenário para o qual o buffer foi dimensionado. Se mesmo assim houver não-conformidades críticas abertas em 2026-12-04, acionar sponsor para decidir entre: (a) go-live parcial com módulos aprovados no UAT e liberação gradual dos demais, ou (b) adiamento do go-live para dentro da folga residual (até 31/12/2026).

---

### RSK-010 — Processo de Inovação Não Documentado (ALTO | P×I = 9)

**Categoria:** Governança
**Estratégia:** Mitigar — levantar a lacuna antes do início da especificação

**Gatilho de ativação:** No Workshop de Requisitos M3 (tarefa 2.1.2), equipe de inovação não consegue responder às perguntas de fluxo: "quem aprova?", "quais os critérios de aprovação por nível?", "o que acontece quando o gestor rejeita uma ideia?"

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-10.1 | Solicitar a Jadson, antes do kick-off, o envio de toda documentação existente sobre o processo de inovação atual: manual de fluxo, critérios de aprovação, formulários vigentes na plataforma SaaS | Jadson | 2026-06-17 |
| AP-10.2 | Se a documentação for inexistente ou insuficiente, alocar 2 dias de workshop de mapeamento de processo (business process mapping) antes dos workshops de requisitos — a equipe de inovação + 1 analista de negócios documentam o processo "as is" e o "to be" | GP VMO + Jadson | 2026-07-06 a 2026-07-07 |

**Plano de Contingência:** Se o processo não estiver documentado e o mapeamento revelar processos divergentes por divisão (cada área aprova de um jeito diferente), definir processo padrão unificado em conjunto com Jadson e o sponsor antes de especificar o M3 — aceitar que a plataforma vai padronizar o processo (oportunidade de melhoria) e comunicar isso como mudança gerenciada para os gestores de área.

---

### RSK-011 — Falha de Conformidade com LGPD (MÉDIO | P×I = 8)

**Categoria:** Conformidade
**Estratégia:** Mitigar — incorporar LGPD como requisito não-funcional desde a especificação

**Gatilho de ativação:** Equipe jurídica identifica no workshop de requisitos que dados de colaboradores (nome vinculado à ideia, histórico de participação, avaliações dos gestores) não possuem base legal mapeada ou mecanismo de anonimização

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-11.1 | Incluir o Jurídico/Compliance nos workshops de requisitos para validar o tratamento de dados pessoais de cada módulo — identificar quais dados são pessoais, qual a base legal de tratamento, e definir os controles de privacidade (anonimização, consentimento, direito de exclusão) | Jurídico + ARQ | 2026-07-15 |
| AP-11.2 | Incluir requisitos de LGPD no ERF v2 como requisitos não-funcionais obrigatórios — arquitetura da plataforma deve prever perfis de acesso segregados, logs de auditoria e mecanismo de exclusão de dados a pedido | ARQ | 2026-07-24 |

**Plano de Contingência:** Se após a avaliação jurídica for identificada inconsistência com a LGPD na arquitetura proposta, solicitar revisão arquitetural (estimativa: 1–2 semanas de retrabalho) dentro do buffer disponível, e atrasar a contratação do fornecedor até a arquitetura estar validada pelo jurídico.

---

### RSK-012 — Fornecedor SaaS Atual Interrompido Antes do Go-Live (MÉDIO | P×I = 8)

**Categoria:** Fornecimento
**Estratégia:** Transferir + Mitigar — garantir contratualmente a continuidade até o go-live

**Gatilho de ativação:** Fornecedor SaaS notifica encerramento de contrato com menos de 60 dias de antecedência, ou apresenta aumento de preço acima de 20% exigindo renegociação imediata

**Ações Preventivas:**

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| AP-12.1 | Verificar o contrato vigente com o fornecedor SaaS atual — prazo de vigência, cláusulas de rescisão, e notificação de encerramento — e garantir que o contrato esteja ativo pelo menos até 31/01/2027 | Jadson + Jurídico | 2026-06-10 |
| AP-12.2 | Se necessário, renovar o contrato SaaS por período mínimo (6 meses) explicitando que é renovação de transição — documentar o custo como parte do projeto PROJ-2026-006 (não como custo operacional recorrente) | Jadson + Jurídico | 2026-06-20 |

**Plano de Contingência:** Se o fornecedor SaaS encerrar o contrato prematuramente, implementar medida de emergência: exportar imediatamente todos os dados disponíveis (backups completos) e operacionalizar um processo manual transitório via planilha para registro de ideias e aprovações, até o go-live da nova plataforma — processo manual documentado e comunicado aos usuários.

---

## 5. Reserva de Contingência — Cálculo por VME

### 5.1 Definição Metodológica

**VME (Valor Monetário Esperado)** = Probabilidade (%) × Impacto Financeiro Estimado

O impacto financeiro estimado considera:
- Custo direto de correção do risco (horas extras, fornecedor adicional, retrabalho)
- Custo indireto de atraso (para RSK-001 e RSK-003: perda do Prêmio Inovação = perda de economia de R$ 85.000 no primeiro ano)
- Custo de conformidade para RSK-011

### 5.2 VME por Risco CRÍTICO e ALTO

| ID | Risco | Nível | P (%) | Impacto Financeiro Est. | VME |
|---|---|---|---|---|---|
| RSK-001 | Sponsor não identificado — inviabiliza o projeto ou força redesenho | CRÍTICO | 80% | R$ 100.000 | **R$ 80.000** |
| RSK-003 | Atraso no caminho crítico — perda do Prêmio Inovação jan/2027 + custo de aceleração | CRÍTICO | 80% | R$ 85.000 | **R$ 68.000** |
| RSK-002 | Orçamento insuficiente — aporte adicional ou corte de escopo | CRÍTICO | 80% | R$ 30.000 | **R$ 24.000** |
| RSK-004 | Complexidade M3 — desenvolvedor adicional ou simplificação de escopo | CRÍTICO | 80% | R$ 20.000 | **R$ 16.000** |
| RSK-008 | Baixa adoção — perda parcial do benefício anual de R$ 85.000 | ALTO | 60% | R$ 40.000 | **R$ 24.000** |
| RSK-005 | Modelo dev indefinido — atraso de contratação + sobrecusto de urgência | ALTO | 60% | R$ 25.000 | **R$ 15.000** |
| RSK-006 | Scope creep — custo de funcionalidades não orçadas | ALTO | 60% | R$ 20.000 | **R$ 12.000** |
| RSK-009 | Retrabalho UAT — horas extras de desenvolvimento e teste | ALTO | 60% | R$ 20.000 | **R$ 12.000** |
| RSK-007 | Migração de dados — esforço de migração manual + risco de perda | ALTO | 60% | R$ 15.000 | **R$ 9.000** |
| **TOTAL VME** | | | | | **R$ 260.000** |

### 5.3 Interpretação e Recomendação

O VME bruto agregado de **R$ 260.000** reflete a exposição máxima teórica do projeto se todos os riscos se materializassem com sua probabilidade e impacto máximos. Na prática:

- RSK-001 e RSK-003 possuem forte correlação: se o sponsor não for identificado (RSK-001), o projeto provavelmente não começa e RSK-003 não se materializa independentemente
- A reserva aprovada no TAP de **R$ 17.000 (20% do orçamento base)** cobre apenas os riscos de execução de menor magnitude (RSK-004, RSK-006, RSK-007, RSK-009)

**Recomendação de reserva:**

| Camada | Finalidade | Valor |
|---|---|---|
| Reserva de contingência aprovada no TAP | Riscos de execução identificados (RSK-004, RSK-007, RSK-009, parte do RSK-006) | R$ 17.000 |
| Reserva adicional recomendada | Cobertura parcial de RSK-002 (orçamento), RSK-008 (adoção) e RSK-005 (fornecimento) | **R$ 10.000** |
| **Reserva total recomendada** | | **R$ 27.000 (32,5% do orçamento base)** |

> RSK-001 e RSK-003 possuem natureza estratégica e não são cobertos por reserva de contingência — eles requerem ação preventiva imediata (escalada ao sponsor, controle de prazo). Se materializados em sua plenitude, o projeto precisará de decisão executiva de redesenho, não apenas de aplicação de reserva.

---

## 6. Oportunidades Identificadas

> Pedro Perigo — Princípio 3: Risco e oportunidade — ambos devem ser documentados.

| ID | Oportunidade | Condição de Realização | Potencial de Ganho |
|---|---|---|---|
| OPO-001 | Entrega antecipada do go-live (antes de 07/12/2026) — permite que o Prêmio Inovação jan/2027 tenha dados reais da nova plataforma em vez de dados migrados | Buffer de 3,5 semanas não precisar ser totalmente consumido (riscos mitigados com sucesso) | Dados qualitativamente superiores para o Prêmio Inovação; NPS interno potencialmente mais alto |
| OPO-002 | Eliminação antecipada do contrato SaaS — se a migração for concluída e a plataforma go-live antes de 31/12/2026, encerrar o contrato SaaS com até 1 mês de antecedência | Go-live em novembro/2026 | Economia adicional de até R$ 7.500 (1 mês de licença SaaS) |
| OPO-003 | Processo de inovação padronizado como subproduto do M3 — a especificação do fluxo de aprovação pode resultar em um manual do processo de inovação unificado para todas as divisões | Envolvimento ativo dos gestores de área nos workshops de M3 | Redução de inconsistências de aprovação entre divisões; apoio ao Prêmio Inovação |
| OPO-004 | Plataforma como produto replicável — se o projeto for entregue com sucesso, a VMO Consultoria pode oferecer a plataforma como produto de gestão de inovação para outros clientes | Qualidade de código e documentação suficiente para replicação | Novo ativo comercial para a VMO; possível modelo de licença SaaS própria |

---

## 7. Monitoramento e Revisão

### 7.1 Frequência de Revisão do Registro de Riscos

| Evento | Ação |
|---|---|
| Semanal (reunião de acompanhamento) | Verificar gatilhos dos riscos CRÍTICOS e ALTOS; atualizar status (Identificado / Em monitoramento / Materializado / Encerrado) |
| A cada marco de módulo (M2 a M5) | Revisão completa do registro de riscos — novos riscos podem surgir; riscos encerrados devem ser fechados |
| Quando gatilho for ativado | Acionar plano de contingência imediatamente; comunicar sponsor se risco for CRÍTICO ou ALTO |
| Encerramento do projeto | Registrar quais riscos se materializaram, qual foi o custo real e lições aprendidas para projetos futuros |

### 7.2 Responsabilidades

| Papel | Responsabilidade |
|---|---|
| Marcelo Silveira (GP VMO) | Dono do registro de riscos; aciona planos de contingência; reporta ao sponsor |
| Sponsor (a designar) | Decisão sobre riscos CRÍTICOS que requerem mudança de escopo, prazo ou orçamento |
| Jadson (Gestor de Inovação) | Monitorar riscos de adoção (RSK-008) e migração (RSK-007); prover informações sobre processo de inovação |
| ARQ (a designar) | Monitorar riscos técnicos (RSK-004, RSK-007, RSK-011) |
| Jurídico | Monitorar RSK-011 (LGPD) e RSK-012 (contrato SaaS) |

---

## 8. Checklist de Qualidade do Plano de Riscos

- [x] Mínimo 8 riscos com P, I e score calculado — **12 riscos documentados**
- [x] Todos os CRÍTICOS e ALTOS com gatilho e plano de contingência — **RSK-001 a RSK-010 com gatilho e contingência**
- [x] Riscos cobrindo ao menos 4 categorias — **6 categorias: Governança/Sponsor, Técnico, Prazo, Financeiro, Adoção, Conformidade/Fornecimento**
- [x] Reserva de contingência calculada com VME por risco — **VME calculado para todos os 9 riscos CRÍTICOS e ALTOS; total R$ 260.000; reserva recomendada R$ 27.000**
- [x] Responsável e prazo de ação preventiva definidos para todos os riscos

---

*Documento elaborado por: Pedro Perigo — Analista de Riscos | VMO Autônomo (VMO Consultoria)*
*Versão 1.0 — 2026-05-16 | PROJ-2026-006*
*Referência metodológica: PMBOK 7ª edição — Domínio de Desempenho de Incerteza e Risco*
