# Parecer de Qualificação — DEM-2026-007
## INT015: Integração GRLOG-SAP — Faturamento Integrado por Medições Aprovadas

**ID:** DEM-2026-007 | **Data:** 2026-05-24 | **Analista:** Felipe Filtro (VMO Autônomo)
**Projeto:** PROJ-2026-007

---

## Resumo Executivo

A Diretoria de Logística Dedicada (VIX Matriz) solicita a integração INT015 entre o GRLOG (Sistema de Gestão de Receita) e o SAP ERP para automatizar o ciclo completo de faturamento a partir de medições realizadas e aprovadas — emissão de NFSe, Recibo, Nota de Débito e retorno dos documentos ao GRLOG. A demanda tem embasamento regulatório (CPC 47 / IFRS 15), criticidade Emergencial declarada e origem executiva (CEO do Grupo Águia Branca).

**Decisão: APROVADO COM CONDIÇÕES** — 5 condições bloqueantes devem ser resolvidas antes do início formal do projeto.

---

## Claims de Alto Risco Identificados

| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "Projeto semelhante já implantado no GAB" (WAVE, Plataforma de Venda de Ativos) | PARCIAL — mencionado no ticket, sem documentação técnica comparativa | Critério 2: teto rebaixado para 5/10 até confirmação de aderência arquitetural |
| "Investimento menor de R$10K" | NÃO — sem memória de cálculo, sem estimativa por fase | Critério 3: estimativa suspeita para integração bidirecional com 4 fluxos; confiança BAIXA |
| "Área possui escopo detalhado" | PARCIAL — declarado no ticket, documento não anexado | Critério 5: maturidade penalizada até recebimento do escopo |
| "Não impacta outras divisões" | PARCIAL — Holding DTI envolvida como grupo solucionador | Critério 8: declaração contradiz participação ativa da Holding |

---

## Critérios de Qualificação

### Critérios 1–6: Valor da Demanda

**1. Alinhamento Estratégico — 9/10**
Evidência disponível: **SIM**
Duplo embasamento: (a) conformidade com CPC 47 / IFRS 15 — norma contábil de reconhecimento de receita com exigência legal (Fonte F5); (b) determinação direta da CEO do Grupo Águia Branca (Fonte F6). Alinhamento não declarativo — é requisito de compliance e diretriz executiva de primeiro escalão. Confiança: ALTA. Nota 9 (não 10): ausência de OKR corporativo documentado conectando esta integração a uma meta de resultado mensurável.

**2. Viabilidade Técnica — 5/10**
Evidência disponível: **PARCIAL**
Integração bidirecional GRLOG↔SAP com 4 fluxos distintos: geração de ordem de vendas, emissão de NFSe, emissão de Recibo, contabilização de Nota de Débito + retorno ao GRLOG. Claim de replicação (WAVE / Plataforma de Venda de Ativos) sem documentação técnica comparativa — nenhum documento de arquitetura, API ou mapeamento de campos disponível. A premissa P-01 ("GRLOG já possui os dados base") é declaratória e não validada. Teto 5/10 aplicado. Para revisar esta nota: "Qual é a documentação técnica (spec de API, mapeamento de campos, fluxo AS-IS da integração WAVE) que pode ser reaproveitada para a INT015?"

**3. Retorno sobre Investimento — 4/10**
Evidência disponível: **NÃO**
Benefícios descritos qualitativamente sem quantificação de baseline ou valor anual. Estimativa de investimento de "menos de R$10K" é suspeita: integração bidirecional com dois sistemas ERP core envolvendo fluxos de ordens de vendas e emissão de documentos fiscais raramente se resolve em menos de 80–120h de desenvolvimento (≥ R$12K–18K considerando hora técnica Basis/ABAP). Confiança: BAIXA. Para revisar: "Qual é o volume mensal de medições/faturamentos processados? Qual foi o custo de desenvolvimento da integração WAVE (benchmark)?"

**4. Urgência — 7/10**
Evidência disponível: **SIM (parcial)**
Três sinais concretos: (a) SLA do chamado já em atraso 18h05 desde 13/05/2026; (b) demanda originada pela CEO — pressão executiva ativa; (c) conformidade CPC 47/IFRS 15 — risco regulatório com impacto em demonstrativos. Nota rebaixada de 9 para 7: prazo concreto esperado pela CEO não declarado (L-09); data-limite de conformidade não especificada; consequência financeira da inação não quantificada. Para revisar: "Qual é a data que a CEO espera para entrega operacional? Existe prazo de auditoria ou fechamento fiscal que define o limite da norma?"

**5. Maturidade da Demanda — 4/10**
Evidência disponível: **PARCIAL**
Problema de negócio bem identificado (necessidade de conformidade regulatória + automação do faturamento). No entanto: (a) processo AS-IS não documentado; (b) escopo detalhado declarado como existente mas não disponibilizado; (c) sponsor não identificado; (d) descrição técnica de uma página insuficiente para estimativa de esforço de integração ERP. Para revisar: "Envie o documento de escopo detalhado mencionado no ticket. Sem ele a qualificação técnica fica comprometida."

**6. Disponibilidade de Recursos — 3/10**
Evidência disponível: **NÃO**
Três lacunas simultâneas: (a) investimento estimado em <R$10K sem aprovação formal — e provavelmente subestimado; (b) responsável técnico não designado no Projetos DTI; (c) disponibilidade das equipes de GRLOG e SAP Basis não confirmada. O chamado permanece 11 dias sem nenhuma ação após abertura, possivelmente indicando baixa prioridade operacional — contradição com criticidade Emergencial declarada.

### Critérios 7–10: Complexidade de Execução

**7. Esforço Estimado — 8/10**
Evidência disponível: **PARCIAL**
Estimativa preliminar sem escopo técnico disponível: levantamento/análise (40–60h) + desenvolvimento GRLOG (60–100h) + configuração/desenvolvimento SAP SD/FI (60–100h) + testes de integração (40–60h) + go-live/suporte (20–30h) = **220–350h totais** (confiança BAIXA). Muito acima de 160h → confirma classificação como PROJETO. Nota 8 (não 10): estimativa dedutiva — sem acesso ao escopo técnico ou arquitetura existente dos sistemas.

**8. Impacto Organizacional — 7/10**
Evidência disponível: **SIM (com ressalva)**
Impacto documentado: VIX Matriz (operação GRLOG), Diretoria de Logística Dedicada, Holding DTI (Projetos DTI + Cassio Ribeiro Rosa). Mudança de processo: faturamento passa de execução manual para fluxo integrado disparado por medições aprovadas — mudança de comportamento para usuários GRLOG e área fiscal. Claim "não impacta outras divisões" contradiz participação ativa da Holding DTI; avaliado como PARCIALMENTE VERIFICADO.

**9. Governança Necessária — 8/10**
Evidência disponível: **SIM**
Projeto de integração ERP com conformidade regulatória, visibilidade executiva (CEO), múltiplos sistemas core, múltiplos stakeholders, esforço acima de 220h. Requer formalmente: TAP com sponsor executivo, cronograma com marcos de validação, plano de riscos técnicos e de integração, gestão de stakeholders e controle de qualidade dos documentos fiscais gerados. Não pode ser gerido informalmente pelo time técnico.

**10. Impacto Regulatório/Financeiro — 9/10**
Evidência disponível: **SIM**
CPC 47 / IFRS 15 — norma de reconhecimento de receita adotada compulsoriamente por empresas com demonstrativos auditados. Não conformidade pode implicar: reapresentação de demonstrações financeiras, qualificação do relatório de auditoria independente, notificações de reguladores, impacto em credores e investidores. Fluxo de emissão de documentos fiscais (NFSe, Nota de Débito) adiciona risco de compliance fiscal e tributário. Nota 9 (não 10): impacto financeiro já materializado não quantificado — custo de inação não declarado pelo solicitante.

---

## Resultado

```
 1. Alinhamento Estratégico        9/10
 2. Viabilidade Técnica            5/10
 3. ROI                            4/10
 4. Urgência                       7/10
 5. Maturidade da Demanda          4/10
 6. Disponibilidade de Recursos    3/10
 7. Esforço Estimado               8/10
 8. Impacto Organizacional         7/10
 9. Governança Necessária          8/10
10. Impacto Regulatório/Financeiro 9/10
                                ────────
                                64/100 (64%)
```

**CLASSIFICAÇÃO: PROJETO**
Critérios 7–10: Esforço (8), Impacto Org. (7), Governança (8), Regulatório (9) — todos ≥ 7/10. A integração bidirecional GRLOG↔SAP com 4 fluxos funcionais, conformidade regulatória obrigatória e impacto em múltiplas áreas/sistemas configura inequivocamente um projeto formal. Tratamento como melhoria de sustentação ERP seria subestimação estrutural com risco elevado de estouro de escopo e prazo.

**DECISÃO: APROVADO COM CONDIÇÕES**
Pontuação 64% (faixa 50–74%). A demanda tem fundamento sólido (alinhamento regulatório + urgência executiva), mas apresenta cinco condições bloqueantes que, se não resolvidas, criam risco elevado de fracasso na execução.

---

## Análise Comercial

### Benefícios Esperados

| Benefício | Valor Estimado | Prazo Realização | Confiança |
|-----------|----------------|-----------------|-----------|
| Redução de retrabalho manual de faturamento (est. 1,5 FTE × 20% reaproveitamento) | R$ 18.000–30.000/ano | 3 meses pós go-live | BAIXA |
| Eliminação de atrasos de faturamento (receita pendente) | Não quantificado | Imediato no go-live | BAIXA |
| Redução de risco regulatório CPC 47/IFRS 15 (custo de auditoria qualificada) | R$ 50.000–200.000/evento | Permanente | MÉDIA |
| Aumento de produtividade por emissão diária por usuário | Não quantificado | 3 meses pós go-live | BAIXA |

**Total de benefícios anuais estimados: R$ 68.000–230.000/ano** (confiança BAIXA — ausência de dados de baseline torna o intervalo muito amplo)

### Custo do Projeto (estimativa preliminar — sujeita a revisão do escopo)

| Item | Estimativa |
|------|------------|
| Levantamento e análise (GRLOG + SAP Basis) | R$ 6.000–9.000 |
| Desenvolvimento GRLOG (4 fluxos + retorno) | R$ 9.000–15.000 |
| Configuração/desenvolvimento SAP SD/FI | R$ 9.000–15.000 |
| Testes integrados (ciclo completo) | R$ 6.000–9.000 |
| Go-live e suporte pós-implantação | R$ 3.000–4.500 |
| Documentação técnica | R$ 2.000–3.000 |
| Contingência 20% | R$ 7.000–11.100 |
| **TOTAL** | **R$ 42.000–66.600** |

> ⚠️ **Alerta de subestimação**: A estimativa do solicitante de "menos de R$10K" representa 15–25% do custo estimado acima. A discrepância deve ser esclarecida antes do TAP. Possível causa: custo interno não precificado, ou subestimação da complexidade dos 4 fluxos de integração.

### Métricas de Retorno

- Payback estimado (conservador): ~9,5 meses (custo R$54K / benefício R$68K/ano)
- Payback estimado (otimista): ~2,2 meses (custo R$42K / benefício R$230K/ano)
- Nível de confiança geral: **BAIXA** — intervalo muito amplo para recomendação gerencial precisa

### Custo de Não-Fazer

Manutenção do processo manual com: (a) risco contínuo de não conformidade com CPC 47/IFRS 15 — exposição a auditoria qualificada e impactos em credores e reguladores; (b) faturamento pendente acumulado — receita reconhecida fora do período correto; (c) retrabalho operacional mantido indefinidamente; (d) desobediência a determinação da CEO com impacto no credencial do PMO junto à liderança.

### Proposta de Valor

> "O projeto INT015, com investimento estimado entre R$42K e R$67K (revisão do budget <R$10K declarado é necessária), automatizará o ciclo completo de faturamento a partir das medições aprovadas no GRLOG — gerando ordens de vendas no SAP e emitindo NFSe, Recibo e Nota de Débito com retorno automático ao GRLOG. Além de eliminar retrabalho operacional e atrasos de faturamento, o projeto garante conformidade com CPC 47 / IFRS 15, protegendo o Grupo Águia Branca de risco de auditoria qualificada em demonstrativos financeiros. Alinhado à determinação da CEO e de alta urgência regulatória."

---

## Condições Bloqueantes

- **CB-01:** Identificar e confirmar sponsor formal com nível mínimo de Diretor — sem sponsor, TAP não pode ser aprovado e decisões de escopo ficam sem autoridade decisória. **Responsável:** Projetos DTI / Jairo De Melo Ferreira Mendes. **Prazo:** 48h.
- **CB-02:** Iniciar e concluir rito de aprovação orçamentária — budget de <R$10K precisa ser revisado para R$42K–R$67K (estimativa preliminar). **Responsável:** Jairo / Financeiro GAB. **Prazo:** 5 dias úteis.
- **CB-03:** Enviar documento de escopo detalhado declarado como existente — insumo mínimo para TAP e ERF. **Responsável:** Jairo De Melo Ferreira Mendes. **Prazo:** 24h.
- **CB-04:** Declarar prazo esperado pela CEO para entrega operacional da integração — sem este dado, o cronograma não pode ser elaborado. **Responsável:** Jairo / Projetos DTI. **Prazo:** 24h.
- **CB-05:** Nomear responsável técnico no Projetos DTI e confirmar disponibilidade de equipes GRLOG e SAP Basis. **Responsável:** Gestor do Projetos DTI. **Prazo:** 24h.

## Próximos Passos

| Ação | Responsável | Prazo Sugerido |
|------|-------------|----------------|
| Nomear responsável técnico no chamado #6813896 | Gestor Projetos DTI | 24h |
| Enviar documento de escopo detalhado ao VMO | Jairo De Melo Ferreira Mendes | 24h |
| Declarar prazo comprometido pela CEO | Jairo De Melo Ferreira Mendes | 24h |
| Identificar e confirmar sponsor formal (Diretor+) | Projetos DTI / VMO | 48h |
| Revisar e iniciar aprovação do orçamento real (>R$10K) | Jairo / Financeiro GAB | 5 dias úteis |
| Iniciar elaboração do TAP após CB-01 a CB-05 resolvidas | Diana Documento / VMO | Após CBs |

---

*Parecer emitido por Felipe Filtro — Analista de Qualificação (VMO Autônomo)*
*Data: 2026-05-24 | DEM-2026-007 | PROJ-2026-007*
