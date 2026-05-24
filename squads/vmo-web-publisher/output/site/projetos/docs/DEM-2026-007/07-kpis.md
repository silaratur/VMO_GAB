# Framework de KPIs — DEM-2026-007
Projeto: Implantação DDA SAP — VAB Matriz
Elaborado por: Marcela Métrica (VMO Autônomo)
Data: 2026-05-20
Versão: 1.0

BAC (Budget at Completion): R$2.000 (reserva de contingência — custo externo meta: R$0)
Método de medição de EV: Marcos binários (0% / 100%) por fase do cronograma

---

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Linha de Base | Limiar Amarelo | Limiar Vermelho | Responsável |
|-----|---------|--------------|---------------|----------------|-------------|
| **SPI** (Schedule Performance Index) | EV / PV | 1,00 | 0,85 – 0,94 | < 0,85 | GP |
| **CPI** (Cost Performance Index) | EV / AC | 1,00 | 0,85 – 0,94 | < 0,85 | GP |
| **EAC** (Estimate at Completion) | BAC / CPI | R$2.000 | R$2.001–R$2.350 | > R$2.350 | GP |
| **VAC** (Variance at Completion) | BAC – EAC | R$0 | -R$350 a -R$1 | < -R$350 | GP |
| **% Conclusão** | Marcos concluídos / Total marcos | 0% (início) | N/A | N/A | GP |

> **Nota:** Como o custo alvo é R$0 externo, o EVM monitora principalmente o prazo (SPI).
> O CPI e EAC aplicam-se somente se a reserva de contingência (R$2.000) for acionada.

---

## Configuração EVM

| Parâmetro | Valor |
|-----------|-------|
| BAC (Budget at Completion) | R$2.000 |
| Método de EV | Marcos binários — 100% somente quando o marco está 100% concluído |
| Marcos totais | 6 (M-0 a M-6) |
| PV por marco | M-0: 0%; M-1: 17%; M-2: 30%; M-3: 55%; M-4: 70%; M-5: 85%; M-6: 100% |
| Frequência de cálculo | Quinzenal (em cada Status Report) |
| Custo horas internas | Não contabilizado no EVM (custo interno DTI — fora do BAC) |

**Tabela de valor planejado (PV) por marco:**

| Marco | Data | % PV acumulado | PV R$ (sobre BAC R$2.000) |
|-------|------|---------------|--------------------------|
| M-0 — Gate Kick-off | 06/06/2026 | 0% | R$0 |
| M-1 — Levantamento técnico | 27/06/2026 | 17% | R$340 |
| M-2 — Habilitação Santander | 18/07/2026 | 30% | R$600 |
| M-3 — Config + testes homologação | 08/08/2026 | 55% | R$1.100 |
| M-4 — UAT aprovado | 15/08/2026 | 70% | R$1.400 |
| M-5 — Go-live | 25/08/2026 | 85% | R$1.700 |
| M-6 — Encerramento | 30/09/2026 | 100% | R$2.000 |

---

## KPIs de Resultado (vinculados aos Critérios de Sucesso do TAP)

| KPI | Critério de Sucesso | Meta | Limiar Mínimo | Quando Medir | Responsável |
|-----|--------------------|----|--------------|-------------|-------------|
| **KR-1** Taxa de automação DDA | CS-1: 100% boletos DDA sem digitação manual | 100% | ≥ 99% | 30 dias pós-go-live | GP + DTI FI |
| **KR-2** Incidentes por ausência de boleto | CS-2: Zero atrasos por ausência de boleto digital | 0 ocorrências/mês | ≤ 1 por mês | 60 dias pós-go-live | Noemia / CP |
| **KR-3** Satisfação equipe CP | CS-3: ≥ 8/10 na pesquisa pós-implantação | ≥ 8,0/10 | ≥ 7,0/10 | 30 dias pós-go-live | GP |
| **KR-4** Prazo de go-live | CS-4: Go-live até 30/09/2026 | 30/09/2026 | ≤ 14/10/2026 | Data do go-live | GP |
| **KR-5** Tempo de processamento arquivo DDA | RNF-002: ≤ 30 min para arquivo com até 500 boletos | ≤ 30 min | ≤ 60 min | Semana 1 em produção | DTI FI |
| **KR-6** Disponibilidade DDA | RNF-001: ≥ 99,5% em horário bancário | 99,5% | 98% | Primeiro mês em produção | DTI FI |

---

## Semáforo de Saúde do Projeto

| Dimensão | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|----------|---------|-----------|------------|
| **Cronograma** (SPI) | ≥ 0,95 | 0,85 – 0,94 | < 0,85 |
| **Custo** (CPI) | ≥ 0,95 | 0,85 – 0,94 | < 0,85 |
| **Escopo** | Sem mudanças não controladas | 1 CR em análise | > 1 CR ou CR crítico |
| **Riscos** | Todos sob controle | 1 risco ALTO ativo | 1+ risco CRÍTICO ativo ou R-001/R-002 materializados |
| **Governança** | CBs resolvidas | 1 CB em prazo | CB vencida sem resolução |
| **Resultado (pós go-live)** | KR-1 = 100%; KR-2 = 0 | KR-1 ≥ 95%; KR-2 ≤ 2 | KR-1 < 95%; KR-2 > 2 |

---

## KPIs de Gestão de Riscos

| KPI | Meta | Limiar | Quando |
|-----|------|--------|--------|
| Riscos CRÍTICOS ativos | 0 | ≤ 0 | Contínuo |
| Riscos ALTOS ativos sem plano de resposta | 0 | ≤ 0 | Quinzenal |
| % riscos com trigger definido | 100% | ≥ 100% | Por revisão |
| R-001 (autorização Holding): status | Resolvido antes do kick-off | Resolvido em M-0 | Gate kick-off |
| R-002 (ajustes ABAP): status | Confirmado como parametrização em M-1 | Confirmado em M-1 | Gate M-1 |

---

## Pesquisa de Satisfação — Template

A pesquisa será aplicada 30 dias após o go-live (KR-3):

**Bloco 1 — NPS**
- Em uma escala de 0 a 10, qual a probabilidade de você recomendar o novo processo de DDA a um colega de outra divisão?

**Bloco 2 — Percepção do resultado**
- O processo de recebimento de boletos melhorou com a implantação do DDA? (1 = Muito pior / 10 = Muito melhor)
- Você ainda precisa digitar manualmente algum código de barras? (Sim / Não / Às vezes)
- O processo de obtenção de boletos eliminou a dependência de terceiros? (1 = Não mudou / 10 = Totalmente eliminada)

**Bloco 3 — Qualitativo**
- Qual foi o maior benefício percebido no novo processo?
- Há algo que ainda poderia ser melhorado?
