---
task: "Levantar Requisitos"
order: 1
input:
  - qualificacao_aprovada: "Qualificação aprovada com escopo e resultado esperado"
  - tap: "TAP (se disponível) com escopo delimitado"
output:
  - lista_requisitos_bruta: "Lista de requisitos elicitados sem priorização ainda"
  - perguntas_abertas: "Questões que requerem validação com stakeholders"
---

# Levantar Requisitos

Elicita todos os requisitos funcionais e não-funcionais do projeto a partir das informações disponíveis. Usa técnicas de decomposição de escopo, análise de use cases e derivação de critérios de sucesso para garantir cobertura completa.

## Process

1. **Derivar requisitos dos critérios de sucesso**: Cada critério de sucesso do TAP implica ao menos 1-2 requisitos funcionais necessários para atingi-lo.
2. **Decompor as funcionalidades do escopo**: Para cada item "dentro do escopo" do TAP, derivar os requisitos funcionais necessários para implementá-lo.
3. **Identificar requisitos não-funcionais**: Para o contexto do projeto, definir requisitos de performance, segurança, disponibilidade e usabilidade.
4. **Documentar perguntas abertas**: Requisitos que não podem ser completamente especificados com as informações atuais são documentados como perguntas para validação com stakeholders.
5. **Estruturar com ID único**: Atribuir ID a cada requisito no formato RF001 (funcional) ou RNF001 (não-funcional).

## Output Format

```markdown
# Requisitos Elicitados — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD

## Requisitos Funcionais

### [Área Funcional 1]
| ID | Descrição | Origem |
|----|-----------|--------|
| RF001 | O sistema deve [ação] para que [usuário] possa [objetivo] | [TAP/Critério X] |

## Requisitos Não-Funcionais
| ID | Categoria | Descrição |
|----|-----------|-----------|
| RNF001 | Performance | O sistema deve responder em até [N] segundos para [% das] requisições |
| RNF002 | Disponibilidade | O sistema deve estar disponível [N]% do tempo, exceto janelas de manutenção |
| RNF003 | Segurança | Dados de localização devem ser criptografados em trânsito e em repouso |

## Perguntas Abertas
| ID | Questão | Para quem | Prazo |
|----|---------|-----------|-------|
| Q001 | [questão que bloqueia especificação de requisito] | [stakeholder] | [data] |
```

## Output Example

```markdown
# Requisitos Elicitados — SRF (Sistema de Rastreamento de Fornecedores)
Versão: 1.0 | Data: 2026-04-15

## Requisitos Funcionais

### Rastreamento em Tempo Real
| ID | Descrição | Origem |
|----|-----------|--------|
| RF001 | O sistema deve exibir a localização atual de cada entrega ativa dos fornecedores Tier 1 com atualização a cada 15 minutos no máximo | TAP — Escopo item 1 |
| RF002 | O sistema deve registrar o histórico de localização de cada entrega por no mínimo 90 dias | TAP — Escopo item 1 |
| RF003 | O sistema deve calcular e exibir a previsão de chegada (ETA) de cada entrega com base na localização atual | Critério de Sucesso #1 |

### Alertas Automáticos
| ID | Descrição | Origem |
|----|-----------|--------|
| RF004 | O sistema deve enviar alerta automático por e-mail e Teams quando o atraso estimado de uma entrega for superior a 2 horas | TAP — Escopo item 4 |
| RF005 | O alerta deve identificar: fornecedor, pedido, produto, atraso estimado e responsável pelo acompanhamento | TAP — Escopo item 4 |

### Integração SAP
| ID | Descrição | Origem |
|----|-----------|--------|
| RF006 | O sistema deve importar automaticamente os pedidos de compra do SAP MM com status "aguardando entrega" | TAP — Escopo item 3 |
| RF007 | O sistema deve atualizar o SAP MM com o status de entrega ("em trânsito", "entregue", "atrasado") a cada ciclo de atualização | TAP — Escopo item 3 |

### Dashboard
| ID | Descrição | Origem |
|----|-----------|--------|
| RF008 | O dashboard deve exibir o mapa com localização de todas as entregas ativas simultaneamente | TAP — Escopo item 2 |
| RF009 | O dashboard deve permitir filtro por fornecedor, status de entrega e período | Critério de Sucesso #1 |

## Requisitos Não-Funcionais
| ID | Categoria | Descrição |
|----|-----------|-----------|
| RNF001 | Performance | O dashboard deve carregar em até 3 segundos para 95% das requisições com até 50 usuários simultâneos |
| RNF002 | Disponibilidade | O sistema deve estar disponível 99,5% do tempo (máx. 3,6h/mês de indisponibilidade), exceto janelas de manutenção programadas |
| RNF003 | Segurança | Dados de localização devem ser criptografados em trânsito (TLS 1.3) e em repouso (AES-256) |
| RNF004 | Compliance | Todos os dados devem ser armazenados em servidores no Brasil (LGPD) |
| RNF005 | Usabilidade | Usuário deve conseguir encontrar o status de qualquer entrega em no máximo 3 cliques |

## Perguntas Abertas
| ID | Questão | Para quem | Prazo |
|----|---------|-----------|-------|
| Q001 | Fornecedores usarão app mobile ou dispositivo IoT para envio de localização? | TI + Procurement | 2026-04-20 |
| Q002 | Qual o nível de acesso de cada perfil de usuário (Supply Chain vs. TI vs. Fornecedor)? | Ana Ferreira | 2026-04-20 |
| Q003 | O SAP usa API REST ou BAPI para integração com sistemas externos? | Equipe TI SAP | 2026-04-18 |
```

## Quality Criteria

- [ ] Cada requisito funcional tem ID único no formato RF001
- [ ] Cada requisito está escrito com "O sistema deve" + ação + contexto
- [ ] Ao menos 4 categorias de RNF: performance, disponibilidade, segurança, usabilidade
- [ ] Perguntas abertas têm stakeholder responsável e prazo
- [ ] Todos os itens "dentro do escopo" do TAP têm ao menos 1 RF correspondente

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Algum item "dentro do escopo" do TAP não tem nenhum requisito funcional correspondente
2. Nenhum requisito não-funcional foi especificado (RNFs são sempre obrigatórios)
