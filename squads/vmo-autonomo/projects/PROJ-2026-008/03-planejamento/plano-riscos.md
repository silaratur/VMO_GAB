# Plano de Gestão de Riscos — Ajustes Monitores ZMMR_GSI02/03/04 (PROJ-2026-008)
Versão: 1.0 | Data: 2026-06-10 | Elaborado por: Pedro Perigo (VMO Autônomo)

## Registro de Riscos

| ID | Categoria | Descrição do Risco | Prob (1-5) | Impacto (1-5) | Score | Nível |
|----|-----------|---------------------|------------|----------------|-------|-------|
| R-001 | Governança/Stakeholders | A aprovação formal de Diretoria (CB-1) pode não ser obtida até o prazo (2026-06-13), impedindo que a demanda seja considerada "VALIDADA" pela regra de governança do VMO e atrasando o kick-off (M0) | 3 | 5 | 15 | ALTO |
| R-002 | Técnico/Fiscal-Contábil | A lógica de estorno de fatura/pedido (item 13, GSI03/GSI04) pode gerar inconsistência de dados fiscais/contábeis (links de fatura/requisição, log de auditoria) se a especificação formal (CB-6) não cobrir todos os cenários de borda (estorno parcial, MIRO já paga) | 3 | 5 | 15 | ALTO |
| R-003 | Técnico/Organizacional | A alteração de comportamento padrão dos campos "DT. Básica"/"Vencimento Em" da MIRO (item 14) pode impactar outros usuários/processos da MIRO fora do fluxo do monitor GSI03, não verificados no Critério 8 (Impacto Organizacional = 4/10) | 3 | 4 | 12 | ALTO |
| R-004 | Financeiro | O custo estimado com contingência (R$ 36.000) pode exceder o teto de investimento aprovado (R$ 30.000), sem confirmação de aditivo (CB-Orçamento) | 4 | 3 | 12 | ALTO |
| R-005 | Prazo/Recursos | A disponibilidade real do SQUAD PM/MM (dedicação parcial, sem confirmação formal — CB-5 pendente até 2026-06-17) pode não comportar o cronograma de 3 ondas, especialmente o pacote crítico do item 13 (12 dias úteis) | 3 | 4 | 12 | ALTO |
| R-006 | Stakeholders | A divergência entre Prioridade "Baixa" (Work Request) e SLA "1 semana"/Criticidade "2-Alta" (chamado) — CB-4 — pode gerar expectativa do solicitante de entrega em 1 semana, incompatível com o cronograma real de ~14,5 semanas | 4 | 3 | 12 | ALTO |
| R-007 | Técnico | As estimativas de esforço por analogia com a V1 podem subestimar o esforço real dos itens 5, 7, 13 e 14 — que não têm cobertura direta na V1 segundo o histórico de alterações (Critério 2: viabilidade técnica = 6/10) | 3 | 3 | 9 | ALTO |
| R-008 | Escopo | O destino exato da coluna "Data de lançamento" do item 6 (GSI03, GSI04 ou ambos — CB-3) pode não ser confirmado a tempo do pacote 1.2.2.3, gerando retrabalho de desenvolvimento já iniciado | 3 | 2 | 6 | MÉDIO |
| R-009 | Externo | Atualizações/patches do SAP ECC aplicados pelo Basis durante o período do projeto (2026-06 a 2026-09) podem invalidar BAdIs/user-exits desenvolvidos para os itens 5, 7, 13 e 14, exigindo retrabalho de adaptação | 2 | 3 | 6 | MÉDIO |

---

## Análise por Categoria

### Riscos Técnicos
**R-002, R-003, R-007** concentram o maior risco técnico do projeto, todos relacionados aos itens de maior complexidade lógica (5, 7, 13, 14 — Onda 3), exatamente os itens sem cobertura direta na V1. R-002 e R-003 têm potencial de impacto em integridade fiscal/contábil, indo além de "bug de sistema" — podem gerar lançamentos incorretos em demonstrativos contábeis (Imobilizado VIX 2800184-0). R-007 é um risco "meta" — a própria base de estimativa (analogia com a V1) é menos confiável para esses itens.

### Riscos de Prazo
**R-005, R-006 e R-008** são os riscos de prazo principais. R-005 ataca diretamente o caminho crítico identificado por Carlos Cronograma (pacote 1.4.2.4 — item 13, 12 dias). R-006 não é um risco de atraso técnico, mas de **gestão de expectativa**: se o solicitante (que abriu um chamado com SLA de 1 semana) não for comunicado sobre o cronograma real de 3 ondas/~3,5 meses, o projeto pode ser percebido como "atrasado" desde o primeiro status report, mesmo estando dentro do planejado.

### Riscos Financeiros
**R-004** é o único risco puramente financeiro, mas com alta probabilidade (4/5): a estimativa de Felipe Filtro já indicou que o custo com contingência (R$36K) excede o teto declarado (R$30K). Sem resolução de CB-Orçamento, este risco tende a se materializar assim que a primeira fatura/medição for emitida.

### Riscos de Stakeholders/Governança
**R-001 e R-006** são riscos de governança/stakeholders herdados diretamente das Condições Bloqueantes do Step 4 (Felipe Filtro) e do Step 1 (Iara Inbound). R-001 é o de maior impacto potencial: sem aprovação de Diretoria, a demanda permanece "NÃO VALIDADA" pela regra de governança do VMO, o que pode significar a paralisação formal do projeto mesmo após o kick-off técnico ter começado.

---

## Plano por Risco

### R-001 — Aprovação de Diretoria não confirmada (CB-1) — ALTO
- **Estratégia:** Evitar (resolução antes do kick-off técnico)
- **Gatilho:** Aprovação formal de Diretoria não recebida até 2026-06-13 (prazo da CB-1)
- **Ações de Resposta:**
  1. Escalar formalmente a pendência de aprovação de "André" (citado por Tatiane no e-mail de 06/03/2026) ao GP VMO e à Tatiane Dias de Moraes — Responsável: GP VMO — Prazo: 2026-06-12
  2. Solicitar o PDF original de "APROVAÇÃO - DIRETOR DA ÁREA.pdf" para verificar se contém manifestação de Diretor não capturada na extração — Responsável: Tatiane / Projetos DTI — Prazo: 2026-06-12
  3. Caso a aprovação de Diretoria não seja obtida até 2026-06-13, suspender o kick-off (M0) e reportar ao sponsor provisório (Nubia Carla Freitas Santos Souza) para escalonamento — Responsável: GP VMO — Prazo: 2026-06-13
- **Plano de Contingência:** Iniciar apenas as atividades de especificação (1.2.1.1, 1.2.1.2, 1.4.1.1, 1.4.1.2 — que não requerem orçamento liberado) enquanto a aprovação formal de Diretoria é regularizada, sem iniciar desenvolvimento (1.2.2.x em diante)
- **Custo da Resposta:** R$ 0

### R-002 — Inconsistência Fiscal/Contábil no Estorno (Item 13) — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Especificação funcional formal do item 13 (CB-6, prazo 2026-06-24) não cobre explicitamente os cenários "estorno parcial" e "MIRO já paga"
- **Ações de Resposta:**
  1. Garantir que a especificação formal (1.4.1.1) seja revisada e aprovada por um especialista fiscal/contábil da Contabilidade VIXPar, além do SQUAD PM/MM — Responsável: Especialista Funcional + Nubia (Gerente Contábil) — Prazo: 2026-06-24
  2. Incluir no plano de testes dedicado (1.4.3.2) cenários de borda explícitos: estorno parcial, MIRO já paga, ordem fatura→pedido violada — Responsável: SQUAD PM/MM (QA) — Prazo: 2026-09-09
  3. Executar o item 13 em ambiente de homologação com dados reais (massa de teste anonimizada) antes do go-live da Onda 3 — Responsável: SQUAD PM/MM — Prazo: 2026-09-11
- **Plano de Contingência:** Em caso de inconsistência detectada pós go-live, reverter o item 13 (feature toggle) e processar estornos manualmente até correção, registrando log manual de auditoria
- **Custo da Resposta:** R$ 0 (interno) / até R$ 5.000 se for necessária correção de dados pós-incidente

### R-003 — Impacto da Alteração da MIRO (Item 14) em Outros Usuários — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Identificação de qualquer área/usuário fora do fluxo do monitor GSI03 que utilize os campos "DT. Básica"/"Vencimento Em" da MIRO em relatórios ou processos próprios
- **Ações de Resposta:**
  1. Levantar, junto à Contabilidade/Fiscal corporativa, se há outros usuários/relatórios dependentes do preenchimento automático atual de "DT. Básica" — Responsável: SQUAD PM/MM + Nubia — Prazo: 2026-08-19 (antes do dev do item 14)
  2. Caso existam dependências, restringir a alteração de comportamento ao escopo do monitor GSI03 (via BAdI condicionado por transação de origem), preservando o comportamento padrão fora do monitor — Responsável: SQUAD PM/MM (ABAP) — Prazo: 2026-08-31
- **Plano de Contingência:** Se o impacto só for identificado pós go-live, reverter via feature toggle e comunicar formalmente as áreas afetadas
- **Custo da Resposta:** R$ 0

### R-004 — Estouro de Orçamento (CB-Orçamento) — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Medição/fatura de qualquer onda projeta custo acumulado acima de R$ 30.000
- **Ações de Resposta:**
  1. Validar formalmente, junto a Tatiane/Projetos DTI, se o teto aprovado de R$30K já contempla a contingência de 20% (R$6K) ou se requer aditivo — Responsável: GP VMO — Prazo: 2026-06-24
  2. Caso não haja aditivo, priorizar a execução interna pelo SQUAD PM/MM (sem custo de "ramp-up" de fornecedor externo) para manter o custo dentro de R$30K, reservando os R$6K de contingência apenas para a Onda 3 (maior risco técnico) — Responsável: GP VMO — Prazo: contínuo
- **Plano de Contingência:** Se o estouro for inevitável, priorizar a entrega das Ondas 1 e 2 (R$ ~20K estimado) e submeter a Onda 3 (itens 5,7,13,14) como aditivo de escopo separado
- **Custo da Resposta:** R$ 0 (gestão) / R$ 6.000 (contingência já prevista no TAP)

### R-005 — Disponibilidade do SQUAD PM/MM (CB-5) — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** SQUAD PM/MM não confirma disponibilidade ≥ 50% até 2026-06-17 (prazo CB-5), ou pacote 1.4.2.4 (item 13) ultrapassa 12 dias úteis em execução
- **Ações de Resposta:**
  1. Obter confirmação formal de alocação do especialista Jerfesson Fernandes Helmer (ou substituto com contexto da V1) para o período 2026-06-17 a 2026-09-25 — Responsável: Projetos DTI — Prazo: 2026-06-17
  2. Revisar o cronograma (Step 10) assim que CB-5 for resolvida, ajustando durações/datas conforme estimativa real do squad — Responsável: Carlos Cronograma / GP VMO — Prazo: 2026-06-19
- **Plano de Contingência:** Reforço pontual com consultoria SAP MM/ABAP externa apenas para a Onda 3 (conforme dualidade de destinatário registrada no Work Request, Step 9) — benchmark de mercado: R$ 25.000-80.000 para escopo equivalente
- **Custo da Resposta:** R$ 0 / até R$ 15.000 se reforço externo pontual for necessário (Onda 3)

### R-006 — Expectativa de Prazo do Solicitante (CB-4) — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** Solicitante (Tatiane/João Henrique) demonstra insatisfação ou aciona novamente o chamado 6898567 cobrando o SLA de 1 semana após o kick-off
- **Ações de Resposta:**
  1. Comunicar formalmente a Tatiane/João Henrique, antes do kick-off, o cronograma real (3 ondas, M0-M5, conclusão prevista 2026-09-25 + buffer) e a justificativa da divergência entre a Prioridade "Baixa" do WR e o SLA "Alta/1 semana" do chamado — Responsável: GP VMO — Prazo: 2026-06-17
  2. Resolver formalmente CB-4 (qual classificação prevalece) e registrar a decisão no chamado 6898567, encerrando o SLA de 1 semana com justificativa de replanejamento — Responsável: GP VMO + Tatiane — Prazo: 2026-06-13
  3. Entregar a Onda 1 (itens de menor complexidade) o mais cedo possível (M1, 2026-07-15) como demonstração tangível de progresso — Responsável: SQUAD PM/MM — Prazo: 2026-07-15
- **Plano de Contingência:** Se a pressão por SLA persistir, priorizar 1-2 itens de "vitória rápida" (ex.: itens 2 e 3, exposição de campo já existente) para entrega em até 2 semanas do kick-off, fora da sequência da Onda 1
- **Custo da Resposta:** R$ 0

### R-007 — Subestimativa de Esforço (Itens sem Cobertura na V1) — ALTO
- **Estratégia:** Mitigar
- **Gatilho:** CB-5 (estimativa do SQUAD PM/MM) resulta em esforço > 20% acima do estimado por analogia para os itens 5, 7, 13, 14
- **Ações de Resposta:**
  1. Tratar a estimativa por analogia deste cronograma como preliminar, substituindo-a pela estimativa de CB-5 assim que disponível (2026-06-17) — Responsável: Carlos Cronograma — Prazo: 2026-06-19
  2. Reservar o buffer de 15% (Step 10) prioritariamente para a Onda 3 — Responsável: GP VMO — Prazo: contínuo
- **Plano de Contingência:** Se o esforço real exceder em > 30% a estimativa, negociar extensão de prazo (de 2026-09-30 para 2026-10-10, conforme alerta já registrado no cronograma) com o sponsor
- **Custo da Resposta:** R$ 0

### R-008 — Indefinição do Destino do Item 6 (CB-3) — MÉDIO
- **Estratégia:** Mitigar
- **Gatilho:** Resposta de Tatiane/João Henrique sobre GSI03/GSI04/ambos não recebida até 2 dias úteis após o kick-off (2026-06-19)
- **Ações de Resposta:**
  1. Incluir a pergunta de CB-3 na comunicação de kick-off (R-006, ação 1) para resposta antecipada — Responsável: GP VMO — Prazo: 2026-06-17
- **Plano de Contingência:** Se não houver resposta até 2026-06-19, mover o pacote 1.2.2.3 (item 6) para a Onda 2, sem impacto no caminho crítico (conforme nota do cronograma)
- **Custo da Resposta:** R$ 0

### R-009 — Atualizações/Patches do SAP ECC durante o Projeto — MÉDIO
- **Estratégia:** Aceitar (com monitoramento)
- **Gatilho:** Comunicado do time Basis sobre aplicação de patch/upgrade no ambiente SAP ECC entre 2026-06 e 2026-09
- **Ações de Resposta:**
  1. Incluir o time Basis na comunicação de status report quinzenal (1.1.2) para alinhamento de janelas de manutenção — Responsável: GP VMO — Prazo: contínuo
- **Plano de Contingência:** Re-executar testes unitários (1.2.3.1 / 1.3.3.1 / 1.4.3.1) das ondas já entregues após qualquer patch aplicado durante o projeto
- **Custo da Resposta:** até R$ 8.000 se retestes completos forem necessários

---

## Reserva de Contingência Calculada

| ID | Risco | Prob (%) | Impacto (R$) | Valor Esperado |
|----|-------|----------|----------------|-----------------|
| R-001 | Aprovação de Diretoria não confirmada | 30% | R$ 5.000 (replanejamento/escalonamento) | R$ 1.500 |
| R-002 | Inconsistência fiscal/contábil — estorno (item 13) | 40% | R$ 15.000 (correção de dados pós-incidente) | R$ 6.000 |
| R-003 | Impacto MIRO em outros usuários (item 14) | 30% | R$ 8.000 (retrabalho/comunicação) | R$ 2.400 |
| R-004 | Estouro de orçamento (R$36K vs R$30K) | 60% | R$ 6.000 (contingência já prevista) | R$ 3.600 |
| R-005 | Indisponibilidade SQUAD PM/MM | 40% | R$ 15.000 (reforço externo Onda 3) | R$ 6.000 |
| R-006 | Expectativa de prazo do solicitante | 50% | R$ 3.000 (esforço extra de gestão/comunicação) | R$ 1.500 |
| R-007 | Subestimativa de esforço (itens sem cobertura V1) | 40% | R$ 10.000 (horas extras/extensão) | R$ 4.000 |
| R-008 | Indefinição destino item 6 (CB-3) | 30% | R$ 2.000 (retrabalho de desenvolvimento) | R$ 600 |
| R-009 | Patch/upgrade SAP durante o projeto | 15% | R$ 8.000 (retestes completos) | R$ 1.200 |
| **TOTAL** | | | | **R$ 26.800** |

**Reserva já incluída no TAP:** R$ 6.000 (20% de contingência sobre R$ 30.000).

⚠️ **Alerta de Pedro Perigo:** o valor esperado calculado (R$ 26.800) é **mais de 4x maior** que a reserva de contingência atualmente prevista no TAP (R$ 6.000). Isso não significa que o projeto custará R$ 56.800 — a maior parte dos riscos (R-001, R-005, R-006, R-007, R-008, R-009) tem impacto predominante em **prazo e esforço interno**, não em desembolso financeiro direto, e várias ações de resposta têm custo R$ 0 (gestão/comunicação/escalonamento). Recomenda-se:
1. Tratar a reserva financeira de R$ 6.000 como cobertura apenas para R-002, R-003, R-004 e R-009 (riscos com maior componente de desembolso direto), totalizando valor esperado de R$ 13.200 — ainda acima da reserva atual.
2. Tratar R-001, R-005, R-006, R-007 e R-008 prioritariamente via **ações de mitigação sem custo** (já detalhadas acima), com reavaliação no primeiro status report (Step 13/Sara Status) após resolução das CBs.
3. Caso CB-Orçamento (R-004) seja resolvida com aditivo ao teto de R$ 30K, reavaliar se a contingência financeira pode subir de R$ 6.000 para algo entre R$ 10.000-13.000, alinhada ao valor esperado dos riscos com maior componente financeiro.

## Próxima Revisão do Registro de Riscos

Conforme princípio "riscos revisados a cada ciclo de status report", este registro deve ser revisado:
- Imediatamente após a resolução de CB-1 a CB-6 (esperado até 2026-06-24) — reavaliar R-001, R-005, R-006, R-007, R-008.
- A cada status report quinzenal (Sara Status, Step 13 e ciclos subsequentes de execução).
- Obrigatoriamente antes do início da Onda 3 (2026-08-13) — reavaliar R-002, R-003, R-007, R-009.
