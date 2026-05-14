# Documentacao Base de Iniciacao — Caminhos Estrategicos do ERP GAB

**ID Projeto:** PROJ-2026-003
**ID Demanda:** DEM-2026-003
**Versao:** 1.0
**Data:** 05/04/2026
**Elaborado por:** Diana Documento — Arquiteta de Projetos (VMO Autonomo)
**Run ID:** 2026-04-05-173000

---

# PARTE 1 — TERMO DE ABERTURA DO PROJETO (TAP)

## 1. Identificacao do Projeto

| Campo | Detalhe |
|---|---|
| **Nome do Projeto** | Caminhos Estrategicos do ERP GAB |
| **ID Projeto** | PROJ-2026-003 |
| **ID Demanda** | DEM-2026-003 |
| **Area Solicitante** | Grupo Aguia Branca — VP de Inovacao e Financas (Holding GAB) |
| **Area Executora** | KPMG Consultoria Ltda. (consultoria externa contratada) |
| **Acompanhamento PMO** | VMO Autonomo |
| **Data de Abertura** | 02/04/2026 (Kick Off Operacional realizado) |
| **Data de Registro VMO** | 05/04/2026 |
| **Versao do TAP** | 1.0 |
| **Status** | Em Execucao — Semana 0 concluida, Semana 1 iniciando em 06/04/2026 |
| **Classificacao** | Projeto Estrategico — Assessment / Selecao de Plataforma Tecnologica |
| **Complexidade** | ALTA |
| **Prioridade VMO** | ALTA |

---

## 2. Autorizacao

### Sponsors do Projeto

| Nome | Cargo | Entidade | Nivel de Autoridade |
|---|---|---|---|
| Decio Luiz Chieppe | VP de Inovacao e Financas | Holding GAB | Sponsor Executivo Principal — autoridade para aprovar a recomendacao final de plataforma e autorizar investimentos subsequentes de implementacao |
| Paula Barcelos T. Correa | Diretora | VAB Passageiros | Sponsor da Divisao de Passageiros — autoridade para validar aderencia da plataforma aos processos da VAB e aprovar participacao das areas internas nos workshops |
| Patricia Poubel Chieppe | Diretora | VixPar Logistica | Sponsor da Divisao Logistica — autoridade para validar aderencia da plataforma aos processos da VixPar e aprovar participacao das areas internas nos workshops |

### Gerente de Projeto Interno

| Nome | Cargo | Contato | Status | Nivel de Autoridade |
|---|---|---|---|---|
| Marcelo Silveira | GP Interno (Interino) | marcelov@aguiabranca.com.br | Interino — titularizacao pendente de confirmacao (LAC-003) | Ponto focal operacional junto a KPMG e VMO; autoridade para coordenar cronograma, validar entregas parciais e escalar impedimentos aos Sponsors |

### Equipe de Lideranca KPMG

| Nome | Cargo | Papel no Projeto |
|---|---|---|
| Rodrigo Figaro | Socio Responsavel (KPMG) | Responsavel contratual pela entrega; participa do Comite Executivo semanal |
| Wallacy Lima | Gerente Senior (KPMG) | Coordenacao operacional da equipe de 22 profissionais; ponto focal tecnico para o GP Interno |

---

## 3. Objetivo do Projeto (SMART)

**Objetivo Principal:**

Selecionar e recomendar, ate 08/05/2026 (Semana 5), a plataforma ERP que substituira o SAP ECC 6.0 no Grupo Aguia Branca, avaliando as tres plataformas candidatas (SAP S/4HANA Rise, Oracle ERP Cloud e TOTVS Protheus) por meio do Score Model KPMG Powered Enterprise, com aderencia documentada em 7 areas de processo (Manutencao/Frotas, Suprimentos, Financas, Fiscal, DP/SESMT, RH e Tecnologia) e 3 entidades do grupo (Holding GAB, VixPar Logistica e VAB Passageiros), gerando relatorio de recomendacao com scores comparativos que fundamentara a decisao executiva para os proximos 10+ anos.

**Verificacao SMART:**

| Criterio | Verificacao |
|---|---|
| **S** — Especifico | Selecionar plataforma ERP entre 3 candidatas para 3 entidades do GAB |
| **M** — Mensuravel | Score Model com 6 pilares ponderados; matriz de aderencia por area de processo; relatorio comparativo |
| **A** — Alcancavel | Equipe de 22 profissionais KPMG com metodologia comprovada; orcamento aprovado de R$ 930.000 (Fase 1) |
| **R** — Relevante | SAP ECC 6.0 perde suporte em 2027; decisao define arquitetura ERP por 10+ anos |
| **T** — Temporal | Fase 1 ate 08/05/2026 (5 semanas); Fase 2 (RFP) ate ~05/06/2026 (4 semanas adicionais) |

**Objetivo Secundario (Fase 2):**

Elaborar e conduzir, ate ~05/06/2026, o processo formal de Request for Proposal (RFP) com os fornecedores finalistas identificados na Fase 1, com investimento de R$ 170.000,00, viabilizando a contratacao da implementacao da plataforma selecionada.

---

## 4. Justificativa

### Por que este projeto existe

O Grupo Aguia Branca opera suas tres entidades (Holding GAB, VixPar Logistica e VAB Passageiros) sobre a plataforma SAP ECC 6.0, que tera seu suporte oficial encerrado pela SAP em 2027 ("end of maintenance"). A continuidade da operacao sobre um sistema sem suporte apos essa data expoe o grupo a:

- **Riscos de seguranca:** Vulnerabilidades nao corrigidas em sistema sem patches de seguranca
- **Riscos de compliance:** Impossibilidade de atualizacao para atendimento a novas exigencias regulatorias (fiscal, trabalhista, LGPD)
- **Riscos operacionais:** Descontinuidade de funcionalidades criticas para transporte de passageiros e logistica de frotas
- **Riscos financeiros:** Custo crescente de manutencao de sistema legado sem suporte do fabricante

A decisao sobre qual plataforma substituira o SAP ECC 6.0 e de natureza fundacional: define a arquitetura tecnologica central do grupo por 10 ou mais anos e impacta todas as areas de negocio das tres entidades. Uma decisao mal embasada pode resultar em custos de retrabalho entre R$ 5M e R$ 20M+ em um projeto de implementacao tipicamente orcado entre R$ 15M e R$ 50M+ para um grupo do porte do GAB.

### Por que agora

- Prazo externo nao negociavel: suporte SAP ECC encerra em 2027
- Necessidade de tempo para implementacao: apos a selecao, a implementacao do novo ERP demandara 2-4 anos
- Janela de decisao critica: o assessment precisa ser concluido ate maio/2026 para que o ciclo de implementacao possa iniciar no segundo semestre de 2026

### Por que com a KPMG

- Consultoria global com metodologia propria e estabelecida (Powered Enterprise)
- Experiencia em selecao de ERP de escala equivalente
- Modelo de pontuacao estruturado (Score Model) que elimina subjetividade excessiva e garante auditabilidade da decisao
- Equipe de 22 profissionais especializados por area de processo e tecnologia

---

## 5. Escopo — Dentro do Escopo

Os seguintes itens estao incluidos no escopo deste projeto:

1. **Avaliacao de aderencia das tres plataformas ERP candidatas** (SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus) por meio do Score Model KPMG Powered Enterprise com 6 pilares ponderados
2. **Mapeamento dos processos-chave (AS-IS)** das tres entidades do grupo nas 7 areas de processo: Manutencao/Frotas, Suprimentos, Financas, Fiscal, DP/SESMT, RH e Tecnologia
3. **Conducao de workshops de levantamento** com as areas de negocio das tres entidades ao longo de 5 semanas
4. **Geracao de matriz de aderencia** de cada plataforma candidata aos requisitos identificados por area de processo e por entidade
5. **Scoring comparativo** por pilar metodologico (Estrategico 30%, Produto 20%, Tecnologia 20%, Cliente 10%, Financeiro 10%, Operacao 10%) e por plataforma
6. **Relatorio de recomendacao de plataforma ERP** com fundamentacao tecnica, estrategica e financeira para o Grupo Aguia Branca
7. **Material para apresentacao ao Comite Executivo** (Kick Off Executivo e Apresentacao Final de Recomendacao)
8. **Elaboracao e conducao do processo de RFP (Fase 2)** com os fornecedores finalistas identificados na Fase 1
9. **Governanca e acompanhamento operacional** com cadencia definida: Flash Report diario, Status Report semanal (quartas) e Comite Executivo semanal (quintas)
10. **Documentacao e rastreabilidade** pelo VMO Autonomo para registro no portfolio e knowledge base

---

## 6. Escopo — Fora do Escopo

Os seguintes itens NAO estao incluidos neste projeto:

1. **Implementacao da plataforma ERP selecionada** — este projeto limita-se a selecao e recomendacao; a implementacao sera objeto de projeto futuro
2. **Desenvolvimento de software customizado** — nao ha codificacao, integracao de sistemas ou configuracao de plataforma neste escopo
3. **Migracoes de dados** do SAP ECC 6.0 para qualquer plataforma candidata
4. **Avaliacao de plataformas alem das tres candidatas definidas em contrato** — apenas SAP S/4HANA Rise, Oracle ERP Cloud e TOTVS Protheus sao objeto de analise
5. **Entidades do Grupo Aguia Branca fora do escopo contratual** — apenas Holding GAB, VixPar e VAB estao incluidas
6. **Redesenho de processos (TO-BE)** — o assessment mapeia processos atuais (AS-IS) e avalia aderencia das plataformas; nao inclui redesenho de processos de negocio
7. **Negociacao comercial com fornecedores de ERP** — a RFP (Fase 2) estrutura o processo formal, mas a negociacao comercial final sera conduzida pelo GAB
8. **Treinamento de usuarios** em qualquer plataforma ERP
9. **Gestao da mudanca organizacional** decorrente da futura implementacao do ERP

---

## 7. Criterios de Sucesso

| # | Criterio | Metrica | Prazo |
|---|---|---|---|
| CS-01 | Entrega do relatorio de recomendacao de plataforma ERP com scores comparativos | Relatorio entregue e aceito pelo Comite Executivo | Ate 08/05/2026 |
| CS-02 | Cobertura completa das 7 areas de processo nas 3 entidades | 100% das areas mapeadas com pelo menos 1 workshop realizado por area | Ate final da Semana 2 (17/04/2026) |
| CS-03 | Scoring de todas as 3 plataformas nos 6 pilares do Score Model | Matriz completa (3 plataformas x 6 pilares) sem celulas em branco | Ate final da Semana 4 (01/05/2026) |
| CS-04 | Participacao dos Sponsors no Comite Executivo | Presenca de pelo menos 2 dos 3 Sponsors em cada sessao semanal | Todas as quintas-feiras durante a execucao |
| CS-05 | Aderencia ao orcamento contratado | Execucao dentro do valor de R$ 930.000 (Fase 1) e R$ 170.000 (Fase 2) sem aditivos | Ate o encerramento do projeto |
| CS-06 | Aprovacao formal da recomendacao pelo Comite Executivo | Ata de aprovacao assinada com decisao sobre plataforma selecionada | Ate 15/05/2026 |
| CS-07 | Inicio da RFP (Fase 2) conforme cronograma | Fase 2 iniciada ate 05/05/2026 | 05/05/2026 |

---

## 8. Premissas

| # | Premissa |
|---|---|
| PREM-01 | Os tres Sponsors executivos (Decio Luiz Chieppe, Paula Barcelos T. Correa, Patricia Poubel Chieppe) participarao ativamente do Comite Executivo semanal as quintas-feiras e estarao disponiveis para decisoes estrategicas |
| PREM-02 | As areas de negocio do GAB (Manutencao, Suprimentos, Financas, Fiscal, DP/SESMT, RH e Tecnologia) disponibilizarao profissionais-chave para participacao nos workshops durante as 5 semanas da Fase 1 |
| PREM-03 | A Fase 2 (RFP) sera executada pela mesma equipe KPMG, conforme proposta comercial assinada, mantendo continuidade de conhecimento |
| PREM-04 | A KPMG tera acesso as informacoes, sistemas e documentacoes internas necessarias para conduzir o mapeamento de processos das tres entidades |
| PREM-05 | O resultado da Fase 1 gerara uma recomendacao clara e objetiva que sera aprovada pelo Comite Executivo antes do inicio formal da Fase 2 (RFP) |
| PREM-06 | O contrato com a KPMG permanecera vigente e inalterado durante toda a execucao — sem necessidade de aditivos contratuais |
| PREM-07 | O GP Interno (Marcelo Silveira) permanecera como ponto focal operacional durante toda a Fase 1, mesmo em carater interino, ou sera substituido formalmente sem interrupcao de governanca |
| PREM-08 | Os fornecedores das plataformas candidatas (SAP, Oracle, TOTVS) disponibilizarao informacoes tecnicas e comerciais solicitadas durante o processo de avaliacao |

---

## 9. Restricoes

| # | Restricao | Detalhe |
|---|---|---|
| REST-01 | **Prazo fixo da Fase 1** | 5 semanas — entrega final prevista para 08/05/2026; nao ha indicacao de flexibilidade de prazo no contrato |
| REST-02 | **Plataformas candidatas definidas em contrato** | Apenas SAP S/4HANA Rise, Oracle ERP Cloud e TOTVS Protheus sao objeto de avaliacao; nao e possivel adicionar candidatas sem aditivo contratual |
| REST-03 | **Orcamento contratado e fechado** | R$ 930.000,00 (Fase 1) + R$ 170.000,00 (Fase 2) = R$ 1.100.000,00 total; nao ha indicacao de margem para aditivos |
| REST-04 | **Entidades no escopo definidas em contrato** | Holding GAB, VixPar e VAB — outras entidades do grupo, caso existam, nao estao no escopo |
| REST-05 | **Metodologia definida pelo contratado** | A KPMG conduz a avaliacao pelo metodo Powered Enterprise com Score Model de 6 pilares ponderados; o GAB nao pode alterar a metodologia unilateralmente |
| REST-06 | **Equipe KPMG definida em proposta** | 22 profissionais designados conforme proposta comercial; substituicoes dependem de acordo entre as partes |
| REST-07 | **Deadline externo SAP ECC** | O suporte ao SAP ECC 6.0 encerra em 2027, criando restricao temporal absoluta para o ciclo completo de selecao + implementacao |

---

## 10. Riscos de Alto Nivel

| # | Risco | Probabilidade | Impacto | Resposta Planejada |
|---|---|---|---|---|
| R01 | **Baixo engajamento das areas de negocio nos workshops** — areas internas do GAB podem nao dedicar tempo/atencao suficiente as sessoes de levantamento | Media | Alto — mapeamento incompleto ou superficial gera scoring baseado em dados fracos | Envolvimento dos Sponsors para garantir priorizacao; GP Interno acompanha presenca e reporta desvios no Flash Report diario |
| R02 | **Foco excessivo em ferramenta em detrimento do cenario-alvo de processos** — decisores podem priorizar escolha de plataforma sem definir modelo operacional alvo | Media | Alto — selecao de plataforma desalinhada com a estrategia de processos futuros do grupo | KPMG conduzir workshops com foco em necessidades de negocio antes de demonstracoes de produto; Comite Executivo reforcar diretriz |
| R03 | **Dependencia excessiva de percepcoes individuais em vez de dados objetivos** — avaliacao influenciada por preferencias pessoais de stakeholders | Media | Alto — distorcao no Score Model e questionamento posterior da recomendacao | Score Model com criterios pre-definidos e pesos objetivos; documentacao de evidencias por pontuacao atribuida |
| R04 | **Comunicacao insuficiente sobre o projeto para stakeholders internos** — areas nao envolvidas podem nao compreender o impacto e resistir a mudanca futura | Baixa | Medio — resistencia a implementacao e falta de legitimidade da decisao | Plano de comunicacao com Flash Report, Status Report e Comite Executivo; comunicacao top-down dos Sponsors |
| R05 | **Descontinuidade do GP Interno (interino)** — Marcelo Silveira atua de forma interina; saida sem sucessor definido interrompe governanca operacional | Media | Alto — perda de ponto focal interno durante fase critica do projeto | Condicao bloqueante CB-01: confirmar titularizacao ou designar backup formal ate 07/04/2026 |
| R06 | **Atraso no cronograma de workshops por indisponibilidade de participantes** — feriados, ferias ou demandas operacionais impedem realizacao de sessoes conforme planejado | Baixa | Alto — compressao de atividades nas semanas finais compromete qualidade do scoring | Planejamento antecipado de agenda; sessoes de reposicao no mesmo dia; escala de participantes por area |
| R07 | **Inconsistencia na metodologia Score Model** — discrepancia entre 5 e 6 pilares identificada nos materiais pode gerar confusao na avaliacao | Baixa | Medio — criterios de avaliacao ambiguos comprometem confianca no resultado | Condicao desejavel CD-04: KPMG deve confirmar numero e descricao dos pilares na Semana 1 |

---

## 11. Partes Interessadas Principais

| # | Nome | Papel | Entidade | Interesse Principal |
|---|---|---|---|---|
| 1 | Decio Luiz Chieppe | Sponsor Executivo Principal — VP Inovacao e Financas | Holding GAB | Decisao estrategica de plataforma; retorno sobre investimento; continuidade operacional do grupo |
| 2 | Paula Barcelos T. Correa | Sponsor — Diretora VAB | VAB Passageiros | Aderencia da plataforma aos processos de transporte de passageiros |
| 3 | Patricia Poubel Chieppe | Sponsor — Diretora VixPar | VixPar Logistica | Aderencia da plataforma aos processos de logistica e manutencao de frotas |
| 4 | Marcelo Silveira | GP Interno (Interino) | GAB | Coordenacao operacional; interface entre KPMG, Sponsors e VMO |
| 5 | Rodrigo Figaro | Socio Responsavel KPMG | KPMG | Entrega contratual; qualidade da recomendacao; reputacao da consultoria |
| 6 | Wallacy Lima | Gerente Senior KPMG | KPMG | Coordenacao operacional da equipe de 22 profissionais; execucao dos workshops |
| 7 | 20 especialistas KPMG | Equipe Tecnica | KPMG | Execucao dos workshops, mapeamento de processos e scoring por area |
| 8 | Gestores de area GAB (Manutencao, Suprimentos, Financas, Fiscal, DP/SESMT, RH, TI) | Participantes dos workshops | Holding, VixPar, VAB | Garantir que necessidades de suas areas sejam mapeadas e consideradas na avaliacao |
| 9 | VMO Autonomo | Acompanhamento de portfolio e governanca | VMO | Rastreabilidade, documentacao, geracao de knowledge base |
| 10 | SAP, Oracle, TOTVS | Fornecedores das plataformas candidatas | Externo | Fornecer informacoes tecnicas e comerciais para avaliacao |

---

## 12. Orcamento Resumido

| Fase | Descricao | Valor | Status |
|---|---|---|---|
| Fase 1 | Software Selection — Assessment de aderencia e recomendacao de plataforma | R$ 930.000,00 | Contratado e em execucao |
| Fase 2 | RFP — Elaboracao e conducao do processo de Request for Proposal | R$ 170.000,00 | Contratado; execucao prevista para inicio em ~05/05/2026 |
| **Total** | **Investimento total contratado via KPMG** | **R$ 1.100.000,00** | **Aprovado e contratado (DocuSign 13-17/03/2026)** |

**Observacoes sobre contingencia:**
- O contrato com a KPMG e de valor fechado — nao ha indicacao de margem para aditivos contratuais
- O orcamento nao contempla custos internos do GAB (horas de profissionais internos nos workshops, infraestrutura de salas, etc.)
- Eventuais custos adicionais (viagens, alocacao de recursos nao previstos) devem ser aprovados pelos Sponsors
- O codigo do centro de custo / imputacao contabil do projeto ainda nao foi informado ao VMO (LAC-011)

---

## 13. Cronograma Sumarizado

| Semana | Periodo | Atividade Principal | Marco | Status |
|---|---|---|---|---|
| Pre-projeto | 13-17/03/2026 | Assinatura do contrato KPMG via DocuSign | Contrato assinado | REALIZADO |
| Semana 0 | 30/03-03/04/2026 | Kick Off Operacional | Inicio formal da execucao (02/04) | CONCLUIDA |
| Semana 1 | 06-10/04/2026 | Workshops: Manutencao, Suprimentos, Financeiro, Fiscal | Inicio dos workshops de levantamento | EM ANDAMENTO |
| Semana 2 | 13-17/04/2026 | Workshops: RH, DP/SESMT; continuacao Financeiro | Conclusao do levantamento de processos | PREVISTA |
| Semana 3 | 20-24/04/2026 | Analise e Definicao de Aderencias (Scoring) | Inicio do scoring comparativo | PREVISTA |
| Semana 4 | 27/04-01/05/2026 | Analise e Definicao de Aderencias — continuacao | Scores por plataforma consolidados | PREVISTA |
| Semana 5 | 04-08/05/2026 | Revisoes Finais + Apresentacao de Resultados | **Entrega do relatorio de recomendacao** | PREVISTA |
| Fase 2 | ~05/05-05/06/2026 | RFP — Processo de Request for Proposal | Inicio da Fase 2 em paralelo ao final da Fase 1 | PREVISTA |

**Marcos adicionais:**
- **Kick Off Executivo:** Abril/2026 (data exata pendente de confirmacao — LAC-001)
- **Apresentacao Final ao Comite Executivo:** Semana 5 (~08/05/2026)
- **Aprovacao formal da recomendacao:** Ate 15/05/2026 (estimativa VMO)

---

## 14. Condicoes Especiais

Este projeto foi qualificado pelo VMO Autonomo com resultado **APROVADO COM CONDICOES** (27/30 pontos — 90%). Duas condicoes bloqueantes foram identificadas:

### Condicoes Bloqueantes

| # | Condicao | Responsavel | Prazo | Status |
|---|---|---|---|---|
| CB-01 | **Titularizacao do GP Interno:** Confirmar ou definir prazo para titularizacao de Marcelo Silveira como GP do projeto. Se nao houver previsao, designar formalmente um backup de GP para garantir continuidade de governanca. | Marcelo Silveira / Diretoria GAB | 07/04/2026 | PENDENTE |
| CB-02 | **Agenda da Semana 1:** Fornecer ao VMO a agenda detalhada dos workshops da Semana 1 (06-10/04/2026): datas, horarios, areas, facilitadores KPMG e participantes internos por sessao. | Marcelo Silveira / KPMG (Wallacy Lima) | 06/04/2026 (urgente) | PENDENTE |

### Condicoes Desejaveis

| # | Condicao | Responsavel | Prazo |
|---|---|---|---|
| CD-01 | Fornecer contatos diretos (e-mail) dos tres Sponsors | Marcelo Silveira | Semana 1 |
| CD-02 | Confirmar data exata do Kick Off Executivo | Marcelo Silveira | Semana 1 |
| CD-03 | Fornecer lista dos 20 especialistas KPMG por area de processo | Wallacy Lima (KPMG) | Semana 1 |
| CD-04 | Confirmar numero correto de pilares do Score Model (5 ou 6) | Wallacy Lima (KPMG) | Semana 1 |
| CD-05 | Fornecer codigo do centro de custo do projeto | Area Financeira GAB | Semana 1 |

---

## 15. Aprovacao

Este Termo de Abertura de Projeto foi elaborado pelo VMO Autonomo com base na documentacao contratual e materiais de projeto disponibilizados pelo GP Interno.

| Papel | Nome | Assinatura | Data |
|---|---|---|---|
| Sponsor Executivo Principal | Decio Luiz Chieppe | _________________ | ____/____/2026 |
| Sponsor VAB | Paula Barcelos T. Correa | _________________ | ____/____/2026 |
| Sponsor VixPar | Patricia Poubel Chieppe | _________________ | ____/____/2026 |
| GP Interno | Marcelo Silveira | _________________ | ____/____/2026 |
| VMO Autonomo | Diana Documento | _________________ | 05/04/2026 |

---

# PARTE 2 — PM CANVAS

## Visao Geral do PM Canvas — Caminhos Estrategicos do ERP GAB

O PM Canvas sintetiza em 9 blocos os elementos essenciais do projeto para comunicacao rapida e alinhamento entre todas as partes interessadas.

---

### Bloco 1 — POR QUE? (Justificativa)

| Elemento | Descricao |
|---|---|
| **Problema** | O SAP ECC 6.0, plataforma ERP central do Grupo Aguia Branca, tera seu suporte encerrado pela SAP em 2027 (end of maintenance). Operar sem suporte expoe o grupo a riscos de seguranca, compliance e descontinuidade operacional. |
| **Necessidade Estrategica** | O grupo precisa selecionar a plataforma ERP que atendera suas tres entidades (Holding, VixPar, VAB) pelos proximos 10+ anos. A decisao impacta operacoes criticas de transporte de passageiros e logistica de frotas. |
| **Urgencia** | Deadline externo nao negociavel (SAP 2027) combinado com ciclo de implementacao de 2-4 anos exige inicio imediato do processo de selecao. |
| **Valor do Investimento** | Investimento de R$ 1,1M em qualidade de decisao que evita risco de escolha inadequada estimado entre R$ 5M e R$ 20M+ em retrabalho. Alavancagem de 5x a 18x sobre o investimento. |
| **Proposta de Valor** | Decisao fundamentada, auditavel e baseada em criterios objetivos sobre qual plataforma ERP substituira o SAP ECC 6.0, reduzindo risco de implementacao mal orientada e garantindo continuidade operacional apos 2027. |

---

### Bloco 2 — O QUE? (Entregas)

| # | Entregavel | Descricao | Prazo |
|---|---|---|---|
| E-01 | Documentacao de processos AS-IS | Mapeamento dos processos-chave das 3 entidades nas 7 areas de processo cobertas | Semanas 1-2 (ate 17/04/2026) |
| E-02 | Matriz de aderencia por plataforma | Aderencia de cada uma das 3 plataformas candidatas aos requisitos identificados por area de processo e por entidade | Semanas 3-4 (ate 01/05/2026) |
| E-03 | Score comparativo por pilar | Pontuacao estruturada por pilar metodologico (Estrategico, Produto, Tecnologia, Cliente, Financeiro, Operacao) para cada plataforma | Semanas 3-4 (ate 01/05/2026) |
| E-04 | Relatorio de recomendacao de plataforma | Documento consolidado com recomendacao fundamentada, scores comparativos e analise por area de processo | Semana 5 (ate 08/05/2026) |
| E-05 | Material de apresentacao executiva | Apresentacao para o Comite Executivo com sintese da recomendacao e evidencias de sustentacao | Semana 5 (ate 08/05/2026) |
| E-06 | Processo de RFP estruturado (Fase 2) | Documentacao de RFP para fornecedores finalistas; conducao do processo de Request for Proposal | ~05/05 a 05/06/2026 |

---

### Bloco 3 — QUEM? (Partes Interessadas)

**Lado GAB (Contratante):**

| Nome | Papel | Responsabilidade Principal |
|---|---|---|
| Decio Luiz Chieppe | Sponsor Executivo — VP Inovacao e Financas (Holding) | Aprovacao final da recomendacao; direcao estrategica; autorizacao de investimentos |
| Paula Barcelos T. Correa | Sponsor — Diretora (VAB Passageiros) | Validacao da aderencia para processos de transporte de passageiros |
| Patricia Poubel Chieppe | Sponsor — Diretora (VixPar Logistica) | Validacao da aderencia para processos de logistica e manutencao de frotas |
| Marcelo Silveira | GP Interno (Interino) | Coordenacao operacional; interface com KPMG e VMO; gestao do dia-a-dia |
| Gestores das 7 areas de processo | Participantes dos workshops | Fornecimento de informacoes sobre processos; validacao de mapeamentos |

**Lado KPMG (Executante):**

| Nome | Papel | Responsabilidade Principal |
|---|---|---|
| Rodrigo Figaro | Socio Responsavel | Entrega contratual; participacao no Comite Executivo; qualidade da recomendacao |
| Wallacy Lima | Gerente Senior | Coordenacao operacional da equipe; conducao dos workshops; ponto focal tecnico |
| 20 especialistas | Equipe Tecnica | Execucao dos workshops, mapeamento de processos, scoring e documentacao |

**Lado VMO (Acompanhamento):**

| Agente | Papel | Responsabilidade Principal |
|---|---|---|
| VMO Autonomo | Acompanhamento de portfolio | Rastreabilidade, documentacao de projeto, governanca e knowledge base |

---

### Bloco 4 — COMO? (Metodologia)

| Elemento | Descricao |
|---|---|
| **Metodologia Principal** | KPMG Powered Enterprise — abordagem proprietaria para avaliacao e selecao de plataformas ERP |
| **Modelo de Avaliacao** | Score Model com 6 pilares ponderados: Estrategico (30%), Produto (20%), Tecnologia (20%), Cliente (10%), Financeiro (10%), Operacao (10%) |
| **Dinamica de Levantamento** | Workshops presenciais/remotos com areas de negocio do GAB, conduzidos por especialistas KPMG por area de processo |
| **Cobertura** | 7 areas de processo (Manutencao/Frotas, Suprimentos, Financas, Fiscal, DP/SESMT, RH, Tecnologia) x 3 entidades (Holding, VixPar, VAB) |
| **Plataformas Avaliadas** | SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus |
| **Processo de Decisao** | Scoring objetivo por pilar → Consolidacao por plataforma → Relatorio de recomendacao → Aprovacao pelo Comite Executivo |
| **Fase 2 (RFP)** | Elaboracao de documentacao de RFP e conducao do processo formal com fornecedores finalistas |
| **Governanca Operacional** | Flash Report diario + Status Report semanal (quartas) + Comite Executivo semanal (quintas) |

---

### Bloco 5 — QUANDO? (Cronograma)

| Marco | Data / Periodo | Status |
|---|---|---|
| Assinatura do contrato KPMG | 13-17/03/2026 | REALIZADO |
| Kick Off Operacional | 02/04/2026 | REALIZADO |
| Semana 1 — Workshops: Manutencao, Suprimentos, Financeiro, Fiscal | 06-10/04/2026 | EM ANDAMENTO |
| Semana 2 — Workshops: RH, DP/SESMT; continuacao Financeiro | 13-17/04/2026 | PREVISTO |
| Kick Off Executivo | Abril/2026 (data a confirmar) | PENDENTE |
| Semana 3 — Inicio Scoring | 20-24/04/2026 | PREVISTO |
| Semana 4 — Consolidacao Scoring | 27/04-01/05/2026 | PREVISTO |
| Semana 5 — Revisoes + Apresentacao Final | 04-08/05/2026 | PREVISTO |
| **Entrega Relatorio de Recomendacao** | **~08/05/2026** | **PREVISTO** |
| Inicio Fase 2 (RFP) | ~05/05/2026 | PREVISTO |
| Conclusao Fase 2 (RFP) | ~05/06/2026 | PREVISTO |

**Duracao total:** Fase 1: 5 semanas (02/04-08/05/2026) + Fase 2: 4 semanas (~05/05-05/06/2026)

---

### Bloco 6 — QUANTO? (Orcamento)

| Fase | Valor | Condicao |
|---|---|---|
| Fase 1 — Software Selection | R$ 930.000,00 | Contratado e em execucao |
| Fase 2 — RFP | R$ 170.000,00 | Contratado; execucao a partir de ~05/05/2026 |
| **Total Contratado** | **R$ 1.100.000,00** | **Aprovado — contrato assinado via DocuSign em 13-17/03/2026** |

**Detalhamento:**
- Investimento 100% em consultoria externa (KPMG)
- Valor fechado em contrato — sem margem para aditivos indicada
- Custos internos do GAB (horas de profissionais, infraestrutura) nao estao contabilizados
- Centro de custo / imputacao contabil pendente de informacao (LAC-011)

---

### Bloco 7 — ONDE? (Localizacao)

| Local | Utilizacao |
|---|---|
| **Escritorios do Grupo Aguia Branca** | Workshops presenciais com as areas de negocio; reunioes de Comite Executivo |
| **Escritorios/Remoto KPMG** | Trabalho de analise, consolidacao de dados, elaboracao de relatorios e scoring |
| **Ambiente virtual (videoconferencia)** | Flash Reports diarios, sessoes de alinhamento remoto, apresentacoes intermediarias |
| **Comite Executivo (sala de reuniao executiva GAB)** | Reunioes semanais de quinta-feira com Sponsors e Socio KPMG |
| **Plataforma de comunicacao do projeto** | Compartilhamento de documentos, comunicados e Flash Reports |

---

### Bloco 8 — PREMISSAS

| # | Premissa |
|---|---|
| PREM-01 | Os tres Sponsors executivos (Decio, Paula, Patricia) participarao ativamente do Comite Executivo semanal e estarao disponiveis para decisoes estrategicas criticas |
| PREM-02 | As 7 areas de negocio do GAB disponibilizarao profissionais-chave com conhecimento suficiente dos processos para participar dos workshops nas Semanas 1 e 2 |
| PREM-03 | A Fase 2 (RFP) sera executada pela mesma equipe KPMG, conforme proposta comercial, sem necessidade de novo processo de contratacao |
| PREM-04 | A KPMG tera acesso irrestrito as informacoes, sistemas e documentacoes internas necessarias para conduzir mapeamento completo dos processos |
| PREM-05 | A recomendacao da Fase 1 gerara uma decisao clara aprovada pelo Comite Executivo antes do inicio da RFP |
| PREM-06 | O GP Interno (Marcelo Silveira) permanecera no papel durante toda a Fase 1 ou sera substituido formalmente sem interrupcao de governanca |
| PREM-07 | Os fornecedores (SAP, Oracle, TOTVS) cooperarao com informacoes tecnicas e comerciais durante o assessment |
| PREM-08 | O contrato KPMG permanecera vigente e inalterado — sem necessidade de aditivos |

---

### Bloco 9 — RISCOS

| # | Risco | Probabilidade | Impacto | Classificacao |
|---|---|---|---|---|
| R01 | Baixo engajamento das areas de negocio nos workshops — mapeamento incompleto compromete qualidade do scoring | Media | Alto | CRITICO |
| R02 | Foco excessivo em ferramenta em detrimento do cenario-alvo de processos — selecao desalinhada com estrategia futura | Media | Alto | CRITICO |
| R03 | Dependencia de percepcoes individuais em vez de dados objetivos — distorcao no Score Model | Media | Alto | CRITICO |
| R04 | Comunicacao insuficiente sobre o projeto para stakeholders internos — resistencia futura a implementacao | Baixa | Medio | MODERADO |
| R05 | Descontinuidade do GP Interno interino — perda de governanca operacional durante fase critica | Media | Alto | CRITICO |
| R06 | Atraso nos workshops por indisponibilidade de participantes — compressao de cronograma nas semanas finais | Baixa | Alto | ALTO |
| R07 | Inconsistencia na definicao do Score Model (5 vs. 6 pilares) — ambiguidade nos criterios de avaliacao | Baixa | Medio | MODERADO |

---

# PARTE 3 — PLANO GERAL DO PROJETO

## Plano de Gerenciamento do Projeto — Caminhos Estrategicos do ERP GAB

Este plano endereca as 10 areas de conhecimento do PMBOK, adaptadas ao contexto de um projeto de assessment e selecao de software ERP conduzido por consultoria externa (KPMG), com acompanhamento do VMO Autonomo.

---

### 1. Gerenciamento da Integracao

**Abordagem:**
O gerenciamento da integracao assegura que todas as partes do projeto estejam coordenadas e que mudancas sejam controladas. Neste projeto, a integracao e particularmente relevante porque envolve tres entidades organizacionais distintas, uma consultoria externa de 22 profissionais e tres sponsors executivos.

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Marcelo Silveira (GP Interno) | Integracao operacional — coordena interface entre KPMG, areas internas e Sponsors |
| Wallacy Lima (KPMG) | Integracao tecnica — consolida outputs dos workshops e garante consistencia do scoring |
| VMO Autonomo | Integracao documental — garante rastreabilidade entre TAP, entregas e relatorios de acompanhamento |

**Ferramentas e Metodos:**
- TAP como documento integrador de referencia
- Flash Report diario como mecanismo de integracao operacional
- Status Report semanal como consolidacao integrada de progresso
- Comite Executivo semanal como instancia de integracao decisoria
- Controle integrado de mudancas: qualquer alteracao de escopo, cronograma ou orcamento deve ser formalizada e aprovada pelo Comite Executivo

**Consideracoes Especiais:**
- O projeto ja esta em execucao (desde 02/04/2026) — o TAP e de reconhecimento retroativo
- A metodologia e propriedade da KPMG; a integracao deve respeitar os processos da consultoria
- O VMO Autonomo nao tem autoridade executiva — seu papel e de acompanhamento, documentacao e governanca

---

### 2. Gerenciamento do Escopo

**Abordagem:**
O escopo esta definido em contrato assinado com a KPMG e nao deve sofrer alteracoes sem aditivo contratual formal. O gerenciamento do escopo foca em garantir que as entregas contratuais sejam executadas integralmente e que nao haja expansao nao autorizada (scope creep).

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Rodrigo Figaro (KPMG) | Responsavel contratual pelo escopo da entrega |
| Marcelo Silveira (GP Interno) | Validacao de escopo — confirma que entregas atendem necessidades do GAB |
| Comite Executivo | Aprovacao de mudancas de escopo (se houver) |

**Ferramentas e Metodos:**
- Proposta comercial KPMG como baseline de escopo
- EAP (Estrutura Analitica do Projeto): Workshop por area de processo → Mapeamento AS-IS → Scoring → Relatorio → Apresentacao
- Criterios de aceite: matriz de aderencia completa (3 plataformas x 7 areas x 3 entidades), scores por pilar, relatorio de recomendacao
- Validacao de escopo: revisao de entregas parciais no Status Report semanal; aceite formal no Comite Executivo

**Consideracoes Especiais:**
- Escopo limita-se a selecao e recomendacao — implementacao esta fora do escopo
- Apenas 3 plataformas candidatas (contratualmente definidas)
- Apenas 3 entidades do grupo (contratualmente definidas)
- Fase 2 (RFP) e escopo contratual, porem com inicio condicionado a conclusao da Fase 1

---

### 3. Gerenciamento do Cronograma

**Abordagem:**
O cronograma e de prazo fixo (5 semanas para Fase 1, 4 semanas para Fase 2), definido contratualmente. O gerenciamento foca em monitorar aderencia ao cronograma planejado e identificar desvios precocemente.

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Wallacy Lima (KPMG) | Gerenciamento operacional do cronograma de workshops e analises |
| Marcelo Silveira (GP Interno) | Monitoramento de marcos; reporte de atrasos ao Comite Executivo |
| VMO Autonomo | Registro de aderencia cronologica nos Status Reports |

**Ferramentas e Metodos:**
- Cronograma semanal como baseline (ver Secao 13 do TAP)
- Flash Report diario como mecanismo de deteccao precoce de atrasos
- Status Report semanal (quartas) com indicador de aderencia ao cronograma (no prazo / em risco / atrasado)
- Marcos-chave: conclusao de workshops (Semana 2), conclusao de scoring (Semana 4), entrega do relatorio (Semana 5)

**Marcos Criticos:**

| Marco | Data Prevista | Tolerancia |
|---|---|---|
| Inicio workshops Semana 1 | 06/04/2026 | Zero — ja agendado |
| Conclusao levantamento de processos | 17/04/2026 | +2 dias uteis (com reposicao) |
| Conclusao scoring | 01/05/2026 | +2 dias uteis |
| Entrega relatorio final | 08/05/2026 | Sem tolerancia contratual indicada |
| Inicio Fase 2 (RFP) | ~05/05/2026 | Condicionado a aprovacao da recomendacao |

**Consideracoes Especiais:**
- Feriados no periodo devem ser mapeados e compensados (verificar calendario de abril-maio 2026)
- A sobreposicao entre final da Fase 1 e inicio da Fase 2 requer planejamento de transicao

---

### 4. Gerenciamento de Custos

**Abordagem:**
O orcamento e fechado em contrato (R$ 1.100.000,00) sem indicacao de margem para aditivos. O gerenciamento de custos foca em monitorar a execucao financeira conforme contrato e garantir que nao haja custos nao autorizados.

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Decio Luiz Chieppe (Sponsor) | Autoridade final sobre investimentos e aprovacao de eventuais aditivos |
| Marcelo Silveira (GP Interno) | Monitoramento de custos; aprovacao de invoices KPMG; reporte financeiro |
| Area Financeira GAB | Processamento de pagamentos e controle contabil |
| VMO Autonomo | Registro de baseline de orcamento e acompanhamento de desvios |

**Ferramentas e Metodos:**
- Contrato KPMG como baseline de custo
- Controle de invoices: verificacao de entrega parcial antes de aprovacao de pagamento
- Reporte mensal de custos no Status Report
- Centro de custo do projeto: pendente de informacao (LAC-011)

**Decomposicao Orcamentaria:**

| Item | Valor | % do Total |
|---|---|---|
| Fase 1 — Software Selection | R$ 930.000,00 | 84,5% |
| Fase 2 — RFP | R$ 170.000,00 | 15,5% |
| **Total** | **R$ 1.100.000,00** | **100%** |

**Consideracoes Especiais:**
- Nao ha reserva de contingencia orcamentaria documentada
- Custos internos (horas de profissionais GAB) nao estao contabilizados no orcamento do projeto
- Cronograma de desembolso (parcelas de pagamento) nao foi detalhado nos materiais disponibilizados — deve ser confirmado com GP Interno

---

### 5. Gerenciamento da Qualidade

**Abordagem:**
A qualidade do projeto e medida pela capacidade da recomendacao final de fundamentar uma decisao estrategica solida sobre a plataforma ERP. O gerenciamento de qualidade foca em garantir rigor metodologico, completude de cobertura e auditabilidade do processo de avaliacao.

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Rodrigo Figaro (KPMG) | Garantia de qualidade metodologica — responsavel pela aplicacao correta do Powered Enterprise |
| Wallacy Lima (KPMG) | Controle de qualidade operacional — revisao de outputs de workshops e scores |
| Marcelo Silveira (GP Interno) | Validacao de qualidade do ponto de vista do GAB — entregas atendem necessidades |
| Sponsors | Aceite final da qualidade do relatorio de recomendacao |

**Ferramentas e Metodos:**
- Score Model KPMG como framework de qualidade da avaliacao (6 pilares ponderados)
- Criterios de qualidade por entrega:
  - Mapeamento AS-IS: completude (todas as areas e entidades cobertas), profundidade (processos-chave identificados com detalhamento suficiente)
  - Matriz de aderencia: celulas preenchidas para todas as combinacoes plataforma x area x entidade
  - Score comparativo: fundamentacao documentada para cada nota atribuida
  - Relatorio: recomendacao clara, fundamentada e auditavel
- Revisoes de qualidade: validacao parcial nas sessoes do Status Report semanal
- Aceite formal: Comite Executivo aprova a entrega final

**Consideracoes Especiais:**
- A inconsistencia entre 5 e 6 pilares do Score Model (LAC-007) deve ser resolvida na Semana 1 para garantir integridade metodologica
- Criterios de desempate no Score Model nao estao documentados (LAC-008) — devem ser confirmados com KPMG

---

### 6. Gerenciamento de Recursos

**Abordagem:**
Os recursos deste projeto sao compostos por equipe externa (KPMG, 22 profissionais) e equipe interna do GAB (gestores e profissionais das 7 areas de processo). O gerenciamento foca em garantir disponibilidade dos recursos internos e coordenacao com a equipe externa.

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Wallacy Lima (KPMG) | Gestao da equipe KPMG — alocacao por workshop, qualidade do trabalho tecnico |
| Marcelo Silveira (GP Interno) | Garantia de disponibilidade dos recursos internos do GAB; escala de participantes por workshop |
| Sponsors | Direcionamento top-down para que areas priorizem participacao nos workshops |

**Recursos Externos (KPMG):**

| Recurso | Quantidade | Observacao |
|---|---|---|
| Socio Responsavel | 1 (Rodrigo Figaro) | Comite Executivo + supervisao |
| Gerente Senior | 1 (Wallacy Lima) | Coordenacao operacional full-time |
| Especialistas por area | 20 | Consultores por area de processo e tecnologia |
| **Total KPMG** | **22 profissionais** | Lista nominal pendente (LAC-004) |

**Recursos Internos (GAB):**

| Recurso | Quantidade Estimada | Observacao |
|---|---|---|
| GP Interno | 1 (Marcelo Silveira) | Dedicacao parcial (acumula outras funcoes) — carater interino |
| Gestores e profissionais por area | A definir | 7 areas de processo x 3 entidades; lista nominal pendente (LAC-005) |
| Sponsors | 3 | Dedicacao parcial — Comite Executivo semanal + decisoes estrategicas |

**Consideracoes Especiais:**
- O principal risco de recursos e a concorrencia de prioridades dos profissionais internos do GAB (R01)
- A lista de profissionais internos designados por area de processo nao foi fornecida (LAC-005) — e urgente para a Semana 1
- O GP Interno atua de forma interina — risco de descontinuidade (R05, CB-01)

---

### 7. Gerenciamento das Comunicacoes

**Abordagem:**
O projeto possui cadencia de comunicacao definida em tres niveis: operacional (diario), tatico (semanal) e estrategico (semanal). O gerenciamento de comunicacoes assegura que cada nivel receba a informacao adequada no momento correto.

**Cadencia Definida:**

| Tipo | Objetivo | Frequencia | Dia | Participantes | Formato |
|---|---|---|---|---|---|
| **Flash Report** | Alinhamento operacional — impedimentos, andamento do dia, decisoes rapidas | Diario | Todos os dias uteis | Equipe KPMG + GP Interno (Marcelo Silveira) | Stand-up presencial ou videoconferencia (15-30 min) |
| **Status Report** | Consolidacao de progresso semanal, riscos, proximos passos | Semanal | Quarta-feira | GP Interno + Leads KPMG (Wallacy Lima) | Relatorio escrito + reuniao de alinhamento |
| **Comite Executivo** | Decisoes estrategicas, escaladas, validacao de entregas | Semanal | Quinta-feira | Sponsors GAB (Decio, Paula, Patricia) + Socio KPMG (Rodrigo Figaro) + GP Interno | Reuniao formal com ata |

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Wallacy Lima (KPMG) | Preparacao e conducao do Flash Report diario; input para Status Report |
| Marcelo Silveira (GP Interno) | Consolidacao do Status Report semanal; preparacao da pauta do Comite Executivo; comunicacao com areas internas |
| Rodrigo Figaro (KPMG) | Participacao no Comite Executivo; comunicacao estrategica com Sponsors |
| VMO Autonomo | Registro documental dos Status Reports; rastreabilidade de comunicacoes formais |

**Matriz de Comunicacao Complementar:**

| Comunicacao | De | Para | Frequencia | Canal |
|---|---|---|---|---|
| Convocacao de workshops | KPMG (Wallacy) | Areas internas GAB | Semanal (antecedencia) | E-mail + calendario |
| Escala de impedimentos | GP Interno | Sponsors | Sob demanda | E-mail + telefone |
| Relatorio de recomendacao (Fase 1) | KPMG | Comite Executivo | Unico (Semana 5) | Apresentacao presencial + documento |
| Comunicados do VMO | VMO Autonomo | GP Interno | Sob demanda | E-mail / plataforma VMO |

**Consideracoes Especiais:**
- Nao foi fornecido plano de comunicacao formal do projeto (LAC-009) — a cadencia acima foi definida com base na documentacao de kick off e na proposta KPMG
- Recomenda-se que o GP Interno formalize a lista de distribuicao de cada comunicacao
- O Comite Executivo de quinta-feira e o ponto de validacao para entregas formais — atas devem ser registradas

---

### 8. Gerenciamento de Riscos

**Abordagem:**
O gerenciamento de riscos combina os riscos identificados pela KPMG na proposta comercial com riscos adicionais identificados pelo VMO Autonomo durante o processo de qualificacao.

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Marcelo Silveira (GP Interno) | Monitoramento continuo de riscos; reporte no Status Report semanal; acionamento de respostas |
| Wallacy Lima (KPMG) | Identificacao e gestao de riscos tecnicos e metodologicos |
| Comite Executivo | Decisao sobre respostas a riscos de alto impacto |
| VMO Autonomo | Registro e rastreabilidade de riscos no portfolio |

**Registro de Riscos:**

| # | Risco | Prob. | Impacto | Classif. | Resposta | Responsavel |
|---|---|---|---|---|---|---|
| R01 | Baixo engajamento das areas nos workshops | Media | Alto | CRITICO | Direcao top-down dos Sponsors; monitoramento de presenca no Flash Report | GP Interno + Sponsors |
| R02 | Foco em ferramenta vs. cenario-alvo de processos | Media | Alto | CRITICO | Workshops focados em necessidades antes de demonstracoes; reforco pelo Comite Executivo | KPMG + Sponsors |
| R03 | Percepcoes individuais vs. dados objetivos | Media | Alto | CRITICO | Score Model com criterios pre-definidos e evidencias documentadas | KPMG |
| R04 | Comunicacao insuficiente para stakeholders internos | Baixa | Medio | MODERADO | Cadencia de comunicacao (Flash, Status, Comite); comunicacao top-down | GP Interno + Sponsors |
| R05 | Descontinuidade do GP Interno interino | Media | Alto | CRITICO | CB-01: titularizacao ou backup formal ate 07/04 | GP Interno + Diretoria |
| R06 | Atraso por indisponibilidade de participantes | Baixa | Alto | ALTO | Agenda antecipada; sessoes de reposicao; escala de participantes | GP Interno + KPMG |
| R07 | Inconsistencia Score Model (5 vs. 6 pilares) | Baixa | Medio | MODERADO | CD-04: confirmacao com KPMG na Semana 1 | KPMG |

**Ferramentas e Metodos:**
- Registro de riscos atualizado no Status Report semanal
- Classificacao por probabilidade x impacto (escala: Baixa/Media/Alta x Baixo/Medio/Alto)
- Flash Report diario como mecanismo de deteccao precoce
- Comite Executivo como instancia de escalada para riscos criticos

---

### 9. Gerenciamento de Aquisicoes

**Abordagem:**
A principal aquisicao deste projeto — o contrato com a KPMG — ja foi realizada. O gerenciamento de aquisicoes foca no acompanhamento contratual, processo de aprovacao de invoices e planejamento da Fase 2.

**Status Contratual:**

| Elemento | Detalhe |
|---|---|
| **Fornecedor** | KPMG Consultoria Ltda. |
| **Tipo de Contrato** | Contrato de prestacao de servicos de consultoria (valor fechado) |
| **Assinatura** | 13-17/03/2026 via DocuSign |
| **Valor Total** | R$ 1.100.000,00 (Fase 1: R$ 930.000 + Fase 2: R$ 170.000) |
| **Status** | Vigente e em execucao |

**Responsabilidades:**

| Responsavel | Atribuicao |
|---|---|
| Marcelo Silveira (GP Interno) | Gestao do contrato; validacao de entregas parciais; aprovacao de invoices |
| Rodrigo Figaro (KPMG) | Responsavel contratual pela entrega; interlocutor para questoes contratuais |
| Area Financeira GAB | Processamento de pagamentos conforme cronograma de desembolso |
| Decio Luiz Chieppe (Sponsor) | Autoridade final para eventuais aditivos contratuais |

**Processo de Aprovacao de Invoices:**
1. KPMG emite invoice vinculada a entrega parcial ou marco contratual
2. GP Interno (Marcelo Silveira) verifica a entrega correspondente
3. GP Interno aprova o invoice e encaminha para a Area Financeira GAB
4. Area Financeira processa o pagamento conforme condicoes contratuais

**Planejamento da Fase 2:**
- A Fase 2 (RFP, R$ 170.000) esta contratada no mesmo instrumento — nao requer novo processo de aquisicao
- O inicio da Fase 2 esta condicionado a conclusao e aprovacao da recomendacao da Fase 1
- A equipe KPMG da Fase 1 continuara na Fase 2 (PREM-03)

**Consideracoes Especiais:**
- O cronograma de desembolso (parcelas de pagamento) nao foi detalhado nos materiais — deve ser confirmado com GP Interno e Area Financeira
- Nao ha indicacao de margem para aditivos contratuais — mudancas de escopo requerem aprovacao do Sponsor e negociacao com KPMG
- O contrato inclui ambas as fases; a transicao da Fase 1 para Fase 2 e administrativa, nao contratual

---

### 10. Gerenciamento das Partes Interessadas

**Abordagem:**
O gerenciamento de partes interessadas foca em manter o engajamento de tres grupos criticos: Sponsors (decisao estrategica), areas de negocio do GAB (participacao nos workshops) e equipe KPMG (execucao tecnica).

**Mapa de Partes Interessadas:**

| Stakeholder | Poder | Interesse | Estrategia de Engajamento |
|---|---|---|---|
| Decio Luiz Chieppe (Sponsor Principal) | Alto | Alto | **Gerenciar de Perto** — Comite Executivo semanal; reportes diretos sobre decisoes estrategicas |
| Paula Barcelos T. Correa (Sponsor VAB) | Alto | Alto | **Gerenciar de Perto** — Comite Executivo semanal; validacao de aderencia para processos VAB |
| Patricia Poubel Chieppe (Sponsor VixPar) | Alto | Alto | **Gerenciar de Perto** — Comite Executivo semanal; validacao de aderencia para processos VixPar |
| Marcelo Silveira (GP Interno) | Medio | Alto | **Manter Informado e Engajado** — Interacao diaria; canal direto com VMO e KPMG |
| Rodrigo Figaro (Socio KPMG) | Alto | Alto | **Gerenciar de Perto** — Comite Executivo semanal; alinhamento sobre qualidade da entrega |
| Wallacy Lima (Gerente KPMG) | Medio | Alto | **Manter Informado e Engajado** — Flash Report diario; Status Report semanal |
| Gestores de area GAB | Medio | Medio | **Manter Informados** — Convocacao para workshops com antecedencia; comunicacao sobre impacto e beneficios |
| Equipe tecnica KPMG (20) | Baixo | Alto | **Monitorar** — Coordenacao via Wallacy Lima; suporte operacional nos workshops |
| SAP, Oracle, TOTVS (fornecedores) | Baixo | Alto | **Monitorar** — Interacao via KPMG durante o assessment; interacao direta na Fase 2 (RFP) |
| VMO Autonomo | Baixo | Medio | **Monitorar** — Acompanhamento documental e de portfolio |

**Ferramentas e Metodos:**
- Matriz poder/interesse para classificacao de stakeholders
- Comite Executivo semanal como principal mecanismo de engajamento de alta lideranca
- Flash Report e Status Report como mecanismos de comunicacao continua
- Mapeamento de participantes por workshop (pendente — LAC-005)

**Acoes de Engajamento Prioritarias:**

| # | Acao | Responsavel | Prazo |
|---|---|---|---|
| 1 | Confirmar contatos diretos dos 3 Sponsors (CD-01) | Marcelo Silveira | Semana 1 |
| 2 | Mapear profissionais internos GAB por area de processo (LAC-005) | Marcelo Silveira | Antes do inicio de cada workshop |
| 3 | Garantir comunicacao top-down dos Sponsors sobre importancia dos workshops | Sponsors | Semana 1 |
| 4 | Alinhar expectativas da KPMG sobre acesso a informacoes internas | Marcelo Silveira + Wallacy Lima | Semana 1 |

---

# VERIFICACAO DE CONSISTENCIA

A tabela abaixo verifica a consistencia dos dados entre os tres documentos produzidos:

| Elemento | TAP (Parte 1) | PM Canvas (Parte 2) | Plano Geral (Parte 3) | Consistente? |
|---|---|---|---|---|
| **Nome do Projeto** | Caminhos Estrategicos do ERP GAB | Caminhos Estrategicos do ERP GAB | Caminhos Estrategicos do ERP GAB | SIM |
| **ID Projeto** | PROJ-2026-003 | PROJ-2026-003 (cabecalho) | PROJ-2026-003 (cabecalho) | SIM |
| **Orcamento Fase 1** | R$ 930.000,00 | R$ 930.000,00 | R$ 930.000,00 | SIM |
| **Orcamento Fase 2** | R$ 170.000,00 | R$ 170.000,00 | R$ 170.000,00 | SIM |
| **Orcamento Total** | R$ 1.100.000,00 | R$ 1.100.000,00 | R$ 1.100.000,00 | SIM |
| **Prazo Fase 1** | 5 semanas (02/04 a 08/05/2026) | 5 semanas (02/04 a 08/05/2026) | 5 semanas (02/04 a 08/05/2026) | SIM |
| **Prazo Fase 2** | 4 semanas (~05/05 a 05/06/2026) | 4 semanas (~05/05 a 05/06/2026) | 4 semanas (~05/05 a 05/06/2026) | SIM |
| **Sponsor 1** | Decio Luiz Chieppe — VP Inovacao e Financas | Decio Luiz Chieppe | Decio Luiz Chieppe | SIM |
| **Sponsor 2** | Paula Barcelos T. Correa — Diretora VAB | Paula Barcelos T. Correa | Paula Barcelos T. Correa | SIM |
| **Sponsor 3** | Patricia Poubel Chieppe — Diretora VixPar | Patricia Poubel Chieppe | Patricia Poubel Chieppe | SIM |
| **GP Interno** | Marcelo Silveira (Interino) | Marcelo Silveira (Interino) | Marcelo Silveira (Interino) | SIM |
| **Escopo (plataformas)** | SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus | SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus | SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus | SIM |
| **Escopo (entidades)** | Holding GAB, VixPar, VAB | Holding GAB, VixPar, VAB | Holding GAB, VixPar, VAB | SIM |
| **Escopo (areas)** | 7 areas de processo | 7 areas de processo | 7 areas de processo | SIM |
| **Riscos** | 7 riscos (R01-R07) | 7 riscos (R01-R07) | 7 riscos (R01-R07) | SIM |
| **Premissas** | 8 premissas (PREM-01 a PREM-08) | 8 premissas (PREM-01 a PREM-08) | Referenciadas nos planos por area | SIM |
| **Cadencia de comunicacao** | Flash Report diario, Status Report quarta, Comite Executivo quinta | Flash Report diario, Status Report quarta, Comite Executivo quinta | Flash Report diario, Status Report quarta, Comite Executivo quinta | SIM |

**Resultado da Verificacao:** Todos os 17 elementos verificados estao CONSISTENTES entre os tres documentos.

---

## Lacunas de Informacao Remanescentes

As seguintes lacunas nao puderam ser preenchidas com os materiais disponiveis e devem ser resolvidas pelo GP Interno:

| # | Lacuna | Impacto | Prazo Recomendado |
|---|---|---|---|
| LAC-001 | Data exata do Kick Off Executivo | Cronograma incompleto | Semana 1 |
| LAC-002 | Contatos diretos dos Sponsors (e-mail) | Comunicacao formal do VMO | Semana 1 |
| LAC-003 | Titularizacao do GP Interno | Governanca — CB-01 | 07/04/2026 |
| LAC-004 | Lista nominal dos 20 especialistas KPMG | Plano de recursos incompleto | Semana 1 |
| LAC-005 | Profissionais internos GAB por area de processo | Plano de recursos e engajamento | Antes de cada workshop |
| LAC-006 | Agenda da Semana 1 | Rastreabilidade operacional — CB-02 | 06/04/2026 |
| LAC-007 | Numero correto de pilares do Score Model | Integridade metodologica | Semana 1 |
| LAC-008 | Criterios de desempate no Score Model | Qualidade da decisao | Semana 1 |
| LAC-009 | Plano de comunicacao formal | Gestao de comunicacoes | Semana 1 |
| LAC-011 | Codigo do centro de custo do projeto | Controle financeiro | Semana 1 |
| LAC-012 | Data exata de inicio da Fase 2 | Cronograma da Fase 2 | Semana 3 |
| LAC-013 | Processo de aprovacao da recomendacao final | Governanca de decisao | Semana 2 |

---

*Documento elaborado por Diana Documento — Arquiteta de Projetos, VMO Autonomo*
*Run ID: 2026-04-05-173000 | Etapa: 5/12 — Criar Documentacao Base | ID Projeto: PROJ-2026-003*
