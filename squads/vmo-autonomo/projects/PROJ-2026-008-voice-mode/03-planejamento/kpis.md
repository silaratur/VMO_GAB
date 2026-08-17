# Framework de KPIs — Estudo de Viabilidade Voice Mode

**Projeto:** PROJ-2026-008-voice-mode
**Data:** 17/08/2026
**Analista:** Marcela Métrica
**Versão:** 1.0

---

## KPIs do Projeto

### 1. Performance de Prazo (SPI)

| Campo | Valor |
|---|---|
| **Indicador** | Schedule Performance Index |
| **Fórmula** | EV / PV (Earned Value / Planned Value) |
| **Baseline** | SPI = 1.0 |
| **Frequência** | Diária (projeto de 2 dias) |
| **Responsável** | Neemias Buceli |
| **Limites** | 🟢 ≥ 0,95 | 🟡 0,85-0,95 | 🔴 < 0,85 |

### 2. Performance de Custo (CPI)

| Campo | Valor |
|---|---|
| **Indicador** | Cost Performance Index |
| **Fórmula** | EV / AC (Earned Value / Actual Cost) |
| **Baseline** | CPI = 1.0 |
| **Frequência** | Ao final do projeto |
| **Responsável** | Neemias Buceli |
| **Limites** | 🟢 ≥ 0,95 | 🟡 0,85-0,95 | 🔴 < 0,85 |

### 3. Cobertura de Critérios

| Campo | Valor |
|---|---|
| **Indicador** | % de critérios avaliados |
| **Fórmula** | Critérios avaliados / 7 × 100 |
| **Meta** | 100% (7/7) |
| **Frequência** | Ao final da análise |
| **Responsável** | Analista Data AI |
| **Limites** | 🟢 100% | 🟡 85-99% (6/7) | 🔴 < 85% (≤5/7) |

### 4. Qualidade da Análise

| Campo | Valor |
|---|---|
| **Indicador** | % de critérios com evidência documentada |
| **Fórmula** | Critérios com fonte verificável / total de critérios × 100 |
| **Meta** | ≥ 80% |
| **Frequência** | Na revisão de qualidade |
| **Responsável** | Vera Veredito |
| **Limites** | 🟢 ≥ 80% | 🟡 60-79% | 🔴 < 60% |

### 5. Satisfação do Solicitante

| Campo | Valor |
|---|---|
| **Indicador** | Aprovação do estudo pelo solicitante |
| **Fórmula** | Aprovação formal (SIM/NÃO) |
| **Meta** | Aprovação formal |
| **Frequência** | Na entrega |
| **Responsável** | Neemias Buceli |
| **Limites** | 🟢 Aprovado | 🟡 Aprovado com ressalvas | 🔴 Reprovado |

---

## Dashboard de Saúde

| Dimensão | Indicador | Status Atual | Semáforo |
|---|---|---|---|
| Prazo | SPI | 1.0 (no baseline) | 🟢 |
| Custo | CPI | 1.0 (no baseline) | 🟢 |
| Escopo | Mudanças de escopo | 0 mudanças | 🟢 |
| Qualidade | Cobertura de critérios | Em andamento | 🟡 |
| Riscos | RSK-001 (prazo) ativo | 1 risco crítico | 🟡 |

---

## Vinculação com Critérios de Sucesso (TAP)

| Critério de Sucesso | KPI Vinculado |
|---|---|
| CS1 — Estudo entregue no prazo | SPI (KPI 1) |
| CS2 — 7 critérios avaliados | Cobertura de Critérios (KPI 3) |
| CS3 — Recomendação incluída | Qualidade da Análise (KPI 4) |
| CS4 — Stakeholders satisfeitos | Satisfação do Solicitante (KPI 5) |
| CS5 — Decisão viabilizada | Satisfação + Cobertura (KPI 5 + 3) |
