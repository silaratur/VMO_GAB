---
task: "Qualificar Demanda"
order: 1
input:
  - demanda_estruturada: "Output do checkpoint de validação (demanda-validada.md)"
  - documentos_estrategicos: "OKRs ou objetivos organizacionais disponíveis"
output:
  - analise_qualificacao: "Avaliação dos 12 critérios (6 de valor + 6 de complexidade) com pontuação e justificativa"
  - modalidade: "PROJETO FORMAL / GOVERNANÇA LEVE / TAREFA OPERACIONAL"
  - decisao: "APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA"
  - proximos_passos: "Ações requeridas com responsável e prazo"
---

# Qualificar Demanda

Avalia se a demanda deve ser transformada em projeto formal, tratada com governança leve ou encaminhada como tarefa operacional. A qualificação opera em **duas fases complementares**:

- **Fase 1 — Valor da Demanda** (6 critérios, 1-5 cada, máx 30 pts): determina se a demanda *vale a pena* — alinhamento, viabilidade, ROI, urgência, maturidade e recursos.
- **Fase 2 — Filtro de Complexidade** (6 critérios binários, máx 6 pts): determina se a demanda *precisa de projeto formal* — esforço, impacto organizacional, integração, mudança de processo, governança e risco regulatório.

A combinação dos dois eixos gera a decisão final e a **modalidade de execução**, evitando que demandas de baixo valor sejam aprovadas como projetos e que demandas complexas sejam subestimadas como tarefas.

---

## Process

### Fase 1 — Valor da Demanda

1. **Carregar contexto estratégico**: Ler OKRs e objetivos organizacionais disponíveis.
2. **Avaliar os 6 critérios de valor**: Para cada critério, atribuir pontuação de 1 a 5 com justificativa de ao menos 2 linhas baseada em dados da demanda.
3. **Calcular score de valor**: Somar os 6 critérios (máximo 30) e calcular percentual.

### Fase 2 — Filtro de Complexidade

4. **Avaliar os 6 critérios de complexidade**: Para cada critério, responder SIM (1 pt) / PARCIAL (0,5 pt) / NÃO (0 pt) com justificativa de ao menos 1 linha. Nunca inferir — se não houver dados, marcar PARCIAL com questionamento.
5. **Calcular score de complexidade**: Somar os 6 critérios (máximo 6 pontos).
6. **Classificar complexidade**: ALTA (≥ 4 pts) / MÉDIA (2–3 pts) / BAIXA (≤ 1 pt).

### Decisão Final

7. **Cruzar valor × complexidade** usando a matriz abaixo e determinar **modalidade** e **decisão**:

| Score de Valor | Complexidade | Modalidade | Decisão |
|---|---|---|---|
| ≥ 70% (≥ 21/30) | ALTA (≥ 4) | Projeto Formal | APROVADO |
| ≥ 70% (≥ 21/30) | MÉDIA (2–3) | Governança Leve | APROVADO |
| ≥ 70% (≥ 21/30) | BAIXA (≤ 1) | Tarefa Operacional | APROVADO |
| 50–69% (15–20/30) | ALTA (≥ 4) | Projeto Formal | APROVADO COM CONDIÇÕES |
| 50–69% (15–20/30) | MÉDIA ou BAIXA | — | EM ESPERA |
| < 50% (< 15/30) | qualquer | — | REPROVADO |

> **Nota sobre modalidades:**
> - **Projeto Formal** → segue para o pipeline completo VMO (TAP, ERF, Cronograma, Riscos, KPIs, WR)
> - **Governança Leve** → segue pipeline simplificado — TAP reduzido + acompanhamento quinzenal, sem necessariamente ERF completa
> - **Tarefa Operacional** → encaminhada para a área responsável sem pipeline VMO; monitoramento operacional apenas

8. **Definir próximos passos**: Para aprovação, listar ações de iniciação. Para condições, listar o que deve ser resolvido com responsável e prazo. Para reprovação, documentar motivo e aprendizado.

---

## Output Format

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: [DEM-AAAA-NNN]
Data: YYYY-MM-DD
Analista: Felipe Filtro (VMO Autônomo)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 1 — CRITÉRIOS DE VALOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Alinhamento Estratégico    [N/5]
   [qual OKR/objetivo endereça; nível de confiança]

2. Viabilidade Técnica        [N/5]
   [recursos, tecnologia, complexidade técnica estimada]

3. Retorno sobre Investimento [N/5]
   [benefício estimado, custo estimado, payback em meses]

4. Urgência                   [N/5]
   [impacto de não fazer; pressão temporal concreta]

5. Maturidade da Demanda      [N/5]
   [clareza do problema, completude das informações disponíveis]

6. Disponibilidade de Recursos [N/5]
   [equipe, orçamento, conflitos de portfólio]

SCORE DE VALOR: [total]/30 ([%]%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 2 — FILTRO DE COMPLEXIDADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7. Esforço Estimado > 160h           [SIM=1 / PARCIAL=0,5 / NÃO=0]
   [estimativa de esforço com base no escopo; se incerto, usar PARCIAL]

8. Impacto Organizacional Amplo      [SIM=1 / PARCIAL=0,5 / NÃO=0]
   [quantas áreas/divisões são impactadas; se apenas 1 área, NÃO]

9. Integração entre Sistemas         [SIM=1 / PARCIAL=0,5 / NÃO=0]
   [há necessidade de integrar ERP com outros sistemas? qualquer integração técnica formal]

10. Mudança de Processo Relevante    [SIM=1 / PARCIAL=0,5 / NÃO=0]
    [há alteração de fluxo operacional, papéis, responsabilidades ou ferramentas de trabalho?]

11. Governança Formal Necessária     [SIM=1 / PARCIAL=0,5 / NÃO=0]
    [a entrega exige acompanhamento formal — marcos, aprovações, relatórios — ou pode ser feita de forma autônoma?]

12. Impacto Regulatório ou Financeiro [SIM=1 / PARCIAL=0,5 / NÃO=0]
    [há risco de compliance, exposição legal, impacto em demonstrativos financeiros ou auditorias?]

SCORE DE COMPLEXIDADE: [X]/6 → [ALTA ≥4 / MÉDIA 2–3 / BAIXA ≤1]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESULTADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCORE DE VALOR: [total]/30 ([%]%)
COMPLEXIDADE: [X]/6 → [ALTA / MÉDIA / BAIXA]
MODALIDADE: [PROJETO FORMAL / GOVERNANÇA LEVE / TAREFA OPERACIONAL]
DECISÃO: [APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA]

CONDIÇÕES BLOQUEANTES (se aplicável):
- [condição que deve ser resolvida antes de prosseguir]

PRÓXIMOS PASSOS:
| Ação | Responsável | Prazo |
|------|-------------|-------|
```

---

## Output Example

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-047
Data: 2026-04-11
Analista: Felipe Filtro (VMO Autônomo)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 1 — CRITÉRIOS DE VALOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Alinhamento Estratégico    4/5
   OKR Q1/2026: "Reduzir falhas de fornecimento em 30%" — endereçamento direto.
   Confiança: ALTA (OKR documentado; ata de reunião confirma pressão do board).

2. Viabilidade Técnica        3/5
   SAP possui API de integração confirmada pela área de TI.
   Complexidade da integração legada pode gerar risco de escopo.
   Requer POC técnica para confirmar viabilidade. Confiança: MÉDIA.

3. Retorno sobre Investimento 4/5
   Custo estimado: R$ 280.000. Benefício: R$ 520.000/ano (economia de rupturas).
   Payback estimado: 6,5 meses. Confiança: MÉDIA (baseado em benchmarks).

4. Urgência                   5/5
   3 incidentes de ruptura em Q1/2026 com custo R$135.000.
   Reunião de avaliação de fornecedores em julho exige solução implementada.

5. Maturidade da Demanda      3/5
   Problema bem definido, solução técnica clara.
   Gaps: sponsor não designado, orçamento não formalizado.

6. Disponibilidade de Recursos 3/5
   Orçamento sinalizado como disponível (aguarda formalização).
   Equipe TI com 60% de disponibilidade — conflito com projeto SAP em paralelo.

SCORE DE VALOR: 22/30 (73%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 2 — FILTRO DE COMPLEXIDADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7. Esforço Estimado > 160h           SIM (1)
   Integração SAP + rastreamento em tempo real + alertas + dashboard: estimativa
   mínima de 400h de desenvolvimento, sem contar infraestrutura e testes.

8. Impacto Organizacional Amplo      SIM (1)
   Impacta Supply Chain, TI, e os 12 fornecedores Tier 1 como partes externas.
   Mudança afeta operação de múltiplas áreas simultaneamente.

9. Integração entre Sistemas         SIM (1)
   Integração com SAP MM para importação de pedidos e atualização de status.
   Integração técnica formal confirmada pelo solicitante.

10. Mudança de Processo Relevante    SIM (1)
    Analista de Supply Chain passa a monitorar entregas via dashboard em vez de
    e-mails e telefonemas. Processo de acionamento de fornecedor também muda.

11. Governança Formal Necessária     SIM (1)
    Projeto com múltiplos fornecedores, integração SAP e prazo vinculado a evento
    externo (reunião de fornecedores jul/2026). Governança formal obrigatória.

12. Impacto Regulatório ou Financeiro PARCIAL (0,5)
    Custos de ruptura impactam demonstrativo financeiro (R$135k em Q1/2026).
    Não há risco regulatório direto identificado. Impacto financeiro existe mas
    é mitigação de custo operacional, não obrigação legal.

SCORE DE COMPLEXIDADE: 5,5/6 → ALTA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESULTADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCORE DE VALOR: 22/30 (73%)
COMPLEXIDADE: 5,5/6 → ALTA
MODALIDADE: PROJETO FORMAL
DECISÃO: APROVADO COM CONDIÇÕES

CONDIÇÕES BLOQUEANTES:
1. Designar sponsor executivo com autoridade para aprovar TAP
2. Formalizar orçamento em CAPEX (aprovação financeira)
3. Validar disponibilidade TI sem conflito crítico com projeto SAP

PRÓXIMOS PASSOS:
| Ação | Responsável | Prazo |
|------|-------------|-------|
| Designar sponsor | VP Supply Chain / CIO | 2026-04-14 |
| Formalizar orçamento CAPEX | Ana Ferreira + Financeiro | 2026-04-14 |
| Mapa de conflito de recursos TI | PMO + TI | 2026-04-13 |
| Iniciar elaboração do TAP (após condições) | PMO | 2026-04-17 |
```

---

## Quality Criteria

- [ ] Todos os 6 critérios de valor avaliados com pontuação 1–5 e justificativa ≥ 2 linhas
- [ ] Todos os 6 critérios de complexidade avaliados com SIM/PARCIAL/NÃO e justificativa ≥ 1 linha
- [ ] Score de valor calculado corretamente (soma / 30 × 100)
- [ ] Score de complexidade calculado corretamente (soma dos pontos binários)
- [ ] Modalidade declarada (Projeto Formal / Governança Leve / Tarefa Operacional)
- [ ] Decisão coerente com a matriz valor × complexidade
- [ ] Condições bloqueantes distintas de condições desejáveis
- [ ] Próximos passos com responsável e prazo

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. A decisão não corresponde à matriz valor × complexidade (ex: "APROVADO" com score 45% independente da complexidade)
2. Algum critério de valor avaliado sem justificativa de ao menos 1 linha
3. Algum critério de complexidade avaliado sem justificativa (SIM/NÃO sem explicação não é qualificação)
4. Modalidade ausente ou incoerente com a complexidade calculada
