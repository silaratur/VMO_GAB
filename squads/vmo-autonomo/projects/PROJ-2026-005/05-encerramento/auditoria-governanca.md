# Auditoria de Governança VMO — PROJ-2026-005
Data: 2026-05-18 | Auditor: Gabriel Governança | Projeto: Auditor Fiscal — Módulo Nativo NBS

---

## VEREDICTO: REPROVADO ❌

**Fundamento: NC-CRÍTICA — Ausência de Sponsor Executivo (CB-01)**

O projeto PROJ-2026-005 não pode receber aprovação de governança na presente data em razão de não-conformidade crítica de grau bloqueante: o campo de Sponsor Executivo permanece sem preenchimento no Termo de Abertura de Projeto (TAP), registrado com a marcação explícita "⚠ A IDENTIFICAR — CONDIÇÃO BLOQUEANTE CB-01". A política VMO estabelece que todo projeto com orçamento e saving documentados exige designação formal de sponsor no nível de Diretor ou superior como condição de aprovação da fase de iniciação. Sem sponsor executivo nomeado, o projeto carece da autoridade necessária para aprovar recursos, escalar decisões e assinar contratos com o fornecedor NBS.

A reprovação não reflete falha na qualidade do pacote de instrução — o score Vera Veredito de **91/100** confirma excelência documental — mas é mandatória por força da política de governança VMO, independentemente do mérito técnico do projeto.

**Condição de desbloqueio:** Identificação e formalização do sponsor executivo até **25/05/2026** (prazo CB-01 já registrado no TAP).

---

## D1 — Governança de Sponsor

**Status: NÃO CONFORME ❌ — NC-CRÍTICA**

| Campo | Situação |
|---|---|
| Sponsor Executivo Designado | **NÃO** — "A IDENTIFICAR" |
| Cargo Mínimo Exigido (Política VMO) | Diretor ou superior |
| Prazo para Regularização | 25/05/2026 (CB-01) |
| Condição no TAP | Bloqueante registrada — adequado |
| Prazo Restante na Data desta Auditoria | **7 dias corridos** |

**Análise:**

O TAP do projeto registra corretamente a ausência de sponsor como condição bloqueante CB-01, com prazo de resolução em 25/05/2026. A equipe de planejamento foi transparente ao identificar, nomear e estabelecer prazo para esta lacuna — postura que demonstra maturidade de governança. No entanto, a transparência documental não substitui o preenchimento da condição: o sponsor executivo é o ponto de autoridade formal do projeto, e sua ausência impede a aprovação de recursos, a sanção do contrato de expansão NBS e a escalada de decisões estratégicas durante a execução.

A política VMO exige cargo mínimo de Diretor ou superior para atuar como sponsor executivo em projetos com saving acima de R$ 50.000/ano ou orçamento residual acima de R$ 20.000. O PROJ-2026-005 atende ambos os critérios (saving R$ 78.000/ano; orçamento R$ 35.000), tornando o requisito de sponsor não negociável.

**Ação corretiva obrigatória:** Identificar Diretor ou superior na Divisão Comércio como sponsor executivo até 25/05/2026 (prazo CB-01 já registrado no TAP). Candidatos sugeridos: Diretor da Divisão Comércio ou CFO do Grupo.

---

## D2 — Rastreabilidade Cross-Document

**Status: CONFORME COM RESSALVA MODERADA ⚠**

### Orçamento — R$ 35.000

| Documento | Valor Registrado | Consistente? |
|---|---|---|
| qualificacao.md | R$ 35.000 (cenário central) | Sim ✅ |
| documentacao-base.md (TAP) | R$ 35.000 | Sim ✅ |
| cronograma.md | R$ 35.000 (BAC) | Sim ✅ |
| kpis.md | BAC R$ 35.000 | Sim ✅ |
| status-report-inicial.md | R$ 35.000 | Sim ✅ |

**Conclusão:** O orçamento de R$ 35.000 é completamente consistente em todos os documentos do pacote. Nenhuma divergência orçamentária identificada.

### Saving Esperado — R$ 78.000/ano

| Documento | Valor Registrado | Consistente? |
|---|---|---|
| demanda-coletada.md | R$ 78.000/ano | Sim ✅ |
| qualificacao.md | R$ 78.000/ano | Sim ✅ |
| documentacao-base.md | R$ 78.000/ano | Sim ✅ |
| requisitos.md | R$ 78.000/ano | Sim ✅ |
| kpis.md | R$ 78.000/ano | Sim ✅ |
| revisao-final.md | R$ 78.000/ano (referenciado) | Sim ✅ |

**Conclusão:** O saving de R$ 78.000/ano é consistente em todos os documentos que o mencionam. A rastreabilidade financeira do business case está íntegra.

### Prazo — Ressalva Moderada (NC-MOD-01)

O prazo de entrega (go-live) está parametrizado como "A confirmar com NBS" no TAP, com benchmark de 6–12 meses e referência de go-live em outubro/novembro 2026 no cronograma. A variabilidade declarada é documentada como premissa no próprio TAP, o que mitiga parcialmente a imprecisão. No entanto, do ponto de vista de governança, a ausência de confirmação formal da NBS sobre o prazo de desenvolvimento constitui **NC-MOD-01** — não-conformidade moderada — pois impede o comprometimento contratual do fornecedor com datas de entrega.

**Mitigante:** O Work Request (WR) foi emitido em 2026-05-18 para a NBS com prazo de submissão de proposta definido, o que inicia o processo formal de confirmação. O risco de prazo aberto está documentado no plano de riscos (RSK-01, RSK-02).

### Work Request

O WR foi emitido em 2026-05-18, endereçado formalmente à NBS, com escopo, prazo de resposta e condições definidas. A rastreabilidade da instrução ao fornecedor está estabelecida.

---

## D3 — Conformidade com Políticas VMO

**Status: NÃO CONFORME ❌ (por CB-01) | Demais itens: CONFORME ✅**

| Política VMO | Situação |
|---|---|
| Sponsor executivo — Diretor ou superior | **NÃO CONFORME ❌** — NC-CRÍTICA (CB-01) |
| Orçamento documentado e rastreável | CONFORME ✅ |
| Saving justificado com cálculo auditável | CONFORME ✅ |
| Requisitos formalizados (ERF) | CONFORME ✅ — 27 RFs + 12 RNFs com critérios testáveis |
| Plano de riscos com P×I documentado | CONFORME ✅ — 18 riscos com score e estratégia |
| KPIs com metas quantitativas | CONFORME ✅ — EVM completo, thresholds definidos |
| Cronograma com caminho crítico | CONFORME ✅ |
| Work Request emitido ao fornecedor | CONFORME ✅ — emitido 2026-05-18 |
| Business case com análise de ROI | CONFORME ✅ — payoff < 6 meses |

A única não-conformidade de política VMO de caráter bloqueante é a ausência do sponsor executivo (CB-01). Todos os demais elementos de conformidade estão atendidos com qualidade acima do padrão mínimo esperado.

---

## D4 — Completude da Documentação

**Status: CONFORME ✅ — 11/11 documentos presentes**

| # | Documento | Fase | Status |
|---|---|---|---|
| 01 | 01-qualificacao/demanda-coletada.md | Qualificação | Presente ✅ |
| 02 | 01-qualificacao/qualificacao.md | Qualificação | Presente ✅ |
| 03 | 01-qualificacao/qualificacao-aprovada.md | Qualificação | Presente ✅ |
| 04 | 02-iniciacao/documentacao-base.md | Iniciação | Presente ✅ |
| 05 | 02-iniciacao/requisitos.md | Iniciação | Presente ✅ |
| 06 | 02-iniciacao/work-request.md | Iniciação | Presente ✅ — emitido 2026-05-18 |
| 07 | 03-planejamento/cronograma.md | Planejamento | Presente ✅ |
| 08 | 03-planejamento/plano-riscos.md | Planejamento | Presente ✅ |
| 09 | 03-planejamento/kpis.md | Planejamento | Presente ✅ |
| 10 | 04-monitoramento/status-report-inicial.md | Monitoramento | Presente ✅ |
| 11 | 05-encerramento/revisao-final.md | Encerramento | Presente ✅ — score 91/100 |

**Total: 11/11 documentos ✅**

A completude documental do projeto é integral. O pacote cobre todas as fases do ciclo VMO — qualificação, iniciação, planejamento, monitoramento e encerramento — com conteúdo substantivo em cada documento. Não há placeholders ou documentos vazios. Esta é uma conformidade de alto mérito.

---

## D5 — Riscos de Governança

**Status: MONITORADO — Riscos críticos formalizados e cobertos no plano ✅**

### RSK-01 — Sponsor Executivo Não Identificado

| Atributo | Valor |
|---|---|
| Score P×I | **25/25** — Crítico |
| Probabilidade | 5 (Alta) |
| Impacto | 5 (Catastrófico) |
| Frequência de Monitoramento | Diária |
| Status na Data da Auditoria | **Materializado — CB-01 em aberto** |
| Cobertura no Plano de Riscos | Sim ✅ — com ação preventiva, contingência e dono designado |

O RSK-01 está materializado: o sponsor não foi identificado até a data desta auditoria (2026-05-18), confirmando o cenário de risco previsto. A equipe de planejamento antecipou corretamente este risco com score máximo (25/25) e monitoramento diário, o que demonstra maturidade no planejamento. O prazo de resolução (CB-01: 25/05/2026) ainda não expirou — restam 7 dias.

### RSK-02 — Orçamento Não Aprovado / Premissa NBS Não Confirmada

| Atributo | Valor |
|---|---|
| Score P×I | **20/25** — Alto |
| Probabilidade | 4 (Moderada-Alta) |
| Impacto | 5 (Catastrófico) |
| Frequência de Monitoramento | Diária |
| Status na Data da Auditoria | Pendente — CB-02 prazo 30/05/2026 |
| Cobertura no Plano de Riscos | Sim ✅ |

O RSK-02 cobre a não-confirmação do acordo contratual com a NBS que sustenta o custo zero de desenvolvimento. O WR emitido em 2026-05-18 inicia o processo de confirmação formal. O risco está adequadamente documentado com VME calculado (R$ 56.000) e contingência definida. Status: monitoramento ativo necessário até 30/05/2026.

### Avaliação Geral dos Riscos de Governança

O plano de riscos do projeto é exemplar em cobertura de governança. Além de RSK-01 e RSK-02, os riscos RSK-03 a RSK-06 cobrem cenários de escopo, prazo e relacionamento com o fornecedor que são diretamente relevantes para a fase de execução. A metodologia P×I com escalas documentadas, análise VME e fichas individuais com causa raiz e ações de resposta está acima do padrão VMO esperado para projetos deste porte.

---

## Consolidado de Não-Conformidades

| ID | Grau | Dimensão | Descrição | Prazo para Resolução |
|---|---|---|---|---|
| **NC-CRÍTICA-01** | **CRÍTICA ❌** | D1 — Sponsor | Sponsor executivo não identificado — ausência de autoridade formal do projeto | **25/05/2026 (CB-01)** |
| **NC-MOD-01** | Moderada ⚠ | D2 — Rastreabilidade | Prazo de entrega do projeto não confirmado com a NBS — benchmark declarado, não comprometido | 30/05/2026 (CB-02 / WR emitido) |
| NC-LEVE-01 | Leve | D2 — Consistência | Estimativa de rescisão do Fiscal Defender diverge entre TAP (R$ 7K) e cronograma (R$ 10K) — sem nota de revisão | Próxima revisão documental |
| NC-OBS-01 | Observação | D3 — Política | Aprovação do TAP registrada por GP "A definir" — contradição interna de autoria | Resolução junto com CB-01 |

**Resumo de graus:**
- NC-CRÍTICA: 1 (bloqueante — impede aprovação de governança)
- NC-MOD: 1 (não bloqueante — requer resolução no curto prazo)
- NC-LEVE: 1 (requer correção antes do kick-off)
- NC-OBS: 1 (requer nota explicativa; não bloqueia)

---

## Recomendações para a Fase de Execução

### Ação Imediata — Desbloqueio (até 25/05/2026)

**1. Identificar e formalizar o Sponsor Executivo (CB-01 — BLOQUEANTE)**

Identificar Diretor ou superior na Divisão Comércio como sponsor executivo até 25/05/2026 (prazo CB-01 já registrado no TAP). Candidatos sugeridos: Diretor da Divisão Comércio ou CFO do Grupo. Após nomeação, o TAP deve ser atualizado com nome, cargo e assinatura do sponsor, e o campo de aprovação do documento deve ser regularizado (NC-OBS-01 sanada em conjunto).

**2. Confirmar premissa contratual NBS (CB-02 — até 30/05/2026)**

O WR emitido em 2026-05-18 deve receber resposta formal da NBS até 30/05/2026. A confirmação do desenvolvimento como contrapartida do contrato existente é a premissa que sustenta o business case (custo zero de desenvolvimento; orçamento residual R$ 35.000). Caso a NBS não confirme, o VME de RSK-02 (R$ 56.000) deve ser acionado como gatilho de revisão do business case.

### Alta Prioridade — Fase 0 / Kick-off

**3. Regularização das NC-LEVE-01 e NC-OBS-01**

Alinhar o valor de rescisão do Fiscal Defender entre TAP e cronograma (ou registrar nota de revisão), e regularizar a autoria e aprovação do TAP após designação do sponsor.

**4. Engajar Financeiro e Jurídico da Divisão Comércio**

Os requisitos PEN-003 e PEN-004 do ERF estão classificados como "a confirmar" com estas duas áreas. Devem ser incluídos nos workshops da Fase 2 com participação obrigatória, para evitar retrabalho de requisitos em fases avançadas.

**5. Validar SLA de disponibilidade 99,5% com a NBS**

O RNF-005 do ERF especifica 99,5% de disponibilidade como critério de aceite. Esta premissa deve ser validada com a NBS antes do congelamento dos requisitos para integrar o contrato de desenvolvimento.

### Consideração de Mérito

O plano de riscos deste projeto é exemplar — RSK-01 já antecipou este risco com score crítico (25/25) e monitoramento diário. O projeto pode ser rapidamente re-aprovado após a identificação do sponsor. O pacote de instrução completo, com score 91/100 e 11/11 documentos entregues, representa trabalho de planejamento de alto padrão. A reprovação de governança desta auditoria é exclusivamente processual e não reflete qualquer deficiência técnica ou de mérito do projeto — é, ao contrário, evidência de que a própria equipe identificou e documentou a lacuna com rigor antes que ela se tornasse um problema oculto em execução.

Assim que CB-01 for sanada, o projeto pode receber aprovação de governança imediatamente, sem necessidade de replanejamento, desde que CB-02 seja confirmada no prazo de 30/05/2026.

---

*Auditoria realizada por Gabriel Governança — Auditor de Governança VMO*
*Data: 2026-05-18 | Versão: v1 | Projeto: PROJ-2026-005 — Auditor Fiscal — Módulo Nativo NBS — Divisão Comércio*
