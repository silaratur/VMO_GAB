---
task: "Avaliação de Change Request"
order: 3
mode: on-demand
input:
  - descricao_mudanca: "Descrição da mudança solicitada fornecida pelo usuário"
  - documentacao_base: "projects/{project}/02-iniciacao/documentacao-base.md"
  - cronograma: "projects/{project}/03-planejamento/cronograma.md"
  - plano_riscos: "projects/{project}/03-planejamento/plano-riscos.md"
  - kpis: "projects/{project}/03-planejamento/kpis.md"
output:
  - change_request: "Avaliação formal do CR com impacto calculado e recomendação"
---

# Avaliação de Change Request

Avalia formalmente qualquer solicitação de mudança de baseline (escopo, prazo ou custo) em um projeto ativo. Toda mudança — independente do tamanho percebido — passa por esta avaliação antes de ser autorizada. Mudança aprovada verbalmente sem CR formal é escopo creep e não será reconhecida como baseline oficial.

## Process

1. **Capturar a solicitação:** Registrar a mudança solicitada com clareza: o que muda, quem solicitou e por quê.
2. **Documentar a baseline atual:** Registrar os valores atuais de escopo, prazo e custo ANTES da mudança.
3. **Calcular o impacto nas 3 dimensões:**
   - **Escopo:** O que é adicionado, removido ou alterado? Quantos RFs são afetados?
   - **Prazo:** Quantos dias/semanas de impacto? O caminho crítico é afetado?
   - **Custo:** Qual o impacto financeiro em R$? O BAC precisa ser revisado?
4. **Avaliar impacto em riscos:** A mudança introduz novos riscos? Riscos existentes têm probabilidade ou impacto alterados?
5. **Emitir recomendação:** APROVAR / APROVAR COM RESSALVAS / REJEITAR com justificativa.
6. **Documentar nova baseline (se aprovado):** Registrar os valores pós-mudança para cada dimensão afetada.

## Output Format

```markdown
# Change Request CR-[PROJ-CODE]-[NNN]
Data: YYYY-MM-DD | Auditor: Gabriel Governança | Projeto: [nome]
Solicitante: [nome] | Tipo: [Escopo / Prazo / Custo / Múltiplo]

## Descrição da Mudança Solicitada
[O que está sendo solicitado, com contexto e justificativa do solicitante]

## Baseline Atual (antes da mudança)
| Dimensão | Valor atual |
|----------|-------------|
| Escopo | [descrição do escopo atual] |
| Prazo | [data de go-live atual] |
| Custo (BAC) | R$ [valor atual] |

## Análise de Impacto

### Impacto no Escopo
[O que muda no escopo. Se adição: quantos RFs novos? Se remoção: quais RFs saem?]
**Delta de escopo:** [+N RFs / -N RFs / modificação de X funcionalidades]

### Impacto no Prazo
[Quantos dias/semanas são acrescentados ou removidos. O caminho crítico é afetado?]
**Delta de prazo:** [+N semanas / sem impacto / redução de N dias]
**Nova data de go-live estimada:** [data]

### Impacto no Custo
[Qual o impacto financeiro? Desenvolvimento adicional, infraestrutura, licenças?]
**Delta de custo:** [+R$ / -R$ / sem impacto]
**Novo BAC estimado:** R$ [valor]
**Contingência remanescente:** R$ [valor]

### Impacto em Riscos
| Risco | Antes | Depois | Novo risco? |
|-------|-------|--------|-------------|
| [risco existente] | P=X I=Y | P=X' I=Y' | — |
| [novo risco introduzido] | — | P=X I=Y | Sim |

## RECOMENDAÇÃO: [APROVAR ✅ | APROVAR COM RESSALVAS ⚠️ | REJEITAR ❌]

**Justificativa:** [Raciocínio da recomendação em 3-5 linhas]

## [Se APROVADO] — Nova Baseline

| Dimensão | Baseline anterior | Nova baseline |
|----------|------------------|---------------|
| Prazo | [data anterior] | [nova data] |
| Custo (BAC) | R$ [anterior] | R$ [novo] |
| Escopo | [anterior] | [novo] |

**Documentos que precisam ser atualizados:**
- [ ] TAP (seção de escopo / orçamento)
- [ ] Cronograma (marcos e datas)
- [ ] ERF (RFs adicionados/removidos)
- [ ] KPIs (BAC atualizado)
- [ ] Plano de Riscos (novos riscos)

## [Se REJEITADO]
**Motivo da rejeição:** [justificativa objetiva]
**Alternativa sugerida:** [se houver uma forma de atender à necessidade sem a mudança proposta]
```

## Veto Conditions

Rejeitar e refazer se:
1. Impacto calculado sem valores numéricos (dias, R$, número de RFs)
2. APROVADO sem documentar a nova baseline nas dimensões afetadas
3. Novos riscos introduzidos pela mudança não foram identificados
