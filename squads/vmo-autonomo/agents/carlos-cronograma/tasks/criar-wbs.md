---
task: "Criar WBS (Estrutura Analítica do Projeto)"
order: 1
input:
  - tap: "TAP com escopo e fases"
  - erf: "Especificação de requisitos para decomposição técnica"
output:
  - wbs: "WBS com pelo menos 3 níveis de decomposição"
---

# Criar WBS

Cria a Estrutura Analítica do Projeto (EAP/WBS) decompondo o escopo aprovado no TAP em pacotes de trabalho gerenciáveis, com no mínimo 3 níveis hierárquicos e cobertura de 100% dos entregáveis.

## Process

1. **Identificar as fases do projeto**: A partir do TAP e do ciclo de vida definido, identificar as fases principais (nível 1 da WBS).
2. **Decompor cada fase em entregáveis**: Para cada fase, identificar os entregáveis concretos (nível 2).
3. **Decompor entregáveis em pacotes de trabalho**: Subdividir cada entregável em pacotes com duração ≤ 2 semanas (nível 3).
4. **Verificar cobertura de 100%**: Confirmar que todos os itens "dentro do escopo" do TAP aparecem na WBS.
5. **Numerar hierarquicamente**: Usar numeração tipo 1.0, 1.1, 1.1.1 para todos os elementos.

## Output Format

```markdown
# WBS — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD

## Estrutura Hierárquica

1.0 [Nome do Projeto]
  1.1 Gerenciamento do Projeto
    1.1.1 Elaboração do TAP e documentação de iniciação
    1.1.2 Reports e comunicações periódicas
    1.1.3 Encerramento e lições aprendidas
  1.2 [Fase 1]
    1.2.1 [Entregável 1.1]
      1.2.1.1 [Pacote de trabalho ≤ 2 semanas]
  ...

## Dicionário da WBS (resumido)
| ID | Entregável | Descrição | Critério de Conclusão |
|----|------------|-----------|----------------------|
| 1.2.1.1 | [nome] | [descrição] | [o que significa "feito"] |
```

## Output Example

```markdown
# WBS — Sistema de Rastreamento de Fornecedores (SRF)
Versão: 1.0 | Data: 2026-04-15

1.0 Projeto SRF
  1.1 Gerenciamento do Projeto
    1.1.1 Documentação de iniciação (TAP, ERF, Plano Geral)
    1.1.2 Status reports quinzenais
    1.1.3 Gestão de riscos e issues
    1.1.4 Encerramento e lições aprendidas

  1.2 Fase 1 — Requisitos e Arquitetura
    1.2.1 Especificação de Requisitos Funcionais
      1.2.1.1 Workshop de requisitos com Supply Chain
      1.2.1.2 Especificação técnica da integração SAP
      1.2.1.3 Revisão e aprovação da ERF
    1.2.2 Arquitetura da Solução
      1.2.2.1 Design da arquitetura cloud
      1.2.2.2 POC de integração API SAP MM
      1.2.2.3 Aprovação da arquitetura pelo Sponsor

  1.3 Fase 2 — Desenvolvimento
    1.3.1 Módulo de Rastreamento GPS
      1.3.1.1 Desenvolvimento do agente de coleta de localização
      1.3.1.2 Desenvolvimento da API de recebimento
    1.3.2 Integração SAP MM
      1.3.2.1 Desenvolvimento do middleware de integração
      1.3.2.2 Mapeamento de campos SAP ↔ Sistema SRF
    1.3.3 Dashboard de Monitoramento
      1.3.3.1 Desenvolvimento da interface web (mapa + lista)
      1.3.3.2 Desenvolvimento dos filtros e relatórios
    1.3.4 Sistema de Alertas
      1.3.4.1 Desenvolvimento do motor de regras de alerta
      1.3.4.2 Integração com e-mail corporativo e Teams

  1.4 Fase 3 — Testes
    1.4.1 Testes Unitários e de Integração
      1.4.1.1 Testes do módulo de rastreamento
      1.4.1.2 Testes da integração SAP
    1.4.2 Testes de Aceitação do Usuário (UAT)
      1.4.2.1 Preparação do ambiente e casos de teste
      1.4.2.2 Execução do UAT com Supply Chain
      1.4.2.3 Correções pós-UAT e aprovação final

  1.5 Implantação e Go-Live
    1.5.1 Treinamento de Usuários
      1.5.1.1 Elaboração dos materiais de treinamento
      1.5.1.2 Treinamento do time Supply Chain (8 pessoas)
    1.5.2 Go-Live
      1.5.2.1 Migração para produção
      1.5.2.2 Monitoramento pós-go-live (30 dias)
    1.5.3 Onboarding de Fornecedores
      1.5.3.1 Comunicação e treinamento dos 12 fornecedores Tier 1

## Dicionário da WBS (resumido)
| ID | Entregável | Critério de Conclusão |
|----|------------|----------------------|
| 1.2.1.3 | ERF aprovada | Documento assinado pelo solicitante e pelo GP |
| 1.3.2.1 | Middleware SAP | Integração enviando e recebendo dados do SAP sem erros por 48h |
| 1.4.2.3 | UAT aprovado | Planilha de casos de teste com 100% dos Must Have aprovados |
| 1.5.2.2 | Pós-go-live | 30 dias de operação com SLA de disponibilidade ≥ 99,5% atingido |
```

## Quality Criteria

- [ ] WBS tem mínimo 3 níveis de decomposição
- [ ] Todos os pacotes de trabalho no nível mais baixo têm duração estimada ≤ 2 semanas
- [ ] Todos os itens "dentro do escopo" do TAP aparecem na WBS
- [ ] Gerenciamento do projeto é um elemento explícito da WBS (1.1)
- [ ] Dicionário da WBS com critério de conclusão para entregáveis críticos

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. A WBS tem menos de 3 níveis de decomposição
2. Algum item "dentro do escopo" do TAP não tem entrada correspondente na WBS
