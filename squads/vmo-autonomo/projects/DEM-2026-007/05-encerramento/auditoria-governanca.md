# Auditoria de Governança VMO — DEM-2026-007
Data: 2026-05-20 | Auditor: Gabriel Governança | Projeto: Implantação DDA SAP — VAB Matriz

---

## VEREDICTO: ⚠️ APROVADO COM RESSALVAS

O pacote de iniciação está estruturalmente completo, internamente consistente e com todos os
documentos obrigatórios presentes. As não-conformidades identificadas são gerenciáveis e já
estão registradas como Condições Bloqueantes de Kick-off — nenhuma representa falha de processo
não documentada. O projeto pode avançar ao Checkpoint Final com as 3 ressalvas formalizadas.

---

## D1 — Governança de Sponsor e Autorização

| Item | Status | Evidência | Classificação |
|------|--------|-----------|---------------|
| Sponsor identificado | ✅ | Gladston Campos — Gerência TI e Projetos Estratégicos, documentacao-base.md § Autorização | — |
| Nível Diretor ou superior | ⚠️ PARCIAL | Gladston Campos é Gerente, não Diretor. CB-Sponsor aberta e documentada como condição de kick-off em qualificacao-aprovada.md, documentacao-base.md e revisao-final.md | NC-MOD-001 |
| CB-Orçamento registrada | ✅ | CB-3 presente em qualificacao-aprovada.md (Condições de Kick-off), documentacao-base.md (Restrições R-3) e plano-riscos.md (R-001) | — |
| CB-Escopo registrada | ✅ | CB-2 presente em qualificacao-aprovada.md, requisitos.md (nota CB-2 nos RFs afetados) e cronograma.md (nota de premissa) | — |
| Autorização Holding documentada | ✅ | Walace Bacelar/Holding: autorização condicional custo zero registrada em demanda-coletada.md § Aprovações, documentacao-base.md § Autorização nota, qualificacao-aprovada.md § Aprovações | — |

**Nota D1:** NC-MOD-001 (Sponsor sem nível Diretor+) foi identificada desde o Gate 02 de Qualificação
e está formalmente gerenciada como CB-Sponsor com prazo 30/05/2026. Não é uma descoberta nova —
é uma condição de governança já em tratamento. Não bloqueia este gate (1 NC-MOD abaixo do limiar).

---

## D2 — Rastreabilidade Cross-Document

| Campo | TAP | PM Canvas | Cronograma | KPIs | WR | Status |
|-------|-----|-----------|------------|------|----|--------|
| Prazo meta (go-live) | 30/09/2026 | 30/09/2026 | 30/09/2026 | 30/09/2026 | 30/09/2026 | ✅ Consistente |
| Kick-off | Junho 2026 | — | 08/06/2026 | M-0 06/06 | Junho/2026 | ✅ Consistente |
| Orçamento externo | R$0–R$2.000 | R$0–R$2.000 | — | BAC R$2.000 | R$0 externo | ✅ Consistente |
| Integração | SAP x Santander CNAB 240 | SAP FI x Santander | SAP x Santander | — | SAP x Santander | ✅ Consistente |
| Sponsor | Gladston Campos | Gladston Campos | — | — | Gladston Campos | ✅ Consistente |
| Escopo (DDA VAB CP) | DDA VAB Matriz CP | DDA VAB CP | Fases DDA | — | DDA VAB Matriz | ✅ Consistente |
| Must Have ERF → Escopo TAP | RF001–RF005 | — | Fases 2–4 cobrem E-01 a E-06 | — | E-01 a E-09 | ✅ Rastreável |
| Critérios sucesso → KPIs | CS-1 a CS-4 | Bloco 4 | — | KR-1 a KR-4 | — | ✅ Rastreável |
| Riscos TAP → Plano Riscos | 5 riscos alto nível | Bloco 9 | Fator caminho crítico | R-001 CRÍTICO | G9 artefato | ✅ Consistente |

**Resultado D2:** Zero inconsistências detectadas entre documentos. Rastreabilidade prazo/custo/
escopo/stakeholders/critérios de sucesso/riscos verificada numericamente. ✅

---

## D3 — Conformidade com Políticas VMO

| Política | Status | Detalhe |
|----------|--------|---------|
| Work Request emitido antes de envio a fornecedores | ✅ | 02-iniciacao/work-request.md presente com data 20/05/2026 |
| Artefato Obrigatório (10 grupos / 41 itens) | ✅ | WR § 11: G1 a G10 com 41 itens OK/NOK/Observações |
| Score Vera Veredito ≥ 85 (=7,0 ponderado) | ✅ | 8,30/10 — revisao-final.md "APROVADO COM CONDIÇÕES" |
| CBs de qualificação formalizadas no TAP | ✅ | CB-2 e CB-3 como condições de kick-off na seção "Restrições" do TAP |
| CB-Sponsor registrada no TAP | ✅ | Nota de governança na seção "Autorização" do TAP |
| Gates de governança executados (Steps 2 e 5) | ✅ | gate-intake.md (PASS) e gate-qualificacao.md (v2, PASS) presentes |
| Condição de kick-off documentada (não início sem gate) | ✅ | M-0 é condição explícita em todos os documentos |

**Resultado D3:** Plena conformidade com políticas VMO. ✅

---

## D4 — Completude da Documentação de Iniciação

| Documento | Arquivo | Existe | Tem conteúdo | Status |
|-----------|---------|--------|-------------|--------|
| Demanda Coletada | 01-qualificacao/demanda-coletada.md | ✅ | ✅ | OK |
| Gate Intake | 01-qualificacao/gate-intake.md | ✅ | ✅ PASS | OK |
| Qualificação | 01-qualificacao/qualificacao.md | ✅ | ✅ 49/100 EM ESPERA v2 | OK |
| Gate Qualificação | 01-qualificacao/gate-qualificacao.md | ✅ | ✅ PASS v2 | OK |
| Qualificação Aprovada | 01-qualificacao/qualificacao-aprovada.md | ✅ | ✅ | OK |
| Documentação Base (TAP+Canvas+Plano) | 02-iniciacao/documentacao-base.md | ✅ | ✅ | OK |
| Requisitos (ERF) | 02-iniciacao/requisitos.md | ✅ | ✅ 12 RF + 5 RNF | OK |
| Work Request | 02-iniciacao/work-request.md | ✅ | ✅ 10 grupos/41 itens | OK |
| Cronograma | 03-planejamento/cronograma.md | ✅ | ✅ WBS 3 níveis, M-0 a M-6 | OK |
| Plano de Riscos | 03-planejamento/plano-riscos.md | ✅ | ✅ 10 riscos, reserva calculada | OK |
| Framework de KPIs | 03-planejamento/kpis.md | ✅ | ✅ EVM + 6 KRs | OK |
| Status Report | 04-monitoramento/status-report-2026-05-20.md | ✅ | ✅ | OK |
| Revisão de Qualidade | 05-encerramento/revisao-final.md | ✅ | ✅ 8,30/10 APROVADO CC | OK |

**Resultado D4:** 13/13 documentos presentes com conteúdo. ✅ Pacote 100% completo.

---

## D5 — Riscos de Governança

| Risco de Governança | Coberto no plano | Localização | Classificação |
|--------------------|-----------------|-------------|---------------|
| Sponsor ausente/insuficiente | ✅ | R-005: "Sponsor sem alçada Diretor+" — ALTO (30), com trigger e plano | — |
| Orçamento não aprovado / autorização Holding | ✅ | R-001: "Autorização Holding inválida se custo externo" — CRÍTICO (56) | — |
| Mudança de escopo sem controle formal | ✅ | R-009: "Scope creep durante levantamento técnico" — MÉDIO (20) + Plano Geral § 10 | — |
| CB-2 (ajustes mais complexos → reclassificação) | ✅ | R-002: "Ajustes mais complexos que parametrização" — ALTO (40) | — |
| Recurso técnico inadequado | ✅ | R-006: "Recurso DTI sem disponibilidade/conhecimento" — ALTO (28) | — |

**Resultado D5:** Todos os riscos de governança obrigatórios cobertos no plano de riscos. ✅

---

## Consolidado de Não-Conformidades

| ID | Domínio | Descrição | Tipo | Ação Corretiva | Responsável | Prazo |
|----|---------|-----------|------|----------------|-------------|-------|
| NC-MOD-001 | D1 | Sponsor (Gladston Campos) com nível Gerente, abaixo do mínimo Diretor+. CB-Sponsor aberta e documentada. | NC-MOD | Identificar e documentar no TAP um sponsor com nível Diretor ou superior antes do gate de kick-off (M-0). Gladston deve acionar um Diretor+ como patrocinador formal. | Gladston Campos | 30/05/2026 |
| NC-MEN-001 | D2 | Status Report sem percentual numérico global de conclusão do projeto (issue levantada pela Vera, C-SR-1). | NC-MENOR | Incluir "% conclusão global do projeto" no header dos status reports a partir do M-0. | GP (a designar) | M-0+ |
| NC-MEN-002 | D4 | Qualificação em status EM ESPERA (49/100 — 1 ponto abaixo do limiar formal). Avançou por decisão do usuário com condições. | NC-MENOR | Requalificação final pendente após M-1 (CB-2 resolvida). Resultado do levantamento técnico pode elevar para APROVADO COM CONDIÇÕES formalmente. | Felipe Filtro / VMO | Após M-1 |

**Total NC-CRÍTICAS:** 0 | **Total NC-MOD:** 1 | **Total NC-MENORES:** 2

> **Regra:** Bloqueia se NC-CRÍTICA > 0 OU NC-MOD ≥ 3.
> **Situação atual:** 0 CRÍTICAS + 1 MOD = **NÃO BLOQUEIA** → APROVADO COM RESSALVAS ✅

---

## Recomendações para a Fase de Execução

**REC-1 (URGENTE — antes do M-0):**
A resolução da NC-MOD-001 (sponsor Diretor+) é pré-requisito obrigatório para o gate de kick-off.
Gladston Campos deve identificar o Diretor responsável e documentar no TAP até 30/05/2026.
O gate de kick-off (Gabriel Governança — task pre-kickoff-gate.md) verificará esta condição.

**REC-2 (ANTES DO KICK-OFF):**
A re-autorização do Holding (Walace Bacelar) para o caso com custo zero deve ser obtida por
escrito antes do kick-off. O e-mail de confirmação deve ser arquivado na pasta do projeto.
Referência: R-001 CRÍTICO, CB-3.

**REC-3 (M-1 — após levantamento técnico):**
Após o Entregável E-01 (levantamento técnico), o GP deve comunicar ao VMO se houve:
(a) confirmação de parametrização → requalificação formal para APROVADO COM CONDIÇÕES; ou
(b) necessidade de desenvolvimento ABAP → reclassificação para PROJETO e novo ciclo.

**REC-4 (DURANTE EXECUÇÃO):**
O GP deve monitorar o artefato obrigatório do Work Request (G1 a G10) como checklist de
confirmação de pré-condições no kick-off. Todos os itens "NOK" devem ser resolvidos antes
de iniciar as atividades das fases afetadas.

---

*Auditoria realizada por Gabriel Governança — Auditor de Governança VMO*
*Próximo passo: Checkpoint Step 16 — Aprovar Documentação Final (usuário)*
