# Plano de Riscos — PROJ-2026-005

| Campo | Valor |
|---|---|
| **Projeto** | PROJ-2026-005 — Auditor Fiscal: Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Demanda** | DEM-2026-002 |
| **Data de Referência** | 2026-05-15 |
| **Versão** | v5 |
| **Autor** | Pedro Perigo — Especialista em Gestão de Riscos, VMO Autônomo |
| **Revisão** | Plano inicial — para validação pelo Sponsor |

---

## 1. Metodologia de Riscos

### 1.1 Escalas de Avaliação

**Escala de Probabilidade (P)**

| Nível | Descrição | Critério |
|---|---|---|
| 1 | Raro | Ocorrência improvável (<10% de chance) |
| 2 | Improvável | Pouco provável de ocorrer (10–30%) |
| 3 | Possível | Pode ocorrer em algum momento (30–50%) |
| 4 | Provável | Mais provável que ocorra do que não (50–70%) |
| 5 | Quase Certo | Ocorrência esperada em praticamente todos os cenários (>70%) |

**Escala de Impacto (I)**

| Nível | Descrição | Critério Geral |
|---|---|---|
| 1 | Insignificante | Sem impacto perceptível no prazo, custo ou compliance |
| 2 | Baixo | Atraso < 1 semana ou desvio orçamentário < R$5K |
| 3 | Moderado | Atraso de 2–4 semanas ou desvio orçamentário R$5K–R$15K |
| 4 | Alto | Atraso de 1–3 meses, desvio > R$15K, ou risco de compliance |
| 5 | Catastrófico | Cancelamento do projeto, descontinuidade de compliance fiscal, multas regulatórias |

**Score de Risco = P × I**

| Classificação | Faixa de Score | Ação Requerida |
|---|---|---|
| **Crítico** | 15–25 | Resposta imediata; escalonamento ao Sponsor |
| **Alto** | 10–14 | Plano de ação obrigatório; monitoramento semanal |
| **Médio** | 6–9 | Monitoramento quinzenal; ação preventiva planejada |
| **Baixo** | 1–5 | Aceite com registro; revisão mensal |

### 1.2 Estrutura de Categorias

| Código | Categoria |
|---|---|
| GOV | Governança e Patrocínio |
| FOR | Fornecedor / Dependência Externa |
| CTR | Contratual / Jurídico |
| CMP | Compliance Fiscal e Regulatório |
| REC | Recursos Humanos / Disponibilidade |
| TEC | Tecnologia / Integração |
| OPE | Operacional / Processo |
| FIN | Financeiro / Orçamentário |

---

## 2. Registro de Riscos

### 2.1 Tabela Resumida

| ID | Categoria | Descrição Resumida | P | I | Score | Classificação |
|---|---|---|:---:|:---:|:---:|---|
| RSK-01 | GOV | Sponsor executivo não identificado | 5 | 5 | **25** | Crítico |
| RSK-02 | CTR | Acordo NBS sem verificação documental | 4 | 5 | **20** | Crítico |
| RSK-03 | FOR | Atrasos da NBS no desenvolvimento | 4 | 4 | **16** | Crítico |
| RSK-04 | CMP | Descontinuidade do Fiscal Defender antes da prontidão do módulo NBS | 3 | 5 | **15** | Crítico |
| RSK-05 | REC | Disponibilidade insuficiente das equipes de UAT | 4 | 3 | **12** | Alto |
| RSK-06 | FOR | Descontinuidade ou falência da NBS durante o desenvolvimento | 2 | 5 | **10** | Alto |
| RSK-07 | TEC | Incompatibilidade de integração entre módulo NBS e sistemas legados GAB | 3 | 4 | **12** | Alto |
| RSK-08 | CMP | Mudança na legislação fiscal durante o projeto | 3 | 4 | **12** | Alto |
| RSK-09 | OPE | Recesso de dezembro impede encerramento formal do projeto | 4 | 3 | **12** | Alto |
| RSK-10 | GOV | Conflito de prioridades entre áreas (Contabilidade, Financeiro, Jurídico) | 3 | 3 | **9** | Médio |
| RSK-11 | TEC | Perda ou corrupção de dados fiscais históricos na migração | 2 | 5 | **10** | Alto |
| RSK-12 | FIN | Custos residuais acima do previsto (R$35K) por retrabalho ou adequações | 3 | 3 | **9** | Médio |
| RSK-13 | REC | Rotatividade de pessoal-chave durante o projeto (12 meses) | 2 | 4 | **8** | Médio |
| RSK-14 | OPE | Resistência dos usuários-chave à mudança de ferramenta | 3 | 3 | **9** | Médio |
| RSK-15 | CTR | NBS reivindica cobrança posterior por funcionalidades "fora do escopo" | 2 | 4 | **8** | Médio |
| RSK-16 | FOR | NBS prioriza outros clientes e reduz dedicação ao GAB | 3 | 3 | **9** | Médio |
| RSK-17 | FIN | Fiscal Defender aciona cláusula contratual ao ser notificado da substituição | 2 | 3 | **6** | Médio |
| RSK-18 | TEC | Módulo NBS não atende requisitos de performance em ambiente de produção GAB | 2 | 4 | **8** | Médio |

---

### 2.2 Fichas Detalhadas de Riscos

---

#### RSK-01 | Governança | Sponsor Executivo Não Identificado

| Campo | Detalhe |
|---|---|
| **Categoria** | GOV — Governança e Patrocínio |
| **Descrição** | Nenhum Sponsor executivo foi formalmente designado para o projeto até a data de referência. |
| **Causa Raiz** | Falta de definição na estrutura de governança corporativa entre as divisões afetadas (Comércio: Contabilidade, Financeiro, Jurídico); ausência de processo formal de abertura de projetos com designação de Sponsor. |
| **Consequência** | Projeto sem autoridade para decisões críticas de escopo, resolução de conflitos entre áreas, aprovação de orçamento e negociação com NBS. Todas as demais condições bloqueantes permanecem abertas indefinidamente. |
| **Probabilidade** | 5 — Quase Certo (condição já ativa em 15/05/2026) |
| **Impacto** | 5 — Catastrófico |
| **Score** | **25 — Crítico** |
| **Estratégia de Resposta** | Confrontar (eliminar a causa raiz) |
| **Ação Preventiva** | Convocar reunião de abertura com diretoria da Divisão Comércio até 20/05/2026 para designação formal do Sponsor; incluir na pauta a aprovação do Termo de Abertura do Projeto (TAP). |
| **Ação de Contingência** | Se prazo 25/05/2026 não for cumprido, suspender formalmente o projeto e comunicar à diretoria que o go-live de 30/10/2026 está em risco; solicitar decisão executiva de continuidade ou cancelamento. |
| **Dono do Risco** | VMO Autônomo (escalação para diretoria da Divisão Comércio) |
| **Prazo de Monitoramento** | Monitoramento diário até 25/05/2026 (condição bloqueante CB-01) |

---

#### RSK-02 | Contratual | Acordo NBS Sem Verificação Documental

| Campo | Detalhe |
|---|---|
| **Categoria** | CTR — Contratual / Jurídico |
| **Descrição** | O acordo que define o módulo NBS como contrapartida contratual sem custo adicional não foi verificado documentalmente. |
| **Causa Raiz** | Acordo estabelecido verbalmente ou em comunicações informais durante negociação do contrato ERP; ausência de cláusula específica no contrato formalizado ou aditivo. |
| **Consequência** | A premissa central do projeto (custo zero de desenvolvimento = ROI de R$78K/ano) pode ser invalidada; NBS pode cobrar pelo desenvolvimento; projeto perde justificativa financeira e pode ser cancelado. |
| **Probabilidade** | 4 — Provável (ausência de verificação confirmada) |
| **Impacto** | 5 — Catastrófico |
| **Score** | **20 — Crítico** |
| **Estratégia de Resposta** | Confrontar (verificação imediata e formalização) |
| **Ação Preventiva** | Área Jurídica deve revisar contrato ERP e todos os aditivos até 30/05/2026; solicitar declaração escrita da NBS confirmando o escopo e custo zero; lavrar aditivo contratual se necessário. |
| **Ação de Contingência** | Se acordo não puder ser verificado ou não existir formalmente, recalcular o business case com custo de desenvolvimento NBS; avaliar manutenção do Fiscal Defender vs. nova contratação de desenvolvimento. |
| **Dono do Risco** | Jurídico GAB (com apoio do Sponsor a ser designado) |
| **Prazo de Monitoramento** | Monitoramento diário até 30/05/2026 (condição bloqueante CB-02) |

---

#### RSK-03 | Fornecedor | Atrasos da NBS no Desenvolvimento

| Campo | Detalhe |
|---|---|
| **Categoria** | FOR — Fornecedor / Dependência Externa |
| **Descrição** | A NBS, como único fornecedor responsável pelo desenvolvimento do módulo, entrega com atraso em relação ao cronograma previsto (jul–set/2026). |
| **Causa Raiz** | GAB não tem controle sobre o backlog e a capacidade da NBS; o módulo como contrapartida contratual pode ter menor prioridade frente a projetos pagos da NBS; estimativas de prazo estabelecidas sem baseline técnico. |
| **Consequência** | UAT não pode iniciar conforme planejado (set/2026); go-live de 30/10/2026 é comprometido; contrato do Fiscal Defender precisa ser prorrogado (custo adicional); risco de período sem cobertura de compliance. |
| **Probabilidade** | 4 — Provável |
| **Impacto** | 4 — Alto |
| **Score** | **16 — Crítico** |
| **Estratégia de Resposta** | Mitigar (reduzir probabilidade via SLA contratual e mitigar impacto via buffer de prazo) |
| **Ação Preventiva** | Incluir no aditivo contratual cláusulas de SLA de entrega com multas; estabelecer marcos de entrega intermediários (milestones mensais jul–set); designar ponto focal técnico GAB para acompanhamento semanal. |
| **Ação de Contingência** | Se atraso > 4 semanas for detectado até ago/2026, acionar cláusula contratual; avaliar prorrogação do contrato Fiscal Defender por 6 meses (R$39K); revisar go-live para mar/2027. |
| **Dono do Risco** | Gerente do Projeto + Jurídico GAB |
| **Prazo de Monitoramento** | Semanal a partir de jul/2026; mensal nas fases anteriores |

---

#### RSK-04 | Compliance | Descontinuidade do Fiscal Defender Antes da Prontidão do Módulo NBS

| Campo | Detalhe |
|---|---|
| **Categoria** | CMP — Compliance Fiscal e Regulatório |
| **Descrição** | O contrato do Fiscal Defender é encerrado antes que o módulo NBS esteja homologado e em produção, gerando lacuna na cobertura de compliance fiscal. |
| **Causa Raiz** | Planejamento de rescisão do Fiscal Defender atrelado ao go-live do módulo NBS sem margem de segurança; atrasos no desenvolvimento (RSK-03) podem criar janela de exposição; rescisão antecipada por iniciativa do Fiscal Defender após notificação. |
| **Consequência** | GAB opera sem ferramenta de compliance fiscal obrigatório (SPED, EFD, DCTF, etc.); risco de autuações fiscais, multas e sanções; impacto reputacional com receita federal e SEFAZ. |
| **Probabilidade** | 3 — Possível |
| **Impacto** | 5 — Catastrófico |
| **Score** | **15 — Crítico** |
| **Estratégia de Resposta** | Mitigar + Transferir parcialmente |
| **Ação Preventiva** | Manter contrato Fiscal Defender ativo até 30 dias após go-live confirmado do módulo NBS; incluir cláusula de extensão de 90 dias no contrato Fiscal Defender como seguro; não notificar o Fiscal Defender antes de set/2026. |
| **Ação de Contingência** | Se lacuna for iminente (< 30 dias sem cobertura), prorrogar Fiscal Defender emergencialmente; acionar fornecedor backup de compliance; acionar equipe fiscal interna para processos manuais temporários com suporte de consultoria externa. |
| **Dono do Risco** | Gestor Contabilidade + Jurídico GAB |
| **Prazo de Monitoramento** | Mensal até set/2026; semanal a partir de out/2026 |

---

#### RSK-05 | Recursos | Disponibilidade Insuficiente das Equipes de UAT

| Campo | Detalhe |
|---|---|
| **Categoria** | REC — Recursos Humanos / Disponibilidade |
| **Descrição** | As equipes de Contabilidade, Financeiro e Jurídico não têm disponibilidade suficiente para executar UAT com qualidade no período previsto (set–out/2026). |
| **Causa Raiz** | Equipes operacionais com carga de trabalho de rotina de 100%; estimativa de 50% de disponibilidade para UAT é otimista frente ao período (fechamento trimestral e obrigações fiscais de out/2026); ausência de liberação formal de dedicação. |
| **Consequência** | UAT executado de forma superficial aumenta risco de bugs em produção; atraso no ciclo de UAT comprime o go-live; erros de compliance passam para produção. |
| **Probabilidade** | 4 — Provável |
| **Impacto** | 3 — Moderado |
| **Score** | **12 — Alto** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Formalizar com os gestores das áreas a dedicação de UAT antes do kick-off (jun/2026); dimensionar equipe mínima de 2 usuários por área com liberação de 40% da carga; planejar UAT em ciclos de 2 semanas com marcos claros. |
| **Ação de Contingência** | Se disponibilidade < 30%, contratar consultoria externa para suporte ao UAT (R$8K–R$12K); estender período de UAT em 2 semanas absorvendo folga do cronograma. |
| **Dono do Risco** | Gerente do Projeto + Gestores de Área |
| **Prazo de Monitoramento** | Quinzenal; confirmação formal até jun/2026 |

---

#### RSK-06 | Fornecedor | Descontinuidade ou Insolvência da NBS

| Campo | Detalhe |
|---|---|
| **Categoria** | FOR — Fornecedor / Dependência Externa |
| **Descrição** | A NBS encerra operações, é adquirida por terceiro ou passa por reestruturação que compromete a entrega do módulo ou o suporte futuro do ERP. |
| **Causa Raiz** | Dependência de fornecedor único para ERP e para o módulo de compliance; mercado de ERPs de médio porte sujeito a consolidações e aquisições; GAB não tem acesso ao código-fonte ou alternativa tecnológica equivalente. |
| **Consequência** | Projeto cancelado; GAB precisa contratar solução alternativa de compliance (impacto > R$100K) e eventual migração de ERP no longo prazo; perda do investimento de integração. |
| **Probabilidade** | 2 — Improvável |
| **Impacto** | 5 — Catastrófico |
| **Score** | **10 — Alto** |
| **Estratégia de Resposta** | Aceitar + Mitigar (manter plano de contingência de fornecedor) |
| **Ação Preventiva** | Monitorar saúde financeira da NBS; incluir no contrato cláusula de escrow de código-fonte; avaliar fornecedores alternativos de compliance como fallback. |
| **Ação de Contingência** | Acionar cláusula de escrow; contratar emergencialmente ferramenta de compliance alternativa (Totvs, Synchro ou equivalente); avaliar continuidade do Fiscal Defender durante transição. |
| **Dono do Risco** | Jurídico GAB + Sponsor |
| **Prazo de Monitoramento** | Trimestral |

---

#### RSK-07 | Tecnologia | Incompatibilidade de Integração com Sistemas Legados GAB

| Campo | Detalhe |
|---|---|
| **Categoria** | TEC — Tecnologia / Integração |
| **Descrição** | O módulo NBS não integra adequadamente com sistemas adjacentes da GAB (faturamento, contas a pagar, controle de estoque, sistemas da divisão Comércio). |
| **Causa Raiz** | Customizações históricas no ERP GAB não documentadas; interfaces desenvolvidas para o Fiscal Defender que não têm equivalente no módulo NBS; falta de análise de gap técnico antes do kick-off. |
| **Consequência** | Módulo entregue pela NBS requer adaptações adicionais não previstas; desenvolvimento extra pode ter custo; go-live atrasado; dados fiscais gerados com inconsistências. |
| **Probabilidade** | 3 — Possível |
| **Impacto** | 4 — Alto |
| **Score** | **12 — Alto** |
| **Estratégia de Resposta** | Mitigar (antecipar análise técnica) |
| **Ação Preventiva** | Realizar levantamento técnico de integrações (analysis gap) antes do kick-off formal; documentar todas as interfaces do Fiscal Defender com outros sistemas; entregar à NBS antes do início do desenvolvimento (jul/2026). |
| **Ação de Contingência** | Se gaps identificados em UAT, negociar com NBS cobertura como parte do contrato; se recusado, orçar desenvolvimento de middleware (R$15K–R$25K estimado). |
| **Dono do Risco** | Arquiteto Técnico GAB + Ponto Focal NBS |
| **Prazo de Monitoramento** | Quinzenal a partir de jun/2026 |

---

#### RSK-08 | Compliance | Mudança na Legislação Fiscal Durante o Projeto

| Campo | Detalhe |
|---|---|
| **Categoria** | CMP — Compliance Fiscal e Regulatório |
| **Descrição** | Alteração de legislação fiscal federal ou estadual (SPED, EFD-ICMS/IPI, NF-e, eSocial, reforma tributária) durante o período de desenvolvimento e homologação impõe novos requisitos ao módulo. |
| **Causa Raiz** | Ambiente regulatório brasileiro em constante mudança; Reforma Tributária em implementação (IBS, CBS, IS) com regulamentações sendo publicadas; prazo de 12 meses expõe o projeto a ciclos legislativos. |
| **Consequência** | Módulo entregue pela NBS em set/2026 pode não atender requisitos legais vigentes em out/2026; retrabalho de desenvolvimento; atraso no go-live; GAB não pode substituir Fiscal Defender. |
| **Probabilidade** | 3 — Possível |
| **Impacto** | 4 — Alto |
| **Score** | **12 — Alto** |
| **Estratégia de Resposta** | Mitigar + Transferir (responsabilidade contratual da NBS) |
| **Ação Preventiva** | Incluir no contrato cláusula de atualização legislativa como responsabilidade da NBS sem custo adicional; monitorar publicações do Diário Oficial e comunicar NBS imediatamente; incluir período de buffer pós-UAT para adaptações regulatórias. |
| **Ação de Contingência** | Se mudança relevante publicada antes de set/2026, solicitar sprint adicional da NBS; se após UAT, avaliar go-live parcial com funcionalidades estáveis. |
| **Dono do Risco** | Equipe Fiscal/Contabilidade + Jurídico |
| **Prazo de Monitoramento** | Mensal (monitoramento de legislação contínuo) |

---

#### RSK-09 | Operacional | Recesso de Dezembro Impede Encerramento Formal

| Campo | Detalhe |
|---|---|
| **Categoria** | OPE — Operacional / Processo |
| **Descrição** | O recesso coletivo de dezembro/2026 impede a conclusão das atividades de encerramento do projeto (lições aprendidas, documentação, descomissionamento do Fiscal Defender, aceite formal). |
| **Causa Raiz** | Go-live previsto para 30/10/2026 deixa apenas ~60 dias para encerramento antes do recesso; atividades de pós-implantação (estabilização, treinamento final, aceite) podem se estender; recesso reduz disponibilidade de equipes a partir de 20/12. |
| **Consequência** | Projeto formalmente aberto em 2027; custos de encerramento carregados para novo exercício fiscal; Fiscal Defender não rescindido no prazo impactando R$78K de economia anual. |
| **Probabilidade** | 4 — Provável |
| **Impacto** | 3 — Moderado |
| **Score** | **12 — Alto** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Planejar marco de encerramento até 15/12/2026; iniciar processo de rescisão do Fiscal Defender em nov/2026; documentar lições aprendidas durante estabilização (nov/dez) e não após. |
| **Ação de Contingência** | Formalizar encerramento parcial em 15/12 com pendências residuais documentadas; retomar em jan/2027 com responsável designado; garantir rescisão do Fiscal Defender independentemente do encerramento formal. |
| **Dono do Risco** | Gerente do Projeto |
| **Prazo de Monitoramento** | Mensal até out/2026; semanal em nov–dez/2026 |

---

#### RSK-10 | Governança | Conflito de Prioridades Entre Áreas

| Campo | Detalhe |
|---|---|
| **Categoria** | GOV — Governança e Patrocínio |
| **Descrição** | As três áreas impactadas (Contabilidade, Financeiro, Jurídico) têm requisitos divergentes para o módulo, gerando conflito de prioridades durante a definição de escopo e UAT. |
| **Causa Raiz** | Ausência de Sponsor com autoridade sobre as três áreas; cada área tem gestor próprio com agenda e prioridades distintas; não há processo estabelecido de resolução de conflitos de requisitos. |
| **Consequência** | Escopo indefinido ou em constante expansão (scope creep); ciclos de UAT mais longos; decisões não tomadas atrasam fases críticas. |
| **Probabilidade** | 3 — Possível |
| **Impacto** | 3 — Moderado |
| **Score** | **9 — Médio** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Estabelecer comitê de governança com representante de cada área e Sponsor no kick-off; documentar matriz de decisão RACI; congelar escopo após kick-off com processo formal de change request. |
| **Ação de Contingência** | Escalação imediata ao Sponsor para decisão de desempate; se impasse persistir, priorizar requisitos de compliance regulatório sobre preferências operacionais. |
| **Dono do Risco** | Sponsor + Gerente do Projeto |
| **Prazo de Monitoramento** | Quinzenal |

---

#### RSK-11 | Tecnologia | Perda ou Corrupção de Dados Fiscais Históricos na Migração

| Campo | Detalhe |
|---|---|
| **Categoria** | TEC — Tecnologia / Integração |
| **Descrição** | A migração de dados históricos fiscais do Fiscal Defender para o módulo NBS resulta em perda, corrupção ou inconsistência de registros. |
| **Causa Raiz** | Diferença de modelos de dados entre Fiscal Defender e módulo NBS; ausência de ferramenta homologada de migração; dados históricos podem ter formatações legadas incompatíveis. |
| **Consequência** | GAB não consegue auditar obrigações fiscais retroativas; risco de autuação em caso de fiscalização; obrigatoriedade de reprocessamento manual de períodos anteriores. |
| **Probabilidade** | 2 — Improvável |
| **Impacto** | 5 — Catastrófico |
| **Score** | **10 — Alto** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Incluir plano de migração de dados no escopo do UAT; definir período mínimo de histórico a migrar (5 anos de SPED); executar validação cruzada de totalizadores pré e pós-migração; manter backup do Fiscal Defender por 12 meses pós-go-live. |
| **Ação de Contingência** | Manter acesso somente-leitura ao Fiscal Defender por 24 meses; contratar consultoria de migração de dados se qualidade insuficiente (R$10K–R$15K). |
| **Dono do Risco** | Arquiteto Técnico GAB + Contabilidade |
| **Prazo de Monitoramento** | Quinzenal durante UAT |

---

#### RSK-12 | Financeiro | Custos Residuais Acima do Previsto

| Campo | Detalhe |
|---|---|
| **Categoria** | FIN — Financeiro / Orçamentário |
| **Descrição** | Os custos residuais do projeto superam a estimativa de R$35.000 devido a necessidades não previstas de adequação, consultoria ou infraestrutura. |
| **Causa Raiz** | Estimativa de R$35K elaborada sem levantamento técnico detalhado; escopo técnico real desconhecido até análise de gap; riscos de integração e migração podem gerar custos adicionais. |
| **Consequência** | Impacto no orçamento da Divisão Comércio; necessidade de aprovação adicional de verba; comprometimento do ROI do projeto. |
| **Probabilidade** | 3 — Possível |
| **Impacto** | 3 — Moderado |
| **Score** | **9 — Médio** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Revisar e detalhar estimativa de R$35K após análise de gap técnico; incluir reserva de contingência formal no orçamento; obter aprovação orçamentária ampliada preventivamente. |
| **Ação de Contingência** | Acionar reserva de contingência; solicitar aprovação emergencial ao Sponsor se ultrapassar 20% do orçamento base. |
| **Dono do Risco** | Gerente do Projeto + Financeiro GAB |
| **Prazo de Monitoramento** | Mensal |

---

#### RSK-13 | Recursos | Rotatividade de Pessoal-Chave

| Campo | Detalhe |
|---|---|
| **Categoria** | REC — Recursos Humanos / Disponibilidade |
| **Descrição** | Membros-chave das equipes de projeto (especialista fiscal, arquiteto técnico, ponto focal NBS) deixam a empresa ou são realocados durante os 12 meses do projeto. |
| **Causa Raiz** | Projeto com duração de 12+ meses exposto ao turnover natural; profissionais de compliance fiscal têm alta demanda no mercado; realocações internas possíveis dada a natureza matricial da estrutura. |
| **Consequência** | Perda de conhecimento acumulado; retrabalho de alinhamento; atraso de 2–6 semanas para onboarding de substituto; qualidade técnica do UAT comprometida. |
| **Probabilidade** | 2 — Improvável |
| **Impacto** | 4 — Alto |
| **Score** | **8 — Médio** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Documentar conhecimento tácito desde o kick-off; designar backup para cada papel crítico; registrar decisões e configurações em wiki do projeto. |
| **Ação de Contingência** | Acionar substituto designado; contatar consultoria externa para cobertura emergencial (R$5K–R$10K); solicitar suporte técnico NBS para repassar conhecimento. |
| **Dono do Risco** | Gerente do Projeto + RH |
| **Prazo de Monitoramento** | Trimestral |

---

#### RSK-14 | Operacional | Resistência à Mudança pelos Usuários-Chave

| Campo | Detalhe |
|---|---|
| **Categoria** | OPE — Operacional / Processo |
| **Descrição** | Usuários das áreas de Contabilidade, Financeiro e Jurídico resistem à adoção do módulo NBS por familiaridade com o Fiscal Defender. |
| **Causa Raiz** | Usuários utilizam o Fiscal Defender há anos e têm workflows estabelecidos; módulo NBS pode ter interface ou processos diferentes; ausência de programa estruturado de gestão da mudança. |
| **Consequência** | UAT superficial com menor identificação de bugs; baixa adoção pós-go-live; erros operacionais no preenchimento de obrigações fiscais; retrabalho e reprocessamento. |
| **Probabilidade** | 3 — Possível |
| **Impacto** | 3 — Moderado |
| **Score** | **9 — Médio** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Incluir usuários-chave como co-owners do UAT desde o início; realizar demonstração comparativa (Fiscal Defender vs. módulo NBS) no kick-off; estruturar treinamento hands-on antes do go-live. |
| **Ação de Contingência** | Ampliar período de suporte pós-go-live de 30 para 60 dias; manter "linha direta" NBS para dúvidas operacionais; considerar consultoria de change management (R$5K). |
| **Dono do Risco** | Gerente do Projeto + Líderes de Área |
| **Prazo de Monitoramento** | Quinzenal durante UAT e pós-go-live |

---

#### RSK-15 | Contratual | NBS Reivindica Cobrança por Funcionalidades "Fora do Escopo"

| Campo | Detalhe |
|---|---|
| **Categoria** | CTR — Contratual / Jurídico |
| **Descrição** | Durante ou após o desenvolvimento, a NBS alega que funcionalidades solicitadas pelo GAB estão além do escopo da contrapartida contratual e exige pagamento adicional. |
| **Causa Raiz** | Escopo da contrapartida não detalhado no contrato; ausência de especificação funcional homologada antes do desenvolvimento; requisitos das três áreas GAB podem expandir além do acordado. |
| **Consequência** | Custo de desenvolvimento não previsto (R$30K–R$80K estimado); disputa contratual com NBS; atraso no desenvolvimento durante negociação; risco de perda de funcionalidades críticas. |
| **Probabilidade** | 2 — Improvável |
| **Impacto** | 4 — Alto |
| **Score** | **8 — Médio** |
| **Estratégia de Resposta** | Mitigar + Transferir |
| **Ação Preventiva** | Formalizar escopo detalhado do módulo antes do kick-off com assinatura de ambas as partes; limitar requisitos aos contemplados na especificação assinada; qualquer adição passa por change request formal com aprovação NBS. |
| **Ação de Contingência** | Acionar cláusula contratual e Jurídico GAB para disputa; priorizar entrega do escopo original sem funcionalidades adicionais. |
| **Dono do Risco** | Jurídico GAB + Sponsor |
| **Prazo de Monitoramento** | Mensal durante desenvolvimento |

---

#### RSK-16 | Fornecedor | NBS Reduz Dedicação ao GAB por Outros Clientes

| Campo | Detalhe |
|---|---|
| **Categoria** | FOR — Fornecedor / Dependência Externa |
| **Descrição** | A NBS redireciona capacidade de desenvolvimento para projetos de clientes pagantes, reduzindo o time alocado ao módulo GAB (contrapartida sem receita direta). |
| **Causa Raiz** | Para a NBS, o módulo GAB é contrapartida contratual sem receita; clientes pagantes têm prioridade natural; ausência de penalidade contratual por atraso incentiva deprioritização. |
| **Consequência** | Ritmo de desenvolvimento abaixo do necessário; atrasos graduais que se acumulam; entregas de qualidade inferior por equipe júnior ou subdimensionada. |
| **Probabilidade** | 3 — Possível |
| **Impacto** | 3 — Moderado |
| **Score** | **9 — Médio** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Incluir no contrato garantia de alocação mínima (nomes ou FTEs); exigir relatórios de progresso quinzenais; estabelecer penalidades por atraso além de X semanas. |
| **Ação de Contingência** | Escalar ao executivo de contas NBS; usar alavancagem do contrato ERP principal para pressionar priorização; avaliar desenvolvimento paralelo por terceiro (R$40K–R$60K). |
| **Dono do Risco** | Gerente do Projeto + Sponsor |
| **Prazo de Monitoramento** | Quinzenal durante jul–set/2026 |

---

#### RSK-17 | Financeiro | Fiscal Defender Aciona Cláusula Contratual ao Ser Notificado

| Campo | Detalhe |
|---|---|
| **Categoria** | FIN — Financeiro / Orçamentário |
| **Descrição** | Ao ser notificado da rescisão, o Fiscal Defender aciona cláusula de multa rescisória ou de não-cancelamento antecipado, gerando custo não previsto. |
| **Causa Raiz** | Contratos de SaaS/licença frequentemente contêm multa de rescisão antecipada; prazo de vigência do contrato pode não coincidir com o go-live planejado (out/2026); cláusula de renovação automática pode ter sido ativada. |
| **Consequência** | Custo adicional de R$10K–R$30K de multa rescisória; impacto no ROI do projeto; possível necessidade de manter o Fiscal Defender até o vencimento natural. |
| **Probabilidade** | 2 — Improvável |
| **Impacto** | 3 — Moderado |
| **Score** | **6 — Médio** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Revisar contrato Fiscal Defender imediatamente (jun/2026); identificar data de vencimento, cláusula de rescisão e multas; planejar notificação dentro do prazo mínimo contratual. |
| **Ação de Contingência** | Negociar com Fiscal Defender encerramento sem multa mediante demonstração de contrapartida contratual; se inviável, absorver multa no orçamento do projeto. |
| **Dono do Risco** | Jurídico GAB + Financeiro |
| **Prazo de Monitoramento** | Ação imediata em jun/2026; monitoramento mensal |

---

#### RSK-18 | Tecnologia | Módulo NBS Não Atende Requisitos de Performance

| Campo | Detalhe |
|---|---|
| **Categoria** | TEC — Tecnologia / Integração |
| **Descrição** | O módulo NBS, em ambiente de produção do GAB, apresenta performance insatisfatória (lentidão, timeout, falhas em processamento em lote de obrigações fiscais). |
| **Causa Raiz** | Módulo desenvolvido em ambiente de desenvolvimento com dados sintéticos; volume de dados e complexidade do ambiente de produção GAB não replicados no desenvolvimento; testes de carga não previstos no escopo da NBS. |
| **Consequência** | Módulo aprovado no UAT mas com degradação em produção; atrasos no cumprimento de obrigações fiscais; instabilidade no início de operação; necessidade de otimização pós-go-live. |
| **Probabilidade** | 2 — Improvável |
| **Impacto** | 4 — Alto |
| **Score** | **8 — Médio** |
| **Estratégia de Resposta** | Mitigar |
| **Ação Preventiva** | Incluir teste de carga/performance no plano de UAT com dados reais (anonimizados); especificar critérios de aceite de performance (ex.: processamento de SPED em < X minutos); validar dimensionamento de infraestrutura. |
| **Ação de Contingência** | Escalar para NBS como bug crítico pós-go-live; manter Fiscal Defender em standby por 30 dias como fallback; acionar SLA de correção contratual. |
| **Dono do Risco** | Arquiteto Técnico GAB + NBS |
| **Prazo de Monitoramento** | Quinzenal durante UAT; semanal nos primeiros 30 dias pós-go-live |

---

## 3. Matriz de Probabilidade × Impacto (P×I)

> Posicionamento dos riscos na matriz 5×5. Leitura: linha = Probabilidade (P), coluna = Impacto (I).

|  | **I=1** Insignificante | **I=2** Baixo | **I=3** Moderado | **I=4** Alto | **I=5** Catastrófico |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **P=5** Quase Certo | — | — | — | — | 🔴 **RSK-01** |
| **P=4** Provável | — | — | RSK-09 | RSK-03 | 🔴 **RSK-02** |
| **P=3** Possível | — | — | RSK-10, RSK-14, RSK-16 | RSK-07, RSK-08 | 🟠 RSK-04 |
| **P=2** Improvável | — | — | RSK-17 | RSK-13, RSK-15, RSK-18 | RSK-06, RSK-11 |
| **P=1** Raro | — | — | — | — | — |

**Legenda de Classificação:**

| Score | Classificação | Cor |
|---|---|---|
| ≥ 15 | Crítico | 🔴 Vermelho |
| 10–14 | Alto | 🟠 Laranja |
| 6–9 | Médio | 🟡 Amarelo |
| 1–5 | Baixo | 🟢 Verde |

**Scores detalhados para mapeamento na matriz:**

| ID | P | I | Score | Faixa |
|---|:---:|:---:|:---:|---|
| RSK-01 | 5 | 5 | 25 | 🔴 Crítico |
| RSK-02 | 4 | 5 | 20 | 🔴 Crítico |
| RSK-03 | 4 | 4 | 16 | 🔴 Crítico |
| RSK-04 | 3 | 5 | 15 | 🔴 Crítico |
| RSK-05 | 4 | 3 | 12 | 🟠 Alto |
| RSK-06 | 2 | 5 | 10 | 🟠 Alto |
| RSK-07 | 3 | 4 | 12 | 🟠 Alto |
| RSK-08 | 3 | 4 | 12 | 🟠 Alto |
| RSK-09 | 4 | 3 | 12 | 🟠 Alto |
| RSK-10 | 3 | 3 | 9 | 🟡 Médio |
| RSK-11 | 2 | 5 | 10 | 🟠 Alto |
| RSK-12 | 3 | 3 | 9 | 🟡 Médio |
| RSK-13 | 2 | 4 | 8 | 🟡 Médio |
| RSK-14 | 3 | 3 | 9 | 🟡 Médio |
| RSK-15 | 2 | 4 | 8 | 🟡 Médio |
| RSK-16 | 3 | 3 | 9 | 🟡 Médio |
| RSK-17 | 2 | 3 | 6 | 🟡 Médio |
| RSK-18 | 2 | 4 | 8 | 🟡 Médio |

---

## 4. Reserva de Contingência

### 4.1 Valor Monetário Esperado (VME)

O VME é calculado como: **VME = Probabilidade (decimal) × Impacto Financeiro Estimado**

| ID | Risco | Prob. (%) | Impacto Financeiro Estimado | VME |
|---|---|:---:|---|---|
| RSK-02 | Acordo NBS inválido — necessidade de contratar desenvolvimento | 70% | R$ 80.000 (desenvolvimento externo mínimo) | **R$ 56.000** |
| RSK-03 | Atraso NBS — prorrogação do Fiscal Defender por 6 meses | 60% | R$ 39.000 (6 × R$6.500/mês) | **R$ 23.400** |
| RSK-04 | Lacuna de compliance — consultoria emergencial + multa fiscal estimada | 40% | R$ 50.000 (conservative; multas variam muito) | **R$ 20.000** |
| RSK-05 | UAT insuficiente — contratação de consultoria de apoio | 60% | R$ 10.000 | **R$ 6.000** |
| RSK-07 | Gaps de integração — desenvolvimento de middleware | 40% | R$ 20.000 | **R$ 8.000** |
| RSK-09 | Recesso — prorrogação contrato Fiscal Defender 1 mês | 60% | R$ 6.500 | **R$ 3.900** |
| RSK-11 | Corrupção de dados — consultoria de migração | 20% | R$ 12.000 | **R$ 2.400** |
| RSK-12 | Custos residuais acima do previsto (25% de overrun sobre R$35K) | 40% | R$ 8.750 | **R$ 3.500** |
| RSK-13 | Rotatividade — consultoria emergencial | 20% | R$ 8.000 | **R$ 1.600** |
| RSK-15 | Cobrança NBS por funcionalidades fora do escopo | 25% | R$ 40.000 | **R$ 10.000** |
| RSK-16 | Desenvolvimento alternativo por terceiro (parcial) | 30% | R$ 20.000 | **R$ 6.000** |
| RSK-17 | Multa rescisória Fiscal Defender | 20% | R$ 15.000 | **R$ 3.000** |
| RSK-18 | Otimização de performance pós-go-live | 20% | R$ 8.000 | **R$ 1.600** |
| **TOTAL VME** | | | | **R$ 145.400** |

### 4.2 Proposta de Reserva de Contingência

| Componente | Valor | Justificativa |
|---|---|---|
| **Reserva de Contingência Identificada** | R$ 145.400 | VME calculado sobre riscos com impacto financeiro estimável |
| **Reserva de Gerenciamento (10% do total)** | R$ 18.000 | Riscos desconhecidos (unknown-unknowns), estimado como 10% da reserva de contingência |
| **Reserva Total Recomendada** | **R$ 163.400** | |

**Nota crítica:** O VME é dominado pelo RSK-02 (R$56K) que representa a invalidação da premissa central do projeto. A verificação documental do acordo NBS (CB-02) deve ser tratada como prioridade absoluta pois, se o risco se materializar, o business case do projeto colapsa. O valor de R$80K de desenvolvimento externo anula completamente a economia de R$78K/ano prevista no primeiro ano, tornando o projeto financeiramente neutro na melhor hipótese.

**Recomendação:** Aprovar orçamento total de projeto de R$35.000 (operacional) + R$163.400 (reservas) = **R$198.400**, condicionado à verificação do acordo NBS. Sem verificação documental do CB-02, recomendar suspensão da aprovação orçamentária.

---

## 5. Top 5 Riscos Críticos — Análise Aprofundada

### 5.1 RSK-01 — Sponsor Executivo Não Identificado (Score: 25)

**Por que é o risco #1:** Um projeto sem Sponsor é um projeto sem governança. Todas as demais respostas a riscos dependem de autoridade executiva para decisão — incluindo a resolução de CB-01 e CB-02. Em termos práticos, RSK-01 amplifica todos os outros riscos do registro.

**Cenários de materialização:**
- *Cenário A (Melhor):* Sponsor designado até 25/05/2026 — projeto segue com autoridade.
- *Cenário B (Esperado):* Sponsor designado com atraso (jun/2026) — kick-off atrasado, cronograma comprime.
- *Cenário C (Pior):* Sponsor não designado até jul/2026 — projeto suspenso; go-live de out/2026 inviável.

**Indicadores de alerta (Early Warning Signs):**
- Ausência de resposta da diretoria após 3 dias úteis da convocação
- Nenhum executivo comparece à reunião de kick-off
- Decisões críticas sendo adiadas por falta de "responsável"

**Resposta estruturada:**
1. VMO Autônomo formaliza solicitação escrita à diretoria da Divisão Comércio até 16/05/2026
2. Se sem resposta até 20/05, escalação ao CEO/Diretor Geral do GAB
3. Se sem resposta até 25/05, emitir relatório de risco formal declarando projeto em risco crítico
4. Suspensão formal do projeto com comunicado à diretoria em 26/05 se não resolvido

---

### 5.2 RSK-02 — Acordo NBS Sem Verificação Documental (Score: 20)

**Por que é o risco #2:** A premissa de "custo zero" é o principal diferencial que torna o projeto atraente (ROI de R$78K/ano). Sem verificação, todo o planejamento baseia-se em premissa não validada. Este risco tem o maior VME individual do registro (R$56K).

**Cenários de materialização:**
- *Cenário A (Melhor):* Acordo verificado e cláusula específica encontrada no contrato.
- *Cenário B (Parcial):* Acordo verificado mas com escopo limitado — requer negociação de aditivo.
- *Cenário C (Pior):* Acordo inexistente formalmente — NBS cobra pelo desenvolvimento.

**Análise de impacto no business case:**

| Cenário | Custo Desenvolvimento | Economia Anual | ROI Ano 1 |
|---|---|---|---|
| Custo zero confirmado | R$ 0 | R$ 78K | **R$ 78K positivo** |
| NBS cobra R$40K | R$ 40K | R$ 78K | **R$ 38K positivo** |
| NBS cobra R$80K | R$ 80K | R$ 78K | **R$ 2K negativo** |
| NBS cobra R$150K | R$ 150K | R$ 78K | **R$ 72K negativo** |

**Resposta estruturada:**
1. Jurídico acessa contrato ERP original e todos os aditivos até 22/05/2026
2. Verificar ata de reunião ou e-mails que documentam o acordo
3. Solicitar confirmação escrita da NBS até 27/05/2026
4. Se não encontrado, iniciar negociação de aditivo antes de 30/05/2026
5. Recalcular business case e submeter para aprovação do Sponsor antes de continuar

---

### 5.3 RSK-03 — Atrasos da NBS no Desenvolvimento (Score: 16)

**Por que é o risco #3:** GAB está em posição de dependência total de um fornecedor que não tem incentivo financeiro direto para priorizar este projeto. O risco é estrutural e permanente durante todo o ciclo de desenvolvimento (jul–set/2026).

**Análise de dependência:**

```
GAB (sem controle) ──depende de──> NBS (desenvolvimento)
                                        |
                                        ├── Prioridade: Clientes pagantes
                                        ├── Prioridade: Projetos internos
                                        └── Prioridade: GAB (contrapartida = BAIXA)
```

**Modelo de monitoramento:**

| Marco | Data Prevista | Entregável | Critério de Aceite |
|---|---|---|---|
| M1 — Especificação | 15/07/2026 | Documento de requisitos assinado | Aprovação GAB |
| M2 — Protótipo | 15/08/2026 | Versão alpha para revisão técnica | Funcionalidades core presentes |
| M3 — Beta | 15/09/2026 | Versão para UAT | Critérios de entrada UAT atendidos |
| M4 — RC | 10/10/2026 | Release candidate | Zero bugs críticos |

**Gatilho de escalonamento:** Qualquer marco com atraso > 10 dias úteis aciona reunião de crise com NBS e análise de impacto no go-live.

---

### 5.4 RSK-04 — Descontinuidade do Fiscal Defender (Score: 15)

**Por que é o risco #4:** Compliance fiscal não tem tolerância a interrupções. Uma lacuna de 30 dias sem ferramenta pode gerar multas automáticas por atraso na entrega de obrigações acessórias (SPED EFD, EFD-Contribuições, ECF, DCTF, etc.).

**Mapa de obrigações fiscais críticas (Divisão Comércio — referência):**

| Obrigação | Periodicidade | Multa por Atraso |
|---|---|---|
| SPED EFD ICMS/IPI | Mensal | R$1.500/mês + 1% do valor das operações |
| EFD-Contribuições | Mensal | R$1.500/mês |
| ECF | Anual | R$1.000/mês de atraso |
| DCTF | Mensal | R$500/mês ou 2% sobre débito |
| NFe/CTe | Diário | Multa por documento + cancelamento de inscrição |

**Janela crítica identificada:** Se o módulo NBS atrasar e o go-live sair de out para nov/2026, o período de nov é de fechamento fiscal intenso. Qualquer lacuna neste período é catastrófica.

**Resposta estruturada:**
- Cláusula no contrato Fiscal Defender: extensão emergencial de 90 dias sem multa
- Go/No-Go formal do Fiscal Defender somente após UAT aprovado (não antes)
- Plano B documentado: prestação de serviço manual com apoio de consultoria (R$5K/mês)

---

### 5.5 RSK-05 — Disponibilidade das Equipes de UAT (Score: 12)

**Por que é o #5:** UAT é o único mecanismo de controle que o GAB tem sobre a qualidade do módulo NBS. Se executado de forma precária, todos os outros riscos de qualidade e compliance passam para produção sem detecção.

**Análise de disponibilidade por área:**

| Área | Atividades de Rotina Conflitantes (set–out/2026) | Disponibilidade Real Estimada |
|---|---|---|
| Contabilidade | Fechamento 3T26, preparação ECF, SPED trimestral | 25–30% |
| Financeiro | Fechamento orçamentário trimestral, projeções 4T26 | 30–35% |
| Jurídico | Menor sazonalidade | 40–50% |

**Estratégia recomendada:**
- UAT em dois ciclos: 01–15/set (funcionalidades core) e 16–30/set (cenários de borda)
- Mínimo 2 usuários por área dedicados por ciclo
- Contratação de analista fiscal externo para complementar UAT (R$8K–R$10K se necessário)
- Critérios de saída do UAT documentados antes do início (não negociáveis)

---

## 6. Plano de Monitoramento de Riscos

### 6.1 Cadência de Revisão

| Fase do Projeto | Período | Frequência de Revisão | Responsável | Fórum |
|---|---|---|---|---|
| Sanação de Bloqueantes | mai/2026 | **Diária** (CB-01, CB-02) | PMO / VMO | Report diário ao Sponsor |
| Pré-Kick-off | mai–jun/2026 | Semanal | Gerente do Projeto | Reunião de status semanal |
| Desenvolvimento NBS | jul–set/2026 | Quinzenal | Gerente do Projeto | Comitê de acompanhamento |
| UAT | set–out/2026 | **Semanal** | Gerente do Projeto | Daily stand-up de UAT |
| Go-live e Estabilização | out–nov/2026 | **Semanal** | Gerente do Projeto | War room pós-go-live |
| Encerramento | nov–dez/2026 | Mensal | Gerente do Projeto | Reunião de encerramento |

### 6.2 Responsáveis por Categoria

| Categoria | Responsável Primário | Escalação |
|---|---|---|
| GOV — Governança | VMO Autônomo / PMO | Diretoria Divisão Comércio |
| FOR — Fornecedor | Gerente do Projeto | Sponsor + Jurídico |
| CTR — Contratual | Jurídico GAB | Sponsor |
| CMP — Compliance | Gestor Contabilidade | Diretor Financeiro |
| REC — Recursos | Gerente do Projeto | Gestores de Área |
| TEC — Tecnologia | Arquiteto Técnico GAB | CTO / Gerente de TI |
| OPE — Operacional | Gerente do Projeto | Sponsor |
| FIN — Financeiro | Gerente do Projeto + Financeiro | CFO |

### 6.3 Gatilhos de Escalação

Os gatilhos abaixo exigem escalação imediata ao Sponsor e comunicação ao Comitê Executivo:

| Gatilho | Ação Imediata | Prazo de Resposta |
|---|---|---|
| CB-01 não resolvido até 25/05/2026 | Suspensão formal do projeto; comunicado à diretoria | 24h |
| CB-02 não resolvido até 30/05/2026 | Revisão do business case; reunião de go/no-go | 48h |
| Atraso NBS > 10 dias úteis em qualquer marco | Reunião de crise com NBS; análise de impacto no go-live | 72h |
| Lacuna de compliance iminente (< 30 dias) | Prorrogação emergencial Fiscal Defender; plano de contingência | 24h |
| Custo projetado ultrapassa R$50.000 | Revisão orçamentária com Sponsor | 1 semana |
| Bug crítico de segurança fiscal em UAT | Stop de go-live; notificação NBS para correção emergencial | 24h |
| Saída de pessoal-chave | Acionamento de backup designado; avaliação de impacto | 1 semana |

### 6.4 Indicadores de Saúde do Projeto (KRIs — Key Risk Indicators)

| KRI | Meta | Sinal de Alerta | Fonte |
|---|---|---|---|
| % marcos NBS entregues no prazo | 100% | < 80% | Relatório quinzenal NBS |
| % disponibilidade equipe UAT | ≥ 40% | < 30% | Confirmação gestores de área |
| Dias até go-live vs. planejado | 0 dias de desvio | > 10 dias de desvio | Cronograma |
| Itens abertos de UAT (bugs críticos) | 0 críticos | ≥ 1 crítico | Plataforma de testes |
| Dias restantes com cobertura Fiscal Defender | > 60 dias após go-live | < 30 dias | Contrato |
| Orçamento utilizado vs. reserva | ≤ 70% da reserva | > 80% da reserva | Controle financeiro |

---

## 7. Riscos Residuais — Aceites Conscientes

Os riscos abaixo são aceitos mediante justificativa, sem plano de ação ativa além do monitoramento:

| ID | Risco | Score | Justificativa do Aceite | Condição de Revisão |
|---|---|:---:|---|---|
| RSK-06 | Descontinuidade/insolvência da NBS | 10 | Probabilidade baixa (2); empresa com histórico estabelecido; cobertura contratual existente; custo de monitoramento intensivo supera o benefício | Se indicadores financeiros da NBS deteriorarem; se houver notícia de M&A |
| RSK-13 | Rotatividade de pessoal-chave | 8 | Projeto de 12 meses com baixa probabilidade (2) de turnover crítico; custo de mitigação adicional (retenção) não justificado para projeto de R$35K | Se houver movimentação de mercado significativa ou sinalização interna de saída |
| RSK-17 | Multa rescisória Fiscal Defender | 6 | Probabilidade baixa (2); valor máximo estimado (R$15K) representa < 10% do benefício anual; verificação do contrato Fiscal Defender em jun/2026 é suficiente | Se revisão contratual revelar multa > R$20K |
| RSK-18 | Performance insuficiente módulo NBS | 8 | Probabilidade baixa (2); ambiente NBS é o mesmo ERP já em uso; issues de performance geralmente corrigíveis por configuração; plano de contingência (fallback Fiscal Defender) cobre o período | Se testes de carga em homologação revelarem degradação > 30% do Fiscal Defender |

**Declaração de aceite:** Os riscos residuais acima foram avaliados com base em análise de custo-benefício das respostas disponíveis. O aceite não implica desconsideração — todos estão sujeitos ao ciclo de monitoramento definido na seção 6 e serão reavaliados a cada revisão quinzenal/mensal conforme tabela de cadência.

---

## 8. Sumário Executivo de Riscos

### Distribuição por Classificação

| Classificação | Quantidade | % do total |
|---|---|---|
| 🔴 Crítico (≥15) | 4 | 22% |
| 🟠 Alto (10–14) | 6 | 33% |
| 🟡 Médio (6–9) | 8 | 45% |
| 🟢 Baixo (1–5) | 0 | 0% |
| **Total** | **18** | **100%** |

### Distribuição por Categoria

| Categoria | Riscos | Maior Score |
|---|---|---|
| FOR — Fornecedor | 3 (RSK-03, RSK-06, RSK-16) | 16 (RSK-03) |
| GOV — Governança | 2 (RSK-01, RSK-10) | 25 (RSK-01) |
| CTR — Contratual | 2 (RSK-02, RSK-15) | 20 (RSK-02) |
| CMP — Compliance | 2 (RSK-04, RSK-08) | 15 (RSK-04) |
| TEC — Tecnologia | 3 (RSK-07, RSK-11, RSK-18) | 12 (RSK-07) |
| REC — Recursos | 2 (RSK-05, RSK-13) | 12 (RSK-05) |
| OPE — Operacional | 2 (RSK-09, RSK-14) | 12 (RSK-09) |
| FIN — Financeiro | 2 (RSK-12, RSK-17) | 9 (RSK-12) |

### Ações Imediatas Requeridas (próximos 30 dias)

| Prioridade | Ação | Prazo | Responsável |
|---|---|---|---|
| 1 | Designação formal do Sponsor executivo | 25/05/2026 | Diretoria Divisão Comércio |
| 2 | Verificação documental do acordo NBS | 30/05/2026 | Jurídico GAB |
| 3 | Revisão do contrato Fiscal Defender (prazo e rescisão) | 15/06/2026 | Jurídico GAB |
| 4 | Formalização do escopo técnico do módulo com NBS | 15/06/2026 | Gerente do Projeto + NBS |
| 5 | Confirmação de disponibilidade das equipes de UAT | 30/06/2026 | Sponsor + Gestores de Área |

---

*Documento produzido por Pedro Perigo — Especialista em Gestão de Riscos, VMO Autônomo*
*Data: 2026-05-15 | Versão v5 | Próxima revisão: 2026-05-22 (após sanação das condições bloqueantes)*
