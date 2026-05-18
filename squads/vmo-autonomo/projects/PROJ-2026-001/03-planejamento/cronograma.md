# CRONOGRAMA — PROJ-2026-001
## Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados
**Versão:** 1.0 | **Data:** 2026-04-03 | **Gerado por:** Carlos Cronograma — Planejador de Prazo

---

## WBS — Estrutura Analítica do Projeto

```
1.0 PROJ-2026-001 — Inclusão de Aprovador SAP FI
  │
  ├─ 1.1 Gerenciamento do Projeto
  │    ├─ 1.1.1 Elaboração e aprovação do TAP
  │    ├─ 1.1.2 Designação do Gerente de Projeto e kickoff
  │    ├─ 1.1.3 Status reports quinzenais (3 ciclos)
  │    └─ 1.1.4 Encerramento, aceite formal e lições aprendidas
  │
  ├─ 1.2 Planejamento Técnico
  │    ├─ 1.2.1 Análise técnica (spike)
  │    │    ├─ 1.2.1.1 Verificar parametrização ZFI0057 no ambiente DEV
  │    │    └─ 1.2.1.2 Confirmar viabilidade sem ABAP — relatório técnico
  │    ├─ 1.2.2 Mapeamento de stakeholders e fluxo atual
  │    │    ├─ 1.2.2.1 Identificar aprovadores existentes no fluxo ZFI0057
  │    │    └─ 1.2.2.2 Confirmar nome/ID SAP do Diretor Financeiro
  │    └─ 1.2.3 Planejamento detalhado e reserva de janela QAS
  │
  ├─ 1.3 Parametrização e Testes em DEV
  │    ├─ 1.3.1 Parametrização em DEV (ZFI0057 + SBWP)
  │    │    ├─ 1.3.1.1 Incluir Diretor Financeiro como aprovador na ZFI0057
  │    │    └─ 1.3.1.2 Configurar roteamento de tarefa no SBWP
  │    ├─ 1.3.2 Testes unitários em DEV
  │    │    ├─ 1.3.2.1 Testar submissão → aprovação pelo Diretor Financeiro
  │    │    └─ 1.3.2.2 Testar cenário de rejeição e roteamento de exceções
  │    └─ 1.3.3 Transporte DEV → QAS
  │
  ├─ 1.4 Testes Integrados em QAS
  │    ├─ 1.4.1 Preparação do ambiente QAS
  │    │    └─ 1.4.1.1 Validar transporte e ajustar perfis de acesso em QAS
  │    ├─ 1.4.2 Execução de testes integrados
  │    │    ├─ 1.4.2.1 Casos de teste: lançamento → fila SBWP Diretor
  │    │    ├─ 1.4.2.2 Casos de teste: aprovação, rejeição e retorno
  │    │    └─ 1.4.2.3 Validação com Ivanilde Ribeiro Machado (UAT)
  │    └─ 1.4.3 Correções e revalidação
  │         └─ 1.4.3.1 Ajustes pós-teste e reteste (se necessário)
  │
  ├─ 1.5 Go-Live (PRD)
  │    ├─ 1.5.1 Treinamento do aprovador
  │    │    ├─ 1.5.1.1 Elaborar guia do aprovador (SBWP)
  │    │    └─ 1.5.1.2 Sessão de treinamento com o Diretor Financeiro
  │    ├─ 1.5.2 Transporte QAS → PRD
  │    │    ├─ 1.5.2.1 Solicitar janela de transporte (change management)
  │    │    └─ 1.5.2.2 Executar transporte e validar em PRD
  │    └─ 1.5.3 Comunicação aos usuários
  │         └─ 1.5.3.1 Notificar usuários do fluxo sobre nova etapa de aprovação
  │
  └─ 1.6 Acompanhamento Pós Go-Live
       ├─ 1.6.1 Monitoramento operacional (10 du)
       │    ├─ 1.6.1.1 Monitorar fila SBWP do Diretor Financeiro
       │    └─ 1.6.1.2 Confirmar ausência de bypass nos lançamentos
       ├─ 1.6.2 Coleta de evidências de sucesso
       │    └─ 1.6.2.1 Extrair relatório de lançamentos com aprovação do Diretor
       └─ 1.6.3 Encerramento formal
            └─ 1.6.3.1 Aceite do Sponsor + documentação final
```

---

## Dicionário da WBS (Entregáveis Críticos)

| ID | Entregável | Critério de Conclusão |
|----|------------|-----------------------|
| 1.2.1.2 | Relatório técnico de viabilidade | Doc confirmando ZFI0057 suporta novo aprovador sem ABAP, assinado pelo técnico Basis |
| 1.3.1.1 | Aprovador parametrizado em DEV | ZFI0057 em DEV mostra Diretor Financeiro como aprovador ativo |
| 1.4.2.3 | UAT validado pela solicitante | E-mail ou ata de Ivanilde confirmando testes satisfatórios em QAS |
| 1.5.1.2 | Treinamento concluído | Aceite formal ou e-mail do Diretor Financeiro confirmando capacitação |
| 1.5.2.2 | Go-live PRD | Transação SAP PRD com aprovador ativo; primeiro lançamento real aprovado |
| 1.6.2.1 | Evidência de cobertura | Relatório SAP com 100% dos lançamentos pré-editados com step do Diretor |

---

## Cronograma por Fase

> **Referência:** Du 1 = data de assinatura do TAP. Todas as durações em dias úteis (du).
> **Premissa de disponibilidade:** Equipe Basis estimada a 70% (projetos SAP concorrentes).

### Fase 1.1 — Iniciação (Du 1–5)

| ID | Atividade | Início | Fim | Dur | Dep | Responsável | ⭐ |
|----|-----------|--------|-----|-----|-----|-------------|-----|
| 1.1.1 | Aprovação do TAP e designação do GP | Du 1 | Du 2 | 2du | — | PMO / Sponsor | ⭐ |
| 1.1.2 | Kickoff com DTI e solicitante | Du 3 | Du 5 | 3du | 1.1.1 | GP | ⭐ |

### Fase 1.2 — Planejamento Técnico (Du 6–15)

| ID | Atividade | Início | Fim | Dur | Dep | Responsável | ⭐ |
|----|-----------|--------|-----|-----|-----|-------------|-----|
| 1.2.1.1 | Verificar ZFI0057 em DEV | Du 6 | Du 8 | 3du | 1.1.2 | Basis SAP | ⭐ |
| 1.2.1.2 | Relatório técnico de viabilidade | Du 9 | Du 10 | 2du | 1.2.1.1 | Basis SAP | ⭐ |
| 1.2.2.1 | Mapear aprovadores existentes no fluxo | Du 6 | Du 8 | 3du | 1.1.2 | GP + Negócio | — |
| 1.2.2.2 | Confirmar nome/ID SAP do Diretor Financeiro | Du 6 | Du 7 | 2du | 1.1.2 | GP | ⭐ |
| 1.2.3 | Plano detalhado + reserva de janela QAS | Du 11 | Du 15 | 5du | 1.2.1.2 | GP | ⭐ |

### Fase 1.3 — Parametrização DEV (Du 16–30)

| ID | Atividade | Início | Fim | Dur | Dep | Responsável | ⭐ |
|----|-----------|--------|-----|-----|-----|-------------|-----|
| 1.3.1.1 | Parametrizar Diretor Financeiro na ZFI0057 (DEV) | Du 16 | Du 19 | 4du | 1.2.3 | Basis SAP | ⭐ |
| 1.3.1.2 | Configurar roteamento SBWP (DEV) | Du 20 | Du 23 | 4du | 1.3.1.1 | Basis SAP | ⭐ |
| 1.3.2.1 | Teste unitário: aprovação normal | Du 24 | Du 26 | 3du | 1.3.1.2 | Basis + Func | ⭐ |
| 1.3.2.2 | Teste unitário: rejeição e exceções | Du 27 | Du 28 | 2du | 1.3.2.1 | Basis + Func | — |
| 1.3.3 | Transporte DEV → QAS | Du 29 | Du 30 | 2du | 1.3.2.1 | Basis SAP | ⭐ |

### Fase 1.4 — Testes Integrados QAS (Du 31–42)

| ID | Atividade | Início | Fim | Dur | Dep | Responsável | ⭐ |
|----|-----------|--------|-----|-----|-----|-------------|-----|
| 1.4.1.1 | Validar transporte e perfis QAS | Du 31 | Du 32 | 2du | 1.3.3 | Basis SAP | ⭐ |
| 1.4.2.1 | Testes: lançamento → fila SBWP Diretor | Du 33 | Du 35 | 3du | 1.4.1.1 | Func SAP | ⭐ |
| 1.4.2.2 | Testes: aprovação, rejeição, retorno | Du 36 | Du 38 | 3du | 1.4.2.1 | Func SAP | ⭐ |
| 1.4.2.3 | Validação com solicitante (UAT) | Du 39 | Du 40 | 2du | 1.4.2.2 | GP + Ivanilde | ⭐ |
| 1.4.3.1 | Ajustes pós-teste e reteste (se necessário) | Du 41 | Du 42 | 2du | 1.4.2.3 | Basis SAP | — |

### Fase 1.5 — Go-Live PRD (Du 43–47)

| ID | Atividade | Início | Fim | Dur | Dep | Responsável | ⭐ |
|----|-----------|--------|-----|-----|-----|-------------|-----|
| 1.5.1.1 | Elaborar guia do aprovador | Du 39 | Du 41 | 3du | 1.4.2.2 | GP / Func | — |
| 1.5.1.2 | Treinamento do Diretor Financeiro | Du 43 | Du 44 | 2du | 1.4.2.3 | GP | ⭐ |
| 1.5.2.1 | Solicitar janela de transporte PRD | Du 40 | Du 42 | 3du | 1.4.2.3 | GP | — |
| 1.5.2.2 | Executar transporte QAS → PRD + validar | Du 45 | Du 46 | 2du | 1.5.1.2 | Basis SAP | ⭐ |
| 1.5.3.1 | Comunicar usuários do fluxo | Du 47 | Du 47 | 1du | 1.5.2.2 | GP | — |

### Fase 1.6 — Acompanhamento Pós Go-Live (Du 48–52)

| ID | Atividade | Início | Fim | Dur | Dep | Responsável | ⭐ |
|----|-----------|--------|-----|-----|-----|-------------|-----|
| 1.6.1.1 | Monitorar fila SBWP do Diretor (semanas 1–2) | Du 48 | Du 51 | 4du | 1.5.2.2 | GP + DTI | ⭐ |
| 1.6.1.2 | Confirmar ausência de bypass | Du 48 | Du 51 | 4du | 1.5.2.2 | Func SAP | ⭐ |
| 1.6.2.1 | Extrair relatório de cobertura | Du 52 | Du 52 | 1du | 1.6.1.2 | Func SAP | ⭐ |
| 1.6.3.1 | Aceite formal do Sponsor + encerramento | Du 52 | Du 52 | 1du | 1.6.2.1 | GP / Sponsor | ⭐ |

---

## Marcos Principais

| Marco | Du | Critério |
|-------|----|---------|
| M0 — TAP aprovado | Du 2 | TAP assinado pelo Sponsor e PMO |
| M1 — Kick-off | Du 5 | Reunião realizada, equipe mobilizada |
| M2 — Viabilidade técnica confirmada | Du 10 | Relatório Basis: sem ABAP necessário |
| M3 — Parametrização DEV concluída | Du 28 | Testes unitários aprovados em DEV |
| M4 — UAT aprovado em QAS | Du 40 | Validação da solicitante por e-mail/ata |
| M5 — Go-Live PRD | Du 46 | Primeiro lançamento real aprovado pelo Diretor |
| M6 — Encerramento formal | Du 52 | Aceite do Sponsor + relatório de cobertura 100% |

---

## Caminho Crítico ⭐

```
1.1.1 → 1.1.2 → 1.2.1.1 → 1.2.1.2 → 1.2.3 → 1.3.1.1 → 1.3.1.2
→ 1.3.2.1 → 1.3.3 → 1.4.1.1 → 1.4.2.1 → 1.4.2.2 → 1.4.2.3
→ 1.5.1.2 → 1.5.2.2 → 1.6.1.1 → 1.6.2.1 → 1.6.3.1
```
**Folga total do caminho crítico: 0 dias.**
Qualquer atraso em atividade marcada com ⭐ impacta diretamente o deadline do projeto.

---

## Buffer de Contingência

| Item | Valor | Observação |
|------|-------|------------|
| Prazo base (sem buffer) | 52 du | Conclusão no Du 52 (baseline) |
| Buffer de gestão (15% de 52du) | + 8 du | Reserva centralizada — gerenciada pelo GP, NÃO distribuída nas atividades |
| **Deadline máximo (TAP)** | **Du 60** | Teto inegociável sem revisão formal do TAP e aprovação do Sponsor |

---

*Documento gerado por Carlos Cronograma — Planejador de Prazo | VMO Autônomo Squad*
*Versão 1.0 — 2026-04-03 — Baseline pendente de aprovação do Sponsor (TAP)*
