# Plano de Gestão de Riscos — DEM-2026-008
Integração SGMM03 — Campos Empresa e Contrato (InterCompany)
Versão: 1.0 | Data: 2026-05-28
Analista: Pedro Perigo (VMO Autônomo)

---

## Registro de Riscos

| ID | Categoria | Descrição | Prob (1-5) | Impacto (1-5) | Score (P×I) | Nível |
|----|-----------|-----------|-----------|---------------|-------------|-------|
| R-001 | Governança | Sponsor não designado (CB-1 aberta) — atraso na autorização de decisões e marcos | 4 | 4 | 16 | **CRÍTICO** |
| R-002 | Técnico | Restrição técnica oculta nos campos Empresa/Contrato no SAP PM (similar ao Cenário/CenPlan) — aumentando escopo e prazo | 3 | 4 | 12 | **ALTO** |
| R-003 | Prazo/Comercial | Atraso no processo de equalização e contratação das consultorias — postergando kick-off e comprimindo prazo de execução | 3 | 3 | 9 | **ALTO** |
| R-004 | Técnico | Ambiente SAP (DEV/QAS/PRD) indisponível nas datas previstas por outros projetos paralelos ou janelas de manutenção | 2 | 3 | 6 | **MÉDIO** |
| R-005 | Escopo | Fluxo InterCompany SGMM03 impacta outras divisões do grupo além da VIX Matriz (lacuna L4 não resolvida) — ampliação de escopo não prevista | 2 | 4 | 8 | **MÉDIO** |
| R-006 | Qualidade | Consultora selecionada não tem familiaridade suficiente com o ambiente SGMM03 específico do GAB — necessitando de ramp-up adicional | 2 | 3 | 6 | **MÉDIO** |
| R-007 | Financeiro | Valor contratado da consultora excede o envelope referencial (R$ 34.800) — necessitando aprovação adicional | 2 | 2 | 4 | **BAIXO** |
| R-008 | Prazo | UAT da VIX Matriz demanda mais ciclos de correção que o previsto (2 iterações) — consumindo buffer | 2 | 3 | 6 | **MÉDIO** |

---

## Plano de Resposta por Risco

### R-001 — Sponsor Não Designado — CRÍTICO

- **Estratégia:** Evitar (resolução antes do kick-off)
- **Gatilho:** Sponsor não nomeado até 30/05/2026 (data prevista na CB-1)
- **Ações de Resposta:**
  1. Escalar para a liderança da Holding DTI a necessidade de nomeação do sponsor até 30/05/2026 — Responsável: GP/PMO — Prazo: 28/05/2026 (imediato)
  2. Propor candidatos ao papel de sponsor (Diretores da área de negócio VIX ou Holding) ao PMO — Responsável: Mara Rubia — Prazo: 29/05/2026
  3. Se sponsor não designado até 02/06: paralisar elaboração do TAP formal e emitir alerta de bloqueio — Responsável: GP — Prazo: 02/06/2026
- **Plano de Contingência:** Solicitar designação de sponsor interino com autoridade delegada pelo CIO/Diretor disponível, para desbloquear decisões de baixo impacto enquanto o sponsor permanente não é designado
- **Custo da Resposta:** R$ 0 (gestão interna)

---

### R-002 — Restrição Técnica Oculta nos Campos Empresa/Contrato — ALTO

- **Estratégia:** Mitigar
- **Gatilho:** Durante a análise técnica (Fase 1, atividade 1.2.2.1), a consultora identifica que os campos Empresa e/ou Contrato têm restrição de gravação via interface (ex: campo bloqueado, BAPI sem parâmetro, validação hard-coded)
- **Ações de Resposta:**
  1. Incluir na especificação técnica uma análise prévia das BAPIs/RFCs disponíveis para os campos Empresa e Contrato antes de iniciar o desenvolvimento — Responsável: Consultora — Prazo: 17/06/2026 (início da Fase 1)
  2. Consultar a documentação técnica do campo Cenário/CenPlan (que tem restrição conhecida) para identificar padrão de restrição no SGMM03 — Responsável: DTI + Consultora — Prazo: 17/06/2026
  3. Se restrição identificada: avaliar solução técnica alternativa (user-exit, BAdI, desenvolvimento Z) e reestimar prazo/custo antes de prosseguir — Responsável: GP + Consultora — Prazo: 20/06/2026
- **Plano de Contingência:** Solicitar change request para extensão de prazo em até 5 dias úteis + custo adicional da consultora para desenvolvimento alternativo (estimado R$ 3.000–8.000 adicionais)
- **Custo da Resposta:** R$ 0 (análise preventiva na Fase 1) / R$ 3.000–8.000 se contingência ativada

---

### R-003 — Atraso na Contratação — ALTO

- **Estratégia:** Mitigar
- **Gatilho:** Equalização das propostas não concluída em 29/05/2026 OU contrato não assinado até 13/06/2026
- **Ações de Resposta:**
  1. Confirmar com Mara Rubia o recebimento das propostas de Seletor e MW (que pediram prazo adicional) — Responsável: Mara Rubia — Prazo: 29/05/2026
  2. Definir critério de desempate técnico-comercial antes da reunião de equalização — Responsável: GP + Mara Rubia — Prazo: 28/05/2026
  3. Priorizar consultora com experiência comprovada em SGMM03 ou interfaces similares (reduz risco R-006 em paralelo)
- **Plano de Contingência:** Se contratação atrasar > 5 dias úteis além de 13/06: revisar cronograma comprimindo Fases 1 e 2 em paralelo (onde tecnicamente possível), aceitar risco de redução de buffer; se atraso > 2 semanas: replanejar prazo de go-live para agosto
- **Custo da Resposta:** R$ 0 (gestão interna) / Custo de oportunidade do atraso se contingência ativada

---

### R-004 — Indisponibilidade de Ambientes SAP — MÉDIO

- **Estratégia:** Mitigar
- **Gatilho:** Ambiente DEV, QAS ou PRD indisponível por mais de 2 dias úteis durante as janelas de desenvolvimento ou testes previstas
- **Ações de Resposta:**
  1. Confirmar as janelas de disponibilidade dos ambientes DEV/QAS/PRD com a equipe de infraestrutura da DTI antes do kick-off — Responsável: DTI (Mara Rubia) — Prazo: 16/06/2026
  2. Inscrever o projeto no calendário de mudanças do grupo para reservar as janelas de transporte necessárias — Responsável: DTI — Prazo: 16/06/2026
- **Plano de Contingência:** Realizar desenvolvimento em DEV alternativo se disponível, ou ajustar o cronograma de atividades para utilizar o tempo de indisponibilidade em documentação e preparação de testes
- **Custo da Resposta:** R$ 0

---

### R-005 — Impacto em Outras Divisões (Escopo Oculto) — MÉDIO

- **Estratégia:** Mitigar
- **Gatilho:** Durante a análise técnica, a consultora identifica que o fluxo InterCompany SGMM03 é utilizado por outras empresas do grupo além da VIX Matriz
- **Ações de Resposta:**
  1. Resolver a lacuna L4 (impacto em outras divisões) durante a Fase 1 — incluir pergunta na agenda do kick-off — Responsável: GP + DTI — Prazo: 16/06/2026 (kick-off)
  2. Se outras divisões forem identificadas: avaliar se a implementação afeta o fluxo delas e se testes adicionais são necessários — Responsável: GP — Prazo: 18/06/2026
- **Plano de Contingência:** Emitir Change Request para expansão controlada de escopo, com estimativa de impacto em prazo e custo e aprovação do sponsor
- **Custo da Resposta:** R$ 0 preventivo / Custo do Change Request se ativado (a estimar)

---

### R-006 — Ramp-up da Consultora — MÉDIO

- **Estratégia:** Mitigar
- **Gatilho:** Consultora declara na reunião de kick-off que não tem familiaridade com a interface SGMM03 específica do GAB e estima ramp-up > 3 dias úteis
- **Ações de Resposta:**
  1. Exigir na seleção da consultora (M1) comprovação de experiência em integração SAP PM — Responsável: GP + Mara Rubia — Prazo: durante seleção (até 06/06)
  2. Disponibilizar a documentação existente do SGMM03 (incluindo documentação do campo Centro de Planejamento) à consultora selecionada antes do kick-off — Responsável: DTI — Prazo: 13/06/2026
- **Plano de Contingência:** Designar analista técnico sênior da DTI como par da consultora para acelerar o ramp-up (dedicação de 50% na Fase 1)
- **Custo da Resposta:** R$ 0 preventivo / Custo de horas adicionais da consultora se ramp-up > 2 dias extras (estimado R$ 1.500–3.000)

---

### R-007 — Custo Acima do Envelope Referencial — BAIXO

- **Estratégia:** Aceitar com monitoramento
- **Gatilho:** Proposta selecionada > R$ 40.000 (teto do envelope referencial)
- **Ações de Resposta:**
  1. Se proposta > R$ 40.000: obter justificativa técnica detalhada da consultora para a diferença — Responsável: GP + Mara Rubia — Prazo: durante equalização (29/05)
  2. Apresentar justificativa ao sponsor para aprovação do novo envelope — Responsável: GP — Prazo: antes da assinatura do contrato
- **Plano de Contingência:** Se nenhuma proposta dentro do envelope: renegociar escopo para reduzir a fase de repasse/documentação como opcional, ou usar a contingência de 20% do orçamento
- **Custo da Resposta:** R$ 0 (gestão comercial)

---

### R-008 — UAT com Múltiplos Ciclos de Correção — MÉDIO

- **Estratégia:** Mitigar
- **Gatilho:** VIX Matriz identifica defeitos no UAT que requerem mais de 1 ciclo de correção (> 2 dias úteis de reteste)
- **Ações de Resposta:**
  1. Preparar casos de teste UAT em conjunto com a VIX Matriz antes do início (atividade 1.4.2.1) para garantir clareza dos critérios — Responsável: GP + Jenifer — Prazo: 11/07/2026
  2. Executar desk review dos critérios de aceitação dos RF Must Have com a consultora antes do UAT — Responsável: Consultora + GP — Prazo: 14/07/2026
- **Plano de Contingência:** Alocar os primeiros 3 dias do buffer (01/08–03/08) para correção de defeitos UAT residuais, se necessário
- **Custo da Resposta:** R$ 0 preventivo / Uso de até 3 dias do buffer se ciclo adicional de UAT necessário

---

## Reserva de Contingência Calculada

| ID | Risco | Prob (%) | Impacto Financeiro (R$) | Valor Esperado (R$) |
|----|-------|----------|------------------------|---------------------|
| R-001 | Sponsor não designado (atraso geral) | 40% | R$ 5.000 (custo atraso geral) | R$ 2.000 |
| R-002 | Restrição técnica oculta | 30% | R$ 8.000 (desenvolvimento alternativo) | R$ 2.400 |
| R-003 | Atraso na contratação | 30% | R$ 4.000 (replanejamento/custo oportunidade) | R$ 1.200 |
| R-004 | Indisponibilidade ambientes SAP | 20% | R$ 2.000 (atraso e replanejamento) | R$ 400 |
| R-005 | Escopo oculto outras divisões | 20% | R$ 6.000 (ampliação de escopo) | R$ 1.200 |
| R-006 | Ramp-up da consultora | 20% | R$ 3.000 (horas adicionais) | R$ 600 |
| R-007 | Custo acima do envelope | 25% | R$ 5.200 (diferença do envelope) | R$ 1.300 |
| R-008 | UAT com múltiplos ciclos | 25% | R$ 2.500 (horas correção + reteste) | R$ 625 |
| **TOTAL** | | | | **R$ 9.725** |

**Reserva recomendada: R$ 6.960** (20% do valor total do projeto de R$ 34.800 — já incluída no orçamento como contingência)

> **Observação:** O VME calculado (R$ 9.725) supera ligeiramente a contingência de 20% do orçamento
> (R$ 5.800). Recomenda-se ao sponsor avaliar se a contingência deve ser elevada para R$ 9.725
> (28% do contrato) ou se aceita o risco residual de R$ 2.765. Dado o perfil de baixa complexidade
> da demanda, aceitar o risco residual é razoável — mas deve ser uma decisão consciente do sponsor.

---

## Política de Revisão dos Riscos

- **Frequência de revisão:** Quinzenal (junto ao status report)
- **Riscos CRÍTICOS/ALTOS:** Revisão imediata a cada nova informação relevante
- **Novos riscos identificados:** Adicionados ao registro e avaliados na próxima reunião de status
- **Responsável:** GP — com comunicação imediata ao sponsor para riscos CRÍTICOS
