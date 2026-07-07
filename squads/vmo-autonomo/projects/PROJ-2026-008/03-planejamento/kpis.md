# FRAMEWORK DE KPIs — PROJ-2026-008
Implantação/Expansão do TVM para Fluxo de Caixa, Controle Orçamentário e
Rastreabilidade de Riscos (Grupo Águia Branca)

Autora: Marcela Métrica (Monitora de Performance, VMO Autônomo)
Data: 2026-07-07 | Versão: 1.0 | Status: RASCUNHO (documentação de iniciação
ainda com 6 CBs em aberto — ver `documentacao-base.md`)

Fontes: `documentacao-base.md` (TAP — critérios de sucesso, orçamento),
`cronograma.md` (Carlos Cronograma — WBS, marcos M0-M6), `plano-riscos.md`
(Pedro Perigo — registro de riscos e reserva de contingência).

---

## ⚠️ Alerta Metodológico Crítico — BAC Provisório (leia antes de usar o EVM abaixo)

O TAP registra **duas faixas de orçamento não reconciliadas**:
- Faixa sinalizada como aprovada pela CEO: **R$ 30.000 – R$ 32.000**
- Estimativa real de custo pelo sizing (206–334h): **R$ 43.080 – R$ 69.720**
- Reconciliação entre as duas é a **CB-3**, ainda **pendente**.

Este framework **não escolhe arbitrariamente** um dos dois valores como se a
pendência estivesse resolvida. Para permitir o cálculo de EVM desde já (o
projeto precisa de instrumentação de custo mesmo em RASCUNHO), adota-se:

> **BAC PROVISÓRIO = R$ 31.000** (ponto médio da faixa hoje sinalizada como
> aprovada, R$30.000–32.000) — **não** o valor do sizing (R$43-70k), porque
> este último ainda não foi formalmente aprovado como orçamento do projeto.

**Isto é um artefato de instrumentação, não uma resolução de CB-3.**
Consequências explícitas:
1. O CPI/EAC/VAC calculados com este BAC **medem consumo relativo a um
   orçamento ainda não fechado** — um CPI "saudável" (≥0,95) contra o BAC
   provisório **não significa que o projeto está dentro do orçamento real**,
   significa apenas que está dentro da faixa hoje sinalizada como aprovada.
   Como o sizing aponta custo real de R$43-70k, é matematicamente esperado
   que o CPI real (contra o custo total do projeto) seja pior do que o CPI
   contra este BAC provisório — R-002 (CRÍTICO, plano-riscos.md) já cobre
   esse gap.
2. **No momento em que CB-3 for resolvida** (valor único aprovado pela
   CEO/sponsor), este framework deve ser atualizado: o BAC será substituído
   pelo valor reconciliado, e todo o histórico de CPI/EAC/VAC recalculado
   com o BAC final antes de qualquer leitura de tendência ser levada ao
   sponsor.
3. Até lá, todo relatório de status que exiba CPI/EAC/VAC **deve** repetir
   esta ressalva — nunca apresentar o BAC de R$31.000 como definitivo.

---

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|---------|----------|------|-----------|------------|-------|-------------|
| CPI (Cost Performance Index) | EV / AC | 1,00 | ≥ 0,95 | 0,85–0,95 | < 0,85 | Quinzenal | GP (a designar) / PMO (Marcelo Silveira) até designação |
| SPI (Schedule Performance Index) | EV / PV | 1,00 | ≥ 0,95 | 0,85–0,95 | < 0,85 | Quinzenal | GP (a designar) / PMO |
| EAC (Estimate at Completion) | BAC ÷ CPI | R$ 31.000 (BAC provisório) | ≤ R$ 32.632 | R$ 32.632–36.471 | > R$ 36.471 | Quinzenal | GP / PMO |
| VAC (Variance at Completion) | BAC − EAC | R$ 0 | ≥ −R$ 1.632 | −R$ 5.471 a −R$ 1.632 | < −R$ 5.471 | Quinzenal | GP / PMO |

⚠️ EAC/VAC calculados acima usam o BAC provisório de R$31.000. **No dia em
que CB-3 for resolvida**, se o valor final aprovado ficar mais próximo da
estimativa do sizing (R$43-70k), os limiares de EAC/VAC acima devem ser
recalculados na mesma hora — os valores em R$ acima **perdem validade**
assim que o BAC mudar; apenas a lógica percentual (CPI ≥0,95 / 0,85-0,95 /
<0,85) permanece válida.

**Regra de escalonamento de anomalia** (todos os KPIs de EVM e de
resultado): qualquer KPI com desvio **> 25%** em relação à meta é escalado
imediatamente ao GP e ao PMO (Marcelo Silveira), independentemente do
calendário quinzenal/mensal de reporte — não espera o próximo ciclo formal.

---

## Configuração do EVM

**BAC (Budget at Completion):** R$ 31.000 — **PROVISÓRIO**, ponto médio da
faixa aprovada (R$30-32k). Sujeito a recálculo integral quando CB-3 for
resolvida (ver alerta acima). Reserva de contingência calculada por Pedro
Perigo (R$56.750, valor esperado) **não está incluída neste BAC** — ela é
tratada como reserva de gerenciamento separada, a ser acionada/aprovada
conforme os gatilhos de risco se materializem, não como parte do baseline
de custo do escopo.

**Método de medição de EV:** por pacote de trabalho da WBS (Carlos
Cronograma, `cronograma.md`), **nunca por % de esforço gasto**:

| Tipo de pacote | Método | Exemplos (WBS) |
|---|---|---|
| Entregáveis de documentação/governança (CBs, ERF) | 0/100 | 1.1.2.x (CBs), 1.2.2.2 (ERF v2.0) |
| Pacotes de desenvolvimento/configuração | 50/50 (50% ao iniciar o pacote, 50% na aprovação/teste do pacote) | 1.3.1.x (Financeiro), 1.3.2.x (Suprimentos), 1.3.3.x (Riscos), 1.3.4.x (Transversal) |
| Testes e homologação (UAT por frente) | 0/100 (aprovado ou não aprovado) | 1.4.2, 1.4.3, 1.4.4 |
| Treinamento e cutover | 0/100 | 1.5.1, 1.5.2 |
| Acompanhamento pós-go-live (1 ciclo) | 0/100 no fechamento do ciclo (M5) | 1.5.3 |
| Atividades de gerenciamento contínuas (status report, gestão de riscos) | Proporcional ao tempo decorrido | 1.1.3, 1.1.4 |

**PV Baseline (curva S provisória)** — construída a partir dos marcos do
cronograma (`cronograma.md`) e da distribuição de esforço por fase (piso da
faixa do sizing, único dado de peso disponível até que os pacotes tenham
custo próprio na ERF v2.0). Pesos por fase: Fase 1 = 48h (17,8%), Fase 2 =
150h (55,6%), Fase 3 = 40h (14,8%), Fase 4 = 32h (11,9%) — médias da faixa
206-334h.

| Marco | Data (rel. a T0) | PV cumulativo (% do BAC) | PV cumulativo (R$, sobre BAC provisório) |
|-------|------------------|---------------------------|---------------------------------------------|
| M0 — Kick-off | T0 | 0% | R$ 0 |
| M1 — ERF v2.0 fechada | T0 + 10d | 17,8% | R$ 5.511 |
| M2 — Desenvolvimento completo | T0 + 38d | 73,3% | R$ 22.733 |
| M3 — UAT aprovado | T0 + 50d | 88,1% | R$ 27.311 |
| M4 — Go-live | T0 + 58d (sem buffer) / T0 + ~67d (com buffer 15%) | 100% | R$ 31.000 |
| M5 — Aceite pós-go-live | T0 + 88d | 100% (sem novo pacote de custo — período de observação) | R$ 31.000 |
| M6 — Encerramento | T0 + 90d | 100% | R$ 31.000 |

⚠️ Esta curva-S é **provisória em dois níveis**: (a) o BAC de referência é
provisório (CB-3), e (b) os pesos por fase vêm do sizing agregado, não de
custo por pacote da ERF — deve ser refinada assim que a ERF v2.0 (com
custo/esforço por RF individual) estiver fechada em M1.

---

## KPIs de Resultado do Projeto (derivados dos 5 Critérios de Sucesso do TAP)

| # Critério TAP | KPI | Descrição/Medição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|---|-----|-----------|----------|------|-----------|------------|-------|-------------|
| 1 | Cobertura de frentes em produção | Nº de frentes (Financeiro, Suprimentos, Riscos/Desempenho) operando no TVM em produção, com Excel deixando de ser fonte primária de apresentação à diretoria | 0/3 (0%) | 3/3 (100%) até M4 (Go-live, T0+~67d) | 2/3 (67%) até M4 | ≤1/3 (≤33%) até M4 | Por marco (M2/M3/M4) | GP / Cássio (líder técnico) |
| 2 | Validação do horizonte de previsão de 90 dias | Ciclo mensal completo de previsão de caixa a 90 dias operando sem intervenção manual (Critério de Sucesso #2 / marco M5) | Não iniciado | 1 ciclo completo validado até M5 (T0+88d), 0 intervenções manuais corretivas | Ciclo completo com 1–3 intervenções manuais pontuais | Ciclo não completado até M5, ou > 3 intervenções manuais | Ao fechar o ciclo (M5) + acompanhamento semanal durante o ciclo | Thamyris (ponto focal Riscos/Desempenho) / GP |
| 3 | Alertas de consumo orçamentário testados | % das faixas de alerta (70%, 85%) testadas e funcionando corretamente (sem falso positivo/negativo) em ao menos 1 ciclo orçamentário de Suprimentos | 0/2 (0%) | 2/2 (100%) testadas até UAT (M3, T0+50d) | 1/2 (50%) testada até M3 | 0/2 testada até M3 | No UAT (M3) + 1ª verificação em produção pós-go-live | Wellington Gonçalves (ponto focal Suprimentos) / Equipe TVM |
| 4 | Redução de dependência de Thamyris | % de redução nas horas/mês de Thamyris dedicadas à consolidação manual, vs. baseline pré-projeto | **PENDENTE DE QUANTIFICAÇÃO (CB-6)** — nenhuma fonte informou o volume de horas/mês hoje gasto; baseline provisório = "a levantar na Fase 1" | ≥ 70% de redução até M6 (Encerramento) — **meta provisória**, a confirmar/ajustar quando CB-6 for resolvida | 40–69% de redução | < 40% de redução, **ou** CB-6 seguir não quantificada até M1 (ERF v2.0 fechada) | Mensal a partir do go-live da frente Riscos/Desempenho | Thamyris / GP |
| 5 | Adoção pelas 3 áreas em 90 dias | % de usuários ativos das 3 áreas usando o TVM como ferramenta primária, 90 dias após o respectivo go-live de cada frente | 0% | ≥ 90% em cada frente, aos 90 dias pós-go-live da frente | 70–89% | < 70% | Mensal (pós-go-live de cada frente, até completar 90 dias) | GP / pontos focais de cada área (Alessandra, Wellington, Thamyris) |

⚠️ **KPI #4 tem a mesma natureza de pendência do BAC**: a meta de "≥70% de
redução" é **provisória**, baseada em referência qualitativa (Felipe
Filtro, qualificação), não em uma linha de base quantificada. Assim que
CB-6 for resolvida (horas/mês atuais levantadas com Thamyris/Alessandra),
este KPI deve ser recalibrado com baseline real antes de qualquer leitura
de "sucesso" ou "fracasso" ser reportada ao sponsor.

### KPIs Complementares (Qualidade e Satisfação — cobertura adicional além dos 5 critérios)

| KPI | Descrição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|-----------|----------|------|-----------|------------|-------|-------------|
| Qualidade dos dados parciais (RF-FIN-03/RF-RIS-02) | % de divergência entre relatório do TVM e cálculo manual de referência, para os 2 requisitos Must Have que operam em granularidade parcial (ver R-008, plano-riscos.md) | N/A (pré-UAT) | Divergência = R$ 0,00 no UAT | Divergência > R$ 0,00 e ≤ 1% do valor de referência | Divergência > 1% do valor de referência | No UAT (M3) e mensal pós-go-live (2 primeiros ciclos) | Equipe TVM / Diana Documento (documentação da limitação) |
| Satisfação dos pontos focais (NPS interno) | Pesquisa de satisfação pós-go-live com Alessandra, Wellington e Thamyris (0-10) | — | ≥ 8/10 (média das 3 frentes) | 6–7/10 | < 6/10 | Pós-go-live (30 dias, M5) | GP / Sara Status |
| Estabilidade de escopo | Nº de mudanças de escopo aprovadas formalmente (fora dos 5 itens já sinalizados como incertos por CB-5) | 0 | 0 mudanças não previstas | 1–2 mudanças aprovadas | > 2 mudanças, ou qualquer mudança não submetida a controle formal | Quinzenal | GP / PMO |

---

## Semáforo de Saúde do Projeto

Referência-base: semáforo padrão do VMO Autônomo (`pipeline/data/domain-framework.md`),
com a dimensão **Riscos** adaptada às condições reais deste projeto (ver nota
abaixo).

| Dimensão | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|----------|----------|-----------|------------|
| Cronograma (SPI) | ≥ 0,95 | 0,85–0,95 | < 0,85 |
| Custo (CPI, sobre BAC provisório — ver ressalva) | ≥ 0,95 | 0,85–0,95 | < 0,85 |
| Escopo | Sem mudanças não previstas | 1–2 mudanças aprovadas | > 2 mudanças, ou mudança fora de controle formal |
| **Riscos** (ver nota de calibração) | 0 riscos CRÍTICOS abertos e ≤ 1 risco ALTO ativo sem gatilho disparado | 1–2 riscos CRÍTICOS abertos, **com** plano de resposta ativo e **nenhum gatilho de materialização disparado** (situação de partida deste projeto) | Qualquer risco CRÍTICO com gatilho de materialização disparado (ver `plano-riscos.md`), **ou** ≥ 3 riscos CRÍTICOS abertos |
| Satisfação (NPS interno pontos focais) | ≥ 8/10 | 6–7/10 | < 6/10 |

### ⚠️ Nota de calibração da dimensão "Riscos" — este projeto NÃO nasce verde

O template padrão do VMO Autônomo assume "Riscos = Verde" como estado
inicial neutro ("sob controle"). **Isto não se aplica a este projeto**: o
registro de riscos de Pedro Perigo (`plano-riscos.md`) já identifica, desde
a linha de base (antes mesmo do kick-off), **2 riscos CRÍTICOS abertos**:

- **R-001** (Governança, score 20) — CBs de governança (CB-1/CB-2) sem
  evidência documental
- **R-002** (Financeiro, score 16) — gap entre orçamento aprovado (R$30-32k)
  e custo estimado real (R$43-70k)

Ambos têm plano de resposta ativo e gatilho de materialização definido
(R-001: kick-off atingido sem evidência documental anexada; R-002: proposta
de fornecedor retorna valor acima de R$32.000), mas **nenhum dos dois foi
"resolvido"** — apenas está sendo gerenciado. Reportar este projeto como
"Riscos = Verde" no dia 1 seria falso: esconderia que o valor esperado total
de riscos (R$56.750) já supera o próprio orçamento hoje sinalizado como
aprovado.

**Calibração adotada**: o semáforo de Riscos deste projeto **abre em
🟡 AMARELO** (não verde) desde o marco M0 (Kick-off), refletindo os 2
riscos CRÍTICOS já abertos com plano de resposta ativo. Ele só deve
retornar a 🟢 Verde quando R-001 e R-002 forem efetivamente fechados
(evidência documental obtida / orçamento reconciliado via CB-3) — não pela
simples passagem do tempo. Ele passa a 🔴 Vermelho se qualquer um dos dois
gatilhos de materialização definidos por Pedro Perigo for disparado, ou se
um terceiro risco CRÍTICO surgir no registro.

**Leitura consolidada de saúde na abertura do projeto (T0, antes de
qualquer execução):** Cronograma e Custo ainda não têm leitura (SPI/CPI só
existem após início da execução, baseline = 1,00); Escopo = Verde (nenhuma
mudança ainda); **Riscos = Amarelo** (calibração acima); Satisfação =
sem leitura (pesquisa só ocorre pós-go-live). O projeto **não deve ser
reportado como "tudo verde" no kick-off** — a dimensão de Riscos já
carrega uma ressalva ativa desde o dia zero.

---

## Resumo para o Sponsor / PMO

1. **BAC de R$31.000 é provisório** (ponto médio da faixa aprovada) —
   **não** reflete o custo real estimado (R$43-70k, sizing). CPI/EAC/VAC
   calculados com este BAC devem sempre vir acompanhados desta ressalva até
   CB-3 ser resolvida.
2. **5 KPIs de resultado**, um por critério de sucesso do TAP — o KPI #4
   (redução de dependência de Thamyris) também carrega uma meta provisória,
   pendente da mesma quantificação que falta em CB-6.
3. **O semáforo de Riscos abre em Amarelo, não Verde**, porque o projeto já
   nasce com 2 riscos CRÍTICOS abertos (R-001 governança, R-002 orçamento) —
   reportar "tudo verde" no kick-off seria omitir essa exposição já
   conhecida.
