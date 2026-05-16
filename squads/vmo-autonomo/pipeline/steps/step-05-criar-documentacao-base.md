---
execution: subagent
agent: diana-documento
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao-aprovada.md
outputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md
model_tier: powerful
---

# Step 05: Criar Documentação Base (TAP + PM Canvas + Plano Geral)

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao-aprovada.md` — qualificação aprovada com todos os dados do projeto
- `squads/vmo-autonomo/pipeline/data/domain-framework.md` — padrões e modelos PMO/PMBOK
- `squads/vmo-autonomo/pipeline/data/output-examples.md` — exemplos de TAP e PM Canvas
- `squads/vmo-autonomo/pipeline/data/quality-criteria.md` — critérios de qualidade dos documentos

## Instructions

### Process
1. **Executar tarefa `criar-tap.md`**: Gerar o Termo de Abertura do Projeto completo.
2. **Executar tarefa `criar-pm-canvas.md`**: Gerar o PM Canvas em 9 blocos consistente com o TAP.
3. **Executar tarefa `criar-plano-geral.md`**: Gerar o Plano Geral com os 10 planos subsidiários.
4. **Verificar consistência cross-documentos**: Confirmar que prazo, custo, escopo e stakeholders são idênticos nos três documentos.
5. **Salvar output consolidado**: Escrever todos os três documentos em `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md`.

## Output Format

```markdown
# Documentação Base de Iniciação — [Nome do Projeto]

---
## TERMO DE ABERTURA DO PROJETO (TAP)
[TAP completo]

---
## PM CANVAS
[Canvas 9 blocos]

---
## PLANO GERAL DO PROJETO
[Plano com 10 planos subsidiários]
```

## Output Example

> Ver `squads/vmo-autonomo/pipeline/data/output-examples.md` — Exemplo 2 (TAP completo) e documentação de referência.

## Veto Conditions

Reject and redo if ANY are true:
1. O TAP não tem objetivo SMART com métrica e prazo
2. O PM Canvas tem algum dos 9 blocos vazio
3. Prazo ou orçamento diferente entre TAP e PM Canvas

## Quality Criteria

- [ ] TAP com objetivo SMART, sponsor, escopo "dentro/fora", mínimo 3 critérios de sucesso
- [ ] PM Canvas com todos os 9 blocos preenchidos
- [ ] Plano Geral com todos os 10 planos subsidiários
- [ ] Consistência verificada: prazo e custo idênticos nos três documentos
