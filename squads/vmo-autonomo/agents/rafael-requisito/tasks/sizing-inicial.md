---
task: "Sizing Inicial de Escopo"
order: 0
input:
  - demanda_validada: "projects/{project}/01-qualificacao/demanda-validada.md"
  - demanda_coletada: "projects/{project}/01-qualificacao/demanda-coletada.md"
output:
  - sizing: "projects/{project}/01-qualificacao/sizing.md"
---

# Sizing Inicial de Escopo

Leve levantamento de escopo realizado ANTES da qualificação formal do Felipe Filtro.
O objetivo é fornecer ao Felipe uma estimativa fundamentada de esforço (critério 7) —
não inventada por benchmark, mas derivada da análise do escopo declarado na demanda.

Este NÃO é a ERF completa. É uma estimativa de pré-qualificação: rápida, baseada
no que está disponível, com confiança declarada e lacunas documentadas.

---

## Process

1. **Ler e mapear o escopo da demanda**: Identificar o que precisa ser feito (funcionalidades,
   integrações, configurações) a partir da demanda coletada e validada.
   Separar: o que está claro vs. o que está implícito ou incerto.

2. **Estimar esforço por fase** com base no escopo mapeado:
   - Levantamento de requisitos detalhado
   - Desenvolvimento / configuração / integração
   - Testes (unitário, integrado, UAT)
   - Go-live e suporte inicial
   Para cada fase: declarar o esforço estimado E o nível de confiança (ALTA/MÉDIA/BAIXA).
   Confiança ALTA = escopo claro e precedente técnico disponível.
   Confiança BAIXA = escopo incerto ou tecnologia não mapeada.

3. **Classificar o esforço total**:
   - < 80h → Melhoria Corretiva ou Evolutiva simples
   - 80–160h → Melhoria Evolutiva complexa (pode ser projeto dependendo de outros critérios)
   - > 160h → Projeto formal (exige pipeline VMO completo)

4. **Identificar fatores de risco de esforço**: Elementos do escopo que podem aumentar
   significativamente o esforço se confirmados (ex: integrações adicionais, restrições técnicas,
   múltiplos ambientes, necessidade de customização vs. configuração padrão).

5. **Listar lacunas de escopo**: O que ainda não está claro e que, se confirmado como necessário,
   mudaria a classificação de esforço. Máximo 5 perguntas objetivas.

---

## Regras de Estimativa

- **Nunca estimar por benchmark de mercado sem base no escopo específico**: "Integrações SAP
  costumam levar X horas" não é estimativa — é chute. A estimativa parte do que a demanda
  declara, não do que o mercado costuma fazer.
- **Confiança BAIXA não é falta de rigor — é honestidade**: Quando o escopo está incerto,
  declarar confiança BAIXA com a faixa de variação é mais útil que uma estimativa pontual falsa.
- **Usar faixas em vez de pontos quando necessário**: "80–140h, confiança BAIXA" é superior
  a "110h" quando o escopo não está definido.
- **Precedente técnico na mesma iniciativa = evidência válida para confiança mais alta**: Se
  existe uma solução similar já entregue no mesmo contexto, isso melhora a confiança da estimativa
  — mas deve-se documentar o que mudou entre o precedente e a demanda atual.

---

## Output Format

```markdown
# Sizing Inicial de Escopo
Projeto: {project}
Data: YYYY-MM-DD
Analista: Rafael Requisito
Fase: Pré-qualificação (subsidia critério 7 do Felipe Filtro)

## Escopo Preliminar Identificado
| # | Componente | Tipo | Clareza do Escopo |
|---|-----------|------|-------------------|
| 1 | [funcionalidade/integração] | [configuração / desenvolvimento / integração] | [claro / incerto / a confirmar] |

## Estimativa de Esforço por Fase
| Fase | Atividades | Estimativa | Confiança | Premissas |
|------|-----------|------------|-----------|-----------|
| Levantamento de requisitos | Elicitação com solicitante e TI | Xh | ALTA/MÉDIA/BAIXA | [premissas assumidas] |
| Desenvolvimento/Configuração | [o que será desenvolvido] | Xh | ALTA/MÉDIA/BAIXA | [premissas] |
| Testes e homologação | [testes previstos] | Xh | ALTA/MÉDIA/BAIXA | [premissas] |
| Go-live e suporte inicial | Deploy, treinamento, cutover | Xh | ALTA/MÉDIA/BAIXA | [premissas] |
| **TOTAL** | | **Xh–Yh** | **MÉDIA/BAIXA** | |

## Classificação de Esforço
**[ ] < 80h** / **[ ] 80–160h** / **[X] > 160h** → [classificação resultante]

## Fatores de Risco que Afetam o Esforço
| Fator | Impacto se confirmado | Probabilidade |
|-------|----------------------|---------------|
| [fator de risco] | +Xh | ALTA/MÉDIA/BAIXA |

## Lacunas de Escopo (para ERF futura)
| # | Lacuna | Por que afeta o esforço |
|---|--------|------------------------|
| 1 | [pergunta de escopo] | [como muda a estimativa] |

## Nota para Felipe Filtro
[Resumo executivo de 3-4 linhas: classificação de esforço, principais premissas e o
que pode mudar a estimativa — para Felipe usar diretamente na avaliação do critério 7]
```

---

## Quality Criteria

- [ ] Cada componente de escopo identificado e classificado (configuração/desenvolvimento/integração)
- [ ] Esforço estimado por fase (não apenas total) com confiança declarada
- [ ] Classificação de esforço (<80h / 80-160h / >160h) explicitamente declarada
- [ ] Fatores de risco documentados com impacto em horas
- [ ] Lacunas de escopo listadas com perguntas objetivas (máximo 5)
- [ ] Nota para Felipe Filtro presente (resumo executivo)

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Esforço dado como número único sem fases (ex: "200h" sem divisão)
2. Confiança não declarada para ao menos uma fase
3. Classificação de esforço ausente (<80h / 80-160h / >160h)
4. Estimativa baseada em benchmark de mercado sem análise do escopo da demanda
5. "Nota para Felipe Filtro" ausente
