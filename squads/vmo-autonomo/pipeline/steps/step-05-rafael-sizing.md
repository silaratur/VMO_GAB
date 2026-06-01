---
execution: inline
agent: rafael-requisito
inputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-validada.md
outputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/sizing.md
---

# Step 05: Sizing Inicial de Escopo

Rafael Requisito realiza um levantamento leve de escopo para subsidiar o Felipe Filtro
na avaliação do critério 7 (Esforço Estimado). Este step NÃO é a ERF completa —
é uma estimativa de esforço por fase, baseada no escopo declarado na demanda.

## Por que este step existe

Felipe Filtro não pode dimensionar esforço por benchmark sem dados de requisitos.
Critério 7 só pode ser pontuado com confiança quando há uma estimativa de esforço
fundamentada em escopo — mesmo que preliminar. Este step garante esse dado antes
da qualificação.

## Context Loading

Carregar antes de executar:
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-validada.md`
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md`

## Instructions

Executar a task `sizing-inicial.md` do agente Rafael Requisito.

## Output Format

```markdown
# Sizing Inicial de Escopo
Projeto: {project}
Data: YYYY-MM-DD
Analista: Rafael Requisito
Fase: Pré-qualificação (para subsidiar critério 7 — Esforço)

## Escopo Preliminar Identificado
[Lista de funcionalidades/integrações identificadas a partir da demanda]

## Estimativa de Esforço por Fase
| Fase | Atividades principais | Esforço estimado | Confiança |
|------|----------------------|------------------|-----------|
| Levantamento de requisitos | ... | Xh | ALTA/MÉDIA/BAIXA |
| Desenvolvimento/Configuração | ... | Xh | ALTA/MÉDIA/BAIXA |
| Testes e homologação | ... | Xh | ALTA/MÉDIA/BAIXA |
| Go-live e suporte inicial | ... | Xh | ALTA/MÉDIA/BAIXA |
| TOTAL | | Xh | ALTA/MÉDIA/BAIXA |

## Classificação de Esforço
- [ ] < 80h → Melhoria Corretiva/Evolutiva simples
- [ ] 80–160h → Melhoria Evolutiva complexa
- [ ] > 160h → Projeto formal

## Fatores de Risco que Afetam o Esforço
[Itens que podem aumentar ou diminuir o esforço estimado]

## Lacunas de Escopo (para ERF futura)
[O que ainda precisa ser definido antes de um dimensionamento preciso]

## Perguntas para Confirmar Escopo
[Máximo 5 perguntas que, se respondidas, reduziriam a incerteza da estimativa]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Estimativa de esforço dada como número único sem divisão por fase
2. Confiança não declarada para cada fase
3. Classificação de esforço (<80h / 80-160h / >160h) ausente
4. Rafael usou benchmark de mercado sem analisar o escopo específico da demanda

## Quality Criteria

- [ ] Escopo preliminar identificado com base na demanda (não genérico)
- [ ] Esforço estimado por fase com confiança declarada
- [ ] Classificação de esforço (<80h / 80-160h / >160h) declarada
- [ ] Fatores de risco documentados
- [ ] Perguntas de escopo listadas para ERF futura
