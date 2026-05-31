---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md
on_reject: 1
---

# [ORQ] Step 01-ORQ: Avaliar Demanda Coletada

## Context

- **Deliverable avaliado**: Demanda Coletada (`demanda-coletada.md`)
- **Agente responsável**: Iara Inbound
- **Critérios aplicáveis**: Anti-Patterns de Captação de Demanda (`pipeline/data/anti-patterns.md`) + Critérios Gerais
- **Cross-check**: não aplicável (primeiro deliverable)

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md` — deliverable a avaliar
- `pipeline/data/quality-criteria.md` — seção: Critérios Gerais
- `pipeline/data/anti-patterns.md` — seção: Anti-Patterns de Captação de Demanda

### Critérios BLOCKING para este deliverable

1. Canal de entrada identificado e documentado (e-mail, ticket, PDF, transcrição, etc.)
2. Solicitante com nome, cargo e área registrados
3. Descrição da necessidade presente (não apenas solução pedida)
4. Lacunas de informação documentadas (campos "não informado" ou perguntas de esclarecimento)

### Processo de Avaliação

1. Ler a `demanda-coletada.md` na íntegra.
2. Verificar os 4 critérios BLOCKING acima — um a um.
3. Se todos passarem: verificar critérios de qualidade (rastreabilidade de fonte, contexto organizacional presente, prazo questionado ou registrado como "não informado").
4. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema na Demanda Coletada. O que prefere fazer?"
- Opção 1: "Redirecionar para Iara Inbound — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 1` (retorna ao Step 1 — Iara).

## Veto Conditions

Reject and redo if ANY are true:
1. Avaliação feita sem ler quality-criteria.md e anti-patterns.md primeiro
2. Critério BLOCKING violado mas decisão marcada como APROVADO
3. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
