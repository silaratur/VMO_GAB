ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-008
Data: 2026-06-10
Analista: Felipe Filtro (VMO Autônomo)

RESUMO:
A área de Contabilidade/Controle de Ativos (VIXPar/VIX Matriz) solicita 15 ajustes nos
monitores SAP ZMMR_GSI02, GSI03 e GSI04 (módulo MM), com foco em autonomia operacional
para alterar/excluir processos, novos campos exibidos e automações entre PM/Imobilizado
(AS02) e os monitores GSI, incluindo lógica de estorno de fatura/pedido. O Work Request
classifica a demanda como "Demanda / Adaptativa" para o SQUAD PM/MM, com Prioridade
"Baixa" — em contradição com o SLA do chamado de Service Desk (Criticidade "2 - Alta",
1 semana). Benefício declarado é qualitativo ("maior eficiência, agilidade e assertividade"),
sem indicador de medição. Investimento de até R$ 30K declarado como aprovado, sem evidência
documental específica de aprovação financeira. Pendências de governança (aprovação de
Diretoria e confirmação do cargo de Gerente de TI) seguem em aberto desde o Step 1.

---

## Claims de Alto Risco Identificados

| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "Possui investimento aprovado? Sim" (até R$ 30K) | PARCIAL | Critério 6: existe sinalização no formulário do chamado, mas nenhum documento de aprovação financeira (CAPEX/orçamento) foi anexado — apenas e-mails de "De acordo." sobre o projeto em si, não sobre o valor de investimento. Teto aplicado: 6/10. |
| "Esse projeto envolve ou impacta outras áreas de negócio? Não" / "outras divisões? Não" | NÃO | Critério 8: a demanda toca módulos PM, MM, AM (imobilizado) e Contabilidade/Fiscal de forma integrada (itens 5, 7, 13, 14). "Não impacta outras áreas" não foi verificado tecnicamente. Teto aplicado: 4/10. |
| "A princípio não temos riscos" (Work Request, campo Riscos) | NÃO | Critérios 9 e 10: a demanda inclui lógica de estorno de fatura/pedido (item 13) e alteração de comportamento padrão de campos financeiros da MIRO (item 14), com impacto direto em integridade fiscal/contábil — afirmação de "sem riscos" não é sustentável sem análise técnica. Sinalizado para o Plano de Riscos (Pedro Perigo). |
| "Projeto semelhante já implantado no GAB" — Monitores de requisição, pedido e imobilizado (V1, por Jerfesson Fernandes Helmer) | SIM (PARCIAL) | Critério 2: existe precedente direto (V1 já entregue pelo mesmo especialista), o que reduz incerteza técnica geral — porém os itens 5, 7 e 13 introduzem automações novas (não presentes na V1, segundo o histórico de alterações), portanto o precedente não cobre 100% do escopo. |
| Prioridade "Baixa" (Work Request) vs. Criticidade "2 - Alta" / SLA 1 semana (chamado) | NÃO | Critério 4: a inconsistência impede afirmar urgência real com data concreta. Tratado como ausência de urgência declarada de forma confiável — nota rebaixada conforme regra ("É urgente sem data e custo de inação = nota máxima 4/10"). |

---

## Critérios de Qualificação

1. Alinhamento Estratégico      5/10
   Evidência disponível: PARCIAL
   Não há OKR ou objetivo estratégico corporativo citado nas fontes. O alinhamento é
   operacional/setorial: melhorar autonomia e agilidade do fechamento contábil mensal
   da Contabilidade/Controle de Ativos. Confiança: MÉDIA — alinhamento plausível com
   eficiência operacional, mas sem documento estratégico que o referencie.
   Para revisar esta nota, precisamos de: existe algum objetivo formal de eficiência
   de fechamento contábil (OKR, meta de área) ao qual esta demanda se vincule?

2. Viabilidade Técnica          6/10
   Evidência disponível: PARCIAL
   Existe precedente direto: a V1 dos monitores ZMMR_GSI01-04 já foi implementada pelo
   mesmo especialista (Jerfesson Fernandes Helmer), reduzindo incerteza geral de
   plataforma. Os itens 2, 3, 4, 6, 9, 11 e 15 são exposições de campos já existentes
   na origem (ME53N/AS01) — viabilidade alta. Os itens 1 (campo novo + obrigatoriedade
   via ZMMTR002), 5 (detecção automática de histórico de pedido + carga de MIRO via
   GRC), 7 (sincronização PM→AS02), 8 (regra automática de legalização), 10/12/13
   (alteração de regras de edição/estorno entre 3 monitores) e 14 (alteração de
   comportamento padrão da MIRO) envolvem desenvolvimento ABAP/BAdI/exits e lógica de
   estado entre módulos — viabilidade moderada-alta mas não trivial. Confiança: MÉDIA.
   Para revisar esta nota, precisamos de: confirmação da equipe técnica (SQUAD PM/MM)
   sobre os user-exits/BAdIs disponíveis para os itens 1, 5, 7 e 14.

3. Retorno sobre Investimento   3/10
   Evidência disponível: NÃO
   Benefício declarado é qualitativo: "Maior eficiência, agilidade e assertividade no
   processo de criação de imobilizado de frota e entrada de notas fiscais" — sem valor
   em R$ ou tempo, e o campo "Indicador para medir ganhos" está N/A. Custo: até R$ 30K
   (declarado, sem detalhamento). Sem dados de volume (quantos pedidos/imobilizados por
   mês), não é possível calcular payback. Confiança: BAIXA.
   Para revisar esta nota, precisamos de: volume mensal de pedidos/imobilizados afetados
   pelo processo atual, tempo médio gasto hoje em retrabalho/correções manuais, e meta
   de redução desse tempo após a entrega.

4. Urgência                     3/10
   Evidência disponível: NÃO
   Prioridade declarada no Work Request é "Baixa". O campo "Se a demanda for urgente,
   justifique o motivo" está preenchido como "N/A". O SLA de 1 semana do chamado não é
   acompanhado de nenhuma consequência de negócio quantificada para o não-cumprimento.
   Confiança: BAIXA.
   Para revisar esta nota, precisamos de: existe algum evento de calendário (ex.:
   fechamento de mês/trimestre, auditoria) que torne algum dos 15 itens urgente em
   data específica?

5. Maturidade da Demanda        7/10
   Evidência disponível: SIM
   O escopo técnico é incomumente bem detalhado para uma demanda de melhoria: 15 itens
   numerados, cada um referenciando telas, transações e campos específicos (ex.: "DT.
   Básica" e "Vencimento Em" na aba Pagamentos da MIRO; "Grupo deprec." na aba
   Atribuições; aba "Histórico do pedido" da ME22N). Isso indica que o problema técnico
   está bem compreendido pelos solicitantes e pelo especialista (Jerfesson). Confiança:
   ALTA quanto à definição técnica. O que impede nota mais alta: lacunas de processo
   (governança, priorização) e duas inconsistências internas do próprio escopo (item 6
   cita GSI03 e GSI04 simultaneamente; ZMMR_GSI01 aparece no cabeçalho sem item
   correspondente) — ver lacunas L7, L10, L12 da demanda coletada.

6. Disponibilidade de Recursos  5/10
   Evidência disponível: PARCIAL
   O SQUAD PM/MM já atua nesse conjunto de monitores (entregou a V1) — equipe técnica
   com contexto prévio existe e está identificada (Jerfesson Fernandes Helmer). O
   chamado foi encaminhado ao Grupo Solucionador "Projetos DTI", mas o campo
   "Responsável" segue "Não Informado". Orçamento: sinalizado como aprovado (até R$30K),
   mas sem documento de aprovação financeira específico (ver Claim de Alto Risco acima).
   Confiança: MÉDIA.
   Para revisar esta nota, precisamos de: confirmação de quem será o responsável técnico
   designado pela Projetos DTI (lacuna L14), e evidência documental da aprovação
   orçamentária (lacuna L6).

7. Esforço Estimado             5/10
   Evidência disponível: NÃO
   Não há estimativa de horas por fase em nenhuma fonte. Pela natureza dos 15 itens,
   é razoável esperar que o esforço total ultrapasse 160h: pelo menos 6 itens (2, 3, 4,
   6, 9, 11, 15) são de baixa complexidade (exposição de campo já existente, ~8-16h
   cada), mas os itens 1, 5, 7, 8, 10, 12, 13 e 14 envolvem lógica de negócio nova,
   integração entre módulos e/ou máquina de estados (estorno) — plausivelmente 24-60h
   cada, especialmente o item 13. Sem estimativa por fase declarada pelo solicitante ou
   pela equipe técnica, a nota máxima permitida por incerteza é 5/10, independentemente
   da minha estimativa indicar esforço provavelmente alto.
   Para revisar esta nota, precisamos de: estimativa de horas por fase (levantamento,
   desenvolvimento, testes, go-live) para cada um dos 15 itens, feita pelo SQUAD PM/MM.

8. Impacto Organizacional       4/10
   Evidência disponível: NÃO
   O formulário do chamado declara "Não" para impacto em outras áreas e divisões de
   negócio, mas essa afirmação não foi verificada tecnicamente — a demanda toca, no
   mínimo, os processos de Compras (ME21N/ME22N/ME51N/ME52N), Imobilizado/Patrimônio
   (AS01/AS02), PM (cadastro de equipamento) e Fiscal (MIRO/notas fiscais), além de
   alterar regras de autonomia/edição usadas pela equipe de Contabilidade no fechamento
   mensal. Mudança de comportamento em campos como "DT. Básica"/"Vencimento Em" da MIRO
   (item 14) pode afetar relatórios e processos de outros usuários da MIRO que não
   utilizam o monitor. Por regra, "não impacta outras áreas" sem evidência explícita
   tem teto de 4/10.
   Para revisar esta nota, precisamos de: confirmação de que NENHUM outro usuário/área
   utiliza a MIRO fora do fluxo do monitor GSI03 (relevante para o item 14), e que a
   alteração de regra do item 10 (Tipo de Veículo pós-pedido) não conflita com
   processos já fechados/auditados.

9. Governança Necessária        6/10
   Evidência disponível: PARCIAL
   Trata-se de uma "Melhoria/Demanda Adaptativa" para um time de sustentação (SQUAD
   PM/MM), não um projeto novo — o que reduz a necessidade de estrutura de projeto
   formal completa (TAP, cronograma multi-fase, etc.). Por outro lado, o item 13
   (estorno com atualização de status/log entre dois monitores e regra de ordem
   fatura→pedido) e o item 14 (alteração de comportamento padrão de campos financeiros)
   têm potencial de gerar inconsistências de dados entre GSI02/03/04 se mal
   especificados — exigindo, no mínimo, especificação funcional formal e plano de
   testes dedicado para esses itens, mesmo que o conjunto não justifique um projeto
   completo.

10. Impacto Regulatório/Financeiro 6/10
    Evidência disponível: PARCIAL
    A demanda toca diretamente lançamentos fiscais (entrada de notas fiscais via MIRO),
    cadastro de imobilizado (depreciação — item 15, "Grupo deprec.") e o processo de
    estorno de faturas (item 13), todos com potencial impacto em demonstrativos
    contábeis e em auditorias (Centro de Custo/Imobilizado VIX – 2800184-0 informado).
    "Necessidade Legal/Obrigatório? Não" foi declarado, mas a natureza fiscal/contábil
    dos itens 1, 13, 14 e 15 justifica nota acima do mínimo conforme a regra de
    integrações fiscais.

---

PONTUAÇÃO: 50/100 (50%)

**CLASSIFICAÇÃO: MELHORIA EVOLUTIVA — Time de Sustentação ERP: PM/MM**
Nenhum dos critérios 7–10 (Esforço 5, Impacto Organizacional 4, Governança 6, Impacto
Regulatório/Financeiro 6) atinge 7/10 individualmente — portanto não há, pelos critérios
objetivos, indicação de necessidade de gestão de projeto formal completa (pipeline VMO
de 16 passos com TAP/Cronograma/EVM). A própria origem da demanda já a classifica como
"Tipo de Atendimento: Demanda" / "Tipo de Intervenção: Adaptativa" / "Equipe: SQUAD
PM/MM" — ou seja, ajuste evolutivo a um sistema (monitores ZMMR_GSI01-04) que já existe
em produção (V1 entregue pelo mesmo especialista). Trata-se de evolução funcional sem
mudança estrutural de processo de negócio (o processo de aquisição/legalização de frota
permanece o mesmo; o que muda é a ferramenta de apoio). Recomenda-se tratamento como
**Melhoria Evolutiva conduzida pelo SQUAD PM/MM**, com os itens 13 e 14 recebendo
especificação funcional formal e plano de testes dedicado dado seu maior risco de
inconsistência de dados fiscais/contábeis (ver Claims de Alto Risco).

**DECISÃO: APROVADO COM CONDIÇÕES**

A pontuação de 50% está no limite inferior da faixa "50–74% com condições resolvíveis".
A aprovação está condicionada à resolução das pendências de governança herdadas do
Step 1 (CB-1 e CB-2) e ao detalhamento técnico mínimo necessário para priorização e
planejamento da execução (CB-3 a CB-6).

---

## Condições Bloqueantes

- **CB-1:** Confirmar formalmente a aprovação de Diretoria da área solicitante
  (esclarecer a aprovação de "André" mencionada no e-mail de 06/03/2026 e a
  inconsistência do arquivo "APROVAÇÃO - DIRETOR DA ÁREA.pdf", que contém o e-mail da
  Gerente Contábil — Lacunas L4/L5). Sem esta confirmação, a demanda permanece
  **NÃO VALIDADA** segundo a regra de governança do VMO (Diretoria + Gerente de TI).

- **CB-2:** Confirmar o cargo formal de Raphael Leitão Sbardelotti como Gerente de TI
  da divisão solicitante (Lacuna L3), ou identificar e obter aprovação do Gerente de TI
  correto.

- **CB-3:** Esclarecer com o solicitante (Tatiane/João Henrique) o destino exato da
  coluna "Data de lançamento" do item 6 (GSI03, GSI04 ou ambos) e a relação entre o
  cabeçalho "ZMMR_GSI01" e o escopo dos 15 itens, que não o referenciam (Lacunas L10,
  L12).

- **CB-4:** Resolver a divergência de priorização entre "Baixa" (Work Request) e
  "2 - Alta" / SLA 1 semana (chamado), definindo o prazo real esperado para
  planejamento (Lacuna L7).

- **CB-5:** Obter do SQUAD PM/MM uma estimativa de esforço por fase (levantamento,
  desenvolvimento, testes, go-live) para os 15 itens, com destaque para os itens 1, 5,
  7, 10, 12, 13 e 14 (maior complexidade), para permitir a priorização do backlog.

- **CB-6:** Especificar formalmente as regras de negócio do item 13 (estorno) e do item
  14 (cálculo de "Vencimento Em" e comportamento de "DT. Básica" na MIRO), incluindo
  cenários de borda (ex.: estorno parcial, MIRO já paga), antes do início do
  desenvolvimento — dado o risco de inconsistência fiscal/contábil identificado nos
  Claims de Alto Risco.

---

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Resolver CB-1 e CB-2 (governança) — confirmar aprovação de Diretoria e cargo de Gerente de TI | Tatiane Dias de Moraes / Projetos DTI | 2026-06-13 |
| Resolver CB-3 e CB-4 (esclarecimentos de escopo e priorização) junto ao solicitante | Tatiane / João Henrique | 2026-06-13 |
| Resolver CB-5 (estimativa de esforço por fase, 15 itens) | SQUAD PM/MM (Jerfesson Fernandes Helmer) | 2026-06-17 |
| Resolver CB-6 (especificação funcional dos itens 13 e 14, com plano de testes) | SQUAD PM/MM + Especialista Funcional | 2026-06-24 |
| Designar responsável técnico formal pelo atendimento (campo "Responsável" do chamado) | Projetos DTI | 2026-06-13 |
| Após CB-1 a CB-6: priorizar os 15 itens em ondas de entrega (sugestão: onda 1 — itens
2,3,4,6,9,11,15; onda 2 — itens 1,8,10,12; onda 3 — itens 5,7,13,14) | SQUAD PM/MM + GP VMO | A definir após CB-5 |

---

# ANÁLISE COMERCIAL — Ajustes Monitores ZMMR_GSI02/03/04 (DEM-2026-008)
Data: 2026-06-10

BENEFÍCIOS ESPERADOS

| Benefício | Valor Estimado | Prazo | Confiança |
|-----------|----------------|-------|-----------|
| Redução de retrabalho no fechamento mensal (autonomia para corrigir/excluir processos nos monitores) | Não quantificado | Não informado | BAIXA |
| Redução de tempo no processo de criação/legalização de imobilizado de frota | Não quantificado | Não informado | BAIXA |
| Redução de inconsistências entre monitores GSI02/03/04 (estorno, tipo de veículo) | Não quantificado | Não informado | BAIXA |
| Redução de erros em lançamento de fatura (cálculo automático de "Vencimento Em") | Não quantificado | Não informado | BAIXA |

Total de benefícios anuais estimados: **não calculável** — nenhuma das fontes fornece
volume de transações, tempo médio atual de processamento ou meta de redução. O campo
"Indicador para medir ganhos" do chamado está N/A.

CUSTO DO PROJETO

| Item | Estimativa |
|------|------------|
| Desenvolvimento/Implantação (15 itens, ABAP/Customização) | Até R$ 30.000 (teto declarado pelo solicitante — sem decomposição por item) |
| Infraestrutura (12 meses) | R$ 0 (ajuste em sistema já existente — SAP ECC on-premise) |
| Licenças | R$ 0 (não aplicável — customização interna) |
| Treinamento | Não informado — recomenda-se incluir, dado que itens 1, 10, 11, 13, 15 alteram
  fluxos de tela percebidos pelo usuário final |
| Contingência (20% sobre o teto declarado) | R$ 6.000 |
TOTAL ESTIMADO (com contingência): **R$ 36.000** — acima do teto de R$ 30K declarado
como "investimento aprovado". Recomenda-se validar se o teto aprovado já contempla
contingência ou se precisará de aditivo.

MÉTRICAS DE RETORNO

- Payback: **não calculável** — ausência de quantificação de benefício (ver acima)
- ROI em 12 meses: não calculável
- ROI em 24 meses: não calculável
- Nível de confiança geral: BAIXA

CUSTO DE NÃO-FAZER

Não quantificado nas fontes. Qualitativamente: manutenção da situação atual em que
usuários de Contabilidade/Controle de Ativos dependem de outras equipes (TI/Suporte)
para corrigir/excluir processos nos monitores, prolongando o tempo de fechamento
contábil mensal e mantendo o risco de lançamentos de MIRO "fora do fluxo" (via GRC) não
refletidos automaticamente no monitor (item 5) — o que já hoje gera retrabalho manual de
conciliação.

PROPOSTA DE VALOR

"A demanda DEM-2026-008, com investimento estimado de até R$ 30-36K, entrega 15 ajustes
evolutivos aos monitores ZMMR_GSI02/03/04 (SAP MM), conferindo autonomia operacional à
equipe de Contabilidade/Controle de Ativos para corrigir e gerenciar processos de
aquisição e legalização de frota diretamente nos monitores. Embora o ganho declarado
('maior eficiência, agilidade e assertividade') ainda não esteja quantificado, a entrega
reduz dependência de equipes externas para correções e fecha lacunas de automação
(MIRO via GRC, sincronização PM/Imobilizado, estorno) que hoje geram retrabalho manual
no fechamento mensal. Recomenda-se quantificar o benefício (CB-5/Próximos Passos) antes
do início da execução, para permitir medição do ganho de produtividade pós-entrega."
