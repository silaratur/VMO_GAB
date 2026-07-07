# ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS E NÃO FUNCIONAIS (ERF) — PROJ-2026-008

Implantação/Expansão do TVM para Fluxo de Caixa, Controle Orçamentário e
Rastreabilidade de Riscos (Grupo Águia Branca)

Demanda de origem: DEM-2026-008
Autor: Rafael Requisito (Engenheiro de Requisitos, VMO Autônomo)
Data: 2026-07-07
Versão: 1.1
Status: **RASCUNHO** — elaborado com as 6 Condições Bloqueantes (CB-1 a CB-6) do
TAP ainda em aberto. Em particular: **CB-4** (levantamento da frente Financeiro
com Alessandra ainda incompleto) e **CB-5** (viabilidade técnica de 5 dos 14
componentes de escopo do sizing ainda não confirmada pela equipe técnica TVM)
afetam diretamente esta ERF e estão tratadas explicitamente abaixo — nenhum dos
dois foi tratado como resolvido.

**Nota de revisão (v1.1):** correção de cross-check apontada por Oscar
Orquestrador — RF-FIN-03 e RF-SUP-04 são itens listados no TAP como "dentro do
escopo" **sem** ressalva de incerteza, mas a v1.0 os havia rebaixado para
Should Have. Ambos foram desdobrados em 2 níveis (Must Have parcial viável +
Could Have condicionado), no mesmo padrão já usado para RF-RIS-02/RF-RIS-03,
para eliminar a divergência silenciosa entre a promessa do TAP e a garantia da
ERF. Ver Seção 2.1, 2.2 e 4.

Fontes utilizadas: `qualificacao-aprovada.md`, `documentacao-base.md` (TAP/PM
Canvas/Plano Geral), `sizing.md`, `demanda-validada.md`.

---

## 1. Convenções deste documento

- **RF** = Requisito Funcional | **RNF** = Requisito Não Funcional
- Prioridade em **MoSCoW**: M = Must Have, S = Should Have, C = Could Have,
  W = Won't Have (nesta fase)
- Todo requisito tem **Origem** (rastreabilidade ao documento/ata de onde veio)
- Todo requisito **Must Have** tem **Critério de Aceitação** testável
- Termos vagos ("rápido", "fácil", "eficiente", "intuitivo") são proibidos sem
  métrica associada — todo requisito de qualidade percebida tem número
- Os 5 itens de viabilidade técnica incerta (CB-5) são tratados como
  **Could Have condicionado** ou **Won't Have nesta fase**, nunca como Must
  Have, até confirmação da equipe técnica TVM

---

## 2. Requisitos Funcionais por Área Funcional

### 2.1 Área Financeiro (Solicitante: Alessandra Comério)

⚠️ Esta frente tem levantamento **incompleto** (CB-4 — sessão de continuação
com Alessandra ainda não realizada). Os RFs abaixo cobrem apenas o que a ata
disponível (07/07) sustenta; ver Seção 5 (Perguntas Abertas) para o que falta.

| ID | Requisito | Origem | Prioridade |
|----|-----------|--------|------------|
| RF-FIN-01 | O sistema deve permitir o registro e a consulta de ingressos e egressos de caixa no TVM, substituindo a planilha Excel hoje usada como fonte primária. | TAP §Escopo/Financeiro; sizing item 1 | **M** |
| RF-FIN-02 | O sistema deve calcular e apresentar o LAIR (Lucro Antes do Imposto de Renda) a partir dos lançamentos de ingressos/egressos e despesas categorizadas registrados no TVM. | TAP §Escopo/Financeiro; sizing item 1 | **M** |
| RF-FIN-03 | O sistema deve permitir que o usuário Financeiro classifique manualmente cada lançamento de receita por tipo de negócio (ex.: "Squad", bandeira de cartão) no momento do registro no TVM, gerando relatório de receitas segregado por essa classificação — independentemente de o SAP fornecer essa segregação automaticamente. | TAP §Escopo/Financeiro (item listado sem ressalva de incerteza); sizing item 2 | **M** — versão viável hoje com confiança razoável: classificação manual-assistida no ato do lançamento, sem depender de extração automática do SAP |
| RF-FIN-03-C | O sistema deve segregar receitas por tipo de negócio **automaticamente**, a partir de extração/integração direta com o SAP, sem exigir classificação manual do usuário. | sizing item 2 (parte incerta: "claro no requisito, incerto no como") | **C** — **condicionado à confirmação técnica** de que o SAP fornece (ou pode ser configurado para fornecer) o dado de tipo de negócio nesse nível de granularidade (ver PA-05); critério de aceite não pode ser fechado até a confirmação, mesmo padrão de RF-RIS-03 |
| RF-FIN-04 | O sistema deve permitir o agrupamento de despesas por categoria (manutenção, combustível, TI) até a composição do LAIR. | TAP §Escopo/Financeiro; sizing item 3 | **M** |
| RF-FIN-05 | O sistema deve gerar automaticamente a apresentação/relatório consolidado de fluxo de caixa para a diretoria, eliminando a consolidação manual semanal hoje feita em Excel. | TAP §Escopo/Financeiro; sizing item 4; TAP §Critérios de Sucesso #1 | **M** |
| RF-FIN-06 | [Reservado] Requisitos adicionais da frente Financeiro a definir após sessão de continuação com Alessandra. | CB-4 | *Não especificável agora — ver PA-02* |

**Critérios de Aceitação (Must Have):**
- **RF-FIN-01**: Dado um lançamento de ingresso ou egresso inserido no TVM, o valor deve aparecer no extrato de caixa do TVM em até 1 minuto, sem necessidade de reinserção em planilha externa. Teste: inserir 10 lançamentos de teste e confirmar 100% de correspondência entre o lançamento e o extrato.
- **RF-FIN-02**: Dado um conjunto de lançamentos de um mês fechado, o TVM deve apresentar o valor de LAIR calculado, auditável linha a linha até os lançamentos de origem, com diferença de R$ 0,00 frente ao cálculo manual de referência do mesmo período (validação cruzada em 1 ciclo de UAT).
- **RF-FIN-03**: Dado um lançamento de receita, o usuário deve conseguir selecionar o tipo de negócio em um campo/lista do TVM no ato do lançamento; o relatório de receitas segregado por tipo de negócio deve refletir 100% de correspondência com a classificação manual inserida. Teste: 10 lançamentos cobrindo ao menos 3 tipos de negócio distintos, validando 100% de correspondência entre classificação e relatório.
- **RF-FIN-04**: Dado um lançamento de despesa, o usuário deve conseguir classificá-lo em uma das categorias definidas (manutenção, combustível, TI ou outra a mapear) em uma única operação de lançamento, com o valor refletido no LAIR do período.
- **RF-FIN-05**: O relatório consolidado para diretoria deve ser gerado sem edição manual em planilha, contendo no mínimo: ingressos, egressos, despesas por categoria e LAIR do período, disponível em até 1 dia útil após o fechamento do período de referência.

---

### 2.2 Área Suprimentos (Ponto focal: Wellington Gonçalves)

| ID | Requisito | Origem | Prioridade |
|----|-----------|--------|------------|
| RF-SUP-01 | O sistema deve exibir um painel de baseline orçamentário que se atualiza automaticamente a cada novo lançamento de compra/despesa. | TAP §Escopo/Suprimentos; sizing item 11 | **M** |
| RF-SUP-02 | O sistema deve projetar pagamentos parcelados em janelas de 30, 60 e 90 dias a partir da data de referência. | TAP §Escopo/Suprimentos; sizing item 12 | **M** |
| RF-SUP-03 | O sistema deve emitir alertas automáticos quando o consumo do orçamento atingir as faixas de 70% e 85% do valor orçado, por categoria/centro de custo. | TAP §Escopo/Suprimentos; sizing item 13 | **M** |
| RF-SUP-04 | O sistema deve gerar um relatório básico de consumo por fornecedor e por categoria, derivado diretamente dos dados já capturados no baseline orçamentário (RF-SUP-01), em formato tabular, para apoiar negociação com fornecedores. | TAP §Escopo/Suprimentos (item listado sem ressalva de incerteza); sizing item 8 | **M** — versão viável hoje com confiança razoável: relatório tabular derivado de dado já Must Have (RF-SUP-01), sem necessidade de nova integração |
| RF-SUP-04-C | O sistema deve oferecer visão analítica avançada de visibilidade financeira das compras (comparativos históricos multiperíodo, tendências gráficas por fornecedor) para negociação estratégica. | Ata Wellington (visão ampliada mencionada); TAP §Escopo/Suprimentos não detalha profundidade | **C** — **condicionado à mesma confirmação técnica de capacidade de dashboards/BI de RF-TRA-02 (CB-5)**; não pode ser Must Have sem essa confirmação. Sobrepõe-se parcialmente a RF-TRA-02 (Won't Have nesta fase) — se a capacidade de BI for confirmada e priorizada, esta funcionalidade deve ser tratada como parte da mesma iniciativa de dashboards/BI, não como item separado |

**Critérios de Aceitação (Must Have):**
- **RF-SUP-01**: Após um lançamento de compra/despesa, o painel de baseline deve refletir o novo valor de consumo em até 15 minutos (ver RNF-PERF-02), sem necessidade de atualização manual/refresh de planilha.
- **RF-SUP-02**: Dado um lançamento parcelado, o sistema deve exibir corretamente o valor projetado a pagar nos períodos de 30, 60 e 90 dias, validado contra 1 caso de teste com parcelamento real de Suprimentos.
- **RF-SUP-03**: Ao atingir 70% do orçado em uma categoria, o sistema deve notificar o gestor responsável (e-mail ou notificação no TVM) em até 1 dia útil da transação que cruzou o limiar; o mesmo se aplica ao limiar de 85%. Teste: simular lançamento que cruze cada limiar e confirmar recebimento do alerta.
- **RF-SUP-04**: Dado o baseline orçamentário populado com lançamentos de ao menos 3 fornecedores e 2 categorias, o sistema deve exibir relatório com total consumido por fornecedor e por categoria no período selecionado, sem necessidade de exportação/manipulação manual em planilha.

---

### 2.3 Área Riscos e Desempenho Organizacional (Ponto focal: Thamyris)

⚠️ Esta é a área com maior dependência de pessoa-chave (risco já registrado no
TAP) e onde reside 1 dos 5 itens de viabilidade incerta (rastreabilidade a
nível de nota fiscal).

| ID | Requisito | Origem | Prioridade |
|----|-----------|--------|------------|
| RF-RIS-01 | O sistema deve ampliar o horizonte de previsão de caixa de mensal para 90 dias corridos. | TAP §Escopo/Riscos; TAP §Critérios de Sucesso #2 | **M** |
| RF-RIS-02 | O sistema deve permitir a rastreabilidade de custos por categoria e centro de custo, no nível de granularidade hoje suportado pelo SAP (lote/grupo de conta). | TAP §Escopo/Riscos; sizing item 7 (parte viável hoje) | **M** |
| RF-RIS-03 | O sistema deve permitir rastreabilidade de custos até o nível individual de nota fiscal. | sizing item 7; TAP Premissas item 2 (CB-5) | **C** — **condicionado à confirmação técnica da equipe TVM (CB-5)**; SAP hoje não desce a este nível, podendo exigir mudança estrutural de lançamento no SAP, o que está explicitamente **fora do escopo atual** do projeto (TAP §Fora do Escopo). Critério de aceite não pode ser fechado até a confirmação. |

**Critérios de Aceitação (Must Have):**
- **RF-RIS-01**: O sistema deve apresentar projeção de saldo de caixa para os próximos 90 dias corridos a partir da data corrente, atualizada a cada fechamento de período, validada em uso real por pelo menos 1 ciclo mensal completo (mesmo critério do TAP §Critérios de Sucesso #2).
- **RF-RIS-02**: Dado um lançamento de despesa, o sistema deve permitir consultar o custo agregado por categoria e por centro de custo (nível lote/grupo de conta, conforme estrutura atual do SAP), com rastreabilidade até o lançamento de origem.

---

### 2.4 Requisitos Transversais / Segurança / Auditoria

| ID | Requisito | Origem | Prioridade |
|----|-----------|--------|------------|
| RF-TRA-05 | O sistema deve restringir o acesso funcional às 3 áreas hoje mapeadas (Financeiro/Alessandra, Suprimentos/Wellington, Riscos-Desempenho/Thamyris), com cada gestor visualizando/editando apenas os dados da sua área, salvo permissão explícita de leitura cruzada aprovada pelo GP. | TAP §Fora do Escopo (permissões ampliadas fora, base de 3 áreas dentro); PM Canvas §5 | **M** |
| RF-TRA-06 | O sistema deve manter uma trilha de auditoria (log) de toda alteração em lançamentos financeiros e orçamentários, registrando usuário, data/hora, valor anterior e valor novo. | Inferido da natureza dos dados (caixa/orçamento) + governança exigida pela Regra GP 2026-05-24 citada no TAP | **M** |

**Critérios de Aceitação (Must Have):**
- **RF-TRA-05**: Um usuário autenticado como gestor de Suprimentos não deve conseguir editar lançamentos da área Financeiro (teste de acesso negado); tentativa registrada em log (ver RF-TRA-06).
- **RF-TRA-06**: Toda edição de um lançamento gera 1 registro de auditoria imutável (usuário, timestamp, campo alterado, valor antes/depois), consultável por um perfil de auditoria/PMO. Teste: editar 5 lançamentos de teste e confirmar 5 registros de auditoria correspondentes.

---

### 2.5 Requisitos Condicionados à Confirmação Técnica (CB-5) — Fora do escopo atual do TAP

Os 4 itens abaixo estão explicitamente listados no TAP como **"Fora do escopo
nesta fase"**. São documentados aqui para rastreabilidade e para uso futuro
por Carlos Cronograma/Pedro Perigo, **não** para execução no escopo atual.
Qualquer promoção destes itens para o escopo exige (a) confirmação técnica da
equipe TVM (CB-5) e (b) controle formal de mudança aprovado pelo GP/sponsor,
conforme o Plano de Gerenciamento de Mudanças do Plano Geral.

| ID | Requisito | Origem | Prioridade |
|----|-----------|--------|------------|
| RF-TRA-01 | Projeções analíticas por linha (receita/despesa) para orçado vs. realizado. | sizing item 5; TAP §Fora do Escopo | **W** — condicionado a CB-5; se confirmado viável, candidato a mudança formal de escopo (não Must Have nesta ERF) |
| RF-TRA-02 | Dashboards gráficos e/ou integração com ferramenta de BI. | sizing item 6; TAP §Fora do Escopo | **W** — condicionado a CB-5 ("plus" nas atas, sem compromisso de entrega) |
| RF-TRA-03 | Integração com o sistema Atenas para as 2 empresas fora do SAP. | sizing item 10; TAP §Fora do Escopo | **W** — condicionado a CB-5 e a definição do formato de integração (ver PA-03) |
| RF-TRA-04 | Definição de níveis de permissão/acesso ampliados a gestores além das 3 áreas mapeadas. | sizing item 14; TAP §Fora do Escopo | **W** — condicionado a CB-5 e a decisão formal de ampliação |

Nenhum destes 4 itens tem critério de aceitação fechado nesta versão — critério
de aceite só pode ser escrito após a confirmação técnica (CB-5), conforme o
Plano de Gerenciamento da Qualidade do Plano Geral.

---

## 3. Requisitos Não Funcionais (RNF)

RNFs não são opcionais dado o caráter sensível dos dados (fluxo de caixa e
orçamento). Mínimo de 4 categorias cobertas: Performance, Disponibilidade,
Segurança/Auditoria, Usabilidade.

### 3.1 Performance

| ID | Requisito | Prioridade | Critério de Aceitação |
|----|-----------|------------|------------------------|
| RNF-PERF-01 | O painel de baseline orçamentário (Suprimentos) deve carregar em no máximo 5 segundos, para até 12 meses de dados, medido em ambiente de produção sob carga normal de uso (até 20 usuários simultâneos). | **M** | Medir tempo de carregamento em 10 execuções de teste; 100% das execuções ≤ 5s. |
| RNF-PERF-02 | Após um lançamento, a atualização do baseline orçamentário e do fluxo de caixa deve ser refletida na visualização em até 15 minutos. Mecanismo (batch vs. tempo real) a confirmar tecnicamente (ver PA-04) — o SLA de 15 minutos vale independentemente do mecanismo escolhido. | **M** | Inserir lançamento de teste e cronometrar o tempo até refletir no painel; ≤ 15 min em 100% de 10 execuções. |

### 3.2 Disponibilidade

| ID | Requisito | Prioridade | Critério de Aceitação |
|----|-----------|------------|------------------------|
| RNF-DISP-01 | O TVM deve estar disponível para as 3 frentes com no mínimo 99% de uptime em horário comercial (08h–18h, dias úteis), medido mensalmente. | **M** | Relatório de uptime mensal do TVM (ou da equipe técnica) ≥ 99% em horário comercial. |
| RNF-DISP-02 | Manutenções programadas devem ocorrer fora do horário comercial e ser comunicadas aos gestores das 3 áreas com no mínimo 24 horas de antecedência. | **M** | Verificar registro de comunicação prévia em 100% das manutenções programadas realizadas em 1 ciclo de teste. |

### 3.3 Segurança e Auditoria

| ID | Requisito | Prioridade | Critério de Aceitação |
|----|-----------|------------|------------------------|
| RNF-SEG-01 | Controle de acesso baseado em perfil (RBAC), restrito às 3 áreas hoje mapeadas (ver RF-TRA-05); qualquer ampliação exige aprovação formal. | **M** | Ver critério de aceite de RF-TRA-05. |
| RNF-SEG-02 | Toda alteração em lançamento financeiro/orçamentário deve gerar registro de auditoria retido por no mínimo 5 anos (alinhado a requisitos fiscais/contábeis usuais no Brasil). | **M** | Ver critério de aceite de RF-TRA-06; confirmar política de retenção configurada para ≥ 5 anos. |
| RNF-SEG-03 | Dados de fluxo de caixa e orçamento devem ser criptografados em trânsito (TLS 1.2 ou superior) e em repouso. | **M** | Verificação técnica (scan de configuração) confirmando TLS ≥ 1.2 em todas as conexões e criptografia em repouso ativa no banco/armazenamento do TVM. |
| RNF-SEG-04 | Autenticação dos usuários deve utilizar o mecanismo corporativo já existente (SSO/Active Directory do Grupo Águia Branca), sem criação de credenciais paralelas no TVM. | **S** — condicionado à confirmação técnica de que o TVM suporta integração com o provedor de identidade corporativo (ver PA-09); se não suportar, rebaixar para credencial local com política de senha equivalente | Login de um usuário de teste via SSO corporativo sem necessidade de senha adicional específica do TVM. |

### 3.4 Usabilidade

| ID | Requisito | Prioridade | Critério de Aceitação |
|----|-----------|------------|------------------------|
| RNF-USA-01 | O relatório consolidado para diretoria (RF-FIN-05) deve ser gerado em no máximo 3 telas/cliques a partir da tela inicial do TVM, sem necessidade de manipulação manual de planilha. | **M** | Teste com 1 usuário Financeiro cronometrando navegação até geração do relatório; ≤ 3 cliques/telas em 100% das tentativas. |
| RNF-USA-02 | Em teste de usabilidade com pelo menos 3 usuários por área (Financeiro, Suprimentos, Riscos/Desempenho) executando as tarefas críticas (lançamento, consulta de painel, geração de alerta), a taxa de erro do usuário deve ser ≤ 10% após 1 sessão de treinamento inicial. | **M** | Sessão de teste registrada com contagem de erros/tentativas por usuário; taxa agregada ≤ 10%. |

---

## 4. Tabela-Resumo MoSCoW

| Prioridade | RF | RNF | Total | % do total (30) |
|------------|----|----|-------|------------------|
| **Must Have (M)** | 13 | 9 | 22 | 73,3% |
| **Should Have (S)** | 0 | 1 | 1 | 3,3% |
| **Could Have (C)** | 3 | 0 | 3 | 10,0% |
| **Won't Have nesta fase (W)** | 4 | 0 | 4 | 13,3% |
| **Total** | 20 | 10 | 30 | 100% |

Notas de leitura:
- Os 4 itens "Won't Have nesta fase" são exatamente os 4 dos 5 itens de CB-5
  que o TAP já classifica como "fora do escopo" (projeções analíticas por
  linha, dashboards/BI, integração Atenas, permissões ampliadas).
- O 5º item de CB-5 (rastreabilidade a nível de nota fiscal, RF-RIS-03) está
  marcado como **Could Have condicionado**, e não Won't Have, porque a
  rastreabilidade de custos em si (em nível SAP atual) já é Must Have
  (RF-RIS-02) — apenas o aprofundamento até a NF individual é incerto.
- Nenhum item de CB-5 foi tratado como Must Have, em conformidade com a
  condição de veto #5 desta especificação.
- **Correção v1.1 (cross-check TAP vs. ERF, Oscar Orquestrador)**: RF-FIN-03 e
  RF-SUP-04 são itens que o TAP lista como "dentro do escopo" **sem** ressalva
  de incerteza. Diferente dos 5 itens formais de CB-5, a incerteza aqui é
  apenas sobre o **mecanismo**, não sobre o **requisito em si**. Por isso
  ambos foram desdobrados no mesmo padrão de RF-RIS-02/RF-RIS-03: a versão
  viável hoje com confiança razoável virou **Must Have** (RF-FIN-03 —
  classificação manual-assistida; RF-SUP-04 — relatório básico derivado do
  baseline), e a versão automática/avançada virou **Could Have condicionado**
  (RF-FIN-03-C, RF-SUP-04-C), à parte da lista formal de 5 itens de CB-5.
  Resultado: todo item "dentro do escopo" do TAP agora tem cobertura de pelo
  menos 1 Must Have — nenhuma divergência silenciosa entre TAP e ERF
  permanece; não foi necessário registrar divergência formal de escopo
  porque, após análise, a versão parcial se mostrou viável com confiança
  razoável para ambos os itens.

---

## 5. Perguntas Abertas (Pendências de Especificação)

| ID | Pergunta | Por que não pode ser especificado hoje | Bloqueia |
|----|----------|------------------------------------------|----------|
| PA-01 | O TVM suporta projeções analíticas por linha (receita/despesa) para orçado vs. realizado? | Viabilidade técnica não confirmada (CB-5) | RF-TRA-01 |
| PA-02 | Quais são os requisitos completos da frente Financeiro além dos já levantados na ata parcial? | Sessão de continuação com Alessandra ainda não realizada (CB-4) | RF-FIN-06 e possível ajuste de RF-FIN-01 a 05 |
| PA-03 | Qual o formato técnico exato da integração com o sistema Atenas (API, arquivo, frequência, autenticação) e quais das 2 empresas fora do SAP realmente precisam dela? | "A ser avaliada tecnicamente" nas próprias atas; nenhuma fonte definiu o mecanismo (CB-5) | RF-TRA-03 |
| PA-04 | A apresentação "automática"/"tempo real" à diretoria (RF-FIN-05) será batch ou tempo real de fato? Qual a periodicidade tecnicamente viável? | sizing: "claro no objetivo, incerto no mecanismo" | RF-FIN-05, RNF-PERF-02 |
| PA-05 | Qual o mapeamento técnico exato para segregar receitas por tipo de negócio (Squad, bandeira de cartão) automaticamente, se o SAP hoje não segrega neste nível? (A versão manual-assistida, RF-FIN-03, já não depende desta resposta.) | sizing item 2: "claro no requisito, incerto no como" | RF-FIN-03-C |
| PA-06 | A rastreabilidade a nível de nota fiscal é viável apenas configurando o TVM, ou exige mudança na estrutura de lançamento do SAP (fora do escopo atual)? | Viabilidade técnica não confirmada (CB-5); SAP hoje só desce a lote/grupo de conta | RF-RIS-03 |
| PA-07 | Dashboards gráficos/BI são escopo obrigatório desta fase ou item de fase futura? | Tratado como "plus" nas atas, capacidade técnica não confirmada (CB-5) | RF-TRA-02, RF-SUP-04-C (visão analítica avançada de compras depende da mesma capacidade de BI) |
| PA-08 | A equipe técnica TVM tem disponibilidade confirmada para dimensionar e executar o projeto? | TAP Premissa 5: "não confirmada por nenhuma fonte até o momento" | Cronograma (Carlos Cronograma), viabilidade geral de todos os RFs |
| PA-09 | O TVM suporta autenticação via SSO/Active Directory corporativo do Grupo Águia Branca? | Não mencionado em nenhuma ata nem no sizing | RNF-SEG-04 |
| PA-10 | Qual o volume de horas/mês hoje gasto na consolidação manual (para servir de baseline de comparação pós-implantação)? | CB-6 — nenhuma fonte quantificou até o momento | Medição de benefício (fora do escopo desta ERF, mas necessário para ROI) |
| PA-11 | Será necessária aquisição de licenças adicionais de usuário para as 3 frentes, e qual o custo? | TAP Plano de Aquisições: "informação pendente" | Orçamento (CB-3), não bloqueia RFs desta ERF diretamente |

---

## 6. Glossário

| Termo | Definição |
|-------|-----------|
| **TVM** | Sistema/ferramenta de gestão financeira e orçamentária já implantada e validada na VIX (outra empresa do Grupo Águia Branca), usada como núcleo de configuração deste projeto. |
| **LAIR** | Lucro Antes do Imposto de Renda — indicador financeiro composto por ingressos/egressos e despesas categorizadas, usado como referência de resultado nas apresentações à diretoria. |
| **SAP** | Sistema ERP hoje utilizado pelo Grupo Águia Branca para lançamentos financeiros e de compras; fonte de extração manual atual dos dados que alimentam as planilhas Excel. |
| **Nota fiscal (NF)** | Documento fiscal individual de uma transação de compra/venda; nível de granularidade mais fino de rastreabilidade de custo cogitado (RF-RIS-03), hoje não suportado nativamente pela estrutura de lançamento do SAP (que desce apenas a lote/grupo de conta). |
| **Atenas** | Sistema usado por 2 empresas do grupo que operam fora do SAP; integração com ele é um dos 5 itens de viabilidade técnica incerta (CB-5). |
| **TAP** | Termo de Abertura do Projeto — documento de iniciação elaborado por Diana Documento, base normativa desta ERF. |
| **RF / RNF** | Requisito Funcional / Requisito Não Funcional. |
| **MoSCoW** | Técnica de priorização: Must Have, Should Have, Could Have, Won't Have (nesta fase). |
| **CB** | Condição Bloqueante — pendência formal registrada na Qualificação/TAP que precisa ser resolvida (CB-1 a CB-6 neste projeto). |
| **CB-4** | Levantamento incompleto da frente Financeiro (Alessandra) — sessão de continuação ainda não realizada. |
| **CB-5** | Viabilidade técnica não confirmada de 5 dos 14 componentes de escopo do sizing (projeções analíticas por linha, dashboards/BI, integração Atenas, rastreabilidade a nota fiscal, permissões ampliadas). |
| **RBAC** | Role-Based Access Control — controle de acesso baseado em perfil/papel do usuário. |
| **SLA** | Service Level Agreement — acordo de nível de serviço, expresso aqui como métrica objetiva (ex.: tempo, disponibilidade). |
| **UAT** | User Acceptance Testing — testes de homologação com o usuário final, previstos no TAP para as 3 frentes. |
| **Baseline orçado** | Valor de referência orçamentário de Suprimentos contra o qual o consumo real é comparado para gerar alertas de 70%/85%. |
| **SSO** | Single Sign-On — mecanismo de autenticação corporativa única, cogitado para o TVM (PA-09, não confirmado). |

---

## 7. Seção de Aprovação

Este documento organiza e detalha, em nível de requisito funcional/não
funcional, o escopo já delimitado no TAP (`documentacao-base.md`) e no sizing
(`sizing.md`). Ele **não resolve** nenhuma das 6 Condições Bloqueantes
registradas na Qualificação — em particular, permanece dependente de:
- **CB-4**: conclusão da sessão com Alessandra (pode adicionar/alterar RFs da
  Área Financeiro, especialmente RF-FIN-06);
- **CB-5**: confirmação técnica da equipe TVM sobre os 5 itens formais de
  viabilidade incerta (RF-TRA-01 a 04, RF-RIS-03), e também sobre os 2 itens
  adicionais de incerteza de mecanismo identificados na correção v1.1
  (RF-FIN-03-C — segregação automática de receitas; RF-SUP-04-C — visão
  analítica avançada de compras, que depende da mesma capacidade técnica de
  RF-TRA-02). Estes 2 últimos não fazem parte da lista formal dos 5 itens de
  CB-5, mas seguem o mesmo princípio: nunca tratados como Must Have sem
  confirmação técnica.

Esta ERF é insumo direto para:
- **Carlos Cronograma** (WBS e cronograma detalhado, Step seguinte) — usar a
  tabela MoSCoW da Seção 4 para priorizar sequenciamento (Must Have primeiro);
- **Pedro Perigo** (análise de riscos) — usar a Seção 5 (Perguntas Abertas)
  como insumo direto de riscos de requisito não especificado.

| Papel | Nome | Aprovação | Data |
|-------|------|-----------|------|
| Engenheiro de Requisitos | Rafael Requisito | Documento elaborado | 2026-07-07 |
| Solicitante — Financeiro | Alessandra Comério | PENDENTE (CB-4 em aberto) | ____ |
| Ponto focal — Suprimentos | Wellington Gonçalves | PENDENTE | ____ |
| Ponto focal — Riscos/Desempenho | Thamyris | PENDENTE | ____ |
| Líder técnico | Cássio | PENDENTE (confirmação CB-5) | ____ |
| PMO / Governança | Marcelo Silveira | PENDENTE | ____ |
| Sponsor | Paula Barcelos (CEO) | PENDENTE (CB-1 — evidência documental) | ____ |

**Status final desta ERF: RASCUNHO PARA REVISÃO — não deve ser tratada como
baseline de requisitos aprovada até resolução de CB-4 e CB-5, e aprovação
formal dos papéis acima.**
