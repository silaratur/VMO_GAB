# WORK REQUEST — PROJ-2026-008
## Implantação/Expansão do TVM para Fluxo de Caixa, Controle Orçamentário e Rastreabilidade de Riscos (Grupo Águia Branca)

**Versão:** 1.0 | **Data de Emissão:** 2026-07-07 | **Elaborado por:** VMO Consultoria
**Validade deste WR:** 60 dias a partir da data de emissão (até 2026-09-05)

> **Aviso de status:** Este WR é emitido em paralelo à finalização da documentação interna de iniciação do projeto (TAP e ERF ainda em status RASCUNHO, com 6 condições bloqueantes — CBs — em resolução pelo PMO). Isso é deliberado: o objetivo é permitir que fornecedores qualificados preparem propostas enquanto o planejamento interno detalhado (cronograma físico, matriz de riscos interna) é concluído. Todas as incertezas materiais conhecidas até esta data (prazo, orçamento, viabilidade técnica de itens específicos) estão declaradas explicitamente nas seções abaixo — nenhuma foi omitida.

---

## 1. Identificação do Projeto

| Campo | Valor |
|---|---|
| Código do Projeto | PROJ-2026-008 |
| Demanda de origem | DEM-2026-008 |
| Nome do Projeto | Implantação/Expansão do TVM para Fluxo de Caixa, Controle Orçamentário e Rastreabilidade de Riscos |
| Contratante | Grupo Águia Branca |
| Sponsor | Paula Barcelos (CEO) — identidade confirmada verbalmente pelo PMO; evidência documental formal em processo de formalização (não impede a emissão deste WR ao mercado) |
| Gerente de Projeto (GP) | A designar pelo PMO — ponto de contato interino: Marcelo Silveira (Coordenador PMO e Sustentação ERP) |
| Solicitante formal | Alessandra Comério (Financeiro) |
| Líder técnico do contratante | Cássio |
| Tipo de solução | Desenvolvimento/Configuração sobre plataforma já licenciada (SAP add-on) — **NÃO é aquisição de nova plataforma** (ver Seção 2) |
| Modalidade de contratação | Serviços de configuração, desenvolvimento e integração |
| Prazo final para submissão de proposta | 2026-07-28 (21 dias corridos a partir da emissão deste WR) — ver Seção 11 |

---

## 2. Contexto e Justificativa

O Grupo Águia Branca controla hoje seu fluxo de caixa e orçamento de forma manual, por meio de planilhas Excel alimentadas com extrações do SAP. Esse processo está concentrado em poucas pessoas — com dependência crítica de uma única colaboradora para a consolidação de números apresentados à diretoria — o que gera baixa rastreabilidade de despesas, ausência de visibilidade financeira das compras para negociação com fornecedores, e horizonte de previsão de caixa limitado a base mensal.

O grupo já opera, em uma de suas empresas (VIX), uma solução de tesouraria/gestão financeira interna identificada como **"TVM"**. Esta contratação **não é para adquirir ou escolher uma nova plataforma** — é para contratar serviços de **configuração, desenvolvimento e integração** que estendam essa solução já licenciada/contratada pelo grupo às demais frentes de negócio (Financeiro, Suprimentos, Riscos e Desempenho Organizacional), nos mesmos moldes já validados na VIX.

**Nota de pesquisa de mercado sobre "TVM" (transparência ao fornecedor):** A VMO Consultoria pesquisou o mercado brasileiro de soluções de gestão de fluxo de caixa e tesouraria corporativa para contextualizar esta contratação. A pesquisa identificou como candidato mais provável a suíte **"TVM — Treasury, Bank and Planning"**, da empresa brasileira **MakeValue** (Joinville/SC), um conjunto de soluções nativas (add-on) para o ambiente **SAP ERP / SAP S/4HANA**, voltado a tesouraria, gestão bancária e planejamento financeiro, com casos públicos de implantação em grupos corporativos brasileiros (DEXCO, iFood, Brisanet, Grupo Ferroeste). Esse achado é **consistente** com o contexto declarado no TAP do projeto (grupo já opera SAP como ERP central; TVM é tratado como ferramenta interna já validada em outra empresa do grupo, não como produto a ser escolhido nesta contratação). **Esta identificação não foi confirmada formalmente pelo contratante e não deve ser tratada como certeza** — é uma hipótese de mercado razoável, registrada aqui para que o fornecedor selecionado já chegue ao kick-off com contexto técnico útil. O fornecedor deve confirmar com o líder técnico do contratante (Cássio) a plataforma/versão exata em uso antes de fechar sua proposta técnica.

O benefício financeiro desta iniciativa ainda não foi quantificado formalmente pelo contratante (pendência interna registrada no TAP). A justificativa de negócio é, no momento, predominantemente qualitativa: redução de dependência de pessoa-chave, maior credibilidade dos números apresentados à diretoria, e previsibilidade de caixa ampliada.

**Pesquisa de mercado — prazos e custos de referência (contexto para o fornecedor, não vinculante):**
- Projetos de implantação de sistemas de gestão financeira/orçamentária especializados no Brasil, quando tratados como **configuração** (e não construção de sistema do zero), tendem a variar entre aproximadamente **90 dias e 12 meses**, dependendo do escopo e do grau de customização. Fases de teste/homologação tipicamente consomem de 2 a 4 semanas, e a fase de implantação/go-live entre 1 e 2 semanas.
- Como este projeto é **configuração/desenvolvimento sobre uma plataforma já implantada e validada em outra empresa do grupo** (não uma implantação do zero), o contratante trabalha com uma expectativa de prazo posicionada na faixa inferior da média de mercado para implantações completas — ver Seção 6 (cronograma reconciliado: Go-live em ~13,4 semanas úteis, Encerramento em ~90 dias úteis).
- Faixas de custo para projetos de configuração/customização de sistemas de gestão financeira/ERP no Brasil variam amplamente conforme escopo e porte (de poucos milhares de reais para pequenas customizações a mais de R$ 100.000 para projetos corporativos complexos). Este WR usa como envelope de referência o orçamento do TAP (ver Seção 9), não uma média de mercado genérica.
- Fontes consultadas: MakeValue (makevalue.com.br — cases DEXCO, iFood, Brisanet, Ferroeste), Portal ERP (portalerp.com), SAP Brasil (sap.com/brazil), Coupa, blogs especializados em ERP/custos de implantação (cora.com.br, gestaopro.com.br, tedsys.com.br, treasy.com.br).

---

## 3. Objetivo da Contratação

O fornecedor selecionado deverá **configurar, desenvolver e integrar** a solução TVM já licenciada pelo Grupo Águia Branca para operar de forma unificada nas 3 frentes de negócio abaixo, eliminando o Excel como fonte primária de informação para a diretoria:

1. **Financeiro** — fluxo de caixa segregado por tipo de negócio e categoria de despesa até o LAIR, com apresentação automatizada à diretoria;
2. **Suprimentos** — painel de baseline orçamentário com atualização automática e alertas de consumo por faixa (70%/85%);
3. **Riscos e Desempenho Organizacional** — ampliação do horizonte de previsão de caixa de mensal para 90 dias corridos.

**Critério de sucesso da contratação (do ponto de vista do contratante):** as 3 frentes operando em produção no TVM, com adoção ativa pelas áreas usuárias por no mínimo 90 dias após o respectivo go-live de cada frente, e sem dependência de consolidação manual em planilha para a apresentação de números à diretoria.

---

## 4. Escopo da Contratação

### 4.1 Escopo Incluso

Todos os itens abaixo são **Must Have** (prioridade obrigatória) da Especificação de Requisitos (ERF v1.1) do projeto. Os IDs devem ser referenciados pelo fornecedor em sua proposta técnica (Seção 2.2 do Artefato Obrigatório, Seção 10 deste WR).

**Frente Financeiro**

| ID | Funcionalidade requerida |
|---|---|
| RF-FIN-01 | Registro e consulta de ingressos e egressos de caixa no TVM, substituindo a planilha Excel hoje usada como fonte primária |
| RF-FIN-02 | Cálculo e apresentação do LAIR (Lucro Antes do Imposto de Renda) a partir dos lançamentos registrados no TVM |
| RF-FIN-03 | Classificação manual-assistida, no momento do lançamento, de cada receita por tipo de negócio (ex.: linha de negócio, bandeira de cartão), com relatório de receitas segregado por essa classificação |
| RF-FIN-04 | Agrupamento de despesas por categoria (manutenção, combustível, TI, entre outras a mapear) até a composição do LAIR |
| RF-FIN-05 | Geração automática do relatório/apresentação consolidada de fluxo de caixa para a diretoria, eliminando a consolidação manual semanal em Excel |

**Frente Suprimentos**

| ID | Funcionalidade requerida |
|---|---|
| RF-SUP-01 | Painel de baseline orçamentário com atualização automática a cada novo lançamento de compra/despesa |
| RF-SUP-02 | Projeção de pagamentos parcelados em janelas de 30, 60 e 90 dias a partir da data de referência |
| RF-SUP-03 | Alertas automáticos quando o consumo do orçamento atingir 70% e 85% do valor orçado, por categoria/centro de custo |
| RF-SUP-04 | Relatório básico de consumo por fornecedor e por categoria, em formato tabular, derivado do baseline orçamentário, para apoio à negociação com fornecedores |

**Frente Riscos e Desempenho Organizacional**

| ID | Funcionalidade requerida |
|---|---|
| RF-RIS-01 | Ampliação do horizonte de previsão de caixa de mensal para 90 dias corridos |
| RF-RIS-02 | Rastreabilidade de custos por categoria e centro de custo, no nível de granularidade hoje suportado pelo SAP (lote/grupo de conta) |

**Requisitos Transversais (Segurança e Auditoria) — aplicam-se às 3 frentes**

| ID | Funcionalidade requerida |
|---|---|
| RF-TRA-05 | Restrição de acesso funcional às 3 áreas (Financeiro, Suprimentos, Riscos/Desempenho), com cada gestor visualizando/editando apenas os dados da própria área |
| RF-TRA-06 | Trilha de auditoria (log) de toda alteração em lançamentos financeiros e orçamentários — usuário, data/hora, valor anterior e valor novo |

**Requisitos Não Funcionais Must Have (aplicam-se às 3 frentes)**

| ID | Requisito |
|---|---|
| RNF-PERF-01 | Painel de baseline orçamentário deve carregar em até 5 segundos, com até 12 meses de dados, até 20 usuários simultâneos |
| RNF-PERF-02 | Atualização do baseline orçamentário e do fluxo de caixa refletida na visualização em até 15 minutos após o lançamento |
| RNF-DISP-01 | Disponibilidade mínima de 99% de uptime em horário comercial (08h–18h, dias úteis), medida mensalmente |
| RNF-DISP-02 | Manutenções programadas fora do horário comercial, comunicadas às áreas com no mínimo 24h de antecedência |
| RNF-SEG-01 | Controle de acesso baseado em perfil (RBAC), restrito às 3 áreas mapeadas |
| RNF-SEG-02 | Registro de auditoria de toda alteração financeira/orçamentária, retido por no mínimo 5 anos |
| RNF-SEG-03 | Dados criptografados em trânsito (TLS 1.2 ou superior) e em repouso |
| RNF-USA-01 | Relatório consolidado para diretoria gerado em no máximo 3 telas/cliques a partir da tela inicial |
| RNF-USA-02 | Taxa de erro do usuário ≤ 10% em teste de usabilidade com pelo menos 3 usuários por área, após 1 sessão de treinamento |

**Nota de tecnologia (com base na pesquisa de mercado, Seção 2):** a solução técnica a ser configurada/desenvolvida é, com alta probabilidade, um add-on nativo do ambiente SAP (hipótese: suíte TVM da MakeValue ou equivalente). O fornecedor deve declarar em sua proposta se possui experiência comprovada em customização/configuração sobre a plataforma identificada pelo líder técnico do contratante na reunião de esclarecimentos (Seção 11), incluindo, se aplicável, certificação ou parceria formal com o fabricante da plataforma e/ou com a SAP.

### 4.2 Escopo Excluso

As exclusões abaixo protegem o contratante de propostas que incluam serviços não solicitados ou que assumam compromissos técnicos ainda não confirmados internamente. **Nenhuma delas deve ser incluída no preço ou no cronograma da proposta.**

| # | Item excluído | Justificativa |
|---|---|---|
| 1 | **Aquisição, licenciamento ou seleção de nova plataforma de gestão financeira/fluxo de caixa.** O TVM já é ferramenta contratada/licenciada pelo Grupo Águia Branca (uso corrente validado em outra empresa do grupo, VIX). Esta contratação é exclusivamente de **serviços** de configuração, desenvolvimento e integração sobre a plataforma existente. | Evita que o fornecedor precifique ou proponha uma plataforma alternativa; o objeto é serviço, não produto. |
| 2 | **Projeções analíticas por linha (receita/despesa) para orçado vs. realizado** (RF-TRA-01). | Viabilidade técnica ainda não confirmada pela equipe técnica interna do contratante (condição bloqueante em aberto). Item tratado como possível ampliação de escopo formal futura, não incorporação automática nesta contratação. |
| 3 | **Dashboards gráficos e/ou integração com ferramenta de BI** (RF-TRA-02). | Mencionado nas tratativas internas como "diferencial desejável", mas sem confirmação de viabilidade técnica nem compromisso de entrega nesta fase. |
| 4 | **Integração com o sistema Atenas** (usado por 2 empresas do grupo fora do SAP) (RF-TRA-03). | Formato técnico de integração (API, arquivo, frequência, autenticação) ainda não definido internamente; exige avaliação técnica prévia antes de qualquer compromisso de entrega. |
| 5 | **Definição de níveis de permissão/acesso ampliados** a gestores além das 3 áreas hoje mapeadas (RF-TRA-04). | Fora do escopo aprovado internamente nesta fase; qualquer ampliação exige decisão formal de governança do contratante. |
| 6 | **Segregação automática de receitas por tipo de negócio via extração/integração direta com o SAP** (RF-FIN-03-C — a versão manual-assistida, RF-FIN-03, está inclusa). | Depende de confirmação técnica de que o SAP fornece o dado nesse nível de granularidade; não deve ser assumida como entregável garantido nesta contratação. |
| 7 | **Visão analítica avançada de compras** (comparativos históricos multiperíodo, tendências gráficas por fornecedor) (RF-SUP-04-C — o relatório básico, RF-SUP-04, está incluso). | Depende da mesma confirmação de capacidade de dashboards/BI do item 3 acima; tratada como possível extensão futura, não obrigação desta contratação. |
| 8 | **Rastreabilidade de custos até o nível individual de nota fiscal** (RF-RIS-03 — a rastreabilidade no nível hoje suportado pelo SAP, RF-RIS-02, está inclusa). | O SAP hoje não desce a este nível de granularidade; viabilizar isso pode exigir mudança estrutural de lançamento no próprio SAP, o que está fora do escopo desta contratação (exigiria estudo de viabilidade e contratação à parte). |
| 9 | **Autenticação via SSO/Active Directory corporativo** (RNF-SEG-04) como obrigação contratual firme. | Depende de confirmação técnica de que a plataforma suporta integração com o provedor de identidade corporativo do contratante; se não suportar, será aceita autenticação local com política de senha equivalente, sem penalidade ao fornecedor. |
| 10 | **Qualquer alteração na estrutura de lançamento no SAP** (módulos, plano de contas, granularidade de lançamento). | O projeto atua sobre o TVM (camada de configuração/serviço); mudanças estruturais no SAP são fora de escopo e, se necessárias, exigem novo estudo e contratação separada. |

---

## 5. Premissas e Responsabilidades do Grupo

O Grupo Águia Branca (contratante), por meio da equipe do projeto, disponibilizará ao fornecedor selecionado:

- Acesso ao ambiente TVM/SAP já existente (instância já em uso pela VIX, incluindo réplica ou ambiente de homologação a definir com a equipe técnica interna) para fins de configuração e testes;
- Um ponto focal dedicado por frente de negócio: Alessandra Comério (Financeiro), Wellington Gonçalves (Suprimentos) e Thamyris (Riscos e Desempenho Organizacional), para levantamento complementar, validação de requisitos e homologação (UAT);
- Suporte do líder técnico interno (Cássio) e da equipe técnica TVM do grupo para dúvidas de plataforma, integrações existentes com o SAP e liberação de acessos;
- Aprovação formal, pelo GP designado (e, quando aplicável, pelo sponsor), de cada entregável intermediário e de qualquer mudança de escopo, prazo ou custo em relação ao definido neste WR;
- Dados de referência (extrações atuais do SAP, planilhas Excel em uso) necessários para os testes de migração e validação cruzada (ex.: validação do cálculo de LAIR).

**Premissas que o fornecedor deve considerar em sua proposta:**
- A viabilidade técnica de 5 itens específicos de escopo (listados na Seção 4.2, itens 2–5 e 8) ainda está em confirmação interna pelo contratante; a proposta não deve assumir esses itens como entregáveis obrigatórios;
- O levantamento de requisitos da frente Financeiro está parcialmente concluído — pode haver complementação de escopo dentro da mesma frente após sessão de continuação interna, a ser comunicada ao fornecedor selecionado antes do fechamento do contrato ou logo no início do levantamento detalhado;
- A disponibilidade da equipe técnica interna do TVM do grupo para apoiar o fornecedor ainda não está formalmente confirmada pelo contratante; o fornecedor deve sinalizar em sua proposta o nível de autonomia técnica com que consegue operar caso esse apoio seja limitado.

---

## 6. Cronograma Esperado

**Importante:** o cronograma abaixo já reflete o **cronograma detalhado construído internamente** (Carlos Cronograma, Planejamento de Prazo, `03-planejamento/cronograma.md`) e a **reconciliação de prazo** feita entre TAP, PM Canvas e Plano Geral (Diana Documento) — isso substitui a data-alvo provisória anterior de "T0 + 7 semanas úteis", que era calculada apenas sobre o piso do sizing (206h), sem considerar o buffer de gestão nem o ciclo de acompanhamento pós-go-live exigido pelo próprio Critério de Sucesso #2 do projeto. Os marcos abaixo usam nomenclatura própria do WR (letras A–G) para não conflitar com a numeração interna do cronograma do contratante (M0–M6), mas os **prazos são os mesmos**, com referência cruzada na última coluna. O cronograma é **relativo ao marco T0 (kick-off / assinatura do contrato)**, já que a data de início real ainda depende de designação formal do GP e resolução de pendências internas — **nenhuma data de calendário fixa está sendo assumida neste WR.**

| Marco (WR) | Descrição | Prazo estimado (relativo a T0) | Ref. cronograma interno |
|---|---|---|---|
| A | Kick-off do projeto com o fornecedor selecionado | T0 | M0 |
| B | Fechamento do levantamento de requisitos detalhado e ERF v2.0 (3 frentes) | T0 + 10 dias úteis (~2 semanas) | M1 |
| C | Desenvolvimento/configuração completo (3 frentes + transversal) | T0 + 38 dias úteis (~7,6 semanas) | M2 |
| D | Testes e homologação (UAT) aprovados — 3 frentes | T0 + 50 dias úteis (~10 semanas) | M3 |
| E | Go-live das 3 frentes | T0 + 58 dias úteis (~11,6 semanas) sem buffer de gestão / **T0 + ~67 dias úteis (~13,4 semanas) incluindo buffer de gestão de 15%** — este último é o prazo de referência publicado | M4 |
| F | Aceite pós-go-live (1 ciclo mensal completo de acompanhamento, Critério de Sucesso #2 do TAP) | T0 + 88 dias úteis (~17,6 semanas) | M5 |
| G | Encerramento do projeto (inclui período de garantia/suporte deste WR, Seção 9) | **T0 + ~90 dias úteis** | M6 |

**Prazo de referência deste WR:** Go-live esperado em **T0 + ~13,4 semanas úteis** (incluindo buffer de gestão de 15%); Encerramento (incluindo o ciclo de acompanhamento pós-go-live) em **T0 + ~90 dias úteis**. Estes valores substituem qualquer menção anterior a "T0 + 7 semanas" em versões prévias deste documento ou de outros artefatos de iniciação — o prazo de 7 semanas media apenas o esforço de desenvolvimento no cenário mais otimista, sem buffer nem período de observação pós-go-live, e não deve mais ser usado como referência.

**Nota de calibração de mercado:** com o prazo reconciliado de **T0 + ~13,4 semanas até o Go-live (~94 dias corridos)**, o prazo interno do contratante passa a se posicionar **dentro da faixa inferior do benchmark de mercado** observado para implantações de sistemas de gestão financeira (tipicamente 90 dias a 12 meses) — uma calibração mais realista do que a estimativa provisória anterior, e ainda assim competitiva frente à média de mercado. Isso é coerente com o fato de o escopo desta contratação ser **configuração/desenvolvimento sobre uma plataforma já implantada e validada em outra empresa do grupo** (VIX) — não uma implantação do zero — o que justifica um prazo no piso da faixa de mercado, mas não abaixo dela. Ainda assim, o fornecedor deve avaliar criticamente essa expectativa em sua proposta e declarar se a considera exequível para o escopo desta Seção 4.1, propondo ajuste justificado caso julgue necessário. Propostas de prazo devem vir acompanhadas de cronograma macro próprio (ver Artefato Obrigatório, Grupo 8).

---

## 7. Entregáveis Obrigatórios

| Entregável | Critério de aceite (binário) |
|---|---|
| Especificação funcional detalhada por frente | Aceito somente se cobrir 100% dos itens do Escopo Incluso (Seção 4.1) com rastreabilidade explícita aos IDs de RF/RNF |
| Especificação técnica da configuração/desenvolvimento | Aceito somente se detalhar objetos/configurações/customizações por frente, revisado e sem pendência técnica aberta pelo líder técnico do contratante |
| Ambiente configurado — Frente Financeiro | Aceito somente se RF-FIN-01 a 05 passarem nos testes de aceite descritos na ERF, sem divergência entre lançamento e relatório em 100% dos casos de teste |
| Ambiente configurado — Frente Suprimentos | Aceito somente se RF-SUP-01 a 04 passarem nos testes de aceite descritos na ERF, incluindo disparo correto de alertas nos limiares de 70% e 85% |
| Ambiente configurado — Frente Riscos/Desempenho | Aceito somente se RF-RIS-01 e RF-RIS-02 passarem nos testes de aceite descritos na ERF, com projeção de caixa de 90 dias funcional |
| Plano e relatório de testes (UAT) | Aceito somente se cobrir as 3 frentes, com evidência de execução e resultado (aprovado/reprovado) por caso de teste |
| Plano de implantação / cutover | Aceito somente se definir data de corte, plano de rollback e responsáveis, aprovado formalmente pelo GP do contratante antes do go-live |
| Plano de suporte pós-implantação e SLA | Aceito somente se definir canal, tempos de resposta por severidade e escopo de cobertura, conforme Seção 9 |
| Plano de repasse para sustentação (transferência de conhecimento) | Aceito somente se incluir sessão(ões) de repasse documentada(s) para a equipe técnica interna do contratante, com lista de presença e material entregue |
| Status reports periódicos | Aceito somente se entregues na frequência definida na Seção 8, sem lacunas não justificadas |
| Trilha de auditoria e controle de acesso configurados (RF-TRA-05, RF-TRA-06) | Aceito somente se teste de acesso negado e teste de log de auditoria (Seção 4.1) passarem 100% dos casos |

---

## 8. Governança e Comunicação

- **Status report:** periodicidade semanal, por escrito, ao GP designado pelo contratante (interinamente, Marcelo Silveira/PMO), cobrindo progresso por frente, riscos abertos e pendências de decisão do contratante;
- **Reunião de acompanhamento:** quinzenal, com GP e pontos focais das 3 frentes conforme pauta relevante ao momento do projeto;
- **Canal oficial de comunicação:** e-mail formal ao GP designado, com cópia ao PMO (Marcelo Silveira), para todas as decisões, aprovações e mudanças de escopo;
- **Processo de aprovação de entregas:** cada entregável da Seção 7 é submetido formalmente por e-mail ou ata de reunião, com aceite ou rejeição justificada registrada pelo GP em até 5 dias úteis da submissão;
- **Escalonamento:** qualquer impasse não resolvido entre fornecedor e GP em até 5 dias úteis é escalado ao sponsor/PMO.

---

## 9. Condições Comerciais

- **Envelope de referência orçamentário:** o contratante sinaliza como **aprovado** o valor de **R$ 30.000 a R$ 32.000**. **Nota de transparência (obrigatória ao mercado):** o contratante possui, internamente, uma estimativa de custo real do escopo completo desta contratação na faixa de **R$ 43.080 a R$ 69.720**, com base em dimensionamento de esforço (206–334h) e taxa de referência de mercado ainda não confirmada com fornecedor. A reconciliação entre as duas faixas está em andamento internamente e **não é responsabilidade do fornecedor resolver** — mas o fornecedor deve saber, ao propor, que valores acima de R$ 32.000 **serão considerados e não são automaticamente desclassificados**, desde que acompanhados de justificativa clara de escopo/esforço/equipe. Propostas acima de R$ 70.000 exigem justificativa reforçada e serão avaliadas com atenção redobrada quanto ao custo-benefício.
- **Modelo de faturamento:** por marcos de entrega (nunca por hora), vinculado à aceitação formal de cada entregável da Seção 7, seguindo a estrutura de marcos da Seção 6 (ex.: parcela na assinatura/kick-off, parcelas nas entregas por frente, parcela na homologação/UAT, parcela no go-live e encerramento do suporte inicial). O fornecedor deve detalhar em sua proposta o percentual e o critério de cada parcela.
- **Prazo de pagamento:** até 30 dias corridos após a validação/aceite formal do marco correspondente pelo GP do contratante.
- **Reajuste:** não se aplica reajuste de valores dentro do prazo de execução previsto neste WR (até T0 + ~90 dias úteis, marco de Encerramento — Seção 6 —, incluindo Go-live em ~13,4 semanas e ciclo de acompanhamento pós-go-live, mais o período de garantia), dado o horizonte de poucos meses do contrato; reajuste só é aplicável em caso de prorrogação superior a 12 meses, pelo índice a acordar em contrato.
- **Penalidades por atraso:** multa de 0,3% ao dia sobre o valor do marco em atraso, limitada a 10% do valor total do contrato, sem prejuízo de eventual rescisão por atraso superior a 30 dias corridos não justificado.
- **Período de garantia:** mínimo de 90 dias corridos após o go-live de cada frente, cobrindo correção de defeitos sem custo adicional ao contratante.
- **SLA de suporte pós-implantação:** o fornecedor deve declarar em sua proposta tempos de resposta e resolução por nível de severidade (crítico, alto, médio, baixo), com no mínimo: severidade crítica com resposta em até 4 horas úteis.

---

## 10. Artefato Obrigatório — Conformidade da Proposta

**Esta seção é inegociável.** Toda proposta recebida deve vir acompanhada deste checklist preenchido pelo fornecedor (coluna "Atendido" com OK/NOK e coluna "Observações" com evidência ou justificativa). Propostas que não anexarem o checklist preenchido serão desclassificadas (ver Seção 11).

```
Grupo 1 — Identificação da Proposta (6 itens):
  1.1 Nome do fornecedor
  1.2 Projeto / Demanda
  1.3 Tipo de solução (SaaS / Desenvolvimento / SAP)
  1.4 Data de recebimento da proposta
  1.5 Versão da proposta
  1.6 Validade da proposta (mín. 30 dias)

Grupo 2 — Escopo Detalhado da Entrega (6 itens):
  2.1 Objetivo da solução claramente descrito
  2.2 Funcionalidades incluídas detalhadas
  2.3 Módulos, programas ou componentes impactados listados
  2.4 Integrações descritas ou formalmente declaradas como não impactadas
  2.5 Relatórios impactados descritos ou declarados como não impactados
  2.6 Necessidade de licenças claramente informada ou declarada como não aplicável

Grupo 3 — Exclusões de Escopo (2 itens):
  3.1 Exclusões de escopo explicitamente listadas
  3.2 Não utilização de frases genéricas ou ambíguas

Grupo 4 — Premissas (3 itens):
  4.1 Premissas técnicas claramente descritas
  4.2 Premissas de acesso a ambientes e sistemas
  4.3 Premissas de aprovação das entregas intermediárias

Grupo 5 — Metodologia e Abordagem (3 itens):
  5.1 Metodologia adotada explicitamente definida
  5.2 Etapas do projeto claramente descritas
  5.3 Processo de validação e aceite das entregas definido

Grupo 6 — Entregáveis (9 itens):
  6.1 Especificação funcional
  6.2 Especificação técnica
  6.3 Documentação da solução/configuração
  6.4 Plano de testes detalhado
  6.5 Relatórios de execução de testes
  6.6 Plano de implantação / Cutover
  6.7 Plano de suporte pós-implantação
  6.8 Plano de repasse para sustentação
  6.9 Status reports periódicos previstos

Grupo 7 — Governança e Gestão (3 itens):
  7.1 Matriz RACI apresentada
  7.2 Matriz de riscos apresentada
  7.3 Plano de comunicação definido

Grupo 8 — Prazo, Cronograma e Equipe (5 itens):
  8.1 Prazo total de execução informado
  8.2 Cronograma macro apresentado
  8.3 Marcos de entrega definidos
  8.4 Equipe envolvida descrita
  8.5 Prazo para mobilização de recursos

Grupo 9 — Condições Comerciais e Financeiras (4 itens):
  9.1 Valor total do investimento informado
  9.2 Modelo de faturamento por marcos definido
  9.3 Critérios de validação dos marcos descritos
  9.4 Prazo e regras de pagamento definidos

Grupo 10 — Penalidades, Garantia e Sustentação (4 itens):
  10.1 Penalidades e multas previstas
  10.2 Período e condições de garantia definidos
  10.3 SLAs de suporte definidos
  10.4 Plano de sustentação apresentado
```

| Grupo | Nº de itens | Atendido (OK/NOK) | Observações |
|---|---|---|---|
| 1 — Identificação da Proposta | 6 | _a preencher pelo fornecedor_ | |
| 2 — Escopo Detalhado da Entrega | 6 | _a preencher pelo fornecedor_ | |
| 3 — Exclusões de Escopo | 2 | _a preencher pelo fornecedor_ | |
| 4 — Premissas | 3 | _a preencher pelo fornecedor_ | |
| 5 — Metodologia e Abordagem | 3 | _a preencher pelo fornecedor_ | |
| 6 — Entregáveis | 9 | _a preencher pelo fornecedor_ | |
| 7 — Governança e Gestão | 3 | _a preencher pelo fornecedor_ | |
| 8 — Prazo, Cronograma e Equipe | 5 | _a preencher pelo fornecedor_ | |
| 9 — Condições Comerciais e Financeiras | 4 | _a preencher pelo fornecedor_ | |
| 10 — Penalidades, Garantia e Sustentação | 4 | _a preencher pelo fornecedor_ | |
| **Total** | **41** | | |

---

## 11. Processo de Submissão

- **Prazo final para envio da proposta:** 2026-07-28 (21 dias corridos a partir da data de emissão deste WR), até 18h (horário de Brasília). Propostas recebidas após este prazo não serão consideradas.
- **Canal de envio:** e-mail formal ao GP do projeto (a designar) com cópia obrigatória ao PMO — Marcelo Silveira (Coordenador PMO e Sustentação ERP). Até a designação formal do GP, o canal interino de recebimento é o e-mail do PMO.
- **Formato aceito:** proposta técnica e comercial em **PDF**, acompanhada de **planilha (XLSX)** com a composição de custos por marco e o Artefato Obrigatório (Seção 10) preenchido.
- **Assunto do e-mail:** `PROPOSTA — PROJ-2026-008 — [Nome do Fornecedor]`
- **Contato para esclarecimentos técnicos:** Cássio (líder técnico do contratante), via e-mail do PMO, com prazo de resposta de até 3 dias úteis.
- **Contato para esclarecimentos comerciais/contratuais:** PMO — Marcelo Silveira.
- **Condições de desclassificação automática:**
  1. Proposta recebida após o prazo final definido acima;
  2. Ausência do Artefato Obrigatório (Seção 10) preenchido, integral ou parcialmente;
  3. Ausência de referência explícita aos IDs de RF/RNF do Escopo Incluso (Seção 4.1) na proposta técnica;
  4. Ausência de modelo de faturamento por marcos (proposta baseada exclusivamente em faturamento por hora não será aceita);
  5. Validade de proposta inferior a 30 dias corridos;
  6. Proposta que inclua, como entregável obrigatório precificado, qualquer item listado no Escopo Excluso (Seção 4.2) sem separação clara como item opcional/adicional.

---
*Work Request emitido pelo VMO Consultoria em nome do Grupo Águia Branca.*
