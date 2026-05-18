# Auditoria de Governança VMO — PROJ-2026-001
Data: 2026-05-18 | Auditor: Gabriel Governança | Projeto: Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados

---

## VEREDICTO: APROVADO COM RESSALVAS ⚠️

O projeto PROJ-2026-001 atende aos requisitos essenciais de governança VMO: sponsor identificado com cargo de Diretor, score Vera Veredito de 8.7/10 (acima do mínimo de 8.5), orçamento e prazo consistentes entre todos os documentos, escopo rastreável e todos os 11 documentos obrigatórios presentes com conteúdo. O Work Request foi emitido em conformidade com as novas políticas VMO, contendo os 10 grupos e 41 itens obrigatórios. A ressalva única registrada é a ausência da assinatura formal do TAP pelo sponsor Andre Chieppe (NC-MENOR), condição que não bloqueia o avanço do projeto mas deve ser regularizada antes do início formal da execução.

---

## D1 — Governança de Sponsor

| Critério | Verificação | Status |
|---|---|---|
| Sponsor identificado | Andre Chieppe | ✅ Conforme |
| Cargo do sponsor | Diretor Financeiro — VIX Manutenção | ✅ Conforme (cargo Diretor atende política VMO) |
| Sponsor com alçada de aprovação | Sim (Diretor Financeiro, escopo financeiro SAP FI) | ✅ Conforme |
| Assinatura formal do TAP | Pendente — TAP em status AGUARDANDO ASSINATURA | ⚠️ NC-MENOR |
| Sponsor ativo no projeto | Sim — identificado e referenciado em todos os documentos | ✅ Conforme |

**Observação D1:** O nome completo do Diretor Financeiro (Andre Chieppe) não estava confirmado na época da emissão original do TAP, o que motivou o status "AGUARDANDO ASSINATURA". O sponsor está formalmente identificado; a assinatura física/digital do documento TAP é a única pendência.

---

## D2 — Rastreabilidade Cross-Document

| Parâmetro | TAP / Qualificação | Cronograma | KPIs | Work Request | Status |
|---|---|---|---|---|---|
| Orçamento | R$ 8.640 | R$ 8.640 | R$ 8.640 | R$ 8.640 | ✅ Consistente |
| Prazo | 60 dias úteis | 60 dias úteis | 60 dias úteis | 60 dias úteis | ✅ Consistente |
| Escopo — Parametrização ZFI0057 | ✅ Referenciado | ✅ Referenciado | ✅ Referenciado | ✅ Referenciado | ✅ Consistente |
| Escopo — SBWP (workflow SAP) | ✅ Referenciado | ✅ Referenciado | ✅ Referenciado | ✅ Referenciado | ✅ Consistente |
| Sponsor Andre Chieppe | ✅ Identificado | ✅ Identificado | ✅ Identificado | ✅ Identificado | ✅ Consistente |
| Condições Bloqueantes (CBs) | Nenhuma CB bloqueante | — | — | — | ✅ Sem bloqueio |

**Resultado D2:** Rastreabilidade cross-document integral. Nenhuma inconsistência detectada entre os documentos de qualificação, iniciação, planejamento, monitoramento e encerramento.

---

## D3 — Conformidade com Políticas VMO

| Política VMO | Critério Verificado | Status |
|---|---|---|
| Score mínimo Vera Veredito: 8.5/10 | Score obtido: 8.7/10 | ✅ Conforme |
| Sponsor com cargo mínimo de Gerente | Cargo: Diretor Financeiro | ✅ Conforme |
| Work Request com 10 grupos / 41 itens obrigatórios | WR emitido em 2026-05-18 com 10 grupos / 41 itens | ✅ Conforme |
| Teto orçamentário respeitado (com contingência) | R$ 8.640 — dentro do teto máximo aprovado | ✅ Conforme |
| Plano de riscos presente | Presente em 03-planejamento/plano-riscos.md | ✅ Conforme |
| KPIs definidos e mensuráveis | Presentes em 03-planejamento/kpis.md | ✅ Conforme |
| Revisão final / score encerramento | Realizado em 05-encerramento/revisao-final.md (8.7/10) | ✅ Conforme |
| Assinatura do TAP pelo sponsor | Pendente | ⚠️ NC-MENOR |

**Observação D3:** O Work Request foi inserido em 2026-05-18 em conformidade com as novas políticas VMO. O documento está completo e atende integralmente ao padrão exigido de 10 grupos e 41 itens. Nenhuma outra não-conformidade com políticas VMO identificada.

---

## D4 — Completude da Documentação

| # | Documento | Caminho | Status |
|---|---|---|---|
| 1 | Demanda Coletada | 01-qualificacao/demanda-coletada.md | ✅ Presente e com conteúdo |
| 2 | Qualificação | 01-qualificacao/qualificacao.md | ✅ Presente e com conteúdo |
| 3 | Qualificação Aprovada | 01-qualificacao/qualificacao-aprovada.md | ✅ Presente e com conteúdo |
| 4 | Documentação Base (TAP) | 02-iniciacao/documentacao-base.md | ✅ Presente e com conteúdo |
| 5 | Requisitos | 02-iniciacao/requisitos.md | ✅ Presente e com conteúdo |
| 6 | Work Request | 02-iniciacao/work-request.md | ✅ Presente e com conteúdo |
| 7 | Cronograma | 03-planejamento/cronograma.md | ✅ Presente e com conteúdo |
| 8 | Plano de Riscos | 03-planejamento/plano-riscos.md | ✅ Presente e com conteúdo |
| 9 | KPIs | 03-planejamento/kpis.md | ✅ Presente e com conteúdo |
| 10 | Status Report Inicial | 04-monitoramento/status-report-inicial.md | ✅ Presente e com conteúdo |
| 11 | Revisão Final | 05-encerramento/revisao-final.md | ✅ Presente e com conteúdo (score 8.7/10) |

**Resultado D4:** 11/11 documentos obrigatórios presentes com conteúdo. Completude documental: 100%.

---

## D5 — Riscos de Governança

| ID Risco | Descrição | Cobertura no Plano de Riscos | Classificação | Status |
|---|---|---|---|---|
| RG-01 | TAP sem assinatura formal do sponsor — pode impactar o marco de início oficial do projeto | Coberto (risco de sponsor não assinar o TAP registrado no plano) | Alto | ⚠️ Ativo — pendente regularização |
| RG-02 | Indisponibilidade do ambiente QAS SAP durante testes de parametrização | Coberto no plano de riscos | Médio | ✅ Mitigado no plano |
| RG-03 | Resistência dos usuários à mudança no processo de aprovação SAP FI (change management) | Coberto no plano de riscos | Médio | ✅ Mitigado no plano |
| RG-04 | Desvio de prazo acima do teto de 60 dias úteis | Coberto via KPIs e cronograma com marco de controle | Médio | ✅ Monitorado |
| RG-05 | Desvio orçamentário além do teto de R$ 8.640 | Teto com contingência já incorporado ao orçamento aprovado | Baixo | ✅ Controlado |

**Resultado D5:** O único risco de governança ativo é o RG-01 (TAP sem assinatura), classificado como NC-MENOR. Todos os demais riscos identificados possuem cobertura adequada no plano de riscos.

---

## Consolidado de Não-Conformidades

| ID | Domínio | Descrição | Tipo | Ação Corretiva | Responsável | Prazo |
|---|---|---|---|---|---|---|
| NC-001 | D1 — Governança de Sponsor / D3 — Políticas VMO | TAP (documentacao-base.md) em status AGUARDANDO ASSINATURA — assinatura formal de Andre Chieppe (Diretor Financeiro) pendente | NC-MENOR | Obter assinatura física ou digital do sponsor no TAP antes do início formal da execução do projeto | PMO VMO + Andre Chieppe | Antes do kick-off de execução |

**Total de Não-Conformidades:** 1 (um)
- NC-Crítica: 0
- NC-Maior: 0
- NC-Menor: 1

---

## Recomendações para a Fase de Execução

1. **Regularizar assinatura do TAP (prioritário):** Antes do kick-off formal de execução, o PMO deve garantir a assinatura de Andre Chieppe no TAP. Sugere-se envio via DocuSign ou equivalente com prazo máximo de 5 dias úteis após esta auditoria.

2. **Controle de prazo rigoroso:** O prazo de 60 dias úteis não comporta folgas adicionais dado o orçamento ajustado. Recomenda-se revisão quinzenal do cronograma com o sponsor para antecipar desvios.

3. **Gestão do ambiente QAS:** Agendar janela de ambiente QAS SAP com a equipe de Basis com antecedência mínima de 10 dias úteis antes dos testes de parametrização ZFI0057 e SBWP, mitigando o risco RG-02.

4. **Plano de comunicação para change management:** Iniciar comunicação formal aos usuários impactados pelo novo fluxo de aprovação SAP FI antes da entrada em produção, endereçando o risco RG-03.

5. **Monitoramento dos KPIs desde o início:** Ativar o painel de KPIs já na primeira semana de execução, utilizando o status-report-inicial como linha de base, garantindo rastreabilidade do progresso.

6. **Arquivo da auditoria:** Este relatório de auditoria deve ser anexado ao pacote de encerramento do projeto e referenciado na qualificação-aprovada para fins de auditoria futura.

---

## Resumo Executivo

| Dimensão | Resultado |
|---|---|
| Governança de Sponsor (D1) | Conforme com ressalva (assinatura pendente) |
| Rastreabilidade Cross-Document (D2) | Conforme — 100% consistente |
| Conformidade com Políticas VMO (D3) | Conforme com ressalva (TAP não assinado) |
| Completude da Documentação (D4) | Conforme — 11/11 documentos |
| Riscos de Governança (D5) | 1 risco ativo (RG-01 — NC-MENOR) |
| **Veredicto Final** | **APROVADO COM RESSALVAS ⚠️** |

---

*Auditoria realizada por Gabriel Governança — Auditor de Governança VMO*
*Data de emissão: 2026-05-18*
*Referência: PROJ-2026-001 — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados*
