# Demanda Coletada + Estruturada

**Projeto:** PROJ-2026-008-voice-mode
**Data de Coleta:** 17/08/2026
**Versão:** 1.0
**Agente Responsável:** Iara Inbound

---

## Canal de Entrada

**Canal:** Transcrição Fireflies — Reunião de Discovery
**Tipo:** Transcrição de áudio (voice agent)
**ID Fireflies:** 01M08HA35T9P10W3SYTH94MTRH
**Link:** https://app.fireflies.ai/view/01M08HA35T9P10W3SYTH94MTRH
**Data da Reunião:** 17/08/2026, 18:56 UTC
**Duração:** ~11 minutos

---

## Identificação do Solicitante

| Campo | Valor | Fonte |
|---|---|---|
| **Nome** | Neemias Buceli | Transcrição Fireflies [00:04] |
| **Cargo** | Não informado | ⚠️ Lacuna — cargo exato não declarado na conversa |
| **Área** | Time de Data AI | Transcrição Fireflies [06:52] |
| **Organização** | Grupo Águia Branca | Transcrição Fireflies [03:32] |
| **E-mail** | Não informado | ⚠️ Lacuna — e-mail não fornecido na transcrição |

---

## Descrição da Necessidade (Problema Real)

### Necessidade de Negócio
A organização precisa definir qual solução tecnológica adotar para habilitar a **modalidade de voz (Voice Mode)** em seu sistema multiagente. Atualmente, existe uma solução funcional via Fireflies que opera com voice mode, porém **não é homologada** pela organização. A decisão envolve avaliar três caminhos distintos para determinar o mais adequado considerando governança, custo, prazo e conformidade.

**Fonte:** Transcrição Fireflies [00:14 - 01:28]

### Pedido Técnico Específico (o que foi solicitado)
Elaboração de um **estudo de viabilidade** documentando prós e contras de três soluções multiagentes com capacidade de resposta por voz, com possibilidade de incluir uma recomendação, mas **sem detalhar implementação**.

**Fonte:** Transcrição Fireflies [01:20 - 01:28], [07:34 - 07:41]

### Requisito Fundamental
A solução escolhida **deve ter capacidade de integrar modalidade de voz** — especificamente, resposta por áudio (não apenas interação por texto).

**Fonte:** Transcrição Fireflies [02:46 - 02:53], [03:17 - 03:18]

---

## Soluções a Avaliar

### Solução 1 — Fireflies (Voice Mode)
| Aspecto | Detalhe | Fonte |
|---|---|---|
| Status | Funcional, operando atualmente | Transcrição [00:14 - 00:46] |
| Homologação | Não homologada na organização | Transcrição [00:14] |
| Risco principal | Custo desconhecido para deploy interno; falta de governança corporativa | Transcrição [04:33 - 04:50] |
| Vantagem | Já funciona com voice mode completo | Transcrição [00:14] |

### Solução 2 — Microsoft Teams + Copilot Studio
| Aspecto | Detalhe | Fonte |
|---|---|---|
| Status | Toggle de voice calling habilitado, funcionalidade em desenvolvimento | Transcrição [00:46 - 01:12] |
| Homologação | Homologada pela organização | Transcrição [00:14] |
| Risco principal | Prazo incerto (estimativa 1-3 meses) | Transcrição [04:51 - 05:04] |
| Vantagem | Governança Microsoft integrada; multiagente já operando em texto | Transcrição [00:46] |

### Solução 3 — Azure Telefonia (Central Azure)
| Aspecto | Detalhe | Fonte |
|---|---|---|
| Status | Disponível, requer habilitação de número | Transcrição [01:12 - 01:20] |
| Homologação | Homologada pela organização | Inferido — dentro do ecossistema Azure/Microsoft |
| Risco principal | Escopo restrito a call center; implementação mais complexa | Transcrição [05:04 - 05:16] |
| Vantagem | Protocolos de segurança para voz; adequada para atendimento ao cliente | Transcrição [01:12] |

---

## Benefício Esperado

Digitalização e melhoria da interação com agentes multiagentes em toda a organização, começando pela área de Sistemas ERP. A funcionalidade de voz visa aumentar a agilidade e qualidade do atendimento e posicionar o Grupo Águia Branca na adoção de soluções inteligentes.

**Fonte:** Transcrição Fireflies [02:10 - 02:23], [03:32 - 03:36]

---

## Critérios de Avaliação Definidos pelo Solicitante

| # | Critério | Fonte |
|---|---|---|
| 1 | Custo | Transcrição [07:57 - 08:02] |
| 2 | Prazo | Transcrição [07:57 - 08:02] |
| 3 | Capacidades Técnicas | Transcrição [07:57 - 08:02] |
| 4 | Governança | Transcrição [07:57 - 08:02] |
| 5 | Risco | Transcrição [07:57 - 08:02] |
| 6 | Segurança | Transcrição [08:17 - 08:19] |
| 7 | Conformidade legal (LGPD e políticas internas) | Transcrição [08:29 - 08:37] |

---

## Público-Alvo

| Campo | Valor | Fonte |
|---|---|---|
| **Abrangência** | Toda a organização | Transcrição [03:32] |
| **Foco inicial** | Área de Sistemas ERP | Transcrição [03:32 - 03:36] |
| **Áreas envolvidas** | Call Center, ITeam, Data AI | Transcrição [06:25 - 06:34] |

---

## Stakeholders Identificados

| Stakeholder | Papel | Fonte |
|---|---|---|
| Neemias Buceli | Solicitante (Data AI) | Transcrição [06:52] |
| Time de Sistemas ERP | Avaliação técnica e timeline | Transcrição [05:45 - 05:56] |
| Call Center | Área envolvida na decisão | Transcrição [06:25 - 06:34] |
| ITeam | Área envolvida na decisão | Transcrição [06:25 - 06:34] |

---

## Restrições e Premissas

### Restrições
| Restrição | Detalhe | Fonte |
|---|---|---|
| **Prazo** | Entrega do estudo de viabilidade para 18/08/2026 (dia seguinte) | Transcrição [09:42 - 09:43] |
| **Escopo** | Apenas estudo de viabilidade — sem implementação | Transcrição [07:10 - 07:22] |
| **Orçamento** | Não é foco neste momento | Transcrição [10:03 - 10:06] |

### Premissas
| Premissa | Fonte |
|---|---|
| A solução escolhida deve ter capacidade de voz (requisito inegociável) | Transcrição [02:46 - 02:53] |
| O estudo pode incluir uma recomendação | Transcrição [07:34 - 07:41] |
| O time de Sistemas ERP definirá o timeline de implementação | Transcrição [05:45 - 05:56] |

---

## Lacunas Identificadas

| # | Lacuna | Impacto | Ação Requerida |
|---|---|---|---|
| L1 | **Cargo do solicitante** não informado | Médio — necessário para definir nível de autoridade | Confirmar com Neemias Buceli |
| L2 | **E-mail do solicitante** não fornecido | Baixo — necessário para comunicação formal | Obter via canal de comunicação |
| L3 | **Sponsor formal** não identificado | Alto — TAP requer sponsor com nome, cargo e autoridade | Identificar quem patrocina a iniciativa |
| L4 | **Orçamento estimado** não discutido | Médio — necessário para estudo de viabilidade de custos | Levantar com time de Sistemas ERP |
| L5 | **Timeline de implementação** não definido | Alto — prazo incerto afeta análise de viabilidade | Consultar time de Sistemas ERP |
| L6 | **Processos atuais** não detalhados | Baixo — solicitante indicou que não faz parte do escopo | Neemias informou que não é escopo [03:51] |
| L7 | **Homologação de Azure Telefonia** inferida, não confirmada | Médio — assumido por estar no ecossistema Microsoft | Confirmar com área de TI |

---

## Contexto Organizacional

- **Urgência:** Alta — prazo de entrega para o dia seguinte
- **Motivação:** Necessidade de definir estratégia para Voice Mode em soluções multiagentes
- **Histórico:** Já existe solução funcional via Fireflies (não homologada) e solução Microsoft (homologada, sem voz)
- **Pressão:** O solicitante demonstrou objetividade e foco — redirecionou perguntas fora de escopo de volta ao objetivo do estudo de viabilidade

---

## Resumo de Confirmação

Neemias Buceli, do time de Data AI do Grupo Águia Branca, solicita um **estudo de viabilidade** comparando três soluções multiagentes com capacidade de voz: (1) Fireflies — funcional mas não homologada, (2) Microsoft Teams/Copilot Studio — homologada mas com voz em desenvolvimento, e (3) Azure Telefonia — homologada mas restrita a call center. O estudo deve avaliar custo, prazo, capacidades técnicas, governança, risco, segurança e conformidade LGPD, incluindo uma recomendação sem detalhar implementação. Prazo: 18/08/2026.

**Confirmação do solicitante:** Sim — resumo validado em [09:24 - 09:30].
