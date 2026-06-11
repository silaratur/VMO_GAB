# ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS (ERF)
Projeto: Ajustes nos Monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 — SAP ECC Módulo MM
ID: PROJ-2026-008 (Demanda DEM-2026-008)
Versão: 1.0 | Data: 2026-06-10
Analista: Rafael Requisito (VMO Autônomo)

---

## 0. Notas de Leitura

- Esta ERF cobre os 15 itens de escopo aprovados na qualificação (`01-qualificacao/qualificacao-aprovada.md`) e
  consolidados no TAP/PM Canvas/Plano Geral (`02-iniciacao/documentacao-base.md`), organizados nas 3 ondas de
  priorização já definidas (Onda 1: itens 2,3,4,6,9,11,15; Onda 2: itens 1,8,10,12; Onda 3: itens 5,7,13,14).
- Itens 13 e 14 foram desmembrados em mais de um RF cada, devido à complexidade lógica e ao status de
  Condição Bloqueante CB-6 (especificação funcional formal pendente, prazo 2026-06-24).
- O item 6 carrega a pendência CB-3 (destino exato da coluna "Data de lançamento": GSI03, GSI04 ou ambos) —
  registrado como requisito condicional, sem definição arbitrária do destino.
- Todos os requisitos usam terminologia precisa e critérios mensuráveis, evitando termos vagos
  ("rápido", "fácil", "eficiente", "robusto", "conforme necessário") sem definição quantitativa.

---

## 1. Requisitos Funcionais

### 1.1 GSI02 — Requisição de Compra / Imobilizado (Itens 1, 2, 3, 4, 11, 15)

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|------------------------|--------|
| RF001 | O sistema deve disponibilizar um novo campo "Classificação" na transação ME53N (visualização da requisição de compra), com lista de valores predefinida pelo SQUAD PM/MM em conjunto com Tatiane Dias de Moraes, para que o usuário de Compras/Controle de Ativos classifique cada requisição no momento da criação/edição. | Must Have | Em ambiente de teste, o campo "Classificação" é exibido na tela da ME53N, aceita apenas valores da lista predefinida (rejeitando valores fora da lista com mensagem de erro) e o valor selecionado é persistido e recuperável na mesma requisição após gravação. | Item 1 — Tatiane Dias de Moraes / Jerfesson Fernandes Helmer |
| RF002 | O sistema deve tornar o preenchimento do campo "Classificação" obrigatório nas requisições de compra criadas/alteradas via transação ZMMTR002, impedindo a gravação da requisição enquanto o campo estiver em branco. | Must Have | Teste com requisição via ZMMTR002 sem valor em "Classificação": sistema bloqueia a gravação e exibe mensagem de erro identificando o campo obrigatório; com valor preenchido, a gravação é concluída com sucesso em 100% dos casos testados (mínimo 5 requisições de teste). | Item 1 — Tatiane Dias de Moraes |
| RF003 | O sistema deve exibir o campo "Classificação" como coluna no monitor ZMMR_GSI02, com os mesmos valores gravados na requisição de origem (ME53N/ZMMTR002), permitindo ordenação e filtro por essa coluna. | Must Have | A coluna "Classificação" aparece no layout padrão do GSI02; para uma amostra de 10 requisições com valores distintos de "Classificação", o valor exibido no GSI02 corresponde exatamente ao gravado na ME53N; filtro por valor de "Classificação" retorna apenas as requisições com aquele valor. | Item 1 — Tatiane Dias de Moraes |
| RF004 | O sistema deve exibir o campo "Vencimento NF" (já existente na ME53N) como coluna no monitor ZMMR_GSI02, refletindo o valor atual do campo de origem sem necessidade de atualização manual no monitor. | Must Have | A coluna "Vencimento NF" está visível no layout padrão do GSI02; para uma amostra de 10 requisições, o valor exibido é idêntico ao campo "Vencimento NF" da ME53N na mesma requisição; alteração do campo na ME53N reflete no GSI02 na próxima atualização/refresh do monitor (sem necessidade de reprocessamento manual). | Item 2 — Tatiane Dias de Moraes / João Henrique |
| RF005 | O sistema deve exibir o campo "CR" (Centro de Custo, já existente na ME53N) como coluna no monitor ZMMR_GSI02, com a mesma lógica de espelhamento e filtro do RF004. | Must Have | A coluna "CR" está visível no layout padrão do GSI02; para uma amostra de 10 requisições, o valor exibido é idêntico ao campo "CR" da ME53N na mesma requisição; o monitor permite filtrar requisições por valor de "CR". | Item 3 — Tatiane Dias de Moraes / João Henrique |
| RF006 | O sistema deve exibir o campo "Data Liberação/aprovação" da requisição de compra (data em que a requisição foi liberada/aprovada no fluxo de aprovação SAP) como coluna no monitor ZMMR_GSI02. | Should Have | A coluna "Data Liberação/aprovação" está visível no layout padrão do GSI02; para uma amostra de 10 requisições já liberadas, a data exibida corresponde à data de liberação registrada no histórico de status de liberação da requisição (transação ME54N/ME53N); requisições ainda não liberadas exibem o campo em branco ou com indicador "Pendente". | Item 4 — Tatiane Dias de Moraes |
| RF007 | O sistema deve exibir o campo "Tipo de Veículo" (associado à requisição/pedido de compra) como coluna no monitor ZMMR_GSI02, permitindo filtro e ordenação por esse campo. | Must Have | A coluna "Tipo de Veículo" está visível no layout padrão do GSI02; para uma amostra de 10 requisições/pedidos com "Tipo de Veículo" preenchido, o valor exibido corresponde ao valor de origem; o monitor permite filtrar por "Tipo de Veículo". | Item 11 — Tatiane Dias de Moraes (relacionado ao Item 10 / RF014-RF015) |
| RF008 | O sistema deve permitir que, ao registrar um cadastro de imobilizado de frota via monitor ZMMR_GSI02, o usuário informe o campo "Grupo deprec." (Grupo de Depreciação, campo já existente na transação AS01), gravando esse valor no cadastro de imobilizado criado na AS01. | Must Have | No fluxo de criação de imobilizado via GSI02, o campo "Grupo deprec." é exibido e editável; ao concluir a criação, o ativo correspondente na AS02/AS03 (consulta) exibe o mesmo valor de "Grupo deprec." informado no GSI02, em 100% de uma amostra de 5 imobilizados criados em teste. | Item 15 — Tatiane Dias de Moraes / Jerfesson Fernandes Helmer |

### 1.2 GSI03 — Acompanhamento de Pedido / Legalização / MIRO (Itens 5, 6, 8, 12, 13, 14)

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|------------------------|--------|
| RF009 | O sistema deve detectar automaticamente, na aba "Histórico do pedido" da transação ME22N, lançamentos de fatura (MIRO) realizados fora do fluxo padrão do monitor (ex.: lançados via processo GRC), capturando o número do documento MIRO gerado. | Must Have | Em cenário de teste no qual uma fatura MIRO é lançada para um pedido via processo GRC fora do monitor, o sistema identifica o novo registro de fatura na aba "Histórico do pedido" da ME22N do respectivo pedido em até 1 ciclo de atualização (job batch) do monitor, sem intervenção manual. | Item 5 — Tatiane Dias de Moraes / Jerfesson Fernandes Helmer |
| RF010 | Ao detectar uma MIRO lançada fora do fluxo (RF009), o sistema deve carregar automaticamente o número do documento MIRO no campo correspondente do monitor ZMMR_GSI03 e marcar como concluída a etapa do fluxo associada ao recebimento da fatura. | Must Have | Para o cenário de teste do RF009, após o ciclo de atualização do monitor, o GSI03 exibe: (a) o número do documento MIRO no campo "Nº MIRO" do pedido correspondente, e (b) a etapa de "Fatura Recebida" (ou etapa equivalente do fluxo) marcada como concluída, sem que o usuário tenha realizado qualquer lançamento manual no monitor. | Item 5 — Tatiane Dias de Moraes / Jerfesson Fernandes Helmer |
| RF011 | [CONDICIONAL — pendente CB-3] O sistema deve exibir o campo "Data de lançamento" da fatura (MIRO, data de registro contábil do documento) como coluna no monitor ZMMR_GSI03 e/ou ZMMR_GSI04, conforme definição a ser confirmada pelo solicitante (Tatiane Dias de Moraes / João Henrique). | Should Have | A ser definido após resolução de CB-3. Critério provisório: a coluna "Data de lançamento" estará visível no(s) monitor(es) confirmado(s) (GSI03, GSI04 ou ambos), exibindo a data de lançamento contábil (campo BUDAT do documento MIRO/BKPF) idêntica à exibida na transação MIR4/FB03 do mesmo documento, para uma amostra de 10 faturas. | Item 6 — Tatiane Dias de Moraes / João Henrique — **PENDENTE: CB-3 (prazo 2026-06-13)**. Não desenvolver até confirmação do destino exato (GSI03, GSI04 ou ambos) e esclarecimento da relação com ZMMR_GSI01. |
| RF012 | O sistema deve marcar automaticamente como concluída a etapa de "Legalização" no monitor ZMMR_GSI03 para registros de máquinas e implementos agrícolas/industriais que, por sua natureza, não são sujeitos a emplacamento (ex.: não possuem categoria de veículo emplacável conforme tabela de tipos de veículo do RF007/RF014). | Must Have | Para uma amostra de 5 registros de máquinas/implementos classificados como "não emplacáveis" no campo "Tipo de Veículo", a etapa "Legalização" no GSI03 é marcada automaticamente como "Concluída" no momento em que o registro é criado/sincronizado, sem exigir ação manual do usuário; registros de "Tipo de Veículo" emplacável continuam exigindo conclusão manual da etapa. | Item 8 — Tatiane Dias de Moraes / Jerfesson Fernandes Helmer |
| RF013 | O sistema deve permitir que o usuário corrija manualmente o conteúdo de um XML de nota fiscal incorreto associado a um registro do monitor ZMMR_GSI03, desde que o registro atenda simultaneamente às condições: (a) o equipamento/PM relacionado ainda não foi legalizado, e (b) o cadastro de imobilizado (AS02) ainda não foi criado para esse registro. | Must Have | Em teste com registro que atende (a) e (b): o botão/ação "Corrigir XML" fica habilitado e permite a edição/substituição do XML, com gravação confirmada. Em teste com registro em que (a) ou (b) não são atendidos (legalização concluída ou imobilizado já criado): a ação "Corrigir XML" fica desabilitada e o sistema exibe mensagem informando o motivo do bloqueio, em 100% dos casos testados (mínimo 4 cenários: ambas condições atendidas, apenas (a), apenas (b), nenhuma atendida). | Item 12 — Tatiane Dias de Moraes / Jerfesson Fernandes Helmer |
| RF014 | O sistema deve permitir que o usuário altere o campo "Tipo de Veículo" de um pedido de compra após a criação do pedido (alteração não permitida atualmente conforme regra de negócio vigente da V1), registrando a alteração com usuário e data/hora (log de auditoria). | Must Have | Em teste, um pedido com "Tipo de Veículo" = X é alterado para "Tipo de Veículo" = Y após a criação do pedido pelo usuário autorizado; a alteração é gravada com sucesso e o log de auditoria registra usuário, data/hora, valor anterior (X) e novo valor (Y) para 100% das alterações testadas (mínimo 5 alterações). | Item 10 — Tatiane Dias de Moraes (mudança de regra de negócio existente, validar com Jerfesson Fernandes Helmer) |
| RF015 | Quando o campo "Tipo de Veículo" de um pedido for alterado conforme RF014, o sistema deve propagar automaticamente o novo valor para os campos correspondentes nos monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04, sem necessidade de atualização manual em cada monitor. | Must Have | Para o mesmo cenário de teste do RF014, após a alteração do "Tipo de Veículo" do pedido, os três monitores (GSI02, GSI03, GSI04) exibem o novo valor (Y) para o registro correspondente em até 1 ciclo de atualização do monitor, em 100% dos casos testados. | Item 10 — Tatiane Dias de Moraes |
| RF016 | [CB-6 — especificação funcional formal pendente] O sistema deve, ao identificar o estorno de um documento de fatura (MIRO) associado a um pedido controlado pelo monitor ZMMR_GSI03/GSI04, excluir o vínculo entre a fatura estornada e o registro do monitor, atualizando o campo de status do registro para refletir que a fatura foi estornada, e registrando essa ocorrência em log de auditoria (data, hora, usuário, documento estornado, status anterior e novo). | Must Have | A ser detalhado na especificação funcional formal do item 13 (CB-6, prazo 2026-06-24). Critério provisório de alto nível: em cenário de teste com estorno de uma MIRO vinculada a um registro do GSI03/GSI04, após o estorno: (a) o vínculo da fatura original é removido/desativado no registro do monitor, (b) o campo "Status" do registro passa para um valor que indique "Fatura Estornada" (nomenclatura a definir na especificação formal), e (c) o log de auditoria contém os 5 campos exigidos para 100% dos estornos testados (mínimo 3 cenários). | Item 13 — Jerfesson Fernandes Helmer / Nubia Carla Freitas Santos Souza — **PENDENTE: CB-6 (prazo 2026-06-24)**. Não iniciar desenvolvimento antes da especificação funcional formal e plano de testes dedicados, dado o risco fiscal/contábil identificado na qualificação. |
| RF017 | [CB-6 — especificação funcional formal pendente] Após o estorno de uma MIRO conforme RF016, o sistema deve permitir o lançamento de uma nova MIRO para o mesmo pedido, vinculando o novo documento ao registro do monitor e restaurando o status da etapa de fatura para "Pendente" ou equivalente, conforme definido na especificação funcional formal. | Must Have | A ser detalhado na especificação funcional formal do item 13 (CB-6). Critério provisório: para o mesmo pedido do cenário de teste do RF016, após o estorno, é possível lançar uma nova MIRO; o novo documento é vinculado ao registro do monitor e o status da etapa de fatura é atualizado de acordo com a regra a ser definida na especificação formal, em 100% dos cenários testados. | Item 13 — Jerfesson Fernandes Helmer — **PENDENTE: CB-6 (prazo 2026-06-24)** |
| RF018 | [CB-6 — especificação funcional formal pendente] O sistema deve impedir o estorno do pedido de compra associado a um registro do monitor enquanto existir uma MIRO ativa (não estornada) vinculada a esse pedido, exibindo mensagem de bloqueio que identifique o documento MIRO ativo impeditivo. | Must Have | A ser detalhado na especificação funcional formal do item 13 (CB-6), incluindo cenários de borda (estorno parcial, MIRO já paga). Critério provisório: em teste de tentativa de estorno de pedido com MIRO ativa vinculada, o sistema bloqueia a operação e exibe mensagem identificando o número do documento MIRO ativo, em 100% dos casos testados (mínimo 3 cenários, incluindo MIRO parcialmente paga). | Item 13 — Jerfesson Fernandes Helmer / Nubia Carla Freitas Santos Souza — **PENDENTE: CB-6 (prazo 2026-06-24)**. Cenários de borda (estorno parcial, MIRO já paga) a serem definidos na especificação formal antes da implementação. |
| RF019 | [CB-6 — especificação funcional formal pendente] O sistema deve alterar o comportamento do campo "DT. Básica" (aba Pagamentos da MIRO, transação MIR4/FB03) associado aos pedidos controlados pelo GSI03, de modo que esse campo deixe de ser preenchido automaticamente no momento da criação do pedido de compra (ME21N/ME51N), passando a ser preenchido somente no momento do lançamento da fatura (MIRO), com o valor do campo "Data da Fatura" informado nesse lançamento. | Must Have | A ser detalhado na especificação funcional formal do item 14 (CB-6, prazo 2026-06-24). Critério provisório: em teste de criação de um pedido novo controlado pelo GSI03, o campo "DT. Básica" permanece em branco até o momento do lançamento da MIRO; após o lançamento da MIRO com "Data da Fatura" = D, o campo "DT. Básica" do documento é igual a D, em 100% de uma amostra de 5 pedidos testados. | Item 14 — Jerfesson Fernandes Helmer / Nubia Carla Freitas Santos Souza — **PENDENTE: CB-6 (prazo 2026-06-24)**. Risco de impacto em outros usuários da MIRO fora do fluxo do GSI03 (ver qualificação, Critério 8) — escopo de aplicação da regra (todos os pedidos vs. apenas os controlados pelo monitor) deve ser definido na especificação formal. |
| RF020 | [CB-6 — especificação funcional formal pendente] O sistema deve calcular automaticamente o campo "Vencimento Em" (aba Pagamentos da MIRO) como o resultado da soma entre o campo "DT. Básica" (conforme RF019) e o prazo definido na "Condição de Pagamento" associada ao fornecedor/pedido, atualizando o cálculo sempre que "DT. Básica" ou "Condição de Pagamento" forem alterados antes da gravação do documento. | Must Have | A ser detalhado na especificação funcional formal do item 14 (CB-6). Critério provisório: para uma amostra de 5 lançamentos de MIRO de teste com "DT. Básica" = D e "Condição de Pagamento" com prazo de N dias, o campo "Vencimento Em" calculado pelo sistema é igual a D + N dias em 100% dos casos; alteração de "Condição de Pagamento" antes da gravação recalcula "Vencimento Em" automaticamente. | Item 14 — Jerfesson Fernandes Helmer — **PENDENTE: CB-6 (prazo 2026-06-24)** |

### 1.3 GSI04 — Consulta / Imobilizado / Veículo (Itens 7, 9)

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|------------------------|--------|
| RF021 | O sistema deve incluir o campo "Nº de Requisição de Compra" como parâmetro de busca/filtro disponível na tela de seleção do monitor ZMMR_GSI04, retornando os registros vinculados à requisição informada. | Must Have | Na tela de seleção do GSI04, o campo "Nº de Requisição de Compra" está disponível para entrada; ao informar um número de requisição existente vinculado a registros do GSI04, o sistema retorna todos os registros associados àquela requisição (mínimo 3 requisições de teste com 1+ registro vinculado cada); ao informar um número inexistente, o sistema retorna lista vazia sem erro. | Item 9 — Tatiane Dias de Moraes / João Henrique |
| RF022 | O sistema deve, ao identificar o cadastro/atualização de um veículo ou equipamento na transação de Plant Maintenance (PM), atualizar automaticamente o campo "Placa do veículo" no cadastro de imobilizado correspondente na transação AS02, sem necessidade de digitação manual da placa pelo usuário de Controle de Ativos. | Must Have | Em teste, ao cadastrar/atualizar um equipamento em PM com placa informada, o campo "Placa do veículo" do imobilizado vinculado na AS02 é atualizado automaticamente com o mesmo valor em até 1 ciclo de sincronização, para 100% de uma amostra de 5 equipamentos testados; equipamentos sem placa (não emplacáveis) não geram erro nem sobrescrevem o campo com valor inválido. | Item 7 — Tatiane Dias de Moraes / Jerfesson Fernandes Helmer |

---

## 2. Requisitos Não-Funcionais

| ID | Categoria | Descrição | Prioridade | Critério de Aceitação |
|----|-----------|-----------|------------|------------------------|
| RNF001 | Performance | Os monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04, após a inclusão das novas colunas/campos (RF003-RF008, RF011, RF021), devem manter o tempo de carregamento da listagem em até 5 segundos para uma seleção de até 500 registros, em condições normais de carga do servidor SAP de produção (até 50 usuários simultâneos no sistema). | Must Have | Teste de carga em ambiente de homologação (QAS) com seleção de 500 registros e 50 usuários simultâneos ativos no sistema: tempo de exibição da listagem completa ≤ 5,0 segundos no percentil 95 das execuções (mínimo 10 execuções). |
| RNF002 | Performance | As automações em background (detecção de MIRO via GRC — RF009/RF010; sincronização PM→AS02 — RF022; propagação de "Tipo de Veículo" — RF015; marcação automática de Legalização — RF012) devem ser executadas em job(s) batch com periodicidade máxima de 1 hora, refletindo as alterações nos monitores em até 1 ciclo de execução do job. | Must Have | Verificação do agendamento (transação SM37) confirma job(s) configurados com periodicidade ≤ 1 hora; em teste de ponta a ponta, uma alteração de origem (lançamento MIRO via GRC, cadastro PM, alteração de Tipo de Veículo, registro não emplacável) é refletida no(s) monitor(es) correspondente(s) em até 1 execução do job após a alteração, em 100% de uma amostra de 5 cenários por automação. |
| RNF003 | Segurança | O acesso às novas funcionalidades de edição/exclusão introduzidas (correção de XML — RF013; alteração de Tipo de Veículo pós-pedido — RF014; estorno de fatura/pedido — RF016-RF018) deve ser restrito por autorização SAP (objeto de autorização dedicado ou papel/role específico), de modo que apenas usuários com o papel "Controle de Ativos — Editor GSI" (ou equivalente a definir) possam executar essas ações. | Must Have | Teste de autorização: usuário sem o papel "Controle de Ativos — Editor GSI" tenta executar correção de XML, alteração de Tipo de Veículo pós-pedido ou estorno via monitor e recebe mensagem de bloqueio por falta de autorização (transação SU53 confirma o objeto de autorização verificado), em 100% de 3 cenários testados; usuário com o papel consegue executar a ação normalmente. |
| RNF004 | Segurança | Toda alteração realizada pelas novas funcionalidades de edição/exclusão (RF013, RF014, RF016-RF018, RF019-RF020) deve gerar registro de log de auditoria contendo, no mínimo: usuário, data/hora (timestamp completo), identificação do registro alterado, valor anterior e valor novo. | Must Have | Para cada uma das funcionalidades RF013, RF014, RF016, RF017, RF018, em pelo menos 1 execução de teste, o log de auditoria gerado contém os 5 campos obrigatórios (usuário, timestamp, identificação do registro, valor anterior, valor novo) e é consultável por usuário com perfil de auditoria/gestão (ex.: Nubia Carla Freitas Santos Souza). |
| RNF005 | Disponibilidade | Os monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 devem manter disponibilidade igual à disponibilidade padrão do ambiente produtivo SAP ECC do Grupo Águia Branca, sem degradação adicional decorrente das novas automações em background (RNF002), respeitando as janelas de manutenção já programadas para o ambiente. | Must Have | Monitoramento de 30 dias após o go-live de cada onda confirma que a disponibilidade dos monitores GSI02/03/04 permanece dentro do mesmo intervalo de disponibilidade do ambiente SAP ECC produtivo geral (sem incidentes de indisponibilidade atribuíveis às novas automações), exceto janelas de manutenção programadas e comunicadas previamente. |
| RNF006 | Disponibilidade | Em caso de falha na execução de qualquer job batch das automações (RNF002), o sistema deve registrar o erro em log de monitoramento de jobs (SM37) com identificação da automação afetada, sem interromper a disponibilidade de consulta/edição manual dos monitores GSI02/03/04. | Should Have | Em teste de simulação de falha de um dos jobs (ex.: indisponibilidade temporária de uma interface), o job registra status de erro em SM37 identificando a automação (ex.: "Sincronização PM→AS02"), e os monitores GSI02/03/04 continuam acessíveis para consulta e edição manual durante a falha. |
| RNF007 | Usabilidade | As novas colunas incluídas nos monitores (RF003-RF008, RF011, RF021) devem ser adicionadas ao layout padrão (variante de exibição padrão) dos respectivos monitores, sendo visíveis sem necessidade de configuração manual de layout pelo usuário final no primeiro acesso após o go-live de cada onda. | Must Have | Após o go-live de cada onda, um usuário sem layout personalizado previamente salvo, ao abrir o monitor correspondente (GSI02, GSI03 ou GSI04), visualiza as novas colunas daquela onda já presentes no layout exibido por padrão, sem executar nenhuma ação de configuração de variante. |
| RNF008 | Usabilidade | As mensagens de bloqueio/erro exibidas pelas novas validações (campo "Classificação" obrigatório — RF002; bloqueio de correção de XML — RF013; bloqueio de estorno de pedido com MIRO ativa — RF018) devem identificar de forma explícita o motivo do bloqueio e, quando aplicável, o campo, documento ou condição que precisa ser resolvida para liberar a ação. | Must Have | Para cada uma das 3 validações (RF002, RF013, RF018), em teste com a condição de bloqueio ativa, a mensagem exibida ao usuário identifica nominalmente o campo/documento/condição causador do bloqueio (ex.: "Campo Classificação obrigatório", "XML não pode ser alterado: equipamento já legalizado", "Pedido possui MIRO ativa nº XXXXXXXXXX — estorno bloqueado"), validado por revisão funcional com Tatiane Dias de Moraes/João Henrique. |
| RNF009 | Compatibilidade / Não-regressão | As alterações implementadas em qualquer onda não devem alterar o comportamento de funcionalidades da V1 dos monitores GSI02/03/04 que não estejam explicitamente listadas nos 15 itens de escopo deste projeto. | Must Have | Antes do go-live de cada onda, é executado um roteiro de teste de regressão cobrindo as funcionalidades-chave da V1 (a definir com Jerfesson Fernandes Helmer), com 0 (zero) defeitos de regressão classificados como críticos ou altos identificados nas funcionalidades fora do escopo dos 15 itens. |

---

## 3. Resumo de Priorização MoSCoW

### 3.1 Requisitos Funcionais

| Prioridade | Qtde | Percentual |
|------------|------|------------|
| Must Have | 19 | 86% |
| Should Have | 3 | 14% |
| Could Have | 0 | 0% |
| Won't Have | 0 | 0% |
| **Total RF** | **22** | **100%** |

### 3.2 Requisitos Não-Funcionais

| Prioridade | Qtde | Percentual |
|------------|------|------------|
| Must Have | 8 | 89% |
| Should Have | 1 | 11% |
| Could Have | 0 | 0% |
| Won't Have | 0 | 0% |
| **Total RNF** | **9** | **100%** |

### 3.3 Geral (RF + RNF)

| Prioridade | Qtde | Percentual |
|------------|------|------------|
| Must Have | 27 | 87% |
| Should Have | 4 | 13% |
| Could Have | 0 | 0% |
| Won't Have | 0 | 0% |
| **Total** | **31** | **100%** |

**Observação sobre concentração em "Must Have":** A alta proporção de Must Have reflete a natureza da
demanda — cada um dos 15 itens de escopo foi formalmente solicitado e validado pelo solicitante/especialista
na qualificação aprovada, sem itens "extras" especulativos. Os Should Have correspondem a: (a) o item 4
(RF006 — "Data Liberação/aprovação"), considerado informativo/consulta e não bloqueante para o objetivo
central de autonomia operacional; (b) o item 6 (RF011), classificado como Should Have **adicionalmente** por
estar pendente de definição (CB-3) — sua prioridade final pode ser revista para Must Have após a confirmação
do destino; e (c) RNF006 (log de falha de job), que é uma boa prática operacional mas não bloqueia a entrega
funcional dos demais itens. Nenhum requisito foi classificado como Could Have ou Won't Have, pois os 15 itens
já passaram por filtro de qualificação (50/100, aprovado com condições) — itens especulativos ou de baixo
valor não compõem este escopo fechado.

---

## 4. Tabela de Rastreabilidade

| RF/RNF | Item de Escopo Original | Onda | Stakeholder de Origem | Observações |
|--------|--------------------------|------|------------------------|-------------|
| RF001 | Item 1 — Campo "Classificação" novo na ME53N | Onda 2 | Tatiane Dias de Moraes / Jerfesson Fernandes Helmer | Lista de valores a definir em conjunto com SQUAD PM/MM |
| RF002 | Item 1 — Obrigatoriedade via ZMMTR002 | Onda 2 | Tatiane Dias de Moraes | Depende de RF001 |
| RF003 | Item 1 — Coluna "Classificação" no GSI02 | Onda 2 | Tatiane Dias de Moraes | Depende de RF001 |
| RF004 | Item 2 — Coluna "Vencimento NF" no GSI02 | Onda 1 | Tatiane Dias de Moraes / João Henrique | — |
| RF005 | Item 3 — Coluna "CR" no GSI02 | Onda 1 | Tatiane Dias de Moraes / João Henrique | — |
| RF006 | Item 4 — Coluna "Data Liberação/aprovação" no GSI02 | Onda 1 | Tatiane Dias de Moraes | Should Have — informativo |
| RF007 | Item 11 — Coluna "Tipo de Veículo" no GSI02 | Onda 1 | Tatiane Dias de Moraes | Relacionado a RF014/RF015 (Item 10) |
| RF008 | Item 15 — Campo "Grupo deprec." no cadastro de imobilizado via GSI02 | Onda 1 | Tatiane Dias de Moraes / Jerfesson Fernandes Helmer | — |
| RF009 | Item 5 — Detecção automática de MIRO via GRC na ME22N (parte 1: detecção) | Onda 3 | Tatiane Dias de Moraes / Jerfesson Fernandes Helmer | Risco organizacional ALTO (qualificação) |
| RF010 | Item 5 — Carga de nº MIRO + marcação de etapa no GSI03 (parte 2: ação) | Onda 3 | Tatiane Dias de Moraes / Jerfesson Fernandes Helmer | Depende de RF009 |
| RF011 | Item 6 — Coluna "Data de lançamento" da MIRO no GSI03 e/ou GSI04 | Onda 1 | Tatiane Dias de Moraes / João Henrique | **PENDENTE CB-3** — destino não definido; também relação com ZMMR_GSI01 a esclarecer |
| RF012 | Item 8 — Marcação automática de Legalização concluída (não emplacados) | Onda 2 | Tatiane Dias de Moraes / Jerfesson Fernandes Helmer | Depende de RF007/RF014 (categoria de Tipo de Veículo) |
| RF013 | Item 12 — Alteração de XML incorreto no GSI03 (condicionado) | Onda 2 | Tatiane Dias de Moraes / Jerfesson Fernandes Helmer | — |
| RF014 | Item 10 — Alteração de "Tipo de Veículo" pós-pedido (parte 1: permissão) | Onda 2 | Tatiane Dias de Moraes | Mudança de regra de negócio existente — validar com Jerfesson |
| RF015 | Item 10 — Propagação para GSI02/03/04 (parte 2: sincronização) | Onda 2 | Tatiane Dias de Moraes | Depende de RF014 |
| RF016 | Item 13 — Estorno: exclusão de vínculo + atualização de status/log (parte 1) | Onda 3 | Jerfesson Fernandes Helmer / Nubia Carla Freitas Santos Souza | **PENDENTE CB-6** — especificação funcional formal e plano de testes obrigatórios antes do desenvolvimento |
| RF017 | Item 13 — Estorno: permitir nova MIRO após estorno (parte 2) | Onda 3 | Jerfesson Fernandes Helmer | **PENDENTE CB-6** |
| RF018 | Item 13 — Estorno: regra de ordem fatura→pedido (parte 3: bloqueio de estorno de pedido com MIRO ativa) | Onda 3 | Jerfesson Fernandes Helmer / Nubia Carla Freitas Santos Souza | **PENDENTE CB-6** — inclui cenários de borda (estorno parcial, MIRO já paga) |
| RF019 | Item 14 — "DT. Básica" não auto-preenche; preenche com "Data da Fatura" | Onda 3 | Jerfesson Fernandes Helmer / Nubia Carla Freitas Santos Souza | **PENDENTE CB-6** — risco organizacional sobre outros usuários da MIRO (Critério 8 da qualificação) |
| RF020 | Item 14 — "Vencimento Em" = "DT. Básica" + "Condição de Pagamento" | Onda 3 | Jerfesson Fernandes Helmer | **PENDENTE CB-6** — depende de RF019 |
| RF021 | Item 9 — "Nº de Requisição de Compra" como parâmetro de busca no GSI04 | Onda 1 | Tatiane Dias de Moraes / João Henrique | — |
| RF022 | Item 7 — Cadastro de veículo/equipamento em PM atualiza "Placa do veículo" no AS02 | Onda 3 | Tatiane Dias de Moraes / Jerfesson Fernandes Helmer | Risco técnico moderado-alto (qualificação, Critério 2) |
| RNF001 | Não-funcional — Performance dos monitores | Transversal (todas as ondas) | SQUAD PM/MM / Usuários finais (Contabilidade/Controle de Ativos) | Aplica-se a RF003-RF008, RF011, RF021 |
| RNF002 | Não-funcional — Performance das automações em background | Onda 2 e 3 | SQUAD PM/MM | Aplica-se a RF009/RF010, RF012, RF015, RF022 |
| RNF003 | Não-funcional — Segurança / autorização | Onda 2 e 3 | Nubia Carla Freitas Santos Souza (Gerente Contábil) | Aplica-se a RF013, RF014, RF016-RF018 |
| RNF004 | Não-funcional — Segurança / log de auditoria | Onda 2 e 3 | Nubia Carla Freitas Santos Souza | Aplica-se a RF013, RF014, RF016-RF020 |
| RNF005 | Não-funcional — Disponibilidade dos monitores | Transversal | SQUAD PM/MM / Usuários finais | — |
| RNF006 | Não-funcional — Disponibilidade / monitoramento de jobs | Onda 2 e 3 | SQUAD PM/MM | — |
| RNF007 | Não-funcional — Usabilidade / layout padrão | Onda 1, 2 e 3 | Tatiane Dias de Moraes / João Henrique | — |
| RNF008 | Não-funcional — Usabilidade / clareza de mensagens de erro | Onda 2 e 3 | Tatiane Dias de Moraes / João Henrique | — |
| RNF009 | Não-funcional — Compatibilidade / não-regressão da V1 | Transversal | Jerfesson Fernandes Helmer | — |

---

## 5. Glossário

| Termo | Definição |
|-------|-----------|
| GSI02 (ZMMR_GSI02) | Monitor SAP customizado (V1) que acompanha requisições de compra e o processo de criação de imobilizado de frota, módulo MM. |
| GSI03 (ZMMR_GSI03) | Monitor SAP customizado (V1) que acompanha o status do pedido de compra, recebimento de fatura (MIRO), legalização de veículos/equipamentos e XML de notas fiscais. |
| GSI04 (ZMMR_GSI04) | Monitor SAP customizado (V1) usado para consulta de imobilizados/veículos e vínculos entre requisição, pedido e fatura. |
| ZMMR_GSI01 | Monitor SAP customizado citado no cabeçalho do chamado original, sem item de escopo correspondente nos 15 itens — relação com o item 6 a esclarecer (CB-3). Não faz parte do escopo desta ERF além da menção no RF011. |
| MIRO | Transação SAP para lançamento (entrada) de fatura/nota fiscal vinculada a um pedido de compra (Verificação de Fatura Logística). |
| MIR4 / FB03 | Transações SAP de exibição/consulta de documento de fatura (MIRO) já lançado. |
| GRC | Governance, Risk and Compliance — sistema/processo de aprovação que, neste contexto, pode originar lançamentos de MIRO "fora do fluxo" do monitor GSI03 (item 5). |
| AS01 / AS02 / AS03 | Transações SAP de criação (AS01), alteração (AS02) e exibição (AS03) de cadastro de imobilizado (Asset Master Data), módulo Asset Accounting (AA/FI-AA). |
| PM (Plant Maintenance) | Módulo SAP de Manutenção de Planta, usado para cadastro de veículos/equipamentos como objetos técnicos. |
| ME21N / ME22N / ME51N / ME52N | Transações SAP do módulo MM: ME51N (criar requisição de compra), ME52N (alterar requisição de compra), ME21N (criar pedido de compra), ME22N (alterar pedido de compra). |
| ME53N / ME54N | Transações SAP de exibição (ME53N) e liberação/aprovação (ME54N) de requisição de compra. |
| ZMMTR002 | Transação customizada SAP usada para criação/alteração de requisições de compra com regras específicas do Grupo Águia Branca (módulo MM). |
| "Classificação" (campo) | Novo campo a ser criado na requisição de compra (ME53N), com lista de valores a definir, usado para categorizar a requisição (item 1). |
| "Vencimento NF" (campo) | Campo já existente na ME53N que indica a data de vencimento da nota fiscal associada à requisição (item 2). |
| "CR" (campo) | Campo já existente na ME53N que indica o Centro de Custo (Cost Center) associado à requisição (item 3). |
| "Data Liberação/aprovação" (campo) | Data em que a requisição de compra foi liberada/aprovada no fluxo de liberação SAP (transação ME54N), referenciada no item 4. |
| "Tipo de Veículo" (campo) | Campo associado ao pedido de compra/requisição que classifica o tipo de veículo (ex.: leve, pesado, máquina/implemento não emplacável), usado nos itens 10 e 11. |
| "Grupo deprec." (campo) | Campo "Grupo de Depreciação" já existente na transação AS01, usado para definir a regra de depreciação contábil do imobilizado (item 15). |
| "Placa do veículo" (campo) | Campo no cadastro de imobilizado (AS02) que armazena a placa de identificação do veículo, a ser preenchido automaticamente a partir do cadastro em PM (item 7). |
| "DT. Básica" (campo) | Campo da aba "Pagamentos" da MIRO que define a data básica usada para cálculo de vencimento de pagamento (item 14). |
| "Vencimento Em" (campo) | Campo da aba "Pagamentos" da MIRO que indica a data de vencimento do pagamento, calculada a partir de "DT. Básica" + "Condição de Pagamento" (item 14). |
| "Condição de Pagamento" (campo) | Campo SAP que define o prazo (em dias) e termos de pagamento associados ao fornecedor/pedido. |
| Estorno | Operação SAP que reverte/cancela um documento contábil ou logístico previamente lançado (ex.: estorno de MIRO, estorno de pedido). |
| MoSCoW | Técnica de priorização de requisitos: Must Have (essencial/obrigatório), Should Have (importante, mas não bloqueante), Could Have (desejável), Won't Have (fora do escopo atual). |
| RF / RNF | Requisito Funcional (RF) — descreve uma funcionalidade que o sistema deve executar; Requisito Não-Funcional (RNF) — descreve uma característica de qualidade do sistema (performance, segurança, disponibilidade, usabilidade, etc.). |
| CB | Condição Bloqueante — pendência identificada na qualificação (CB-1 a CB-6, CB-Orçamento) que precisa ser resolvida em prazo definido para não bloquear etapas do projeto. |
| Onda | Agrupamento de itens de escopo por complexidade/sequência de entrega: Onda 1 (baixa complexidade), Onda 2 (mudanças de regra de negócio), Onda 3 (alta complexidade — automações/integrações/estorno). |
| Job batch | Programa SAP executado de forma agendada e automática (transação SM37), usado para as automações de sincronização entre módulos/monitores. |
| Imobilizado de frota | Ativo fixo (veículo, máquina, implemento) registrado no módulo Asset Accounting (AA), vinculado ao processo de aquisição via MM. |

---

## 6. Perguntas Abertas (vinculadas às Condições Bloqueantes)

| ID | Questão | Para quem | Prazo |
|----|---------|-----------|-------|
| Q001 (= CB-3) | Qual o destino exato da coluna "Data de lançamento" da fatura (MIRO): GSI03, GSI04 ou ambos (RF011)? E qual a relação entre o cabeçalho "ZMMR_GSI01" do chamado e os 15 itens de escopo (nenhum item referencia GSI01)? | Tatiane Dias de Moraes / João Henrique | 2026-06-13 |
| Q002 (= CB-6, item 13) | Quais são as regras detalhadas de estorno de fatura/pedido (RF016-RF018), incluindo: nomenclatura exata dos status no GSI03/GSI04 após estorno, tratamento de estorno parcial de MIRO, e tratamento de MIRO já paga ao tentar estornar o pedido? | SQUAD PM/MM (Jerfesson Fernandes Helmer) + Especialista Funcional | 2026-06-24 |
| Q003 (= CB-6, item 14) | O novo comportamento de "DT. Básica" (RF019) e o cálculo de "Vencimento Em" (RF020) devem se aplicar a TODOS os pedidos lançados via MIRO no SAP, ou apenas aos pedidos controlados pelo monitor GSI03? Existe algum outro processo/área que utiliza a MIRO fora do fluxo do monitor e seria impactado por essa mudança de comportamento padrão? | SQUAD PM/MM (Jerfesson Fernandes Helmer) + Nubia Carla Freitas Santos Souza | 2026-06-24 |
| Q004 | Qual a lista de valores válidos para o novo campo "Classificação" (RF001/RF002/RF003) e quais regras de negócio determinam a obrigatoriedade por tipo de requisição na ZMMTR002? | Tatiane Dias de Moraes | A definir antes do início da Onda 2 |
| Q005 | Qual o papel/role SAP existente (ou a ser criado) que deve ser usado como referência para a restrição de acesso descrita em RNF003 ("Controle de Ativos — Editor GSI")? | SQUAD PM/MM (segurança) + Nubia Carla Freitas Santos Souza | A definir antes do início da Onda 2 |

---

## 7. Aprovação

Analista: Rafael Requisito (VMO Autônomo) ___________________ Data: __________

Solicitante Principal: Tatiane Dias de Moraes ___________________ Data: __________

Co-Solicitante: João Henrique ___________________ Data: __________

Especialista Técnico de Referência: Jerfesson Fernandes Helmer ___________________ Data: __________

Gestor Direto / Sponsor: Nubia Carla Freitas Santos Souza ___________________ Data: __________

**Nota de Status:** Esta ERF está apta para validação dos itens das Ondas 1 e 2 (exceto RF011, pendente CB-3).
Os requisitos da Onda 3 relativos aos itens 13 e 14 (RF016-RF020) são apresentados em nível de requisito de
negócio com critérios de aceitação **provisórios**, e NÃO devem avançar para desenvolvimento até a conclusão
da especificação funcional formal e do plano de testes exigidos pela CB-6 (prazo 2026-06-24).
