# Plano de Gestão de Riscos — PROJ-2026-008
Implantação/Expansão do TVM para Fluxo de Caixa, Controle Orçamentário e
Rastreabilidade de Riscos (Grupo Águia Branca)

Autor: Pedro Perigo (Analista de Riscos, VMO Autônomo)
Data: 2026-07-07 | Versão: 1.0 | Status: RASCUNHO (6 CBs do TAP ainda em aberto)

Fontes analisadas: `documentacao-base.md` (TAP — premissas e restrições),
`cronograma.md` (caminho crítico), `requisitos.md` (itens condicionados
CB-5), `sizing.md` (fatores de risco técnico).

---

## Registro de Riscos

| ID | Categoria | Descrição do Risco | Prob (1-5) | Impacto (1-5) | Score | Nível |
|----|-----------|---------------------|:---:|:---:|:---:|:---:|
| R-001 | Governança | As Condições Bloqueantes de governança (CB-1: evidência documental do sponsor; CB-2: aprovação de Diretoria + Gerente de TI) podem não ser resolvidas antes do kick-off, impedindo a validação formal da demanda mesmo com a documentação de iniciação pronta | 4 | 5 | 20 | CRÍTICO |
| R-002 | Financeiro | O orçamento sinalizado como aprovado (R$30-32k) pode se confirmar insuficiente frente ao custo real estimado (R$43-70k), exigindo aprovação de verba adicional no meio do projeto (CB-3) | 4 | 4 | 16 | CRÍTICO |
| R-003 | Prazo | O caminho crítico do cronograma depende do fechamento da sessão de continuação com Alessandra (CB-4) logo na Fase 1 — qualquer atraso nessa sessão desliza toda a Fase 1 e, em cascata, o Go-live | 3 | 4 | 12 | ALTO |
| R-004 | Técnico | A viabilidade técnica de 5 dos 20 requisitos da ERF (RF-FIN-03-C, RF-SUP-04-C, RF-RIS-03, RF-TRA-01/02/03/04 — itens CB-5) pode não se confirmar, exigindo desenvolvimento adicional não dimensionado no sizing atual | 3 | 3 | 9 | ALTO |
| R-005 | Stakeholders/Recursos | Dependência crítica de uma única pessoa (Thamyris) para o conhecimento operacional do processo atual — sua indisponibilidade (agenda, saída, licença) atrasa significativamente o levantamento e a homologação da frente Riscos/Desempenho | 3 | 4 | 12 | ALTO |
| R-006 | Recursos/Prazo | A disponibilidade da equipe técnica TVM (premissa de ~30h úteis/semana usada em todo o cronograma) não foi confirmada por nenhuma fonte — se a disponibilidade real for menor, todas as durações do cronograma se estendem proporcionalmente | 3 | 3 | 9 | ALTO |
| R-007 | Financeiro/Governança | A ausência de benefício financeiro quantificado (CB-6) dificulta a defesa de uma eventual aprovação orçamentária adicional (decorrente de R-002) junto ao comitê/diretoria | 3 | 2 | 6 | MÉDIO |
| R-008 | Compliance/Externo | Erros de segregação de receita ou de rastreabilidade de custos (dado que 2 dos requisitos Must Have — RF-FIN-03 e RF-RIS-02 — operam em nível de granularidade parcial, não total) podem gerar informação financeira imprecisa em relatórios usados pela diretoria e contabilidade gerencial | 2 | 4 | 8 | MÉDIO |

---

## Análise por Categoria

### Riscos de Governança
**R-001 (CRÍTICO):** Nenhuma das duas aprovações formais exigidas pela Regra GP 2026-05-24 está documentada até o momento — apenas confirmação verbal do PMO nesta sessão. Premissa violada se testada: "identidade do sponsor confirmada é suficiente para autorizar o TAP" — não é, falta documento.
Sinal de materialização: kick-off (M0) atingido sem evidência documental anexada para CB-1 e CB-2.

### Riscos Financeiros
**R-002 (CRÍTICO):** O gap entre R$30-32k (aprovado) e R$43-70k (estimado) é uma das maiores incertezas do projeto — maior, inclusive, que o próprio valor aprovado.
Sinal de materialização: cotação/estimativa detalhada do fornecedor (via Work Request) retorna valor acima de R$40k.
**R-007 (MÉDIO):** Sem benefício quantificado, uma eventual necessidade de verba adicional (R-002) terá dificuldade de aprovação rápida.

### Riscos de Prazo
**R-003 (ALTO):** A própria WBS/cronograma do Carlos identifica a frente Financeiro como dominante no caminho crítico — não por complexidade técnica, mas por depender de uma pendência de negócio (CB-4) ainda sem data.
Sinal de materialização: sessão de continuação com Alessandra não agendada até 5 dias úteis após o kick-off (M0).
**R-006 (ALTO):** Toda a estimativa de duração do cronograma (WBS, marcos, buffer) parte de uma premissa de capacidade não confirmada.
Sinal de materialização: equipe técnica TVM reporta disponibilidade real abaixo de 20h úteis/semana em qualquer semana das Fases 1-3.

### Riscos Técnicos
**R-004 (ALTO):** Os mesmos 5 itens que a ERF já tratou com cautela (Could Have condicionado / Won't Have) são risco de escopo, não apenas de "recurso extra" — se a equipe técnica confirmar inviabilidade total (não parcial), pode ser necessário replanejar parte da Fase 2.
Sinal de materialização: sessão técnica de confirmação (WBS 1.2.2.1) não resolve pelo menos 3 dos 5 itens até o marco M1 (ERF v2.0).

### Riscos de Stakeholders / Compliance
**R-005 (ALTO):** Nenhum plano de redistribuição de conhecimento foi formalmente criado ainda — o Plano Geral (Diana Documento, plano 5) já registrou isso como recomendação, mas não como entregável obrigatório.
Sinal de materialização: Thamyris fica indisponível (agenda, licença) por mais de 5 dias úteis durante as Fases 1-2.
**R-008 (MÉDIO):** RF-FIN-03 (classificação manual-assistida) e RF-RIS-02 (rastreabilidade em nível SAP atual, não NF) são versões parciais dos requisitos originalmente desejados — o risco é que usuários/diretoria tratem o dado como mais preciso do que realmente é.
Sinal de materialização: qualquer divergência entre o relatório do TVM e o cálculo manual de referência durante o UAT (RF-FIN-02) acima de R$ 0,00.

---

## Plano de Resposta a Riscos

### R-001 — CBs de Governança Não Resolvidas — CRÍTICO
- **Estratégia:** Evitar (resolução antes do kick-off formal)
- **Gatilho:** Kick-off (M0) alcançado sem evidência documental anexada para CB-1/CB-2
- **Ações de Resposta:**
  1. Obter e-mail/ata assinada confirmando Paula Barcelos como sponsor — Responsável: Marcelo Silveira (PMO) — Prazo: antes do M0
  2. Obter aprovação formal de Diretoria (Financeiro) e Gerente de TI da divisão — Responsável: PMO / Alessandra Comério — Prazo: antes do M0
- **Plano de Contingência:** Se M0 precisar ocorrer antes da resolução completa, GP registra ciência formal do risco (aceite documentado do PMO) e mantém o cronograma como condicional até a resolução — nunca tratar como resolvido por omissão.
- **Custo da Resposta:** R$ 0 (ação administrativa)

### R-002 — Insuficiência Orçamentária — CRÍTICO
- **Estratégia:** Mitigar
- **Gatilho:** Proposta de fornecedor (via Work Request) retorna valor acima de R$ 32.000
- **Ações de Resposta:**
  1. Solicitar decomposição de custo detalhada ao fornecedor selecionado antes de assinar contrato — Responsável: Fábio Fornecedor / PMO — Prazo: na fase de seleção de fornecedor
  2. Apresentar à CEO a reconciliação orçamentária (CB-3) com base na proposta real recebida, não na estimativa do sizing — Responsável: Marcelo Silveira (PMO) — Prazo: antes da assinatura do WR
- **Plano de Contingência:** Reduzir escopo da Fase 2 (postergar RF-FIN-03/RF-SUP-04 completos para fase 2, mantendo apenas o núcleo Must Have de menor esforço) se o orçamento adicional não for aprovado
- **Custo da Resposta:** R$ 0 / até R$ 40.000 adicionais se a contingência de verba não for aprovada e for necessário reduzir escopo com retrabalho

### R-003 — Atraso da Frente Financeiro no Caminho Crítico — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Sessão de continuação com Alessandra não agendada até 5 dias úteis após M0
- **Ações de Resposta:**
  1. Agendar a sessão de continuação com Alessandra imediatamente após o kick-off, como primeira ação do GP — Responsável: PMO / GP designado — Prazo: M0 + 3 dias úteis
  2. Preparar pauta objetiva cobrindo exatamente as lacunas já mapeadas (PA-02, sistemas, prazo, critérios de sucesso) para não estender a sessão — Responsável: Rafael Requisito — Prazo: antes da sessão
- **Plano de Contingência:** Se a sessão não ocorrer no prazo, iniciar Fase 2 apenas nas frentes Suprimentos e Riscos/Desempenho (que não dependem de CB-4), postergando a frente Financeiro sem travar o projeto inteiro
- **Custo da Resposta:** R$ 0

### R-004 — Viabilidade Técnica Não Confirmada (CB-5) — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Sessão técnica (WBS 1.2.2.1) não resolve ao menos 3 dos 5 itens até o marco M1
- **Ações de Resposta:**
  1. Priorizar a sessão técnica com Cássio e equipe TVM logo na primeira semana da Fase 1 — Responsável: Cássio — Prazo: M0 + 8 dias úteis (já no cronograma)
  2. Preparar plano B de escopo reduzido (manter apenas as versões Must Have já viáveis) caso a confirmação não ocorra a tempo — Responsável: Rafael Requisito — Prazo: M1
- **Plano de Contingência:** Formalizar os itens não confirmados como mudança de escopo futura (Fase 2 do programa maior mencionado por Wellington), não como falha deste projeto
- **Custo da Resposta:** R$ 0 / custo de desenvolvimento adicional a estimar após confirmação (ver sizing.md, fatores de risco: +20-50h por item conforme aplicável)

### R-005 — Dependência Crítica de Thamyris — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Indisponibilidade de Thamyris por mais de 5 dias úteis durante as Fases 1-2
- **Ações de Resposta:**
  1. Documentar formalmente o processo manual atual (runbook) como parte da Fase 1, não depender apenas de conhecimento tácito — Responsável: Thamyris + Rafael Requisito — Prazo: durante a Fase 1
  2. Identificar um backup/substituto parcial (ex: analista Lucas, já mencionado nas atas) para continuidade em caso de indisponibilidade — Responsável: Thamyris / PMO — Prazo: antes do M0
- **Plano de Contingência:** Estender prazo da Fase 1 especificamente para a frente Riscos/Desempenho sem impactar as demais frentes, usando a folga não-crítica identificada no cronograma do Carlos
- **Custo da Resposta:** R$ 0

### R-006 — Disponibilidade de Equipe TVM Não Confirmada — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Disponibilidade real reportada abaixo de 20h úteis/semana em qualquer semana das Fases 1-3
- **Ações de Resposta:**
  1. Confirmar formalmente com a equipe técnica TVM a alocação de ~30h úteis/semana antes do kick-off — Responsável: Cássio / PMO — Prazo: antes de M0
  2. Se não confirmado, recalcular o cronograma com a capacidade real disponível antes de basear o cronograma (nunca basear sem confirmação, conforme princípio do Carlos Cronograma) — Responsável: Carlos Cronograma — Prazo: antes de M0
- **Plano de Contingência:** Reforço temporário de equipe (recurso externo) financiado pela reserva de contingência, se a capacidade real for insuficiente e o prazo não puder deslizar
- **Custo da Resposta:** R$ 0 / R$ 15.000 se reforço de equipe for necessário

### R-007 — Benefício Não Quantificado Dificulta Aprovação de Verba Adicional — MÉDIO
- **Estratégia:** Mitigar
- **Gatilho:** Necessidade de verba adicional (R-002) surge antes de qualquer benefício estar quantificado
- **Ações de Resposta:**
  1. Quantificar ao menos 1 benefício principal (ex: horas/mês do analista Lucas hoje gastas na consolidação manual × custo-hora) — Responsável: Alessandra Comério / Thamyris / PMO — Prazo: antes do TAP ser considerado final (CB-6, já registrada)
- **Plano de Contingência:** Apresentar a proposta de valor qualitativa já registrada por Felipe Filtro (qualificacao.md) como argumento intermediário, reconhecendo a limitação
- **Custo da Resposta:** R$ 0

### R-008 — Dados Financeiros Parciais Tratados Como Completos — MÉDIO
- **Estratégia:** Mitigar
- **Gatilho:** Divergência entre relatório do TVM e cálculo manual de referência durante o UAT (RF-FIN-02) acima de R$ 0,00
- **Ações de Resposta:**
  1. Documentar explicitamente, em toda a documentação de treinamento e nos relatórios gerados (RF-FIN-05), que a segregação de receita é manual-assistida e a rastreabilidade de custos está no nível SAP atual (não nota fiscal) — Responsável: Diana Documento / Sara Status — Prazo: antes do treinamento (Fase 4)
  2. Incluir nota de rodapé/legenda nos relatórios automáticos indicando o nível de granularidade dos dados — Responsável: Equipe técnica TVM — Prazo: Fase 2
- **Plano de Contingência:** Se a diretoria exigir maior precisão, tratar como gatilho para avaliar a promoção dos itens condicionados (RF-FIN-03-C, RF-RIS-03) via mudança formal de escopo
- **Custo da Resposta:** R$ 0

---

## Reserva de Contingência Calculada

| ID | Risco | Prob (%) | Impacto (R$) | Valor Esperado |
|----|-------|:---:|---:|---:|
| R-001 | CBs de governança não resolvidas | 60% | R$ 15.000 (custo de replanejamento/atraso) | R$ 9.000 |
| R-002 | Insuficiência orçamentária | 60% | R$ 20.000 (gap médio estimado vs. aprovado) | R$ 12.000 |
| R-003 | Atraso CB-4 no caminho crítico | 50% | R$ 8.000 (retrabalho de replanejamento) | R$ 4.000 |
| R-004 | Viabilidade técnica CB-5 | 50% | R$ 25.000 (desenvolvimento adicional médio) | R$ 12.500 |
| R-005 | Dependência de Thamyris | 45% | R$ 10.000 (atraso/consultoria de apoio) | R$ 4.500 |
| R-006 | Disponibilidade de equipe TVM | 45% | R$ 15.000 (reforço de equipe) | R$ 6.750 |
| R-007 | Benefício não quantificado | 40% | R$ 5.000 (custo de atraso na aprovação de verba) | R$ 2.000 |
| R-008 | Dados parciais tratados como completos | 30% | R$ 20.000 (retrabalho/correção de relatório) | R$ 6.000 |
| **TOTAL** | | | | **R$ 56.750** |

⚠️ **Alerta ao GP/Sponsor**: o valor esperado total de riscos (**R$ 56.750**) é
maior que o orçamento hoje sinalizado como aprovado (R$ 30.000-32.000) e da
mesma ordem de grandeza da própria estimativa de custo do projeto (R$
43.080-69.720, CB-3). Isso não significa que o projeto deva ser cancelado —
significa que a reserva de contingência **não pode ser tratada como
detalhe formal**: os riscos R-001 e R-002 (CRÍTICOS) já cobrem, sozinhos,
R$ 21.000 de valor esperado, quase o valor total do orçamento aprovado.

**Reserva recomendada: R$ 56.750**, a ser tratada como um dado de entrada
para a decisão da CEO/sponsor sobre a reconciliação orçamentária (CB-3) —
não uma reserva "extra" sobre um orçamento já fechado, mas parte do que
precisa ser aprovado antes do início da execução.
