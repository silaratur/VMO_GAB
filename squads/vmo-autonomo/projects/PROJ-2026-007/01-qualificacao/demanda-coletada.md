# Demanda Coletada
Data da Coleta: 2026-05-31
Coletado por: Iara Inbound
Canal de Entrada: múltiplos — ticket de service desk (PDF) + documento técnico anexado (PDF)

## Fontes Consultadas

| # | Canal | Tipo | Descrição | Data |
|---|-------|------|-----------|------|
| 1 | ticket | PDF | Chamado 6800446 — Sistemática ERP > Solicitação de Novas Demandas / Projetos | 08/05/2026 |
| 2 | documento técnico | PDF | Mapeamento_SGMM03_InterCompany.pdf — email técnico [SGM] Integração SAP + SGM (SGM 003) - Atendimento InterCompany | 08/05/2026 |

## Dados da Demanda

**Solicitante**
- Nome: Jenifer dos Santos Carvalho
- Cargo: NÃO INFORMADO — requer esclarecimento
- Área/Divisão: VIX Matriz
- Contato: NÃO INFORMADO — requer esclarecimento
- Fonte: Chamado 6800446, campo "Solicitante"

**Responsável Técnico (Holding DTI)**
- Nome: Mara Rubia Silva Rocha
- Área: Holding DTI — Grupo Solucionador: Projetos DTI
- Papel: Responsável pelo chamado e pela gestão das propostas
- Fonte: Chamado 6800446, campos "Responsável" e "Grupo Solucionador"

**Participantes Adicionais Identificados**
- Jhonny Henrique M. F. de Freitas (VIX Matriz) — copiado no chamado
- João Gabriel Virginio Barbierato (VIX Matriz) — copiado no chamado; remetente do email técnico
- Marcelo Válério Silveira (Holding DTI) — destinatário do email técnico de mapeamento
- Thayna Borges De Souza, Johann Henrique, José Victor Teixeira Bobillo — copiados no email técnico
- Técnicos de INNOVATECH e GETEC — participam da discussão técnica mencionada no documento
- Fonte: Chamado 6800446, campo "Copiados" + Mapeamento_SGMM03_InterCompany.pdf

**Necessidade de Negócio**
O sistema SGMM03 (sistema de gestão de manutenção) envia dados para o SAP no processo InterCompany, mas os campos "Empresa a Contrato" inseridos pela área de manutenção na abertura de Ordens de Manutenção (OM) não são integrados ao SAP. Sem essa integração, o SAP não recebe os dados que precisa para processar corretamente as OM no fluxo InterCompany, comprometendo a rastreabilidade e o controle financeiro intercompanhia. O campo CenPlan (Cenário) — com valores MAM1 e MWV1 — está identificado como campo crítico com restrição ativa no SAP (destacado em vermelho na tela), indicando bloqueio funcional real.
Fonte: Chamado 6800446, campo "Descrição da Demanda" + Mapeamento_SGMM03_InterCompany.pdf

**Pedido Específico**
Desenvolver integração no SGMM03 para que os dados de "Empresa a Contrato" inseridos na abertura de OM sejam transmitidos ao SAP, com permissão de alteração desses campos no SAP tanto no momento de criação quanto de alteração de OM. O escopo mínimo identificado no documento técnico inclui os campos: Empresa, Contrato e Cenário (CenPlan). A integração de Centro de Planejamento já está entregue — esta demanda cobre o restante.
Fonte: Chamado 6800446, "Descrição da Demanda" + Mapeamento_SGMM03_InterCompany.pdf

**Benefício Esperado**
Permitir o fluxo completo InterCompany no SAP com dados de Empresa e Contrato provenientes do SGMM03, eliminando o bloqueio do campo CenPlan e garantindo a integridade dos dados de OM. Benefício quantificado: NÃO INFORMADO.
Fonte: Inferido a partir da descrição da demanda e do documento técnico

**Urgência e Prazo**
- Prazo desejado: NÃO INFORMADO — deadline de produção não declarado no chamado
- Urgência declarada: Alta (SLA do chamado já expirado em 81:42h; atraso de aproximadamente 13 dias além do prazo original de 15/05/2026)
- Origem do prazo: Prazo do ticket (1 semana a partir de 08/05/2026 = 15/05/2026) — já vencido. Prazo de recebimento de propostas de consultoria: 29/05/2026 (já vencido na data desta coleta)
- SLA do ticket: Em Atraso — 81:42 horas decorridas além do prazo
- Fonte: Chamado 6800446, campos de datas + histórico de atuações de 26/05/2026 e 11/05/2026

**Aprovações e Autorizações Identificadas**
- Nenhuma aprovação formal de orçamento ou sponsor executivo documentada nas fontes
- A gestão das propostas está sendo conduzida por Mara Rubia Silva Rocha (Holding DTI), responsável técnica — não há evidência de autorização de nível gerencial/diretivo para contratação
- Fonte: Histórico de atuações do Chamado 6800446

**Contexto Organizacional**
- Divisão/empresa: VIX Matriz (solicitante) + Holding DTI (responsável pela solução)
- Área executora: Projetos DTI (Holding) — com provável contratação de consultoria externa
- Projetos relacionados: Integração SAP + SGM (SGM 003) — projeto de integração mais amplo do qual esta demanda é um entregável parcial (Centro de Planejamento já entregue)
- Restrições conhecidas: campo CenPlan com restrição ativa no SAP (vermelho); processo de contratação de consultoria em andamento com 4 fornecedores consultados (LinkUP, Ocean, Seletor, MW)
- Contexto de mercado: processo competitivo de cotação com múltiplos fornecedores — indica ausência de fornecedor preferencial ou contrato vigente para este tipo de demanda
- Fonte: Chamado 6800446 + Mapeamento_SGMM03_InterCompany.pdf

**Contexto Implícito**
1. **Urgência real maior que declarada**: O ticket já está em atraso há 13+ dias e o prazo original (15/05) já foi superado. A equipe DTI está gerenciando múltiplas rodadas de cotação desde 11/05, indicando que a pressão para resolver é alta mas a capacidade de execução direta é limitada (dependência de terceiros).
2. **Escopo potencialmente maior**: O documento de mapeamento lista vários campos SAP (Tipo de Ordem, Prioridade, Locacional, Equipamento, Conjunto, Cenário, Modelo, Ordem) — há risco de que o escopo real seja mais amplo que o descrito no chamado, o que pode impactar significativamente o orçamento e prazo.
3. **Relação com projeto maior**: A menção de que "Centro de Planejamento já entrega" indica que esta é uma evolução de uma integração existente, não um desenvolvimento do zero — o que pode simplificar o escopo mas também introduz riscos de compatibilidade com o que já está em produção.
4. **Sponsor executivo ausente**: Nenhum nome de sponsor de nível Diretor ou superior identificado — risco para aprovação de orçamento e tomada de decisão.
- Fonte: Análise cruzada de Chamado 6800446 + Mapeamento_SGMM03_InterCompany.pdf

## Lacunas Identificadas

| # | Campo | Status | Pergunta para Esclarecimento |
|---|-------|--------|------------------------------|
| 1 | Sponsor executivo | NÃO INFORMADO | Quem é o sponsor executivo desta demanda (nível Diretor ou superior) com autoridade para aprovar orçamento e prioridade? |
| 2 | Budget máximo aprovado | NÃO INFORMADO | Qual é o orçamento máximo aprovado para esta contratação? Existe aprovação formal (CAPEX/OPEX)? |
| 3 | Deadline de produção | NÃO INFORMADO | Qual é a data crítica de entrada em produção? Existe algum evento de negócio (fechamento, auditoria, contrato) que defina esse prazo? |
| 4 | Escopo exato dos campos | PARCIALMENTE INFORMADO | O escopo abrange apenas os campos Empresa, Contrato e CenPlan, ou todos os campos listados no mapeamento (Prioridade, Locacional, Equipamento, Conjunto, Modelo, Ordem)? |
| 5 | Impacto de negócio atual | NÃO INFORMADO | Qual processo de negócio está sendo impactado hoje pela ausência desta integração? Há impacto financeiro ou operacional mensurável? |
| 6 | Cargo da solicitante | NÃO INFORMADO | Qual o cargo de Jenifer dos Santos Carvalho na VIX Matriz? |
| 7 | Contato da solicitante | NÃO INFORMADO | Qual o e-mail ou ramal de Jenifer dos Santos Carvalho para esclarecimentos? |
| 8 | Status das propostas pós-29/05 | NÃO INFORMADO | As propostas de LinkUP, Ocean, Seletor e MW foram recebidas até 29/05/2026? Alguma foi selecionada? |

## Resumo para Confirmação

> "Entendemos que a VIX Matriz necessita que o SAP receba, via integração com o SGMM03, os dados de 'Empresa a Contrato' inseridos na abertura de Ordens de Manutenção (OM), no contexto do processo InterCompany. Atualmente, o campo CenPlan (Cenário) está bloqueado no SAP (restrição em vermelho), impedindo o fluxo completo. A solução deve permitir tanto criação quanto alteração de OM com esses dados integrados. O chamado está em atraso desde 15/05/2026 e aguarda propostas de consultoria externa (prazo: 29/05/2026).
>
> Precisamos confirmar: (1) quem é o sponsor executivo da demanda; (2) qual o budget aprovado; (3) qual a data crítica de entrada em produção; (4) se o escopo se limita a Empresa/Contrato/CenPlan ou abrange outros campos do mapeamento."
