# Auditoria de Governança VMO — DEM-2026-008
Integração SGMM03 — Campos Empresa e Contrato (InterCompany)
Data: 2026-05-28
Auditor: Gabriel Governança (VMO Autônomo)

---

## VEREDICTO: APROVADO COM RESSALVAS ⚠️

> **Justificativa:** Zero não-conformidades CRÍTICAS identificadas. 2 não-conformidades MODERADAS
> (NC-MOD) identificadas — abaixo do limiar de 3 NC-MODs que acionaria bloqueio. O projeto é
> autorizado a avançar para o checkpoint de aprovação final com plano de correção das NC-MODs.

---

## Domínios Auditados

### D1 — Governança de Sponsor e Autorização

**Evidências consultadas:** TAP (documentacao-base.md), qualificacao-aprovada.md, gate-qualificacao.md

| Verificação | Status | Evidência |
|-------------|--------|-----------|
| TAP identifica sponsor com nome e cargo | ⚠️ NC-MOD | Sponsor marcado como "[A CONFIRMAR — CB-1]" — não há nome/cargo específico |
| Cargo do sponsor atende ao mínimo Diretor+ | ⚠️ NC-MOD (dependente de CB-1) | Não verificável até CB-1 resolvida — política do grupo requer Diretor ou superior |
| CB-Sponsor registrada como condição bloqueante | ✅ CONFORME | CB-1 documentada em qualificacao-aprovada.md, gate-qualificacao.md e TAP |
| CB-Orçamento registrada como condição bloqueante | ✅ CONFORME | CB-2 documentada em múltiplos documentos com prazo 02/06/2026 |
| Evidência documental de resolução das CBs | ⚠️ N/A | CBs ainda abertas — resolução prevista para 30/05–02/06/2026 |

**Avaliação D1:** NC-MOD ativa para sponsor. A condição bloqueante está corretamente rastreada
e o processo de resolução está em andamento (prazo 30/05/2026). Não configura NC-CRÍTICA porque
a CB está formalmente registrada e o processo está sendo gerido — não está sendo ignorada.

---

### D2 — Rastreabilidade e Consistência Cross-Document

**Evidências consultadas:** TAP, PM Canvas, Cronograma, KPIs, ERF, WR

| Verificação | Status | Evidência |
|-------------|--------|-----------|
| Prazo: TAP = PM Canvas = Cronograma | ✅ CONFORME | Go-live 31/07, encerramento 08/08 — idênticos nos 3 documentos |
| Orçamento: TAP = BAC nos KPIs = Envelope no WR | ✅ CONFORME | R$ 34.800 em TAP, KPIs e WR (como referencial) |
| Escopo TAP → RF Must Have da ERF | ✅ CONFORME | Campos Empresa e Contrato / criação e alteração mapeados nos 4 RF Must Have principais (RF001, RF004, RF006, RF009) |
| Critérios de sucesso do TAP → KPIs correspondentes | ✅ CONFORME | Critério 1 (100% OMs) → KPI "Taxa de Integração Correta"; Critério 2 (zero manuais) → KPI "Preenchimentos Manuais Residuais" |
| Módulos WR → escopo TAP e ERF | ✅ CONFORME | WR referencia RF001, RF004, RF006, RF009, RF011 explicitamente |
| Exclusões TAP → exclusões WR | ✅ CONFORME | Campo Cenário/CenPlan, SGM, outras interfaces — exclusos em ambos os documentos |

**Avaliação D2:** Totalmente conforme. Nenhuma inconsistência entre documentos detectada.

---

### D3 — Conformidade com Políticas VMO

**Evidências consultadas:** work-request.md, revisao-final.md, qualificacao-aprovada.md

| Verificação | Status | Evidência |
|-------------|--------|-----------|
| Work Request emitido antes do envio a fornecedores | ✅ CONFORME | WR elaborado (DEM-2026-008/02-iniciacao/work-request.md) — processo de equalização de propostas ainda em andamento (29/05) |
| WR contém Artefato Obrigatório completo (10 grupos) | ✅ CONFORME | Seção 11 do WR contém todos os 10 grupos com 41 itens transcrito integralmente |
| Revisão de qualidade da Vera executada e aprovada | ✅ CONFORME | Revisao-final.md: pontuação 8,68/10 — APROVADO |
| CBs da qualificação registradas no TAP | ✅ CONFORME | CB-1 e CB-2 documentadas explicitamente no TAP com prazo e responsável |
| Sponsor Diretor+ documentado | ⚠️ NC-MOD (ver D1) | Pendente de resolução da CB-1 |

**Avaliação D3:** Conforme na maioria dos itens. A NC-MOD do sponsor é a mesma identificada em D1 — não duplicada na contagem.

---

### D4 — Completude da Documentação de Iniciação

**Evidências consultadas:** Diretório DEM-2026-008/

| Entregável | Arquivo | Status |
|------------|---------|--------|
| 01-qualificacao/demanda-coletada.md | ✅ Existe e tem conteúdo | CONFORME |
| 01-qualificacao/gate-intake.md | ✅ Existe — PASS | CONFORME |
| 01-qualificacao/qualificacao.md | ✅ Existe — 50/100 | CONFORME |
| 01-qualificacao/gate-qualificacao.md | ✅ Existe — PASS | CONFORME |
| 01-qualificacao/qualificacao-aprovada.md | ✅ Existe — Auto-aprovado | CONFORME |
| 02-iniciacao/documentacao-base.md | ✅ Existe — TAP + Canvas + Plano Geral | CONFORME |
| 02-iniciacao/requisitos.md | ✅ Existe — 12 RF + 6 RNF | CONFORME |
| 02-iniciacao/work-request.md | ✅ Existe — Mini-RFP completo | CONFORME |
| 03-planejamento/cronograma.md | ✅ Existe — WBS 3 níveis + cronograma | CONFORME |
| 03-planejamento/plano-riscos.md | ✅ Existe — 8 riscos + planos | CONFORME |
| 03-planejamento/kpis.md | ✅ Existe — Framework EVM + KPIs resultado | CONFORME |
| 04-monitoramento/status-report-2026-05-28.md | ✅ Existe — Report #001 + Pesquisa | CONFORME |
| 05-encerramento/revisao-final.md | ✅ Existe — APROVADO 8,68/10 | CONFORME |

**Avaliação D4:** 100% dos entregáveis obrigatórios existem e têm conteúdo. Totalmente conforme.

---

### D5 — Riscos de Governança

**Evidências consultadas:** plano-riscos.md, qualificacao.md, status-report-2026-05-28.md

| Verificação | Status | Evidência |
|-------------|--------|-----------|
| Riscos de governança identificados no plano | ✅ CONFORME | R-001 (Sponsor) é explicitamente um risco de governança CRÍTICO |
| VME calculado com dados de impacto financeiro | ✅ CONFORME | VME = R$ 9.725 documentado na tabela de reserva de contingência |
| Diferença VME vs. Contingência orçada reportada | ✅ CONFORME | Diferença de R$ 2.765 documentada com recomendação ao sponsor |
| Issues abertas no status report com responsável/prazo | ✅ CONFORME | 4 issues abertas no status report com responsável e prazo |
| Processo de escalada de riscos CRÍTICOS definido | ✅ CONFORME | Plano de riscos e Plano Geral definem escalada para o sponsor |

**Avaliação D5:** Totalmente conforme.

---

## Tabela Consolidada de Não-Conformidades

| # | Domínio | Tipo | Descrição | Ação Corretiva | Responsável | Prazo |
|---|---------|------|-----------|----------------|-------------|-------|
| NC-01 | D1 | NC-MOD | Sponsor não designado (CB-1 aberta) — TAP não pode ser assinado formalmente | Nomear sponsor Diretor+ e atualizar TAP para versão 1.1 | PMO / Holding DTI | 30/05/2026 |
| NC-02 | D1/D3 | NC-MOD | Orçamento não aprovado formalmente (CB-2 aberta) — orçamento referencial não substitui aprovação | Obter aprovação formal do sponsor após equalização das propostas | Sponsor designado + Mara Rubia | 02/06/2026 |

**Contagem de NC:** 0 CRÍTICAS | 2 MODERADAS | 0 MENORES
**Limiar de bloqueio:** 0 NC-CRÍTICAS ✅ | < 3 NC-MODs ✅

---

## Verificação de Rastreabilidade Numérica Cross-Document

| Critério de Sucesso TAP | KPI Correspondente | RF Origem | Entregável WR |
|-------------------------|-------------------|-----------|---------------|
| CS-1: 100% OMs com campos gravados automaticamente | Taxa de Integração Correta (meta: 100%) | RF001, RF004, RF006, RF009 | E3 (Dev) + E5 (UAT) + E6 (Go-live) |
| CS-2: Zero preenchimentos manuais residuais | Preenchimentos Manuais Residuais (meta: 0) | RF001, RF004, RF006, RF009 | E5 (UAT) + E9 (Estabilização) |
| CS-3: Aceite formal da VIX Matriz | NPS ≥ 8/10 + Aceite UAT (qualitativo) | Todos os Must Have | E5 (UAT aceite) |
| CS-4: Go-live até 31/07/2026 | SPI (meta: ≥ 1,00) | — | M7 (Go-live PRD 21/07) |
| CS-5: Documentação técnica entregue | Cobertura Documentação (meta: 100%) | RNF006 | E7 (Docs) + E8 (Walkthrough) |

**Rastreabilidade:** 100% dos critérios de sucesso têm KPI e entregável correspondentes. ✅

---

## Encaminhamento

**APROVADO COM RESSALVAS → Step 16: Checkpoint Final (AUTO-APROVADO)**

O pacote de iniciação DEM-2026-008 está aprovado para o checkpoint final com as seguintes
ressalvas ativas (NC-MODs que não bloqueiam o pipeline mas devem ser resolvidas antes do kick-off):

1. **NC-01:** Designar sponsor Diretor+ e atualizar TAP (versão 1.1) até 30/05/2026
2. **NC-02:** Formalizar aprovação do orçamento pelo sponsor até 02/06/2026

O pacote de iniciação está completo, consistente, rastreável e com qualidade acima do mínimo
(8,68/10 na revisão da Vera). A documentação gerada é suficiente para o kick-off do projeto
após resolução das CBs.
