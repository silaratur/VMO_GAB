# Auditoria de Governança VMO — PROJ-2026-006
## Plataforma Própria de Gestão de Ideias e Inovação

| Campo | Valor |
|---|---|
| **Auditor** | Gabriel Governança — Auditor de Governança VMO |
| **Data da Auditoria** | 2026-05-17 |
| **Versão** | 1.0 |
| **Pacote auditado** | Iniciação completa — 11 documentos |
| **Score de qualidade (Vera)** | 92,25/100 — APROVADO COM CONDIÇÕES |
| **Referência** | Step 13 do pipeline VMO Autônomo |

---

## ❌ VEREDICTO: REPROVADO

**O pacote de iniciação do PROJ-2026-006 não está autorizado a avançar para o checkpoint final.**

Uma não-conformidade crítica (NC-CRÍTICA) foi identificada no domínio de governança de sponsor. A qualidade documental avaliada pela Vera (92,25/100) é excelente — os documentos estão bem escritos. O bloqueio é de **processo**: o sponsor formal com nível Diretor ou superior não foi identificado, e o TAP não pode ser considerado autorizado sem essa formalidade. Documentos impecáveis assinados sem sponsor são, do ponto de vista de governança, documentos não autorizados.

**Ação imediata exigida:** Jadson deve identificar o Diretor responsável pela área de Inovação (ou equivalente com autoridade orçamentária) e submetê-lo ao GP VMO para validação de nível hierárquico. Após nomeação e assinatura do TAP, o projeto poderá ser reapresentado para nova auditoria.

---

## D1 — Governança de Sponsor

| Item | Status | Evidência | Classificação |
|------|--------|-----------|---------------|
| Sponsor identificado com nome e cargo | ❌ | TAP seção 1: `"[A DEFINIR — Diretor ou superior, conforme condição bloqueante CB-01]"` | **NC-CRÍTICA** |
| Nível hierárquico Diretor ou superior confirmado | ❌ | Impossível verificar — sponsor não nomeado | **NC-CRÍTICA** (mesma raiz) |
| CB-01 registrada formalmente na qualificação | ✅ | `qualificacao-aprovada.md` — CB-01 documentada com responsável (Jadson) e prazo (13/06/2026) | Conforme |
| CB-02 registrada formalmente na qualificação | ✅ | `qualificacao-aprovada.md` — CB-02 documentada com prazo (20/06/2026) | Conforme |
| Ressalva do GP sobre nível mínimo de sponsor | ✅ | `qualificacao-aprovada.md`: *"Nível mínimo de sponsor: Diretor ou superior"* — explicitado pelo GP Marcelo Silveira | Conforme |

**Análise:** A ausência do sponsor não é uma surpresa — é uma condição bloqueante documentada desde a qualificação. O ponto de auditoria é que a CB-01 ainda está em aberto na data desta auditoria (2026-05-17) e o TAP foi elaborado com o campo sponsor preenchido como "[A DEFINIR]". Isso é correto do ponto de vista documental (Diana Documento agiu corretamente ao não inventar um nome), mas impede a aprovação de governança. O TAP não tem validade de autorização sem assinatura de sponsor com nível verificado.

---

## D2 — Rastreabilidade Cross-Document

| Campo | TAP | PM Canvas | Cronograma | KPIs | WR | Status |
|-------|-----|-----------|------------|------|----|--------|
| Prazo máximo | 31/12/2026 | 31/12/2026 | 31/12/2026 (go-live 07/12) | 07/12/2026 go-live | Kick-off 24/06 | ✅ Consistente |
| Orçamento/BAC | R$100.000 | R$100.000 | — | BAC R$100.000 | Envelope R$100.000 | ✅ Consistente |
| Escopo (módulos) | M1-M6 + infraestrutura | M1-M6 | M1-M6 sequencial | M1-M6 | M1-M6 (19 RFs) | ✅ Consistente |
| Critérios de sucesso | CS-01 a CS-05 | CS-01 a CS-05 | Marcos vinculados a CS | KPIs vinculados a CS | — | ⚠️ Ver NC-002 |
| Cobertura de testes | UAT mencionado | — | UAT 80% cobertura | — | 70% cobertura | ⚠️ Ver NC-003 |

**NC-002 — Inconsistência de referência nos KPIs:**
O `kpis.md` registra KPI-R-04 como vinculado ao CS-04 (custo dentro do orçamento), quando a lógica do documento indica que deveria referenciar CS-03 (adoção pelos usuários ≥ 70%). Essa inconsistência foi também identificada pela Vera Veredito (condição de melhoria #1 do relatório de revisão). A referência cruzada incorreta cria ambiguidade sobre o que está sendo monitorado pelo KPI-R-04.

**NC-003 — Divergência de cobertura de testes entre WR e Cronograma:**
O `work-request.md` (Seção 9.4, Condições de Aceite do Marco M5) especifica cobertura mínima de testes de **70%**, enquanto o `cronograma.md` planeja UAT com critério de aceite de **80% de cenários aprovados**. Essa divergência de 10 pontos percentuais pode gerar conflito de expectativas com o fornecedor contratado via WR. Identificada também por Vera (condição de melhoria #5).

**Análise geral D2:** O alinhamento entre os documentos é sólido nas dimensões estratégicas (prazo, orçamento, escopo de módulos). As duas não-conformidades são inconsistências pontuais que não invalidam o pacote, mas devem ser corrigidas antes do envio do WR ao mercado.

---

## D3 — Conformidade com Políticas VMO

| Política | Status | Evidência |
|----------|--------|-----------|
| Work Request emitido antes do envio a fornecedores | ✅ | `work-request.md` — WR-2026-006 emitido em 16/05/2026; prazo de submissão 06/06/2026 |
| Artefato Obrigatório completo (10 grupos / 41 itens) | ✅ | WR-2026-006 — relatório de Fábio Fornecedor confirma todos os grupos presentes com OK/NOK/Observações |
| Score Vera ≥ 85/100 | ✅ | `revisao-final.md` — Score 92,25/100 — APROVADO COM CONDIÇÕES |
| Condições bloqueantes formalizadas no TAP | ✅ | `documentacao-base.md` — CB-01 e CB-02 em seção dedicada com status PENDENTE |
| Sponsor identificado com nível Diretor+ documentado | ❌ | TAP: `[A DEFINIR — Diretor ou superior]` — mesmo bloqueio de D1 |
| GP designado com nome | ❌ | TAP seção 1: *"Gerente de Projeto: A designar após aprovação formal do TAP"* — consequência direta de CB-01 | **NC-MENOR** |

**Análise D3:** O WR foi emitido corretamente e o Artefato Obrigatório está completo — esta é a primeira validação bem-sucedida do agente Fábio Fornecedor. O processo VMO foi seguido. A única não-conformidade relevante em D3 é reflexo de D1 (sponsor ausente), não uma falha independente de processo.

---

## D4 — Completude da Documentação

| Documento | Arquivo | Existe | Não vazio | Status |
|-----------|---------|--------|-----------|--------|
| Demanda Coletada | 01-qualificacao/demanda-coletada.md | ✅ | ✅ | OK |
| Qualificação | 01-qualificacao/qualificacao.md | ✅ | ✅ | OK |
| Qualificação Aprovada | 01-qualificacao/qualificacao-aprovada.md | ✅ | ✅ | OK |
| Documentação Base (TAP+Canvas+Plano) | 02-iniciacao/documentacao-base.md | ✅ | ✅ | OK |
| ERF (Requisitos) | 02-iniciacao/requisitos.md | ✅ | ✅ | OK |
| Cronograma | 03-planejamento/cronograma.md | ✅ | ✅ | OK |
| Plano de Riscos | 03-planejamento/plano-riscos.md | ✅ | ✅ | OK |
| Framework de KPIs | 03-planejamento/kpis.md | ✅ | ✅ | OK |
| Work Request | 03-planejamento/work-request.md | ✅ | ✅ | OK |
| Status Report | 04-monitoramento/status-report-2026-05-16.md | ✅ | ✅ | OK |
| Revisão Final (Vera) | 05-encerramento/revisao-final.md | ✅ | ✅ | OK |

**Verificação:** `test -s` executado em todos os 11 arquivos — todos retornaram PASS.

**Análise D4:** Completude perfeita. Todos os entregáveis obrigatórios da fase de iniciação existem e têm conteúdo. Este é o resultado esperado de um pipeline bem executado.

---

## D5 — Riscos de Governança

| Risco de Governança | Coberto no Plano de Riscos | Evidência | Classificação |
|---------------------|---------------------------|-----------|---------------|
| Sponsor ausente ou nível insuficiente | ✅ | RSK-001 — score 20 (CRÍTICO), maior risco do projeto; estratégia: Evitar; ação: Jadson ativar rede de liderança até [data] | Conforme |
| Orçamento não aprovado formalmente | ✅ | RSK-002 — score 16 (CRÍTICO); estratégia: Mitigar; ação: levantamento formal de custo com fornecedor | Conforme |
| Prazo fixo com caminho crítico sequencial | ✅ | RSK-003 — score 20 (CRÍTICO); estratégia: Mitigar via buffer 15% | Conforme |
| Mudança de escopo sem controle formal de CR | ❌ | Não identificado explicitamente como risco no plano — as 12 categorias cobrem Governança/Sponsor, Financeiro, Prazo, Técnico, Adoção, Conformidade, mas não modelam o risco de "scope creep por ausência de processo de CR" | **NC-MOD** |

**NC-005 — Risco de mudança de escopo sem Change Request formal:**
O plano de riscos é abrangente (12 riscos, 6 categorias, VME R$260k), mas não modela explicitamente o risco de mudança de escopo não formalizada — um dos principais vetores de desvio em projetos de desenvolvimento de plataforma. Com fornecedor externo a ser contratado via WR, a ausência de um processo formal de CR e seu risco associado é uma lacuna de governança a corrigir antes da execução.

**Análise D5:** Cobertura de riscos de governança é boa — os dois maiores (sponsor e orçamento) são os primeiros da lista. A lacuna de CR é pontual e corrigível com uma linha adicional no plano de riscos.

---

## Consolidado de Não-Conformidades

| ID | Domínio | Descrição | Tipo | Ação Corretiva | Responsável | Prazo |
|----|---------|-----------|------|----------------|-------------|-------|
| **NC-001** | D1 + D3 | Sponsor não identificado — TAP contém `[A DEFINIR]`. Nenhum documento pode ser considerado formalmente autorizado sem assinatura de Diretor+ | **NC-CRÍTICA** | Jadson identifica o Diretor responsável → GP VMO valida nível hierárquico → Diretor assina o TAP → Gabriel reaudita | Jadson | **2026-06-13** |
| NC-002 | D2 | KPI-R-04 no `kpis.md` referencia CS-04 (custo) quando deveria referenciar CS-03 (adoção ≥ 70%). Inconsistência de rastreabilidade CS↔KPI | NC-MOD | Marcela Métrica corrige a referência de CS no KPI-R-04 | Marcela Métrica / GP VMO | 2026-05-24 |
| NC-003 | D2 | Cobertura de testes diverge: WR especifica 70%, Cronograma planeja 80%. Fornecedor contratado pelo WR pode usar o critério mais baixo | NC-MOD | Alinhar ambos os documentos para 80% antes do envio do WR ao mercado (prazo de submissão: 06/06/2026) | GP VMO | **2026-06-03** |
| NC-004 | D5 | Risco de mudança de escopo sem CR formal não mapeado no plano de riscos | NC-MOD | Pedro Perigo adiciona RSK-013: "Mudança de escopo não formalizada — probabilidade 3, impacto 4, score 12 (ALTO); estratégia: Mitigar via processo de CR obrigatório" | Pedro Perigo | 2026-05-24 |
| NC-005 | D3 | GP não designado nominalmente no TAP — consequência de CB-01, mas cria lacuna de responsabilidade formal no documento | NC-MENOR | Após resolução de NC-001, inserir nome do GP no TAP antes da assinatura | GP VMO | Com NC-001 |

**Resumo:**
| Tipo | Total |
|------|-------|
| NC-CRÍTICA | **1** — bloqueia o projeto |
| NC-MODERADA | **3** — não bloqueiam individualmente, mas 3 NC-MOD ativas = limite máximo |
| NC-MENOR | **1** — para ciência |

> ⚠️ **Atenção:** O projeto possui exatamente 3 NC-MOD ativas. Pelo critério de governança, 3 ou mais NC-MODERADAS também resultam em bloqueio. Mesmo que NC-001 (sponsor) fosse resolvida, as NC-002, NC-003 e NC-004 precisariam ser reduzidas para menos de 3 antes da aprovação. As três são corrigíveis rapidamente (renomeação de referência, alinhamento de percentual, adição de risco).

---

## Recomendações para a Fase de Execução

Após a resolução das NCs e aprovação desta auditoria, registrar as seguintes recomendações para o início da execução:

1. **Estabelecer processo de Change Request (CR) formal antes do kick-off** — o plano de comunicação deve prever canal oficial para submissão de CRs, com template e fluxo de aprovação pelo GP e Sponsor.
2. **Alinhar o prazo de submissão do WR com a resolução de NC-001** — o WR tem prazo de submissão em 06/06/2026. Se o sponsor não for identificado até lá, o processo seletivo será iniciado sem TAP assinado — risco contratual para o grupo.
3. **Atualizar o `kpis.md` e `plano-riscos.md` nas próximas 48h** — as correções de NC-002 e NC-004 são triviais (edição de referência e adição de uma linha de risco) e devem ser feitas imediatamente, independente da NC-001.
4. **Criar a política de CR no TAP revisado** — quando o Sponsor assinar o TAP, incluir na seção de Plano de Mudanças a exigência formal de CR para qualquer desvio de baseline ≥ 2 dias ou R$2.000.

---

## Histórico de Decisão da Auditoria

| Critério | Resultado |
|----------|-----------|
| NC-CRÍTICAS | 1 — **BLOQUEIA** |
| NC-MODERADAS | 3 — **BLOQUEIA** (limite: < 3) |
| NC-MENORES | 1 — Não bloqueia |
| Score Vera | 92,25/100 — Acima do limiar (≥ 85) |
| Completude documental | 11/11 arquivos OK |
| **Veredicto** | **REPROVADO ❌** |

---

## Próximos Passos Obrigatórios (em ordem)

| # | Ação | Responsável | Prazo | Desbloqueio |
|---|------|-------------|-------|-------------|
| 1 | Corrigir NC-002 (KPI-R-04 → CS-03) no `kpis.md` | Marcela Métrica / GP VMO | 2026-05-24 | NC-002 |
| 2 | Corrigir NC-003 (cobertura testes 70% → 80%) no `work-request.md` | GP VMO | 2026-06-03 | NC-003 |
| 3 | Adicionar RSK-013 (risco de escopo sem CR) no `plano-riscos.md` | Pedro Perigo | 2026-05-24 | NC-004 |
| 4 | Jadson identifica o Diretor responsável e submete ao GP VMO para validação | Jadson | 2026-06-13 | NC-001 |
| 5 | GP VMO valida nível hierárquico (Diretor+) com documentação comprobatória | Marcelo Silveira | 2026-06-13 | NC-001 |
| 6 | Diretor nomeado assina o TAP fisicamente ou via assinatura eletrônica | Sponsor designado | 2026-06-13 | NC-001 |
| 7 | GP VMO insere nome do GP no TAP e corrige NC-005 | GP VMO | Com passo 6 | NC-005 |
| **8** | **Gabriel Governança reauditado para emissão de APROVADO** | Gabriel Governança | Após passos 1-7 | — |

---

*Auditoria realizada por Gabriel Governança — Auditor de Governança VMO*
*Próxima ação: resolver NC-002, NC-003 e NC-004 imediatamente; resolver NC-001 até 13/06/2026*
*Reauditoria: solicitar via `/opensquad run vmo-autonomo --agent gabriel-governanca` após resolução de todas as NCs*
