# Plano de Gestão de Riscos — DEM-2026-007
Projeto: Implantação DDA SAP — VAB Matriz
Elaborado por: Pedro Perigo (VMO Autônomo)
Data: 2026-05-20
Versão: 1.0

Escala de Probabilidade: BAIXA (1–3) / MÉDIA (4–6) / ALTA (7–9) | 1–9
Escala de Impacto: BAIXO (1–3) / MÉDIO (4–6) / ALTO (7–9) | 1–9
Score = Probabilidade × Impacto | Nível: CRÍTICO (≥49) / ALTO (25–48) / MÉDIO (10–24) / BAIXO (<10)

---

## Registro de Riscos

| ID | Categoria | Descrição | P | I | Score | Nível |
|----|-----------|-----------|---|---|-------|-------|
| R-001 | Governança | Autorização do Holding (Walace Bacelar) torna-se inválida se houver qualquer custo externo — kickoff precisa ser sustado e autorização renegociada | 7 | 8 | 56 | **CRÍTICO** |
| R-002 | Técnico | "Ajustes necessários" (CB-2) revelam-se mais complexos que parametrização, exigindo desenvolvimento ABAP novo — reclassificação para PROJETO e novo ciclo de planejamento | 5 | 8 | 40 | **ALTO** |
| R-003 | Externo | Processo de habilitação DDA no Santander demora mais que os 15 dias estimados, atrasando o caminho crítico | 5 | 6 | 30 | **ALTO** |
| R-004 | Técnico | Ambiente SAP FI da VAB Matriz difere da Divisão Logística de forma não antecipada (versão, configuração base, transportes) | 3 | 7 | 21 | **MÉDIO** |
| R-005 | Governança | Sponsor Diretor+ não é identificado antes do kick-off — decisões de escopo/custo ficam sem alçada formal | 5 | 6 | 30 | **ALTO** |
| R-006 | Pessoas | Recurso técnico DTI designado não tem disponibilidade suficiente ou conhecimento em FEBAN/DDA | 4 | 7 | 28 | **ALTO** |
| R-007 | Pessoas | Resistência ou baixa participação da equipe CP da VAB no UAT e treinamento | 2 | 4 | 8 | **BAIXO** |
| R-008 | Técnico | Layout CNAB 240 do Santander para a conta VAB difere do layout já configurado na Divisão Logística | 3 | 6 | 18 | **MÉDIO** |
| R-009 | Processo | Mudança de escopo não controlada durante a fase de levantamento técnico (scope creep via "ajustes" adicionais) | 4 | 5 | 20 | **MÉDIO** |
| R-010 | Processo | Encerramento do projeto sem documentação técnica finalizada — próxima manutenção sem referência | 2 | 5 | 10 | **MÉDIO** |

---

## Plano de Resposta por Risco

---

### R-001 — Autorização Holding inválida se houver custo externo
**Nível:** CRÍTICO | P: 7 | I: 8 | Score: 56
**Estratégia:** MITIGAR + EVITAR

**Trigger:** Qualquer indicação de custo externo durante o levantamento técnico (E-01) ou contratação de serviço externo.

**Ações de mitigação:**
1. Executar o projeto com horas internas DTI exclusivamente (meta custo zero)
2. No artefato obrigatório do WR (G6), confirmar viabilidade de custo zero antes do kick-off
3. Se E-01 identificar necessidade de custo externo, PARAR antes de qualquer gasto e:
   a. Quantificar o custo exato
   b. Levar ao Gladston para aprovação
   c. Contatar Walace Bacelar (Holding) para nova autorização formal
4. Não contratar nenhum serviço externo sem nova autorização do Holding, independentemente do valor

**Plano de contingência:** Se Holding não re-autorizar o custo → projeto vai para EM ESPERA até
solução sem custo externo ser encontrada OU até nova janela de orçamento.

**Responsável:** GP + Gladston Campos
**Prazo de mitigação:** Antes e durante todo o projeto (monitoramento contínuo)

---

### R-002 — Ajustes mais complexos que parametrização (CB-2)
**Nível:** ALTO | P: 5 | I: 8 | Score: 40
**Estratégia:** MITIGAR

**Trigger:** E-01 (levantamento técnico) identifica necessidade de desenvolvimento ABAP, novo
programa Z, ou modificação de objeto SAP standard para implementar o DDA na VAB.

**Ações de mitigação:**
1. Priorizar o levantamento técnico (Fase 2) como primeira atividade do projeto
2. Na reunião com a Div. Logística, verificar explicitamente: houve desenvolvimento ABAP?
3. Se E-01 identificar necessidade de desenvolvimento:
   a. Estimar esforço total (incluindo desenvolvimento)
   b. Atualizar classificação do projeto (MELHORIA → PROJETO) formalmente
   c. Apresentar nova qualificação ao VMO antes de prosseguir
   d. Verificar impacto no custo (re-acionamento da CB-3 e R-001)

**Plano de contingência:** Reclassificação como PROJETO → novo ciclo de planejamento com
TAP revisado, cronograma revisado e aprovação do sponsor.

**Responsável:** Recurso técnico DTI + GP
**Prazo de mitigação:** M-1 (27/06/2026) — decisão definitiva no E-01

---

### R-003 — Habilitação DDA Santander demorada
**Nível:** ALTO | P: 5 | I: 6 | Score: 30
**Estratégia:** MITIGAR

**Trigger:** Santander não confirmar habilitação DDA até 18/07/2026 (M-2 previsto).

**Ações de mitigação:**
1. Iniciar processo de habilitação no banco no primeiro dia do kick-off (3.1 no cronograma)
2. Identificar o contato Santander (gerente de conta corporativo VAB) antes do kick-off
3. Solicitar ao Santander prazo formal de habilitação em resposta ao pedido
4. Monitorar semanalmente o status da habilitação
5. Escalar para Noemia/tesouraria VAB se Santander não responder em 5 dias úteis

**Plano de contingência:** Atraso de até 2 semanas é absorvido pelo buffer de setembro.
Atraso acima de 2 semanas → revisar data de go-live e comunicar ao sponsor.

**Responsável:** Noemia Tambara (ponto focal bancário) + GP
**Prazo de mitigação:** Início em 30/06/2026; M-2 monitorado semanalmente

---

### R-004 — Ambiente SAP VAB difere da Divisão Logística
**Nível:** MÉDIO | P: 3 | I: 7 | Score: 21
**Estratégia:** MITIGAR

**Trigger:** Levantamento técnico (2.1) identifica divergência de versão SAP, patch level,
configuração base do FI ou transporte de customizações que impeça replicação direta.

**Ações de mitigação:**
1. Incluir na agenda do levantamento (2.1) verificação explícita de versão e patch level SAP
2. Solicitar print da versão SAP do ambiente VAB antes da reunião de análise
3. Se divergência identificada: avaliar impacto antes de iniciar qualquer configuração

**Plano de contingência:** Divergência leve (patch level) → ajuste na configuração (+2–5 dias).
Divergência severa (versão principal) → reclassificação escopo e notificação ao sponsor.

**Responsável:** Recurso técnico DTI
**Prazo de mitigação:** M-1 (27/06/2026)

---

### R-005 — Sponsor sem alçada Diretor+ (CB-Sponsor)
**Nível:** ALTO | P: 5 | I: 6 | Score: 30
**Estratégia:** MITIGAR

**Trigger:** Gate de kick-off ocorre sem identificação de sponsor Diretor+.

**Ações de mitigação:**
1. CB-Sponsor é condição obrigatória do gate de kick-off (Gabriel Governança verifica)
2. Gladston Campos deve identificar ou acionar um Diretor+ antes do kick-off
3. Se impossível: formalizar e-mail de ciência de um Diretor+ como patrocinador da decisão

**Plano de contingência:** Gate de kick-off bloqueado até resolução — não há contingência
que substitua um sponsor com autoridade formal.

**Responsável:** Gladston Campos → escalada ao Diretor de TI/negócio VAB
**Prazo:** Antes do gate de kick-off (06/06/2026)

---

### R-006 — Recurso técnico DTI sem disponibilidade ou conhecimento
**Nível:** ALTO | P: 4 | I: 7 | Score: 28
**Estratégia:** MITIGAR

**Trigger:** Recurso designado tem < 50% de disponibilidade para o projeto OU não tem
experiência com FEBAN/integração bancária SAP.

**Ações de mitigação:**
1. No artefato do WR (G3), confirmar disponibilidade e perfil técnico antes do kick-off
2. Exigir que o recurso designado tenha ao menos familiaridade com FEBAN ou DDA SAP
3. Incluir sessão de transferência de conhecimento com o recurso da Div. Logística

**Plano de contingência:** Recurso inadequado → solicitar substituição ao DTI antes do
início da Fase 2 (levantamento técnico).

**Responsável:** Gladston Campos + GP
**Prazo:** Confirmado em M-0 (gate de kick-off)

---

### R-007 — Resistência da equipe CP ao UAT e treinamento
**Nível:** BAIXO | P: 2 | I: 4 | Score: 8
**Estratégia:** ACEITAR com monitoramento

**Trigger:** Equipe CP recusa participação no UAT ou treinamento sem justificativa.

**Ações:** Comunicação antecipada dos benefícios para a equipe. Noemia como facilitadora
da participação. Treinamento de duração máxima de 0,5 dia para minimizar impacto operacional.

**Responsável:** Noemia Tambara + GP

---

### R-008 — Layout CNAB 240 Santander diverge da Divisão Logística
**Nível:** MÉDIO | P: 3 | I: 6 | Score: 18
**Estratégia:** MITIGAR

**Trigger:** Layout CNAB 240 enviado pelo Santander para a conta VAB difere do que está
configurado no sistema da Divisão Logística (campos adicionais, posições diferentes).

**Ações de mitigação:** Solicitar ao Santander o manual do layout CNAB 240 DDA antes do início
da configuração. Comparar com o layout da Div. Logística durante o levantamento (2.1).

**Plano de contingência:** Divergência pequena → ajuste de mapeamento CNAB (+3–5 dias).
Divergência grande → avaliar desenvolvimento ABAP (aciona R-002 e potencialmente R-001).

**Responsável:** Recurso técnico DTI
**Prazo de mitigação:** M-1 (27/06/2026)

---

### R-009 — Scope creep durante o levantamento técnico
**Nível:** MÉDIO | P: 4 | I: 5 | Score: 20
**Estratégia:** MITIGAR

**Trigger:** Noemia ou equipe CP solicita funcionalidades adicionais durante o levantamento
(ex: integração com outros bancos, relatórios extras, automação adicional de AP).

**Ações de mitigação:** TAP com escopo excluso explícito. GP responsável por documentar
qualquer solicitação fora do escopo e tratar como Change Request. Noemia ciente do escopo
delimitado antes do início do levantamento.

**Responsável:** GP
**Prazo:** Monitoramento durante toda a Fase 2

---

### R-010 — Encerramento sem documentação técnica
**Nível:** MÉDIO | P: 2 | I: 5 | Score: 10
**Estratégia:** MITIGAR

**Trigger:** Go-live ocorre mas E-09 (documentação técnica) não é entregue antes do encerramento.

**Ações de mitigação:** E-09 é critério de aceite do encerramento — sem documentação não há
aceite formal. Documentação iniciada durante a fase de configuração (não somente ao final).

**Responsável:** Recurso técnico DTI + GP
**Prazo:** Entregue antes da reunião de encerramento (M-6)

---

## Reserva de Contingência Calculada

| ID | Risco | Probabilidade | Impacto (dias) | Valor Esperado (dias) |
|----|-------|--------------|---------------|----------------------|
| R-001 | Autorização Holding | 0,7 | 15 dias de parada | 10,5 dias |
| R-002 | Ajustes complexos ABAP | 0,5 | 20 dias | 10,0 dias |
| R-003 | Santander demorado | 0,5 | 10 dias | 5,0 dias |
| R-004 | Ambiente SAP divergente | 0,3 | 5 dias | 1,5 dias |
| R-005 | Sponsor sem alçada | 0,5 | 10 dias | 5,0 dias |
| R-006 | Recurso inadequado | 0,4 | 7 dias | 2,8 dias |
| R-008 | CNAB divergente | 0,3 | 5 dias | 1,5 dias |
| R-009 | Scope creep | 0,4 | 5 dias | 2,0 dias |
| **TOTAL** | | | | **38,3 dias** |

> **Interpretação:** O valor esperado de impacto em prazo, considerando todos os riscos, é
> de ~38 dias. O buffer de contingência do cronograma (setembro 2026 = ~26 dias úteis após
> go-live base de 25/08) cobre parcialmente este valor. Os riscos CRÍTICO (R-001) e ALTO
> (R-002, R-005) têm potencial de exceder o buffer se materializarem simultaneamente.

**Recomendação de reserva financeira:** R$2.000 (reserva orçamentária aprovada no TAP).
Se R-001 ou R-002 materializarem com custo externo: nova autorização obrigatória antes de
qualquer gasto (não coberto pela reserva — requer CR formal).

---

## Revisão de Riscos

| Quando | Evento | Responsável |
|--------|--------|-------------|
| Gate de Kick-off | Verificar R-001, R-002, R-005, R-006 | GP + Gabriel Governança |
| M-1 (27/06) | Verificar R-002, R-004, R-008 (pós-levantamento técnico) | GP |
| M-2 (18/07) | Verificar R-003 (habilitação Santander) | GP + Noemia |
| M-4 (15/08) | Verificar R-009, R-010 pós-UAT | GP |
| Quinzenal | Revisão geral do registro de riscos | GP |
| Evento de materialização | Notificação imediata ao sponsor | GP |
