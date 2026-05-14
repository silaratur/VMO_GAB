---
type: checkpoint
outputFile: squads/vmo-autonomo/output/qualificacao-aprovada.md
---

# Step 04: Checkpoint — Aprovar Qualificação

O Felipe Filtro analisou a demanda e emitiu um parecer de qualificação. Revise a análise e decida se o projeto deve avançar para a fase de documentação.

## O que foi analisado

Leia o arquivo `squads/vmo-autonomo/output/qualificacao.md` e apresente ao usuário:

1. **Resumo do parecer**: decisão emitida, pontuação e principais justificativas
2. **Condições bloqueantes** (se houver): o que precisa ser resolvido antes de avançar
3. **ROI e proposta de valor**: investimento esperado e retorno

## Opções para o usuário

Apresente com AskUserQuestion:
1. **Aprovar e avançar para documentação** — iniciar criação de TAP, PM Canvas e requisitos
2. **Aprovar com ressalvas** — avançar mas registrar pontos de atenção adicionais
3. **Solicitar ajuste na análise** — algum critério foi avaliado incorretamente
4. **Suspender — aguardar mais informações** — resolver condições bloqueantes antes de prosseguir

## Output

Salvar a qualificação aprovada (com decisão do usuário e quaisquer ressalvas registradas) em `squads/vmo-autonomo/output/qualificacao-aprovada.md`.

**Nota:** Somente avançar para o Step 05 se o usuário aprovar (opções 1 ou 2). Se opção 4, encerrar o pipeline e aguardar resolução das condições.
