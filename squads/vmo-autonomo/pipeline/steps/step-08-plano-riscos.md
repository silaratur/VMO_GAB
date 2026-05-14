---
execution: inline
agent: pedro-perigo
inputFile: squads/vmo-autonomo/output/documentacao-base.md
outputFile: squads/vmo-autonomo/output/plano-riscos.md
---

# Step 08: Plano de Riscos

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/output/documentacao-base.md` — TAP com premissas, restrições e contexto
- `squads/vmo-autonomo/output/cronograma.md` — cronograma com caminho crítico (fontes de risco de prazo)
- `squads/vmo-autonomo/output/requisitos.md` — requisitos (fontes de riscos técnicos)
- `squads/vmo-autonomo/pipeline/data/anti-patterns.md` — riscos típicos em projetos PMO

## Instructions

### Process
1. **Executar tarefa `identificar-riscos.md`**: Identificar mínimo 5 riscos com P×I e nível de prioridade.
2. **Executar tarefa `criar-plano-riscos.md`**: Definir estratégia de resposta, trigger e reserva de contingência.
3. **Compilar documento único**: Registro de Riscos + Plano de Resposta em arquivo único.
4. **Salvar output**: Escrever em `squads/vmo-autonomo/output/plano-riscos.md`.

## Output Format

```markdown
# Plano de Gestão de Riscos — [Nome do Projeto]

## Registro de Riscos
[tabela com ID, categoria, descrição, P, I, score, nível]

## Plano de Resposta por Risco
[para cada risco: estratégia, trigger, ações, responsável, prazo, contingência]

## Reserva de Contingência Calculada
[tabela de valor esperado + recomendação de reserva]
```

## Output Example

> Ver exemplos nas tasks `identificar-riscos.md` e `criar-plano-riscos.md` — Projeto SRF com R-001 a R-007.

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 5 riscos documentados
2. Algum risco CRÍTICO ou ALTO sem trigger definido
3. Reserva de contingência sem cálculo de valor esperado

## Quality Criteria

- [ ] Mínimo 5 riscos com P, I e score calculado
- [ ] Todos os CRÍTICOS e ALTOS com trigger e plano de contingência
- [ ] Riscos cobrindo ao menos 4 categorias
- [ ] Reserva de contingência calculada com valor esperado
