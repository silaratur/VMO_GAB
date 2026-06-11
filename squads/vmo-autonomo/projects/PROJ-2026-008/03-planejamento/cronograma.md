# Planejamento de Prazo — Ajustes Monitores ZMMR_GSI02/03/04 (PROJ-2026-008)
Versão: 1.0 | Data: 2026-06-10 | Elaborado por: Carlos Cronograma (VMO Autônomo)

## Premissas de Estimativa

- Técnica utilizada: **decomposição por pacote de trabalho + analogia** (com base na V1 já entregue pelo SQUAD PM/MM, especialista Jerfesson Fernandes Helmer).
- Início do projeto: **2026-06-17** (segunda-feira seguinte ao prazo das CB-1 a CB-4, previsto para 2026-06-13).
- Pacotes de trabalho ≤ 2 semanas, conforme princípio do Carlos Cronograma.
- Equipe-base: SQUAD PM/MM (1 desenvolvedor ABAP sênior + 1 analista funcional, dedicação parcial — confirmação de disponibilidade real é uma ação pendente, ver Marco M0).
- A execução está organizada nas **3 ondas de priorização** definidas por Felipe Filtro na qualificação:
  - Onda 1 (baixa complexidade — exposição de campos existentes): itens 2, 3, 4, 6, 9, 11, 15
  - Onda 2 (mudanças de regra de negócio): itens 1, 8, 10, 12
  - Onda 3 (alta complexidade — automações/integrações/estorno): itens 5, 7, 13, 14
- **CB-5** (estimativa de esforço por fase pelo SQUAD PM/MM, prazo 2026-06-17) e **CB-6** (especificação funcional formal dos itens 13/14, prazo 2026-06-24) devem ser resolvidas antes do início efetivo das Ondas 1 e 3, respectivamente — este cronograma é uma baseline preliminar e DEVE ser revisado assim que CB-5/CB-6 forem encerradas.
- Item 6 (CB-3, destino GSI03/GSI04 a confirmar) está alocado na Onda 1 com nota de pendência — não bloqueia o início da onda, mas bloqueia a finalização do pacote correspondente.

---

## WBS (Estrutura Analítica do Projeto)

```
1.0 PROJ-2026-008 — Ajustes Monitores ZMMR_GSI02/03/04
  1.1 Gerenciamento do Projeto
    1.1.1 Resolução das Condições Bloqueantes (CB-1 a CB-6, CB-Orçamento)
    1.1.2 Status reports quinzenais (Sara Status)
    1.1.3 Gestão de riscos e issues (Pedro Perigo)
    1.1.4 Encerramento e lições aprendidas

  1.2 Onda 1 — Exposição de Campos (itens 2, 3, 4, 6, 9, 11, 15)
    1.2.1 Especificação funcional Onda 1
      1.2.1.1 Confirmar destino do item 6 (GSI03/GSI04 — CB-3) com Tatiane/João Henrique
      1.2.1.2 Especificação funcional consolidada (itens 2,3,4,6,9,11,15)
    1.2.2 Desenvolvimento ABAP Onda 1
      1.2.2.1 Itens 2,3,4 — colunas ME53N → GSI02 (Vencimento NF, CR, Data Liberação)
      1.2.2.2 Itens 9,11,15 — parâmetro de busca GSI04 + coluna Tipo de Veículo + Grupo deprec.
      1.2.2.3 Item 6 — coluna Data de lançamento (GSI03 e/ou GSI04, conforme CB-3)
    1.2.3 Testes Onda 1
      1.2.3.1 Testes unitários (7 itens)
      1.2.3.2 UAT Onda 1 com Tatiane/João Henrique
    1.2.4 Go-live Onda 1

  1.3 Onda 2 — Mudanças de Regra de Negócio (itens 1, 8, 10, 12)
    1.3.1 Especificação funcional Onda 2
      1.3.1.1 Especificação consolidada (itens 1,8,10,12)
    1.3.2 Desenvolvimento ABAP Onda 2
      1.3.2.1 Item 1 — campo "Classificação" (ME53N + ZMMTR002 + GSI02)
      1.3.2.2 Item 8 — marcação automática de Legalização concluída (GSI03)
      1.3.2.3 Itens 10/12 — flexibilização de "Tipo de Veículo" pós-pedido + alteração de XML incorreto (GSI02/03/04)
    1.3.3 Testes Onda 2
      1.3.3.1 Testes unitários e de regressão (4 itens + Onda 1)
      1.3.3.2 UAT Onda 2
    1.3.4 Go-live Onda 2

  1.4 Onda 3 — Automações, Integrações e Estorno (itens 5, 7, 13, 14)
    1.4.1 Especificação funcional formal Onda 3 (CB-6)
      1.4.1.1 Especificação funcional formal item 13 (estorno fatura/pedido + log)
      1.4.1.2 Especificação funcional formal item 14 (DT. Básica / Vencimento Em na MIRO)
      1.4.1.3 Especificação itens 5 e 7 (integração GRC→GSI03 e PM→AS02)
    1.4.2 Desenvolvimento ABAP Onda 3
      1.4.2.1 Item 7 — sincronização PM → AS02 (Placa do veículo)
      1.4.2.2 Item 5 — detecção MIRO via GRC + flag automática no GSI03
      1.4.2.3 Item 14 — recálculo "DT. Básica"/"Vencimento Em" na MIRO
      1.4.2.4 Item 13 — lógica de estorno fatura/pedido com log de auditoria (BAdI/exit dedicado)
    1.4.3 Testes Onda 3
      1.4.3.1 Testes unitários e de integração (4 itens)
      1.4.3.2 Plano de testes dedicado para itens 13/14 (cenários de borda: estorno parcial, MIRO já paga)
      1.4.3.3 UAT Onda 3
    1.4.4 Go-live Onda 3

  1.5 Encerramento
    1.5.1 Consolidação de lições aprendidas (V1 → V2)
    1.5.2 Aceite formal do solicitante (Tatiane Dias de Moraes)
    1.5.3 Repasse de documentação para sustentação (SQUAD PM/MM)
```

## Dicionário da WBS (resumido)

| ID | Entregável | Critério de Conclusão |
|----|------------|------------------------|
| 1.1.1 | CBs resolvidas | CB-1 a CB-6 e CB-Orçamento com status "resolvida" registrado em status report |
| 1.2.1.1 | Confirmação item 6 (CB-3) | Resposta formal de Tatiane/João Henrique sobre GSI03/GSI04/ambos |
| 1.2.3.2 | UAT Onda 1 aprovado | 7/7 itens (2,3,4,6,9,11,15) aprovados pelo solicitante |
| 1.3.3.2 | UAT Onda 2 aprovado | 4/4 itens (1,8,10,12) aprovados, sem regressão na Onda 1 |
| 1.4.1.1 / 1.4.1.2 | Especificações formais 13/14 aprovadas (CB-6) | Documento de especificação funcional + plano de testes assinado pelo Especialista Funcional e SQUAD PM/MM |
| 1.4.3.2 | Plano de testes itens 13/14 executado | 100% dos cenários de borda (estorno parcial, MIRO já paga, fatura→pedido) com resultado PASS |
| 1.4.4 | Go-live Onda 3 | Itens 5,7,13,14 em produção sem incidente crítico em 5 dias úteis |
| 1.5.2 | Aceite formal | E-mail/documento de aceite de Tatiane Dias de Moraes cobrindo os 15 itens |

---

## Cronograma Detalhado

### Fase 1.1 — Gerenciamento do Projeto (transversal)
| ID | Atividade | Início | Fim | Dur. | Dependência | Responsável | ⭐ |
|----|-----------|--------|-----|------|-------------|-------------|-----|
| 1.1.1 | Resolução das CBs (1-6 + Orçamento) | 2026-06-10 | 2026-06-24 | 10d | - | GP VMO + Tatiane/João Henrique + Projetos DTI | ⭐ |
| 1.1.2 | Status reports quinzenais | 2026-06-17 | 2026-09-25 | contínuo | 1.1.1 | Sara Status | - |
| 1.1.3 | Gestão de riscos e issues | 2026-06-17 | 2026-09-25 | contínuo | 1.1.1 | Pedro Perigo / GP | - |

### Onda 1 — Exposição de Campos (2026-06-17 – 2026-07-15)
| ID | Atividade | Início | Fim | Dur. | Dependência | Responsável | ⭐ |
|----|-----------|--------|-----|------|-------------|-------------|-----|
| 1.2.1.1 | Confirmar destino item 6 (CB-3) | 2026-06-17 | 2026-06-19 | 3d | 1.1.1 | GP VMO / Tatiane | ⭐ |
| 1.2.1.2 | Especificação funcional Onda 1 | 2026-06-17 | 2026-06-24 | 6d | 1.1.1 | SQUAD PM/MM | ⭐ |
| 1.2.2.1 | Dev itens 2,3,4 (colunas GSI02) | 2026-06-25 | 2026-07-03 | 7d | 1.2.1.2 | SQUAD PM/MM (ABAP) | ⭐ |
| 1.2.2.2 | Dev itens 9,11,15 (GSI04/GSI02) | 2026-06-25 | 2026-07-03 | 7d | 1.2.1.2 | SQUAD PM/MM (ABAP) | - |
| 1.2.2.3 | Dev item 6 (coluna Data lançamento) | 2026-06-25 | 2026-07-01 | 5d | 1.2.1.1, 1.2.1.2 | SQUAD PM/MM (ABAP) | - |
| 1.2.3.1 | Testes unitários Onda 1 | 2026-07-04 | 2026-07-08 | 3d | 1.2.2.1, 1.2.2.2, 1.2.2.3 | SQUAD PM/MM (QA) | ⭐ |
| 1.2.3.2 | UAT Onda 1 | 2026-07-09 | 2026-07-13 | 3d | 1.2.3.1 | Tatiane / João Henrique | ⭐ |
| 1.2.4 | Go-live Onda 1 | 2026-07-14 | 2026-07-15 | 2d | 1.2.3.2 | SQUAD PM/MM | ⭐ |

### Onda 2 — Mudanças de Regra de Negócio (2026-07-16 – 2026-08-12)
| ID | Atividade | Início | Fim | Dur. | Dependência | Responsável | ⭐ |
|----|-----------|--------|-----|------|-------------|-------------|-----|
| 1.3.1.1 | Especificação funcional Onda 2 | 2026-07-16 | 2026-07-22 | 5d | 1.2.4 | SQUAD PM/MM | ⭐ |
| 1.3.2.1 | Dev item 1 (campo Classificação) | 2026-07-23 | 2026-07-31 | 7d | 1.3.1.1 | SQUAD PM/MM (ABAP) | ⭐ |
| 1.3.2.2 | Dev item 8 (legalização automática) | 2026-07-23 | 2026-07-29 | 5d | 1.3.1.1 | SQUAD PM/MM (ABAP) | - |
| 1.3.2.3 | Dev itens 10/12 (Tipo de Veículo / XML) | 2026-07-23 | 2026-08-03 | 8d | 1.3.1.1 | SQUAD PM/MM (ABAP) | ⭐ |
| 1.3.3.1 | Testes unitários e regressão Onda 2 | 2026-08-04 | 2026-08-06 | 3d | 1.3.2.1, 1.3.2.2, 1.3.2.3 | SQUAD PM/MM (QA) | ⭐ |
| 1.3.3.2 | UAT Onda 2 | 2026-08-07 | 2026-08-10 | 2d | 1.3.3.1 | Tatiane / João Henrique | ⭐ |
| 1.3.4 | Go-live Onda 2 | 2026-08-11 | 2026-08-12 | 2d | 1.3.3.2 | SQUAD PM/MM | ⭐ |

### Onda 3 — Automações, Integrações e Estorno (2026-08-13 – 2026-09-11)
| ID | Atividade | Início | Fim | Dur. | Dependência | Responsável | ⭐ |
|----|-----------|--------|-----|------|-------------|-------------|-----|
| 1.4.1.1 | Especificação formal item 13 (estorno) — CB-6 | 2026-06-17 | 2026-06-24 | 6d | 1.1.1 | Especialista Funcional + SQUAD PM/MM | ⭐ |
| 1.4.1.2 | Especificação formal item 14 (MIRO) — CB-6 | 2026-06-17 | 2026-06-24 | 6d | 1.1.1 | Especialista Funcional + SQUAD PM/MM | ⭐ |
| 1.4.1.3 | Especificação itens 5 e 7 (integrações) | 2026-08-13 | 2026-08-19 | 5d | 1.3.4 | SQUAD PM/MM | ⭐ |
| 1.4.2.1 | Dev item 7 (PM → AS02, Placa do veículo) | 2026-08-20 | 2026-08-28 | 7d | 1.4.1.3 | SQUAD PM/MM (ABAP) | - |
| 1.4.2.2 | Dev item 5 (MIRO via GRC → GSI03) | 2026-08-20 | 2026-09-02 | 10d | 1.4.1.3 | SQUAD PM/MM (ABAP) | ⭐ |
| 1.4.2.3 | Dev item 14 (DT. Básica / Vencimento Em) | 2026-08-20 | 2026-08-31 | 8d | 1.4.1.2 (CB-6) | SQUAD PM/MM (ABAP) | ⭐ |
| 1.4.2.4 | Dev item 13 (estorno + log auditoria) | 2026-08-20 | 2026-09-04 | 12d | 1.4.1.1 (CB-6) | SQUAD PM/MM (ABAP) | ⭐ |
| 1.4.3.1 | Testes unitários e integração Onda 3 | 2026-09-05 | 2026-09-07 | 3d | 1.4.2.1–1.4.2.4 | SQUAD PM/MM (QA) | ⭐ |
| 1.4.3.2 | Plano de testes dedicado itens 13/14 (bordas) | 2026-09-08 | 2026-09-09 | 2d | 1.4.3.1 | SQUAD PM/MM (QA) + Especialista Funcional | ⭐ |
| 1.4.3.3 | UAT Onda 3 | 2026-09-10 | 2026-09-11 | 2d | 1.4.3.2 | Tatiane / João Henrique | ⭐ |
| 1.4.4 | Go-live Onda 3 | 2026-09-12 | 2026-09-12 | 1d | 1.4.3.3 | SQUAD PM/MM | ⭐ |

### Encerramento (2026-09-13 – 2026-09-25)
| ID | Atividade | Início | Fim | Dur. | Dependência | Responsável | ⭐ |
|----|-----------|--------|-----|------|-------------|-------------|-----|
| 1.5.1 | Consolidação de lições aprendidas | 2026-09-13 | 2026-09-17 | 3d | 1.4.4 | GP VMO + SQUAD PM/MM | ⭐ |
| 1.5.2 | Aceite formal do solicitante | 2026-09-18 | 2026-09-22 | 3d | 1.5.1 | Tatiane Dias de Moraes | ⭐ |
| 1.5.3 | Repasse de documentação p/ sustentação | 2026-09-23 | 2026-09-25 | 3d | 1.5.2 | SQUAD PM/MM | ⭐ |

---

## Marcos Principais

| Marco | Data | Critério |
|-------|------|----------|
| M0 — Kick-off / CBs resolvidas | 2026-06-24 | CB-1 a CB-6 e CB-Orçamento com status "resolvida" ou "mitigada" |
| M1 — Go-live Onda 1 (campos) | 2026-07-15 | Itens 2,3,4,6,9,11,15 em produção, UAT aprovado |
| M2 — Go-live Onda 2 (regras de negócio) | 2026-08-12 | Itens 1,8,10,12 em produção, sem regressão na Onda 1 |
| M3 — Especificações formais 13/14 aprovadas (CB-6) | 2026-06-24 | Documento de especificação + plano de testes assinado |
| M4 — Go-live Onda 3 (automações/estorno) | 2026-09-12 | Itens 5,7,13,14 em produção, plano de testes de borda 100% PASS |
| M5 — Encerramento do projeto | 2026-09-25 | Aceite formal de Tatiane + repasse à sustentação concluído |

## Caminho Crítico

```
1.1.1 (Resolução CBs) → 1.4.1.1/1.4.1.2 (Especificação CB-6, em paralelo)
                       → 1.2.1.2 (Espec. Onda 1) → 1.2.2.1 (Dev itens 2,3,4)
                       → 1.2.3.1 (Testes) → 1.2.3.2 (UAT) → 1.2.4 (Go-live Onda 1)
                       → 1.3.1.1 (Espec. Onda 2) → 1.3.2.3 (Dev itens 10/12)
                       → 1.3.3.1 (Testes) → 1.3.3.2 (UAT) → 1.3.4 (Go-live Onda 2)
                       → 1.4.1.3 (Espec. itens 5/7) → 1.4.2.4 (Dev item 13 — estorno, 12d)
                       → 1.4.3.1 → 1.4.3.2 (Plano de testes 13/14) → 1.4.3.3 (UAT) → 1.4.4 (Go-live Onda 3)
                       → 1.5.1 → 1.5.2 → 1.5.3 (Encerramento)
```

Folga total do caminho crítico: 0 dias. O item de maior risco de atraso é **1.4.2.4 (Dev item 13 — estorno, 12 dias)**, o de maior complexidade lógica do escopo conforme apontado por Felipe Filtro.

## Buffer de Contingência

| Item | Prazo | Observação |
|------|-------|------------|
| Baseline sem buffer (Início 2026-06-17 → Fim 2026-09-25) | ~14,5 semanas | Conclusão do Encerramento (1.5.3) |
| Buffer de gestão (15%) | +2,2 semanas (~15 dias corridos) | Reserva centralizada, gerenciada pelo GP VMO — não distribuída entre atividades |
| Conclusão com buffer | 2026-10-10 | — |
| Deadline declarado no TAP | 2026-09-30 | ⚠️ **Risco de prazo:** a baseline sem buffer (2026-09-25) está dentro do prazo do TAP, mas a conclusão **com buffer aplicado** (2026-10-10) ultrapassa em ~10 dias o prazo declarado de 2026-09-30. Recomenda-se: (a) revisar este cronograma assim que CB-5 (estimativa de esforço do SQUAD PM/MM) for resolvida, podendo confirmar ou comprimir as durações estimadas por analogia; ou (b) negociar com o sponsor um ajuste do prazo-alvo do TAP para 2026-10-10, preservando o buffer de 15% como reserva de gestão real. |

---

## Observações Finais (Carlos Cronograma)

- Este cronograma é uma **baseline preliminar baseada em estimativa por analogia** com a V1 já entregue pelo SQUAD PM/MM — não substitui CB-5 (estimativa de esforço por fase pelo próprio squad), que deve ser usada para refinar as durações acima até 2026-06-17.
- As especificações formais dos itens 13 e 14 (CB-6) foram posicionadas **em paralelo com a resolução das demais CBs** (1.1.1), e não no início da Onda 3, porque seu prazo de governança (2026-06-24) é anterior ao início real do desenvolvimento da Onda 3 (2026-08-20) — isso evita que a especificação formal vire gargalo do caminho crítico mais adiante.
- O item 6 (CB-3) está na Onda 1, mas seu pacote de desenvolvimento (1.2.2.3) depende da confirmação do destino (GSI03/GSI04/ambos) em até 2 dias úteis após o kick-off — caso a resposta não chegue a tempo, recomenda-se mover o item 6 para a Onda 2 sem impacto no caminho crítico.
- Nenhum pacote de trabalho excede 12 dias úteis (item 1.4.2.4); todos os demais estão dentro do limite de 2 semanas (10 dias úteis).
