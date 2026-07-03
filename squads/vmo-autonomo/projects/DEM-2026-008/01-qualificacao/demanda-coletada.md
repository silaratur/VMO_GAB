# Demanda Coletada
Data da Coleta: 2026-07-03
Coletado por: Iara Inbound (VMO Autônomo)
Canal de Entrada: Fireflies (transcrição de reunião de discovery)

---

## Fontes Consultadas

| # | Canal | Tipo | Descrição | Data |
|---|-------|------|-----------|------|
| 1 | Fireflies | Transcrição | "Discovery Demandas - Dario Demanda <> Wellington Gonçalves" (ID 01KWJ8RNAQGVTWDAV5QHTRYTT3, 15min32s) | 02/07/2026 |
| 2 | Fireflies | Transcrição | "Discovery Demandas - Dario Demanda <> Wellington Gonçalves" (ID 01KWJ8MGP615NGFE2SY9DT5GBH, 1min08s — abertura curta, mesmo entrevistado, mesma sessão retomada) | 02/07/2026 |

---

## Dados da Demanda

**Solicitante**
- Nome (entrevistado/gestor participante): Wellington Gonçalves
- Cargo: Gerente de Suprimentos
- Área/Divisão: Suprimentos — Divisão Passageiros (Grupo Águia Branca)
- Contato: NÃO INFORMADO — apenas nome coletado na transcrição
- Fonte: Fonte 1

**Solicitante Formal / Patrocinadora**
- Nome: Alessandra Comério
- Papel declarado: Solicitante formal registrada e patrocinadora da iniciativa (aprovação da CEO já obtida)
- Fonte: Fonte 1 — "a Alessandra Comério [é] a solicitante formal e patrocinadora da iniciativa, com você, Wellington, como gestor participante"

**Necessidade de Negócio**
A área de Suprimentos da Divisão Passageiros não consegue ter visibilidade entre o
orçado e o realizado nas compras ao longo do mês. O SAP, sistema atual, não oferece
relatórios que permitam essa gestão efetiva. O maior desafio está na compra de peças,
que envolve grande volume de fornecedores e itens com condições de pagamento variadas,
inviabilizando o controle linha a linha. Isso compromete a previsibilidade de caixa da
empresa, especialmente em horizontes de 30/60/90 dias (pagamentos parcelados).
Atualmente a gestão é feita de forma manual por uma pessoa (Tamiris, de outra área/entrevista
não incluída nesta fonte) com base em dados históricos e relatórios parciais; a área de
Suprimentos também mantém controles manuais próprios para combustível e investimentos, mas
não para o volume principal de peças.
Fonte: Fonte 1

**Pedido Específico**
Implantação do sistema **TVM** (já com histórico de uso no Grupo Águia Branca) com regras
de negócio específicas para Suprimentos, incluindo:
- Painel com baseline do orçado
- Atualização do realizado conforme lançamentos de pagamento
- Projeção de pagamentos futuros parcelados (30/60/90 dias)
- Alertas automáticos por faixa de consumo do orçamento (ex.: 70% e 85% do orçado)

O entrevistado avaliou que desenvolver essa funcionalidade diretamente no SAP seria
complexo, e que a preferência é seguir com o TVM por já haver histórico de implantação
no grupo.
Fonte: Fonte 1

**Benefício Esperado**
- Melhoria na qualidade e confiabilidade da informação orçamentária
- Redução do trabalho manual de consolidação de dados (3 pessoas hoje dedicadas a
  levantamentos semanais de diesel, investimento e pneus)
- Visão prospectiva de caixa (30/60/90 dias) que hoje não existe
- Suporte à tomada de decisão da diretoria, alinhado à nova governança financeira de caixa
  do grupo
Fonte: Fonte 1

**Urgência e Prazo**
- Prazo desejado: 30 dias para a solução estar no ar
- Urgência declarada: Definida pela urgência da necessidade — não vinculada a evento formal
  (fechamento de ciclo orçamentário, auditoria etc.) declarado explicitamente
- Origem do prazo: proposta já aprovada com essa especificação de prazo pela equipe
- SLA de ticket: não aplicável (canal é reunião de discovery, não ticket)
Fonte: Fonte 1

**Aprovações e Autorizações Identificadas**
1. **CEO do Grupo Águia Branca** (nome não informado na transcrição)
   - Conteúdo: "Ela já está aprovada pela nossa CEO" — aprovação da iniciativa como um todo
   - Natureza: **INCONDICIONAL**, conforme declarado
   - Fonte: Fonte 1
2. **Equipe de TI e equipe TVM**
   - Conteúdo: "O investimento já foi aprovado junto a nossa equipe de TI e juntamente também
     com a equipe TVM"
   - Natureza: aprovação de investimento, sem detalhamento de condicionantes
   - Fonte: Fonte 1

**Contexto Organizacional**
- Divisão/empresa: Divisão Passageiros — Grupo Águia Branca
- Área executora provável: Equipe TVM (interna/fornecedor do grupo) + TI
- Áreas impactadas: Contabilidade, Financeiro, Suprimentos, Gestão de Riscos, Diretoria
- Divisões impactadas: concentrada na Divisão Passageiros (declarado pelo entrevistado)
- Sistemas envolvidos: SAP (atual, considerado insuficiente) e TVM (proposto)
- Outras integrações (ex. Power BI): NÃO INFORMADO — entrevistado declarou não ter essa
  informação
- Requisito legal/regulatório/contratual: NÃO INFORMADO — entrevistado declarou não ter
  conhecimento
- Investimento aprovado: Sim, junto a TI e equipe TVM (ver Aprovações)
- Valor do investimento: ⚠️ **INCONSISTÊNCIA** — ver seção abaixo
- Fonte: Fonte 1

**Stakeholders Identificados**
| Nome | Papel | Área | Fonte |
|------|-------|------|-------|
| Wellington Gonçalves | Gerente de Suprimentos; entrevistado; gestor participante do projeto | Suprimentos / Div. Passageiros | Fonte 1 |
| Alessandra Comério | Solicitante formal e patrocinadora da iniciativa | Não informado | Fonte 1 |
| CEO (nome não informado) | Patrocinadora/aprovadora da iniciativa | Diretoria | Fonte 1 |
| Tamiris | Responsável atual pela gestão manual de caixa e orçamento (mencionada, não entrevistada nesta fonte) | Não informado | Fonte 1 |

**Contexto Implícito**
- ⚠️ **POSSÍVEL SOBREPOSIÇÃO DE DEMANDA**: esta demanda apresenta forte semelhança com outra
  reunião de discovery já registrada no Fireflies — "MARCELO SILVEIRA <> Discovery Demandas -
  Hugo (1)" (02/07/2026), na qual Marcelo Silveira solicita, também para a **Divisão Passageiros**,
  a automação da gestão de fluxo de caixa via SAP, replicando o modelo já em produção na
  **Divisão Logística**, com orçamento de **R$ 30 mil já aprovado pela CEO** e prazo de
  **4 a 5 semanas**. Os dois relatos (Wellington/Suprimentos e Marcelo/Financeiro) descrevem a
  mesma divisão, o mesmo padrão de replicação de solução, valor de orçamento na mesma ordem
  de grandeza (R$ 30 mil) e prazo equivalente (~30 dias), mas com pedidos técnicos diferentes
  (TVM com regras de suprimentos vs. SAP replicado da Div. Logística). Não é possível
  confirmar, apenas com esta fonte, se são a mesma iniciativa vista por dois stakeholders
  diferentes ou duas demandas distintas dentro do mesmo programa de governança de caixa.
  **Recomenda-se ao Felipe Filtro (Analista de Qualificação) avaliar consolidação ou
  vinculação entre as duas demandas antes de prosseguir com qualificação independente.**
- A demanda se insere em um momento de maturidade da governança financeira do grupo:
  segundo o entrevistado, "antes a gente não tinha uma governança em relação à estrutura de
  caixa" e a empresa está "implementando um controle de caixa bastante efetivo". Isso sugere
  que pode haver outras demandas semelhantes surgindo de diferentes áreas/divisões como parte
  do mesmo movimento organizacional — vale investigar no levantamento.
- Existe forte dependência atual de uma única pessoa (Tamiris) para consolidação manual de
  dados de caixa, o que representa um risco operacional não formalmente registrado como tal
  pelo entrevistado.
Fonte: análise cruzada da Fonte 1 com o histórico de transcrições Fireflies do canal

---

## Inconsistências Identificadas

| Campo | Fonte 1 (transcrição literal) | Observação |
|-------|-------------------------------|------------|
| Valor do investimento | Wellington Gonçalves declara verbalmente **"30 Bilhões"** em resposta direta à pergunta sobre o valor aprovado | ⚠️ **INCONSISTÊNCIA** — o valor de R$ 30 bilhões é incompatível com o porte da iniciativa (painel de orçamento/alertas de consumo) e com o precedente da demanda correlata (Marcelo Silveira), que registra R$ 30 mil aprovados pela CEO para escopo semelhante. Não corrigido unilateralmente — mantido registrado como declarado, com flag para confirmação junto ao solicitante antes de qualquer uso em documentação financeira subsequente. |

---

## Lacunas Identificadas

| # | Campo | Status | Pergunta para Esclarecimento |
|---|-------|--------|------------------------------|
| L1 | Valor real do investimento aprovado | ⚠️ INCONSISTENTE — requer confirmação | O valor aprovado é R$ 30 mil (conforme demanda correlata da Div. Passageiros) ou outro valor? "30 Bilhões" foi um erro de fala/transcrição? |
| L2 | Nome da CEO aprovadora | NÃO INFORMADO | Quem é a CEO que aprovou formalmente a iniciativa, para fins de registro de patrocínio? |
| L3 | Cargo/área completa de Tamiris | NÃO INFORMADO | Qual o cargo e área de Tamiris, responsável atual pela consolidação manual de caixa? |
| L4 | Integrações de sistema (Power BI etc.) | NÃO INFORMADO | Quais sistemas além de SAP e TVM estarão envolvidos na solução (visualização, extração de dados)? |
| L5 | Requisito legal/regulatório | NÃO INFORMADO | Existe alguma obrigação de compliance, auditoria ou contratual que a solução precise atender? |
| L6 | Contato do solicitante (Wellington e Alessandra) | NÃO INFORMADO | E-mail/telefone de Wellington Gonçalves e de Alessandra Comério para rastreabilidade e follow-up. |
| L7 | Relação com demanda correlata (Marcelo Silveira / Div. Passageiros) | NÃO CONFIRMADO | Esta demanda é a mesma iniciativa relatada por Marcelo Silveira em reunião separada, ou uma demanda distinta dentro do mesmo programa? Requer avaliação de consolidação. |
| L8 | Cargo formal de Alessandra Comério | NÃO INFORMADO | Qual o cargo/área de Alessandra Comério como solicitante formal e patrocinadora? |

---

## Resumo para Confirmação

A área de Suprimentos da Divisão Passageiros (Grupo Águia Branca), representada por
Wellington Gonçalves (Gerente de Suprimentos), solicita a implantação do sistema TVM com
regras de negócio específicas para gestão orçamentária de compras — painel de baseline
orçado, atualização do realizado, projeção de pagamentos parcelados (30/60/90 dias) e
alertas automáticos por faixa de consumo do orçamento. O problema central é a falta de
previsibilidade de caixa causada pelo alto volume de fornecedores/itens de peças e pela
dependência de consolidação manual. A demanda já tem aprovação da CEO e da equipe de
TI/TVM, com prazo desejado de 30 dias. Solicitante formal registrada: Alessandra Comério.
8 lacunas identificadas, com destaque crítico para: (1) inconsistência no valor do
investimento declarado ("30 Bilhões" vs. precedente de R$ 30 mil) e (2) possível
sobreposição com outra demanda de discovery da mesma Divisão Passageiros (Marcelo
Silveira), que requer avaliação de consolidação pelo Felipe Filtro antes de prosseguir.
