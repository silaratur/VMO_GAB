---
task: "Criar Plano de Resposta a Riscos"
order: 2
input:
  - lista_riscos: "Registro de riscos da tarefa anterior com scores e priorização"
output:
  - plano_riscos: "Plano completo de resposta a riscos com estratégias, responsáveis e reserva de contingência"
---

# Criar Plano de Resposta a Riscos

Desenvolve o plano de resposta para cada risco identificado, definindo estratégia (Evitar/Transferir/Mitigar/Aceitar), ações concretas, gatilho de acionamento, responsável, prazo e reserva de contingência.

## Process

1. **Selecionar estratégia por risco**: Para riscos CRÍTICOS e ALTOS, preferir Evitar ou Mitigar. Para MÉDIOS, avaliar custo-benefício entre Mitigar e Aceitar. Para BAIXOS, geralmente Aceitar com monitoramento.
2. **Definir ações de resposta**: Para cada risco com estratégia Evitar/Transferir/Mitigar, definir 1-3 ações concretas com responsável e prazo.
3. **Definir trigger (gatilho)**: Para todos os riscos CRÍTICOS e ALTOS, definir o sinal observável que indica que o risco está se materializando.
4. **Calcular reserva de contingência**: Somatório de (probabilidade × impacto financeiro estimado) para todos os riscos identificados.
5. **Definir plano de contingência**: Para riscos Aceitar e como backup para Mitigar, definir o que fazer se o risco se materializar.

## Output Format

```markdown
# PLANO DE RESPOSTA A RISCOS — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD

## Plano por Risco

### R-001 — [Descrição Breve] — [NÍVEL]
- **Estratégia:** [Evitar / Transferir / Mitigar / Aceitar]
- **Gatilho:** [sinal observável de materialização]
- **Ações de Resposta:**
  1. [ação concreta] — Responsável: [nome] — Prazo: [data ou período]
- **Plano de Contingência:** [o que fazer se o risco se materializar]
- **Custo da Resposta:** R$ [estimativa ou "sem custo adicional"]

## Reserva de Contingência Calculada

| ID | Risco | Prob (%) | Impacto (R$) | Valor Esperado |
|----|-------|----------|--------------|----------------|
| R-001 | [risco] | [%] | R$ [valor] | R$ [P×I] |
| TOTAL | | | | R$ [soma] |

Reserva recomendada: R$ [valor] ([N]% de incremento sobre o total do projeto)
```

## Output Example

```markdown
# PLANO DE RESPOSTA A RISCOS — SRF
Versão: 1.0 | Data: 2026-04-16

## Plano por Risco

### R-001 — Conflito de Recursos com Projeto SAP — CRÍTICO
- **Estratégia:** Evitar (resolução antes do início do projeto)
- **Gatilho:** Disponibilidade real da equipe TI cair abaixo de 40% em qualquer semana do cronograma crítico
- **Ações de Resposta:**
  1. Obter comprometimento formal de dedicação de 2 analistas sênior TI — Responsável: Sponsor (CIO) — Prazo: 2026-04-25
  2. Criar plano de escalonamento para substituição se analista for redirecionado — Responsável: GP — Prazo: 2026-05-01
  3. Renegociar timeline do projeto SAP para garantir que fases críticas não coincidam — Responsável: CIO — Prazo: 2026-04-30
- **Plano de Contingência:** Contratar recurso externo especializado SAP por R$ 25.000/mês para cobertura das atividades críticas
- **Custo da Resposta:** R$ 0 (ações de negociação interna) / R$ 25.000 se contingência ativada

### R-002 — Complexidade da API SAP — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** POC de integração SAP requer mais de 12 dias (vs. estimados 8 dias)
- **Ações de Resposta:**
  1. Realizar POC de integração na Fase 1 (semana 3-4) — Responsável: TI SAP — Prazo: 2026-05-28
  2. Mapear APIs SAP disponíveis (REST vs. BAPI vs. RFC) antes do design — Responsável: Analista TI — Prazo: 2026-05-08
- **Plano de Contingência:** Usar middleware comercial de integração SAP (ex: Dell Boomi) — custo adicional estimado R$ 30.000/ano
- **Custo da Resposta:** R$ 0 / R$ 30.000 se contingência ativada

### R-003 — Resistência dos Fornecedores — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Mais de 2 fornecedores recusam participação após comunicação inicial
- **Ações de Resposta:**
  1. Comunicar benefícios para fornecedores (visibilidade mútua, SLA mais justo) — Responsável: Procurement — Prazo: 2026-09-01
  2. Oferecer suporte técnico gratuito para onboarding — Responsável: TI — Prazo: go-live
- **Plano de Contingência:** Incluir exigência de rastreamento no contrato de fornecimento na próxima renovação
- **Custo da Resposta:** R$ 5.000 (material de comunicação e suporte)

### R-006 — Atraso na Aprovação da ERF — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Solicitante não aprova ERF até 3 dias úteis após envio para revisão
- **Ações de Resposta:**
  1. Agendar sessão de revisão da ERF com solicitante antes de envio final — Responsável: GP — Prazo: 2026-05-15
  2. Incluir checkpoint de aprovação no plano do projeto com deadline claro — Responsável: GP — Prazo: 2026-05-21
- **Plano de Contingência:** Iniciar desenvolvimento de RF Must Have com menor ambiguidade enquanto ERF aguarda aprovação formal
- **Custo da Resposta:** R$ 0

## Reserva de Contingência Calculada

| ID | Risco | Prob (%) | Impacto (R$) | Valor Esperado |
|----|-------|----------|--------------|----------------|
| R-001 | Conflito recursos SAP | 70% | R$ 50.000 | R$ 35.000 |
| R-002 | Complexidade API SAP | 50% | R$ 35.000 | R$ 17.500 |
| R-003 | Resistência fornecedores | 40% | R$ 20.000 | R$ 8.000 |
| R-004 | Custo cloud acima estimado | 25% | R$ 15.000 | R$ 3.750 |
| R-005 | Requisitos LGPD adicionais | 20% | R$ 25.000 | R$ 5.000 |
| R-006 | Atraso aprovação ERF | 40% | R$ 10.000 | R$ 4.000 |
| R-007 | Mudanças regulatórias | 10% | R$ 30.000 | R$ 3.000 |
| **TOTAL** | | | | **R$ 76.250** |

Reserva recomendada: R$ 56.000 (já incluída no TAP, representa 16,7% do custo do projeto — ligeiramente acima do valor esperado calculado de R$ 76.250; ajustar se aprovado)
```

## Quality Criteria

- [ ] Estratégia de resposta definida para todos os riscos do registro
- [ ] Todos os riscos CRÍTICOS e ALTOS têm gatilho definido
- [ ] Ações de resposta têm responsável e prazo
- [ ] Plano de contingência definido para todos os riscos Aceitar e CRÍTICO
- [ ] Reserva de contingência calculada com valor esperado
- [ ] Custo das ações de resposta estimado

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Algum risco CRÍTICO ou ALTO não tem gatilho (trigger) definido
2. A reserva de contingência calculada está ausente ou baseia-se apenas em percentual fixo sem cálculo de valor esperado
