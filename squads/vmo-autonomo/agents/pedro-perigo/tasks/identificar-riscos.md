---
task: "Identificar Riscos"
order: 1
input:
  - tap: "TAP com premissas, restrições e contexto do projeto"
  - cronograma: "Cronograma com caminho crítico e marcos"
  - erf: "Requisitos funcionais e não-funcionais"
output:
  - lista_riscos: "Registro inicial de riscos com categorização e análise qualitativa"
---

# Identificar Riscos

Identifica e classifica os riscos do projeto usando técnicas PMBOK: análise de premissas, análise de listas de verificação por categoria, e brainstorming estruturado baseado no contexto do projeto.

## Process

1. **Analisar premissas e restrições do TAP**: Cada premissa é uma fonte potencial de risco (o que acontece se a premissa for falsa?). Cada restrição é uma limitação que pode gerar risco.
2. **Verificar checklist por categoria de risco**: Para cada categoria (técnico, financeiro, prazo, stakeholders, externo), identificar riscos específicos ao contexto do projeto.
3. **Analisar o caminho crítico**: Atividades no caminho crítico são fontes primárias de riscos de prazo — analisar cada pacote crítico.
4. **Avaliar probabilidade e impacto**: Para cada risco, atribuir probabilidade (1-5) e impacto (1-5) e calcular score de exposição (P × I).
5. **Priorizar por score de exposição**: Ordenar riscos do maior para o menor score; classificar como CRÍTICO (>= 16), ALTO (9-15), MÉDIO (4-8), BAIXO (1-3).

## Output Format

```markdown
# REGISTRO DE RISCOS — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD

## Registro de Riscos

| ID | Categoria | Descrição do Risco | Prob (1-5) | Impacto (1-5) | Score | Nível |
|----|-----------|-------------------|------------|---------------|-------|-------|
| R-001 | [categoria] | [descrição como evento futuro] | [P] | [I] | [P×I] | [nível] |

## Análise por Categoria
### Riscos Técnicos
[detalhamento dos riscos técnicos]

### Riscos de Prazo
[detalhamento dos riscos de prazo]

### Riscos Financeiros
[detalhamento dos riscos financeiros]

### Riscos de Stakeholders
[detalhamento dos riscos de stakeholders]
```

## Output Example

```markdown
# REGISTRO DE RISCOS — SRF
Versão: 1.0 | Data: 2026-04-16

## Registro de Riscos

| ID | Categoria | Descrição do Risco | Prob | Impacto | Score | Nível |
|----|-----------|-------------------|------|---------|-------|-------|
| R-001 | Prazo/Recursos | A atualização do SAP em andamento pode atrair os mesmos recursos do projeto SRF, reduzindo disponibilidade do time de TI abaixo de 30% | 4 | 5 | 20 | CRÍTICO |
| R-002 | Técnico | A API do SAP MM pode não suportar os requisitos de integração sem desenvolvimento customizado adicional além do estimado | 3 | 4 | 12 | ALTO |
| R-003 | Stakeholders | Os 12 fornecedores Tier 1 podem resistir à adoção do sistema de rastreamento por preocupações com privacidade ou custo de dispositivos | 3 | 3 | 9 | ALTO |
| R-004 | Financeiro | Custos de infraestrutura cloud podem exceder a estimativa em caso de volume de dados maior que o projetado | 2 | 3 | 6 | MÉDIO |
| R-005 | Técnico | Requisitos de segurança (LGPD) podem exigir certificações adicionais não planejadas | 2 | 4 | 8 | MÉDIO |
| R-006 | Prazo | Atrasos na aprovação da ERF pelo solicitante podem atrasar o início da fase de desenvolvimento | 3 | 3 | 9 | ALTO |
| R-007 | Externo | Mudanças regulatórias na área de rastreamento de dados de localização durante o projeto | 1 | 4 | 4 | MÉDIO |

## Análise por Categoria

### Riscos CRÍTICOS e ALTOS — Detalhe
R-001 (CRÍTICO): O projeto SAP em andamento compete pelos mesmos recursos de TI.
  Premissa violada: "Equipe TI disponível 60% no Q2/2026"
  Sinal de materialização: Disponibilidade TI cai < 40% em qualquer semana do caminho crítico
  
R-002 (ALTO): POC realizada na Fase 1 reduzirá esta incerteza — risco reavaliado após M3.
  Sinal de materialização: POC requer > 5 dias adicionais além do estimado de 8 dias
  
R-003 (ALTO): Depende da abordagem de onboarding. Fornecedores sem smartphone precisarão de dispositivo IoT a custo do projeto.
  Sinal de materialização: Mais de 2 fornecedores recusam participação após comunicação inicial
```

## Quality Criteria

- [ ] Mínimo 5 riscos identificados e documentados
- [ ] Todos os riscos com probabilidade E impacto avaliados (escala 1-5)
- [ ] Score de exposição calculado (P × I) para todos os riscos
- [ ] Riscos cobrem ao menos 4 categorias distintas
- [ ] Riscos CRÍTICOS e ALTOS têm sinal de materialização documentado

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Menos de 5 riscos identificados em qualquer projeto
2. Algum risco descrito como problema presente, não como evento futuro incerto
