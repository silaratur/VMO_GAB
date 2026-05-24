# Adendo de Governança — Regras GP 2026-05-24
## Aplicação Retroativa à DEM-2026-007 / PROJ-2026-007

**Data:** 2026-05-24
**Emitido por:** Gabriel Governança — Auditor de Governança VMO
**Origem:** Novas regras estabelecidas pelo GP VMO (Marcelo Silveira) em 2026-05-24

---

## Regras Incorporadas

### Regra 1 — Evidência Obrigatória para Citação de Alta Patente
Toda citação de CEO, Diretor Executivo, VP ou outra alta patente como origem ou justificativa de urgência exige evidência documental comprobatória (e-mail, ata, documento assinado). Sem evidência, o critério de Urgência (Felipe Filtro) não pode sustentar nota acima de 3/10 para este sub-fundamento.

### Regra 2 — Aprovações Obrigatórias para Validação de Demanda
Toda demanda deve ter, obrigatoriamente e sem exceção:
1. Aprovação formal em nível de Diretoria da área solicitante
2. Aprovação formal do Gerente de TI da divisão solicitante

Sem ambas, a demanda retorna ao solicitante para complementação — independente de urgência declarada, criticidade ou pressão política.

---

## Impacto na Qualificação Atual

### Impacto 1 — Critério 4: Urgência (revisão de nota)

**Situação identificada:** Campo "Justificativa de Urgência" = `"Atendimento a demanda da CEO."` — texto livre sem evidência documental comprobatória (e-mail, ata, comunicado formal da CEO).

| Critério | Nota Anterior | Nota Revisada | Motivo |
|----------|--------------|---------------|--------|
| 4. Urgência | 7/10 | **5/10** | Fundamento "CEO demand" rebaixado por ausência de evidência. Urgência válida restante: SLA vencido + risco regulatório CPC 47/IFRS 15 (sem prazo declarado). |

### Impacto 2 — Aprovações Obrigatórias Ausentes

| Aprovação Obrigatória | Status |
|-----------------------|--------|
| Aprovação — Diretoria da área solicitante (Logística Dedicada) | ❌ AUSENTE |
| Aprovação — Gerente de TI da divisão solicitante (VIX Matriz / DTI) | ❌ AUSENTE |

**Status da demanda:** ⚠️ RETORNO REQUERIDO — demanda não pode ser considerada VALIDADA sem as duas aprovações obrigatórias.

---

## Pontuação Revisada

```
 1. Alinhamento Estratégico        9/10  (sem alteração)
 2. Viabilidade Técnica            5/10  (sem alteração)
 3. ROI                            4/10  (sem alteração)
 4. Urgência                       5/10  ▼ revisado (CEO sem evidência)
 5. Maturidade da Demanda          4/10  (sem alteração)
 6. Disponibilidade de Recursos    3/10  (sem alteração)
 7. Esforço Estimado               8/10  (sem alteração)
 8. Impacto Organizacional         7/10  (sem alteração)
 9. Governança Necessária          8/10  (sem alteração)
10. Impacto Regulatório/Financeiro 9/10  (sem alteração)
                                ─────────
                                62/100 (62%)
```

**Decisão:** APROVADO COM CONDIÇÕES (mantida — 62% na faixa 50–74%)
**Status de validação:** ⚠️ RETORNO REQUERIDO (CB-07 e CB-08 bloqueantes)

---

## CBs Adicionadas por este Adendo

- **CB-06:** Apresentar evidência documental da determinação da CEO (e-mail, ata, comunicado formal). Sem evidência, Critério 4 permanece limitado a 5/10.
- **CB-07:** Aprovação formal da Diretoria da área solicitante (Diretoria de Logística Dedicada ou equivalente) — e-mail, ata ou documento assinado.
- **CB-08:** Aprovação formal do Gerente de TI da divisão solicitante (VIX Matriz / Holding DTI) — e-mail, ata ou documento assinado.

**CB-07 e CB-08 são pré-condições de validação**, não apenas condições de kickoff. O pipeline não deve avançar para documentação de iniciação sem que ambas estejam resolvidas.

---

## Quadro Consolidado de Condições Bloqueantes

| CB | Descrição | Origem | Prioridade |
|----|-----------|--------|------------|
| CB-01 | Sponsor formal (Diretor+) | Felipe Filtro | Alta |
| CB-02 | Aprovação orçamentária (revisão <R$10K → R$42–67K) | Felipe Filtro | Alta |
| CB-03 | Escopo detalhado anexado ao processo | Felipe Filtro | Alta |
| CB-04 | Prazo comprometido pela CEO declarado | Felipe Filtro | Alta |
| CB-05 | Responsável técnico nomeado no Projetos DTI | Felipe Filtro | Alta |
| CB-06 | Evidência documental da determinação da CEO | Adendo GP | Alta |
| CB-07 | Aprovação formal — Diretoria área solicitante | Adendo GP | **Bloqueante de validação** |
| CB-08 | Aprovação formal — Gerente de TI da divisão | Adendo GP | **Bloqueante de validação** |

---

*Adendo emitido por Gabriel Governança — Auditor de Governança VMO*
*Baseado em regras estabelecidas pelo GP VMO em 2026-05-24*
*Projeto: PROJ-2026-007 | Demanda: DEM-2026-007*
