# PLANO DE RISCOS — PROJ-2026-001
## Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados
**Versão:** 1.0 | **Data:** 2026-04-03 | **Gerado por:** Pedro Perigo — Analista de Riscos VMO

---

## Registro de Riscos

| ID | Categoria | Risco | Probabilidade (1–5) | Impacto (1–5) | Score | Nível | Estratégia |
|----|-----------|-------|--------------------:|--------------|------:|-------|------------|
| R01 | Técnico | A parametrização via ZFI0057 revelar limitação que exige desenvolvimento ABAP, expandindo custo e prazo além do aprovado | 2 | 5 | 10 | **ALTO** | Mitigar |
| R02 | Prazo | Indisponibilidade do ambiente QAS na janela planejada, impedindo execução dos testes integrados no prazo | 3 | 4 | 12 | **ALTO** | Mitigar |
| R03 | Stakeholders | Indisponibilidade ou resistência do Diretor Financeiro para treinamento e validação antes da go-live | 3 | 4 | 12 | **ALTO** | Mitigar |
| R04 | Prazo | Processo de change management do cliente (janelas de transporte PRD) incompatível com o cronograma, postergando o go-live | 3 | 3 | 9 | **MÉDIO** | Mitigar |
| R05 | Técnico | Identificação de outros aprovadores no fluxo atual impactados pela parametrização, gerando necessidade de redesenho | 2 | 3 | 6 | **MÉDIO** | Mitigar |
| R06 | Financeiro | Custo real do projeto superar o teto de R$ 8.640 por necessidade não prevista (ex.: suporte OSS SAP, horas extras) | 2 | 3 | 6 | **MÉDIO** | Aceitar com contingência |
| R07 | Stakeholders | Resistência dos usuários do fluxo à nova etapa de aprovação, gerando solicitações de bypass ou atraso na adoção | 2 | 2 | 4 | **BAIXO** | Mitigar |

**Escala:** Probabilidade 1=Muito Baixa, 2=Baixa, 3=Média, 4=Alta, 5=Muito Alta | Impacto idem
**Nível:** ALTO (Score ≥ 9), MÉDIO (5–8), BAIXO (≤ 4)

---

## Matriz de Probabilidade × Impacto

```
Impacto →    1       2       3       4       5
           Muito  Baixo   Médio   Alto  Crítico
           Baixo

P=5 Muito Alta  5      10      15      20      25
P=4 Alta        4       8      12  [R02⭐]  [R03⭐]  20
P=3 Média       3       6   [R04][R05]  [R02]  15
P=2 Baixa       2    [R07]   [R05][R06] [R01⭐] 10
P=1 Muito Baixa 1       2       3       4       5
```

**Riscos de nível ALTO (zona vermelha):** R01, R02, R03

---

## Plano de Resposta a Riscos

---

### R01 — Limitação técnica ZFI0057 exigindo ABAP
**Categoria:** Técnico | **Nível:** ALTO | **Estratégia:** Mitigar
**Probabilidade:** 2 (Baixa) | **Impacto:** 5 (Crítico)

**Gatilho (Trigger):**
Equipe Basis confirma, durante o spike técnico (Du 6–10), que a parametrização na ZFI0057 não suporta o novo aprovador sem criação de programa ABAP customizado ou modificação de código SAP.

**Plano de Mitigação:**
- Executar spike técnico detalhado nos Du 6–10 (antes de qualquer comprometimento de prazo com o negócio)
- Validar a parametrização em ambiente DEV como primeiro entregável — não assumir viabilidade sem confirmação técnica
- Consultar notas SAP (OSS) sobre ZFI0057 durante o spike

**Plano de Contingência (se materializado):**
- Escalar imediatamente ao Sponsor com análise de impacto (custo adicional estimado para ABAP, prazo adicional)
- Avaliar alternativa: aprovação manual temporária via SBWP até solução definitiva
- Solicitar revisão formal do TAP com novo orçamento e prazo

**Responsável:** GP + Basis SAP
**Prazo de ação de mitigação:** Du 6–10 (spike técnico obrigatório)

---

### R02 — Indisponibilidade do ambiente QAS
**Categoria:** Prazo | **Nível:** ALTO | **Estratégia:** Mitigar
**Probabilidade:** 3 (Média) | **Impacto:** 4 (Alto)

**Gatilho (Trigger):**
Na Du 25 (5 du antes do transporte planejado para QAS), a equipe Basis confirma que o ambiente QAS está ocupado por outro projeto sem previsão de liberação dentro da janela planejada (Du 31–40).

**Plano de Mitigação:**
- Reservar formalmente janela de QAS durante o planejamento (Du 11–15), com confirmação por e-mail da gestão de ambiente SAP
- Incluir no cronograma folga de 5du no planejamento de testes como absorção de pequenos atrasos
- Mapear projetos concorrentes que usam QAS durante os Du 31–42

**Plano de Contingência (se materializado):**
- Acionar buffer de contingência (Du 52–60) para absorver o atraso
- Se o atraso superar 8du (buffer total), escalar ao Sponsor para revisão de prazo
- Avaliar execução de testes parciais em DEV para reduzir dependência do QAS

**Responsável:** GP
**Prazo de ação de mitigação:** Du 11–15 (reserva formal de janela QAS)

---

### R03 — Indisponibilidade ou resistência do Diretor Financeiro
**Categoria:** Stakeholders | **Nível:** ALTO | **Estratégia:** Mitigar
**Probabilidade:** 3 (Média) | **Impacto:** 4 (Alto)

**Gatilho (Trigger):**
Na Du 37 (3du antes do treinamento planejado), o Diretor Financeiro não confirma disponibilidade para a sessão de treinamento (Du 43–44) ou informa impossibilidade de participação no prazo do projeto.

**Plano de Mitigação:**
- Engajar o Sponsor (o próprio Diretor Financeiro, neste caso) desde o kickoff para comprometimento com o cronograma
- Comunicar formalmente a data de treinamento com 10du de antecedência mínima
- Preparar material de treinamento assíncrono (guia escrito + vídeo tutorial) como alternativa

**Plano de Contingência (se materializado):**
- Disponibilizar treinamento assíncrono (guia + vídeo) para o Diretor realizar no seu tempo
- Colher aceite formal por e-mail após treinamento assíncrono (substitui sessão presencial)
- Se Diretor não aceitar nenhuma modalidade no prazo: escalar ao PMO e ao Comitê de Governança

**Observação:** Este risco tem natureza especial — o Sponsor é o próprio aprovador. Esse duplo papel reduz o risco de resistência, mas pode gerar indisponibilidade por agenda executiva.

**Responsável:** GP
**Prazo de ação de mitigação:** Du 5 (kickoff) e Du 33 (confirmação de agenda)

---

### R04 — Janelas de transporte PRD incompatíveis com o cronograma
**Categoria:** Prazo | **Nível:** MÉDIO | **Estratégia:** Mitigar
**Probabilidade:** 3 (Média) | **Impacto:** 3 (Médio)

**Plano de Mitigação:**
- Mapear calendário de transportes PRD na fase de planejamento (Du 11–15)
- Solicitar janela de transporte com antecedência mínima de 10du (Du 30–32) antes da go-live planejada

**Plano de Contingência:**
- Acionar buffer de contingência para absorver atraso de até 5du
- Se próxima janela disponível > 5du após o planejado, escalar ao Sponsor

**Responsável:** GP + Basis SAP | **Prazo:** Du 11–15

---

### R05 — Outros aprovadores impactados pela parametrização
**Categoria:** Técnico | **Nível:** MÉDIO | **Estratégia:** Mitigar
**Probabilidade:** 2 (Baixa) | **Impacto:** 3 (Médio)

**Plano de Mitigação:**
- Mapear TODOS os aprovadores atuais no fluxo ZFI0057 antes de iniciar a parametrização (Du 6–8)
- Validar com área de negócio o impacto da mudança nos aprovadores existentes

**Plano de Contingência:**
- Se houver aprovadores impactados não mapeados: suspender parametrização e redesenhar fluxo com área de negócio
- Escalar ao Sponsor como mudança de escopo com análise de impacto

**Responsável:** GP + Basis | **Prazo:** Du 6–8

---

### R06 — Custo real supera teto de R$ 8.640
**Categoria:** Financeiro | **Nível:** MÉDIO | **Estratégia:** Aceitar com contingência
**Probabilidade:** 2 (Baixa) | **Impacto:** 3 (Médio)

**Plano de Contingência:**
- Contingência de 20% já incluída no orçamento teto (R$ 8.640)
- Se o custo real tender a superar R$ 7.200 (sinal de esgotamento da contingência), escalar ao Sponsor antes de comprometer o teto
- Se o teto for insuficiente: solicitar orçamento adicional via mudança formal do TAP

**Responsável:** GP | **Prazo:** Monitoramento contínuo

---

### R07 — Resistência dos usuários à nova etapa de aprovação
**Categoria:** Stakeholders | **Nível:** BAIXO | **Estratégia:** Mitigar
**Probabilidade:** 2 (Baixa) | **Impacto:** 2 (Baixo)

**Plano de Mitigação:**
- Comunicar a mudança com antecedência mínima de 5du antes do go-live (Du 47)
- Explicar o motivo da mudança (governança e controle interno) na comunicação
- Disponibilizar contato de suporte para dúvidas no período pós-go-live

**Responsável:** GP | **Prazo:** Du 47

---

## Reserva de Contingência (Valor Esperado)

| ID | Risco | Prob. | Impacto Financeiro Estimado | Valor Esperado |
|----|-------|-------|----------------------------|----------------|
| R01 | Limitação técnica ABAP | 0,20 | R$ 15.000 (est. custo ABAP) | R$ 3.000 |
| R02 | Indisponibilidade QAS | 0,30 | R$ 2.000 (custo de atraso ~5du) | R$ 600 |
| R03 | Indisponibilidade Diretor | 0,30 | R$ 1.500 (custo de atraso ~3du) | R$ 450 |
| R04 | Janelas transporte PRD | 0,30 | R$ 1.000 (custo de atraso ~2du) | R$ 300 |
| R05 | Aprovadores impactados | 0,20 | R$ 3.000 (redesenho do fluxo) | R$ 600 |
| R06 | Custo supera teto | 0,20 | R$ 2.000 (custo adicional típico) | R$ 400 |
| R07 | Resistência usuários | 0,20 | R$ 500 (suporte adicional) | R$ 100 |
| **TOTAL** | | | | **R$ 5.450** |

> **Nota:** A reserva de contingência embutida no orçamento (20% de R$ 7.200 ≈ R$ 1.440) é inferior ao valor esperado calculado (R$ 5.450) devido ao risco R01 (ABAP). O GP deve sinalizar ao Sponsor que R01, se materializado, requer revisão formal do TAP independentemente da reserva existente.

---

## Frequência de Revisão do Registro de Riscos

| Ciclo | Frequência | Responsável |
|-------|------------|-------------|
| Status report quinzenal | A cada 2 semanas | GP |
| Gate review (a cada fase) | Ao final de F2, F3, F4 | GP + Sponsor |
| Monitoramento contínuo ALTO | A cada semana (R01, R02, R03) | GP |

---

*Documento gerado por Pedro Perigo — Analista de Riscos | VMO Autônomo Squad*
*Versão 1.0 — 2026-04-03 — Sujeito a revisão quinzenal durante a execução do projeto*
