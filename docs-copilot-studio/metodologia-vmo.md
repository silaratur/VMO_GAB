# Metodologia VMO — Guia Completo de Processos

**VMO Consultoria | Versão 1.0 | 2026**
**Responsável:** Marcelo Silveira

---

## 1. VISÃO GERAL DA METODOLOGIA

A metodologia VMO (Value Management Office) combina elementos do **PMBOK**, **metodologias ágeis** e **governança corporativa** adaptados à realidade de projetos de TI em empresas brasileiras de médio e grande porte.

### Princípio Central
> "Todo projeto só existe se gera valor mensurável para o negócio. A documentação não é burocracia — é a prova do valor."

### Os 3 Pilares
1. **Governança:** Aprovações formais, sponsors comprometidos, gates de qualidade
2. **Rastreabilidade:** Cada entregável liga a um benefício declarado
3. **Mensuração:** KPIs definidos antes do projeto começar, não depois

---

## 2. PIPELINE COMPLETO — 26 STEPS

### FASE 01 — QUALIFICAÇÃO (Steps 1–9)

#### Step 1 — Coletar Demanda (Iara Inbound)
**Objetivo:** Estruturar a demanda bruta em formato padronizado VMO.

**Entradas aceitas:**
- Email de solicitação
- Ticket de sistema (ServiceNow, Jira, etc.)
- PDF de briefing
- Conversa informal transcrita

**Campos obrigatórios a extrair:**
| Campo | Descrição |
|-------|-----------|
| Demandante | Nome completo, cargo, email |
| Área solicitante | Departamento/gerência |
| Necessidade | Problema ou oportunidade (máx. 3 parágrafos) |
| Pedido | O que especificamente está sendo solicitado |
| Benefício esperado | Resultado de negócio desejado (quantificado se possível) |
| Urgência | 1–10 com justificativa |
| Aprovação diretoria | Nome, cargo, forma de aprovação, data |
| Aprovação TI | Nome, cargo, forma de aprovação, data |
| Lacunas identificadas | Perguntas abertas, informações faltantes |

**Output:** `demanda-coletada.md` em `projects/PROJ-XXXX/01-qualificacao/`

---

#### Step 2 — Gate de Intake (Gabriel Governança)
**Objetivo:** Verificar conformidade mínima antes de investir tempo na análise.

**Critérios verificados:**
- ✅ Aprovação diretoria documentada
- ✅ Aprovação TI documentada
- ✅ Urgência com evidência (se > 3)
- ✅ Demanda tem descrição clara da necessidade

**Resultado:**
- **APROVADO:** Avança para Sizing
- **BLOQUEADO:** Demanda devolvida ao solicitante com lista de pendências

---

#### Step 3 — Checkpoint 1: Validar Demanda (Usuário)
**Objetivo:** Usuário (Marcelo) confirma que a demanda coletada está correta antes de investir análise.

**Ações possíveis:**
- Confirmar e avançar
- Corrigir informações
- Cancelar projeto

---

#### Step 4 — Sizing Inicial (Rafael Requisito)
**Objetivo:** Estimar esforço e complexidade para alimentar a qualificação.

**Entregáveis do sizing:**
| Item | Descrição |
|------|-----------|
| Tipo de projeto | Novo desenvolvimento / Melhoria / Integração / Manutenção |
| Complexidade | Baixa / Média / Alta / Muito Alta |
| Esforço estimado | Range em dias-homem (ex: 45–90 DH) |
| Nº estimado de RFs | Quantidade de requisitos funcionais prováveis |
| Equipes envolvidas | Áreas de TI, fornecedores, negócio |
| Premissas | Condições assumidas para o sizing |
| Restrições identificadas | Limitações técnicas, de prazo ou recursos |

**Nota crítica:** Este sizing é **obrigatório** antes de Felipe iniciar a qualificação.

**Output:** `sizing.md` em `projects/PROJ-XXXX/01-qualificacao/`

---

#### Step 5 — Qualificar Demanda (Felipe Filtro)
**Objetivo:** Calcular score 0–30 para decidir se o projeto vale ser iniciado.

**10 critérios (0–3 pts cada):**
1. Clareza da necessidade
2. Alinhamento estratégico
3. Benefício mensurável
4. Viabilidade técnica
5. Recursos disponíveis
6. Prazo realista
7. **Esforço estimado (Rafael)** — EM ESPERA se Rafael não fez sizing
8. Risco aceitável
9. Sponsor identificável
10. Aprovações documentadas

**Output:** `qualificacao.md` com tabela de scores, justificativas, classificação e condições (se CONDICIONAL)

---

#### Step 6 — Gate de Qualificação (Gabriel Governança)
**Objetivo:** Confirmar que a qualificação atende aos requisitos metodológicos.

**Verifica:**
- Score ≥ 15 (ou justificativa para exceção documentada)
- Critério 7 (Esforço) não está "EM ESPERA"
- Condições CONDICIONAIS estão listadas claramente

**Output:** `gate-qualificacao.md`

---

#### Step 7 — Checkpoint 2: Aprovar Qualificação (Usuário)
**Objetivo:** Usuário confirma score e condições antes de partir para documentação.

**Atenção:** Condições C1, C2, C3 devem ser explicitamente aceitas ou resolvidas.

---

### FASE 02 — INICIAÇÃO (Steps 10–11)

#### Step 8 — Criar Documentação Base (Diana Documento)
**Objetivo:** Produzir os documentos fundacionais do projeto.

**Entregáveis:**

**TAP — Termo de Abertura do Projeto**
| Campo | Conteúdo Esperado |
|-------|------------------|
| Objetivo | Frase SMART: específico, mensurável, alcançável, relevante, temporal |
| Sponsor | Nome, cargo, email, compromisso |
| Escopo incluído | Lista do que está dentro do projeto |
| Escopo excluído | Lista explícita do que está FORA |
| Critérios de sucesso | 3–5 critérios mensuráveis |
| Orçamento estimado | Faixa de R$ com fonte da estimativa |
| Prazo estimado | Data de início → data de entrega |
| Restrições | Limitações técnicas, políticas, de recursos |
| Premissas | O que está sendo assumido como verdadeiro |
| Aprovação | Assinatura do sponsor (ou validação formal) |

**PM Canvas (9 Blocos)**
| Bloco | Pergunta | Conteúdo |
|-------|----------|---------|
| Por quê | Qual o problema/oportunidade? | Justificativa de negócio |
| O quê | Qual o produto/entregável? | Descrição do resultado |
| Quem | Quem são os stakeholders? | Mapa de partes interessadas |
| Como | Qual a abordagem/metodologia? | Ágil, preditivo, híbrido |
| Quando | Qual o marco principal? | Data crítica do projeto |
| Onde | Onde será implementado? | Sistemas, locais, departamentos |
| Quanto | Qual a estimativa de custo? | Budget por fase |
| Risco | Qual o maior risco? | Risco principal com mitigação |
| Sucesso | Como saberemos que deu certo? | KPI principal e meta |

**Plano Geral do Projeto**
- Fases do projeto com objetivos de cada fase
- Responsáveis por fase (negócio + TI)
- Dependências críticas entre fases
- Pontos de atenção e riscos de planejamento

**Output:** `tap-canvas-plano-geral.md` em `projects/PROJ-XXXX/02-iniciacao/`

---

#### Step 9 — [ORQ] Oscar Avalia Documentação Base
**Oscar verifica:** completude do TAP, 9 blocos do Canvas preenchidos, sponsor definido.
Se reprovado: volta para Diana com lista de correções.

---

### FASE 03 — PLANEJAMENTO (Steps 12–23)

#### Step 10 — Especificar Requisitos (Rafael Requisito)
**Objetivo:** Detalhar o que o sistema/projeto deve fazer e como.

**ERF — Especificação de Requisitos Funcionais**

**Formato dos RFs:**
```
RF001 — [Nome do Requisito]
Prioridade: [Must / Should / Could / Won't]
Descrição: O sistema deve [ação] para [usuário] de forma que [resultado].
Critério de Aceitação: [condição testável e verificável]
Dependências: [RF002, RF005]
```

**Formato dos RNFs:**
```
RNF001 — [Categoria: Performance / Segurança / Usabilidade / Disponibilidade]
Descrição: [requisito não-funcional]
Métrica: [como será medido]
Meta: [valor alvo]
```

**Priorização MoSCoW:**
- **Must:** Requisito obrigatório — sem ele o projeto não entrega valor
- **Should:** Importante mas negociável
- **Could:** Desejável se houver tempo/budget
- **Won't:** Fora do escopo desta fase

**Output:** `erf-requisitos.md` em `projects/PROJ-XXXX/02-iniciacao/`

---

#### Step 11 — Criar Work Request / Mini-RFP (Fábio Fornecedor)
**Objetivo:** Estruturar a solicitação de proposta para fornecedores.

**10 Grupos de Atividades (estrutura padrão VMO):**

| Grupo | Categoria | Itens Típicos |
|-------|-----------|--------------|
| 1 | Análise e Levantamento | Reuniões, documentação AS-IS, validação requisitos |
| 2 | Design e Arquitetura | Solução técnica, modelagem dados, design interfaces |
| 3 | Desenvolvimento | Codificação, configuração, integrações |
| 4 | Testes | Unit tests, integração, UAT, performance |
| 5 | Documentação Técnica | Manual do sistema, documentação de API, runbook |
| 6 | Treinamento | Usuários finais, equipe TI, gestores |
| 7 | Implantação | Deploy, migração de dados, go-live |
| 8 | Suporte Pós-Go-Live | Período de estabilização (mínimo 30 dias) |
| 9 | Gestão do Projeto | PM do fornecedor, reuniões, status reports |
| 10 | Infraestrutura / Licenças | Servidores, licenças, acessos |

**Cada item deve ter:**
- Descrição clara
- Unidade de medida (hora, diária, unidade, pacote)
- Quantidade estimada
- Campo para preenchimento de preço pelo fornecedor

**Output:** `work-request.md` em `projects/PROJ-XXXX/03-planejamento/`

---

#### Step 12 — Criar Cronograma e WBS (Carlos Cronograma)
**Objetivo:** Estruturar o trabalho em pacotes gerenciáveis com linha do tempo.

**WBS — Work Breakdown Structure**
- Nível 1: Projeto
- Nível 2: Fases (Análise, Design, Desenvolvimento, Testes, Implantação)
- Nível 3: Entregas por fase
- Nível 4: Pacotes de trabalho (máx. 2 semanas cada)

**Cronograma**
- Data de início e fim por fase
- Marcos principais (milestones)
- Dependências entre atividades
- **Caminho Crítico:** sequência de atividades que define a duração mínima do projeto
- Baseline de prazo (data de referência imutável após aprovação)

**Output:** `cronograma-wbs.md` em `projects/PROJ-XXXX/03-planejamento/`

---

#### Step 13 — Plano de Riscos (Pedro Perigo)
**Objetivo:** Identificar e planejar resposta aos principais riscos.

**Formato padrão de risco:**
```
RISCO-001 — [Nome do risco]
Categoria: [Técnico / Pessoas / Processo / Externo / Financeiro]
Probabilidade: [1–5] | Impacto: [1–5] | Score: [P × I]
VME: R$ [valor × probabilidade%] (se aplicável)
Estratégia: [Evitar / Mitigar / Transferir / Aceitar]
Ação preventiva: [o que fazer ANTES do risco ocorrer]
Plano de contingência: [o que fazer SE o risco ocorrer]
Responsável: [nome/função]
Trigger (gatilho): [sinal de que o risco está se materializando]
Prazo de revisão: [data]
```

**Mínimo:** 5 riscos identificados para projetos de complexidade Média ou superior.

**Matriz de Prioridade:**
| Score | Prioridade | Cor |
|-------|-----------|-----|
| 1–4 | Baixo | 🟢 Verde |
| 5–9 | Médio | 🟡 Amarelo |
| 10–15 | Alto | 🟠 Laranja |
| 16–25 | Crítico | 🔴 Vermelho |

**Output:** `plano-riscos.md` em `projects/PROJ-XXXX/03-planejamento/`

---

#### Step 14 — Framework de KPIs (Marcela Métrica)
**Objetivo:** Definir como o sucesso será medido antes, durante e após o projeto.

**Estrutura do Framework:**

**EVM — Earned Value Management**
| Métrica | Fórmula | Interpretação |
|---------|---------|--------------|
| BAC | Budget At Completion | Total orçado para o projeto |
| PV | Planned Value | Valor planejado até a data |
| EV | Earned Value | Valor real realizado |
| AC | Actual Cost | Custo real incorrido |
| CPI | EV / AC | > 1 = dentro do orçamento |
| SPI | EV / PV | > 1 = adiantado no cronograma |
| EAC | BAC / CPI | Previsão de custo final |
| VAC | BAC − EAC | Variação de custo prevista |

**Curva S**
- Eixo X: Tempo (semanas/meses)
- Eixo Y: % de execução / custo acumulado
- Linha planejada vs linha real (desvio visível)

**KRs Pós-Go-Live (3–5 métricas)**
Cada KR deve ter:
- Nome da métrica
- Baseline atual (antes do projeto)
- Meta após 90 dias
- Meta após 180 dias
- Como será medido (sistema, relatório, processo)
- Responsável pela medição

**Output:** `framework-kpis.md` em `projects/PROJ-XXXX/03-planejamento/`

---

#### Step 15 — Status Report Inicial (Sara Status)
**Objetivo:** Criar o primeiro relatório de status antes do go-live, como linha de base.

**Estrutura do Status Report:**
```
## STATUS REPORT — [PROJ-XXXX] — [Data]

### Semáforo Geral: 🟢/🟡/🔴

| Dimensão | Status | Observação |
|----------|--------|-----------|
| Escopo | 🟢 | Definido e aprovado |
| Prazo | 🟡 | Risco de atraso em análise |
| Custo | 🟢 | Dentro do orçamento |
| Qualidade | 🟢 | Documentação aprovada |
| Riscos | 🟡 | 2 riscos médios ativos |
| Stakeholders | 🟢 | Sponsor engajado |

### Conquistas desta fase
- [lista de entregas concluídas]

### Pendências abertas
- [lista de itens em aberto com responsável e prazo]

### Próximos marcos
- [data]: [marco]

### Pesquisa de Satisfação (1–5)
- Qualidade da documentação: X/5
- Clareza do processo: X/5
- Alinhamento com expectativas: X/5
```

**Output:** `status-report-inicial.md` em `projects/PROJ-XXXX/04-monitoramento/`

---

### FASE 04 — REVISÃO E AUDITORIA (Steps 24–25)

#### Step 16 — Revisão de Qualidade (Vera Veredito)
**Score 0–100** avaliando completude, alinhamento VMO, qualidade técnica, rastreabilidade, sizing e consistência entre documentos.

Score < 70 → retorna para Step 8 (Diana).
Score ≥ 70 → avança para auditoria.

---

#### Step 17 — Auditoria de Governança (Gabriel Governança)
Verifica todos os BLOCKING RULES e gera relatório com NC-CRÍTICAs e NC-MENORs.

NC-CRÍTICAs abertas → não pode aprovar.
Apenas NC-MENORs → aprovado com ressalvas.

---

### FASE 05 — ENCERRAMENTO (Step 26)

#### Step 18 — Checkpoint Final: Aprovação (Usuário)
Usuário (Marcelo) revisa o pacote completo e decide:
- Aprovar → projeto encerrado formalmente, pronto para execução
- Aprovar com ressalvas → aprovado com lista de pendências aceitas
- Revisar → retorna para ajustes específicos
- Reprovar → projeto encerrado sem aprovação

---

## 3. DOCUMENTOS E ARTEFATOS VMO

### Pasta de Projeto (estrutura obrigatória)

```
projects/PROJ-AAAA-NNN/
├── 01-qualificacao/
│   ├── demanda-coletada.md
│   ├── gate-intake.md
│   ├── sizing.md
│   ├── qualificacao.md
│   └── gate-qualificacao.md
├── 02-iniciacao/
│   ├── tap-canvas-plano-geral.md
│   └── erf-requisitos.md
├── 03-planejamento/
│   ├── work-request.md
│   ├── cronograma-wbs.md
│   ├── plano-riscos.md
│   └── framework-kpis.md
├── 04-monitoramento/
│   └── status-report-[data].md
├── 05-encerramento/
│   ├── revisao-qualidade.md
│   └── auditoria-governanca.md
└── state.json
```

### Matriz de Rastreabilidade

Todo projeto deve manter rastreabilidade entre:

```
Necessidade de negócio
       ↓
Objetivo SMART (TAP)
       ↓
Requisitos funcionais (ERF)
       ↓
Entregáveis (WBS/Cronograma)
       ↓
KPIs de sucesso (Framework)
       ↓
Riscos associados (Plano de Riscos)
```

---

## 4. GLOSSÁRIO VMO

| Termo | Definição |
|-------|-----------|
| **VMO** | Value Management Office — evolução do PMO com foco em valor |
| **PMO** | Project Management Office — escritório de gestão de projetos |
| **TAP** | Termo de Abertura do Projeto — documento de autorização oficial |
| **ERF** | Especificação de Requisitos Funcionais |
| **WBS** | Work Breakdown Structure — estrutura analítica do projeto |
| **EVM** | Earned Value Management — metodologia de controle de valor |
| **BAC** | Budget At Completion — orçamento total planejado |
| **CPI** | Cost Performance Index — índice de desempenho de custo |
| **SPI** | Schedule Performance Index — índice de desempenho de prazo |
| **MoSCoW** | Método de priorização: Must / Should / Could / Won't |
| **VME** | Valor Monetário Esperado — probabilidade × impacto financeiro |
| **NC-CRÍTICA** | Não-conformidade que bloqueia aprovação do projeto |
| **NC-MENOR** | Não-conformidade registrada mas que não bloqueia |
| **Gate** | Ponto de decisão Go/No-Go no pipeline |
| **Sponsor** | Executivo patrocinador do projeto (mínimo Diretor) |
| **Work Request** | Mini-RFP estruturado para solicitar propostas a fornecedores |
| **Sizing** | Estimativa de esforço e complexidade (Rafael) |
| **KR** | Key Result — resultado-chave mensurável |
| **GMUD** | Gestão de Mudança (em sistemas ITSM) |
| **Baseline** | Linha de base (prazo, custo, escopo) — referência imutável após aprovação |

---

## 5. FLUXOGRAMA RESUMIDO

```
[DEMANDA] → Iara coleta → Gabriel intake
                                ↓
              ✅ Gate OK?  ──── ❌ → Devolver ao solicitante
                  ↓
           Rafael sizing → Felipe score 0-30
                                ↓
            Score ≥ 15?  ──── ❌ → Reprovar demanda
                  ↓
     ✓ Checkpoint 2: Usuário aprova qualificação
                  ↓
       Diana: TAP + Canvas + Plano Geral
                  ↓
       Rafael: ERF (RFs + RNFs MoSCoW)
                  ↓
       Fábio: Work Request (10 grupos)
                  ↓
       Carlos: Cronograma + WBS
                  ↓
       Pedro: Plano de Riscos
                  ↓
       Marcela: KPIs + EVM
                  ↓
       Sara: Status Report Inicial
                  ↓
       Vera: Revisão qualidade (0-100)
                  ↓
       Score ≥ 70?  ──── ❌ → Volta Diana (máx. 2x)
            ↓
       Gabriel: Auditoria Governança
                  ↓
       NC-CRÍTICA?  ──── ✅ → NC-MENOR apenas → Aprovado c/ ressalvas
            ↓ (sem NC-CRÍTICA)
     ✓ Checkpoint Final: Usuário aprova
                  ↓
          [PROJETO APROVADO ✅]
          Pronto para execução
```

---

*Documento de metodologia para configuração dos agentes VMO no Copilot Studio.*
*Baseado no projeto VMO_GAB v0.1.14 — pipeline.yaml versão 4.0.0.*
