# Especificacao de Requisitos Funcionais (ERF) — Caminhos Estrategicos do ERP GAB

**ID Projeto:** PROJ-2026-003
**ID Demanda:** DEM-2026-003
**Versao:** 1.0
**Data:** 05/04/2026
**Elaborado por:** Rafael Requisito — Engenheiro de Requisitos (VMO Autonomo)
**Run ID:** 2026-04-05-173000

---

## 1. Introducao e Objetivo

Este documento constitui a Especificacao de Requisitos Funcionais (ERF) do projeto "Caminhos Estrategicos do ERP GAB" (PROJ-2026-003). A ERF descreve, de forma testavel e rastreavel, os requisitos que o VMO Autonomo e o GP Interno devem atender para garantir governanca, monitoramento, comunicacao e controle de qualidade adequados durante a execucao deste projeto de assessment e selecao de plataforma ERP conduzido pela KPMG.

**Natureza do projeto:** Este NAO e um projeto de desenvolvimento de software. Trata-se de um projeto de **Software Selection Assessment** gerenciado por um PMO. Os requisitos aqui especificados sao requisitos de gestao de projeto — o que o escritorio de projetos e a equipe de governanca necessitam para gerenciar, monitorar, reportar e garantir a qualidade das entregas desta iniciativa.

**Fontes de elicitacao:**
- Parecer de Qualificacao (DEM-2026-003) — Felipe Filtro, 05/04/2026
- Documentacao Base de Iniciacao (TAP, PM Canvas, Plano Geral) — Diana Documento, 05/04/2026
- Proposta comercial KPMG (referenciada nos documentos acima)
- Condicoes bloqueantes e desejaveis identificadas na qualificacao

**Convencao de escrita:**
- Todos os requisitos utilizam o verbo "deve" indicando obrigatoriedade do stakeholder responsavel
- Cada requisito possui criterio de aceitacao mensuravel
- Priorizacao MoSCoW aplicada: Must Have (M), Should Have (S), Could Have (C), Won't Have (W)
- Rastreabilidade: cada requisito referencia sua fonte documental

---

## 2. Escopo da ERF

### 2.1 Dentro do Escopo

Esta ERF cobre os seguintes dominios de requisitos de gestao de projeto:

1. **Entregaveis e Governanca (RF001-RF020):** Requisitos sobre as entregas esperadas do projeto (tanto da KPMG quanto do VMO/GP Interno), fluxos de aprovacao, participacao em comites e documentacao de governanca.
2. **Monitoramento e Controle (RF021-RF030):** Requisitos sobre acompanhamento de progresso, rastreamento de presenca, registro de riscos, controle de issues e acompanhamento orcamentario.
3. **Comunicacao e Reporting (RF031-RF040):** Requisitos sobre formatos, cadencias e conteudos dos reportes operacionais, taticos e estrategicos.
4. **Qualidade das Entregas KPMG (RF041-RF050):** Requisitos sobre criterios de validacao, auditabilidade do Score Model, padrao de documentacao de workshops e processo de aceite de entregas.
5. **Gestao de Mudancas e Riscos (RF051-RF060):** Requisitos sobre controle de mudancas, registro de riscos, escalada e tratamento de impedimentos.
6. **Requisitos Nao-Funcionais (RNF001-RNF010):** Requisitos sobre disponibilidade de documentacao, tempos de resposta, confidencialidade, trilha de auditoria e padroes de formato.

### 2.2 Fora do Escopo

- Requisitos de funcionalidades das plataformas ERP candidatas (SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus)
- Requisitos de implementacao de ERP
- Requisitos de infraestrutura de TI
- Requisitos de integracao de sistemas

---

## 3. Requisitos Funcionais — Entregaveis e Governanca

### RF001 — Entrega do Relatorio de Recomendacao de Plataforma ERP

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve entregar relatorio consolidado de recomendacao de plataforma ERP contendo scores comparativos das 3 plataformas candidatas (SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus) nos 6 pilares do Score Model Powered Enterprise, com fundamentacao tecnica, estrategica e financeira. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Relatorio entregue em formato digital (PDF ou equivalente) ate 08/05/2026, contendo: (a) scores numericos para cada plataforma em cada pilar; (b) recomendacao explicitada com justificativa por pilar; (c) assinatura do Socio Responsavel KPMG (Rodrigo Figaro). |
| **Fonte** | TAP CS-01; PM Canvas E-04; Proposta KPMG |

### RF002 — Entrega das Matrizes de Aderencia por Area de Processo

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve entregar matrizes de aderencia que documentem, para cada uma das 3 plataformas candidatas, o nivel de aderencia aos requisitos identificados em cada uma das 7 areas de processo (Manutencao/Frotas, Suprimentos, Financas, Fiscal, DP/SESMT, RH, Tecnologia) e 3 entidades (Holding GAB, VixPar, VAB). |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Matrizes entregues ate 01/05/2026 (final da Semana 4), sem celulas em branco, cobrindo 100% das combinacoes: 3 plataformas x 7 areas x 3 entidades = 63 avaliacoes de aderencia documentadas. |
| **Fonte** | TAP CS-02, CS-03; PM Canvas E-02 |

### RF003 — Entrega do Score Comparativo por Pilar Metodologico

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve entregar pontuacao estruturada por pilar metodologico (Estrategico 30%, Produto 20%, Tecnologia 20%, Cliente 10%, Financeiro 10%, Operacao 10%) para cada uma das 3 plataformas candidatas. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Scores entregues ate 01/05/2026, com: (a) pontuacao numerica por pilar e por plataforma; (b) peso percentual de cada pilar documentado; (c) pontuacao ponderada consolidada por plataforma; (d) ranking final das plataformas. |
| **Fonte** | TAP CS-03; PM Canvas E-03; Proposta KPMG |

### RF004 — Entrega de Material de Apresentacao Executiva

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve produzir material de apresentacao executiva para o Comite Executivo contendo sintese da recomendacao de plataforma e evidencias de sustentacao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Apresentacao entregue ao GP Interno ate 2 dias uteis antes da data da sessao de apresentacao final ao Comite Executivo (prevista para Semana 5), em formato editavel (PowerPoint ou equivalente), com no maximo 30 slides. |
| **Fonte** | PM Canvas E-05; TAP Secao 13 |

### RF005 — Elaboracao e Aprovacao do TAP pelo VMO

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve elaborar o Termo de Abertura do Projeto (TAP) e submetelo para aprovacao dos Sponsors e GP Interno. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | TAP elaborado contendo no minimo: identificacao do projeto, autorizacao (sponsors), objetivo SMART, justificativa, escopo (dentro e fora), criterios de sucesso, premissas, restricoes, riscos de alto nivel, partes interessadas, orcamento e cronograma sumarizado. Assinaturas de pelo menos 2 dos 3 Sponsors e do GP Interno obtidas ate 11/04/2026. |
| **Fonte** | Documentacao Base — Parte 1 (TAP); Pipeline VMO Step 5 |

### RF006 — Elaboracao do PM Canvas

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve elaborar o PM Canvas sintetizando em blocos visuais os elementos essenciais do projeto para comunicacao rapida. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | PM Canvas entregue ate 07/04/2026, contendo os 9 blocos (Por Que, O Que, Quem, Como, Quando, Quanto, Onde, Premissas, Riscos), com dados consistentes com o TAP (verificacao cruzada de pelo menos 15 elementos-chave). |
| **Fonte** | Documentacao Base — Parte 2 (PM Canvas) |

### RF007 — Elaboracao do Plano Geral do Projeto

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve elaborar o Plano Geral do Projeto cobrindo as 10 areas de conhecimento do PMBOK adaptadas ao contexto do assessment. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Plano entregue ate 07/04/2026, cobrindo: Integracao, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicacoes, Riscos, Aquisicoes e Partes Interessadas. Cada area com: abordagem, responsabilidades, ferramentas/metodos e consideracoes especiais. |
| **Fonte** | Documentacao Base — Parte 3 (Plano Geral) |

### RF008 — Producao de Status Report Semanal

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve produzir e distribuir Status Report semanal consolidando progresso, riscos, impedimentos e proximos passos do projeto. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Status Report entregue toda quarta-feira ate as 18h, contendo no minimo: (a) resumo de atividades da semana; (b) status dos marcos (no prazo / em risco / atrasado); (c) indicadores SPI e CPI quando disponiveis; (d) top 3 riscos atualizados; (e) impedimentos abertos; (f) proximos passos para a semana seguinte. Primeiro Status Report ate 09/04/2026. |
| **Fonte** | Plano Geral — Secao 7 (Comunicacoes); Qualificacao — Proximo Passo #6 |

### RF009 — Producao de Flash Report Diario

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno, em conjunto com a KPMG, deve produzir Flash Report diario durante todos os dias uteis de execucao do projeto. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Flash Report realizado diariamente (stand-up de 15 a 30 minutos, presencial ou videoconferencia) com registro escrito (ata ou resumo) contendo: (a) o que foi realizado no dia anterior; (b) o que sera realizado no dia; (c) impedimentos identificados. Registro disponibilizado ao VMO ate as 10h do dia seguinte. Primeiro Flash Report em 07/04/2026. |
| **Fonte** | Plano Geral — Secao 7 (Comunicacoes); PM Canvas Bloco 4 |

### RF010 — Elaboracao do Plano de Riscos Detalhado

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve elaborar plano de riscos detalhado a partir dos 7 riscos de alto nivel identificados no TAP, acrescentando riscos identificados durante a execucao. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Plano de riscos documentado ate 11/04/2026, contendo para cada risco: descricao, probabilidade (Baixa/Media/Alta), impacto (Baixo/Medio/Alto), classificacao resultante, resposta planejada, responsavel e prazo de revisao. Minimo de 7 riscos registrados (R01-R07 do TAP). |
| **Fonte** | TAP Secao 10; Plano Geral — Secao 8 |

### RF011 — Participacao dos Sponsors no Comite Executivo Semanal

| Atributo | Detalhe |
|---|---|
| **Descricao** | Os Sponsors do projeto (Decio Luiz Chieppe, Paula Barcelos T. Correa, Patricia Poubel Chieppe) devem participar do Comite Executivo semanal as quintas-feiras. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Presenca de pelo menos 2 dos 3 Sponsors em cada sessao semanal do Comite Executivo. Ausencia de mais de 1 Sponsor em sessao consecutiva deve ser reportada como risco no Status Report seguinte. |
| **Fonte** | TAP CS-04; TAP PREM-01 |

### RF012 — Participacao do Socio KPMG no Comite Executivo Semanal

| Atributo | Detalhe |
|---|---|
| **Descricao** | O Socio Responsavel da KPMG (Rodrigo Figaro) deve participar do Comite Executivo semanal as quintas-feiras, representando a consultoria executante. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Presenca do Socio KPMG (ou substituto formalmente designado por ele) em 100% das sessoes do Comite Executivo. Ausencia sem substituto deve ser registrada como desvio contratual. |
| **Fonte** | TAP Secao 2 (Autorizacao); Plano Geral — Secao 7 |

### RF013 — Registro de Ata do Comite Executivo

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve produzir ata formal de cada sessao do Comite Executivo semanal. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Ata produzida e distribuida aos participantes em ate 1 dia util apos a sessao, contendo: (a) data, horario e local; (b) lista de presentes e ausentes; (c) pauta discutida; (d) decisoes tomadas com responsaveis e prazos; (e) acoes pendentes da sessao anterior e seu status. |
| **Fonte** | Plano Geral — Secao 7 (Comunicacoes) |

### RF014 — Definicao e Titularizacao do GP Interno

| Atributo | Detalhe |
|---|---|
| **Descricao** | A Diretoria do GAB deve confirmar a titularizacao de Marcelo Silveira como GP do projeto ou designar formalmente um backup de GP para garantir continuidade de governanca. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Confirmacao formal (e-mail ou documento) recebida pelo VMO ate 07/04/2026, indicando: (a) se Marcelo Silveira sera titularizado, com prazo definido; ou (b) nome do backup de GP designado com dados de contato. |
| **Fonte** | Qualificacao CB-01; TAP PREM-07; Risco R05 |

### RF015 — Fornecimento da Agenda de Workshops ao VMO

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve fornecer ao VMO a agenda detalhada dos workshops de cada semana com antecedencia minima definida. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Agenda de cada semana entregue ao VMO ate a sexta-feira da semana anterior (exceto Semana 1, cuja agenda deve ser fornecida ate 06/04/2026 — CB-02), contendo: datas, horarios, areas de processo cobertas, facilitadores KPMG responsaveis e participantes internos GAB convocados. |
| **Fonte** | Qualificacao CB-02; LAC-006 |

### RF016 — Fluxo de Aprovacao para Transicao de Fases

| Atributo | Detalhe |
|---|---|
| **Descricao** | O projeto deve possuir fluxo formal de aprovacao para a transicao entre Fase 1 (Software Selection) e Fase 2 (RFP). |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Fluxo documentado ate 17/04/2026 (final da Semana 2), contendo: (a) criterios de aceite para conclusao da Fase 1; (b) instancia de aprovacao (Comite Executivo); (c) formato do documento de aprovacao (ata assinada); (d) prazo maximo entre solicitacao e decisao (3 dias uteis). |
| **Fonte** | TAP CS-06; TAP REST-01; LAC-013 |

### RF017 — Documentacao de Participantes e Presenca nos Workshops

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve registrar os participantes e a presenca em cada sessao de workshop conduzida pela KPMG. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Lista de presenca assinada (fisica ou digital) para cada sessao de workshop, contendo: data, horario, area de processo, entidade, nome dos participantes, cargo e assinatura. Listas consolidadas no Status Report semanal. |
| **Fonte** | Plano Geral — Secao 6 (Recursos); LAC-005 |

### RF018 — Elaboracao do Framework de KPIs do Projeto

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve definir o framework de indicadores-chave de desempenho (KPIs) para monitoramento do projeto. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Framework documentado ate 11/04/2026, contendo no minimo 6 KPIs com: nome do indicador, formula de calculo, meta, frequencia de medicao e responsavel pela coleta. KPIs obrigatorios: SPI, CPI, taxa de presenca em workshops, taxa de resolucao de impedimentos, aderencia ao cronograma de entregas KPMG, taxa de presenca de Sponsors no Comite Executivo. |
| **Fonte** | Plano Geral — Secoes 3, 4, 5 |

### RF019 — Designacao de Profissionais Internos GAB por Area de Processo

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve fornecer lista nominal dos profissionais internos do GAB designados para participar dos workshops em cada area de processo e entidade. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Lista nominal entregue ao VMO ate 1 dia util antes do inicio dos workshops de cada area, contendo: nome, cargo, area de processo, entidade (Holding/VixPar/VAB) e confirmacao de disponibilidade. Para a Semana 1, lista ate 06/04/2026. |
| **Fonte** | LAC-005; TAP PREM-02; Risco R01 |

### RF020 — Registro Formal de Baseline do Projeto

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve registrar a baseline do projeto (escopo, cronograma e orcamento) como referencia para medicao de desvios ao longo da execucao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Baseline registrada ate 07/04/2026, contendo: (a) escopo conforme TAP Secoes 5 e 6; (b) cronograma conforme TAP Secao 13 com datas-chave; (c) orcamento conforme TAP Secao 12 (Fase 1: R$ 930.000; Fase 2: R$ 170.000; Total: R$ 1.100.000). Documento versionado e armazenado no repositorio do VMO. |
| **Fonte** | TAP Secoes 5, 12, 13; Plano Geral — Secoes 2, 3, 4 |

---

## 4. Requisitos Funcionais — Monitoramento e Controle

### RF021 — Formato Padronizado do Status Report Semanal

| Atributo | Detalhe |
|---|---|
| **Descricao** | O Status Report semanal deve seguir formato padronizado definido pelo VMO, com secoes obrigatorias e indicadores quantitativos. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Template de Status Report definido e aprovado pelo GP Interno ate 07/04/2026, contendo no minimo as secoes: (a) resumo executivo (3-5 linhas); (b) RAG status geral (Red/Amber/Green); (c) indicadores SPI e CPI (quando dados disponiveis); (d) progresso por marco (% conclusao); (e) top 3 riscos com classificacao atualizada; (f) impedimentos abertos (com idade em dias); (g) proximos passos com responsaveis e prazos. |
| **Fonte** | Plano Geral — Secao 7; RF008 |

### RF022 — Rastreamento de Presenca nos Workshops

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve manter registro consolidado de presenca nos workshops, permitindo identificar areas ou entidades com participacao abaixo do esperado. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Planilha ou registro atualizado semanalmente contendo: (a) sessao (data, area, entidade); (b) numero de participantes convocados vs. presentes; (c) taxa de presenca percentual por sessao; (d) alerta automatico quando taxa de presenca for inferior a 70% em qualquer sessao. Consolidado reportado no Status Report semanal. |
| **Fonte** | Risco R01; TAP PREM-02; RF017 |

### RF023 — Atualizacao do Registro de Riscos

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve atualizar o registro de riscos do projeto semanalmente, incluindo novos riscos identificados e reclassificacao de riscos existentes. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Registro de riscos atualizado toda quarta-feira (junto com o Status Report), contendo para cada risco: ID, descricao, probabilidade, impacto, classificacao, status da resposta planejada, responsavel e data da ultima atualizacao. Novos riscos identificados durante a semana devem ser incluidos com justificativa. |
| **Fonte** | Plano Geral — Secao 8; TAP Secao 10 |

### RF024 — Manutencao do Log de Issues/Impedimentos

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve manter log de issues e impedimentos do projeto com rastreabilidade completa desde a abertura ate a resolucao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Log mantido com os seguintes campos por issue: ID, descricao, data de abertura, responsavel, severidade (Alta/Media/Baixa), status (Aberto/Em Tratamento/Resolvido), data de resolucao, resolucao aplicada. Issues com mais de 3 dias uteis sem resolucao devem ser escaladas ao Comite Executivo. |
| **Fonte** | Plano Geral — Secoes 1, 7; Flash Report |

### RF025 — Acompanhamento Orcamentario vs. Contrato

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve manter controle de execucao orcamentaria confrontando valores realizados (invoices pagos) com o orcamento contratado. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Relatorio de acompanhamento orcamentario atualizado a cada pagamento de invoice, contendo: (a) valor contratado por fase; (b) valor faturado acumulado; (c) valor pago acumulado; (d) percentual de execucao financeira vs. percentual de execucao fisica (CPI); (e) previsao de desembolso restante. Desvios superiores a 10% entre execucao fisica e financeira devem ser reportados ao Comite Executivo. |
| **Fonte** | TAP Secao 12; Plano Geral — Secao 4; TAP CS-05 |

### RF026 — Monitoramento de Aderencia ao Cronograma

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve monitorar a aderencia do projeto ao cronograma baseline, reportando desvios no Status Report semanal. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Cada Status Report semanal deve conter: (a) status de cada marco (no prazo / em risco / atrasado); (b) calculo do SPI (Schedule Performance Index) quando aplicavel; (c) para marcos atrasados: numero de dias de atraso, causa raiz e plano de recuperacao. Marcos com atraso superior a 2 dias uteis devem ser escalados ao Comite Executivo. |
| **Fonte** | Plano Geral — Secao 3; TAP Secao 13 |

### RF027 — Controle de Lacunas de Informacao

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve manter registro atualizado das lacunas de informacao (LACs) identificadas durante o projeto, com responsavel e prazo para resolucao. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Registro de LACs atualizado semanalmente, contendo: ID, descricao, impacto, responsavel, prazo, status (Aberta/Resolvida/Cancelada), data de resolucao. LACs com prazo vencido devem ser destacadas no Status Report. As 12 LACs identificadas na documentacao base (LAC-001 a LAC-013) devem constar no registro inicial. |
| **Fonte** | Documentacao Base — Secao "Lacunas de Informacao Remanescentes" |

### RF028 — Monitoramento de Condicoes Bloqueantes

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve monitorar diariamente o status das condicoes bloqueantes (CB-01 e CB-02) ate sua resolucao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Status das condicoes bloqueantes verificado diariamente e registrado no Flash Report. Condicao bloqueante nao resolvida apos seu prazo limite (CB-01: 07/04/2026; CB-02: 06/04/2026) deve ser escalada ao Sponsor Executivo Principal (Decio Luiz Chieppe) em ate 4 horas uteis. |
| **Fonte** | Qualificacao Secao 5; CB-01; CB-02 |

### RF029 — Verificacao de Consistencia entre Documentos do Projeto

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve realizar verificacao de consistencia entre os documentos do projeto (TAP, PM Canvas, Plano Geral, Status Reports) a cada nova versao de documento produzida. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Checklist de consistencia aplicado com pelo menos 15 elementos-chave verificados (conforme tabela de verificacao da Documentacao Base), com resultado "Consistente" ou "Inconsistente" por elemento. Inconsistencias encontradas devem ser corrigidas em ate 2 dias uteis. |
| **Fonte** | Documentacao Base — Secao "Verificacao de Consistencia" |

### RF030 — Registro de Entregas Parciais da KPMG

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve registrar formalmente cada entrega parcial da KPMG, com data de recebimento e status de validacao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Registro contendo para cada entrega: (a) descricao da entrega; (b) data prevista vs. data efetiva de recebimento; (c) responsavel pela validacao no lado GAB; (d) status (Recebido/Em Revisao/Aceito/Rejeitado com ressalvas); (e) prazo de aceite ou devolucao (maximo 3 dias uteis apos recebimento). |
| **Fonte** | Plano Geral — Secao 9 (Aquisicoes); TAP CS-01 |

---

## 5. Requisitos Funcionais — Comunicacao e Reporting

### RF031 — Formato Padronizado do Flash Report

| Atributo | Detalhe |
|---|---|
| **Descricao** | O Flash Report diario deve seguir formato padronizado com secoes obrigatorias que permitam rastreabilidade operacional. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Template de Flash Report definido ate 07/04/2026, contendo no minimo: (a) data e participantes; (b) atividades realizadas no dia anterior; (c) atividades previstas para o dia; (d) impedimentos identificados (com classificacao de severidade); (e) decisoes tomadas. Formato maximo: 1 pagina A4 ou equivalente digital. |
| **Fonte** | Plano Geral — Secao 7; RF009 |

### RF032 — Cadencia e Distribuicao do Status Report

| Atributo | Detalhe |
|---|---|
| **Descricao** | O Status Report semanal deve ser distribuido as quartas-feiras para uma lista de distribuicao pre-definida, com antecedencia ao Comite Executivo de quinta-feira. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Status Report distribuido toda quarta-feira ate as 18h para: GP Interno, leads KPMG (Wallacy Lima), VMO Autonomo. Versao executiva resumida (1 pagina) enviada aos Sponsors ate as 20h da mesma quarta-feira. Atraso na entrega superior a 4 horas deve ser justificado na edicao seguinte. |
| **Fonte** | Plano Geral — Secao 7 |

### RF033 — Pauta e Ata do Comite Executivo

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve preparar pauta do Comite Executivo semanal (quintas-feiras) com antecedencia e produzir ata formal apos cada sessao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Pauta distribuida aos participantes ate as 12h de quarta-feira (24h antes da sessao); (b) Ata distribuida ate 1 dia util apos a sessao, conforme criterios do RF013; (c) Pauta deve conter: itens de decisao, itens informacionais, status de acoes pendentes de sessoes anteriores, riscos a serem escalados. |
| **Fonte** | Plano Geral — Secao 7; RF013 |

### RF034 — Notificacao de Riscos Elevados a Classificacao CRITICA

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve notificar os Sponsors imediatamente quando um risco for reclassificado para nivel CRITICO (probabilidade Media/Alta + impacto Alto). |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Notificacao enviada por e-mail aos 3 Sponsors e ao Socio KPMG em ate 4 horas uteis apos a identificacao ou reclassificacao do risco, contendo: descricao do risco, classificacao anterior e atual, impacto potencial no projeto, resposta planejada e decisao necessaria. |
| **Fonte** | Plano Geral — Secao 8; Risco R01-R07 |

### RF035 — Ciclo de Revisao e Feedback para Entregas KPMG

| Atributo | Detalhe |
|---|---|
| **Descricao** | O projeto deve estabelecer ciclo formal de revisao e feedback para cada entrega principal da KPMG. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Ciclo definido ate 11/04/2026, contendo: (a) prazo de revisao pelo GP Interno: 2 dias uteis apos recebimento; (b) prazo para consolidacao de feedback das areas: 1 dia util adicional; (c) prazo para devolutiva da KPMG: 2 dias uteis apos recebimento do feedback; (d) criterios de aceite ou rejeicao por entrega. |
| **Fonte** | Plano Geral — Secao 5 (Qualidade); Secao 9 (Aquisicoes) |

### RF036 — Comunicacao de Convocacao de Workshops

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG, em coordenacao com o GP Interno, deve enviar convocacao formal para cada sessao de workshop com antecedencia minima. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Convocacao enviada por e-mail e calendario corporativo com antecedencia minima de 3 dias uteis, contendo: data, horario, duracao estimada, area de processo, entidade, pauta de trabalho, participantes convocados e materiais preparatorios (quando aplicavel). |
| **Fonte** | Plano Geral — Secao 7 (Matriz de Comunicacao Complementar) |

### RF037 — Reporte de Progresso dos Workshops ao VMO

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve reportar ao VMO o status de conclusao dos workshops por area de processo e entidade, permitindo monitoramento de cobertura. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Reporte semanal no Status Report contendo: (a) matriz de cobertura (7 areas x 3 entidades) com status por celula (Realizado/Pendente/Cancelado); (b) percentual geral de cobertura; (c) sessoes reprogramadas com justificativa. Meta: 100% de cobertura ate 17/04/2026. |
| **Fonte** | TAP CS-02; Plano Geral — Secao 3 |

### RF038 — Lista de Distribuicao Formal do Projeto

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve formalizar a lista de distribuicao de cada tipo de comunicacao do projeto (Flash Report, Status Report, Comite Executivo, comunicados gerais). |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Lista de distribuicao documentada ate 09/04/2026, contendo para cada tipo de comunicacao: destinatarios (nome e e-mail), tipo de distribuicao (para/cc), formato de envio (e-mail/reuniao/documento). |
| **Fonte** | Plano Geral — Secao 7; LAC-009 |

### RF039 — Comunicacao de Resultados Preliminares de Scoring

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve apresentar resultados preliminares de scoring ao GP Interno antes da apresentacao final ao Comite Executivo, permitindo revisao e ajustes. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Resultados preliminares apresentados ao GP Interno ate 3 dias uteis antes da sessao final de apresentacao ao Comite Executivo, em formato que permita identificar: scores por pilar, scores por plataforma, ranking preliminar e pontos de atencao. |
| **Fonte** | Plano Geral — Secao 5 (Qualidade); PM Canvas E-03, E-04 |

### RF040 — Reporte de Status das Condicoes Desejaveis

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve acompanhar e reportar o status de resolucao das condicoes desejaveis (CD-01 a CD-05) identificadas na qualificacao. |
| **Prioridade** | Could Have |
| **Criterio de Aceitacao** | Status das 5 condicoes desejaveis reportado no Status Report semanal ate sua resolucao, com indicacao de: status (Pendente/Resolvida), data de resolucao e observacoes. |
| **Fonte** | Qualificacao Secao 5 (Condicoes Desejaveis) |

---

## 6. Requisitos Funcionais — Gestao de Qualidade das Entregas KPMG

### RF041 — Criterios de Validacao da Matriz de Aderencia

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve validar cada matriz de aderencia entregue pela KPMG conforme criterios de qualidade pre-definidos. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Checklist de validacao aplicado a cada matriz, verificando: (a) 100% das celulas preenchidas (3 plataformas x 7 areas x 3 entidades); (b) escala de aderencia utilizada de forma consistente (definicao unica da escala em toda a matriz); (c) justificativa textual para cada nota de aderencia; (d) referencia ao workshop ou fonte de dados que embasou a nota. Matriz com mais de 5% de celulas sem justificativa deve ser devolvida para complementacao. |
| **Fonte** | RF002; TAP CS-02, CS-03; Plano Geral — Secao 5 |

### RF042 — Auditabilidade do Calculo do Score Model

| Atributo | Detalhe |
|---|---|
| **Descricao** | O Score Model entregue pela KPMG deve ser auditavel, permitindo que o GAB verifique a composicao de cada pontuacao final. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Score Model entregue em formato que permita rastreio completo do calculo: (a) nota bruta por criterio de avaliacao; (b) peso de cada criterio dentro do pilar; (c) nota ponderada por pilar; (d) nota final consolidada por plataforma; (e) formula de calculo documentada; (f) arquivo em formato editavel (Excel ou equivalente) para verificacao numerica independente. |
| **Fonte** | RF003; TAP CS-03; Plano Geral — Secao 5; Risco R03 |

### RF043 — Padrao de Documentacao de Workshops

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve documentar cada sessao de workshop seguindo padrao que permita rastreabilidade do levantamento de processos. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Documentacao de cada workshop contendo: (a) area de processo e entidade avaliada; (b) data, duracao e local; (c) participantes (KPMG e GAB) com nome e cargo; (d) processos-chave levantados (AS-IS); (e) requisitos identificados; (f) observacoes e notas de campo; (g) pendencias para sessoes subsequentes. Documentacao disponibilizada ao GP Interno em ate 3 dias uteis apos a sessao. |
| **Fonte** | PM Canvas E-01; TAP Escopo item 3; Plano Geral — Secao 5 |

### RF044 — Processo de Aceite Formal de Entregas KPMG

| Atributo | Detalhe |
|---|---|
| **Descricao** | O projeto deve possuir processo formal de aceite para cada entrega principal da KPMG (mapeamento AS-IS, matrizes de aderencia, Score Model, relatorio de recomendacao). |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Processo documentado contendo: (a) responsavel pelo aceite no lado GAB (GP Interno para entregas operacionais; Comite Executivo para relatorio final); (b) prazo maximo para aceite: 3 dias uteis para entregas operacionais, 5 dias uteis para relatorio final; (c) formato do termo de aceite (documento padronizado com campos: entrega, data, status, observacoes, assinatura); (d) procedimento para rejeicao com devolucao justificada. |
| **Fonte** | Plano Geral — Secao 9 (Aquisicoes); RF030 |

### RF045 — Confirmacao da Metodologia Score Model

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve fornecer documentacao oficial da metodologia Score Model Powered Enterprise utilizada no projeto, resolvendo a inconsistencia entre 5 e 6 pilares. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Documento recebido ate 10/04/2026 (final da Semana 1), contendo: (a) numero e descricao de cada pilar; (b) peso percentual de cada pilar (totalizando 100%); (c) escala de pontuacao utilizada; (d) criterios de desempate (LAC-008); (e) assinatura ou confirmacao formal de Wallacy Lima ou Rodrigo Figaro. |
| **Fonte** | Qualificacao CD-04; LAC-007; LAC-008; Risco R07 |

### RF046 — Revisao de Qualidade dos Mapeamentos AS-IS

| Atributo | Detalhe |
|---|---|
| **Descricao** | Os gestores de area do GAB devem revisar e validar os mapeamentos de processos AS-IS produzidos pela KPMG antes que estes sejam utilizados para scoring. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Cada mapeamento AS-IS revisado e aprovado pelo gestor da area respectiva em ate 2 dias uteis apos disponibilizacao, com registro de: (a) data de recebimento; (b) data de revisao; (c) status (Aprovado/Aprovado com ressalvas/Rejeitado); (d) ressalvas ou correcoes solicitadas, quando aplicavel. Mapeamentos nao revisados dentro do prazo devem ser escalados ao Sponsor da respectiva entidade. |
| **Fonte** | PM Canvas E-01; Plano Geral — Secao 5; Risco R02 |

### RF047 — Verificacao de Cobertura de Areas e Entidades

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve verificar que todas as 7 areas de processo e 3 entidades estao sendo cobertas pelo assessment, sem lacunas de avaliacao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Matriz de cobertura (7 areas x 3 entidades = 21 celulas) atualizada semanalmente no Status Report, indicando para cada celula: status do workshop (Realizado/Pendente), status do mapeamento AS-IS (Entregue/Pendente), status do scoring (Realizado/Pendente). Meta: 100% de celulas com workshop realizado ate 17/04/2026; 100% com scoring ate 01/05/2026. |
| **Fonte** | TAP CS-02; PM Canvas E-02; Plano Geral — Secao 2 |

### RF048 — Padrao de Evidencias para Notas do Score Model

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve fornecer evidencia documental para cada nota atribuida no Score Model, reduzindo dependencia de percepcoes individuais. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Cada nota no Score Model acompanhada de: (a) referencia ao workshop ou fonte de dados; (b) justificativa textual de no minimo 2 linhas; (c) identificacao do avaliador KPMG responsavel. Notas sem evidencia documental devem ser sinalizadas no processo de revisao. |
| **Fonte** | Risco R03; Plano Geral — Secao 5 |

### RF049 — Relatorio de Recomendacao com Secao de Limitacoes

| Atributo | Detalhe |
|---|---|
| **Descricao** | O relatorio final de recomendacao da KPMG deve conter secao explicita sobre limitacoes da analise e premissas assumidas. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Secao de limitacoes presente no relatorio final, contendo: (a) premissas da avaliacao; (b) areas nao cobertas ou cobertas parcialmente (se houver); (c) limitacoes de dados; (d) fatores externos nao considerados; (e) disclaimer de responsabilidade sobre a decisao final (que cabe ao GAB). |
| **Fonte** | Plano Geral — Secao 5; TAP Secao 6 (Fora do Escopo) |

### RF050 — Validacao Cruzada de Scores entre Entidades

| Atributo | Detalhe |
|---|---|
| **Descricao** | A KPMG deve demonstrar que os scores atribuidos sao consistentes entre as 3 entidades, ou justificar diferencas significativas quando existirem. |
| **Prioridade** | Could Have |
| **Criterio de Aceitacao** | Analise de consistencia documentada no relatorio final, contendo: (a) comparacao de scores por entidade para cada plataforma; (b) justificativa para diferencas superiores a 20% entre entidades no mesmo pilar; (c) recomendacao de plataforma considerando visao consolidada do grupo e visao por entidade. |
| **Fonte** | TAP Escopo item 1; PM Canvas E-03 |

---

## 7. Requisitos Funcionais — Gestao de Mudancas e Riscos

### RF051 — Processo de Solicitacao de Mudanca

| Atributo | Detalhe |
|---|---|
| **Descricao** | O projeto deve possuir processo formal para registro e tratamento de solicitacoes de mudanca de escopo, cronograma ou orcamento. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Processo documentado ate 11/04/2026, contendo: (a) formulario padronizado de solicitacao de mudanca (descricao, justificativa, impacto estimado em escopo/cronograma/custo, urgencia); (b) fluxo de aprovacao (GP Interno analisa → Comite Executivo decide); (c) prazo maximo para analise: 2 dias uteis; (d) prazo maximo para decisao: na proxima sessao do Comite Executivo (maximo 7 dias). |
| **Fonte** | Plano Geral — Secao 1 (Integracao); TAP REST-02, REST-03 |

### RF052 — Registro de Mudancas Aprovadas

| Atributo | Detalhe |
|---|---|
| **Descricao** | Toda mudanca aprovada pelo Comite Executivo deve ser registrada formalmente e a baseline do projeto deve ser atualizada. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Registro contendo: (a) ID da solicitacao; (b) descricao da mudanca; (c) impacto em escopo, cronograma e/ou custo; (d) data de aprovacao e instancia aprovadora; (e) nova baseline (quando aplicavel); (f) comunicacao da mudanca a todos os stakeholders afetados em ate 1 dia util apos aprovacao. |
| **Fonte** | Plano Geral — Secao 1; RF020 |

### RF053 — Escalada de Impedimentos ao Comite Executivo

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve escalar impedimentos nao resolvidos em nivel operacional ao Comite Executivo para decisao. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Impedimento escalado quando: (a) nao resolvido em 3 dias uteis no nivel operacional (GP Interno + KPMG); ou (b) impacto estimado em atraso de marco superior a 2 dias uteis; ou (c) requer decisao que excede autoridade do GP Interno. Escalada formalizada na pauta do Comite Executivo com: descricao, tentativas de resolucao, opcoes de acao e recomendacao. |
| **Fonte** | Plano Geral — Secoes 7, 8; RF024 |

### RF054 — Monitoramento Proativo de Risco R01 (Engajamento nos Workshops)

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve monitorar proativamente o engajamento das areas de negocio nos workshops, acionando respostas antes que o risco se materialize. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Monitoramento diario via Flash Report contendo: (a) confirmacao de presenca dos participantes convocados para a sessao do dia; (b) alerta quando taxa de presenca for inferior a 70%; (c) acionamento dos Sponsors em ate 4 horas quando area nao comparece sem justificativa; (d) registro de sessoes reagendadas com nova data confirmada em ate 1 dia util. |
| **Fonte** | Risco R01; TAP PREM-02; RF022 |

### RF055 — Monitoramento de Risco R05 (Continuidade do GP Interno)

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve monitorar o status de titularizacao ou designacao de backup do GP Interno ate resolucao definitiva. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Status verificado semanalmente no Status Report ate resolucao. Se CB-01 nao for resolvida ate 07/04/2026, risco R05 deve ser reclassificado para CRITICO e escalado conforme RF034. Resolucao aceita: (a) titularizacao formal de Marcelo Silveira; ou (b) designacao formal de backup com dados de contato e data de disponibilidade. |
| **Fonte** | Risco R05; CB-01; RF014 |

### RF056 — Tratamento de Scope Creep

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve identificar e reportar qualquer atividade executada fora do escopo contratual do projeto (scope creep). |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Desvio de escopo identificado e registrado em ate 1 dia util apos deteccao, contendo: descricao do desvio, quem solicitou, impacto estimado e recomendacao (formalizar como mudanca ou reverter). Reportado no Status Report semanal e, se significativo, escalado ao Comite Executivo. |
| **Fonte** | Plano Geral — Secao 2 (Escopo); TAP REST-02 |

### RF057 — Plano de Contingencia para Indisponibilidade de Participantes

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve elaborar plano de contingencia para garantir continuidade dos workshops em caso de indisponibilidade de participantes-chave. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Plano documentado ate 09/04/2026, contendo: (a) lista de substitutos para cada participante-chave por area de processo; (b) regra para reagendamento de sessoes (maximo 2 dias uteis de atraso); (c) sessoes de reposicao previstas no mesmo dia da ausencia (quando possivel); (d) limite de reagendamentos por area (maximo 2 por semana). |
| **Fonte** | Risco R06; TAP PREM-02 |

### RF058 — Registro de Licoes Aprendidas

| Atributo | Detalhe |
|---|---|
| **Descricao** | O VMO Autonomo deve coletar e registrar licoes aprendidas ao longo do projeto para alimentar a knowledge base do portfolio. |
| **Prioridade** | Could Have |
| **Criterio de Aceitacao** | Registro atualizado ao final de cada fase (Fase 1 e Fase 2), contendo: (a) licao identificada; (b) contexto (o que aconteceu); (c) impacto (positivo ou negativo); (d) recomendacao para projetos futuros. Minimo de 5 licoes registradas por fase. |
| **Fonte** | Plano Geral — Secao 1 (Integracao); Pipeline VMO |

### RF059 — Revisao de Riscos Pos-Workshops

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve realizar revisao do registro de riscos apos a conclusao dos workshops (final da Semana 2), incorporando novos riscos identificados durante o levantamento de processos. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | Revisao documentada ate 20/04/2026, contendo: (a) reavaliacao de probabilidade e impacto dos riscos existentes (R01-R07); (b) novos riscos identificados durante os workshops; (c) atualizacao das respostas planejadas; (d) apresentacao ao Comite Executivo na sessao seguinte. |
| **Fonte** | Plano Geral — Secao 8; RF023 |

### RF060 — Processo de Aprovacao de Invoices KPMG

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve validar cada invoice da KPMG vinculando-o a entrega parcial ou marco contratual correspondente antes de encaminhar para pagamento. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | Cada invoice processado com: (a) verificacao da entrega correspondente (status aceito conforme RF030); (b) conferencia do valor contra baseline contratual; (c) aprovacao formal do GP Interno em ate 3 dias uteis apos recebimento; (d) encaminhamento a Area Financeira GAB com referencia ao marco contratual. Invoices sem entrega aceita correspondente devem ser retidos ate regularizacao. |
| **Fonte** | Plano Geral — Secao 9 (Aquisicoes) |

---

## 8. Requisitos Nao-Funcionais

### RNF001 — Disponibilidade e Formato da Documentacao do Projeto

| Atributo | Detalhe |
|---|---|
| **Descricao** | Toda documentacao do projeto deve estar armazenada em repositorio acessivel ao GP Interno, Sponsors e VMO Autonomo, em formatos padronizados. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Repositorio unico definido ate 07/04/2026 (pasta compartilhada, SharePoint ou equivalente); (b) Documentos em formato PDF para versoes finais e formato editavel (Word, Excel, PowerPoint) para documentos de trabalho; (c) Nomenclatura padronizada: [PROJ-2026-003]_[TipoDocumento]_[vX.X]_[AAAA-MM-DD]; (d) Acesso confirmado para: GP Interno, 3 Sponsors, leads KPMG, VMO Autonomo. |
| **Fonte** | Plano Geral — Secao 1 (Integracao) |

### RNF002 — Tempo de Resposta para Escaladas

| Atributo | Detalhe |
|---|---|
| **Descricao** | Impedimentos e escaladas devem ser respondidos dentro de prazos definidos conforme o nivel de severidade. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Severidade Alta (impacto em marco do projeto): resposta do responsavel em ate 4 horas uteis; decisao do Comite Executivo na proxima sessao ou sessao extraordinaria em ate 24 horas uteis; (b) Severidade Media: resposta em ate 1 dia util; decisao em ate 3 dias uteis; (c) Severidade Baixa: resposta em ate 2 dias uteis; decisao em ate 5 dias uteis. |
| **Fonte** | Plano Geral — Secoes 7, 8; RF053 |

### RNF003 — Confidencialidade dos Dados do Assessment

| Atributo | Detalhe |
|---|---|
| **Descricao** | Os dados levantados durante o assessment (processos internos, custos, indicadores operacionais do GAB) devem ser tratados com confidencialidade por todas as partes envolvidas. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Clausula de confidencialidade presente no contrato com a KPMG (verificacao: sim/nao); (b) Documentos do projeto classificados como "Confidencial — Grupo Aguia Branca" em cabecalho ou rodape; (c) Compartilhamento de informacoes do assessment com terceiros (incluindo fornecedores SAP, Oracle, TOTVS) somente mediante autorizacao formal do Sponsor Executivo Principal. |
| **Fonte** | TAP Secao 4 (Justificativa); Contrato KPMG |

### RNF004 — Trilha de Auditoria de Decisoes

| Atributo | Detalhe |
|---|---|
| **Descricao** | Todas as decisoes relevantes do projeto devem ser rastreadas com registro de quem decidiu, quando e com base em que informacoes. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Decisoes registradas em ata do Comite Executivo (RF013); (b) Cada decisao com: descricao, data, decisor(es), opcoes consideradas e justificativa da escolha; (c) Decisoes fora do Comite Executivo registradas pelo GP Interno em log de decisoes, com referencia ao autorizador. |
| **Fonte** | Plano Geral — Secao 1; TAP CS-06 |

### RNF005 — Idioma e Padrao de Redacao dos Documentos

| Atributo | Detalhe |
|---|---|
| **Descricao** | Todos os documentos do projeto devem ser redigidos em portugues do Brasil, com linguagem formal de negocios. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Idioma: portugues do Brasil (pt-BR); (b) Termos tecnicos em ingles permitidos quando consagrados (ERP, Score Model, RFP, AS-IS, workshop); (c) Documentos KPMG podem ser bilíngues (pt-BR + en) quando a metodologia Powered Enterprise exigir terminologia original; (d) Siglas definidas na primeira ocorrencia em cada documento. |
| **Fonte** | Plano Geral — Secao 7 |

### RNF006 — Versionamento de Documentos

| Atributo | Detalhe |
|---|---|
| **Descricao** | Documentos do projeto devem ser versionados, permitindo identificar a versao mais atual e o historico de alteracoes. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | (a) Cada documento com campo de versao no cabecalho (formato X.Y — major.minor); (b) Historico de revisoes com: versao, data, autor e descricao da alteracao; (c) Versoes anteriores preservadas no repositorio (nao sobrescritas). |
| **Fonte** | Plano Geral — Secao 1 |

### RNF007 — Retencao de Documentacao Pos-Projeto

| Atributo | Detalhe |
|---|---|
| **Descricao** | A documentacao completa do projeto deve ser retida e acessivel apos o encerramento para referencia futura durante a implementacao do ERP. |
| **Prioridade** | Should Have |
| **Criterio de Aceitacao** | (a) Toda documentacao consolidada em pacote de encerramento ate 15 dias apos a conclusao da Fase 2; (b) Retencao minima de 5 anos (periodo estimado de implementacao + estabilizacao do novo ERP); (c) Responsavel pela custodia definido (Area de TI ou Escritorio de Projetos do GAB). |
| **Fonte** | TAP Secao 4 (decisao de 10+ anos); Plano Geral — Secao 1 |

### RNF008 — Disponibilidade do GP Interno para Interacoes com VMO

| Atributo | Detalhe |
|---|---|
| **Descricao** | O GP Interno deve estar disponivel para interacoes com o VMO Autonomo durante o horario comercial, garantindo fluxo de informacoes para monitoramento. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Tempo de resposta a solicitacoes do VMO: ate 4 horas uteis para assuntos operacionais; ate 1 dia util para assuntos documentais; (b) Canal de comunicacao definido (e-mail: marcelov@aguiabranca.com.br + canal de mensageria instantanea); (c) Em caso de ausencia programada, GP Interno deve informar VMO com 24h de antecedencia e indicar ponto focal substituto. |
| **Fonte** | TAP Secao 2; Plano Geral — Secao 7 |

### RNF009 — Integridade dos Dados de Scoring

| Atributo | Detalhe |
|---|---|
| **Descricao** | Os dados numericos do Score Model devem manter integridade durante todo o ciclo de producao, revisao e apresentacao, sem alteracoes nao rastreadas. |
| **Prioridade** | Must Have |
| **Criterio de Aceitacao** | (a) Score Model entregue em formato que preserve formulas e calculos (Excel ou equivalente — nao apenas PDF); (b) Qualquer alteracao de score apos primeira entrega deve ser registrada com: valor anterior, valor novo, justificativa e data; (c) Versao final do Score Model deve ser idêntica entre o arquivo de trabalho e o relatorio de recomendacao (verificacao cruzada). |
| **Fonte** | RF042; Risco R03; Plano Geral — Secao 5 |

### RNF010 — Backup e Recuperacao de Documentos Criticos

| Atributo | Detalhe |
|---|---|
| **Descricao** | Documentos criticos do projeto (Score Model, relatorio de recomendacao, atas do Comite Executivo) devem possuir copia de seguranca. |
| **Prioridade** | Could Have |
| **Criterio de Aceitacao** | (a) Copia de seguranca em local distinto do repositorio principal (e-mail para stakeholder designado ou armazenamento secundario); (b) Backup realizado no mesmo dia da producao ou recebimento do documento critico; (c) Teste de recuperacao: ao menos 1 documento recuperado com sucesso a partir do backup durante o projeto (validacao do processo). |
| **Fonte** | Plano Geral — Secao 1 |

---

## 9. Tabela Resumo MoSCoW

### Requisitos Funcionais

| ID | Descricao Resumida | Prioridade |
|---|---|---|
| RF001 | Entrega do Relatorio de Recomendacao de Plataforma ERP | Must Have |
| RF002 | Entrega das Matrizes de Aderencia por Area de Processo | Must Have |
| RF003 | Entrega do Score Comparativo por Pilar Metodologico | Must Have |
| RF004 | Entrega de Material de Apresentacao Executiva | Must Have |
| RF005 | Elaboracao e Aprovacao do TAP pelo VMO | Must Have |
| RF006 | Elaboracao do PM Canvas | Must Have |
| RF007 | Elaboracao do Plano Geral do Projeto | Must Have |
| RF008 | Producao de Status Report Semanal | Must Have |
| RF009 | Producao de Flash Report Diario | Must Have |
| RF010 | Elaboracao do Plano de Riscos Detalhado | Should Have |
| RF011 | Participacao dos Sponsors no Comite Executivo Semanal | Must Have |
| RF012 | Participacao do Socio KPMG no Comite Executivo Semanal | Must Have |
| RF013 | Registro de Ata do Comite Executivo | Must Have |
| RF014 | Definicao e Titularizacao do GP Interno | Must Have |
| RF015 | Fornecimento da Agenda de Workshops ao VMO | Must Have |
| RF016 | Fluxo de Aprovacao para Transicao de Fases | Must Have |
| RF017 | Documentacao de Participantes e Presenca nos Workshops | Must Have |
| RF018 | Elaboracao do Framework de KPIs do Projeto | Should Have |
| RF019 | Designacao de Profissionais Internos GAB por Area | Must Have |
| RF020 | Registro Formal de Baseline do Projeto | Must Have |
| RF021 | Formato Padronizado do Status Report Semanal | Must Have |
| RF022 | Rastreamento de Presenca nos Workshops | Must Have |
| RF023 | Atualizacao do Registro de Riscos | Must Have |
| RF024 | Manutencao do Log de Issues/Impedimentos | Must Have |
| RF025 | Acompanhamento Orcamentario vs. Contrato | Should Have |
| RF026 | Monitoramento de Aderencia ao Cronograma | Must Have |
| RF027 | Controle de Lacunas de Informacao | Should Have |
| RF028 | Monitoramento de Condicoes Bloqueantes | Must Have |
| RF029 | Verificacao de Consistencia entre Documentos | Should Have |
| RF030 | Registro de Entregas Parciais da KPMG | Must Have |
| RF031 | Formato Padronizado do Flash Report | Must Have |
| RF032 | Cadencia e Distribuicao do Status Report | Must Have |
| RF033 | Pauta e Ata do Comite Executivo | Must Have |
| RF034 | Notificacao de Riscos Elevados a CRITICA | Must Have |
| RF035 | Ciclo de Revisao e Feedback para Entregas KPMG | Must Have |
| RF036 | Comunicacao de Convocacao de Workshops | Should Have |
| RF037 | Reporte de Progresso dos Workshops ao VMO | Must Have |
| RF038 | Lista de Distribuicao Formal do Projeto | Should Have |
| RF039 | Comunicacao de Resultados Preliminares de Scoring | Should Have |
| RF040 | Reporte de Status das Condicoes Desejaveis | Could Have |
| RF041 | Criterios de Validacao da Matriz de Aderencia | Must Have |
| RF042 | Auditabilidade do Calculo do Score Model | Must Have |
| RF043 | Padrao de Documentacao de Workshops | Must Have |
| RF044 | Processo de Aceite Formal de Entregas KPMG | Must Have |
| RF045 | Confirmacao da Metodologia Score Model | Must Have |
| RF046 | Revisao de Qualidade dos Mapeamentos AS-IS | Must Have |
| RF047 | Verificacao de Cobertura de Areas e Entidades | Must Have |
| RF048 | Padrao de Evidencias para Notas do Score Model | Should Have |
| RF049 | Relatorio de Recomendacao com Secao de Limitacoes | Should Have |
| RF050 | Validacao Cruzada de Scores entre Entidades | Could Have |
| RF051 | Processo de Solicitacao de Mudanca | Must Have |
| RF052 | Registro de Mudancas Aprovadas | Must Have |
| RF053 | Escalada de Impedimentos ao Comite Executivo | Must Have |
| RF054 | Monitoramento Proativo de Risco R01 (Engajamento) | Must Have |
| RF055 | Monitoramento de Risco R05 (Continuidade GP) | Must Have |
| RF056 | Tratamento de Scope Creep | Should Have |
| RF057 | Plano de Contingencia para Indisponibilidade | Should Have |
| RF058 | Registro de Licoes Aprendidas | Could Have |
| RF059 | Revisao de Riscos Pos-Workshops | Should Have |
| RF060 | Processo de Aprovacao de Invoices KPMG | Must Have |

### Requisitos Nao-Funcionais

| ID | Descricao Resumida | Prioridade |
|---|---|---|
| RNF001 | Disponibilidade e Formato da Documentacao | Must Have |
| RNF002 | Tempo de Resposta para Escaladas | Must Have |
| RNF003 | Confidencialidade dos Dados do Assessment | Must Have |
| RNF004 | Trilha de Auditoria de Decisoes | Must Have |
| RNF005 | Idioma e Padrao de Redacao | Must Have |
| RNF006 | Versionamento de Documentos | Should Have |
| RNF007 | Retencao de Documentacao Pos-Projeto | Should Have |
| RNF008 | Disponibilidade do GP Interno para VMO | Must Have |
| RNF009 | Integridade dos Dados de Scoring | Must Have |
| RNF010 | Backup e Recuperacao de Documentos Criticos | Could Have |

### Distribuicao MoSCoW

| Prioridade | Funcionais (RF) | Nao-Funcionais (RNF) | Total | % |
|---|---|---|---|---|
| Must Have | 40 | 6 | 46 | 65,7% |
| Should Have | 14 | 2 | 16 | 22,9% |
| Could Have | 4 | 1 | 5 | 7,1% |
| Won't Have | 2 | 1 | 3 | 4,3% |
| **Total** | **60** | **10** | **70** | **100%** |

**Nota sobre Won't Have:** Os seguintes requisitos foram considerados e explicitamente excluidos do escopo desta ERF:

| Item | Justificativa da Exclusao |
|---|---|
| Requisitos de funcionalidades das plataformas ERP | Fora do escopo do PMO — sao requisitos de negocio da KPMG |
| Requisitos de implementacao de ERP | Projeto futuro — fora do escopo deste assessment |
| Auditoria externa independente do Score Model | Desejavel mas impraticavel no prazo de 5 semanas do projeto |

---

## 10. Rastreabilidade

### 10.1 Matriz de Rastreabilidade: Requisito → Fonte

| ID | Fonte Primaria | Fonte Secundaria |
|---|---|---|
| RF001 | TAP CS-01 | PM Canvas E-04 |
| RF002 | TAP CS-02, CS-03 | PM Canvas E-02 |
| RF003 | TAP CS-03 | PM Canvas E-03 |
| RF004 | PM Canvas E-05 | TAP Secao 13 |
| RF005 | Documentacao Base (TAP) | Pipeline VMO Step 5 |
| RF006 | Documentacao Base (PM Canvas) | — |
| RF007 | Documentacao Base (Plano Geral) | — |
| RF008 | Plano Geral — Secao 7 | Qualificacao Proximo Passo #6 |
| RF009 | Plano Geral — Secao 7 | PM Canvas Bloco 4 |
| RF010 | TAP Secao 10 | Plano Geral — Secao 8 |
| RF011 | TAP CS-04, PREM-01 | Plano Geral — Secao 10 |
| RF012 | TAP Secao 2 | Plano Geral — Secao 7 |
| RF013 | Plano Geral — Secao 7 | — |
| RF014 | Qualificacao CB-01 | TAP PREM-07; Risco R05 |
| RF015 | Qualificacao CB-02, LAC-006 | — |
| RF016 | TAP CS-06 | TAP REST-01; LAC-013 |
| RF017 | Plano Geral — Secao 6 | LAC-005 |
| RF018 | Plano Geral — Secoes 3, 4, 5 | — |
| RF019 | LAC-005 | TAP PREM-02; Risco R01 |
| RF020 | TAP Secoes 5, 12, 13 | Plano Geral — Secoes 2, 3, 4 |
| RF021 | Plano Geral — Secao 7 | RF008 |
| RF022 | Risco R01 | TAP PREM-02 |
| RF023 | Plano Geral — Secao 8 | TAP Secao 10 |
| RF024 | Plano Geral — Secoes 1, 7 | — |
| RF025 | TAP Secao 12 | Plano Geral — Secao 4 |
| RF026 | Plano Geral — Secao 3 | TAP Secao 13 |
| RF027 | Documentacao Base — LACs | — |
| RF028 | Qualificacao Secao 5 | CB-01, CB-02 |
| RF029 | Documentacao Base — Verificacao | — |
| RF030 | Plano Geral — Secao 9 | TAP CS-01 |
| RF031 | Plano Geral — Secao 7 | RF009 |
| RF032 | Plano Geral — Secao 7 | — |
| RF033 | Plano Geral — Secao 7 | RF013 |
| RF034 | Plano Geral — Secao 8 | Riscos R01-R07 |
| RF035 | Plano Geral — Secoes 5, 9 | — |
| RF036 | Plano Geral — Secao 7 | — |
| RF037 | TAP CS-02 | Plano Geral — Secao 3 |
| RF038 | Plano Geral — Secao 7 | LAC-009 |
| RF039 | Plano Geral — Secao 5 | PM Canvas E-03, E-04 |
| RF040 | Qualificacao Secao 5 | — |
| RF041 | RF002 | TAP CS-02; Plano Geral — Secao 5 |
| RF042 | RF003 | Risco R03; Plano Geral — Secao 5 |
| RF043 | PM Canvas E-01 | Plano Geral — Secao 5 |
| RF044 | Plano Geral — Secao 9 | RF030 |
| RF045 | Qualificacao CD-04 | LAC-007; LAC-008; Risco R07 |
| RF046 | PM Canvas E-01 | Plano Geral — Secao 5; Risco R02 |
| RF047 | TAP CS-02 | PM Canvas E-02; Plano Geral — Secao 2 |
| RF048 | Risco R03 | Plano Geral — Secao 5 |
| RF049 | Plano Geral — Secao 5 | TAP Secao 6 |
| RF050 | TAP Escopo item 1 | PM Canvas E-03 |
| RF051 | Plano Geral — Secao 1 | TAP REST-02, REST-03 |
| RF052 | Plano Geral — Secao 1 | RF020 |
| RF053 | Plano Geral — Secoes 7, 8 | RF024 |
| RF054 | Risco R01 | TAP PREM-02 |
| RF055 | Risco R05; CB-01 | RF014 |
| RF056 | Plano Geral — Secao 2 | TAP REST-02 |
| RF057 | Risco R06 | TAP PREM-02 |
| RF058 | Plano Geral — Secao 1 | Pipeline VMO |
| RF059 | Plano Geral — Secao 8 | RF023 |
| RF060 | Plano Geral — Secao 9 | — |
| RNF001 | Plano Geral — Secao 1 | — |
| RNF002 | Plano Geral — Secoes 7, 8 | RF053 |
| RNF003 | TAP Secao 4 | Contrato KPMG |
| RNF004 | Plano Geral — Secao 1 | TAP CS-06 |
| RNF005 | Plano Geral — Secao 7 | — |
| RNF006 | Plano Geral — Secao 1 | — |
| RNF007 | TAP Secao 4 | Plano Geral — Secao 1 |
| RNF008 | TAP Secao 2 | Plano Geral — Secao 7 |
| RNF009 | RF042 | Risco R03; Plano Geral — Secao 5 |
| RNF010 | Plano Geral — Secao 1 | — |

### 10.2 Cobertura de Riscos do TAP pelos Requisitos

| Risco TAP | Requisitos que Endereçam |
|---|---|
| R01 — Baixo engajamento nos workshops | RF017, RF019, RF022, RF054, RF057 |
| R02 — Foco excessivo em ferramenta | RF046, RF048, RF049 |
| R03 — Percepcoes individuais vs. dados | RF042, RF048, RNF009 |
| R04 — Comunicacao insuficiente | RF031, RF032, RF033, RF034, RF038 |
| R05 — Descontinuidade GP Interno | RF014, RF028, RF055 |
| R06 — Atraso por indisponibilidade | RF015, RF022, RF026, RF057 |
| R07 — Inconsistencia Score Model | RF045 |

### 10.3 Cobertura de Criterios de Sucesso do TAP

| Criterio | Requisitos que Endereçam |
|---|---|
| CS-01 — Entrega relatorio recomendacao | RF001, RF030, RF044 |
| CS-02 — Cobertura 7 areas x 3 entidades | RF002, RF017, RF037, RF047 |
| CS-03 — Scoring 3 plataformas x 6 pilares | RF003, RF042, RF045 |
| CS-04 — Presenca Sponsors no Comite | RF011 |
| CS-05 — Aderencia ao orcamento | RF025, RF060 |
| CS-06 — Aprovacao formal da recomendacao | RF016, RF044, RNF004 |
| CS-07 — Inicio RFP conforme cronograma | RF016 |

---

## 11. Glossario de Termos

| Termo | Definicao |
|---|---|
| **Score Model** | Modelo de pontuacao estruturado utilizado pela KPMG (metodologia Powered Enterprise) para avaliar e comparar as plataformas ERP candidatas. Composto por 6 pilares ponderados: Estrategico (30%), Produto (20%), Tecnologia (20%), Cliente (10%), Financeiro (10%) e Operacao (10%). |
| **KPMG Powered Enterprise** | Metodologia proprietaria da KPMG para avaliacao e selecao de plataformas ERP, baseada em modelos de referencia de processos de negocio e scoring comparativo estruturado. |
| **Software Selection** | Processo estruturado de avaliacao, comparacao e selecao de uma plataforma de software (neste caso, ERP) a partir de criterios objetivos, conduzido tipicamente por consultoria especializada. Fase 1 deste projeto. |
| **Flash Report** | Reporte operacional diario de curta duracao (15-30 minutos), conduzido em formato stand-up, para alinhamento de atividades do dia, identificacao de impedimentos e decisoes rapidas entre GP Interno e equipe KPMG. |
| **Status Report** | Relatorio semanal consolidado de progresso do projeto, produzido pelo GP Interno as quartas-feiras, contendo indicadores de desempenho, riscos atualizados, impedimentos e proximos passos. |
| **Comite Executivo** | Instancia de governanca estrategica do projeto, reunida semanalmente as quintas-feiras, composta pelos 3 Sponsors do GAB (Decio, Paula, Patricia), Socio KPMG (Rodrigo Figaro) e GP Interno (Marcelo Silveira). Responsavel por decisoes estrategicas, escaladas e aprovacao formal de entregas. |
| **Sponsor** | Executivo de alto nivel com autoridade para aprovar a recomendacao final, autorizar investimentos e direcionar as areas internas do GAB. Neste projeto: Decio Luiz Chieppe (Sponsor Executivo Principal), Paula Barcelos T. Correa (Sponsor VAB) e Patricia Poubel Chieppe (Sponsor VixPar). |
| **GP (Gerente de Projeto)** | Profissional responsavel pela coordenacao operacional do projeto no lado do contratante (GAB). Neste projeto: Marcelo Silveira (interino). Atua como ponto focal entre KPMG, Sponsors e VMO. |
| **VMO (Value Management Office)** | Escritorio de gestao de valor que acompanha o portfolio de projetos do Grupo Aguia Branca, garantindo rastreabilidade, governanca e geracao de knowledge base. Neste projeto, operado pelo VMO Autonomo. |
| **ERF (Especificacao de Requisitos Funcionais)** | Documento formal que descreve, de forma testavel e rastreavel, os requisitos que devem ser atendidos pelo projeto para cumprir seus objetivos de governanca, monitoramento e qualidade. Este documento. |
| **TAP (Termo de Abertura do Projeto)** | Documento formal que autoriza a existencia do projeto, define seus objetivos, escopo, premissas, restricoes e nomeia o gerente do projeto. |
| **PM Canvas** | Ferramenta visual que sintetiza em 9 blocos os elementos essenciais de um projeto para comunicacao rapida e alinhamento entre partes interessadas. |
| **SAP ECC** | SAP ERP Central Component — plataforma ERP atual do Grupo Aguia Branca, versao 6.0, com suporte oficial da SAP previsto para encerramento em 2027 (end of maintenance). |
| **SAP S/4HANA Rise** | Plataforma ERP de nova geracao da SAP, oferecida como servico na nuvem (RISE with SAP). Uma das 3 candidatas neste assessment. |
| **Oracle ERP Cloud** | Plataforma ERP em nuvem da Oracle Corporation. Uma das 3 candidatas neste assessment. |
| **TOTVS Protheus** | Plataforma ERP da TOTVS, empresa brasileira de software. Uma das 3 candidatas neste assessment. |
| **Aderencia** | Grau de compatibilidade de uma plataforma ERP candidata com os requisitos e processos de negocio do Grupo Aguia Branca, medido por area de processo e por entidade. |
| **RFP (Request for Proposal)** | Processo formal de solicitacao de propostas comerciais a fornecedores. Fase 2 deste projeto (R$ 170.000), na qual os fornecedores finalistas da Fase 1 apresentam propostas detalhadas de implementacao. |
| **SBWP (Statement of Business Work Principles)** | Documento que define os principios e premissas de trabalho entre contratante e consultoria, tipicamente utilizado em engagements de consultoria de grande porte como referencia para a relacao de trabalho. |
| **End of Maintenance** | Encerramento do suporte oficial de um fabricante de software para uma versao de produto. No contexto deste projeto, refere-se ao encerramento do suporte da SAP ao SAP ECC 6.0, previsto para 2027, que motiva a necessidade de selecao de nova plataforma ERP. |
| **SPI (Schedule Performance Index)** | Indicador de desempenho de cronograma do projeto. SPI = Valor Agregado / Valor Planejado. SPI = 1.0 indica aderencia ao cronograma; SPI < 1.0 indica atraso; SPI > 1.0 indica adiantamento. |
| **CPI (Cost Performance Index)** | Indicador de desempenho de custo do projeto. CPI = Valor Agregado / Custo Real. CPI = 1.0 indica aderencia ao orcamento; CPI < 1.0 indica estouro; CPI > 1.0 indica economia. |
| **MoSCoW** | Metodo de priorizacao de requisitos: Must Have (obrigatorio), Should Have (importante mas nao critico), Could Have (desejavel), Won't Have (excluido do escopo atual). |
| **RAG Status** | Sistema de sinalizacao por cores: Red (vermelho — problemas criticos), Amber (ambar — riscos ou atencao necessaria), Green (verde — dentro do planejado). |
| **AS-IS** | Estado atual dos processos de negocio, conforme operam hoje na organizacao. O assessment mapeia os processos AS-IS para avaliar aderencia das plataformas candidatas. |
| **Scope Creep** | Expansao nao controlada do escopo de um projeto, sem aprovacao formal de mudanca, que pode comprometer prazo, custo e qualidade. |

---

## 12. Aprovacao

Este documento de Especificacao de Requisitos Funcionais foi elaborado pelo VMO Autonomo com base na documentacao de qualificacao e documentacao base de iniciacao do projeto PROJ-2026-003.

| Papel | Nome | Assinatura | Data |
|---|---|---|---|
| Engenheiro de Requisitos (VMO) | Rafael Requisito | _________________ | 05/04/2026 |
| GP Interno | Marcelo Silveira | _________________ | ____/____/2026 |
| Sponsor Executivo Principal | Decio Luiz Chieppe | _________________ | ____/____/2026 |

**Historico de Revisoes:**

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 05/04/2026 | Rafael Requisito (VMO Autonomo) | Versao inicial da ERF — 60 requisitos funcionais + 10 requisitos nao-funcionais |

---

*Documento elaborado por Rafael Requisito — Engenheiro de Requisitos, VMO Autonomo*
*Run ID: 2026-04-05-173000 | Etapa: 6/12 — Especificar Requisitos | ID Projeto: PROJ-2026-003*
