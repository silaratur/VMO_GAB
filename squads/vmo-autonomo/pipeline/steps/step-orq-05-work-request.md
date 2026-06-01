---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/work-request.md
on_reject: 14
---

# [ORQ] Step 05-ORQ: Avaliar Work Request (Mini-RFP)

## Context

- **Deliverable avaliado**: Work Request — Mini-RFP (`work-request.md`)
- **Agente responsável**: Fábio Fornecedor
- **Critérios aplicáveis**: quality-criteria.md — Critérios Gerais + critérios do step-07
- **Cross-check**: `requisitos.md` — todos os RF Must Have devem estar referenciados no WR

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/work-request.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md` — para cross-check de RFs
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — para verificar exclusões de escopo
- `pipeline/data/quality-criteria.md` — seção: Critérios Gerais

### Critérios BLOCKING — Work Request

1. Identificação do projeto completa (código do projeto, demanda, sponsor, GP, tipo de solução)
2. Todos os RF Must Have da ERF referenciados no escopo incluso do WR
3. Ao menos 3 exclusões explícitas de escopo documentadas
4. Artefato Obrigatório presente com todos os 10 grupos (sem grupos ausentes)
5. Processo de submissão com prazo final de recebimento de propostas
6. Condições comerciais com modelo de faturamento por marcos

### Critério BLOCKING adicional — Cross-check com ERF
- Cada RF classificado como Must Have na ERF deve aparecer no escopo incluso do WR (rastreabilidade obrigatória)

### Processo de Avaliação

1. Ler `work-request.md` na íntegra.
2. Verificar os 6 critérios BLOCKING do WR — um a um.
3. Listar todos os RF Must Have da ERF e verificar se cada um está no escopo incluso do WR.
4. Verificar se as exclusões do TAP aparecem no escopo excluso do WR.
5. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema no Work Request (Mini-RFP). O que prefere fazer?"
- Opção 1: "Redirecionar para Fábio Fornecedor — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 14` (retorna ao Step 13 — Fábio).

## Veto Conditions

Reject and redo if ANY are true:
1. Cross-check de RF Must Have com ERF não realizado
2. Qualquer BLOCKING violado mas decisão marcada como APROVADO
3. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
