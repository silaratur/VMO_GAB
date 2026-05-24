# Demanda Coletada — DEM-2026-007

**ID da Demanda:** DEM-2026-007
**Data da Coleta:** 2026-05-24
**Coletado por:** Iara Inbound (Coletora de Demandas — Squad VMO Autônomo)
**Canal de Entrada:** Ticket de Service Desk — Sistema Business Desk (Águia Branca)
**Projeto Vinculado:** PROJ-2026-007
**Versão:** 1.0

---

## 1. Fontes Consultadas

| # | Fonte | Tipo | Conteúdo Extraído | Confiabilidade |
|---|-------|------|-------------------|----------------|
| F1 | Ticket #6813896 — Business Desk Águia Branca | Sistema oficial de gestão de chamados | Todos os campos estruturados do ticket: identificação, status, SLA, participantes, dados adicionais | Alta — sistema oficial |
| F2 | Campo "Descrição" do Ticket | Texto livre do solicitante | Objeto técnico da integração INT015; documentos envolvidos (NFSe, Recibo, Nota de Débito) | Média — sem detalhamento técnico |
| F3 | Campo "Escopo Mapeado" do Ticket | Texto livre do solicitante | Fluxo de faturamento; integração GRLOG-SAP; retorno de documentos ao GRLOG | Média — declaratório, requer validação |
| F4 | Campo "Ganhos Previstos" / "Indicador de Ganhos" do Ticket | Texto livre do solicitante | Benefícios esperados: produtividade, receita, processo | Média — sem métricas quantitativas ou linha de base |
| F5 | Campo "Norma/Requisito Legal" do Ticket | Dado estruturado | CPC 47 / IFRS 15 — Reconhecimento de Receita | Alta — norma identificada pelo solicitante |
| F6 | Campo "Justificativa de Urgência" do Ticket | Texto livre do solicitante | Demanda originada pela CEO | Alta — declaração direta |
| F7 | Campos "Solução já existe no mercado" e "Projeto semelhante já implantado no GAB" | Dado estruturado | WAVE e Plataforma de Venda de Ativos como referências | Média — sem detalhamento de aderência ou arquitetura |
| F8 | Metadados do Ticket (datas, status, SLA, participantes) | Sistema Business Desk | Status Em Aberto; SLA Em Atraso 18h05; tempo ativo 63h; datas de abertura e término previsto | Alta — sistema oficial |

---

## 2. Dados da Demanda

### 2.1 Identificação

| Campo | Valor | Fonte |
|-------|-------|-------|
| ID da Demanda | DEM-2026-007 | Gerado pelo Squad VMO Autônomo |
| Número do Chamado | 6813896 | F1 |
| Título do Chamado | Sistematica ERP > Solicitacao de Novas Demandas / Projetos | F1 |
| Tipo de Atividade | Melhoria | F1 |
| Data de Abertura | 13/05/2026 às 20:50 | F1 / F8 |
| Data de Término Prevista (SLA) | 20/05/2026 às 18:00 | F1 / F8 |
| Status do Chamado | Em Aberto | F1 / F8 |
| Situação do SLA | Em Atraso (18h05 de atraso registrado em 13/05/2026; tempo ativo: 63h00 em aberto) | F1 / F8 |
| Última Ação Registrada | Enviar para Grupo Solucionador — 13/05/2026 às 20:50 | F1 |

### 2.2 Solicitante e Partes Envolvidas

| Papel | Nome | Unidade | Fonte |
|-------|------|---------|-------|
| Solicitante / Beneficiado | Jairo De Melo Ferreira Mendes | VIX Matriz | F1 |
| Contato Telefônico | 27988544297 | VIX Matriz | F1 |
| Copiado | Ana Silvia Calegari | VIX Matriz | F1 |
| Copiado | Cassio Ribeiro Rosa | Holding DTI | F1 |
| Copiado | Kelli Catrinque Furtulino | VIX Matriz | F1 |
| Grupo Solucionador | Projetos DTI (último acesso: 23/05/2026 às 12:06) | Holding DTI | F1 |
| Grupo SAN | 1 Nível — Corporativo (último acesso: 15/05/2026 às 16:57) | Corporativo | F1 |
| Responsável pelo Chamado | **Não Informado** | — | F1 |
| Sponsor / Patrocinador Formal | **LACUNA — ver Seção 4 (L-07)** | — | — |

### 2.3 Pedido Técnico (o que foi solicitado)

> Esta seção registra o pedido conforme declarado pelo solicitante, sem interpretação adicional.

| Campo | Valor | Fonte |
|-------|-------|-------|
| Nome da Integração | Integração GRLOG com SAP — código interno: INT015 | F1 / F2 |
| Sistemas Envolvidos | GRLOG (Sistema de Gestão de Receita) e SAP (ERP corporativo) | F1 / F2 / F3 |
| Funcionalidades Solicitadas | (1) Geração de ordens de vendas; (2) faturamento para documentos NFSe e Recibo; (3) contabilização de Nota de Débito; (4) retorno dos documentos emitidos ao GRLOG | F2 / F3 |
| Trigger do Processo | Medições realizadas e aprovadas no GRLOG | F2 |
| Escopo Declarado pelo Solicitante | "O GRLOG possui os contratos e medições realizadas no sistema; é necessário incluir o fluxo de faturamento para integrar com o SAP, realizar a emissão dos documentos e retornar ao GRLOG com esses documentos." | F3 |

### 2.4 Necessidade de Negócio (problema real subjacente)

> **Distinção aplicada (PMO):** O pedido técnico é a implementação da integração INT015. A necessidade de negócio é garantir o reconhecimento de receita de forma tempestiva, automática e em conformidade regulatória, eliminando riscos operacionais e financeiros decorrentes do processo manual atual.

| Campo | Valor | Fonte |
|-------|-------|-------|
| Problema Central | Processo de faturamento não integrado entre GRLOG e SAP, resultando em emissão de documentos fora do prazo, execução manual de conferências e retrabalho operacional | F3 / F4 |
| Consequência Operacional | Faturamento pendente; aumento de conferências manuais; redução do volume diário de documentos emitidos por usuário; retrabalho da equipe de operações | F4 |
| Consequência Regulatória | Risco de não conformidade com CPC 47 / IFRS 15 — Reconhecimento de Receita | F5 |
| Impacto Estratégico | Demanda originada pela CEO do Grupo Águia Branca — contexto de urgência executiva | F6 |
| Área Impactada | Diretoria de Logística Dedicada | F1 |

### 2.5 Restrições

| # | Restrição | Descrição | Fonte |
|---|-----------|-----------|-------|
| R-01 | Restrição Orçamentária | Expectativa de investimento menor que R$10.000; investimento **não aprovado** na data de coleta | F1 |
| R-02 | Restrição de Prazo | Data de término prevista pelo SLA (20/05/2026) já ultrapassada; prazo real do projeto não declarado | F1 / F8 |
| R-03 | Restrição Legal | Conformidade obrigatória com CPC 47 / IFRS 15 — norma de reconhecimento de receita | F5 |
| R-04 | Restrição de Processo | Processo de negócio atual (AS-IS) não documentado formalmente | F1 |
| R-05 | Restrição de Governança | Responsável técnico no grupo solucionador não designado; chamado sem avanço desde a abertura | F1 / F8 |

### 2.6 Premissas Declaradas pelo Solicitante

| # | Premissa | Origem | Fonte |
|---|----------|--------|-------|
| P-01 | O GRLOG já possui os contratos e as medições aprovadas como base de dados para o faturamento | Escopo mapeado pelo solicitante | F3 |
| P-02 | A inclusão do fluxo de faturamento será realizada no GRLOG (não apenas configuração no SAP) | Escopo mapeado pelo solicitante | F3 |
| P-03 | A área de negócio possui escopo detalhado disponível para compartilhamento | Campo estruturado do ticket marcado como "SIM" | F1 |
| P-04 | Projetos similares já foram implantados no GAB: WAVE e Plataforma de Venda de Ativos | Campo estruturado do ticket | F7 |
| P-05 | Soluções de mercado equivalentes existem e foram identificadas (WAVE e Plataforma de Venda de Ativos) | Campo estruturado do ticket | F7 |

### 2.7 Classificações e Indicadores

| Campo | Valor | Observação | Fonte |
|-------|-------|------------|-------|
| Criticidade | 1 — Emergencial | Afeta serviço/operação crítica; risco operacional e legal identificados | F1 |
| Necessidade Legal / Obrigatória | SIM | CPC 47 / IFRS 15 — Reconhecimento de Receita | F5 |
| Envolve Outras Áreas de Negócio | SIM | Diretoria de Logística Dedicada | F1 |
| Envolve Outras Divisões | NÃO | Conforme declarado pelo solicitante | F1 |
| Requer Integração com Outros Sistemas | SIM | GRLOG e SAP | F1 |
| Centro de Custo / Imobilizado | 2800171-0 | Informado pelo solicitante | F1 |
| Identificador do Projeto | Não Informado | **LACUNA — ver Seção 4 (L-03)** | F1 |
| Classificação da Demanda | Não Selecionado | **LACUNA — ver Seção 4 (L-04)** | F1 |
| Tipo da Requisição | Não Selecionado | **LACUNA — ver Seção 4 (L-04)** | F1 |
| Investimento Aprovado | NÃO | Orçamento pendente de aprovação formal | F1 |
| Expectativa de Investimento | Menor de R$10.000 | Declarado pelo solicitante; sem detalhamento de base de cálculo | F1 |
| Aumento de Receita Esperado | SIM | "Faturamento integrado e no prazo da solicitação evitando faturamento pendente" | F4 |
| Redução de Custo Esperada | NÃO | Conforme declarado pelo solicitante | F1 |
| Melhoria de Processo Esperada | SIM | "Redução de trabalho e conferências manuais e retrabalho para a operação" | F4 |
| Aumento de Produtividade Esperado | SIM | "Aumento no volume de faturamento diário" | F4 |
| Indicador de Ganhos | Volume de emissão diário por usuário | Sem linha de base declarada — **LACUNA L-08** | F4 |

---

## 3. Contexto Implícito Registrado

> Esta seção documenta informações que emergem da leitura combinada dos campos do ticket, mas que não foram declaradas de forma direta pelo solicitante. Todo item desta seção requer confirmação explícita antes de uso em documentos decisórios ou planejamentos formais.

| # | Contexto Implícito | Evidência no Ticket | Flag |
|---|-------------------|---------------------|------|
| CI-01 | A demanda possui patrocínio executivo de alto nível (CEO), o que pressiona o prazo e eleva o risco político de atraso ou depriorizacão | Campo "Justificativa de Urgência": "Atendimento a demanda da CEO" | INFERIDO — confirmar |
| CI-02 | O SLA já está em atraso e o grupo solucionador não possui responsável nomeado, indicando risco de governança interna no encaminhamento da demanda | Situação SLA "Em Atraso 18h05"; campo Responsável: "Não Informado"; última ação em 13/05/2026 | INFERIDO — confirmar |
| CI-03 | A ausência de investimento aprovado combinada com criticidade Emergencial sugere que a demanda foi iniciada sem o rito formal de aprovação orçamentária | Criticidade "1 — Emergencial" + "Investimento Aprovado: NÃO" | INFERIDO — confirmar |
| CI-04 | Os projetos WAVE e Plataforma de Venda de Ativos mencionados como referência podem conter documentação técnica ou arquitetura aproveitável para acelerar a integração INT015 | Campos "Solução no mercado" e "Projeto semelhante implantado" apontam para os mesmos dois sistemas | INFERIDO — confirmar |
| CI-05 | A participação da Holding DTI (Cassio Ribeiro Rosa copiado; Grupo Solucionador = Projetos DTI) indica que a demanda envolve governança corporativa além da VIX Matriz, com possível impacto em padrões de integração corporativa | Lista de participantes do ticket | INFERIDO — confirmar |
| CI-06 | O campo "Área de negócio possui escopo detalhado: SIM" indica que existe documentação de escopo não anexada ao ticket — este material é crítico para o início da qualificação e deve ser solicitado formalmente | Campo estruturado do ticket + ausência de qualquer anexo | INFERIDO — confirmar |

---

## 4. Lacunas Identificadas

| # | Lacuna | Campo Afetado no Ticket | Impacto na Qualificação | Pergunta de Esclarecimento para o Solicitante |
|---|--------|-------------------------|------------------------|-----------------------------------------------|
| L-01 | Responsável técnico pelo chamado não informado | Campo "Responsável" = "Não Informado" | Alto — impede designação formal, acompanhamento e comunicação estruturada | Quem é o responsável técnico pelo encaminhamento deste chamado no grupo Projetos DTI? |
| L-02 | Investimento não aprovado em contexto de criticidade Emergencial | Campo "Investimento Aprovado: NÃO" | Alto — impede início formal do projeto; cria bloqueio estrutural | Qual é o rito e o prazo previsto para aprovação orçamentária do investimento estimado em menos de R$10K? Existe autorização verbal ou por e-mail da CEO que possa ser formalizada com urgência? |
| L-03 | Identificador do projeto no portfólio interno não informado | Campo "Identificador do Projeto: Não Informado" | Médio — dificulta rastreabilidade no portfólio de TI do GAB | Este projeto possui algum código ou identificador interno no portfólio de TI / PMO do GAB? |
| L-04 | Classificação da demanda e tipo da requisição não selecionados | Campos "Classificação da Demanda" e "Tipo da Requisição" = "Não Selecionado" | Médio — impede categorização no portfólio VMO e priorização formal | O solicitante pode complementar a classificação e o tipo de requisição diretamente no sistema Business Desk? |
| L-05 | Processo de negócio atual (AS-IS) não documentado | Campo "Processo Documentado: NÃO" | Alto — impede especificação funcional adequada e análise de impacto | Existe BPMN, fluxograma ou descrição textual do processo de faturamento atual (AS-IS)? Em caso negativo, quando e por quem pode ser elaborado? |
| L-06 | Escopo detalhado declarado como existente, mas não anexado ao ticket | Campo "Área de negócio possui escopo detalhado: SIM" + ausência de anexo | Alto — escopo declarado é requisito mínimo para início da qualificação | Onde está o documento de escopo detalhado mencionado no ticket? Pode ser compartilhado com o time do Projetos DTI para análise? |
| L-07 | Sponsor / Patrocinador formal do projeto não identificado | Ausência do campo no ticket; solicitante e beneficiado são o mesmo indivíduo | Alto — necessário para aprovação de mudanças de escopo, resolução de conflitos e tomada de decisão | Quem é o patrocinador formal deste projeto? É o próprio solicitante Jairo De Melo Ferreira Mendes ou há outro executivo com autoridade decisória sobre o projeto? |
| L-08 | Linha de base do indicador de ganhos não declarada | Campo "Indicador de Ganhos": "volume de emissão diário por usuário" — sem valor atual | Médio — impede a mensuração do benefício realizado ao final do projeto | Qual é o volume atual de emissão diária de documentos por usuário no processo manual (estado AS-IS)? |
| L-09 | Prazo desejado / comprometido pela CEO não declarado | Campos de prazo preenchidos apenas com a data do SLA do chamado (já vencida) | Alto — SLA do chamado vencido; prazo real do projeto desconhecido | Qual é o prazo que a CEO espera para a entrega operacional desta integração? Existe data-limite associada à conformidade com CPC 47 / IFRS 15? |
| L-10 | Papel da Diretoria de Logística Dedicada no projeto não detalhado | Campo "Projeto envolve outras áreas de negócio: SIM — Diretoria de Logística Dedicada" | Médio — escopo de impacto, aprovação de requisitos e envolvimento desta área são desconhecidos | Qual é o papel da Diretoria de Logística Dedicada neste projeto: usuária do sistema, aprovadora de requisitos, impactada pelo faturamento, ou outro papel? |

---

## 5. Inconsistências Detectadas

| # | Inconsistência | Descrição | Ação Recomendada |
|---|---------------|-----------|-----------------|
| INC-01 | Criticidade Emergencial x Investimento Não Aprovado | Um chamado com criticidade Emergencial pressupõe ação imediata. Contudo, o investimento não foi formalmente aprovado, criando um bloqueio estrutural para o início do projeto. | Confirmar com Jairo De Melo Ferreira Mendes e Projetos DTI se há caminho de aprovação acelerada dado o status emergencial e a origem da demanda (CEO). |
| INC-02 | SLA Vencido x Responsável Não Informado | O chamado está em atraso (18h05 declarados) sem responsável designado no grupo solucionador, sem nenhuma ação registrada desde a abertura em 13/05/2026. | Escalada interna ao Gestor do Grupo Projetos DTI para nomeação imediata de responsável e registro de ação no Business Desk. |
| INC-03 | Data de Término Prevista Ultrapassada x Status "Em Aberto" | A data de término prevista (20/05/2026) foi ultrapassada há 4 dias em relação à data de coleta (24/05/2026). O chamado permanece em aberto sem atualização de prazo. | Renegociação formal do prazo com o solicitante e atualização do registro no Business Desk com nova data de término prevista. |

---

## 6. Resumo da Demanda para Confirmação com o Solicitante

**DEM-2026-007 — Integração GRLOG-SAP (INT015): Faturamento Integrado por Medições Aprovadas**

O solicitante Jairo De Melo Ferreira Mendes (VIX Matriz) abriu o chamado #6813896 em 13/05/2026, solicitando a implementação da integração INT015 entre o GRLOG (Sistema de Gestão de Receita) e o SAP (ERP corporativo) para automatizar o fluxo de faturamento a partir de medições realizadas e aprovadas. O escopo declarado compreende: geração de ordens de vendas, emissão de documentos fiscais (NFSe e Recibo), contabilização de Notas de Débito e retorno dos documentos ao GRLOG.

A necessidade de negócio subjacente ao pedido técnico é garantir o reconhecimento de receita de forma tempestiva e em conformidade com CPC 47 / IFRS 15, eliminando o processo manual atual que gera atrasos de faturamento, retrabalho operacional e risco regulatório. A demanda foi classificada como Emergencial (criticidade 1) e tem como justificativa declarada o atendimento a determinação direta da CEO do Grupo Águia Branca.

O chamado apresenta, na data de coleta, as seguintes situações de atenção: SLA em atraso (18h05); responsável técnico não designado no grupo Projetos DTI; investimento estimado em menos de R$10.000 sem aprovação formal; processo de negócio atual sem documentação; e escopo detalhado mencionado como existente mas não anexado ao ticket.

Para que o Squad VMO Autônomo possa iniciar formalmente a qualificação desta demanda, solicitamos ao Solicitante que providencie: (1) nomeação imediata do responsável técnico no Projetos DTI; (2) envio do documento de escopo detalhado; (3) confirmação do prazo esperado pela CEO para entrega da integração; (4) início do rito de aprovação orçamentária; e (5) identificação do sponsor formal do projeto. O VMO ficará à disposição para alinhar os próximos passos após o recebimento dessas informações.

---

## 7. Próximas Ações Recomendadas

| # | Ação | Responsável Sugerido | Prazo Sugerido | Prioridade |
|---|------|----------------------|----------------|------------|
| A-01 | Nomear responsável técnico no chamado #6813896 (Projetos DTI) | Gestor do Grupo Projetos DTI | Imediato | Alta |
| A-02 | Solicitar formalmente o documento de escopo detalhado ao solicitante (L-06) | Iara Inbound / VMO | Imediato | Alta |
| A-03 | Iniciar rito de aprovação orçamentária para investimento menor de R$10K — contexto emergencial (L-02) | Jairo De Melo Ferreira Mendes | 24–48 horas | Alta |
| A-04 | Confirmar prazo esperado pela CEO para entrega da integração INT015 (L-09) | Jairo De Melo Ferreira Mendes | Imediato | Alta |
| A-05 | Identificar e confirmar o sponsor formal do projeto (L-07) | VMO / Projetos DTI | 24 horas | Alta |
| A-06 | Obter documentação do processo atual AS-IS junto à Diretoria de Logística Dedicada (L-05) | Jairo De Melo Ferreira Mendes | A combinar | Média |
| A-07 | Levantar artefatos de arquitetura dos projetos WAVE e Plataforma de Venda de Ativos para potencial reuso (CI-04) | Projetos DTI | A combinar | Média |
| A-08 | Atualizar data de término prevista no Business Desk (INC-03) | Responsável do Projetos DTI | Após nomeação (A-01) | Média |

---

## 8. Checklist de Qualidade — Iara Inbound

- [x] Canal de entrada identificado e documentado (Business Desk — Águia Branca, Ticket #6813896)
- [x] Todas as fontes consultadas listadas com grau de confiabilidade (F1 a F8)
- [x] Cada campo possui referência explícita à fonte de rastreabilidade
- [x] Necessidade de negócio distinguida do pedido técnico (Seções 2.3 e 2.4)
- [x] Lacunas documentadas com perguntas específicas para o solicitante (10 lacunas — Seção 4)
- [x] Contexto implícito registrado com flag "INFERIDO — confirmar" (6 itens — Seção 3)
- [x] Inconsistências detectadas e documentadas (3 inconsistências — Seção 5)
- [x] ID DEM-2026-007 gerado e registrado no cabeçalho
- [x] Resumo de confirmação para o solicitante incluído (Seção 6)
- [x] Próximas ações recomendadas com responsáveis e prazos (Seção 7)
- [x] Sponsor, orçamento aprovado e prazo comprometido **não foram inferidos** (conformidade com critério de não-inferência)

---

*Documento gerado pelo Squad VMO Autônomo — Agente Iara Inbound (Coletora de Demandas)*
*Data de geração: 2026-05-24*
*Versão: 1.0*
*Chamado de origem: #6813896 — Business Desk Águia Branca*
