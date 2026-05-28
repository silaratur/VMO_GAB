# Framework de KPIs — DEM-2026-008
Integração SGMM03 — Campos Empresa e Contrato (InterCompany)
Versão: 1.0 | Data: 2026-05-28
Analista: Marcela Métrica (VMO Autônomo)

---

## Configuração EVM

| Parâmetro | Valor |
|-----------|-------|
| **BAC (Budget at Completion)** | R$ 34.800 |
| **Método de medição de EV** | Porcentagem física concluída por entregável aprovado |
| **Data de início do baseline** | 2026-06-16 |
| **Data de fim do baseline (sem buffer)** | 2026-07-31 |
| **Data de fim máxima (com buffer)** | 2026-08-08 |
| **Período de reporte** | Quinzenal |

**Regras de medição de EV por tipo de entregável:**
- Entregável aprovado (spec, relatório de testes, aceite UAT): 100% do peso quando aprovado, 0% antes
- Atividades de desenvolvimento: 50% quando desenvolvimento concluído em DEV, 100% quando aprovado em QAS
- Atividades de testes: 0% → 50% → 100% (iniciado → em progresso → aprovado)

**Pesos dos entregáveis para cálculo do PV e EV:**

| Entregável | Peso (% do BAC) |
|------------|-----------------|
| E1 — Especificação Funcional aprovada | 10% |
| E2 — Especificação Técnica aprovada | 5% |
| E3 — Desenvolvimento + Testes DEV completos | 35% |
| E4 — Testes QAS aprovados | 15% |
| E5 — UAT aprovado | 15% |
| E6 — Go-live PRD | 10% |
| E7 — Documentação + Repasse à sustentação | 8% |
| E8 — Encerramento formal | 2% |
| **TOTAL** | **100%** |

---

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|---------|----------|------|-----------|------------|-------|-------------|
| **CPI** (Cost Performance Index) | EV / AC | 1,00 | ≥ 1,00 | 0,85 – 0,95 | < 0,85 | Quinzenal | GP |
| **SPI** (Schedule Performance Index) | EV / PV | 1,00 | ≥ 1,00 | 0,85 – 0,95 | < 0,85 | Quinzenal | GP |
| **EAC** (Estimate at Completion) | BAC / CPI | R$ 34.800 | ≤ R$ 34.800 | R$ 34.800 – R$ 40.000 | > R$ 40.000 | Quinzenal | GP |
| **VAC** (Variance at Completion) | BAC – EAC | R$ 0 | ≥ R$ 0 | R$ -5.200 a R$ 0 | < –R$ 5.200 | Quinzenal | GP |
| **SV** (Schedule Variance) | EV – PV | R$ 0 | ≥ R$ 0 | R$ -3.480 a R$ 0 | < –R$ 3.480 | Quinzenal | GP |
| **CV** (Cost Variance) | EV – AC | R$ 0 | ≥ R$ 0 | R$ -3.480 a R$ 0 | < –R$ 3.480 | Quinzenal | GP |

---

## KPIs de Resultado do Projeto

| KPI | Descrição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|-----------|----------|------|-----------|------------|-------|-------------|
| **Taxa de Integração Correta** | % das OMs InterCompany com campos Empresa e Contrato gravados automaticamente (verificado nos primeiros 15 dias pós go-live) | 0% | 100% | 95–99% | < 95% | Diária (15 dias pós go-live) | DTI |
| **Taxa de Falhas de Integração** | % de OMs InterCompany que geraram erro de integração nos campos Empresa/Contrato | 0% | 0% | 0,1–2% | > 2% | Diária (15 dias pós go-live) | DTI + Consultora (garantia) |
| **Preenchimentos Manuais Residuais** | Número de OMs onde os campos Empresa/Contrato precisaram ser preenchidos manualmente após go-live (target: zero) | N/A | 0 ocorrências | 1–3 ocorrências | > 3 ocorrências | Semanal (30 dias pós go-live) | DTI + VIX Matriz |
| **UAT — Casos de Teste Aprovados** | % dos casos de teste UAT (Must Have) aprovados pela VIX Matriz na 1ª execução | 0% | 100% | 85–99% | < 85% | Por ciclo de UAT | Jenifer (VIX Matriz) |
| **Satisfação VIX Matriz (NPS)** | Nota de satisfação da solicitante com a entrega (0–10) | — | ≥ 8/10 | 6–7/10 | < 6/10 | Pós-encerramento | GP |
| **Cobertura da Documentação** | % dos entregáveis de documentação aprovados pelo time de sustentação DTI PM/FI | 0% | 100% | 85–99% | < 85% | Pós-encerramento | DTI PM/FI |

---

## KPIs de Gestão de Riscos

| KPI | Descrição | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. | Responsável |
|-----|-----------|----------|------|-----------|------------|-------|-------------|
| **Riscos ALTOS abertos** | Número de riscos classificados como ALTO ou CRÍTICO sem plano de resposta ativo | 2 (R-001, R-002) | 0 riscos ALTO/CRÍTICO sem tratamento | 1 risco | > 1 risco | Quinzenal | GP |
| **CB-1 Status** | Status da Condição Bloqueante — Sponsor nomeado | ABERTA | RESOLVIDA até 30/05/2026 | EM ATRASO (após 30/05) | NÃO RESOLVIDA até kick-off | Diária até resolução | GP |
| **CB-2 Status** | Status da Condição Bloqueante — Orçamento aprovado | ABERTA | RESOLVIDA até 02/06/2026 | EM ATRASO (após 02/06) | NÃO RESOLVIDA até contrato | Diária até resolução | GP |

---

## Semáforo de Saúde do Projeto

| Dimensão | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|----------|----------|------------|-------------|
| **Cronograma (SPI)** | SPI ≥ 0,95 | SPI 0,85–0,95 | SPI < 0,85 |
| **Custo (CPI)** | CPI ≥ 0,95 | CPI 0,85–0,95 | CPI < 0,85 |
| **Escopo** | 0 mudanças de escopo | 1 change request aberto | > 1 change request ou mudança não aprovada |
| **Riscos** | 0 riscos CRÍTICOS/ALTOS sem tratamento | 1 risco ALTO em monitoramento | Qualquer risco CRÍTICO sem plano ativo |
| **Qualidade (UAT)** | 100% Must Have aprovados | 85–99% aprovados (em correção) | < 85% aprovados ou defeito crítico |
| **Integração (Pós go-live)** | 0 falhas de integração | 1–3 falhas com correção em garantia | > 3 falhas ou falha sistêmica |
| **Condições Bloqueantes** | Todas CBs resolvidas | 1 CB aberta com plano de resolução | 1+ CB aberta sem plano ou em atraso |
| **Satisfação VIX Matriz** | NPS ≥ 8/10 | NPS 6–7/10 | NPS < 6/10 |

---

## Relatório de Status de KPIs — Iniciação (28/05/2026)

> Status inicial do projeto — fase de qualificação concluída, execução ainda não iniciada.

| KPI | Valor Atual | Status | Observação |
|-----|-------------|--------|------------|
| CPI | N/A (pré-execução) | — | Baseline estabelecido em R$ 34.800 |
| SPI | N/A (pré-execução) | — | Baseline: kick-off em 16/06/2026 |
| Taxa de Integração Correta | N/A | — | Medição inicia após go-live |
| CB-1 (Sponsor) | ABERTA | 🔴 | Prazo: 30/05/2026 — 2 dias úteis restantes |
| CB-2 (Orçamento) | ABERTA | 🟡 | Prazo: 02/06/2026 — aguardando equalização propostas |
| Riscos ALTO/CRÍTICO sem tratamento | 2 (R-001, R-002) | 🟡 | R-001 será resolvido com CB-1; R-002 em fase de análise |

**Status Geral da Iniciação: 🟡 ATENÇÃO** — CBs críticas abertas (sponsor e orçamento), aguardando resolução até 02/06/2026 para liberar o kick-off.
