# Especificação de Requisitos Funcionais (ERF)
## PROJ-2026-005 — Auditor Fiscal: Módulo Nativo NBS

---

| Campo           | Valor                                                        |
|-----------------|--------------------------------------------------------------|
| **Projeto**     | PROJ-2026-005                                                |
| **Demanda**     | DEM-2026-002                                                 |
| **Título**      | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Solicitante** | Sandro Siqueira — Coordenador de Contabilidade, Divisão Comércio, Grupo Águia Branca |
| **Versão**      | 3.0                                                          |
| **Data**        | 2026-05-15                                                   |
| **Autor**       | Rafael Requisito — Engenheiro de Requisitos, VMO Autônomo    |
| **Status**      | Em revisão pelo solicitante                                  |

---

## Histórico de Revisões

| Versão | Data       | Autor            | Descrição                                          |
|--------|------------|------------------|----------------------------------------------------|
| 1.0    | 2026-05-15 | Rafael Requisito | Rascunho inicial a partir dos requisitos Iara      |
| 2.0    | 2026-05-15 | Rafael Requisito | Expansão de RFs e adição de RNFs                   |
| 3.0    | 2026-05-15 | Rafael Requisito | Inclusão de matriz de rastreabilidade e pendências |

---

## Sumário

1. [Introdução](#1-introdução)
2. [Glossário do Domínio](#2-glossário-do-domínio)
3. [Atores e Perfis de Usuário](#3-atores-e-perfis-de-usuário)
4. [Requisitos Funcionais](#4-requisitos-funcionais)
5. [Requisitos Não-Funcionais](#5-requisitos-não-funcionais)
6. [Matriz de Rastreabilidade](#6-matriz-de-rastreabilidade)
7. [Restrições Técnicas](#7-restrições-técnicas)
8. [Premissas da Especificação](#8-premissas-da-especificação)
9. [Itens Fora do Escopo](#9-itens-fora-do-escopo)
10. [Pendências e Requisitos a Confirmar](#10-pendências-e-requisitos-a-confirmar)

---

## 1. Introdução

### 1.1 Objetivo do Documento

Esta Especificação de Requisitos Funcionais (ERF) define, de forma verificável e não ambígua, os requisitos do módulo **Auditor Fiscal** a ser desenvolvido pela NBS como componente nativo do ERP corporativo do Grupo Águia Branca (Divisão Comércio). O documento serve como contrato técnico entre o Grupo Águia Branca e a NBS para orientar o desenvolvimento, os testes de aceitação e a homologação do módulo.

### 1.2 Escopo da Solução

O módulo Auditor Fiscal substituirá integralmente o produto Fiscal Defender no processo de auditoria de Notas Fiscais Eletrônicas (NF-e) da Divisão Comércio. A solução operará de forma nativa sobre a base de dados do ERP NBS, eliminando a integração externa atualmente necessária para exportar dados ao Fiscal Defender.

O escopo inclui:
- Ingestão e processamento de NF-e já presentes na base NBS
- Auditoria automatizada de conformidade fiscal e tributária
- Detecção de inconsistências, fraudes e pagamentos indevidos
- Emissão de alertas de risco de multa e irregularidades
- Geração de relatórios operacionais e gerenciais acessíveis no ERP e, potencialmente, via Power BI

O escopo **não** inclui emissão de NF-e, escrituração fiscal (SPED), transmissão para SEFAZ, nem auditoria de outras divisões do Grupo Águia Branca além da Divisão Comércio nesta fase.

### 1.3 Público-Alvo da ERF

| Público                        | Finalidade de uso do documento                                    |
|--------------------------------|-------------------------------------------------------------------|
| Sandro Siqueira (Contabilidade)| Validar completude dos requisitos operacionais                    |
| Equipe NBS (desenvolvimento)   | Guia de implementação e base para testes de aceitação             |
| VMO Autônomo                   | Gestão do projeto e acompanhamento de entregas                    |
| Financeiro — Divisão Comércio  | Confirmar requisitos de relatórios e alertas financeiros          |
| Jurídico — Divisão Comércio    | Confirmar requisitos de conformidade e evidências para litígios   |
| TI — Grupo Águia Branca        | Planejar infraestrutura, permissões e integração Power BI         |

---

## 2. Glossário do Domínio

| Termo                  | Definição                                                                                                                                             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NF-e**               | Nota Fiscal Eletrônica. Documento fiscal digital, de existência apenas virtual, que documenta operações de circulação de mercadorias e prestação de serviços. |
| **DANFE**              | Documento Auxiliar da NF-e. Representação gráfica simplificada da NF-e, impresso para acompanhar a mercadoria em trânsito.                            |
| **Chave de Acesso**    | Código numérico de 44 dígitos que identifica univocamente uma NF-e perante a SEFAZ.                                                                   |
| **SEFAZ**              | Secretaria de Estado de Fazenda. Órgão estadual responsável pela autorização, validação e guarda das NF-e no ambiente nacional (SEFAZ Nacional / AN). |
| **XML da NF-e**        | Arquivo em formato XML que contém todos os dados estruturados de uma NF-e, assinado digitalmente pelo emitente e autorizado pela SEFAZ.               |
| **Auditoria Fiscal**   | Processo de verificação da conformidade de documentos fiscais com as legislações tributárias federal, estadual e municipal aplicáveis.                 |
| **Fiscal Defender**    | Produto de terceiro (substituído por este módulo) que realizava auditoria de NF-e recebendo dados via integração com o ERP NBS.                       |
| **Auditor Fiscal**     | Nome do módulo nativo NBS objeto desta especificação.                                                                                                 |
| **NBS**                | Fornecedor do ERP corporativo do Grupo Águia Branca; responsável pelo desenvolvimento do módulo Auditor Fiscal.                                       |
| **ERP**                | Enterprise Resource Planning. Sistema integrado de gestão empresarial. Neste contexto, o sistema fornecido pela NBS ao Grupo Águia Branca.             |
| **ICMS**               | Imposto sobre Circulação de Mercadorias e Serviços. Imposto estadual incidente sobre operações fiscais auditadas pelo módulo.                         |
| **PIS/COFINS**         | Contribuições federais (PIS = Programa de Integração Social; COFINS = Contribuição para o Financiamento da Seguridade Social) incidentes sobre receitas. |
| **IPI**                | Imposto sobre Produtos Industrializados. Imposto federal que pode constar em NF-e de produtos industrializados.                                       |
| **Crédito Tributário** | Direito do contribuinte de abater, do imposto a recolher, valores de imposto pago em etapas anteriores da cadeia produtiva.                           |
| **CST / CSOSN**        | Código de Situação Tributária / Código de Situação da Operação no Simples Nacional. Codificam o tratamento tributário de cada item da NF-e.           |
| **CFOP**               | Código Fiscal de Operações e Prestações. Código que identifica a natureza de circulação de mercadoria ou a prestação de serviço.                      |
| **NCM**                | Nomenclatura Comum do Mercosul. Código de oito dígitos que classifica mercadorias para fins tributários.                                              |
| **Duplicata / Fatura** | Título de crédito que documenta a obrigação de pagamento decorrente da operação comercial registrada na NF-e.                                         |
| **Pagamento Indevido** | Pagamento realizado em decorrência de NF-e com irregularidade (duplicidade, valor incorreto, NF-e cancelada, etc.).                                   |
| **MoSCoW**             | Método de priorização de requisitos: Must Have (obrigatório), Should Have (importante), Could Have (desejável), Won't Have (fora desta versão).       |
| **Power BI**           | Ferramenta de Business Intelligence da Microsoft, potencialmente usada para consumo externo dos dados de relatórios do módulo.                        |
| **LGPD**               | Lei Geral de Proteção de Dados Pessoais (Lei 13.709/2018). Aplicável ao tratamento de dados de pessoas físicas eventualmente presentes em NF-e.       |

---

## 3. Atores e Perfis de Usuário

### 3.1 Perfil: Analista de Contabilidade

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Contabilidade — Divisão Comércio, Grupo Águia Branca                                          |
| **Frequência de uso** | Diária — múltiplas sessões por dia                                                            |
| **Volume esperado**   | A confirmar com Sandro Siqueira (ver Seção 10, PEN-001)                                       |
| **Principais tarefas**| Revisar fila de NF-e auditadas; investigar alertas; tratar divergências; aprovar/rejeitar NF-e; consultar histórico de auditoria |
| **Nível técnico**     | Usuário funcional de ERP; familiaridade com legislação tributária                             |
| **Responsabilidade**  | Tomada de decisão operacional sobre conformidade de NF-e                                      |

### 3.2 Perfil: Supervisor de Contabilidade

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Contabilidade — Divisão Comércio, Grupo Águia Branca                                          |
| **Frequência de uso** | Diária — principalmente para acompanhamento gerencial                                        |
| **Principais tarefas**| Monitorar dashboard de conformidade; acompanhar KPIs de auditoria; escalar irregularidades; aprovar relatórios periódicos |
| **Nível técnico**     | Usuário gerencial de ERP; alto conhecimento de legislação tributária                          |
| **Responsabilidade**  | Supervisão da equipe de contabilidade e resposta a fiscalizações externas                     |

### 3.3 Perfil: Analista Financeiro

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Financeiro — Divisão Comércio, Grupo Águia Branca                                            |
| **Frequência de uso** | Semanal a mensal (relatórios e alertas pontuais)                                              |
| **Principais tarefas**| Consultar alertas de pagamentos indevidos; acessar relatórios de NF-e bloqueadas; solicitar estorno de pagamentos irregulares |
| **Nível técnico**     | Usuário funcional de ERP; sem necessidade de conhecimento tributário aprofundado              |
| **Responsabilidade**  | Prevenção e recuperação de pagamentos indevidos                                               |
| **Observação**        | Requisitos detalhados a confirmar (ver Seção 10, PEN-003)                                     |

### 3.4 Perfil: Analista Jurídico

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Jurídico — Divisão Comércio, Grupo Águia Branca                                              |
| **Frequência de uso** | Sob demanda (em processos, auditorias externas, consultas de conformidade)                    |
| **Principais tarefas**| Consultar histórico de NF-e; extrair evidências documentais; acessar relatórios de risco e conformidade |
| **Nível técnico**     | Usuário eventual de ERP; demanda relatórios exportáveis em formatos usáveis em peças jurídicas|
| **Responsabilidade**  | Suporte a litígios fiscais, defesas administrativas e auditoria de conformidade regulatória   |
| **Observação**        | Requisitos detalhados a confirmar (ver Seção 10, PEN-004)                                     |

### 3.5 Perfil: Administrador do Sistema (TI / NBS)

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | TI — Grupo Águia Branca / Equipe NBS                                                         |
| **Frequência de uso** | Eventual (configurações, manutenção, criação de usuários)                                     |
| **Principais tarefas**| Gerenciar perfis e permissões; configurar parâmetros tributários; monitorar logs de sistema; executar atualizações de tabelas fiscais |
| **Nível técnico**     | Administrador de ERP; não necessariamente especialista fiscal                                 |
| **Responsabilidade**  | Disponibilidade e integridade operacional do módulo                                           |

---

## 4. Requisitos Funcionais

Os requisitos funcionais estão organizados em seis módulos funcionais. Cada RF segue o padrão: ID único, descrição na voz "O sistema deve...", prioridade MoSCoW, critério de aceitação verificável e rastreabilidade à origem.

**Legenda de Prioridade:**
- **M** = Must Have (obrigatório para entrar em produção)
- **S** = Should Have (importante; deve ser incluído se possível)
- **C** = Could Have (desejável; incluído se houver capacidade)
- **W** = Won't Have (esta versão; registrado para futuras versões)

---

### M1 — Módulo de Ingestão de NF-e

---

**RF-001 — Acesso nativo às NF-e da base NBS**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve acessar, ler e processar NF-e já registradas na base de dados do ERP NBS sem exportação de dados para sistemas externos.     |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Dado um lote de 1.000 NF-e presentes na base NBS, o módulo deve recuperar e enfileirar 100% delas para processamento sem intervenção manual e sem geração de arquivo intermediário de exportação. |
| **Rastreabilidade**    | RF-01 (Iara Inbound); RNF-01; RNF-02                                                                                                        |

---

**RF-002 — Seleção de escopo temporal de processamento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao usuário definir o intervalo de datas de emissão ou de entrada das NF-e a serem processadas em cada execução de auditoria. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O usuário consegue selecionar intervalo de datas (data inicial e data final) e o sistema processa exclusivamente NF-e cujo campo de data configurado esteja dentro do intervalo. NF-e fora do intervalo não aparecem no lote. |
| **Rastreabilidade**    | RF-01 (Iara Inbound); entrevista Sandro Siqueira                                                                                            |

---

**RF-003 — Seleção de escopo por fornecedor e CNPJ**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir filtrar NF-e para processamento por CNPJ do emitente, razão social do emitente ou grupo de fornecedores previamente cadastrado. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Dado um filtro por CNPJ "00.000.000/0001-00", o lote de processamento contém apenas NF-e cujo CNPJ emitente seja exatamente "00.000.000/0001-00". Nenhuma NF-e de outro emitente é incluída no lote. |
| **Rastreabilidade**    | RF-01 (Iara Inbound); RF-07 (fluxo operacional)                                                                                             |

---

**RF-004 — Reprocessamento de NF-e auditadas**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao Analista de Contabilidade solicitar o reprocessamento de uma NF-e já auditada, substituindo o resultado anterior pelo novo, com registro da data, hora e usuário que solicitou o reprocessamento. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Após solicitar reprocessamento de uma NF-e, o resultado anterior é substituído pelo novo resultado. O histórico registra a versão anterior com o atributo "substituída", a data/hora do reprocessamento e o login do usuário solicitante. |
| **Rastreabilidade**    | RF-07 (manter fluxo operacional); entrevista Sandro Siqueira                                                                                |

---

### M2 — Módulo de Auditoria Automatizada

---

**RF-005 — Auditoria de conformidade de dados cadastrais do emitente**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve verificar, para cada NF-e processada, se o CNPJ do emitente está ativo na base da Receita Federal (ou na base cadastral do ERP) e se a razão social constante na NF-e corresponde ao cadastro. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para uma NF-e emitida por CNPJ com situação "inapta" na base cadastral, o sistema classifica a NF-e com o alerta "Emitente com CNPJ inapto" e bloqueia o fluxo de aprovação até resolução manual. Taxa de falsos negativos (NF-e irregulares não detectadas) deve ser 0% para CNPJs inaptos presentes na base cadastral. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-03 (detecção de fraudes)                                                                                 |

---

**RF-006 — Auditoria de consistência dos valores tributários declarados**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve calcular os valores de ICMS, IPI, PIS e COFINS esperados para cada item da NF-e com base no NCM, CFOP, CST/CSOSN e alíquotas vigentes, e comparar com os valores declarados pelo emitente, sinalizando divergências. |
| **Prioridade**         : M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para uma NF-e com valor de ICMS declarado divergindo em mais de R$ 0,01 do valor calculado pelo sistema, o sistema sinaliza a divergência com o código de alerta "ICMS-DIV", exibe o valor declarado, o valor calculado e a diferença. A taxa de detecção de divergências de ICMS acima de R$ 1,00 deve ser 100% sobre lote de teste validado com a equipe de contabilidade. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-04 (risco de multa)                                                                                      |

---

**RF-007 — Auditoria de duplicidade de NF-e**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve identificar NF-e duplicadas pelo cruzamento de chave de acesso, CNPJ emitente, número da nota, série e valor total, sinalizando qualquer duplicidade detectada antes da aprovação do pagamento. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para um lote de teste contendo 5 pares de NF-e duplicadas (mesma chave de acesso), o sistema detecta e sinaliza os 10 documentos envolvidos com o código "NF-DUP", bloqueando o fluxo de pagamento de ambas até resolução. Taxa de detecção: 100% sobre lote de teste. |
| **Rastreabilidade**    | RF-03 (detecção de fraudes); RF-05 (pagamentos indevidos)                                                                                   |

---

**RF-008 — Auditoria de NF-e canceladas pagas ou em fila de pagamento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve cruzar o status de cada NF-e com o registro de cancelamento na base NBS e, ao identificar NF-e cancelada com pagamento registrado ou pendente, emitir alerta imediato ao Analista de Contabilidade e ao Analista Financeiro. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para um lote de teste com 3 NF-e canceladas e com pagamento pendente, o sistema detecta as 3 notas, emite alerta "NF-CANCEL-PAG" para os perfis Contabilidade e Financeiro e bloqueia o fluxo de pagamento. Tempo máximo entre registro do cancelamento na base e geração do alerta: 15 minutos (em processamento contínuo). |
| **Rastreabilidade**    | RF-03 (detecção de fraudes); RF-05 (pagamentos indevidos); RF-04 (risco de multa)                                                           |

---

**RF-009 — Auditoria de conformidade do CFOP com a natureza da operação**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve verificar se o CFOP declarado em cada item da NF-e é compatível com a natureza da operação (compra, transferência, devolução, etc.) registrada no ERP, com base em tabela de regras configurável pelo administrador. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Para um lote de teste com 10 NF-e de compra contendo CFOP incompatível com a natureza "entrada por compra", o sistema sinaliza as 10 com código "CFOP-INC" e registra a inconsistência no log de auditoria. A tabela de regras deve ser editável pelo perfil Administrador sem necessidade de deploy de nova versão. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-04 (risco de multa)                                                                                      |

---

**RF-010 — Auditoria de validade da autorização SEFAZ (chave de acesso)**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve verificar a autenticidade de cada NF-e pelo confronto da chave de acesso com o status de autorização registrado na base NBS (proveniente da consulta SEFAZ no momento da entrada da nota), sinalizando NF-e com chave não autorizada ou com status diferente de "autorizado de uso". |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para um lote de teste com 5 NF-e cujo status SEFAZ seja "denegada" ou "sem resposta", o sistema classifica as 5 com o código "SEFAZ-INV" e impede o fluxo de aprovação. Taxa de detecção: 100% sobre lote de teste. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-03 (detecção de fraudes)                                                                                 |

---

**RF-011 — Registro de resultado de auditoria por NF-e**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve registrar, para cada NF-e processada, o resultado da auditoria (aprovada, aprovada com ressalvas, bloqueada), os códigos de alerta emitidos, a data/hora do processamento e a versão das regras tributárias aplicadas. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para qualquer NF-e processada, o registro de auditoria deve conter: chave de acesso, status final, lista de códigos de alerta (vazia se aprovada sem ressalvas), timestamp do processamento (formato ISO 8601) e identificador da versão do conjunto de regras usado. Registro deve ser imutável após conclusão do processamento; qualquer revisão deve gerar novo registro vinculado. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-07 (fluxo operacional)                                                                                   |

---

### M3 — Módulo de Alertas

---

**RF-012 — Alerta de risco de multa por atraso ou incorreção tributária**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar alerta para o Analista de Contabilidade quando identificar NF-e com divergência tributária que configure risco de autuação fiscal, classificando o alerta por nível de criticidade (Alta, Média, Baixa) com base em critérios configuráveis pelo administrador. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Um alerta de criticidade "Alta" é gerado em até 15 minutos após a conclusão do processamento da NF-e que originhou a divergência (em modo de processamento contínuo). O alerta exibe: chave de acesso, tipo de divergência, criticidade, valor em risco e ação sugerida. O usuário consegue acessar o alerta diretamente do painel principal sem mais de 2 cliques. |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); entrevista Sandro Siqueira                                                                               |

---

**RF-013 — Alerta de pagamento indevido**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar alerta direcionado ao Analista Financeiro quando identificar NF-e com risco de pagamento indevido (duplicidade, NF-e cancelada com pagamento pendente, valor incorreto acima de tolerância configurável). |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para cada evento de pagamento indevido detectado, um alerta é enviado ao perfil Financeiro dentro de 15 minutos (modo contínuo). O alerta especifica: CNPJ do emitente, número e chave de acesso da NF-e, tipo de irregularidade, valor em risco e data de vencimento do pagamento (se aplicável). |
| **Rastreabilidade**    | RF-05 (alertas de pagamentos indevidos); perfil Analista Financeiro                                                                         |

---

**RF-014 — Painel de alertas com fila de resolução**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve disponibilizar um painel centralizado de alertas ativos, permitindo ao Analista de Contabilidade visualizar todos os alertas pendentes, filtrá-los por tipo, criticidade e data, registrar a ação tomada e marcar o alerta como resolvido. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O painel exibe todos os alertas com status "pendente" para o perfil logado. O usuário consegue filtrar por qualquer combinação de: tipo de alerta, nível de criticidade e intervalo de datas. Ao marcar um alerta como "resolvido", o sistema exige preenchimento de campo "Descrição da resolução" (mínimo 10 caracteres) e registra o login do usuário e o timestamp. |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); RF-05 (pagamentos indevidos); RF-07 (fluxo operacional)                                                  |

---

**RF-015 — Notificação automática por e-mail para alertas críticos**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve enviar notificação por e-mail aos usuários destinatários configurados quando um alerta de criticidade "Alta" for gerado, com link direto para o alerta no ERP. |
| **Prioridade**         | C — Could Have                                                                                                                              |
| **Critério de Aceitação** | Para cada alerta de criticidade "Alta" gerado, o e-mail é enviado em até 5 minutos ao(s) destinatário(s) configurados para o tipo de alerta. O e-mail contém: tipo do alerta, NF-e envolvida (chave de acesso e número), valor em risco, criticidade e link direto para o alerta no ERP. O envio de e-mail deve ser configurável por tipo de alerta (ativável/desativável pelo administrador). |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); RF-08 (usabilidade)                                                                                      |

---

### M4 — Módulo de Relatórios

---

**RF-016 — Relatório operacional de NF-e auditadas**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório listando todas as NF-e auditadas em um intervalo de datas definido pelo usuário, com os campos: chave de acesso, número, série, CNPJ emitente, data de emissão, valor total, status de auditoria, códigos de alerta e data do processamento. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O relatório é gerado em até 60 segundos para lotes de até 10.000 NF-e. O resultado é exportável em formato XLSX e PDF diretamente do ERP. Todos os campos listados na descrição estão presentes no relatório exportado. |
| **Rastreabilidade**    | RF-06 (relatórios operacionais e gerenciais); perfil Analista de Contabilidade                                                              |

---

**RF-017 — Relatório gerencial de conformidade tributária**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório gerencial com indicadores de conformidade: total de NF-e processadas, percentual aprovadas sem ressalvas, percentual com alertas por categoria, valor total em risco e evolução mês a mês, para um período selecionável pelo usuário. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O relatório gerencial exibe os indicadores acima com corte mensal para qualquer período de até 24 meses consecutivos. É exportável em XLSX e PDF. Os dados do relatório correspondem, com 100% de exatidão, à soma dos registros individuais de auditoria no mesmo período (verificável por auditoria cruzada). |
| **Rastreabilidade**    | RF-06 (relatórios gerenciais); perfil Supervisor de Contabilidade                                                                           |

---

**RF-018 — Relatório de conformidade e risco para o Jurídico**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório de histórico de auditoria de NF-e por fornecedor, exibindo todas as irregularidades registradas, ações tomadas, datas e responsáveis, exportável em PDF com layout adequado para uso em peças jurídicas e defesas administrativas. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O relatório PDF gerado contém: identificação do emitente (CNPJ, razão social), lista cronológica de NF-e com irregularidades, descrição da irregularidade, ação registrada, usuário responsável e data de resolução. O PDF inclui rodapé com identificação do sistema, data/hora de geração e login do usuário que gerou o relatório. A equipe jurídica valida o layout como adequado para uso formal (a ser verificado em teste de aceitação com representante do Jurídico). |
| **Rastreabilidade**    | RF-06 (relatórios); perfil Analista Jurídico; PEN-004                                                                                       |

---

**RF-019 — Relatório de pagamentos indevidos**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório consolidado de pagamentos indevidos detectados no período, listando: NF-e envolvida, tipo de irregularidade, valor do pagamento em risco, status de resolução e valor efetivamente recuperado (quando informado pelo usuário). |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O relatório é exportável em XLSX. O campo "valor recuperado" é editável pelo perfil Financeiro após resolução do alerta correspondente. O somatório de "valor em risco" e "valor recuperado" no relatório coincide, com diferença de até R$ 0,01 (tolerância de arredondamento), com a soma dos registros individuais de alerta no período. |
| **Rastreabilidade**    | RF-05 (pagamentos indevidos); RF-06 (relatórios); perfil Analista Financeiro                                                                |

---

**RF-020 — Disponibilização de dados para consumo por Power BI**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve expor os dados de resultados de auditoria, alertas e indicadores gerenciais por meio de mecanismo compatível com Power BI (API REST, OData endpoint ou view de banco de dados de leitura), permitindo construção de dashboards externos. |
| **Prioridade**         | C — Could Have                                                                                                                              |
| **Critério de Aceitação** | Um relatório no Power BI Desktop consegue conectar-se à fonte de dados do módulo, importar dados de NF-e auditadas (pelo menos os campos de RF-016) e atualizar ao acionar "Atualizar" no Power BI. A configuração da conexão deve ser documentada pela NBS. |
| **Rastreabilidade**    | RF-06 (relatórios); RNF-10 (compatibilidade Power BI); demanda Sandro Siqueira                                                              |

---

### M5 — Módulo de Configuração de Regras Tributárias

---

**RF-021 — Cadastro e manutenção de regras tributárias**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao perfil Administrador cadastrar, editar, desativar e versionar regras tributárias (alíquotas, exceções por NCM, CFOP permitidos por operação, etc.) sem necessidade de intervenção da NBS para cada atualização legislativa. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O Administrador consegue criar uma nova regra de alíquota de ICMS para um NCM específico, salvar e verificar que NF-e com aquele NCM processadas após a ativação da regra são auditadas com a nova alíquota. A regra anterior permanece no histórico de versões com data de vigência. O sistema não permite ativação de regra sem data de início de vigência. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-07 (fluxo operacional); RNF-05 (manutenibilidade)                                                        |

---

**RF-022 — Configuração de tolerâncias e limiares de alerta**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao perfil Administrador configurar limiares numéricos que definem quando uma divergência gera alerta (ex.: diferença de ICMS acima de R$ X, duplicidade exata vs. aproximada, percentual de variação de valor entre NF-e do mesmo fornecedor). |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O Administrador consegue alterar o limiar de divergência de ICMS de R$ 1,00 para R$ 5,00. Após a alteração, NF-e com divergência de ICMS entre R$ 1,00 e R$ 4,99 não geram mais alerta. NF-e com divergência de R$ 5,00 ou mais continuam gerando alerta. A alteração é registrada no log de auditoria do sistema. |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); RF-05 (pagamentos indevidos); entrevista Sandro Siqueira                                                 |

---

**RF-023 — Atualização de tabelas fiscais de referência**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve manter tabelas fiscais de referência (tabela NCM, tabela CFOP, tabela CST/CSOSN, alíquotas estaduais de ICMS) atualizadas, permitindo ao Administrador importar novas versões dessas tabelas em formato definido pela NBS. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O Administrador consegue importar um arquivo de atualização da tabela NCM no formato especificado, confirmar a importação e verificar que novos NCMs estão disponíveis nas regras tributárias. NF-e com NCMs novos processadas após a atualização são auditadas corretamente. O sistema rejeita arquivos em formato inválido com mensagem de erro descritiva. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RNF-05 (manutenibilidade)                                                                                   |

---

### M6 — Módulo de Administração e Controle de Acesso

---

**RF-024 — Gestão de perfis e permissões de usuário**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve controlar o acesso às funcionalidades por perfil de usuário (Analista de Contabilidade, Supervisor de Contabilidade, Analista Financeiro, Analista Jurídico, Administrador), garantindo que cada perfil acesse apenas as funcionalidades e dados para os quais tem permissão. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Um usuário com perfil "Analista Financeiro" não consegue acessar a tela de configuração de regras tributárias nem alterar o status de auditoria de uma NF-e. Um usuário com perfil "Analista Jurídico" consegue gerar e exportar relatórios, mas não consegue marcar alertas como resolvidos. A separação de permissões é testada para todos os 5 perfis listados. |
| **Rastreabilidade**    | RNF-06 (controle de acesso); RNF-07 (auditoria de ações)                                                                                    |

---

**RF-025 — Log de auditoria de ações de usuário**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve registrar em log imutável todas as ações de usuário que alteram dados ou configurações do módulo, incluindo: login do usuário, data/hora (ISO 8601, fuso UTC-3), tipo de ação, entidade afetada e valores anteriores e posteriores à alteração. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para cada ação de alteração de dado (resolução de alerta, edição de regra, reprocessamento de NF-e, alteração de permissão), um registro de log é criado contendo os campos acima. O log não pode ser editado ou excluído por nenhum perfil de usuário, incluindo o Administrador. O Supervisor de Contabilidade e o Administrador conseguem consultar e exportar o log por período. |
| **Rastreabilidade**    | RNF-07 (auditoria de ações); conformidade LGPD; entrevista Sandro Siqueira                                                                  |

---

**RF-026 — Dashboard operacional de status do módulo**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve exibir, na tela inicial do módulo, um dashboard com os seguintes indicadores em tempo real (defasagem máxima de 5 minutos): total de NF-e processadas no dia, total de alertas pendentes por criticidade, total de NF-e bloqueadas aguardando resolução e data/hora do último processamento executado. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Após processamento de um lote de NF-e, os contadores do dashboard refletem os novos valores em no máximo 5 minutos. Os valores exibidos no dashboard coincidem com os totais calculados pelos relatórios de mesmo período (diferença permitida: zero). |
| **Rastreabilidade**    | RF-08 (usabilidade superior ao Fiscal Defender); RF-07 (fluxo operacional)                                                                  |

---

**RF-027 — Exportação do log de auditoria para conformidade regulatória**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao perfil Supervisor de Contabilidade e ao perfil Analista Jurídico exportar o log completo de auditoria de ações de um período definido, em formato XLSX ou PDF, para fins de comprovação perante órgãos fiscalizadores. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O log exportado em XLSX contém todos os campos do RF-025 para o período solicitado, sem omissões. O PDF exportado inclui identificação do sistema, período do log e login de quem solicitou a exportação. A exportação de um período de 12 meses é concluída em até 120 segundos. |
| **Rastreabilidade**    | RF-06 (relatórios); RF-025; perfil Analista Jurídico                                                                                        |

---

## 5. Requisitos Não-Funcionais

---

**RNF-001 — Integração nativa ao ERP NBS (arquitetura)**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo Auditor Fiscal deve ser desenvolvido como componente nativo do ERP NBS, sem dependência de sistemas externos para sua operação de auditoria. |
| **Critério de Aceitação** | A auditoria de uma NF-e é executada do início ao fim sem que o módulo realize chamadas a endpoints externos ao ERP NBS, verificável por análise de tráfego de rede durante execução de lote de auditoria. |
| **Rastreabilidade**    | RNF-01 (Iara Inbound)                                                                                                                       |

---

**RNF-002 — Operação sobre base de dados unificada NBS**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve operar sobre a mesma base de dados do ERP NBS, eliminando a necessidade de sincronização, exportação ou replicação de dados de NF-e para processamento. |
| **Critério de Aceitação** | Uma NF-e registrada na base NBS é processável pelo módulo sem etapa de importação ou cópia para base separada. A inserção de uma NF-e na base NBS torna-a disponível ao módulo para processamento em até 5 minutos (em modo de processamento contínuo). |
| **Rastreabilidade**    | RNF-02 (Iara Inbound)                                                                                                                       |

---

**RNF-003 — Custo de desenvolvimento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O desenvolvimento do módulo não deve gerar custo direto de desenvolvimento para o Grupo Águia Branca, sendo coberto pelo contrato de fornecimento do ERP NBS já vigente ou por acordo comercial separado entre NBS e Grupo Águia Branca. |
| **Critério de Aceitação** | Contrato ou adendo contratual firmado entre Grupo Águia Branca e NBS antes do início do desenvolvimento, especificando que o módulo está incluído no escopo sem custo adicional de licença ou desenvolvimento. **Nota:** Este critério depende de negociação em andamento (ver Premissa P-002). |
| **Rastreabilidade**    | RNF-03 (Iara Inbound)                                                                                                                       |

---

**RNF-004 — Performance: processamento de lote**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve processar lotes de NF-e dentro dos seguintes limites de tempo, medidos em ambiente de produção com carga normal do ERP. |
| **Critério de Aceitação** | (a) Lote de até 1.000 NF-e: processamento completo em no máximo 10 minutos. (b) Lote de até 10.000 NF-e: processamento completo em no máximo 90 minutos. (c) Processamento de NF-e individual (modo interativo): resultado em no máximo 30 segundos. Os limites de volume de NF-e do Grupo Águia Branca Divisão Comércio devem ser confirmados (ver PEN-001). |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RNF-04 (Iara Inbound)                                                                                       |

---

**RNF-005 — Disponibilidade do sistema**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve estar disponível para uso durante o horário de operação da Divisão Comércio, com janela de manutenção restrita a períodos de baixo impacto. |
| **Critério de Aceitação** | Disponibilidade mensal mínima de 99,5% no horário de 07h00 às 20h00 (dias úteis), medida pelo monitoramento do ERP NBS. Janelas de manutenção planejadas devem ser comunicadas com antecedência mínima de 48 horas e agendadas preferencialmente nos horários 22h00–05h00. Tempo máximo de indisponibilidade não planejada em um único incidente: 4 horas. |
| **Rastreabilidade**    | RNF-04 (Iara Inbound)                                                                                                                       |

---

**RNF-006 — Segurança: controle de acesso**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O acesso ao módulo deve ser controlado por autenticação integrada ao mecanismo de autenticação do ERP NBS, com controle de permissões por perfil de usuário conforme definido em RF-024. |
| **Critério de Aceitação** | (a) Usuário não autenticado no ERP não acessa nenhuma funcionalidade do módulo. (b) Usuário autenticado com perfil inadequado recebe mensagem de "Acesso não autorizado" ao tentar acessar funcionalidade restrita — sem exposição de dados da funcionalidade. (c) Tentativas de acesso não autorizado são registradas no log de segurança do ERP. |
| **Rastreabilidade**    | RF-024 (controle de acesso); LGPD; entrevista Sandro Siqueira                                                                               |

---

**RNF-007 — Segurança: auditoria de ações (rastreabilidade de usuário)**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | Todas as ações de alteração de dados, configurações e resultados de auditoria realizadas por usuários devem ser rastreáveis individualmente, conforme RF-025. |
| **Critério de Aceitação** | Para qualquer alteração realizada há até 5 anos (período de guarda mínimo), é possível identificar: quem realizou, quando (data/hora UTC-3), o quê foi alterado e os valores antes e depois. O log é armazenado de forma que não possa ser alterado por usuários da aplicação, incluindo o perfil Administrador. |
| **Rastreabilidade**    | RF-025; LGPD; conformidade fiscal                                                                                                           |

---

**RNF-008 — Usabilidade: tempo de treinamento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | Um novo Analista de Contabilidade com experiência prévia no ERP NBS deve ser capaz de executar as tarefas principais do módulo (processar lote, consultar alertas, gerar relatório operacional) após treinamento formal máximo de 4 horas. |
| **Critério de Aceitação** | Em teste de usabilidade com 3 Analistas de Contabilidade que nunca usaram o módulo mas têm experiência no ERP NBS: após 4 horas de treinamento formal, cada analista consegue executar as 3 tarefas principais sem auxílio externo, com taxa de erro abaixo de 10% nas tarefas (erro = ação que produz resultado diferente do esperado ou que gera mensagem de erro não intencional). |
| **Rastreabilidade**    | RF-08 (usabilidade superior ao Fiscal Defender)                                                                                             |

---

**RNF-009 — Usabilidade: acesso a alerta em no máximo 3 cliques**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | A partir da tela inicial do módulo, o usuário deve conseguir visualizar o detalhe de qualquer alerta pendente em no máximo 3 cliques. |
| **Critério de Aceitação** | Em teste com usuário do perfil Analista de Contabilidade logado na tela inicial do módulo: o acesso ao detalhe de um alerta específico (selecionado aleatoriamente da fila de alertas pendentes) requer no máximo 3 cliques (interações com elementos da interface). Verificado para 10 alertas distintos. |
| **Rastreabilidade**    | RF-08 (usabilidade superior ao Fiscal Defender); RF-014 (painel de alertas)                                                                 |

---

**RNF-010 — Compatibilidade com Power BI**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve expor dados de auditoria por mecanismo compatível com conexão direta do Power BI Desktop e Power BI Service (Microsoft), sem necessidade de desenvolvimento de conector customizado. |
| **Critério de Aceitação** | Utilizando o Power BI Desktop (versão mais recente disponível no momento do teste de aceitação), o usuário consegue criar uma conexão com a fonte de dados do módulo utilizando conectores nativos do Power BI (OData, SQL Server, API REST via conector Web ou equivalente) e importar dados de NF-e auditadas sem desenvolvimento adicional. |
| **Rastreabilidade**    | RF-020; demanda Sandro Siqueira                                                                                                             |

---

**RNF-011 — Manutenibilidade: responsabilidade da NBS**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | A NBS deve garantir que atualizações de versão do ERP NBS não quebrem a compatibilidade do módulo Auditor Fiscal, sendo responsável por adequar o módulo às novas versões do ERP dentro do ciclo normal de suporte do produto. |
| **Critério de Aceitação** | O SLA de compatibilidade está contratualmente definido: a NBS entrega versão compatível do módulo em até 30 dias após o lançamento de nova versão do ERP NBS que afete o módulo. Mudanças legislativas tributárias com vigência publicada oficialmente com mais de 30 dias de antecedência são incorporadas ao módulo antes da data de vigência. |
| **Rastreabilidade**    | RNF-05 (manutenibilidade — Iara Inbound); RNF-003                                                                                           |

---

**RNF-012 — Conformidade com a LGPD**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve tratar dados de pessoas físicas eventualmente presentes em NF-e (CPF de destinatário, dados de transportadores, etc.) em conformidade com a Lei 13.709/2018 (LGPD), garantindo que dados pessoais não sejam expostos em relatórios a perfis sem necessidade legítima de acesso. |
| **Critério de Aceitação** | Relatório gerado pelo perfil Analista Financeiro não exibe CPF de pessoas físicas constantes nas NF-e, exibindo apenas dados da pessoa jurídica (CNPJ, razão social). O perfil Analista Jurídico tem acesso a CPF apenas mediante justificativa registrada no log. |
| **Rastreabilidade**    | LGPD; RNF-006; entrevista Sandro Siqueira                                                                                                   |

---

## 6. Matriz de Rastreabilidade

| RF / RNF | Título Resumido                                 | Origem                             | Módulo | MoSCoW | Critério de Aceitação Resumido                                                              |
|----------|-------------------------------------------------|------------------------------------|--------|--------|---------------------------------------------------------------------------------------------|
| RF-001   | Acesso nativo às NF-e da base NBS               | RF-01 Iara; RNF-01; RNF-02         | M1     | M      | 100% das NF-e do lote recuperadas sem arquivo intermediário                                 |
| RF-002   | Seleção de escopo temporal                      | RF-01 Iara; Sandro                 | M1     | M      | Filtragem por intervalo de datas correta                                                    |
| RF-003   | Seleção por fornecedor/CNPJ                     | RF-01 Iara; RF-07                  | M1     | S      | Filtro por CNPJ retorna apenas NF-e do emitente correto                                     |
| RF-004   | Reprocessamento de NF-e                         | RF-07; Sandro                      | M1     | S      | Resultado anterior substituído; histórico mantido com log de usuário                        |
| RF-005   | Auditoria de cadastro do emitente               | RF-02; RF-03 Iara                  | M2     | M      | CNPJ inapto detectado com 0% de falso negativo                                              |
| RF-006   | Auditoria de valores tributários                | RF-02; RF-04 Iara                  | M2     | M      | Divergências acima de R$ 1,00 detectadas a 100%                                             |
| RF-007   | Auditoria de duplicidade de NF-e                | RF-03; RF-05 Iara                  | M2     | M      | 100% dos pares duplicados detectados e bloqueados                                           |
| RF-008   | NF-e cancelada com pagamento pendente           | RF-03; RF-05; RF-04 Iara           | M2     | M      | Detecção e alerta em ≤15 min; bloqueio de pagamento                                         |
| RF-009   | Auditoria de CFOP vs. natureza da operação      | RF-02; RF-04 Iara                  | M2     | S      | 100% de CFOP incompatíveis detectados; regras editáveis sem deploy                          |
| RF-010   | Validação da autorização SEFAZ                  | RF-02; RF-03 Iara                  | M2     | M      | 100% de NF-e não autorizadas bloqueadas                                                     |
| RF-011   | Registro de resultado de auditoria              | RF-02; RF-07 Iara                  | M2     | M      | Registro imutável com todos os campos; revisão cria novo registro                           |
| RF-012   | Alerta de risco de multa                        | RF-04 Iara; Sandro                 | M3     | M      | Alerta Alta gerado em ≤15 min; acessível em ≤2 cliques                                      |
| RF-013   | Alerta de pagamento indevido                    | RF-05 Iara; Financeiro             | M3     | M      | Alerta ao Financeiro em ≤15 min com todos os campos                                         |
| RF-014   | Painel de alertas com fila de resolução         | RF-04; RF-05; RF-07 Iara           | M3     | M      | Filtros funcionais; resolução exige campo descritivo; log registrado                        |
| RF-015   | Notificação por e-mail (alertas críticos)       | RF-04; RF-08 Iara                  | M3     | C      | E-mail entregue em ≤5 min; configurável por tipo de alerta                                  |
| RF-016   | Relatório operacional de NF-e auditadas         | RF-06 Iara; Contabilidade          | M4     | M      | Gerado em ≤60 s para 10.000 NF-e; exportável XLSX/PDF                                      |
| RF-017   | Relatório gerencial de conformidade             | RF-06 Iara; Supervisão             | M4     | M      | Dados corretos para 24 meses; exportável XLSX/PDF                                          |
| RF-018   | Relatório de conformidade/risco (Jurídico)      | RF-06 Iara; Jurídico               | M4     | S      | PDF com layout formal; validado pelo Jurídico                                               |
| RF-019   | Relatório de pagamentos indevidos               | RF-05; RF-06 Iara; Financeiro      | M4     | S      | Valor recuperado editável; totais consistentes                                              |
| RF-020   | Dados para Power BI                             | RF-06 Iara; Sandro; RNF-10         | M4     | C      | Conexão Power BI via conector nativo sem desenvolvimento extra                              |
| RF-021   | Cadastro de regras tributárias                  | RF-02; RF-07 Iara; RNF-05          | M5     | M      | Regra nova aplicada imediatamente; histórico de versões mantido                             |
| RF-022   | Configuração de tolerâncias de alerta           | RF-04; RF-05 Iara; Sandro          | M5     | S      | Alteração de limiar reflete em comportamento de alertas; log registrado                     |
| RF-023   | Atualização de tabelas fiscais                  | RF-02 Iara; RNF-05                 | M5     | M      | Tabela atualizada reflete em auditoria; arquivos inválidos rejeitados                       |
| RF-024   | Gestão de perfis e permissões                   | RNF-06; RNF-07                     | M6     | M      | Perfil inadequado bloqueado sem expor dados; 5 perfis testados                              |
| RF-025   | Log de auditoria de ações de usuário            | RNF-07; LGPD; Sandro               | M6     | M      | Log imutável com todos os campos; 5 anos de guarda                                          |
| RF-026   | Dashboard operacional                           | RF-08; RF-07 Iara                  | M6     | S      | Atualização em ≤5 min; totais coerentes com relatórios                                      |
| RF-027   | Exportação do log para conformidade             | RF-06; RF-025; Jurídico            | M6     | S      | XLSX completo; PDF identificado; exportação 12 meses em ≤120 s                              |
| RNF-001  | Integração nativa ao ERP NBS                    | RNF-01 Iara                        | —      | M      | Sem chamadas externas durante auditoria                                                     |
| RNF-002  | Base de dados unificada NBS                     | RNF-02 Iara                        | —      | M      | NF-e disponível para o módulo em ≤5 min após inserção                                      |
| RNF-003  | Custo zero de desenvolvimento                   | RNF-03 Iara                        | —      | M      | Contrato/adendo firmado antes do desenvolvimento                                            |
| RNF-004  | Performance de processamento                    | RF-02; RNF-04 Iara                 | —      | M      | 1.000 NF-e em ≤10 min; 10.000 NF-e em ≤90 min; individual em ≤30 s                        |
| RNF-005  | Disponibilidade (SLA)                           | RNF-04 Iara                        | —      | M      | ≥99,5% em horário comercial; incidente máximo de 4 h                                        |
| RNF-006  | Controle de acesso                              | RF-024; LGPD                       | —      | M      | Não autenticado: sem acesso; perfil inadequado: mensagem de erro sem exposição de dados     |
| RNF-007  | Auditoria de ações (rastreabilidade)            | RF-025; LGPD; fiscal               | —      | M      | Qualquer ação dos últimos 5 anos rastreável; log inalterável                                |
| RNF-008  | Usabilidade: tempo de treinamento               | RF-08 Iara                         | —      | M      | 3 analistas executam tarefas principais após 4h; erro <10%                                  |
| RNF-009  | Usabilidade: acesso a alerta em ≤3 cliques      | RF-08; RF-014                      | —      | M      | ≤3 cliques para detalhe de qualquer alerta; 10 alertas testados                             |
| RNF-010  | Compatibilidade Power BI                        | RF-020; Sandro                     | —      | C      | Conexão com conector nativo; dados importáveis sem dev adicional                            |
| RNF-011  | Manutenibilidade pela NBS                       | RNF-05 Iara; RNF-003               | —      | M      | Compatibilidade em ≤30 dias pós-nova versão ERP; legislação antes da vigência               |
| RNF-012  | Conformidade LGPD                               | LGPD; RNF-006; Sandro              | —      | M      | CPF oculto para Financeiro; acesso Jurídico com log de justificativa                        |

---

## 7. Restrições Técnicas

| ID    | Restrição                                                                                                                                  |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| RT-01 | O módulo deve ser desenvolvido na plataforma tecnológica do ERP NBS, sem introdução de tecnologias de terceiros não suportadas pela NBS.    |
| RT-02 | O acesso à base de dados do ERP NBS pelo módulo deve seguir as políticas de acesso a dados definidas pela NBS, sem acesso direto a tabelas de banco de dados por queries ad hoc de usuários finais. |
| RT-03 | A exportação de dados para Power BI deve utilizar mecanismo aprovado pela equipe de TI do Grupo Águia Branca, respeitando as políticas de segurança de dados corporativos. |
| RT-04 | O módulo não pode modificar registros originais de NF-e na base NBS; toda anotação de resultado de auditoria deve ser gravada em estrutura de dados separada e vinculada por chave de acesso. |
| RT-05 | A comunicação entre o módulo e qualquer serviço da NBS ou do Grupo Águia Branca deve utilizar canais criptografados (TLS 1.2 ou superior). |
| RT-06 | O ambiente de homologação do módulo deve ser segregado do ambiente de produção, com dados anonimizados de NF-e para testes (sem dados fiscais reais). |

---

## 8. Premissas da Especificação

| ID    | Premissa                                                                                                                                    | Impacto se inválida                                                                                           |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| P-001 | As NF-e da Divisão Comércio já estão integralmente disponíveis na base de dados do ERP NBS no momento em que o módulo for implantado, sem necessidade de migração histórica de dados do Fiscal Defender. | Se houver necessidade de migração histórica, o RF-001 deve ser revisado para incluir requisitos de importação de dados legados. |
| P-002 | **O acordo entre o Grupo Águia Branca e a NBS para desenvolvimento do módulo sem custo adicional ainda não foi verificado documentalmente.** Essa especificação assume que tal acordo será formalizado antes do início do desenvolvimento. | Se o acordo não for formalizado, o RNF-003 não pode ser garantido, e o projeto pode não ser viável nas condições atuais. Esta é a premissa de maior risco do projeto. |
| P-003 | As regras tributárias aplicáveis às operações da Divisão Comércio (alíquotas de ICMS, IPI, PIS/COFINS, exceções por NCM, etc.) serão fornecidas pela equipe de Contabilidade em formato estruturado para cadastro inicial no módulo. | Se as regras não forem fornecidas, o módulo não poderá executar auditoria tributária ao entrar em produção. |
| P-004 | O Fiscal Defender continuará operando em paralelo ao módulo Auditor Fiscal durante um período de operação paralela a ser definido (sugestão: 30 a 60 dias), para validação dos resultados antes do desligamento definitivo. | Se não houver operação paralela, o risco de falhas não detectadas no módulo é elevado. |
| P-005 | Os usuários dos perfis Financeiro e Jurídico participarão de sessões de levantamento de requisitos para confirmar os RFs e RNFs relacionados aos seus perfis (ver Seção 10, PEN-003 e PEN-004). | Se não participarem, os requisitos para esses perfis podem estar incompletos, impactando a aceitação do módulo. |
| P-006 | A NBS tem capacidade técnica e recursos disponíveis para desenvolver o módulo dentro do prazo a ser negociado, sem impactar o roadmap dos demais módulos do ERP em uso pelo Grupo Águia Branca. | Se a NBS não tiver capacidade, o cronograma do projeto precisa ser revisto. |

---

## 9. Itens Fora do Escopo

| ID    | Item fora do escopo                                                                                           | Justificativa / Observação                                                          |
|-------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| FE-01 | Emissão de NF-e                                                                                               | Funcionalidade já existente no ERP NBS; fora do escopo do módulo Auditor Fiscal     |
| FE-02 | Escrituração fiscal e geração de obrigações acessórias (SPED Fiscal, EFD-Contribuições, etc.)                | Funcionalidade já existente no ERP NBS ou em módulo separado                        |
| FE-03 | Transmissão direta de NF-e para a SEFAZ                                                                       | Responsabilidade do módulo de emissão do ERP NBS                                   |
| FE-04 | Auditoria de NF-e de outras divisões do Grupo Águia Branca além da Divisão Comércio                          | Escopo desta fase restrito à Divisão Comércio; extensão para outras divisões é projeto futuro |
| FE-05 | Auditoria de documentos fiscais que não sejam NF-e (CT-e, NFS-e municipal, NF-e de combustíveis com regras específicas, etc.) | Fora do escopo desta versão; pode ser incluído em versão futura                     |
| FE-06 | Integração com sistemas de gestão de fornecedores para acionamento automático de disputa                      | Fora do escopo; a resolução de alertas é manual pelo usuário no módulo              |
| FE-07 | Substituição ou modificação do processo de importação de NF-e no ERP NBS (processo de entrada de documentos) | O módulo audita NF-e já importadas; não altera o processo de importação             |
| FE-08 | Funcionalidades de BI ou analytics avançados integrados ao módulo (dashboards analíticos complexos)           | A integração Power BI (RF-020 / RNF-010) é o mecanismo previsto para BI avançado    |
| FE-09 | Manutenção ou suporte ao Fiscal Defender após o desligamento                                                  | O Fiscal Defender será desativado após a validação do módulo; suporte é do fornecedor |
| FE-10 | Integração com sistemas de outras empresas do Grupo Águia Branca fora da Divisão Comércio                    | Fora do escopo desta fase                                                           |

---

## 10. Pendências e Requisitos a Confirmar

| ID      | Pendência                                                                                       | Responsável pela resposta             | Impacto nos Requisitos                                                                                      | Data-limite sugerida |
|---------|-------------------------------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------|
| PEN-001 | Volume médio e máximo de NF-e processadas por dia/mês pela Divisão Comércio                     | Sandro Siqueira (Contabilidade)       | Calibra os critérios de aceitação de RNF-004 (performance) e dimensionamento da solução                     | Antes do início do desenvolvimento |
| PEN-002 | Formalização documentada do acordo NBS — desenvolvimento do módulo sem custo adicional           | Grupo Águia Branca (Diretoria) / NBS  | Condiciona viabilidade do projeto conforme RNF-003 e Premissa P-002; bloqueante para início do desenvolvimento | Urgente — antes da aprovação desta ERF |
| PEN-003 | Requisitos detalhados do perfil Financeiro: quais alertas, relatórios e fluxos de trabalho são necessários para prevenção e recuperação de pagamentos indevidos | Responsável pelo Financeiro — Divisão Comércio | Pode revelar novos RFs ou ajustar RF-013 e RF-019; necessário para teste de aceitação do Financeiro          | Antes do início do desenvolvimento |
| PEN-004 | Requisitos detalhados do perfil Jurídico: formato dos relatórios, campos obrigatórios para peças jurídicas, período de retenção de histórico exigido por compliance | Responsável pelo Jurídico — Divisão Comércio  | Pode revelar novos RFs ou ajustar RF-018 e RF-027; necessário para teste de aceitação do Jurídico            | Antes do início do desenvolvimento |
| PEN-005 | Definição do período e critérios da operação paralela (Fiscal Defender + Auditor Fiscal) antes do desligamento do Fiscal Defender | Sandro Siqueira + NBS                 | Necessário para planejar o cronograma de implantação e os critérios de go/no-go para desligamento do Fiscal Defender (Premissa P-004) | Antes da implantação |
| PEN-006 | Confirmação das regras tributárias específicas vigentes para as operações da Divisão Comércio que devem ser pré-configuradas no módulo no go-live | Sandro Siqueira (Contabilidade)       | Necessário para RF-021 e RF-023; sem essas regras, o módulo não pode entrar em produção com auditoria funcional | Antes da implantação |
| PEN-007 | Definição do mecanismo técnico de integração com o Power BI que a NBS irá implementar (OData, API REST, view de BD, etc.) | NBS (equipe técnica) + TI Grupo Águia Branca | Define o critério de aceitação de RF-020 e RNF-010 e as políticas de segurança aplicáveis                   | Durante o desenvolvimento |
| PEN-008 | Confirmação do período de retenção de dados de auditoria exigido pela legislação fiscal e pelas políticas internas do Grupo Águia Branca | Jurídico + Contabilidade — Divisão Comércio | Define o RNF-007 (prazo de guarda do log de auditoria); o período de 5 anos mencionado é sugestão, deve ser validado | Antes da implantação |

---

*Documento produzido por Rafael Requisito — Engenheiro de Requisitos, VMO Autônomo.*
*Versão 3.0 — 2026-05-15 — Para revisão e aprovação pelo solicitante Sandro Siqueira e pela equipe NBS.*
