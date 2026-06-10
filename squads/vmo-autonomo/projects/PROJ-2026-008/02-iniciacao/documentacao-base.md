# Documentação Base de Iniciação — Ajustes nos Monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 (SAP ECC MM)

---
## TERMO DE ABERTURA DO PROJETO (TAP)

```
TERMO DE ABERTURA DO PROJETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Versão: 1.0
Data: 2026-06-10
Status: RASCUNHO — Aguardando confirmação de Sponsor de nível Diretoria (CB-1)

IDENTIFICAÇÃO DO PROJETO
  Nome: Ajustes nos Monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 — SAP ECC Módulo MM
  ID:   PROJ-2026-008 (Demanda DEM-2026-008)
  Classificação: MELHORIA EVOLUTIVA — não constitui "Projeto" pleno; tratada como
                 melhoria evolutiva sob governança simplificada do VMO/PMO
  Área Solicitante: Grupo Águia Branca — Divisão VIXPar/VIX Matriz —
                    Contabilidade / Controle de Ativos e Recebimento Fiscal
  Área Executora: SQUAD PM/MM (Time de Sustentação ERP)

AUTORIZAÇÃO
  Sponsor: Nubia Carla Freitas Santos Souza — Gerente Contábil (Gestor Direto)
           [PROVISÓRIO — aprovação de nível Diretoria PENDENTE, ver CB-1]
  Co-Sponsor / Aprovador a confirmar: Raphael Leitão Sbardelotti — cargo "Gerente
           de TI" NÃO CONFIRMADO (ver CB-2)
  Solicitante Principal: Tatiane Dias de Moraes — Coordenadora de Controle de
           Ativos e Recebimento Fiscal
  Co-Solicitante: João Henrique
  Especialista Técnico de Referência: Jerfesson Fernandes Helmer (autor da V1
           dos monitores, já em produção)
  Gerente de Projeto: A designar pelo SQUAD PM/MM (Time de Sustentação ERP)
  Autoridade do GP: Aprovar ajustes técnicos e priorização de itens dentro das
           3 ondas definidas; gastos adicionais e mudanças de escopo acima de
           R$ 5.000 ou que impactem prazo/orçamento total requerem validação
           do Sponsor

  ⚠️ RESTRIÇÃO/RISCO DE GOVERNANÇA (ALTO): A autorização formal deste TAP em
     nível de Diretoria está PENDENTE (CB-1, prazo 2026-06-13). Até a
     confirmação, este documento tem caráter de RASCUNHO autorizado apenas
     pelo Gestor Direto (Gerente Contábil). O início de atividades de Onda 2
     e Onda 3 fica condicionado à resolução de CB-1 e CB-2.

OBJETIVO DO PROJETO (SMART)
  Implementar os 15 ajustes adaptativos priorizados em 3 ondas (Onda 1: itens
  2, 3, 4, 6, 9, 11, 15; Onda 2: itens 1, 8, 10, 12; Onda 3: itens 5, 7, 13, 14)
  nos monitores SAP ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 (módulo MM), até
  30/09/2026, aumentando a autonomia operacional da equipe de Contabilidade /
  Controle de Ativos para correção, exclusão e acompanhamento de processos de
  imobilizado de frota e entrada de notas fiscais sem dependência direta de
  TI, com indicador de sucesso quantitativo (ex.: redução do tempo de
  fechamento mensal e do número de retrabalhos manuais de conciliação
  MIRO/GRC) a ser definido formalmente pelo SQUAD PM/MM até 17/06/2026
  (CB-5 / lacuna L9).

JUSTIFICATIVA
  Os monitores ZMMR_GSI02/03/04 (V1, já em produção) suportam o processo de
  criação de imobilizado de frota e o ciclo de entrada de notas fiscais
  (ME51N/ME52N/ME21N/ME22N/ZMMTR002/AS01/AS02). Hoje, a equipe de Contabilidade
  identifica 15 lacunas operacionais que geram retrabalho manual, dependência
  de TI para correções pontuais e risco de inconsistência entre o status do
  pedido/fatura no SAP e o status registrado nos monitores. O projeto endereça
  diretamente a meta de eficiência operacional do Time de Sustentação ERP,
  reduzindo intervenções manuais e o tempo de ciclo do processo de
  fechamento contábil/fiscal de ativos.

ESCOPO
  DENTRO DO ESCOPO:
    Onda 1 — Baixa complexidade (exposição de campos existentes):
      - Item 2: Coluna "Vencimento NF" (já existe na ME53N) no GSI02
      - Item 3: Coluna "CR" (já existe na ME53N) no GSI02
      - Item 4: Coluna "Data Liberação/aprovação" da requisição no GSI02
      - Item 6: Coluna "Data de lançamento" da fatura (MIRO) no GSI03 e/ou
                GSI04 (destino exato a confirmar — CB-3)
      - Item 9: Parâmetro de busca "Nº de Requisição de Compra" no GSI04
      - Item 11: Coluna "Tipo de Veículo" no GSI02
      - Item 15: Campo "Grupo deprec." (já existe na AS01) no cadastro de
                 imobilizado via GSI02

    Onda 2 — Mudanças de regra de negócio:
      - Item 1: Campo "Classificação" novo na ME53N + obrigatoriedade via
                ZMMTR002 + coluna no GSI02
      - Item 8: Marcação automática de etapa de Legalização concluída para
                máquinas/implementos não emplacados (GSI03)
      - Item 10: Permitir alterar "Tipo de Veículo" após criação do pedido,
                 propagando para GSI02/03/04
      - Item 12: Permitir alteração de XML incorreto no GSI03, condicionado a
                 PM não legalizado nem equipamento criado

    Onda 3 — Alta complexidade (automações/integrações/estorno):
      - Item 5: Detecção automática de lançamento MIRO via GRC (fora do
                fluxo) na ME22N, carregando nº MIRO e marcando etapa no GSI03
      - Item 7: Cadastro de veículo/equipamento em PM atualizando
                automaticamente "Placa do veículo" no AS02
      - Item 13: Estorno de fatura/pedido — exclusão de link de fatura no
                 GSI03/GSI04, atualização de status/log, permissão de nova
                 MIRO e regras de ordem fatura→pedido (item de maior
                 complexidade lógica)
      - Item 14: GSI03/MIRO — campo "DT. Básica" deixa de auto-preencher na
                 criação do pedido, passando a ser preenchido com "Data da
                 Fatura"; "Vencimento Em" = "DT. Básica" + "Condição de
                 Pagamento"

  FORA DO ESCOPO:
    - Ajustes no monitor ZMMR_GSI01 (não há item de escopo correspondente;
      relação com item 6 a esclarecer via CB-3)
    - Novas integrações com sistemas externos não mencionados nos 15 itens
    - Alterações em outros monitores, transações ou módulos SAP não citados
      nesta lista (ex.: FI, CO fora do escopo de imobilizado/MM tratado aqui)
    - Desenvolvimento de novos relatórios gerenciais não solicitados
    - Treinamento amplo de usuários além da capacitação operacional da
      equipe de Contabilidade/Controle de Ativos diretamente impactada

CRITÉRIOS DE SUCESSO
  1. 100% dos 7 itens da Onda 1 implementados e validados em produção até
     31/07/2026
  2. 100% dos 4 itens da Onda 2 implementados e validados em produção até
     31/08/2026
  3. 100% dos 4 itens da Onda 3 implementados, testados (incluindo
     especificação funcional formal e plano de testes dos itens 13 e 14 —
     CB-6) e validados em produção até 30/09/2026
  4. Indicador quantitativo de eficiência (ex.: redução do tempo de
     fechamento mensal e/ou do número de retrabalhos manuais de conciliação
     MIRO/GRC) definido formalmente até 17/06/2026 (CB-5) e medido na
     baseline antes do go-live de cada onda, com meta de melhoria mínima de
     20% em até 60 dias após o go-live da Onda 3
  5. Zero incidentes críticos de divergência fiscal/contábil decorrentes dos
     itens 13 e 14 nos primeiros 30 dias após go-live da Onda 3

PREMISSAS
  - O especialista técnico Jerfesson Fernandes Helmer permanecerá disponível
    como referência funcional/técnica da V1 durante todo o projeto
  - O SQUAD PM/MM (Time de Sustentação ERP) terá capacidade alocada conforme
    estimativa de esforço por fase a ser entregue até 2026-06-17 (CB-5)
  - As integrações citadas (GRC, PM, AS01/AS02) já existem e estão
    operacionais, não sendo necessário desenvolvimento de novas interfaces
    externas
  - O orçamento de até R$ 30.000 declarado como aprovado será confirmado ou
    ajustado frente à estimativa com contingência (R$ 36.000) até o início
    da Onda 2

RESTRIÇÕES
  - Aprovação formal de Diretoria ainda não confirmada (CB-1, prazo
    2026-06-13) — condição para avanço além da Onda 1
  - Cargo de "Gerente de TI" de Raphael Leitão Sbardelotti não confirmado
    (CB-2, prazo 2026-06-13)
  - Investimento aprovado declarado em até R$ 30.000; estimativa do Felipe
    Filtro com 20% de contingência totaliza R$ 36.000 — pode exceder o teto
    aprovado e requer validação orçamentária
  - Divergência de priorização não resolvida: chamado com SLA de 1 semana e
    Criticidade "2-Alta" vs. Work Request com prioridade declarada "Baixa"
    (CB-4, prazo 2026-06-13)
  - Especificação funcional formal e plano de testes dos itens 13 e 14
    (Onda 3) ainda não elaborados (CB-6, prazo 2026-06-24) — pré-requisito
    para início da execução da Onda 3
  - Destino da coluna "Data de lançamento" (item 6) entre GSI03/GSI04 e
    relação com ZMMR_GSI01 ainda não definido (CB-3, prazo 2026-06-13)

RISCOS DE ALTO NÍVEL
  1. [ALTO] Risco fiscal/contábil nos itens 13 e 14 (estorno de fatura/pedido
     e alteração das regras de "DT. Básica"/"Vencimento Em"): erros na lógica
     de estorno ou no cálculo de vencimento podem gerar inconsistências
     fiscais/contábeis em imobilizado e contas a pagar — mitigação via
     especificação funcional formal e plano de testes (CB-6) antes da
     execução
  2. [ALTO] Impacto organizacional do item 5 (detecção automática de
     lançamento MIRO via GRC fora do fluxo): mudança de processo pode gerar
     resistência da equipe de Contabilidade e exigir comunicação/treinamento
     adicional não previstos no escopo original
  3. [ALTO] Orçamentário: estimativa total com contingência (R$ 36.000) pode
     exceder o teto declarado como aprovado (R$ 30.000), exigindo aprovação
     adicional de Diretoria já pendente (CB-1)
  4. [MÉDIO] Governança/aprovação: ausência de confirmação formal de
     sponsor de nível Diretoria (CB-1) e de identificação correta do
     aprovador de TI (CB-2) pode atrasar o início das Ondas 2 e 3
  5. [MÉDIO] Priorização ambígua (CB-4) pode gerar conflito de alocação do
     SQUAD PM/MM frente a outras demandas classificadas como "2-Alta"
  6. [BAIXO] Indisponibilidade pontual do especialista de referência
     (Jerfesson Fernandes Helmer) pode atrasar validações funcionais de
     itens da V1

PARTES INTERESSADAS PRINCIPAIS
  | Nome/Área | Papel | Interesse |
  |-----------|-------|-----------|
  | Nubia Carla Freitas Santos Souza (Gerente Contábil) | Sponsor provisório / Gestor Direto | Aprovação e priorização do projeto; aprovação de Diretoria ainda pendente (CB-1) |
  | Tatiane Dias de Moraes (Coordenadora de Controle de Ativos e Recebimento Fiscal) | Solicitante Principal | Garantir que os 15 itens atendam à operação diária |
  | João Henrique | Co-Solicitante | Validação funcional complementar dos requisitos |
  | Jerfesson Fernandes Helmer | Especialista Técnico de Referência | Continuidade técnica e aderência à V1 já em produção |
  | Raphael Leitão Sbardelotti (cargo a confirmar — possível Gerente de TI) | Aprovador técnico/orçamentário (CB-2) | Validação de viabilidade técnica e orçamentária |
  | SQUAD PM/MM (Time de Sustentação ERP) | Equipe Executora | Execução técnica, estimativa de esforço (CB-5) e qualidade da entrega |
  | Diretoria (área solicitante) | Aprovador formal pendente (CB-1) | Autorização final do investimento e do TAP |
  | Equipe de Contabilidade / Controle de Ativos e Recebimento Fiscal (usuários finais) | Usuários finais | Operação cotidiana dos monitores GSI02/03/04 |

ORÇAMENTO RESUMIDO
  Estimativa base (15 itens, 3 ondas):       R$ 30.000
  Reserva de contingência (20%):             R$  6.000
  ─────────────────────────────────────────────────────
  TOTAL ESTIMADO (com contingência):         R$ 36.000

  Investimento declarado como aprovado:      até R$ 30.000
  ⚠️ ATENÇÃO: O total estimado com contingência (R$ 36.000) pode exceder o
     teto declarado como aprovado (R$ 30.000). Validação orçamentária
     necessária junto ao Sponsor/Diretoria — recomendação registrada como
     CB-Orçamento. Estimativa de esforço por fase será refinada pelo
     SQUAD PM/MM até 2026-06-17 (CB-5).

CRONOGRAMA SUMARIZADO
  Início:                          2026-06-10
  Resolução de CBs críticas (CB-1, CB-2, CB-3, CB-4): até 2026-06-13
  Onda 1 (itens 2,3,4,6,9,11,15):  2026-06-15 a 2026-07-31
  Estimativa de esforço SQUAD PM/MM (CB-5): até 2026-06-17
  Onda 2 (itens 1,8,10,12):        2026-08-01 a 2026-08-31
  Especificação funcional + plano de testes itens 13/14 (CB-6): até 2026-06-24
  Onda 3 (itens 5,7,13,14):        2026-09-01 a 2026-09-30
  Encerramento:                    2026-09-30

APROVAÇÃO
  Sponsor: _____________________ Data: _______
           (Nubia Carla Freitas Santos Souza — Gerente Contábil)
  Aprovação Diretoria (PENDENTE — CB-1): _____________________ Data: _______
  PMO/VMO: _____________________ Data: _______
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---
## PM CANVAS

```
PM CANVAS — Ajustes nos Monitores ZMMR_GSI02/03/04 (SAP ECC MM)
Versão: 1.0 | Data: 2026-06-10

┌────────────────────────────────────────────────────────────────────────────┐
│                  PM CANVAS — PROJ-2026-008 / DEM-2026-008                  │
├──────────────────────┬─────────────────────────┬──────────────────────────┤
│  1. POR QUÊ?         │  2. O QUÊ?              │  3. QUEM?                │
│                      │                         │                          │
│ 15 lacunas           │ • Onda 1 (7 itens):     │ Sponsor (provisório):    │
│ operacionais nos     │   exposição de campos   │  Nubia C. F. S. Souza    │
│ monitores GSI02/03/04│   existentes (itens     │  (Ger. Contábil) —       │
│ geram retrabalho     │   2,3,4,6,9,11,15)      │  Diretoria PENDENTE      │
│ manual e dependência │ • Onda 2 (4 itens):     │  (CB-1)                  │
│ de TI para correções │   mudanças de regra de  │ Solicitante: Tatiane     │
│ pontuais no processo │   negócio (itens        │  Dias de Moraes          │
│ de imobilizado de    │   1,8,10,12)            │ Co-Solicitante: João     │
│ frota e entrada de   │ • Onda 3 (4 itens):     │  Henrique                │
│ notas fiscais.       │   automações, integração│ Especialista Ref.:       │
│                      │   GRC/PM e estorno      │  Jerfesson F. Helmer     │
│ Conecta à meta de    │   (itens 5,7,13,14)     │ Equipe Executora: SQUAD  │
│ eficiência do Time   │                         │  PM/MM (Sustentação ERP) │
│ de Sustentação ERP:  │ Entregável final: 15    │ Aprovador TI (cargo a    │
│ maior autonomia da   │ ajustes em produção nos │  confirmar — CB-2):      │
│ Contabilidade/       │ monitores ZMMR_GSI02/   │  Raphael L. Sbardelotti  │
│ Controle de Ativos   │ 03/04                   │ Usuários: Equipe de      │
│ sem dependência TI.  │                         │  Contabilidade/Controle  │
│                      │                         │  de Ativos e Receb.      │
│                      │                         │  Fiscal                  │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│  4. COMO?            │  5. QUANDO?             │  6. QUANTO?              │
│                      │                         │                          │
│ Melhoria evolutiva   │ Início:    2026-06-10   │ Estimativa base:         │
│ executada pelo SQUAD │ CBs críticas (CB-1,2,3,4│   R$ 30.000              │
│ PM/MM em 3 ondas     │  ) resolvidas: 2026-06-13│ Contingência (20%):     │
│ sequenciais sobre o  │ Onda 1: 2026-06-15 a    │   R$  6.000              │
│ ambiente SAP ECC já  │   2026-07-31            │ ──────────────────────  │
│ em produção (V1).    │ Onda 2: 2026-08-01 a    │ TOTAL ESTIMADO:          │
│ Estimativa de esforço│   2026-08-31            │   R$ 36.000              │
│ por fase a ser       │ Onda 3: 2026-09-01 a    │                          │
│ formalizada (CB-5).  │   2026-09-30            │ ⚠️ Pode exceder teto     │
│ Itens 13/14 exigem   │ Encerramento: 2026-09-30│ aprovado de R$ 30.000 —  │
│ especificação        │                         │ validar com Sponsor/     │
│ funcional formal e   │                         │ Diretoria (CB-Orçamento) │
│ plano de testes      │                         │                          │
│ (CB-6).              │                         │                          │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│  7. PREMISSAS        │  8. RESTRIÇÕES          │  9. RISCOS               │
│                      │                         │                          │
│ • Especialista       │ • Aprovação Diretoria   │ • [ALTO] Risco fiscal/   │
│   Jerfesson Helmer   │   pendente (CB-1,       │   contábil itens 13/14   │
│   disponível durante │   2026-06-13)           │   (estorno e regras de   │
│   todo o projeto     │ • Cargo de Gerente de TI│   "DT. Básica")          │
│ • SQUAD PM/MM com    │   (Raphael Sbardelotti) │ • [ALTO] Impacto         │
│   capacidade alocada │   não confirmado (CB-2) │   organizacional do item │
│   conforme CB-5      │ • Orçamento aprovado    │   5 (detecção automática │
│ • Integrações GRC,   │   até R$ 30.000 vs.     │   MIRO via GRC) — mudança│
│   PM, AS01/AS02 já   │   estimativa de R$36.000│   de processo            │
│   operacionais       │ • Divergência de        │ • [ALTO] Estouro de      │
│ • Orçamento de       │   priorização Baixa vs. │   orçamento (R$36k vs.   │
│   R$30k confirmado   │   2-Alta/SLA 1 semana   │   R$30k aprovado)        │
│   ou ajustado antes  │   não resolvida (CB-4)  │ • [MÉDIO] Atraso por     │
│   da Onda 2          │ • Itens 13/14 sem       │   pendência de aprovação │
│                      │   especificação formal  │   (CB-1/CB-2)            │
│                      │   até CB-6 (2026-06-24) │ • [MÉDIO] Conflito de    │
│                      │                         │   priorização (CB-4)     │
└──────────────────────┴─────────────────────────┴──────────────────────────┘
```

---
## PLANO GERAL DO PROJETO

```
PLANO GERAL DO PROJETO — Ajustes nos Monitores ZMMR_GSI02/03/04 (SAP ECC MM)
Versão: 1.0 | Data: 2026-06-10
```

### 1. Plano de Gerenciamento do Escopo
- **Abordagem:** Escopo fechado em 15 itens, organizados em 3 ondas (Onda 1:
  itens 2,3,4,6,9,11,15; Onda 2: itens 1,8,10,12; Onda 3: itens 5,7,13,14),
  validados pelo solicitante (Tatiane Dias de Moraes) e pelo especialista
  técnico de referência (Jerfesson Fernandes Helmer). Cada item será
  decomposto em pacotes de trabalho durante o detalhamento por onda.
- **Ferramenta:** WBS por onda + dicionário descritivo de cada um dos 15 itens
  (já consolidados na qualificação aprovada).
- **Responsável:** Gerente de Projeto designado pelo SQUAD PM/MM.
- **Processo de mudança de escopo:** Qualquer alteração nos 15 itens (inclusão,
  exclusão ou redefinição, ex. CB-3 sobre o item 6) deve ser submetida via
  formulário de mudança, avaliada quanto a impacto em prazo/custo e aprovada
  pelo Sponsor antes de atualização da baseline.

### 2. Plano de Gerenciamento do Cronograma
- **Abordagem:** Planejamento por ondas sequenciais (Onda 1 → Onda 2 → Onda 3),
  com marcos de entrega ao final de cada onda (31/07, 31/08 e 30/09/2026).
- **Ferramenta:** Cronograma em Markdown/planilha por onda, com pacotes de
  trabalho ≤ 2 semanas.
- **Frequência de atualização:** Quinzenal.
- **Indicador:** SPI (alerta se < 0,85); atraso em uma onda é avaliado quanto
  ao impacto nas ondas seguintes antes de replanejamento.

### 3. Plano de Gerenciamento dos Custos
- **Abordagem:** Monitoramento por Earned Value (EVM) sobre o orçamento total
  estimado de R$ 36.000 (R$ 30.000 base + R$ 6.000 de contingência de 20%),
  com acompanhamento específico do risco de estouro frente ao teto declarado
  de R$ 30.000 (CB-Orçamento).
- **Ferramenta:** Planilha EVM simples por onda.
- **Frequência de atualização:** Mensal, com checkpoint adicional ao final de
  cada onda.
- **Indicador:** CPI (alerta se < 0,85); validação orçamentária formal exigida
  antes do início da Onda 2 caso a estimativa supere R$ 30.000.

### 4. Plano de Gerenciamento da Qualidade
- **Abordagem:** Validação funcional de cada item por onda diretamente com a
  Coordenadora Tatiane Dias de Moraes, o co-solicitante João Henrique e o
  especialista Jerfesson Fernandes Helmer, garantindo aderência à V1 já em
  produção.
- **Critérios de qualidade do produto:** Derivados dos critérios de sucesso do
  TAP — entrega funcional dos itens por onda dentro do prazo, ausência de
  incidentes fiscais/contábeis nos itens 13/14, e indicador de eficiência
  (CB-5) atendido.
- **Processo de revisão:** Revisão técnica por pares dentro do SQUAD PM/MM +
  homologação/UAT pelos usuários finais (equipe de Contabilidade/Controle de
  Ativos) antes de cada go-live de onda. Itens 13 e 14 exigem plano de testes
  formal específico (CB-6).

### 5. Plano de Gerenciamento dos Recursos
- **Abordagem:** Recursos do SQUAD PM/MM (Time de Sustentação ERP) alocados
  por onda, conforme estimativa de esforço a ser definida (CB-5, prazo
  2026-06-17).
- **Papéis e responsabilidades:** RACI a detalhar na fase de planejamento
  detalhado; papéis preliminares: GP (coordenação geral), desenvolvedores
  ABAP/MM do SQUAD (implementação), especialista Jerfesson Helmer (consultoria
  funcional), Tatiane Dias de Moraes/João Henrique (validação funcional/UAT).
- **Resolução de conflitos de recursos:** Conflitos de alocação do SQUAD PM/MM
  com outras demandas (especialmente diante da divergência de priorização
  CB-4) escalados ao Sponsor para arbitragem de prioridade.

### 6. Plano de Gerenciamento das Comunicações
| Comunicação | Audiência | Frequência | Canal | Responsável |
|-------------|-----------|------------|-------|-------------|
| Status Report | Sponsor (Nubia Souza) + Tatiane Dias de Moraes | Quinzenal | E-mail | GP |
| Reunião de acompanhamento | SQUAD PM/MM + Jerfesson Helmer | Semanal | Teams | GP |
| Relatório de fechamento de onda | Sponsor + Diretoria (quando confirmada — CB-1) | Ao final de cada onda | Documento | GP |
| Validação funcional / UAT | Tatiane Dias de Moraes + João Henrique | Por item, ao final de cada onda | Reunião + ambiente de teste | GP/SQUAD |

### 7. Plano de Gerenciamento dos Riscos
- **Abordagem:** Identificação inicial dos riscos de alto nível registrada no
  TAP (riscos fiscal/contábil dos itens 13/14, impacto organizacional do item
  5, estouro orçamentário, governança/aprovação CB-1/CB-2, priorização CB-4 e
  disponibilidade do especialista). Análise qualitativa (probabilidade x
  impacto) e plano de resposta detalhados no início de cada onda.
- **Frequência de revisão:** A cada status report quinzenal, com revisão
  extraordinária ao final de cada onda.
- **Ferramenta:** Registro de Riscos em Markdown, vinculado aos itens de
  escopo afetados.
- **Alerta automático:** Risco classificado como ALTO (ex.: itens 13/14, item
  5, ou estouro orçamentário) gera notificação imediata ao Sponsor.

### 8. Plano de Gerenciamento das Aquisições
- **Abordagem:** Não há aquisições externas previstas — execução 100% interna
  pelo SQUAD PM/MM (Time de Sustentação ERP), sem contratação de terceiros.
- **Itens a contratar:** Nenhum identificado no escopo atual.
- **Processo de aprovação:** Caso surja necessidade de contratação externa
  (ex.: consultoria especializada para itens 13/14), valores acima de R$ 5.000
  requerem aprovação do Sponsor; acima de R$ 30.000 requerem aprovação de
  Diretoria (sujeito à confirmação de CB-1).

### 9. Plano de Gerenciamento dos Stakeholders
- **Abordagem:** Stakeholders identificados na seção "Partes Interessadas
  Principais" do TAP (Sponsor provisório, solicitante, co-solicitante,
  especialista de referência, SQUAD PM/MM, aprovador de TI a confirmar,
  Diretoria, usuários finais), engajados conforme seu nível de
  interesse/influência — atenção especial à resolução das pendências de
  governança (CB-1, CB-2) com Diretoria.
- **Ferramenta:** Registro de Stakeholders + Mapa de Influência/Interesse.
- **Frequência de revisão:** Mensal, ou imediatamente após resolução de
  CB-1/CB-2/CB-4.

### 10. Plano de Gerenciamento das Mudanças
**Processo de solicitação de mudança:**
1. Solicitante (Tatiane Dias de Moraes, João Henrique ou outro stakeholder)
   preenche formulário de mudança descrevendo o item afetado e a alteração
   proposta.
2. GP avalia impacto em escopo (relação com os 15 itens/3 ondas), prazo,
   custo (frente ao teto de R$ 30.000/estimativa de R$ 36.000) e qualidade.
3. Sponsor (Nubia Souza, ou Diretoria quando CB-1 for resolvida) aprova
   mudanças com impacto em mais de uma onda, em itens classificados como
   ALTA complexidade (5, 7, 13, 14), ou que alterem o orçamento total.
4. Baseline (escopo, cronograma e orçamento) atualizada após aprovação e
   comunicada a todos os stakeholders no próximo status report.

### Ciclo de Vida e Gates
| Gate | Critério de Progressão | Aprovador |
|------|----------------------|-----------|
| G1 — Iniciação aprovada | TAP, PM Canvas e Plano Geral aprovados; CB-1, CB-2, CB-3, CB-4 resolvidas | Sponsor (Nubia Souza) / Diretoria |
| G2 — Planejamento da Onda 1 completo | Estimativa de esforço (CB-5) entregue; WBS e cronograma da Onda 1 aprovados | GP + Sponsor |
| G3 — Onda 1 concluída | Itens 2,3,4,6,9,11,15 implementados e validados (UAT) | GP |
| G4 — Onda 2 concluída | Itens 1,8,10,12 implementados e validados; orçamento revalidado (CB-Orçamento) | GP + Sponsor |
| G5 — Onda 3 concluída / Go-live final | Itens 5,7,13,14 implementados; especificação funcional e plano de testes (CB-6) executados; UAT aprovado | Sponsor |
| G6 — Encerramento | Lições aprendidas documentadas + aceite formal da equipe de Contabilidade/Controle de Ativos | Sponsor |
```

---

## Verificação de Consistência Cross-Documento

| Elemento | TAP | PM Canvas | Plano Geral |
|---|---|---|---|
| Sponsor | Nubia Carla Freitas Santos Souza (provisório), Diretoria pendente (CB-1) | Idêntico | Idêntico |
| Prazo final | 2026-09-30 | 2026-09-30 | 2026-09-30 (Gate G5/G6) |
| Orçamento total | R$ 36.000 (R$ 30.000 + 20% contingência) | R$ 36.000 | R$ 36.000 (referência no Plano de Custos) |
| Escopo (15 itens / 3 ondas) | Detalhado por onda | Detalhado por onda | Referenciado por onda nos Gates |
| Stakeholders principais | 8 partes interessadas listadas | Mesmas partes no bloco "Quem?" | Mesmas partes no Plano de Stakeholders |
| Riscos de alto nível | 6 riscos (3 ALTO, 2 MÉDIO, 1 BAIXO) | Top 6 listados no bloco "Riscos" | Referenciados no Plano de Riscos |
| CBs herdadas (CB-1 a CB-6, CB-Orçamento) | Registradas como restrições/riscos | Registradas em Restrições/Riscos | Referenciadas nos Gates e Planos de Custo/Riscos/Mudanças |

**Resultado:** Consistente — prazo (2026-09-30), orçamento (R$ 36.000) e
sponsor são idênticos nos três documentos. Todas as 6 Condições Bloqueantes
(CB-1 a CB-6) e a recomendação CB-Orçamento foram registradas como
pendências/restrições/riscos, sem bloquear a criação desta documentação.
```
