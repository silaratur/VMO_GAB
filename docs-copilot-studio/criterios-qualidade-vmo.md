# Critérios de Qualidade VMO — Referência para Agentes

**VMO Consultoria | Versão 1.0 | 2026**
**Responsável:** Marcelo Silveira

---

## 1. BLOCKING RULES — Regras Inegociáveis

As regras abaixo são **BLOQUEANTES**. Se qualquer uma for violada, o projeto é **imediatamente suspenso** e não pode avançar até a correção.

### BR-01 — Aprovações Obrigatórias
Toda demanda deve ter **obrigatoriamente**:
- Aprovação documentada da Diretoria da área solicitante (cargo mínimo: Gerente Sênior ou Diretor)
- Aprovação documentada do Gerente de TI ou superior

**Evidência aceita:** email formal, ata de reunião, ticket aprovado em sistema, Teams/WhatsApp com identificação clara do aprovador e cargo.

**Violação:** Demanda apresentada sem pelo menos uma das aprovações → **BLOQUEADO no Gate de Intake.**

---

### BR-02 — Sponsor Executivo
Todo projeto aprovado para iniciação deve ter um **sponsor executivo designado** com:
- Cargo mínimo: Diretor (ou equivalente)
- Comprometimento formal (email ou ata)
- Disponibilidade para participar de checkpoints

**Violação:** Projeto sem sponsor até o final da Qualificação → **NC-CRÍTICA na Auditoria Gabriel.**

---

### BR-03 — Urgência com Evidência
Urgência declarada acima de **3/10** exige evidência documental que justifique a prioridade.

**Evidências aceitas:** email de diretor ou superior, ata de comitê executivo, risco regulatório documentado, impacto financeiro mensurável.

**Violação:** Urgência > 3 sem evidência → urgência é automaticamente reduzida para **3/10** pela Iara Inbound. O score de Felipe não pode usar urgência inflada.

---

### BR-04 — Sizing Obrigatório Antes da Qualificação
O **Rafael Requisito deve realizar o sizing** (estimativa de esforço e complexidade) **antes** de Felipe Filtro calcular o score de qualificação.

Felipe **nunca** pode estimar o critério de Esforço (critério 7) por benchmark próprio — apenas com base no sizing formal do Rafael.

**Violação:** Score de Felipe gerado sem sizing do Rafael → **qualificação inválida, repetir.**

---

### BR-05 — Não-Conformidades Críticas Bloqueiam Aprovação Final
Se a Auditoria de Governança (Gabriel) identificar **qualquer NC-CRÍTICA**, o projeto não pode ser aprovado no Checkpoint Final até resolução.

**NC-CRÍTICA inclui:** ausência de sponsor, ausência de aprovações, escopo indefinido, orçamento não aprovado.

---

## 2. CRITÉRIOS DE QUALIFICAÇÃO — Felipe Filtro (Score 0–30)

Cada critério vale de **0 a 3 pontos**.

| # | Critério | 0 pts | 1 pt | 2 pts | 3 pts |
|---|----------|-------|------|-------|-------|
| 1 | **Clareza da necessidade** | Vaga/confusa | Parcialmente clara | Clara com lacunas | Totalmente clara e objetiva |
| 2 | **Alinhamento estratégico** | Sem alinhamento | Alinhamento fraco | Alinhamento moderado | Alinhamento direto com estratégia |
| 3 | **Benefício mensurável** | Sem benefício | Benefício vago | Benefício estimado | Benefício quantificado (R$, %, horas) |
| 4 | **Viabilidade técnica** | Inviável | Viabilidade duvidosa | Viável com restrições | Totalmente viável |
| 5 | **Recursos disponíveis** | Sem recursos | Recursos insuficientes | Recursos parciais | Recursos confirmados |
| 6 | **Prazo realista** | Prazo impossível | Prazo muito apertado | Prazo ajustável | Prazo realista e aceito |
| 7 | **Esforço estimado (Rafael)** | Não estimado (EM ESPERA) | Esforço muito alto sem justificativa | Esforço alto mas justificado | Esforço adequado ao escopo |
| 8 | **Risco aceitável** | Risco crítico sem mitigação | Risco alto | Risco médio controlável | Risco baixo |
| 9 | **Sponsor identificável** | Sem possível sponsor | Sponsor incerto | Sponsor provável | Sponsor confirmado |
| 10 | **Aprovações documentadas** | Sem aprovações | 1 aprovação apenas | Aprovações verbais | Aprovações formais documentadas |

### Classificação Final
| Score | Classificação | Ação |
|-------|--------------|------|
| 0–14 | ❌ REPROVADO | Demanda devolvida. Não avança. |
| 15–20 | ⚠️ CONDICIONAL | Avança com condições a serem cumpridas (C1, C2, C3...) |
| 21–30 | ✅ APROVADO | Avança normalmente para Iniciação |

### Condições Condicionais (C1–Cn)
Quando score é CONDICIONAL, Felipe deve listar as condições específicas:
- **C1:** [descrição da condição 1 — quem deve resolver — prazo]
- **C2:** [descrição da condição 2...]

O Checkpoint 2 só pode ser confirmado com as condições aceitas pelo usuário.

---

## 3. CRITÉRIOS DE QUALIDADE DOS DOCUMENTOS — Vera Veredito (Score 0–100)

### Completude (25 pontos)
| Item | Pontos | Verificação |
|------|--------|-------------|
| TAP preenchido com todos os campos | 5 | Objetivo SMART, sponsor, escopo, critérios, orçamento, prazo |
| PM Canvas com 9 blocos | 5 | Todos os blocos têm conteúdo substantivo |
| Plano Geral com fases e responsáveis | 5 | Mínimo 3 fases com responsáveis identificados |
| ERF com RFs e RNFs | 5 | Mínimo 5 RFs + 3 RNFs com MoSCoW |
| Cronograma com WBS | 5 | Mínimo 3 níveis de WBS + marcos identificados |

### Alinhamento VMO (20 pontos)
| Item | Pontos | Verificação |
|------|--------|-------------|
| Foco em geração de valor (não apenas escopo) | 5 | Benefícios quantificados nos documentos |
| Orientação a resultados e métricas | 5 | KPIs mensuráveis definidos |
| Governança e controle presente | 5 | Sponsor, aprovações e gates documentados |
| Linguagem executiva e profissional | 5 | Tom adequado para relatório a diretoria |

### Qualidade Técnica (20 pontos)
| Item | Pontos | Verificação |
|------|--------|-------------|
| Requisitos com critério de aceitação | 5 | Cada RF tem CA testável |
| Riscos com VME ou scoring | 5 | Probabilidade × Impacto calculados |
| Work Request completo (10 grupos) | 5 | Mínimo 30 itens no WR |
| EVM configurado corretamente | 5 | BAC, curva S e KPIs definidos |

### Rastreabilidade (15 pontos)
| Item | Pontos | Verificação |
|------|--------|-------------|
| Requisitos rastreáveis ao escopo do TAP | 5 | Consistência TAP ↔ ERF |
| KPIs rastreáveis aos benefícios declarados | 5 | Consistência Qualificação ↔ KPIs |
| Riscos rastreáveis ao plano de resposta | 5 | Cada risco tem dono e trigger |

### Sizing e Consistência (10 pontos)
| Item | Pontos | Verificação |
|------|--------|-------------|
| Esforço do sizing consistente com cronograma | 5 | Dias estimados ≈ duração no cronograma |
| Complexidade refletida nos riscos | 5 | Alta complexidade → mais riscos mapeados |

### Consistência Entre Documentos (10 pontos)
| Item | Pontos | Verificação |
|------|--------|-------------|
| Prazo do TAP = prazo do cronograma | 3 | Datas não conflitam |
| Escopo do TAP = escopo dos requisitos | 4 | Sem requisitos fora do escopo declarado |
| Orçamento do TAP = estimativa do WR | 3 | Valores compatíveis |

### Classificação Vera
| Score | Classificação | Ação |
|-------|--------------|------|
| 0–69 | ❌ REPROVAR | Volta para Diana (documentação base). Loop máximo: 2 vezes. |
| 70–84 | ⚠️ APROVADO COM RESSALVAS | Lista as ressalvas. Avança mas Gabriel registra NC-MENORs. |
| 85–100 | ✅ APROVADO | Avança para Auditoria Gabriel sem pendências. |

---

## 4. CHECKLIST DE GOVERNANÇA — Gabriel Governança

### NC-CRÍTICA (Não-Conformidade Crítica) — Bloqueia aprovação final
- [ ] **GOV-01:** Sponsor executivo designado e documentado (Diretor+)
- [ ] **GOV-02:** Aprovação da Diretoria da área solicitante documentada
- [ ] **GOV-03:** Aprovação do Gerente de TI documentada
- [ ] **GOV-04:** TAP revisado e aceito pelo sponsor
- [ ] **GOV-05:** Orçamento aprovado ou em processo formal de aprovação
- [ ] **GOV-06:** Escopo claramente definido (sem "a definir" em itens críticos)

### NC-MENOR (Não-Conformidade Menor) — Registrada mas não bloqueia
- [ ] **GOV-07:** Todos os documentos têm data e versão
- [ ] **GOV-08:** Riscos têm responsável designado
- [ ] **GOV-09:** KPIs têm baseline e meta definidos
- [ ] **GOV-10:** Datas do cronograma estão no futuro (não no passado)
- [ ] **GOV-11:** Work Request tem fornecedores potenciais identificados
- [ ] **GOV-12:** Status Report tem data de próxima atualização

### Formato do Relatório de Auditoria
```
## AUDITORIA DE GOVERNANÇA VMO
**Projeto:** [codigo]
**Data:** [data]
**Auditor:** Gabriel Governança

### NC-CRÍTICAs Encontradas
[NC-CRIT-01]: [descrição] — [status: ABERTA / RESOLVIDA]

### NC-MENOREs Encontradas
[NC-MEN-01]: [descrição] — [status: ABERTA / ACEITA]

### PARECER FINAL
[APROVADO / APROVADO COM RESSALVAS / BLOQUEADO]
[Justificativa]
```

---

## 5. ANTI-PATTERNS — O que NUNCA fazer

### Iara Inbound (coleta)
- ❌ Nunca assumir que aprovações verbais são suficientes
- ❌ Nunca inflar urgência para priorizar o projeto
- ❌ Nunca registrar demanda incompleta como "completa" para avançar

### Felipe Filtro (qualificação)
- ❌ Nunca estimar Esforço sem o sizing do Rafael
- ❌ Nunca arredondar score para aprovar projeto borderline
- ❌ Nunca omitir critérios que penalizariam o score

### Oscar Orquestrador
- ❌ Nunca reescrever o trabalho dos agentes — avaliar, não substituir
- ❌ Nunca aprovar documento com NC-CRÍTICA aberta
- ❌ Nunca pular um step mesmo que pareça redundante

### Diana Documento
- ❌ Nunca criar TAP com objetivo vago ("melhorar o processo")
- ❌ Nunca deixar campos do Canvas sem preenchimento substantivo
- ❌ Nunca copiar a descrição da demanda como objetivo SMART

### Gabriel Governança
- ❌ Nunca fechar NC-CRÍTICA sem evidência de resolução
- ❌ Nunca aprovar projeto sem sponsor, independentemente da pressão
- ❌ Nunca reduzir NC-CRÍTICA para NC-MENOR por conveniência

---

*Documento de referência para configuração de agentes VMO no Copilot Studio.*
*Baseado nas regras operacionais do VMO Squad (projeto VMO_GAB v0.1.14).*
