---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md
on_reject: 16
---

# [ORQ] Step 06-ORQ: Avaliar Cronograma (WBS + Cronograma Detalhado)

## Context

- **Deliverable avaliado**: WBS + Cronograma Detalhado (`cronograma.md`)
- **Agente responsável**: Carlos Cronograma
- **Critérios aplicáveis**: quality-criteria.md — seção: WBS + Cronograma
- **Cross-check**: `documentacao-base.md` — prazo de conclusão do TAP deve coincidir com o cronograma

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — para cross-check de prazo
- `pipeline/data/quality-criteria.md` — seção: WBS + Cronograma
- `pipeline/data/anti-patterns.md` — seção: Anti-Patterns de Cronograma

### Critérios BLOCKING — WBS + Cronograma

1. WBS com mínimo 3 níveis de decomposição (nível 1: projeto, nível 2: fases, nível 3: pacotes de trabalho)
2. Pacotes de trabalho no último nível com duração ≤ 2 semanas cada
3. Marcos principais identificados (mínimo: início, meio e fim do projeto)
4. Dependências documentadas entre atividades críticas
5. Caminho crítico identificado

### Critério BLOCKING adicional — Cross-check com TAP
- A data de conclusão do cronograma deve coincidir com o prazo de conclusão definido no TAP — divergência = BLOCKING (inconsistência cross-documento)

### Processo de Avaliação

1. Ler `cronograma.md` na íntegra.
2. Verificar os 5 critérios BLOCKING do cronograma — um a um.
3. Comparar data de conclusão do cronograma com o prazo do TAP.
4. Verificar critérios de qualidade: 100% dos entregáveis do escopo cobertos, responsável por pacote, baseline, buffer de contingência (10-20% do prazo).
5. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema no Cronograma/WBS. O que prefere fazer?"
- Opção 1: "Redirecionar para Carlos Cronograma — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 16` (retorna ao Step 15 — Carlos).

## Veto Conditions

Reject and redo if ANY are true:
1. WBS não verificado para os 3 níveis de decomposição
2. Cross-check de prazo com TAP não realizado
3. Qualquer BLOCKING violado mas decisão marcada como APROVADO
4. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
