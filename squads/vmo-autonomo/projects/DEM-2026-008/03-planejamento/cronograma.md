# Planejamento de Prazo — Integração SGMM03 Campos Empresa e Contrato
Versão: 1.0 | Data: 2026-05-28
Analista: Carlos Cronograma (VMO Autônomo)

Início do Projeto: 2026-06-16 (após resolução das CBs)
Conclusão Prevista (sem buffer): 2026-07-31
Conclusão Máxima (com buffer 15%): 2026-08-08

---

## WBS — Estrutura Analítica do Projeto

```
1. DEM-2026-008 — Integração SGMM03 Empresa/Contrato
│
├── 1.1. Pré-Execução (Resolução de CBs e Contratação)
│   ├── 1.1.1. Gestão de Condições Bloqueantes
│   │   ├── 1.1.1.1. Identificar e nomear sponsor (CB-1)
│   │   ├── 1.1.1.2. Equalizar propostas das 4 consultorias
│   │   └── 1.1.1.3. Formalizar orçamento aprovado (CB-2)
│   └── 1.1.2. Contratação
│       ├── 1.1.2.1. Selecionar consultora (análise técnico-comercial)
│       └── 1.1.2.2. Assinar contrato com marcos e SLA
│
├── 1.2. Iniciação e Especificação
│   ├── 1.2.1. Kick-off do Projeto
│   │   ├── 1.2.1.1. Reunião de kick-off (DTI + VIX Matriz + Consultora)
│   │   └── 1.2.1.2. Alinhamento de premissas e acesso aos ambientes
│   └── 1.2.2. Especificação Técnica
│       ├── 1.2.2.1. Análise técnica dos campos Empresa e Contrato no SAP PM
│       ├── 1.2.2.2. Mapeamento dos objetos SAP (BAPIs/RFCs/IDocs/BAdIs)
│       ├── 1.2.2.3. Elaboração da especificação funcional
│       ├── 1.2.2.4. Elaboração da especificação técnica
│       └── 1.2.2.5. Aprovação da especificação (GP + DTI)
│
├── 1.3. Desenvolvimento e Configuração (Ambiente DEV)
│   ├── 1.3.1. Implementação — Evento de Criação de OM
│   │   ├── 1.3.1.1. Implementar integração campo Empresa — Criação (RF001)
│   │   ├── 1.3.1.2. Implementar integração campo Contrato — Criação (RF006)
│   │   └── 1.3.1.3. Implementar tratamento de erros — Criação (RF011)
│   ├── 1.3.2. Implementação — Evento de Alteração de OM
│   │   ├── 1.3.2.1. Implementar integração campo Empresa — Alteração (RF004)
│   │   ├── 1.3.2.2. Implementar integração campo Contrato — Alteração (RF009)
│   │   └── 1.3.2.3. Implementar tratamento de erros — Alteração (RF011)
│   ├── 1.3.3. Requisitos Não-Funcionais
│   │   ├── 1.3.3.1. Implementar log WE05/WE09 (RNF005)
│   │   └── 1.3.3.2. Validar comportamento não-bloqueante (RNF003)
│   └── 1.3.4. Testes Unitários (DEV)
│       ├── 1.3.4.1. Executar testes unitários — criação de OM
│       ├── 1.3.4.2. Executar testes unitários — alteração de OM
│       ├── 1.3.4.3. Executar testes de erro e log
│       └── 1.3.4.4. Aprovar transporte DEV→QAS
│
├── 1.4. Testes (Ambiente QAS e UAT)
│   ├── 1.4.1. Testes Sistêmicos (QAS — DTI)
│   │   ├── 1.4.1.1. Executar casos de teste RF001, RF004, RF006, RF009
│   │   ├── 1.4.1.2. Executar casos de teste RF011, RNF001, RNF003, RNF005
│   │   ├── 1.4.1.3. Elaborar relatório de testes QAS
│   │   └── 1.4.1.4. Aprovação dos testes QAS pelo GP/DTI
│   └── 1.4.2. UAT — Testes de Aceitação (VIX Matriz)
│       ├── 1.4.2.1. Preparar casos de teste UAT com VIX Matriz
│       ├── 1.4.2.2. Executar UAT (Jenifer + equipe VIX Matriz)
│       ├── 1.4.2.3. Corrigir defeitos do UAT (se houver)
│       └── 1.4.2.4. Aceite formal do UAT (Jenifer assina)
│
├── 1.5. Implantação e Go-live (Ambiente PRD)
│   ├── 1.5.1. Preparação do Go-live
│   │   ├── 1.5.1.1. Elaborar plano de implantação/cutover
│   │   ├── 1.5.1.2. Aprovar janela de transporte PRD
│   │   └── 1.5.1.3. Autorização de go-live pelo sponsor
│   ├── 1.5.2. Execução do Go-live
│   │   ├── 1.5.2.1. Transportar para PRD
│   │   └── 1.5.2.2. Validar integração em produção (OMs de smoke test)
│   └── 1.5.3. Estabilização (15 dias)
│       ├── 1.5.3.1. Monitorar logs de integração (primeiros 3 dias)
│       ├── 1.5.3.2. Monitorar OMs InterCompany (dias 4–15)
│       └── 1.5.3.3. Tratar incidentes dentro do período de garantia
│
└── 1.6. Encerramento
    ├── 1.6.1. Documentação Final
    │   ├── 1.6.1.1. Finalizar documentação técnica completa
    │   ├── 1.6.1.2. Entregar ao time sustentação DTI PM/FI
    │   └── 1.6.1.3. Walkthrough de repasse (consultora → DTI)
    ├── 1.6.2. Aceite Formal
    │   ├── 1.6.2.1. Emitir relatório de encerramento
    │   └── 1.6.2.2. Aceite formal assinado pelo sponsor e VIX Matriz
    └── 1.6.3. Lições Aprendidas
        └── 1.6.3.1. Registrar lições aprendidas no VMO
```

---

## Cronograma Detalhado

### Fase 0 — Pré-Execução: CBs e Contratação (28/05 – 13/06/2026)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | ⭐ Crítico |
|----|-----------|--------|-----|---------|-------------|-------------|-----------|
| 1.1.1.1 | Identificar e nomear sponsor (CB-1) | 28/05 | 30/05 | 2d | — | PMO / Holding DTI | ⭐ |
| 1.1.1.2 | Equalizar propostas das 4 consultorias | 29/05 | 29/05 | 1d | — | Mara Rubia | ⭐ |
| 1.1.1.3 | Formalizar orçamento aprovado (CB-2) | 30/05 | 02/06 | 2d | 1.1.1.1 + 1.1.1.2 | Sponsor + Mara | ⭐ |
| 1.1.2.1 | Selecionar consultora (análise técnico-comercial) | 02/06 | 06/06 | 4d | 1.1.1.2 | GP + Mara Rubia | ⭐ |
| 1.1.2.2 | Assinar contrato com marcos e SLA | 09/06 | 13/06 | 4d | 1.1.2.1 + 1.1.1.3 | GP + Sponsor | ⭐ |

### Fase 1 — Iniciação e Especificação (16/06 – 20/06/2026)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | ⭐ Crítico |
|----|-----------|--------|-----|---------|-------------|-------------|-----------|
| 1.2.1.1 | Reunião de kick-off | 16/06 | 16/06 | 1d | 1.1.2.2 | GP + DTI + Consultora | ⭐ |
| 1.2.1.2 | Alinhamento de premissas e acesso a ambientes | 16/06 | 17/06 | 2d | 1.2.1.1 | DTI + Consultora | ⭐ |
| 1.2.2.1 | Análise técnica campos Empresa/Contrato SAP PM | 17/06 | 18/06 | 2d | 1.2.1.2 | Consultora + DTI | ⭐ |
| 1.2.2.2 | Mapeamento objetos SAP (BAPIs/IDocs/BAdIs) | 17/06 | 18/06 | 2d | 1.2.1.2 | Consultora | ⭐ |
| 1.2.2.3 | Elaboração especificação funcional | 18/06 | 19/06 | 2d | 1.2.2.1 | Consultora | ⭐ |
| 1.2.2.4 | Elaboração especificação técnica | 18/06 | 19/06 | 2d | 1.2.2.2 | Consultora | ⭐ |
| 1.2.2.5 | Aprovação da especificação (GP + DTI) | 20/06 | 20/06 | 1d | 1.2.2.3 + 1.2.2.4 | GP + DTI | ⭐ |

### Fase 2 — Desenvolvimento e Configuração DEV (23/06 – 04/07/2026)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | ⭐ Crítico |
|----|-----------|--------|-----|---------|-------------|-------------|-----------|
| 1.3.1.1 | Implementar integração Empresa — Criação (RF001) | 23/06 | 25/06 | 3d | 1.2.2.5 | Consultora | ⭐ |
| 1.3.1.2 | Implementar integração Contrato — Criação (RF006) | 23/06 | 25/06 | 3d | 1.2.2.5 | Consultora | ⭐ |
| 1.3.2.1 | Implementar integração Empresa — Alteração (RF004) | 26/06 | 28/06 | 3d | 1.3.1.1 | Consultora | ⭐ |
| 1.3.2.2 | Implementar integração Contrato — Alteração (RF009) | 26/06 | 28/06 | 3d | 1.3.1.2 | Consultora | ⭐ |
| 1.3.3.1 | Implementar log WE05/WE09 e tratamento erros | 26/06 | 27/06 | 2d | 1.3.1.1 | Consultora | — |
| 1.3.3.2 | Validar comportamento não-bloqueante (RNF003) | 28/06 | 28/06 | 1d | 1.3.2.1 + 1.3.2.2 | Consultora | — |
| 1.3.4.1 | Testes unitários — criação de OM | 30/06 | 01/07 | 2d | 1.3.1.1 + 1.3.1.2 | Consultora | ⭐ |
| 1.3.4.2 | Testes unitários — alteração de OM | 30/06 | 01/07 | 2d | 1.3.2.1 + 1.3.2.2 | Consultora | ⭐ |
| 1.3.4.3 | Testes de erro, log e não-bloqueante | 02/07 | 03/07 | 2d | 1.3.3.2 | Consultora | — |
| 1.3.4.4 | Aprovação transporte DEV→QAS | 04/07 | 04/07 | 1d | 1.3.4.1 + 1.3.4.2 | GP + DTI | ⭐ |

### Fase 3 — Testes QAS e UAT (07/07 – 18/07/2026)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | ⭐ Crítico |
|----|-----------|--------|-----|---------|-------------|-------------|-----------|
| 1.4.1.1 | Executar testes RF001, RF004, RF006, RF009 em QAS | 07/07 | 09/07 | 3d | 1.3.4.4 | DTI + Consultora | ⭐ |
| 1.4.1.2 | Executar testes RF011, RNF001, RNF003, RNF005 | 07/07 | 09/07 | 3d | 1.3.4.4 | DTI + Consultora | ⭐ |
| 1.4.1.3 | Elaborar relatório de testes QAS | 10/07 | 10/07 | 1d | 1.4.1.1 + 1.4.1.2 | Consultora | ⭐ |
| 1.4.1.4 | Aprovação testes QAS pelo GP/DTI | 11/07 | 11/07 | 1d | 1.4.1.3 | GP + DTI | ⭐ |
| 1.4.2.1 | Preparar casos de teste UAT com VIX Matriz | 10/07 | 11/07 | 2d | 1.4.1.3 | GP + Jenifer | — |
| 1.4.2.2 | Executar UAT (VIX Matriz) | 14/07 | 16/07 | 3d | 1.4.1.4 + 1.4.2.1 | Jenifer + VIX Matriz | ⭐ |
| 1.4.2.3 | Corrigir defeitos UAT (se houver) | 14/07 | 16/07 | 3d | 1.4.2.2 | Consultora | — |
| 1.4.2.4 | Aceite formal UAT (Jenifer assina) | 18/07 | 18/07 | 1d | 1.4.2.2 + 1.4.2.3 | Jenifer | ⭐ |

### Fase 4 — Implantação e Go-live PRD (21/07 – 31/07/2026)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | ⭐ Crítico |
|----|-----------|--------|-----|---------|-------------|-------------|-----------|
| 1.5.1.1 | Elaborar plano de implantação/cutover | 18/07 | 18/07 | 1d | 1.4.2.4 | Consultora + GP | ⭐ |
| 1.5.1.2 | Aprovar janela de transporte PRD | 21/07 | 21/07 | 1d | 1.5.1.1 | DTI | ⭐ |
| 1.5.1.3 | Autorização de go-live pelo sponsor | 21/07 | 21/07 | 1d | 1.5.1.2 | Sponsor | ⭐ |
| 1.5.2.1 | Transportar para PRD | 21/07 | 21/07 | 1d | 1.5.1.3 | DTI + Consultora | ⭐ |
| 1.5.2.2 | Validar integração em produção (smoke test) | 21/07 | 22/07 | 1d | 1.5.2.1 | DTI + Jenifer | ⭐ |
| 1.5.3.1 | Monitorar logs integração (primeiros 3 dias) | 22/07 | 24/07 | 3d | 1.5.2.2 | DTI + Consultora | — |
| 1.5.3.2 | Monitorar OMs InterCompany (dias 4–15 pós go-live) | 25/07 | 05/08 | 8d | 1.5.3.1 | DTI | — |

### Fase 5 — Encerramento (06/08 – 08/08/2026)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | ⭐ Crítico |
|----|-----------|--------|-----|---------|-------------|-------------|-----------|
| 1.6.1.1 | Finalizar documentação técnica completa | 25/07 | 01/08 | 6d | 1.5.2.2 | Consultora | — |
| 1.6.1.2 | Entregar documentação à sustentação DTI PM/FI | 04/08 | 05/08 | 2d | 1.6.1.1 + 1.5.3.2 | Consultora | ⭐ |
| 1.6.1.3 | Walkthrough de repasse (Consultora → DTI) | 05/08 | 05/08 | 1d | 1.6.1.2 | Consultora + DTI | ⭐ |
| 1.6.2.1 | Emitir relatório de encerramento | 06/08 | 06/08 | 1d | 1.6.1.3 | GP | ⭐ |
| 1.6.2.2 | Aceite formal (Sponsor + VIX Matriz) | 07/08 | 08/08 | 1d | 1.6.2.1 | Sponsor + Jenifer | ⭐ |
| 1.6.3.1 | Registrar lições aprendidas no VMO | 08/08 | 08/08 | 1d | 1.6.2.2 | GP + VMO | — |

---

## Marcos Principais

| Marco | Data | Critério |
|-------|------|----------|
| M0 — Qualificação Aprovada | 28/05/2026 | Parecer DEM-2026-008 aprovado com condições — CONCLUÍDO |
| M1 — CBs Resolvidas e Contrato Assinado | 13/06/2026 | Sponsor nomeado, orçamento aprovado, consultora contratada |
| M2 — Kick-off | 16/06/2026 | Reunião de kick-off realizada, acessos concedidos |
| M3 — Especificação Técnica Aprovada | 20/06/2026 | Spec funcional + técnica aprovadas pelo GP e DTI |
| M4 — Desenvolvimento Completo (DEV) | 04/07/2026 | 100% dos RF Must Have implementados e testados em DEV |
| M5 — Testes QAS Aprovados | 11/07/2026 | Testes sistêmicos aprovados pelo GP/DTI |
| M6 — UAT Aprovado | 18/07/2026 | Aceite formal da VIX Matriz (Jenifer assina) |
| M7 — Go-live PRD | 21/07/2026 | Integração ativa em produção com smoke test aprovado |
| M8 — Encerramento Formal | 08/08/2026 | 15 dias de produção estável + documentação + aceite formal |

---

## Caminho Crítico

Sequência de atividades com zero folga (qualquer atraso impacta o prazo final):

```
CB-1 (Sponsor) → CB-2 (Orçamento) → Seleção Consultora → Contrato →
Kick-off → Análise Técnica → Especificação → Aprovação Spec →
Desenvolvimento (Criação e Alteração) → Testes Unitários DEV →
Aprovação Transporte DEV→QAS → Testes QAS (RF001/004/006/009) →
Relatório QAS → Aprovação QAS → UAT → Aceite Formal UAT →
Plano Implantação → Autorização Go-live → Transporte PRD → Smoke Test →
Documentação → Entrega à Sustentação → Walkthrough → Aceite Final
```

**Duração total no caminho crítico (dias úteis):** ~37 dias úteis (sem buffer)

---

## Buffer de Contingência

| Item | Datas | Duração | Observação |
|------|-------|---------|------------|
| Buffer de gestão (15% do prazo de execução ~37 DU) | 01/08 – 08/08/2026 | ~6 dias úteis (~1 semana) | Reserva centralizada, gerenciada pelo GP. Não deve ser consumida por atividades individuais — acionada apenas para desvios do caminho crítico |
| Baseline sem buffer | 31/07/2026 | | Conclusão do go-live + estabilização |
| Deadline máximo com buffer | 08/08/2026 | | Encerramento formal com documentação entregue |

> **Regra do buffer:** O GP deve acionar o buffer apenas quando desvio no caminho crítico for
> identificado. Desvios < 2 dias úteis são absorvidos localmente pela consultora sem consumir o buffer.
> Desvios de 3+ dias úteis: GP notifica o sponsor com plano de mitigação antes de consumir o buffer.
