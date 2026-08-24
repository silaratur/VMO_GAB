# Demanda Coletada + Estruturada

**Projeto:** PROJ-2026-009
**Demanda:** DEM-2026-009
**Coletora:** Iara Inbound — Coletora de Demandas
**Data da Coleta:** 2026-08-24

---

## 1. Canal e Fontes

| Item | Detalhe |
|------|---------|
| Canal de entrada | Reuniao de Discovery via Fireflies (videoconferencia gravada) |
| Fonte primaria | Transcricao Fireflies — ID: `01M0TKBYCN3C53JWQZQ04Y71H1` |
| URL | https://app.fireflies.ai/view/01M0TKBYCN3C53JWQZQ04Y71H1 |
| Reuniao | "Discovery Demandas - Dario Demanda <> Jairo de Melo Ferreira Mendes" |
| Data da reuniao | 2026-08-24 |
| Duracao | ~11 minutos |
| Participantes | Jairo de Melo Ferreira Mendes (solicitante), Dario Demanda (agente VMO) |
| Fonte secundaria | Resumo e keywords gerados pelo Fireflies |

---

## 2. Dados Brutos Extraidos (com Rastreabilidade)

### 2.1 Identificacao do Chamado
| Dado | Valor | Fonte |
|------|-------|-------|
| Numero do chamado | 7122686 | Transcricao [00:56-01:03], reiterado em [01:25-01:27] |
| Tipo de solicitacao | Solicitacao de projetos | Transcricao [00:56-01:03] |

### 2.2 Descricao da Necessidade
| Dado | Valor | Fonte |
|------|-------|-------|
| Descricao geral | Integracao do SAP com o sistema GRLOG para cadastro automatico de centro de custo, centro de lucro e clientes | Transcricao [01:40-02:08] |
| Objetivo | Evitar cadastro manual, erros de cadastro e falta de cadastro; manter sistema atualizado com dados da receita | Transcricao [01:40-02:08] |
| Classificacao | Melhoria de processo ja existente | Transcricao [05:35-05:38] |

### 2.3 Situacao Atual (As-Is)
| Dado | Valor | Fonte |
|------|-------|-------|
| Processo atual | Abertura manual do SAP, visualizacao do cadastro novo, copia dos dados e colagem na tela de cadastro do GRLOG (mesmos campos) | Transcricao [02:25-02:44] |
| Quantidade de pessoas | 5 pessoas executando o processo | Transcricao [03:02-03:09] |
| Frequencia | Diariamente, sempre que nasce novo centro de custo, centro de lucro ou cliente | Transcricao [03:02-03:09] |

### 2.4 Impacto da Situacao Atual
| Dado | Valor | Fonte |
|------|-------|-------|
| Impacto de erro/falta de cadastro | Visualizacao incorreta dos dados de receita; a companhia enxerga dados incorretos | Transcricao [03:25-03:47] |
| Relacao entre sistemas | SAP e o mandante; GRLOG e o sistema que contem informacoes de receita | Transcricao [03:25-03:47] |
| Impacto no BI | BI do GRLOG mostra "nao informado" em vez do cliente ou centro de lucro correto, ao lado do valor da receita | Transcricao [04:11-04:31] |
| Visibilidade executiva | BI acompanhado pela CEO da companhia | Transcricao [04:11-04:31] |

> **CLAIM SEM EVIDENCIA:** Jairo menciona que "o BI e acompanhado pela CEO da companhia" [04:11-04:31]. Nao ha evidencia documental que comprove o envolvimento direto da CEO. Conforme regra do squad: "Nunca aceitar citacao de alta patente sem evidencia documental."

### 2.5 Resultado Esperado (To-Be)
| Dado | Valor | Fonte |
|------|-------|-------|
| Funcionamento esperado | Integracao diaria automatica cadastrando centros de lucro, centro de custo e clientes novos | Transcricao [04:59-05:16] |
| Beneficio 1 | Dados 100% cadastrados no sistema sem risco de erro manual — confiabilidade dos dados no BI | Transcricao [06:09-06:17], [06:41-06:46] |
| Beneficio 2 | Reducao do trabalho manual das 5 pessoas (reaproveitamento do tempo) | Transcricao [06:41-06:46] |
| Criterio de sucesso | Cadastro automatico no sistema ocorrendo diariamente, sem necessidade de cadastro manual | Transcricao [09:35-09:44] |

### 2.6 Stakeholders
| Dado | Valor | Fonte |
|------|-------|-------|
| Solicitante formal | Jairo de Melo Ferreira Mendes | Transcricao [07:39-07:49] |
| Aprovadora de custos | Ana Silvia Kallegard — Gerencia Executiva de Controladoria | Transcricao [07:39-07:49] |
| Areas impactadas | Gestao da Receita e toda a Diretoria | Transcricao [07:02-07:06] |
| Usuarios do GRLOG | Mais de 200 usuarios | Transcricao [07:17-07:20] |

### 2.7 Escopo Tecnico
| Dado | Valor | Fonte |
|------|-------|-------|
| Sistemas envolvidos | SAP e GRLOG (somente esses dois) | Transcricao [08:10-08:11] |
| Entidades a integrar | Centro de custo, centro de lucro, clientes | Transcricao [01:40-02:08] |
| Requisitos legais/regulatorios | Nenhum mencionado | Transcricao [08:29] |

### 2.8 Restricoes e Prazos
| Dado | Valor | Fonte |
|------|-------|-------|
| Prazo desejado | Outubro de 2026 | Transcricao [08:40-08:57] |
| Urgencia | "Quanto antes" — para ter dados confiaveis em outubro | Transcricao [08:40-08:57] |
| Orcamento | Nao definido — depende de estudo da DTI | Transcricao [09:14-09:20] |

---

## 3. Lacunas Identificadas

| # | Lacuna | Pergunta de Esclarecimento | Prioridade |
|---|--------|---------------------------|------------|
| L1 | Aprovacao formal de Diretoria ausente | Conforme regra do squad, e obrigatoria aprovacao formal em nivel de Diretoria. Ana Silvia Kallegard (Gerencia Executiva de Controladoria) foi citada como aprovadora de custos, mas nao ha aprovacao formal de Diretoria registrada. Quem da Diretoria aprova formalmente esta demanda? | BLOQUEANTE |
| L2 | Aprovacao do Gerente de TI ausente | Conforme regra do squad, e obrigatoria aprovacao do Gerente de TI. Nenhum Gerente de TI foi mencionado na reuniao. Quem e o Gerente de TI responsavel e qual e sua posicao sobre esta demanda? | BLOQUEANTE |
| L3 | Envolvimento da CEO sem evidencia | Jairo afirma que o BI e acompanhado pela CEO [04:11-04:31]. Nao ha evidencia documental. E possivel fornecer evidencia (e-mail, ata, comunicado) do acompanhamento da CEO? | ALTA |
| L4 | Detalhes tecnicos da integracao | Nao foram discutidos: metodo de integracao (API, RFC, arquivo flat, middleware), volumetria de registros, ambiente SAP (modulo, versao), arquitetura do GRLOG. Qual e a arquitetura tecnica prevista pela DTI? | MEDIA |
| L5 | Estudo de viabilidade da DTI | Mencionado que a DTI fara o estudo [09:14-09:20], mas nao ha prazo nem responsavel nomeado para este estudo. Quem na DTI e responsavel e qual o prazo para conclusao do estudo? | ALTA |
| L6 | Orcamento e fonte de recursos | Orcamento nao definido e dependente do estudo da DTI. Existe previsao orcamentaria ou centro de custo para absorver este investimento? | ALTA |
| L7 | Regras de negocio de mapeamento | Nao foram detalhadas as regras de correspondencia entre campos SAP e campos GRLOG. Existem campos com transformacao ou apenas copia direta? Ha campos obrigatorios no GRLOG que nao existem no SAP? | MEDIA |
| L8 | Tratamento de erros e excecoes | Nao foi discutido: o que acontece se a integracao falhar? Ha processo de rollback? Quem e notificado? | MEDIA |
| L9 | Cargo/area de Jairo | Jairo nao informou seu cargo nem sua area exata dentro da organizacao. Qual e o cargo e a area de Jairo de Melo Ferreira Mendes? | BAIXA |
| L10 | SLA e janela de execucao | "Diariamente" foi mencionado, mas nao foi definido horario, janela de execucao ou SLA de tempo maximo para a sincronizacao. Qual e a janela de execucao e o SLA esperado? | MEDIA |

---

# Demanda Estruturada — Integracao SAP-GRLOG para Cadastro Automatico

## Identificacao

| Campo | Valor |
|-------|-------|
| ID da Demanda | DEM-2026-009 |
| Projeto | PROJ-2026-009 |
| Nome Preliminar | Integracao SAP-GRLOG para Cadastro Automatico de Centros de Custo, Centros de Lucro e Clientes |
| Tipo | Melhoria de processo existente |
| Chamado de origem | 7122686 |
| Data de registro | 2026-08-24 |
| Status | Coletada — Pendente de aprovacoes obrigatorias |

## Solicitante

| Campo | Valor | Fonte |
|-------|-------|-------|
| Nome | Jairo de Melo Ferreira Mendes | Transcricao [titulo da reuniao], [07:39-07:49] |
| Cargo | Nao informado (Lacuna L9) | — |
| Area | Gestao da Receita (inferido de [07:02-07:06]) | Transcricao [07:02-07:06] |
| Aprovadora de custos | Ana Silvia Kallegard — Gerencia Executiva de Controladoria | Transcricao [07:39-07:49] |
| Aprovacao Diretoria | NAO OBTIDA (Lacuna L1) | — |
| Aprovacao Gerente TI | NAO OBTIDA (Lacuna L2) | — |

## Resumo Executivo

Integracao automatica entre SAP e GRLOG para sincronizacao diaria de cadastros de centros de custo, centros de lucro e clientes. Hoje 5 pessoas realizam esse cadastro manualmente, gerando erros, atrasos e dados exibidos como "nao informado" no BI de receita da companhia. O objetivo e eliminar o trabalho manual, garantir confiabilidade dos dados e liberar capacidade da equipe.

**Fonte:** Transcricao completa [01:40-02:08], [02:25-02:44], [03:02-03:09], [04:11-04:31], [04:59-05:16], [06:09-06:46].

## Necessidade de Negocio (o problema)

O processo atual de cadastro manual de dados do SAP no GRLOG apresenta:

1. **Erros de cadastro** — copia manual sujeita a falhas humanas [01:40-02:08]
2. **Atrasos na atualizacao** — cadastros pendentes ou desatualizados [04:11-04:31]
3. **Dados incorretos no BI** — campos exibidos como "nao informado" no BI de receita [04:11-04:31]
4. **Impacto na visibilidade executiva** — a companhia enxerga dados incorretos de receita [03:25-03:47]
5. **Custo operacional** — 5 pessoas dedicando tempo diario ao cadastro manual [03:02-03:09]

> **NOTA:** Jairo afirma que o BI e acompanhado pela CEO da companhia [04:11-04:31]. **CLAIM SEM EVIDENCIA DOCUMENTAL** — conforme regra do squad, esta citacao de alta patente nao pode ser validada sem evidencia.

## Pedido Especifico (a solucao solicitada)

Implementar integracao automatica entre SAP e GRLOG que:
- Sincronize diariamente os cadastros de centros de custo, centros de lucro e clientes [04:59-05:16]
- Elimine a necessidade de cadastro manual [06:09-06:17]
- Garanta dados 100% cadastrados e confiaveis no BI [06:09-06:17]

## Resultado Esperado

| Indicador | Descricao | Fonte |
|-----------|-----------|-------|
| Cadastro automatico | Sincronizacao diaria sem intervencao manual | [04:59-05:16], [09:35-09:44] |
| Zero "nao informado" | Eliminacao de registros sem identificacao no BI | [04:11-04:31], [06:09-06:17] |
| Confiabilidade | Dados de receita corretos e confiaveis | [06:41-06:46] |
| Produtividade | Liberacao de tempo das 5 pessoas para outras atividades | [06:41-06:46], [06:50-07:00] |

**Criterio de sucesso declarado pelo solicitante:** "Cadastro automatico no sistema ocorrendo diariamente, sem necessidade de cadastro manual." [09:35-09:44]

## Contexto Estrategico

| Campo | Valor | Fonte |
|-------|-------|-------|
| Alinhamento | Melhoria da confiabilidade dos dados de receita para tomada de decisao executiva | [03:25-03:47], [06:41-06:46] |
| Areas impactadas | Gestao da Receita, Diretoria | [07:02-07:06] |
| Usuarios impactados | Mais de 200 usuarios do GRLOG | [07:17-07:20] |
| Sistemas | SAP (mandante), GRLOG (receita) | [03:25-03:47], [08:10-08:11] |

## Estimativas Preliminares

| Campo | Valor | Fonte | Observacao |
|-------|-------|-------|------------|
| Prazo desejado | Outubro 2026 | [08:40-08:57] | Solicitante deseja "quanto antes" |
| Orcamento | Nao definido | [09:14-09:20] | Depende de estudo de viabilidade da DTI |
| Esforco | Nao estimado | — | Conforme regra do squad: esforco exige Rafael Requisitos |

## Premissas

1. O SAP e o sistema mandante e contem os dados-fonte corretos [03:25-03:47]
2. O GRLOG possui tela de cadastro com os mesmos campos do SAP [02:25-02:44]
3. Somente SAP e GRLOG estao envolvidos na integracao [08:10-08:11]
4. Nao ha requisitos legais ou regulatorios aplicaveis [08:29]
5. A DTI sera responsavel pelo estudo de viabilidade tecnica [09:14-09:20]

## Restricoes

1. Orcamento nao aprovado — dependente do estudo da DTI [09:14-09:20]
2. Prazo de outubro 2026 como expectativa do solicitante [08:40-08:57]
3. Aprovacoes obrigatorias de Diretoria e Gerente de TI ainda nao obtidas (BLOQUEANTE)

## Lacunas e Perguntas Pendentes

### Bloqueantes
- **L1:** Aprovacao formal de Diretoria — obrigatoria conforme regras do squad. Quem aprova?
- **L2:** Aprovacao do Gerente de TI — obrigatoria conforme regras do squad. Quem e o Gerente de TI responsavel?

### Alta Prioridade
- **L3:** Evidencia documental do acompanhamento da CEO (claim sem evidencia)
- **L5:** Responsavel e prazo do estudo de viabilidade da DTI
- **L6:** Previsao orcamentaria e centro de custo para investimento

### Media Prioridade
- **L4:** Detalhes tecnicos: metodo de integracao, volumetria, versao SAP, arquitetura GRLOG
- **L7:** Regras de mapeamento de campos entre SAP e GRLOG
- **L8:** Tratamento de erros, rollback e notificacoes
- **L10:** Janela de execucao e SLA da sincronizacao diaria

### Baixa Prioridade
- **L9:** Cargo e area exata de Jairo de Melo Ferreira Mendes

## Resumo para Confirmacao

> Jairo de Melo Ferreira Mendes solicita, por meio do chamado 7122686, a implementacao de uma integracao automatica entre SAP e GRLOG para sincronizacao diaria de cadastros de centros de custo, centros de lucro e clientes. Atualmente, 5 pessoas realizam esse cadastro manualmente todos os dias, o que gera erros, atrasos e exibicao de "nao informado" no BI de receita. O prazo desejado e outubro de 2026. O orcamento depende de estudo de viabilidade da DTI, e custos serao aprovados por Ana Silvia Kallegard (Gerencia Executiva de Controladoria). A demanda esta classificada como melhoria de processo existente. **Esta demanda NAO pode avancar para qualificacao sem: (1) aprovacao formal de Diretoria e (2) aprovacao do Gerente de TI, conforme regras obrigatorias do squad.**

---

*Documento gerado por Iara Inbound — Coletora de Demandas | VMO Autonomo Squad*
*Fonte: Transcricao Fireflies ID 01M0TKBYCN3C53JWQZQ04Y71H1 | 2026-08-24*
