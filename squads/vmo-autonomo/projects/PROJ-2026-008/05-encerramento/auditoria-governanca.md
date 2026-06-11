# Auditoria de Governança VMO — PROJ-2026-008
Data: 2026-06-11 | Auditor: Gabriel Governança | Projeto: Ajustes nos Monitores ZMMR_GSI02/03/04 (SAP ECC Módulo MM)

---

## VEREDICTO: ❌ REPROVADO / BLOQUEADO (com encaminhamento específico — ver "Próximo Passo")

O pacote de iniciação está **documentalmente completo e foi aprovado com condições pela Vera Veredito (8,23/10)**. No entanto, esta auditoria identifica **1 não-conformidade CRÍTICA (D1 — sponsor abaixo do nível mínimo, CB-1 não resolvida com evidência)** e **3 não-conformidades MODERADAS (D2/D1)**, ambas isoladamente suficientes para bloquear o avanço ao checkpoint final conforme a política VMO. O bloqueio é de **governança/processo**, não de qualidade documental — e suas causas são **ações externas pendentes (CB-1, CB-2, designação de GP)**, não retrabalho de conteúdo. Ver seção "Próximo Passo" para o encaminhamento recomendado, que não é o retrabalho documental padrão de `on_reject: 5`.

---

## D1 — Governança de Sponsor e Autorização

| Item | Status | Evidência | Classificação |
|------|--------|-----------|---------------|
| Sponsor identificado (nome e cargo explícitos) | ✅ | `documentacao-base.md`, Identificação: "Sponsor: Nubia Carla Freitas Santos Souza — Gerente Contábil (Gestor Direto) [PROVISÓRIO]" | — |
| Nível Diretor ou superior | ❌ | Cargo registrado é "Gerente Contábil" — abaixo do mínimo Diretor+ exigido pela política do grupo. O próprio TAP marca o sponsor como **PROVISÓRIO**, com status do documento "RASCUNHO — Aguardando confirmação de Sponsor de nível Diretoria (CB-1)" | **NC-CRÍTICA (NC-001)** |
| CB-1 registrada na qualificação | ✅ | `qualificacao-aprovada.md`: "CB-1 \| Confirmar aprovação formal de Diretoria da área solicitante \| Tatiane Dias de Moraes / Projetos DTI \| 2026-06-13" | — |
| CB-2 registrada na qualificação | ✅ | `qualificacao-aprovada.md`: "CB-2 \| Confirmar cargo formal de Gerente de TI (Raphael Leitão Sbardelotti) \| ... \| 2026-06-13" | — |
| Evidência documental de resolução de CB-1/CB-2 | ❌ | Nenhum documento do pacote registra confirmação de Diretoria nem confirmação do cargo do aprovador técnico/orçamentário. Status Report #001 (`status-report-2026-06-11.md`) lista ambas como ISS-001/ISS-002, **prazo 2026-06-13, ainda não vencido na data desta auditoria (2026-06-11)** | **NC-CRÍTICA (decorrência de NC-001)** |
| Gerente de Projeto designado | ❌ | `documentacao-base.md`, Identificação: "Gerente de Projeto: A designar pelo SQUAD PM/MM (Time de Sustentação ERP)". Já registrado como ISS-009/Condição #1 da Vera | **NC-MOD (NC-002)** |

---

## D2 — Rastreabilidade Cross-Document

| Campo | TAP | PM Canvas | Cronograma | KPIs | WR | Status |
|-------|-----|-----------|------------|------|----|--------|
| Prazo final | 2026-09-30 | 2026-09-30 | Baseline M5 = 2026-09-25; **com buffer de 15% (~2,2 sem.) projeta 2026-10-10** | PV baseline ancorado nos marcos do cronograma (M0-M5) | Marcos de alto nível alinhados às ondas (M3/M4/M6 = Ondas 1/2/3) | ⚠️ |
| Orçamento | R$ 30.000 (teto declarado aprovado) + R$ 6.000 (contingência 20%) = R$ 36.000 | R$ 36.000 (consistente com TAP) | — | BAC = R$ 36.000 (com nota explícita sobre a diferença frente ao teto de R$ 30.000) | Envelope de calibração R$ 30-36K (benchmark de mercado R$ 25-80K usado apenas como referência externa, dual-recipient) | ⚠️ |
| Escopo (15 itens / 3 ondas) | Onda 1 (7 itens), Onda 2 (4 itens), Onda 3 (4 itens) — idêntico em todas as fontes | idem | WBS 1.2/1.3/1.4 = Ondas 1/2/3, mesma composição de itens | KPIs de cobertura por onda com a mesma composição | Escopo incluso organizado pelas mesmas 3 ondas, com IDs de RF da ERF referenciados | ✅ |
| RF Must Have (ERF) → WBS | — | — | Pacotes da WBS referenciam RFs (ex.: itens 13/14 → 1.4.2.4, CB-6) | KPIs de cobertura referenciam os mesmos itens | Escopo incluso do WR referencia RF001-RF022 por onda | ✅ |
| Critérios de Sucesso TAP → KPIs | 5 critérios | — | — | 8 KPIs de resultado mapeados 1:1 e N:1 aos 5 critérios (tabela de rastreabilidade em `kpis.md`) | — | ✅ |

**Inconsistências identificadas:**

1. **Prazo (NC-MOD — NC-003)**: O TAP compromete 2026-09-30 como prazo final, mas o Cronograma — calculado a partir da própria WBS derivada do TAP — projeta, com o buffer de contingência padrão (15%), uma data de conclusão de 2026-10-10 (~10 dias além do compromisso do TAP). Esta divergência **já está documentada de forma transparente** em `cronograma.md`, `plano-riscos.md` (risco R-007) e `status-report-2026-06-11.md` (ISS-008), e corresponde à Condição Requerida #3 da Vera Veredito. Não é uma inconsistência "escondida", mas **permanece sem decisão formal registrada** — o que a mantém como NC-MOD em aberto até a decisão do Sponsor/GP em M0 (2026-06-24).

2. **Orçamento / CB-Orçamento (NC-MOD — NC-004)**: O TAP declara um teto "aprovado" de R$ 30.000, mas adota R$ 36.000 (com contingência de 20%) como BAC para fins de EVM nos KPIs e como referência no Plano de Riscos (R-004). A reconciliação entre o teto formalmente aprovado e o BAC operacional **não foi formalizada** — está registrada como CB-Orçamento (`qualificacao-aprovada.md`, recomendação do Gate de Qualificação) e como ISS-007 no Status Report, mas sem prazo definido ("A definir"). Condição Requerida #4 da Vera trata do mesmo gap pelo lado da reserva de riscos (R$ 26.800 vs R$ 6.000).

---

## D3 — Conformidade com Políticas VMO

| Política | Status | Detalhe |
|----------|--------|---------|
| Work Request emitido | ✅ | `02-iniciacao/work-request.md` existe, validado (`test -s` PASS no Step 9) |
| Artefato Obrigatório (10 grupos / 41 itens) | ✅ | Transcrito integralmente conforme task `criar-work-request.md` (verificado no Step 9) |
| Score Vera ≥ 85 | ⚠️ | Score obtido: **8,23/10 (= 82,3/100)**. Este valor **atende ao critério de aprovação vinculante de `pipeline/data/quality-criteria.md`** ("Aprovação global: Pontuação ponderada ≥ 7,0 E nenhum critério BLOCKING não atendido" — ambos satisfeitos, veredicto da Vera = APROVADO COM CONDIÇÕES, não REPROVADO). O limiar "85/100" citado em `pipeline/steps/step-12-revisao-qualidade.md` usa uma escala de 100 pontos não convertida explicitamente para a escala de 10 pontos de `quality-criteria.md` — **inconsistência entre dois documentos do framework VMO**, não do projeto. Classificado como **NC-MENOR (NC-006)**, registrada para ciência dos mantenedores do framework, não bloqueante para este projeto (a Vera aplicou corretamente o critério vinculante ≥7,0/10 que rege seu próprio veredicto). |
| CBs formalizadas no TAP | ✅ | `documentacao-base.md` referencia CB-1 a CB-6 e CB-Orçamento explicitamente nas seções de Restrições, Riscos de Alto Nível e Status do Documento |
| Sponsor mínimo Diretor+ documentado | ❌ | Ver D1/NC-001 — sponsor documentado, mas abaixo do nível mínimo e marcado como provisório |

---

## D4 — Completude da Documentação de Iniciação

| Documento | Arquivo | Existe | Conteúdo | Status |
|-----------|---------|--------|----------|--------|
| Demanda Coletada | `01-qualificacao/demanda-coletada.md` | ✅ | ✅ | OK |
| Qualificação | `01-qualificacao/qualificacao.md` | ✅ | ✅ (50/100, APROVADO COM CONDIÇÕES) | OK |
| Gate de Qualificação | `01-qualificacao/gate-qualificacao.md` | ✅ | ✅ (Veredicto PASS) | OK |
| Qualificação Aprovada (checkpoint) | `01-qualificacao/qualificacao-aprovada.md` | ✅ | ✅ (aprovado por Marcelo Silveira, GP VMO) | OK |
| Documentação Base (TAP+Canvas+Plano Geral) | `02-iniciacao/documentacao-base.md` | ✅ | ✅ | OK |
| Requisitos (ERF) | `02-iniciacao/requisitos.md` | ✅ | ✅ (22 RF + 9 RNF, MoSCoW) | OK |
| Work Request | `02-iniciacao/work-request.md` | ✅ | ✅ (10 grupos / 41 itens) | OK |
| Cronograma + WBS | `03-planejamento/cronograma.md` | ✅ | ✅ (3+ níveis, M0-M5, caminho crítico) | OK |
| Plano de Riscos | `03-planejamento/plano-riscos.md` | ✅ | ✅ (9 riscos, reserva R$ 26.800) | OK |
| Framework de KPIs | `03-planejamento/kpis.md` | ✅ | ✅ (CPI/SPI/EAC/VAC, semáforo 5 dimensões) | OK |
| Status Report Inicial | `04-monitoramento/status-report-2026-06-11.md` | ✅ | ✅ (semáforo, 9 issues, pesquisa de satisfação) | OK |
| Revisão Final (Vera) | `05-encerramento/revisao-final.md` | ✅ | ✅ (8,23/10, APROVADO COM CONDIÇÕES) | OK |

**D4: 12/12 documentos presentes e com conteúdo. Nenhuma NC.**

---

## D5 — Riscos de Governança

| Risco | Coberto no plano | Classificação |
|-------|-----------------|---------------|
| Sponsor ausente/insuficiente | ✅ — R-001 (Governança/Stakeholders, score 15/ALTO), trigger e plano de resposta vinculados a CB-1/CB-2 | — |
| Orçamento não aprovado | ✅ — R-004 (Financeiro, score 12/ALTO), trigger vinculado a CB-Orçamento | — |
| Mudança de escopo sem controle formal | ✅ — R-008 (Escopo, score 6/MÉDIO), com plano de resposta referenciando necessidade de CR formal (Gabriel Governança) em caso de alteração | — |

**D5: 3/3 riscos de governança obrigatórios cobertos. Nenhuma NC.**

---

## Consolidado de Não-Conformidades

| ID | Domínio | Descrição | Tipo | Ação Corretiva | Responsável | Prazo |
|----|---------|-----------|------|----------------|-------------|-------|
| NC-001 | D1 | Sponsor (Nubia Carla Freitas Santos Souza, Gerente Contábil) está abaixo do nível mínimo Diretor+ exigido pela política VMO; CB-1 (aprovação formal de Diretoria) sem evidência documental de resolução | **CRÍTICA** | Diretoria da área solicitante formaliza aprovação do TAP (CB-1), com registro escrito (e-mail, ata ou assinatura formal) anexado ao pacote do projeto. Alternativamente, a Diretoria emite delegação formal de autoridade de sponsor a Nubia Carla Freitas Santos Souza, documentada por escrito | Tatiane Dias de Moraes / Projetos DTI (conforme `qualificacao-aprovada.md`) | 2026-06-13 |
| NC-002 | D1 | Gerente de Projeto não designado no TAP ("A designar pelo SQUAD PM/MM") | MODERADA | SQUAD PM/MM designa o GP responsável e atualiza o TAP (campo "Gerente de Projeto") para v1.1 | SQUAD PM/MM (Time de Sustentação ERP) | 2026-06-13 |
| NC-003 | D2 | Divergência de prazo entre TAP (2026-09-30) e Cronograma com buffer de 15% (2026-10-10), ~10 dias, sem decisão formal registrada | MODERADA | GP VMO + Sponsor decidem entre comprimir cronograma (via resultado de CB-5) ou formalizar aditivo de prazo do TAP para 2026-10-10; registrar decisão por escrito (anexo ao TAP v1.1) | GP VMO (a designar — ver NC-002) + Sponsor | 2026-06-24 (M0) |
| NC-004 | D2 | CB-Orçamento (R$ 30.000 teto aprovado vs. R$ 36.000 BAC com contingência) sem prazo de resolução definido e sem reconciliação formal | MODERADA | GP VMO + Sponsor formalizam, por escrito, qual valor é o teto orçamentário vigente do projeto, e como o gap de R$ 6.000 (e o gap adicional de R$ 20.800 de exposição a risco — Condição #4 da Vera) será tratado | GP VMO + Sponsor | 2026-06-24 (M0) |
| NC-005 | D3 | Inconsistência de escala entre `step-12-revisao-qualidade.md` ("mínimo 85/100") e `quality-criteria.md` ("Aprovação global ≥ 7,0/10") — documentos do framework VMO, não do projeto | MENOR | Atualizar `step-12-revisao-qualidade.md` para referenciar a escala de 0-10 de `quality-criteria.md` (ou converter explicitamente: 85/100 → 8,5/10) | Mantenedores do framework VMO Autônomo | Sem prazo (não bloqueia este projeto) |

**Total NC-CRÍTICAS:** 1 | **Total NC-MOD:** 3 (NC-002, NC-003, NC-004) | **Total NC-MENORES:** 1 (NC-005)

> Pela política VMO, tanto a presença de **1 NC-CRÍTICA** quanto a **acumulação de 3 NC-MOD** são, isoladamente, suficientes para o veredicto BLOQUEADO. Ambas as condições estão presentes.

---

## Recomendações para a Fase de Execução

1. **Não iniciar a Onda 1 (mobilização do SQUAD PM/MM) antes da resolução de NC-001 e NC-002** — iniciar execução sem sponsor formalizado e sem GP designado reproduz exatamente o padrão de falha que a governança VMO existe para prevenir (Princípio 1 de Gabriel Governança).
2. **Tratar NC-003 e NC-004 como uma única decisão de M0**: ambas decorrem da mesma causa raiz (estimativa de R$ 30.000 / cronograma sem buffer foi otimista frente à realidade de caminho crítico com folga zero e item 13 complexo). Uma decisão conjunta (ex.: "aceitar prazo até 2026-10-10 e BAC de R$ 36.000, formalizando ambos como nova baseline") resolve as duas NCs com um único registro.
3. **Reagendar a reauditoria de governança para 2026-06-13** (prazo de NC-001/NC-002) — não é necessário reexecutar a Vera Veredito (conteúdo documental já aprovado), apenas verificar evidência de resolução das NCs CRÍTICA e MODERADAS de D1.
4. **Registrar NC-005 no backlog de manutenção do framework VMO** (`squads/vmo-autonomo/_memory/`), fora do escopo deste projeto.

---

## Próximo Passo

Esta auditoria classifica o projeto como **BLOQUEADO para autorização de execução** — mas o bloqueio é de **governança externa (CB-1/CB-2/designação de GP)**, não de qualidade ou completude documental (D3 e D4 plenamente atendidos, D2 com 2 NC-MOD já transparentemente documentadas e com plano de decisão definido para M0).

**Não recomendo o `on_reject: 5`** (retorno a Diana Documento para retrabalho de TAP/Canvas/Plano Geral) **como encaminhamento mecânico**, pois nenhuma das NC-CRÍTICA/MOD identificadas é corrigível por reescrita de documentação — todas dependem de ações de governança externas ao squad VMO Autônomo (Diretoria, SQUAD PM/MM, Sponsor).

Encaminho para o **Step 16 — Checkpoint de Aprovação Final**, onde o usuário/GP VMO deve decidir entre:
- **(a)** Registrar o estado atual como "Iniciação documentada e revisada — Execução BLOQUEADA pendente de NC-001/NC-002 (prazo 2026-06-13)", encerrando este ciclo do pipeline com reauditoria agendada para 2026-06-13; ou
- **(b)** Confirmar que CB-1/CB-2/designação de GP já foram resolvidas por canal externo ao pipeline (com evidência), permitindo a Gabriel emitir um adendo de reauditoria nesta mesma sessão; ou
- **(c)** Autorizar formalmente uma exceção de governança (waiver), assinada pelo GP VMO, registrando a ciência do risco de prosseguir com sponsor provisório — prática que Gabriel desaconselha (Anti-Pattern "Autorizar kick-off com CB em aberto"), mas que permanece prerrogativa do GP VMO.

---

*Auditoria realizada por Gabriel Governança — Auditor de Governança VMO*
*Documentos consultados: `qualificacao-aprovada.md`, `documentacao-base.md`, `requisitos.md`, `cronograma.md`, `plano-riscos.md`, `kpis.md`, `work-request.md`, `status-report-2026-06-11.md`, `revisao-final.md`*
