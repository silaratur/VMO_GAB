---
execution: inline
agent: gabriel-governanca
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao.md
outputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/gate-qualificacao.md
---

# Step 05: Gate de Governança — Qualificação

Gabriel Governança executa o segundo gate do pipeline: verifica se o parecer de qualificação
emitido pelo Felipe Filtro atende aos requisitos de governança antes de ser apresentado ao
usuário para aprovação. Não re-avalia os critérios de negócio (isso é do Felipe) — verifica
se o **processo de qualificação foi aplicado com rigor e se as condições de governança estão
documentadas corretamente**.

## Context Loading

- `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md`
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao.md`
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/gate-intake.md`

## Instructions

Executar a task `gate-fase-02-qualificacao.md` do agente Gabriel Governança.

## Veto Conditions

Reject and redo (retornar ao Step 4 — Felipe) if ANY are true:
1. A decisão (APROVADO / COM CONDIÇÕES / REPROVADO / EM ESPERA) está ausente do parecer
2. A classificação (PROJETO / MELHORIA EVOLUTIVA / MELHORIA CORRETIVA) está ausente
3. Algum critério (1–10) não tem pontuação explícita

## Quality Criteria

- [ ] Gate executado com veredicto explícito: PASS ou HOLD
- [ ] Se HOLD: cada bloqueio de governança tem ação específica para Felipe corrigir
- [ ] Documento salvo em 01-qualificacao/gate-qualificacao.md
