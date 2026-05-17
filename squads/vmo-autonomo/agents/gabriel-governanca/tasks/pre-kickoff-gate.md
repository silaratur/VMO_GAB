---
task: "Gate de Kick-off"
order: 2
mode: on-demand
input:
  - qualificacao_aprovada: "projects/{project}/01-qualificacao/qualificacao-aprovada.md"
  - documentacao_base: "projects/{project}/02-iniciacao/documentacao-base.md"
output:
  - kickoff_gate: "Autorização formal de kick-off ou lista de bloqueios pendentes"
---

# Gate de Kick-off

Verifica formalmente se todas as condições bloqueantes (CBs) foram resolvidas antes de autorizar o início da fase de execução do projeto. Este gate é o ponto de controle entre a fase de iniciação (documentação aprovada) e a fase de execução (trabalho real começa). Sem autorização formal do gate, o kick-off não pode ocorrer.

## Process

1. **Listar todas as CBs da qualificação:** Ler `qualificacao-aprovada.md` e extrair todas as condições bloqueantes registradas.
2. **Verificar cada CB no TAP:** Para cada CB, verificar no `documentacao-base.md` (TAP) se há evidência documental de resolução — não apenas campo preenchido, mas conteúdo concreto (nome real do sponsor, número de aprovação do orçamento, etc.).
3. **Verificar sponsor:** Confirmar que o TAP tem sponsor com nome, cargo e que o cargo é Diretor ou superior.
4. **Verificar orçamento:** Confirmar que há evidência de aprovação formal do orçamento (não apenas estimativa).
5. **Emitir veredicto:** AUTORIZADO (todas CBs resolvidas) ou BLOQUEADO (listar CBs pendentes com ação e prazo).

## Output Format

```markdown
# Gate de Kick-off — [PROJ-CODE]
Data: YYYY-MM-DD | Auditor: Gabriel Governança

## RESULTADO: [AUTORIZADO ✅ | BLOQUEADO 🔴]

## Verificação de Condições Bloqueantes

| CB | Descrição | Status | Evidência |
|----|-----------|--------|-----------|
| CB-01 | Sponsor Diretor+ identificado | ✅/❌ | [Nome, Cargo — fonte: TAP seção X] |
| CB-02 | Orçamento aprovado formalmente | ✅/❌ | [Valor aprovado, aprovador — fonte: ...] |

## [Se AUTORIZADO]
**Kick-off autorizado para:** [data recomendada]
**Observações:** [pontos de atenção para a fase de execução]

## [Se BLOQUEADO]
**CBs pendentes que impedem o kick-off:**

| CB | Ação requerida | Responsável | Prazo limite |
|----|---------------|-------------|-------------|
| CB-01 | [ação específica] | [nome] | [data] |

**Revisão do gate:** após resolução das CBs acima, solicitar nova verificação.
```

## Veto Conditions

Rejeitar e refazer se:
1. AUTORIZADO emitido com qualquer CB não resolvida com evidência documental
2. Sponsor listado sem verificação do nível hierárquico (Diretor+)
