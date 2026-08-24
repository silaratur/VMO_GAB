ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-009
Data: 2026-08-24
Analista: Felipe Filtro (VMO Autônomo)

RESUMO:
Jairo de Melo Ferreira Mendes solicita integração automática entre SAP e GRLOG para
sincronização diária de centros de custo, centros de lucro e clientes. Atualmente 5 pessoas
executam cadastro manual diário, gerando erros e dados exibidos como "não informado" no BI
de receita. O sizing de Rafael Requisito estima 180–290h (projeto formal). A demanda é
aprovada com condições: faltam aprovação formal de Diretoria, aprovação do Gerente de TI e
formalização do orçamento. Classificação: PROJETO.

---

## Claims de Alto Risco Identificados

| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "O BI é acompanhado pela CEO da companhia" [04:11-04:31] | NÃO — CLAIM SEM EVIDÊNCIA (corretamente sinalizado por Iara) | Critério 1: teto rebaixado; alinhamento executivo não comprovado documentalmente. Nota máxima 6/10 para componente "visibilidade executiva". |
| "É melhoria de processo já existente" [05:35-05:38] — implica simplicidade | PARCIAL — processo existe mas integração é nova | Critério 2: verificado que é integração nova entre dois sistemas, não ajuste de funcionalidade existente. Claim de simplicidade não confirmado. |
| Orçamento "depende de estudo da DTI" [09:14-09:20] — implica orçamento futuro | NÃO — nenhuma previsão orçamentária documentada | Critério 6: orçamento não aprovado, nem sinalizado formalmente. Nota rebaixada. |

---

## Critérios de Qualificação

### Critérios 1–6 — Valor da Demanda

1. Alinhamento Estratégico      6/10
   Evidência disponível: PARCIAL
   A demanda endereça confiabilidade dos dados de receita para tomada de decisão executiva [03:25-03:47].
   Não há OKR ou objetivo estratégico formal citado — alinhamento é inferido do contexto operacional,
   não de documento estratégico. Jairo afirma que o BI é acompanhado pela CEO [04:11-04:31], mas
   esta é uma CLAIM SEM EVIDÊNCIA — teto aplicado. Sem evidência documental do vínculo com objetivo
   estratégico formal, nota máxima 6/10.
   Para revisar esta nota, precisamos de: documento de OKR ou planejamento estratégico que endereça
   confiabilidade de dados de receita; ou evidência documental do acompanhamento da CEO.

2. Viabilidade Técnica           5/10
   Evidência disponível: PARCIAL
   SAP e GRLOG são os dois sistemas envolvidos [08:10-08:11], com campos correspondentes declarados
   pelo solicitante [02:25-02:44]. Porém: método de integração não definido (API, RFC, flat file,
   middleware — Lacuna L4); mapeamento de campos não detalhado (Lacuna L7); arquitetura técnica do
   GRLOG desconhecida; estudo de viabilidade da DTI não iniciado (Lacuna L5). A afirmação de que é
   "melhoria de processo existente" foi verificada: o processo de cadastro existe, mas a integração
   automática é desenvolvimento novo, não ajuste de funcionalidade existente. Sem estudo técnico da
   DTI e sem definição do método de integração, a viabilidade é incerta.
   Para revisar esta nota, precisamos de: parecer técnico da DTI sobre método de integração viável;
   mapeamento de campos SAP→GRLOG; confirmação de APIs ou serviços disponíveis.

3. Retorno sobre Investimento    6/10
   Evidência disponível: PARCIAL
   Benefícios qualitativos claros: eliminação de erros de cadastro, confiabilidade do BI,
   liberação de tempo de 5 pessoas [06:41-06:46]. Porém: nenhum valor financeiro quantificado pelo
   solicitante — nem custo do trabalho manual atual, nem valor da receita impactada por dados incorretos,
   nem custo estimado do projeto. Orçamento depende de estudo da DTI [09:14-09:20]. Payback não pode
   ser calculado com precisão sem custos.
   Estimativa de Felipe (confiança BAIXA): se 5 pessoas dedicam ~1h/dia ao cadastro manual = ~5h/dia
   = ~110h/mês. A custo médio de R$50/h (analista operacional), isso representa ~R$66.000/ano de
   custo operacional evitável. Custo do projeto estimado por Rafael: 180–290h, a ~R$200/h
   (desenvolvimento/integração) = R$36.000–58.000 + 20% contingência = R$43.200–69.600.
   Payback estimado: 8–13 meses. ROI 12 meses: -5% a +53%. Confiança: BAIXA — baseado em premissas
   não validadas pelo solicitante.
   Para revisar esta nota, precisamos de: custo/hora real das 5 pessoas; tempo real dedicado ao
   cadastro manual; custo estimado do projeto pela DTI.

4. Urgência                      6/10
   Evidência disponível: PARCIAL
   Prazo desejado: outubro 2026 [08:40-08:57] — data concreta presente. "Quanto antes" indica
   pressão temporal [08:40-08:57]. Porém: a consequência de não-fazer não foi quantificada em
   valor financeiro. Impacto descrito é operacional (dados incorretos no BI, trabalho manual),
   mas não há evidência de incidente, multa, auditoria ou perda financeira concreta causada pelo
   problema. A urgência é genuína (dados incorretos visíveis no BI) mas não é crítica (não há
   regulatório, não há SLA em risco, não há penalidade contratual).
   Para revisar esta nota, precisamos de: quantificação do custo de decisões baseadas em dados
   incorretos no BI; ou evidência de incidente passado causado pela falta de integração.

5. Maturidade da Demanda         7/10
   Evidência disponível: SIM
   O problema está bem definido: processo manual de cadastro entre SAP e GRLOG, com 5 pessoas
   executando diariamente [02:25-02:44], [03:02-03:09]. As entidades estão identificadas (centro
   de custo, centro de lucro, clientes). O impacto está claro (dados incorretos no BI [04:11-04:31]).
   O critério de sucesso está declarado [09:35-09:44]. Lacunas técnicas existem (método de
   integração, mapeamento de campos) mas são esperadas nesta fase — o escopo funcional está
   suficientemente maduro para qualificação. Iara documentou 10 lacunas com prioridade, demonstrando
   que a captação foi rigorosa.
   Evidência: transcrição Fireflies com timestamps, 10 lacunas classificadas, necessidade separada
   de pedido, premissas e restrições documentadas.

6. Disponibilidade de Recursos   3/10
   Evidência disponível: NÃO
   Orçamento NÃO aprovado — depende de estudo da DTI que não tem responsável nomeado nem prazo
   [09:14-09:20] (Lacuna L5). Aprovação formal de Diretoria AUSENTE (Lacuna L1 — BLOQUEANTE conforme
   regras do squad). Aprovação do Gerente de TI AUSENTE (Lacuna L2 — BLOQUEANTE). Ana Sílvia
   Kallegard é aprovadora de custos [07:39-07:49], mas isso não é aprovação formal de orçamento.
   Disponibilidade da equipe de TI não verificada. Nenhum recurso está formalmente comprometido.
   Para tornar esta nota mais alta: aprovação formal de Diretoria + Gerente de TI; formalização
   do orçamento com centro de custo; confirmação de disponibilidade da equipe DTI.

### Critérios 7–10 — Complexidade de Execução

7. Esforço Estimado              8/10
   Evidência disponível: SIM
   Fonte: sizing.md de Rafael Requisito (Step 5). Estimativa por fase:
   - Levantamento de requisitos: 40–60h (confiança MÉDIA)
   - Desenvolvimento/Configuração: 80–140h (confiança BAIXA)
   - Testes e homologação: 40–60h (confiança MÉDIA)
   - Go-live e suporte inicial: 20–30h (confiança ALTA)
   - TOTAL: 180–290h (confiança BAIXA)
   Classificação de Rafael: > 160h → Projeto formal. Mesmo no cenário otimista (180h), ultrapassa
   o limiar. Nota 8/10 reflete esforço significativo com faixa ampla de incerteza. Não é nota 9 ou
   10 porque o cenário otimista (180h) está próximo do limiar de melhoria complexa (160h).

8. Impacto Organizacional        6/10
   Evidência disponível: PARCIAL
   Áreas declaradas como impactadas: Gestão da Receita e "toda a Diretoria" [07:02-07:06]. +200
   usuários do GRLOG [07:17-07:20]. Porém: a integração SAP→GRLOG em si será operada pela equipe
   técnica/DTI, não por 200 usuários. O impacto nos 200 usuários é indireto (dados corretos no BI).
   Mudança de processo: as 5 pessoas que fazem cadastro manual terão essa atividade eliminada —
   impacto direto mas restrito a um grupo pequeno. Não há evidência de mudança de processo em
   múltiplas gerências distintas. Treinamento: mínimo (usuários continuam usando GRLOG; a mudança
   é no backend). Nota reflete impacto real mas concentrado.
   Para revisar esta nota, precisamos de: confirmação de que equipes de gerências distintas
   operam ou dependem diretamente do processo de cadastro.

9. Governança Necessária         7/10
   Evidência disponível: PARCIAL
   Integração entre dois sistemas corporativos (SAP e GRLOG) com rotina automatizada diária. Envolve
   DTI para desenvolvimento, Gestão da Receita como área de negócio, Controladoria como aprovadora
   de custos — 3 áreas com interesses distintos requerem coordenação formal. Prazo externo (outubro
   2026) exige cronograma. Orçamento por definir exige governança financeira. Não é gerível como
   task de sustentação — precisa de gestão de stakeholders e controle de escopo.
   NOTA: GMUD não foi usada como justificativa — governança baseada em multiplicidade de
   stakeholders e necessidade de coordenação inter-áreas, não em processo padrão de mudança SAP.

10. Impacto Regulatório/Financeiro  4/10
    Evidência disponível: PARCIAL
    Solicitante declarou "nenhum requisito legal/regulatório" [08:29]. Impacto financeiro é indireto:
    dados incorretos no BI de receita afetam visibilidade executiva mas não há evidência de impacto
    em demonstrativos contábeis, obrigações fiscais ou compliance. Centros de custo e centros de lucro
    são entidades contábeis — um cadastro incorreto poderia gerar alocação incorreta de custos/receitas,
    mas o solicitante não reportou esse tipo de problema. Nota 4/10 reflete risco implícito baixo
    pela natureza contábil das entidades, sem evidência de impacto regulatório concreto.

---

PONTUAÇÃO: 58/100 (58%)

**CLASSIFICAÇÃO: PROJETO**
Critérios 7–10: Esforço (8/10), Governança (7/10) — 2 de 4 critérios ≥ 7 confirmam necessidade
de gestão formal. A integração automatizada entre SAP e GRLOG com 180–290h de esforço, 3 áreas
envolvidas (DTI, Gestão da Receita, Controladoria) e prazo externo de outubro 2026 tornam inviável
o tratamento como melhoria de sustentação. Pipeline VMO completo é obrigatório.

**DECISÃO: APROVADO COM CONDIÇÕES**
Pontuação de 58% (faixa 50–74%) com condições resolvíveis. A demanda tem valor operacional claro
(eliminação de trabalho manual, confiabilidade de dados) e complexidade que justifica projeto formal.
As condições são bloqueios administrativos/organizacionais, não técnicos ou de viabilidade.

---

## Condições Bloqueantes

- **CB-1:** Obter aprovação formal de Diretoria — obrigatória conforme regras do squad. Sem isso a demanda não pode avançar para documentação. Quem da Diretoria aprova formalmente?
- **CB-2:** Obter aprovação do Gerente de TI — obrigatória conforme regras do squad. Nenhum Gerente de TI foi mencionado na reunião de discovery.
- **CB-3:** Formalizar orçamento — definir centro de custo, previsão de investimento e aprovação formal. Orçamento "depende da DTI" não é orçamento aprovado.
- **CB-4:** Concluir estudo de viabilidade da DTI — nomear responsável e definir prazo. Sem estudo técnico, a viabilidade é incerta (nota 5/10).

## Condições Desejáveis (não bloqueantes)

- **CD-1:** Obter evidência documental do acompanhamento do BI pela CEO (melhoria da nota de alinhamento estratégico)
- **CD-2:** Quantificar custo real do trabalho manual atual (melhoria da estimativa de ROI)
- **CD-3:** Confirmar método de integração com DTI antes do kick-off (redução da faixa de esforço)

---

## Análise Comercial

### Benefícios Esperados

| Benefício | Valor Estimado | Prazo | Confiança |
|-----------|----------------|-------|-----------|
| Eliminação de trabalho manual de cadastro (5 pessoas × ~1h/dia) | R$ 66.000/ano | Imediato após go-live | BAIXA — tempo dedicado e custo/hora não confirmados |
| Eliminação de erros de cadastro e dados "não informado" no BI | Não quantificado — impacto em qualidade de dados | 1 mês | — |
| Confiabilidade de dados de receita para decisão executiva | Não quantificado — impacto estratégico | 1 mês | — |
| Reaproveitamento de capacidade das 5 pessoas em atividades de maior valor | Não quantificado — depende da realocação | 3 meses | — |
Total de benefícios anuais quantificáveis estimados: ~R$ 66.000 (confiança BAIXA)

### Custo do Projeto

| Item | Estimativa |
|------|------------|
| Desenvolvimento e configuração (cenário médio ~170h × R$ 200/h) | R$ 34.000 |
| Levantamento de requisitos (~50h × R$ 200/h) | R$ 10.000 |
| Testes e homologação (~50h × R$ 200/h) | R$ 10.000 |
| Go-live e suporte inicial (~25h × R$ 200/h) | R$ 5.000 |
| Infraestrutura (12 meses — servidor/middleware se necessário) | R$ 6.000 |
| Licenças (se middleware SAP PI/PO necessário) | R$ 0–15.000 |
| Treinamento operacional | R$ 3.000 |
| Contingência (20%) | R$ 13.600–16.600 |
| **TOTAL** | **R$ 81.600–99.600** |

Nota: cenário com RFC/API direta (sem middleware) = ~R$ 81.600; cenário com middleware = ~R$ 99.600.

### Métricas de Retorno

- Payback: 15–18 meses (com contingência)
- ROI em 12 meses: -21% a -34% (ainda em amortização)
- ROI em 24 meses: +32% a +62%
- Nível de confiança geral: BAIXA — benefícios quantificáveis baseados em premissas não validadas; benefícios qualitativos (confiabilidade de dados, visibilidade executiva) podem ser mais relevantes que o ROI financeiro direto.

Nota: sem contingência, payback seria ~12–15 meses.

### Custo de Não-Fazer

Manutenção do status quo: 5 pessoas dedicando ~1h/dia ao cadastro manual, com risco permanente de:
- Erros de cadastro gerando dados "não informado" no BI de receita
- Decisões executivas baseadas em dados incompletos ou incorretos
- Custo operacional de ~R$ 66.000/ano sem tendência de redução
- Risco reputacional: se o BI é efetivamente acompanhado pela CEO, dados incorretos impactam credibilidade da área de Gestão da Receita

### Proposta de Valor

"O projeto de Integração SAP-GRLOG, com investimento estimado de R$ 82.000–100.000, eliminará
o cadastro manual diário realizado por 5 pessoas, garantindo sincronização automática de centros
de custo, centros de lucro e clientes. O retorno estimado é de R$ 66.000/ano em custo operacional
evitável, com payback de 15–18 meses, além de benefícios qualitativos de confiabilidade de dados
de receita que impactam a visibilidade executiva e a qualidade da tomada de decisão."

---

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Obter aprovação formal de Diretoria (CB-1) | Jairo de Melo Ferreira Mendes (articular) | 2026-09-05 |
| Identificar e obter aprovação do Gerente de TI (CB-2) | Jairo + DTI | 2026-09-05 |
| Concluir estudo de viabilidade técnica da DTI (CB-4) | DTI (responsável a nomear) | 2026-09-12 |
| Formalizar orçamento com centro de custo (CB-3) | Ana Sílvia Kallegard (Controladoria) | 2026-09-12 |
| Quantificar tempo real dedicado ao cadastro manual (CD-2) | Jairo + equipe Gestão da Receita | 2026-09-05 |
| Confirmar método de integração preferencial (CD-3) | DTI | 2026-09-12 |
| Resubmeter para qualificação final após condições resolvidas | VMO Autônomo | Após resoluções |

---

*Parecer emitido por Felipe Filtro — Analista de Qualificação | VMO Autônomo Squad | 2026-08-24*
