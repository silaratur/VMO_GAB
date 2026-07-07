# Sizing Inicial de Escopo
Projeto: PROJ-2026-008
Data: 2026-07-07
Analista: Rafael Requisito
Fase: Pré-qualificação (subsidia critério 7 do Felipe Filtro)

## Escopo Preliminar Identificado

| # | Componente | Tipo | Clareza do Escopo |
|---|-----------|------|-------------------|
| 1 | Migração do fluxo de caixa (ingressos, egressos, LAIR) de Excel para o TVM | Configuração/Desenvolvimento | Claro |
| 2 | Segregação de receitas por tipo de negócio (ex.: "Squad", cartão por bandeira) | Desenvolvimento | Claro no requisito, incerto no como (SAP hoje não segrega neste nível) |
| 3 | Despesas agrupadas por categoria (manutenção, combustível, TI) até o LAIR | Configuração | Claro |
| 4 | Automação em tempo real (substitui apresentação semanal manual à diretoria) | Desenvolvimento | Claro no objetivo, incerto no mecanismo (batch vs. real-time real) |
| 5 | Projeções analíticas por linha (receita/despesa) para orçado vs. realizado | Desenvolvimento/Configuração | **Incerto** — dúvida técnica explicitamente em aberto na ata (capacidade do TVM não confirmada) |
| 6 | Dashboards gráficos + possível integração com BI | Desenvolvimento/Integração | Incerto — tratado como "plus", capacidade técnica a confirmar |
| 7 | Rastreabilidade de custos até nível de nota fiscal (hoje SAP só desce a lote/grupo de conta) | Desenvolvimento | Claro no requisito, mas exige granularidade de dado hoje inexistente no SAP — a confirmar viabilidade |
| 8 | Visibilidade financeira das compras para Suprimentos (relatórios de consumo) | Configuração/Desenvolvimento | Claro |
| 9 | Ampliação do horizonte de previsão de caixa de mensal para 90 dias | Configuração | Claro |
| 10 | Integração adicional com sistema Atenas (2 empresas fora do SAP) | Integração | **Incerto** — "a ser avaliada tecnicamente" na própria ata |
| 11 | Painel Suprimentos: baseline orçado com atualização automática por lançamento | Desenvolvimento | Claro |
| 12 | Projeção de pagamentos parcelados (30/60/90 dias) | Desenvolvimento | Claro |
| 13 | Alertas automáticos por faixa de consumo do orçado (70%/85%) | Desenvolvimento/Configuração | Claro |
| 14 | Definição de níveis de permissão/acesso no SAP/TVM para ampliação a outros gestores | Configuração | A confirmar (fora de escopo imediato, mas mencionado) |

**Precedente técnico relevante**: o TVM já está implantado e em uso pela VIX (outra empresa do grupo), citado como modelo de referência por Thamyris. Isso eleva a confiança para os componentes de configuração-padrão (itens 1, 3, 8, 9, 11, 12, 13), mas **não** para os itens que exigem customização nova ou integração não testada no grupo (itens 2, 5, 6, 7, 10), que vão além do que a VIX já usa.

## Estimativa de Esforço por Fase

| Fase | Atividades | Estimativa | Confiança | Premissas |
|------|-----------|------------|-----------|-----------|
| Levantamento de requisitos detalhado | Fechar a frente Financeiro (ata parcial), confirmar capacidade técnica do TVM (itens 5, 6, 7, 10) junto à equipe técnica, elicitação com as 3 áreas (Financeiro, Suprimentos, Riscos) | 40–56h | MÉDIA | Assume que a sessão de continuação com Alessandra ocorre antes do início formal; se não ocorrer, esforço desta fase aumenta |
| Desenvolvimento/Configuração | Configuração TVM nos moldes VIX (itens 1,3,8,9,11,12,13) + desenvolvimento customizado para segregação de receita, projeções analíticas, dashboards/BI e rastreabilidade a NF (itens 2,5,6,7) + avaliação/implementação de integração Atenas (item 10) | 110–190h | BAIXA | Faixa larga porque 5 dos 14 componentes têm viabilidade técnica não confirmada; se TVM não suportar projeções analíticas por linha (item 5) ou integração Atenas (item 10), parte do escopo muda para solução alternativa, alterando a estimativa |
| Testes e homologação | Testes de configuração (padrão VIX) + testes específicos dos itens customizados (segregação de receita, alertas, projeções) + UAT com as 3 áreas | 32–48h | MÉDIA | Presume 3 ciclos de UAT (um por área/frente) |
| Go-live e suporte inicial | Cutover do processo manual (Excel) para o TVM nas 3 frentes, treinamento de usuários (Financeiro, Suprimentos, Riscos), acompanhamento pós-go-live | 24–40h | MÉDIA | Presume rollout simultâneo das 3 frentes; rollout faseado aumentaria o esforço total |
| **TOTAL** | | **206h–334h** | **BAIXA** (puxada para baixo pelos itens de viabilidade técnica não confirmada) | |

## Classificação de Esforço
**[ ] < 80h** / **[ ] 80–160h** / **[X] > 160h** → **Projeto formal** (mesmo no piso da faixa, 206h já ultrapassa o limiar de 160h)

## Fatores de Risco que Afetam o Esforço

| Fator | Impacto se confirmado | Probabilidade |
|-------|----------------------|---------------|
| TVM não suportar projeções analíticas por linha (orçado vs. realizado) — item 5 | +30–50h (necessidade de solução alternativa ou desenvolvimento adicional) | MÉDIA |
| Integração com sistema Atenas exigir desenvolvimento customizado (não apenas configuração) — item 10 | +20–40h | MÉDIA |
| Rastreabilidade a nível de nota fiscal exigir mudança de estrutura de lançamento no SAP (não só no TVM) — item 7 | +25–40h | MÉDIA-ALTA |
| Dashboards/BI (item 6) confirmados como escopo obrigatório (hoje é "plus") | +20–35h | BAIXA-MÉDIA |
| Rollout faseado por área em vez de simultâneo (por resistência ou disponibilidade de equipe) | +15–25h | MÉDIA |
| Frente Financeiro (Alessandra) trazer requisitos adicionais relevantes na sessão de continuação ainda não realizada | +10–20h | ALTA (a sessão ainda nem ocorreu) |

## Lacunas de Escopo (para ERF futura)

| # | Lacuna | Por que afeta o esforço |
|---|--------|------------------------|
| 1 | O TVM suporta inserção de projeções analíticas por linha (receitas/despesas) para orçado vs. realizado? | Determina se o item 5 é configuração (baixo esforço) ou desenvolvimento customizado/solução alternativa (alto esforço) |
| 2 | Qual o escopo técnico real da integração com o sistema Atenas, e quais das duas empresas pendentes precisam dela? | Define se o item 10 é integração simples ou projeto de integração à parte |
| 3 | A rastreabilidade a nível de nota fiscal é viável apenas no TVM, ou exige mudança na forma de lançamento no SAP? | Muda a superfície de impacto de "só TVM" para "TVM + processo SAP", elevando esforço e risco |
| 4 | Dashboards gráficos e integração com BI são escopo obrigatório desta fase ou item futuro (fase 2)? | Se obrigatório agora, adiciona um bloco de desenvolvimento e integração não dimensionado nas fases padrão VIX |
| 5 | Quando ocorrerá a sessão de continuação com a Alessandra (Financeiro), e qual o prazo real disponível para incorporar seus requisitos? | Requisitos da frente Financeiro ainda incompletos podem alterar escopo e cronograma antes mesmo do início do desenvolvimento |

## Nota para Felipe Filtro

Classificação de esforço: **Projeto formal** (206h–334h, ultrapassa o limiar de 160h mesmo no cenário mais otimista). Isso é consistente com a visão de Wellington ("projeto", não melhoria pontual) e diverge da leitura inicial de Alessandra ("melhoria de processo") — a diferença provavelmente reflete que cada um viu apenas sua fatia do escopo. Principal driver de incerteza: 5 dos 14 componentes de escopo (projeções analíticas, dashboards/BI, integração Atenas, rastreabilidade a NF, e os requisitos ainda não levantados da frente Financeiro) têm viabilidade técnica ou completude não confirmada — a confiança geral é BAIXA por isso, não por falta de precedente (o TVM já roda na VIX para o núcleo do escopo). Recomendo não fechar a classificação final (critério 7) até obter resposta às 5 lacunas acima, especialmente a continuação da entrevista com Alessandra, que ainda pode adicionar escopo.
