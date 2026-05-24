# Documentação Base — PROJ-2026-006
## Plataforma Própria de Gestão de Ideias e Inovação

**Versão:** 1.0
**Data de elaboração:** 2026-05-16
**Elaborado por:** Diana Documento — Arquiteta de Projetos VMO Autônomo
**Status:** Aguardando assinatura do Sponsor (condição bloqueante CB-01)

---

# PARTE 1 — TERMO DE ABERTURA DO PROJETO (TAP)

> Referência metodológica: PMBOK 7ª edição

---

## 1. Identificação do Projeto

| Campo | Valor |
|---|---|
| Código | PROJ-2026-006 |
| Nome | Plataforma Própria de Gestão de Ideias e Inovação |
| Tipo | Melhoria — substituição de solução SaaS terceira por desenvolvimento interno |
| Origem | DEM-2026-006 — demanda qualificada em 2026-05-16 |
| Decisão de qualificação | APROVADO COM CONDIÇÕES — 21/30 (70%) |
| Solicitante | Jadson — Gestor de Inovação |
| Sponsor | **[A DEFINIR — Diretor ou superior, conforme condição bloqueante CB-01]** |
| Gerente de Projeto | A designar após aprovação formal do TAP |
| Data de início prevista | Após resolução das condições bloqueantes CB-01 e CB-02 |
| Data de conclusão prevista | 31 de dezembro de 2026 |

---

## 2. Objetivo SMART

**Desenvolver e implantar, até 31 de dezembro de 2026, uma plataforma web própria de gestão de ideias e inovação com os 6 módulos funcionais (M1 a M6), eliminando o contrato de licenciamento SaaS terceiro e gerando economia anual de R$85.000, com payback projetado em 14 meses e ROI positivo de +70% ao longo de 24 meses.**

| Dimensão SMART | Verificação |
|---|---|
| Específico (S) | Plataforma web com 6 módulos definidos (M1-M6), substituindo SaaS atual |
| Mensurável (M) | Economia anual de R$85k; payback em 14 meses; ROI +70% em 24 meses |
| Atingível (A) | Investimento de R$100k com 20% de contingência; equipe interna + fornecedor |
| Relevante (R) | Reduz custo, aumenta flexibilidade e suporta o Prêmio Inovação jan/2027 |
| Temporal (T) | Prazo de entrega: 31/12/2026; marco vinculado: lançamento jan/2027 |

---

## 3. Justificativa e Necessidade de Negócio

A VMO Consultoria (grupo) opera atualmente com plataforma SaaS terceira para gestão do programa de inovação corporativa, incorrendo em custo anual de **R$80.000 a R$90.000** em licenciamento. O modelo atual apresenta três limitações estruturais:

1. **Custo crescente:** o modelo de precificação por usuário inviabiliza a escalabilidade do programa sem aumento proporcional de licença.
2. **Baixa flexibilidade:** a solução terceira não permite customizações alinhadas ao processo de inovação do grupo, exigindo adaptação de processo ao sistema.
3. **Maturidade do programa:** o programa de inovação atingiu nível de maturidade que justifica investimento em solução proprietária, com retorno financeiro mensurável.

**Marco estratégico:** a plataforma deve estar operacional para suportar o **Prêmio Inovação** de janeiro de 2027, que demanda rastreabilidade de ideias, fluxo de aprovação e mensuração de ganhos.

---

## 4. Escopo do Projeto

### 4.1 Dentro do Escopo

| ID | Módulo | Descrição |
|---|---|---|
| M1 | Cadastro de Ideias | Formulário estruturado com campos: problema, ganhos esperados, benefícios e atributos de classificação |
| M2 | Campanhas e Desafios | Área para o time de inovação publicar desafios temáticos e campanhas abertas |
| M3 | Fluxo de Aprovação | Workflow de aprovação por gestores de área, com status rastreável por ideia |
| M4 | Mini Gestão de Projetos | Plano de ação macro para ideias aprovadas (responsáveis, prazos, entregas) |
| M5 | Mensuração de Ganhos | Registro e acompanhamento dos resultados financeiros e operacionais de ideias implementadas |
| M6 | Dashboard de Monitoramento | Painel consolidado de projetos de inovação em andamento, com indicadores-chave |

**Adicionalmente no escopo:**
- Infraestrutura de hospedagem e banco de dados da plataforma
- Testes de aceitação (UAT) com usuários finais
- Treinamento e documentação de uso para gestores e colaboradores
- Migração de dados históricos da plataforma SaaS atual (volume a levantar)
- Encerramentos contratuais com fornecedor SaaS atual

### 4.2 Fora do Escopo (versão 1)

| Exclusão | Justificativa |
|---|---|
| Integração com sistemas externos (ERP, HRIS, BI) | Explicitamente excluída da v1 — avaliação futura |
| Aplicativo mobile (iOS/Android) | Fora do escopo — apenas plataforma web responsiva |
| Módulos adicionais além de M1-M6 | Demanda futura; novas funcionalidades por solicitação formal |
| Customizações por divisão específica | Usuários de todas as divisões usam a mesma interface padrão |
| Suporte técnico continuado pós-entrega | Objeto de contrato de sustentação separado (pós-projeto) |
| Desenvolvimento de política de inovação | Responsabilidade da Área de Inovação; fora do escopo técnico |

---

## 5. Critérios de Sucesso Mensuráveis

| # | Critério | Meta | Como medir |
|---|---|---|---|
| CS-01 | Eliminação do custo de licença SaaS | Economia de R$85.000/ano a partir de jan/2027 | Comparativo de despesas anuais (2026 vs 2027) |
| CS-02 | Plataforma entregue no prazo | Go-live até 31/12/2026 | Data de aceite do Termo de Entrega assinado |
| CS-03 | Adoção pelos usuários | ≥ 70% dos gestores de área realizando aprovações pela plataforma em até 60 dias após o go-live | Relatório de logins e aprovações do sistema |
| CS-04 | Custo dentro do orçamento | Investimento total ≤ R$100.000 (incluindo contingência de 20%) | Relatório de custos acumulados ao encerramento |
| CS-05 | Satisfação dos usuários-chave | NPS interno ≥ 7 (pesquisa com gestores e time de inovação) | Pesquisa aplicada 30 dias após go-live |

---

## 6. Premissas

| # | Premissa |
|---|---|
| P-01 | O Sponsor de nível Diretor ou superior será identificado e formalizará o TAP antes do início do projeto |
| P-02 | O orçamento de R$100.000 (com 20% de contingência) será aprovado formalmente pelo Sponsor antes do kick-off |
| P-03 | A Área de Inovação (Jadson e equipe) estará disponível para co-design dos módulos, revisão de protótipos e validação de entregas ao longo do projeto |
| P-04 | O processo de inovação do grupo (critérios de aprovação, fluxos, responsáveis) está documentado e disponível para a equipe de desenvolvimento |
| P-05 | A plataforma SaaS atual permanecerá operacional em paralelo até o go-live, garantindo continuidade do programa de inovação durante o desenvolvimento |
| P-06 | Os dados históricos da plataforma SaaS são exportáveis em formato padrão (CSV/JSON) para fins de migração |

---

## 7. Restrições

| # | Restrição |
|---|---|
| R-01 | Prazo máximo de entrega: 31 de dezembro de 2026 — data vinculada ao Prêmio Inovação de janeiro/2027 e inegociável |
| R-02 | Teto orçamentário de R$100.000 — qualquer extrapolação requer aprovação formal do Sponsor |
| R-03 | Sem integrações com sistemas externos na versão 1 — requisito técnico deliberado para controle de escopo e prazo |
| R-04 | A plataforma deve ser desenvolvida em tecnologia mantida internamente ou por fornecedor com suporte de longo prazo (sem tecnologias experimental/end-of-life) |
| R-05 | Conformidade com LGPD — dados de colaboradores tratados pela plataforma devem seguir política de privacidade do grupo |

---

## 8. Stakeholders

| Nome / Papel | Categoria | Interesse | Nível de Influência |
|---|---|---|---|
| **[A DEFINIR] — Sponsor Executivo** (Diretor+) | Patrocinador | Retorno financeiro, alinhamento estratégico e autorização de recursos | Alto |
| **Jadson** — Gestor de Inovação | Solicitante / Cliente principal | Substituição da plataforma; melhoria de processo; suporte ao Prêmio Inovação | Alto |
| **Marcelo Silveira** — GP VMO | Gestor do Projeto | Entrega no prazo, custo e qualidade | Alto |
| **Gestores de Área** (todas as divisões) | Usuário-chave | Aprovação de ideias; facilidade de uso; visibilidade do fluxo | Médio |
| **Colaboradores do grupo** | Usuário final | Submissão de ideias; acompanhamento do status | Baixo-Médio |
| **Equipe de TI / Infraestrutura** | Suporte técnico | Hospedagem, segurança e integração de dados | Médio |
| **Fornecedor de desenvolvimento** (a contratar) | Executor | Entrega técnica dos módulos | Alto |
| **Fornecedor SaaS atual** | Parte afetada | Encerramento de contrato | Baixo |
| **Jurídico / Compliance** | Apoio | LGPD, encerramento de contrato SaaS, termos de uso | Médio |

---

## 9. Orçamento Estimado

> **CONDIÇÃO BLOQUEANTE CB-02:** O orçamento abaixo é estimado. A aprovação formal pelo Sponsor é condição obrigatória para o início do projeto (kick-off).

| Categoria | Valor Estimado |
|---|---|
| Desenvolvimento de software (M1-M6) | R$ 65.000 |
| Infraestrutura (hospedagem, banco de dados, segurança) | R$ 10.000 |
| Testes, UAT e correções | R$ 8.000 |
| Treinamento e documentação | R$ 4.000 |
| Gestão de projeto (VMO) | R$ 6.000 |
| **Subtotal** | **R$ 83.000** |
| **Reserva de contingência (20%)** | **R$ 17.000** |
| **TOTAL APROVADO ESTIMADO** | **R$ 100.000** |

**Benefício anual projetado:** R$85.000 (eliminação da licença SaaS)
**Payback:** aproximadamente 14 meses
**ROI em 24 meses:** +70%

---

## 10. Riscos de Alto Nível

| ID | Risco | Probabilidade | Impacto | Resposta preliminar |
|---|---|---|---|---|
| RI-01 | Sponsor não identificado até a data prevista de início, atrasando o kick-off | Alta | Alto | Escalada imediata pela GP VMO; definição de prazo-limite para o solicitante Jadson mobilizar a liderança |
| RI-02 | Escopo ampliado no desenvolvimento (scope creep) sem aprovação formal, estourando prazo ou orçamento | Média | Alto | Controle rigoroso de mudanças; qualquer requisito novo passa por análise de impacto e aprovação do Sponsor |
| RI-03 | Atraso na entrega pelo fornecedor de desenvolvimento comprometendo o prazo de 31/12/2026 | Média | Alto | Cláusulas de prazo no contrato de prestação de serviço; marcos intermediários com validação mensal |
| RI-04 | Baixa adoção pelos gestores de área após go-live, reduzindo o retorno esperado do programa de inovação | Média | Médio | Plano de comunicação e engajamento; treinamentos obrigatórios para gestores; suporte pós-go-live |
| RI-05 | Dados históricos da plataforma SaaS atual não são exportáveis ou estão em formato incompatível | Baixa | Médio | Levantar capacidade de exportação antes da rescisão do contrato SaaS; plano B de migração manual parcial |

---

## 11. Condições Bloqueantes

> As condições abaixo são pré-requisitos obrigatórios estabelecidos na qualificação DEM-2026-006 (aprovação com condições — Marcelo Silveira, GP VMO, 2026-05-16). O projeto NÃO pode ser iniciado enquanto ambas estiverem pendentes.

| ID | Condição | Status | Responsável | Prazo |
|---|---|---|---|---|
| **CB-01** | Identificação e formalização do Sponsor de nível Diretor ou superior, com assinatura do TAP | PENDENTE | Jadson + GP VMO | A definir |
| **CB-02** | Aprovação formal do orçamento de R$100.000 pelo Sponsor, antes do kick-off | PENDENTE | Sponsor (a definir) | A definir |

---

## 12. Autorizações

| Papel | Nome | Assinatura | Data |
|---|---|---|---|
| Sponsor | [A DEFINIR — CB-01] | _________________ | _________ |
| Solicitante | Jadson — Gestor de Inovação | _________________ | _________ |
| Gerente de Projeto VMO | Marcelo Silveira | _________________ | _________ |

---
---

# PARTE 2 — PM CANVAS

> Síntese estratégica do projeto — 9 blocos

---

## PROJ-2026-006 — Plataforma Própria de Gestão de Ideias e Inovação

| | | |
|---|---|---|
| **POR QUÊ** | **O QUÊ** | **QUEM (Clientes)** |
| A plataforma SaaS terceira custa R$80-90k/ano com escala limitada por usuário e baixa flexibilidade de customização. O grupo possui maturidade em inovação e precisa de solução proprietária que reduza custo, amplie controle e suporte o Prêmio Inovação de jan/2027. Benefício anual projetado: R$85k. Payback: 14 meses. ROI 24m: +70%. | Desenvolver plataforma web própria com 6 módulos: **M1** Cadastro de Ideias, **M2** Campanhas e Desafios, **M3** Fluxo de Aprovação, **M4** Mini Gestão de Projetos, **M5** Mensuração de Ganhos, **M6** Dashboard de Monitoramento. Plataforma web responsiva, sem integrações externas na v1, com migração de dados históricos. | **Primários:** Equipe de Inovação (Jadson e time) — gestão e publicação de campanhas. **Secundários:** Gestores de Área de todas as divisões — aprovação de ideias. **Terciários:** Colaboradores do grupo — submissão de ideias e acompanhamento. |
| **QUEM (Equipe)** | **COMO (Entregas)** | **QUANDO** |
| **Sponsor:** [A DEFINIR — Diretor+, CB-01]. **Solicitante/focal:** Jadson (Gestor de Inovação). **GP VMO:** Marcelo Silveira. **Equipe técnica:** Fornecedor de desenvolvimento (a contratar). **Apoio:** TI/Infra (hospedagem), Jurídico (LGPD e rescisão SaaS), Área de Inovação (validações e UAT). | **E1:** Arquitetura e protótipos validados (M1-M6). **E2:** Ambiente de desenvolvimento e infraestrutura provisionados. **E3:** Módulos M1-M3 desenvolvidos e testados. **E4:** Módulos M4-M6 desenvolvidos e testados. **E5:** UAT com usuários-chave concluído. **E6:** Treinamento e documentação entregues. **E7:** Go-live e encerramento do contrato SaaS. | **Kick-off:** após CB-01 e CB-02 resolvidas (previsto jun/2026). **M1:** Protótipos aprovados — jul/2026. **M2:** M1-M3 entregues — set/2026. **M3:** M4-M6 entregues — nov/2026. **M4:** UAT e correções — dez/2026. **GO-LIVE:** 31/12/2026. **Marco vinculado:** Prêmio Inovação — jan/2027. |
| **QUANTO** | **PREMISSAS** | **RESTRIÇÕES** |
| **Investimento total:** R$100.000 (inclui 20% de contingência — R$17k). Distribuição: Desenvolvimento R$65k / Infra R$10k / Testes R$8k / Treinamento R$4k / GP R$6k / Contingência R$17k. **Benefício anual:** R$85k (eliminação da licença SaaS). **Payback:** ~14 meses. **ROI 24m:** +70%. Orçamento pendente de aprovação formal pelo Sponsor (CB-02). | 1. Sponsor Diretor+ identificado e TAP assinado (CB-01). 2. Orçamento R$100k aprovado formalmente antes do kick-off (CB-02). 3. Jadson e equipe de inovação disponíveis para validações e co-design. 4. Processo de inovação documentado e acessível à equipe técnica. 5. Plataforma SaaS atual mantida em operação paralela até o go-live. | 1. Prazo máximo: 31/12/2026 — inegociável (vinculado ao Prêmio Inovação jan/2027). 2. Teto orçamentário: R$100.000 — extrapolações exigem aprovação do Sponsor. 3. Sem integrações com sistemas externos na v1. 4. Plataforma web apenas (sem app mobile). 5. Tecnologia com suporte de longo prazo (conformidade LGPD obrigatória). |

---
---

# PARTE 3 — PLANO GERAL DO PROJETO

> Referência: 10 planos subsidiários do PMBOK

---

## PG-01 — Plano de Gerenciamento do Escopo

**Abordagem:** O escopo é definido pelos 6 módulos funcionais (M1-M6) descritos no TAP. A EAP (Estrutura Analítica do Projeto) será elaborada com o fornecedor de desenvolvimento e validada por Jadson antes do início da fase de construção. Qualquer adição de funcionalidade fora dos módulos M1-M6 será tratada como mudança formal e submetida ao processo de controle de mudanças (PG-10). A validação do escopo ocorrerá em cada marco de entrega (E1 a E7) com aceite documentado pelo cliente (Jadson) e GP VMO.

**Ferramentas:** EAP detalhada por módulo; checklists de aceite por entregável; backlog de requisitos rastreável por módulo.

**Validação:** Aceite por entrega intermediária (E1-E7) com assinatura do responsável da Área de Inovação.

---

## PG-02 — Plano de Gerenciamento do Cronograma

**Abordagem:** O projeto será gerenciado em fases sequenciais com marcos de controle mensais. O prazo de 31/12/2026 é inegociável. O cronograma mestre será elaborado pelo GP VMO com o fornecedor de desenvolvimento após o kick-off, usando abordagem ágil adaptada (sprints quinzenais) dentro de marcos fixos.

**Marcos principais:**

| Marco | Data-alvo |
|---|---|
| Kick-off (após CB-01 e CB-02) | Jun/2026 |
| Protótipos M1-M6 aprovados | Jul/2026 |
| M1-M3 desenvolvidos e testados | Set/2026 |
| M4-M6 desenvolvidos e testados | Nov/2026 |
| UAT concluído e correções aplicadas | Dez/2026 |
| Go-live | 31/Dez/2026 |

**Controle:** Reuniões quinzenais de acompanhamento com fornecedor; relatório mensal de progresso ao Sponsor; alerta imediato para desvios superiores a 2 semanas.

---

## PG-03 — Plano de Gerenciamento dos Custos

**Abordagem:** O orçamento total aprovado estimado é de R$100.000 (incluindo 20% de contingência). Os custos serão monitorados mensalmente pelo GP VMO com comparativo previsto vs. realizado. O uso da reserva de contingência (R$17.000) requer aprovação do GP VMO e ciência do Sponsor. Qualquer custo adicional acima do teto exige aprovação formal do Sponsor (gatilho de mudança).

**Linha de base de custos:**

| Categoria | Orçamento |
|---|---|
| Desenvolvimento (M1-M6) | R$ 65.000 |
| Infraestrutura | R$ 10.000 |
| Testes e UAT | R$ 8.000 |
| Treinamento e documentação | R$ 4.000 |
| Gestão de Projeto VMO | R$ 6.000 |
| Contingência (20%) | R$ 17.000 |
| **Total** | **R$ 100.000** |

**KPI financeiro:** CPI (Cost Performance Index) monitorado mensalmente; alerta em CPI < 0,9.

---

## PG-04 — Plano de Gerenciamento da Qualidade

**Abordagem:** A qualidade será garantida por critérios de aceite definidos por módulo (M1-M6) antes do início do desenvolvimento, validados com Jadson e equipe de inovação. O processo inclui revisão de código pelo fornecedor, testes funcionais por módulo, UAT com usuários reais e critérios de aceite mensuráveis.

**Critérios de qualidade:**
- Todos os campos obrigatórios de M1 funcionais e validados
- Fluxo de aprovação (M3) com rastreabilidade completa de status
- Dashboard (M6) com atualização em tempo real (máx. 5 min de delay)
- Taxa de bugs críticos no UAT: zero para go-live
- Tempo de resposta da plataforma: < 3 segundos para operações padrão

**Ferramentas:** Checklists de teste por módulo; relatório de bugs por sprint; critérios de aceite documentados no contrato com fornecedor.

---

## PG-05 — Plano de Gerenciamento dos Recursos

**Abordagem:** Os recursos do projeto incluem equipe interna (GP VMO, Área de Inovação para validações) e fornecedor externo de desenvolvimento (a contratar via processo de aquisição — PG-08). A alocação de Jadson e equipe será parcial, estimada em 20% do tempo durante as fases de design, validação e UAT.

**Papéis e responsabilidades:**

| Papel | Responsabilidade | Alocação estimada |
|---|---|---|
| Sponsor (a definir) | Aprovação de recursos, decisões críticas, escalada | < 5% |
| GP VMO (Marcelo) | Gestão integral do projeto, relatórios, controle | 50-70% |
| Jadson — Gestor de Inovação | Validações, co-design, UAT, aceite formal | 20% |
| Equipe de Inovação | Testes de usuário, feedback de funcionalidades | 10% |
| TI/Infra | Provisionamento de ambiente, segurança | 10-15% (fases específicas) |
| Fornecedor de Desenvolvimento | Desenvolvimento técnico de todos os módulos | 100% (dedicado) |

---

## PG-06 — Plano de Gerenciamento das Comunicações

**Abordagem:** As comunicações serão estruturadas por público e frequência, garantindo transparência ao Sponsor e engajamento dos stakeholders-chave sem sobrecarga de informação.

**Matriz de comunicações:**

| Comunicação | Público | Frequência | Responsável | Canal |
|---|---|---|---|---|
| Relatório de status | Sponsor, Jadson | Mensal | GP VMO | E-mail + reunião |
| Reunião de acompanhamento | GP VMO + Fornecedor | Quinzenal | GP VMO | Videoconferência |
| Atualização de marcos | Sponsor | A cada marco | GP VMO | E-mail formal |
| Validação de protótipos | Jadson + equipe de inovação | Por entregável | GP VMO | Reunião + apresentação |
| Comunicado de go-live | Todos os colaboradores | Único (go-live) | Área de Inovação + GP VMO | E-mail corporativo |
| Reporte de riscos críticos | Sponsor | Sob demanda | GP VMO | Reunião urgente |

---

## PG-07 — Plano de Gerenciamento dos Riscos

**Abordagem:** Os riscos serão identificados, avaliados e monitorados durante todo o ciclo do projeto. O registro de riscos será atualizado mensalmente e revisado a cada marco. A reserva de contingência de R$17.000 cobre riscos de custo; riscos de prazo serão tratados com buffer de cronograma nas fases M4-M6.

**Registro de riscos (alto nível):**

| ID | Risco | P | I | Score | Resposta |
|---|---|---|---|---|---|
| RI-01 | Sponsor não identificado — atraso no kick-off | Alta | Alto | Crítico | Escalada imediata; prazo-limite para Jadson mobilizar Diretor |
| RI-02 | Scope creep sem controle formal | Média | Alto | Alto | Processo de mudanças ativo; qualquer novo requisito passa por análise de impacto |
| RI-03 | Atraso do fornecedor de desenvolvimento | Média | Alto | Alto | Cláusulas contratuais de prazo; marcos intermediários com penalidade |
| RI-04 | Baixa adoção pós-go-live | Média | Médio | Médio | Plano de comunicação; treinamento obrigatório; suporte nas primeiras 4 semanas |
| RI-05 | Dados SaaS não exportáveis | Baixa | Médio | Médio | Levantar exportação antes de encerrar contrato; plano B de migração manual |

**Limiares:** Riscos com score "Alto" ou "Crítico" reportados ao Sponsor imediatamente.

---

## PG-08 — Plano de Gerenciamento das Aquisições

**Abordagem:** O principal item de aquisição é o contrato com fornecedor de desenvolvimento de software (M1-M6). O processo de seleção ocorrerá após aprovação do TAP (kick-off) com prazo máximo de 3 semanas para contratação, dado o prazo restrito do projeto.

**Estratégia de aquisição:**
- **Modalidade:** Contratação de serviço de desenvolvimento — preço fixo por entregável (preferred) ou tempo e material com teto de gastos
- **Processo:** Briefing técnico → solicitação de proposta para 3 fornecedores pré-qualificados → avaliação por critério técnico (60%) e preço (40%) → negociação → contrato
- **Cláusulas críticas:** marcos de entrega com aceite; cláusula de prazo final (31/12/2026); propriedade intelectual 100% do grupo; suporte pós-entrega mínimo de 6 meses

**Encerramento de contrato SaaS atual:** Processo de rescisão a ser iniciado após go-live da plataforma própria, com sobreposição de 30 dias para garantia de continuidade.

---

## PG-09 — Plano de Gerenciamento dos Stakeholders

**Abordagem:** O engajamento dos stakeholders será gerenciado de forma diferenciada por nível de influência e interesse. O foco prioritário são: Sponsor (sem ele o projeto não começa), Jadson (representante do cliente) e Gestores de Área (adoção pós-go-live).

**Matriz de engajamento:**

| Stakeholder | Engajamento atual | Engajamento desejado | Estratégia |
|---|---|---|---|
| Sponsor (a definir) | Não identificado | Comprometido | Mobilização via Jadson e GP VMO — prioridade imediata |
| Jadson — Gestor de Inovação | Engajado | Comprometido (co-design ativo) | Reuniões de validação; autoridade formal em aceites |
| Gestores de Área | Neutro | Favorável | Comunicação de benefícios; treinamento antes do go-live |
| Colaboradores do grupo | Neutro | Consciente | Comunicado de lançamento; guia de uso simplificado |
| TI/Infra | Resistente (carga adicional) | Favorável | Reunião de alinhamento inicial; definição clara de escopo de responsabilidade |
| Fornecedor SaaS atual | Resistente (perda de contrato) | Gerenciado | Comunicação formal e respeitosa; processo de rescisão com aviso prévio contratual |

**Revisão:** Análise de engajamento revisada a cada marco de projeto.

---

## PG-10 — Plano de Gerenciamento de Mudanças

**Abordagem:** Todo o projeto opera sob controle formal de mudanças. Qualquer alteração de escopo, prazo ou custo — independente do tamanho — segue o fluxo abaixo. O objetivo é proteger o prazo de 31/12/2026 e o teto de R$100.000.

**Fluxo de controle de mudanças:**

```
Solicitação de mudança (qualquer stakeholder)
       |
       v
Registro formal pelo GP VMO (formulário de mudança)
       |
       v
Análise de impacto: escopo / prazo / custo / risco
       |
       v
Classificação:
  [Sem impacto] → GP VMO aprova e implementa
  [Impacto menor] → GP VMO + Jadson aprovam
  [Impacto em prazo/custo] → Sponsor aprova
       |
       v
Atualização dos documentos de projeto (TAP, Cronograma, Linha de base)
       |
       v
Comunicação aos stakeholders afetados
```

**Registro:** Todas as mudanças registradas no Log de Mudanças do projeto (número sequencial, data, impacto, decisão e responsável).

**Proteção ao prazo:** Mudanças que ameacem o marco de 31/12/2026 são classificadas automaticamente como impacto crítico e requerem decisão do Sponsor em até 48h.

---
---

## Consistência entre Documentos — Verificação Final

| Parâmetro | TAP | PM Canvas | Plano Geral |
|---|---|---|---|
| Prazo de entrega | 31/12/2026 | 31/12/2026 | 31/12/2026 |
| Orçamento total | R$100.000 | R$100.000 | R$100.000 |
| Módulos no escopo | M1-M6 | M1-M6 | M1-M6 |
| Sponsor | [A DEFINIR — CB-01] | [A DEFINIR — CB-01] | [A DEFINIR — CB-01] |
| Condição CB-01 | Registrada | Registrada (premissas) | Registrada (PG-09) |
| Condição CB-02 | Registrada | Registrada (premissas) | Registrada (PG-03) |
| Benefício anual | R$85.000 | R$85.000 | — (referenciado no PG-03) |

---

*Documento elaborado por Diana Documento — Arquiteta de Projetos VMO Autônomo*
*Data: 2026-05-16 | Versão: 1.0 | Status: Aguardando resolução de CB-01 e CB-02 para assinatura do TAP*
