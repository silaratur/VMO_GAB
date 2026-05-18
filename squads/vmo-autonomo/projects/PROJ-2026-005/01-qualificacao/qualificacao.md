# Parecer de Qualificação de Demanda

---

## Cabeçalho

| Campo | Valor |
|---|---|
| **ID da Demanda** | DEM-2026-002 |
| **Código do Projeto** | PROJ-2026-005 |
| **Título** | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Data do Parecer** | 2026-05-15 |
| **Agente Responsável** | Felipe Filtro — Analista de Qualificação, VMO Autônomo |
| **Documento de Referência** | demanda-coletada.md (v1, 2026-05-15) |
| **Entrevista de Origem** | Fireflies ID 01KRP1TW4YV4TZMB3V0044FD16 — Hugo × Sandro Siqueira |
| **Versão do Parecer** | v1 |
| **Status** | EMITIDO — Aguarda deliberação do Comitê VMO |

---

## 1. Resumo da Demanda

A Divisão Comércio do Grupo Águia Branca propõe substituir o produto de auditoria fiscal de terceiros **Fiscal Defender** — contratado por R$ 78.000,00/ano — pelo módulo proprietário **Auditor Fiscal**, a ser desenvolvido pelo fornecedor do ERP corporativo, a empresa **NBS**, como contrapartida de um acordo comercial já em vigor, sem custo de desenvolvimento para a organização. O novo módulo operará nativamente no ERP NBS, eliminando a camada de integração hoje existente entre os dois sistemas, e manterá as funcionalidades essenciais de auditoria de notas fiscais eletrônicas, detecção de fraudes, alertas de risco de multa e geração de relatórios — acrescidas de melhorias de usabilidade declaradas pelo solicitante. A demanda é de compliance contínuo, de escopo restrito à Divisão Comércio (impactando Contabilidade, Financeiro e Jurídico), classificada pelo próprio solicitante como nova solução, e não possui sponsor executivo formalmente identificado, prazo acordado com a NBS nem documentação contratual verificada pelas áreas competentes.

---

## 2. Análise por Critério

### Critério 1 — Alinhamento Estratégico (Peso: 1)

**Nota: 4/5**

A iniciativa está diretamente alinhada a dois eixos estratégicos recorrentes em grupos empresariais de grande porte: racionalização do portfólio de fornecedores de TI e consolidação tecnológica em plataformas centrais. A substituição do Fiscal Defender pelo módulo nativo NBS reduz a dependência de um fornecedor adicional, elimina risco de descontinuidade tecnológica de terceiros e fortalece o ecossistema já investido no ERP. Adicionalmente, a demanda preserva a conformidade fiscal obrigatória — atividade não negociável no ambiente regulatório brasileiro —, o que reforça o alinhamento com objetivos de governança corporativa e gestão de riscos tributários. O único fator que impede nota máxima é a ausência de referência explícita a um objetivo estratégico formal do Grupo Águia Branca (ex.: planejamento estratégico, OKRs, PDT), o que fragiliza a pontuação em rituais de priorização portfólio. O alinhamento é sólido por inferência, mas não documentado.

---

### Critério 2 — Retorno sobre Investimento / Viabilidade Financeira (Peso: 1)

**Nota: 4/5**

O saving anual identificado é de R$ 78.000,00, correspondente à eliminação integral do contrato com o fornecedor do Fiscal Defender. O custo de desenvolvimento é R$ 0,00, confirmado pelo solicitante como contrapartida contratual já negociada com a NBS. Mesmo considerando custos residuais estimados (detalhados na seção 5 deste parecer), o payback é inferior a 12 meses e o ROI no primeiro ciclo anual permanece fortemente positivo. A nota não é máxima porque: (a) o saving de R$ 78K não foi formalmente registrado no orçamento corporativo, existindo como declaração do solicitante sem validação da Controladoria; (b) custos residuais de implementação, treinamento e rescisão contratual do Fiscal Defender não foram quantificados; e (c) não há confirmação de que o saving será capturado no budget em curso ou apenas no próximo exercício. O potencial financeiro é real e expressivo, mas a maturidade da evidência financeira ainda é incompleta.

---

### Critério 3 — Viabilidade Técnica (Peso: 1)

**Nota: 3/5**

A viabilidade técnica é plausível, mas apresenta incertezas relevantes. O desenvolvimento é de inteira responsabilidade da NBS, o que reduz a carga técnica interna do Grupo Águia Branca. A eliminação da camada de integração é um ganho arquitetural concreto e bem fundamentado: o módulo operará sobre a mesma base de dados do ERP, eliminando riscos de inconsistência de dados. No entanto, quatro incertezas técnicas permanecem abertas: (1) o escopo funcional exato do Auditor Fiscal não foi detalhado — não se sabe se as funcionalidades cobrirão integralmente as do Fiscal Defender; (2) a necessidade de integração com Power BI e outros sistemas não foi avaliada tecnicamente; (3) a necessidade de migração de dados históricos do Fiscal Defender não foi abordada; (4) não há interlocutor técnico identificado na NBS. A nota de 3/5 reflete viabilidade alta em princípio, mas condicionada à validação de escopo e capacidade de entrega do fornecedor — que até o momento repousa apenas na declaração verbal do solicitante.

---

### Critério 4 — Urgência / Impacto Operacional (Peso: 1)

**Nota: 3/5**

A demanda possui urgência moderada. O Fiscal Defender está em operação e atende as necessidades de compliance hoje, portanto não há risco imediato de interrupção do processo de auditoria fiscal. Contudo, dois fatores elevam a urgência para além do trivial: (a) a janela de oportunidade do acordo contratual com a NBS pode não ser perene — não iniciar o projeto em tempo hábil pode comprometer a entrega do módulo como contrapartida; (b) o custo de R$ 78K/ano continua sendo consumido enquanto a substituição não ocorre, gerando um custo de oportunidade mensurável de R$ 6.500/mês de atraso. A ausência de prazo legal específico e a continuidade operacional garantida pelo Fiscal Defender impedem nota mais alta. O risco de multa e fraude mencionado pelo solicitante é real, porém já mitigado pelo sistema atual — não representa urgência nova.

---

### Critério 5 — Maturidade da Demanda (Peso: 1)

**Nota: 2/5**

Este é o critério com maior déficit da demanda. Embora o problema de negócio esteja claro e o benefício seja bem articulado, quatro lacunas críticas (LAC-01 a LAC-04) comprometem a maturidade formal da demanda: ausência de sponsor executivo identificado, budget residual não confirmado, prazo de entrega desconhecido e documentação contratual do acordo NBS não verificada. A demanda existe exclusivamente na narrativa do solicitante, sem evidências documentais que comprovem o compromisso da NBS, o escopo acordado ou a autorização interna para o projeto. Além disso, o impacto sobre as áreas Financeiro e Jurídico foi declarado superficialmente, sem entrevistas ou validação com os stakeholders afetados. A demanda é madura em intenção, imatura em formalização — estado característico de demandas nascentes que ainda não percorreram o processo mínimo de instrução.

---

### Critério 6 — Disponibilidade de Recursos (Peso: 1)

**Nota: 2/5**

A disponibilidade de recursos apresenta o segundo maior déficit. O desenvolvimento técnico está alocado ao fornecedor NBS (custo zero), o que é favorável. Porém, os demais recursos essenciais para um projeto bem-sucedido estão indefinidos: (1) não há sponsor executivo identificado, comprometendo a autoridade de aprovação e condução interna; (2) não há confirmação de budget para custos residuais de implementação, treinamento e eventual rescisão antecipada do Fiscal Defender; (3) não há equipe interna formalmente designada para receber, testar e implantar o módulo; (4) o interlocutor técnico da NBS para o desenvolvimento não foi identificado. A demanda depende de um fornecedor como principal executor sem que os vínculos de governança e responsabilidade estejam estabelecidos. O risco de projeto sem dono é alto.

---

## 3. Tabela de Scoring

| # | Critério | Nota | Máximo |
|---|---|:---:|:---:|
| 1 | Alinhamento Estratégico | 4 | 5 |
| 2 | Retorno sobre Investimento / Viabilidade Financeira | 4 | 5 |
| 3 | Viabilidade Técnica | 3 | 5 |
| 4 | Urgência / Impacto Operacional | 3 | 5 |
| 5 | Maturidade da Demanda | 2 | 5 |
| 6 | Disponibilidade de Recursos | 2 | 5 |
| | **TOTAL** | **18** | **30** |
| | **Percentual** | **60%** | **100%** |

---

## 4. Análise de ROI

### 4.1 Premissas Adotadas

| Item | Valor | Base |
|---|---|---|
| Saving anual (eliminação Fiscal Defender) | R$ 78.000,00 | Declarado pelo solicitante |
| Custo de desenvolvimento | R$ 0,00 | Contrapartida contratual NBS |
| Nível de confiança do saving | **Médio** | Declaração sem validação da Controladoria |

### 4.2 Estimativa de Custos Residuais

Os custos abaixo são **estimativas analíticas** na ausência de levantamento formal, baseadas em referência de mercado para projetos de substituição de sistemas de auditoria fiscal de porte similar:

| Item | Estimativa Mínima | Estimativa Máxima | Observação |
|---|---|---|---|
| Implementação / parametrização interna | R$ 5.000 | R$ 20.000 | Alocação de analistas internos de TI para homologação e testes |
| Treinamento dos usuários (Contabilidade, Financeiro, Jurídico) | R$ 3.000 | R$ 10.000 | Estimado para ~15–30 usuários da Divisão Comércio |
| Rescisão antecipada do Fiscal Defender (se aplicável) | R$ 0 | R$ 30.000 | Depende da vigência contratual e cláusulas de multa — **não verificado** |
| Migração de dados históricos (se necessário) | R$ 0 | R$ 15.000 | Necessidade não confirmada; pode ser zero se dispensado |
| Operação paralela temporária dos dois sistemas | R$ 0 | R$ 19.500 | Estimado como até 3 meses de custo proporcional do Fiscal Defender (R$6.500/mês) |
| **Total Residual (cenário mínimo)** | **R$ 8.000** | — | |
| **Total Residual (cenário máximo)** | — | **R$ 94.500** | Inclui rescisão máxima e todos os itens |
| **Total Residual (cenário central estimado)** | — | **R$ 35.000** | Sem rescisão onerosa; operação paralela de 1 mês |

### 4.3 Projeção de Payback

| Cenário | Custo Residual Total | Saving Anual | Payback Estimado | Confiança |
|---|---|---|---|---|
| **Otimista** | R$ 8.000 | R$ 78.000 | ~1,2 meses | Baixa — supõe ausência de rescisão e dados históricos desnecessários |
| **Central** | R$ 35.000 | R$ 78.000 | ~5,4 meses | Média — cenário mais provável dado o porte da operação |
| **Conservador** | R$ 94.500 | R$ 78.000 | ~14,6 meses | Baixa — improvável salvo rescisão onerosa e migração complexa |

**Confiança geral da análise de ROI: MÉDIA-BAIXA.** O saving de R$ 78K/ano é robusto e verificável. Os custos residuais são estimativas sem levantamento formal — a variável mais crítica e imprevisível é a condição contratual de rescisão do Fiscal Defender (LAC-02 + LAC-09), que pode transformar o cenário otimista em conservador.

### 4.4 ROI Estimado (Cenário Central — 3 anos)

| Período | Economia Acumulada | Custo Acumulado | Resultado Líquido |
|---|---|---|---|
| Ano 1 | R$ 78.000 | R$ 35.000 | **+ R$ 43.000** |
| Ano 2 | R$ 156.000 | R$ 35.000 | **+ R$ 121.000** |
| Ano 3 | R$ 234.000 | R$ 35.000 | **+ R$ 199.000** |

**ROI em 3 anos (cenário central): ~469%** — economicamente expressivo mesmo no cenário conservador.

---

## 5. Condições Bloqueantes

As condições abaixo são **pré-requisitos obrigatórios** para aprovação definitiva e abertura formal do projeto. A ausência de qualquer uma delas impede o início da execução.

| ID | Condição Bloqueante | Lacuna Associada | Prazo Máximo para Sanação |
|---|---|---|---|
| **CB-01** | Identificação e formalização do **sponsor executivo** com autoridade para aprovar e conduzir o projeto internamente na Divisão Comércio | LAC-01 | 10 dias corridos |
| **CB-02** | Apresentação e validação pela área Jurídica/Contratos da **documentação contratual do acordo com a NBS** referente ao módulo Auditor Fiscal — comprovando escopo, prazo e custo zero | LAC-04 | 15 dias corridos |

**Justificativa:** LAC-01 e LAC-04 são bloqueantes porque, sem sponsor, não há autoridade para comprometer recursos internos e tomar decisões de projeto; sem documentação contratual verificada, a premissa central da demanda — desenvolvimento gratuito pela NBS — é apenas uma declaração verbal sujeita a contestação. Iniciar o projeto sem essas duas bases é aceitar risco de paralisação posterior com custo político e financeiro elevado.

---

## 6. Condições Desejáveis

As condições abaixo são **recomendadas antes do início da execução**, mas não impedem a aprovação condicional da demanda. Devem ser sanadas na fase de instrução do projeto.

| ID | Condição Desejável | Lacuna Associada | Responsável Sugerido |
|---|---|---|---|
| CD-01 | Confirmação formal de **budget residual** para implementação e treinamento, com validação da Controladoria | LAC-02 | Financeiro / Controladoria |
| CD-02 | Definição de **prazo de entrega** acordado com a NBS, com marco de Go-Live e cronograma de desenvolvimento | LAC-03 | Sandro Siqueira + NBS |
| CD-03 | Entrevistas de impacto com as áreas **Financeiro e Jurídico** da Divisão Comércio para validar requisitos e adoção | LAC-05 | PMO / Hugo |
| CD-04 | Verificação das **condições contratuais do Fiscal Defender** (vigência, aviso prévio, cláusula de rescisão) | LAC-09 | Jurídico / Contratos |
| CD-05 | Identificação do **interlocutor técnico da NBS** responsável pelo desenvolvimento do módulo | LAC-10 | Sandro Siqueira |
| CD-06 | Avaliação da **necessidade de migração de dados históricos** do Fiscal Defender | LAC-11 | TI / Sandro Siqueira |

---

## 7. Decisão Final

### Resultado: APROVADO COM CONDIÇÕES

**Pontuação:** 18/30 (60%) — limiar inferior da faixa "APROVADO COM CONDIÇÕES" (18–24/30).

### Justificativa

A demanda DEM-2026-002 apresenta fundamentos econômicos e estratégicos sólidos: saving anual comprovável de R$ 78.000,00, custo de desenvolvimento declarado como zero, alinhamento com objetivos de consolidação tecnológica e compliance fiscal obrigatório. O ROI é fortemente positivo mesmo nos cenários conservadores, e a viabilidade técnica é plausível dado que o desenvolvimento é de responsabilidade exclusiva do fornecedor do ERP.

Contudo, a demanda chega ao processo de qualificação em estágio de maturidade insuficiente para aprovação irrestrita. As lacunas LAC-01 (ausência de sponsor) e LAC-04 (documentação contratual não verificada) representam riscos estruturais que, se não sanados, podem comprometer a execução independentemente da qualidade da ideia. A premissa central da demanda — custo zero de desenvolvimento — existe apenas como declaração do solicitante, sem evidência documental verificada pelos órgãos competentes do Grupo Águia Branca.

A aprovação é condicionada à sanação das duas condições bloqueantes (CB-01 e CB-02) dentro dos prazos estabelecidos. Após confirmação das condições bloqueantes, a demanda deve retornar ao Comitê VMO para deliberação de abertura formal de projeto. Caso as condições não sejam sanadas no prazo, a demanda será reclassificada para **EM ESPERA** até nova instrução.

---

## 8. Próximos Passos

| # | Ação | Responsável | Prazo Sugerido | Prioridade |
|---|---|---|---|---|
| 1 | Identificar e formalizar o sponsor executivo da demanda (CB-01) | Sandro Siqueira + PMO | até 2026-05-25 | CRÍTICA |
| 2 | Solicitar, revisar e validar a documentação contratual do acordo NBS (CB-02) | Jurídico / Contratos + Sandro Siqueira | até 2026-05-30 | CRÍTICA |
| 3 | Confirmar budget residual para implementação/treinamento com Controladoria (CD-01) | Financeiro / Controladoria | até 2026-06-06 | ALTA |
| 4 | Obter cronograma e prazo de entrega acordado com a NBS (CD-02) | Sandro Siqueira + NBS | até 2026-06-06 | ALTA |
| 5 | Verificar condições contratuais de rescisão do Fiscal Defender (CD-04) | Jurídico / Contratos | até 2026-06-06 | ALTA |
| 6 | Realizar entrevistas de impacto com Financeiro e Jurídico da Divisão Comércio (CD-03) | Hugo / PMO | até 2026-06-13 | MÉDIA |
| 7 | Identificar interlocutor técnico da NBS para o projeto (CD-05) | Sandro Siqueira | até 2026-06-06 | MÉDIA |
| 8 | Avaliar necessidade de migração de dados históricos (CD-06) | TI / Sandro Siqueira | até 2026-06-13 | MÉDIA |
| 9 | Retornar ao Comitê VMO com evidências das condições bloqueantes para deliberação final | PMO / Felipe Filtro | após sanação de CB-01 e CB-02 | CRÍTICA |
| 10 | Em caso de aprovação definitiva: elaborar Termo de Abertura de Projeto (TAP) | PMO | após etapa 9 | — |

---

## Controle do Documento

| Campo | Valor |
|---|---|
| **Documento gerado por** | Felipe Filtro — Analista de Qualificação, VMO Autônomo |
| **Data de emissão** | 2026-05-15 |
| **Versão** | v1 |
| **Status** | Emitido — Aguarda deliberação do Comitê VMO |
| **Documentos de referência** | demanda-coletada.md (v1); materiais-demanda.md; Fireflies 01KRP1TW4YV4TZMB3V0044FD16 |
| **Próxima revisão** | Após sanação de CB-01 e CB-02 (prazo máximo: 2026-05-30) |
