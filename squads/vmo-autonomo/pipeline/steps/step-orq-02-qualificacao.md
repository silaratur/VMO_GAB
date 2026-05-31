---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao.md
on_reject: 5
---

# [ORQ] Step 02-ORQ: Avaliar Qualificação da Demanda

## Context

- **Deliverable avaliado**: Parecer de Qualificação (`qualificacao.md`)
- **Agente responsável**: Felipe Filtro
- **Critérios aplicáveis**: Fase 2 — Qualificação (`pipeline/data/domain-framework.md`) + Anti-Patterns de Qualificação
- **Cross-check**: `demanda-coletada.md` — verificar consistência entre demanda e qualificação

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md` — para cross-check
- `pipeline/data/quality-criteria.md` — seção: Critérios Gerais
- `pipeline/data/domain-framework.md` — seção: Fase 2 (Critérios de Qualificação)
- `pipeline/data/anti-patterns.md` — seção: Anti-Patterns de Qualificação

### Critérios BLOCKING para este deliverable

1. Todos os 6 critérios de qualificação avaliados com pontuação e justificativa (não pode haver critério sem nota)
2. Decisão de qualificação explícita: APROVADO COMO PROJETO / APROVADO COMO TAREFA / REPROVADO / EM ESPERA
3. Benefício esperado quantificado (mesmo que estimado — não pode ser apenas "alto")
4. Se reprovado: justificativa documentada com raciocínio explícito

### Critério BLOCKING adicional — Cross-check com demanda
- A necessidade identificada na qualificação deve ser coerente com a demanda coletada — divergências de escopo ou solicitante são BLOCKING

### Processo de Avaliação

1. Ler a `qualificacao.md` na íntegra.
2. Verificar os critérios BLOCKING — um a um.
3. Comparar com `demanda-coletada.md`: o problema qualificado corresponde ao problema coletado?
4. Verificar pontuação dos 6 critérios: cada um tem nota E justificativa?
5. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema no Parecer de Qualificação. O que prefere fazer?"
- Opção 1: "Redirecionar para Felipe Filtro — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 5` (retorna ao Step 5 — Felipe).

## Veto Conditions

Reject and redo if ANY are true:
1. Avaliação feita sem ler domain-framework.md e anti-patterns.md primeiro
2. Critério BLOCKING violado mas decisão marcada como APROVADO
3. Cross-check com demanda-coletada.md não realizado
4. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
