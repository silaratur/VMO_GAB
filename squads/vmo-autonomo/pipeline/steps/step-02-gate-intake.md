---
execution: inline
agent: gabriel-governanca
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md
outputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/gate-intake.md
---

# Step 02: Gate de Governança — Intake

Gabriel Governança executa o primeiro gate do pipeline: verifica se a demanda coletada
atende aos requisitos mínimos de governança de entrada antes de ser exposta ao usuário
no checkpoint. Não avalia qualidade do conteúdo (isso é do Felipe) — avalia se o
**processo de captação foi seguido corretamente**.

## Context Loading

- `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md` — output da Iara

## Instructions

Executar a task `gate-fase-01-intake.md` do agente Gabriel Governança.

## Veto Conditions

Reject and redo (retornar ao Step 1) if ANY are true:
1. O campo "Solicitante" está completamente vazio — sem nome, cargo ou área
2. Nenhuma fonte foi documentada para nenhum campo
3. A seção "Lacunas Identificadas" está ausente do documento

## Quality Criteria

- [ ] Gate executado com veredicto explícito: PASS ou HOLD
- [ ] Se HOLD: cada bloqueio tem responsável e ação clara para desbloqueio
- [ ] Documento salvo em 01-qualificacao/gate-intake.md
