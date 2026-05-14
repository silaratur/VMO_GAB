---
task: "Pesquisa de Satisfação"
order: 2
input:
  - tap: "TAP com critérios de sucesso e stakeholders"
  - status_atual: "Status do projeto e issues recentes para contextualizar perguntas"
output:
  - pesquisa: "Formulário de pesquisa de satisfação + análise de respostas (quando disponíveis)"
---

# Pesquisa de Satisfação

Cria e/ou processa a pesquisa de satisfação do cliente/solicitante do projeto. Na fase de iniciação, cria o template da pesquisa. Quando respondida, analisa os resultados e gera plano de ação para feedback negativo.

## Process

1. **Definir momento da pesquisa**: Pesquisa de iniciação (validar expectativas), pesquisa de marco (ao final de cada fase) ou pesquisa final (pós-go-live).
2. **Elaborar perguntas**: Combinar pergunta quantitativa (NPS 0-10) com perguntas qualitativas abertas relevantes ao momento do projeto.
3. **Contextualizar para o projeto**: As perguntas devem mencionar aspectos específicos do projeto (não ser genéricas).
4. **Se respostas disponíveis**: Calcular NPS, identificar padrões nos comentários, gerar plano de ação para scores < 7.
5. **Registrar no histórico**: Documentar o resultado da pesquisa para rastreamento de tendência.

## Output Format

```markdown
# PESQUISA DE SATISFAÇÃO — [Nome do Projeto]
Tipo: [Iniciação / Marco N / Final] | Data: YYYY-MM-DD

## Formulário

**Pergunta 1 (NPS)**
Em uma escala de 0 a 10, o quanto você está satisfeito com [aspecto específico do projeto]?
[  ] 0  [  ] 1  [  ] 2  [  ] 3  [  ] 4  [  ] 5  [  ] 6  [  ] 7  [  ] 8  [  ] 9  [  ] 10

**Pergunta 2 (Qualitativa — aberta)**
[pergunta aberta específica sobre aspecto do projeto]

**Pergunta 3 (Qualitativa — aberta)**
[pergunta sobre ponto de melhoria ou expectativa]

---
(Se respostas recebidas:)

## Análise dos Resultados

NPS: [score médio] — Classificação: [Promotor ≥8 / Neutro 6-7 / Detrator ≤5]
Respondentes: [N]

### Pontos Positivos
- [tema recorrente]

### Pontos de Melhoria
- [tema recorrente]

### Plano de Ação
| Score | Feedback | Ação | Responsável | Prazo |
|-------|----------|------|-------------|-------|
```

## Output Example

```markdown
# PESQUISA DE SATISFAÇÃO — SRF
Tipo: Iniciação (validação das expectativas) | Data: 2026-04-16

## Formulário — A ser enviado ao solicitante (Ana Ferreira) e co-sponsor (Carlos Mendes)

**Pergunta 1 (Expectativas)**
Em uma escala de 0 a 10, o quanto as expectativas e objetivos do projeto SRF estão 
claros e alinhados com sua visão? (0 = totalmente diferente do que esperava; 
10 = exatamente o que precisamos)

[  ] 0  [  ] 1  [  ] 2  [  ] 3  [  ] 4  [  ] 5  [  ] 6  [  ] 7  [  ] 8  [  ] 9  [  ] 10

**Pergunta 2 (Documentação)**
Avaliando a documentação de iniciação (TAP, PM Canvas, Cronograma), o que está 
mais bem descrito e o que ainda precisa de maior clareza?

[campo de texto]

**Pergunta 3 (Riscos e Preocupações)**
Existe alguma preocupação ou risco que você acredita que não foi suficientemente 
abordado na documentação de iniciação?

[campo de texto]

**Pergunta 4 (Comunicação)**
Como você prefere receber as atualizações do projeto? Com qual frequência?

[campo de texto]

---
Próxima pesquisa: Marco M3 (Arquitetura aprovada) — 2026-05-31
Pesquisa final: 30 dias após go-live — prevista para 2026-10-31
```

## Quality Criteria

- [ ] Ao menos 1 pergunta quantitativa (NPS 0-10) presente
- [ ] Ao menos 2 perguntas qualitativas abertas e específicas ao projeto
- [ ] Perguntas contextualizadas ao momento do projeto (não genéricas)
- [ ] Próxima pesquisa programada com data
- [ ] Se respostas disponíveis: NPS calculado e plano de ação para scores < 7

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Pesquisa com perguntas genéricas sem referência ao projeto específico
2. Feedback negativo (score < 7) sem plano de ação associado quando respostas estão disponíveis
