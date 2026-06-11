# WORK REQUEST — PROJ-2026-008
## Ajustes nos Monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 — SAP ECC Módulo MM (Demanda DEM-2026-008)

**Versão:** 1.0 | **Data de Emissão:** 2026-06-11 | **Elaborado por:** VMO Consultoria
**Validade deste WR:** 60 dias a partir da data de emissão

---

## 1. Identificação do Projeto

| Campo | Informação |
|---|---|
| Código do Projeto | PROJ-2026-008 |
| Demanda | DEM-2026-008 |
| Nome do Projeto | Ajustes nos Monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 — SAP ECC Módulo MM |
| Classificação | Melhoria Evolutiva — Time de Sustentação ERP (PM/MM) |
| Sponsor | Nubia Carla Freitas Santos Souza — Gerente Contábil (aprovação de Diretoria em confirmação — CB-1) |
| Solicitante Principal | Tatiane Dias de Moraes — Coordenadora de Controle de Ativos e Recebimento Fiscal |
| Co-Solicitante | João Henrique |
| Especialista Técnico de Referência (V1) | Jerfesson Fernandes Helmer |
| Gerente de Projeto (VMO) | A designar pelo SQUAD PM/MM (Time de Sustentação ERP) |
| Tipo de Solução | Customização SAP ECC (módulo MM) — desenvolvimento ABAP em monitores Z já existentes (BAdIs, user-exits, ajustes de tela e jobs batch) |
| **Destinatário primário deste WR** | **SQUAD PM/MM (Time de Sustentação ERP — Grupo Águia Branca / VIX)** |
| **Destinatário alternativo / complementar** | **Consultoria SAP MM/ABAP externa qualificada — apenas se houver necessidade de complementação de capacidade do squad interno (ver Seção 2)** |
| Prazo de Submissão de Propostas | até 2026-06-25 (10 dias úteis após emissão) — ver Seção 11 |
| Prazo Final de Execução (TAP) | 2026-09-30 |

---

## 2. Contexto e Justificativa

A área de Contabilidade / Controle de Ativos e Recebimento Fiscal do Grupo Águia Branca (VIXPar/VIX Matriz) opera, desde a V1, três monitores SAP customizados — ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 — que dão suporte ao ciclo completo de imobilizado de frota e entrada de notas fiscais (requisição → pedido → recebimento de fatura → cadastro de ativo). Esses monitores já estão em produção e foram desenvolvidos pelo especialista de referência Jerfesson Fernandes Helmer.

No dia a dia, a equipe identificou **15 lacunas operacionais** que hoje geram retrabalho manual, dependência constante de TI para correções pontuais e risco de divergência entre o status real do pedido/fatura no SAP e o status exibido nos monitores. Em outras palavras: o time de Contabilidade frequentemente "não confia" no que o monitor mostra e precisa checar manualmente nas transações originais (ME53N, ME22N, MIRO, AS02), o que consome tempo de fechamento mensal e aumenta o risco de erro de conciliação.

O resultado esperado desta contratação é simples de descrever: **fazer com que os três monitores reflitam, automaticamente e sem intervenção manual, o que já acontece nas transações padrão do SAP** — exibindo campos que faltam, automatizando marcações de status e corrigindo duas regras de cálculo de datas que hoje geram inconsistência fiscal/contábil.

**Importante — natureza desta contratação:** Diferente de um projeto novo, trata-se de um **pacote fechado de 15 ajustes evolutivos** sobre uma solução já existente e estável (V1). O fornecedor não está "construindo do zero" — está fazendo manutenção evolutiva guiada, com acesso ao código-fonte da V1 e ao especialista que o construiu.

**Destinatário deste WR:** Este Work Request é encaminhado, em primeiro lugar, ao **SQUAD PM/MM (Time de Sustentação ERP do Grupo Águia Branca/VIX)**, que já é responsável pela V1 dos monitores e tem o contexto técnico necessário para esta evolução. Caso o squad interno identifique que não possui capacidade plena alocada dentro do prazo do projeto (até 2026-09-30), este mesmo WR pode ser encaminhado a uma **consultoria SAP MM/ABAP externa qualificada**, para complementar a capacidade — total ou parcialmente, por onda. As referências de mercado (custo e prazo) trazidas neste documento (Seção 6 e Seção 9) servem justamente para calibrar essa decisão: comparar o que o squad interno consegue entregar dentro do envelope de R$ 30.000–36.000 com o que o mercado cobraria por escopo equivalente.

---

## 3. Objetivo da Contratação

O fornecedor (squad interno ou consultoria externa complementar) deve entregar os **15 ajustes** descritos na Seção 4, distribuídos em **3 ondas sequenciais**, todos em produção, testados e validados pelos usuários finais, até **30/09/2026**.

**Critério de sucesso da contratação (visão do contratante):**
- 100% dos itens da Onda 1 em produção e validados até 31/07/2026;
- 100% dos itens da Onda 2 em produção e validados até 31/08/2026;
- 100% dos itens da Onda 3 (incluindo os dois itens de maior risco fiscal/contábil — estorno de fatura/pedido e regras de data de vencimento) em produção, testados com plano de testes formal e validados até 30/09/2026;
- Nenhuma funcionalidade hoje existente nos monitores GSI02/03/04 deve parar de funcionar ou mudar de comportamento fora do que está descrito neste WR (não-regressão);
- Indicador de eficiência operacional (a ser formalizado pelo contratante até 17/06/2026) medido antes e depois do go-live de cada onda, com meta de melhoria mínima de 20% em até 60 dias após a Onda 3.

---

## 4. Escopo da Contratação

### 4.1 Escopo Incluso

O escopo está organizado em **3 ondas**, conforme priorização já validada com o solicitante e o especialista de referência. Cada item abaixo referencia o(s) Requisito(s) Funcional(is) (RF) da Especificação de Requisitos (ERF v1.0), que fazem parte integrante deste WR e devem ser lidos na íntegra pelo fornecedor antes da elaboração da proposta.

#### Onda 1 — Exposição de campos existentes (baixa complexidade) — meta: 31/07/2026

| Item | Descrição (linguagem de negócio) | RF de Referência | Monitor(es) |
|---|---|---|---|
| 2 | Exibir a coluna "Vencimento NF" (já existe na tela de requisição) dentro do monitor GSI02 | RF004 | GSI02 |
| 3 | Exibir a coluna "CR" (Centro de Custo, já existe na tela de requisição) dentro do monitor GSI02 | RF005 | GSI02 |
| 4 | Exibir a coluna "Data Liberação/aprovação" da requisição dentro do monitor GSI02 | RF006 (Should Have) | GSI02 |
| 6 | Exibir a coluna "Data de lançamento" da fatura no(s) monitor(es) GSI03 e/ou GSI04 — destino exato a confirmar (ver Seção 5 / CB-3) | RF011 (condicional, pendente CB-3) | GSI03 e/ou GSI04 |
| 9 | Incluir "Nº de Requisição de Compra" como campo de busca/filtro no monitor GSI04 | RF021 | GSI04 |
| 11 | Exibir a coluna "Tipo de Veículo" dentro do monitor GSI02, com filtro/ordenação | RF007 | GSI02 |
| 15 | Permitir informar o campo "Grupo deprec." (já existe no cadastro de imobilizado) ao criar o ativo via GSI02 | RF008 | GSI02 |
| Transversal | Performance: monitores devem carregar até 500 registros em até 5 segundos com até 50 usuários simultâneos | RNF001 | GSI02/03/04 |
| Transversal | Novas colunas devem aparecer no layout padrão, sem configuração manual do usuário | RNF007 | GSI02/03/04 |

#### Onda 2 — Mudanças de regra de negócio (complexidade média) — meta: 31/08/2026

| Item | Descrição (linguagem de negócio) | RF de Referência | Monitor(es) |
|---|---|---|---|
| 1 | Criar campo "Classificação" na tela de requisição, torná-lo obrigatório no fluxo customizado de criação de requisições, e exibi-lo como coluna no GSI02 | RF001, RF002, RF003 | GSI02 |
| 8 | Marcar automaticamente como "concluída" a etapa de Legalização no GSI03 para máquinas/implementos que não precisam de emplacamento | RF012 | GSI03 |
| 10 | Permitir alterar o "Tipo de Veículo" de um pedido depois de criado (com registro de quem alterou e quando), propagando a alteração para os três monitores | RF014, RF015 | GSI02/03/04 |
| 12 | Permitir corrigir manualmente o XML de uma nota fiscal incorreta vinculada a um registro do GSI03, somente quando o equipamento ainda não foi legalizado e o ativo ainda não foi cadastrado | RF013 | GSI03 |
| Transversal | Automações em background devem rodar em jobs com periodicidade máxima de 1 hora | RNF002 | GSI02/03/04 |
| Transversal | Acesso às novas funções de edição/exclusão restrito a perfil específico de autorização | RNF003 | GSI03 |
| Transversal | Toda alteração feita pelas novas funções deve gerar log de auditoria (usuário, data/hora, valor anterior/novo) | RNF004 | GSI02/03/04 |
| Transversal | Mensagens de bloqueio devem identificar claramente o motivo e o campo/documento causador | RNF008 | GSI02/03/04 |

#### Onda 3 — Automações, integrações e estorno (alta complexidade) — meta: 30/09/2026

| Item | Descrição (linguagem de negócio) | RF de Referência | Monitor(es) |
|---|---|---|---|
| 5 | Detectar automaticamente quando uma fatura (MIRO) é lançada "fora do fluxo" (via processo GRC) e, ao detectar, carregar o número da fatura no GSI03 e marcar a etapa correspondente como concluída | RF009, RF010 | GSI03 |
| 7 | Quando um veículo/equipamento for cadastrado/atualizado no módulo de Manutenção de Planta (PM), atualizar automaticamente a placa do veículo no cadastro de imobilizado correspondente | RF022 | GSI04 / AS02 |
| 13 | Estorno de fatura/pedido: ao estornar uma fatura vinculada a um registro do GSI03/GSI04, remover o vínculo, atualizar o status do registro, registrar log de auditoria, permitir lançamento de nova fatura após o estorno e impedir o estorno do pedido enquanto houver fatura ativa vinculada | RF016, RF017, RF018 | GSI03/GSI04 |
| 14 | Alterar a regra de preenchimento da data de vencimento da fatura: a "Data Básica" deixa de ser preenchida automaticamente na criação do pedido e passa a ser preenchida com a "Data da Fatura" no momento do lançamento; o "Vencimento" passa a ser calculado automaticamente como Data Básica + Condição de Pagamento | RF019, RF020 | GSI03 |

> **Atenção especial — Itens 13 e 14:** Estes dois itens envolvem regras fiscais/contábeis sensíveis (estorno de documentos e datas de vencimento de pagamento) e foram classificados como risco ALTO na qualificação do projeto. **A especificação funcional formal e o plano de testes detalhado destes itens (Condição Bloqueante CB-6) estão em elaboração e devem ser entregues ao fornecedor até 24/06/2026, antes do início do desenvolvimento desta onda.** O fornecedor deve prever, em sua proposta, que o desenvolvimento da Onda 3 só pode iniciar formalmente após o recebimento dessa especificação.

### 4.2 Nota Técnica — Tecnologias e Padrões (baseada em pesquisa de mercado)

- O ambiente é **SAP ECC (módulo MM)**, com monitores customizados (transações "Z") já desenvolvidos em **ABAP**. Toda a customização solicitada deve ser feita em **ABAP clássico/OO**, utilizando preferencialmente **BAdIs (Business Add-Ins)** e, onde a V1 já utiliza, **user-exits** — sem alteração de código-padrão SAP (evitar modificações "core" para preservar upgrades futuros).
- As automações em background (itens 5, 7, 8, 10, 15) devem ser implementadas como **jobs batch (transação SM37)**, conforme já é o padrão da V1.
- O fornecedor deve obrigatoriamente trabalhar em cima do código-fonte e da arquitetura existente da V1 — **não se trata de novo desenvolvimento, mas de evolução de solução em produção**. Acesso ao especialista de referência (Jerfesson Fernandes Helmer) será disponibilizado (ver Seção 5).
- **Nota de mercado:** SAP anunciou o fim do suporte mainstream ao ECC (EHP 6/7/8) para 31/12/2027, com suporte estendido até 2030. Isso reforça que esta é uma manutenção evolutiva de curto prazo sobre uma base que ainda tem vida útil — não recomenda-se nenhum redesenho ou nova arquitetura, apenas ajustes pontuais e bem delimitados.

---

## 5. Premissas e Responsabilidades do Grupo

O Grupo Águia Branca (contratante) disponibilizará ao fornecedor selecionado:

1. **Acesso aos ambientes SAP** (desenvolvimento, qualidade/homologação e, em janela controlada, produção) com usuário e autorizações compatíveis com o trabalho a ser realizado.
2. **Acesso ao código-fonte da V1** dos monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04, incluindo documentação técnica existente (se houver).
3. **Disponibilidade do especialista técnico de referência**, Jerfesson Fernandes Helmer, durante todo o projeto, para esclarecimentos funcionais/técnicos sobre a V1.
4. **Pontos focais de negócio** para validação funcional e UAT: Tatiane Dias de Moraes (Coordenadora) e João Henrique (Co-Solicitante).
5. **Aprovação das entregas intermediárias** (por onda) em até 5 dias úteis após a entrega para homologação, via reunião de validação funcional + ambiente de teste.
6. **Definição da lista de valores do campo "Classificação"** (item 1) e do **papel/role de autorização** para as novas funções de edição (item 12, 13, 14) — a serem fornecidos pelo contratante antes do início da Onda 2.
7. **Resolução das pendências (Condições Bloqueantes) que afetam o escopo:**
   - **CB-3** (destino da coluna "Data de lançamento" — item 6/RF011): resposta esperada até 13/06/2026;
   - **CB-6** (especificação funcional formal e plano de testes dos itens 13 e 14): resposta esperada até 24/06/2026, condição para início da Onda 3;
   - **CB-5** (estimativa de esforço por fase pelo SQUAD PM/MM): até 17/06/2026 — usada para refinar este cronograma.

**O fornecedor não deve incluir em sua proposta**: custos de licenciamento SAP, infraestrutura de servidores/ambientes, ou qualquer item relacionado ao acesso ao sistema — tudo isso é de responsabilidade e custo do contratante.

---

## 6. Cronograma Esperado

> **Nota:** Este cronograma é baseado no prazo macro do TAP (encerramento em 30/09/2026) e em benchmarks de mercado para projetos de pequeno/médio porte de customização SAP ABAP (que, segundo pesquisa de mercado, costumam variar de **6 a 12 semanas para pacotes de até ~15 ajustes pontuais**, dependendo da complexidade e da necessidade de especificação funcional formal para itens de maior risco). O cronograma detalhado e definitivo será negociado com o fornecedor selecionado e está sujeito a refinamento pela estimativa de esforço por fase do SQUAD PM/MM (CB-5, esperada até 17/06/2026).

| Marco | Descrição | Data-alvo |
|---|---|---|
| M0 | Emissão deste WR / início do prazo de propostas | 2026-06-11 |
| M1 | Recebimento de propostas | até 2026-06-25 |
| M2 | Seleção do fornecedor (interno SQUAD PM/MM e/ou complementação externa) e kick-off | até 2026-06-30 |
| M3 | **Onda 1 concluída e validada em produção** (itens 2,3,4,6,9,11,15) | 2026-07-31 |
| M4 | **Onda 2 concluída e validada em produção** (itens 1,8,10,12) | 2026-08-31 |
| M5 | Recebimento da especificação funcional formal e plano de testes dos itens 13/14 (CB-6) — pré-requisito para M6 | até 2026-06-24 (idealmente concluído antes do início da Onda 3) |
| M6 | **Onda 3 concluída, testada e validada em produção** (itens 5,7,13,14) | 2026-09-30 |
| M7 | Encerramento, repasse à sustentação e medição do indicador de eficiência (baseline vs. pós-Onda 3) | até 2026-11-30 (60 dias após go-live da Onda 3) |

**Observações:**
- O intervalo entre M2 (kick-off) e M3 (~4-5 semanas) é compatível com benchmarks de mercado para pacotes de baixa complexidade (exposição de campos existentes).
- O intervalo M3→M4 (~1 mês) cobre as 4 mudanças de regra de negócio da Onda 2, alinhado a faixas de mercado para ajustes de regras/validação em transações já existentes.
- O intervalo M4→M6 (~1 mês) é o mais apertado frente a benchmarks de mercado para itens com especificação funcional formal e risco fiscal (itens 13 e 14) — **o fornecedor deve sinalizar na proposta se esse prazo é exequível ou se requer paralelismo com a Onda 2**, condicionado ao recebimento antecipado da especificação CB-6.
- Caso o SQUAD PM/MM identifique, na sua estimativa de esforço (CB-5), que o prazo da Onda 3 não é exequível com a capacidade interna disponível, este WR autoriza a busca de complementação externa especificamente para a Onda 3.

---

## 7. Entregáveis Obrigatórios

| Entregável | Critério de Aceite (binário) |
|---|---|
| Especificação funcional detalhada por item (1 a 15) | Aceito se cobre 100% dos RF Must Have correspondentes (RF001-RF022, conforme aplicável) e foi validada por escrito pelo solicitante (Tatiane Dias de Moraes) |
| Especificação técnica (objetos ABAP, BAdIs/user-exits, jobs alterados/criados) | Aceito se lista todos os objetos técnicos impactados por item, sem pendências de "a definir" |
| Desenvolvimento implementado em ambiente de desenvolvimento/qualidade | Aceito se a funcionalidade está disponível e testável em ambiente de homologação (QAS) |
| Plano de testes (geral + específico para itens 13 e 14) | Aceito se contém, no mínimo, os cenários de teste descritos nos critérios de aceitação dos RF correspondentes (ex.: RF013 com 4 cenários, RF016-RF018 com mínimo 3 cenários) |
| Relatório de execução de testes por onda | Aceito se demonstra execução de 100% dos cenários do plano de testes, com evidência (print/log) de cada resultado |
| Roteiro e relatório de teste de regressão (RNF009) | Aceito se cobre as funcionalidades-chave da V1 com 0 defeitos críticos/altos identificados fora do escopo dos 15 itens |
| Pacote de transporte para produção, por onda | Aceito se aplicado em produção sem erro e validado pelo usuário em até 5 dias úteis (UAT) |
| Documentação da solução/configuração final (atualização da documentação da V1) | Aceito se reflete fielmente o comportamento implementado, revisado pelo especialista de referência |
| Plano de implantação / cutover por onda | Aceito se define data, responsáveis, plano de rollback e janela de execução |
| Plano de suporte pós-implantação (hipercare) | Aceito se define duração, canal e SLA de atendimento a incidentes pós-go-live |
| Plano de repasse para sustentação | Aceito se inclui handover documentado ao SQUAD PM/MM/Time de Sustentação ERP |
| Status reports periódicos | Aceito se entregue na frequência definida na Seção 8, sem interrupções não justificadas |

---

## 8. Governança e Comunicação

- **Status report:** quinzenal, por e-mail, para o GP VMO e Tatiane Dias de Moraes (Solicitante Principal).
- **Reunião de acompanhamento:** semanal (Teams), com participação do fornecedor, GP, e — quando necessário — Jerfesson Fernandes Helmer.
- **Validação funcional / UAT:** ao final de cada onda, em reunião dedicada com Tatiane Dias de Moraes e João Henrique, em ambiente de homologação.
- **Canal oficial de comunicação:** e-mail + Teams, conforme definido pelo GP designado.
- **Processo de aprovação de entregas:** cada onda só é considerada "concluída" após (a) execução do plano de testes, (b) UAT aprovado pelos pontos focais de negócio, e (c) ausência de defeitos críticos/altos de regressão (RNF009).
- **Escalonamento:** qualquer item classificado como ALTO risco (especialmente itens 5, 13 e 14) que apresentar atraso ou problema técnico deve ser comunicado ao Sponsor (Nubia Carla Freitas Santos Souza) em até 24 horas.

---

## 9. Condições Comerciais

- **Modelo de faturamento: por marcos (milestones), nunca por hora.** O fornecedor deve apresentar o valor total da proposta decomposto por marco/onda (M3, M4, M6 da Seção 6), com percentual de faturamento vinculado à entrega aceita de cada onda.
- **Envelope de referência:** até **R$ 30.000** (investimento declarado como aprovado), podendo chegar a **R$ 36.000** (com 20% de contingência), valor ainda sujeito à validação orçamentária do Sponsor/Diretoria (**CB-Orçamento**, em aberto). **Propostas que ultrapassem R$ 36.000 devem vir acompanhadas de justificativa técnica detalhada e serão avaliadas separadamente.**
- **Referência de mercado para calibração (pesquisa realizada):** para pacotes fechados de customização ABAP em monitores SAP ECC MM de pequeno/médio porte (BAdIs, user-exits, jobs batch, ~15 itens, sem novo módulo), consultorias especializadas no Brasil costumam praticar diárias/homem-hora de consultoria sênior SAP significativamente acima da média salarial de mercado (CLT), com projetos de escopo fechado e prazo de 6-12 semanas tipicamente variando entre **R$ 25.000 e R$ 80.000+**, dependendo da complexidade dos itens de maior risco (como os itens 13 e 14 desta demanda, que envolvem especificação funcional formal). **O envelope de R$ 30-36K está no limite inferior dessa faixa de mercado** — o que reforça a recomendação de execução primária pelo SQUAD PM/MM interno (que já conhece a V1 e não cobra "ramp-up"), reservando eventual complementação externa apenas para os itens de maior complexidade (Onda 3), caso necessário.
- **Prazo de pagamento:** até 15 dias após aprovação formal (UAT) de cada marco/onda.
- **Reajuste:** não se aplica — contrato de escopo fechado, sem repactuação dentro da vigência prevista (até 30/09/2026), exceto por mudança de escopo formalmente aprovada (ver processo de mudança do Plano Geral do Projeto).
- **Penalidades por atraso:** multa de 0,5% do valor do marco em atraso por dia útil de atraso não justificado, limitada a 10% do valor total do marco; atrasos decorrentes de pendências do contratante (ex.: CB-3, CB-6 não resolvidas no prazo) não geram penalidade ao fornecedor.
- **Garantia:** período de garantia de **60 dias corridos** após o go-live de cada onda, durante o qual correções de defeitos relacionados ao escopo entregue não geram custo adicional ao contratante.
- **SLA de suporte pós-implantação (hipercare):** durante o período de garantia, o fornecedor deve responder a incidentes críticos (bloqueio de operação) em até 4 horas úteis e incidentes não-críticos em até 1 dia útil.

---

## 10. Artefato Obrigatório — Conformidade da Proposta

Toda proposta recebida deve conter o checklist abaixo preenchido com OK / NOK / Observações para cada um dos 41 itens. Propostas com qualquer item NOK sem justificativa serão consideradas incompletas.

| Item | Descrição | OK / NOK | Observações |
|---|---|---|---|
| **Grupo 1 — Identificação da Proposta** | | | |
| 1.1 | Nome do fornecedor | | |
| 1.2 | Projeto / Demanda | | |
| 1.3 | Tipo de solução (SaaS / Desenvolvimento / SAP) | | |
| 1.4 | Data de recebimento da proposta | | |
| 1.5 | Versão da proposta | | |
| 1.6 | Validade da proposta (mín. 30 dias) | | |
| **Grupo 2 — Escopo Detalhado da Entrega** | | | |
| 2.1 | Objetivo da solução claramente descrito | | |
| 2.2 | Funcionalidades incluídas detalhadas | | |
| 2.3 | Módulos, programas ou componentes impactados listados | | |
| 2.4 | Integrações descritas ou formalmente declaradas como não impactadas | | |
| 2.5 | Relatórios impactados descritos ou declarados como não impactados | | |
| 2.6 | Necessidade de licenças claramente informada ou declarada como não aplicável | | |
| **Grupo 3 — Exclusões de Escopo** | | | |
| 3.1 | Exclusões de escopo explicitamente listadas | | |
| 3.2 | Não utilização de frases genéricas ou ambíguas | | |
| **Grupo 4 — Premissas** | | | |
| 4.1 | Premissas técnicas claramente descritas | | |
| 4.2 | Premissas de acesso a ambientes e sistemas | | |
| 4.3 | Premissas de aprovação das entregas intermediárias | | |
| **Grupo 5 — Metodologia e Abordagem** | | | |
| 5.1 | Metodologia adotada explicitamente definida | | |
| 5.2 | Etapas do projeto claramente descritas | | |
| 5.3 | Processo de validação e aceite das entregas definido | | |
| **Grupo 6 — Entregáveis** | | | |
| 6.1 | Especificação funcional | | |
| 6.2 | Especificação técnica | | |
| 6.3 | Documentação da solução/configuração | | |
| 6.4 | Plano de testes detalhado | | |
| 6.5 | Relatórios de execução de testes | | |
| 6.6 | Plano de implantação / Cutover | | |
| 6.7 | Plano de suporte pós-implantação | | |
| 6.8 | Plano de repasse para sustentação | | |
| 6.9 | Status reports periódicos previstos | | |
| **Grupo 7 — Governança e Gestão** | | | |
| 7.1 | Matriz RACI apresentada | | |
| 7.2 | Matriz de riscos apresentada | | |
| 7.3 | Plano de comunicação definido | | |
| **Grupo 8 — Prazo, Cronograma e Equipe** | | | |
| 8.1 | Prazo total de execução informado | | |
| 8.2 | Cronograma macro apresentado | | |
| 8.3 | Marcos de entrega definidos | | |
| 8.4 | Equipe envolvida descrita | | |
| 8.5 | Prazo para mobilização de recursos | | |
| **Grupo 9 — Condições Comerciais e Financeiras** | | | |
| 9.1 | Valor total do investimento informado | | |
| 9.2 | Modelo de faturamento por marcos definido | | |
| 9.3 | Critérios de validação dos marcos descritos | | |
| 9.4 | Prazo e regras de pagamento definidos | | |
| **Grupo 10 — Penalidades, Garantia e Sustentação** | | | |
| 10.1 | Penalidades e multas previstas | | |
| 10.2 | Período e condições de garantia definidos | | |
| 10.3 | SLAs de suporte definidos | | |
| 10.4 | Plano de sustentação apresentado | | |

---

## 11. Processo de Submissão

- **Prazo final para recebimento de propostas:** **2026-06-25** (10 dias úteis após a data de emissão deste WR, 2026-06-11).
- **Canal de envio:** e-mail do GP VMO / Projetos DTI (a ser informado pelo coordenador do pipeline VMO Autônomo no momento do envio efetivo deste WR).
- **Formato aceito:** proposta em PDF + planilha (Excel/Google Sheets) com o detalhamento de custos por marco/onda e o checklist do Artefato Obrigatório (Seção 10) preenchido.
- **Assunto do e-mail:** `PROPOSTA — PROJ-2026-008 / DEM-2026-008 — [Nome do Fornecedor]`
- **Contato para esclarecimentos técnicos:** Especialista Técnico de Referência (Jerfesson Fernandes Helmer), via SQUAD PM/MM.
- **Contato para esclarecimentos comerciais/processuais:** GP VMO designado para o projeto.
- **Condições de desclassificação automática:**
  - Proposta recebida após o prazo final (2026-06-25), sem prorrogação formal previamente comunicada;
  - Artefato Obrigatório (Seção 10) com qualquer item não preenchido;
  - Ausência de modelo de faturamento por marcos (proposta baseada em cobrança por hora);
  - Ausência de qualquer das 3 exclusões de escopo descritas na Seção 4.2 do TAP (replicadas abaixo) na seção de exclusões da proposta do fornecedor;
  - Proposta que não referencie pelo menos os RF Must Have de uma onda completa (indicando leitura incompleta da ERF).

### Escopo Excluso (referência obrigatória — fornecedor deve declarar conformidade)

1. **Ajustes no monitor ZMMR_GSI01** — não há item de escopo correspondente entre os 15 itens aprovados; a relação entre o ZMMR_GSI01 (citado no chamado original) e o item 6 ainda está em esclarecimento (CB-3). Qualquer ajuste no GSI01 está fora deste WR e não deve ser orçado.
2. **Novas integrações com sistemas externos ao SAP ECC** não mencionadas nos 15 itens de escopo — as integrações citadas (GRC, PM, AS01/AS02) já existem e estão operacionais; não há previsão de desenvolvimento de novas interfaces externas.
3. **Novos módulos SAP ou alterações em módulos não citados** (ex.: FI, CO, fora do contexto de imobilizado/MM tratado aqui) — qualquer necessidade identificada nesse sentido deve ser tratada como nova demanda, fora deste WR.
4. **Desenvolvimento de novos relatórios gerenciais não solicitados** — o escopo se limita aos ajustes nos 3 monitores já existentes (GSI02/03/04); criação de relatórios adicionais não faz parte desta contratação.
5. **Treinamento amplo de usuários** além da capacitação operacional da equipe de Contabilidade/Controle de Ativos diretamente impactada pelos 15 itens — treinamentos corporativos amplos ou para outras áreas estão fora de escopo.

---

*Work Request emitido pelo VMO Consultoria em nome do Grupo Águia Branca / VIX. Este documento incorpora referências de pesquisa de mercado (consultoria SAP ABAP no Brasil, faixas de custo e prazo para pacotes de customização de pequeno/médio porte) para fins de calibração do envelope de referência e do cronograma esperado, sem prejuízo da prioridade de execução pelo SQUAD PM/MM (Time de Sustentação ERP) conforme classificação desta demanda como Melhoria Evolutiva.*
