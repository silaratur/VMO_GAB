# Auditoria de Governança VMO — PROJ-2026-008
Data: 2026-07-07 | Auditor: Gabriel Governança | Projeto: Implantação/Expansão do
TVM para Fluxo de Caixa, Controle Orçamentário e Rastreabilidade de Riscos
(Grupo Águia Branca)

---

## VEREDICTO: ⚠️ APROVADO COM RESSALVAS

**Atualização pós-auditoria (2026-07-07):** NC-003 foi corrigida por Fábio
Fornecedor imediatamente após esta auditoria (Work Request atualizado para
T0+~13,4 semanas, consistente com os demais documentos) — verificado por
grep, sem menções ativas ao prazo antigo. **NC-001 e NC-002 permanecem
abertas** (dependem de ação administrativa externa ao pipeline — evidência
documental de sponsor e de aprovação de Diretoria/Gerente de TI). Status
atual: 0 NC-CRÍTICA, 2 NC-MODERADA aberta (NC-001, NC-002), 1 NC-MODERADA
resolvida (NC-003).

Zero não-conformidades CRÍTICAS. 3 não-conformidades MODERADAS identificadas
— dentro do limiar que permite avanço ao checkpoint final com plano de
correção formal, não um bloqueio de processo. O projeto pode prosseguir ao
Step 26 (Checkpoint de Aprovação Final), mas o GP/sponsor deve receber as 3
NC-MOD e o plano de correção antes de autorizar o kick-off.

---

## D1 — Governança de Sponsor e Autorização

| Item | Status | Evidência | Classificação |
|------|--------|-----------|---------------|
| Sponsor identificado (nome + cargo) | ✅ | Paula Barcelos, CEO — `documentacao-base.md` §Autorização | — |
| Nível Diretor ou superior | ✅ | CEO está acima do mínimo exigido (Diretor+) | — |
| CB-1 (evidência documental do sponsor) registrada na qualificação | ✅ | `qualificacao-aprovada.md` — CB-1 listada explicitamente | — |
| CB-2 (aprovação Diretoria + Gerente de TI) registrada na qualificação | ✅ | `qualificacao-aprovada.md` — CB-2 listada explicitamente | — |
| Evidência documental de resolução de CB-1 (e-mail/ata assinada) | ❌ | Apenas confirmação verbal do PMO nesta sessão — nenhum documento anexado | **NC-MODERADA** |
| Evidência documental de resolução de CB-2 (Diretoria + Gerente de TI) | ❌ | Nenhuma aprovação formal documentada até o momento | **NC-MODERADA** |

**Observação**: a identidade do sponsor está corretamente estabelecida (não é
o caso clássico de "sponsor a definir", que seria NC-CRÍTICA). O problema é
exclusivamente de **evidência documental**, não de identidade ou nível de
autoridade — por isso classificado como NC-MOD, não NC-CRÍTICA, consistente
com a distinção que todos os agentes desta pipeline já vinham fazendo desde
o intake (Iara Inbound sinalizou isso como "CLAIM SEM EVIDÊNCIA" já no
Step 1).

## D2 — Rastreabilidade e Consistência Cross-Document

| Campo | TAP | PM Canvas | Cronograma | KPIs | Work Request | Status |
|-------|-----|-----------|------------|------|---------------|--------|
| Prazo (Go-live) | T0+~13,4 sem. | T0+~13,4 sem. | T0+~13,4 sem. (M4) | Baseline PV alinhada a M0-M6 | **T0+7 sem. (M6)** | ⚠️ **INCONSISTENTE** |
| Orçamento | R$30-32k aprov. / R$43-70k estim. | Idêntico | — (não se aplica) | BAC provisório R$31k | R$30-32k aprov. / R$43-70k estim. (mesma transparência) | ✅ |
| Escopo (Must Have) | 22 itens, 3 frentes | Idêntico | WBS cobre os 22 | — | 22 itens referenciados por ID | ✅ |
| Sponsor | Paula Barcelos (CEO) | Idêntico | — | — | Não aplicável (documento de mercado) | ✅ |

**NC-MODERADA identificada**: o Work Request (`work-request.md`, Seção 6 —
Cronograma Esperado) ainda apresenta o marco M6 (Go-live) como **T0 + 7
semanas úteis**, valor que era o placeholder original do TAP **antes** da
reconciliação feita por Diana Documento com base no cronograma detalhado do
Carlos (que resultou em T0 + ~13,4 semanas úteis, incluindo buffer de 15% e
justificativa completa). O Work Request foi elaborado no Step 14, **antes**
da correção do Step 17 — a atualização não se propagou de volta ao WR.
Isso é uma inconsistência material: um fornecedor que já tenha recebido ou
esteja preparando proposta com base neste WR está planejando contra um
prazo que o próprio contratante já sabe ser irreal (o cronograma detalhado
interno usa quase o dobro do tempo).

## D3 — Conformidade com Políticas VMO

| Política | Status | Detalhe |
|----------|--------|---------|
| Work Request emitido | ✅ | `work-request.md` existe e completo |
| Artefato Obrigatório (10 grupos / 41 itens) | ✅ | Todos os 10 grupos e 41 itens transcritos integralmente, verificado no Step 15 |
| Score Vera ≥ 85 | ✅ | 89/100 (8,9/10) — `revisao-final.md` |
| CBs formalizadas no TAP | ✅ | Todas as 6 CBs (CB-1 a CB-6) explicitamente listadas em Premissas/Restrições/Riscos do TAP |

## D4 — Completude da Documentação de Iniciação

| Documento | Arquivo | Existe | Conteúdo (test -s) | Status |
|-----------|---------|:---:|:---:|--------|
| Demanda Coletada | `01-qualificacao/demanda-coletada.md` | ✅ | ✅ | OK |
| Demanda Validada | `01-qualificacao/demanda-validada.md` | ✅ | ✅ | OK |
| Gate Intake | `01-qualificacao/gate-intake.md` | ✅ | ✅ | OK |
| Sizing Inicial | `01-qualificacao/sizing.md` | ✅ | ✅ | OK |
| Qualificação | `01-qualificacao/qualificacao.md` | ✅ | ✅ | OK |
| Gate Qualificação | `01-qualificacao/gate-qualificacao.md` | ✅ | ✅ | OK |
| Qualificação Aprovada | `01-qualificacao/qualificacao-aprovada.md` | ✅ | ✅ | OK |
| TAP + Canvas + Plano Geral | `02-iniciacao/documentacao-base.md` | ✅ | ✅ | OK |
| ERF | `02-iniciacao/requisitos.md` | ✅ | ✅ | OK |
| Work Request | `02-iniciacao/work-request.md` | ✅ | ✅ | OK (com ressalva D2) |
| Cronograma (WBS+Detalhado) | `03-planejamento/cronograma.md` | ✅ | ✅ | OK |
| Plano de Riscos | `03-planejamento/plano-riscos.md` | ✅ | ✅ | OK |
| Framework de KPIs | `03-planejamento/kpis.md` | ✅ | ✅ | OK |
| Status Report #001 | `04-monitoramento/status-report-2026-07-07.md` | ✅ | ✅ | OK |
| Revisão Final (Vera) | `05-encerramento/revisao-final.md` | ✅ | ✅ | OK |

Verificação executada via `test -s` em todos os 15 arquivos — 100% presentes
e não-vazios. Nenhuma NC de completude.

## D5 — Riscos de Governança

| Risco | Coberto no plano | Classificação |
|-------|:---:|---------------|
| Sponsor ausente/insuficiente ou sem evidência documental | ✅ (R-001) | — |
| Orçamento não aprovado/reconciliado | ✅ (R-002) | — |
| Mudança de escopo sem controle formal | ✅ (Plano Geral, item 10 — Gerenciamento de Mudanças; ERF trata os itens condicionados como candidatos a CR formal) | — |

Nenhuma NC — os 3 riscos de governança padrão estão cobertos no registro de
riscos do Pedro Perigo, com estratégia, gatilho e responsável definidos.

---

## Consolidado de Não-Conformidades

| ID | Domínio | Descrição | Tipo | Ação Corretiva | Responsável | Prazo |
|----|---------|-----------|------|----------------|--------------|-------|
| NC-001 | D1 | CB-1 (evidência documental do sponsor) sem resolução documental | MODERADA | Anexar e-mail/ata assinada confirmando Paula Barcelos como sponsor | Marcelo Silveira (PMO) | Antes do kick-off |
| NC-002 | D1 | CB-2 (aprovação Diretoria + Gerente de TI) sem resolução documental | MODERADA | Obter e anexar aprovação formal de Diretoria (Financeiro) e do Gerente de TI da divisão | PMO / Alessandra Comério | Antes do kick-off |
| NC-003 | D2 | Work Request cita prazo desatualizado (T0+7 semanas) divergente do TAP/Cronograma reconciliados (T0+~13,4 semanas) | MODERADA | Atualizar Seção 6 (Cronograma Esperado) e cláusulas dependentes (reajuste, penalidades) do Work Request para refletir T0+~13,4 semanas | Fábio Fornecedor | Antes do envio efetivo do WR a qualquer fornecedor |

**Total NC-CRÍTICAS:** 0 | **Total NC-MODERADAS:** 3 | **Total NC-MENORES:** 0

Nota sobre o limiar de decisão: a task de auditoria (`auditoria-governanca.md`)
registra, na tabela de classificação de NCs, que "3+ NC-MOD" é tratado como
bloqueio; já a instrução do step do pipeline (`step-13-auditoria-governanca.md`)
define explicitamente que "zero NC-CRÍTICAS mas 3+ NC-MODERADAS" resulta em
**APROVADO COM RESSALVAS** (avança com plano de correção), não em reprovação.
Sigo a instrução do step, que é a que governa a decisão de fluxo do pipeline —
mas registro a ambiguidade entre os dois textos para conhecimento do PMO.

---

## Recomendações para a Fase de Execução

1. NC-003 é a única das 3 não-conformidades que pode ser corrigida agora,
   dentro do próprio pipeline (não depende de terceiros/aprovações externas)
   — recomendo corrigi-la antes do checkpoint final, para que o pacote
   completo não carregue uma inconsistência de prazo evitável para a
   aprovação do GP.
2. NC-001 e NC-002 dependem de ações administrativas externas ao pipeline
   (obtenção de documentos assinados) — não são corrigíveis por um agente
   do squad; devem constar explicitamente no checkpoint final como
   pré-requisitos de kick-off, não como pendências "resolvíveis depois".
3. Antes de enviar o Work Request a qualquer fornecedor real, reconfirmar
   que nenhuma outra seção do WR ficou desatualizada por correções
   posteriores no TAP/Cronograma (prática recomendada: sempre revalidar
   documentos de mercado após qualquer reconciliação interna de baseline).

---

*Auditoria realizada por Gabriel Governança — Auditor de Governança VMO*
*Próximo passo: recomendo corrigir NC-003 (Fábio Fornecedor) antes de
encaminhar para o Step 26 — Checkpoint de Aprovação Final.*
