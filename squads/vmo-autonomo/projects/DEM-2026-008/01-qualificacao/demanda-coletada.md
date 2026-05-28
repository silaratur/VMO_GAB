# Demanda Coletada
Data da Coleta: 2026-05-28
Coletado por: Iara Inbound (VMO Autônomo)
Canal de Entrada: múltiplos — ticket de service desk (texto direto) + histórico de interações + documento técnico de mapeamento (referenciado no anexo)

---

## Fontes Consultadas

| # | Canal | Tipo | Descrição | Data |
|---|-------|------|-----------|------|
| 1 | Ticket Service Desk | Texto direto | Ticket #6800446 — Sistemática ERP > Solicitação de Novas Demandas/Projetos | 08/05/2026 |
| 2 | Histórico do Ticket | Texto direto | Interações entre Mara, consultoras LinkUP, Ocean, Seletor e MW | 11/05/2026 a 26/05/2026 |
| 3 | Anexo técnico | PDF referenciado | "Mapeamento_SGMM03_InterCompany.pdf" — mapeamento técnico de campos SAP/SGM | 08/05/2026 |

---

## Dados da Demanda

**Solicitante**
- Nome: Jenifer dos Santos Carvalho
- Cargo: NÃO INFORMADO — requer esclarecimento
- Área/Divisão: VIX Matriz
- Contato: NÃO INFORMADO (apenas nome no ticket)
- Fonte: Ticket #6800446 (Fonte 1)

**Copiados / Partes Envolvidas**
- Jhonny Henrique M. F. de Freitas — VIX Matriz
- João Gabriel Virígio Barbierato — VIX Matriz
- Fonte: Ticket #6800446 (Fonte 1)

**Responsável pelo Ticket**
- Nome: Mara Rubia Silva Rocha
- Área: Holding DTI
- Papel: Gestão do chamado; articulação com fornecedores consultores
- Fonte: Ticket #6800446 (Fonte 1) + Histórico (Fonte 2)

**Necessidade de Negócio**
No processo de InterCompany da integração SGMM03 (SAP + SGM), quando a manutenção registra
uma Ordem de Manutenção (OM) no SGM, alguns dados inseridos nesse processo — especificamente
o campo "Empresa a Contrato" — não são integrados ao SAP. Isso obriga operadores a preencher
manualmente esses campos no SAP ou a realizarem correções pós-criação/alteração da OM.
O problema ocorre tanto na criação quanto na alteração de OMs, gerando retrabalho e risco
de inconsistência de dados entre os dois sistemas.
Fonte: Ticket #6800446 (Fonte 1) + Mapeamento_SGMM03_InterCompany.pdf (Fonte 3)

**Pedido Específico**
Integrar os campos "Empresa" e "Contrato" da OM (inseridos no SGM durante o processo de abertura
de OM pela manutenção) para que esses dados sejam automaticamente transmitidos ao SAP.
A integração deve suportar tanto a **criação** quanto a **alteração** de OMs no SAP,
permitindo que esses campos sejam gravados/atualizados via integração SGMM03.
Fonte: Ticket #6800446 (Fonte 1) — "integre os dados da Empresa a Contrato inseridos pela manutenção no processo de abertura de OM, que deverão permitir alteração destes campos no SAP, tanto na criação quanto na alteração de OM."

**Contexto Técnico Detalhado (do Mapeamento_SGMM03_InterCompany.pdf)**
- Integração: SAP + SGM via interface SGMM03 — fluxo InterCompany
- Campos já mapeados na OM SAP: Tipo de Ordem (SGCM), Prioridade, Locacional, Equipamento
  (ex: SRSCS14), Conjunto, Cenário/CenPlan (MAM1, MWV1 — campo crítico com restrição técnica),
  Modelo, Ordem
- Campo já entregue anteriormente: Centro de Planejamento (concluído)
- Campos desta demanda (pendentes): **Empresa** e **Contrato**
- Campo com restrição técnica conhecida: Cenário/CenPlan (MAM1, MWV1) — restrição de
  preenchimento identificada pelos consultores nas discussões
- Empresas envolvidas no fluxo técnico: INNOVATECH, GETEC (mencionadas nas discussões) + DTI
- Fonte: Mapeamento_SGMM03_InterCompany.pdf (Fonte 3) + Histórico (Fonte 2)

**Benefício Esperado**
- Eliminação de preenchimento manual dos campos Empresa e Contrato no SAP
- Eliminação de inconsistências de dados entre SGM e SAP para OMs InterCompany
- Agilidade no processo de abertura e alteração de OM — dados fluem automaticamente
- Redução de retrabalho da equipe de manutenção e TI
- Consistência do fluxo InterCompany completo na integração SGMM03
Fonte: Ticket #6800446 (Fonte 1)

**Urgência e Prazo**
- Prazo original do ticket: 15/05/2026
- SLA do ticket: EM ATRASO — 81h42min de atraso no momento da captura (ticket aberto em 08/05/2026)
- Urgência declarada: Pendente Fornecedor (status atual) — aguardando precificação de consultorias
- Data esperada de retorno dos fornecedores: 29/05/2026 (sexta-feira) — conforme histórico de 26/05
- Mara Rubia tentará equalizar propostas no dia 29/05/2026
- Origem do prazo: NÃO DECLARADA explicitamente — sem evento de negócio, contrato ou lei associados
- Impacto de não fazer: retrabalho contínuo no processo de abertura/alteração de OM InterCompany
Fonte: Ticket #6800446 (Fonte 1) + Histórico (Fonte 2)

**Aprovações e Autorizações Identificadas**
- Nenhuma aprovação formal de sponsor ou orçamento identificada nas fontes disponíveis
- O ticket está no fluxo normal de demandas do Sistemática ERP (Solicitação de Novas Demandas/Projetos)
- Consultoras em processo de precificação: LinkUP, Ocean, Seletor, MW (propostas sendo comparadas)
- Fonte: Histórico (Fonte 2)

**Contexto Organizacional**
- Divisão/empresa solicitante: VIX Matriz
- Área responsável: Holding DTI (gestão do chamado via Mara Rubia)
- Tipo de solução: Melhoria de integração SAP (módulo PM — Plant Maintenance / manutenção)
- Sistema origem: SGM (sistema de gestão de manutenção)
- Sistema destino: SAP
- Interface: SGMM03 — fluxo InterCompany
- Precedente: Campo "Centro de Planejamento" já foi integrado anteriormente na mesma interface
- Consultores envolvidos no processo: LinkUP, Ocean, Seletor, MW
- Centro de Custo: NÃO INFORMADO
- Orçamento aprovado: NÃO — em fase de precificação
- Fonte: Ticket #6800446 (Fonte 1) + Histórico (Fonte 2) + Mapeamento (Fonte 3)

**Stakeholders Identificados**
| Nome | Papel | Área | Fonte |
|------|-------|------|-------|
| Jenifer dos Santos Carvalho | Solicitante | VIX Matriz | Ticket |
| Jhonny Henrique M. F. de Freitas | Copiado — parte interessada | VIX Matriz | Ticket |
| João Gabriel Virígio Barbierato | Copiado — parte interessada | VIX Matriz | Ticket |
| Mara Rubia Silva Rocha | Responsável Holding DTI — gestão do chamado | Holding DTI | Ticket + Histórico |
| Consultoras (LinkUP, Ocean, Seletor, MW) | Fornecedores potenciais de execução | Externas | Histórico |
| INNOVATECH | Parte técnica envolvida nas discussões de mapeamento | Externa | Mapeamento |
| GETEC | Parte técnica envolvida nas discussões de mapeamento | Externa | Mapeamento |

**Contexto Implícito**
- A presença de 4 consultorias sendo consultadas simultaneamente (LinkUP, Ocean, Seletor, MW)
  indica que o grupo possui processo de cotação múltipla para demandas de consultoria SAP — o WR
  formal desta demanda deve ser preparado para este processo.
- O campo Cenário/CenPlan (MAM1, MWV1) foi identificado como "campo crítico com restrição" nas
  discussões técnicas — embora não seja o escopo desta demanda, a equipe de implementação precisa
  estar ciente da restrição ao trabalhar na mesma interface SGMM03.
- O fato de o campo "Centro de Planejamento" já ter sido entregue na mesma integração é um
  precedente técnico positivo — a consultora que o implementou pode ter vantagem de contexto.
- O SLA em atraso (81h42min) em conjunto com o processo de cotação ainda em andamento indica
  que não há urgência crítica de negócio — o prazo é de processo interno de PMO/DTI.
- Fonte: análise cruzada das Fontes 1, 2 e 3

---

## Lacunas Identificadas

| # | Campo | Status | Pergunta para Esclarecimento |
|---|-------|--------|------------------------------|
| L1 | Cargo da Solicitante | NÃO INFORMADO | Qual o cargo e área específica de Jenifer dos Santos Carvalho? |
| L2 | Sponsor formal | NÃO INFORMADO | Quem é o sponsor com nível Diretor ou superior responsável pela aprovação desta demanda? |
| L3 | Orçamento aprovado | NÃO — em precificação | Qual o envelope de orçamento aprovado ou referencial para esta melhoria? |
| L4 | Impacto em outras áreas | NÃO INFORMADO | Além da VIX Matriz, outras empresas/áreas usam o fluxo InterCompany SGMM03 e serão impactadas? |
| L5 | Volume de OMs afetadas | NÃO INFORMADO | Quantas OMs InterCompany são abertas/alteradas por mês? Qual o volume de retrabalho atual? |
| L6 | Documentação do processo atual | NÃO CONFIRMADO | Existe documentação do fluxo atual do SGMM03 além do Mapeamento_SGMM03_InterCompany.pdf? |
| L7 | Ambiente SAP | NÃO INFORMADO | Qual o ambiente SAP (cliente/mandante) e versão envolvidos na integração SGMM03? |
| L8 | Centro de Custo | NÃO INFORMADO | Qual o centro de custo para alocação desta demanda? |
| L9 | Prazo de negócio real | NÃO DECLARADO | Existe algum evento de negócio (auditoria, contrato, go-live) que exige esta entrega até uma data específica? |
| L10 | Status das propostas | AGUARDANDO | As propostas de Seletor e MW foram recebidas? O processo de equalização de 29/05 foi concluído? |

---

## Resumo para Confirmação

A VIX Matriz solicita a integração dos campos "Empresa" e "Contrato" da Ordem de Manutenção (OM)
do SGM para o SAP, via interface SGMM03 no fluxo InterCompany. Atualmente, esses campos são
preenchidos manualmente no SAP após a abertura da OM no SGM, gerando retrabalho e risco de
inconsistência. A demanda envolve criação e alteração de OMs. O ticket está em atraso de SLA
(81h42min), com 4 consultorias em processo de precificação — retorno esperado para 29/05/2026.
O campo "Centro de Planejamento" foi implementado anteriormente na mesma interface como precedente.
10 lacunas identificadas, sendo as mais críticas: sponsor não identificado, orçamento não aprovado
e impacto em outras áreas não avaliado.
