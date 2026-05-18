# Work Request (Mini-RFP)
## PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação

**Emitido por:** VMO Consultoria — Fábio Fornecedor (Especialista em Mini-RFP)
**Data de Emissão:** 18/05/2026
**Versão:** 1.0
**Status:** Aguardando Propostas

---

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Informação |
|---|---|
| **ID do Projeto** | PROJ-2026-004 |
| **Nome do Projeto** | Plataforma Interna de Gestão de Ideias de Inovação |
| **Cliente** | Grupo Águia Branca — Área de Inovação |
| **Solicitante** | Jadson (Área de Inovação — Grupo Águia Branca) |
| **Sponsor** | A DEFINIR ⚠️ CB-01 — Condição Bloqueante (ver Seção 8) |
| **Gestor do Projeto (VMO)** | A designar |
| **Orçamento Máximo Aprovado** | R$ 90.000,00 (noventa mil reais) |
| **Prazo de Go-Live** | 30/11/2026 |
| **Evento Marco** | Prêmio Inovação Grupo Águia Branca — Janeiro/2027 |
| **Tipo de Solução** | Desenvolvimento de plataforma web interna (SaaS próprio) |
| **Data de Emissão do WR** | 18/05/2026 |
| **Prazo Máximo para Submissão de Propostas** | 06/06/2026 |

---

## 2. CONTEXTO E JUSTIFICATIVA

O Grupo Águia Branca mantém atualmente uma plataforma terceirizada de gestão de ideias de inovação, cuja licença anual representa um desembolso recorrente estimado entre **R$ 80.000,00 e R$ 90.000,00 por ano**. Essa dependência de fornecedor externo impõe limitações de customização, restrições de integração com o ecossistema tecnológico do Grupo e custos crescentes sem correspondente ganho de aderência funcional às necessidades específicas da operação.

A Área de Inovação do Grupo identificou a oportunidade estratégica de substituir essa plataforma por uma **solução própria, desenvolvida sob medida**, o que permitirá:

- **Eliminar o custo recorrente de licença** estimado em R$ 80–90K/ano, gerando ROI positivo já no primeiro ano de operação;
- **Adequar totalmente os fluxos de trabalho** — campanhas, desafios, aprovação de ideias e gestão de projetos — ao processo real do time de inovação;
- **Escalar sem custo adicional** de licença conforme o crescimento da base de usuários;
- **Preparar infraestrutura** para suportar o Prêmio Inovação de janeiro/2027, principal evento de reconhecimento do programa de inovação corporativa.

O retorno sobre investimento no **Ano 1** é estimado em positivo já no primeiro ciclo de renovação evitada, uma vez que o custo de desenvolvimento (≤ R$ 90.000,00) é equivalente ou inferior à licença anual da plataforma atual. A partir do **Ano 2**, a economia líquida projetada é de R$ 80.000,00 a R$ 90.000,00 ao ano.

---

## 3. OBJETIVO DA CONTRATAÇÃO

Contratar empresa especializada em desenvolvimento de software para **projetar, construir, testar e implantar** uma plataforma web interna de gestão de ideias de inovação para o Grupo Águia Branca, compreendendo:

- Portal web responsivo para submissão e acompanhamento de ideias por colaboradores;
- Módulo de campanhas e desafios configurável pela equipe de inovação;
- Fluxo estruturado de aprovação com governança por papel (gestor, time de inovação, administrador);
- Módulo de mini gestão de projetos para ideias aprovadas e em execução;
- Módulo de mensuração e registro de ganhos obtidos;
- Dashboard executivo com métricas do pipeline de inovação;
- Controle de acesso baseado em papéis (RBAC) com suporte a 10.000+ usuários cadastrados e 500 usuários simultâneos sem degradação de performance.

A solução deve estar pronta para operação plena em **30/11/2026**, possibilitando a apresentação dos resultados no Prêmio Inovação de janeiro/2027.

---

## 4. ESCOPO DA CONTRATAÇÃO

### 4.1 Escopo Incluso

O fornecedor contratado deverá entregar integralmente os seguintes requisitos funcionais, identificados no Estudo de Requisitos Funcionais (ERF) do projeto:

| ID | Requisito | Descrição |
|---|---|---|
| **RF001** | Portal web responsivo — Cadastro de Ideias | Portal web acessível em dispositivos desktop e mobile (via browser) para submissão de ideias com campos de descrição, ganhos esperados e benefícios. |
| **RF002** | Campos obrigatórios da submissão | Formulário de cadastro de ideia com os seguintes campos obrigatórios: título, categoria, área proponente, colaborador proponente, descrição do problema, solução proposta e ganhos esperados. |
| **RF003** | Upload de anexos por ideia | Funcionalidade de upload de arquivos por ideia, suportando formatos PDF, imagens (JPG, PNG) e apresentações (PPT, PPTX). |
| **RF004** | Módulo de Campanhas e Desafios | Módulo configurável pelo time de inovação para criação e gestão de campanhas temáticas e desafios, com definição de período, público-alvo e critérios de participação. |
| **RF005** | Fluxo de Aprovação de Ideias | Workflow de aprovação pelo gestor da área proponente, com ações de aprovação, rejeição e solicitação de ajustes, incluindo registro de justificativa em cada decisão. |
| **RF006** | Notificações automáticas por e-mail | Disparo automático de notificações por e-mail para proponentes e gestores em eventos-chave do ciclo de vida da ideia (submissão, aprovação, rejeição, ajuste solicitado, conclusão). |
| **RF007** | Módulo de Mini Gestão de Projetos | Módulo para acompanhamento de ideias aprovadas em execução, com campos de responsável, prazo, status, etapas/tarefas e percentual de avanço. |
| **RF008** | Módulo de Mensuração de Ganhos | Módulo para registro e acompanhamento dos ganhos efetivamente obtidos com a implementação de ideias aprovadas (ganhos financeiros, operacionais, qualitativos). |
| **RF009** | Dashboard Executivo | Painel gerencial com métricas do pipeline de inovação: total de ideias submetidas, em avaliação, aprovadas, em execução, concluídas, canceladas, ganhos realizados e outros KPIs definidos com o cliente. |
| **RF010** | Controle de Acesso por Papel (RBAC) | Sistema de controle de acesso com quatro perfis mínimos: Colaborador (proponente), Gestor de Área (aprovador), Time de Inovação (administração de campanhas e pipeline) e Administrador do Sistema. |
| **RF011** | Capacidade e Performance | Plataforma dimensionada para suportar base de 10.000+ usuários cadastrados e picos de 500 usuários simultâneos sem degradação de tempo de resposta (SLA de performance a ser definido com o fornecedor). |
| **RF012** | Exportação de Relatórios | Funcionalidade de exportação de relatórios e dados em formatos PDF e XLSX a partir do dashboard e dos módulos da plataforma. |

### 4.2 Escopo Excluso

Os itens a seguir estão **explicitamente fora do escopo** desta contratação. Propostas que condicionarem a entrega dos requisitos acima à inclusão dos itens abaixo serão desclassificadas.

| # | Item Excluído | Observação |
|---|---|---|
| **EX-01** | Integração com sistemas legados (ERP, RH, folha de pagamento) | A plataforma operará de forma standalone. Integrações futuras poderão ser contratadas em escopo separado. |
| **EX-02** | Aplicativo mobile nativo (iOS e/ou Android) | A responsividade do portal web (RF001) atende ao acesso mobile via browser. App nativo não está no escopo desta fase. |
| **EX-03** | Migração de dados da plataforma terceirizada atual | Eventuais dados históricos da plataforma atual não serão migrados nesta contratação. |
| **EX-04** | Suporte pós-implantação além dos 90 dias de garantia | O período de garantia de 90 dias (Seção 9) cobre correção de bugs. Contrato de suporte continuado é escopo separado. |
| **EX-05** | Hospedagem e infraestrutura de produção | A infraestrutura de produção é de responsabilidade exclusiva da TI do Grupo Águia Branca (ver Premissas). |
| **EX-06** | Treinamento presencial para todos os colaboradores | O escopo inclui treinamento para usuários-chave (train-the-trainer). Disseminação ampla para todos os colaboradores é responsabilidade do Grupo. |

---

## 5. PREMISSAS E RESPONSABILIDADES DO GRUPO ÁGUIA BRANCA

O cumprimento do cronograma e do orçamento desta contratação está condicionado ao atendimento das premissas abaixo pelo Grupo Águia Branca. A inobservância de qualquer premissa poderá ensejar reprogramação de prazo e/ou revisão de escopo, sem ônus para o fornecedor.

| # | Premissa | Responsável |
|---|---|---|
| **P-01** | A TI do Grupo Águia Branca provisionará a infraestrutura de produção (servidores, banco de dados, domínio interno, certificados SSL) dentro do prazo necessário para o go-live em 30/11/2026. | TI — Grupo Águia Branca |
| **P-02** | A TI do Grupo provisionará um ambiente de homologação (staging) equivalente ao de produção, disponível até 30/08/2026 para início do ciclo de UAT do Marco 1. | TI — Grupo Águia Branca |
| **P-03** | Jadson e o time de inovação estarão disponíveis para sessões de UAT (Teste de Aceitação do Usuário) conforme cronograma acordado, com SLA de retorno de feedbacks em até 5 dias úteis por ciclo. | Jadson / Time de Inovação |
| **P-04** | A documentação da plataforma terceirizada atual (fluxos, campos, relatórios) será disponibilizada ao fornecedor até 5 dias úteis após o kickoff, como referência de requisitos. | Jadson / Time de Inovação |
| **P-05** | O Sponsor do projeto será definido e formalmente comunicado ao fornecedor até a data do kickoff (CB-01 — ver Seção 8). A ausência de Sponsor é condição bloqueante para início do projeto. | Grupo Águia Branca (Diretoria) |
| **P-06** | Decisões de aprovação de escopo, aceite de entregáveis e liberação de pagamentos por marcos terão prazo máximo de 10 dias úteis após submissão formal pelo fornecedor. | Sponsor / Jadson |
| **P-07** | O Grupo designará pelo menos um ponto focal técnico da TI para suporte ao fornecedor durante a fase de configuração de ambiente e deploy. | TI — Grupo Águia Branca |

---

## 6. CRONOGRAMA ESPERADO

| Marco | Descrição | Data Esperada |
|---|---|---|
| **M0 — Kickoff** | Reunião de início do projeto, alinhamento de escopo, apresentação de equipes e planejamento detalhado. | 20/06/2026 |
| **M1 — Portal + Cadastro de Ideias** | Entrega de RF001, RF002, RF003, RF010 (parcial) e RF006 (parcial). Portal web responsivo funcional com cadastro de ideias e upload de anexos. | 15/08/2026 |
| **M2 — Módulo Campanhas + Aprovação** | Entrega de RF004, RF005, RF006 (completo) e RF010 (completo). Módulo de campanhas configurável e fluxo de aprovação com notificações. | 30/09/2026 |
| **M3 — Gestão de Projetos + Métricas** | Entrega de RF007, RF008, RF009 e RF012. Módulo de mini gestão de projetos, mensuração de ganhos, dashboard executivo e exportação de relatórios. | 31/10/2026 |
| **M4 — UAT + Correções** | Ciclo completo de Teste de Aceitação do Usuário com o time de inovação. Correção de não conformidades identificadas. Aceite formal do cliente. | 15/11/2026 |
| **M5 — Go-Live** | Implantação em ambiente de produção, ativação da plataforma para todos os usuários e encerramento da fase de implantação. | 30/11/2026 |

> **Atenção:** O prazo de submissão de propostas é **06/06/2026**. Propostas recebidas após essa data não serão consideradas neste processo.

---

## 7. ENTREGÁVEIS OBRIGATÓRIOS

Todos os entregáveis listados abaixo são mandatórios. O aceite é **binário (Aceito / Não Aceito)** — não haverá aceite parcial. O fornecedor só terá direito ao pagamento do marco correspondente após o aceite formal de todos os entregáveis associados.

| # | Entregável | Marco | Critério de Aceite |
|---|---|---|---|
| **E-01** | Documento de Especificação Funcional (DEF) | M0/M1 | 100% dos RF001–RF012 detalhados com casos de uso, regras de negócio e protótipos de tela validados pelo cliente. Aceito somente com assinatura de aprovação de Jadson. |
| **E-02** | Documento de Arquitetura Técnica | M0/M1 | Diagrama de arquitetura, stack tecnológica, modelo de dados e estratégia de segurança documentados. Aprovado pelo ponto focal técnico da TI do Grupo. |
| **E-03** | Portal Web + Módulo Cadastro de Ideias (RF001–RF003) | M1 | Funcional em ambiente de homologação, todos os campos obrigatórios (RF002) presentes e operacionais, upload de anexos funcionando. Zero bugs críticos ou bloqueadores abertos. |
| **E-04** | Controle de Acesso RBAC (RF010) | M1 | Quatro perfis implementados e validados. Acesso indevido entre perfis não ocorre em nenhum dos casos de teste executados. |
| **E-05** | Módulo de Campanhas e Desafios (RF004) | M2 | Criação, edição, ativação e encerramento de campanhas operacionais. Configuração de período e público-alvo funcionando. Validado pelo time de inovação. |
| **E-06** | Fluxo de Aprovação de Ideias (RF005) | M2 | Aprovação, rejeição e solicitação de ajustes operacionais. Histórico de decisões registrado. Validado com cenários de teste documentados. |
| **E-07** | Notificações por E-mail (RF006) | M2 | Disparo automático em todos os eventos mapeados. Taxa de entrega ≥ 98% nos testes executados. Templates validados pelo cliente. |
| **E-08** | Módulo de Mini Gestão de Projetos (RF007) | M3 | Criação de projetos a partir de ideias aprovadas, atribuição de responsável, prazo e tarefas operacionais. Validado pelo time de inovação. |
| **E-09** | Módulo de Mensuração de Ganhos (RF008) | M3 | Registro e visualização de ganhos por ideia/projeto operacional. Campos de ganho financeiro, operacional e qualitativo presentes e funcionando. |
| **E-10** | Dashboard Executivo (RF009) | M3 | Métricas do pipeline exibidas corretamente com dados de teste. Exportação em PDF e XLSX (RF012) funcional para todos os relatórios. |
| **E-11** | Relatório de Testes (RT) | M4 | Cobertura de 100% dos requisitos funcionais. Resultados documentados. Zero bugs críticos ou bloqueadores em aberto na data do aceite. |
| **E-12** | Aceite Formal de UAT | M4 | Documento de aceite assinado por Jadson e/ou Sponsor, atestando conformidade da plataforma com os requisitos do ERF. |
| **E-13** | Plano de Implantação (Deploy) | M4 | Plano documentado de ativação em produção, incluindo rollback, janela de manutenção e checklist de go-live. Aprovado pela TI do Grupo. |
| **E-14** | Manual do Usuário e Documentação Técnica | M4 | Manual de usuário por perfil (colaborador, gestor, time de inovação, administrador). Documentação técnica (API, banco de dados, arquitetura) entregue em formato digital. |
| **E-15** | Plataforma em Produção (Go-Live) | M5 | Plataforma acessível a todos os usuários em URL de produção. Performance validada (RF011): tempo de resposta ≤ 3 segundos para 95% das transações com 500 usuários simultâneos. |
| **E-16** | Plano de Sustentação pós-Go-Live | M5 | Documento com procedimentos de manutenção, monitoramento e escalonamento de incidentes para o período de garantia de 90 dias. |

---

## 8. GOVERNANÇA E COMUNICAÇÃO

### 8.1 Condição Bloqueante — CB-01: Definição do Sponsor

⚠️ **A ausência de Sponsor formalmente designado pelo Grupo Águia Branca é uma condição bloqueante para o início do projeto.** O kickoff não ocorrerá sem a indicação formal do Sponsor. O fornecedor selecionado será notificado sobre o desdobramento desta condição até a data de kickoff prevista (20/06/2026).

### 8.2 Estrutura de Governança

| Papel | Responsabilidade |
|---|---|
| **Sponsor (Grupo Águia Branca)** | Aprovação de marcos, resolução de impasses, autorização de mudanças de escopo. |
| **Ponto Focal do Cliente (Jadson)** | Validação de requisitos, participação em UAT, aceite de entregáveis funcionais. |
| **Gestor do Projeto (VMO)** | Coordenação do projeto, gestão de riscos, interface entre cliente e fornecedor. |
| **Gerente de Projeto (Fornecedor)** | Planejamento detalhado, gestão da equipe técnica, reporte de status e gestão de issues. |

### 8.3 Cadência de Comunicação

| Reunião | Frequência | Participantes | Objetivo |
|---|---|---|---|
| Status Report Semanal | Semanal | GP VMO + GP Fornecedor | Acompanhamento de progresso, riscos e impedimentos. |
| Comitê de Projeto | Quinzenal | Sponsor + Jadson + GP VMO + GP Fornecedor | Decisões estratégicas, mudanças de escopo, aprovação de marcos. |
| Reunião de Marco | A cada marco | Todas as partes | Apresentação e aceite formal do entregável do marco. |
| Reunião de UAT | Conforme cronograma | Jadson + Time de Inovação + Equipe Fornecedor | Execução e validação dos testes de aceitação. |

### 8.4 Gestão de Mudanças

Qualquer alteração de escopo, prazo ou orçamento deverá ser formalizada via **Solicitação de Mudança (Change Request — CR)**, com análise de impacto pelo fornecedor e aprovação pelo Sponsor antes da implementação. Mudanças não aprovadas formalmente não serão executadas nem remuneradas.

---

## 9. CONDIÇÕES COMERCIAIS

### 9.1 Orçamento e Modelo de Faturamento

O valor máximo desta contratação é de **R$ 90.000,00 (noventa mil reais)**, com faturamento vinculado ao aceite formal de cada marco, conforme tabela abaixo:

| Marco | Entregável Principal | % do Valor Total | Valor Indicativo (base R$ 90K) | Condição de Pagamento |
|---|---|---|---|---|
| **M1** | Portal + Cadastro de Ideias (RF001–RF003, RF010 parcial) | 20% | R$ 18.000,00 | Aceite formal dos entregáveis E-01 a E-04 |
| **M2** | Módulo Campanhas + Aprovação (RF004–RF006, RF010 completo) | 25% | R$ 22.500,00 | Aceite formal dos entregáveis E-05 a E-07 |
| **M3** | Gestão de Projetos + Métricas (RF007–RF009, RF012) | 25% | R$ 22.500,00 | Aceite formal dos entregáveis E-08 a E-10 |
| **M4** | UAT + Correções + Documentação | 20% | R$ 18.000,00 | Aceite formal dos entregáveis E-11 a E-14 |
| **M5** | Go-Live + Plano de Sustentação | 10% | R$ 9.000,00 | Aceite formal dos entregáveis E-15 e E-16 |
| **TOTAL** | | **100%** | **R$ 90.000,00** | |

> Os percentuais e valores indicativos acima servem como referência. O fornecedor poderá propor distribuição diferente, desde que justificada e não superior ao teto de R$ 90.000,00.

### 9.2 Prazo de Pagamento

O pagamento de cada marco será realizado em até **15 (quinze) dias corridos** após o aceite formal documentado pelo cliente, mediante emissão de Nota Fiscal pelo fornecedor.

### 9.3 Penalidades

| Evento | Penalidade |
|---|---|
| Atraso na entrega de marco (por semana ou fração) | 1% do valor do marco, limitado a 10% |
| Não conformidade recorrente (3ª rejeição do mesmo entregável) | Direito de rescisão contratual sem ônus para o Grupo |
| Indisponibilidade da plataforma em produção por falha do fornecedor durante a garantia | SLA de restauração de 4h para incidentes críticos; multa de R$ 500/hora excedente |

### 9.4 Garantia

O fornecedor deverá prover **garantia técnica de 90 (noventa) dias** a partir da data de go-live (30/11/2026), cobrindo:

- Correção de bugs e não conformidades identificados em produção;
- Suporte técnico por e-mail e/ou ticket com SLA de primeira resposta em até 4 horas úteis para severidade crítica e 24 horas úteis para demais severidades;
- Sem custo adicional para o Grupo Águia Branca.

O período de garantia **não** inclui novas funcionalidades, mudanças de escopo ou adequações regulatórias surgidas após o go-live.

---

## 10. ARTEFATO OBRIGATÓRIO — CONFORMIDADE DA PROPOSTA

**Este artefato é de preenchimento obrigatório pelo fornecedor.** A proposta que não apresentar este artefato completamente preenchido será **automaticamente desclassificada**, independentemente de seu conteúdo técnico ou comercial.

O fornecedor deve preencher a coluna **Status** (OK / NOK) e a coluna **Observações** para cada item. Para itens com status NOK, a justificativa na coluna Observações é obrigatória.

---

### GRUPO 1 — IDENTIFICAÇÃO DA PROPOSTA (6 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **1.1** | Nome completo do fornecedor (Razão Social e CNPJ) está identificado na proposta | | |
| **1.2** | Projeto/Demanda ao qual a proposta se refere está claramente identificado (PROJ-2026-004) | | |
| **1.3** | Tipo de solução proposta está descrito (ex.: desenvolvimento sob demanda, produto customizável, SaaS próprio) | | |
| **1.4** | Data de recebimento/emissão da proposta está registrada | | |
| **1.5** | Versão da proposta está identificada | | |
| **1.6** | Prazo de validade da proposta está declarado (mínimo 30 dias corridos a partir da data de submissão) | | |

---

### GRUPO 2 — ESCOPO DA SOLUÇÃO PROPOSTA (6 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **2.1** | O objetivo da contratação foi descrito e reflete o entendimento correto da demanda (Seção 3 deste WR) | | |
| **2.2** | Todas as funcionalidades (RF001 a RF012) foram detalhadas individualmente na proposta, com descrição da abordagem de atendimento a cada requisito | | |
| **2.3** | Os módulos e componentes da solução estão listados e mapeados aos requisitos funcionais deste WR | | |
| **2.4** | As integrações previstas (ou a ausência delas, conforme escopo excluso) estão descritas na proposta | | |
| **2.5** | Os relatórios e funcionalidades de exportação (RF012) estão descritos, com indicação de formatos suportados | | |
| **2.6** | A necessidade ou ausência de licenças de software de terceiros está informada, com detalhamento de custo e responsabilidade pela aquisição | | |

---

### GRUPO 3 — EXCLUSÕES DE ESCOPO (2 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **3.1** | As exclusões de escopo da proposta estão listadas de forma explícita, contemplando no mínimo as exclusões EX-01 a EX-06 deste WR | | |
| **3.2** | As exclusões são descritas de forma objetiva e específica, sem uso de frases genéricas do tipo "itens não mencionados neste documento" ou equivalentes | | |

---

### GRUPO 4 — PREMISSAS DA PROPOSTA (3 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **4.1** | As premissas técnicas adotadas pelo fornecedor estão declaradas (ex.: versões de tecnologia, ambiente, browser suportados) | | |
| **4.2** | As premissas de acesso e colaboração do cliente estão declaradas (ex.: disponibilidade de ambiente, ponto focal, prazo de retorno de feedbacks) | | |
| **4.3** | As premissas de aprovação e governança estão declaradas (ex.: prazo máximo para aceite de entregáveis, processo de change request) | | |

---

### GRUPO 5 — METODOLOGIA DE TRABALHO (3 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **5.1** | A metodologia de desenvolvimento está definida na proposta (ex.: Scrum, Kanban, modelo híbrido) com cadência de sprints/ciclos e cerimônias previstas | | |
| **5.2** | As etapas do projeto estão descritas (ex.: levantamento, design, desenvolvimento, testes, homologação, go-live) com duração estimada para cada fase | | |
| **5.3** | O processo de validação e aceite de entregáveis está descrito, incluindo ciclos de feedback, critérios de aceite e gestão de não conformidades | | |

---

### GRUPO 6 — ENTREGÁVEIS DA PROPOSTA (9 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **6.1** | A proposta prevê entrega de Especificação Funcional (DEF) ou documento equivalente com detalhamento de casos de uso, regras de negócio e protótipos | | |
| **6.2** | A proposta prevê entrega de Especificação Técnica com arquitetura da solução, stack tecnológica, modelo de dados e estratégia de segurança | | |
| **6.3** | A proposta prevê entrega de documentação técnica completa (manual de instalação, documentação de API, dicionário de dados) | | |
| **6.4** | A proposta prevê entrega de Plano de Testes com cobertura dos requisitos funcionais (RF001–RF012) e cenários de teste documentados | | |
| **6.5** | A proposta prevê entrega de Relatório de Testes com resultados, evidências e status de cada caso de teste executado | | |
| **6.6** | A proposta prevê entrega de Plano de Implantação (deploy em produção) com procedimento de rollback e checklist de go-live | | |
| **6.7** | A proposta prevê entrega de Plano de Suporte e SLAs durante o período de garantia (90 dias pós-go-live) | | |
| **6.8** | A proposta prevê entrega de Plano de Repasse de Conhecimento (train-the-trainer) com manual do usuário por perfil | | |
| **6.9** | A proposta prevê envio de Status Reports periódicos conforme cadência definida em Governança (Seção 8.3) | | |

---

### GRUPO 7 — GESTÃO DO PROJETO (3 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **7.1** | A proposta apresenta Matriz RACI com papéis e responsabilidades do fornecedor e do cliente para as atividades-chave do projeto | | |
| **7.2** | A proposta apresenta Matriz de Riscos com identificação, probabilidade, impacto e plano de mitigação dos principais riscos do projeto | | |
| **7.3** | A proposta apresenta Plano de Comunicação com canais, frequência e responsáveis pelas comunicações do projeto | | |

---

### GRUPO 8 — CRONOGRAMA E EQUIPE (5 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **8.1** | O prazo de entrega proposto é compatível com o go-live em 30/11/2026, respeitando os marcos definidos na Seção 6 deste WR | | |
| **8.2** | O cronograma macro está apresentado com datas de início e fim de cada fase, compatível com os marcos M1 a M5 | | |
| **8.3** | Os marcos de entrega e seus critérios de aceite estão descritos na proposta e alinhados com a Seção 7 deste WR | | |
| **8.4** | A composição da equipe do fornecedor está declarada (cargos, senioridade e dedicação percentual ao projeto) | | |
| **8.5** | O prazo de mobilização da equipe está declarado (tempo entre assinatura do contrato e início efetivo das atividades) | | |

---

### GRUPO 9 — CONDIÇÕES COMERCIAIS (4 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **9.1** | O valor total da proposta está declarado e é igual ou inferior ao orçamento máximo de R$ 90.000,00 | | |
| **9.2** | O modelo de faturamento por marcos está descrito, com indicação do valor ou percentual de cada parcela vinculada a cada marco de entrega | | |
| **9.3** | Os critérios de validação e aceite para liberação de cada pagamento de marco estão descritos na proposta | | |
| **9.4** | O prazo de pagamento esperado pelo fornecedor após o aceite de cada marco está declarado | | |

---

### GRUPO 10 — PENALIDADES, GARANTIA E SUSTENTAÇÃO (4 itens)

| ID | Item de Conformidade | Status (OK/NOK) | Observações |
|---|---|---|---|
| **10.1** | A proposta declara aceite das condições de penalidade por atraso definidas na Seção 9.3 deste WR, ou apresenta contraproposta justificada | | |
| **10.2** | A proposta declara o período de garantia (mínimo 90 dias após go-live) e as condições de cobertura (tipos de ocorrências cobertas e exclusões) | | |
| **10.3** | Os SLAs de suporte durante o período de garantia estão declarados (tempo de primeira resposta e resolução por severidade de incidente) | | |
| **10.4** | A proposta apresenta Plano de Sustentação pós-go-live com procedimentos de monitoramento, manutenção preventiva e escalonamento de incidentes | | |

---

### Resumo de Conformidade (a preencher pelo fornecedor)

| Grupo | Total de Itens | Itens OK | Itens NOK |
|---|---|---|---|
| Grupo 1 — Identificação | 6 | | |
| Grupo 2 — Escopo | 6 | | |
| Grupo 3 — Exclusões | 2 | | |
| Grupo 4 — Premissas | 3 | | |
| Grupo 5 — Metodologia | 3 | | |
| Grupo 6 — Entregáveis | 9 | | |
| Grupo 7 — Gestão | 3 | | |
| Grupo 8 — Cronograma e Equipe | 5 | | |
| Grupo 9 — Condições Comerciais | 4 | | |
| Grupo 10 — Penalidades e Garantia | 4 | | |
| **TOTAL** | **45** | | |

> **Atenção:** Propostas com mais de 3 itens NOK nos Grupos 2 (Escopo) ou 8 (Cronograma e Equipe) serão eliminadas da avaliação, independentemente da pontuação nos demais grupos.

---

## 11. PROCESSO DE SUBMISSÃO

### 11.1 Prazo

As propostas devem ser submetidas até **06/06/2026, às 18h00 (horário de Brasília)**. Propostas recebidas após este prazo não serão consideradas, sem exceções.

### 11.2 Formato de Entrega

- As propostas devem ser entregues em formato **PDF**, organizadas conforme a estrutura de seções deste WR;
- O **Artefato de Conformidade (Seção 10)** deve ser entregue em arquivo separado (PDF ou XLSX);
- Documentos de apoio (portfólio, certificações, referências) podem ser enviados como anexos adicionais.

### 11.3 Canal de Submissão

As propostas devem ser enviadas exclusivamente por e-mail ao Gestor do Projeto da VMO Consultoria, com cópia para Jadson (Grupo Águia Branca). Os endereços serão comunicados aos fornecedores habilitados mediante convite formal.

### 11.4 Esclarecimentos

Dúvidas sobre este Work Request devem ser enviadas até **30/05/2026**. As respostas serão consolidadas e enviadas a todos os fornecedores convidados até **03/06/2026**, garantindo isonomia no processo.

### 11.5 Critérios de Avaliação

As propostas serão avaliadas com base nos seguintes critérios:

| Critério | Peso |
|---|---|
| Conformidade técnica (cobertura dos RF001–RF012) | 40% |
| Adequação do cronograma e plano de projeto | 25% |
| Valor total e modelo de faturamento | 20% |
| Qualificação da equipe e portfólio de projetos similares | 15% |

### 11.6 Resultado

O resultado da avaliação será comunicado aos fornecedores participantes até **13/06/2026**, com kickoff previsto para **20/06/2026**.

---

## CONTROLE DO DOCUMENTO

| Versão | Data | Autor | Descrição da Alteração |
|---|---|---|---|
| 1.0 | 18/05/2026 | Fábio Fornecedor (VMO Consultoria) | Emissão inicial |

---

*Work Request emitido pela VMO Consultoria em nome do Grupo Águia Branca — Área de Inovação.*
*Documento confidencial — uso restrito aos fornecedores convidados para este processo.*
