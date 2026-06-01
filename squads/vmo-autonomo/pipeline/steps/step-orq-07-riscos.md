---
execution: inline
agent: oscar-orquestrador
inputFile: squads/vmo-autonomo/projects/{project}/03-planejamento/plano-riscos.md
on_reject: 18
---

# [ORQ] Step 07-ORQ: Avaliar Plano de Riscos

## Context

- **Deliverable avaliado**: Plano de Riscos e Registro de Riscos (`plano-riscos.md`)
- **Agente responsável**: Pedro Perigo
- **Critérios aplicáveis**: quality-criteria.md — seção: Plano de Riscos
- **Cross-check**: `documentacao-base.md` — riscos de alto nível do TAP devem estar no registro de riscos

## Instructions

### Carregar antes de avaliar
- `squads/vmo-autonomo/projects/{project}/03-planejamento/plano-riscos.md` — deliverable a avaliar
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — para cross-check de riscos de alto nível do TAP
- `pipeline/data/quality-criteria.md` — seção: Plano de Riscos
- `pipeline/data/anti-patterns.md` — seção: Anti-Patterns de Gestão de Riscos

### Critérios BLOCKING — Plano de Riscos

1. Mínimo 5 riscos identificados e documentados
2. Probabilidade e impacto avaliados para CADA risco (escala 1-5 ou H/M/L — consistente ao longo do documento)
3. Estratégia de resposta definida para cada risco (mitigar, aceitar, transferir, evitar)
4. Responsável e prazo por ação de resposta definidos (risco sem dono não é gerenciado)

### Critério BLOCKING adicional — Cross-check com TAP
- Os riscos de alto nível listados no TAP devem aparecer no registro de riscos (não podem ser ignorados)

### Processo de Avaliação

1. Ler `plano-riscos.md` na íntegra.
2. Contar os riscos identificados — mínimo 5.
3. Verificar os 4 critérios BLOCKING — um a um, para cada risco.
4. Verificar cross-check: riscos do TAP estão presentes no registro?
5. Verificar critérios de qualidade: cobertura de 4 categorias (técnico, financeiro, prazo, stakeholders), triggers para riscos críticos, reserva de contingência estimada.
6. Emitir decisão conforme `avaliar-entrega.md`.

### Se REDIRECIONAMENTO for necessário

Apresentar via AskUserQuestion:
- Pergunta: "Detectei problema no Plano de Riscos. O que prefere fazer?"
- Opção 1: "Redirecionar para Pedro Perigo — [ação específica detectada]"
- Opção 2: "Continuar mesmo assim — registrar ressalva e seguir"

Se confirmado: emitir REPROVADO → Pipeline Runner aciona `on_reject: 18` (retorna ao Step 17 — Pedro).

## Veto Conditions

Reject and redo if ANY are true:
1. Contagem de riscos não realizada (não pode presumir que há 5+)
2. Cross-check com riscos de alto nível do TAP não realizado
3. Qualquer BLOCKING violado mas decisão marcada como APROVADO
4. Redirecionamento executado sem AskUserQuestion com confirmação do usuário
