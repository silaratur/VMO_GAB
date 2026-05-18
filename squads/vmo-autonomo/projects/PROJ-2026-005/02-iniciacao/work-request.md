# WORK REQUEST — MINI-RFP
## VMO Consultoria | Gestão de Fornecedores e Projetos

---

| Campo | Informação |
|---|---|
| **WR Nº** | WR-2026-005 |
| **Projeto** | PROJ-2026-005 |
| **Data de Emissão** | 18/05/2026 |
| **Prazo de Submissão** | 06/06/2026 |
| **Status** | Aguardando Sponsor (CB-01) |

---

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Informação |
|---|---|
| **ID do Projeto** | PROJ-2026-005 |
| **Nome do Projeto** | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Cliente** | Divisão Comércio — Grupo Águia Branca |
| **Solicitante** | Sandro Siqueira — Coordenador de Contabilidade, Divisão Comércio |
| **Sponsor** | A IDENTIFICAR — CB-01 (prazo limite: 25/05/2026) |
| **Fornecedor Principal** | NBS (desenvolvimento como contrapartida contratual — custo zero) |
| **Gestor VMO** | Fábio Fornecedor — Especialista em Gestão de Fornecedores |
| **Tipo de Projeto** | Implementação de Módulo Nativo ERP + Migração de Sistema Legado |
| **Categoria** | Compliance Fiscal / Automação Tributária |
| **Envelope Orçamentário** | R$ 35.000 (serviços residuais) |
| **Go-live Estimado** | Outubro/2026 (janela set–nov/2026) |

> **NOTA IMPORTANTE:** O desenvolvimento do módulo Auditor Fiscal é **contrapartida contratual da NBS** e portanto tem **custo zero** para o Grupo Águia Branca. Este Work Request cobre exclusivamente os **serviços residuais de implantação**: parametrização, migração de configurações, treinamento de usuários e suporte ao processo de rescisão do Fiscal Defender.

---

## 2. CONTEXTO E JUSTIFICATIVA

### 2.1 Situação Atual

A Divisão Comércio do Grupo Águia Branca opera atualmente com o **Fiscal Defender** como solução de auditoria e validação de documentos fiscais eletrônicos. A ferramenta cobre processos críticos de compliance: validação de NF-e, auditoria de campos SPED/NFSE e controle de inconsistências em documentos tributários.

O contrato do Fiscal Defender representa um custo recorrente anual de **R$ 78.000**, desembolsado integralmente pela Divisão Comércio, sem perspectiva de redução tarifária nas renovações projetadas para os próximos ciclos.

### 2.2 Oportunidade Identificada

No escopo do contrato vigente com a **NBS** — fornecedora do ERP utilizado pela Divisão Comércio —, foi identificada a obrigação contratual de entrega de um **módulo nativo de Auditor Fiscal**, capaz de replicar e superar as funcionalidades do Fiscal Defender dentro da própria plataforma ERP. Essa entrega constitui **contrapartida contratual já negociada**, sem ônus adicional para o Grupo.

A migração para o módulo nativo NBS elimina a dependência de uma solução de terceiro, reduz o custo total de propriedade e consolida o ecossistema fiscal dentro de uma única plataforma integrada.

### 2.3 Justificativa Econômica

| Item | Valor |
|---|---|
| Saving anual com eliminação do Fiscal Defender | **R$ 78.000/ano** |
| Investimento nos serviços residuais (WR) | R$ 35.000 (único) |
| Payback estimado | **< 6 meses** |
| Saving acumulado em 3 anos (líquido) | **R$ 199.000** |

### 2.4 Justificativa Estratégica e de Compliance

- **Integração nativa:** módulo embedded no ERP NBS elimina integrações point-to-point frágeis e reduz risco operacional
- **Atualização automática de legislação:** o fornecedor NBS assume responsabilidade pela adequação às normas SPED, NBS (Nomenclatura Brasileira de Serviços) e NF-e conforme evolução regulatória
- **Governança fiscal:** log de auditoria nativo, controle de perfis de acesso e rastreabilidade completa de validações
- **Continuidade de negócios:** eliminação de dependência de terceiro em processo crítico de compliance

---

## 3. OBJETIVO DA CONTRATAÇÃO

Contratar os **serviços residuais de implantação, parametrização, migração de configurações e treinamento** necessários para que o módulo nativo **Auditor Fiscal NBS** — entregue pela NBS como contrapartida contratual sem custo — entre em operação plena na Divisão Comércio, substituindo integralmente o Fiscal Defender até outubro/2026, com:

- 100% das funcionalidades operacionais do Fiscal Defender replicadas no novo módulo
- Migração de todas as regras e configurações de validação ativas
- Equipes de Contabilidade, Financeiro e Jurídico capacitadas para operação autônoma
- Rescisão formal do contrato Fiscal Defender executada com segurança e sem penalidades

---

## 4. ESCOPO DA CONTRATAÇÃO

### 4.1 Serviços Inclusos

> Os itens abaixo correspondem aos **serviços residuais** contratados via este WR. O desenvolvimento do módulo em si é obrigação da NBS (custo zero). A execução dos serviços listados está condicionada à entrega do módulo pela NBS no Marco 1 (31/07/2026).

| ID | Requisito | Descrição |
|---|---|---|
| **RF001** | Replicação funcional completa | Mapear, validar e parametrizar 100% das funcionalidades operacionais do Fiscal Defender no módulo Auditor Fiscal NBS, sem lacuna funcional. |
| **RF002** | Auditoria automatizada de NF-e | Configurar validação automatizada de campos obrigatórios conforme exigências SPED/NFSE, garantindo cobertura integral das regras vigentes na Divisão Comércio. |
| **RF003** | Validação de NBS (Nomenclatura Brasileira de Serviços) | Parametrizar validação de códigos NBS em documentos fiscais eletrônicos, conforme tabelas e regras vigentes de tributação de serviços. |
| **RF004** | Alertas automáticos de inconsistências | Configurar régua de alertas e notificações automáticas para NF-e com inconsistências, irregularidades ou campos inválidos, com roteamento para os responsáveis. |
| **RF005** | Integração nativa ERP NBS | Validar e garantir que a integração do Auditor Fiscal com os demais módulos do ERP NBS (Financeiro, Contábil, Fiscal) opera sem desenvolvimento adicional ou customização. |
| **RF006** | Relatórios de auditoria | Configurar e homologar geração de relatórios de auditoria por período, por tipo de documento e por exceção, substituindo todos os relatórios equivalentes do Fiscal Defender. |
| **RF007** | Perfis de acesso diferenciados | Criar e validar perfis de acesso para os papéis: contador, analista fiscal, auditoria e administrador, conforme política de segurança da informação do Grupo Águia Branca. |
| **RF008** | Log de auditoria | Validar que o módulo registra log completo de todas as ações de validação realizadas pelo sistema e pelos usuários, com rastreabilidade e imutabilidade. |
| **RF009** | Migração de configurações e regras | Executar a migração de todas as configurações e regras de validação ativas no Fiscal Defender para o módulo NBS, com validação de paridade pré-go-live. |
| **RF010** | Treinamento de equipes | Conduzir programa de treinamento para as equipes de Contabilidade, Financeiro e Jurídico da Divisão Comércio, cobrindo operação, configuração e troubleshooting do Auditor Fiscal NBS. |

### 4.2 Serviços Explicitamente Excluídos

Os itens a seguir estão **fora do escopo** deste Work Request e não devem ser contemplados nas propostas:

| # | Item Excluído | Observação |
|---|---|---|
| EX01 | Desenvolvimento de novas funcionalidades | Apenas replicação do Fiscal Defender. Qualquer nova feature deve ser tratada como projeto separado. |
| EX02 | Integração com sistemas externos à plataforma NBS | O escopo se restringe à integração nativa entre módulos NBS. |
| EX03 | Migração de dados históricos do Fiscal Defender | Apenas configurações e regras ativas são migradas. Histórico de auditoria permanece no Fiscal Defender até encerramento contratual. |
| EX04 | Extensão da solução para outras divisões do Grupo | Escopo exclusivo da Divisão Comércio. Rollout para outras unidades é projeto futuro. |
| EX05 | Suporte técnico pós go-live além do período contratual | O período de garantia encerra em 31/01/2027. Suporte além dessa data deve ser negociado em contrato separado de sustentação. |

---

## 5. PREMISSAS E RESPONSABILIDADES DO GRUPO

### 5.1 Premissas

Para execução do projeto dentro do prazo e orçamento previstos, as seguintes premissas devem ser verdadeiras no momento do kickoff:

| # | Premissa | Impacto se não atendida |
|---|---|---|
| P01 | A NBS entrega o módulo Auditor Fiscal conforme compromisso contratual, **sem custo**, até 31/07/2026 | Atraso de todos os marcos subsequentes; replanejamento obrigatório |
| P02 | Acesso ao ambiente ERP NBS da Divisão Comércio (produção e homologação) disponível para configuração e testes | Bloqueio imediato das atividades de parametrização |
| P03 | Documentação completa das regras e configurações atuais do Fiscal Defender disponível antes do início da migração | Retrabalho e risco de lacuna funcional pós-migração |
| P04 | Equipes de Contabilidade e Jurídico disponíveis para participação no UAT (User Acceptance Testing) no período de setembro/2026 | Atraso no go-live |
| P05 | Prazo de rescisão do contrato Fiscal Defender é compatível com o go-live em outubro/2026 (aviso contratual dentro do prazo) | Custo duplicado de licença no período de sobreposição |
| P06 | Sponsor formalmente designado (CB-01) até 25/05/2026 | Bloqueio na aprovação do WR e na emissão de Purchase Order |

### 5.2 Responsabilidades do Grupo Águia Branca / Divisão Comércio

| Responsabilidade | Área Responsável | Prazo |
|---|---|---|
| Designação formal do Sponsor | CB-01 (alta gestão) | 25/05/2026 |
| Disponibilização de acesso ao ambiente ERP NBS | TI / Infraestrutura | Antes do kickoff |
| Fornecimento da documentação do Fiscal Defender | Contabilidade — Sandro Siqueira | Até Marco 1 (31/07/2026) |
| Aprovação do plano de treinamento | Contabilidade / RH | Até Marco 2 (31/08/2026) |
| Participação e assinatura do UAT | Contabilidade, Financeiro, Jurídico | Marco 3 (set/2026) |
| Emissão do aviso de rescisão ao Fiscal Defender | Contratos / Jurídico | A definir com base no contrato vigente |
| Aprovação de marcos e liberação de pagamentos | Sponsor | Conforme cronograma |

### 5.3 Responsabilidades da NBS (Fornecedor ERP)

| Responsabilidade | Prazo Contratual |
|---|---|
| Entrega do módulo Auditor Fiscal (contrapartida contratual) | 31/07/2026 |
| Suporte técnico ao fornecedor contratado para implantação | Durante todo o projeto |
| Atualização do módulo conforme evolução regulatória | Contínuo (suporte padrão NBS) |

---

## 6. CRONOGRAMA ESPERADO

```
LINHA DO TEMPO — PROJ-2026-005
───────────────────────────────────────────────────────────────────

 Mai/2026   Jun/2026   Jul/2026   Ago/2026   Set/2026   Out/2026   Nov/2026   Jan/2027
    │           │           │           │           │           │           │           │
    ├── CB-01 ──┤           │           │           │           │           │           │
    │    25/05  │           │           │           │           │           │           │
    │           ├── M0 ─────┤           │           │           │           │           │
    │           │  Kickoff  │           │           │           │           │           │
    │           │  15/06    │           │           │           │           │           │
    │           │           ├── M1 ─────┤           │           │           │           │
    │           │           │  Módulo   │           │           │           │           │
    │           │           │  NBS      │           │           │           │           │
    │           │           │  entregue │           │           │           │           │
    │           │           │  31/07    │           │           │           │           │
    │           │           │           ├── M2 ─────┤           │           │           │
    │           │           │           │  Config + │           │           │           │
    │           │           │           │  Migração │           │           │           │
    │           │           │           │  31/08    │           │           │           │
    │           │           │           │           ├── M3 ─────┤           │           │
    │           │           │           │           │  Testes + │           │           │
    │           │           │           │           │  UAT      │           │           │
    │           │           │           │           │  30/09    │           │           │
    │           │           │           │           │           ├── M4 ─────┤           │
    │           │           │           │           │           │  Go-live  │           │
    │           │           │           │           │           │  Treino   │           │
    │           │           │           │           │           │  31/10    │           │
    │           │           │           │           │           │           │           ├── Enc.
    │           │           │           │           │           │           │           │  31/01/27
```

| Marco | Descrição | Data Prevista | % Pagamento |
|---|---|---|---|
| **CB-01** | Designação do Sponsor | 25/05/2026 | — |
| **CB-02** | Aprovação do WR e emissão de PO | 06/06/2026 | — |
| **M0 — Kickoff** | Reunião de início do projeto | 15/06/2026 (est.) | — |
| **M1** | Módulo Auditor Fiscal entregue pela NBS | 31/07/2026 | 30% |
| **M2** | Configuração completa + migração de regras homologada | 31/08/2026 | 30% |
| **M3** | Testes integrados e UAT aprovado com aceite formal | 30/09/2026 | 25% |
| **M4** | Go-live + treinamento concluído + rescisão Fiscal Defender iniciada | 31/10/2026 | 15% |
| **Encerramento** | Fim do período de garantia | 31/01/2027 | — |

> **Prazo de submissão das propostas:** 06/06/2026 às 18h00 (horário de Brasília)

---

## 7. ENTREGÁVEIS OBRIGATÓRIOS

O fornecedor deve entregar obrigatoriamente os seguintes artefatos ao longo do projeto:

| # | Entregável | Marco | Responsável |
|---|---|---|---|
| E01 | Plano de Projeto detalhado (cronograma, riscos, recursos) | M0 | Fornecedor |
| E02 | Relatório de levantamento funcional (gap analysis Fiscal Defender × Auditor Fiscal NBS) | M1 | Fornecedor |
| E03 | Documento de configurações parametrizadas (RF001 a RF008) | M2 | Fornecedor |
| E04 | Relatório de migração de regras com rastreabilidade (RF009) | M2 | Fornecedor |
| E05 | Plano de testes e roteiro de UAT | M2 | Fornecedor |
| E06 | Relatório de testes integrados com evidências (logs, prints) | M3 | Fornecedor |
| E07 | Termo de Aceite de UAT assinado pelos representantes do cliente | M3 | Cliente + Fornecedor |
| E08 | Material de treinamento (apresentações, manuais, vídeos) | M4 | Fornecedor |
| E09 | Relatório de execução do treinamento (frequência, avaliação de aprendizagem) | M4 | Fornecedor |
| E10 | Checklist de go-live validado e aprovado | M4 | Fornecedor |
| E11 | Termo de Encerramento de Projeto | Encerramento | Fornecedor + VMO |

---

## 8. GOVERNANÇA E COMUNICAÇÃO

### 8.1 Estrutura de Governança

| Papel | Responsável | Função |
|---|---|---|
| **Sponsor** | A identificar — CB-01 | Aprovação estratégica, desbloqueio de impedimentos, aprovação final de marcos |
| **Gestor do Projeto (Cliente)** | Sandro Siqueira — Coordenador de Contabilidade | Acompanhamento operacional, ponto focal técnico, aceite de entregáveis |
| **Gestor VMO** | Fábio Fornecedor | Gestão contratual do fornecedor, controle de marcos, interface entre partes |
| **Gestor do Projeto (Fornecedor)** | A nomear na proposta | Execução do projeto, coordenação técnica, entrega de artefatos |
| **Responsável NBS** | A nomear pela NBS | Entrega do módulo, suporte técnico à implantação |

### 8.2 Rituais de Acompanhamento

| Reunião | Frequência | Participantes | Objetivo |
|---|---|---|---|
| Reunião de Status | Quinzenal | Gestor Cliente + Gestor VMO + Gestor Fornecedor | Avanço de atividades, riscos, impedimentos |
| Reunião de Marco | A cada entrega de marco | Sponsor + Gestores + NBS | Aceite formal, liberação de pagamento |
| Reunião de UAT | Setembro/2026 | Equipes Contabilidade, Financeiro, Jurídico + Fornecedor | Validação funcional pelo usuário final |
| Reunião de Go-live | Outubro/2026 | Todos os stakeholders | Checklist de prontidão, declaração de go-live |

### 8.3 Comunicação e Documentação

- Toda comunicação formal deve ser registrada via e-mail ou plataforma de gestão de projetos definida no kickoff
- Atas de reunião devem ser emitidas em até 24 horas após cada reunião e aprovadas em até 48 horas
- Relatórios de status quinzenais devem ser entregues até toda segunda-feira da semana de reunião
- Solicitações de mudança de escopo (Change Requests) devem ser submetidas formalmente à VMO e aprovadas pelo Sponsor antes de qualquer execução
- O fornecedor deve designar um Gerente de Projeto com dedicação mínima de 50% ao projeto

---

## 9. CONDIÇÕES COMERCIAIS

### 9.1 Envelope Orçamentário

| Item | Valor |
|---|---|
| **Envelope total disponível** | **R$ 35.000** |
| Desenvolvimento do módulo Auditor Fiscal NBS | R$ 0 (contrapartida contratual NBS) |
| Implantação e parametrização (RF001 a RF008) | A detalhar na proposta |
| Migração de configurações (RF009) | A detalhar na proposta |
| Treinamento (RF010) | A detalhar na proposta |
| Gestão de rescisão Fiscal Defender | A detalhar na proposta (se aplicável) |

> Propostas que excedam o envelope de **R$ 35.000** serão automaticamente desclassificadas.

### 9.2 Cronograma de Pagamentos

O faturamento será realizado por marcos, conforme execução verificada e aceite formal da VMO e do cliente:

| Marco | Condição de Pagamento | % | Valor (referência) |
|---|---|---|---|
| **M1** — Módulo NBS entregue e validado | Aceite do relatório de levantamento funcional (E02) | 30% | R$ 10.500 |
| **M2** — Configuração e migração homologadas | Aceite dos entregáveis E03 e E04 | 30% | R$ 10.500 |
| **M3** — UAT aprovado | Aceite do Termo de UAT (E07) | 25% | R$ 8.750 |
| **M4** — Go-live e treinamento concluídos | Aceite dos entregáveis E08, E09, E10 | 15% | R$ 5.250 |
| **Total** | | **100%** | **R$ 35.000** |

> Pagamentos realizados em até **15 dias corridos** após o aceite formal do marco correspondente.

### 9.3 Condições Gerais

- Preços devem ser apresentados em **Reais (BRL)**, fixos e sem reajuste durante o projeto
- A proposta deve especificar claramente horas, perfis profissionais e cronograma físico-financeiro
- Regime de contratação: **preço global por escopo** (não serão aceitas propostas por hora ou por produto sem preço global)
- Impostos e encargos devem estar inclusos nos valores propostos
- O fornecedor deve apresentar comprovação de experiência prévia em projetos de implantação NBS e/ou migração de ferramentas de auditoria fiscal
- A VMO se reserva o direito de solicitar apresentação técnica da proposta antes da adjudicação

---

## 10. ARTEFATO OBRIGATÓRIO — CHECKLIST DE CONFORMIDADE DA PROPOSTA

> **Instruções:** O fornecedor deve preencher o checklist abaixo e submeter como **anexo obrigatório** à proposta. Propostas sem o checklist preenchido serão desclassificadas. Para cada item, marque **OK** (atendido), **NOK** (não atendido) ou **N/A** (não aplicável), e inclua observações quando necessário.

---

### GRUPO 1 — QUALIFICAÇÃO TÉCNICA DO FORNECEDOR (6 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 1.1 | Comprovação de ao menos 2 projetos de implantação de módulos NBS (Nomenclatura Brasileira de Serviços) concluídos nos últimos 3 anos | ☐ | ☐ | |
| 1.2 | Comprovação de ao menos 1 projeto de migração de ferramenta de auditoria fiscal (Fiscal Defender ou similar) para plataforma ERP integrada | ☐ | ☐ | |
| 1.3 | Equipe técnica com certificação ou habilitação formal na plataforma ERP NBS | ☐ | ☐ | |
| 1.4 | Experiência documentada com projetos em empresas do segmento de Comércio ou Distribuição | ☐ | ☐ | |
| 1.5 | Apresentação de referências de clientes (mínimo 2 contatos verificáveis) | ☐ | ☐ | |
| 1.6 | Empresa regularmente constituída há mais de 3 anos, com comprovante de regularidade fiscal (CND Federal, Estadual e Municipal) | ☐ | ☐ | |

---

### GRUPO 2 — COMPOSIÇÃO DA EQUIPE DO PROJETO (6 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 2.1 | Gerente de Projeto nomeado com dedicação mínima de 50% ao projeto, com CV anexo | ☐ | ☐ | |
| 2.2 | Consultor Funcional Fiscal com experiência comprovada em módulos de auditoria NF-e e SPED | ☐ | ☐ | |
| 2.3 | Consultor Técnico NBS com experiência em parametrização e integração de módulos da plataforma | ☐ | ☐ | |
| 2.4 | Instrutor de treinamento habilitado para capacitação em sistemas ERP (presencial ou remoto) | ☐ | ☐ | |
| 2.5 | Plano de contingência de substituição de recursos críticos em caso de desligamento ou indisponibilidade | ☐ | ☐ | |
| 2.6 | Compromisso formal de não substituição de recursos-chave sem aprovação prévia da VMO | ☐ | ☐ | |

---

### GRUPO 3 — METODOLOGIA E GESTÃO DO PROJETO (2 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 3.1 | Metodologia de implantação documentada, com fases, atividades e responsáveis claramente definidos | ☐ | ☐ | |
| 3.2 | Plano de gestão de riscos identificando ao menos 5 riscos do projeto com probabilidade, impacto e plano de mitigação | ☐ | ☐ | |

---

### GRUPO 4 — ESCOPO TÉCNICO E COBERTURA FUNCIONAL (3 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 4.1 | Proposta técnica demonstra cobertura de todos os 10 requisitos funcionais (RF001 a RF010) com descrição do approach de execução de cada um | ☐ | ☐ | |
| 4.2 | Plano de levantamento funcional (gap analysis) entre Fiscal Defender e Auditor Fiscal NBS incluído na proposta | ☐ | ☐ | |
| 4.3 | Estratégia de migração de configurações e regras do Fiscal Defender detalhada, com garantia de paridade funcional pré-go-live | ☐ | ☐ | |

---

### GRUPO 5 — CRONOGRAMA E MARCOS (3 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 5.1 | Cronograma físico detalhado por atividade, compatível com os marcos M1 a M4 definidos no WR | ☐ | ☐ | |
| 5.2 | Cronograma financeiro alinhado ao modelo de pagamento por marcos (30/30/25/15%) | ☐ | ☐ | |
| 5.3 | Declaração formal de comprometimento com o go-live até 31/10/2026 | ☐ | ☐ | |

---

### GRUPO 6 — TREINAMENTO E CAPACITAÇÃO (9 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 6.1 | Plano de treinamento detalhado cobrindo os três públicos: Contabilidade, Financeiro e Jurídico | ☐ | ☐ | |
| 6.2 | Carga horária de treinamento por perfil de usuário especificada | ☐ | ☐ | |
| 6.3 | Modalidade de treinamento definida (presencial / remoto / híbrido) com justificativa | ☐ | ☐ | |
| 6.4 | Material didático incluído no escopo (apresentações, manuais de usuário, guias rápidos) | ☐ | ☐ | |
| 6.5 | Metodologia de avaliação de aprendizagem dos participantes descrita | ☐ | ☐ | |
| 6.6 | Cobertura de treinamento para os perfis: contador, analista fiscal, auditoria e administrador (RF007) | ☐ | ☐ | |
| 6.7 | Vídeo-aulas ou gravações das sessões incluídas como entregável (para uso interno e onboarding futuro) | ☐ | ☐ | |
| 6.8 | Plano de suporte pós-treinamento durante o período de garantia (dúvidas operacionais) | ☐ | ☐ | |
| 6.9 | Prazo máximo de entrega dos materiais de treinamento (mínimo 10 dias antes das sessões) | ☐ | ☐ | |

---

### GRUPO 7 — TESTES E QUALIDADE (3 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 7.1 | Plano de testes integrados contemplando todos os módulos NBS integrados ao Auditor Fiscal | ☐ | ☐ | |
| 7.2 | Roteiro de UAT com casos de teste baseados nos fluxos reais do Fiscal Defender, para validação pelo usuário final | ☐ | ☐ | |
| 7.3 | Critérios de aceite do UAT claramente definidos, com percentual mínimo de casos de teste aprovados para liberação do go-live | ☐ | ☐ | |

---

### GRUPO 8 — CONDIÇÕES COMERCIAIS E CONTRATUAIS (5 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 8.1 | Proposta comercial dentro do envelope de R$ 35.000 (propostas acima serão desclassificadas) | ☐ | ☐ | |
| 8.2 | Preços apresentados em BRL, fixos, sem reajuste, com impostos inclusos | ☐ | ☐ | |
| 8.3 | Detalhamento da composição de preço por entregável/marco (não apenas valor global) | ☐ | ☐ | |
| 8.4 | Prazo de validade da proposta mínimo de 60 dias a partir da data de submissão | ☐ | ☐ | |
| 8.5 | Declaração de aceite das condições gerais deste Work Request e disponibilidade para negociação contratual com a VMO | ☐ | ☐ | |

---

### GRUPO 9 — CONFORMIDADE DOCUMENTAL (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 9.1 | Proposta técnica e proposta comercial apresentadas em documentos separados | ☐ | ☐ | |
| 9.2 | Checklist de conformidade (este artefato) preenchido e assinado digitalmente pelo responsável legal da empresa | ☐ | ☐ | |
| 9.3 | Documentos de regularidade fiscal anexos: CND Federal, CND Estadual, CND Municipal, FGTS e Trabalhista | ☐ | ☐ | |
| 9.4 | Contrato social ou certificado da Junta Comercial atualizado (últimos 12 meses) | ☐ | ☐ | |

---

### GRUPO 10 — SEGURANÇA, PRIVACIDADE E COMPLIANCE (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 10.1 | Política de segurança da informação do fornecedor disponível para análise pelo cliente | ☐ | ☐ | |
| 10.2 | Compromisso formal de confidencialidade (NDA) para acesso a dados fiscais e configurações do ERP do Grupo Águia Branca | ☐ | ☐ | |
| 10.3 | Conformidade com a LGPD declarada, incluindo tratamento de dados pessoais acessados durante o projeto | ☐ | ☐ | |
| 10.4 | Plano de descarte seguro de dados do cliente ao término do projeto | ☐ | ☐ | |

---

> **Resumo do Checklist:**
>
> | Grupo | Itens | OK | NOK | N/A |
> |---|---|---|---|---|
> | 1 — Qualificação Técnica | 6 | | | |
> | 2 — Composição da Equipe | 6 | | | |
> | 3 — Metodologia e Gestão | 2 | | | |
> | 4 — Escopo Técnico | 3 | | | |
> | 5 — Cronograma e Marcos | 3 | | | |
> | 6 — Treinamento e Capacitação | 9 | | | |
> | 7 — Testes e Qualidade | 3 | | | |
> | 8 — Condições Comerciais | 5 | | | |
> | 9 — Conformidade Documental | 4 | | | |
> | 10 — Segurança e Compliance | 4 | | | |
> | **TOTAL** | **41** | | | |

---

## 11. PROCESSO DE SUBMISSÃO

### 11.1 Prazo e Canal

| Item | Informação |
|---|---|
| **Prazo limite de submissão** | **06/06/2026 às 18h00 (horário de Brasília)** |
| **Canal de submissão** | E-mail para o Gestor VMO responsável |
| **Assunto do e-mail** | `[PROPOSTA] PROJ-2026-005 — Auditor Fiscal NBS — [Nome do Fornecedor]` |
| **Formato dos arquivos** | PDF (proposta técnica, proposta comercial, checklist) + XLS ou XLSX (cronograma detalhado) |

### 11.2 Documentos a Submeter

O fornecedor deve enviar, dentro do prazo, os seguintes documentos:

| # | Documento | Formato |
|---|---|---|
| D01 | Proposta Técnica (escopo, metodologia, equipe, cronograma) | PDF |
| D02 | Proposta Comercial (preços por marco, composição de custos) | PDF |
| D03 | Checklist de Conformidade (Artefato Obrigatório — Seção 10) preenchido e assinado | PDF |
| D04 | Cronograma físico-financeiro detalhado | XLS/XLSX ou PDF |
| D05 | Documentos de qualificação (regularidade fiscal, contrato social) | PDF |
| D06 | CVs dos profissionais designados para o projeto | PDF |
| D07 | Referências de clientes (nome, empresa, telefone, e-mail) | PDF ou no corpo da proposta técnica |

### 11.3 Processo de Avaliação

| Fase | Atividade | Prazo |
|---|---|---|
| Submissão | Recebimento das propostas | Até 06/06/2026 |
| Triagem | Verificação de conformidade documental e checklist | 07–09/06/2026 |
| Análise técnica | Avaliação das propostas técnicas pela VMO e cliente | 10–13/06/2026 |
| Apresentação (se necessário) | Apresentação técnica das propostas finalistas | 14–15/06/2026 (est.) |
| Adjudicação | Decisão e comunicação ao fornecedor selecionado | 16/06/2026 (est.) |
| Negociação e contrato | Alinhamento contratual final | 17–20/06/2026 (est.) |
| Kickoff | Início formal do projeto | 15/06/2026 (est.) |

### 11.4 Critérios de Avaliação

As propostas serão avaliadas segundo os seguintes critérios e pesos:

| Critério | Peso |
|---|---|
| Qualificação técnica e experiência comprovada | 30% |
| Qualidade e completude da proposta técnica | 25% |
| Proposta comercial (valor e detalhamento) | 25% |
| Perfil e experiência da equipe designada | 15% |
| Conformidade documental (checklist 10/10 grupos) | 5% |
| **Total** | **100%** |

### 11.5 Esclarecimentos

Dúvidas sobre este Work Request devem ser encaminhadas até **30/05/2026** ao Gestor VMO responsável pelo e-mail, com assunto `[DÚVIDA] PROJ-2026-005 — [Nome do Fornecedor]`. As respostas serão consolidadas e enviadas a todos os fornecedores convidados até **02/06/2026**.

---

## APROVAÇÕES

| Papel | Nome | Assinatura | Data |
|---|---|---|---|
| Elaboração | Fábio Fornecedor — VMO Consultoria | | 18/05/2026 |
| Validação Técnica | Sandro Siqueira — Coordenador de Contabilidade | | |
| Aprovação | Sponsor (CB-01 — A identificar) | | Até 25/05/2026 |

---

> **VMO Consultoria | Gestão Estratégica de Fornecedores e Projetos**
> Documento confidencial — uso restrito ao Grupo Águia Branca e fornecedores convidados.
> Versão 1.0 | Emitido em 18/05/2026 | PROJ-2026-005
