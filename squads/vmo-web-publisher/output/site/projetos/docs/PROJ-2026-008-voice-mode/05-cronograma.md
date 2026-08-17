# WBS + Cronograma — Estudo de Viabilidade Voice Mode

**Projeto:** PROJ-2026-008-voice-mode
**Data:** 17/08/2026
**Analista:** Carlos Cronograma
**Versão:** 1.0

---

## WBS — Estrutura Analítica do Projeto

```
1. Estudo de Viabilidade Voice Mode Multiagente
├── 1.1 Levantamento
│   ├── 1.1.1 Pesquisa técnica Fireflies (funcionalidades, API, custos)
│   ├── 1.1.2 Pesquisa técnica Microsoft Teams/Copilot Studio (roadmap, Voice Mode)
│   ├── 1.1.3 Pesquisa técnica Azure Telefonia (Central, números, custos)
│   └── 1.1.4 Levantamento de requisitos LGPD e políticas internas
├── 1.2 Análise Comparativa
│   ├── 1.2.1 Avaliação de custo (TCO por solução)
│   ├── 1.2.2 Avaliação de prazo (disponibilidade de Voice Mode)
│   ├── 1.2.3 Avaliação de capacidades técnicas
│   ├── 1.2.4 Avaliação de governança
│   ├── 1.2.5 Avaliação de risco
│   ├── 1.2.6 Avaliação de segurança
│   └── 1.2.7 Avaliação de conformidade LGPD
├── 1.3 Elaboração do Estudo
│   ├── 1.3.1 Matriz de prós e contras
│   ├── 1.3.2 Matriz de decisão ponderada
│   ├── 1.3.3 Recomendação fundamentada
│   └── 1.3.4 Resumo executivo
└── 1.4 Validação e Entrega
    ├── 1.4.1 Revisão interna
    ├── 1.4.2 Validação com solicitante
    └── 1.4.3 Entrega formal
```

---

## Cronograma Detalhado

| ID | Atividade | Responsável | Início | Fim | Duração | Dependência |
|---|---|---|---|---|---|---|
| 1.1.1 | Pesquisa técnica Fireflies | Analista Data AI | 17/08 08:00 | 17/08 12:00 | 4h | — |
| 1.1.2 | Pesquisa técnica Microsoft Teams | Analista Data AI | 17/08 08:00 | 17/08 14:00 | 6h | — |
| 1.1.3 | Pesquisa técnica Azure Telefonia | Analista Data AI | 17/08 13:00 | 17/08 17:00 | 4h | — |
| 1.1.4 | Levantamento LGPD | Analista Data AI | 17/08 14:00 | 17/08 17:00 | 3h | — |
| 1.2.1-7 | Análise comparativa (7 critérios) | Analista Data AI | 17/08 17:00 | 18/08 10:00 | 8h | 1.1.1-4 |
| 1.3.1 | Matriz de prós e contras | Analista Data AI | 18/08 10:00 | 18/08 12:00 | 2h | 1.2 |
| 1.3.2 | Matriz de decisão ponderada | Analista Data AI | 18/08 12:00 | 18/08 13:00 | 1h | 1.3.1 |
| 1.3.3 | Recomendação fundamentada | Analista Data AI | 18/08 13:00 | 18/08 15:00 | 2h | 1.3.2 |
| 1.3.4 | Resumo executivo | Analista Data AI | 18/08 15:00 | 18/08 16:00 | 1h | 1.3.3 |
| 1.4.1 | Revisão interna | Analista Data AI | 18/08 16:00 | 18/08 17:00 | 1h | 1.3.4 |
| 1.4.2 | Validação com solicitante | Neemias Buceli | 18/08 17:00 | 18/08 18:00 | 1h | 1.4.1 |
| 1.4.3 | Entrega formal | Analista Data AI | 18/08 18:00 | 18/08 18:00 | 0h | 1.4.2 |

---

## Marcos Principais

| Marco | Data | Status |
|---|---|---|
| **M1 — Início do projeto** | 17/08/2026 | ✅ Concluído |
| **M2 — Levantamento técnico concluído** | 17/08/2026 17:00 | ⏳ Em andamento |
| **M3 — Análise comparativa concluída** | 18/08/2026 10:00 | 🔲 Pendente |
| **M4 — Estudo elaborado** | 18/08/2026 16:00 | 🔲 Pendente |
| **M5 — Entrega formal** | 18/08/2026 18:00 | 🔲 Pendente |

---

## Caminho Crítico

```
1.1.2 (Pesquisa Microsoft) → 1.2 (Análise Comparativa) → 1.3.1 (Matriz) → 1.3.2 (Decisão) → 1.3.3 (Recomendação) → 1.3.4 (Resumo) → 1.4.1 (Revisão) → 1.4.2 (Validação) → 1.4.3 (Entrega)
```

**Duração do caminho crítico:** ~22h (de 17/08 08:00 a 18/08 18:00)
**Buffer disponível:** 0h — prazo apertado, sem margem para atraso.

---

## Baseline

| Dimensão | Valor Baseline |
|---|---|
| **Prazo** | 17/08/2026 — 18/08/2026 (2 dias) |
| **Esforço** | 64-96h (cenário otimista — pessimista) |
| **Custo** | Custo interno de pessoal |
