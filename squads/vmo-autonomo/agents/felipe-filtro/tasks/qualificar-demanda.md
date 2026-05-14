---
task: "Qualificar Demanda"
order: 1
input:
  - demanda_estruturada: "Output do checkpoint de validação (demanda-validada.md)"
  - documentos_estrategicos: "OKRs ou objetivos organizacionais disponíveis"
output:
  - analise_qualificacao: "Avaliação dos 6 critérios com pontuação e justificativa"
  - decisao: "APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA"
  - proximos_passos: "Ações requeridas com responsável e prazo"
---

# Qualificar Demanda

Avalia se a demanda recebida deve ser transformada em projeto formal, aplicando os 6 critérios de qualificação do VMO com pontuação justificada. Emite um parecer fundamentado que habilita a decisão do GP ou do PMO.

## Process

1. **Carregar contexto estratégico**: Ler documentos de OKRs e objetivos organizacionais disponíveis para avaliar alinhamento.
2. **Avaliar os 6 critérios**: Para cada critério, atribuir pontuação de 1 a 5 com justificativa de ao menos 2 linhas baseada em dados da demanda.
3. **Calcular pontuação total**: Somar os 6 critérios (máximo 30) e calcular percentual.
4. **Emitir decisão**: ≥ 70% = APROVADO; 50-69% com condições resolvíveis = APROVADO COM CONDIÇÕES; < 50% = REPROVADO; informação insuficiente = EM ESPERA.
5. **Definir próximos passos**: Para aprovação, listar ações de iniciação. Para condições, listar o que deve ser resolvido. Para reprovação, documentar motivo.

## Output Format

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: [DEM-AAAA-NNN]
Data: YYYY-MM-DD

CRITÉRIOS DE QUALIFICAÇÃO

1. Alinhamento Estratégico    [N/5]
   [justificativa — qual OKR/objetivo endereça, com confiança]

2. Viabilidade Técnica        [N/5]
   [justificativa — recursos, tecnologia, complexidade]

3. Retorno sobre Investimento [N/5]
   [benefício estimado, custo estimado, payback em meses]

4. Urgência                   [N/5]
   [impacto de não fazer, pressão temporal]

5. Maturidade da Demanda      [N/5]
   [clareza do problema, completude das informações]

6. Disponibilidade de Recursos [N/5]
   [equipe, orçamento, conflitos de portfólio]

PONTUAÇÃO: [total]/30 ([%]%)
DECISÃO: [APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA]

CONDIÇÕES BLOQUEANTES (se aplicável):
- [condição que deve ser resolvida antes de prosseguir]

PRÓXIMOS PASSOS:
| Ação | Responsável | Prazo |
|------|-------------|-------|
```

## Output Example

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-047
Data: 2026-04-11

CRITÉRIOS DE QUALIFICAÇÃO

1. Alinhamento Estratégico    4/5
   OKR Q1/2026: "Reduzir falhas de fornecimento em 30%" — endereçamento direto.
   Confiança: ALTA (OKR documentado, ata de reunião confirma pressão do board).

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

PONTUAÇÃO: 22/30 (73%)
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

## Quality Criteria

- [ ] Todos os 6 critérios avaliados com pontuação e justificativa
- [ ] ROI com valores estimados e prazo de payback
- [ ] Decisão emitida e coerente com a pontuação
- [ ] Condições bloqueantes distintas de condições desejáveis
- [ ] Próximos passos com responsável e prazo

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. A decisão não corresponde à pontuação calculada (ex: "APROVADO" com 45%)
2. Algum critério foi avaliado sem justificativa de ao menos 1 linha
