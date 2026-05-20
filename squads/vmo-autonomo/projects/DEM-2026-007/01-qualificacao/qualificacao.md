ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-007
Data: 2026-05-20
Analista: Felipe Filtro (VMO Autônomo)

---

## Resumo da Demanda

A VAB Matriz solicita a automação do recebimento de boletos via DDA (Débito Direto Autorizado)
integrado ao SAP, eliminando o processo manual de impressão física e digitação de código de barras
pela equipe de Contas a Pagar. A solução seria uma replicação do modelo já operacional na Divisão
Logística do mesmo ambiente GAB e na unidade VIX, com "alguns ajustes necessários" não especificados.
Integração envolvida: SAP x Santander. Ticket #6700943, aberto em 07/04/2026.

---

## Claims de Alto Risco Identificados

| Claim | Fonte | Evidência disponível | Impacto na análise |
|-------|-------|---------------------|--------------------|
| "É só uma replicação do que já existe" | E-mail Noemia (Fonte 2): "replicação do modelo existente com alguns ajustes necessários" | NÃO — documentação técnica da Div. Logística inexistente nos materiais (L6); ajustes não especificados (L7) | Viabilidade Técnica e Esforço: teto 5/10. Para revisar, preciso da documentação original e da especificação dos ajustes |
| "Custo zero / sem investimento" | Walace autorizou "presumindo que não terá custos adicionais" | PARCIAL — o próprio ticket declara expectativa de investimento < R$10K, contradizendo a premissa de Walace. Não há confirmação de quem vai executar de que é custo zero | Disponibilidade de Recursos: contradição ativa. Autorização da Holding pode ser inválida se houver qualquer custo |
| "Já está aprovado" | Gladston (06/05): "Aprovado!"; Walace (08/04): autorização condicional | PARCIAL — Gladston aprovou incondicionalmente; Walace aprovou condicionalmente a custo zero. A tensão entre as duas aprovações não foi resolvida | Disponibilidade de Recursos: não há autorização inequívoca e coerente para o caso com custo |
| "Não impacta outras áreas" | Declarado pelo solicitante no ticket | NÃO — afirmação do solicitante sem análise técnica. Integração bancária (SAP x Santander) envolve no mínimo equipe CP, DTI e banco. Sem avaliação de impacto em tesouraria ou FI | Impacto Organizacional: teto 4/10 por ausência de evidência |
| "É urgente" / SLA em atraso | Ticket com 204h de atraso de SLA | NÃO — o próprio solicitante classificou como Criticidade 3 - Normal. Sem data-limite concreta e sem custo de inação quantificado. O atraso de SLA é do ticket de service desk, não da implementação | Urgência: teto 4/10 por ausência de data concreta; nota efetiva 3/10 |

---

## Critérios de Qualificação

### Valor da Demanda

**1. Alinhamento Estratégico   [6/10]**
Evidência disponível: PARCIAL
A demanda endereça um tema claramente relevante — automação financeira e eliminação de trabalho
manual no processo de pagamento, alinhada a qualquer diretriz de eficiência operacional ou
transformação digital. A denominação "Controladoria do Futuro" usada por Noemia sugere que a
iniciativa pode fazer parte de um programa estratégico mais amplo, mas não foi confirmada (L9).
O fato de o mesmo padrão já ter sido implantado na Div. Logística (mesmo grupo) e na VIX indica
reconhecimento organizacional do valor da solução.
Nenhum OKR ou objetivo estratégico formal foi citado nos materiais fornecidos. Regra aplicada:
"alinhado com digitalização" sem OKR específico = máximo 6/10.
Para revisar esta nota, precisamos de: referência ao objetivo estratégico ou programa ao qual
esta iniciativa se vincula formalmente.

**2. Viabilidade Técnica   [5/10]**
Evidência disponível: PARCIAL
**Claim de Alto Risco aplicado**: "replicação com ajustes" sem documentação técnica da solução
original. O precedente na Div. Logística é um sinal positivo de que a solução existe e funciona
no ambiente SAP do grupo. Porém, faltam: (a) documentação da configuração SAP FI da solução
existente (layouts CNAB, configurações FEBAN, desenvolvimentos ABAP — L6 em aberto); (b) especificação
dos "ajustes necessários" para o CP da VAB (L7 em aberto); (c) confirmação de que a conta
Santander da VAB Matriz está habilitada para receber DDA (L5 em aberto). A integração SAP x
Santander para DDA é um processo conhecido no mercado, mas cada ambiente tem particularidades.
Sem esses três elementos, a afirmação "é uma replicação" não pode ser validada. Teto 5/10 aplicado.
Para revisar esta nota, precisamos de: documentação técnica da Div. Logística + lista específica
dos ajustes + confirmação da habilitação DDA no Santander VAB.

**3. Retorno sobre Investimento   [4/10]**
Evidência disponível: NÃO
O benefício qualitativo é real e bem descrito: eliminação de impressão de boletos, digitação
manual de código de barras e dependência de terceiros para obter boletos no momento do pagamento.
A equipe de CP da VAB Matriz tem desgaste operacional comprovado pelo relato. Porém, o ROI não
pode ser calculado sem os dados básicos: volume mensal de boletos processados (L3 em aberto),
tempo médio por operação e custo do trabalho manual. Sem esses dados, é impossível calcular
benefício em R$/hora ou payback. O custo estimado é < R$10K segundo o ticket, mas não formalizado
(L8 em aberto). Confiança: BAIXA.
Para revisar esta nota, precisamos de: volume mensal de boletos por tipo + tempo médio de
processamento manual por boleto + custo formal da implementação.

**4. Urgência   [3/10]**
Evidência disponível: NÃO
**Regra aplicada**: sem data concreta + sem custo de inação quantificado = máximo 4/10.
O próprio solicitante classificou a demanda como "Criticidade 3 - Normal" no ticket — não há
urgência declarada pelo requerente. Não há data-limite, evento de negócio (fechamento contábil,
auditoria, vencimento de contrato), requisito legal ou consequência financeira quantificada
associada à inação. O desgaste operacional contínuo é real mas não constitui ruptura de processo.
O atraso de SLA de 204h reflete baixo desempenho do processo de atendimento de TI, não urgência
do negócio. Nota 3/10 — impacto de não fazer existe mas é operacional e gradual, sem ponto
de ruptura declarado.
O que tornaria esta nota mais alta: identificação de um evento de negócio com data concreta
(ex: fechamento fiscal, auditoria, expiração de contrato com banco) e quantificação do custo
financeiro de cada mês de atraso.

**5. Maturidade da Demanda   [4/10]**
Evidência disponível: NÃO
**Regra aplicada**: processo não documentado + escopo não declarado = máximo 5/10.
O problema está claramente identificado (processo manual, dependência de terceiros). A solução
está pré-concebida e baseada em precedente interno — isso é positivo. Mas há 10 lacunas abertas
identificadas pela Iara, sendo as mais críticas para a maturidade: volume de boletos não informado
(L3), processo atual não documentado (L4), "ajustes necessários" não especificados (L7), habilitação
DDA no Santander não confirmada (L5). A solução pré-concebida ("é igual ao que já temos") carrega
o risco de o solicitante ter pulado a etapa de análise de requisitos — assumindo que o que funciona
na Logística funcionará no CP sem investigação. Nota 4/10.
O que tornaria esta nota mais alta: documentação do processo atual + especificação dos requisitos
do CP da VAB + lista dos ajustes + confirmação técnica de habilitação DDA.

**6. Disponibilidade de Recursos   [3/10]**
Evidência disponível: NÃO
**Claim de Alto Risco aplicado (custo zero + já aprovado)**: situação de recursos criticamente
comprometida. Primeiro, o orçamento: o ticket declara expectativa de investimento < R$10K, mas não
está formalizado financeiramente (L8). Segundo, a autorização do Holding (Walace Bacelar, 08/04)
é explicitamente condicional a custo zero — se houver qualquer custo, a autorização precisa ser
renegociada. Isso cria uma Condição Bloqueante ativa. Terceiro, após 43 dias das aprovações
gerenciais (08/04 a 20/05), nenhum responsável técnico foi designado no DTI (L10) — o campo
"Responsável" do ticket está vazio. Aprovação gerencial sem designação técnica não é capacidade
operacional. O responsável técnico é um pré-requisito para qualquer estimativa real. Nota 3/10.
O que tornaria esta nota mais alta: (a) resolução da contradição orçamentária com nova autorização
formal da Holding, (b) designação de responsável técnico DTI, (c) formalização do orçamento.

---

### Complexidade de Execução

**7. Esforço Estimado   [5/10]**
Evidência disponível: NÃO
Sem estimativa por fase fornecida nos materiais. Nota reflete incerteza, não esforço declarado.
**Regra aplicada**: claim de "replicação" sem documentação + ausência de estimativa por fase =
máximo 5/10. Com base no perfil típico de uma integração DDA SAP x Santander:
levantamento e análise (20–40h) + configuração SAP FI/FEBAN (20–40h) + adaptação/desenvolvimento
(0–60h, dependendo dos "ajustes") + testes integrados com banco (20–40h) + cutover e documentação
(8–16h). Estimativa: 68–196h, amplitude altíssima por falta de definição dos ajustes. Se os ajustes
forem mínimos (reconfiguração), esforço < 100h (abaixo de 160h = Melhoria). Se envolver
desenvolvimento ABAP ou mapeamento novo de CNAB, pode ultrapassar 160h (Projeto). A definição
dos "ajustes necessários" (L7) é determinante para a classificação correta. Nota 5/10.
Para revisar esta nota, precisamos de: estimativa por fase emitida por quem vai executar + lista
específica dos ajustes vs. solução da Div. Logística.

**8. Impacto Organizacional   [4/10]**
Evidência disponível: PARCIAL
**Claim de Alto Risco aplicado**: "não impacta outras áreas" declarado pelo solicitante sem
análise técnica. Teto 4/10 aplicado. A implementação de DDA no SAP envolve minimamente: equipe
de CP da VAB Matriz (mudança de processo — positiva), time técnico DTI (execução), e o banco
Santander (habilitação do serviço, testes). Possível impacto em Tesouraria/FI (processamento
eletrônico de arquivos CNAB de retorno). O solicitante declarou que outras divisões não são
impactadas, mas isso não foi avaliado tecnicamente — a afirmação "sem impacto" é do requerente,
não da área técnica. A mudança de processo na equipe de CP requer treinamento e adaptação
operacional. Nota 4/10 — impacto limitado mas a afirmação de impacto zero é questionável.
Para revisar esta nota, precisamos de: mapeamento técnico das áreas impactadas pelo fluxo
CNAB de retorno DDA + confirmação da área de tesouraria/FI.

**9. Governança Necessária   [5/10]**
Evidência disponível: PARCIAL
A demanda envolve múltiplos stakeholders (Holding, VAB Matriz, DTI, Santander), integração com
sistema bancário externo e tensão de autorização não resolvida entre Holding e gestão local. Esses
elementos exigem mais do que gestão técnica autônoma. Porém, o escopo declarado é restrito (VAB
CP + Santander) e a complexidade de governança é moderada. A ausência de responsável técnico
(L10) e a contradição de autorização (OBS-1 do Gate) são sinalizadores de que gestão formal
será necessária para não perder o fio das aprovações e do escopo. Nota 5/10 — não descartável,
mas o nível de governança depende da confirmação do esforço real e dos ajustes.

**10. Impacto Regulatório/Financeiro   [5/10]**
Evidência disponível: PARCIAL
Regra aplicada: integrações bancárias ou fiscais merecem ao menos 4/10 pelo risco implícito.
DDA é um mecanismo de pagamento financeiro real — erros de configuração, mapeamento incorreto de
CNAB ou falha na integração com Santander podem resultar em boletos não recebidos, pagamentos
perdidos ou duplicados, com impacto financeiro direto no fluxo de Contas a Pagar da VAB. Não há
requisito legal explícito declarado (campo "Requisito legal: Não" no ticket), mas o processo
de pagamento está sujeito a auditoria contábil. O risco financeiro não é desprezível para
uma integração bancária em ambiente de produção. Nota 5/10.

---

## Resultado

**PONTUAÇÃO TOTAL: 44/100 (44%)**

| Critério | Nota | Evidência |
|----------|------|-----------|
| 1. Alinhamento Estratégico | 6 | PARCIAL |
| 2. Viabilidade Técnica | 5 | PARCIAL |
| 3. Retorno sobre Investimento | 4 | NÃO |
| 4. Urgência | 3 | NÃO |
| 5. Maturidade da Demanda | 4 | NÃO |
| 6. Disponibilidade de Recursos | 3 | NÃO |
| 7. Esforço Estimado | 5 | NÃO |
| 8. Impacto Organizacional | 4 | PARCIAL |
| 9. Governança Necessária | 5 | PARCIAL |
| 10. Impacto Regulatório/Financeiro | 5 | PARCIAL |
| **TOTAL** | **44/100** | |

---

**CLASSIFICAÇÃO PROVISÓRIA: MELHORIA EVOLUTIVA → Sustentação ERP FI**

Justificativa técnica: nenhum dos critérios 7–10 atingiu ≥ 7/10 individualmente (máximos: 5/5/5/5),
portanto a regra de classificação como PROJETO não é atendida com os dados atuais. O escopo
declarado é o de uma melhoria funcional (replicação de configuração existente com ajustes) sem
alteração estrutural de processo de negócio. A área técnica responsável é FI (integração bancária,
processo de Contas a Pagar). Nota de alerta: se os "ajustes necessários" (L7) envolverem
desenvolvimento ABAP novo ou mapeamento de CNAB diferente do padrão, o esforço pode ultrapassar
160h e a classificação deve ser reavaliada como PROJETO — isso é determinante.

**DECISÃO: EM ESPERA**

A pontuação de 44% está abaixo do limiar de 50% para APROVADO COM CONDIÇÕES. Contudo, a causa
principal não é ausência de mérito — é ausência de evidência para avaliar os claims críticos
("replicação", "custo zero", "já aprovado"). Se as 4 Condições Bloqueantes abaixo forem atendidas,
a requalificação pode atingir 55–65% (APROVADO COM CONDIÇÕES). A demanda não deve ser reprovada
definitivamente pois o precedente interno é um elemento real de valor.

---

## Condições Bloqueantes

- **CB-1:** Documentação técnica da implementação DDA na Divisão Logística (configuração SAP FI,
  layouts CNAB, especificação de integração Santander) — ou confirmação técnica documentada de
  que a solução da Logística é aplicável ao ambiente do CP da VAB sem modificações estruturais.
  Sem isso, a afirmação "replicação" não pode ser validada e Viabilidade Técnica permanece em 5/10.

- **CB-2:** Especificação dos "ajustes necessários" com estimativa de esforço por fase
  (levantamento + configuração + desenvolvimento + testes + go-live). Esta é a informação mais
  crítica: define se estamos falando de 80h ou 200h, e se a classificação é Melhoria ou Projeto.

- **CB-3:** Resolução da contradição de autorização da Holding. Cenário A: quem vai executar
  confirma por escrito que o custo é zero (sem licenças, consultoria externa, infraestrutura
  adicional). Cenário B: nova autorização do Walace Bacelar/Holding aceitando o custo estimado
  (valor real, não "< R$10K"). Sem isso, a aprovação da Holding pode ser inválida se houver
  qualquer custo, gerando risco de rollback da autorização no meio do projeto.

- **CB-4:** Designação de responsável técnico no DTI (Projetos ou Sustentação ERP FI) por
  Gladston Campos. Aprovação sem executor é aprovação sem capacidade operacional.

---

## Perguntas em Aberto

- **P-1:** [Noemia / DTI] Existe documentação técnica da implementação DDA na Divisão Logística
  (configurações SAP FEBAN, layout CNAB do Santander, desenvolvimentos ABAP associados)?
  Resposta necessária até: antes da requalificação.

- **P-2:** [Noemia / DTI] Quais são especificamente os "ajustes necessários" para o CP da VAB
  em relação ao modelo da Div. Logística? É possível obter uma estimativa de esforço por fase?
  Resposta necessária até: antes da requalificação.

- **P-3:** [Noemia ou Lucas] Qual o volume mensal de boletos processados pelo CP da VAB Matriz
  (total e por tipo: fornecedores, tributos, outros)? Qual o tempo médio estimado por boleto
  no processo manual atual?
  Resposta necessária até: antes da requalificação (necessária para calcular ROI).

- **P-4:** [Noemia ou DTI] A conta bancária Santander da VAB Matriz já está cadastrada/habilitada
  para receber boletos via DDA eletronicamente? Já existe relacionamento com o gerente Santander
  para esse produto?
  Resposta necessária até: antes da requalificação.

- **P-5:** [Gladston Campos] A aprovação da Holding (Walace Bacelar) foi condicionada a custo
  zero. O ticket declara expectativa de investimento < R$10K. Preciso de uma de duas confirmações:
  (a) o responsável técnico confirma custo zero para a VAB; ou (b) nova autorização da Holding
  para o custo estimado real. Qual o caminho a seguir?
  Resposta necessária até: antes da requalificação.

- **P-6:** [Gladston Campos] Após as aprovações de abril/maio, nenhum responsável técnico foi
  designado no DTI. Quem será o responsável técnico por esta implementação?
  Resposta necessária até: imediatamente — esta designação é pré-requisito para qualquer estimativa.

---

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Levantar documentação técnica da Div. Logística (CB-1) | Noemia / DTI | 7 dias corridos |
| Especificar os "ajustes necessários" com estimativa de esforço (CB-2) | DTI (após designação) | 10 dias corridos após CB-4 |
| Resolver contradição de autorização Holding (CB-3) | Noemia → Gladston → Walace | 5 dias corridos |
| Designar responsável técnico DTI (CB-4) | Gladston Campos | 2 dias corridos — urgente |
| Levantar volume de boletos CP VAB (P-3) | Noemia / Lucas | 5 dias corridos |
| Requalificação da demanda após CBs atendidas | Felipe Filtro / VMO | Após todas as CBs |
