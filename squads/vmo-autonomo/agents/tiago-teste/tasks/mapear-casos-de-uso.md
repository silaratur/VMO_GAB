---
task: "Mapear Casos de Uso"
order: 1
input:
  - erf: "ERF com requisitos RF e RNF priorizados com MoSCoW e critérios de aceitação"
  - documentacao_base: "TAP com stakeholders, escopo e atores identificados"
output:
  - catalogo_uc: "Catálogo de casos de uso com fluxos principal, alternativo e de exceção"
  - mapa_rastreabilidade_uc_rf: "Tabela de rastreabilidade UC → RF para validação de cobertura"
---

# Mapear Casos de Uso

Deriva os casos de uso do sistema a partir dos requisitos funcionais da ERF e dos stakeholders/atores identificados no TAP. Cada caso de uso descreve uma interação completa entre um ator e o sistema, cobrindo o fluxo principal (happy path), variações esperadas (fluxos alternativos) e condições de erro (fluxos de exceção). O catálogo garante que 100% dos RF Must Have estejam cobertos por ao menos um UC.

## Process

1. **Identificar atores**: A partir do TAP (stakeholders) e da ERF (usuários implícitos nos requisitos), listar todos os atores primários (iniciam a interação), secundários (participam sem iniciar) e sistemas externos (integram com o sistema).
2. **Agrupar RFs por área funcional**: Usar as áreas funcionais já definidas na ERF para agrupar requisitos relacionados — cada agrupamento tende a corresponder a um ou mais casos de uso.
3. **Definir os UCs**: Para cada agrupamento, definir o(s) UC(s) necessário(s). Um UC cobre uma sequência coesa de interações com objetivo único para o ator. Evitar UCs muito amplos (cobrindo múltiplos objetivos) ou muito estreitos (cobrindo um único passo).
4. **Redigir cada UC no formato padrão**: Preencher todos os campos obrigatórios — ator, pré-condições, pós-condições, fluxo principal (numerado), fluxos alternativos e fluxo de exceção.
5. **Mapear rastreabilidade UC → RF**: Para cada UC, listar quais RFs ele implementa. Construir a tabela de rastreabilidade.
6. **Verificar cobertura inversa**: Confirmar que cada RF Must Have tem ao menos 1 UC que o cobre. RFs Must Have sem UC representam lacuna de especificação — devem ser cobertos antes de finalizar.

## Output Format

```markdown
# CATÁLOGO DE CASOS DE USO — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD | Elaborado por: Tiago Teste (VMO)

## Atores do Sistema

| Ator | Tipo | Descrição | RFs Relacionados |
|------|------|-----------|-----------------|
| [Nome do Ator] | Primário | [descrição do papel e motivação] | RF001, RF002 |
| [Sistema Externo] | Sistema Externo | [descrição da integração] | RF006, RF007 |

## Índice de Casos de Uso

| ID | Nome | Ator Principal | Prioridade | RFs Cobertos |
|----|------|----------------|------------|--------------|
| UC001 | [Nome descritivo do UC] | [Ator] | Must Have | RF001, RF002 |
| UC002 | [Nome descritivo do UC] | [Ator] | Should Have | RF003 |

---

## UC001 — [Nome Descritivo do Caso de Uso]

**Ator principal:** [nome do ator que inicia a interação]
**Atores secundários:** [nomes dos atores que participam, ou "Nenhum"]
**Prioridade:** [Must Have | Should Have | Could Have]

**Pré-condições:**
- [Estado verificável do sistema antes da interação — deve ser possível confirmar se está satisfeito]
- [Ex: Usuário autenticado com perfil "Operador"]
- [Ex: Ao menos 1 entrega ativa registrada no sistema]

**Pós-condições (sucesso):**
- [Estado do sistema após execução bem-sucedida do fluxo principal]
- [Ex: Localização da entrega registrada com timestamp e exibida no mapa]

**Pós-condições (falha/exceção):**
- [Estado do sistema após qualquer fluxo de exceção]
- [Ex: Sistema permanece no estado anterior; log de erro registrado]

**Fluxo Principal:**
1. [Ator] acessa [funcionalidade/tela]
2. Sistema exibe [dados/interface]
3. [Ator] seleciona/informa [dado ou ação]
4. Sistema valida [condição de validação]
5. Sistema processa [operação]
6. Sistema confirma [resultado para o ator]

**Fluxo Alternativo A — [Nome descritivo da alternativa]:**
> Condição: Quando [condição específica que desvia do fluxo principal] no passo [N]
>
> A1. [Ator ou Sistema] [ação alternativa]
> A2. Sistema [resposta da alternativa]
> A3. [Retorna ao passo X do fluxo principal | Caso de uso conclui com [resultado alternativo]]

**Fluxo Alternativo B — [Nome descritivo da alternativa B]:**
> Condição: Quando [condição específica] no passo [N]
>
> B1. [ação]
> B2. [resposta]
> B3. [continuação]

**Fluxo de Exceção E1 — [Nome do erro]:**
> Condição: Quando [condição de erro verificável] no passo [N]
>
> E1a. Sistema exibe mensagem: "[texto exato da mensagem de erro]"
> E1b. Sistema registra log de erro contendo: [dados do log — ex: timestamp, usuário, código de erro]
> E1c. Caso de uso termina. Estado do sistema: [estado de falha]

**Requisitos cobertos:** RF001, RF002, RNF003

---
```

## Output Example

```markdown
# CATÁLOGO DE CASOS DE USO — SRF (Sistema de Rastreamento de Fornecedores)
Versão: 1.0 | Data: 2026-04-18 | Elaborado por: Tiago Teste (VMO)

## Atores do Sistema

| Ator | Tipo | Descrição | RFs Relacionados |
|------|------|-----------|-----------------|
| Analista de Supply Chain | Primário | Monitora entregas e aciona fornecedores em caso de atraso | RF001, RF002, RF004, RF008, RF009 |
| Fornecedor Tier 1 | Primário | Envia atualizações de localização via app/dispositivo IoT | RF001 |
| Administrador TI | Secundário | Configura integrações e perfis de acesso | RF006, RF007 |
| SAP MM | Sistema Externo | Fonte de pedidos de compra; receptor de status de entrega | RF006, RF007 |

## Índice de Casos de Uso

| ID | Nome | Ator Principal | Prioridade | RFs Cobertos |
|----|------|----------------|------------|--------------|
| UC001 | Monitorar Entregas em Tempo Real | Analista de Supply Chain | Must Have | RF001, RF002, RF008, RF009 |
| UC002 | Receber Alerta de Atraso | Analista de Supply Chain | Must Have | RF004, RF005 |
| UC003 | Consultar Histórico de Localização | Analista de Supply Chain | Should Have | RF002 |
| UC004 | Integrar Pedidos do SAP | SAP MM | Must Have | RF006, RF007 |
| UC005 | Atualizar Localização da Entrega | Fornecedor Tier 1 | Must Have | RF001, RF003 |

---

## UC001 — Monitorar Entregas em Tempo Real

**Ator principal:** Analista de Supply Chain
**Atores secundários:** Nenhum
**Prioridade:** Must Have

**Pré-condições:**
- Analista autenticado no sistema com perfil "Supply Chain"
- Ao menos 1 entrega ativa com fornecedor Tier 1 registrada no sistema
- Dados de localização atualizados há no máximo 15 minutos (conforme RNF001)

**Pós-condições (sucesso):**
- Mapa exibido com localização de todas as entregas ativas de fornecedores Tier 1
- ETA calculado e exibido para cada entrega ativa
- Timestamp da última atualização visível por entrega

**Pós-condições (falha/exceção):**
- Sistema permanece na tela anterior; mensagem de erro exibida
- Nenhuma entrega é removida ou alterada

**Fluxo Principal:**
1. Analista acessa o dashboard de monitoramento
2. Sistema carrega o mapa com localização de todas as entregas ativas
3. Sistema exibe para cada entrega: fornecedor, pedido, produto, localização atual e ETA
4. Sistema sinaliza entregas com atraso previsto > 0 min com indicador visual
5. Analista seleciona uma entrega específica para ver detalhes
6. Sistema exibe painel lateral com detalhes: histórico de localização das últimas 4 horas, ETA atualizado, responsável pelo acompanhamento

**Fluxo Alternativo A — Filtrar entregas por fornecedor:**
> Condição: Analista deseja visualizar apenas entregas de um fornecedor específico no passo 2
>
> A1. Analista aplica filtro por fornecedor no campo de filtros do dashboard
> A2. Sistema recarrega o mapa exibindo apenas entregas do fornecedor selecionado
> A3. Fluxo continua a partir do passo 3

**Fluxo Alternativo B — Filtrar por status de entrega:**
> Condição: Analista deseja ver apenas entregas com status "Atrasado" no passo 2
>
> B1. Analista seleciona filtro "Status: Atrasado"
> B2. Sistema recarrega o mapa exibindo apenas entregas com atraso previsto > 0 min
> B3. Fluxo continua a partir do passo 3

**Fluxo de Exceção E1 — Dados de localização desatualizados:**
> Condição: Sistema detecta que dados de alguma entrega estão desatualizados há > 15 minutos no passo 2
>
> E1a. Sistema exibe indicador de alerta na entrega afetada: "Sem atualização há [N] min"
> E1b. Sistema registra log: timestamp, ID da entrega, minutos sem atualização
> E1c. Caso de uso continua — sistema exibe as demais entregas normalmente; entrega afetada sinalizada

**Fluxo de Exceção E2 — Falha no carregamento do mapa:**
> Condição: Sistema não consegue carregar o mapa no passo 2 (timeout ou erro de conectividade)
>
> E2a. Sistema exibe: "Não foi possível carregar o mapa. Verifique sua conexão e tente novamente."
> E2b. Sistema registra log: timestamp, código de erro HTTP, duração do timeout
> E2c. Caso de uso termina. Estado do sistema: tela de erro com botão "Tentar novamente"

**Requisitos cobertos:** RF001, RF002, RF008, RF009, RNF001
```

## Quality Criteria

- [ ] Tabela de atores com tipo (primário/secundário/sistema externo) e RFs relacionados
- [ ] Índice de UCs com ID único, ator principal, prioridade e RFs cobertos
- [ ] Cada UC tem: pré-condições verificáveis, pós-condições de sucesso e de falha
- [ ] Fluxo principal de cada UC tem mínimo 4 passos numerados
- [ ] Cada UC tem ao menos 1 fluxo alternativo documentado
- [ ] Cada UC tem ao menos 1 fluxo de exceção documentado
- [ ] Rastreabilidade UC → RF listada ao final de cada UC
- [ ] 100% dos RF Must Have aparecem em ao menos 1 UC

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Algum UC não tem ator principal definido
2. Algum UC não tem fluxo alternativo ou fluxo de exceção
3. Algum RF Must Have não aparece em nenhum UC (lacuna de cobertura)
