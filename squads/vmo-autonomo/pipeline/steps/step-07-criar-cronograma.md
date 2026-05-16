---
execution: inline
agent: carlos-cronograma
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md
outputFile: squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md
---

# Step 07: Criar Cronograma

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — TAP com escopo, fases e restrições de prazo
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md` — ERF com requisitos priorizados para decomposição técnica
- `squads/vmo-autonomo/pipeline/data/domain-framework.md` — fases típicas de projetos PMO e entregas

## Instructions

### Process
1. **Executar tarefa `criar-wbs.md`**: Decompor o escopo em WBS com mínimo 3 níveis.
2. **Executar tarefa `criar-cronograma.md`**: Criar cronograma com datas, dependências e caminho crítico.
3. **Incluir buffer de contingência**: 15% do prazo total como reserva de gestão explícita.
4. **Salvar output**: Escrever WBS + Cronograma em `squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md`.

## Output Format

```markdown
# Planejamento de Prazo — [Nome do Projeto]

## WBS (Estrutura Analítica do Projeto)
[WBS hierárquica com 3+ níveis]

## Cronograma Detalhado
[tabela por fase com datas, durações, dependências, responsáveis]

## Marcos Principais
[tabela de milestones]

## Caminho Crítico
[sequência de atividades com zero folga]

## Buffer de Contingência
[reserva explícita de 15% do prazo]
```

## Output Example

> Ver o exemplo completo no `criar-cronograma.md` — Projeto SRF com fases de maio a dezembro/2026.

## Veto Conditions

Reject and redo if ANY are true:
1. WBS tem menos de 3 níveis
2. Nenhum caminho crítico identificado no cronograma
3. Buffer de contingência ausente ou embutido nas atividades individuais

## Quality Criteria

- [ ] WBS com mínimo 3 níveis cobrindo 100% do escopo do TAP
- [ ] Cronograma com datas de início/fim por atividade
- [ ] Dependências documentadas para atividades críticas
- [ ] Marcos principais identificados
- [ ] Buffer de 15% explícito e centralizado
