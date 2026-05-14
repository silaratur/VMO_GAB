---
task: "Criar Termo de Abertura do Projeto (TAP)"
order: 1
input:
  - qualificacao_aprovada: "Qualificação aprovada com dados de sponsor, orçamento e escopo"
  - analise_comercial: "Análise de ROI e proposta de valor do Felipe Filtro"
output:
  - tap: "Termo de Abertura do Projeto completo e estruturado"
---

# Criar Termo de Abertura do Projeto (TAP)

Gera o Termo de Abertura do Projeto (Project Charter) formal conforme padrão PMBOK 7ª edição, transformando a demanda qualificada em documento executivo que autoriza formalmente o projeto e designa autoridade ao gerente de projetos.

## Process

1. **Extrair dados-base**: Ler qualificação aprovada e extrair: nome do projeto, sponsor, objetivos preliminares, escopo indicado, partes interessadas, orçamento aprovado e prazo.
2. **Reformular objetivo como SMART**: Transformar o objetivo da demanda em declaração SMART — específica, mensurável, atingível, relevante e temporal.
3. **Delimitar escopo**: Criar listas explícitas de "dentro do escopo" e "fora do escopo" baseadas nas informações disponíveis.
4. **Definir critérios de sucesso**: Derivar mínimo 3 critérios mensuráveis dos objetivos e benefícios esperados.
5. **Estruturar o TAP completo**: Preencher todas as seções do template com os dados extraídos e as formulações elaboradas.

## Output Format

```markdown
TERMO DE ABERTURA DO PROJETO
Versão: 1.0 | Data: YYYY-MM-DD | Status: RASCUNHO

IDENTIFICAÇÃO
  Nome: [nome do projeto]
  ID: PROJ-[AAAA]-[NNN]
  Área Solicitante: [área]
  Área Executora: [área]

AUTORIZAÇÃO
  Sponsor: [nome] — [cargo]
  Co-Sponsor: [nome] — [cargo] (se aplicável)
  Gerente de Projeto: [nome ou "A designar"]
  Autoridade do GP: [limites de aprovação]

OBJETIVO DO PROJETO (SMART)
  [objetivo específico, mensurável, com prazo]

JUSTIFICATIVA
  [problema endereçado e conexão com estratégia organizacional]

ESCOPO
  DENTRO DO ESCOPO:
    - [item 1]
  FORA DO ESCOPO:
    - [item 1]

CRITÉRIOS DE SUCESSO
  1. [critério mensurável com métrica e prazo]
  2. [critério mensurável com métrica e prazo]
  3. [critério mensurável com métrica e prazo]

PREMISSAS
  - [premissa 1]
  - [premissa 2]
  - [premissa 3]

RESTRIÇÕES
  - [restrição 1]
  - [restrição 2]
  - [restrição 3]

RISCOS DE ALTO NÍVEL
  1. [risco] — Classificação: [ALTO/MÉDIO/BAIXO]
  2. [risco] — Classificação: [...]

PARTES INTERESSADAS PRINCIPAIS
  | Nome/Área | Papel | Interesse |
  |-----------|-------|-----------|

ORÇAMENTO RESUMIDO
  [Item]: R$ [valor]
  Contingência (20%): R$ [valor]
  TOTAL APROVADO: R$ [valor]

CRONOGRAMA SUMARIZADO
  Início: YYYY-MM-DD
  [Fase 1]: YYYY-MM-DD a YYYY-MM-DD
  Conclusão: YYYY-MM-DD

APROVAÇÃO
  Sponsor: _________________ Data: _______
  PMO: _____________________ Data: _______
```

## Output Example

> Ver `pipeline/data/output-examples.md` — Exemplo 2 (TAP completo para projeto SRF).

## Quality Criteria

- [ ] Objetivo escrito em formato SMART com métrica e prazo
- [ ] Sponsor identificado com nome, cargo e limites de autoridade
- [ ] Escopo tem listas "dentro" e "fora" com mínimo 3 itens cada
- [ ] Mínimo 3 critérios de sucesso mensuráveis
- [ ] Mínimo 3 premissas e 3 restrições
- [ ] Mínimo 3 riscos de alto nível identificados
- [ ] Orçamento com contingência explícita de 20%
- [ ] Seção de aprovação com campos de assinatura

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. O objetivo não contém métrica mensurável E prazo de conclusão (dois requisitos mínimos do SMART)
2. O sponsor está "A definir" — o TAP não pode ser finalizado sem sponsor designado
