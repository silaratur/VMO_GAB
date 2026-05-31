---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/04-monitoramento/status-report-{date}.md
on_reject: 21
---

# [ORQ] Step 09-ORQ: Avaliar Status Report Inicial

## Context

- **Deliverable avaliado**: Status Report Inicial (`status-report-{date}.md`)
- **Agente responsável**: Sara Status
- **Critérios aplicáveis**: quality-criteria.md — seção: Status Report
- **Cross-check**: `kpis.md` + `cronograma.md` — valores de progresso e semáforo devem ser coerentes com os baselines

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/04-monitoramento/status-report-{date}.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/03-planejamento/kpis.md` — para cross-check do semáforo
- `squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md` — para cross-check de progresso vs. baseline
- `pipeline/data/quality-criteria.md` — seção: Status Report
- `pipeline/data/anti-patterns.md` — seção: Anti-Patterns de Monitoramento e Reports

### Critérios BLOCKING — Status Report

1. Status geral (semáforo: verde/amarelo/vermelho) presente e visível no topo do relatório
2. Data do report e período coberto explícitos
3. Progresso em percentual comparado ao baseline (não apenas progresso absoluto)
4. Issues abertas com responsável e prazo de resolução (issues sem dono = BLOCKING)

### Critério BLOCKING adicional — Cross-check com KPIs e Cronograma
- O semáforo do status report deve ser coerente com os thresholds do framework de KPIs (se CPI < 0,85 → relatório não pode ser verde)
- O percentual de progresso deve ser coerente com a posição no cronograma (não pode estar à frente sem justificativa)

### Processo de Avaliação

1. Ler `status-report-{date}.md` na íntegra.
2. Verificar os 4 critérios BLOCKING — um a um.
3. Comparar semáforo do report com os thresholds dos KPIs.
4. Verificar se o progresso reportado é coerente com a posição no cronograma.
5. Verificar critérios de qualidade: sumário executivo de 1 página, ações SMART com responsável e prazo, desvios explicados (não apenas reportados), próximos passos claros.
6. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema no Status Report Inicial. O que prefere fazer?"
- Opção 1: "Redirecionar para Sara Status — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 21` (retorna ao Step 21 — Sara).

## Veto Conditions

Reject and redo if ANY are true:
1. Semáforo não verificado contra thresholds do framework de KPIs
2. Progresso não verificado contra posição no cronograma
3. Qualquer BLOCKING violado mas decisão marcada como APROVADO
4. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
