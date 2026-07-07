# Planejamento de Prazo — PROJ-2026-008
Implantação/Expansão do TVM para Fluxo de Caixa, Controle Orçamentário e
Rastreabilidade de Riscos (Grupo Águia Branca)

Autor: Carlos Cronograma (Planejador de Prazo, VMO Autônomo)
Data: 2026-07-07 | Versão: 1.0 | Status: RASCUNHO (6 CBs do TAP ainda em aberto)

⚠️ **Nota metodológica**: como a data de kick-off ainda não está confirmada
(depende de CB-1/CB-2 — governança — e da designação do GP), este cronograma
usa **T0 = data de kick-off** como referência relativa, em vez de datas de
calendário fixas — mesma lógica já aplicada no TAP e no Work Request. Datas
de calendário reais serão calculadas assim que T0 for confirmado.

⚠️ **Premissa de equipe NÃO confirmada**: este cronograma assume dedicação
parcial de ~30h úteis/semana da equipe técnica TVM (mesma premissa usada no
TAP para o cálculo de "T + 7 semanas úteis"). A disponibilidade real da
equipe não foi confirmada por nenhuma fonte (TAP, Premissa 5) — este é um
risco explícito, não uma confirmação.

---

## WBS (Estrutura Analítica do Projeto)

```
1.0 PROJ-2026-008 — TVM Fluxo de Caixa/Suprimentos/Riscos
  1.1 Gerenciamento do Projeto
    1.1.1 Documentação de iniciação (TAP, PM Canvas, Plano Geral, ERF, WR) — CONCLUÍDO
    1.1.2 Resolução de Condições Bloqueantes (CB-1 a CB-6)
      1.1.2.1 Evidência documental do sponsor (CB-1)
      1.1.2.2 Aprovação de Diretoria + Gerente de TI (CB-2)
      1.1.2.3 Reconciliação orçamentária (CB-3)
      1.1.2.4 Sessão de continuação com Alessandra (CB-4)
      1.1.2.5 Confirmação técnica dos 5 itens incertos (CB-5)
      1.1.2.6 Quantificação de benefício financeiro (CB-6)
    1.1.3 Status reports periódicos (quinzenal, a partir do kick-off)
    1.1.4 Gestão de riscos e issues (contínuo)
    1.1.5 Encerramento e lições aprendidas

  1.2 Fase 1 — Levantamento de Requisitos Detalhado
    1.2.1 Validação da ERF com pontos focais das 3 frentes
      1.2.1.1 Workshop de validação — Financeiro (Alessandra) — inclui fechamento de CB-4
      1.2.1.2 Workshop de validação — Suprimentos (Wellington Gonçalves)
      1.2.1.3 Workshop de validação — Riscos/Desempenho (Thamyris)
    1.2.2 Confirmação técnica com equipe TVM
      1.2.2.1 Sessão técnica: viabilidade dos 5 itens incertos (CB-5) e PA-01/03/05/06/07/09
      1.2.2.2 Fechamento da ERF v2.0 (pós-confirmações)

  1.3 Fase 2 — Desenvolvimento/Configuração
    1.3.1 Frente Financeiro
      1.3.1.1 Configuração de fluxo de caixa (ingressos/egressos/LAIR) — RF-FIN-01, 02, 04
      1.3.1.2 Classificação manual-assistida de receita por tipo de negócio — RF-FIN-03
      1.3.1.3 Relatório consolidado automático para diretoria — RF-FIN-05
    1.3.2 Frente Suprimentos
      1.3.2.1 Painel de baseline orçamentário — RF-SUP-01
      1.3.2.2 Projeção de pagamentos parcelados 30/60/90 dias — RF-SUP-02
      1.3.2.3 Alertas automáticos de consumo (70%/85%) — RF-SUP-03
      1.3.2.4 Relatório básico de consumo por fornecedor — RF-SUP-04
    1.3.3 Frente Riscos/Desempenho
      1.3.3.1 Previsão de caixa a 90 dias — RF-RIS-01
      1.3.3.2 Rastreabilidade de custos (nível SAP atual) — RF-RIS-02
    1.3.4 Transversal — Segurança e Auditoria
      1.3.4.1 Controle de acesso por perfil/área — RF-TRA-05, RNF-SEG-01
      1.3.4.2 Trilha de auditoria de lançamentos — RF-TRA-06, RNF-SEG-02
      1.3.4.3 Criptografia em trânsito/repouso — RNF-SEG-03

  1.4 Fase 3 — Testes e Homologação
    1.4.1 Testes internos (unitário/integração) — TI/equipe TVM
    1.4.2 UAT Financeiro (Alessandra)
    1.4.3 UAT Suprimentos (Wellington Gonçalves)
    1.4.4 UAT Riscos/Desempenho (Thamyris)
    1.4.5 Consolidação de correções pós-UAT e aprovação final

  1.5 Fase 4 — Go-live e Suporte Inicial
    1.5.1 Treinamento das 3 áreas
    1.5.2 Cutover (migração Excel → TVM) por frente
    1.5.3 Acompanhamento pós-go-live (mínimo 1 ciclo mensal completo — Critério de Sucesso #2 do TAP)

  1.6 Itens Fora do Escopo Atual (não incluídos nesta WBS)
    Projeções analíticas avançadas (RF-TRA-01), Dashboards/BI (RF-TRA-02),
    Integração Atenas (RF-TRA-03), Permissões ampliadas (RF-TRA-04),
    Segregação automática via SAP (RF-FIN-03-C), Visão analítica avançada de
    compras (RF-SUP-04-C), Rastreabilidade a NF (RF-RIS-03) — todos
    condicionados a CB-5 e a mudança formal de escopo (ver TAP §Fora do
    Escopo e WR §4.2). Não recebem estimativa de esforço nesta WBS.
```

### Dicionário da WBS (resumido)

| ID | Entregável | Critério de Conclusão |
|----|------------|------------------------|
| 1.1.2 | CBs resolvidas | Evidência documental para CB-1/CB-2 anexada; CB-3 reconciliado com valor único aprovado; CB-4 concluída; CB-5 confirmada tecnicamente; CB-6 com ao menos 1 benefício quantificado |
| 1.2.2.2 | ERF v2.0 | Documento assinado pelos 3 pontos focais + Cássio (líder técnico) |
| 1.3.1.1 | Fluxo de caixa configurado | RF-FIN-01/02/04 passam nos critérios de aceitação da ERF sem exceção |
| 1.3.4.2 | Trilha de auditoria ativa | 5 edições de teste geram 5 registros de auditoria correspondentes (critério RF-TRA-06) |
| 1.4.5 | UAT aprovado | 100% dos Must Have (22 itens) aprovados pelos 3 pontos focais |
| 1.5.3 | Pós-go-live validado | 1 ciclo mensal completo de previsão de 90 dias operando sem intervenção manual (Critério de Sucesso #2 do TAP) |

---

## Cronograma Detalhado (relativo a T0 = kick-off, semanas úteis)

Premissa de capacidade: ~30h úteis/semana de dedicação parcial da equipe (mesma
premissa do TAP). Estimativas de esforço herdadas do sizing.md (Rafael
Requisito), técnica de decomposição por pacote de trabalho.

### Fase 1 — Levantamento de Requisitos Detalhado (Semana 1–2)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | Caminho Crítico |
|----|-----------|--------|-----|---------|--------------|-------------|:---:|
| 1.2.1.1 | Workshop validação Financeiro (fecha CB-4) | T0 | T0+3d | 3d | Kick-off | Alessandra + PMO | ⭐ |
| 1.2.1.2 | Workshop validação Suprimentos | T0 | T0+2d | 2d | Kick-off | Wellington Gonçalves | - |
| 1.2.1.3 | Workshop validação Riscos/Desempenho | T0 | T0+2d | 2d | Kick-off | Thamyris | - |
| 1.2.2.1 | Sessão técnica CB-5 (5 itens incertos) | T0+3d | T0+8d | 5d | 1.2.1.1 | Cássio + equipe TVM | ⭐ |
| 1.2.2.2 | Fechamento ERF v2.0 | T0+8d | T0+10d | 2d | 1.2.2.1 | Rafael Requisito | ⭐ |

### Fase 2 — Desenvolvimento/Configuração (Semana 3–8)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | Caminho Crítico |
|----|-----------|--------|-----|---------|--------------|-------------|:---:|
| 1.3.1.1 | Config. fluxo de caixa (RF-FIN-01/02/04) | T0+10d | T0+20d | 10d | 1.2.2.2 | Equipe TVM | ⭐ |
| 1.3.1.2 | Classificação de receita (RF-FIN-03) | T0+20d | T0+25d | 5d | 1.3.1.1 | Equipe TVM | - |
| 1.3.1.3 | Relatório consolidado diretoria (RF-FIN-05) | T0+25d | T0+30d | 5d | 1.3.1.2 | Equipe TVM | ⭐ |
| 1.3.2.1 | Painel baseline Suprimentos (RF-SUP-01) | T0+10d | T0+18d | 8d | 1.2.2.2 | Equipe TVM | - |
| 1.3.2.2 | Projeção 30/60/90 (RF-SUP-02) | T0+18d | T0+23d | 5d | 1.3.2.1 | Equipe TVM | - |
| 1.3.2.3 | Alertas 70%/85% (RF-SUP-03) | T0+23d | T0+28d | 5d | 1.3.2.2 | Equipe TVM | - |
| 1.3.2.4 | Relatório de consumo (RF-SUP-04) | T0+28d | T0+31d | 3d | 1.3.2.3 | Equipe TVM | - |
| 1.3.3.1 | Previsão de caixa 90 dias (RF-RIS-01) | T0+10d | T0+17d | 7d | 1.2.2.2 | Equipe TVM | - |
| 1.3.3.2 | Rastreabilidade nível SAP (RF-RIS-02) | T0+17d | T0+24d | 7d | 1.3.3.1 | Equipe TVM | - |
| 1.3.4.1 | Controle de acesso por área (RF-TRA-05) | T0+10d | T0+15d | 5d | 1.2.2.2 | Equipe TVM | - |
| 1.3.4.2 | Trilha de auditoria (RF-TRA-06) | T0+15d | T0+20d | 5d | 1.3.4.1 | Equipe TVM | ⭐ |
| 1.3.4.3 | Criptografia trânsito/repouso (RNF-SEG-03) | T0+20d | T0+23d | 3d | 1.3.4.1 | Equipe TVM | - |
| — | Integração/consolidação das 3 frentes | T0+31d | T0+38d | 7d | Todos acima | Equipe TVM + Cássio | ⭐ |

### Fase 3 — Testes e Homologação (Semana 9)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | Caminho Crítico |
|----|-----------|--------|-----|---------|--------------|-------------|:---:|
| 1.4.1 | Testes internos (unitário/integração) | T0+38d | T0+43d | 5d | Integração | Equipe TVM | ⭐ |
| 1.4.2 | UAT Financeiro | T0+43d | T0+46d | 3d | 1.4.1 | Alessandra | ⭐ |
| 1.4.3 | UAT Suprimentos | T0+43d | T0+45d | 2d | 1.4.1 | Wellington Gonçalves | - |
| 1.4.4 | UAT Riscos/Desempenho | T0+43d | T0+45d | 2d | 1.4.1 | Thamyris | - |
| 1.4.5 | Consolidação e correções pós-UAT | T0+46d | T0+50d | 4d | 1.4.2, 1.4.3, 1.4.4 | Equipe TVM | ⭐ |

### Fase 4 — Go-live e Suporte Inicial (Semana 10–11+)

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | Caminho Crítico |
|----|-----------|--------|-----|---------|--------------|-------------|:---:|
| 1.5.1 | Treinamento das 3 áreas | T0+50d | T0+55d | 5d | 1.4.5 | PMO + Equipe TVM | ⭐ |
| 1.5.2 | Cutover (Excel → TVM) por frente | T0+55d | T0+58d | 3d | 1.5.1 | Equipe TVM | ⭐ |
| 1.5.3 | Acompanhamento pós-go-live (1 ciclo mensal) | T0+58d | T0+88d | 30d | 1.5.2 | GP + PMO | ⭐ (marco de aceite) |

---

## Marcos Principais

| Marco | Data (relativa a T0) | Critério |
|-------|------------------------|----------|
| M0 — Kick-off | T0 | CB-1/CB-2 resolvidas ou formalmente aceitas como risco pelo GP; GP designado; equipe mobilizada |
| M1 — ERF v2.0 fechada | T0 + 10 dias úteis | CB-4 e CB-5 resolvidas; ERF assinada pelos 3 pontos focais + Cássio |
| M2 — Desenvolvimento completo | T0 + 38 dias úteis | 100% dos 22 Must Have (RF+RNF) configurados/desenvolvidos |
| M3 — UAT aprovado | T0 + 50 dias úteis | 100% dos Must Have aprovados nos UAT das 3 frentes |
| M4 — Go-live | T0 + 58 dias úteis | Cutover realizado nas 3 frentes; Excel deixa de ser fonte primária (Critério de Sucesso #1 do TAP) |
| M5 — Aceite pós-go-live | T0 + 88 dias úteis | 1 ciclo mensal completo de previsão de 90 dias validado (Critério de Sucesso #2 do TAP) |
| M6 — Encerramento | T0 + 90 dias úteis | Lições aprendidas documentadas; aceite formal do sponsor |

---

## Caminho Crítico

```
1.2.1.1 (Workshop Financeiro) → 1.2.2.1 (Sessão técnica CB-5) → 1.2.2.2 (ERF v2.0)
  → 1.3.1.1 (Config. fluxo de caixa) → 1.3.1.2 → 1.3.1.3 (Relatório diretoria)
  → [Integração das 3 frentes] → 1.4.1 (Testes internos) → 1.4.2 (UAT Financeiro)
  → 1.4.5 (Correções pós-UAT) → 1.5.1 (Treinamento) → 1.5.2 (Cutover)
  → 1.5.3 (Acompanhamento pós-go-live) → M6 (Encerramento)
```
Folga total do caminho crítico: 0 dias. A frente Financeiro domina o caminho
crítico porque (a) depende do fechamento de CB-4 antes de sequer iniciar a
validação de requisitos, e (b) o relatório consolidado à diretoria (RF-FIN-05)
é o entregável mais dependente de decisões ainda em aberto (CB-4, PA-04).
Suprimentos e Riscos/Desempenho têm folga em relação a este caminho.

---

## Buffer de Contingência

| Item | Prazo | Observação |
|------|-------|------------|
| Baseline sem buffer (Fases 1-4, até M4 Go-live) | T0 + 58 dias úteis (~11,6 semanas) | Cenário do piso do sizing (206h), premissa de 30h úteis/semana |
| Buffer de gestão (15%) | + 8,7 dias úteis (~1,7 semana) | Reserva centralizada, gerenciada pelo GP — não distribuída nas atividades individuais |
| **Data-alvo com buffer (até Go-live, M4)** | **T0 + ~67 dias úteis (~13,4 semanas)** | |
| Acompanhamento pós-go-live (M5) + Encerramento (M6) | + 30 dias corridos | Fora do caminho de desenvolvimento; não recebe buffer adicional (já é período de observação) |

⚠️ **Divergência a reconciliar com o TAP**: o TAP registra a data-alvo
provisória como **"T + 7 semanas úteis"**, calculada apenas sobre o **piso**
do sizing (206h ÷ 30h/semana ≈ 7 semanas) e **sem considerar** o buffer de
gestão de 15% nem a fase de acompanhamento pós-go-live (que o próprio
Critério de Sucesso #2 do TAP exige — 1 ciclo mensal completo). Este
cronograma detalhado, aplicando a mesma premissa de capacidade mas incluindo
buffer e período de observação pós-go-live, chega a **T0 + ~13,4 semanas até
o Go-live** (M4) e **T0 + ~90 dias úteis até o Encerramento** (M6) —
significativamente mais longo que os "7 semanas" do TAP. Recomendo que o TAP
seja atualizado para refletir esta data-alvo mais realista antes da
aprovação final do pacote de documentação (Vera Veredito / Gabriel
Governança), ou que a divergência seja registrada como ressalva explícita
até lá. Não alterei o TAP diretamente — meu papel é planejar o prazo, não
reescrever o TAP (isso é escopo da Diana Documento).

---

## Riscos de Prazo Identificados (a detalhar por Pedro Perigo no Step 18)

1. **Dependência do caminho crítico na frente Financeiro**: se CB-4 (sessão com Alessandra) atrasar, todo o caminho crítico desliza — nenhuma atividade de desenvolvimento da frente Financeiro pode começar antes do fechamento de CB-4/M1.
2. **Disponibilidade da equipe técnica TVM não confirmada**: a premissa de 30h úteis/semana é estimativa, não confirmação — se a disponibilidade real for menor, todas as durações deste cronograma se estendem proporcionalmente.
3. **CB-5 pode alterar o escopo de desenvolvimento**: se a sessão técnica (1.2.2.1) revelar que algum dos 5 itens incertos é inviável no TVM sem desenvolvimento adicional significativo, a Fase 2 precisa ser replanejada — este cronograma assume que os itens condicionados permanecem fora de escopo (não incorporados).
