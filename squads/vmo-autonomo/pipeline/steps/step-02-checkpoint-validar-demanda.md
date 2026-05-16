---
type: checkpoint
outputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-validada.md
---

# Step 02: Checkpoint — Validar Demanda

A Iara Inbound coletou e estruturou a demanda. Revise o resumo abaixo e confirme antes de avançar para a qualificação.

## O que foi coletado

Leia o arquivo `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md` e apresente ao usuário:

1. **Resumo da demanda**: solicitante, necessidade, pedido e benefício esperado em 3-5 linhas
2. **Lacunas identificadas**: campos que precisam de confirmação ou esclarecimento
3. **Pergunta de validação**: "Este resumo está correto? Posso avançar para a análise de qualificação?"

## Opções para o usuário

Apresente com AskUserQuestion:
1. **Confirmar e avançar** — demanda está correta, prosseguir para qualificação
2. **Corrigir informação** — algum dado está errado, fornecer correção
3. **Adicionar contexto** — falta informação importante que deve ser incluída

## Output

Salvar o documento de demanda validada (com as correções do usuário, se houver) em `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-validada.md`.
