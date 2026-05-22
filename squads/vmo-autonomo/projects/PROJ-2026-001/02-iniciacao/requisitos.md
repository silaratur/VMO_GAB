# Requisitos Elicitados — Inclusão de Aprovador SAP FI Lançamentos Pré-Editados
Versão: 1.0 | Data: 2026-04-03
Analista: Rafael Requisito — Engenheiro de Requisitos | VMO Autônomo Squad
Referência: DEM-2026-001 / PROJ-2026-001

---

> **Nota de Contexto:** Este documento foi produzido com base nos artefatos disponíveis: demanda coletada (Iara Inbound), demanda estruturada e parecer de qualificação (Felipe Filtro). O sponsor foi posteriormente identificado como o Diretor Financeiro, que também é o aprovador a ser incluído no fluxo. Lacunas remanescentes (L1–L12) estão documentadas na seção "Perguntas Abertas" e não bloqueiam a elicitação dos requisitos técnicos — mas devem ser resolvidas antes da parametrização em produção.

---

## TASK 1 — REQUISITOS ELICITADOS

---

## Requisitos Funcionais

### Configuração de Aprovadores

| ID | Descrição | Origem |
|----|-----------|--------|
| RF001 | O sistema deve permitir a inclusão do Diretor Financeiro como aprovador adicional no fluxo de aprovação de lançamentos pré-editados do módulo SAP FI, por meio da transação ZFI0057. | Escopo do projeto — parametrização via ZFI0057 |
| RF002 | A transação ZFI0057 deve ser utilizada como único mecanismo de configuração do novo aprovador, sem alteração de código ABAP ou customização de tabelas SAP fora do escopo parametrizável desta transação. | Escopo do projeto — "parametrização via transação ZFI0057" |
| RF003 | O novo aprovador (Diretor Financeiro) deve ser identificado por seu ID de usuário SAP (SY-UNAME) antes da parametrização, garantindo que o perfil correto seja vinculado ao fluxo de aprovação. | Lacuna L11 — aprovador não nomeado; viabilidade técnica da qualificação |
| RF004 | Após a parametrização, o fluxo de aprovação de lançamentos pré-editados deve exigir a aprovação do Diretor Financeiro de forma obrigatória, não sendo possível contornar ou ignorar essa etapa do fluxo. | Benefício esperado — governança e controle de fraude |
| RF005 | A posição do Diretor Financeiro na cadeia de aprovação (se sequencial ou paralela aos aprovadores existentes) deve ser definida e documentada antes da parametrização, com a configuração refletindo exatamente a posição aprovada. | Escopo — fluxo de aprovação; segregação de funções |

### Fluxo de Aprovação

| ID | Descrição | Origem |
|----|-----------|--------|
| RF006 | Após a inclusão do novo aprovador, os lançamentos pré-editados no SAP FI devem ser encaminhados automaticamente à caixa de trabalho do Diretor Financeiro (SBWP) para aprovação, sem necessidade de intervenção manual de nenhum usuário para disparar o workflow. | Escopo — fluxo de aprovação via SBWP |
| RF007 | O Diretor Financeiro deve receber, na sua caixa de trabalho SBWP, um item de trabalho contendo as informações do lançamento pré-editado pendente de aprovação, incluindo: número do documento, data, valor, centro de custo, conta contábil e responsável pelo lançamento. | Escopo — SBWP; controle e auditoria |
| RF008 | O Diretor Financeiro deve poder executar as ações "Aprovar" e "Rejeitar" diretamente do item de trabalho na SBWP, sem precisar acessar outras transações para concluir a ação de aprovação. | Escopo — fluxo de aprovação via SBWP |
| RF009 | Em caso de rejeição pelo Diretor Financeiro, o lançamento pré-editado deve retornar ao status anterior (pendente de correção) e o responsável pelo lançamento deve receber uma notificação automática via SBWP indicando a rejeição e, se preenchido, o motivo informado pelo aprovador. | Controle e auditoria; segregação de funções |
| RF010 | O fluxo de aprovação configurado deve manter a integridade dos aprovadores já existentes no fluxo (não deve remover ou reordenar aprovadores pré-existentes sem solicitação formal), adicionando o Diretor Financeiro de forma aditiva. | Restrição de escopo — "sem impacto em outras áreas declarado" |

### Controle e Auditoria

| ID | Descrição | Origem |
|----|-----------|--------|
| RF011 | O sistema deve registrar, no log de auditoria do SAP (tabela CDHDR/CDPOS ou equivalente para workflow FI), cada ação de aprovação ou rejeição realizada pelo Diretor Financeiro, incluindo: ID do usuário aprovador, data e hora da ação, número do documento aprovado/rejeitado e ação realizada. | Benefício — redução de risco de fraude; auditabilidade |
| RF012 | Nenhum lançamento pré-editado deve ser efetivado (postado) no SAP FI enquanto houver aprovação pendente do Diretor Financeiro no fluxo parametrizado, garantindo que a aprovação seja um pré-requisito técnico para a efetivação do documento. | Benefício — governança; controle de fraude |
| RF013 | A parametrização realizada na transação ZFI0057 deve ser registrada no log de transporte SAP (através de ordem de transporte documentada), garantindo rastreabilidade da alteração de configuração entre os ambientes de desenvolvimento, qualidade e produção. | Benefício — governança; controle de mudança em ambiente SAP produtivo |
| RF014 | O sistema deve permitir que usuários com perfil de auditoria (a ser definido pela área de controle interno) consultem o histórico de aprovações do Diretor Financeiro nos lançamentos pré-editados, sem necessidade de acesso de escrita ao fluxo ou aos documentos FI. | Benefício — auditabilidade; segregação de funções |

---

## Requisitos Não-Funcionais

| ID | Categoria | Descrição |
|----|-----------|-----------|
| RNF001 | Segurança | A parametrização da transação ZFI0057 em ambiente de produção deve ser executada exclusivamente por usuário com perfil SAP_BASIS ou perfil customizado equivalente com autorização para o objeto de autorização F_BKPF_BUK, em ambiente controlado, com registro de acesso. |
| RNF002 | Segurança | O ID de usuário SAP do Diretor Financeiro vinculado ao fluxo deve ser o ID corporativo ativo no sistema de identidades da empresa, não sendo permitido uso de usuário genérico, compartilhado ou de serviço para exercer a função de aprovador. |
| RNF003 | Auditabilidade | Toda alteração de configuração realizada na ZFI0057 para este projeto deve ser transportada via ordem de transporte SAP (TR), passando obrigatoriamente pelos ambientes DEV → QA → PRD, sem aplicação manual (hot patch) direta em produção. |
| RNF004 | Performance | O item de trabalho referente ao lançamento pré-editado deve aparecer na caixa SBWP do Diretor Financeiro em até 5 minutos após a conclusão da etapa anterior do fluxo de aprovação, medido em ambiente de produção em horário de pico (08h00–18h00, dias úteis). |
| RNF005 | Disponibilidade | A funcionalidade de aprovação via SBWP deve estar disponível durante o horário de expediente padrão (07h00–20h00, dias úteis), respeitando as janelas de manutenção SAP já estabelecidas pela equipe de Basis, sem criação de nova janela de manutenção dedicada. |
| RNF006 | Rastreabilidade | A parametrização deve ser documentada em documento técnico de configuração (DTC) contendo: print da tela ZFI0057 antes e depois da alteração, número da ordem de transporte, data de transporte para cada ambiente e nome do técnico responsável pela execução. |
| RNF007 | Compatibilidade | A configuração do novo aprovador deve ser compatível com a versão do SAP ECC ou S/4HANA em uso no ambiente produtivo da empresa, sem exigir aplicação de notas OSS (SAP Notes) adicionais além das já existentes no sistema. |
| RNF008 | Segregação de Funções | O Diretor Financeiro, na condição de aprovador, não deve acumular o perfil de criador de lançamentos pré-editados no mesmo ambiente SAP, garantindo a segregação de funções requerida pelo controle interno. Esta verificação deve ser realizada antes da ativação do fluxo em produção. |

---

## Perguntas Abertas

| ID | Questão | Para quem | Prazo |
|----|---------|-----------|-------|
| PA001 | Qual é o ID de usuário SAP (SY-UNAME) do Diretor Financeiro que deve ser incluído como aprovador no fluxo ZFI0057? (Referência: Lacuna L11) | Solicitante (Ivanilde Ribeiro Machado) / DTI | Antes do início da parametrização |
| PA002 | O Diretor Financeiro deve ser incluído como aprovador sequencial (após os aprovadores existentes) ou paralelo (simultaneamente)? Em caso de sequencial, em qual posição na cadeia? | Sponsor (Diretor Financeiro) / Solicitante | Antes do início da parametrização |
| PA003 | Quais são os aprovadores atualmente configurados no fluxo de lançamentos pré-editados na ZFI0057? (necessário para garantir que RF010 — não remoção de aprovadores — seja verificável) | DTI / Basis SAP | Antes da parametrização |
| PA004 | Existe janela de manutenção SAP já estabelecida disponível para a aplicação da ordem de transporte em produção? Qual é o calendário? | DTI / Basis SAP | Antes da execução em PRD |
| PA005 | Qual é o motivo real que originou esta demanda — controle interno, recomendação de auditoria, substituição de responsável, nova política interna ou outro? (Referência: Lacuna L3) | Solicitante (Ivanilde Ribeiro Machado) | Antes da aprovação da ERF |
| PA006 | Quais outros usuários ou áreas utilizam o fluxo de aprovação de lançamentos pré-editados atualmente? (para mapeamento de impacto e validação de RF010) | DTI / Solicitante | Antes da parametrização |
| PA007 | Existe um ambiente de QA (qualidade/homologação) disponível para testes antes da aplicação em produção? O Diretor Financeiro participará dos testes de aceite? | DTI / Sponsor | Antes da execução em QA |
| PA008 | Qual é o centro de custo a ser apontado para os custos de execução deste projeto? (Referência: Lacuna L8) | Solicitante / Área Financeira | Antes da aprovação orçamentária |
| PA009 | O Diretor Financeiro já possui acesso à SBWP configurado em seu usuário SAP? Ou será necessário solicitar abertura de perfil de acesso à caixa de trabalho? | DTI / Basis SAP | Antes da parametrização |
| PA010 | Existe prazo ou evento crítico (ex: auditoria programada, encerramento contábil, reunião de diretoria) que determine uma data-limite para a implementação? (Referência: Lacuna L6/L7) | Sponsor (Diretor Financeiro) / Solicitante | Imediato — impacta planejamento |

---
---

## TASK 2 — ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS (ERF)

---

# ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS (ERF)
Projeto: Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados
ID do Projeto: DEM-2026-001 / PROJ-2026-001
Versão: 1.0 | Data: 2026-04-03
Analista de Requisitos: Rafael Requisito — Engenheiro de Requisitos | VMO Autônomo Squad
Solicitante: Ivanilde Ribeiro Machado — VIX Manutenção
Sponsor: Diretor Financeiro (também é o aprovador a ser incluído no fluxo)

---

## 1. Requisitos Funcionais

### 1.1 Configuração de Aprovadores

| ID | Descrição | Prioridade MoSCoW | Critério de Aceitação | Origem |
|----|-----------|-------------------|----------------------|--------|
| RF001 | O sistema deve permitir a inclusão do Diretor Financeiro como aprovador adicional no fluxo de aprovação de lançamentos pré-editados do módulo SAP FI, por meio da transação ZFI0057. | **Must Have** | Dado que a parametrização foi executada na ZFI0057: ao criar um lançamento pré-editado de teste (tipo definido em PA002), o Diretor Financeiro (ID SAP confirmado via PA001) deve aparecer como aprovador pendente no fluxo, verificável pela transação SWI5 ou equivalente. O teste deve ser executado em ambiente QA antes de PRD. | Escopo do projeto |
| RF002 | A transação ZFI0057 deve ser utilizada como único mecanismo de configuração do novo aprovador, sem alteração de código ABAP ou customização de tabelas SAP fora do escopo parametrizável desta transação. | **Must Have** | O técnico SAP deve executar a configuração exclusivamente via ZFI0057. Não são permitidas modificações via SE11 (dicionário de dados), SE38 (editor ABAP) ou SE16 (acesso direto a tabelas). O relatório de transporte (TR) deve listar apenas objetos parametrizáveis da ZFI0057, sem transportar programas ABAP, tabelas Z ou objetos de desenvolvimento. | Escopo do projeto |
| RF003 | O novo aprovador (Diretor Financeiro) deve ser identificado por seu ID de usuário SAP (SY-UNAME) ativo antes da parametrização. | **Must Have** | Antes do início da parametrização em DEV, o DTI deve fornecer documentalmente o ID SAP do Diretor Financeiro. O técnico deve verificar que o usuário está ativo na SU01 (status = Ativo) e que não é um usuário genérico ou de serviço (tipo de usuário = Dialog). A parametrização só pode ser iniciada após esta verificação documentada. | Lacuna L11; viabilidade técnica |
| RF004 | Após a parametrização, o fluxo de aprovação de lançamentos pré-editados deve exigir a aprovação do Diretor Financeiro de forma obrigatória, não sendo possível contornar ou ignorar essa etapa. | **Must Have** | Em ambiente QA, criar 3 lançamentos pré-editados de teste e tentar efetivá-los (postagem) sem que o Diretor Financeiro (ou usuário de teste equivalente com mesmo perfil) aprove via SBWP. O sistema deve bloquear a efetivação e exibir mensagem de erro ou status "aguardando aprovação" enquanto a aprovação estiver pendente. Nenhum dos 3 lançamentos pode ser efetivado sem aprovação. | Benefício — governança; controle de fraude |
| RF005 | A posição do Diretor Financeiro na cadeia de aprovação (sequencial ou paralela, e em qual posição) deve ser definida e documentada antes da parametrização, com a configuração refletindo exatamente a posição aprovada. | **Must Have** | Um documento de design (ou e-mail com confirmação do Sponsor) deve definir a posição do Diretor Financeiro antes da parametrização. Após a parametrização em QA, deve-se criar um lançamento de teste e verificar que o workflow dispara os aprovadores exatamente na ordem/paralelismo documentado, sem desvio. | Escopo — fluxo de aprovação; segregação de funções |

### 1.2 Fluxo de Aprovação

| ID | Descrição | Prioridade MoSCoW | Critério de Aceitação | Origem |
|----|-----------|-------------------|----------------------|--------|
| RF006 | Após a inclusão do novo aprovador, os lançamentos pré-editados no SAP FI devem ser encaminhados automaticamente à caixa de trabalho do Diretor Financeiro (SBWP) sem intervenção manual. | **Must Have** | Em ambiente QA, criar um lançamento pré-editado e concluir a(s) etapa(s) de aprovação anteriores ao Diretor Financeiro. Em até 5 minutos (conforme RNF004), um item de trabalho deve aparecer automaticamente na SBWP do Diretor Financeiro (ou usuário de teste com mesmo perfil), sem que nenhum usuário precise executar ação manual para disparar o envio. Verificar via SWIA ou SWI5. | Escopo — fluxo via SBWP |
| RF007 | O item de trabalho na SBWP deve conter as informações do lançamento: número do documento, data, valor, centro de custo, conta contábil e responsável pelo lançamento. | **Must Have** | Em ambiente QA, criar lançamento pré-editado com campos preenchidos (número, data, valor, CC, conta contábil, responsável). Acessar o item de trabalho na SBWP do aprovador de teste e verificar que todos os 6 campos listados estão visíveis e com os valores corretos correspondentes ao lançamento criado. | Escopo — SBWP; controle e auditoria |
| RF008 | O Diretor Financeiro deve poder executar as ações "Aprovar" e "Rejeitar" diretamente do item de trabalho na SBWP, sem precisar acessar outras transações. | **Must Have** | Em ambiente QA, o usuário de teste (perfil Diretor Financeiro) deve conseguir: (a) abrir o item de trabalho na SBWP; (b) clicar em "Aprovar" e confirmar que o lançamento avança no fluxo; (c) criar outro lançamento de teste e clicar em "Rejeitar" e confirmar que o lançamento retorna ao status pendente de correção. Ambas as ações devem ser completadas sem navegação para outras transações SAP. | Escopo — fluxo via SBWP |
| RF009 | Em caso de rejeição, o lançamento deve retornar ao status pendente de correção e o responsável pelo lançamento deve receber notificação automática via SBWP com o motivo da rejeição (se preenchido). | **Should Have** | Em ambiente QA, rejeitar um lançamento de teste a partir da SBWP do aprovador, preenchendo o campo de motivo. O criador do lançamento (usuário de teste) deve receber um item de trabalho de notificação em sua SBWP em até 10 minutos após a rejeição, contendo o motivo preenchido. O lançamento deve constar com status "rejeitado" ou "pendente de correção" na consulta via FB03 ou equivalente. | Controle e auditoria |
| RF010 | O fluxo de aprovação configurado deve manter os aprovadores já existentes, adicionando o Diretor Financeiro de forma aditiva, sem remoção ou reordenação dos aprovadores pré-existentes. | **Must Have** | Antes da parametrização, o DTI deve documentar a lista atual de aprovadores configurados na ZFI0057 (print de tela ou extração). Após a parametrização em QA, verificar que todos os aprovadores pré-existentes ainda constam na configuração, na mesma posição/ordem original, e que o Diretor Financeiro foi adicionado sem substituir nenhum deles. | Restrição de escopo |

### 1.3 Controle e Auditoria

| ID | Descrição | Prioridade MoSCoW | Critério de Aceitação | Origem |
|----|-----------|-------------------|----------------------|--------|
| RF011 | O sistema deve registrar, no log de auditoria SAP, cada ação de aprovação ou rejeição do Diretor Financeiro, incluindo: ID do usuário aprovador, data e hora da ação, número do documento e ação realizada. | **Must Have** | Em ambiente QA, executar 2 aprovações e 1 rejeição com o usuário de teste (perfil Diretor Financeiro). Consultar o log de auditoria via SWI5, SWIA ou tabela equivalente e verificar que os 3 eventos estão registrados com todos os campos exigidos (ID do usuário, data/hora com precisão de segundos, número do documento e ação). | Benefício — redução de risco de fraude; auditabilidade |
| RF012 | Nenhum lançamento pré-editado deve ser efetivado no SAP FI enquanto houver aprovação pendente do Diretor Financeiro. | **Must Have** | Incluído no critério de aceitação do RF004 (testes de bloqueio de efetivação sem aprovação). Complementarmente: tentar efetivar via FB01 ou transação equivalente um lançamento pendente de aprovação do Diretor Financeiro. O sistema deve bloquear a operação com mensagem de erro identificável (código de erro ou texto). Registro do bloqueio deve ser verificável em log. | Benefício — governança; controle de fraude |
| RF013 | A parametrização realizada na ZFI0057 deve ser transportada via ordem de transporte SAP (DEV → QA → PRD), com registro documentado de cada transporte. | **Must Have** | O documento técnico de configuração (DTC) deve listar: número da TR de cada ambiente, data e hora de execução do transporte, nome do técnico que aplicou e status da aplicação (sucesso/erro com resolução). Nenhuma alteração pode constar como aplicada diretamente em PRD sem passagem pelos ambientes anteriores. Verificável via SE09/SE10. | Benefício — governança; controle de mudança |
| RF014 | Usuários com perfil de auditoria devem poder consultar o histórico de aprovações do Diretor Financeiro nos lançamentos pré-editados, sem acesso de escrita ao fluxo ou aos documentos. | **Should Have** | Um usuário com perfil de auditoria (read-only) deve conseguir consultar, via SWI5 ou relatório equivalente, o histórico de aprovações/rejeições do Diretor Financeiro em um período de datas definido, sem receber mensagem de autorização negada. O mesmo usuário não deve conseguir executar ações de aprovação, rejeição ou modificação de configuração (tentativa deve resultar em erro de autorização). | Benefício — auditabilidade; segregação de funções |

---

## 2. Requisitos Não-Funcionais

| ID | Categoria | Descrição | Prioridade MoSCoW | Critério de Aceitação |
|----|-----------|-----------|-------------------|----------------------|
| RNF001 | Segurança | A parametrização da ZFI0057 em produção deve ser executada exclusivamente por usuário com perfil Basis ou equivalente com autorização para o objeto F_BKPF_BUK, em sessão de acesso controlada e registrada. | **Must Have** | O documento técnico de configuração (DTC) deve identificar nominalmente o técnico que executou a parametrização em cada ambiente. O log SAP de acesso à ZFI0057 (SM20 ou equivalente) deve confirmar que apenas o técnico autorizado acessou e modificou a configuração. Nenhum acesso não autorizado pode constar no log. |
| RNF002 | Segurança | O ID de usuário SAP do Diretor Financeiro vinculado ao fluxo deve ser o ID corporativo ativo — não é permitido uso de usuário genérico, compartilhado ou de serviço. | **Must Have** | Antes da ativação em PRD, o DTI deve verificar via SU01 que o ID do Diretor Financeiro é do tipo "Dialog" (ou equivalente ao tipo de usuário padrão da empresa), está ativo e é de uso exclusivo do Diretor Financeiro. Esta verificação deve ser documentada no DTC com print da SU01. |
| RNF003 | Auditabilidade | Toda alteração de configuração da ZFI0057 para este projeto deve ser transportada via TR SAP (DEV → QA → PRD), sem aplicação manual (hot patch) direta em produção. | **Must Have** | Verificável via SE09/SE10: a TR deve estar com status "Transportada com sucesso" em todos os ambientes, na sequência correta (DEV antes de QA, QA antes de PRD). O log de transporte não pode registrar erros não resolvidos. |
| RNF004 | Performance | O item de trabalho do lançamento pré-editado deve aparecer na SBWP do Diretor Financeiro em até 5 minutos após a conclusão da etapa anterior do fluxo, em horário de pico (08h00–18h00, dias úteis). | **Must Have** | Em ambiente QA, executar 5 testes em horários distintos dentro do horário de pico. Medir o tempo entre a conclusão da etapa anterior (timestamp no log de workflow) e o aparecimento do item na SBWP (timestamp de criação do item de trabalho). Os 5 testes devem apresentar tempo igual ou inferior a 5 minutos. Nenhum teste pode exceder 5 minutos. |
| RNF005 | Disponibilidade | A funcionalidade de aprovação via SBWP deve estar disponível durante 07h00–20h00 em dias úteis, respeitando as janelas de manutenção SAP já estabelecidas pelo Basis. | **Should Have** | Durante o período de 30 dias úteis após a ativação em PRD, o Diretor Financeiro (ou representante designado) deve confirmar que não houve indisponibilidade da SBWP fora das janelas de manutenção planejadas. Qualquer indisponibilidade não planejada deve ser registrada como incidente e investigada pelo Basis. |
| RNF006 | Rastreabilidade | A parametrização deve ser documentada em Documento Técnico de Configuração (DTC) contendo: print da ZFI0057 antes e depois da alteração, número da TR, datas de transporte por ambiente e nome do técnico. | **Must Have** | O DTC deve ser entregue ao PMO antes da ativação em PRD, contendo todos os elementos listados. Um revisor designado pelo PMO deve validar a completude do documento antes de autorizar o transporte final para PRD. |
| RNF007 | Compatibilidade | A configuração deve ser compatível com a versão SAP em uso no ambiente produtivo, sem exigir aplicação de notas OSS adicionais além das já existentes. | **Must Have** | O técnico Basis deve verificar, antes do início da parametrização, se a versão do SAP em uso suporta a configuração pretendida na ZFI0057 sem necessidade de SAP Notes adicionais. Se notas forem necessárias, o escopo do projeto deve ser revisado e o sponsor notificado antes de prosseguir. |
| RNF008 | Segregação de Funções | O Diretor Financeiro, na função de aprovador, não deve acumular o perfil de criador de lançamentos pré-editados no mesmo ambiente SAP. | **Must Have** | Antes da ativação em PRD, o DTI deve executar relatório de conflito de segregação de funções (via GRC ou verificação manual de perfis na SU01/SUIM) para o ID do Diretor Financeiro. O relatório deve confirmar que o usuário não possui as autorizações de criação de lançamentos pré-editados combinadas com o perfil de aprovador. Resultado deve constar no DTC. |

---

## 3. Resumo de Priorização MoSCoW

| Prioridade | Qtde | Percentual | IDs |
|------------|------|------------|-----|
| Must Have | 16 | 73% | RF001, RF002, RF003, RF004, RF005, RF006, RF007, RF008, RF010, RF011, RF012, RF013, RNF001, RNF002, RNF003, RNF004, RNF006, RNF007, RNF008 |
| Should Have | 3 | 14% | RF009, RF014, RNF005 |
| Could Have | 0 | 0% | — |
| Won't Have | 0 | 0% | — |
| **Total** | **22** | **100%** | |

> **Nota de Priorização:** A concentração em Must Have (73%) é justificada pela natureza do projeto — parametrização de controle crítico em sistema SAP produtivo. Cada requisito Must Have representa uma exigência técnica ou de governança sem a qual a solução é incompleta ou insegura. Os Should Have não comprometem a funcionalidade core, mas aumentam significativamente a maturidade do controle implementado.

---

## 4. Glossário

| Termo | Definição |
|-------|-----------|
| ABAP | Advanced Business Application Programming — linguagem de programação proprietária da SAP utilizada para desenvolvimento e customização do sistema SAP. Alterações em ABAP estão fora do escopo deste projeto. |
| Aprovador | Usuário SAP com autorização para executar ações de aprovação ou rejeição em itens de trabalho de workflow, sem possuir autorização para criar ou modificar os documentos sujeitos à aprovação (exigência de segregação de funções). |
| Basis | Equipe técnica responsável pela administração, configuração de infraestrutura, segurança e transporte de configurações no ambiente SAP. Responsável pela aplicação das ordens de transporte (TR). |
| CDPOS / CDHDR | Tabelas SAP que armazenam o log de alterações de documentos (Change Document Header e Change Document Items). Utilizadas para auditoria de modificações em documentos FI. |
| DEV | Ambiente de desenvolvimento SAP — onde as parametrizações são inicialmente realizadas e testadas pelo técnico antes do transporte para QA. |
| DTC | Documento Técnico de Configuração — documento que registra a parametrização realizada, incluindo evidências (prints), número de TR, datas de transporte e responsável técnico. |
| ERF | Especificação de Requisitos Funcionais — documento formal que descreve, com critérios de aceitação verificáveis, o que um sistema deve fazer para atender às necessidades do projeto. |
| FB01 | Transação SAP utilizada para lançamento direto de documentos contábeis no módulo FI. |
| FB03 | Transação SAP utilizada para consulta (somente leitura) de documentos contábeis no módulo FI. |
| F_BKPF_BUK | Objeto de autorização SAP do módulo FI que controla o acesso a documentos contábeis por empresa. Utilizado para restringir/autorizar operações financeiras no SAP. |
| GRC | Governance, Risk and Compliance — módulo SAP (ou ferramenta equivalente) utilizado para gestão de conflitos de segregação de funções e controle de acesso. |
| Hot Patch | Aplicação de configuração ou código diretamente no ambiente de produção SAP, sem passar pelos ambientes de DEV e QA. Prática não permitida neste projeto por política de controle de mudança. |
| Lançamento Pré-Editado | Documento contábil no módulo FI do SAP que foi criado e salvo em status intermediário (não postado/efetivado), aguardando revisão e aprovação antes de produzir efeito contábil definitivo no sistema. |
| MoSCoW | Técnica de priorização de requisitos: Must Have (obrigatório), Should Have (importante, mas não crítico), Could Have (desejável se houver capacidade), Won't Have (fora do escopo desta versão). |
| OSS (SAP Note) | SAP Online Service System — repositório de notas técnicas da SAP para correção de erros ou implementação de funcionalidades. Aplicação de notas OSS requer análise técnica e está fora do escopo padrão deste projeto. |
| PMO | Project Management Office — escritório de gerenciamento de projetos responsável pela governança e controle do projeto. |
| PRD | Ambiente de produção SAP — sistema em uso real pelos usuários finais. Alterações em PRD somente podem ocorrer após validação em DEV e QA. |
| QA | Ambiente de qualidade/homologação SAP — onde as configurações transportadas de DEV são testadas e validadas pelos usuários antes de serem aplicadas em produção. |
| SBWP | SAP Business Workplace — caixa de trabalho do usuário SAP onde são recebidos e processados itens de workflow, notificações e tarefas pendentes de aprovação. Acesso pela transação SBWP. |
| SE09 / SE10 | Transações SAP para gerenciamento de ordens de transporte (Workbench Organizer e Transport Organizer). Utilizadas para verificar o status e histórico das TRs. |
| SE11 | Transação SAP para manutenção do dicionário de dados (tabelas, estruturas, tipos de dados). Modificações via SE11 estão fora do escopo deste projeto. |
| SE38 | Transação SAP para edição e execução de programas ABAP. Modificações via SE38 estão fora do escopo deste projeto. |
| SE16 | Transação SAP para acesso direto a tabelas do banco de dados (visualização e, em alguns casos, edição). Modificações diretas em tabelas via SE16 estão fora do escopo deste projeto. |
| Segregação de Funções (SoD) | Princípio de controle interno que determina que atividades incompatíveis (ex.: criar e aprovar o mesmo documento) não devem ser executadas pelo mesmo usuário, reduzindo o risco de fraude ou erro não detectado. |
| SM20 | Transação SAP para leitura do log de auditoria de segurança (Security Audit Log). Utilizada para verificar acessos e ações de usuários em transações sensíveis. |
| SU01 | Transação SAP para manutenção de usuários — criação, alteração, bloqueio e consulta de usuários e seus perfis de acesso. |
| SUIM | SAP User Information System — ferramenta para análise de perfis, autorizações e usuários no SAP. Utilizada para verificar conflitos de segregação de funções. |
| SWI5 | Transação SAP para análise de workitems (itens de trabalho) de workflow — utilizada para consultar histórico de aprovações, status de tarefas e logs de workflow. |
| SWIA | Transação SAP para execução e análise de itens de trabalho de workflow pelo administrador. Utilizada para monitoramento e diagnóstico do fluxo de aprovação. |
| SY-UNAME | Campo de sistema SAP que armazena o ID do usuário atualmente logado. Utilizado como identificador único do usuário no ambiente SAP. |
| TR (Transport Request) | Ordem de Transporte SAP — pacote que contém configurações, desenvolvimentos ou parametrizações a serem migrados entre os ambientes DEV, QA e PRD de forma controlada e rastreável. |
| VIX Manutenção | Área da empresa solicitante desta demanda. Responsável pelo processo que originou a necessidade de incluir um aprovador adicional no fluxo de lançamentos pré-editados. |
| VMO | Value Management Office — escritório de gestão de valor responsável pela governança, priorização e acompanhamento de demandas e projetos de transformação digital na empresa. |
| ZFI0057 | Transação SAP customizada (prefixo Z indica desenvolvimento/customização cliente) utilizada para configurar o padrão de aprovadores no fluxo de aprovação de lançamentos pré-editados no módulo FI. |

---

## 5. Perguntas Abertas — Impacto nos Requisitos

| ID | Questão | Requisitos Impactados | Responsável | Prazo |
|----|---------|----------------------|-------------|-------|
| PA001 | Qual o ID SAP (SY-UNAME) do Diretor Financeiro? | RF001, RF003, RF004, RF006, RF007, RF008, RNF002, RNF008 | Solicitante / DTI | Antes da parametrização |
| PA002 | Posição do Diretor Financeiro no fluxo (sequencial/paralelo, em qual posição)? | RF005, RF006, RF010 | Sponsor (Diretor Financeiro) | Antes da parametrização |
| PA003 | Lista atual de aprovadores configurados na ZFI0057? | RF010 | DTI / Basis | Antes da parametrização |
| PA004 | Janela de manutenção disponível para transporte em PRD? | RNF003, RNF005 | DTI / Basis | Antes da execução em PRD |
| PA007 | Ambiente QA disponível? Diretor Financeiro participará dos testes? | RF004, RF006, RF007, RF008, RF011, RNF004 | DTI / Sponsor | Antes dos testes |
| PA009 | Diretor Financeiro já possui acesso à SBWP configurado? | RF006, RF007, RF008 | DTI / Basis | Antes da parametrização |
| PA010 | Existe prazo ou evento crítico que determine data-limite de implementação? | Planejamento geral do projeto | Sponsor / Solicitante | Imediato |

---

## 6. Aprovação

| Papel | Nome | Assinatura | Data |
|-------|------|------------|------|
| Analista de Requisitos | Rafael Requisito (VMO Squad) | _________________ | 2026-04-03 |
| Solicitante | Ivanilde Ribeiro Machado (VIX Manutenção) | _________________ | __________ |
| Sponsor | Diretor Financeiro | _________________ | __________ |
| Responsável DTI | ________________________ | _________________ | __________ |
| PMO | ________________________ | _________________ | __________ |

---

> **Condições para início da parametrização:** Este documento está aprovado para validação com os stakeholders, mas a parametrização em qualquer ambiente SAP (DEV, QA ou PRD) não deve ser iniciada antes que as seguintes perguntas abertas sejam respondidas e documentadas: PA001 (ID SAP do aprovador), PA002 (posição no fluxo), PA003 (lista de aprovadores atuais) e PA007 (confirmação do ambiente QA). As demais perguntas abertas (PA004, PA009, PA010) devem ser resolvidas antes da execução em PRD.

---

*Documento gerado por Rafael Requisito — Engenheiro de Requisitos | VMO Autônomo Squad*
*Versão 1.0 — 2026-04-03 — Status: Aguardando validação com stakeholders*
*Referência: DEM-2026-001 / PROJ-2026-001*
