---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/03-planejamento/kpis.md
on_reject: 20
---

# [ORQ] Step 08-ORQ: Avaliar Framework de KPIs

## Context

- **Deliverable avaliado**: Framework de KPIs (`kpis.md`)
- **Agente responsável**: Marcela Métrica
- **Critérios aplicáveis**: quality-criteria.md — seção: KPIs e Performance
- **Cross-check**: `documentacao-base.md` — KPIs devem estar vinculados aos critérios de sucesso do TAP

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/03-planejamento/kpis.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — para cross-check com critérios de sucesso do TAP
- `pipeline/data/quality-criteria.md` — seção: KPIs e Performance

### Critérios BLOCKING — Framework de KPIs

1. CPI (Cost Performance Index) e SPI (Schedule Performance Index) definidos com baseline estabelecida
2. Frequência de medição definida para cada KPI (semanal, quinzenal, mensal)
3. Limites de alerta definidos para cada KPI (thresholds: amarelo = atenção, vermelho = ação imediata)
4. Responsável pela coleta e reporte de cada KPI nominalmente identificado

### Critério BLOCKING adicional — Cross-check com TAP
- Ao menos um KPI deve ser rastreável a cada critério de sucesso do TAP — KPIs sem ligação aos critérios de sucesso são framework sem propósito

### Processo de Avaliação

1. Ler `kpis.md` na íntegra.
2. Verificar os 4 critérios BLOCKING — um a um.
3. Listar critérios de sucesso do TAP e verificar se cada um tem ao menos um KPI correspondente.
4. Verificar critérios de qualidade: cobertura das dimensões (prazo, custo, escopo, qualidade, satisfação), semáforo visual presente, dashboard de saúde incluso.
5. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema no Framework de KPIs. O que prefere fazer?"
- Opção 1: "Redirecionar para Marcela Métrica — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 20` (retorna ao Step 19 — Marcela).

## Veto Conditions

Reject and redo if ANY are true:
1. CPI e SPI não verificados como presentes com baseline
2. Cross-check com critérios de sucesso do TAP não realizado
3. Qualquer BLOCKING violado mas decisão marcada como APROVADO
4. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
