---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md
on_reject: 11
---

# [ORQ] Step 04-ORQ: Avaliar Especificação de Requisitos (ERF)

## Context

- **Deliverable avaliado**: Especificação de Requisitos Funcionais — ERF (`requisitos.md`)
- **Agente responsável**: Rafael Requisito
- **Critérios aplicáveis**: quality-criteria.md — seção: Especificação de Requisitos Funcionais (ERF)
- **Cross-check**: `documentacao-base.md` — escopo do TAP deve ser coberto pelos requisitos Must Have

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — para cross-check de escopo
- `pipeline/data/quality-criteria.md` — seção: Especificação de Requisitos Funcionais (ERF)
- `pipeline/data/anti-patterns.md` — seção: Anti-Patterns de Documentação (requisitos ambíguos)

### Critérios BLOCKING — ERF

1. Requisitos priorizados usando MoSCoW (Must/Should/Could/Won't) — toda ERF sem priorização é BLOCKING
2. Critério de aceitação definido para CADA requisito Must Have — sem exceção
3. ID único para cada requisito (formato RF001, RNF001 ou similar)
4. Rastreabilidade: cada requisito tem origem documentada (qual parte do escopo ou solicitante o originou)

### Critério BLOCKING adicional — Cross-check com TAP
- O escopo delimitado no TAP ("dentro do escopo") deve estar representado por ao menos um requisito Must Have na ERF

### Processo de Avaliação

1. Ler `requisitos.md` na íntegra.
2. Verificar os 4 critérios BLOCKING da ERF — um a um.
3. Verificar cross-check: o escopo do TAP está coberto pelos Must Have?
4. Verificar critérios de qualidade: requisitos na voz do usuário, sem ambiguidade ("rápido" sem métrica = ambíguo), RNFs endereçados.
5. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema na Especificação de Requisitos (ERF). O que prefere fazer?"
- Opção 1: "Redirecionar para Rafael Requisito — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 11` (retorna ao Step 11 — Rafael).

## Veto Conditions

Reject and redo if ANY are true:
1. Avaliação feita sem verificar os 4 BLOCKINGs da ERF
2. Qualquer BLOCKING violado mas decisão marcada como APROVADO
3. Cross-check de escopo com TAP não realizado
4. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
