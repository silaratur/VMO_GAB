# Status Report #001 — PROJ-2026-006
## Plataforma Própria de Gestão de Ideias e Inovação

| Campo | Valor |
|-------|-------|
| **Projeto** | PROJ-2026-006 |
| **Report nº** | SR-001 |
| **Data** | 2026-05-16 |
| **Fase** | Iniciação — Concluída (aguardando resolução de condições bloqueantes) |
| **Elaborado por** | Sara Status — VMO Consultoria |
| **Versão** | 1.0 |

---

## 1. STATUS GERAL

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   STATUS GERAL:  🟡  ATENÇÃO                            │
│                                                         │
│   Fase de Iniciação concluída. Execução bloqueada por   │
│   2 condições críticas (CB-01 e CB-02) que impedem o    │
│   kick-off. Ação imediata requerida até 13/06/2026.     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> **Critério de determinação:** status geral é determinado pela dimensão mais crítica. A presença de 4 riscos CRÍTICOS abertos (RSK-001 a RSK-004) posiciona o projeto em ATENÇÃO.

---

## 2. SEMÁFORO POR DIMENSÃO

| # | Dimensão | Status | Síntese |
|---|----------|--------|---------|
| 1 | **Cronograma** | 🟡 ATENÇÃO | Kick-off em risco se CB-01 não resolvida até 13/06/2026. Go-live previsto para 07/12/2026 ainda dentro do horizonte, mas janela de manobra está se estreitando. |
| 2 | **Custo** | 🟡 ATENÇÃO | BAC estimado em R$ 100.000. Orçamento não aprovado formalmente (CB-02). Nenhum comprometimento financeiro pode ser feito até aprovação. |
| 3 | **Escopo** | 🟢 VERDE | Escopo bem definido: 31 RF + 13 RNF, 6 marcos (M1–M6), exclusões explícitas documentadas. Baseline de escopo pronto para aceite formal. |
| 4 | **Riscos** | 🔴 CRÍTICO | 4 riscos CRÍTICOS abertos (RSK-001 a RSK-004). VME consolidado: R$ 260.000. RSK-001 (sponsor ausente) é o risco de maior urgência e precede todos os demais. |
| 5 | **Satisfação** | ⚪ N/A | Não aferível — fase pré-execução. Baseline será estabelecido com a pesquisa de satisfação desta fase (ver Seção 7). |

---

## 3. PROGRESSO DA FASE DE INICIAÇÃO

**Completude: 8/8 documentos — 100%**

```
Demanda Coletada (DEM-2026-006)          ████████████████████  100%  ✅
Qualificação (21/30 — 70%)               ████████████████████  100%  ✅
Documentação Base (TAP + Canvas + PG)    ████████████████████  100%  ✅
ERF (31 RF + 13 RNF)                     ████████████████████  100%  ✅
Cronograma (55 pacotes / 9 marcos)       ████████████████████  100%  ✅
Plano de Riscos (12 riscos / 4 críticos) ████████████████████  100%  ✅
Framework de KPIs (EVM + 5 KRs)         ████████████████████  100%  ✅
Work Request (WR-2026-006)               ████████████████████  100%  ✅
```

> A fase de Iniciação está **documentalmente concluída**. O bloqueio para avanço é de natureza **decisória e orçamentária**, não documental.

---

## 4. HIGHLIGHTS DA FASE

### Conquistas
- Fase de Iniciação 100% concluída dentro do processo VMO padrão
- ERF com 31 Requisitos Funcionais e 13 Requisitos Não-Funcionais documentados e priorizados (20 Must Have com critério de aceite validado)
- Plano de Riscos robusto: 12 riscos identificados, VME calculado, planos de mitigação definidos
- Framework de KPIs com EVM configurado (BAC R$ 100k) e 5 Key Results de resultado mensuráveis
- Cronograma detalhado com 55 pacotes de trabalho e go-live fixado para 07/12/2026
- Work Request WR-2026-006 completo com Artefato Obrigatório aprovado

### Pontos de Atenção
- 9 lacunas identificadas na coleta de demanda (DEM-2026-006), sendo **2 críticas** — precisam ser sanadas na fase de planejamento detalhado
- Qualificação aprovada com condições (70% — abaixo do ideal de 80%); sponsor ausente foi o principal fator de penalização
- CB-01 (sponsor não identificado) é um pré-requisito para CB-02, para o kick-off e para mitigação de RSK-001 a RSK-003 — resolve múltiplos bloqueios em cadeia

---

## 5. ISSUES ABERTAS (CONDIÇÕES BLOQUEANTES)

> **Regra:** nenhuma issue sem dono. Nenhuma issue sem prazo.

### CB-01 — Sponsor (Diretor+) não identificado

| Campo | Detalhe |
|-------|---------|
| **ID** | CB-01 |
| **Tipo** | Condição Bloqueante |
| **Impacto** | CRÍTICO — sem sponsor não há autoridade para aprovar orçamento, homologar escopo ou representar o negócio perante a equipe |
| **Responsável** | Jadson |
| **Prazo** | **2026-06-13** |
| **Risco associado** | RSK-001 |
| **Ação requerida** | Identificar e formalizar Diretor ou superior como sponsor do projeto até a data limite |

### CB-02 — Orçamento não aprovado formalmente

| Campo | Detalhe |
|-------|---------|
| **ID** | CB-02 |
| **Tipo** | Condição Bloqueante |
| **Impacto** | ALTO — sem aprovação orçamentária não é possível contratar fornecedores, alocar recursos nem iniciar execução |
| **Responsável** | Sponsor a designar (depende de CB-01) |
| **Prazo** | **2026-06-20** |
| **Risco associado** | RSK-002 |
| **Ação requerida** | Após designação do sponsor (CB-01), submeter BAC de R$ 100.000 para aprovação formal com documento de autorização |

> **Nota de dependência:** CB-02 depende da resolução de CB-01. A sequência correta é: CB-01 (até 13/06) → CB-02 (até 20/06) → Kick-off.

---

## 6. PROXIMOS PASSOS

| # | Ação | Responsável | Data-limite | Dependência |
|---|------|-------------|-------------|-------------|
| 1 | Identificar e formalizar sponsor do projeto (Diretor+) — resolução de CB-01 | Jadson | **2026-06-13** | — |
| 2 | Submeter BAC de R$ 100.000 para aprovação orçamentária formal — resolução de CB-02 | Sponsor designado | **2026-06-20** | CB-01 resolvida |
| 3 | Convocar e realizar reunião de kick-off com sponsor, equipe VMO e stakeholders | Jadson + Sponsor | **2026-06-27** | CB-01 + CB-02 resolvidas |
| 4 | Coletar respostas da Pesquisa de Satisfação — Fase de Iniciação (ver Seção 7) | Jadson | **2026-05-30** | — |
| 5 | Emitir SR-002 após resolução das condições bloqueantes ou na data de 2026-06-14 | Sara Status / VMO | **2026-06-14** | — |

---

## 7. INFORMACOES ADICIONAIS

| Item | Detalhe |
|------|---------|
| **Próximo report** | SR-002 — previsto para 2026-06-14 ou após resolução das CBs |
| **Próxima fase** | Planejamento Detalhado (bloqueada até kick-off) |
| **Go-live previsto** | 07/12/2026 |
| **Documentação** | `/squads/vmo-autonomo/projects/PROJ-2026-006/` |

---
---

# Pesquisa de Satisfacao — Fase de Iniciacao
## PROJ-2026-006 | Plataforma Propria de Gestao de Ideias e Inovacao

| Campo | Valor |
|-------|-------|
| **Pesquisa nº** | PSAT-001 |
| **Projeto** | PROJ-2026-006 |
| **Fase avaliada** | Iniciacao (discovery → documentacao) |
| **Data de emissao** | 2026-05-16 |
| **Prazo de resposta** | 2026-05-30 |
| **Publico-alvo** | Jadson (solicitante) e equipe VMO |
| **Objetivo** | Validar qualidade do processo de captacao e documentacao da demanda |

---

## Instrucoes

Esta pesquisa avalia a **qualidade do processo de Iniciacao** conduzido pelo VMO Consultoria para o projeto PROJ-2026-006. Suas respostas ajudam a melhorar continuamente nossa metodologia. A pesquisa leva aproximadamente **5 minutos** para ser respondida.

**Como responder:** Para cada pergunta, registre sua resposta substituindo o campo `[ RESPOSTA ]` pelo seu texto ou nota.

---

## Secao 1 — NPS (Net Promoter Score)

### Q1 — Recomendacao do Processo VMO

**Pergunta:**
> "Considerando sua experiencia com o processo de Iniciacao conduzido pelo VMO Consultoria neste projeto, qual a probabilidade de voce recomendar essa metodologia de iniciacao de projetos para colegas ou outras areas da organizacao?"

**Escala:** 0 = Definitivamente nao recomendaria | 10 = Recomendaria com certeza

```
  0    1    2    3    4    5    6    7    8    9    10
  |    |    |    |    |    |    |    |    |    |    |
 [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]
```

**Sua nota (0-10):** `[ RESPOSTA ]`

**Breve justificativa (opcional):**
`[ RESPOSTA ]`

---

## Secao 2 — Perguntas Qualitativas

### Q2 — Qualidade da Coleta de Demanda

**Pergunta:**
> "O processo de coleta e entendimento da demanda (entrevistas, levantamento de requisitos, documentacao das lacunas) capturou adequadamente as necessidades reais do projeto? O que funcionou bem e o que poderia ter sido mais aprofundado?"

**Resposta:**
`[ RESPOSTA ]`

---

### Q3 — Clareza e Utilidade dos Documentos Produzidos

**Pergunta:**
> "Os documentos gerados na fase de Iniciacao (TAP, ERF, Cronograma, Plano de Riscos, Framework de KPIs) sao claros, completos e uteis para orientar as proximas fases do projeto? Algum documento precisaria de ajustes ou informacoes adicionais?"

**Resposta:**
`[ RESPOSTA ]`

---

### Q4 — Gestao das Condicoes Bloqueantes

**Pergunta:**
> "As duas condicoes bloqueantes identificadas (CB-01: sponsor nao designado; CB-02: orcamento nao aprovado) foram comunicadas de forma clara e com orientacoes de resolucao suficientes? O VMO poderia ter atuado de forma diferente para antecipar ou mitigar esses bloqueios?"

**Resposta:**
`[ RESPOSTA ]`

---

### Q5 — Expectativas para as Proximas Fases

**Pergunta:**
> "Com base no que foi entregue na fase de Iniciacao, voce se sente confiante de que o projeto esta bem estruturado para atingir seus objetivos? Quais sao suas principais expectativas ou preocupacoes para a fase de Planejamento e Execucao?"

**Resposta:**
`[ RESPOSTA ]`

---

## Secao 3 — Campo Aberto

### Q6 — Comentarios Livres

**Pergunta:**
> "Use este espaco para qualquer comentario, sugestao ou feedback adicional sobre o processo de Iniciacao, a atuacao da equipe VMO ou qualquer outro aspecto que voce considere relevante."

**Resposta:**
`[ RESPOSTA ]`

---

## Resumo das Respostas (preenchido pelo VMO apos coleta)

| Questao | Respondente | Nota / Classificacao | Data |
|---------|------------|---------------------|------|
| Q1 — NPS | | | |
| Q2 — Coleta de Demanda | | | |
| Q3 — Documentos | | | |
| Q4 — Condicoes Bloqueantes | | | |
| Q5 — Expectativas | | | |
| Q6 — Campo Aberto | | | |

**NPS Calculado:** `[ a calcular apos coleta ]`
**Classificacao NPS:** `[ Detrator (0-6) / Neutro (7-8) / Promotor (9-10) ]`

---

*Pesquisa emitida por Sara Status — VMO Consultoria | PROJ-2026-006 | 2026-05-16*
