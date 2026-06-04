# Roteiro Completo: Replicando VMO Autônomo no Copilot Studio

> **Objetivo:** Reproduzir o sistema VMO Autônomo (orquestração de 13 agentes de IA para gestão de projetos) usando Microsoft Copilot Studio + Power Automate + Dataverse.

---

## VISÃO GERAL DA ARQUITETURA

### Como o projeto original funciona (Opensquad + Claude)

```
Usuário → Claude Code → Runner (runner.pipeline.md)
                           ↓
          squad.yaml + 13 agentes (agent.md)
                           ↓
          26 steps em sequência com checkpoints
                           ↓
          Documentos .md → PDF via ReportLab
                           ↓
          Dashboard HTML + WebSocket real-time
```

### Como vai funcionar no Copilot Studio

```
Usuário → Copilot Studio (Agente Orquestrador "Oscar")
                  ↓
     Topics (um por agente/fase do pipeline)
                  ↓
     Power Automate Flows (automação dos steps)
                  ↓
     Dataverse (estado + documentos)
                  ↓
     Word/PDF via Power Automate → SharePoint/OneDrive
                  ↓
     Power BI Dashboard ou SharePoint page
```

---

## PRÉ-REQUISITOS

Antes de começar, você vai precisar de:

- [ ] **Microsoft 365** com licença que inclua Copilot Studio (ex: M365 E3/E5 + Power Platform)
- [ ] **Copilot Studio** acesso em: https://copilotstudio.microsoft.com
- [ ] **Power Automate** acesso em: https://make.powerautomate.com
- [ ] **Dataverse** (vem junto com Power Platform)
- [ ] **SharePoint** para armazenar documentos
- [ ] **Azure OpenAI** (opcional, para modelos GPT-4 diretamente)

---

## PARTE 1 — CONFIGURAÇÃO DO AMBIENTE

### PASSO 1.1 — Acessar o Copilot Studio

1. Acesse: **https://copilotstudio.microsoft.com**
2. Faça login com sua conta Microsoft 365
3. No canto superior, selecione o **ambiente** (Environment) correto
   - Se não tiver ambiente criado: vá em **Power Platform Admin Center** → Environments → New
   - Nome sugerido: `VMO-Producao`

**📸 Print esperado:** Tela inicial do Copilot Studio com lista de agentes (provavelmente vazia)

---

### PASSO 1.2 — Criar o Ambiente no Dataverse

No **Power Platform Admin Center** (admin.powerplatform.microsoft.com):

1. Clique em **Environments → New**
2. Preencha:
   - Name: `VMO Gestão de Projetos`
   - Type: `Production` (ou `Sandbox` para testes)
   - Region: `Brazil South` (ou mais próximo)
   - Create database: **Yes**
   - Currency: `BRL`
   - Language: `Portuguese (Brazil)`
3. Clique **Save** e aguarde (~5 minutos)

**📸 Print esperado:** Ambiente criado com status "Ready"

---

### PASSO 1.3 — Criar as Tabelas no Dataverse

No **Power Apps** (make.powerapps.com) → selecione o ambiente VMO:

1. Vá em **Dataverse → Tables → New Table**

#### Tabela 1: `vmo_projeto`
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| `vmo_codigo` | Text (100) | Sim | Ex: PROJ-2026-001 |
| `vmo_titulo` | Text (500) | Sim | Nome do projeto |
| `vmo_status` | Choice | Sim | em_qualificacao, em_iniciacao, em_planejamento, aprovado, reprovado |
| `vmo_step_atual` | Number (Integer) | Sim | Step atual (1-26) |
| `vmo_solicitante` | Text (200) | Não | Nome do solicitante |
| `vmo_area` | Text (200) | Não | Área solicitante |
| `vmo_descricao` | Text Area | Não | Descrição da demanda |
| `vmo_score_qualificacao` | Number (Decimal) | Não | Score 0-30 |
| `vmo_score_vera` | Number (Decimal) | Não | Score qualidade 0-100 |
| `vmo_data_inicio` | Date | Não | Data de início |
| `vmo_data_aprovacao` | Date | Não | Data de aprovação final |
| `vmo_sponsor` | Text (200) | Não | Nome do sponsor executivo |
| `vmo_json_state` | Text Area (Max) | Não | JSON completo do estado |

**Como criar:**
1. Clique **New Table**
2. Name: `Projeto VMO`
3. Display name plural: `Projetos VMO`
4. Primary column: `vmo_codigo`
5. Salve, depois adicione cada coluna clicando **+ New Column**

#### Tabela 2: `vmo_documento`
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| `vmo_tipo` | Choice | Sim | demanda, qualificacao, tap, requisitos, cronograma, riscos, kpis, status_report, revisao, auditoria |
| `vmo_conteudo` | Text Area (Max) | Sim | Conteúdo Markdown |
| `vmo_url_sharepoint` | URL | Não | Link do arquivo PDF/DOCX |
| `vmo_agente_gerador` | Text (100) | Não | Qual agente gerou |
| `vmo_versao` | Number (Integer) | Não | Versão (começa em 1) |
| `vmo_projeto_id` | Lookup → vmo_projeto | Sim | FK para projeto |

#### Tabela 3: `vmo_checkpoint`
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `vmo_numero_step` | Number | Qual step gerou o checkpoint |
| `vmo_mensagem` | Text Area | Mensagem para o usuário |
| `vmo_decisao` | Choice | pendente, aprovado, rejeitado |
| `vmo_comentario_usuario` | Text Area | Feedback do usuário |
| `vmo_projeto_id` | Lookup → vmo_projeto | FK para projeto |

**📸 Print esperado:** Tabelas criadas no Dataverse com todas as colunas visíveis no designer

---

## PARTE 2 — CRIAR O AGENTE PRINCIPAL NO COPILOT STUDIO

### PASSO 2.1 — Criar o Agente "VMO Orquestrador"

No **Copilot Studio**:

1. Clique **+ Create** (canto superior esquerdo)
2. Selecione **New agent**
3. Preencha:
   - **Name:** `VMO Orquestrador`
   - **Description:** `Sistema autônomo de gestão de projetos VMO. Coleta demandas, qualifica, documenta e audita projetos de TI.`
   - **Instructions (System Prompt):**

```
Você é Oscar, o Orquestrador do VMO Squad da VMO Consultoria.

EMPRESA: VMO Consultoria — especializada em transformação de PMO para VMO (Value Management Office). Responsável: Marcelo Silveira.

SEU PAPEL: Você é o maestro do processo. Você recebe demandas de projetos, coordena os agentes especializados (Iara, Felipe, Diana, Rafael, Carlos, Pedro, Marcela, Fábio, Sara, Vera e Gabriel) e garante que cada entrega atende aos padrões VMO antes de avançar.

PRINCÍPIOS INEGOCIÁVEIS:
1. Nunca avançar um step sem validar o output do anterior
2. Exigir aprovações obrigatórias (Diretoria da área + Gerente de TI) antes de qualquer validação
3. Nunca aceitar urgência alta (> 3/10) sem evidência documental (email ou ata)
4. Projetos de TI sem sponsor designado (Diretor+) devem ser bloqueados

FLUXO DO PROCESSO:
1. Coletar demanda (Iara)
2. Gate de intake (Gabriel)
3. Sizing inicial (Rafael)
4. Qualificar demanda - score 0-30 (Felipe)
5. Gate de qualificação (Gabriel)
6. Documentação base - TAP, Canvas, Plano (Diana)
7. Especificar requisitos ERF com MoSCoW (Rafael)
8. Criar Work Request/mini-RFP (Fábio)
9. Criar cronograma e WBS (Carlos)
10. Plano de riscos (Pedro)
11. Framework de KPIs e EVM (Marcela)
12. Status Report inicial (Sara)
13. Revisão de qualidade - score 0-100 (Vera)
14. Auditoria de governança (Gabriel)
15. Aprovação final pelo usuário

IDIOMA: Sempre em Português (Brasil).
TOM: Profissional, executivo, direto. Sem floreios.
```

4. Clique **Create**

**📸 Print esperado:** Agente criado com tela de configuração mostrando nome, descrição e instruções

---

### PASSO 2.2 — Configurar Conhecimento (Knowledge) do Agente

Ainda no agente **VMO Orquestrador**, vá na aba **Knowledge**:

1. Clique **+ Add knowledge**
2. Selecione **SharePoint** (ou Files)
3. Adicione os documentos de referência (você vai criar estes arquivos):
   - `criterios-qualidade-vmo.docx` — critérios de qualidade e BLOCKING rules
   - `perfil-empresa-vmo.docx` — perfil da VMO Consultoria
   - `metodologia-vmo.docx` — metodologia e padrões

Para criar estes documentos de referência, copie o conteúdo das seções relevantes deste roteiro e salve no SharePoint.

**📸 Print esperado:** Aba Knowledge mostrando documentos adicionados com status "Synced"

---

### PASSO 2.3 — Configurar as Actions (Conexões com Dataverse)

Na aba **Actions** do agente:

1. Clique **+ Add action**
2. Selecione **Dataverse** nas conexões disponíveis
3. Adicione as seguintes ações:

**Ação 1: Criar Projeto**
- Action name: `Criar Novo Projeto VMO`
- Table: `Projetos VMO`
- Operation: `Create a row`
- Inputs expostos ao agente: codigo, titulo, solicitante, area, descricao

**Ação 2: Atualizar Status do Projeto**
- Action name: `Atualizar Status do Projeto`
- Table: `Projetos VMO`
- Operation: `Update a row`
- Inputs: ID do projeto, status, step_atual

**Ação 3: Salvar Documento**
- Action name: `Salvar Documento do Projeto`
- Table: `Documentos VMO`
- Operation: `Create a row`
- Inputs: tipo, conteudo, agente_gerador, projeto_id

**Ação 4: Listar Projetos**
- Action name: `Listar Projetos VMO`
- Table: `Projetos VMO`
- Operation: `List rows`
- Filtro opcional por status

**📸 Print esperado:** Aba Actions mostrando 4 ações configuradas com ícones do Dataverse

---

## PARTE 3 — CRIAR OS TOPICS (FLUXOS DE CONVERSA)

Cada agente do VMO Squad original vira um **Topic** no Copilot Studio.

### PASSO 3.1 — Topic: "Iniciar Novo Projeto"

No agente VMO Orquestrador → aba **Topics** → **+ Add topic** → **From blank**:

**Configuração:**
- Name: `Iniciar Novo Projeto`
- Trigger phrases:
  - `quero abrir um projeto`
  - `nova demanda`
  - `tenho um projeto`
  - `iniciar projeto`
  - `registrar demanda`

**Fluxo do Topic (construa no designer):**

```
[Trigger: Frases acima]
        ↓
[Message Node]
"Olá! Sou o Oscar, Orquestrador do VMO Squad. 
Vou coordenar o processo completo de iniciação do seu projeto. 
Antes de começar, preciso coletar algumas informações com a Iara Inbound."
        ↓
[Question Node - Iara Inbound]
Pergunta: "Qual é o título ou descrição resumida da demanda/projeto?"
Salvar em: {demanda_titulo}
        ↓
[Question Node]
Pergunta: "Quem é o solicitante? (nome e cargo)"
Salvar em: {demanda_solicitante}
        ↓
[Question Node]
Pergunta: "Qual área ou departamento está solicitando?"
Salvar em: {demanda_area}
        ↓
[Question Node]
Pergunta: "Descreva a necessidade/problema que originou essa demanda:"
Salvar em: {demanda_descricao}
        ↓
[Question Node]
Pergunta: "Qual é o benefício esperado? (ex: redução de custo, ganho de eficiência, conformidade)"
Salvar em: {demanda_beneficio}
        ↓
[Question Node]
Pergunta: "Qual o nível de urgência de 1 a 10? Se > 3, anexe o email ou ata que justifica."
Salvar em: {demanda_urgencia}
        ↓
[Question Node]
Pergunta: "Quem aprovou esta demanda na Diretoria da área solicitante? (nome e cargo)"
Salvar em: {aprovacao_diretoria}
        ↓
[Question Node]
Pergunta: "Quem aprovou no lado da TI? (Gerente de TI ou superior)"
Salvar em: {aprovacao_ti}
        ↓
[Action Node → Power Automate: "Criar Projeto e Documentar Demanda"]
Inputs: todos os campos acima
Output: {codigo_projeto} (ex: PROJ-2026-008)
        ↓
[Message Node]
"✅ Demanda coletada pela Iara Inbound!
Projeto criado: **{codigo_projeto}**
Agora o Gabriel Governança irá realizar o Gate de Intake..."
        ↓
[Redirect → Topic: "Gate de Intake"]
```

**📸 Print esperado:** Designer de topic com os nodes de pergunta encadeados visíveis

---

### PASSO 3.2 — Topic: "Gate de Intake"

**Name:** `Gate de Intake`
**Trigger:** Interno (chamado via Redirect do topic anterior)

**Fluxo:**

```
[Message Node]
"🛡️ **Gabriel Governança — Gate de Intake**
Analisando conformidade com regras VMO..."
        ↓
[Generative AI Node - ou Action para GPT]
Prompt para o modelo:
"Você é Gabriel Governança, auditor VMO. 
Analise esta demanda e verifique:
1. ✅/❌ Aprovação da Diretoria da área: {aprovacao_diretoria}
2. ✅/❌ Aprovação do Gerente de TI: {aprovacao_ti}
3. ✅/❌ Urgência {demanda_urgencia}/10 — se > 3, há evidência documental?
4. ✅/❌ Demanda tem descrição de necessidade clara

Se algum item crítico falhar, marque como BLOQUEADO.
Gere um relatório Gate de Intake resumido."
        ↓
[Condition Node]
SE response contém "BLOQUEADO"
  → [Message] "❌ Demanda bloqueada no Gate de Intake. Corrija os itens indicados e reabra."
  → [End conversation]
SENÃO
  → [Message] "✅ Gate de Intake aprovado! Avançando para o Sizing Inicial com Rafael..."
  → [Redirect → Topic: "Checkpoint 1 - Validar Demanda"]
```

---

### PASSO 3.3 — Topic: "Checkpoint 1 - Validar Demanda"

Este topic pausa o processo e pede confirmação ao usuário:

```
[Message Node]
"⏸️ **CHECKPOINT 1 — Validação da Demanda**

**Projeto:** {codigo_projeto}
**Demanda:** {demanda_titulo}
**Solicitante:** {demanda_solicitante} / {demanda_area}

O Gate de Intake foi aprovado. Confirme para prosseguir com:"
        ↓
[Choice Node]
Opções:
- "✅ Confirmar e avançar para Qualificação"
- "✏️ Corrigir informações da demanda"
- "❌ Cancelar projeto"

SE "Confirmar"
  → [Redirect → Topic: "Sizing e Qualificação"]
SE "Corrigir"
  → [Redirect → Topic: "Iniciar Novo Projeto"] (recomeça)
SE "Cancelar"
  → [Action: Atualizar status para "cancelado"]
  → [Message] "Projeto cancelado. Até logo!"
```

---

### PASSO 3.4 — Topic: "Sizing e Qualificação"

```
[Message Node]
"📐 **Rafael Requisito — Sizing Inicial**
Estimando esforço e complexidade..."
        ↓
[Generative AI Node]
Prompt:
"Você é Rafael Requisito, especialista em sizing de projetos TI.
Com base na demanda: {demanda_descricao}
Estime:
- Complexidade: Baixa/Média/Alta/Muito Alta
- Esforço estimado: X a Y dias-homem
- Número estimado de requisitos funcionais: N
- Equipes envolvidas
- Tipo de projeto: Melhoria/Novo desenvolvimento/Integração/Manutenção
Justifique cada estimativa."
        ↓
[Salvar em variável: {sizing_resultado}]
        ↓
[Message Node]
"🔍 **Felipe Filtro — Qualificação da Demanda**
Calculando score de qualificação (0-30)..."
        ↓
[Generative AI Node]
Prompt:
"Você é Felipe Filtro. Avalie esta demanda com score de 0-30:
Demanda: {demanda_descricao}
Sizing: {sizing_resultado}
Benefício: {demanda_beneficio}
Urgência: {demanda_urgencia}
Aprovações: Diretoria={aprovacao_diretoria}, TI={aprovacao_ti}

Critérios (0-3 cada, total 10 critérios):
1. Clareza da necessidade
2. Alinhamento estratégico
3. Benefício mensurável
4. Viabilidade técnica
5. Recursos disponíveis
6. Prazo realista
7. Esforço (use o sizing do Rafael — OBRIGATÓRIO)
8. Risco aceitável
9. Sponsor identificável
10. Aprovações documentadas

Score < 15 = REPROVAR, 15-20 = CONDICIONAL, 21-30 = APROVAR
Gere tabela com nota e justificativa por critério."
        ↓
[Condition: score >= 15]
SE aprovado/condicional
  → [Redirect → Topic: "Checkpoint 2 - Aprovar Qualificação"]
SE reprovado
  → [Message] "❌ Score {score}/30 — abaixo do mínimo. Demanda não qualificada."
  → [Action: Atualizar status projeto para "reprovado"]
```

---

### PASSO 3.5 — Topic: "Checkpoint 2 - Aprovar Qualificação"

```
[Message Node]
"⏸️ **CHECKPOINT 2 — Aprovação da Qualificação**

**Score Felipe Filtro:** {score}/30 — {classificacao}
**Sizing Rafael:** {sizing_resultado}

{resultado_qualificacao}

Confirme para prosseguir com a documentação completa do projeto."
        ↓
[Choice Node]
- "✅ Aprovar e iniciar documentação"
- "📝 Solicitar ajuste na qualificação"
- "❌ Reprovar projeto"
        ↓
[Redirect conforme escolha]
```

---

### PASSO 3.6 — Topics da Fase de Documentação

Crie um topic separado para cada documento. Estrutura padrão:

#### Topic: "Gerar Documentação Base (Diana)"

```
[Message Node] "📋 Diana Documento — Criando TAP, PM Canvas e Plano Geral..."
        ↓
[Generative AI Node]
Prompt:
"Você é Diana Documento, especialista em documentação de projetos PMO/VMO.
Com base nos dados do projeto:
- Título: {demanda_titulo}
- Descrição: {demanda_descricao}
- Benefício: {demanda_beneficio}
- Sizing: {sizing_resultado}
- Qualificação: {resultado_qualificacao}

Gere em português:

## 1. TERMO DE ABERTURA DO PROJETO (TAP)
- Objetivo SMART
- Sponsor executivo (a confirmar)
- Escopo incluído/excluído
- Critérios de sucesso (3-5 mensuráveis)
- Orçamento estimado
- Prazo estimado

## 2. PM CANVAS (9 blocos)
- Por quê (justificativa)
- O quê (produto/entrega)
- Quem (stakeholders)
- Como (abordagem)
- Quando (marco principal)
- Onde (onde será implementado)
- Quanto (estimativa)
- Risco principal
- Critério de sucesso

## 3. PLANO GERAL DO PROJETO
- Fases
- Responsáveis por fase
- Dependências críticas
- Pontos de atenção"
        ↓
[Action: Salvar documento tipo=tap no Dataverse]
[Action: Chamar Power Automate → gerar PDF]
        ↓
[Message: "✅ Documentação base gerada! Próximo: Rafael vai especificar os requisitos..."]
[Redirect → Topic: "Especificar Requisitos (Rafael)"]
```

---

Repita o mesmo padrão para os outros agentes:

#### Topic: "Especificar Requisitos (Rafael)"
- Gerar ERF com RF001-RFN + RNF com MoSCoW
- Salvar como tipo=requisitos

#### Topic: "Criar Work Request (Fábio)"
- Gerar mini-RFP com 10 grupos de atividades
- Salvar como tipo=work_request

#### Topic: "Criar Cronograma (Carlos)"
- Gerar WBS 3 níveis + marcos + caminho crítico
- Salvar como tipo=cronograma

#### Topic: "Plano de Riscos (Pedro)"
- 5+ riscos com prob/impacto + estratégia
- Salvar como tipo=riscos

#### Topic: "Framework KPIs (Marcela)"
- EVM + BAC + curva S + KRs pós-go-live
- Salvar como tipo=kpis

#### Topic: "Status Report (Sara)"
- Status geral + progresso por dimensão
- Salvar como tipo=status_report

---

### PASSO 3.7 — Topic: "Revisão e Auditoria Final"

```
[Message] "✅ **Vera Veredito — Revisão de Qualidade**"
        ↓
[Generative AI Node - Vera]
Prompt:
"Você é Vera Veredito, revisora de qualidade VMO.
Avalie o pacote completo do projeto {codigo_projeto} de 0 a 100:
{todos_documentos_gerados}

CRITÉRIOS DE QUALIDADE (cada um vale pontos):
- Completude dos documentos (25 pts)
- Alinhamento com metodologia VMO (20 pts)
- Qualidade da documentação técnica (20 pts)
- Rastreabilidade requisitos → entregáveis (15 pts)
- Adequação do sizing e esforço (10 pts)
- Consistência entre documentos (10 pts)

Score < 70: REPROVAR (volta para Diana)
Score 70-84: APROVADO COM RESSALVAS
Score >= 85: APROVADO"
        ↓
[Condition: score >= 70]
SE reprovado → [Redirect → Topic: "Gerar Documentação Base (Diana)"]
SE aprovado → continua
        ↓
[Message] "🛡️ **Gabriel Governança — Auditoria Final**"
        ↓
[Generative AI Node - Gabriel]
Prompt:
"Você é Gabriel Governança, auditor VMO.
Execute checklist de governança para {codigo_projeto}:

BLOCKING RULES (se qualquer um falhar → NC-CRÍTICA):
□ Sponsor executivo designado (Diretor ou superior)
□ Aprovações documentadas (Diretoria área + Gerente TI)
□ TAP aprovado pelo sponsor
□ Orçamento aprovado ou em processo

NÃO-CONFORMIDADES MENORES:
□ Todos os documentos completos
□ Riscos mapeados com responsáveis
□ KPIs definidos e mensuráveis
□ Datas realistas no cronograma

Gere relatório de auditoria com NC-CRÍTICA e NC-MENOR numeradas."
        ↓
[Redirect → Topic: "Checkpoint Final"]
```

---

### PASSO 3.8 — Topic: "Checkpoint Final — Aprovação"

```
[Message]
"⏸️ **CHECKPOINT FINAL — Aprovação do Pacote Completo**

**Projeto:** {codigo_projeto}
**Score Vera Veredito:** {score_vera}/100
**Auditoria Gabriel:** {resultado_auditoria}

**Documentos gerados:**
✅ TAP + PM Canvas + Plano Geral
✅ Especificação de Requisitos (ERF)
✅ Work Request / Mini-RFP
✅ Cronograma e WBS
✅ Plano de Riscos
✅ Framework de KPIs
✅ Status Report Inicial"
        ↓
[Choice]
- "✅ APROVAR — Projeto pode avançar para execução"
- "⚠️ APROVAR COM RESSALVAS — detalhe as ressalvas"
- "🔄 REVISAR — solicitar ajustes específicos"
- "❌ REPROVAR — encerrar"
        ↓
[Action: Atualizar status projeto no Dataverse]
[Action: Power Automate → Gerar pacote PDF final e enviar por email]
[Message: "🎉 Projeto {codigo_projeto} concluído com sucesso! Pacote enviado para seu email."]
```

---

## PARTE 4 — CRIAR OS FLOWS NO POWER AUTOMATE

### PASSO 4.1 — Flow: "Criar Projeto e Documentar Demanda"

No **Power Automate** (make.powerautomate.com):

1. **+ New flow** → **Instant cloud flow**
2. Trigger: **When Copilot Studio calls a flow**
3. Adicione os Inputs:
   - `titulo` (Text)
   - `solicitante` (Text)
   - `area` (Text)
   - `descricao` (Text)
   - `beneficio` (Text)
   - `urgencia` (Text)
   - `aprovacao_diretoria` (Text)
   - `aprovacao_ti` (Text)

4. **Ações do Flow:**

```
[Compose: Gerar código do projeto]
Expression: concat('PROJ-', formatDateTime(utcNow(), 'yyyy'), '-', 
            padLeft(string(rand(1, 999)), 3, '0'))

[Dataverse: Add a new row]
Table: Projetos VMO
Campos:
  vmo_codigo: [output do Compose]
  vmo_titulo: [titulo]
  vmo_solicitante: [solicitante]
  vmo_area: [area]
  vmo_descricao: [descricao]
  vmo_status: "em_qualificacao"
  vmo_step_atual: 1
  vmo_data_inicio: [utcNow()]

[Dataverse: Add a new row] - documento demanda
Table: Documentos VMO
Campos:
  vmo_tipo: "demanda"
  vmo_conteudo: [conteúdo formatado em Markdown]
  vmo_agente_gerador: "iara-inbound"
  vmo_projeto_id: [ID do projeto criado]
  vmo_versao: 1

[Return value(s) to Power Virtual Agents]
  codigo_projeto: [vmo_codigo]
  projeto_id: [ID do registro]
```

5. Salve e publique o flow
6. No Copilot Studio, adicione este flow como Action no agente

**📸 Print esperado:** Flow designer mostrando trigger + compose + 2 Dataverse actions + return

---

### PASSO 4.2 — Flow: "Salvar Documento e Gerar PDF"

1. **+ New flow** → **Instant cloud flow**
2. Trigger: **When Copilot Studio calls a flow**
3. Inputs:
   - `projeto_id` (Text)
   - `tipo_documento` (Text)
   - `conteudo_markdown` (Text)
   - `agente_gerador` (Text)

4. **Ações:**

```
[Dataverse: Add a new row]
Table: Documentos VMO
  vmo_tipo: [tipo_documento]
  vmo_conteudo: [conteudo_markdown]
  vmo_agente_gerador: [agente_gerador]
  vmo_projeto_id: [projeto_id]

[Word Online: Populate a Microsoft Word template]
(Precisará de template .docx no SharePoint com marcadores)
Location: SharePoint site VMO
Document Library: Templates VMO
File: template-documento-vmo.docx
Fields: conteudo = [conteudo_markdown], titulo = [tipo_documento]

[SharePoint: Create file]
Site: [seu site SharePoint]
Folder: /VMO Projetos/[projeto_id]/
File Name: [tipo_documento]-[timestamp].docx
File Content: [output do Word]

[Dataverse: Update a row]
Table: Documentos VMO
  vmo_url_sharepoint: [URL do arquivo criado no SharePoint]

[Return values]
  documento_id: [ID]
  url_pdf: [URL SharePoint]
```

**Nota:** Para geração de PDF direto, use o conector **OneDrive for Business** com conversão, ou **Adobe PDF Services** se disponível no seu tenant.

---

### PASSO 4.3 — Flow: "Enviar Resumo Final por Email"

```
[Trigger: When Copilot Studio calls a flow]
Inputs: projeto_id, score_vera, status_final, email_destinatario

[Dataverse: List rows - documentos do projeto]
Filter: vmo_projeto_id eq '[projeto_id]'

[Office 365 Outlook: Send an email]
To: [email_destinatario]
Subject: "VMO - Projeto [codigo_projeto] - Pacote Completo Aprovado"
Body: HTML formatado com:
  - Resumo do projeto
  - Score Vera Veredito
  - Lista de documentos com links SharePoint
  - Status final
  - Próximos passos
```

---

## PARTE 5 — CONFIGURAR GENERATIVE AI

### PASSO 5.1 — Ativar Generative Answers

No agente **VMO Orquestrador** → **Settings** → **Generative AI**:

1. Enable: **Generative answers** → **On**
2. Model: Selecione o modelo disponível (GPT-4 Turbo recomendado)
3. Content moderation: **Medium**
4. Fallback behavior: **Show message** (não silencioso)

**📸 Print esperado:** Tela de configuração de AI com toggle "On" e modelo selecionado

---

### PASSO 5.2 — Configurar Nodes Generativos nos Topics

Para cada topic com Generative AI Node:

1. No designer do topic, adicione **+** → **Advanced** → **Generative answers**
2. Configure:
   - **Input:** Use variáveis do contexto (${demanda_descricao}, etc.)
   - **Data sources:** Selecione o Knowledge configurado no PASSO 2.2
   - **Max tokens:** 2000 (documentos técnicos precisam de espaço)
   - **Temperature:** 0.3 (mais determinístico para documentos técnicos)

**Alternativa: usar Action com Azure OpenAI diretamente**
- Se quiser mais controle, crie um Flow que chama Azure OpenAI API
- Isso permite prompts mais longos e controle total de parâmetros

---

## PARTE 6 — CRIAR O DASHBOARD

### PASSO 6.1 — Dashboard com Power BI

1. Abra **Power BI Desktop** (powerbi.microsoft.com)
2. **Get Data** → **Dataverse**
3. Conecte ao ambiente VMO e selecione:
   - Tabela `vmo_projeto`
   - Tabela `vmo_documento`

4. **Visualizações recomendadas:**

**Card: Total de Projetos**
- Métrica: COUNT(vmo_projeto)

**Gráfico de Barras: Projetos por Status**
- Eixo X: vmo_status
- Valores: COUNT

**Tabela: Últimos Projetos**
- Colunas: vmo_codigo, vmo_titulo, vmo_status, vmo_score_vera, vmo_data_inicio

**KPI: Score Médio Vera**
- Valor: AVG(vmo_score_vera)
- Alvo: 85

**Semáforo: Status por Projeto**
- Vermelho: reprovado/bloqueado
- Amarelo: em_andamento/checkpoint
- Verde: aprovado

5. Publique no **Power BI Service** e incorpore no Teams ou SharePoint

**📸 Print esperado:** Dashboard Power BI com 4 visualizações visíveis, filtros de data e status

---

### PASSO 6.2 — Alternativa: SharePoint Page como Dashboard

1. No **SharePoint**, crie uma página: `VMO - Dashboard de Projetos`
2. Adicione Web Parts:
   - **Power BI** (incorporar o report)
   - **List** (exibir projetos do Dataverse via SharePoint list sincronizada)
   - **Quick Links** (links para documentos)
3. Configure as permissões de acesso

---

## PARTE 7 — PUBLICAR E TESTAR

### PASSO 7.1 — Publicar o Agente

No Copilot Studio → **Publish**:

1. Clique **Publish** (canto superior direito)
2. Aguarde ~2 minutos
3. Vá em **Channels** → ative:
   - **Microsoft Teams** (recomendado — integra direto no Teams da empresa)
   - **SharePoint** (para embed em site interno)
   - **Websites** (para copiar o código de embed)

**Para Teams:**
1. Em Channels → Microsoft Teams → **Add to Teams**
2. Baixe o `.zip` do app
3. No Teams Admin Center → Apps → Upload app → selecione o `.zip`
4. Habilite para os usuários

**📸 Print esperado:** Tela de Channels com Teams como canal ativo (badge verde "Published")

---

### PASSO 7.2 — Testar o Fluxo Completo

No Copilot Studio → **Test** (painel direito):

Teste esta sequência:

1. Escreva: `"quero abrir um projeto"`
2. Responda as perguntas da Iara (use dados fictícios):
   - Título: `"Integração Portal RH com SAP HCM"`
   - Solicitante: `"Ana Paula Santos, Gerente de RH"`
   - Área: `"Recursos Humanos"`
   - Descrição: `"Precisamos integrar o portal de autoatendimento de RH com o SAP HCM para eliminar retrabalho manual..."`
   - Benefício: `"Redução de 40% no tempo de processamento de solicitações de RH"`
   - Urgência: `"4"` (vai exigir evidência)
   - Aprovação Diretoria: `"Carlos Mendes, Diretor de RH"`
   - Aprovação TI: `"Roberto Lima, Gerente de TI"`
3. Confirme no Checkpoint 1
4. Observe a Qualificação (Felipe/Rafael)
5. Confirme no Checkpoint 2
6. Aguarde os documentos serem gerados
7. Confira no Dataverse se os registros foram criados

**Validação esperada:**
- Projeto criado com código `PROJ-2026-XXX`
- Documentos salvos na tabela `Documentos VMO`
- Status atualizando conforme o pipeline avança

---

## PARTE 8 — CONFIGURAÇÕES AVANÇADAS

### PASSO 8.1 — Autenticação e Segurança

No agente → **Settings** → **Security**:

1. **Authentication:** Configure para **Microsoft (Azure AD)** se o agente for interno
   - Isso garante que só colaboradores autenticados acessem o VMO
2. **User variables:** Capture automaticamente o email do usuário logado
   - Use `System.User.DisplayName` e `System.User.Email` nos topics

**No topic "Iniciar Novo Projeto", adicione:**
```
[Set Variable]
solicitante_email = System.User.Email
solicitante_nome = System.User.DisplayName
```

---

### PASSO 8.2 — Configurar Aprovações com Power Automate

Para o Checkpoint Final ser mais robusto, crie um flow de aprovação:

1. **+ New flow** → **Automated cloud flow**
2. Trigger: **When a row is added or modified** (Dataverse, Projetos VMO)
3. Condition: `vmo_status` = `"aguardando_aprovacao_final"`
4. Ação: **Start and wait for an approval**
   - Approval type: **Approve/Reject - Everyone must approve**
   - Assigned to: email do Marcelo Silveira + sponsor do projeto
   - Details: [resumo do projeto com links dos documentos]
5. Quando aprovado → atualizar status para `"aprovado"`
6. Quando rejeitado → atualizar para `"rejeitado"` + notificar

**📸 Print esperado:** Flow designer com Approval action e condições After Approval/After Rejection

---

### PASSO 8.3 — Memória e Histórico de Aprendizados

Para replicar o `memories.md` do projeto original, crie uma tabela adicional:

#### Tabela: `vmo_regra_business`
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `vmo_categoria` | Choice | proibicao, metodologia, preferencia |
| `vmo_descricao` | Text Area | Descrição da regra |
| `vmo_origem` | Text | Projeto que originou a regra |
| `vmo_ativa` | Boolean | Se a regra está ativa |

**Pré-populate com as regras do projeto original:**

Regra 1: `PROIBIÇÃO — Nunca validar demanda sem aprovações obrigatórias. Requer: (1) aprovação Diretoria área solicitante + (2) aprovação Gerente TI`
Regra 2: `PROIBIÇÃO — Nunca aceitar urgência > 3/10 sem evidência documental (email ou ata)`
Regra 3: `METODOLOGIA — Esforço (critério 7 Felipe) EXIGE sizing do Rafael. Felipe não pode estimar por benchmark`
Regra 4: `METODOLOGIA — Step de Sizing deve vir ANTES da Qualificação`

No Knowledge do agente, adicione uma conexão com esta tabela Dataverse para que o agente sempre consulte as regras antes de tomar decisões.

---

## PARTE 9 — CHECKLIST DE CONCLUSÃO

### Itens para marcar como concluídos:

**Infraestrutura:**
- [ ] Ambiente Dataverse criado
- [ ] 3 tabelas criadas (Projeto, Documento, Checkpoint)
- [ ] SharePoint site VMO criado com biblioteca de documentos
- [ ] Template Word para documentos criado

**Copilot Studio:**
- [ ] Agente VMO Orquestrador criado com system prompt
- [ ] Knowledge configurado (documentos de referência)
- [ ] 4+ Actions conectadas ao Dataverse
- [ ] Todos os topics criados (Iniciar, Gate, Checkpoints, Agentes, Final)
- [ ] Autenticação Azure AD configurada

**Power Automate:**
- [ ] Flow "Criar Projeto" publicado e testado
- [ ] Flow "Salvar Documento" publicado e testado
- [ ] Flow "Gerar PDF" funcionando
- [ ] Flow "Enviar Email Final" testado

**Dashboard:**
- [ ] Power BI conectado ao Dataverse
- [ ] Relatório publicado no Power BI Service
- [ ] Incorporado no Teams ou SharePoint

**Teste:**
- [ ] Fluxo completo testado com demanda fictícia
- [ ] Documentos gerados e salvos no SharePoint
- [ ] Email de confirmação recebido
- [ ] Dashboard atualizado com o novo projeto

---

## PARTE 10 — MAPEAMENTO: OPENSQUAD → COPILOT STUDIO

| Conceito Original (Opensquad) | Equivalente no Copilot Studio |
|-------------------------------|-------------------------------|
| `squad.yaml` | Configuração do agente (name, description, instructions) |
| `agent.md` (persona) | System prompt + Topics individuais por agente |
| `pipeline.yaml` (26 steps) | Topics encadeados via Redirects |
| `runner.pipeline.md` | Lógica dos topics + Flows no Power Automate |
| `state.json` | Registro no Dataverse (vmo_projeto + vmo_step_atual) |
| `quality-criteria.md` | Knowledge do agente + Generative AI Node prompts |
| `company.md` | System prompt do agente |
| `memories.md` | Tabela vmo_regra_business no Dataverse |
| Checkpoints | Choice nodes que pausam e pedem confirmação |
| `on_reject` (loop back) | Condition nodes com Redirect para topic anterior |
| `md_to_docs.py` (PDF) | Power Automate: Word template + SharePoint |
| Dashboard HTML | Power BI + Teams/SharePoint |
| WebSocket real-time | Power BI Auto-refresh ou SharePoint |
| `.mcp.json` (Playwright) | Não necessário no Copilot Studio |
| `squad-party.csv` | Topics nomeados por agente (iara, felipe, diana...) |

---

## ESTIMATIVA DE TEMPO

| Fase | Tempo Estimado |
|------|----------------|
| Configurar ambiente + Dataverse | 2-3 horas |
| Criar agente + topics principais | 4-6 horas |
| Criar todos os topics de agentes | 6-8 horas |
| Criar flows Power Automate | 3-4 horas |
| Dashboard Power BI | 2-3 horas |
| Testes e ajustes | 3-5 horas |
| **TOTAL** | **~20-29 horas** |

---

## DICAS IMPORTANTES

1. **Comece pelo MVP:** Implemente só o fluxo Iara → Gate → Checkpoint 1 → Felipe → Checkpoint 2 primeiro. Adicione os outros agentes depois.

2. **Use variables globais:** No Copilot Studio, crie variáveis globais para `codigo_projeto` e `projeto_id` que persistem entre topics.

3. **Teste cada topic isoladamente:** Use o Test Panel para testar cada topic antes de encadear.

4. **Generative AI tem limites:** Copilot Studio tem limite de tokens por mensagem. Para documentos longos (como o ERF com 37+ requisitos), divida em chamadas menores ou use um Flow com Azure OpenAI.

5. **Custo:** Copilot Studio cobra por **mensagem** (session). Estime ~50-80 mensagens por projeto completo. Planeje o orçamento conforme o volume.

6. **Logs:** Use **Analytics** no Copilot Studio para monitorar erros e abandono de sessão.

---

*Roteiro gerado em: 2026-06-04*
*Baseado no projeto VMO_GAB v0.1.14 (Opensquad)*
