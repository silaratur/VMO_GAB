# Relatório de Revisão de Qualidade — DEM-2026-007
Projeto: Implantação DDA SAP — VAB Matriz
Elaborado por: Vera Veredito (VMO Autônomo)
Data: 2026-05-20
Revisão: 1 de 3

---

## Resultado: 🟡 APROVADO COM CONDIÇÕES

## Pontuação Consolidada: 8,30/10

| Documento | Peso | Pontuação | Status |
|-----------|------|-----------|--------|
| TAP | 25% | 8,0/10 | 🟡 Aprovado com condições |
| PM Canvas | 10% | 8,0/10 | ✅ Aprovado |
| ERF | 15% | 9,0/10 | ✅ Aprovado |
| Cronograma | 20% | 8,0/10 | 🟡 Aprovado com condições |
| Plano de Riscos | 15% | 9,0/10 | ✅ Aprovado |
| Framework de KPIs | 10% | 8,0/10 | ✅ Aprovado |
| Status Report | 5% | 8,0/10 | 🟡 Aprovado com condições |
| **CONSOLIDADO** | **100%** | **8,30/10** | **🟡 APROVADO COM CONDIÇÕES** |

> Pontuação ponderada: (8,0×0,25) + (8,0×0,10) + (9,0×0,15) + (8,0×0,20) + (9,0×0,15) + (8,0×0,10) + (8,0×0,05)
> = 2,00 + 0,80 + 1,35 + 1,60 + 1,35 + 0,80 + 0,40 = **8,30/10** ✅ (limiar: 7,0/10)

---

## Pontos Fortes

**PF-1: ERF exemplar para o domínio DDA/SAP**
A especificação de requisitos elaborada pelo Rafael Requisito é sólida: 17 requisitos com ID único,
todos os Must Have com critério de aceitação mensurável e verificável, priorização MoSCoW coerente
com o escopo declarado, e glossário com os 8 termos críticos do domínio (DDA, CNAB 240, FEBAN, CP,
etc.). A rastreabilidade entre RF e critérios de sucesso do TAP está documentada.

**PF-2: Plano de Riscos maduro com CRÍTICO endereçado**
O plano de riscos com 10 riscos em 5 categorias, escala P×I com scores, e plano de resposta detalhado
para os 4 riscos de alto risco e crítico demonstra maturidade. Particularmente bem tratado: R-001
(autorização Holding) tem estratégia MITIGAR + EVITAR com plano de contingência explícito —
isto protege o projeto de seu risco mais grave.

**PF-3: Consistência cross-documentos**
Prazo (30/09/2026), custo (R$0 – R$2.000), escopo (DDA VAB CP x Santander) e stakeholders
(Gladston, Noemia, Lucas, Walace) são consistentes entre TAP, PM Canvas, Cronograma, KPIs e
Status Report. Este é o critério que mais frequentemente falha em revisões e aqui foi respeitado.

**PF-4: WBS e cronograma granulares com buffer explícito**
A WBS com 3 níveis cobre 100% dos entregáveis do TAP. O cronograma identifica o caminho crítico
(habilitação Santander como fator externo crítico), e o buffer de 15% em setembro está explícito
e centralizado — não diluído nas atividades. A estimativa de esforço por fase (130h DTI + 62h
negócio) é um diferencial de transparência.

---

## Avaliação por Documento

---

### TAP — 8,0/10 | 🟡 Aprovado com condições

**Critérios BLOCKING:**
| Critério | Status | Observação |
|----------|--------|-----------|
| Objetivo SMART | ✅ | Específico (DDA VAB CP), Mensurável (100% automação), Temporal (30/09/2026) |
| Sponsor identificado | ⚠️ PARCIAL | Gladston Campos identificado, mas autoridade nível Diretor+ não confirmada (CB-Sponsor aberta) |
| Gerente de Projeto | ⚠️ PARCIAL | "A designar pelo DTI após kick-off" — contextualmente correto para pré-kick-off |
| Escopo dentro/fora | ✅ | 5 itens dentro + 6 fora do escopo definidos explicitamente |
| Critérios de sucesso | ✅ | 4 critérios com métrica e prazo (acima do mínimo de 3) |
| Orçamento aprovado | ✅ | R$0 a R$2.000 com contextualização clara |
| Prazo de conclusão | ✅ | 30/09/2026 definido |

**Critérios de qualidade:**
| Critério | Status |
|----------|--------|
| Justificativa → estratégia | ✅ Programa "Controladoria do Futuro" + precedente GAB |
| ≥ 5 partes interessadas | ✅ 7 stakeholders mapeados |
| ≥ 3 premissas + ≥ 3 restrições | ✅ 6 premissas + 6 restrições |
| ≥ 3 riscos alto nível | ✅ 5 riscos |
| Benefícios quantificados | ⚠️ Qualitativos (100% automação declarado, sem R$ ou horas economizadas) |

**Condições requeridas (TAP):**
- **C-TAP-1:** GP "a designar" — aceito pré-kick-off COMO CONDIÇÃO DE KICK-OFF: o GP deve ser designado antes do M-0 (gate de kick-off). Sem GP designado, o gate de kick-off não será liberado.
- **C-TAP-2:** Sponsor autoridade plena — aceito pré-kick-off, monitorado pela CB-Sponsor. O TAP deve ser revisado com a confirmação do sponsor após resolução da CB-Sponsor.

---

### PM Canvas — 8,0/10 | ✅ Aprovado

**Critérios BLOCKING:**
| Critério | Status | Observação |
|----------|--------|-----------|
| Todos os 9 blocos preenchidos | ✅ | Blocos 1 a 9 presentes e substantivos |
| Consistência interna | ✅ | Prazo/custo/escopo/stakeholders coerentes com TAP |
| Bloco "Por quê?" → estratégia | ✅ | "Automação financeira", "Controladoria do Futuro" |

**Nota:** O PM Canvas em formato tabular markdown cumpre todos os requisitos de conteúdo.

---

### ERF — 9,0/10 | ✅ Aprovado

**Critérios BLOCKING:**
| Critério | Status | Observação |
|----------|--------|-----------|
| MoSCoW priorizado | ✅ | 5 Must / 3 Should / 2 Could / 2 Won't |
| Critério aceitação por Must Have | ✅ | RF001–RF005 todos com critério mensurável |
| ID único por requisito | ✅ | RF001–RF010 + RNF001–005 |
| Rastreabilidade | ✅ | Tabela de rastreabilidade RF → CS do TAP |

**Diferencial positivo:** Os critérios de aceitação dos RFs Must Have são operacionalmente
específicos ("N boletos em um arquivo → N documentos SAP, zero digitação manual") — testáveis
no UAT sem interpretação.

**Observação não-bloqueante:** RF009 e RF010 marcados como Could Have carregam a nota [CB-2].
Após o levantamento técnico (M-1), os itens [CB-2] devem ser revisados e promovidos/confirmados.
Esta revisão não requer nova aprovação de qualificação.

---

### Cronograma — 8,0/10 | 🟡 Aprovado com condições

**Critérios BLOCKING:**
| Critério | Status | Observação |
|----------|--------|-----------|
| WBS ≥ 3 níveis | ✅ | Fases → Grupos → Atividades |
| Pacotes ≤ 2 semanas | ✅ | Maior atividade: 10 dias corridos |
| Marcos mínimos | ✅ | M-0 a M-6 com critério de conclusão |
| Dependências | ✅ | Coluna "Dependência" preenchida |
| Caminho crítico | ✅ | Seção dedicada com sequência identificada |

**Condição requerida (Cronograma):**
- **C-CRON-1:** Responsáveis genéricos ("Recurso DTI", "GP") — aceitável pré-kick-off, mas o
  cronograma deve ser revisado com nomes reais dos responsáveis após designação do GP e do
  recurso técnico DTI (condição de M-0). Esta revisão é parte natural da fase de kick-off.

---

### Plano de Riscos — 9,0/10 | ✅ Aprovado

**Critérios BLOCKING:**
| Critério | Status | Observação |
|----------|--------|-----------|
| ≥ 5 riscos | ✅ | 10 riscos documentados |
| P e I avaliados | ✅ | Escala 1–9 com scores; 1 CRÍTICO, 4 ALTOS, 4 MÉDIOS, 1 BAIXO |
| Estratégia de resposta | ✅ | Mitigar/Evitar/Aceitar por risco |
| Responsável e prazo | ✅ | Por ação de resposta em cada risco |

**Critérios de qualidade:**
| Critério | Status |
|----------|--------|
| ≥ 4 categorias | ✅ Governança, Técnico, Externo, Pessoas, Processo (5) |
| Críticos com contingência | ✅ R-001 CRÍTICO com plano detalhado |
| Triggers definidos | ✅ R-001, R-002, R-003, R-004, R-006, R-008, R-009 |
| Reserva de contingência | ✅ R$2.000 + 38,3 dias valor esperado |

---

### Framework de KPIs — 8,0/10 | ✅ Aprovado

**Critérios BLOCKING:**
| Critério | Status |
|----------|--------|
| CPI e SPI definidos | ✅ Tabela EVM completa com BAC, fórmula e baseline |
| Frequência de medição | ✅ Quinzenal + por evento + pós-go-live |
| Limites de alerta | ✅ Tabela verde/amarelo/vermelho por dimensão |
| Responsável por KPI | ✅ GP, Noemia, DTI FI por KPI |

---

### Status Report — 8,0/10 | 🟡 Aprovado com condições

**Critérios BLOCKING:**
| Critério | Status | Observação |
|----------|--------|-----------|
| Status geral (semáforo) | ✅ | 🟡 ATENÇÃO com breakdown por dimensão |
| Data e período | ✅ | 20/05/2026 — Iniciação |
| Progresso | ⚠️ PARCIAL | "Iniciação concluída" sem % numérico. Contextual para phase 0. |
| Issues abertas | ✅ | CBs e riscos críticos documentados |

**Condição requerida (Status Report):**
- **C-SR-1:** Incluir percentual de conclusão explícito (ex: "Fase de Iniciação: 100% / Projeto
  global: 0% até kick-off"). Aplicar nos próximos reports a partir do M-0.

---

## Bloqueadores Críticos

**Nenhum bloqueador CRÍTICO identificado que impeça o avanço para o gate de kick-off.**

Os dois itens ⚠️ (Sponsor/GP no TAP e responsáveis genéricos no cronograma) são condições
contextuais de pré-kick-off, já documentadas como CBs e condições de gate — não são lacunas
não-gerenciadas. A documentação produzida trata estes itens com transparência adequada.

---

## Condições para Avanço (devem ser atendidas antes ou no M-0)

| # | Condição | Documento | Prazo |
|---|---------|-----------|-------|
| C-TAP-1 | Designar GP e documentar autoridade no TAP | TAP | M-0 (06/06/2026) |
| C-TAP-2 | Atualizar TAP com sponsor Diretor+ (pós CB-Sponsor) | TAP | M-0 |
| C-CRON-1 | Atualizar cronograma com responsáveis reais | Cronograma | M-0 |
| C-SR-1 | Adicionar % de conclusão global nos próximos status reports | Status Report | M-0+ |

---

## Recomendações para a Fase de Execução

1. **Prioridade absoluta:** R-001 (autorização Holding) deve ser tratado como risco de projeto
   ativo, não apenas documentado. O GP deve confirmar custo zero formalmente antes de qualquer
   gasto, mesmo que mínimo. Este é o risco com maior potencial de bloquear todo o projeto.

2. **M-1 é o marco mais crítico do projeto (além do M-0):** O levantamento técnico (CB-2)
   determina se o projeto permanece como Melhoria Evolutiva ou precisa ser reclassificado como
   PROJETO. Alocar o recurso mais experiente da DTI para esta fase.

3. **Iniciar habilitação Santander imediatamente no kick-off (Fase 3.1):** O processo bancário
   é o único fator externo do caminho crítico. Qualquer atraso aqui consome diretamente o buffer.

4. **ERF deve ser validada por Noemia antes do UAT:** A pesquisa de satisfação da iniciação
   deve ser enviada junto com o pacote TAP para validação do escopo com o solicitante.

---

## Assinatura do Revisor

- Revisado por: Vera Veredito — Revisora de Qualidade VMO Autônomo
- Data: 2026-05-20
- Versão do pacote revisado: v1.0
- Revisão: 1 de 3
- Próxima revisão: após gate de kick-off (M-0) com TAP e cronograma atualizados
