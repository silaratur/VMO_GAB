---
task: "Gate de Governança — Fase 02: Qualificação"
order: 1
mode: phase-gate
input:
  - demanda_coletada: "projects/{project}/01-qualificacao/demanda-coletada.md"
  - qualificacao: "projects/{project}/01-qualificacao/qualificacao.md"
  - gate_intake: "projects/{project}/01-qualificacao/gate-intake.md"
output:
  - gate_qualificacao: "Veredicto PASS/HOLD com lista de bloqueios ou confirmação de conformidade"
---

# Gate de Governança — Fase 02: Qualificação

Verifica se o parecer de qualificação emitido pelo Felipe Filtro cumpre os requisitos de
governança antes de ir ao checkpoint de aprovação. Gabriel não re-avalia se as notas
estão certas (isso é domínio do Felipe) — verifica se o **processo de qualificação foi
aplicado com rigor formal**: todos os critérios pontuados, CBs documentadas, classificação
declarada, decisão coerente com pontuação, e se o sponsor mínimo foi identificado ou
formalmente registrado como condição bloqueante.

---

## Checklist de Governança — Qualificação

### G1 — Completude Formal do Parecer
- [ ] Todos os 10 critérios estão presentes e pontuados (1–10 cada)
- [ ] Cada critério tem justificativa de ao menos 1 linha (não apenas número)
- [ ] Pontuação total calculada e percentual declarado
- [ ] Classificação explícita: PROJETO / MELHORIA EVOLUTIVA / MELHORIA CORRETIVA
- [ ] Decisão explícita: APROVADO / COM CONDIÇÕES / REPROVADO / EM ESPERA

### G2 — Coerência da Decisão com a Pontuação
- [ ] ≥75 pts → decisão APROVADO (sem condições desnecessárias)
- [ ] 50–74 pts → decisão COM CONDIÇÕES (condições listadas)
- [ ] <50 pts → decisão REPROVADO ou EM ESPERA (justificativa de EM ESPERA requerida)
- [ ] Decisão inconsistente com pontuação = NC-CRÍTICA → HOLD imediato

### G3 — Condições Bloqueantes de Governança
Verificar se as seguintes CBs obrigatórias estão documentadas (quando aplicáveis):
- [ ] **CB-Sponsor:** Sponsor com nível Diretor+ identificado ou registrado como CB aberta
- [ ] **CB-Orçamento:** Aprovação formal de orçamento presente ou registrada como CB aberta
- [ ] **CB-Escopo:** Escopo mínimo suficiente para iniciar documentação ou registrado como CB
- Ausência de qualquer CB que deveria existir = NC-MODERADA (3+ bloqueia)

### G4 — Consistência com o Gate de Intake
- [ ] Os dados do solicitante no parecer batem com os da demanda coletada
- [ ] Não há informações novas no parecer que não estavam na demanda (sem invenção)
- [ ] Lacunas identificadas pela Iara foram tratadas no parecer (mencionadas ou pontuadas)

### G5 — Sinalizações de Risco de Processo
- [ ] Se demanda classificada como MELHORIA: time de sustentação ERP indicado
- [ ] Se EM ESPERA: prazo para resubmissão declarado
- [ ] Próximos passos com responsável e prazo presentes (ao menos 1 ação)

---

## Output Format

```markdown
# Gate de Governança — Fase 02: Qualificação
Projeto: {project}
Data: YYYY-MM-DD
Auditor: Gabriel Governança

## Veredicto: [PASS / HOLD]

### Checklist
| # | Critério | Status | Observação |
|---|----------|--------|------------|
| G1.1 | 10 critérios pontuados | ✅ / ❌ | |
| G1.2 | Justificativas presentes | ✅ / ⚠️ / ❌ | |
| G1.3 | Classificação declarada | ✅ / ❌ | |
| G1.4 | Decisão declarada | ✅ / ❌ | |
| G2.1 | Decisão coerente com pontuação | ✅ / ❌ | [pontuação: X/100 → decisão esperada: Y] |
| G3.1 | CB-Sponsor documentada | ✅ / ⚠️ ABERTA / ❌ AUSENTE | |
| G3.2 | CB-Orçamento documentada | ✅ / ⚠️ ABERTA / ❌ AUSENTE | |
| G3.3 | CB-Escopo documentada | ✅ / ⚠️ ABERTA / N/A | |
| G4.1 | Dados consistentes com intake | ✅ / ❌ | |
| G4.2 | Sem informações inventadas | ✅ / ❌ | |
| G5.1 | Time sustentação indicado (se melhoria) | ✅ / N/A | |
| G5.2 | Próximos passos com responsável | ✅ / ❌ | |

### [Se HOLD] Bloqueios de Governança
| # | Tipo | Bloqueio | Ação Requerida | Responsável |
|---|------|----------|----------------|-------------|
| B1 | NC-CRÍTICA / NC-MOD | [descrição] | [o que Felipe deve corrigir] | Felipe Filtro |

### [Se PASS] Condições Bloqueantes Registradas (para monitoramento)
| CB | Status | Prazo para Resolução |
|----|--------|----------------------|
| CB-Sponsor | [aberta/resolvida] | [prazo se aberta] |
| CB-Orçamento | [aberta/resolvida] | [prazo se aberta] |

### Encaminhamento
[PASS → Checkpoint Step 6: Aprovar Qualificação]
[HOLD → Retornar ao Step 4: Felipe revisa com as correções B1, B2...]
```

## Quality Criteria

- [ ] Todos os 12 critérios do checklist avaliados
- [ ] Veredicto PASS ou HOLD sem ambiguidade
- [ ] Se HOLD: cada bloqueio tem tipo (CRÍTICA/MOD), descrição e ação para Felipe
- [ ] CBs obrigatórias rastreadas para monitoramento mesmo quando abertas (não bloqueia, mas registra)

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Veredicto ausente
2. HOLD emitido sem identificar qual critério do checklist falhou
3. Decisão inconsistente com pontuação não foi sinalizada como NC-CRÍTICA
4. Gate avaliou se as notas do Felipe estão corretas — isso é fora do escopo de governança
