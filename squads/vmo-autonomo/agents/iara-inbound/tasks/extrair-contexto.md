---
task: "Extrair Contexto"
order: 2
input:
  - demanda_coletada: "Output da tarefa anterior (coletar-demanda.md) com dados brutos"
output:
  - demanda_normalizada: "Demanda estruturada em formato padronizado pronto para qualificação"
  - resumo_para_solicitante: "Parágrafo de confirmação para enviar ao solicitante"
---

# Extrair Contexto

Consolida e normaliza os dados coletados na tarefa anterior, preenche lacunas de baixo impacto com inferências documentadas, e produz o documento final de demanda estruturada pronto para o processo de qualificação.

## Process

1. **Revisar os dados coletados**: Ler o output de coletar-demanda.md e identificar campos completos, lacunas e inconsistências.
2. **Resolver inconsistências documentadas**: Para cada inconsistência entre fontes, selecionar o dado mais recente ou de maior autoridade e documentar a escolha.
3. **Completar inferências de baixo risco**: Para campos de baixo impacto (área provável, contexto geral), fazer inferência razoável com flag "INFERIDO — confirmar". Nunca inferir campos de alto impacto (sponsor, orçamento, prazo).
4. **Redigir resumo para confirmação**: Escrever um parágrafo claro resumindo a demanda conforme entendida para que o solicitante possa confirmar ou corrigir.
5. **Estruturar saída normalizada**: Produzir o documento final em formato padronizado para o analista de qualificação.

## Output Format

```markdown
# Demanda Estruturada — [Nome do Projeto Preliminar]
Versão: 1.0
Data: YYYY-MM-DD

## Identificação
ID Demanda: DEM-[AAAA]-[NNN]
Data de Entrada: YYYY-MM-DD
Canal: [e-mail / Teams / formulário / reunião]

## Solicitante
- Nome: [nome]
- Cargo: [cargo]
- Área: [área]
- Contato: [e-mail ou ramal]

## Resumo da Demanda
[2-3 frases descrevendo o problema e a solução solicitada em linguagem clara]

## Necessidade de Negócio
[problema real que gerou a demanda]

## Resultado Esperado
[o que o solicitante espera ter ao final]

## Contexto Estratégico
[como isso se conecta aos objetivos da organização, se mencionado]

## Estimativas Preliminares
- Prazo desejado: [data ou período]
- Investimento estimado: [valor ou "não informado"]
- Criticidade: [alta / média / baixa]

## Premissas Capturadas
- [premissa identificada nos materiais]

## Restrições Identificadas
- [restrição identificada nos materiais]

## Lacunas para Resolução
| Campo | Ação Requerida | Responsável | Prazo |
|-------|----------------|-------------|-------|
| [campo] | [perguntar ao solicitante] | [analista] | [data] |

## Resumo para Confirmação pelo Solicitante
> "Entendemos que [resumo da demanda em 3-5 linhas]. Está correto? 
> Precisamos confirmar: [lista das lacunas principais]."
```

## Output Example

```markdown
# Demanda Estruturada — Rastreamento de Fornecedores Tier 1
Versão: 1.0
Data: 2026-04-10

## Identificação
ID Demanda: DEM-2026-047
Data de Entrada: 2026-04-08
Canal: E-mail

## Solicitante
- Nome: Ana Carolina Ferreira
- Cargo: Diretora de Operações
- Área: Supply Chain
- Contato: ana.ferreira@empresa.com.br

## Resumo da Demanda
A área de Supply Chain necessita de visibilidade em tempo real sobre entregas
dos 12 fornecedores Tier 1, para prevenir rupturas de fornecimento. Foram
3 incidentes em Q1/2026 com custo de R$ 135.000. A solução deve integrar
com o SAP atual e emitir alertas automáticos para atrasos.

## Necessidade de Negócio
Ausência de visibilidade em tempo real sobre o status de entrega dos
fornecedores críticos. A empresa só descobre o atraso quando a mercadoria
deveria ter chegado e não chegou — sem janela para ação preventiva.

## Resultado Esperado
Sistema de rastreamento integrado ao SAP com: dashboard em tempo real,
alertas automáticos para atrasos > 2h, e cobertura de 100% dos Tier 1.

## Contexto Estratégico
OKR Q1/2026: "Reduzir falhas de fornecimento em 30%". Este projeto é uma
ação direta para atingir este objetivo. (Fonte: Ata de Reunião Q1 Review)

## Estimativas Preliminares
- Prazo desejado: antes de 01/07/2026 (reunião de avaliação de fornecedores)
- Investimento estimado: não informado — pend. aprovação financeira
- Criticidade: alta

## Premissas Capturadas
- SAP atual possui capacidade de integração (a confirmar com TI)
- Os 12 fornecedores Tier 1 têm dispositivos compatíveis com rastreamento

## Restrições Identificadas
- Não substituir o SAP — integração apenas
- Sistema deve funcionar em tempo real (sem delay > 15 min)

## Lacunas para Resolução
| Campo | Ação Requerida | Responsável | Prazo |
|-------|----------------|-------------|-------|
| Orçamento | Confirmar aprovação CAPEX com Financeiro | Ana Ferreira | 2026-04-12 |
| Sponsor | Definir sponsor executivo | Coordenador PMO | 2026-04-12 |
| Disponibilidade TI | Verificar conflito com projeto SAP | PMO | 2026-04-11 |

## Resumo para Confirmação pelo Solicitante
> "Entendemos que a área de Supply Chain precisa de um sistema de rastreamento
> em tempo real dos fornecedores Tier 1, integrado ao SAP, para prevenir 
> rupturas como as 3 ocorridas em Q1/2026 (custo: R$135k). O prazo desejado
> é antes de julho/2026. Está correto? Ainda precisamos confirmar: orçamento
> disponível, sponsor executivo e disponibilidade da equipe de TI."
```

## Quality Criteria

- [ ] ID único de demanda gerado no formato DEM-AAAA-NNN
- [ ] Necessidade de negócio e resultado esperado são campos distintos e preenchidos
- [ ] Lacunas para resolução têm responsável e prazo definidos
- [ ] Resumo de confirmação é legível por não-técnico e captura a essência da demanda
- [ ] Inferências marcadas explicitamente como "INFERIDO — confirmar"

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. A necessidade de negócio e o resultado esperado são idênticos (a necessidade deve ser o problema; o resultado deve ser a solução)
2. O resumo de confirmação contém informações que não estavam nos materiais coletados (inventar contexto)
