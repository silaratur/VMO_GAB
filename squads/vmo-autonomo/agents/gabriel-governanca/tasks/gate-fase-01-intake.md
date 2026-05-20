---
task: "Gate de Governança — Fase 01: Intake"
order: 1
mode: phase-gate
input:
  - demanda_coletada: "projects/{project}/01-qualificacao/demanda-coletada.md"
output:
  - gate_intake: "Veredicto PASS/HOLD com lista de bloqueios ou confirmação de conformidade"
---

# Gate de Governança — Fase 01: Intake

Verifica se a demanda coletada pela Iara Inbound cumpre os requisitos mínimos de governança
de entrada. Este gate não avalia qualidade de conteúdo nem profundidade da análise — avalia
**processo**: o intake foi feito com rastreabilidade, o solicitante está identificado, o canal
está documentado e as lacunas foram reportadas em vez de omitidas.

É um gate rápido: PASS libera para o checkpoint. HOLD retorna ao Step 1 com ações específicas.

---

## Checklist de Governança — Intake

### G1 — Identificação do Solicitante
- [ ] Nome do solicitante presente e não genérico ("alguém da área" não é identificação)
- [ ] Área/divisão identificada
- [ ] Se cargo não informado: registrado como lacuna — não bloqueia, mas deve constar

### G2 — Rastreabilidade de Canal e Fonte
- [ ] Canal de entrada declarado explicitamente (ticket, e-mail, pdf, direto, etc.)
- [ ] Pelo menos uma fonte documentada com data e tipo
- [ ] Cada dado relevante tem referência de origem (não "informação geral")

### G3 — Integridade do Processo de Captação
- [ ] Seção "Lacunas Identificadas" presente (mesmo que vazia significa que Iara verificou)
- [ ] Necessidade de negócio distinguida do pedido técnico (dois campos separados)
- [ ] Não há campos inventados — dados sem fonte devem estar marcados NÃO INFORMADO

### G4 — Sinalizações de Risco de Governança
- [ ] Aprovações informais já concedidas estão documentadas (se existem)
- [ ] Conflitos ou pressões políticas identificados nas fontes estão registrados
- [ ] Se o ticket está com SLA em atraso: registrado e sinalizado

---

## Output Format

```markdown
# Gate de Governança — Fase 01: Intake
Projeto: {project}
Data: YYYY-MM-DD
Auditor: Gabriel Governança

## Veredicto: [PASS / HOLD]

### Checklist
| # | Critério | Status | Observação |
|---|----------|--------|------------|
| G1.1 | Solicitante identificado | ✅ PASS / ⚠️ PARCIAL / ❌ HOLD | [detalhe] |
| G1.2 | Área/divisão identificada | ✅ / ⚠️ / ❌ | |
| G2.1 | Canal de entrada declarado | ✅ / ❌ | |
| G2.2 | Fonte com data e tipo documentada | ✅ / ❌ | |
| G2.3 | Dados com referência de origem | ✅ / ⚠️ / ❌ | |
| G3.1 | Seção Lacunas presente | ✅ / ❌ | |
| G3.2 | Necessidade ≠ Pedido técnico | ✅ / ❌ | |
| G3.3 | Sem campos inventados | ✅ / ❌ | |
| G4.1 | Aprovações informais documentadas | ✅ / N/A | |
| G4.2 | SLA/atraso sinalizado (se aplicável) | ✅ / N/A | |

### [Se HOLD] Bloqueios de Governança
| # | Bloqueio | Ação Requerida | Responsável |
|---|----------|----------------|-------------|
| B1 | [descrição] | [o que Iara deve corrigir] | Iara Inbound |

### [Se PASS] Observações
[Itens ⚠️ PARCIAL que não bloqueiam mas devem ser monitorados nas próximas fases]

### Encaminhamento
[PASS → Checkpoint Step 3: Validar Demanda]
[HOLD → Retornar ao Step 1: Iara refaz com as correções B1, B2...]
```

## Quality Criteria

- [ ] Todos os 10 critérios do checklist avaliados explicitamente
- [ ] Veredicto PASS ou HOLD declarado sem ambiguidade
- [ ] Se HOLD: cada bloqueio tem ação específica e responsável
- [ ] Gate concluído sem re-avaliar conteúdo de negócio (escopo da Iara)

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Veredicto ausente (nem PASS nem HOLD declarado)
2. HOLD emitido sem listar os bloqueios específicos
3. Gate avaliou conteúdo de negócio (ex: "a demanda não tem valor") — fora do escopo
