---
execution: subagent
agent: rafael-requisito
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao-aprovada.md
outputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md
model_tier: powerful
---

# Step 06: Especificar Requisitos Funcionais

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao-aprovada.md` — qualificação com escopo e resultado esperado
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — TAP com escopo delimitado (se já disponível)
- `squads/vmo-autonomo/pipeline/data/domain-framework.md` — referência de tipos de requisitos PMO/TI

## Instructions

### Process
1. **Executar tarefa `levantar-requisitos.md`**: Elicitar todos os RF e RNF a partir do escopo e resultado esperado.
2. **Executar tarefa `criar-erf.md`**: Organizar, priorizar com MoSCoW e adicionar critérios de aceitação.
3. **Salvar output**: Escrever a ERF completa em `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md`.

**Nota:** Este step roda em paralelo com o Step 05. Ambos leem `qualificacao-aprovada.md` independentemente.

## Output Format

```markdown
# Especificação de Requisitos Funcionais (ERF) — [Nome do Projeto]
[ERF completa conforme template da task criar-erf.md]
[incluir: RF numerados com MoSCoW, RNF, glossário, aprovação]
```

## Output Example

> Ver o exemplo completo no `criar-erf.md` — Projeto SRF com RF001-RF009 e RNF001-RNF005.

## Veto Conditions

Reject and redo if ANY are true:
1. Algum Must Have sem critério de aceitação
2. Nenhum RNF especificado (requisitos não-funcionais são sempre obrigatórios)

## Quality Criteria

- [ ] Todos os RF têm ID único e priorização MoSCoW
- [ ] Todos os Must Have têm critério de aceitação mensurável
- [ ] RNFs cobrindo: performance, segurança, disponibilidade
- [ ] Glossário de termos do domínio incluído
- [ ] Tabela de resumo MoSCoW presente
