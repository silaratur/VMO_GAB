# Demanda Coletada — DEM-2026-007

**ID da Demanda:** DEM-2026-007
**Data da Coleta:** 2026-05-24
**Coletado por:** Iara Inbound (Coletora de Demandas — Squad VMO Autônomo)
**Canal de Entrada:** Ticket de Service Desk — Sistema Business Desk (Águia Branca)
**Projeto Vinculado:** PROJ-2026-007

---

## 1. Fontes Consultadas

| # | Fonte | Tipo | Conteúdo Extraído | Confiabilidade |
|---|-------|------|-------------------|----------------|
| F1 | Ticket #6813896 — Business Desk Águia Branca | Sistema de Gestão de Chamados | Todos os campos estruturados do ticket | Alta — sistema oficial |
| F2 | Campo "Descrição" do Ticket | Texto livre do solicitante | Objeto técnico da integração INT015 | Média — sem detalhamento técnico |
| F3 | Campo "Escopo Mapeado" do Ticket | Texto livre do solicitante | Fluxo de faturamento e integração GRLOG-SAP | Média — declaratório, requer validação |
| F4 | Campo "Ganhos Previstos" do Ticket | Texto livre do solicitante | Benefícios esperados (produtividade, receita, processo) | Média — sem métricas quantitativas |
| F5 | Campo "Norma/Requisito Legal" do Ticket | Dado estruturado | CPC 47 / IFRS 15 — Reconhecimento de Receita | Alta — norma identificada pelo solicitante |
| F6 | Campo "Justificativa de Urgência" do Ticket | Texto livre do solicitante | Demanda da CEO | Alta — declaração direta |
| F7 | Campo "Solução já existe no mercado" do Ticket | Dado estruturado | WAVE e Plataforma de Venda de Ativos | Média — sem detalhamento de aderência |
| F8 | Metadados do Ticket (datas, status, SLA) | Sistema Business Desk | Status Em Atraso, tempo ativo, datas de abertura/término | Alta — sistema oficial |

---

## 2. Dados da Demanda

### 2.1 Identificação

| Campo | Valor | Fonte |
|-------|-------|-------|
| ID da Demanda | DEM-2026-007 | Gerado pelo VMO |
| Número do Chamado | 6813896 | F1 |
| Título do Chamado | Sistematica ERP > Solicitacao de Novas Demandas / Projetos | F1 |
| Tipo de Atividade | Melhoria | F1 |
| Data de Abertura | 13/05/2026 às 20:50 | F1 / F8 |
| Data de Término Prevista | 20/05/2026 às 18:00 | F1 / F8 |
| Status do Chamado | Em Aberto | F1 / F8 |
| Situação do SLA | Em Atraso (18h05 de atraso registrado na coleta) | F1 / F8 |
| Tempo Ativo | 63:00 horas | F1 / F8 |

### 2.2 Solicitante e Partes Envolvidas

| Papel | Nome | Unidade | Fonte |
|-------|------|---------|-------|
| Solicitante / Beneficiado | Jairo De Melo Ferreira Mendes | VIX Matriz | F1 |
| Contato telefônico | 27988544297 | VIX Matriz | F1 |
| Copiado | Ana Silvia Calegari | VIX Matriz | F1 |
| Copiado | Cassio Ribeiro Rosa | Holding DTI | F1 |
| Copiado | Kelli Catrinque Furtulino | VIX Matriz | F1 |
| Grupo Solucionador | Projetos DTI (último acesso 23/05/2026 12:06) | Holding DTI | F1 |
| Grupo SAN | 1 Nivel — Corporativo (último acesso 15/05/2026 16:57) | Corporativo | F1 |
| Responsável pelo Chamado | Não Informado | — | F1 |
| Sponsor / Patrocinador | **LACUNA — ver Seção 4** | — | — |

### 2.3 Pedido Técnico (o que foi solicitado)

| Campo | Valor | Fonte |
|-------|-------|-------|
| Objeto da Integração | Integração GRLOG com SAP — código interno INT015 | F1 / F2 |
| Sistemas Envolvidos | GRLOG (Sistema de Gestão de Receita) e SAP (ERP) | F1 / F2 / F3 |
| Funcionalidades Solicitadas | Geração de ordens de vendas; emissão de faturamento; suporte a NFSe e Recibo; contabilização de Nota de Débito; retorno dos documentos emitidos ao GRLOG | F2 / F3 |
| Escopo Declarado pelo Solicitante | "O GRLOG possui os contratos e medições realizadas no sistema; é necessário incluir o fluxo de faturamento para integrar com o SAP, realizar a emissão dos documentos e retornar ao GRLOG com esses documentos." | F3 |
| Trigger do Processo | Medições realizadas e aprovadas no GRLOG | F2 |

### 2.4 Necessidade de Negócio (problema real subjacente)

> **Distinção aplicada:** O pedido técnico é a integração INT015. A necessidade de negócio é o reconhecimento de receita tempestivo, em conformidade com CPC 47 / IFRS 15, eliminando o risco de faturamento pendente e retrabalho operacional.

| Campo | Valor | Fonte |
|-------|-------|-------|
| Problema Central | Processo de faturamento não integrado entre GRLOG e SAP, gerando emissão de documentos fora do prazo, trabalho manual, conferências e retrabalho | F3 / F4 |
| Consequência Operacional | Faturamento pendente; aumento de conferências manuais; redução da produtividade da equipe de operações | F4 |
| Consequência Regulatória | Risco de não conformidade com CPC 47 / IFRS 15 — Reconhecimento de Receita | F5 |
| Impacto Estratégico | Demanda direta da CEO — contexto de urgência executiva | F6 |

### 2.5 Restrições

| Restrição | Descrição | Fonte |
|-----------|-----------|-------|
| Restrição Orçamentária | Expectativa de investimento menor que R$10.000; investimento **não aprovado** na data de abertura do chamado | F1 |
| Restrição de Prazo | Data de término prevista já ultrapassada (20/05/2026); SLA em atraso de 18h05 | F1 / F8 |
| Restrição Legal | Conformidade obrigatória com CPC 47 / IFRS 15 | F5 |
| Restrição de Processo | Processo de negócio não documentado formalmente | F1 |

### 2.6 Premissas Declaradas pelo Solicitante

| Premissa | Origem | Fonte |
|----------|--------|-------|
| O GRLOG já possui os contratos e medições aprovadas como base do faturamento | Escopo mapeado pelo solicitante | F3 |
| Existe fluxo de integração a ser adicionado ao GRLOG (não apenas configuração SAP) | Escopo mapeado pelo solicitante | F3 |
| A área de negócio possui escopo detalhado disponível | Campo estruturado do ticket (marcado "SIM") | F1 |
| Projetos similares já foram implantados no GAB (WAVE e Plataforma de Venda de Ativos) | Campo estruturado do ticket | F7 |
| Soluções de mercado existentes foram consideradas (WAVE e Plataforma de Venda de Ativos) | Campo estruturado do ticket | F7 |

### 2.7 Classificações e Indicadores

| Campo | Valor | Observação | Fonte |
|-------|-------|------------|-------|
| Criticidade | 1 — Emergencial | Afeta serviço/operação crítica; risco operacional e legal | F1 |
| Necessidade Legal / Obrigatória | SIM | CPC 47 / IFRS 15 | F5 |
| Envolve Outras Áreas de Negócio | SIM | Diretoria de Logística Dedicada | F1 |
| Envolve Outras Divisões | NÃO | Conforme declarado | F1 |
| Requer Integração com Outros Sistemas | SIM | GRLOG e SAP | F1 |
| Identificador do Projeto | Não Informado | **LACUNA — ver Seção 4** | F1 |
| Classificação da Demanda | Não Selecionado | **LACUNA — ver Seção 4** | F1 |
| Tipo da Requisição | Não Selecionado | **LACUNA — ver Seção 4** | F1 |
| Centro de Custo / Imobilizado | 2800171-0 | Informado pelo solicitante | F1 |
| Investimento Aprovado | NÃO | Orçamento pendente de aprovação | F1 |
| Aumento de Receita Esperado | SIM | Faturamento integrado e no prazo | F4 |
| Redução de Custo Esperada | NÃO | Conforme declarado | F1 |
| Melhoria de Processo Esperada | SIM | Redução de trabalho manual e retrabalho | F4 |
| Aumento de Produtividade Esperado | SIM | Aumento no volume de faturamento diário | F4 |
| Indicador de Ganhos | Volume de emissão diário por usuário | Sem linha de base declarada | F4 |

---

## 3. Contexto Implícito Registrado

> Esta seção documenta informações que não foram declaradas de forma direta mas emergem da leitura combinada dos campos do ticket. Todo item desta seção requer confirmação explícita antes de uso em documentos decisórios.

| # | Contexto Implícito | Evidência | Flag |
|---|-------------------|-----------|------|
| CI-01 | A demanda possui patrocínio executivo de alto nível (CEO), o que pressiona o prazo e eleva o risco político de atraso | Justificativa de urgência: "Atendimento a demanda da CEO" | INFERIDO — confirmar |
| CI-02 | O SLA já está em atraso e o grupo solucionador não possui responsável nomeado, indicando risco de governança interna no encaminhamento | Situação SLA "Em Atraso 18h05"; campo Responsável: "Não Informado" | INFERIDO — confirmar |
| CI-03 | A ausência de investimento aprovado com criticidade Emergencial sugere possível demanda iniciada sem rito formal de aprovação orçamentária | Criticidade "1 — Emergencial" combinada com "Investimento Aprovado: NÃO" | INFERIDO — confirmar |
| CI-04 | Os projetos WAVE e Plataforma de Venda de Ativos mencionados como referência podem ter documentação técnica ou arquitetura aproveitável para a integração INT015 | Campos "Solução no mercado" e "Projeto semelhante implantado" apontam para os mesmos sistemas | INFERIDO — confirmar |
| CI-05 | A participação da Holding DTI (Cassio Ribeiro Rosa copiado; Grupo Solucionador = Projetos DTI) indica que a demanda envolve governança corporativa além da VIX Matriz | Lista de participantes do ticket | INFERIDO — confirmar |
| CI-06 | O campo "Área de negócio possui escopo detalhado: SIM" indica que existe documentação de escopo não anexada ao ticket — esse material precisa ser solicitado formalmente | Campo estruturado do ticket | INFERIDO — confirmar |

---

## 4. Lacunas Identificadas

| # | Lacuna | Campo Afetado | Impacto | Pergunta de Esclarecimento para o Solicitante |
|---|--------|---------------|---------|-----------------------------------------------|
| L-01 | Responsável técnico pelo chamado não informado | Campo "Responsável" = "Não Informado" | Alto — impede designação formal e acompanhamento | Quem é o responsável técnico pelo encaminhamento deste chamado no Projetos DTI? |
| L-02 | Investimento não aprovado com criticidade Emergencial | Campo "Investimento Aprovado: NÃO" | Alto — impede início formal do projeto | Qual é o rito e prazo previsto para aprovação orçamentária do investimento (< R$10K)? Existe autorização verbal ou por e-mail da CEO que possa ser formalizada? |
| L-03 | Identificador do Projeto não informado | Campo "Identificador do Projeto: Não Informado" | Médio — dificulta rastreabilidade no portfólio | Este projeto possui algum código ou identificador interno no portfólio de TI do GAB? |
| L-04 | Classificação da Demanda e Tipo da Requisição não selecionados | Campos "Classificação da Demanda" e "Tipo da Requisição" = "Não Selecionado" | Médio — impede categorização no portfólio VMO | O solicitante pode selecionar a classificação e o tipo de requisição no sistema Business Desk? |
| L-05 | Processo de negócio não documentado | Campo "Processo Documentado: NÃO" | Alto — impede especificação funcional adequada | Existe BPMN, fluxograma ou descrição textual do processo de faturamento atual (AS-IS)? Se não, quando pode ser elaborado? |
| L-06 | Escopo detalhado mencionado como existente mas não anexado | Campo "Área de negócio possui escopo detalhado: SIM" + ausência de anexo | Alto — escopo declarado não está disponível para análise | Onde está o documento de escopo detalhado? Pode ser compartilhado com o time do Projetos DTI? |
| L-07 | Sponsor / Patrocinador formal não identificado | Ausência do campo no ticket | Alto — necessário para aprovação de mudanças e conflitos | Quem é o patrocinador formal deste projeto? É o próprio solicitante (Jairo Mendes) ou há outro executivo responsável? |
| L-08 | Linha de base do indicador de ganhos ausente | Indicador "volume de emissão diário por usuário" declarado sem valor atual | Médio — impede mensuração do benefício realizado | Qual é o volume atual de emissão diária de documentos por usuário no processo manual? |
| L-09 | Prazo desejado / comprometido não declarado | Campos de prazo preenchidos apenas com data do SLA do chamado | Alto — SLA vencido; prazo real do projeto desconhecido | Qual é o prazo que a CEO espera para a entrega desta integração? Existe data-limite associada à conformidade CPC 47 / IFRS 15? |
| L-10 | Envolvimento da Diretoria de Logística Dedicada não detalhado | Campo "Projeto envolve outras áreas de negócio: SIM — Diretoria de Logística Dedicada" | Médio — escopo de impacto e aprovação desconhecido | Qual é o papel da Diretoria de Logística Dedicada neste projeto: usuária do sistema, aprovadora de requisitos ou impactada pelo faturamento? |

---

## 5. Inconsistências Detectadas

| # | Inconsistência | Descrição | Ação Recomendada |
|---|---------------|-----------|-----------------|
| INC-01 | Criticidade Emergencial x Investimento Não Aprovado | Um chamado Emergencial pressupõe ação imediata, mas o investimento não foi aprovado. Isso cria bloqueio estrutural para início do projeto. | Confirmar com Jairo Mendes e Projetos DTI se há caminho de aprovação acelerada dado o status emergencial. |
| INC-02 | SLA Vencido x Responsável Não Informado | O chamado está em atraso há 18h05 sem responsável designado no grupo solucionador. | Escalada interna ao Projetos DTI para nomeação imediata de responsável. |
| INC-03 | Prazo do Chamado já Ultrapassado (20/05/2026) x Status "Em Aberto" | A data de término prevista passou há 4 dias em relação à data de coleta (24/05/2026). | Renegociação do prazo formal com o solicitante e atualização no Business Desk. |

---

## 6. Resumo da Demanda (para Confirmação com o Solicitante)

**DEM-2026-007 — Integração GRLOG-SAP (INT015): Faturamento Integrado por Medições Aprovadas**

O solicitante Jairo De Melo Ferreira Mendes (VIX Matriz) abriu o chamado #6813896 em 13/05/2026 solicitando a integração entre o GRLOG (Sistema de Gestão de Receita) e o SAP (ERP) para automatizar o fluxo de faturamento a partir de medições aprovadas, com geração de ordens de venda, emissão de documentos fiscais (NFSe, Recibo) e contabilização de Notas de Débito.

A necessidade de negócio subjacente é garantir o reconhecimento de receita de forma tempestiva e em conformidade com CPC 47 / IFRS 15, eliminando o processo manual atual que gera atrasos, retrabalho e risco regulatório. A demanda foi classificada como Emergencial com urgência declarada por determinação da CEO do grupo.

O chamado apresenta SLA em atraso (18h05), responsável técnico não designado e investimento sem aprovação formal. Adicionalmente, o processo de negócio atual não está documentado e o escopo detalhado mencionado pelo solicitante como existente não foi anexado ao ticket.

Antes do início formal da qualificação, o VMO requer: (1) nomeação do responsável técnico no Projetos DTI, (2) envio do documento de escopo detalhado, (3) confirmação do prazo esperado pela CEO, (4) início do rito de aprovação orçamentária, e (5) confirmação do sponsor formal do projeto.

---

## 7. Próximas Ações Recomendadas

| # | Ação | Responsável Sugerido | Prazo Sugerido |
|---|------|----------------------|----------------|
| A-01 | Nomear responsável técnico no chamado (Projetos DTI) | Gestor do Grupo Projetos DTI | Imediato |
| A-02 | Solicitar formalmente o documento de escopo detalhado ao solicitante | Iara Inbound / VMO | Imediato |
| A-03 | Acionar rito de aprovação orçamentária (< R$10K — Emergencial) | Jairo De Melo Ferreira Mendes | 24-48 horas |
| A-04 | Confirmar prazo esperado pela CEO para entrega | Jairo De Melo Ferreira Mendes | Imediato |
| A-05 | Identificar e confirmar o sponsor formal do projeto | VMO / Projetos DTI | 24 horas |
| A-06 | Obter documentação do processo atual (AS-IS) da Diretoria de Logística Dedicada | Jairo De Melo Ferreira Mendes | A combinar |
| A-07 | Levantar artefatos dos projetos WAVE e Plataforma de Venda de Ativos para reuso | Projetos DTI | A combinar |

---

## 8. Checklist de Qualidade (Iara Inbound)

- [x] Canal de entrada identificado e documentado
- [x] Todas as fontes consultadas listadas (F1 a F8)
- [x] Cada campo tem referência explícita à fonte
- [x] Necessidade de negócio distinguida do pedido técnico (Seções 2.3 e 2.4)
- [x] Lacunas documentadas com perguntas específicas (10 lacunas — Seção 4)
- [x] Contexto implícito registrado com flag "INFERIDO — confirmar" (Seção 3)
- [x] ID DEM-2026-007 gerado
- [x] Resumo de confirmação para o solicitante incluído (Seção 6)
- [x] Inconsistências detectadas e documentadas (Seção 5)
- [x] Próximas ações recomendadas listadas (Seção 7)

---

*Documento gerado pelo Squad VMO Autônomo — Iara Inbound (Coletora de Demandas)*
*Data de geração: 2026-05-24*
*Versão: 1.0*
