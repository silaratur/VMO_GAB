---
task: "Análise Comercial"
order: 2
input:
  - qualificacao_basica: "Output da tarefa anterior com score de valor, score de complexidade, modalidade e decisão"
  - dados_financeiros: "Qualquer informação de custo ou benefício disponível"
output:
  - analise_roi: "Análise de retorno sobre investimento detalhada"
  - proposta_valor: "Declaração de valor do projeto para a organização"
---

# Análise Comercial

Aprofunda a análise de retorno sobre investimento e cria a declaração de valor do projeto que será incorporada ao Termo de Abertura. Complementa o critério de ROI avaliado na qualificação com uma análise financeira mais detalhada.

## Process

1. **Identificar benefícios quantificáveis**: Listar todos os benefícios mencionados ou inferíveis da demanda com estimativa de valor (anual ou total).
2. **Estimar custos do projeto**: Decompor em: desenvolvimento/implantação, infraestrutura, licenças, treinamento e reserva de contingência (20%).
3. **Calcular métricas de ROI**: Payback, ROI percentual em 12 e 24 meses, e NPV se dados suficientes estiverem disponíveis.
4. **Avaliar custos de não-fazer**: Qual é o impacto financeiro ou estratégico de NÃO realizar o projeto?
5. **Redigir proposta de valor**: Declaração executiva de 3-5 linhas conectando investimento a resultado estratégico.

## Output Format

```markdown
ANÁLISE COMERCIAL — [Nome da Demanda]
Data: YYYY-MM-DD

BENEFÍCIOS ESPERADOS
| Benefício | Valor Estimado | Prazo | Confiança |
|-----------|----------------|-------|-----------|
| [benefício] | R$ [valor]/ano | [meses] | [H/M/B] |
Total de benefícios anuais estimados: R$ [total]

CUSTO DO PROJETO
| Item | Estimativa |
|------|------------|
| Desenvolvimento/Implantação | R$ [valor] |
| Infraestrutura (12 meses) | R$ [valor] |
| Licenças | R$ [valor] |
| Treinamento | R$ [valor] |
| Contingência (20%) | R$ [valor] |
TOTAL: R$ [total]

MÉTRICAS DE RETORNO
- Payback: [N] meses
- ROI em 12 meses: [%]
- ROI em 24 meses: [%]
- Nível de confiança geral: [ALTA/MÉDIA/BAIXA]

CUSTO DE NÃO-FAZER
[O que acontece financeira e estrategicamente se não fizermos nada?]

PROPOSTA DE VALOR
"[Declaração executiva de 3-5 linhas: o projeto X, com investimento de R$Y,
entregará Z, reduzindo W e alinhado ao objetivo estratégico A.]"
```

## Output Example

```markdown
ANÁLISE COMERCIAL — Rastreamento de Fornecedores Tier 1
Data: 2026-04-11

BENEFÍCIOS ESPERADOS
| Benefício | Valor Estimado | Prazo | Confiança |
|-----------|----------------|-------|-----------|
| Redução de rupturas de fornecimento (-40%) | R$ 108.000/ano | 6 meses | MÉDIA |
| Eliminação de multas contratuais por ruptura | R$ 45.000/ano | 6 meses | ALTA |
| Redução de horas manuais de monitoramento | R$ 24.000/ano | 3 meses | ALTA |
| Melhoria de satisfação de cliente interno (NPS) | Não quantificado | - | - |
Total de benefícios anuais estimados: R$ 177.000

CUSTO DO PROJETO
| Item | Estimativa |
|------|------------|
| Desenvolvimento e configuração | R$ 180.000 |
| Infraestrutura cloud (12 meses) | R$ 45.000 |
| Licenças de rastreamento | R$ 35.000 |
| Treinamento e change management | R$ 20.000 |
| Contingência (20%) | R$ 56.000 |
TOTAL: R$ 336.000

MÉTRICAS DE RETORNO
- Payback: aproximadamente 23 meses (contando contingência)
- ROI em 12 meses: -53% (ainda em fase de amortização)
- ROI em 24 meses: +6% (break-even ultrapassado)
- Nível de confiança geral: MÉDIA (benefícios de ruptura baseados em Q1/2026)
Nota: Sem contingência, payback seria ~19 meses.

CUSTO DE NÃO-FAZER
Manutenção do custo de rupturas: R$ 135.000+/trimestre (tendência histórica).
Risco de penalidades contratuais acumuladas: R$ 45.000–180.000/ano.
Perda de competitividade no SLA com clientes finais.

PROPOSTA DE VALOR
"O projeto SRF, com investimento de R$ 336.000, entregará visibilidade em tempo
real sobre os fornecedores Tier 1, prevenindo as rupturas de fornecimento que
custaram R$ 135.000 apenas no Q1/2026. Com payback de aproximadamente 23 meses
e alinhamento direto ao OKR de redução de falhas de fornecimento, o projeto
transforma um custo reativo em capacidade preventiva estratégica."
```

## Quality Criteria

- [ ] Benefícios listados com valor estimado e nível de confiança
- [ ] Custo do projeto decomposto em ao menos 4 categorias
- [ ] Contingência de 20% incluída
- [ ] Payback calculado em meses
- [ ] Custo de não-fazer documentado
- [ ] Proposta de valor em 3-5 linhas conecta investimento a resultado estratégico

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Payback calculado sem incluir a reserva de contingência no custo total
2. A proposta de valor não menciona o valor financeiro do investimento e o benefício principal
