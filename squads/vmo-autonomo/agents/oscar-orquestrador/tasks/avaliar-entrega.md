# Tarefa: Avaliar Entrega

## Objetivo

Avaliar a qualidade e completude do deliverable produzido pelo agente anterior, contra os critérios VMO documentados, e emitir decisão de APROVADO ou REDIRECIONAMENTO.

## Inputs (fornecidos pelo step file)

- `deliverable_path`: caminho do arquivo a ser avaliado
- `deliverable_type`: tipo de documento (ex: demanda-coletada, tap, requisitos)
- `agent_responsible`: nome completo do agente que produziu o deliverable
- `criteria_section`: seção do quality-criteria.md a aplicar
- `antipattern_section`: seção do anti-patterns.md relevante
- `cross_check_files`: lista de deliverables anteriores para verificação de consistência (quando definido)

## Process

1. **Carregar critérios**: Ler `pipeline/data/quality-criteria.md` — focar na seção indicada em `criteria_section`.
2. **Carregar anti-padrões**: Ler `pipeline/data/anti-patterns.md` — focar em `antipattern_section`.
3. **Ler o deliverable**: Ler o arquivo em `deliverable_path` na íntegra.
4. **Verificar critérios BLOCKING**: Para cada critério BLOCKING da seção, verificar se foi atendido.
   - Se QUALQUER BLOCKING falhar → decisão imediata: REPROVADO. Não pontuar o resto.
5. **Verificar critérios de qualidade** (se todos os BLOCKINGs passaram): Verificar conformidade dos itens não-obrigatórios.
6. **Verificar consistência cross-documento** (se `cross_check_files` definido): Ler os arquivos listados e comparar valores críticos — prazo, custo, escopo, stakeholders. Inconsistência em valor crítico = BLOCKING.
7. **Emitir decisão**:
   - Todos os BLOCKINGs atendidos + consistência ok → **APROVADO**
   - Qualquer BLOCKING violado ou inconsistência crítica → **REDIRECIONAMENTO PROPOSTO**

## Protocolo de Redirecionamento

Quando a decisão é REDIRECIONAMENTO PROPOSTO:

1. Formular o diagnóstico estruturado:
   ```
   🔴 PROBLEMA DETECTADO — {deliverable_type}

   Problema: {descrição específica do que está faltando ou errado}
   Critério violado: {nome do critério} — seção "{criteria_section}" em quality-criteria.md
   Colega responsável: {agent_responsible}
   Ação esperada: {o que o agente deve corrigir, com especificidade}
   ```

2. Apresentar via AskUserQuestion:
   - Pergunta: "Detectei um problema crítico em [deliverable_type]. O que prefere fazer?"
   - Opção 1: "Redirecionar para [agent_responsible] — [ação específica resumida]"
   - Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

3. Se usuário confirmar Opção 1 (redirecionar):
   - Emitir output com marcador "REPROVADO" + diagnóstico completo
   - O `on_reject` do step será acionado pelo Pipeline Runner

4. Se usuário escolher Opção 2 (continuar):
   - Emitir output "APROVADO (COM RESSALVA)" + diagnóstico registrado como ressalva

## Output Format

### Quando APROVADO:
```
🎯 APROVADO — {deliverable_type}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Critérios BLOCKING: todos atendidos
Critérios de qualidade: conformidade satisfatória
{ressalvas não-bloqueantes, se houver — ou omitir}
Ótimo trabalho, {agent_responsible}! Continuando para próximo step.
```

### Quando REPROVADO (após confirmação do usuário):
```
🔴 REDIRECIONAMENTO CONFIRMADO — {deliverable_type}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problema: {descrição específica}
Critério violado: {nome} — {seção em quality-criteria.md}
Colega responsável: {agent_responsible}
Ação esperada: {instrução específica de correção}
```

### Quando APROVADO COM RESSALVA:
```
🟡 APROVADO COM RESSALVA — {deliverable_type}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Critérios BLOCKING: todos atendidos
Ressalva: {ponto subótimo registrado — não bloqueante}
Bom trabalho, {agent_responsible}! Continuando para próximo step.
```

## Veto Conditions

Reject and redo if ANY are true:
1. Decisão emitida sem verificar quality-criteria.md (não pode avaliar de memória)
2. BLOCKING violado mas decisão marcada como APROVADO
3. REDIRECIONAMENTO proposto sem AskUserQuestion (redirecionar sem confirmação do usuário é proibido)
4. Diagnóstico de reprovação sem nomear o colega responsável e a ação esperada
