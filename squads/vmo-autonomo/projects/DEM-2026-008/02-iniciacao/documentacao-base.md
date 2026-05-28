# Documentação Base de Iniciação — Integração SGMM03 Campos Empresa e Contrato

---

## TERMO DE ABERTURA DO PROJETO (TAP)

```
TERMO DE ABERTURA DO PROJETO
Versão: 1.0 | Data: 2026-05-28 | Status: RASCUNHO
```

### IDENTIFICAÇÃO

| Campo | Valor |
|-------|-------|
| Nome | Integração SGMM03 — Campos Empresa e Contrato (InterCompany) |
| ID | DEM-2026-008 |
| Ticket de Origem | #6800446 |
| Área Solicitante | VIX Matriz |
| Área Executora | Holding DTI + Consultoria SAP PM/FI (a contratar) |
| Data de Início Previsto | 16/06/2026 (após resolução das CBs) |
| Data de Conclusão Prevista | 31/07/2026 |
| Tipo | Melhoria Evolutiva — Integração SAP (PM/FI) |

---

### AUTORIZAÇÃO

| Papel | Nome | Cargo | Autoridade |
|-------|------|-------|------------|
| Sponsor | **[A CONFIRMAR — CB-1]** | Diretor ou superior | Aprovação de orçamento, escopo e prazo |
| Responsável DTI | Mara Rubia Silva Rocha | Holding DTI | Gestão operacional do chamado e articulação com fornecedores |
| Gerente de Projeto | A designar pelo PMO | — | Acompanhamento da execução, aprovação de entregáveis |
| Solicitante | Jenifer dos Santos Carvalho | VIX Matriz | Validação funcional dos entregáveis |

> **CB-1 ABERTA:** O sponsor com nível Diretor ou superior deve ser identificado e nomeado
> até 30/05/2026 para que este TAP seja finalizado e assinado. Responsável: PMO / Holding DTI.

---

### OBJETIVO DO PROJETO (SMART)

> Integrar automaticamente os campos **Empresa** e **Contrato** das Ordens de Manutenção (OM)
> da interface SGMM03 do SGM para o SAP, cobrindo os eventos de **criação** e **alteração** de OM,
> de forma que **100% das OMs InterCompany abertas ou alteradas no SGM** tenham esses campos
> gravados corretamente no SAP **sem intervenção manual**, até **31/07/2026**.

**Detalhamento SMART:**
- **Específico:** Integrar 2 campos (Empresa e Contrato) na interface SGMM03, via módulo PM/FI do SAP
- **Mensurável:** 100% das OMs InterCompany com campos preenchidos automaticamente (zero preenchimentos manuais residuais)
- **Atingível:** Precedente confirmado (campo Centro de Planejamento implantado na mesma interface)
- **Relevante:** Elimina retrabalho manual e risco de inconsistência de dados no processo InterCompany
- **Temporal:** Conclusão até 31/07/2026

---

### JUSTIFICATIVA

No processo InterCompany da interface SGMM03 (SGM + SAP), os campos **Empresa** e **Contrato**
inseridos pela manutenção durante a abertura de OM no SGM não são transmitidos automaticamente
ao SAP. Isso obriga operadores a preencher manualmente esses campos no SAP tanto na criação
quanto na alteração de OMs, gerando:

1. Retrabalho operacional contínuo na equipe de manutenção da VIX Matriz
2. Risco de inconsistência de dados entre SGM e SAP nos campos de identificação InterCompany
3. Possíveis erros em relatórios financeiros de alocação de custos InterCompany

A integração é tecnicamente viável com baixo risco: o campo Centro de Planejamento foi
implementado anteriormente na mesma interface SGMM03 como precedente positivo. A demanda
está alinhada com a diretriz de integridade de dados e eficiência operacional do processo
de manutenção do Grupo Águia Branca.

---

### ESCOPO

**DENTRO DO ESCOPO:**
1. Integração do campo **Empresa** da OM: leitura do valor no SGM e gravação no SAP via SGMM03
2. Integração do campo **Contrato** da OM: leitura do valor no SGM e gravação no SAP via SGMM03
3. Suporte ao evento de **criação** de OM (novo registro SAP)
4. Suporte ao evento de **alteração** de OM (atualização de registro SAP existente)
5. Testes de validação em ambiente de desenvolvimento, qualidade e produção
6. Documentação técnica da solução implementada
7. Repasse de conhecimento para o time de sustentação ERP (PM/FI)

**FORA DO ESCOPO:**
1. Integração de outros campos da interface SGMM03 (demandas separadas)
2. O campo Cenário/CenPlan (MAM1/MWV1) — tem restrição técnica conhecida, tratamento separado
3. Alterações no sistema SGM (sistema de origem — fora da responsabilidade do SAP)
4. Modificações em outras interfaces de integração SAP além da SGMM03
5. Implantação em outras divisões do grupo que não a VIX Matriz (exceto se confirmado após avaliação de L4)
6. Desenvolvimento de novas funcionalidades no módulo PM/FI além dos 2 campos especificados

---

### CRITÉRIOS DE SUCESSO

1. **100% das OMs InterCompany** criadas ou alteradas após o go-live têm os campos Empresa e
   Contrato gravados automaticamente no SAP via integração SGMM03 — verificado por relatório
   de comparação SGM × SAP nos primeiros 15 dias de produção.

2. **Zero preenchimentos manuais residuais** dos campos Empresa e Contrato nas OMs InterCompany
   após o go-live — verificado via auditoria de OMs abertas na primeira semana de operação.

3. **Aceite formal da solicitante** (Jenifer dos Santos Carvalho / VIX Matriz) após testes de
   homologação (UAT) confirmando que o comportamento da integração atende à necessidade descrita
   no Chamado #6800446.

4. **Go-live realizado até 31/07/2026** com ambiente de produção estável por 15 dias consecutivos
   sem incidentes relacionados à integração dos novos campos.

5. **Documentação técnica entregue** ao time de sustentação PM/FI da DTI antes do encerramento
   formal do projeto.

---

### PREMISSAS

1. A interface SGMM03 está operacional no ambiente SAP da VIX Matriz e pode ser modificada
   sem impacto em outras integrações ativas.
2. O time técnico da consultoria selecionada tem experiência com o módulo PM do SAP e
   conhece (ou consegue obter) a documentação técnica da interface SGMM03.
3. Os campos Empresa e Contrato existem como campos válidos na estrutura da OM no SAP PM
   e podem receber valores via interface sem customização de dicionário de dados.
4. Os ambientes de desenvolvimento (DEV), qualidade (QAS) e produção (PRD) do SAP estão
   disponíveis para testes e implantação dentro do prazo do projeto.
5. A solicitante (VIX Matriz) disponibilizará casos de teste representativos para o UAT.
6. O campo Centro de Planejamento (implementado anteriormente) pode servir como referência
   técnica para a implementação dos campos Empresa e Contrato.

---

### RESTRIÇÕES

1. **Orçamento:** Envelope máximo de **R$ 48.000** (teto referencial — a ser substituído pelo
   valor contratado após equalização das propostas). Valores acima requerem nova aprovação do sponsor.
2. **Prazo:** Conclusão até **31/07/2026** — sem prazo de negócio externo declarado, mas o
   SLA do ticket já está em atraso (81h42min desde 08/05/2026).
3. **Tecnologia:** A solução deve ser implementada **exclusivamente** via interface SGMM03
   existente — não são permitidas novas interfaces, processos batch ou desenvolvimentos fora
   do escopo do SGMM03.
4. **Ambiente:** Não são permitidas alterações no sistema SGM (escopo excluso).
5. **Mandante SAP:** A implementação deve seguir os padrões de transporte do Grupo Águia Branca
   (DEV → QAS → PRD), com aprovação do GP/DTI antes de cada promoção de ambiente.

---

### RISCOS DE ALTO NÍVEL

1. **Restrição técnica oculta nos campos Empresa/Contrato** — Risco de encontrar no SAP PM
   as mesmas restrições identificadas no campo Cenário/CenPlan, aumentando complexidade e prazo.
   Classificação: **MÉDIO**

2. **Prazo de seleção da consultora** — Atraso na equalização das propostas (além de 29/05)
   ou divergência entre consultoras pode postergar o kick-off, reduzindo folga de prazo.
   Classificação: **MÉDIO**

3. **Disponibilidade do ambiente SAP para testes** — Janelas de indisponibilidade dos ambientes
   DEV/QAS por outros projetos paralelos podem atrasar os ciclos de teste.
   Classificação: **BAIXO**

4. **Sponsor não designado** — A ausência de sponsor formal pode gerar falta de autoridade
   para aprovação de decisões técnicas e de escopo durante a execução.
   Classificação: **ALTO** (CB-1 aberta)

5. **Impacto não mapeado em outras divisões** — Se o fluxo InterCompany SGMM03 também for
   utilizado por outras empresas do grupo, a implementação pode ter escopo maior que o avaliado.
   Classificação: **MÉDIO** (lacuna L4 não resolvida)

---

### PARTES INTERESSADAS PRINCIPAIS

| Nome / Área | Papel no Projeto | Interesse Principal |
|-------------|-----------------|---------------------|
| Jenifer dos Santos Carvalho (VIX Matriz) | Solicitante / Usuária final | Eliminação do retrabalho manual |
| Jhonny Henrique M. F. de Freitas (VIX Matriz) | Parte interessada | Processo de manutenção InterCompany |
| João Gabriel Virígio Barbierato (VIX Matriz) | Parte interessada | Processo de manutenção InterCompany |
| Mara Rubia Silva Rocha (Holding DTI) | Gestora do chamado | Resolução do SLA em atraso |
| Sponsor (A CONFIRMAR — CB-1) | Sponsor executivo | Aprovação e monitoramento |
| Gerente de Projeto (A designar) | GP | Entrega no prazo e custo |
| Consultora selecionada (entre LinkUP, Ocean, Seletor ou MW) | Executora técnica | Contratação e execução |
| Time Sustentação ERP PM/FI (DTI) | Receptor da solução | Sustentabilidade da solução |

---

### ORÇAMENTO RESUMIDO

| Item | Estimativa |
|------|------------|
| Consultoria SAP PM/FI (desenvolvimento, testes, implantação) | R$ 29.000 |
| Gestão interna DTI (custo de oportunidade) | R$ 0 (recurso próprio) |
| Contingência (20%) | R$ 5.800 |
| **TOTAL APROVADO (REFERENCIAL)** | **R$ 34.800** |

> ⚠️ **CB-2 ABERTA:** Este orçamento é referencial. Deve ser substituído pelo valor contratado
> após seleção da consultora e aprovação formal do sponsor. Prazo: 02/06/2026.

---

### CRONOGRAMA SUMARIZADO

| Fase | Período | Duração |
|------|---------|---------|
| Resolução de CBs e contratação | 28/05 – 13/06/2026 | 2 semanas |
| Kick-off e especificação técnica | 16/06 – 20/06/2026 | 1 semana |
| Desenvolvimento e configuração SAP | 23/06 – 04/07/2026 | 2 semanas |
| Testes (DEV/QAS) e UAT | 07/07 – 18/07/2026 | 2 semanas |
| Go-live (PRD) e estabilização | 21/07 – 31/07/2026 | 1,5 semanas |
| **Buffer de contingência (15%)** | **01/08 – 08/08/2026** | **~1 semana** |
| **Conclusão máxima** | **08/08/2026** | — |

---

### APROVAÇÃO

```
Sponsor: _________________________________ Data: ___________
         [A CONFIRMAR — CB-1]

GP/PMO: __________________________________ Data: ___________

Solicitante: ______________________________ Data: ___________
             Jenifer dos Santos Carvalho
```

---
---

## PM CANVAS — DEM-2026-008

# PM CANVAS — Integração SGMM03 Campos Empresa e Contrato
Versão: 1.0 | Data: 2026-05-28

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│              PM CANVAS — DEM-2026-008 — INTEGRAÇÃO SGMM03 EMPRESA/CONTRATO             │
├──────────────────────────┬──────────────────────────────┬──────────────────────────────┤
│  1. POR QUÊ?             │  2. O QUÊ?                   │  3. QUEM?                    │
│                          │                              │                              │
│ Campos Empresa e         │ • Integração campo EMPRESA   │ Sponsor: A confirmar (CB-1)  │
│ Contrato da OM não são   │   SGM → SAP via SGMM03       │ Gestora DTI: Mara Rubia S.R. │
│ integrados do SGM para   │                              │ GP: A designar               │
│ o SAP no fluxo           │ • Integração campo CONTRATO  │ Solicitante: Jenifer (VIX)   │
│ InterCompany SGMM03      │   SGM → SAP via SGMM03       │ Copiados: Jhonny, João (VIX) │
│                          │                              │                              │
│ Resultado: retrabalho    │ • Evento: CRIAÇÃO de OM      │ Executora: Consultoria SAP   │
│ manual + risco de        │   (novo registro SAP)        │ PM/FI (LinkUP/Ocean/Seletor  │
│ inconsistência de dados  │                              │ ou MW — a selecionar)        │
│ entre os dois sistemas   │ • Evento: ALTERAÇÃO de OM    │                              │
│                          │   (atualização SAP existente)│ Sustentação: DTI PM/FI       │
│ Precedente: Centro de    │                              │                              │
│ Planejamento já          │ • Testes DEV/QAS/PRD         │                              │
│ integrado na mesma       │ • UAT com VIX Matriz         │                              │
│ interface                │ • Documentação técnica       │                              │
│                          │ • Repasse sustentação DTI    │                              │
├──────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│  4. COMO?                │  5. QUANDO?                  │  6. QUANTO?                  │
│                          │                              │                              │
│ Metodologia cascata      │ Resolução CBs: até 13/06     │ Consultoria SAP: R$ 29.000   │
│ (waterfall) adaptada     │ Kick-off:      16/06/2026    │ Contingência (20%): R$ 5.800 │
│ para escopo cirúrgico    │ Especificação: 16–20/06      │ ─────────────────────────── │
│ e prazo curto            │ Desenvolvimento: 23/06–04/07 │ TOTAL REFERENCIAL: R$ 34.800 │
│                          │ Testes/UAT:    07/07–18/07   │                              │
│ Interface: SGMM03        │ Go-live:       21/07–31/07   │ ⚠️ CB-2: substituir após     │
│ Módulo SAP: PM + FI      │ Buffer:        01/08–08/08   │ contratação formal           │
│                          │ ─────────────────────────── │                              │
│ Transporte: DEV→QAS→PRD  │ Duração total: ~7 semanas    │ BAC (para EVM): R$ 34.800   │
│ (padrão GAB)             │ Com buffer: ~8 semanas       │                              │
├──────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│  7. PREMISSAS            │  8. RESTRIÇÕES               │  9. RISCOS                   │
│                          │                              │                              │
│ • SGMM03 está ativa e    │ • Prazo: go-live até 31/07   │ • Sponsor não designado      │
│   modificável sem        │   (com buffer até 08/08)     │   [ALTO — CB-1 aberta]       │
│   impacto em outras      │ • Orçamento: ≤ R$ 34.800     │                              │
│   integrações            │   (referencial — CB-2)       │ • Restrição técnica oculta   │
│                          │ • Implementação exclusiva    │   nos campos Empresa/Contrato │
│ • Campos Empresa e       │   via SGMM03 (sem novas      │   (como Cenário/CenPlan)     │
│   Contrato existem no    │   interfaces)                │   [MÉDIO]                    │
│   SAP PM como campos     │ • Não alterar SGM (origem    │                              │
│   válidos para gravação  │   fora do escopo)            │ • Atraso na seleção da       │
│                          │ • Transporte: DEV→QAS→PRD    │   consultora → kick-off      │
│ • Consultora selecionada │   obrigatório                │   atrasado [MÉDIO]           │
│   tem exp. SAP PM        │ • Não escopo: outros campos  │                              │
│                          │   SGMM03 e Cenário/CenPlan   │ • Impacto não mapeado em     │
│ • VIX Matriz disponível  │                              │   outras divisões GAB (L4)   │
│   para UAT               │                              │   [MÉDIO]                    │
└──────────────────────────┴──────────────────────────────┴──────────────────────────────┘
```

---
---

## PLANO GERAL DO PROJETO — DEM-2026-008

# PLANO GERAL DO PROJETO — Integração SGMM03 Empresa/Contrato
Versão: 1.0 | Data: 2026-05-28

---

### 1. Plano de Gerenciamento do Escopo

**Abordagem:** O escopo é estritamente delimitado pelos 2 campos (Empresa e Contrato) na interface
SGMM03 para os eventos de criação e alteração de OM. A WBS é decomposta até o nível de atividade
de configuração técnica. O GP valida o escopo antes de cada entregável.

**Ferramenta:** WBS em Markdown + dicionário de pacotes de trabalho no cronograma.

**Responsável:** GP + Mara Rubia (validação de negócio) + Consultora (execução técnica)

**Processo de mudança de escopo:**
1. Qualquer inclusão de campo ou funcionalidade além dos 2 campos definidos requer Change Request formal
2. GP avalia impacto em prazo e custo
3. Sponsor aprova qualquer mudança com impacto financeiro acima de R$ 2.000
4. Baseline atualizado após aprovação — versão incrementada

---

### 2. Plano de Gerenciamento do Cronograma

**Abordagem:** Cascata com fases sequenciais (especificação → desenvolvimento → testes → go-live).
Reuniões semanais de acompanhamento com a consultora durante a execução.

**Ferramenta:** Cronograma em Markdown (este documento + arquivo cronograma.md)

**Frequência de atualização:** Semanal durante a execução

**Indicadores:**
- SPI (Schedule Performance Index): alerta se < 0,85
- Desvio de prazo: alerta se > 5 dias úteis em relação ao baseline

---

### 3. Plano de Gerenciamento dos Custos

**Abordagem:** Controle por marcos de faturamento (não por hora). O pagamento à consultora
será estruturado em 2–3 marcos vinculados a entregáveis aprovados (ex: especificação técnica,
go-live, documentação).

**Ferramenta:** Planilha de controle de custo — comparação entre orçamento aprovado e NFs emitidas

**Frequência de atualização:** A cada emissão de NF / aprovação de marco

**Indicadores:**
- CPI (Cost Performance Index): alerta se < 0,85
- EAC (Estimate at Completion): comparado ao BAC de R$ 34.800

---

### 4. Plano de Gerenciamento da Qualidade

**Abordagem:** Ciclos de teste estruturados em 3 níveis antes do go-live.

**Critérios de qualidade do produto:**
- 100% dos casos de teste Must Have aprovados no UAT
- Zero erros de integração nos campos Empresa e Contrato após go-live
- Documentação técnica revisada e aprovada pelo time de sustentação PM/FI

**Processo de revisão:**
- DEV: Consultora executa testes unitários e de integração
- QAS: DTI + Consultora executam testes sistêmicos
- UAT: VIX Matriz (Jenifer + equipe) valida funcionalidade de negócio
- PRD: Go-live monitorado nos primeiros 15 dias (período de garantia)

---

### 5. Plano de Gerenciamento dos Recursos

**Abordagem:** Recursos externos (consultora) gerenciados via contrato com marcos e SLA.
Recursos internos (DTI) dedicados parcialmente conforme disponibilidade.

**Papéis e responsabilidades (RACI simplificado):**

| Atividade | Consultora | DTI/Mara | GP | VIX/Jenifer |
|-----------|-----------|----------|-----|-------------|
| Especificação técnica | R | C | A | I |
| Desenvolvimento SAP | R | I | A | I |
| Testes DEV/QAS | R | C | A | I |
| UAT | C | I | A | R |
| Go-live | R | A | A | I |
| Documentação | R | A | I | I |

R=Responsável, A=Aprovador, C=Consultado, I=Informado

**Resolução de conflitos:** Escalada ao sponsor para decisões com impacto > 1 semana de prazo.

---

### 6. Plano de Gerenciamento das Comunicações

| Comunicação | Audiência | Frequência | Canal | Responsável |
|-------------|-----------|------------|-------|-------------|
| Status Report | Sponsor + Mara Rubia + Jenifer | Quinzenal | E-mail | GP |
| Reunião de acompanhamento | GP + Consultora | Semanal (durante execução) | Teams/presencial | GP |
| Relatório de testes | DTI + Jenifer | A cada ciclo de testes | E-mail | Consultora |
| Comunicado de go-live | Todos os stakeholders | Pontual (no go-live) | E-mail | GP |
| Alerta de risco/desvio | Sponsor | Imediato | E-mail/Teams | GP |

---

### 7. Plano de Gerenciamento dos Riscos

**Abordagem:** Identificação na iniciação + revisão a cada status report quinzenal.
Riscos novos identificados durante a execução são adicionados ao registro e avaliados pelo GP.

**Ferramenta:** Registro de Riscos em Markdown (arquivo plano-riscos.md)

**Frequência de revisão:** Quinzenal (junto ao status report)

**Alerta automático:** Risco nível ALTO → notificação imediata ao sponsor via e-mail

---

### 8. Plano de Gerenciamento das Aquisições

**Abordagem:** Make or buy — 100% da execução técnica SAP será contratada externamente.
A DTI atuará como gestora do contrato e validadora técnica.

**Processo de contratação:**
1. Equalização das 4 propostas recebidas (29/05/2026)
2. Seleção da consultora pelo critério técnico-comercial (prazo + custo + experiência PM)
3. Emissão do Work Request formal (WR) antes do contrato
4. Assinatura do contrato com marcos e SLA de testes
5. Aprovação do sponsor obrigatória para valores acima do referencial (R$ 34.800)

**Fornecedores em avaliação:** LinkUP, Ocean, Seletor, MW

---

### 9. Plano de Gerenciamento dos Stakeholders

**Abordagem:** Engajamento ativo da VIX Matriz (usuária final) em todas as fases de validação.
Sponsor engajado nos marcos de aprovação. Consultora gerenciada formalmente via contrato.

**Ferramenta:** Registro de Stakeholders (seção "Partes Interessadas" do TAP)

**Estratégia por grupo:**
- VIX Matriz: engajamento alto em UAT e validação funcional
- Holding DTI / Mara Rubia: engajamento contínuo — ponto focal do projeto
- Sponsor: engajamento nos marcos de aprovação e decisões críticas
- Consultora: comunicação formal via reuniões semanais e relatórios de progresso

**Frequência de revisão:** Mensal (ou quando mudança de stakeholder relevante)

---

### 10. Plano de Gerenciamento das Mudanças

**Processo de solicitação de mudança (Change Request):**
1. Qualquer parte interessada identifica necessidade de mudança e comunica ao GP
2. GP preenche formulário de Change Request com: descrição da mudança, impacto em escopo/prazo/custo/qualidade
3. Impacto ≤ R$ 2.000 e ≤ 2 dias úteis: GP aprova
4. Impacto > R$ 2.000 ou > 2 dias úteis: Sponsor aprova
5. Mudanças aprovadas: baseline atualizado com nova versão do documento
6. Mudanças recusadas: documentadas com justificativa no registro de mudanças

---

### Ciclo de Vida e Gates

| Gate | Critério de Progressão | Aprovador |
|------|----------------------|-----------|
| G0 — Qualificação aprovada | Qualificação 50/100 APROVADA COM CONDIÇÕES + CBs registradas | VMO (auto) |
| G1 — Iniciação aprovada | TAP assinado + orçamento formalizado (CB-2 resolvida) + sponsor nomeado (CB-1) | Sponsor |
| G2 — Especificação aprovada | Especificação técnica assinada pela consultora e pelo GP | GP + Consultora |
| G3 — Desenvolvimento completo | 100% dos RF Must Have implementados em QAS, aprovados pelo GP | GP + DTI |
| G4 — UAT aprovado e go-live autorizado | Casos de teste Must Have 100% aprovados pela VIX Matriz | Sponsor + Jenifer |
| G5 — Encerramento | Documentação técnica entregue à sustentação + aceite formal da VIX Matriz | Sponsor + Jenifer |
