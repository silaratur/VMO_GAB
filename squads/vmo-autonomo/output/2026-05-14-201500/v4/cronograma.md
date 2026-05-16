# Cronograma Detalhado + WBS
## PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação
## Grupo Águia Branca

**Versão:** 1.0
**Data:** 2026-05-14
**Responsável:** Carlos Cronograma — Especialista em Planejamento, VMO Autônomo
**Referências:** `v2/documentacao-base.md` (TAP/PM Canvas/Plano Geral) | `v3/requisitos.md` (ERF v3.0 — 37 RFs, 10 RNFs)

---

## 1. Premissas de Planejamento

| # | Premissa |
|---|---|
| PC-01 | Prazo final inegociável: **30 de novembro de 2026** (go-live em produção) |
| PC-02 | Início da execução: **16 de junho de 2026** (pós kick-off e confirmação de sponsor + orçamento) |
| PC-03 | Janela de execução efetiva: **16/06/2026 a 30/11/2026 = 24,5 semanas (≈ 172 dias corridos)** |
| PC-04 | Capacidade de execução: 2 desenvolvedores full stack (dedicação 100%), 1 tech lead (80%), 1 analista UX/Requisitos (80% até set/2026), 1 QA (80% a partir de out/2026) |
| PC-05 | Metodologia: ágil (sprints de 2 semanas); entrega por módulo funcional |
| PC-06 | Buffer de contingência de **15%** aplicado sobre a duração estimada bruta de cada fase de desenvolvimento |
| PC-07 | Dias úteis: segunda a sexta, excluindo feriados nacionais e municipais (ES) |
| PC-08 | Feriados relevantes no período: 07/09 (Independência), 12/10 (N.S. Aparecida), 02/11 (Finados), 15/11 (Proclamação) — total de 4 dias úteis a descontar |

---

## 2. WBS — Estrutura Analítica do Projeto

```
PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação
│
├── 1. INICIAÇÃO
│   ├── 1.1 Documentação de Iniciação (TAP, PM Canvas, Plano Geral) ✓ CONCLUÍDO
│   ├── 1.2 Especificação de Requisitos (ERF — 37 RFs, 10 RNFs)      ✓ CONCLUÍDO
│   ├── 1.3 Confirmação de Sponsor e Orçamento                        ← PENDENTE (bloqueante)
│   └── 1.4 Kick-off Oficial do Projeto
│
├── 2. PLANEJAMENTO DETALHADO
│   ├── 2.1 Levantamento Complementar de Requisitos (sessão com Jadson)
│   ├── 2.2 Prototipação de Interface (UX/UI — wireframes)
│   ├── 2.3 Backlog Priorizado e Estimado (story points / horas)
│   ├── 2.4 Definição de Arquitetura Técnica
│   └── 2.5 Setup de Ambiente (dev, homologação, CI/CD)
│
├── 3. EXECUÇÃO — MÓDULOS DE DESENVOLVIMENTO
│   ├── 3.1 MÓDULO M1 — Autenticação e Gestão de Usuários (RF001–RF006)
│   │   ├── 3.1.1 Desenvolvimento back-end (auth, RBAC, perfis)
│   │   ├── 3.1.2 Desenvolvimento front-end (login, cadastro, painel do usuário)
│   │   └── 3.1.3 Testes unitários e de integração
│   │
│   ├── 3.2 MÓDULO M2 — Portal de Ideias (RF007–RF014)
│   │   ├── 3.2.1 Formulário de submissão de ideias (problema, ganhos, benefícios)
│   │   ├── 3.2.2 Listagem, busca e filtro de ideias
│   │   ├── 3.2.3 Comentários e histórico de versões
│   │   └── 3.2.4 Testes unitários e de integração
│   │
│   ├── 3.3 MÓDULO M3 — Campanhas e Desafios (RF015–RF020)
│   │   ├── 3.3.1 Criação e publicação de campanhas pelo time de inovação
│   │   ├── 3.3.2 Vinculação de ideias a campanhas abertas
│   │   ├── 3.3.3 Visualização de campanhas pelos colaboradores
│   │   └── 3.3.4 Testes unitários e de integração
│   │
│   ├── 3.4 MÓDULO M4 — Fluxo de Aprovação Gerencial (RF021–RF027)
│   │   ├── 3.4.1 Workflow de aprovação/rejeição pelo gestor
│   │   ├── 3.4.2 Notificações e alertas para gestores e proponentes
│   │   ├── 3.4.3 Histórico de decisões e auditoria
│   │   └── 3.4.4 Testes unitários e de integração
│   │
│   ├── 3.5 MÓDULO M5 — Mini Gestão de Projetos (RF028–RF032)
│   │   ├── 3.5.1 Criação de projeto a partir de ideia aprovada
│   │   ├── 3.5.2 Gestão de tarefas e responsáveis
│   │   ├── 3.5.3 Acompanhamento de progresso e prazos
│   │   └── 3.5.4 Testes unitários e de integração
│   │
│   └── 3.6 MÓDULO M6 — Mensuração de Ganhos (RF033–RF037)
│       ├── 3.6.1 Registro de ganhos obtidos (financeiros e não-financeiros)
│       ├── 3.6.2 Dashboard de resultados por ideia/campanha
│       ├── 3.6.3 Exportação e relatórios
│       └── 3.6.4 Testes unitários e de integração
│
├── 4. INTEGRAÇÃO E TESTES SISTÊMICOS
│   ├── 4.1 Testes de integração entre módulos
│   ├── 4.2 Testes de performance e carga (500 usuários simultâneos)
│   ├── 4.3 Testes de segurança (HTTPS, RBAC, bcrypt, XSS/CSRF)
│   └── 4.4 Correção de defeitos pré-UAT
│
├── 5. UAT — TESTES DE ACEITAÇÃO DO USUÁRIO
│   ├── 5.1 Preparação do ambiente de UAT e casos de teste
│   ├── 5.2 Execução do UAT com time de inovação (Jadson + equipe)
│   ├── 5.3 Registro e priorização de defeitos identificados
│   └── 5.4 Aprovação formal do UAT (meta: ≥ 80% dos casos aprovados)
│
├── 6. IMPLANTAÇÃO
│   ├── 6.1 Setup do ambiente de produção (TI do Grupo)
│   ├── 6.2 Correções pós-UAT e release final
│   ├── 6.3 Deploy em produção + smoke tests
│   ├── 6.4 Treinamento de administradores e time de inovação
│   └── 6.5 Go-live e comunicado interno
│
└── 7. ENCERRAMENTO
    ├── 7.1 Documentação técnica e manual do usuário
    ├── 7.2 Relatório final do projeto
    ├── 7.3 Lições aprendidas
    └── 7.4 Encerramento formal + aceite do cliente
```

---

## 3. Cronograma Detalhado por Fase

### Cálculo do Buffer de 15%

> A duração estimada bruta de cada fase de desenvolvimento foi calculada com base na complexidade dos módulos (nº de RFs, interdependências) e na capacidade da equipe. O buffer de 15% é aplicado sobre a duração bruta de cada fase de desenvolvimento (fases 3.1 a 3.6), arredondado para cima em dias.

| Fase | Duração Bruta (dias úteis) | Buffer 15% | Duração Final (dias úteis) |
|---|---|---|---|
| Planejamento Detalhado | 10 | — | 10 |
| M1 — Auth e Usuários | 10 | +2 | 12 |
| M2 — Portal de Ideias | 12 | +2 | 14 |
| M3 — Campanhas | 8 | +2 | 10 |
| M4 — Aprovação Gerencial | 12 | +2 | 14 |
| M5 — Gestão de Projetos | 10 | +2 | 12 |
| M6 — Mensuração de Ganhos | 8 | +2 | 10 |
| Integração e Testes Sistêmicos | 8 | — | 8 |
| UAT | 10 | — | 10 |
| Implantação e Go-live | 10 | — | 10 |
| **Total de dias úteis** | **98** | **+12** | **110** |

> Janela disponível (16/06 a 30/11/2026): ≈ 120 dias úteis (descontando 4 feriados).
> Folga real após cronograma: **~10 dias úteis** — margem operacional para absorver imprevistos menores.

---

### 3.1 Fase 1 — Iniciação (em andamento / pré-execução)

| ID | Entrega | Início | Fim | Responsável | Status |
|---|---|---|---|---|---|
| 1.1 | TAP, PM Canvas, Plano Geral | 2026-05-14 | 2026-05-14 | Diana Documento | ✅ Concluído |
| 1.2 | ERF — Especificação de Requisitos | 2026-05-14 | 2026-05-14 | Rafael Requisito | ✅ Concluído |
| 1.3 | Confirmação de Sponsor + Orçamento | 2026-05-15 | 2026-06-13 | Jadson + Sponsor | ⚠️ Pendente — BLOQUEANTE |
| 1.4 | Kick-off Oficial | 2026-06-16 | 2026-06-16 | GP + Todos stakeholders | 🔲 Aguardando 1.3 |

**Marco M-01:** Kick-off — **16/06/2026** (condicional à aprovação do sponsor e orçamento até 13/06)

---

### 3.2 Fase 2 — Planejamento Detalhado

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 2.1 | Levantamento complementar de requisitos (sessão Jadson) | 16/06/2026 | 17/06/2026 | 2 | Analista UX + Jadson | Kick-off |
| 2.2 | Prototipação UX/UI — wireframes dos 6 módulos | 18/06/2026 | 24/06/2026 | 5 | Analista UX | 2.1 |
| 2.3 | Backlog priorizado e estimado | 18/06/2026 | 23/06/2026 | 4 | Tech Lead + Analista | 2.1 |
| 2.4 | Arquitetura técnica definida | 18/06/2026 | 20/06/2026 | 3 | Tech Lead | 2.1 |
| 2.5 | Setup de ambientes (dev + homolog + CI/CD) | 23/06/2026 | 30/06/2026 | 6 | Tech Lead + TI Grupo | 2.4 |

**Marco M-02:** Planejamento concluído — **30/06/2026**

---

### 3.3 Fase 3 — Execução por Módulos

#### Sprint 1 — M1 Autenticação + M2 Portal de Ideias (MVP)

**Objetivo do Sprint:** Plataforma base com acesso de usuários e submissão de ideias funcionando — MVP demonstrável.

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 3.1.1 | Back-end: auth, RBAC, gestão de perfis (RF001–006) | 01/07/2026 | 16/07/2026 | 12 | Dev Backend | Setup ambiente |
| 3.1.2 | Front-end: login, cadastro, painel do usuário | 01/07/2026 | 14/07/2026 | 10 | Dev Frontend | Setup ambiente |
| 3.1.3 | Testes M1 (unitários + integração) | 17/07/2026 | 20/07/2026 | 2 | QA / Dev | 3.1.1 + 3.1.2 |
| 3.2.1 | Formulário de submissão de ideias (RF007–010) | 15/07/2026 | 28/07/2026 | 10 | Dev Backend + Frontend | 3.1.1 |
| 3.2.2 | Listagem, busca e filtro de ideias (RF011–013) | 21/07/2026 | 31/07/2026 | 8 | Dev Frontend | 3.2.1 (parcial) |
| 3.2.3 | Comentários e histórico (RF014) | 01/08/2026 | 05/08/2026 | 4 | Dev | 3.2.1 |
| 3.2.4 | Testes M2 (unitários + integração) | 06/08/2026 | 11/08/2026 | 4 | QA / Dev | 3.2.x |

**Marco M-03:** MVP (M1 + M2) em homologação — **11/08/2026**
**Review Sprint 1:** **12/08/2026** — Demonstração para Jadson e time de inovação

---

#### Sprint 2 — M3 Campanhas + M4 Fluxo de Aprovação

**Objetivo do Sprint:** Funcionalidades de gestão de campanhas e workflow completo de aprovação gerencial.

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 3.3.1 | Criação e publicação de campanhas pelo time de inovação (RF015–018) | 13/08/2026 | 25/08/2026 | 9 | Dev Backend + Frontend | M1 pronto |
| 3.3.2 | Vinculação de ideias a campanhas (RF019) | 26/08/2026 | 28/08/2026 | 3 | Dev | 3.3.1 |
| 3.3.3 | Visualização de campanhas pelos colaboradores (RF020) | 26/08/2026 | 28/08/2026 | 3 | Dev Frontend | 3.3.1 |
| 3.3.4 | Testes M3 | 01/09/2026 | 02/09/2026 | 2 | QA / Dev | 3.3.x |
| 3.4.1 | Workflow de aprovação/rejeição pelo gestor (RF021–024) | 13/08/2026 | 01/09/2026 | 14 | Dev Backend + Frontend | M2 pronto |
| 3.4.2 | Notificações e alertas (RF025) | 02/09/2026 | 08/09/2026 | 5 | Dev | 3.4.1 |
| 3.4.3 | Histórico e auditoria (RF026–027) | 02/09/2026 | 05/09/2026 | 4 | Dev Backend | 3.4.1 |
| 3.4.4 | Testes M4 | 09/09/2026 | 12/09/2026 | 4 | QA / Dev | 3.4.x |

> **Feriado:** 07/09 (Independência) — desconsiderado no calendário acima.

**Marco M-04:** M3 + M4 em homologação — **12/09/2026**
**Review Sprint 2:** **15/09/2026** — Demonstração do fluxo completo de aprovação para Jadson

---

#### Sprint 3 — M5 Mini Gestão de Projetos + M6 Mensuração de Ganhos

**Objetivo do Sprint:** Completar a plataforma com os módulos de acompanhamento de implementação e mensuração de resultados.

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 3.5.1 | Criação de projeto a partir de ideia aprovada (RF028–029) | 16/09/2026 | 25/09/2026 | 8 | Dev Backend + Frontend | M4 pronto |
| 3.5.2 | Gestão de tarefas e responsáveis (RF030) | 26/09/2026 | 01/10/2026 | 4 | Dev | 3.5.1 |
| 3.5.3 | Acompanhamento de progresso e prazos (RF031–032) | 02/10/2026 | 08/10/2026 | 5 | Dev | 3.5.2 |
| 3.5.4 | Testes M5 | 09/10/2026 | 12/10/2026 | 2 | QA / Dev | 3.5.x |
| 3.6.1 | Registro de ganhos — financeiros e não-financeiros (RF033–034) | 01/10/2026 | 14/10/2026 | 10 | Dev Backend | M5 (parcial) |
| 3.6.2 | Dashboard de resultados (RF035–036) | 15/10/2026 | 22/10/2026 | 6 | Dev Frontend | 3.6.1 |
| 3.6.3 | Exportação e relatórios (RF037) | 15/10/2026 | 20/10/2026 | 4 | Dev | 3.6.1 |
| 3.6.4 | Testes M6 | 23/10/2026 | 27/10/2026 | 3 | QA / Dev | 3.6.x |

> **Feriados:** 12/10 (N.S. Aparecida) — desconsiderado no calendário acima.

**Marco M-05:** Todos os módulos (M1–M6) integrados e em homologação — **27/10/2026**
**Review Sprint 3:** **28/10/2026** — Demonstração completa da plataforma para Jadson e time de inovação

---

### 3.4 Fase 4 — Integração e Testes Sistêmicos

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 4.1 | Testes de integração entre todos os módulos | 29/10/2026 | 31/10/2026 | 3 | QA + Dev | Sprint 3 concluído |
| 4.2 | Testes de performance e carga (500 usuários simultâneos) | 29/10/2026 | 31/10/2026 | 3 | QA + TI Grupo | Ambiente de homolog. |
| 4.3 | Testes de segurança (HTTPS, RBAC, bcrypt, XSS/CSRF) | 29/10/2026 | 31/10/2026 | 3 | QA + Tech Lead | 4.1 |
| 4.4 | Correção de defeitos pré-UAT (P1 e P2) | 03/11/2026 | 07/11/2026 | 5 | Dev | 4.1–4.3 |

> **Feriados:** 02/11 (Finados) — desconsiderado no calendário acima.

**Marco M-06:** Plataforma liberada para UAT — **07/11/2026**

---

### 3.5 Fase 5 — UAT (Testes de Aceitação do Usuário)

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 5.1 | Preparação: ambiente UAT, roteiro e casos de teste | 07/11/2026 | 07/11/2026 | 1 | GP + QA | M-06 |
| 5.2 | Execução do UAT com Jadson e time de inovação | 10/11/2026 | 13/11/2026 | 4 | Jadson + Time Inovação + QA | 5.1 |
| 5.3 | Registro e priorização de defeitos identificados | 10/11/2026 | 14/11/2026 | 5 | QA + Dev | 5.2 |
| 5.4 | Aprovação formal do UAT (aceite ≥ 80% dos casos) | 14/11/2026 | 14/11/2026 | 1 | Jadson | 5.2 + 5.3 |

**Marco M-07:** UAT aprovado — **14/11/2026** *(meta: ≥ 80% dos casos de teste aprovados; todos os críticos aprovados)*

---

### 3.6 Fase 6 — Implantação e Go-live

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 6.1 | Setup do ambiente de produção | 10/11/2026 | 14/11/2026 | 5 | TI Grupo Águia Branca | Aprovação de infra |
| 6.2 | Correções pós-UAT (defeitos P1/P2 encontrados no UAT) | 17/11/2026 | 21/11/2026 | 5 | Dev | UAT aprovado |
| 6.3 | Deploy em produção + smoke tests | 24/11/2026 | 25/11/2026 | 2 | Tech Lead + TI Grupo | 6.2 |
| 6.4 | Treinamento de administradores e time de inovação | 26/11/2026 | 27/11/2026 | 2 | GP + Tech Lead | 6.3 |
| 6.5 | Go-live + comunicado interno | **28/11/2026** | **28/11/2026** | 1 | GP + Jadson | 6.3 + 6.4 |

> **Feriado:** 15/11 (Proclamação da República) — desconsiderado no calendário acima.
> Go-live em **28/11/2026** — 2 dias antes do prazo limite de 30/11/2026 (margem de segurança final).

**Marco M-08 (CRÍTICO):** Go-live em produção — **28/11/2026** *(prazo máximo: 30/11/2026)*

---

### 3.7 Fase 7 — Encerramento

| ID | Entrega | Início | Fim | Duração (d.u.) | Responsável | Dependência |
|---|---|---|---|---|---|---|
| 7.1 | Documentação técnica e manual do usuário | 01/12/2026 | 05/12/2026 | 5 | Tech Lead + Analista | Go-live |
| 7.2 | Relatório final do projeto | 07/12/2026 | 09/12/2026 | 3 | GP | 7.1 |
| 7.3 | Sessão de lições aprendidas | 10/12/2026 | 10/12/2026 | 1 | GP + Equipe | 7.2 |
| 7.4 | Encerramento formal e aceite do cliente | 12/12/2026 | 15/12/2026 | 2 | GP + Jadson + Sponsor | 7.3 |

**Marco M-09:** Encerramento formal — **15/12/2026**

---

## 4. Resumo de Marcos

| Marco | Descrição | Data Prevista | Status |
|---|---|---|---|
| M-00 | Emissão do TAP e documentação base | 2026-05-14 | ✅ Concluído |
| M-01 | Sponsor confirmado + orçamento aprovado | **2026-06-13** | ⚠️ BLOQUEANTE |
| M-02 | Kick-off oficial do projeto | **2026-06-16** | 🔲 Aguardando M-01 |
| M-03 | Planejamento detalhado concluído | **2026-06-30** | 🔲 |
| M-04 | MVP (M1 + M2) em homologação | **2026-08-11** | 🔲 |
| M-05 | M3 + M4 (Campanhas + Aprovação) em homologação | **2026-09-12** | 🔲 |
| M-06 | M5 + M6 (Projetos + Mensuração) + integração | **2026-10-27** | 🔲 |
| M-07 | Plataforma liberada para UAT | **2026-11-07** | 🔲 |
| M-08 | UAT aprovado | **2026-11-14** | 🔲 |
| **M-09** | **Go-live em produção** | **2026-11-28** | 🔲 **(CRÍTICO — limite: 30/11)** |
| M-10 | Encerramento formal do projeto | **2026-12-15** | 🔲 |

---

## 5. Caminho Crítico

O caminho crítico passa pelas seguintes entregas — qualquer atraso nesta sequência impacta diretamente o go-live:

```
M-01 (Sponsor/Orçamento)
  → Kick-off (16/06)
    → Setup de ambiente (→ 30/06)
      → M1: Auth e Usuários (→ 20/07)
        → M2: Portal de Ideias (→ 11/08)
          → M4: Fluxo de Aprovação (→ 12/09)
            → M5: Gestão de Projetos (→ 27/10)
              → Integração + Testes Sistêmicos (→ 07/11)
                → UAT (→ 14/11)
                  → Correções pós-UAT (→ 21/11)
                    → Deploy em Produção (→ 28/11)
                      → GO-LIVE ✓
```

**Observação:** M3 (Campanhas) e M6 (Mensuração de Ganhos) não estão no caminho crítico — podem sofrer pequenos atrasos sem impactar o go-live, desde que concluídos antes do início dos testes sistêmicos.

---

## 6. Análise de Folga por Módulo

| Módulo | No Caminho Crítico | Folga Total Disponível |
|---|---|---|
| M1 — Auth e Usuários | Sim | 0 dias |
| M2 — Portal de Ideias | Sim | 0 dias |
| M3 — Campanhas | **Não** | **~5 dias úteis** |
| M4 — Aprovação Gerencial | Sim | 0 dias |
| M5 — Gestão de Projetos | Sim | 0 dias |
| M6 — Mensuração de Ganhos | **Não** | **~3 dias úteis** |
| UAT | Sim | 0 dias |

---

## 7. Alertas e Pontos de Atenção

| # | Alerta | Severidade | Ação Preventiva |
|---|---|---|---|
| A-01 | **Sponsor não confirmado** — bloqueia o início do projeto | 🔴 Crítica | Jadson deve confirmar sponsor até 13/06/2026; GP escalará caso não ocorra |
| A-02 | **Prazo de go-live não tem margem de erro no caminho crítico** | 🔴 Crítica | Atraso de mais de 2 semanas em qualquer marco crítico exige revisão formal do plano com sponsor |
| A-03 | Modelo de execução (equipe) ainda indefinido | 🟠 Alta | Definição necessária até kick-off; afeta diretamente as estimativas de duração |
| A-04 | Setup de ambiente de produção depende da TI do Grupo (externo ao controle da VMO) | 🟠 Alta | Solicitar provisionamento em kickoff; validar disponibilidade de ambiente em setembro |
| A-05 | UAT com apenas 4 dias — risco de volume de defeitos exceder capacidade de correção antes do go-live | 🟡 Média | Realizar validações parciais ao final de cada sprint para reduzir surpresas no UAT formal |
| A-06 | Dois feriados em novembro (02/11 e 15/11) impactam as fases mais críticas do projeto | 🟡 Média | Já descontados do calendário; equipe deve manter ritmo nas semanas adjacentes |

---

## 8. Cronograma Visual — Linha do Tempo

```
Mai/26                Jun/26             Jul/26           Ago/26
|---INICIAÇÃO---------|---PLANEJ.---------|---SPRINT 1-----|
  TAP+ERF concluídos    Kick-off: 16/06    M1+M2           MVP: 11/08

Set/26              Out/26             Nov/26            Dez/26
|---SPRINT 2---------|---SPRINT 3--------|---UAT/IMPL.----|-ENCER.-|
  M3+M4: 12/09         M5+M6+Integ:27/10  UAT:14/11        Enc.:15/12
                                          Go-live: 28/11
```

---

*Documento gerado por Carlos Cronograma — Especialista em Planejamento | VMO Autônomo v1.0 | 2026-05-14*
*PROJ-2026-004 | Versão 1.0 | 2026-05-14*
