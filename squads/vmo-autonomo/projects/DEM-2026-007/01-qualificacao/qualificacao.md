ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-007
Data: 2026-05-20 (Requalificação — v2)
Analista: Felipe Filtro (VMO Autônomo)

Histórico:
- v1 (2026-05-20): Decisão EM ESPERA (44/100) — 4 CBs identificadas
- v2 (2026-05-20): Requalificação com respostas às CBs. CB-4 eliminada (processo normal);
  CB-3 convertida em Risco + Gate de Kick-off; CB-1 parcialmente resolvida (existência confirmada,
  sem documentação formal); CB-2 reclassificada como item de descoberta técnica (fase de requisitos).

---

## Resumo da Demanda

A VAB Matriz solicita a automação do recebimento de boletos via DDA (Débito Direto Autorizado)
integrado ao SAP, eliminando o processo manual de impressão física e digitação de código de barras
pela equipe de Contas a Pagar. A solução é uma replicação do modelo em produção na Divisão
Logística (mesmo ambiente GAB) e na unidade VIX, com ajustes cuja natureza exata será determinada
na fase de requisitos. Integração: SAP x Santander. Aprovação gerencial: Gladston Campos
(incondicional, 06/05); Walace Bacelar/Holding (condicional a custo zero, 08/04 — gerenciada
como risco com gate de kick-off obrigatório).

---

## Claims de Alto Risco — Status Atualizado (v2)

| Claim | Fonte | Evidência disponível | Status v2 | Impacto na análise |
|-------|-------|---------------------|-----------|--------------------|
| "É só uma replicação" | E-mail Noemia | PARCIAL — existência confirmada na Div. Logística; sem documentação técnica formal; ajustes desconhecidos | ABERTO (CB-2 → fase de requisitos) | Viabilidade Técnica: sobe para 6/10 (existência real confirmada); Esforço: mantém 5/10 (incerteza em ajustes) |
| "Custo zero" | Autorização Walace | PARCIAL — ticket declara <R$10K, contradizendo premissa | CONVERTIDO EM RISCO + GATE KICK-OFF | Recursos: sobe para 6/10 — contradição gerenciada formalmente; kickoff não ocorre sem formalização |
| "Já está aprovado" | Gladston (incondicional) + Walace (condicional) | PARCIAL — Gladston: APROVADO sem ressalvas (real e operacional); Walace: condicional (gerenciado como gate) | RESOLVIDO PARCIALMENTE | Recursos: 6/10 |
| "Não impacta outras áreas" | Ticket solicitante | NÃO — afirmação do solicitante sem análise técnica | ABERTO | Impacto Organizacional: mantém 4/10 |
| "É urgente" / SLA em atraso | Ticket | NÃO — solicitante: Criticidade Normal | ABERTO | Urgência: mantém 3/10 |
| "Responsável técnico não designado = risco" | Gate intake | RESOLVIDO — processo padrão: DTI designa recurso após aceitação formal | ELIMINADO | Recursos: não penalizar por isso |

---

## Critérios de Qualificação — v2

### Valor da Demanda

**1. Alinhamento Estratégico   [6/10]** — sem alteração
Evidência disponível: PARCIAL
A demanda endereça automação financeira e eliminação de trabalho manual, alinhada a qualquer
objetivo de eficiência operacional ou transformação digital. O nome "Controladoria do Futuro"
(e-mail Noemia) sugere inserção em programa estratégico mais amplo, não confirmado (L9 em aberto).
O precedente da Div. Logística e VIX reforça o reconhecimento organizacional do valor da solução.
Sem OKR ou objetivo estratégico formal citado — regra: digitalização sem OKR específico = máximo
6/10. Mantido.

**2. Viabilidade Técnica   [6/10]** — subiu de 5
Evidência disponível: PARCIAL
Atualização v2: CB-1 esclarecida — a implementação DDA na Div. Logística foi confirmada como real
e em produção no mesmo ambiente GAB/SAP. Isso remove a dúvida sobre existência e eleva a confiança
técnica na viabilidade. A ausência de documentação formal não invalida o precedente — a solução
existe, funciona, e o ambiente é o mesmo. O que permanece em aberto: natureza dos "ajustes
necessários" para o CP da VAB (CB-2 → fase de requisitos), habilitação DDA no Santander VAB (L5).
A viabilidade técnica é plausível com confiança MÉDIA. Subiu de 5 para 6.
Para validar além de 6/10, precisamos de: levantamento técnico dos ajustes (fase de requisitos).

**3. Retorno sobre Investimento   [4/10]** — sem alteração
Evidência disponível: NÃO
Benefício qualitativo claro (eliminar impressão, digitação manual, dependência de terceiros).
Sem volume de boletos/mês (L3), ROI não pode ser calculado. Custo esperado <R$10K, mas não
formalizado. Confiança: BAIXA. Mantido.
Para revisar esta nota, precisamos de: volume mensal de boletos CP VAB por tipo (fornecedores,
tributos, outros).

**4. Urgência   [3/10]** — sem alteração
Evidência disponível: NÃO
Regra aplicada: sem data concreta + sem custo de inação quantificado = máximo 4/10. O próprio
solicitante classificou como Criticidade 3 - Normal. Sem evento de negócio associado. Desgaste
operacional real mas sem ruptura de processo. Nota reflete ausência de pressão temporal formal.
O que tornaria esta nota mais alta: data-limite com consequência financeira quantificada (ex:
fechamento fiscal, auditoria, perda de prazo contratual).

**5. Maturidade da Demanda   [5/10]** — subiu de 4
Evidência disponível: PARCIAL
Atualização v2: CB-2 reclassificada como item de descoberta técnica da fase de requisitos — a
ausência de especificação dos ajustes é esperada neste estágio para uma Melhoria Evolutiva, onde
a fase de requisitos (Rafael Requisito) é o momento correto para esse levantamento. O problema
está bem delimitado (processo manual de boletos no CP), a solução tem precedente real (Div.
Logística), e o escopo é definível pela equipe técnica. Atingiu o teto da regra: processo não
documentado + escopo não declarado = máximo 5/10. Subiu de 4 para 5.

**6. Disponibilidade de Recursos   [6/10]** — subiu de 3
Evidência disponível: PARCIAL
Atualização v2: dois fatores eliminados como penalizações incorretas:
— CB-4 removida: designação de recurso técnico DTI é processo padrão pós-aceitação formal; não
  é um gap de qualificação — é o próximo passo natural após aprovação;
— CB-3 convertida em Risco + Gate de Kick-off: a contradição entre a autorização condicional do
  Holding (custo zero) e a expectativa real (<R$10K) não é ausência de recursos — é um risco
  gerenciado formalmente, com kickoff bloqueado até formalização de custos.
O que permanece: orçamento não formalizado financeiramente (Gladston aprovou operacionalmente,
não financeiramente). Subiu de 3 para 6. Para chegar a 7, precisamos de: alocação orçamentária
formal ou confirmação de custo zero por quem vai executar.

---

### Complexidade de Execução

**7. Esforço Estimado   [5/10]** — sem alteração
Evidência disponível: NÃO
CB-2 permanece sem resposta — a natureza dos "ajustes necessários" é o determinante de esforço.
Sem essa informação, a amplitude 80–200h persiste. Nota reflete incerteza máxima para este claim.
Regra aplicada: claim de replicação sem documentação + estimativa por fase ausente = máximo 5/10.
Variável de classificação: se DTI confirmar ajustes como parametrização (sem desenvolvimento
ABAP) → esforço provável ~80-100h → Melhoria Evolutiva confirmada. Se ajustes exigirem
desenvolvimento → esforço >160h → reclassificar como Projeto.
Para revisar: levantamento técnico dos ajustes vs. solução Div. Logística (fase de requisitos).

**8. Impacto Organizacional   [4/10]** — sem alteração
Evidência disponível: PARCIAL
"Não impacta outras áreas" — declaração do solicitante sem análise técnica; claim de alto risco
não resolvido. Integração bancária envolve minimamente: equipe CP (mudança de processo), DTI
(execução), Santander (habilitação). Possível impacto em tesouraria/FI não avaliado. Teto 4/10.

**9. Governança Necessária   [5/10]** — sem alteração
Evidência disponível: PARCIAL
Multi-stakeholder (Holding + VAB + DTI + Santander) com tensão de autorização agora formalmente
gerenciada pelo gate de kick-off. A estrutura de governança ficou mais clara: Gladston =
aprovador de negócio; DTI = executor (recurso a ser designado); gate de kick-off = ponto de
controle de custo. Escopo restrito ao CP/VAB. Nível de governança adequado para Melhoria Evolutiva.

**10. Impacto Regulatório/Financeiro   [5/10]** — sem alteração
Evidência disponível: PARCIAL
Integração bancária (SAP x Santander) com risco de pagamentos incorretos por falha de
configuração ou layout CNAB. Sem requisito legal explícito, mas processo de pagamento sujeito
a auditoria contábil. Regra: integração bancária = mínimo 4/10. Mantido em 5/10.

---

## Resultado

**PONTUAÇÃO TOTAL: 49/100 (49%)**

| Critério | v1 | v2 | Δ | Evidência |
|----------|----|----|----|-----------|
| 1. Alinhamento Estratégico | 6 | 6 | — | PARCIAL |
| 2. Viabilidade Técnica | 5 | 6 | +1 | PARCIAL |
| 3. Retorno sobre Investimento | 4 | 4 | — | NÃO |
| 4. Urgência | 3 | 3 | — | NÃO |
| 5. Maturidade da Demanda | 4 | 5 | +1 | PARCIAL |
| 6. Disponibilidade de Recursos | 3 | 6 | +3 | PARCIAL |
| 7. Esforço Estimado | 5 | 5 | — | NÃO |
| 8. Impacto Organizacional | 4 | 4 | — | PARCIAL |
| 9. Governança Necessária | 5 | 5 | — | PARCIAL |
| 10. Impacto Regulatório/Financeiro | 5 | 5 | — | PARCIAL |
| **TOTAL** | **44/100** | **49/100** | **+5** | |

---

**CLASSIFICAÇÃO: MELHORIA EVOLUTIVA → Sustentação ERP FI** (classificação provisória)

Justificativa técnica: nenhum dos critérios 7–10 atingiu ≥ 7/10 individualmente (5/4/5/5).
Escopo declarado é o de ajuste funcional com base em solução existente — sem alteração estrutural
de processo de negócio. Área responsável: FI (processo de Contas a Pagar, integração bancária).
Nota de alerta: se o levantamento técnico dos ajustes (CB-2 — fase de requisitos) revelar
esforço >160h ou necessidade de desenvolvimento ABAP novo, reclassificar como PROJETO antes
do gate de kick-off.

**DECISÃO: EM ESPERA** (1 ponto abaixo do limiar de 50% para APROVADO COM CONDIÇÕES)

49/100 = 49% — 1 ponto abaixo do limiar. A última variável determinante é CB-2 (ajustes):
se o levantamento técnico confirmar ajustes como parametrização (sem desenvolvimento), o esforço
cai para ~80-100h e Maturidade/Esforço podem ser revisados para 6/5, levando o total a 51-53/100
(APROVADO COM CONDIÇÕES). Esta demanda não deve ser reprovada — o mérito existe e o pipeline
pode avançar para a fase de requisitos como condição de resolução de CB-2.

Recomendação pragmática: avançar para fase de requisitos com CB-2 aberta como condição de
confirmação de classificação, CB-3 como Condição de Kick-off obrigatória e CB-Sponsor a
resolver na iniciação.

---

## Condições Bloqueantes

- **CB-2 (aberta → fase de requisitos):** Natureza dos "ajustes necessários" para o CP da VAB
  em relação à solução da Div. Logística. A ser levantada por Rafael Requisito (Step 8) junto
  ao DTI. Resultado determina: (a) classificação MELHORIA vs. PROJETO; (b) esforço estimado
  por fase; (c) revisão da pontuação final antes do gate de kick-off.

- **CB-3 (convertida em Condição de Kick-off — OBRIGATÓRIA):** Formalização e alinhamento
  dos custos da implementação. Kickoff NÃO deve ocorrer sem: (a) confirmação escrita de custo
  real por quem vai executar; (b) nova autorização formal do Holding (Walace Bacelar) para o
  custo aprovado — independentemente de ser zero ou não. Registrar como risco ativo no plano
  de riscos (Pedro Perigo — Step 11).

- **CB-Sponsor (a resolver na iniciação):** Sponsor com nível Diretor+ não identificado.
  Gladston Campos é Gerente — decisões de escopo/custo podem não ter alçada suficiente.
  A resolver antes do gate de kick-off como condição de governança (Gabriel Governança).

---

## Condições de Avanço (para sair de EM ESPERA sem bloqueio completo)

A demanda pode avançar para as fases de documentação (Steps 7–13) com as seguintes condições:

1. **CB-2** será investigada por Rafael Requisito (Step 8) — resultado reclassifica ou confirma
2. **CB-3** é Condição de Kick-off — não bloqueia documentação, bloqueia execução
3. **CB-Sponsor** a resolver na iniciação antes do gate de kick-off

---

## Próximos Passos

| Ação | Responsável | Prazo | Fase |
|------|-------------|-------|------|
| Levantar natureza dos ajustes técnicos vs. Div. Logística | Rafael Requisito / DTI | Step 8 | Requisitos |
| Registrar risco de autorização Holding como risco ativo | Pedro Perigo | Step 11 | Planejamento |
| Identificar sponsor Diretor+ ou escalada da aprovação | Noemia / Gladston | Antes do kick-off | Iniciação |
| Formalizar custo e obter autorização Holding (re-autorização) | Noemia → Walace Bacelar | Antes do kick-off | Gate de Kick-off |
| Requalificação final (se CB-2 mudar classificação) | Felipe Filtro | Após Step 8 | Qualificação |
