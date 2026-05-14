---
task: "Criar Plano Geral do Projeto"
order: 3
input:
  - tap: "TAP aprovado"
  - pm_canvas: "PM Canvas criado"
output:
  - plano_geral: "Plano Geral do Projeto com os 10 planos subsidiários"
---

# Criar Plano Geral do Projeto

Cria o Plano Geral do Projeto (Project Management Plan) que integra os 10 planos subsidiários PMBOK. Para projetos de iniciação, os planos são documentados em nível de abordagem e diretrizes — o detalhamento ocorre durante o planejamento detalhado da execução.

## Process

1. **Ler TAP e PM Canvas**: Extrair metodologia, restrições, recursos e abordagem geral.
2. **Definir abordagem para cada um dos 10 planos**: Para cada plano subsidiário, documentar a abordagem que será usada (metodologia, ferramentas, responsável, frequência).
3. **Estabelecer critérios de sucesso do gerenciamento**: Como cada dimensão será medida e o que significa "bem gerenciada".
4. **Documentar o ciclo de vida do projeto**: Fases, marcos de aprovação (gates) e critérios de progressão entre fases.
5. **Definir abordagem de comunicação e mudanças**: Frequência de reports, canal, audiência e processo de gestão de mudanças.

## Output Format

```markdown
# PLANO GERAL DO PROJETO — [Nome]
Versão: 1.0 | Data: YYYY-MM-DD

## 1. Plano de Gerenciamento do Escopo
Abordagem: [como o escopo será definido, validado e controlado]
Ferramenta: [WBS + dicionário da WBS]
Responsável: [GP]
Processo de mudança de escopo: [como solicitar e aprovar mudanças]

## 2. Plano de Gerenciamento do Cronograma
Abordagem: [metodologia de planejamento e controle de prazo]
Ferramenta: [Cronograma Markdown / MS Project / etc.]
Frequência de atualização: [semanal / quinzenal]
Indicador: SPI (alerta se < 0,85)

## 3. Plano de Gerenciamento dos Custos
Abordagem: [EVM — monitoramento por Earned Value]
Ferramenta: [Planilha EVM / SAP]
Frequência de atualização: [mensal]
Indicador: CPI (alerta se < 0,85)

## 4. Plano de Gerenciamento da Qualidade
Abordagem: [como a qualidade será planejada, garantida e controlada]
Critérios de qualidade do produto: [derivados dos critérios de sucesso do TAP]
Processo de revisão: [revisão por pares / UAT]

## 5. Plano de Gerenciamento dos Recursos
Abordagem: [como recursos humanos e físicos serão planejados]
Papéis e responsabilidades: [RACI — a detalhar na fase de planejamento]
Resolução de conflitos de recursos: [processo de escalada para sponsor]

## 6. Plano de Gerenciamento das Comunicações
| Comunicação | Audiência | Frequência | Canal | Responsável |
|-------------|-----------|------------|-------|-------------|
| Status Report | Sponsor + Stakeholders | Quinzenal | E-mail | GP |
| Reunião de acompanhamento | Time do projeto | Semanal | Teams | GP |
| Relatório executivo | Board / Diretoria | Mensal | Documento | GP |

## 7. Plano de Gerenciamento dos Riscos
Abordagem: [identificação, análise qualitativa, plano de resposta]
Frequência de revisão: [a cada status report (quinzenal)]
Ferramenta: [Registro de Riscos em Markdown]
Alerta automático: [risco nível ALTO → notificação imediata ao sponsor]

## 8. Plano de Gerenciamento das Aquisições
Abordagem: [make or buy — o que será desenvolvido internamente vs. contratado]
Itens a contratar: [lista de itens que requerem aquisição]
Processo de aprovação: [valores acima de R$ X requerem aprovação de [cargo]]

## 9. Plano de Gerenciamento dos Stakeholders
Abordagem: [como partes interessadas serão identificadas, engajadas e monitoradas]
Ferramenta: [Registro de Stakeholders + Mapa de Influência/Interesse]
Frequência de revisão: [mensal]

## 10. Plano de Gerenciamento das Mudanças
Processo de solicitação de mudança:
  1. Solicitante preenche formulário de mudança
  2. GP avalia impacto em escopo, prazo, custo e qualidade
  3. Sponsor aprova mudanças com impacto > [limite definido]
  4. Baseline atualizado após aprovação

## Ciclo de Vida e Gates
| Gate | Critério de Progressão | Aprovador |
|------|----------------------|-----------|
| G1 — Iniciação aprovada | TAP assinado + orçamento aprovado | Sponsor |
| G2 — Planejamento completo | Todos os planos subsidiários aprovados | GP + Sponsor |
| G3 — Desenvolvimento completo | Todos os requisitos Must Have implementados | GP |
| G4 — Go-live autorizado | UAT aprovado + treinamento concluído | Sponsor |
| G5 — Encerramento | Lições aprendidas documentadas + aceite formal | Sponsor |
```

## Output Example

> Adaptar o template acima para o projeto específico com as informações do TAP e PM Canvas já criados nesta execução.

## Quality Criteria

- [ ] Todos os 10 planos subsidiários endereçados
- [ ] Plano de comunicações tem tabela com audiência, frequência e canal
- [ ] Plano de riscos define frequência de revisão
- [ ] Plano de mudanças tem processo com aprovador definido
- [ ] Gates de aprovação definidos com critérios e aprovadores

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Menos de 10 planos subsidiários endereçados no documento
2. O plano de comunicações não tem frequência e canal definidos para ao menos o status report ao sponsor
