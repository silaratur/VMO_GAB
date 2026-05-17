# ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
**ID:** DEM-2026-006
**Data:** 2026-05-17
**Analista:** Felipe Filtro (VMO Autônomo)
**Versão das regras:** v2 — 10 critérios / 100 pts / Classificação ERP

---

## Resumo da Demanda

Jadson, Gestor da Área de Inovação, solicita o desenvolvimento de uma plataforma web própria para substituir a ferramenta SaaS terceira atualmente utilizada para gestão de ideias de inovação corporativa — que custa entre R$80–90 mil/ano e impõe limitações de escala. A nova plataforma deve contemplar 6 módulos: cadastro de ideias, campanhas e desafios, fluxo de aprovação por gestores, mini gestão de projetos, mensuração de ganhos e dashboard de monitoramento. Prazo: dezembro de 2026, vinculado ao lançamento do Prêmio Inovação de janeiro de 2027.

---

## Critérios de Qualificação

### Valor da Demanda

**1. Alinhamento Estratégico — 7/10**
O programa de inovação corporativa é uma iniciativa estratégica ativa do grupo, com evento institucional âncora (Prêmio Inovação, jan/2027) que demonstra comprometimento da liderança. A substituição da plataforma terceira por solução própria alinha-se ao objetivo de redução de custos operacionais e ganho de autonomia tecnológica. Confiança: MÉDIA — o alinhamento existe e é real, mas não está documentado em OKR específico com meta mensurável para este ciclo. A ausência de OKR explícito impede nota máxima.

**2. Viabilidade Técnica — 6/10**
Plataforma web com 6 módulos sem integrações externas é tecnicamente viável com tecnologia convencional — o escopo declarado não exige integração com ERP ou outros sistemas (confirmado pelo solicitante: "A princípio não"). O que reduz a nota é o que ainda não foi definido: modelo de desenvolvimento (interno/externo/misto), infraestrutura de hospedagem e detalhamento do fluxo de aprovação (quem aprova, quantas etapas, critérios). Esses gaps técnicos são resolvíveis na fase de requisitos, mas representam risco de escopo hoje. Confiança: MÉDIA.

**3. Retorno sobre Investimento — 8/10**
O caso financeiro é sólido e simples: eliminação de R$80–90k/ano em licença SaaS com investimento de magnitude similar (~R$85k estimado). Payback esperado de 12 meses sobre o custo direto de licenciamento. Benefício adicional não quantificado: capacidade de expandir o programa para todos os colaboradores sem custo incremental por usuário. Confiança: MÉDIA — a estimativa de custo é do solicitante, sem validação de fornecedor ou TI. O risco é o desenvolvimento custar mais que o esperado e estender o payback.

**4. Urgência — 7/10**
O prazo de dezembro de 2026 está ancorado em evento institucional concreto — o Prêmio Inovação de janeiro de 2027, que usa intensamente a plataforma. Atrasar o projeto significa mais um ciclo completo de licença SaaS (+R$85k) e comprometer o lançamento do prêmio. A urgência é real e tem data. O que impede nota 9–10: o grupo não está em situação de crise — a plataforma atual funciona, o programa segue operando. É urgência de oportunidade, não de ruptura.

**5. Maturidade da Demanda — 5/10**
O problema está bem definido (custo + limitação de escala) e as 6 funcionalidades de alto nível foram descritas com clareza pelo solicitante. Porém, a demanda apresenta 9 lacunas documentadas pela Iara, das quais 2 são críticas (L01: sponsor, L02: orçamento) e 5 são de impacto médio para a especificação (L04: usuários, L05: atributos, L06: fluxo de aprovação, L07: infraestrutura, L08: modelo de desenvolvimento). A maturidade é suficiente para avançar com condições, mas não para iniciar a fase de requisitos sem resolver ao menos as lacunas L01 a L06.

**6. Disponibilidade de Recursos — 4/10**
Este é o critério mais fraco da qualificação. Sponsor executivo não identificado. Orçamento formal não aprovado. Modelo de execução (interno/externo) indefinido. Sem sponsor, nenhuma decisão sobre orçamento pode ser tomada. Sem modelo de execução, não é possível estimar prazos reais nem contratar fornecedor. A expectativa do solicitante (~R$80–90k) é um ponto de partida válido, mas não uma aprovação. A nota 4 reflete a sinalização positiva do solicitante sem qualquer formalização.

---

### Complexidade de Execução

**7. Esforço Estimado — 9/10**
Desenvolvimento do zero com 6 módulos funcionais distintos. Estimativa técnica preliminar:
- Módulos M1-M2 (cadastro + campanhas): ~120h
- Módulo M3 (fluxo de aprovação): ~100h — complexidade de workflow
- Módulo M4 (mini gestão de projetos): ~80h
- Módulo M5 (mensuração de ganhos): ~60h
- Módulo M6 (dashboard + visões por perfil): ~80h
- Infraestrutura, autenticação (SSO), testes e implantação: ~160h
- **Total estimado: 600h+** — muito acima do limiar de 160h.

Mesmo em cenário conservador de subestimativa de 30%, o esforço mínimo realista é 420h. Impossível tratar como melhoria do time de sustentação.

**8. Impacto Organizacional — 8/10**
Impacto em todas as divisões do grupo como usuários finais (Comércio, Passageiros, Logística e demais). Gestores de área de todas as divisões são diretamente afetados como aprovadores no fluxo. Mudança de processo relevante: colaboradores passam de uma plataforma terceira para uma nova, exigindo comunicação, treinamento de administradores e migração de dados históricos. O solicitante minimiza o impacto ("só muda o link"), mas a mudança de ferramenta corporativa em múltiplas divisões exige gestão de mudança organizacional — mesmo que a transição seja tecnicamente transparente.

**9. Governança Necessária — 8/10**
Projeto de desenvolvimento de plataforma com 6 meses de duração, prazo vinculado a evento institucional, múltiplas partes interessadas (todas as divisões), processo de seleção de fornecedor (se externo) e migração de dados. Exige cronograma formal, gestão de stakeholders, controle de riscos, aprovação de entregas por marcos e relatórios periódicos. Não pode ser gerido autonomamente pelo time técnico sem estrutura de projeto. A ausência de sponsor e orçamento aprovados adiciona risco de governança ao projeto — não reduz a necessidade, aumenta.

**10. Impacto Regulatório ou Financeiro — 5/10**
Impacto financeiro direto e mensurável: eliminação de R$80–90k/ano em licença SaaS. O solicitante confirmou explicitamente que não há requisito legal ou regulatório. Sem risco de compliance, auditoria ou obrigação fiscal derivada da demanda. A nota 5 reflete o impacto financeiro real (redução de custo que afeta o demonstrativo) sem o componente regulatório — que seria necessário para pontuação mais alta.

---

## Resultado

**PONTUAÇÃO TOTAL: 67/100 (67%)**

> Composição: Valor da Demanda 37/60 (62%) · Complexidade de Execução 30/40 (75%)

---

**CLASSIFICAÇÃO: PROJETO**

Critérios de complexidade 7–10 confirmam inequivocamente a necessidade de gestão formal:
- Esforço estimado (9/10) ≥ 7 ✅ — 600h+ de desenvolvimento
- Impacto Organizacional (8/10) ≥ 7 ✅ — todas as divisões + gestores de área
- Governança Necessária (8/10) ≥ 7 ✅ — cronograma, stakeholders, marcos formais

3 dos 4 critérios de complexidade pontuam acima de 7. O escopo de 6 módulos e 600h+ de esforço estimado torna inviável qualquer tratamento como melhoria. Não se trata de ajuste funcional sobre sistema existente — é desenvolvimento de nova plataforma corporativa. Encaminhar para o pipeline VMO completo: TAP → ERF → Cronograma → Riscos → KPIs → Work Request.

> **Nota comparativa:** na qualificação anterior (versão v1 das regras — 6 critérios /30), esta demanda pontuou 21/30 (70%) — APROVADO COM CONDIÇÕES. Na versão v2 (10 critérios /100), a pontuação de 67% reflete com maior precisão as lacunas reais: especialmente a disponibilidade de recursos (4/10) que antes ficava diluída no critério genérico de "recursos". O diagnóstico é o mesmo — aprovado com condições — mas agora fundamentado em mais dimensões e com maior granularidade.

---

**DECISÃO: APROVADO COM CONDIÇÕES**

*Score 67% está na faixa 50–74%. As condições bloqueantes (sponsor e orçamento) devem ser resolvidas antes da assinatura do TAP. A aprovação é justificada pelo ROI sólido (8/10), complexidade confirmada como projeto (3/4 critérios ≥7) e urgência com prazo institucional concreto.*

---

## Condições Bloqueantes

| # | Condição | Por que bloqueia | Prazo |
|---|----------|-----------------|-------|
| **CB-01** | **Sponsor executivo de nível Diretor ou superior** — não identificado. Jadson (Gestor de Área) não tem autoridade para aprovar o investimento nem assinar o TAP. | Sem sponsor, nenhuma decisão orçamentária ou de prioridade institucional tem respaldo formal. | 2026-06-13 |
| **CB-02** | **Orçamento aprovado formalmente** — a expectativa do solicitante (~R$80–90k) é referência, não aprovação. Precisa de levantamento de custo real validado e aprovação financeira. | Sem orçamento aprovado, o projeto não pode ser contratado nem iniciado. | 2026-06-20 |

## Condições Desejáveis (não bloqueantes, mas recomendadas antes da ERF)

- **L04** — Levantar número de usuários ativos na plataforma atual e projeção de expansão (impacta arquitetura e custo)
- **L06** — Mapear o fluxo de aprovação em detalhe (quantas etapas, quem aprova, critérios) antes do levantamento de requisitos
- **L07** — Definir política de infraestrutura/hospedagem (cloud, data center do grupo ou misto)
- **L08** — Decidir modelo de execução (TI interna / fornecedor externo / misto) antes de emitir o Work Request

---

## Proposta de Valor

> "O projeto Plataforma Própria de Inovação, com investimento estimado em ~R$85k, eliminará o custo de licença SaaS de R$80–90k/ano e desbloqueará a expansão do programa de inovação para todos os colaboradores do grupo sem custo adicional por usuário. Com payback projetado em 12 meses e alinhamento à estratégia de inovação corporativa e ao Prêmio Inovação de janeiro/2027, o projeto transforma uma despesa recorrente de licenciamento em um ativo próprio e customizável do grupo."

---

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Identificar e confirmar sponsor executivo (Diretor+) | Jadson | 2026-06-13 |
| Levantar custo real de desenvolvimento (TI ou fornecedor) | VMO + TI/Compras | 2026-06-13 |
| Aprovação formal do orçamento pelo sponsor | Sponsor a designar | 2026-06-20 |
| Mapear fluxo de aprovação detalhado (L06) e número de usuários (L04) | Jadson + TI | 2026-06-13 |
| Definir modelo de execução: interno / externo / misto | Sponsor + Jadson | 2026-06-13 |
| Iniciar elaboração do TAP após resolução das CBs | VMO | 2026-06-24 |

---

*Parecer elaborado por Felipe Filtro — Analista de Qualificação VMO Autônomo*
*Regras aplicadas: v2 — 10 critérios / escala 1-10 / máx 100 pts / Classificação PROJETO/MELHORIA*
