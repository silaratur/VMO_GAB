---
execution: inline
agent: sara-status
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md
outputFile: squads/vmo-autonomo/projects/{project}/04-monitoramento/status-report-{date}.md
---

# Step 11: Status Report Inicial

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — TAP com objetivos e critérios de sucesso
- `squads/vmo-autonomo/projects/{project}/03-planejamento/kpis.md` — framework de KPIs e semáforo de saúde
- `squads/vmo-autonomo/projects/{project}/03-planejamento/plano-riscos.md` — riscos identificados
- `squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md` — baseline de prazo

## Instructions

### Process
1. **Executar tarefa `gerar-status-report.md`**: Criar o primeiro status report do projeto (fase de iniciação concluída).
2. **Executar tarefa `pesquisa-satisfacao.md`**: Criar o template da pesquisa de satisfação para a fase de iniciação.
3. **Status inicial**: Como este é o report de iniciação, o status geral deve refletir "Iniciação concluída — aguardando início da execução" com semáforo verde.
4. **Salvar output**: Escrever ambos documentos em `squads/vmo-autonomo/projects/{project}/04-monitoramento/status-report-{date}.md`.

## Output Format

```markdown
# Status Report #001 — [Nome do Projeto]
[Status Report completo com semáforo de iniciação]

---

# Pesquisa de Satisfação — Fase de Iniciação
[Formulário de pesquisa para validação das expectativas]
```

## Output Example

> Ver `pipeline/data/output-examples.md` — Exemplo 3 (Status Report) e `pesquisa-satisfacao.md`.

## Veto Conditions

Reject and redo if ANY are true:
1. Status Report sem semáforo visual consolidado
2. Status Report sem seção de próximos passos com responsável e data

## Quality Criteria

- [ ] Semáforo presente por dimensão
- [ ] Progresso de iniciação documentado (documentos criados)
- [ ] Próximos passos claros para início da execução
- [ ] Pesquisa de satisfação com NPS + perguntas qualitativas
