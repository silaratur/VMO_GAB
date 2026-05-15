# Plano de Riscos Detalhado
## PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação
## Grupo Águia Branca

**Versão:** 1.0
**Data:** 2026-05-14
**Responsável:** Pedro Perigo — Especialista em Gestão de Riscos, VMO Autônomo
**Referências:** `v2/documentacao-base.md` | `v3/requisitos.md` | `v4/cronograma.md`

---

## 1. Metodologia de Gestão de Riscos

### 1.1 Escala de Probabilidade

| Nível | Descrição | Critério |
|---|---|---|
| 1 — Muito Baixa | Improvável de ocorrer | < 10% de chance |
| 2 — Baixa | Pouco provável | 10%–30% de chance |
| 3 — Média | Possível | 30%–50% de chance |
| 4 — Alta | Provável | 50%–70% de chance |
| 5 — Muito Alta | Quase certa | > 70% de chance |

### 1.2 Escala de Impacto

| Nível | Descrição | Efeito sobre o Projeto |
|---|---|---|
| 1 — Muito Baixo | Mínimo | Sem impacto em prazo, custo ou escopo |
| 2 — Baixo | Menor | Atraso < 3 dias úteis ou custo < R$ 2.000 |
| 3 — Médio | Moderado | Atraso 3–10 dias úteis ou custo R$ 2.000–10.000 |
| 4 — Alto | Significativo | Atraso 10–20 dias úteis ou custo R$ 10.000–20.000 |
| 5 — Crítico | Catastrófico | Inviabiliza o prazo de go-live (30/11/2026) ou estoura orçamento total |

### 1.3 Matriz de Severidade (Probabilidade × Impacto)

| P \ I | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 🟡 | 10 🟠 | 15 🔴 | 20 🔴 | 25 🔴 |
| **4** | 4 🟢 | 8 🟡 | 12 🟠 | 16 🔴 | 20 🔴 |
| **3** | 3 🟢 | 6 🟡 | 9 🟡 | 12 🟠 | 15 🔴 |
| **2** | 2 🟢 | 4 🟢 | 6 🟡 | 8 🟡 | 10 🟠 |
| **1** | 1 🟢 | 2 🟢 | 3 🟢 | 4 🟢 | 5 🟡 |

**Legenda:** 🟢 Baixo (1–4) | 🟡 Médio (5–9) | 🟠 Alto (10–14) | 🔴 Crítico (15–25)

### 1.4 Estratégias de Resposta

- **Eliminar:** Remover a causa raiz do risco
- **Mitigar:** Reduzir probabilidade e/ou impacto
- **Transferir:** Repassar a responsabilidade do impacto (seguros, contratos)
- **Aceitar:** Aceitar as consequências, com ou sem reserva de contingência
- **Explorar (oportunidade):** Maximizar a probabilidade de ocorrência de eventos positivos

### 1.5 Reserva de Contingência

| Item | Valor |
|---|---|
| Orçamento base do projeto | R$ 75.000,00 |
| Reserva de contingência (20% — já prevista no TAP) | R$ 15.000,00 |
| **Orçamento total aprovável** | **R$ 90.000,00** |
| Alocação inicial da reserva para riscos identificados (ver seção 3) | R$ 10.500,00 |
| Reserva residual (margem não alocada) | R$ 4.500,00 |

> A reserva de contingência é gerenciada pelo GP. Uso acima de R$ 5.000 em um único evento requer aprovação formal do sponsor.

---

## 2. Registro de Riscos — Visão Geral

| Código | Categoria | Risco | Prob. | Impacto | Score | Severidade |
|---|---|---|---|---|---|---|
| RSK-01 | Governança | Sponsor não identificado / orçamento não aprovado a tempo | 4 | 5 | **20** | 🔴 Crítico |
| RSK-02 | Prazo | Atraso no início da execução (pós kick-off) | 3 | 5 | **15** | 🔴 Crítico |
| RSK-03 | Escopo | Scope creep — requisições de novas funcionalidades durante execução | 4 | 4 | **16** | 🔴 Crítico |
| RSK-04 | Técnico | Prazo insuficiente para desenvolvimento completo com equipe a definir | 3 | 4 | **12** | 🟠 Alto |
| RSK-05 | Recursos | Indisponibilidade de recurso-chave durante execução (Dev / Tech Lead) | 2 | 4 | **8** | 🟡 Médio |
| RSK-06 | Infraestrutura | Ambiente de produção (TI do Grupo) não provisionado a tempo | 3 | 3 | **9** | 🟡 Médio |
| RSK-07 | Adoção | Baixa adoção pelos colaboradores após go-live | 2 | 3 | **6** | 🟡 Médio |
| RSK-08 | Técnico | Performance/carga insatisfatória (< 500 usuários simultâneos) | 2 | 4 | **8** | 🟡 Médio |
| RSK-09 | Segurança | Vulnerabilidades de segurança identificadas em auditoria ou produção | 2 | 5 | **10** | 🟠 Alto |
| RSK-10 | Fornecedor | Rescisão do contrato da plataforma terceirizada com multa ou cláusula de fidelidade | 2 | 3 | **6** | 🟡 Médio |
| RSK-11 | Qualidade | Volume de defeitos no UAT acima da capacidade de correção antes do go-live | 3 | 4 | **12** | 🟠 Alto |
| RSK-12 | Dependência externa | Jadson (ponto focal) indisponível em período crítico de validação | 2 | 3 | **6** | 🟡 Médio |

---

## 3. Registro Detalhado de Riscos

---

### RSK-01 — Sponsor não identificado / Orçamento não aprovado a tempo

| Campo | Detalhe |
|---|---|
| **Categoria** | Governança |
| **Probabilidade** | 4 — Alta |
| **Impacto** | 5 — Crítico |
| **Score P×I** | **20 — 🔴 Crítico** |
| **Descrição** | O sponsor executivo não foi identificado até a data deste documento (condição bloqueante). O projeto não pode iniciar a fase de execução sem sponsor designado e orçamento formalmente aprovado. Se não resolvido até 13/06/2026, o prazo de go-live (30/11/2026) fica em risco imediato. |
| **Gatilho** | 13/06/2026 sem confirmação do sponsor e aprovação do orçamento |
| **Estratégia** | **Eliminar** — escalar ativamente até resolução |
| **Plano de Resposta** | 1. GP e PMO VMO escalam para liderança do Grupo Águia Branca imediatamente após emissão do TAP; 2. Prazo-limite: 13/06/2026; 3. Se não resolvido: projeto suspenso formalmente, com comunicado ao comitê de portfólio e reunião extraordinária convocada pelo PMO |
| **Reserva de Contingência** | R$ 0 (risco de governança — não monetizável; resolução é burocrática) |
| **Dono do Risco** | GP / PMO VMO + Jadson |
| **Revisão** | Quinzenal até 13/06/2026; semanal a partir de 01/06 |

---

### RSK-02 — Atraso no início da execução

| Campo | Detalhe |
|---|---|
| **Categoria** | Prazo |
| **Probabilidade** | 3 — Média |
| **Impacto** | 5 — Crítico |
| **Score P×I** | **15 — 🔴 Crítico** |
| **Descrição** | O kick-off depende da confirmação do sponsor e da aprovação do orçamento (RSK-01). Cada semana de atraso no kick-off comprime diretamente o caminho crítico, que já opera com margem de apenas 10 dias úteis. |
| **Gatilho** | Kick-off adiado além de 23/06/2026 |
| **Estratégia** | **Mitigar** — iniciar atividades preparatórias em paralelo antes do kick-off formal |
| **Plano de Resposta** | 1. Iniciar levantamento complementar de requisitos e prototipação UX assim que sponsor for confirmado, sem aguardar aprovação formal do orçamento (risco calculado); 2. Manter equipe de desenvolvimento em standby a partir de 01/06 para início imediato; 3. Se atraso >2 semanas: rever escopo com Jadson e sponsor — priorizar M1+M2+M3+M4 e deslocar M5+M6 para fase 2 pós go-live |
| **Reserva de Contingência** | R$ 0 (risco de prazo — resposta operacional, não financeira) |
| **Dono do Risco** | GP |
| **Revisão** | Semanal até kick-off |

---

### RSK-03 — Scope creep

| Campo | Detalhe |
|---|---|
| **Categoria** | Escopo |
| **Probabilidade** | 4 — Alta |
| **Impacto** | 4 — Alto |
| **Score P×I** | **16 — 🔴 Crítico** |
| **Descrição** | Com a documentação base concluída, há risco elevado de que Jadson e o time de inovação solicitem funcionalidades adicionais durante o desenvolvimento (gamificação, integração com RH, IA para triagem, mobile). Cada nova funcionalidade não planejada consome capacidade da equipe e comprime o prazo. |
| **Gatilho** | Qualquer solicitação de nova funcionalidade sem passagem pelo processo formal de mudanças |
| **Estratégia** | **Mitigar** — processo formal rigoroso de gestão de mudanças |
| **Plano de Resposta** | 1. Apresentar e validar o escopo formalmente no kick-off com assinatura do TAP por Jadson e sponsor; 2. Todo pedido de nova funcionalidade passa pelo formulário de Solicitação de Mudança (SM) com análise de impacto em prazo e custo; 3. Mudanças com impacto > 3 dias úteis ou > R$ 3.000 requerem aprovação do sponsor; 4. GP reporta no status quinzenal toda SM aberta, status e decisão |
| **Reserva de Contingência** | R$ 3.000 (absorção de pequenas mudanças inevitáveis) |
| **Dono do Risco** | GP |
| **Revisão** | Quinzenal — integrado ao relatório de status |

---

### RSK-04 — Prazo insuficiente para desenvolvimento completo

| Campo | Detalhe |
|---|---|
| **Categoria** | Técnico |
| **Probabilidade** | 3 — Média |
| **Impacto** | 4 — Alto |
| **Score P×I** | **12 — 🟠 Alto** |
| **Descrição** | Com 5,5 meses de execução efetiva e 6 módulos funcionais a desenvolver, o cronograma é apertado. A equipe ainda não está definida (modelo de execução pendente), aumentando a incerteza das estimativas. |
| **Gatilho** | Velocidade de entrega no Sprint 1 abaixo de 80% do previsto |
| **Estratégia** | **Mitigar** — abordagem MVP + entregas incrementais |
| **Plano de Resposta** | 1. Entrega em sprints com demos ao final de cada módulo — problemas de velocidade detectados cedo; 2. Priorizar M1+M2+M4 (caminho crítico) sobre M3+M6 (com folga); 3. Se velocidade no Sprint 1 for < 70% do previsto: convocar reunião com sponsor para negociar escopo ou adicionar recurso (usando reserva); 4. Plano B: M5 e M6 entregues em fase 2 pós go-live (janeiro/2027), desde que aprovado formalmente |
| **Reserva de Contingência** | R$ 5.000 (contratação de recurso adicional por 2–3 semanas em caso de aceleração necessária) |
| **Dono do Risco** | GP + Tech Lead |
| **Revisão** | Semanal — monitorar velocidade de entrega por sprint |

---

### RSK-05 — Indisponibilidade de recurso-chave

| Campo | Detalhe |
|---|---|
| **Categoria** | Recursos |
| **Probabilidade** | 2 — Baixa |
| **Impacto** | 4 — Alto |
| **Score P×I** | **8 — 🟡 Médio** |
| **Descrição** | Perda de disponibilidade de desenvolvedor sênior ou tech lead por afastamento, rescisão ou realocação pode atrasar múltiplos módulos simultaneamente, dado o tamanho reduzido da equipe prevista. |
| **Gatilho** | Afastamento > 5 dias úteis de qualquer membro crítico da equipe |
| **Estratégia** | **Mitigar** — redundância de conhecimento e contratos com cláusula de substituição |
| **Plano de Resposta** | 1. Todo conhecimento técnico documentado em repositório compartilhado — sem concentração de conhecimento; 2. Contratos com fornecedores externos devem incluir cláusula de substituição em até 5 dias úteis; 3. Tech Lead faz pair programming com desenvolvedores para garantir conhecimento distribuído; 4. Se afastamento confirmado: GP aciona substituição imediata e avalia impacto no cronograma |
| **Reserva de Contingência** | R$ 2.500 (custo de onboarding de substituto) |
| **Dono do Risco** | GP |
| **Revisão** | Mensal |

---

### RSK-06 — Ambiente de produção não provisionado a tempo

| Campo | Detalhe |
|---|---|
| **Categoria** | Infraestrutura |
| **Probabilidade** | 3 — Média |
| **Impacto** | 3 — Médio |
| **Score P×I** | **9 — 🟡 Médio** |
| **Descrição** | O provisionamento do ambiente de produção depende da área de TI do Grupo Águia Branca, fora do controle direto da VMO. Atraso no ambiente impede o deploy e pode comprometer o go-live. |
| **Gatilho** | Ambiente de produção não disponível até 10/11/2026 |
| **Estratégia** | **Mitigar** — solicitar provisionamento antecipado |
| **Plano de Resposta** | 1. Solicitar especificações e provisionamento do ambiente no kick-off (junho/2026); 2. Validar disponibilidade do ambiente de homologação em setembro/2026 — 6 semanas antes da necessidade; 3. Validar ambiente de produção até 07/11/2026 (antes do início do UAT); 4. Plano de contingência: provisionar ambiente em nuvem temporário (AWS/Azure) às custas do projeto se TI não entregar a tempo |
| **Reserva de Contingência** | R$ 0 (TI do Grupo é responsável — sem custo ao projeto; contingência nuvem seria cobrada da reserva de contingência geral) |
| **Dono do Risco** | GP + Analista TI do Grupo |
| **Revisão** | Mensal; quinzenal a partir de outubro |

---

### RSK-07 — Baixa adoção pelos colaboradores após go-live

| Campo | Detalhe |
|---|---|
| **Categoria** | Adoção |
| **Probabilidade** | 2 — Baixa |
| **Impacto** | 3 — Médio |
| **Score P×I** | **6 — 🟡 Médio** |
| **Descrição** | Plataforma nova pode ter adoção abaixo do esperado por resistência à mudança, confusão com a troca de sistema ou falta de comunicação prévia. Isso compromete o ROI esperado (volume de ideias) e o sucesso do Prêmio Inovação 2027. |
| **Gatilho** | Taxa de cadastro de ideias nos primeiros 30 dias pós-go-live < 50% da média histórica da plataforma atual |
| **Estratégia** | **Mitigar** — comunicação e engajamento antecipado |
| **Plano de Resposta** | 1. Comunicar a mudança para todos os colaboradores pelo menos 4 semanas antes do go-live (coordenado por Jadson e time de inovação); 2. Transição transparente: comunicar que apenas o link muda; 3. Realizar demos da nova plataforma para os gestores de área antes do go-live; 4. Monitorar adoção nas 4 primeiras semanas e acionar time de inovação para campanha de sensibilização se necessário |
| **Reserva de Contingência** | R$ 0 (responsabilidade de comunicação é do cliente) |
| **Dono do Risco** | Jadson (solicitante) |
| **Revisão** | Único check após 30 dias do go-live |

---

### RSK-08 — Performance/carga insatisfatória

| Campo | Detalhe |
|---|---|
| **Categoria** | Técnico |
| **Probabilidade** | 2 — Baixa |
| **Impacto** | 4 — Alto |
| **Score P×I** | **8 — 🟡 Médio** |
| **Descrição** | O sistema deve suportar 500 usuários simultâneos com tempo de resposta < 3 segundos. Se a arquitetura ou infraestrutura forem subdimensionadas, a plataforma pode apresentar degradação em picos de uso — especialmente durante o lançamento do Prêmio Inovação (jan/2027). |
| **Gatilho** | Testes de carga (fase 4.2 do cronograma) com tempo de resposta > 3s para 95% das requisições |
| **Estratégia** | **Mitigar** — arquitetura escalável desde o design inicial |
| **Plano de Resposta** | 1. Arquiteto define solução com escalabilidade horizontal desde o início (Docker/containerização); 2. Testes de carga realizados em homologação em outubro/novembro antes do UAT; 3. Se testes falharem: otimização de queries e cache antes do go-live; 4. Solicitar ambiente de produção com capacidade reservada para escalar se necessário |
| **Reserva de Contingência** | R$ 0 (otimização é atividade técnica da equipe; capacidade de infraestrutura é responsabilidade da TI do Grupo) |
| **Dono do Risco** | Tech Lead |
| **Revisão** | Único check em outubro nos testes sistêmicos |

---

### RSK-09 — Vulnerabilidades de segurança

| Campo | Detalhe |
|---|---|
| **Categoria** | Segurança |
| **Probabilidade** | 2 — Baixa |
| **Impacto** | 5 — Crítico |
| **Score P×I** | **10 — 🟠 Alto** |
| **Descrição** | Uma plataforma web corporativa com dados de inovação estratégica é alvo potencial. Vulnerabilidades como XSS, CSRF, SQL injection, autenticação fraca ou dados expostos podem comprometer a confidencialidade de ideias de inovação e afetar a reputação do programa. |
| **Gatilho** | Vulnerabilidade crítica (OWASP Top 10) identificada nos testes de segurança |
| **Estratégia** | **Mitigar** — security by design e testes dedicados |
| **Plano de Resposta** | 1. Requisitos de segurança definidos na ERF (HTTPS obrigatório, bcrypt para senhas, RBAC, proteção contra XSS/CSRF/SQLi); 2. Code review com foco em segurança em cada sprint; 3. Teste de segurança dedicado na fase 4.3 antes do UAT; 4. Se vulnerabilidade crítica encontrada: bloquear UAT até correção; 5. Não fazer go-live com vulnerabilidade P1 de segurança em aberto |
| **Reserva de Contingência** | R$ 0 (correção é atividade técnica da equipe) |
| **Dono do Risco** | Tech Lead + QA |
| **Revisão** | Contínuo — a cada sprint e dedicado na fase 4.3 |

---

### RSK-10 — Cláusula de fidelidade ou multa na rescisão do contrato da plataforma terceirizada

| Campo | Detalhe |
|---|---|
| **Categoria** | Fornecedor |
| **Probabilidade** | 2 — Baixa |
| **Impacto** | 3 — Médio |
| **Score P×I** | **6 — 🟡 Médio** |
| **Descrição** | O modelo de ROI do projeto assume rescisão imediata do contrato com a plataforma terceirizada no go-live da solução proprietária. Se houver multa contratual ou cláusula de fidelidade, o payback de 12 meses pode ser comprometido. |
| **Gatilho** | Identificação de multa ou prazo mínimo de fidelidade acima de 3 meses no contrato atual |
| **Estratégia** | **Mitigar** — levantar condições contratuais antes do kick-off |
| **Plano de Resposta** | 1. Jadson e área de Suprimentos/Contratos devem levantar condições do contrato atual até o kick-off (13/06/2026); 2. Se houver multa: calcular impacto no ROI e ajustar análise financeira com sponsor; 3. Se prazo de fidelidade > 6 meses: avaliar renegociação ou descontinuação antecipada com o fornecedor |
| **Reserva de Contingência** | R$ 0 (impacto financeiro é do cliente — não afeta o orçamento do projeto) |
| **Dono do Risco** | Jadson + Área de Suprimentos do Grupo |
| **Revisão** | Único check até kick-off |

---

### RSK-11 — Volume de defeitos no UAT acima da capacidade de correção antes do go-live

| Campo | Detalhe |
|---|---|
| **Categoria** | Qualidade |
| **Probabilidade** | 3 — Média |
| **Impacto** | 4 — Alto |
| **Score P×I** | **12 — 🟠 Alto** |
| **Descrição** | O UAT tem apenas 4 dias de execução (10–13/11/2026), com 10 dias restantes até o go-live. Se o time de inovação identificar volume alto de defeitos P1/P2, a equipe pode não ter capacidade de corrigir tudo antes de 28/11/2026. |
| **Gatilho** | Mais de 10 defeitos P1+P2 identificados no UAT |
| **Estratégia** | **Mitigar** — validações parciais antecipadas e critério de aceite bem definido |
| **Plano de Resposta** | 1. Realizar demos de cada módulo ao final de cada sprint (review) — Jadson valida funcionalidades incrementalmente, reduzindo surpresas no UAT; 2. Definir claramente no kick-off o critério de aceite do UAT: ≥ 80% dos casos aprovados; todos os casos críticos aprovados; 3. Se volume alto de defeitos: priorizar P1 e aceitar P2 com plano de resolução em 15 dias pós go-live; 4. Acionar horas extras da equipe de desenvolvimento na semana 17–21/11 para absorver volume |
| **Reserva de Contingência** | R$ 0 (horas extras da equipe são absorvidas no orçamento contratual; se exceder: cobrar da reserva de contingência) |
| **Dono do Risco** | GP + QA |
| **Revisão** | Único check ao final do UAT (14/11/2026) |

---

### RSK-12 — Indisponibilidade de Jadson em período crítico

| Campo | Detalhe |
|---|---|
| **Categoria** | Dependência externa |
| **Probabilidade** | 2 — Baixa |
| **Impacto** | 3 — Médio |
| **Score P×I** | **6 — 🟡 Médio** |
| **Descrição** | Jadson é o único ponto focal identificado do cliente. Sua indisponibilidade em períodos críticos (levantamento de requisitos, reviews de sprint, UAT) pode bloquear validações e aprovações, atrasando o projeto. |
| **Gatilho** | Jadson indisponível por > 5 dias úteis em qualquer uma das semanas de review ou UAT |
| **Estratégia** | **Mitigar** — identificar backup e formalizar no kick-off |
| **Plano de Resposta** | 1. Solicitar no kick-off que Jadson indique um substituto formal com autoridade de validação; 2. Agendar reviews e UAT com antecedência mínima de 3 semanas para garantir disponibilidade; 3. Registrar em ata todas as validações — evitar dependência de validação oral |
| **Reserva de Contingência** | R$ 0 |
| **Dono do Risco** | Jadson / GP |
| **Revisão** | Mensal |

---

## 4. Alocação da Reserva de Contingência

| Risco | Valor Alocado | Gatilho de Uso |
|---|---|---|
| RSK-03 (Scope creep) | R$ 3.000 | Mudanças menores aprovadas sem impacto crítico |
| RSK-04 (Prazo apertado) | R$ 5.000 | Contratação de recurso adicional por 2–3 semanas |
| RSK-05 (Indisponibilidade de recurso) | R$ 2.500 | Custo de onboarding de substituto |
| **Total alocado** | **R$ 10.500** | |
| **Reserva residual** | **R$ 4.500** | Eventos imprevistos não cobertos acima |
| **Reserva total** | **R$ 15.000** | |

> Uso de qualquer valor da reserva deve ser aprovado pelo GP (até R$ 5.000) ou pelo sponsor (acima de R$ 5.000) e registrado no controle financeiro do projeto.

---

## 5. Cronograma de Revisão de Riscos

| Revisão | Frequência | Responsável | Integração |
|---|---|---|---|
| Revisão completa do registro | Quinzenal | GP | Integrada ao relatório de status |
| Monitoramento de gatilhos ativos | Semanal | GP + Equipe | Stand-up / reunião semanal |
| Atualização de probabilidade e impacto | Mensal | GP | Reunião de acompanhamento mensal |
| Revisão pós-marco | A cada marco concluído | GP + PMO | Pós-review de sprint |

---

## 6. Top 5 Riscos Críticos — Watchlist

| # | Código | Risco | Score | Próxima Ação | Data Limite |
|---|---|---|---|---|---|
| 1 | RSK-01 | Sponsor não identificado | 20 🔴 | Escalar para liderança do Grupo imediatamente | **13/06/2026** |
| 2 | RSK-03 | Scope creep | 16 🔴 | Formalizar processo de mudanças no kick-off | **16/06/2026** |
| 3 | RSK-02 | Atraso no início da execução | 15 🔴 | Monitorar semanalmente; iniciar prep. em paralelo | **23/06/2026** |
| 4 | RSK-11 | Volume de defeitos no UAT | 12 🟠 | Realizar validações incrementais por sprint | **14/11/2026** |
| 5 | RSK-04 | Prazo insuficiente para desenvolvimento | 12 🟠 | Definir equipe e monitorar velocidade no Sprint 1 | **31/07/2026** |

---

*Documento gerado por Pedro Perigo — Especialista em Gestão de Riscos | VMO Autônomo v1.0 | 2026-05-14*
*PROJ-2026-004 | Versão 1.0 | 2026-05-14*
