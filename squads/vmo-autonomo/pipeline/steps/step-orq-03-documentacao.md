---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md
on_reject: 10
---

# [ORQ] Step 03-ORQ: Avaliar Documentação Base (TAP + PM Canvas + Plano Geral)

## Context

- **Deliverable avaliado**: Documentação Base — TAP, PM Canvas, Plano Geral (`documentacao-base.md`)
- **Agente responsável**: Diana Documento
- **Critérios aplicáveis**: quality-criteria.md — seções TAP e PM Canvas
- **Cross-check**: `qualificacao.md` — prazo, custo, escopo e sponsor devem ser consistentes

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao.md` — para cross-check
- `pipeline/data/quality-criteria.md` — seções: TAP e PM Canvas
- `pipeline/data/anti-patterns.md` — seção: Anti-Patterns de Documentação

### Critérios BLOCKING — TAP

1. Objetivo SMART: específico, mensurável (tem métrica), atingível, relevante, temporal (tem prazo de conclusão)
2. Sponsor identificado com nome, cargo e nível de autoridade
3. Gerente de Projeto designado com nível de autoridade documentado
4. Escopo delimitado: lista de "dentro do escopo" E "fora do escopo" presentes
5. Critérios de sucesso mensuráveis (mínimo 3)
6. Orçamento aprovado (mesmo que estimado, com faixa de variação)
7. Prazo de conclusão definido com marco final

### Critérios BLOCKING — PM Canvas

1. Todos os 9 blocos preenchidos sem exceção
2. Consistência interna: valores de prazo/custo/escopo batem entre blocos
3. Bloco "Por quê?" conecta diretamente à estratégia organizacional

### Critério BLOCKING adicional — Cross-check com qualificação
- Sponsor, prazo macro e benefício esperado no TAP devem ser coerentes com os valores na qualificação

### Processo de Avaliação

1. Ler `documentacao-base.md` na íntegra.
2. Verificar critérios BLOCKING do TAP — um a um.
3. Verificar critérios BLOCKING do PM Canvas — um a um.
4. Comparar TAP com `qualificacao.md`: valores de sponsor, prazo e benefício são consistentes?
5. Se todos passarem: verificar critérios de qualidade (partes interessadas, premissas, restrições, riscos de alto nível).
6. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema na Documentação Base (TAP/PM Canvas). O que prefere fazer?"
- Opção 1: "Redirecionar para Diana Documento — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 10` (retorna ao Step 9 — Diana).

## Veto Conditions

Reject and redo if ANY are true:
1. Avaliação feita sem verificar todos os 7 BLOCKINGs do TAP e os 3 do PM Canvas
2. Qualquer BLOCKING violado mas decisão marcada como APROVADO
3. Cross-check com qualificacao.md não realizado
4. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
