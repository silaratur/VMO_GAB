---
task: "Coletar Demanda"
order: 1
input:
  - materiais_fornecidos: "Arquivos, e-mails, atas de reunião, formulários ou mensagens fornecidos pelo usuário"
  - canal_entrada: "Descrição do canal de origem (e-mail, Teams, formulário, reunião)"
output:
  - demanda_estruturada: "Dados da demanda organizados em campos padronizados"
  - lacunas_identificadas: "Lista de campos sem informação com ação requerida"
  - fonte_por_campo: "Rastreabilidade de origem para cada informação coletada"
---

# Coletar Demanda

Lê todos os materiais fornecidos pelo usuário (e-mails, documentos, atas, mensagens) e extrai as informações da demanda em um formato estruturado e rastreável. É o primeiro passo do pipeline — a qualidade desta coleta determina a de todos os documentos subsequentes.

## Process

1. **Inventariar os materiais fornecidos**: Listar todos os arquivos, e-mails e mensagens disponíveis com data e tipo de cada fonte.
2. **Ler e extrair dados por campo**: Para cada campo obrigatório (solicitante, necessidade, benefício, urgência, prazo, orçamento estimado, stakeholders), localizar e extrair a informação nos materiais.
3. **Registrar a fonte de cada informação**: Para cada dado extraído, anotar de qual documento ou conversa ele veio (ex: "E-mail Ana Ferreira, 2026-04-08").
4. **Identificar lacunas**: Campos sem informação disponível são marcados como "[NÃO INFORMADO — requer esclarecimento]" com sugestão de pergunta ao solicitante.
5. **Verificar consistências**: Se o mesmo campo aparece com valores diferentes em fontes distintas, registrar ambos como inconsistência para resolução.

## Output Format

```markdown
# Demanda Coletada
Data da Coleta: YYYY-MM-DD
Coletado por: Iara Inbound

## Fontes Consultadas
| # | Tipo | Descrição | Data |
|---|------|-----------|------|
| 1 | E-mail | ... | YYYY-MM-DD |

## Dados da Demanda

**Solicitante**
- Nome: [nome ou NÃO INFORMADO]
- Cargo: [cargo ou NÃO INFORMADO]
- Área: [área ou NÃO INFORMADO]
- Fonte: [referência à fonte]

**Necessidade de Negócio**
[descrição do problema real, não da solução]
Fonte: [referência]

**Pedido Específico**
[o que foi solicitado concretamente]
Fonte: [referência]

**Benefício Esperado**
[benefício descrito ou estimado]
Fonte: [referência]

**Urgência e Prazo**
- Prazo desejado: [data ou NÃO INFORMADO]
- Urgência declarada: [alta/média/baixa ou NÃO INFORMADO]
- Origem do prazo: [por que essa data? ou NÃO INFORMADO]
Fonte: [referência]

**Contexto Organizacional**
- Área executora provável: [área ou NÃO INFORMADO]
- Projetos relacionados: [projetos ou NÃO INFORMADO]
- Restrições conhecidas: [restrições ou NÃO INFORMADO]
Fonte: [referência]

## Lacunas Identificadas
| Campo | Status | Pergunta para Esclarecimento |
|-------|--------|------------------------------|
| [campo] | NÃO INFORMADO | [pergunta específica] |
```

## Output Example

```markdown
# Demanda Coletada
Data da Coleta: 2026-04-10
Coletado por: Iara Inbound

## Fontes Consultadas
| # | Tipo | Descrição | Data |
|---|------|-----------|------|
| 1 | E-mail | Ana Ferreira → PMO, assunto "Solicitação de projeto rastreamento" | 2026-04-08 |
| 2 | Ata de Reunião | Reunião Supply Chain Q1 Review | 2026-04-05 |

## Dados da Demanda

**Solicitante**
- Nome: Ana Carolina Ferreira
- Cargo: Diretora de Operações
- Área: Supply Chain
- Fonte: E-mail #1

**Necessidade de Negócio**
Falta de visibilidade em tempo real sobre o status de entrega dos fornecedores Tier 1
resultou em 3 rupturas de fornecimento no Q1/2026. A área não sabe quando um
atraso está ocorrendo até que a mercadoria deveria ter chegado e não chegou.
Fonte: E-mail #1 + Ata de Reunião #2

**Pedido Específico**
Implementar sistema de rastreamento em tempo real integrado ao SAP, com
alertas automáticos para atrasos e dashboard de acompanhamento.
Fonte: E-mail #1

**Benefício Esperado**
Redução de incidentes de ruptura. Custo dos incidentes de Q1: R$ 135.000.
Benefício estimado pela solicitante: "pelo menos metade desse valor em economia".
Fonte: E-mail #1

**Urgência e Prazo**
- Prazo desejado: "antes do segundo semestre" (= antes de 01/07/2026)
- Urgência declarada: alta
- Origem do prazo: Próxima reunião de avaliação de fornecedores é em julho
Fonte: E-mail #1

**Contexto Organizacional**
- Área executora provável: TI — Sistemas Corporativos
- Projetos relacionados: Atualização do SAP em andamento (fonte: Ata #2)
- Restrições conhecidas: Sistema deve integrar com SAP atual sem substituí-lo
Fonte: E-mail #1, Ata #2

## Lacunas Identificadas
| Campo | Status | Pergunta para Esclarecimento |
|-------|--------|------------------------------|
| Orçamento disponível | NÃO INFORMADO | Há orçamento aprovado ou precisa passar por aprovação? |
| Sponsor formal | NÃO INFORMADO | Quem seria o sponsor executivo do projeto? |
| Equipe executora disponível | NÃO INFORMADO | TI tem disponibilidade? Há conflito com o projeto SAP? |
```

## Quality Criteria

- [ ] Todas as fontes consultadas listadas com data e tipo
- [ ] Cada campo tem referência à fonte de origem
- [ ] Lacunas documentadas explicitamente com pergunta de esclarecimento
- [ ] Necessidade de negócio distinguida do pedido técnico
- [ ] Inconsistências entre fontes sinalizadas com flag

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. O campo "Necessidade de Negócio" está vazio ou apenas repete o pedido técnico sem explicar o problema subjacente
2. Nenhum campo tem rastreabilidade de fonte documentada
