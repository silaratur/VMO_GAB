---
task: "Criar Especificação de Requisitos Funcionais (ERF)"
order: 2
input:
  - lista_requisitos_bruta: "Requisitos elicitados na tarefa anterior"
output:
  - erf: "Documento de Especificação de Requisitos Funcionais completo e priorizado"
---

# Criar ERF

Transforma a lista bruta de requisitos em um documento formal de Especificação de Requisitos Funcionais (ERF) com priorização MoSCoW, critérios de aceitação e rastreabilidade completa.

## Process

1. **Organizar requisitos por área funcional**: Agrupar RF e RNF por módulo ou funcionalidade para facilitar leitura e rastreamento.
2. **Aplicar priorização MoSCoW**: Para cada requisito, classificar como Must Have (essencial), Should Have (importante), Could Have (desejável) ou Won't Have (fora do escopo atual).
3. **Escrever critério de aceitação**: Para cada Must Have, definir o critério verificável e testável que confirma que o requisito foi implementado.
4. **Verificar que nenhum requisito é ambíguo**: Revisar toda a lista e substituir termos vagos por definições quantitativas.
5. **Criar glossário**: Documentar os termos técnicos e de domínio usados nos requisitos.

## Output Format

```markdown
# ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS (ERF)
Projeto: [nome] | Versão: 1.0 | Data: YYYY-MM-DD

## 1. Requisitos Funcionais

### [Área 1]
| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF001 | O sistema deve... | Must Have | [critério testável] | TAP |

## 2. Requisitos Não-Funcionais
| ID | Categoria | Descrição | Prioridade | Critério de Aceitação |
|----|-----------|-----------|------------|----------------------|

## 3. Resumo de Priorização MoSCoW
| Prioridade | Qtde | Percentual |
|------------|------|------------|
| Must Have | [N] | [%] |
| Should Have | [N] | [%] |
| Could Have | [N] | [%] |
| Won't Have | [N] | [%] |

## 4. Glossário
| Termo | Definição |
|-------|-----------|
| [termo] | [definição clara] |

## 5. Aprovação
Analista: _________________ Data: _______
Solicitante: _______________ Data: _______
```

## Output Example

```markdown
# ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS (ERF) — SRF
Projeto: Sistema de Rastreamento de Fornecedores | Versão: 1.0 | Data: 2026-04-15

## 1. Requisitos Funcionais

### Rastreamento em Tempo Real
| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF001 | O sistema deve exibir a localização atual de cada entrega ativa dos fornecedores Tier 1 com atualização máxima de 15 min | Must Have | Dado de localização exibido com timestamp; diferença entre horário do dado e horário atual ≤ 15 min em 100% dos testes | TAP — Escopo 1 |
| RF002 | O sistema deve registrar histórico de localização por mínimo 90 dias | Should Have | Consulta de histórico de entrega com 90+ dias de dados retorna resultado sem erro | TAP — Escopo 1 |

### Alertas Automáticos
| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF004 | O sistema deve enviar alerta por e-mail e Teams quando atraso estimado > 2 horas | Must Have | Alerta enviado em até 5 min após detecção de atraso; verificado em 10 testes consecutivos | TAP — Escopo 4 |
| RF005 | O alerta deve conter: fornecedor, pedido, produto, atraso estimado e responsável | Must Have | Alerta gerado em testes contém todos os 5 campos sem exceção | TAP — Escopo 4 |

## 2. Requisitos Não-Funcionais
| ID | Categoria | Descrição | Prioridade | Critério de Aceitação |
|----|-----------|-----------|------------|----------------------|
| RNF001 | Performance | Dashboard carrega em ≤ 3s para 95% das requisições com 50 usuários simultâneos | Must Have | Teste de carga com 50 usuários: percentil 95 do tempo de resposta ≤ 3,0s |
| RNF002 | Disponibilidade | Sistema disponível 99,5% do tempo | Must Have | Monitoramento de 30 dias pós-go-live confirma uptime ≥ 99,5% |
| RNF003 | Segurança | Dados de localização criptografados (TLS 1.3 + AES-256) | Must Have | Auditoria de segurança confirma criptografia em trânsito e repouso |
| RNF004 | Compliance | Dados armazenados exclusivamente em servidores no Brasil | Must Have | Verificação de infraestrutura confirma 100% dos dados em DCs no Brasil |

## 3. Resumo de Priorização MoSCoW
| Prioridade | Qtde | Percentual |
|------------|------|------------|
| Must Have | 8 | 62% |
| Should Have | 3 | 23% |
| Could Have | 2 | 15% |
| Won't Have | 0 | 0% |

## 4. Glossário
| Termo | Definição |
|-------|-----------|
| Tier 1 | Fornecedores classificados como críticos pela área de Supply Chain — interrupção causa impacto direto na produção |
| ETA | Estimated Time of Arrival — previsão de chegada calculada com base em localização atual e rota |
| SAP MM | Módulo de Materials Management do SAP — responsável pela gestão de pedidos de compra e recebimento |
| Rastreamento em tempo real | Atualização de dados de localização com frequência máxima de 15 minutos |

## 5. Aprovação
Analista: Rafael Requisito (VMO)   Data: ________
Solicitante: Ana Carolina Ferreira   Data: ________
```

## Quality Criteria

- [ ] Todos os Must Have têm critério de aceitação mensurável e testável
- [ ] Priorização MoSCoW aplicada a 100% dos requisitos
- [ ] Nenhum requisito contém termos vagos sem definição quantitativa
- [ ] Glossário documenta ao menos os termos técnicos do domínio
- [ ] Tabela MoSCoW consolidada com contagem e percentual
- [ ] Campos de aprovação (analista e solicitante) incluídos

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Algum requisito Must Have não tem critério de aceitação definido
2. Algum requisito contém o termo "intuitivo", "rápido", "fácil" ou "eficiente" sem definição quantitativa
