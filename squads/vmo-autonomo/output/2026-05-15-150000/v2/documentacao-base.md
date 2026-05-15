# Documentação de Iniciação — PROJ-2026-005
**Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender**
Gerado por: Diana Documento | Data: 2026-05-15 | Versão: 1.0

---

# DOCUMENTO 1 — TAP: Termo de Abertura do Projeto

## 1. Identificação do Projeto

| Campo                     | Conteúdo                                                                     |
|---------------------------|------------------------------------------------------------------------------|
| **Código**                | PROJ-2026-005                                                                |
| **Demanda Origem**        | DEM-2026-002                                                                 |
| **Título**                | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender        |
| **Data de Abertura**      | 2026-05-15                                                                   |
| **Versão do TAP**         | 1.0                                                                          |
| **Elaborado por**         | Marcelo Silveira (GP VMO Autônomo)                                           |
| **Solicitante**           | Sandro Siqueira — Coordenador de Contabilidade, Divisão Comércio, Grupo Águia Branca |
| **Sponsor Executivo**     | **⚠ A IDENTIFICAR — CONDIÇÃO BLOQUEANTE CB-01 (prazo: 25/05/2026)**         |
| **Gestor do Projeto**     | A definir — VMO Autônomo                                                     |
| **Cliente / Área**        | Divisão Comércio — Grupo Águia Branca                                        |
| **Áreas Impactadas**      | Contabilidade, Financeiro, Jurídico                                          |

---

## ⛔ ALERTA: CONDIÇÕES BLOQUEANTES — APROVAÇÃO CONDICIONAL

> Este projeto foi aprovado com **SCORE 18/30 (60%)** — **APROVADO COM CONDIÇÕES**.
> A execução do projeto está **BLOQUEADA** até que as condições abaixo sejam cumpridas.
> O não cumprimento dentro dos prazos estabelecidos implicará em **suspensão automática da abertura formal**.

| Código | Condição Bloqueante                                                                                       | Responsável       | Prazo         | Status     |
|--------|-----------------------------------------------------------------------------------------------------------|-------------------|---------------|------------|
| **CB-01** | Sponsor executivo não identificado. Necessário indicar e confirmar patrocinador executivo do projeto. | Sandro Siqueira / Alta Gestão Div. Comércio | **25/05/2026** | 🔴 ABERTO |
| **CB-02** | Documentação contratual do acordo NBS (compromisso de desenvolvimento do Auditor Fiscal) não verificada. Necessário obter e validar cláusula contratual que formaliza a contrapartida. | Sandro Siqueira / Jurídico | **30/05/2026** | 🔴 ABERTO |

---

## 2. Objetivo SMART

> Substituir **100% das funcionalidades operacionais do Fiscal Defender** pelo módulo nativo **Auditor Fiscal NBS** no ambiente ERP da Divisão Comércio do Grupo Águia Branca, alcançando o **go-live até novembro de 2026** (prazo estimado: 6–8 meses a partir da abertura formal), confirmando a **eliminação do contrato Fiscal Defender** e gerando **saving recorrente de R$ 78.000/ano**, com custo de implementação residual máximo de **R$ 35.000**, garantindo que todas as equipes de Contabilidade, Financeiro e Jurídico operem sem alteração do fluxo de trabalho atual.

| Critério SMART | Conteúdo                                                                                                    |
|----------------|-------------------------------------------------------------------------------------------------------------|
| **Specific**   | Substituição do Fiscal Defender pelo módulo Auditor Fiscal nativo NBS; escopo: Divisão Comércio             |
| **Measurable** | 100% das funcionalidades do Fiscal Defender replicadas; saving de R$78K/ano confirmado; max R$35K residuais |
| **Achievable** | Desenvolvimento como contrapartida contratual NBS (custo zero); estrutura técnica ERP existente             |
| **Relevant**   | Alinhamento estratégico com consolidação da plataforma ERP corporativa e eficiência financeira               |
| **Time-bound** | Go-live: estimado entre setembro e novembro de 2026                                                         |

---

## 3. Justificativa do Projeto

### 3.1 Contexto e Motivação

A Divisão Comércio do Grupo Águia Branca utiliza o sistema **Fiscal Defender** para auditoria automatizada de Notas Fiscais Eletrônicas (NF-e), pagando **R$ 78.000 por ano** por esse serviço. O fornecedor do ERP corporativo, **NBS**, comprometeu-se contratualmente a desenvolver o módulo **Auditor Fiscal** como contrapartida — sem custo adicional de desenvolvimento.

A não aprovação e execução deste projeto representa:

- **Desperdício financeiro:** continuidade de gasto anual de R$ 78.000 em solução externa quando a funcionalidade equivalente estará disponível nativamente.
- **Risco de compliance:** dependência de dois sistemas distintos para auditoria fiscal, com potencial de divergência de dados e lacunas de rastreabilidade.
- **Oportunidade perdida:** o comprometimento contratual da NBS tem prazo e escopo definidos — atrasar o projeto pode comprometer os termos acordados.

### 3.2 ROI e Viabilidade Financeira

| Indicador                        | Valor                         |
|----------------------------------|-------------------------------|
| Custo anual atual (Fiscal Defender) | R$ 78.000/ano              |
| Custo de desenvolvimento         | R$ 0 (contrapartida NBS)     |
| Custo residual estimado          | ~R$ 35.000 (implementação, treinamento, rescisão) |
| **Orçamento total do projeto**   | **~R$ 35.000**               |
| Saving anual recorrente          | R$ 78.000/ano                |
| **Payback estimado**             | **~5,4 meses**               |
| ROI no 1º ano completo           | > 100%                       |

### 3.3 Alinhamento Estratégico

- Consolidação da plataforma ERP NBS como solução única de gestão corporativa.
- Redução de fornecedores e dependências externas.
- Eficiência operacional: integração nativa elimina exportações/importações manuais de dados entre sistemas.

---

## 4. Escopo do Projeto

### 4.1 Dentro do Escopo (IN SCOPE)

- Implantação do módulo Auditor Fiscal NBS na Divisão Comércio.
- Configuração e parametrização do módulo conforme regras fiscais da Divisão Comércio.
- Replicação de todas as funcionalidades operacionais do Fiscal Defender (RF-01 a RF-08).
- Testes de homologação e validação com equipes de Contabilidade, Financeiro e Jurídico.
- Treinamento das equipes usuárias.
- Encerramento formal do contrato Fiscal Defender.
- Gestão da transição (período de operação paralela se necessário).

### 4.2 Fora do Escopo (OUT OF SCOPE)

- Desenvolvimento de novas funcionalidades além das previstas nos RF-01 a RF-08 (salvo aprovação formal de mudança).
- Implantação em outras divisões do Grupo Águia Branca.
- Integração com Power BI (a ser avaliada como demanda futura — não confirmada para este projeto).
- Migração de dados históricos do Fiscal Defender (necessidade não avaliada — a ser definida na fase de planejamento detalhado).
- Alteração dos processos operacionais das equipes (RF-07: manutenção do fluxo atual).
- Customizações no núcleo do ERP NBS não relacionadas ao módulo Auditor Fiscal.

---

## 5. Estimativas de Custo e Prazo

### 5.1 Orçamento

| Categoria                                 | Estimativa         | Observação                                          |
|-------------------------------------------|--------------------|-----------------------------------------------------|
| Desenvolvimento do módulo (NBS)           | R$ 0               | Contrapartida contratual — **SUJEITO A CB-02**      |
| Implementação / configuração / parametrização | ~R$ 15.000     | Horas de consultoria NBS ou interna                 |
| Treinamento das equipes                   | ~R$ 8.000          | Estimativa preliminar                               |
| Rescisão contratual Fiscal Defender       | ~R$ 7.000          | Multas e aviso prévio (verificar contrato)          |
| Contingência (reserva gerencial ~15%)     | ~R$ 5.000          | Sobre custos residuais                              |
| **Total Estimado**                        | **~R$ 35.000**     | Revisão obrigatória após CB-02 resolvida            |

### 5.2 Cronograma Estimado

> Prazo estimado com base em projetos similares de implantação de módulo ERP. Cronograma detalhado a ser elaborado na fase de planejamento.

| Fase                                  | Duração Estimada | Período Provável         |
|---------------------------------------|------------------|--------------------------|
| Iniciação e resolução de condições bloqueantes | 3 semanas | mai/2026               |
| Planejamento detalhado                | 3 semanas        | jun/2026                 |
| Implantação e configuração (NBS)      | 8 semanas        | jul–ago/2026             |
| Testes e homologação                  | 4 semanas        | set/2026                 |
| Treinamento e transição               | 3 semanas        | out/2026                 |
| Go-live e encerramento Fiscal Defender| 2 semanas        | out–nov/2026             |
| **Go-live estimado**                  | —                | **Outubro/Novembro 2026**|
| **Duração total estimada**            | **~6–7 meses**   | mai–nov/2026             |

---

## 6. Premissas

| Código | Premissa                                                                                                        | Status           |
|--------|-----------------------------------------------------------------------------------------------------------------|------------------|
| **P-01** | O acordo contratual NBS para desenvolvimento do Auditor Fiscal está formalizado e vigente.                  | **⚠ A CONFIRMAR — CB-02** |
| P-02   | A NBS entregará o módulo Auditor Fiscal sem custo de desenvolvimento para a Divisão Comércio.                   | A confirmar (dep. P-01) |
| P-03   | Um sponsor executivo da Divisão Comércio será identificado e comprometido até 25/05/2026.                       | **⚠ A CONFIRMAR — CB-01** |
| P-04   | As equipes de Contabilidade, Financeiro e Jurídico disponibilizarão representantes para participação nos testes. | A confirmar       |
| P-05   | O módulo Auditor Fiscal NBS será compatível com a versão do ERP atualmente implantada na Divisão Comércio.      | A confirmar       |
| P-06   | O contrato com o Fiscal Defender permite rescisão dentro do prazo do projeto.                                   | A verificar       |
| P-07   | Não haverá necessidade de migração de dados históricos do Fiscal Defender (ou, se necessária, estará dentro do escopo acordado com NBS). | A avaliar |

---

## 7. Restrições

| Código | Restrição                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------|
| R-01   | O orçamento máximo de custos residuais é de **R$ 35.000**. Qualquer extrapolação requer aprovação do sponsor. |
| R-02   | O fluxo operacional das equipes não pode ser alterado (RF-07) — a solução deve se adaptar ao processo, não o contrário. |
| R-03   | O go-live deve ocorrer dentro do exercício fiscal de 2026 para viabilizar a não renovação do contrato Fiscal Defender. |
| R-04   | O desenvolvimento do módulo é de responsabilidade exclusiva da NBS — o projeto não pode custear desenvolvimento adicional. |
| R-05   | A rescisão do Fiscal Defender só pode ocorrer após validação completa do Auditor Fiscal em ambiente produtivo. |

---

## 8. Critérios de Sucesso

| # | Critério Mensurável                                                                                                  |
|---|----------------------------------------------------------------------------------------------------------------------|
| CS-01 | **100% dos requisitos funcionais** (RF-01 a RF-08) validados e aprovados pelas equipes de Contabilidade, Financeiro e Jurídico antes do go-live. |
| CS-02 | **Contrato Fiscal Defender encerrado** até o go-live, com **saving de R$ 78.000/ano** confirmado em relatório financeiro. |
| CS-03 | **Custo total do projeto ≤ R$ 35.000** (custos residuais), sem necessidade de aporte adicional. |
| CS-04 | **Zero incidentes críticos** de auditoria fiscal não detectados no primeiro trimestre pós go-live, em comparação com o período equivalente no Fiscal Defender. |
| CS-05 | **Satisfação dos usuários ≥ 80%** em pesquisa aplicada 30 dias após o go-live (usabilidade, confiabilidade, aderência ao processo). |

---

## 9. Partes Interessadas (Stakeholders)

| Papel                         | Nome / Área                              | Influência | Interesse | Observação                           |
|-------------------------------|------------------------------------------|------------|-----------|--------------------------------------|
| Solicitante / Patrocinador Solicitante | Sandro Siqueira — Coord. Contabilidade, Div. Comércio | Alta | Alto | Ponto focal da demanda |
| **Sponsor Executivo**         | **A IDENTIFICAR — CB-01**                | **Alta**   | **Alto**  | **⚠ Condição Bloqueante**           |
| Gestor do Projeto             | A designar — VMO Autônomo                | Alta       | Alto      | —                                    |
| Fornecedor (desenvolvimento)  | NBS — Fornecedor ERP                     | Alta       | Médio     | Responsável pelo desenvolvimento do módulo |
| Área de Contabilidade         | Divisão Comércio                         | Média      | Alto      | Usuária principal                    |
| Área Financeiro               | Divisão Comércio                         | Média      | Alto      | Usuária impactada                    |
| Área Jurídico                 | Divisão Comércio                         | Média      | Médio     | Usuária impactada                    |
| TI / Infraestrutura           | Grupo Águia Branca                       | Média      | Médio     | Suporte técnico e ambiente           |
| Aprovador VMO                 | Marcelo Silveira — GP VMO Autônomo       | Alta       | Alto      | Aprovação e acompanhamento do projeto |

---

## 10. Riscos Iniciais Identificados

| Código | Risco                                                                                 | Probabilidade | Impacto | Prioridade | Resposta Preliminar                                              |
|--------|---------------------------------------------------------------------------------------|---------------|---------|------------|------------------------------------------------------------------|
| **RSK-01** | **Sponsor executivo não identificado até 25/05/2026 (CB-01)**                   | Alta          | Alto    | **CRÍTICO** | Bloquear abertura formal; escalar para alta gestão da Div. Comércio |
| **RSK-02** | **Compromisso contratual NBS não verificado/inexistente (CB-02)**               | Média         | Alto    | **CRÍTICO** | Bloquear abertura formal; acionar Jurídico para verificação imediata |
| RSK-03 | NBS atrasar ou não entregar o módulo dentro do prazo acordado                         | Média         | Alto    | Alta       | Definir SLA contratual; acompanhamento mensal de progresso       |
| RSK-04 | Módulo Auditor Fiscal com funcionalidades incompletas em relação ao Fiscal Defender   | Média         | Médio   | Média      | Matriz de rastreabilidade de requisitos; testes comparativos     |
| RSK-05 | Custo de rescisão do Fiscal Defender superior ao estimado                             | Baixa         | Médio   | Baixa      | Revisão antecipada do contrato Fiscal Defender                   |
| RSK-06 | Necessidade de migração de dados históricos não prevista no escopo                    | Média         | Médio   | Média      | Levantar necessidade na fase de planejamento; negociar com NBS   |
| RSK-07 | Resistência das equipes à mudança de ferramenta                                       | Baixa         | Baixo   | Baixa      | Plano de comunicação e treinamento adequado                      |

---

## 11. Aprovação do TAP

| Papel                          | Nome                  | Assinatura / Validação | Data       |
|--------------------------------|-----------------------|------------------------|------------|
| Gestor do Projeto (VMO)        | Marcelo Silveira      | Aprovado               | 2026-05-15 |
| Solicitante                    | Sandro Siqueira       | ⏳ Pendente            | —          |
| **Sponsor Executivo**          | **A IDENTIFICAR**     | **⚠ BLOQUEADO — CB-01** | —         |

> **NOTA:** A abertura formal do projeto fica condicionada à resolução das condições CB-01 e CB-02 até os respectivos prazos. Em caso de não cumprimento, o projeto será suspenso para reavaliação.

---
---

# DOCUMENTO 2 — PM CANVAS

## PROJ-2026-005 | Auditor Fiscal — Módulo Nativo NBS

---

### BLOCO 1 — JUSTIFICATIVA

**Por que este projeto existe?**

A Divisão Comércio do Grupo Águia Branca desembolsa **R$ 78.000/ano** com o Fiscal Defender para auditoria de NF-e. O fornecedor NBS comprometeu-se contratualmente a entregar o módulo **Auditor Fiscal** nativo ao ERP como contrapartida, sem custo de desenvolvimento. Manter o contrato externo representa desperdício financeiro direto e fragmentação do ecossistema tecnológico.

**Drivers:**
- Saving financeiro imediato: R$ 78.000/ano (payback ~5,4 meses sobre R$ 35K residuais)
- Consolidação tecnológica: redução de fornecedores e integração nativa
- Compliance fiscal: eliminação de lacunas entre sistemas distintos

---

### BLOCO 2 — OBJETIVO SMART

Substituir **100% das funcionalidades operacionais do Fiscal Defender** pelo módulo nativo **Auditor Fiscal NBS** na Divisão Comércio do Grupo Águia Branca, com **go-live até novembro de 2026**, dentro do orçamento de **R$ 35.000** em custos residuais, confirmando o encerramento do contrato Fiscal Defender e o **saving recorrente de R$ 78.000/ano**.

---

### BLOCO 3 — BENEFÍCIOS

| Tipo        | Benefício                                                                 | Indicador                          |
|-------------|---------------------------------------------------------------------------|-------------------------------------|
| Financeiro  | Eliminar custo anual de R$ 78.000 com Fiscal Defender                     | Contrato Fiscal Defender encerrado  |
| Financeiro  | ROI > 100% no primeiro ano completo após go-live                          | Relatório financeiro pós-projeto    |
| Operacional | Integração nativa NF-e via ERP — sem exportações manuais entre sistemas   | Zero retrabalho de integração       |
| Operacional | Detecção de fraudes e pagamentos indevidos diretamente no ERP             | Alertas operacionais ativos         |
| Estratégico | Consolidação da plataforma ERP NBS como solução única                     | Redução de fornecedores externos    |
| Qualidade   | Usabilidade superior ao Fiscal Defender (RF-08)                           | Pesquisa de satisfação ≥ 80%        |

---

### BLOCO 4 — PRODUTO

**O que será entregue?**

Módulo **Auditor Fiscal** implantado, configurado e em produção no ERP NBS da Divisão Comércio, com as seguintes capacidades operacionais:

- Importação e processamento automático de NF-e a partir da base ERP
- Motor de auditoria automatizada de notas fiscais
- Alertas de fraude, risco de multa e pagamentos indevidos
- Relatórios operacionais e gerenciais de auditoria fiscal
- Interface compatível com o fluxo operacional atual das equipes
- Usabilidade igual ou superior ao Fiscal Defender

**Entregáveis do Projeto:**
1. Módulo Auditor Fiscal configurado e homologado
2. Documentação técnica e manual do usuário
3. Treinamento aplicado às equipes (Contabilidade, Financeiro, Jurídico)
4. Relatório de encerramento com confirmação do saving

---

### BLOCO 5 — REQUISITOS

| Código  | Requisito                                                                              | Área            |
|---------|----------------------------------------------------------------------------------------|-----------------|
| RF-01   | Importar e processar NF-e a partir da base de dados do ERP NBS                        | Contabilidade   |
| RF-02   | Realizar auditoria automatizada das notas fiscais                                      | Contabilidade   |
| RF-03   | Identificar e alertar sobre possíveis fraudes                                          | Contabilidade / Jurídico |
| RF-04   | Identificar e alertar sobre riscos de multa por inconsistências fiscais                | Contabilidade / Jurídico |
| RF-05   | Identificar e alertar sobre pagamentos indevidos                                       | Financeiro      |
| RF-06   | Gerar relatórios operacionais e gerenciais de auditoria fiscal                         | Contabilidade / Gerência |
| RF-07   | Manter o fluxo operacional atual das equipes (sem alteração de processo)               | Todas           |
| RF-08   | Oferecer funcionalidades de usabilidade superiores ao Fiscal Defender                  | Todas           |

**Requisitos pendentes de levantamento:**
- Necessidade de migração de dados históricos
- Integração com Power BI (possível, não confirmada)
- Requisitos específicos de Financeiro e Jurídico

---

### BLOCO 6 — STAKEHOLDERS

| Stakeholder                              | Papel                           | Nível de Engajamento Esperado |
|------------------------------------------|---------------------------------|-------------------------------|
| Sandro Siqueira (Coord. Contabilidade)   | Solicitante / Ponto Focal       | Alto — participação ativa      |
| **A IDENTIFICAR**                        | **Sponsor Executivo — CB-01**   | **⚠ BLOQUEANTE**              |
| NBS (Fornecedor ERP)                     | Executor do desenvolvimento     | Alto — entrega do módulo       |
| Equipe Contabilidade — Div. Comércio     | Usuária principal               | Alto — testes e homologação    |
| Equipe Financeiro — Div. Comércio        | Usuária impactada               | Médio — validação de RF-05/06  |
| Equipe Jurídico — Div. Comércio          | Usuária impactada               | Médio — validação de RF-03/04  |
| TI / Infraestrutura — Grupo Águia Branca | Suporte técnico                 | Médio — ambiente e acesso      |
| Marcelo Silveira (GP VMO)                | Gestor do Projeto               | Alto — aprovação e acompanhamento |

---

### BLOCO 7 — PREMISSAS

| Código | Premissa                                                                               | Status           |
|--------|----------------------------------------------------------------------------------------|------------------|
| **P-01** | Acordo contratual NBS para Auditor Fiscal está formalizado e vigente               | **⚠ A CONFIRMAR — CB-02** |
| **P-02** | Sponsor executivo da Divisão Comércio será identificado até 25/05/2026             | **⚠ A CONFIRMAR — CB-01** |
| P-03   | NBS desenvolve o módulo sem custo adicional para o cliente                             | Dep. de P-01     |
| P-04   | Equipes disponibilizarão representantes para testes e homologação                      | A confirmar      |
| P-05   | Módulo compatível com versão ERP atual da Divisão Comércio                             | A confirmar      |
| P-06   | Rescisão do Fiscal Defender viável dentro do prazo do projeto                          | A verificar      |

---

### BLOCO 8 — RESTRIÇÕES

| Código | Restrição                                                                              |
|--------|----------------------------------------------------------------------------------------|
| R-01   | Orçamento máximo de custos residuais: **R$ 35.000**                                   |
| R-02   | Fluxo operacional das equipes não pode ser alterado (RF-07)                            |
| R-03   | Go-live dentro do exercício fiscal de 2026                                             |
| R-04   | Desenvolvimento do módulo é responsabilidade exclusiva da NBS                          |
| R-05   | Rescisão do Fiscal Defender somente após validação completa em produção                |

---

### BLOCO 9 — RISCOS

> ⛔ **ATENÇÃO: Dois riscos críticos (condições bloqueantes) impedem a abertura formal do projeto.**

| Código | Risco                                                      | Prob. | Impacto | Prioridade | Ação                                              |
|--------|------------------------------------------------------------|-------|---------|------------|---------------------------------------------------|
| **RSK-01** | **Sponsor executivo não identificado — CB-01**         | Alta  | Alto    | **CRÍTICO** | Escalar imediatamente; prazo: 25/05/2026         |
| **RSK-02** | **Compromisso NBS não verificado/inexistente — CB-02** | Média | Alto    | **CRÍTICO** | Acionar Jurídico; prazo: 30/05/2026              |
| RSK-03 | NBS atrasar entrega do módulo                              | Média | Alto    | Alta       | SLA contratual; acompanhamento mensal            |
| RSK-04 | Funcionalidades do módulo incompletas vs. Fiscal Defender  | Média | Médio   | Média      | Matriz de rastreabilidade; testes comparativos   |
| RSK-05 | Necessidade de migração de dados históricos não prevista   | Média | Médio   | Média      | Levantamento na fase de planejamento             |
| RSK-06 | Custo rescisão Fiscal Defender superior ao estimado        | Baixa | Médio   | Baixa      | Revisar contrato Fiscal Defender antecipadamente |

---
---

# DOCUMENTO 3 — PLANO GERAL DO PROJETO

## PROJ-2026-005 | Auditor Fiscal — Módulo Nativo NBS

**Versão:** 1.0 | **Data:** 2026-05-15 | **Status:** Rascunho — sujeito a revisão após resolução das condições bloqueantes CB-01 e CB-02

> ⚠ **NOTA IMPORTANTE:** Este Plano Geral é preliminar. O detalhamento de cada plano subsidiário deve ser desenvolvido após a abertura formal do projeto, condicionada à resolução de CB-01 (sponsor executivo) e CB-02 (verificação contratual NBS).

---

### 1. Plano de Gerenciamento do Escopo

**Objetivo:** Definir, documentar e controlar o que está dentro e fora do escopo do projeto, prevenindo scope creep.

**Abordagem:**
- O escopo foi definido inicialmente no TAP (seção 4) e será detalhado na fase de planejamento.
- A EAP (Estrutura Analítica do Projeto) será elaborada com base nos 8 requisitos funcionais (RF-01 a RF-08) e nos entregáveis identificados.
- Qualquer alteração de escopo seguirá o processo formal do Plano de Gerenciamento de Mudanças.

**Itens pendentes de levantamento (fora do escopo atual, a avaliar):**
- Migração de dados históricos do Fiscal Defender
- Integração com Power BI
- Impactos detalhados em Financeiro e Jurídico

**Ferramentas:** EAP, Dicionário da EAP, Matriz de Rastreabilidade de Requisitos.

**Processo de controle:**
- Reunião de revisão de escopo a cada fase do projeto
- Solicitações de mudança de escopo submetidas ao Comitê de Mudanças (sponsor + GP)

---

### 2. Plano de Gerenciamento do Cronograma

**Objetivo:** Planejar, sequenciar e controlar as atividades para garantir o go-live dentro do prazo estimado.

**Cronograma macro:**

| Fase                                       | Início Previsto  | Término Previsto | Duração    |
|--------------------------------------------|------------------|------------------|------------|
| Fase 0 — Resolução de condições bloqueantes | 2026-05-15       | 2026-05-30       | ~2 semanas |
| Fase 1 — Iniciação formal                  | 2026-06-02       | 2026-06-13       | ~2 semanas |
| Fase 2 — Planejamento detalhado            | 2026-06-16       | 2026-07-04       | ~3 semanas |
| Fase 3 — Implantação e configuração (NBS)  | 2026-07-07       | 2026-08-29       | ~8 semanas |
| Fase 4 — Testes e homologação              | 2026-09-01       | 2026-09-26       | ~4 semanas |
| Fase 5 — Treinamento e transição           | 2026-09-29       | 2026-10-17       | ~3 semanas |
| Fase 6 — Go-live e encerramento            | 2026-10-20       | 2026-11-07       | ~2,5 semanas |
| **Go-live estimado**                       | **out/nov 2026** | —                | —          |

**Marcos críticos (milestones):**

| Marco | Descrição                                         | Data Prevista  |
|-------|---------------------------------------------------|----------------|
| M-01  | ⚠ CB-01 resolvido (sponsor identificado)          | 25/05/2026     |
| M-02  | ⚠ CB-02 resolvido (contrato NBS verificado)       | 30/05/2026     |
| M-03  | TAP assinado — abertura formal do projeto         | jun/2026       |
| M-04  | Planejamento detalhado aprovado                   | jul/2026       |
| M-05  | Módulo entregue pela NBS (ambiente de testes)     | ago/2026       |
| M-06  | Homologação concluída e aprovada                  | set/2026       |
| M-07  | Treinamento concluído                             | out/2026       |
| **M-08** | **Go-live em produção**                        | **out/nov 2026** |
| M-09  | Encerramento do contrato Fiscal Defender          | nov/2026       |

**Controle:** Relatório de progresso quinzenal; reunião de acompanhamento mensal com sponsor.

---

### 3. Plano de Gerenciamento de Custos

**Objetivo:** Estimar, orçar e controlar os custos residuais do projeto dentro do limite de R$ 35.000.

**Orçamento detalhado:**

| Categoria                              | Estimativa Inicial | Reserva Gerencial (~15%) | Total         |
|----------------------------------------|--------------------|--------------------------|---------------|
| Desenvolvimento NBS                    | R$ 0               | —                        | R$ 0          |
| Implementação e parametrização         | R$ 15.000          | R$ 2.250                 | R$ 17.250     |
| Treinamento das equipes                | R$ 8.000           | R$ 1.200                 | R$ 9.200      |
| Rescisão contratual Fiscal Defender    | R$ 7.000           | R$ 1.050                 | R$ 8.050      |
| Gestão de projeto (VMO)                | R$ 0               | —                        | R$ 0          |
| **Total**                              | **R$ 30.000**      | **R$ 4.500**             | **~R$ 35.000** |

> Nota: Os valores de implementação, treinamento e rescisão são estimativas preliminares a serem refinadas na fase de planejamento, após verificação do contrato Fiscal Defender (CB-02) e definição do modelo de implantação com a NBS.

**Controle:** Relatório de custos mensais; alerta ao sponsor quando 80% do orçamento for comprometido; qualquer extrapolação requer aprovação formal.

---

### 4. Plano de Gerenciamento da Qualidade

**Objetivo:** Garantir que o módulo Auditor Fiscal atenda a todos os requisitos funcionais e de usabilidade antes do go-live.

**Padrões de qualidade:**
- 100% dos RF-01 a RF-08 testados e aprovados pelas áreas usuárias.
- Zero regressão nas funcionalidades do Fiscal Defender (auditoria comparativa).
- Satisfação dos usuários ≥ 80% em pesquisa 30 dias pós go-live.
- Zero incidentes críticos de auditoria fiscal não detectados no primeiro trimestre pós go-live.

**Atividades de qualidade:**

| Atividade                              | Responsável                     | Quando               |
|----------------------------------------|---------------------------------|----------------------|
| Revisão da matriz de requisitos        | GP + Sandro Siqueira            | Fase de planejamento |
| Plano de testes de homologação         | GP + NBS + Equipe Contabilidade | Fase 3               |
| Testes de aceitação do usuário (UAT)   | Equipes de Contabilidade, Financeiro, Jurídico | Fase 4 |
| Auditoria comparativa Fiscal Defender x Auditor Fiscal | Contabilidade | Fase 4 |
| Pesquisa de satisfação pós go-live     | GP VMO                          | 30 dias pós go-live  |

---

### 5. Plano de Gerenciamento de Recursos

**Objetivo:** Identificar, alocar e gerenciar os recursos humanos e materiais necessários ao projeto.

**Equipe do projeto:**

| Papel                                 | Recurso                         | Dedicação Estimada         |
|---------------------------------------|---------------------------------|----------------------------|
| Gestor do Projeto                     | VMO Autônomo (a designar)       | Parcial (~20% do tempo)    |
| Ponto Focal do Cliente                | Sandro Siqueira                 | Parcial (~10% do tempo)    |
| **Sponsor Executivo**                 | **A IDENTIFICAR — CB-01**       | **⚠ Pendente**            |
| Consultor Técnico NBS                 | Equipe NBS (fornecedor)         | A definir com NBS          |
| Representante Contabilidade           | A indicar por Sandro Siqueira   | Parcial — fases 4 e 5      |
| Representante Financeiro              | A indicar                       | Parcial — fase 4           |
| Representante Jurídico                | A indicar                       | Parcial — fase 4           |
| TI / Infraestrutura                   | Equipe TI Grupo Águia Branca    | Pontual                    |

**Recursos materiais:** Ambiente ERP NBS (desenvolvimento, homologação, produção) — provido pela infraestrutura existente.

---

### 6. Plano de Gerenciamento das Comunicações

**Objetivo:** Garantir que as informações certas cheguem às pessoas certas no momento adequado.

**Matriz de comunicações:**

| Comunicação                              | Conteúdo                                    | Frequência     | Formato           | Responsável     | Destinatários                          |
|------------------------------------------|---------------------------------------------|----------------|-------------------|-----------------|----------------------------------------|
| Relatório de status do projeto           | Progresso, custos, riscos, próximos passos  | Quinzenal      | E-mail / PDF      | GP VMO          | Sponsor, Sandro Siqueira               |
| Reunião de acompanhamento                | Status, decisões, impedimentos              | Mensal         | Videoconferência  | GP VMO          | Sponsor, Sandro Siqueira, NBS          |
| Ata de reunião                           | Decisões e ações acordadas                  | Por reunião    | Documento         | GP VMO          | Todos participantes                    |
| Alerta de risco / impedimento            | Riscos críticos ou bloqueios identificados  | Sob demanda    | E-mail urgente    | GP VMO          | Sponsor, Sandro Siqueira               |
| Comunicado de go-live                    | Confirmação da entrada em produção          | Único          | E-mail / Comunicado Interno | GP VMO | Toda a Divisão Comércio             |
| Pesquisa de satisfação pós go-live       | Avaliação das equipes usuárias              | Único (30 dias pós) | Formulário   | GP VMO          | Contabilidade, Financeiro, Jurídico    |

**Canal principal:** E-mail corporativo + ferramenta de gestão de projetos VMO.

---

### 7. Plano de Gerenciamento de Riscos

**Objetivo:** Identificar, analisar, priorizar e responder aos riscos do projeto de forma proativa.

**Metodologia:** Análise qualitativa de riscos (probabilidade × impacto) com revisão mensal.

**Registro de riscos:**

| Código | Risco                                               | Prob. | Impacto | Prioridade  | Estratégia  | Ação de Resposta                                             | Dono          |
|--------|-----------------------------------------------------|-------|---------|-------------|-------------|--------------------------------------------------------------|---------------|
| **RSK-01** | **Sponsor não identificado (CB-01)**            | Alta  | Alto    | **CRÍTICO** | Escalar     | Acionar alta gestão Div. Comércio; bloquear abertura formal  | Sandro Siqueira |
| **RSK-02** | **Compromisso NBS não verificado (CB-02)**      | Média | Alto    | **CRÍTICO** | Verificar   | Acionar Jurídico; obter cópia da cláusula contratual         | Jurídico / Sandro |
| RSK-03 | Atraso na entrega do módulo pela NBS                | Média | Alto    | Alta        | Mitigar     | Definir SLA; cláusula de penalidade no contrato              | GP VMO / Jurídico |
| RSK-04 | Módulo com funcionalidades incompletas              | Média | Médio   | Média       | Mitigar     | Matriz de rastreabilidade de requisitos; testes comparativos | GP VMO        |
| RSK-05 | Migração de dados históricos necessária (não prevista) | Média | Médio | Média    | Aceitar/Mitigar | Levantar necessidade no planejamento; negociar com NBS  | GP VMO        |
| RSK-06 | Custo de rescisão Fiscal Defender > estimado        | Baixa | Médio   | Baixa       | Mitigar     | Revisar contrato Fiscal Defender na fase de planejamento     | Sandro Siqueira |
| RSK-07 | Resistência das equipes à nova ferramenta           | Baixa | Baixo   | Baixa       | Mitigar     | Plano de comunicação e treinamento                           | GP VMO        |

**Frequência de revisão:** Mensal (reunião de acompanhamento) e sob demanda para riscos críticos.

---

### 8. Plano de Gerenciamento de Aquisições

**Objetivo:** Gerenciar a relação com fornecedores e aquisições necessárias ao projeto.

**Fornecedores identificados:**

| Fornecedor         | Objeto                                          | Tipo de Contrato       | Status                          |
|--------------------|-------------------------------------------------|------------------------|---------------------------------|
| **NBS**            | Desenvolvimento do módulo Auditor Fiscal        | Contrapartida contratual vigente | **⚠ A VERIFICAR — CB-02** |
| Fiscal Defender    | Contrato atual a ser rescindido                 | Rescisão               | Verificar cláusulas e multas    |
| NBS (serviços)     | Implementação, parametrização e treinamento     | Ordem de Serviço / SOW | A negociar na fase de planejamento |

**Ações prioritárias de aquisição:**
1. **CB-02:** Verificar e formalizar o compromisso NBS em relação ao Auditor Fiscal.
2. Revisar contrato Fiscal Defender para entender condições e custos de rescisão.
3. Elaborar Declaração de Trabalho (SOW) para os serviços de implementação e treinamento NBS.
4. Formalizar Ordem de Serviço com NBS para as fases de implantação.

**Critérios de encerramento de aquisições:**
- Módulo entregue, homologado e em produção.
- Contrato Fiscal Defender encerrado sem pendências.

---

### 9. Plano de Gerenciamento das Partes Interessadas

**Objetivo:** Engajar as partes interessadas de forma adequada ao longo do projeto, garantindo suporte e reduzindo resistências.

**Análise de engajamento:**

| Stakeholder                     | Engajamento Atual | Engajamento Desejado | Estratégia de Engajamento                                        |
|---------------------------------|-------------------|----------------------|------------------------------------------------------------------|
| Sandro Siqueira                 | Engajado          | Engajado             | Manter comunicação frequente; incluir nas decisões chave         |
| **Sponsor Executivo (CB-01)**   | **Desconhecido**  | **Liderando**        | **Identificar e engajar como prioridade máxima**                |
| NBS                             | Comprometido      | Comprometido         | Formalizar compromissos via contrato; reuniões mensais           |
| Equipe Contabilidade            | Neutro            | Apoiador             | Envolver cedo nos requisitos; comunicar benefícios da mudança    |
| Equipe Financeiro               | Neutro            | Apoiador             | Mapear impactos específicos; incluir nos testes de RF-05        |
| Equipe Jurídico                 | Neutro            | Apoiador             | Mapear impactos em RF-03/04; incluir nos testes                 |
| TI / Infraestrutura             | Neutro            | Apoiador             | Envolver desde o início para ambiente e integrações              |

**Ações prioritárias:**
1. Identificar e engajar o Sponsor Executivo até 25/05/2026 (CB-01).
2. Realizar reunião de kick-off com todas as áreas após abertura formal.
3. Comunicar claramente os benefícios e o impacto mínimo no fluxo operacional (RF-07).

---

### 10. Plano de Gerenciamento de Mudanças

**Objetivo:** Controlar formalmente qualquer alteração no escopo, prazo, custo ou qualidade do projeto.

**Processo de Controle de Mudanças:**

```
Solicitação de Mudança
        │
        ▼
Registro formal pelo GP VMO (Formulário de Mudança)
        │
        ▼
Análise de impacto (escopo / prazo / custo / qualidade)
        │
        ▼
┌───────────────────────────────────────┐
│  Impacto Baixo (≤ 5% orçamento,       │──► Aprovação pelo GP VMO
│  ≤ 1 semana prazo, sem mudança        │
│  de escopo)                           │
└───────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│  Impacto Médio/Alto (> 5% orçamento, │──► Aprovação pelo Sponsor + GP VMO
│  > 1 semana prazo, ou mudança de     │
│  escopo)                             │
└───────────────────────────────────────┘
        │
        ▼
Atualização do TAP / Plano / Cronograma
        │
        ▼
Comunicação às partes interessadas
```

**Categorias de mudança e alçadas:**

| Categoria        | Critério                                              | Alçada de Aprovação         |
|------------------|-------------------------------------------------------|-----------------------------|
| Baixo impacto    | Até 5% do orçamento ou 1 semana no prazo              | Gestor do Projeto (VMO)     |
| Médio impacto    | 5–15% do orçamento ou 2–4 semanas no prazo            | Sponsor + GP VMO            |
| Alto impacto     | > 15% do orçamento ou > 1 mês no prazo ou mudança de escopo significativa | Sponsor + GP VMO + Comitê |

**Registro:** Todas as mudanças aprovadas ou rejeitadas serão registradas no Log de Mudanças do projeto.

**Mudanças proibidas sem aprovação formal do sponsor:**
- Inclusão de novas áreas além da Divisão Comércio.
- Qualquer alteração que comprometa o go-live em 2026.
- Custos que ultrapassem o orçamento aprovado de R$ 35.000.

---

## Aprovação do Plano Geral

| Papel                          | Nome                  | Status             | Data       |
|--------------------------------|-----------------------|--------------------|------------|
| Gestor do Projeto (VMO)        | Marcelo Silveira      | Aprovado           | 2026-05-15 |
| Solicitante                    | Sandro Siqueira       | ⏳ Pendente         | —          |
| **Sponsor Executivo**          | **A IDENTIFICAR**     | **⚠ BLOQUEADO — CB-01** | —    |

---

*Documento gerado por Diana Documento — VMO Autônomo | PROJ-2026-005 | v1.0 | 2026-05-15*
*Próxima revisão: após resolução das condições bloqueantes CB-01 (25/05/2026) e CB-02 (30/05/2026)*
