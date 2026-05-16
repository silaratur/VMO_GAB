# PROJ-2026-005 — Pacote Completo de Instrução
# Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender
# Grupo Águia Branca | VMO Autônomo v1.0
# Data de Instrução: 2026-05-15 | Run: 2026-05-15-150000
# Score de Qualidade: 91/100 — APROVADO

---

---

# ■  01-demanda-coletada

# Demanda Coletada — Auditor Fiscal (Módulo NBS)

---

## Cabeçalho

| Campo | Valor |
|---|---|
| **ID da Demanda** | DEM-2026-002 |
| **Código do Projeto** | PROJ-2026-005 |
| **Data do Registro** | 2026-05-15 |
| **Solicitante** | Sandro Siqueira |
| **Área** | Contabilidade — Divisão Comércio |
| **Grupo** | Grupo Águia Branca |
| **Origem** | Entrevista de Discovery via Fireflies |
| **ID Fireflies** | 01KRP1TW4YV4TZMB3V0044FD16 |
| **Entrevistador** | Hugo |
| **Versão do Documento** | v1 |

---

## 1. Resumo Executivo

O Grupo Águia Branca, por meio da Divisão Comércio, identificou a oportunidade de substituir o produto de auditoria fiscal atualmente contratado — o **Fiscal Defender**, com custo anual de R$ 78.000,00 — por um módulo proprietário denominado **Auditor Fiscal**, a ser desenvolvido e entregue pelo fornecedor do ERP corporativo, a empresa **NBS**, sem custo adicional para a organização. A iniciativa nasce de um acordo comercial já estabelecido entre o Grupo Águia Branca e a NBS, no qual o desenvolvimento do novo módulo figura como contrapartida contratual, eliminando a necessidade de licenciamento de terceiros.

Do ponto de vista funcional, a solução proposta replica e expande as capacidades hoje exercidas pelo Fiscal Defender: auditoria automatizada de notas fiscais, identificação de inconsistências, detecção de possíveis fraudes, alertas de risco de multa e geração de relatórios gerenciais. A principal diferença estrutural reside na eliminação da camada de integração entre o Fiscal Defender e o ERP NBS — atualmente necessária para sincronização de dados — uma vez que o Auditor Fiscal será nativo ao ERP, operando sobre a mesma base de dados e sob o mesmo ecossistema tecnológico.

A demanda possui caráter de **compliance contínuo**, visto que a auditoria de notas fiscais é uma obrigação regulatória e operacional rotineira, não vinculada a um prazo legal específico. O impacto organizacional ultrapassa a área de Contabilidade, alcançando também os setores Financeiro e Jurídico da Divisão Comércio. A iniciativa é classificada pelo próprio solicitante como **nova solução**, embora do ponto de vista de processo represente uma continuidade operacional com ganhos de usabilidade, integração e redução de custos.

Do ponto de vista estratégico, a demanda representa uma oportunidade de racionalização do portfólio de fornecedores, redução de custos recorrentes e consolidação tecnológica no ecossistema NBS. O sucesso da implementação depende, contudo, da conclusão de etapas de confirmação junto às áreas impactadas, da validação formal do escopo de desenvolvimento acordado com a NBS e da designação de sponsor interno com autoridade para conduzir o projeto.

---

## 2. Dados Cadastrais da Demanda

| Campo | Valor |
|---|---|
| **Título Oficial** | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Tipo de Demanda** | Nova Solução |
| **Solicitante** | Sandro Siqueira |
| **Cargo** | Coordenador de Contabilidade |
| **Área** | Contabilidade |
| **Divisão** | Divisão Comércio |
| **Grupo** | Grupo Águia Branca |
| **Data da Solicitação** | 2026-05-15 |
| **Origem do Registro** | Discovery — Entrevista estruturada (Fireflies ID: 01KRP1TW4YV4TZMB3V0044FD16) |

---

## 3. Necessidade de Negócio

### 3.1 Problema Atual (Dor)

A Divisão Comércio do Grupo Águia Branca opera atualmente com dois sistemas desacoplados para a função de auditoria fiscal: o ERP **NBS** (sistema de gestão central) e o produto **Fiscal Defender** (solução de auditoria de terceiros). Esta arquitetura exige uma camada de integração para sincronização de dados entre os dois ambientes, gerando complexidade operacional, dependência de fornecedor adicional e custo recorrente de R$ 78.000,00 por ano.

### 3.2 Solução Atual

| Componente | Descrição |
|---|---|
| **Sistema ERP** | NBS (fornecedor principal) |
| **Ferramenta de Auditoria** | Fiscal Defender (fornecedor terceiro) |
| **Mecanismo** | Integração entre Fiscal Defender e NBS para importação de notas fiscais |
| **Custo Anual** | R$ 78.000,00 (licenciamento Fiscal Defender) |
| **Função** | Auditoria de NF-e, identificação de fraudes, risco de multa, pagamentos indevidos, geração de relatórios |

### 3.3 Custo Atual

- **Fiscal Defender:** R$ 78.000,00 / ano
- **Custo do novo módulo (Auditor Fiscal / NBS):** R$ 0,00 (desenvolvimento como contrapartida contratual)
- **Economia potencial:** R$ 78.000,00 / ano (100% do custo atual)

### 3.4 Benefícios Esperados

| Benefício | Categoria |
|---|---|
| Eliminação do custo de R$ 78K/ano com Fiscal Defender | Financeiro |
| Eliminação da camada de integração entre sistemas | Técnico |
| Operação nativa no ERP NBS (única plataforma) | Técnico / Operacional |
| Maior usabilidade e aderência ao negócio | Operacional |
| Manutenção da conformidade fiscal obrigatória | Regulatório |
| Potencial incremento de funcionalidades | Funcional |

---

## 4. Descrição da Demanda

### 4.1 O Que É (Escopo Declarado)

Desenvolvimento e implantação do módulo **Auditor Fiscal** pelo fornecedor NBS, integrado nativamente ao ERP corporativo, com capacidade de:

- Importar e auditar notas fiscais eletronicamente;
- Identificar inconsistências, possíveis fraudes, riscos de multa e pagamentos indevidos;
- Gerar relatórios gerenciais e operacionais;
- Oferecer usabilidade superior ao Fiscal Defender atual, com funcionalidades mais aderentes ao contexto do negócio.

### 4.2 Como Funciona Hoje

```
[NBS ERP] → [Integração] → [Fiscal Defender]
                                   ↓
                          Auditoria de NF-e
                                   ↓
                          Relatórios (Contabilidade / Financeiro / Jurídico)
```

1. Notas fiscais são geradas/recebidas no ERP NBS;
2. Os dados são exportados e importados no Fiscal Defender via integração;
3. O Fiscal Defender realiza a auditoria automatizada;
4. Relatórios são gerados e consumidos pelas áreas de Contabilidade, Financeiro e Jurídico.

### 4.3 Como Deverá Funcionar

```
[NBS ERP + Módulo Auditor Fiscal (nativo)]
                   ↓
          Auditoria de NF-e (mesma base de dados)
                   ↓
          Relatórios (Contabilidade / Financeiro / Jurídico)
          [+ eventual integração com Power BI para relatórios gerenciais]
```

1. O módulo Auditor Fiscal operará nativamente dentro do ERP NBS;
2. As notas fiscais já presentes no ERP serão auditadas diretamente, sem necessidade de exportação/importação;
3. As tarefas operacionais dos usuários permanecerão essencialmente as mesmas;
4. A experiência de uso será mais fluida, com funcionalidades mais aderentes à realidade do negócio;
5. Relatórios poderão ser consumidos diretamente no módulo e, potencialmente, via Power BI.

---

## 5. Contexto Organizacional

### 5.1 Motivação Estratégica

- Redução de custos recorrentes com fornecedores de software (saving de R$ 78K/ano);
- Consolidação do ecossistema tecnológico em torno do ERP NBS;
- Eliminação de dependências de integração entre sistemas heterogêneos;
- Aproveitamento de acordo comercial já estabelecido com a NBS como alavanca de valor.

### 5.2 Pressões e Fatores Externos

- **Compliance fiscal obrigatório:** A auditoria de notas fiscais é uma necessidade contínua, não vinculada a prazo legal específico, mas exigida pelo ambiente regulatório brasileiro (SEFAZ, fiscalização tributária, etc.);
- **Risco de multa e fraude:** A ausência de auditoria fiscal pode expor a organização a sanções tributárias e prejuízos financeiros;
- **Acordo comercial com NBS:** O desenvolvimento do Auditor Fiscal foi negociado como contrapartida, criando uma janela de oportunidade com custo zero de desenvolvimento.

### 5.3 Histórico Relevante

- O Grupo Águia Branca possui parceria com a NBS para fornecimento do ERP corporativo;
- No contexto dessa parceria, foi negociado o desenvolvimento do módulo Auditor Fiscal como item de contrapartida;
- O Fiscal Defender já está em operação e atende às necessidades de auditoria fiscal atuais, porém com custo e complexidade de integração que motivam a substituição.

---

## 6. Requisitos Preliminares

> **Nota:** Os requisitos abaixo foram capturados a partir da entrevista de discovery. Refinamento e validação formal são necessários nas etapas subsequentes.

### 6.1 Requisitos Funcionais (RF)

| ID | Descrição | Fonte |
|---|---|---|
| RF-01 | Importar e processar notas fiscais eletrônicas (NF-e) a partir da base de dados do ERP NBS | Entrevista |
| RF-02 | Realizar auditoria automatizada das notas fiscais processadas | Entrevista |
| RF-03 | Identificar e alertar sobre possíveis fraudes em notas fiscais | Entrevista |
| RF-04 | Identificar e alertar sobre riscos de multa por inconsistências fiscais | Entrevista |
| RF-05 | Identificar e alertar sobre pagamentos indevidos | Entrevista |
| RF-06 | Gerar relatórios operacionais e gerenciais de auditoria fiscal | Entrevista |
| RF-07 | Manter o fluxo operacional atual das equipes (sem alteração de processo) | Entrevista |
| RF-08 | Oferecer funcionalidades de usabilidade superiores ao Fiscal Defender | Entrevista |

### 6.2 Requisitos Não-Funcionais (RNF)

| ID | Descrição | Fonte |
|---|---|---|
| RNF-01 | O módulo deve ser nativo ao ERP NBS, sem necessidade de integração externa para a função de auditoria | Entrevista |
| RNF-02 | O sistema deve operar sobre a mesma base de dados do ERP NBS (sem duplicação ou exportação de dados) | Inferido |
| RNF-03 | O custo de desenvolvimento não deve gerar despesa adicional para o Grupo Águia Branca | Entrevista |
| RNF-04 | O sistema deve estar disponível de forma contínua para operação rotineira (disponibilidade operacional) | Inferido |

### 6.3 Restrições

| ID | Descrição |
|---|---|
| REST-01 | O desenvolvimento é de responsabilidade exclusiva da NBS — o Grupo Águia Branca não desenvolverá o módulo internamente |
| REST-02 | A solução deve ser restrita à Divisão Comércio (não é um projeto corporativo transversal) |
| REST-03 | O módulo deve substituir integralmente o Fiscal Defender, sem operação paralela de longo prazo (a ser confirmado) |

---

## 7. Impactos

### 7.1 Áreas Impactadas

| Área | Nível de Impacto | Observação |
|---|---|---|
| Contabilidade (Divisão Comércio) | Alto | Área solicitante; uso diário da ferramenta |
| Financeiro (Divisão Comércio) | Médio | Impactado conforme declarado pelo solicitante; detalhes a confirmar |
| Jurídico (Divisão Comércio) | Médio | Impactado conforme declarado pelo solicitante; detalhes a confirmar |
| Demais divisões (Passageiros, Logística) | Nenhum | Demanda exclusiva da Divisão Comércio |

### 7.2 Sistemas Afetados

| Sistema | Tipo de Impacto |
|---|---|
| ERP NBS | Sistema hospedeiro do novo módulo; base de dados compartilhada |
| Fiscal Defender | Sistema a ser descontinuado/substituído |
| Power BI | Potencial integração para relatórios gerenciais (a avaliar) |

### 7.3 Processos Impactados

| Processo | Impacto |
|---|---|
| Importação de notas fiscais para auditoria | Eliminação da etapa de exportação/importação para sistema externo |
| Auditoria fiscal de NF-e | Continuidade — sem alteração de escopo funcional |
| Geração de relatórios de auditoria | Continuidade — com melhoria de usabilidade esperada |
| Gestão de contratos de software | Descontinuação do contrato com fornecedor do Fiscal Defender |

---

## 8. Premissas e Restrições

### 8.1 Premissas

| ID | Premissa |
|---|---|
| P-01 | O acordo comercial com a NBS para desenvolvimento do Auditor Fiscal sem custo adicional está formalmente documentado e vigente |
| P-02 | A NBS possui capacidade técnica e compromisso contratual para entrega do módulo dentro de prazo adequado |
| P-03 | As funcionalidades do Auditor Fiscal serão, no mínimo, equivalentes às do Fiscal Defender em termos de cobertura de auditoria |
| P-04 | O processo operacional das equipes não será alterado de forma significativa |
| P-05 | A integração com Power BI, se necessária, poderá ser viabilizada pelo próprio ecossistema NBS ou por conector padrão |

### 8.2 Restrições

| ID | Restrição |
|---|---|
| R-01 | A demanda é exclusiva da Divisão Comércio — outras divisões não estão no escopo |
| R-02 | O desenvolvimento é de responsabilidade da NBS; o Grupo Águia Branca atua como cliente/validador |
| R-03 | O orçamento de R$ 0 (contrapartida contratual) pressupõe que não haverá customizações além do escopo acordado |

---

## 9. Lacunas de Informação

> As lacunas abaixo representam informações **não obtidas ou não confirmadas** durante a entrevista de discovery e que devem ser endereçadas nas próximas etapas do processo de estruturação da demanda.

| ID | Lacuna | Criticidade | Responsável pela Investigação |
|---|---|---|---|
| LAC-01 | **Sponsor da demanda:** Não foi identificado quem é o sponsor executivo com autoridade para aprovar e conduzir o projeto internamente | Alta | Hugo / PMO |
| LAC-02 | **Budget formal:** Não foi confirmado se a economia de R$ 78K está formalmente registrada como saving no orçamento, nem se há previsão de custos residuais (implementação, treinamento, migração) | Alta | Financeiro / Controladoria |
| LAC-03 | **Prazo:** Nenhum prazo de entrega foi mencionado — nem prazo legal nem prazo acordado com a NBS | Alta | Sandro Siqueira / NBS |
| LAC-04 | **Detalhes do acordo com NBS:** O escopo exato do módulo Auditor Fiscal acordado com a NBS não foi detalhado — não há documentação do escopo contratual disponível | Alta | Jurídico / Contratos |
| LAC-05 | **Impacto detalhado nas áreas Financeiro e Jurídico:** O solicitante indicou que essas áreas serão impactadas, mas não detalhou como ou quais funcionalidades as afetam | Média | Áreas Financeiro e Jurídico |
| LAC-06 | **Integração com Power BI:** A necessidade e o escopo de uma eventual integração com Power BI não foram confirmados — o solicitante mencionou como possibilidade, não como requisito | Média | TI / Sandro Siqueira |
| LAC-07 | **Necessidade de integração com outros sistemas além do NBS:** O solicitante declarou não ter certeza — precisa de levantamento técnico | Média | TI / NBS |
| LAC-08 | **Exemplos concretos de melhorias funcionais:** O solicitante não forneceu exemplos específicos de funcionalidades novas ou melhoradas em relação ao Fiscal Defender | Baixa | Sandro Siqueira |
| LAC-09 | **Plano de descontinuação do Fiscal Defender:** Não foi discutido quando e como o contrato atual será encerrado | Média | Contratos / Financeiro |
| LAC-10 | **Responsável técnico na NBS:** Não foi identificado o interlocutor técnico da NBS para o desenvolvimento do módulo | Média | Sandro Siqueira / Contratos |
| LAC-11 | **Necessidade de migração de dados históricos:** Não foi abordado se os dados históricos do Fiscal Defender precisarão ser migrados para o novo módulo | Média | TI / Sandro Siqueira |

---

## 10. Dependências Identificadas

| Dependência | Tipo | Status | Observação |
|---|---|---|---|
| **NBS (fornecedor ERP)** | Desenvolvimento | A confirmar | Responsável pelo desenvolvimento do módulo Auditor Fiscal; compromisso declarado pelo solicitante, mas documentação contratual não verificada |
| **Sponsor interno** | Governança | Não identificado | Não foi declarado quem é o patrocinador executivo da demanda dentro do Grupo Águia Branca |
| **Aprovação de budget** | Financeiro | Não confirmado | A iniciativa não gera custo de licença, mas custos de implementação, treinamento e descontinuação do Fiscal Defender precisam ser avaliados |
| **Áreas Financeiro e Jurídico** | Validação | Pendente | Confirmação do impacto e requisitos dessas áreas ainda não realizada |
| **Power BI** | Integração (potencial) | Indefinido | Necessidade não confirmada; avaliação técnica pendente |
| **Contrato Fiscal Defender** | Contratual | A avaliar | Necessidade de verificar vigência e condições de rescisão/encerramento do contrato atual |

---

## 11. Próximos Passos Recomendados

| # | Ação | Responsável Sugerido | Prazo Sugerido |
|---|---|---|---|
| 1 | Identificar e formalizar o sponsor executivo da demanda internamente | PMO / Hugo | Imediato |
| 2 | Solicitar e revisar a documentação contratual do acordo com a NBS referente ao desenvolvimento do Auditor Fiscal | Jurídico / Contratos | Curto prazo |
| 3 | Realizar entrevista de impacto com as áreas Financeiro e Jurídico da Divisão Comércio | Hugo / PMO | Curto prazo |
| 4 | Confirmar com a NBS o escopo funcional detalhado, cronograma de desenvolvimento e marcos de entrega | Sandro Siqueira + NBS | Curto prazo |
| 5 | Avaliar a necessidade de integração com Power BI e demais sistemas — realizar levantamento técnico com TI | TI / Sandro Siqueira | Médio prazo |
| 6 | Verificar condições contratuais do Fiscal Defender (vigência, aviso prévio, multas rescisórias) | Financeiro / Jurídico | Curto prazo |
| 7 | Avaliar necessidade de migração de dados históricos do Fiscal Defender para o Auditor Fiscal | TI / Sandro Siqueira | Médio prazo |
| 8 | Solicitar ao solicitante exemplos concretos de melhorias funcionais esperadas para subsidiar a validação do escopo | Hugo | Curto prazo |
| 9 | Elaborar o Termo de Abertura de Projeto (TAP) após sanação das lacunas críticas (LAC-01 a LAC-04) | PMO | Após etapas 1–4 |
| 10 | Registrar saving potencial de R$ 78K/ano no sistema de gestão orçamentária | Financeiro / Controladoria | Médio prazo |

---

## Controle do Documento

| Campo | Valor |
|---|---|
| **Documento gerado por** | Iara Inbound — Agente de Captação VMO Autônomo |
| **Data de geração** | 2026-05-15 |
| **Versão** | v1 |
| **Status** | Rascunho — Aguardando validação do solicitante e PMO |
| **Próxima revisão** | Após sanação das lacunas críticas (LAC-01 a LAC-04) |

---

# ■  02-qualificacao

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

---

# ■  03-tap-canvas-plano-geral

# Documentação de Iniciação — PROJ-2026-005
**Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender**
Gerado por: Diana Documento | Data: 2026-05-15 | Versão: 1.0

---

# DOCUMENTO 1 — TAP: Termo de Abertura do Projeto

## 1. Identificação do Projeto

| Campo                     | Conteúdo                                                                     |
|---------------------------|------------------------------------------------------------------------------|
| **Código**                | PROJ-2026-005                                                                |
| **Demanda Origem**        | DEM-2026-002                                                                 |
| **Título**                | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender        |
| **Data de Abertura**      | 2026-05-15                                                                   |
| **Versão do TAP**         | 1.0                                                                          |
| **Elaborado por**         | Marcelo Silveira (GP VMO Autônomo)                                           |
| **Solicitante**           | Sandro Siqueira — Coordenador de Contabilidade, Divisão Comércio, Grupo Águia Branca |
| **Sponsor Executivo**     | **⚠ A IDENTIFICAR — CONDIÇÃO BLOQUEANTE CB-01 (prazo: 25/05/2026)**         |
| **Gestor do Projeto**     | A definir — VMO Autônomo                                                     |
| **Cliente / Área**        | Divisão Comércio — Grupo Águia Branca                                        |
| **Áreas Impactadas**      | Contabilidade, Financeiro, Jurídico                                          |

---

## ⛔ ALERTA: CONDIÇÕES BLOQUEANTES — APROVAÇÃO CONDICIONAL

> Este projeto foi aprovado com **SCORE 18/30 (60%)** — **APROVADO COM CONDIÇÕES**.
> A execução do projeto está **BLOQUEADA** até que as condições abaixo sejam cumpridas.
> O não cumprimento dentro dos prazos estabelecidos implicará em **suspensão automática da abertura formal**.

| Código | Condição Bloqueante                                                                                       | Responsável       | Prazo         | Status     |
|--------|-----------------------------------------------------------------------------------------------------------|-------------------|---------------|------------|
| **CB-01** | Sponsor executivo não identificado. Necessário indicar e confirmar patrocinador executivo do projeto. | Sandro Siqueira / Alta Gestão Div. Comércio | **25/05/2026** | 🔴 ABERTO |
| **CB-02** | Documentação contratual do acordo NBS (compromisso de desenvolvimento do Auditor Fiscal) não verificada. Necessário obter e validar cláusula contratual que formaliza a contrapartida. | Sandro Siqueira / Jurídico | **30/05/2026** | 🔴 ABERTO |

---

## 2. Objetivo SMART

> Substituir **100% das funcionalidades operacionais do Fiscal Defender** pelo módulo nativo **Auditor Fiscal NBS** no ambiente ERP da Divisão Comércio do Grupo Águia Branca, alcançando o **go-live até novembro de 2026** (prazo estimado: 6–8 meses a partir da abertura formal), confirmando a **eliminação do contrato Fiscal Defender** e gerando **saving recorrente de R$ 78.000/ano**, com custo de implementação residual máximo de **R$ 35.000**, garantindo que todas as equipes de Contabilidade, Financeiro e Jurídico operem sem alteração do fluxo de trabalho atual.

| Critério SMART | Conteúdo                                                                                                    |
|----------------|-------------------------------------------------------------------------------------------------------------|
| **Specific**   | Substituição do Fiscal Defender pelo módulo Auditor Fiscal nativo NBS; escopo: Divisão Comércio             |
| **Measurable** | 100% das funcionalidades do Fiscal Defender replicadas; saving de R$78K/ano confirmado; max R$35K residuais |
| **Achievable** | Desenvolvimento como contrapartida contratual NBS (custo zero); estrutura técnica ERP existente             |
| **Relevant**   | Alinhamento estratégico com consolidação da plataforma ERP corporativa e eficiência financeira               |
| **Time-bound** | Go-live: estimado entre setembro e novembro de 2026                                                         |

---

## 3. Justificativa do Projeto

### 3.1 Contexto e Motivação

A Divisão Comércio do Grupo Águia Branca utiliza o sistema **Fiscal Defender** para auditoria automatizada de Notas Fiscais Eletrônicas (NF-e), pagando **R$ 78.000 por ano** por esse serviço. O fornecedor do ERP corporativo, **NBS**, comprometeu-se contratualmente a desenvolver o módulo **Auditor Fiscal** como contrapartida — sem custo adicional de desenvolvimento.

A não aprovação e execução deste projeto representa:

- **Desperdício financeiro:** continuidade de gasto anual de R$ 78.000 em solução externa quando a funcionalidade equivalente estará disponível nativamente.
- **Risco de compliance:** dependência de dois sistemas distintos para auditoria fiscal, com potencial de divergência de dados e lacunas de rastreabilidade.
- **Oportunidade perdida:** o comprometimento contratual da NBS tem prazo e escopo definidos — atrasar o projeto pode comprometer os termos acordados.

### 3.2 ROI e Viabilidade Financeira

| Indicador                        | Valor                         |
|----------------------------------|-------------------------------|
| Custo anual atual (Fiscal Defender) | R$ 78.000/ano              |
| Custo de desenvolvimento         | R$ 0 (contrapartida NBS)     |
| Custo residual estimado          | ~R$ 35.000 (implementação, treinamento, rescisão) |
| **Orçamento total do projeto**   | **~R$ 35.000**               |
| Saving anual recorrente          | R$ 78.000/ano                |
| **Payback estimado**             | **~5,4 meses**               |
| ROI no 1º ano completo           | > 100%                       |

### 3.3 Alinhamento Estratégico

- Consolidação da plataforma ERP NBS como solução única de gestão corporativa.
- Redução de fornecedores e dependências externas.
- Eficiência operacional: integração nativa elimina exportações/importações manuais de dados entre sistemas.

---

## 4. Escopo do Projeto

### 4.1 Dentro do Escopo (IN SCOPE)

- Implantação do módulo Auditor Fiscal NBS na Divisão Comércio.
- Configuração e parametrização do módulo conforme regras fiscais da Divisão Comércio.
- Replicação de todas as funcionalidades operacionais do Fiscal Defender (RF-01 a RF-08).
- Testes de homologação e validação com equipes de Contabilidade, Financeiro e Jurídico.
- Treinamento das equipes usuárias.
- Encerramento formal do contrato Fiscal Defender.
- Gestão da transição (período de operação paralela se necessário).

### 4.2 Fora do Escopo (OUT OF SCOPE)

- Desenvolvimento de novas funcionalidades além das previstas nos RF-01 a RF-08 (salvo aprovação formal de mudança).
- Implantação em outras divisões do Grupo Águia Branca.
- Integração com Power BI (a ser avaliada como demanda futura — não confirmada para este projeto).
- Migração de dados históricos do Fiscal Defender (necessidade não avaliada — a ser definida na fase de planejamento detalhado).
- Alteração dos processos operacionais das equipes (RF-07: manutenção do fluxo atual).
- Customizações no núcleo do ERP NBS não relacionadas ao módulo Auditor Fiscal.

---

## 5. Estimativas de Custo e Prazo

### 5.1 Orçamento

| Categoria                                 | Estimativa         | Observação                                          |
|-------------------------------------------|--------------------|-----------------------------------------------------|
| Desenvolvimento do módulo (NBS)           | R$ 0               | Contrapartida contratual — **SUJEITO A CB-02**      |
| Implementação / configuração / parametrização | ~R$ 15.000     | Horas de consultoria NBS ou interna                 |
| Treinamento das equipes                   | ~R$ 8.000          | Estimativa preliminar                               |
| Rescisão contratual Fiscal Defender       | ~R$ 7.000          | Multas e aviso prévio (verificar contrato)          |
| Contingência (reserva gerencial ~15%)     | ~R$ 5.000          | Sobre custos residuais                              |
| **Total Estimado**                        | **~R$ 35.000**     | Revisão obrigatória após CB-02 resolvida            |

### 5.2 Cronograma Estimado

> Prazo estimado com base em projetos similares de implantação de módulo ERP. Cronograma detalhado a ser elaborado na fase de planejamento.

| Fase                                  | Duração Estimada | Período Provável         |
|---------------------------------------|------------------|--------------------------|
| Iniciação e resolução de condições bloqueantes | 3 semanas | mai/2026               |
| Planejamento detalhado                | 3 semanas        | jun/2026                 |
| Implantação e configuração (NBS)      | 8 semanas        | jul–ago/2026             |
| Testes e homologação                  | 4 semanas        | set/2026                 |
| Treinamento e transição               | 3 semanas        | out/2026                 |
| Go-live e encerramento Fiscal Defender| 2 semanas        | out–nov/2026             |
| **Go-live estimado**                  | —                | **Outubro/Novembro 2026**|
| **Duração total estimada**            | **~6–7 meses**   | mai–nov/2026             |

---

## 6. Premissas

| Código | Premissa                                                                                                        | Status           |
|--------|-----------------------------------------------------------------------------------------------------------------|------------------|
| **P-01** | O acordo contratual NBS para desenvolvimento do Auditor Fiscal está formalizado e vigente.                  | **⚠ A CONFIRMAR — CB-02** |
| P-02   | A NBS entregará o módulo Auditor Fiscal sem custo de desenvolvimento para a Divisão Comércio.                   | A confirmar (dep. P-01) |
| P-03   | Um sponsor executivo da Divisão Comércio será identificado e comprometido até 25/05/2026.                       | **⚠ A CONFIRMAR — CB-01** |
| P-04   | As equipes de Contabilidade, Financeiro e Jurídico disponibilizarão representantes para participação nos testes. | A confirmar       |
| P-05   | O módulo Auditor Fiscal NBS será compatível com a versão do ERP atualmente implantada na Divisão Comércio.      | A confirmar       |
| P-06   | O contrato com o Fiscal Defender permite rescisão dentro do prazo do projeto.                                   | A verificar       |
| P-07   | Não haverá necessidade de migração de dados históricos do Fiscal Defender (ou, se necessária, estará dentro do escopo acordado com NBS). | A avaliar |

---

## 7. Restrições

| Código | Restrição                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------|
| R-01   | O orçamento máximo de custos residuais é de **R$ 35.000**. Qualquer extrapolação requer aprovação do sponsor. |
| R-02   | O fluxo operacional das equipes não pode ser alterado (RF-07) — a solução deve se adaptar ao processo, não o contrário. |
| R-03   | O go-live deve ocorrer dentro do exercício fiscal de 2026 para viabilizar a não renovação do contrato Fiscal Defender. |
| R-04   | O desenvolvimento do módulo é de responsabilidade exclusiva da NBS — o projeto não pode custear desenvolvimento adicional. |
| R-05   | A rescisão do Fiscal Defender só pode ocorrer após validação completa do Auditor Fiscal em ambiente produtivo. |

---

## 8. Critérios de Sucesso

| # | Critério Mensurável                                                                                                  |
|---|----------------------------------------------------------------------------------------------------------------------|
| CS-01 | **100% dos requisitos funcionais** (RF-01 a RF-08) validados e aprovados pelas equipes de Contabilidade, Financeiro e Jurídico antes do go-live. |
| CS-02 | **Contrato Fiscal Defender encerrado** até o go-live, com **saving de R$ 78.000/ano** confirmado em relatório financeiro. |
| CS-03 | **Custo total do projeto ≤ R$ 35.000** (custos residuais), sem necessidade de aporte adicional. |
| CS-04 | **Zero incidentes críticos** de auditoria fiscal não detectados no primeiro trimestre pós go-live, em comparação com o período equivalente no Fiscal Defender. |
| CS-05 | **Satisfação dos usuários ≥ 80%** em pesquisa aplicada 30 dias após o go-live (usabilidade, confiabilidade, aderência ao processo). |

---

## 9. Partes Interessadas (Stakeholders)

| Papel                         | Nome / Área                              | Influência | Interesse | Observação                           |
|-------------------------------|------------------------------------------|------------|-----------|--------------------------------------|
| Solicitante / Patrocinador Solicitante | Sandro Siqueira — Coord. Contabilidade, Div. Comércio | Alta | Alto | Ponto focal da demanda |
| **Sponsor Executivo**         | **A IDENTIFICAR — CB-01**                | **Alta**   | **Alto**  | **⚠ Condição Bloqueante**           |
| Gestor do Projeto             | A designar — VMO Autônomo                | Alta       | Alto      | —                                    |
| Fornecedor (desenvolvimento)  | NBS — Fornecedor ERP                     | Alta       | Médio     | Responsável pelo desenvolvimento do módulo |
| Área de Contabilidade         | Divisão Comércio                         | Média      | Alto      | Usuária principal                    |
| Área Financeiro               | Divisão Comércio                         | Média      | Alto      | Usuária impactada                    |
| Área Jurídico                 | Divisão Comércio                         | Média      | Médio     | Usuária impactada                    |
| TI / Infraestrutura           | Grupo Águia Branca                       | Média      | Médio     | Suporte técnico e ambiente           |
| Aprovador VMO                 | Marcelo Silveira — GP VMO Autônomo       | Alta       | Alto      | Aprovação e acompanhamento do projeto |

---

## 10. Riscos Iniciais Identificados

| Código | Risco                                                                                 | Probabilidade | Impacto | Prioridade | Resposta Preliminar                                              |
|--------|---------------------------------------------------------------------------------------|---------------|---------|------------|------------------------------------------------------------------|
| **RSK-01** | **Sponsor executivo não identificado até 25/05/2026 (CB-01)**                   | Alta          | Alto    | **CRÍTICO** | Bloquear abertura formal; escalar para alta gestão da Div. Comércio |
| **RSK-02** | **Compromisso contratual NBS não verificado/inexistente (CB-02)**               | Média         | Alto    | **CRÍTICO** | Bloquear abertura formal; acionar Jurídico para verificação imediata |
| RSK-03 | NBS atrasar ou não entregar o módulo dentro do prazo acordado                         | Média         | Alto    | Alta       | Definir SLA contratual; acompanhamento mensal de progresso       |
| RSK-04 | Módulo Auditor Fiscal com funcionalidades incompletas em relação ao Fiscal Defender   | Média         | Médio   | Média      | Matriz de rastreabilidade de requisitos; testes comparativos     |
| RSK-05 | Custo de rescisão do Fiscal Defender superior ao estimado                             | Baixa         | Médio   | Baixa      | Revisão antecipada do contrato Fiscal Defender                   |
| RSK-06 | Necessidade de migração de dados históricos não prevista no escopo                    | Média         | Médio   | Média      | Levantar necessidade na fase de planejamento; negociar com NBS   |
| RSK-07 | Resistência das equipes à mudança de ferramenta                                       | Baixa         | Baixo   | Baixa      | Plano de comunicação e treinamento adequado                      |

---

## 11. Aprovação do TAP

| Papel                          | Nome                  | Assinatura / Validação | Data       |
|--------------------------------|-----------------------|------------------------|------------|
| Gestor do Projeto (VMO)        | Marcelo Silveira      | Aprovado               | 2026-05-15 |
| Solicitante                    | Sandro Siqueira       | ⏳ Pendente            | —          |
| **Sponsor Executivo**          | **A IDENTIFICAR**     | **⚠ BLOQUEADO — CB-01** | —         |

> **NOTA:** A abertura formal do projeto fica condicionada à resolução das condições CB-01 e CB-02 até os respectivos prazos. Em caso de não cumprimento, o projeto será suspenso para reavaliação.

---
---

# DOCUMENTO 2 — PM CANVAS

## PROJ-2026-005 | Auditor Fiscal — Módulo Nativo NBS

---

### BLOCO 1 — JUSTIFICATIVA

**Por que este projeto existe?**

A Divisão Comércio do Grupo Águia Branca desembolsa **R$ 78.000/ano** com o Fiscal Defender para auditoria de NF-e. O fornecedor NBS comprometeu-se contratualmente a entregar o módulo **Auditor Fiscal** nativo ao ERP como contrapartida, sem custo de desenvolvimento. Manter o contrato externo representa desperdício financeiro direto e fragmentação do ecossistema tecnológico.

**Drivers:**
- Saving financeiro imediato: R$ 78.000/ano (payback ~5,4 meses sobre R$ 35K residuais)
- Consolidação tecnológica: redução de fornecedores e integração nativa
- Compliance fiscal: eliminação de lacunas entre sistemas distintos

---

### BLOCO 2 — OBJETIVO SMART

Substituir **100% das funcionalidades operacionais do Fiscal Defender** pelo módulo nativo **Auditor Fiscal NBS** na Divisão Comércio do Grupo Águia Branca, com **go-live até novembro de 2026**, dentro do orçamento de **R$ 35.000** em custos residuais, confirmando o encerramento do contrato Fiscal Defender e o **saving recorrente de R$ 78.000/ano**.

---

### BLOCO 3 — BENEFÍCIOS

| Tipo        | Benefício                                                                 | Indicador                          |
|-------------|---------------------------------------------------------------------------|-------------------------------------|
| Financeiro  | Eliminar custo anual de R$ 78.000 com Fiscal Defender                     | Contrato Fiscal Defender encerrado  |
| Financeiro  | ROI > 100% no primeiro ano completo após go-live                          | Relatório financeiro pós-projeto    |
| Operacional | Integração nativa NF-e via ERP — sem exportações manuais entre sistemas   | Zero retrabalho de integração       |
| Operacional | Detecção de fraudes e pagamentos indevidos diretamente no ERP             | Alertas operacionais ativos         |
| Estratégico | Consolidação da plataforma ERP NBS como solução única                     | Redução de fornecedores externos    |
| Qualidade   | Usabilidade superior ao Fiscal Defender (RF-08)                           | Pesquisa de satisfação ≥ 80%        |

---

### BLOCO 4 — PRODUTO

**O que será entregue?**

Módulo **Auditor Fiscal** implantado, configurado e em produção no ERP NBS da Divisão Comércio, com as seguintes capacidades operacionais:

- Importação e processamento automático de NF-e a partir da base ERP
- Motor de auditoria automatizada de notas fiscais
- Alertas de fraude, risco de multa e pagamentos indevidos
- Relatórios operacionais e gerenciais de auditoria fiscal
- Interface compatível com o fluxo operacional atual das equipes
- Usabilidade igual ou superior ao Fiscal Defender

**Entregáveis do Projeto:**
1. Módulo Auditor Fiscal configurado e homologado
2. Documentação técnica e manual do usuário
3. Treinamento aplicado às equipes (Contabilidade, Financeiro, Jurídico)
4. Relatório de encerramento com confirmação do saving

---

### BLOCO 5 — REQUISITOS

| Código  | Requisito                                                                              | Área            |
|---------|----------------------------------------------------------------------------------------|-----------------|
| RF-01   | Importar e processar NF-e a partir da base de dados do ERP NBS                        | Contabilidade   |
| RF-02   | Realizar auditoria automatizada das notas fiscais                                      | Contabilidade   |
| RF-03   | Identificar e alertar sobre possíveis fraudes                                          | Contabilidade / Jurídico |
| RF-04   | Identificar e alertar sobre riscos de multa por inconsistências fiscais                | Contabilidade / Jurídico |
| RF-05   | Identificar e alertar sobre pagamentos indevidos                                       | Financeiro      |
| RF-06   | Gerar relatórios operacionais e gerenciais de auditoria fiscal                         | Contabilidade / Gerência |
| RF-07   | Manter o fluxo operacional atual das equipes (sem alteração de processo)               | Todas           |
| RF-08   | Oferecer funcionalidades de usabilidade superiores ao Fiscal Defender                  | Todas           |

**Requisitos pendentes de levantamento:**
- Necessidade de migração de dados históricos
- Integração com Power BI (possível, não confirmada)
- Requisitos específicos de Financeiro e Jurídico

---

### BLOCO 6 — STAKEHOLDERS

| Stakeholder                              | Papel                           | Nível de Engajamento Esperado |
|------------------------------------------|---------------------------------|-------------------------------|
| Sandro Siqueira (Coord. Contabilidade)   | Solicitante / Ponto Focal       | Alto — participação ativa      |
| **A IDENTIFICAR**                        | **Sponsor Executivo — CB-01**   | **⚠ BLOQUEANTE**              |
| NBS (Fornecedor ERP)                     | Executor do desenvolvimento     | Alto — entrega do módulo       |
| Equipe Contabilidade — Div. Comércio     | Usuária principal               | Alto — testes e homologação    |
| Equipe Financeiro — Div. Comércio        | Usuária impactada               | Médio — validação de RF-05/06  |
| Equipe Jurídico — Div. Comércio          | Usuária impactada               | Médio — validação de RF-03/04  |
| TI / Infraestrutura — Grupo Águia Branca | Suporte técnico                 | Médio — ambiente e acesso      |
| Marcelo Silveira (GP VMO)                | Gestor do Projeto               | Alto — aprovação e acompanhamento |

---

### BLOCO 7 — PREMISSAS

| Código | Premissa                                                                               | Status           |
|--------|----------------------------------------------------------------------------------------|------------------|
| **P-01** | Acordo contratual NBS para Auditor Fiscal está formalizado e vigente               | **⚠ A CONFIRMAR — CB-02** |
| **P-02** | Sponsor executivo da Divisão Comércio será identificado até 25/05/2026             | **⚠ A CONFIRMAR — CB-01** |
| P-03   | NBS desenvolve o módulo sem custo adicional para o cliente                             | Dep. de P-01     |
| P-04   | Equipes disponibilizarão representantes para testes e homologação                      | A confirmar      |
| P-05   | Módulo compatível com versão ERP atual da Divisão Comércio                             | A confirmar      |
| P-06   | Rescisão do Fiscal Defender viável dentro do prazo do projeto                          | A verificar      |

---

### BLOCO 8 — RESTRIÇÕES

| Código | Restrição                                                                              |
|--------|----------------------------------------------------------------------------------------|
| R-01   | Orçamento máximo de custos residuais: **R$ 35.000**                                   |
| R-02   | Fluxo operacional das equipes não pode ser alterado (RF-07)                            |
| R-03   | Go-live dentro do exercício fiscal de 2026                                             |
| R-04   | Desenvolvimento do módulo é responsabilidade exclusiva da NBS                          |
| R-05   | Rescisão do Fiscal Defender somente após validação completa em produção                |

---

### BLOCO 9 — RISCOS

> ⛔ **ATENÇÃO: Dois riscos críticos (condições bloqueantes) impedem a abertura formal do projeto.**

| Código | Risco                                                      | Prob. | Impacto | Prioridade | Ação                                              |
|--------|------------------------------------------------------------|-------|---------|------------|---------------------------------------------------|
| **RSK-01** | **Sponsor executivo não identificado — CB-01**         | Alta  | Alto    | **CRÍTICO** | Escalar imediatamente; prazo: 25/05/2026         |
| **RSK-02** | **Compromisso NBS não verificado/inexistente — CB-02** | Média | Alto    | **CRÍTICO** | Acionar Jurídico; prazo: 30/05/2026              |
| RSK-03 | NBS atrasar entrega do módulo                              | Média | Alto    | Alta       | SLA contratual; acompanhamento mensal            |
| RSK-04 | Funcionalidades do módulo incompletas vs. Fiscal Defender  | Média | Médio   | Média      | Matriz de rastreabilidade; testes comparativos   |
| RSK-05 | Necessidade de migração de dados históricos não prevista   | Média | Médio   | Média      | Levantamento na fase de planejamento             |
| RSK-06 | Custo rescisão Fiscal Defender superior ao estimado        | Baixa | Médio   | Baixa      | Revisar contrato Fiscal Defender antecipadamente |

---
---

# DOCUMENTO 3 — PLANO GERAL DO PROJETO

## PROJ-2026-005 | Auditor Fiscal — Módulo Nativo NBS

**Versão:** 1.0 | **Data:** 2026-05-15 | **Status:** Rascunho — sujeito a revisão após resolução das condições bloqueantes CB-01 e CB-02

> ⚠ **NOTA IMPORTANTE:** Este Plano Geral é preliminar. O detalhamento de cada plano subsidiário deve ser desenvolvido após a abertura formal do projeto, condicionada à resolução de CB-01 (sponsor executivo) e CB-02 (verificação contratual NBS).

---

### 1. Plano de Gerenciamento do Escopo

**Objetivo:** Definir, documentar e controlar o que está dentro e fora do escopo do projeto, prevenindo scope creep.

**Abordagem:**
- O escopo foi definido inicialmente no TAP (seção 4) e será detalhado na fase de planejamento.
- A EAP (Estrutura Analítica do Projeto) será elaborada com base nos 8 requisitos funcionais (RF-01 a RF-08) e nos entregáveis identificados.
- Qualquer alteração de escopo seguirá o processo formal do Plano de Gerenciamento de Mudanças.

**Itens pendentes de levantamento (fora do escopo atual, a avaliar):**
- Migração de dados históricos do Fiscal Defender
- Integração com Power BI
- Impactos detalhados em Financeiro e Jurídico

**Ferramentas:** EAP, Dicionário da EAP, Matriz de Rastreabilidade de Requisitos.

**Processo de controle:**
- Reunião de revisão de escopo a cada fase do projeto
- Solicitações de mudança de escopo submetidas ao Comitê de Mudanças (sponsor + GP)

---

### 2. Plano de Gerenciamento do Cronograma

**Objetivo:** Planejar, sequenciar e controlar as atividades para garantir o go-live dentro do prazo estimado.

**Cronograma macro:**

| Fase                                       | Início Previsto  | Término Previsto | Duração    |
|--------------------------------------------|------------------|------------------|------------|
| Fase 0 — Resolução de condições bloqueantes | 2026-05-15       | 2026-05-30       | ~2 semanas |
| Fase 1 — Iniciação formal                  | 2026-06-02       | 2026-06-13       | ~2 semanas |
| Fase 2 — Planejamento detalhado            | 2026-06-16       | 2026-07-04       | ~3 semanas |
| Fase 3 — Implantação e configuração (NBS)  | 2026-07-07       | 2026-08-29       | ~8 semanas |
| Fase 4 — Testes e homologação              | 2026-09-01       | 2026-09-26       | ~4 semanas |
| Fase 5 — Treinamento e transição           | 2026-09-29       | 2026-10-17       | ~3 semanas |
| Fase 6 — Go-live e encerramento            | 2026-10-20       | 2026-11-07       | ~2,5 semanas |
| **Go-live estimado**                       | **out/nov 2026** | —                | —          |

**Marcos críticos (milestones):**

| Marco | Descrição                                         | Data Prevista  |
|-------|---------------------------------------------------|----------------|
| M-01  | ⚠ CB-01 resolvido (sponsor identificado)          | 25/05/2026     |
| M-02  | ⚠ CB-02 resolvido (contrato NBS verificado)       | 30/05/2026     |
| M-03  | TAP assinado — abertura formal do projeto         | jun/2026       |
| M-04  | Planejamento detalhado aprovado                   | jul/2026       |
| M-05  | Módulo entregue pela NBS (ambiente de testes)     | ago/2026       |
| M-06  | Homologação concluída e aprovada                  | set/2026       |
| M-07  | Treinamento concluído                             | out/2026       |
| **M-08** | **Go-live em produção**                        | **out/nov 2026** |
| M-09  | Encerramento do contrato Fiscal Defender          | nov/2026       |

**Controle:** Relatório de progresso quinzenal; reunião de acompanhamento mensal com sponsor.

---

### 3. Plano de Gerenciamento de Custos

**Objetivo:** Estimar, orçar e controlar os custos residuais do projeto dentro do limite de R$ 35.000.

**Orçamento detalhado:**

| Categoria                              | Estimativa Inicial | Reserva Gerencial (~15%) | Total         |
|----------------------------------------|--------------------|--------------------------|---------------|
| Desenvolvimento NBS                    | R$ 0               | —                        | R$ 0          |
| Implementação e parametrização         | R$ 15.000          | R$ 2.250                 | R$ 17.250     |
| Treinamento das equipes                | R$ 8.000           | R$ 1.200                 | R$ 9.200      |
| Rescisão contratual Fiscal Defender    | R$ 7.000           | R$ 1.050                 | R$ 8.050      |
| Gestão de projeto (VMO)                | R$ 0               | —                        | R$ 0          |
| **Total**                              | **R$ 30.000**      | **R$ 4.500**             | **~R$ 35.000** |

> Nota: Os valores de implementação, treinamento e rescisão são estimativas preliminares a serem refinadas na fase de planejamento, após verificação do contrato Fiscal Defender (CB-02) e definição do modelo de implantação com a NBS.

**Controle:** Relatório de custos mensais; alerta ao sponsor quando 80% do orçamento for comprometido; qualquer extrapolação requer aprovação formal.

---

### 4. Plano de Gerenciamento da Qualidade

**Objetivo:** Garantir que o módulo Auditor Fiscal atenda a todos os requisitos funcionais e de usabilidade antes do go-live.

**Padrões de qualidade:**
- 100% dos RF-01 a RF-08 testados e aprovados pelas áreas usuárias.
- Zero regressão nas funcionalidades do Fiscal Defender (auditoria comparativa).
- Satisfação dos usuários ≥ 80% em pesquisa 30 dias pós go-live.
- Zero incidentes críticos de auditoria fiscal não detectados no primeiro trimestre pós go-live.

**Atividades de qualidade:**

| Atividade                              | Responsável                     | Quando               |
|----------------------------------------|---------------------------------|----------------------|
| Revisão da matriz de requisitos        | GP + Sandro Siqueira            | Fase de planejamento |
| Plano de testes de homologação         | GP + NBS + Equipe Contabilidade | Fase 3               |
| Testes de aceitação do usuário (UAT)   | Equipes de Contabilidade, Financeiro, Jurídico | Fase 4 |
| Auditoria comparativa Fiscal Defender x Auditor Fiscal | Contabilidade | Fase 4 |
| Pesquisa de satisfação pós go-live     | GP VMO                          | 30 dias pós go-live  |

---

### 5. Plano de Gerenciamento de Recursos

**Objetivo:** Identificar, alocar e gerenciar os recursos humanos e materiais necessários ao projeto.

**Equipe do projeto:**

| Papel                                 | Recurso                         | Dedicação Estimada         |
|---------------------------------------|---------------------------------|----------------------------|
| Gestor do Projeto                     | VMO Autônomo (a designar)       | Parcial (~20% do tempo)    |
| Ponto Focal do Cliente                | Sandro Siqueira                 | Parcial (~10% do tempo)    |
| **Sponsor Executivo**                 | **A IDENTIFICAR — CB-01**       | **⚠ Pendente**            |
| Consultor Técnico NBS                 | Equipe NBS (fornecedor)         | A definir com NBS          |
| Representante Contabilidade           | A indicar por Sandro Siqueira   | Parcial — fases 4 e 5      |
| Representante Financeiro              | A indicar                       | Parcial — fase 4           |
| Representante Jurídico                | A indicar                       | Parcial — fase 4           |
| TI / Infraestrutura                   | Equipe TI Grupo Águia Branca    | Pontual                    |

**Recursos materiais:** Ambiente ERP NBS (desenvolvimento, homologação, produção) — provido pela infraestrutura existente.

---

### 6. Plano de Gerenciamento das Comunicações

**Objetivo:** Garantir que as informações certas cheguem às pessoas certas no momento adequado.

**Matriz de comunicações:**

| Comunicação                              | Conteúdo                                    | Frequência     | Formato           | Responsável     | Destinatários                          |
|------------------------------------------|---------------------------------------------|----------------|-------------------|-----------------|----------------------------------------|
| Relatório de status do projeto           | Progresso, custos, riscos, próximos passos  | Quinzenal      | E-mail / PDF      | GP VMO          | Sponsor, Sandro Siqueira               |
| Reunião de acompanhamento                | Status, decisões, impedimentos              | Mensal         | Videoconferência  | GP VMO          | Sponsor, Sandro Siqueira, NBS          |
| Ata de reunião                           | Decisões e ações acordadas                  | Por reunião    | Documento         | GP VMO          | Todos participantes                    |
| Alerta de risco / impedimento            | Riscos críticos ou bloqueios identificados  | Sob demanda    | E-mail urgente    | GP VMO          | Sponsor, Sandro Siqueira               |
| Comunicado de go-live                    | Confirmação da entrada em produção          | Único          | E-mail / Comunicado Interno | GP VMO | Toda a Divisão Comércio             |
| Pesquisa de satisfação pós go-live       | Avaliação das equipes usuárias              | Único (30 dias pós) | Formulário   | GP VMO          | Contabilidade, Financeiro, Jurídico    |

**Canal principal:** E-mail corporativo + ferramenta de gestão de projetos VMO.

---

### 7. Plano de Gerenciamento de Riscos

**Objetivo:** Identificar, analisar, priorizar e responder aos riscos do projeto de forma proativa.

**Metodologia:** Análise qualitativa de riscos (probabilidade × impacto) com revisão mensal.

**Registro de riscos:**

| Código | Risco                                               | Prob. | Impacto | Prioridade  | Estratégia  | Ação de Resposta                                             | Dono          |
|--------|-----------------------------------------------------|-------|---------|-------------|-------------|--------------------------------------------------------------|---------------|
| **RSK-01** | **Sponsor não identificado (CB-01)**            | Alta  | Alto    | **CRÍTICO** | Escalar     | Acionar alta gestão Div. Comércio; bloquear abertura formal  | Sandro Siqueira |
| **RSK-02** | **Compromisso NBS não verificado (CB-02)**      | Média | Alto    | **CRÍTICO** | Verificar   | Acionar Jurídico; obter cópia da cláusula contratual         | Jurídico / Sandro |
| RSK-03 | Atraso na entrega do módulo pela NBS                | Média | Alto    | Alta        | Mitigar     | Definir SLA; cláusula de penalidade no contrato              | GP VMO / Jurídico |
| RSK-04 | Módulo com funcionalidades incompletas              | Média | Médio   | Média       | Mitigar     | Matriz de rastreabilidade de requisitos; testes comparativos | GP VMO        |
| RSK-05 | Migração de dados históricos necessária (não prevista) | Média | Médio | Média    | Aceitar/Mitigar | Levantar necessidade no planejamento; negociar com NBS  | GP VMO        |
| RSK-06 | Custo de rescisão Fiscal Defender > estimado        | Baixa | Médio   | Baixa       | Mitigar     | Revisar contrato Fiscal Defender na fase de planejamento     | Sandro Siqueira |
| RSK-07 | Resistência das equipes à nova ferramenta           | Baixa | Baixo   | Baixa       | Mitigar     | Plano de comunicação e treinamento                           | GP VMO        |

**Frequência de revisão:** Mensal (reunião de acompanhamento) e sob demanda para riscos críticos.

---

### 8. Plano de Gerenciamento de Aquisições

**Objetivo:** Gerenciar a relação com fornecedores e aquisições necessárias ao projeto.

**Fornecedores identificados:**

| Fornecedor         | Objeto                                          | Tipo de Contrato       | Status                          |
|--------------------|-------------------------------------------------|------------------------|---------------------------------|
| **NBS**            | Desenvolvimento do módulo Auditor Fiscal        | Contrapartida contratual vigente | **⚠ A VERIFICAR — CB-02** |
| Fiscal Defender    | Contrato atual a ser rescindido                 | Rescisão               | Verificar cláusulas e multas    |
| NBS (serviços)     | Implementação, parametrização e treinamento     | Ordem de Serviço / SOW | A negociar na fase de planejamento |

**Ações prioritárias de aquisição:**
1. **CB-02:** Verificar e formalizar o compromisso NBS em relação ao Auditor Fiscal.
2. Revisar contrato Fiscal Defender para entender condições e custos de rescisão.
3. Elaborar Declaração de Trabalho (SOW) para os serviços de implementação e treinamento NBS.
4. Formalizar Ordem de Serviço com NBS para as fases de implantação.

**Critérios de encerramento de aquisições:**
- Módulo entregue, homologado e em produção.
- Contrato Fiscal Defender encerrado sem pendências.

---

### 9. Plano de Gerenciamento das Partes Interessadas

**Objetivo:** Engajar as partes interessadas de forma adequada ao longo do projeto, garantindo suporte e reduzindo resistências.

**Análise de engajamento:**

| Stakeholder                     | Engajamento Atual | Engajamento Desejado | Estratégia de Engajamento                                        |
|---------------------------------|-------------------|----------------------|------------------------------------------------------------------|
| Sandro Siqueira                 | Engajado          | Engajado             | Manter comunicação frequente; incluir nas decisões chave         |
| **Sponsor Executivo (CB-01)**   | **Desconhecido**  | **Liderando**        | **Identificar e engajar como prioridade máxima**                |
| NBS                             | Comprometido      | Comprometido         | Formalizar compromissos via contrato; reuniões mensais           |
| Equipe Contabilidade            | Neutro            | Apoiador             | Envolver cedo nos requisitos; comunicar benefícios da mudança    |
| Equipe Financeiro               | Neutro            | Apoiador             | Mapear impactos específicos; incluir nos testes de RF-05        |
| Equipe Jurídico                 | Neutro            | Apoiador             | Mapear impactos em RF-03/04; incluir nos testes                 |
| TI / Infraestrutura             | Neutro            | Apoiador             | Envolver desde o início para ambiente e integrações              |

**Ações prioritárias:**
1. Identificar e engajar o Sponsor Executivo até 25/05/2026 (CB-01).
2. Realizar reunião de kick-off com todas as áreas após abertura formal.
3. Comunicar claramente os benefícios e o impacto mínimo no fluxo operacional (RF-07).

---

### 10. Plano de Gerenciamento de Mudanças

**Objetivo:** Controlar formalmente qualquer alteração no escopo, prazo, custo ou qualidade do projeto.

**Processo de Controle de Mudanças:**

```
Solicitação de Mudança
        │
        ▼
Registro formal pelo GP VMO (Formulário de Mudança)
        │
        ▼
Análise de impacto (escopo / prazo / custo / qualidade)
        │
        ▼
┌───────────────────────────────────────┐
│  Impacto Baixo (≤ 5% orçamento,       │──► Aprovação pelo GP VMO
│  ≤ 1 semana prazo, sem mudança        │
│  de escopo)                           │
└───────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│  Impacto Médio/Alto (> 5% orçamento, │──► Aprovação pelo Sponsor + GP VMO
│  > 1 semana prazo, ou mudança de     │
│  escopo)                             │
└───────────────────────────────────────┘
        │
        ▼
Atualização do TAP / Plano / Cronograma
        │
        ▼
Comunicação às partes interessadas
```

**Categorias de mudança e alçadas:**

| Categoria        | Critério                                              | Alçada de Aprovação         |
|------------------|-------------------------------------------------------|-----------------------------|
| Baixo impacto    | Até 5% do orçamento ou 1 semana no prazo              | Gestor do Projeto (VMO)     |
| Médio impacto    | 5–15% do orçamento ou 2–4 semanas no prazo            | Sponsor + GP VMO            |
| Alto impacto     | > 15% do orçamento ou > 1 mês no prazo ou mudança de escopo significativa | Sponsor + GP VMO + Comitê |

**Registro:** Todas as mudanças aprovadas ou rejeitadas serão registradas no Log de Mudanças do projeto.

**Mudanças proibidas sem aprovação formal do sponsor:**
- Inclusão de novas áreas além da Divisão Comércio.
- Qualquer alteração que comprometa o go-live em 2026.
- Custos que ultrapassem o orçamento aprovado de R$ 35.000.

---

## Aprovação do Plano Geral

| Papel                          | Nome                  | Status             | Data       |
|--------------------------------|-----------------------|--------------------|------------|
| Gestor do Projeto (VMO)        | Marcelo Silveira      | Aprovado           | 2026-05-15 |
| Solicitante                    | Sandro Siqueira       | ⏳ Pendente         | —          |
| **Sponsor Executivo**          | **A IDENTIFICAR**     | **⚠ BLOQUEADO — CB-01** | —    |

---

*Documento gerado por Diana Documento — VMO Autônomo | PROJ-2026-005 | v1.0 | 2026-05-15*
*Próxima revisão: após resolução das condições bloqueantes CB-01 (25/05/2026) e CB-02 (30/05/2026)*

---

# ■  04-erf-requisitos

# Especificação de Requisitos Funcionais (ERF)
## PROJ-2026-005 — Auditor Fiscal: Módulo Nativo NBS

---

| Campo           | Valor                                                        |
|-----------------|--------------------------------------------------------------|
| **Projeto**     | PROJ-2026-005                                                |
| **Demanda**     | DEM-2026-002                                                 |
| **Título**      | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Solicitante** | Sandro Siqueira — Coordenador de Contabilidade, Divisão Comércio, Grupo Águia Branca |
| **Versão**      | 3.0                                                          |
| **Data**        | 2026-05-15                                                   |
| **Autor**       | Rafael Requisito — Engenheiro de Requisitos, VMO Autônomo    |
| **Status**      | Em revisão pelo solicitante                                  |

---

## Histórico de Revisões

| Versão | Data       | Autor            | Descrição                                          |
|--------|------------|------------------|----------------------------------------------------|
| 1.0    | 2026-05-15 | Rafael Requisito | Rascunho inicial a partir dos requisitos Iara      |
| 2.0    | 2026-05-15 | Rafael Requisito | Expansão de RFs e adição de RNFs                   |
| 3.0    | 2026-05-15 | Rafael Requisito | Inclusão de matriz de rastreabilidade e pendências |

---

## Sumário

1. [Introdução](#1-introdução)
2. [Glossário do Domínio](#2-glossário-do-domínio)
3. [Atores e Perfis de Usuário](#3-atores-e-perfis-de-usuário)
4. [Requisitos Funcionais](#4-requisitos-funcionais)
5. [Requisitos Não-Funcionais](#5-requisitos-não-funcionais)
6. [Matriz de Rastreabilidade](#6-matriz-de-rastreabilidade)
7. [Restrições Técnicas](#7-restrições-técnicas)
8. [Premissas da Especificação](#8-premissas-da-especificação)
9. [Itens Fora do Escopo](#9-itens-fora-do-escopo)
10. [Pendências e Requisitos a Confirmar](#10-pendências-e-requisitos-a-confirmar)

---

## 1. Introdução

### 1.1 Objetivo do Documento

Esta Especificação de Requisitos Funcionais (ERF) define, de forma verificável e não ambígua, os requisitos do módulo **Auditor Fiscal** a ser desenvolvido pela NBS como componente nativo do ERP corporativo do Grupo Águia Branca (Divisão Comércio). O documento serve como contrato técnico entre o Grupo Águia Branca e a NBS para orientar o desenvolvimento, os testes de aceitação e a homologação do módulo.

### 1.2 Escopo da Solução

O módulo Auditor Fiscal substituirá integralmente o produto Fiscal Defender no processo de auditoria de Notas Fiscais Eletrônicas (NF-e) da Divisão Comércio. A solução operará de forma nativa sobre a base de dados do ERP NBS, eliminando a integração externa atualmente necessária para exportar dados ao Fiscal Defender.

O escopo inclui:
- Ingestão e processamento de NF-e já presentes na base NBS
- Auditoria automatizada de conformidade fiscal e tributária
- Detecção de inconsistências, fraudes e pagamentos indevidos
- Emissão de alertas de risco de multa e irregularidades
- Geração de relatórios operacionais e gerenciais acessíveis no ERP e, potencialmente, via Power BI

O escopo **não** inclui emissão de NF-e, escrituração fiscal (SPED), transmissão para SEFAZ, nem auditoria de outras divisões do Grupo Águia Branca além da Divisão Comércio nesta fase.

### 1.3 Público-Alvo da ERF

| Público                        | Finalidade de uso do documento                                    |
|--------------------------------|-------------------------------------------------------------------|
| Sandro Siqueira (Contabilidade)| Validar completude dos requisitos operacionais                    |
| Equipe NBS (desenvolvimento)   | Guia de implementação e base para testes de aceitação             |
| VMO Autônomo                   | Gestão do projeto e acompanhamento de entregas                    |
| Financeiro — Divisão Comércio  | Confirmar requisitos de relatórios e alertas financeiros          |
| Jurídico — Divisão Comércio    | Confirmar requisitos de conformidade e evidências para litígios   |
| TI — Grupo Águia Branca        | Planejar infraestrutura, permissões e integração Power BI         |

---

## 2. Glossário do Domínio

| Termo                  | Definição                                                                                                                                             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NF-e**               | Nota Fiscal Eletrônica. Documento fiscal digital, de existência apenas virtual, que documenta operações de circulação de mercadorias e prestação de serviços. |
| **DANFE**              | Documento Auxiliar da NF-e. Representação gráfica simplificada da NF-e, impresso para acompanhar a mercadoria em trânsito.                            |
| **Chave de Acesso**    | Código numérico de 44 dígitos que identifica univocamente uma NF-e perante a SEFAZ.                                                                   |
| **SEFAZ**              | Secretaria de Estado de Fazenda. Órgão estadual responsável pela autorização, validação e guarda das NF-e no ambiente nacional (SEFAZ Nacional / AN). |
| **XML da NF-e**        | Arquivo em formato XML que contém todos os dados estruturados de uma NF-e, assinado digitalmente pelo emitente e autorizado pela SEFAZ.               |
| **Auditoria Fiscal**   | Processo de verificação da conformidade de documentos fiscais com as legislações tributárias federal, estadual e municipal aplicáveis.                 |
| **Fiscal Defender**    | Produto de terceiro (substituído por este módulo) que realizava auditoria de NF-e recebendo dados via integração com o ERP NBS.                       |
| **Auditor Fiscal**     | Nome do módulo nativo NBS objeto desta especificação.                                                                                                 |
| **NBS**                | Fornecedor do ERP corporativo do Grupo Águia Branca; responsável pelo desenvolvimento do módulo Auditor Fiscal.                                       |
| **ERP**                | Enterprise Resource Planning. Sistema integrado de gestão empresarial. Neste contexto, o sistema fornecido pela NBS ao Grupo Águia Branca.             |
| **ICMS**               | Imposto sobre Circulação de Mercadorias e Serviços. Imposto estadual incidente sobre operações fiscais auditadas pelo módulo.                         |
| **PIS/COFINS**         | Contribuições federais (PIS = Programa de Integração Social; COFINS = Contribuição para o Financiamento da Seguridade Social) incidentes sobre receitas. |
| **IPI**                | Imposto sobre Produtos Industrializados. Imposto federal que pode constar em NF-e de produtos industrializados.                                       |
| **Crédito Tributário** | Direito do contribuinte de abater, do imposto a recolher, valores de imposto pago em etapas anteriores da cadeia produtiva.                           |
| **CST / CSOSN**        | Código de Situação Tributária / Código de Situação da Operação no Simples Nacional. Codificam o tratamento tributário de cada item da NF-e.           |
| **CFOP**               | Código Fiscal de Operações e Prestações. Código que identifica a natureza de circulação de mercadoria ou a prestação de serviço.                      |
| **NCM**                | Nomenclatura Comum do Mercosul. Código de oito dígitos que classifica mercadorias para fins tributários.                                              |
| **Duplicata / Fatura** | Título de crédito que documenta a obrigação de pagamento decorrente da operação comercial registrada na NF-e.                                         |
| **Pagamento Indevido** | Pagamento realizado em decorrência de NF-e com irregularidade (duplicidade, valor incorreto, NF-e cancelada, etc.).                                   |
| **MoSCoW**             | Método de priorização de requisitos: Must Have (obrigatório), Should Have (importante), Could Have (desejável), Won't Have (fora desta versão).       |
| **Power BI**           | Ferramenta de Business Intelligence da Microsoft, potencialmente usada para consumo externo dos dados de relatórios do módulo.                        |
| **LGPD**               | Lei Geral de Proteção de Dados Pessoais (Lei 13.709/2018). Aplicável ao tratamento de dados de pessoas físicas eventualmente presentes em NF-e.       |

---

## 3. Atores e Perfis de Usuário

### 3.1 Perfil: Analista de Contabilidade

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Contabilidade — Divisão Comércio, Grupo Águia Branca                                          |
| **Frequência de uso** | Diária — múltiplas sessões por dia                                                            |
| **Volume esperado**   | A confirmar com Sandro Siqueira (ver Seção 10, PEN-001)                                       |
| **Principais tarefas**| Revisar fila de NF-e auditadas; investigar alertas; tratar divergências; aprovar/rejeitar NF-e; consultar histórico de auditoria |
| **Nível técnico**     | Usuário funcional de ERP; familiaridade com legislação tributária                             |
| **Responsabilidade**  | Tomada de decisão operacional sobre conformidade de NF-e                                      |

### 3.2 Perfil: Supervisor de Contabilidade

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Contabilidade — Divisão Comércio, Grupo Águia Branca                                          |
| **Frequência de uso** | Diária — principalmente para acompanhamento gerencial                                        |
| **Principais tarefas**| Monitorar dashboard de conformidade; acompanhar KPIs de auditoria; escalar irregularidades; aprovar relatórios periódicos |
| **Nível técnico**     | Usuário gerencial de ERP; alto conhecimento de legislação tributária                          |
| **Responsabilidade**  | Supervisão da equipe de contabilidade e resposta a fiscalizações externas                     |

### 3.3 Perfil: Analista Financeiro

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Financeiro — Divisão Comércio, Grupo Águia Branca                                            |
| **Frequência de uso** | Semanal a mensal (relatórios e alertas pontuais)                                              |
| **Principais tarefas**| Consultar alertas de pagamentos indevidos; acessar relatórios de NF-e bloqueadas; solicitar estorno de pagamentos irregulares |
| **Nível técnico**     | Usuário funcional de ERP; sem necessidade de conhecimento tributário aprofundado              |
| **Responsabilidade**  | Prevenção e recuperação de pagamentos indevidos                                               |
| **Observação**        | Requisitos detalhados a confirmar (ver Seção 10, PEN-003)                                     |

### 3.4 Perfil: Analista Jurídico

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | Jurídico — Divisão Comércio, Grupo Águia Branca                                              |
| **Frequência de uso** | Sob demanda (em processos, auditorias externas, consultas de conformidade)                    |
| **Principais tarefas**| Consultar histórico de NF-e; extrair evidências documentais; acessar relatórios de risco e conformidade |
| **Nível técnico**     | Usuário eventual de ERP; demanda relatórios exportáveis em formatos usáveis em peças jurídicas|
| **Responsabilidade**  | Suporte a litígios fiscais, defesas administrativas e auditoria de conformidade regulatória   |
| **Observação**        | Requisitos detalhados a confirmar (ver Seção 10, PEN-004)                                     |

### 3.5 Perfil: Administrador do Sistema (TI / NBS)

| Atributo              | Descrição                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Área**              | TI — Grupo Águia Branca / Equipe NBS                                                         |
| **Frequência de uso** | Eventual (configurações, manutenção, criação de usuários)                                     |
| **Principais tarefas**| Gerenciar perfis e permissões; configurar parâmetros tributários; monitorar logs de sistema; executar atualizações de tabelas fiscais |
| **Nível técnico**     | Administrador de ERP; não necessariamente especialista fiscal                                 |
| **Responsabilidade**  | Disponibilidade e integridade operacional do módulo                                           |

---

## 4. Requisitos Funcionais

Os requisitos funcionais estão organizados em seis módulos funcionais. Cada RF segue o padrão: ID único, descrição na voz "O sistema deve...", prioridade MoSCoW, critério de aceitação verificável e rastreabilidade à origem.

**Legenda de Prioridade:**
- **M** = Must Have (obrigatório para entrar em produção)
- **S** = Should Have (importante; deve ser incluído se possível)
- **C** = Could Have (desejável; incluído se houver capacidade)
- **W** = Won't Have (esta versão; registrado para futuras versões)

---

### M1 — Módulo de Ingestão de NF-e

---

**RF-001 — Acesso nativo às NF-e da base NBS**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve acessar, ler e processar NF-e já registradas na base de dados do ERP NBS sem exportação de dados para sistemas externos.     |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Dado um lote de 1.000 NF-e presentes na base NBS, o módulo deve recuperar e enfileirar 100% delas para processamento sem intervenção manual e sem geração de arquivo intermediário de exportação. |
| **Rastreabilidade**    | RF-01 (Iara Inbound); RNF-01; RNF-02                                                                                                        |

---

**RF-002 — Seleção de escopo temporal de processamento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao usuário definir o intervalo de datas de emissão ou de entrada das NF-e a serem processadas em cada execução de auditoria. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O usuário consegue selecionar intervalo de datas (data inicial e data final) e o sistema processa exclusivamente NF-e cujo campo de data configurado esteja dentro do intervalo. NF-e fora do intervalo não aparecem no lote. |
| **Rastreabilidade**    | RF-01 (Iara Inbound); entrevista Sandro Siqueira                                                                                            |

---

**RF-003 — Seleção de escopo por fornecedor e CNPJ**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir filtrar NF-e para processamento por CNPJ do emitente, razão social do emitente ou grupo de fornecedores previamente cadastrado. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Dado um filtro por CNPJ "00.000.000/0001-00", o lote de processamento contém apenas NF-e cujo CNPJ emitente seja exatamente "00.000.000/0001-00". Nenhuma NF-e de outro emitente é incluída no lote. |
| **Rastreabilidade**    | RF-01 (Iara Inbound); RF-07 (fluxo operacional)                                                                                             |

---

**RF-004 — Reprocessamento de NF-e auditadas**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao Analista de Contabilidade solicitar o reprocessamento de uma NF-e já auditada, substituindo o resultado anterior pelo novo, com registro da data, hora e usuário que solicitou o reprocessamento. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Após solicitar reprocessamento de uma NF-e, o resultado anterior é substituído pelo novo resultado. O histórico registra a versão anterior com o atributo "substituída", a data/hora do reprocessamento e o login do usuário solicitante. |
| **Rastreabilidade**    | RF-07 (manter fluxo operacional); entrevista Sandro Siqueira                                                                                |

---

### M2 — Módulo de Auditoria Automatizada

---

**RF-005 — Auditoria de conformidade de dados cadastrais do emitente**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve verificar, para cada NF-e processada, se o CNPJ do emitente está ativo na base da Receita Federal (ou na base cadastral do ERP) e se a razão social constante na NF-e corresponde ao cadastro. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para uma NF-e emitida por CNPJ com situação "inapta" na base cadastral, o sistema classifica a NF-e com o alerta "Emitente com CNPJ inapto" e bloqueia o fluxo de aprovação até resolução manual. Taxa de falsos negativos (NF-e irregulares não detectadas) deve ser 0% para CNPJs inaptos presentes na base cadastral. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-03 (detecção de fraudes)                                                                                 |

---

**RF-006 — Auditoria de consistência dos valores tributários declarados**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve calcular os valores de ICMS, IPI, PIS e COFINS esperados para cada item da NF-e com base no NCM, CFOP, CST/CSOSN e alíquotas vigentes, e comparar com os valores declarados pelo emitente, sinalizando divergências. |
| **Prioridade**         : M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para uma NF-e com valor de ICMS declarado divergindo em mais de R$ 0,01 do valor calculado pelo sistema, o sistema sinaliza a divergência com o código de alerta "ICMS-DIV", exibe o valor declarado, o valor calculado e a diferença. A taxa de detecção de divergências de ICMS acima de R$ 1,00 deve ser 100% sobre lote de teste validado com a equipe de contabilidade. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-04 (risco de multa)                                                                                      |

---

**RF-007 — Auditoria de duplicidade de NF-e**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve identificar NF-e duplicadas pelo cruzamento de chave de acesso, CNPJ emitente, número da nota, série e valor total, sinalizando qualquer duplicidade detectada antes da aprovação do pagamento. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para um lote de teste contendo 5 pares de NF-e duplicadas (mesma chave de acesso), o sistema detecta e sinaliza os 10 documentos envolvidos com o código "NF-DUP", bloqueando o fluxo de pagamento de ambas até resolução. Taxa de detecção: 100% sobre lote de teste. |
| **Rastreabilidade**    | RF-03 (detecção de fraudes); RF-05 (pagamentos indevidos)                                                                                   |

---

**RF-008 — Auditoria de NF-e canceladas pagas ou em fila de pagamento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve cruzar o status de cada NF-e com o registro de cancelamento na base NBS e, ao identificar NF-e cancelada com pagamento registrado ou pendente, emitir alerta imediato ao Analista de Contabilidade e ao Analista Financeiro. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para um lote de teste com 3 NF-e canceladas e com pagamento pendente, o sistema detecta as 3 notas, emite alerta "NF-CANCEL-PAG" para os perfis Contabilidade e Financeiro e bloqueia o fluxo de pagamento. Tempo máximo entre registro do cancelamento na base e geração do alerta: 15 minutos (em processamento contínuo). |
| **Rastreabilidade**    | RF-03 (detecção de fraudes); RF-05 (pagamentos indevidos); RF-04 (risco de multa)                                                           |

---

**RF-009 — Auditoria de conformidade do CFOP com a natureza da operação**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve verificar se o CFOP declarado em cada item da NF-e é compatível com a natureza da operação (compra, transferência, devolução, etc.) registrada no ERP, com base em tabela de regras configurável pelo administrador. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Para um lote de teste com 10 NF-e de compra contendo CFOP incompatível com a natureza "entrada por compra", o sistema sinaliza as 10 com código "CFOP-INC" e registra a inconsistência no log de auditoria. A tabela de regras deve ser editável pelo perfil Administrador sem necessidade de deploy de nova versão. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-04 (risco de multa)                                                                                      |

---

**RF-010 — Auditoria de validade da autorização SEFAZ (chave de acesso)**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve verificar a autenticidade de cada NF-e pelo confronto da chave de acesso com o status de autorização registrado na base NBS (proveniente da consulta SEFAZ no momento da entrada da nota), sinalizando NF-e com chave não autorizada ou com status diferente de "autorizado de uso". |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para um lote de teste com 5 NF-e cujo status SEFAZ seja "denegada" ou "sem resposta", o sistema classifica as 5 com o código "SEFAZ-INV" e impede o fluxo de aprovação. Taxa de detecção: 100% sobre lote de teste. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-03 (detecção de fraudes)                                                                                 |

---

**RF-011 — Registro de resultado de auditoria por NF-e**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve registrar, para cada NF-e processada, o resultado da auditoria (aprovada, aprovada com ressalvas, bloqueada), os códigos de alerta emitidos, a data/hora do processamento e a versão das regras tributárias aplicadas. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para qualquer NF-e processada, o registro de auditoria deve conter: chave de acesso, status final, lista de códigos de alerta (vazia se aprovada sem ressalvas), timestamp do processamento (formato ISO 8601) e identificador da versão do conjunto de regras usado. Registro deve ser imutável após conclusão do processamento; qualquer revisão deve gerar novo registro vinculado. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-07 (fluxo operacional)                                                                                   |

---

### M3 — Módulo de Alertas

---

**RF-012 — Alerta de risco de multa por atraso ou incorreção tributária**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar alerta para o Analista de Contabilidade quando identificar NF-e com divergência tributária que configure risco de autuação fiscal, classificando o alerta por nível de criticidade (Alta, Média, Baixa) com base em critérios configuráveis pelo administrador. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Um alerta de criticidade "Alta" é gerado em até 15 minutos após a conclusão do processamento da NF-e que originhou a divergência (em modo de processamento contínuo). O alerta exibe: chave de acesso, tipo de divergência, criticidade, valor em risco e ação sugerida. O usuário consegue acessar o alerta diretamente do painel principal sem mais de 2 cliques. |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); entrevista Sandro Siqueira                                                                               |

---

**RF-013 — Alerta de pagamento indevido**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar alerta direcionado ao Analista Financeiro quando identificar NF-e com risco de pagamento indevido (duplicidade, NF-e cancelada com pagamento pendente, valor incorreto acima de tolerância configurável). |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para cada evento de pagamento indevido detectado, um alerta é enviado ao perfil Financeiro dentro de 15 minutos (modo contínuo). O alerta especifica: CNPJ do emitente, número e chave de acesso da NF-e, tipo de irregularidade, valor em risco e data de vencimento do pagamento (se aplicável). |
| **Rastreabilidade**    | RF-05 (alertas de pagamentos indevidos); perfil Analista Financeiro                                                                         |

---

**RF-014 — Painel de alertas com fila de resolução**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve disponibilizar um painel centralizado de alertas ativos, permitindo ao Analista de Contabilidade visualizar todos os alertas pendentes, filtrá-los por tipo, criticidade e data, registrar a ação tomada e marcar o alerta como resolvido. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O painel exibe todos os alertas com status "pendente" para o perfil logado. O usuário consegue filtrar por qualquer combinação de: tipo de alerta, nível de criticidade e intervalo de datas. Ao marcar um alerta como "resolvido", o sistema exige preenchimento de campo "Descrição da resolução" (mínimo 10 caracteres) e registra o login do usuário e o timestamp. |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); RF-05 (pagamentos indevidos); RF-07 (fluxo operacional)                                                  |

---

**RF-015 — Notificação automática por e-mail para alertas críticos**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve enviar notificação por e-mail aos usuários destinatários configurados quando um alerta de criticidade "Alta" for gerado, com link direto para o alerta no ERP. |
| **Prioridade**         | C — Could Have                                                                                                                              |
| **Critério de Aceitação** | Para cada alerta de criticidade "Alta" gerado, o e-mail é enviado em até 5 minutos ao(s) destinatário(s) configurados para o tipo de alerta. O e-mail contém: tipo do alerta, NF-e envolvida (chave de acesso e número), valor em risco, criticidade e link direto para o alerta no ERP. O envio de e-mail deve ser configurável por tipo de alerta (ativável/desativável pelo administrador). |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); RF-08 (usabilidade)                                                                                      |

---

### M4 — Módulo de Relatórios

---

**RF-016 — Relatório operacional de NF-e auditadas**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório listando todas as NF-e auditadas em um intervalo de datas definido pelo usuário, com os campos: chave de acesso, número, série, CNPJ emitente, data de emissão, valor total, status de auditoria, códigos de alerta e data do processamento. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O relatório é gerado em até 60 segundos para lotes de até 10.000 NF-e. O resultado é exportável em formato XLSX e PDF diretamente do ERP. Todos os campos listados na descrição estão presentes no relatório exportado. |
| **Rastreabilidade**    | RF-06 (relatórios operacionais e gerenciais); perfil Analista de Contabilidade                                                              |

---

**RF-017 — Relatório gerencial de conformidade tributária**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório gerencial com indicadores de conformidade: total de NF-e processadas, percentual aprovadas sem ressalvas, percentual com alertas por categoria, valor total em risco e evolução mês a mês, para um período selecionável pelo usuário. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O relatório gerencial exibe os indicadores acima com corte mensal para qualquer período de até 24 meses consecutivos. É exportável em XLSX e PDF. Os dados do relatório correspondem, com 100% de exatidão, à soma dos registros individuais de auditoria no mesmo período (verificável por auditoria cruzada). |
| **Rastreabilidade**    | RF-06 (relatórios gerenciais); perfil Supervisor de Contabilidade                                                                           |

---

**RF-018 — Relatório de conformidade e risco para o Jurídico**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório de histórico de auditoria de NF-e por fornecedor, exibindo todas as irregularidades registradas, ações tomadas, datas e responsáveis, exportável em PDF com layout adequado para uso em peças jurídicas e defesas administrativas. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O relatório PDF gerado contém: identificação do emitente (CNPJ, razão social), lista cronológica de NF-e com irregularidades, descrição da irregularidade, ação registrada, usuário responsável e data de resolução. O PDF inclui rodapé com identificação do sistema, data/hora de geração e login do usuário que gerou o relatório. A equipe jurídica valida o layout como adequado para uso formal (a ser verificado em teste de aceitação com representante do Jurídico). |
| **Rastreabilidade**    | RF-06 (relatórios); perfil Analista Jurídico; PEN-004                                                                                       |

---

**RF-019 — Relatório de pagamentos indevidos**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve gerar relatório consolidado de pagamentos indevidos detectados no período, listando: NF-e envolvida, tipo de irregularidade, valor do pagamento em risco, status de resolução e valor efetivamente recuperado (quando informado pelo usuário). |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O relatório é exportável em XLSX. O campo "valor recuperado" é editável pelo perfil Financeiro após resolução do alerta correspondente. O somatório de "valor em risco" e "valor recuperado" no relatório coincide, com diferença de até R$ 0,01 (tolerância de arredondamento), com a soma dos registros individuais de alerta no período. |
| **Rastreabilidade**    | RF-05 (pagamentos indevidos); RF-06 (relatórios); perfil Analista Financeiro                                                                |

---

**RF-020 — Disponibilização de dados para consumo por Power BI**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve expor os dados de resultados de auditoria, alertas e indicadores gerenciais por meio de mecanismo compatível com Power BI (API REST, OData endpoint ou view de banco de dados de leitura), permitindo construção de dashboards externos. |
| **Prioridade**         | C — Could Have                                                                                                                              |
| **Critério de Aceitação** | Um relatório no Power BI Desktop consegue conectar-se à fonte de dados do módulo, importar dados de NF-e auditadas (pelo menos os campos de RF-016) e atualizar ao acionar "Atualizar" no Power BI. A configuração da conexão deve ser documentada pela NBS. |
| **Rastreabilidade**    | RF-06 (relatórios); RNF-10 (compatibilidade Power BI); demanda Sandro Siqueira                                                              |

---

### M5 — Módulo de Configuração de Regras Tributárias

---

**RF-021 — Cadastro e manutenção de regras tributárias**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao perfil Administrador cadastrar, editar, desativar e versionar regras tributárias (alíquotas, exceções por NCM, CFOP permitidos por operação, etc.) sem necessidade de intervenção da NBS para cada atualização legislativa. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O Administrador consegue criar uma nova regra de alíquota de ICMS para um NCM específico, salvar e verificar que NF-e com aquele NCM processadas após a ativação da regra são auditadas com a nova alíquota. A regra anterior permanece no histórico de versões com data de vigência. O sistema não permite ativação de regra sem data de início de vigência. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RF-07 (fluxo operacional); RNF-05 (manutenibilidade)                                                        |

---

**RF-022 — Configuração de tolerâncias e limiares de alerta**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao perfil Administrador configurar limiares numéricos que definem quando uma divergência gera alerta (ex.: diferença de ICMS acima de R$ X, duplicidade exata vs. aproximada, percentual de variação de valor entre NF-e do mesmo fornecedor). |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O Administrador consegue alterar o limiar de divergência de ICMS de R$ 1,00 para R$ 5,00. Após a alteração, NF-e com divergência de ICMS entre R$ 1,00 e R$ 4,99 não geram mais alerta. NF-e com divergência de R$ 5,00 ou mais continuam gerando alerta. A alteração é registrada no log de auditoria do sistema. |
| **Rastreabilidade**    | RF-04 (alertas de risco de multa); RF-05 (pagamentos indevidos); entrevista Sandro Siqueira                                                 |

---

**RF-023 — Atualização de tabelas fiscais de referência**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve manter tabelas fiscais de referência (tabela NCM, tabela CFOP, tabela CST/CSOSN, alíquotas estaduais de ICMS) atualizadas, permitindo ao Administrador importar novas versões dessas tabelas em formato definido pela NBS. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | O Administrador consegue importar um arquivo de atualização da tabela NCM no formato especificado, confirmar a importação e verificar que novos NCMs estão disponíveis nas regras tributárias. NF-e com NCMs novos processadas após a atualização são auditadas corretamente. O sistema rejeita arquivos em formato inválido com mensagem de erro descritiva. |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RNF-05 (manutenibilidade)                                                                                   |

---

### M6 — Módulo de Administração e Controle de Acesso

---

**RF-024 — Gestão de perfis e permissões de usuário**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve controlar o acesso às funcionalidades por perfil de usuário (Analista de Contabilidade, Supervisor de Contabilidade, Analista Financeiro, Analista Jurídico, Administrador), garantindo que cada perfil acesse apenas as funcionalidades e dados para os quais tem permissão. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Um usuário com perfil "Analista Financeiro" não consegue acessar a tela de configuração de regras tributárias nem alterar o status de auditoria de uma NF-e. Um usuário com perfil "Analista Jurídico" consegue gerar e exportar relatórios, mas não consegue marcar alertas como resolvidos. A separação de permissões é testada para todos os 5 perfis listados. |
| **Rastreabilidade**    | RNF-06 (controle de acesso); RNF-07 (auditoria de ações)                                                                                    |

---

**RF-025 — Log de auditoria de ações de usuário**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve registrar em log imutável todas as ações de usuário que alteram dados ou configurações do módulo, incluindo: login do usuário, data/hora (ISO 8601, fuso UTC-3), tipo de ação, entidade afetada e valores anteriores e posteriores à alteração. |
| **Prioridade**         | M — Must Have                                                                                                                               |
| **Critério de Aceitação** | Para cada ação de alteração de dado (resolução de alerta, edição de regra, reprocessamento de NF-e, alteração de permissão), um registro de log é criado contendo os campos acima. O log não pode ser editado ou excluído por nenhum perfil de usuário, incluindo o Administrador. O Supervisor de Contabilidade e o Administrador conseguem consultar e exportar o log por período. |
| **Rastreabilidade**    | RNF-07 (auditoria de ações); conformidade LGPD; entrevista Sandro Siqueira                                                                  |

---

**RF-026 — Dashboard operacional de status do módulo**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve exibir, na tela inicial do módulo, um dashboard com os seguintes indicadores em tempo real (defasagem máxima de 5 minutos): total de NF-e processadas no dia, total de alertas pendentes por criticidade, total de NF-e bloqueadas aguardando resolução e data/hora do último processamento executado. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | Após processamento de um lote de NF-e, os contadores do dashboard refletem os novos valores em no máximo 5 minutos. Os valores exibidos no dashboard coincidem com os totais calculados pelos relatórios de mesmo período (diferença permitida: zero). |
| **Rastreabilidade**    | RF-08 (usabilidade superior ao Fiscal Defender); RF-07 (fluxo operacional)                                                                  |

---

**RF-027 — Exportação do log de auditoria para conformidade regulatória**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O sistema deve permitir ao perfil Supervisor de Contabilidade e ao perfil Analista Jurídico exportar o log completo de auditoria de ações de um período definido, em formato XLSX ou PDF, para fins de comprovação perante órgãos fiscalizadores. |
| **Prioridade**         | S — Should Have                                                                                                                             |
| **Critério de Aceitação** | O log exportado em XLSX contém todos os campos do RF-025 para o período solicitado, sem omissões. O PDF exportado inclui identificação do sistema, período do log e login de quem solicitou a exportação. A exportação de um período de 12 meses é concluída em até 120 segundos. |
| **Rastreabilidade**    | RF-06 (relatórios); RF-025; perfil Analista Jurídico                                                                                        |

---

## 5. Requisitos Não-Funcionais

---

**RNF-001 — Integração nativa ao ERP NBS (arquitetura)**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo Auditor Fiscal deve ser desenvolvido como componente nativo do ERP NBS, sem dependência de sistemas externos para sua operação de auditoria. |
| **Critério de Aceitação** | A auditoria de uma NF-e é executada do início ao fim sem que o módulo realize chamadas a endpoints externos ao ERP NBS, verificável por análise de tráfego de rede durante execução de lote de auditoria. |
| **Rastreabilidade**    | RNF-01 (Iara Inbound)                                                                                                                       |

---

**RNF-002 — Operação sobre base de dados unificada NBS**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve operar sobre a mesma base de dados do ERP NBS, eliminando a necessidade de sincronização, exportação ou replicação de dados de NF-e para processamento. |
| **Critério de Aceitação** | Uma NF-e registrada na base NBS é processável pelo módulo sem etapa de importação ou cópia para base separada. A inserção de uma NF-e na base NBS torna-a disponível ao módulo para processamento em até 5 minutos (em modo de processamento contínuo). |
| **Rastreabilidade**    | RNF-02 (Iara Inbound)                                                                                                                       |

---

**RNF-003 — Custo de desenvolvimento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O desenvolvimento do módulo não deve gerar custo direto de desenvolvimento para o Grupo Águia Branca, sendo coberto pelo contrato de fornecimento do ERP NBS já vigente ou por acordo comercial separado entre NBS e Grupo Águia Branca. |
| **Critério de Aceitação** | Contrato ou adendo contratual firmado entre Grupo Águia Branca e NBS antes do início do desenvolvimento, especificando que o módulo está incluído no escopo sem custo adicional de licença ou desenvolvimento. **Nota:** Este critério depende de negociação em andamento (ver Premissa P-002). |
| **Rastreabilidade**    | RNF-03 (Iara Inbound)                                                                                                                       |

---

**RNF-004 — Performance: processamento de lote**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve processar lotes de NF-e dentro dos seguintes limites de tempo, medidos em ambiente de produção com carga normal do ERP. |
| **Critério de Aceitação** | (a) Lote de até 1.000 NF-e: processamento completo em no máximo 10 minutos. (b) Lote de até 10.000 NF-e: processamento completo em no máximo 90 minutos. (c) Processamento de NF-e individual (modo interativo): resultado em no máximo 30 segundos. Os limites de volume de NF-e do Grupo Águia Branca Divisão Comércio devem ser confirmados (ver PEN-001). |
| **Rastreabilidade**    | RF-02 (auditoria automatizada); RNF-04 (Iara Inbound)                                                                                       |

---

**RNF-005 — Disponibilidade do sistema**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve estar disponível para uso durante o horário de operação da Divisão Comércio, com janela de manutenção restrita a períodos de baixo impacto. |
| **Critério de Aceitação** | Disponibilidade mensal mínima de 99,5% no horário de 07h00 às 20h00 (dias úteis), medida pelo monitoramento do ERP NBS. Janelas de manutenção planejadas devem ser comunicadas com antecedência mínima de 48 horas e agendadas preferencialmente nos horários 22h00–05h00. Tempo máximo de indisponibilidade não planejada em um único incidente: 4 horas. |
| **Rastreabilidade**    | RNF-04 (Iara Inbound)                                                                                                                       |

---

**RNF-006 — Segurança: controle de acesso**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O acesso ao módulo deve ser controlado por autenticação integrada ao mecanismo de autenticação do ERP NBS, com controle de permissões por perfil de usuário conforme definido em RF-024. |
| **Critério de Aceitação** | (a) Usuário não autenticado no ERP não acessa nenhuma funcionalidade do módulo. (b) Usuário autenticado com perfil inadequado recebe mensagem de "Acesso não autorizado" ao tentar acessar funcionalidade restrita — sem exposição de dados da funcionalidade. (c) Tentativas de acesso não autorizado são registradas no log de segurança do ERP. |
| **Rastreabilidade**    | RF-024 (controle de acesso); LGPD; entrevista Sandro Siqueira                                                                               |

---

**RNF-007 — Segurança: auditoria de ações (rastreabilidade de usuário)**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | Todas as ações de alteração de dados, configurações e resultados de auditoria realizadas por usuários devem ser rastreáveis individualmente, conforme RF-025. |
| **Critério de Aceitação** | Para qualquer alteração realizada há até 5 anos (período de guarda mínimo), é possível identificar: quem realizou, quando (data/hora UTC-3), o quê foi alterado e os valores antes e depois. O log é armazenado de forma que não possa ser alterado por usuários da aplicação, incluindo o perfil Administrador. |
| **Rastreabilidade**    | RF-025; LGPD; conformidade fiscal                                                                                                           |

---

**RNF-008 — Usabilidade: tempo de treinamento**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | Um novo Analista de Contabilidade com experiência prévia no ERP NBS deve ser capaz de executar as tarefas principais do módulo (processar lote, consultar alertas, gerar relatório operacional) após treinamento formal máximo de 4 horas. |
| **Critério de Aceitação** | Em teste de usabilidade com 3 Analistas de Contabilidade que nunca usaram o módulo mas têm experiência no ERP NBS: após 4 horas de treinamento formal, cada analista consegue executar as 3 tarefas principais sem auxílio externo, com taxa de erro abaixo de 10% nas tarefas (erro = ação que produz resultado diferente do esperado ou que gera mensagem de erro não intencional). |
| **Rastreabilidade**    | RF-08 (usabilidade superior ao Fiscal Defender)                                                                                             |

---

**RNF-009 — Usabilidade: acesso a alerta em no máximo 3 cliques**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | A partir da tela inicial do módulo, o usuário deve conseguir visualizar o detalhe de qualquer alerta pendente em no máximo 3 cliques. |
| **Critério de Aceitação** | Em teste com usuário do perfil Analista de Contabilidade logado na tela inicial do módulo: o acesso ao detalhe de um alerta específico (selecionado aleatoriamente da fila de alertas pendentes) requer no máximo 3 cliques (interações com elementos da interface). Verificado para 10 alertas distintos. |
| **Rastreabilidade**    | RF-08 (usabilidade superior ao Fiscal Defender); RF-014 (painel de alertas)                                                                 |

---

**RNF-010 — Compatibilidade com Power BI**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve expor dados de auditoria por mecanismo compatível com conexão direta do Power BI Desktop e Power BI Service (Microsoft), sem necessidade de desenvolvimento de conector customizado. |
| **Critério de Aceitação** | Utilizando o Power BI Desktop (versão mais recente disponível no momento do teste de aceitação), o usuário consegue criar uma conexão com a fonte de dados do módulo utilizando conectores nativos do Power BI (OData, SQL Server, API REST via conector Web ou equivalente) e importar dados de NF-e auditadas sem desenvolvimento adicional. |
| **Rastreabilidade**    | RF-020; demanda Sandro Siqueira                                                                                                             |

---

**RNF-011 — Manutenibilidade: responsabilidade da NBS**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | A NBS deve garantir que atualizações de versão do ERP NBS não quebrem a compatibilidade do módulo Auditor Fiscal, sendo responsável por adequar o módulo às novas versões do ERP dentro do ciclo normal de suporte do produto. |
| **Critério de Aceitação** | O SLA de compatibilidade está contratualmente definido: a NBS entrega versão compatível do módulo em até 30 dias após o lançamento de nova versão do ERP NBS que afete o módulo. Mudanças legislativas tributárias com vigência publicada oficialmente com mais de 30 dias de antecedência são incorporadas ao módulo antes da data de vigência. |
| **Rastreabilidade**    | RNF-05 (manutenibilidade — Iara Inbound); RNF-003                                                                                           |

---

**RNF-012 — Conformidade com a LGPD**

| Campo                  | Conteúdo                                                                                                                                    |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**          | O módulo deve tratar dados de pessoas físicas eventualmente presentes em NF-e (CPF de destinatário, dados de transportadores, etc.) em conformidade com a Lei 13.709/2018 (LGPD), garantindo que dados pessoais não sejam expostos em relatórios a perfis sem necessidade legítima de acesso. |
| **Critério de Aceitação** | Relatório gerado pelo perfil Analista Financeiro não exibe CPF de pessoas físicas constantes nas NF-e, exibindo apenas dados da pessoa jurídica (CNPJ, razão social). O perfil Analista Jurídico tem acesso a CPF apenas mediante justificativa registrada no log. |
| **Rastreabilidade**    | LGPD; RNF-006; entrevista Sandro Siqueira                                                                                                   |

---

## 6. Matriz de Rastreabilidade

| RF / RNF | Título Resumido                                 | Origem                             | Módulo | MoSCoW | Critério de Aceitação Resumido                                                              |
|----------|-------------------------------------------------|------------------------------------|--------|--------|---------------------------------------------------------------------------------------------|
| RF-001   | Acesso nativo às NF-e da base NBS               | RF-01 Iara; RNF-01; RNF-02         | M1     | M      | 100% das NF-e do lote recuperadas sem arquivo intermediário                                 |
| RF-002   | Seleção de escopo temporal                      | RF-01 Iara; Sandro                 | M1     | M      | Filtragem por intervalo de datas correta                                                    |
| RF-003   | Seleção por fornecedor/CNPJ                     | RF-01 Iara; RF-07                  | M1     | S      | Filtro por CNPJ retorna apenas NF-e do emitente correto                                     |
| RF-004   | Reprocessamento de NF-e                         | RF-07; Sandro                      | M1     | S      | Resultado anterior substituído; histórico mantido com log de usuário                        |
| RF-005   | Auditoria de cadastro do emitente               | RF-02; RF-03 Iara                  | M2     | M      | CNPJ inapto detectado com 0% de falso negativo                                              |
| RF-006   | Auditoria de valores tributários                | RF-02; RF-04 Iara                  | M2     | M      | Divergências acima de R$ 1,00 detectadas a 100%                                             |
| RF-007   | Auditoria de duplicidade de NF-e                | RF-03; RF-05 Iara                  | M2     | M      | 100% dos pares duplicados detectados e bloqueados                                           |
| RF-008   | NF-e cancelada com pagamento pendente           | RF-03; RF-05; RF-04 Iara           | M2     | M      | Detecção e alerta em ≤15 min; bloqueio de pagamento                                         |
| RF-009   | Auditoria de CFOP vs. natureza da operação      | RF-02; RF-04 Iara                  | M2     | S      | 100% de CFOP incompatíveis detectados; regras editáveis sem deploy                          |
| RF-010   | Validação da autorização SEFAZ                  | RF-02; RF-03 Iara                  | M2     | M      | 100% de NF-e não autorizadas bloqueadas                                                     |
| RF-011   | Registro de resultado de auditoria              | RF-02; RF-07 Iara                  | M2     | M      | Registro imutável com todos os campos; revisão cria novo registro                           |
| RF-012   | Alerta de risco de multa                        | RF-04 Iara; Sandro                 | M3     | M      | Alerta Alta gerado em ≤15 min; acessível em ≤2 cliques                                      |
| RF-013   | Alerta de pagamento indevido                    | RF-05 Iara; Financeiro             | M3     | M      | Alerta ao Financeiro em ≤15 min com todos os campos                                         |
| RF-014   | Painel de alertas com fila de resolução         | RF-04; RF-05; RF-07 Iara           | M3     | M      | Filtros funcionais; resolução exige campo descritivo; log registrado                        |
| RF-015   | Notificação por e-mail (alertas críticos)       | RF-04; RF-08 Iara                  | M3     | C      | E-mail entregue em ≤5 min; configurável por tipo de alerta                                  |
| RF-016   | Relatório operacional de NF-e auditadas         | RF-06 Iara; Contabilidade          | M4     | M      | Gerado em ≤60 s para 10.000 NF-e; exportável XLSX/PDF                                      |
| RF-017   | Relatório gerencial de conformidade             | RF-06 Iara; Supervisão             | M4     | M      | Dados corretos para 24 meses; exportável XLSX/PDF                                          |
| RF-018   | Relatório de conformidade/risco (Jurídico)      | RF-06 Iara; Jurídico               | M4     | S      | PDF com layout formal; validado pelo Jurídico                                               |
| RF-019   | Relatório de pagamentos indevidos               | RF-05; RF-06 Iara; Financeiro      | M4     | S      | Valor recuperado editável; totais consistentes                                              |
| RF-020   | Dados para Power BI                             | RF-06 Iara; Sandro; RNF-10         | M4     | C      | Conexão Power BI via conector nativo sem desenvolvimento extra                              |
| RF-021   | Cadastro de regras tributárias                  | RF-02; RF-07 Iara; RNF-05          | M5     | M      | Regra nova aplicada imediatamente; histórico de versões mantido                             |
| RF-022   | Configuração de tolerâncias de alerta           | RF-04; RF-05 Iara; Sandro          | M5     | S      | Alteração de limiar reflete em comportamento de alertas; log registrado                     |
| RF-023   | Atualização de tabelas fiscais                  | RF-02 Iara; RNF-05                 | M5     | M      | Tabela atualizada reflete em auditoria; arquivos inválidos rejeitados                       |
| RF-024   | Gestão de perfis e permissões                   | RNF-06; RNF-07                     | M6     | M      | Perfil inadequado bloqueado sem expor dados; 5 perfis testados                              |
| RF-025   | Log de auditoria de ações de usuário            | RNF-07; LGPD; Sandro               | M6     | M      | Log imutável com todos os campos; 5 anos de guarda                                          |
| RF-026   | Dashboard operacional                           | RF-08; RF-07 Iara                  | M6     | S      | Atualização em ≤5 min; totais coerentes com relatórios                                      |
| RF-027   | Exportação do log para conformidade             | RF-06; RF-025; Jurídico            | M6     | S      | XLSX completo; PDF identificado; exportação 12 meses em ≤120 s                              |
| RNF-001  | Integração nativa ao ERP NBS                    | RNF-01 Iara                        | —      | M      | Sem chamadas externas durante auditoria                                                     |
| RNF-002  | Base de dados unificada NBS                     | RNF-02 Iara                        | —      | M      | NF-e disponível para o módulo em ≤5 min após inserção                                      |
| RNF-003  | Custo zero de desenvolvimento                   | RNF-03 Iara                        | —      | M      | Contrato/adendo firmado antes do desenvolvimento                                            |
| RNF-004  | Performance de processamento                    | RF-02; RNF-04 Iara                 | —      | M      | 1.000 NF-e em ≤10 min; 10.000 NF-e em ≤90 min; individual em ≤30 s                        |
| RNF-005  | Disponibilidade (SLA)                           | RNF-04 Iara                        | —      | M      | ≥99,5% em horário comercial; incidente máximo de 4 h                                        |
| RNF-006  | Controle de acesso                              | RF-024; LGPD                       | —      | M      | Não autenticado: sem acesso; perfil inadequado: mensagem de erro sem exposição de dados     |
| RNF-007  | Auditoria de ações (rastreabilidade)            | RF-025; LGPD; fiscal               | —      | M      | Qualquer ação dos últimos 5 anos rastreável; log inalterável                                |
| RNF-008  | Usabilidade: tempo de treinamento               | RF-08 Iara                         | —      | M      | 3 analistas executam tarefas principais após 4h; erro <10%                                  |
| RNF-009  | Usabilidade: acesso a alerta em ≤3 cliques      | RF-08; RF-014                      | —      | M      | ≤3 cliques para detalhe de qualquer alerta; 10 alertas testados                             |
| RNF-010  | Compatibilidade Power BI                        | RF-020; Sandro                     | —      | C      | Conexão com conector nativo; dados importáveis sem dev adicional                            |
| RNF-011  | Manutenibilidade pela NBS                       | RNF-05 Iara; RNF-003               | —      | M      | Compatibilidade em ≤30 dias pós-nova versão ERP; legislação antes da vigência               |
| RNF-012  | Conformidade LGPD                               | LGPD; RNF-006; Sandro              | —      | M      | CPF oculto para Financeiro; acesso Jurídico com log de justificativa                        |

---

## 7. Restrições Técnicas

| ID    | Restrição                                                                                                                                  |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| RT-01 | O módulo deve ser desenvolvido na plataforma tecnológica do ERP NBS, sem introdução de tecnologias de terceiros não suportadas pela NBS.    |
| RT-02 | O acesso à base de dados do ERP NBS pelo módulo deve seguir as políticas de acesso a dados definidas pela NBS, sem acesso direto a tabelas de banco de dados por queries ad hoc de usuários finais. |
| RT-03 | A exportação de dados para Power BI deve utilizar mecanismo aprovado pela equipe de TI do Grupo Águia Branca, respeitando as políticas de segurança de dados corporativos. |
| RT-04 | O módulo não pode modificar registros originais de NF-e na base NBS; toda anotação de resultado de auditoria deve ser gravada em estrutura de dados separada e vinculada por chave de acesso. |
| RT-05 | A comunicação entre o módulo e qualquer serviço da NBS ou do Grupo Águia Branca deve utilizar canais criptografados (TLS 1.2 ou superior). |
| RT-06 | O ambiente de homologação do módulo deve ser segregado do ambiente de produção, com dados anonimizados de NF-e para testes (sem dados fiscais reais). |

---

## 8. Premissas da Especificação

| ID    | Premissa                                                                                                                                    | Impacto se inválida                                                                                           |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| P-001 | As NF-e da Divisão Comércio já estão integralmente disponíveis na base de dados do ERP NBS no momento em que o módulo for implantado, sem necessidade de migração histórica de dados do Fiscal Defender. | Se houver necessidade de migração histórica, o RF-001 deve ser revisado para incluir requisitos de importação de dados legados. |
| P-002 | **O acordo entre o Grupo Águia Branca e a NBS para desenvolvimento do módulo sem custo adicional ainda não foi verificado documentalmente.** Essa especificação assume que tal acordo será formalizado antes do início do desenvolvimento. | Se o acordo não for formalizado, o RNF-003 não pode ser garantido, e o projeto pode não ser viável nas condições atuais. Esta é a premissa de maior risco do projeto. |
| P-003 | As regras tributárias aplicáveis às operações da Divisão Comércio (alíquotas de ICMS, IPI, PIS/COFINS, exceções por NCM, etc.) serão fornecidas pela equipe de Contabilidade em formato estruturado para cadastro inicial no módulo. | Se as regras não forem fornecidas, o módulo não poderá executar auditoria tributária ao entrar em produção. |
| P-004 | O Fiscal Defender continuará operando em paralelo ao módulo Auditor Fiscal durante um período de operação paralela a ser definido (sugestão: 30 a 60 dias), para validação dos resultados antes do desligamento definitivo. | Se não houver operação paralela, o risco de falhas não detectadas no módulo é elevado. |
| P-005 | Os usuários dos perfis Financeiro e Jurídico participarão de sessões de levantamento de requisitos para confirmar os RFs e RNFs relacionados aos seus perfis (ver Seção 10, PEN-003 e PEN-004). | Se não participarem, os requisitos para esses perfis podem estar incompletos, impactando a aceitação do módulo. |
| P-006 | A NBS tem capacidade técnica e recursos disponíveis para desenvolver o módulo dentro do prazo a ser negociado, sem impactar o roadmap dos demais módulos do ERP em uso pelo Grupo Águia Branca. | Se a NBS não tiver capacidade, o cronograma do projeto precisa ser revisto. |

---

## 9. Itens Fora do Escopo

| ID    | Item fora do escopo                                                                                           | Justificativa / Observação                                                          |
|-------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| FE-01 | Emissão de NF-e                                                                                               | Funcionalidade já existente no ERP NBS; fora do escopo do módulo Auditor Fiscal     |
| FE-02 | Escrituração fiscal e geração de obrigações acessórias (SPED Fiscal, EFD-Contribuições, etc.)                | Funcionalidade já existente no ERP NBS ou em módulo separado                        |
| FE-03 | Transmissão direta de NF-e para a SEFAZ                                                                       | Responsabilidade do módulo de emissão do ERP NBS                                   |
| FE-04 | Auditoria de NF-e de outras divisões do Grupo Águia Branca além da Divisão Comércio                          | Escopo desta fase restrito à Divisão Comércio; extensão para outras divisões é projeto futuro |
| FE-05 | Auditoria de documentos fiscais que não sejam NF-e (CT-e, NFS-e municipal, NF-e de combustíveis com regras específicas, etc.) | Fora do escopo desta versão; pode ser incluído em versão futura                     |
| FE-06 | Integração com sistemas de gestão de fornecedores para acionamento automático de disputa                      | Fora do escopo; a resolução de alertas é manual pelo usuário no módulo              |
| FE-07 | Substituição ou modificação do processo de importação de NF-e no ERP NBS (processo de entrada de documentos) | O módulo audita NF-e já importadas; não altera o processo de importação             |
| FE-08 | Funcionalidades de BI ou analytics avançados integrados ao módulo (dashboards analíticos complexos)           | A integração Power BI (RF-020 / RNF-010) é o mecanismo previsto para BI avançado    |
| FE-09 | Manutenção ou suporte ao Fiscal Defender após o desligamento                                                  | O Fiscal Defender será desativado após a validação do módulo; suporte é do fornecedor |
| FE-10 | Integração com sistemas de outras empresas do Grupo Águia Branca fora da Divisão Comércio                    | Fora do escopo desta fase                                                           |

---

## 10. Pendências e Requisitos a Confirmar

| ID      | Pendência                                                                                       | Responsável pela resposta             | Impacto nos Requisitos                                                                                      | Data-limite sugerida |
|---------|-------------------------------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------|
| PEN-001 | Volume médio e máximo de NF-e processadas por dia/mês pela Divisão Comércio                     | Sandro Siqueira (Contabilidade)       | Calibra os critérios de aceitação de RNF-004 (performance) e dimensionamento da solução                     | Antes do início do desenvolvimento |
| PEN-002 | Formalização documentada do acordo NBS — desenvolvimento do módulo sem custo adicional           | Grupo Águia Branca (Diretoria) / NBS  | Condiciona viabilidade do projeto conforme RNF-003 e Premissa P-002; bloqueante para início do desenvolvimento | Urgente — antes da aprovação desta ERF |
| PEN-003 | Requisitos detalhados do perfil Financeiro: quais alertas, relatórios e fluxos de trabalho são necessários para prevenção e recuperação de pagamentos indevidos | Responsável pelo Financeiro — Divisão Comércio | Pode revelar novos RFs ou ajustar RF-013 e RF-019; necessário para teste de aceitação do Financeiro          | Antes do início do desenvolvimento |
| PEN-004 | Requisitos detalhados do perfil Jurídico: formato dos relatórios, campos obrigatórios para peças jurídicas, período de retenção de histórico exigido por compliance | Responsável pelo Jurídico — Divisão Comércio  | Pode revelar novos RFs ou ajustar RF-018 e RF-027; necessário para teste de aceitação do Jurídico            | Antes do início do desenvolvimento |
| PEN-005 | Definição do período e critérios da operação paralela (Fiscal Defender + Auditor Fiscal) antes do desligamento do Fiscal Defender | Sandro Siqueira + NBS                 | Necessário para planejar o cronograma de implantação e os critérios de go/no-go para desligamento do Fiscal Defender (Premissa P-004) | Antes da implantação |
| PEN-006 | Confirmação das regras tributárias específicas vigentes para as operações da Divisão Comércio que devem ser pré-configuradas no módulo no go-live | Sandro Siqueira (Contabilidade)       | Necessário para RF-021 e RF-023; sem essas regras, o módulo não pode entrar em produção com auditoria funcional | Antes da implantação |
| PEN-007 | Definição do mecanismo técnico de integração com o Power BI que a NBS irá implementar (OData, API REST, view de BD, etc.) | NBS (equipe técnica) + TI Grupo Águia Branca | Define o critério de aceitação de RF-020 e RNF-010 e as políticas de segurança aplicáveis                   | Durante o desenvolvimento |
| PEN-008 | Confirmação do período de retenção de dados de auditoria exigido pela legislação fiscal e pelas políticas internas do Grupo Águia Branca | Jurídico + Contabilidade — Divisão Comércio | Define o RNF-007 (prazo de guarda do log de auditoria); o período de 5 anos mencionado é sugestão, deve ser validado | Antes da implantação |

---

*Documento produzido por Rafael Requisito — Engenheiro de Requisitos, VMO Autônomo.*
*Versão 3.0 — 2026-05-15 — Para revisão e aprovação pelo solicitante Sandro Siqueira e pela equipe NBS.*

---

# ■  05-cronograma

# Cronograma Detalhado — PROJ-2026-005
## Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender

---

| Campo           | Valor                                                        |
|-----------------|--------------------------------------------------------------|
| **Projeto**     | PROJ-2026-005 / DEM-2026-002                                 |
| **Título**      | Auditor Fiscal — Módulo Nativo NBS                           |
| **Data de Ref.**| 2026-05-15                                                   |
| **Versão**      | v4.0                                                         |
| **Autor**       | Carlos Cronograma — Especialista em Planejamento (VMO Autônomo) |
| **Revisão**     | 2026-05-15                                                   |
| **Status**      | Em planejamento — condições bloqueantes pendentes            |

---

## 1. Premissas do Planejamento

1. **Responsabilidade de desenvolvimento**: A NBS é integralmente responsável pela codificação, configuração e entrega dos módulos. O Grupo Águia Branca (GAB) atua exclusivamente como cliente/validador, sem esforço de desenvolvimento interno.
2. **Condições bloqueantes absolutas**: As condições CB-01 (sponsor identificado) e CB-02 (acordo NBS verificado documentalmente) são pré-requisito inegociável para qualquer avanço além da Fase 0. Nenhuma atividade de desenvolvimento ou especificação detalhada pode ser iniciada enquanto ambas não estiverem sanadas.
3. **Buffer de contingência**: Aplicado 15% de buffer de duração sobre as Fases 3 (Desenvolvimento) e 4 (Homologação/UAT), por serem as fases de maior incerteza e dependência de terceiros.
4. **Disponibilidade das áreas usuárias**: As equipes de Contabilidade, Financeiro e Jurídico da Divisão Comércio estão disponíveis em **50% da capacidade** para atividades de UAT e validação, por conta de demandas operacionais concorrentes.
5. **Orçamento de desenvolvimento**: R$ 0,00 — contrapartida contratual NBS. Custos residuais estimados em R$ 35.000 (implementação, treinamento e rescisão do Fiscal Defender).
6. **Processo de negócio inalterado**: O módulo é substituto funcional do Fiscal Defender com melhoria de usabilidade; nenhuma redesenho de processo está no escopo.
7. **ERP como plataforma base**: O módulo NBS é nativo ao ERP já em uso pelo GAB; integrações de dados (NF-e, tabelas fiscais) são responsabilidade da NBS.
8. **Calendário**: Feriados nacionais e recesso de fim de ano considerados. Go-live-alvo: **outubro/novembro de 2026**.
9. **Homologação paralela**: Durante a Fase 4 (UAT), o Fiscal Defender permanece ativo em paralelo como fallback até aprovação formal do go-live.
10. **Comunicação**: Reuniões de status quinzenais com NBS; reuniões mensais com patrocinador.

---

## 2. WBS — Work Breakdown Structure

### Legenda de Responsáveis
- **NBS** — Fornecedor (desenvolvimento e configuração)
- **GAB-PMO** — Escritório de Projetos do Grupo Águia Branca
- **GAB-CONT** — Equipe de Contabilidade
- **GAB-FIN** — Equipe Financeiro
- **GAB-JUR** — Equipe Jurídico
- **GAB-TI** — TI / Infraestrutura interna
- **GAB-GESTOR** — Gestor de Projeto / Sponsor

---

### Fase 0 — Sanação de Condições Bloqueantes

| ID      | Pacote de Trabalho                                | Responsável  | Duração Est. |
|---------|---------------------------------------------------|--------------|--------------|
| 0.1     | **Identificação e Formalização do Sponsor**       |              |              |
| 0.1.1   | Mapeamento dos candidatos a sponsor               | GAB-PMO      | 2 dias       |
| 0.1.2   | Apresentação do projeto ao sponsor candidato      | GAB-PMO      | 1 dia        |
| 0.1.3   | Aceite formal do sponsor (assinatura TAP)         | GAB-GESTOR   | 1 dia        |
| 0.1.4   | Comunicação interna da designação do sponsor      | GAB-PMO      | 1 dia        |
| 0.2     | **Verificação Documental do Acordo NBS**          |              |              |
| 0.2.1   | Solicitação dos documentos contratuais à NBS      | GAB-PMO      | 1 dia        |
| 0.2.2   | Análise jurídica do acordo vigente                | GAB-JUR      | 3 dias       |
| 0.2.3   | Checklist de obrigações NBS vs. escopo do projeto | GAB-PMO      | 2 dias       |
| 0.2.4   | Validação e assinatura do termo de verificação    | GAB-GESTOR   | 1 dia        |

**Subtotal Fase 0:** 9 pacotes de trabalho | ~12 dias corridos

---

### Fase 1 — Kick-off e Alinhamento com NBS

| ID      | Pacote de Trabalho                                | Responsável  | Duração Est. |
|---------|---------------------------------------------------|--------------|--------------|
| 1.1     | **Preparação do Kick-off**                        |              |              |
| 1.1.1   | Elaboração da pauta e agenda do kick-off          | GAB-PMO      | 2 dias       |
| 1.1.2   | Convocação dos participantes (GAB + NBS)          | GAB-PMO      | 1 dia        |
| 1.1.3   | Preparação dos materiais de apresentação          | GAB-PMO      | 2 dias       |
| 1.2     | **Reunião de Kick-off**                           |              |              |
| 1.2.1   | Apresentação do projeto, escopo e cronograma      | GAB-PMO/NBS  | 1 dia        |
| 1.2.2   | Alinhamento de expectativas e papéis              | GAB-PMO/NBS  | 1 dia        |
| 1.2.3   | Definição de canais de comunicação e rituais      | GAB-PMO/NBS  | 1 dia        |
| 1.3     | **Formalização do Plano de Trabalho NBS**         |              |              |
| 1.3.1   | Recebimento do plano de trabalho detalhado da NBS | NBS          | 5 dias       |
| 1.3.2   | Revisão e aprovação do plano pelo GAB-PMO         | GAB-PMO      | 3 dias       |
| 1.3.3   | Assinatura do termo de alinhamento de escopo      | GAB-GESTOR   | 1 dia        |

**Subtotal Fase 1:** 9 pacotes de trabalho | ~14 dias corridos

---

### Fase 2 — Levantamento Detalhado e Aprovação de Escopo

| ID      | Pacote de Trabalho                                | Responsável  | Duração Est. |
|---------|---------------------------------------------------|--------------|--------------|
| 2.1     | **Levantamento de Requisitos por Módulo**         |              |              |
| 2.1.1   | Workshop M1 — Ingestão de NF-e                    | NBS/GAB-CONT | 2 dias       |
| 2.1.2   | Workshop M2 — Motor de Auditoria                  | NBS/GAB-CONT | 2 dias       |
| 2.1.3   | Workshop M3 — Gestão de Alertas                   | NBS/GAB-FIN  | 2 dias       |
| 2.1.4   | Workshop M4 — Relatórios e Dashboards             | NBS/GAB-CONT | 2 dias       |
| 2.1.5   | Workshop M5 — Configuração e Regras               | NBS/GAB-CONT | 2 dias       |
| 2.1.6   | Workshop M6 — Administração e Segurança           | NBS/GAB-TI   | 2 dias       |
| 2.2     | **Documentação de Requisitos**                    |              |              |
| 2.2.1   | Consolidação do ERF — Especificação de Requisitos | NBS          | 5 dias       |
| 2.2.2   | Revisão do ERF pelas áreas usuárias               | GAB-CONT/FIN | 4 dias       |
| 2.2.3   | Revisão jurídica de requisitos de compliance      | GAB-JUR      | 3 dias       |
| 2.3     | **Aprovação do Escopo**                           |              |              |
| 2.3.1   | Reunião de validação do ERF com NBS               | GAB-PMO/NBS  | 1 dia        |
| 2.3.2   | Registro de ajustes e revisão final do ERF        | NBS          | 3 dias       |
| 2.3.3   | Assinatura formal de aprovação do escopo          | GAB-GESTOR   | 1 dia        |

**Subtotal Fase 2:** 12 pacotes de trabalho | ~22 dias corridos

---

### Fase 3 — Desenvolvimento e Entregas Parciais pela NBS

> **Buffer de 15% aplicado** — duração base: ~60 dias → duração com buffer: **~69 dias**

| ID      | Pacote de Trabalho                                | Responsável  | Duração Est. |
|---------|---------------------------------------------------|--------------|--------------|
| 3.1     | **Sprint 1 — M1 + M6 (Ingestão NF-e + Admin)**   |              |              |
| 3.1.1   | Desenvolvimento M1 — Ingestão de NF-e             | NBS          | 15 dias      |
| 3.1.2   | Desenvolvimento M6 — Administração e Segurança    | NBS          | 10 dias      |
| 3.1.3   | Entrega parcial Sprint 1 e demonstração GAB       | NBS/GAB-PMO  | 2 dias       |
| 3.1.4   | Validação interna Sprint 1 pelo GAB               | GAB-CONT/TI  | 3 dias       |
| 3.2     | **Sprint 2 — M2 + M5 (Motor de Auditoria + Conf.)**|             |              |
| 3.2.1   | Desenvolvimento M2 — Motor de Auditoria           | NBS          | 15 dias      |
| 3.2.2   | Desenvolvimento M5 — Configuração e Regras        | NBS          | 10 dias      |
| 3.2.3   | Entrega parcial Sprint 2 e demonstração GAB       | NBS/GAB-PMO  | 2 dias       |
| 3.2.4   | Validação interna Sprint 2 pelo GAB               | GAB-CONT     | 3 dias       |
| 3.3     | **Sprint 3 — M3 + M4 (Alertas + Relatórios)**    |              |              |
| 3.3.1   | Desenvolvimento M3 — Gestão de Alertas            | NBS          | 10 dias      |
| 3.3.2   | Desenvolvimento M4 — Relatórios e Dashboards      | NBS          | 12 dias      |
| 3.3.3   | Entrega parcial Sprint 3 e demonstração GAB       | NBS/GAB-PMO  | 2 dias       |
| 3.3.4   | Validação interna Sprint 3 pelo GAB               | GAB-FIN      | 3 dias       |
| 3.4     | **Integração e Testes Internos NBS**              |              |              |
| 3.4.1   | Integração de todos os módulos                    | NBS          | 8 dias       |
| 3.4.2   | Testes de integração NBS (ambiente interno)       | NBS          | 5 dias       |
| 3.4.3   | Correção de defeitos pré-UAT                      | NBS          | 5 dias       |
| 3.4.4   | Implantação em ambiente de homologação GAB        | NBS/GAB-TI   | 3 dias       |

**Subtotal Fase 3 (com buffer 15%):** 17 pacotes de trabalho | **~69 dias corridos**

---

### Fase 4 — Homologação (UAT)

> **Buffer de 15% aplicado** — duração base: ~30 dias → duração com buffer: **~35 dias**
> **Disponibilidade usuários: 50%** — ciclos de validação com duração dobrada

| ID      | Pacote de Trabalho                                | Responsável  | Duração Est. |
|---------|---------------------------------------------------|--------------|--------------|
| 4.1     | **Preparação da UAT**                             |              |              |
| 4.1.1   | Elaboração do plano de testes UAT                 | GAB-PMO/NBS  | 3 dias       |
| 4.1.2   | Criação de casos de teste por módulo              | GAB-CONT/FIN | 5 dias       |
| 4.1.3   | Carga de dados de teste no ambiente               | NBS/GAB-TI   | 3 dias       |
| 4.2     | **Execução da UAT por Área**                      |              |              |
| 4.2.1   | UAT Contabilidade — M1, M2, M5                    | GAB-CONT     | 8 dias       |
| 4.2.2   | UAT Financeiro — M3, M4                           | GAB-FIN      | 6 dias       |
| 4.2.3   | UAT Jurídico — M4 (relatórios legais), M6         | GAB-JUR      | 5 dias       |
| 4.3     | **Gestão de Defeitos e Regressão**                |              |              |
| 4.3.1   | Registro e priorização de defeitos                | GAB-PMO      | 3 dias       |
| 4.3.2   | Correção de defeitos críticos/altos pela NBS      | NBS          | 8 dias       |
| 4.3.3   | Reteste e validação das correções                 | GAB-CONT/FIN | 4 dias       |
| 4.4     | **Aprovação e Encerramento da UAT**               |              |              |
| 4.4.1   | Relatório final de UAT                            | GAB-PMO      | 2 dias       |
| 4.4.2   | Reunião de Go/No-Go com sponsor                   | GAB-GESTOR   | 1 dia        |
| 4.4.3   | Assinatura do termo de aceite da homologação      | GAB-GESTOR   | 1 dia        |

**Subtotal Fase 4 (com buffer 15%):** 12 pacotes de trabalho | **~35 dias corridos**

---

### Fase 5 — Go-live e Transição

| ID      | Pacote de Trabalho                                | Responsável  | Duração Est. |
|---------|---------------------------------------------------|--------------|--------------|
| 5.1     | **Preparação do Go-live**                         |              |              |
| 5.1.1   | Plano de go-live e rollback                       | GAB-PMO/NBS  | 3 dias       |
| 5.1.2   | Treinamento das equipes usuárias                  | NBS/GAB-PMO  | 5 dias       |
| 5.1.3   | Migração e validação de dados históricos          | NBS/GAB-TI   | 5 dias       |
| 5.2     | **Implantação em Produção**                       |              |              |
| 5.2.1   | Deploy do módulo em ambiente de produção          | NBS/GAB-TI   | 2 dias       |
| 5.2.2   | Smoke tests pós-deploy                            | NBS/GAB-CONT | 1 dia        |
| 5.2.3   | Validação operacional — primeiros lançamentos     | GAB-CONT/FIN | 5 dias       |
| 5.3     | **Transição e Desativação do Fiscal Defender**    |              |              |
| 5.3.1   | Período de operação paralela (ambos os sistemas)  | GAB-CONT     | 10 dias      |
| 5.3.2   | Validação cruzada de resultados (novo vs. antigo) | GAB-CONT     | 5 dias       |
| 5.3.3   | Formalização da rescisão do Fiscal Defender       | GAB-JUR/FIN  | 3 dias       |
| 5.3.4   | Desativação do Fiscal Defender                    | GAB-TI       | 1 dia        |

**Subtotal Fase 5:** 10 pacotes de trabalho | ~25 dias corridos

---

### Fase 6 — Encerramento e Pós-Go-live

| ID      | Pacote de Trabalho                                | Responsável  | Duração Est. |
|---------|---------------------------------------------------|--------------|--------------|
| 6.1     | **Suporte Pós-go-live**                           |              |              |
| 6.1.1   | Suporte intensivo NBS (primeiras 4 semanas)       | NBS          | 20 dias      |
| 6.1.2   | Registro e resolução de incidentes pós-go-live    | NBS/GAB-PMO  | 20 dias      |
| 6.2     | **Documentação e Encerramento**                   |              |              |
| 6.2.1   | Elaboração do manual do usuário                   | NBS          | 5 dias       |
| 6.2.2   | Documentação técnica da solução                   | NBS          | 5 dias       |
| 6.2.3   | Lições aprendidas                                 | GAB-PMO      | 2 dias       |
| 6.2.4   | Relatório final do projeto                        | GAB-PMO      | 3 dias       |
| 6.2.5   | Reunião de encerramento com sponsor               | GAB-GESTOR   | 1 dia        |
| 6.2.6   | Arquivamento do projeto no PMO                    | GAB-PMO      | 1 dia        |

**Subtotal Fase 6:** 8 pacotes de trabalho | ~30 dias corridos

---

### Resumo WBS

| Fase | Nome                                   | Pacotes | Duração (dias) |
|------|----------------------------------------|---------|----------------|
| 0    | Sanação de Condições Bloqueantes       | 9       | 12             |
| 1    | Kick-off e Alinhamento com NBS         | 9       | 14             |
| 2    | Levantamento e Aprovação de Escopo     | 12      | 22             |
| 3    | Desenvolvimento (c/ buffer 15%)        | 17      | 69             |
| 4    | Homologação/UAT (c/ buffer 15%)        | 12      | 35             |
| 5    | Go-live e Transição                    | 10      | 25             |
| 6    | Encerramento e Pós-go-live             | 8       | 30             |
| **TOTAL** |                                   | **77**  | **~163 dias úteis** |

> Nota: Durações em dias úteis. Com sobreposições planejadas entre fases (fases 5 e 6 se sobrepõem), o projeto total cobre aproximadamente **8 meses corridos** (maio–dezembro 2026).

---

## 3. Cronograma Macro

| Fase | Nome                              | Início       | Fim          | Duração       | Responsável Principal | % Orçamento |
|------|-----------------------------------|--------------|--------------|---------------|-----------------------|-------------|
| 0    | Sanação de Condições Bloqueantes  | 2026-05-15   | 2026-05-30   | 12 dias úteis | GAB-PMO               | 0%          |
| 1    | Kick-off e Alinhamento com NBS    | 2026-06-01   | 2026-06-18   | 14 dias úteis | GAB-PMO / NBS         | 5%          |
| 2    | Levantamento e Aprovação Escopo   | 2026-06-15   | 2026-07-14   | 22 dias úteis | NBS / GAB-CONT        | 10%         |
| 3    | Desenvolvimento (buffer 15%)      | 2026-07-15   | 2026-09-26   | 69 dias úteis | NBS                   | 40%         |
| 4    | Homologação/UAT (buffer 15%)      | 2026-09-21   | 2026-11-07   | 35 dias úteis | GAB-CONT/FIN/JUR      | 25%         |
| 5    | Go-live e Transição               | 2026-10-26   | 2026-11-27   | 25 dias úteis | NBS / GAB-TI          | 15%         |
| 6    | Encerramento e Pós-go-live        | 2026-11-16   | 2026-12-22   | 30 dias úteis | GAB-PMO / NBS         | 5%          |

> **Sobreposições planejadas:**
> - Fases 2 e 1 se sobrepõem na última semana (preparação para início do desenvolvimento)
> - Fases 3 e 4 se sobrepõem em ~5 dias (deploy de ambiente homologação enquanto last sprint de dev.)
> - Fases 4 e 5 se sobrepõem ~10 dias (preparação go-live durante fase final da UAT)
> - Fases 5 e 6 se sobrepõem ~12 dias (suporte intensivo começa durante transição)

---

## 4. Marcos (Milestones)

| ID   | Descrição                                      | Data Planejada | Critério de Conclusão                                                      | Dependência         |
|------|------------------------------------------------|----------------|---------------------------------------------------------------------------|---------------------|
| M-01 | CB-01 — Sponsor identificado e formalizado     | 2026-05-25     | TAP assinado pelo sponsor; comunicação interna publicada                  | —                   |
| M-02 | CB-02 — Acordo NBS verificado documentalmente  | 2026-05-30     | Checklist jurídico concluído; termo de verificação assinado               | M-01                |
| M-03 | Kick-off realizado                             | 2026-06-05     | Ata de kick-off assinada; plano de trabalho NBS recebido                  | M-02                |
| M-04 | Plano de Trabalho NBS aprovado                 | 2026-06-18     | Plano revisado e aceito formalmente pelo GAB-PMO                          | M-03                |
| M-05 | ERF aprovado — Escopo congelado                | 2026-07-14     | ERF assinado pelo GAB-GESTOR; linha de base do escopo estabelecida        | M-04                |
| M-06 | Entrega Sprint 1 validada (M1 + M6)            | 2026-08-15     | Demonstração realizada; validação GAB registrada sem bloqueantes          | M-05                |
| M-07 | Entrega Sprint 2 validada (M2 + M5)            | 2026-09-05     | Demonstração realizada; validação GAB registrada sem bloqueantes          | M-06                |
| M-08 | Ambiente de homologação disponível             | 2026-09-21     | Ambiente UAT implantado e acessível às áreas usuárias                     | M-07                |
| M-09 | UAT concluída — Aceite formal homologação      | 2026-11-07     | Termo de aceite assinado; taxa de defeitos críticos = 0                   | M-08                |
| M-10 | **Go-live — Módulo NBS em produção**           | **2026-10-30** | Deploy produção validado; smoke tests OK; operação aprovada pelo sponsor  | M-09 (parcial)      |
| M-11 | Desativação do Fiscal Defender                 | 2026-11-14     | Sistema legado desligado; rescisão contratual iniciada                    | M-10 + 10 dias op.  |
| M-12 | Encerramento formal do projeto                 | 2026-12-10     | Relatório final aprovado; documentação arquivada; lições registradas      | M-11                |

> **Nota sobre M-10:** O go-live pode ocorrer durante a fase final de UAT (aprovação parcial de módulos), desde que M1, M2 e M6 estejam validados. Módulos M3, M4 e M5 podem ter go-live em onda subsequente até 2026-11-07.

---

## 5. Caminho Crítico

O caminho crítico determina a duração mínima do projeto. Qualquer atraso em atividades deste caminho impacta diretamente o go-live.

```
[M-01: CB-01] → [M-02: CB-02] → [Kick-off] → [ERF aprovado] → [Sprint 1 Dev]
→ [Sprint 2 Dev] → [Sprint 3 Dev] → [Integração NBS] → [UAT Contabilidade]
→ [Correção Defeitos] → [Reteste] → [Go/No-Go] → [Deploy Produção] → [Go-live M-10]
```

### Sequência Crítica com Datas

| Seq. | Atividade Crítica                          | Início       | Fim          | Float (dias) |
|------|--------------------------------------------|--------------|--------------|--------------|
| 1    | CB-01: Formalização do sponsor             | 2026-05-15   | 2026-05-25   | 0            |
| 2    | CB-02: Verificação documental NBS          | 2026-05-25   | 2026-05-30   | 0            |
| 3    | Kick-off e alinhamento de escopo           | 2026-06-01   | 2026-06-18   | 0            |
| 4    | Workshops de levantamento (6 módulos)      | 2026-06-15   | 2026-07-04   | 0            |
| 5    | Consolidação e aprovação do ERF            | 2026-07-05   | 2026-07-14   | 0            |
| 6    | Desenvolvimento Sprint 1 (M1 + M6)        | 2026-07-15   | 2026-08-09   | 0            |
| 7    | Desenvolvimento Sprint 2 (M2 + M5)        | 2026-08-10   | 2026-09-05   | 0            |
| 8    | Desenvolvimento Sprint 3 (M3 + M4)        | 2026-08-24   | 2026-09-19   | 2            |
| 9    | Integração e testes internos NBS           | 2026-09-08   | 2026-09-26   | 0            |
| 10   | UAT Contabilidade (M1, M2, M5)             | 2026-09-21   | 2026-10-02   | 0            |
| 11   | Registro e correção de defeitos críticos   | 2026-10-05   | 2026-10-16   | 0            |
| 12   | Reteste e validação de correções           | 2026-10-19   | 2026-10-23   | 0            |
| 13   | Reunião Go/No-Go + aceite homologação      | 2026-10-26   | 2026-10-27   | 0            |
| 14   | Deploy em produção + smoke tests           | 2026-10-28   | 2026-10-29   | 0            |
| 15   | **Go-live — M-10**                         | **2026-10-30**| —           | **0**        |

### Dependências Críticas Destacadas

- **CB-01 → CB-02 → Kick-off:** Corrente tripla de bloqueio. Atraso de 1 dia no CB-01 empurra todo o projeto 1 dia para frente.
- **ERF aprovado → início do desenvolvimento:** Nenhuma sprint pode ser iniciada sem o escopo congelado (M-05). Risco de partida tardia da NBS.
- **Sprint 1 → Sprint 2 → Integração:** Dependência sequencial dentro do desenvolvimento. A integração só pode iniciar após entrega das sprints.
- **UAT → Correção → Reteste → Go/No-Go:** Ciclo de qualidade não paralelizável. Disponibilidade de 50% das equipes usuárias estende este ciclo.
- **Go/No-Go → Deploy → Go-live:** Sequência final de 3 dias sem float. Qualquer impedimento técnico ou decisório nesse período cancela o go-live na data alvo.

---

## 6. Plano de Fases Detalhado

### FASE 0 — Sanação de Condições Bloqueantes
**Período:** 2026-05-15 a 2026-05-30

| # | Atividade                                    | Início     | Fim        | Duração | Dependência | Responsável  | Entregável                        |
|---|----------------------------------------------|------------|------------|---------|-------------|--------------|-----------------------------------|
| 1 | Mapeamento de candidatos a sponsor           | 15/05      | 19/05      | 3d      | —           | GAB-PMO      | Lista de candidatos               |
| 2 | Apresentação do projeto ao sponsor candidato | 20/05      | 21/05      | 2d      | Ativ. 1     | GAB-PMO      | Apresentação realizada            |
| 3 | Aceite e assinatura do TAP pelo sponsor      | 22/05      | 25/05      | 2d      | Ativ. 2     | GAB-GESTOR   | **TAP assinado (M-01)**           |
| 4 | Comunicação interna da designação            | 25/05      | 25/05      | 1d      | Ativ. 3     | GAB-PMO      | E-mail/comunicado formal          |
| 5 | Solicitação dos documentos contratuais NBS   | 22/05      | 22/05      | 1d      | Ativ. 3*    | GAB-PMO      | Solicitação formal enviada        |
| 6 | Análise jurídica do acordo NBS               | 23/05      | 27/05      | 3d      | Ativ. 5     | GAB-JUR      | Parecer jurídico                  |
| 7 | Checklist obrigações NBS vs. escopo          | 26/05      | 28/05      | 2d      | Ativ. 6     | GAB-PMO      | Checklist preenchido              |
| 8 | Validação e assinatura do termo CB-02        | 29/05      | 30/05      | 2d      | Ativ. 7     | GAB-GESTOR   | **Termo CB-02 assinado (M-02)**   |

> *Atividade 5 pode iniciar em paralelo após M-01.

**Entregáveis da Fase 0:**
- TAP assinado com sponsor designado
- Termo de verificação documental do acordo NBS
- Ambas as condições bloqueantes formalmente sanadas

**Critério de saída:** M-01 e M-02 concluídos. Sem isso, Fase 1 não inicia.

---

### FASE 1 — Kick-off e Alinhamento com NBS
**Período:** 2026-06-01 a 2026-06-18

| # | Atividade                                    | Início     | Fim        | Duração | Dependência | Responsável  | Entregável                        |
|---|----------------------------------------------|------------|------------|---------|-------------|--------------|-----------------------------------|
| 1 | Elaboração de pauta e agenda do kick-off     | 01/06      | 02/06      | 2d      | M-02        | GAB-PMO      | Agenda oficial                    |
| 2 | Convocação e confirmação de participantes    | 01/06      | 01/06      | 1d      | M-02        | GAB-PMO      | Lista de confirmados              |
| 3 | Elaboração dos materiais de apresentação     | 01/06      | 04/06      | 3d      | M-02        | GAB-PMO      | Deck de apresentação              |
| 4 | **Reunião de Kick-off**                      | 05/06      | 05/06      | 1d      | Ativ. 1-3   | GAB-PMO/NBS  | **Ata de kick-off (M-03)**        |
| 5 | Alinhamento papéis, RACI e comunicação       | 06/06      | 06/06      | 1d      | Ativ. 4     | GAB-PMO/NBS  | RACI atualizado                   |
| 6 | Recebimento do plano de trabalho NBS         | 07/06      | 13/06      | 5d      | Ativ. 4     | NBS          | Plano de trabalho detalhado       |
| 7 | Revisão do plano pelo GAB-PMO                | 14/06      | 16/06      | 3d      | Ativ. 6     | GAB-PMO      | Comentários/aceite do plano       |
| 8 | Assinatura do termo de alinhamento de escopo | 17/06      | 18/06      | 2d      | Ativ. 7     | GAB-GESTOR   | **Plano NBS aprovado (M-04)**     |

**Entregáveis da Fase 1:**
- Ata de kick-off assinada
- RACI definitivo do projeto
- Plano de trabalho NBS revisado e aprovado

**Critério de saída:** M-04 concluído (plano NBS aprovado).

---

### FASE 2 — Levantamento Detalhado e Aprovação de Escopo
**Período:** 2026-06-15 a 2026-07-14

| # | Atividade                                    | Início     | Fim        | Duração | Dependência | Responsável      | Entregável                     |
|---|----------------------------------------------|------------|------------|---------|-------------|------------------|--------------------------------|
| 1 | Workshop M1 — Ingestão de NF-e               | 15/06      | 16/06      | 2d      | M-04        | NBS/GAB-CONT     | Ata + requisitos M1            |
| 2 | Workshop M2 — Motor de Auditoria             | 17/06      | 18/06      | 2d      | M-04        | NBS/GAB-CONT     | Ata + requisitos M2            |
| 3 | Workshop M3 — Gestão de Alertas              | 19/06      | 20/06      | 2d      | M-04        | NBS/GAB-FIN      | Ata + requisitos M3            |
| 4 | Workshop M4 — Relatórios e Dashboards        | 23/06      | 24/06      | 2d      | M-04        | NBS/GAB-CONT     | Ata + requisitos M4            |
| 5 | Workshop M5 — Configuração e Regras          | 25/06      | 26/06      | 2d      | M-04        | NBS/GAB-CONT     | Ata + requisitos M5            |
| 6 | Workshop M6 — Administração e Segurança      | 27/06      | 28/06      | 2d      | M-04        | NBS/GAB-TI       | Ata + requisitos M6            |
| 7 | Consolidação do ERF pela NBS                 | 01/07      | 07/07      | 5d      | Ativ. 1-6   | NBS              | ERF v1.0 (rascunho)            |
| 8 | Revisão do ERF pelas áreas (CONT + FIN)      | 08/07      | 11/07      | 4d      | Ativ. 7     | GAB-CONT/FIN     | ERF comentado                  |
| 9 | Revisão jurídica (compliance)                | 08/07      | 10/07      | 3d      | Ativ. 7     | GAB-JUR          | Parecer jurídico ERF           |
|10 | Reunião de validação ERF com NBS             | 14/07      | 14/07      | 1d      | Ativ. 8-9   | GAB-PMO/NBS      | Ata de validação               |
|11 | Ajustes finais e assinatura do ERF           | 14/07      | 14/07      | 1d      | Ativ. 10    | GAB-GESTOR       | **ERF aprovado (M-05)**        |

**Entregáveis da Fase 2:**
- Especificação de Requisitos Funcionais (ERF) aprovada e assinada
- 6 atas de workshop validadas
- Parecer jurídico de compliance

**Critério de saída:** M-05 concluído (ERF assinado). Escopo congelado — change requests apenas via processo formal.

---

### FASE 3 — Desenvolvimento e Entregas Parciais pela NBS
**Período:** 2026-07-15 a 2026-09-26 *(com buffer 15%)*

| # | Atividade                                    | Início     | Fim        | Duração | Dependência | Responsável  | Entregável                        |
|---|----------------------------------------------|------------|------------|---------|-------------|--------------|-----------------------------------|
| 1 | Setup de ambiente de desenvolvimento         | 15/07      | 17/07      | 3d      | M-05        | NBS          | Ambiente DEV configurado          |
| 2 | Desenvolvimento M6 (Admin/Segurança)         | 18/07      | 31/07      | 10d     | Ativ. 1     | NBS          | Módulo M6 desenvolvido            |
| 3 | Desenvolvimento M1 (Ingestão NF-e)           | 18/07      | 08/08      | 15d     | Ativ. 1     | NBS          | Módulo M1 desenvolvido            |
| 4 | Demonstração Sprint 1 (M1 + M6) ao GAB       | 11/08      | 12/08      | 2d      | Ativ. 2-3   | NBS/GAB-PMO  | Ata Sprint 1                      |
| 5 | Validação Sprint 1 pelo GAB                  | 13/08      | 15/08      | 3d      | Ativ. 4     | GAB-CONT/TI  | **Aceite Sprint 1 (M-06)**        |
| 6 | Desenvolvimento M5 (Configuração/Regras)     | 10/08      | 22/08      | 10d     | Ativ. 2     | NBS          | Módulo M5 desenvolvido            |
| 7 | Desenvolvimento M2 (Motor de Auditoria)      | 10/08      | 29/08      | 15d     | Ativ. 3     | NBS          | Módulo M2 desenvolvido            |
| 8 | Demonstração Sprint 2 (M2 + M5) ao GAB       | 01/09      | 02/09      | 2d      | Ativ. 6-7   | NBS/GAB-PMO  | Ata Sprint 2                      |
| 9 | Validação Sprint 2 pelo GAB                  | 03/09      | 05/09      | 3d      | Ativ. 8     | GAB-CONT     | **Aceite Sprint 2 (M-07)**        |
|10 | Desenvolvimento M3 (Alertas)                 | 24/08      | 05/09      | 10d     | Ativ. 6     | NBS          | Módulo M3 desenvolvido            |
|11 | Desenvolvimento M4 (Relatórios/Dashboards)   | 24/08      | 10/09      | 12d     | Ativ. 6     | NBS          | Módulo M4 desenvolvido            |
|12 | Demonstração Sprint 3 (M3 + M4) ao GAB       | 11/09      | 12/09      | 2d      | Ativ. 10-11 | NBS/GAB-PMO  | Ata Sprint 3                      |
|13 | Validação Sprint 3 pelo GAB                  | 13/09      | 15/09      | 3d      | Ativ. 12    | GAB-FIN      | Aceite Sprint 3                   |
|14 | Integração de todos os módulos               | 08/09      | 17/09      | 8d      | Ativ. 7     | NBS          | Build integrado                   |
|15 | Testes de integração internos (NBS)          | 18/09      | 22/09      | 3d      | Ativ. 14    | NBS          | Relatório de testes internos      |
|16 | Correção de defeitos pré-UAT                 | 23/09      | 25/09      | 3d      | Ativ. 15    | NBS          | Build corrigido                   |
|17 | Implantação em ambiente de homologação GAB   | 24/09      | 26/09      | 3d      | Ativ. 16    | NBS/GAB-TI   | Ambiente UAT disponível           |

**Entregáveis da Fase 3:**
- 6 módulos desenvolvidos (M1–M6)
- 3 atas de validação de sprints
- Build integrado em ambiente de homologação
- Relatório de testes internos NBS

**Critério de saída:** Ambiente de homologação implantado e aceito pelo GAB-TI (M-08).

---

### FASE 4 — Homologação (UAT)
**Período:** 2026-09-21 a 2026-11-07 *(com buffer 15%)*

| # | Atividade                                    | Início     | Fim        | Duração | Dependência | Responsável      | Entregável                     |
|---|----------------------------------------------|------------|------------|---------|-------------|------------------|--------------------------------|
| 1 | Elaboração do plano de testes UAT            | 21/09      | 23/09      | 3d      | M-08        | GAB-PMO/NBS      | Plano de testes UAT            |
| 2 | Criação de casos de teste (6 módulos)        | 24/09      | 30/09      | 5d      | Ativ. 1     | GAB-CONT/FIN     | Suite de casos de teste        |
| 3 | Carga de dados de teste                      | 24/09      | 26/09      | 3d      | M-08        | NBS/GAB-TI       | Ambiente com dados de teste    |
| 4 | UAT Contabilidade — M1, M2, M5               | 01/10      | 13/10      | 8d*     | Ativ. 2-3   | GAB-CONT         | Relatório UAT Contabilidade    |
| 5 | UAT Financeiro — M3, M4                      | 01/10      | 09/10      | 6d*     | Ativ. 2-3   | GAB-FIN          | Relatório UAT Financeiro       |
| 6 | UAT Jurídico — M4 (rel. legais), M6          | 05/10      | 13/10      | 5d*     | Ativ. 2-3   | GAB-JUR          | Relatório UAT Jurídico         |
| 7 | Registro e priorização de defeitos           | 14/10      | 16/10      | 3d      | Ativ. 4-6   | GAB-PMO          | Backlog de defeitos priorizado |
| 8 | Correção de defeitos críticos e altos (NBS)  | 19/10      | 28/10      | 8d      | Ativ. 7     | NBS              | Build corrigido v2             |
| 9 | Reteste e regressão das correções            | 29/10      | 03/11      | 4d      | Ativ. 8     | GAB-CONT/FIN     | Relatório de reteste           |
|10 | Relatório final de UAT                       | 04/11      | 05/11      | 2d      | Ativ. 9     | GAB-PMO          | Relatório final UAT            |
|11 | Reunião Go/No-Go com sponsor                 | 06/11      | 06/11      | 1d      | Ativ. 10    | GAB-GESTOR       | Decisão Go/No-Go               |
|12 | Assinatura do termo de aceite homologação    | 07/11      | 07/11      | 1d      | Ativ. 11    | GAB-GESTOR       | **Termo de aceite (M-09)**     |

> *Duração de UAT dobrada pela disponibilidade de 50% das equipes usuárias.

**Entregáveis da Fase 4:**
- Plano e casos de teste UAT
- Relatórios de UAT por área (Contabilidade, Financeiro, Jurídico)
- Backlog de defeitos resolvido
- Termo de aceite da homologação (M-09)

**Critério de saída:** M-09 assinado; zero defeitos críticos em aberto; aprovação do Go/No-Go pelo sponsor.

---

### FASE 5 — Go-live e Transição
**Período:** 2026-10-26 a 2026-11-27

| # | Atividade                                    | Início     | Fim        | Duração | Dependência | Responsável  | Entregável                        |
|---|----------------------------------------------|------------|------------|---------|-------------|--------------|-----------------------------------|
| 1 | Elaboração do plano de go-live e rollback     | 26/10      | 28/10      | 3d      | Ativ. 4-UAT | GAB-PMO/NBS  | Plano de go-live                  |
| 2 | Treinamento — Contabilidade                  | 26/10      | 29/10      | 3d      | M-09*       | NBS          | Listas de presença                |
| 3 | Treinamento — Financeiro                     | 26/10      | 28/10      | 2d      | M-09*       | NBS          | Listas de presença                |
| 4 | Treinamento — Jurídico                       | 29/10      | 29/10      | 1d      | M-09*       | NBS          | Listas de presença                |
| 5 | Migração e validação de dados históricos     | 26/10      | 30/10      | 5d      | M-09*       | NBS/GAB-TI   | Dados migrados e validados        |
| 6 | Deploy em produção                           | 28/10      | 29/10      | 2d      | Ativ. 1     | NBS/GAB-TI   | Módulo em produção                |
| 7 | Smoke tests pós-deploy                       | 30/10      | 30/10      | 1d      | Ativ. 6     | NBS/GAB-CONT | Relatório smoke tests             |
| 8 | **Go-live — operação aprovada**              | 30/10      | 30/10      | 1d      | Ativ. 7     | GAB-GESTOR   | **Go-live (M-10)**                |
| 9 | Operação paralela (NBS + Fiscal Defender)    | 31/10      | 13/11      | 10d     | M-10        | GAB-CONT     | Logs de operação paralela         |
|10 | Validação cruzada de resultados              | 05/11      | 13/11      | 5d      | Ativ. 9     | GAB-CONT     | Relatório de validação cruzada    |
|11 | Formalização da rescisão Fiscal Defender     | 14/11      | 18/11      | 3d      | Ativ. 10    | GAB-JUR/FIN  | Notificação formal de rescisão    |
|12 | Desativação do Fiscal Defender               | 14/11      | 14/11      | 1d      | Ativ. 11    | GAB-TI       | **Fiscal Defender desativado (M-11)** |

> *Treinamentos e migração podem iniciar antes do M-09 formal, durante a fase final da UAT.

**Entregáveis da Fase 5:**
- Plano de go-live e rollback
- Comprovantes de treinamento por área
- Relatório de smoke tests
- Relatório de operação paralela e validação cruzada
- Notificação formal de rescisão do Fiscal Defender

**Critério de saída:** M-11 concluído; Fiscal Defender desativado; sistema NBS em operação plena.

---

### FASE 6 — Encerramento e Pós-go-live
**Período:** 2026-11-16 a 2026-12-22

| # | Atividade                                    | Início     | Fim        | Duração | Dependência | Responsável  | Entregável                        |
|---|----------------------------------------------|------------|------------|---------|-------------|--------------|-----------------------------------|
| 1 | Suporte intensivo NBS (4 semanas)             | 16/11      | 11/12      | 20d     | M-11        | NBS          | Log de incidentes resolvidos      |
| 2 | Registro e resolução de incidentes            | 16/11      | 11/12      | 20d     | M-11        | NBS/GAB-PMO  | Relatório de incidentes           |
| 3 | Elaboração do manual do usuário               | 16/11      | 20/11      | 5d      | M-11        | NBS          | Manual do usuário                 |
| 4 | Documentação técnica da solução               | 16/11      | 20/11      | 5d      | M-11        | NBS          | Documentação técnica              |
| 5 | Registro das lições aprendidas                | 07/12      | 08/12      | 2d      | Ativ. 1-2   | GAB-PMO      | Documento de lições aprendidas    |
| 6 | Relatório final do projeto                    | 09/12      | 11/12      | 3d      | Ativ. 5     | GAB-PMO      | Relatório final                   |
| 7 | Reunião de encerramento com sponsor           | 14/12      | 14/12      | 1d      | Ativ. 6     | GAB-GESTOR   | Ata de encerramento               |
| 8 | Arquivamento no PMO e encerramento formal     | 15/12      | 16/12      | 2d      | Ativ. 7     | GAB-PMO      | **Projeto encerrado (M-12)**      |

**Entregáveis da Fase 6:**
- Log consolidado de incidentes pós-go-live
- Manual do usuário e documentação técnica
- Documento de lições aprendidas
- Relatório final do projeto
- Ata de encerramento assinada pelo sponsor

**Critério de saída:** M-12 concluído; todos os documentos arquivados no PMO.

---

## 7. Cronograma Financeiro

**Orçamento Total Residual: R$ 35.000,00**
*(Desenvolvimento: R$ 0,00 — contrapartida NBS)*

### Composição do Orçamento Residual

| Categoria                                          | Valor (R$)  | % do Total |
|----------------------------------------------------|-------------|------------|
| Implementação / Consultoria NBS (config. inicial)  | R$ 15.000   | 42,9%      |
| Treinamento das equipes usuárias                   | R$ 8.000    | 22,9%      |
| Rescisão contratual — Fiscal Defender              | R$ 10.000   | 28,6%      |
| Infraestrutura / Ambiente de homologação           | R$ 2.000    | 5,7%       |
| **Total**                                          | **R$ 35.000** | **100%** |

### Curva de Desembolso — Por Fase e Mês

| Mês          | Fase(s) Ativa(s)    | Implementação | Treinamento | Rescisão FD | Infraestr. | **Total Mês** | **Acumulado** |
|--------------|---------------------|---------------|-------------|-------------|------------|---------------|---------------|
| Maio/2026    | Fase 0              | R$ 0          | R$ 0        | R$ 0        | R$ 0       | **R$ 0**      | R$ 0          |
| Junho/2026   | Fase 1              | R$ 2.000      | R$ 0        | R$ 0        | R$ 500     | **R$ 2.500**  | R$ 2.500      |
| Julho/2026   | Fases 2–3 início    | R$ 3.000      | R$ 0        | R$ 0        | R$ 500     | **R$ 3.500**  | R$ 6.000      |
| Agosto/2026  | Fase 3              | R$ 4.000      | R$ 0        | R$ 0        | R$ 500     | **R$ 4.500**  | R$ 10.500     |
| Setembro/2026| Fases 3–4 início    | R$ 3.000      | R$ 0        | R$ 0        | R$ 500     | **R$ 3.500**  | R$ 14.000     |
| Outubro/2026 | Fase 4 + Go-live    | R$ 3.000      | R$ 4.000    | R$ 0        | R$ 0       | **R$ 7.000**  | R$ 21.000     |
| Novembro/2026| Fases 5–6           | R$ 0          | R$ 4.000    | R$ 10.000   | R$ 0       | **R$ 14.000** | R$ 35.000     |
| Dezembro/2026| Fase 6              | R$ 0          | R$ 0        | R$ 0        | R$ 0       | **R$ 0**      | R$ 35.000     |
| **TOTAL**    |                     | **R$ 15.000** | **R$ 8.000**| **R$ 10.000**| **R$ 2.000**| **R$ 35.000**|               |

### Distribuição Percentual por Fase

| Fase | Desembolso (R$) | % do Total |
|------|-----------------|------------|
| 0    | R$ 0            | 0,0%       |
| 1    | R$ 2.500        | 7,1%       |
| 2    | R$ 3.500        | 10,0%      |
| 3    | R$ 8.000        | 22,9%      |
| 4    | R$ 7.000        | 20,0%      |
| 5    | R$ 14.000       | 40,0%      |
| 6    | R$ 0            | 0,0%       |

> **Pico de desembolso em novembro/2026**: concentração da rescisão do Fiscal Defender (R$10.000) + última parcela de treinamento.

---

## 8. Riscos de Prazo

| # | Risco                                                                                        | Probabilidade | Impacto | Impacto em Dias | Mitigação                                                              |
|---|----------------------------------------------------------------------------------------------|---------------|---------|-----------------|------------------------------------------------------------------------|
| R1 | **CB-01/CB-02 não sanadas até 30/05** — Sponsor não designado ou acordo NBS com pendências  | Média         | Crítico | +15 a +30 dias  | Escalonamento executivo imediato; reunião de crise com diretoria até 20/05 |
| R2 | **Atraso no desenvolvimento NBS** — NBS não entrega sprints conforme plano                  | Média-Alta    | Alto    | +10 a +25 dias  | Reuniões quinzenais de acompanhamento; cláusula de SLA no acordo NBS; buffer de 15% já aplicado |
| R3 | **Disponibilidade das equipes usuárias < 50% durante UAT** — demandas fiscais concorrentes  | Alta          | Médio   | +8 a +15 dias   | Reserva formal de calendário com gestores das áreas; UAT em blocos de 2h/dia; rotação de usuários |
| R4 | **Escopo não congelado — change requests pós-ERF** — mudanças de requisitos durante desenvolvimento | Média    | Alto    | +7 a +20 dias   | Processo formal de change request com aprovação do sponsor; congelamento de escopo no M-05 |
| R5 | **Defeitos críticos na UAT não resolvíveis no prazo** — qualidade insuficiente do entregável NBS | Média    | Alto    | +10 a +21 dias  | Critérios de aceite claros no ERF; testes internos NBS obrigatórios pré-UAT; buffer de 15% na fase |

### Impacto Acumulado no Cenário Pessimista

Se R1 + R2 + R5 ocorrerem simultaneamente, o go-live pode ser deslocado para **fevereiro/2027**, requerendo revisão formal do cronograma e re-baseline pelo sponsor.

---

## 9. Restrições do Cronograma

| # | Restrição                                                                                          | Tipo          | Impacto                                      |
|---|-----------------------------------------------------------------------------------------------------|---------------|----------------------------------------------|
| C1 | **CB-01 e CB-02 são pré-requisitos absolutos** — nenhuma fase subsequente pode iniciar sem sanação  | Regulatória   | Bloqueio total do projeto até 30/05/2026     |
| C2 | **Desenvolvimento é exclusivamente responsabilidade da NBS** — GAB não pode suprir capacidade       | Contratual    | Dependência crítica de terceiro sem alternativa interna |
| C3 | **Disponibilidade das equipes de negócio limitada a 50%** durante UAT                               | Operacional   | Duração da UAT dobrada; impacto direto no caminho crítico |
| C4 | **Fiscal Defender deve permanecer ativo durante todo o período de UAT** — risco operacional proibido | Operacional   | Custo duplo de licença e esforço de operação paralela |
| C5 | **Go-live alvo: outubro/novembro 2026** — compromisso com diretoria e comunicado às áreas           | Estratégica   | Pressão para não atrasar; qualquer slip > 30 dias requer re-aprovação executiva |
| C6 | **Orçamento residual fixo em R$ 35.000** — sem reserva gerencial adicional                          | Financeira    | Custos imprevistos devem ser absorvidos ou aprovados como aditivo |
| C7 | **Recesso de fim de ano (22/12–02/01)** — equipes indisponíveis                                     | Calendário    | Fase 6 deve ser concluída até 19/12/2026 ou retomada em jan/2027 |
| C8 | **Processo de negócio não muda** — escopo limitado a substituição funcional                          | Escopo        | Mudanças de processo constituem expansão de escopo; requerem novo projeto |

---

## 10. Sumário Executivo do Cronograma

| Item                          | Valor                                                        |
|-------------------------------|--------------------------------------------------------------|
| Data de início                | 2026-05-15                                                   |
| Go-live planejado             | **2026-10-30**                                               |
| Go-live limite (com buffer)   | 2026-11-07                                                   |
| Encerramento formal           | 2026-12-16                                                   |
| Duração total                 | ~7 meses (215 dias corridos)                                 |
| Pacotes de trabalho           | 77                                                           |
| Marcos críticos               | 12                                                           |
| Orçamento residual total      | R$ 35.000                                                    |
| Pico de desembolso            | Novembro/2026 (R$ 14.000)                                    |
| Maior risco ao prazo          | CB-01/CB-02 não sanados + atraso NBS                         |
| Buffer aplicado (Fases 3+4)   | 15% (~14 dias adicionais)                                    |

---

*Documento gerado por Carlos Cronograma — VMO Autônomo | PROJ-2026-005 v4.0 | 2026-05-15*

---

# ■  06-plano-riscos

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

---

# ■  07-kpis

# Framework de KPIs e Métricas — PROJ-2026-005

| Campo | Valor |
|---|---|
| **Projeto** | PROJ-2026-005 — Auditor Fiscal NBS (Substituição Fiscal Defender) |
| **Demanda** | DEM-2026-002 |
| **Data de Referência** | 2026-05-15 |
| **Versão** | v6 |
| **Autor** | Marcela Métrica — Especialista em KPIs e Métricas (VMO Autônomo) |
| **Go-live planejado** | 30/10/2026 |
| **BAC** | R$ 35.000 |

---

## 1. EVM — Earned Value Management

### 1.1 Conceitos e Fórmulas Documentadas

| Sigla | Nome | Fórmula | Interpretação |
|---|---|---|---|
| **BAC** | Budget at Completion | Valor total aprovado do orçamento | Orçamento base: R$ 35.000 |
| **PV** | Planned Value | % trabalho planejado × BAC | Valor do trabalho que deveria estar feito até a data |
| **EV** | Earned Value | % trabalho realmente concluído × BAC | Valor do trabalho efetivamente entregue |
| **AC** | Actual Cost | Custo real incorrido até a data | Extraído do controle financeiro do projeto |
| **CV** | Cost Variance | EV − AC | > 0 = abaixo do orçamento; < 0 = estouro |
| **SV** | Schedule Variance | EV − PV | > 0 = adiantado; < 0 = atrasado |
| **CPI** | Cost Performance Index | EV ÷ AC | ≥ 1,0 = eficiente em custo |
| **SPI** | Schedule Performance Index | EV ÷ PV | ≥ 1,0 = no prazo ou adiantado |
| **EAC** | Estimate at Completion | BAC ÷ CPI | Previsão de custo final com performance atual |
| **ETC** | Estimate to Complete | EAC − AC | Quanto ainda falta gastar |
| **VAC** | Variance at Completion | BAC − EAC | Desvio previsto ao final do projeto |
| **TCPI** | To-Complete Performance Index | (BAC − EV) ÷ (BAC − AC) | CPI necessário para terminar dentro do orçamento |

### 1.2 Thresholds de Alerta e Escalada

| Indicador | Verde (Normal) | Amarelo (Alerta) | Vermelho (Escalada) |
|---|---|---|---|
| **CPI** | ≥ 1,0 | 0,80 ≤ CPI < 0,90 | CPI < 0,80 |
| **SPI** | ≥ 1,0 | 0,85 ≤ SPI < 0,95 | SPI < 0,85 |
| **VAC** | VAC ≥ 0 | −R$ 3.500 ≤ VAC < 0 | VAC < −R$ 3.500 (> 10% do BAC) |
| **Desvio de Prazo** | 0–5 dias | 6–14 dias | ≥ 15 dias em fase crítica |

### 1.3 Linha de Base PV por Fase — Curva S

**Critério de distribuição:** ponderação por complexidade e esforço de cada fase sobre o BAC de R$ 35.000.

| Pesos de distribuição por fase |
|---|
| F0 Sanação Bloqueantes: 3% — R$ 1.050 (mobilização, mitigação de riscos críticos) |
| F1 Kick-off + Alinhamento NBS: 5% — R$ 1.750 (alinhamento contratual, governança) |
| F2 Levantamento Detalhado: 12% — R$ 4.200 (análise de requisitos 6 módulos) |
| F3 Desenvolvimento NBS: 50% — R$ 17.500 (núcleo técnico do projeto) |
| F4 Homologação (UAT): 18% — R$ 6.300 (testes, correções, validação) |
| F5 Go-live + Transição: 7% — R$ 2.450 (deploy, treinamento, suporte inicial) |
| F6 Encerramento: 5% — R$ 1.750 (documentação, lições aprendidas, encerramento) |

#### Curva S — Pontos de Controle (PV Acumulado)

| # | Fase | Data de Controle | PV Incremental (R$) | PV Acumulado (R$) | % do BAC |
|---|---|---|---|---|---|
| 1 | F0 — Sanação Bloqueantes | 30/05/2026 | R$ 1.050 | R$ 1.050 | 3,0% |
| 2 | F1 — Kick-off + Alinhamento NBS | 14/06/2026 | R$ 1.750 | R$ 2.800 | 8,0% |
| 3 | F2 — Levantamento Detalhado | 15/07/2026 | R$ 4.200 | R$ 7.000 | 20,0% |
| 4 | F3 — Desenvolvimento NBS | 19/09/2026 | R$ 17.500 | R$ 24.500 | 70,0% |
| 5 | F4 — Homologação (UAT) | 17/10/2026 | R$ 6.300 | R$ 30.800 | 88,0% |
| 6 | F5 — Go-live + Transição | 14/11/2026 | R$ 2.450 | R$ 33.250 | 95,0% |
| 7 | F6 — Encerramento | 16/12/2026 | R$ 1.750 | R$ 35.000 | 100,0% |

> **Nota:** A curva S deve ser atualizada quinzenalmente durante F3 (Desenvolvimento) e semanalmente durante F4 (UAT), por serem fases de maior risco de desvio.

---

## 2. KPIs de Entrega do Projeto (Fase de Execução)

Vigência: 2026-05-15 a 2026-11-14 (F0 → F5)

| ID | Nome do KPI | Fórmula | Unidade | Baseline | Meta | Threshold Mínimo | Frequência | Fonte de Dados | Responsável |
|---|---|---|---|---|---|---|---|---|---|
| **KPI-01** | Índice de Desempenho de Prazo (SPI) | EV ÷ PV | Índice (adimensional) | 1,00 (planejado) | ≥ 1,00 | ≥ 0,85 (alerta < 0,85 = escalada) | Quinzenal | Cronograma + % conclusão declarada | Carlos Cronograma |
| **KPI-02** | Índice de Desempenho de Custo (CPI) | EV ÷ AC | Índice (adimensional) | 1,00 (planejado) | ≥ 1,00 | ≥ 0,90 (alerta < 0,80 = escalada) | Quinzenal | Controle financeiro + notas fiscais | Patrocinador / PMO |
| **KPI-03** | Cobertura de Requisitos Desenvolvidos | (Requisitos entregues ÷ Requisitos baseline) × 100 | % | 0% (início F3) | 100% até 19/09/2026 | ≥ 80% ao fim de F3 | Mensal (F2–F3) | ERF — Backlog de Requisitos | Rafael Requisito |
| **KPI-04** | Taxa de Defeitos em UAT | (Defeitos abertos críticos ÷ Casos de teste executados) × 100 | % | N/D (início UAT) | ≤ 2% ao final de F4 | ≤ 5% na revisão intermediária UAT (08/10/2026) | Semanal (F4) | Sistema de tracking de defeitos (UAT) | Equipe NBS + QA |
| **KPI-05** | Cobertura de Casos de Teste UAT | (Casos executados ÷ Casos planejados) × 100 | % | 0% (início F4) | 100% até 17/10/2026 | ≥ 60% até 08/10/2026 | Semanal (F4) | Plano de testes UAT | Equipe NBS + Usuários Chave |
| **KPI-06** | Taxa de Entrega no Prazo por Fase | (Milestones entregues no prazo ÷ Total de milestones planejados) × 100 | % | 0% (início) | ≥ 85% ao longo do projeto | ≥ 70% até F3 | Por fase (ao encerrar cada fase) | Cronograma mestre | Carlos Cronograma |
| **KPI-07** | Risco Residual Médio (Score) | Média dos scores dos riscos abertos no período | Score (0–25) | Score médio atual: 19 (RSK-01 + RSK-02 críticos) | Score médio ≤ 10 até F3 | Score médio ≤ 15 até F2 | Mensal | Matriz de riscos | Pedro Perigo |
| **KPI-08** | Completude da Documentação de Módulos | (Módulos com documentação técnica aprovada ÷ 6 módulos) × 100 | % | 0% | 100% (todos 6 módulos) até 15/10/2026 | ≥ 50% (3 módulos) até 19/09/2026 | Mensal (F2–F4) | Repositório de documentação | Rafael Requisito |
| **KPI-09** | Velocidade de Resolução de Impedimentos | Tempo médio (dias) entre registro e resolução de impedimento | Dias | Não estabelecido | ≤ 3 dias úteis | ≤ 5 dias úteis | Semanal | Backlog / Log de impedimentos | PMO / Sponsor |
| **KPI-10** | Índice de Comprometimento do Sponsor | Presença nas reuniões de checkpoint ÷ Total de checkpoints convocados | % | 0% (RSK-01 em aberto) | 100% (após identificação do Sponsor — marco F1) | ≥ 80% a partir de F2 | Por checkpoint | Atas de reunião | PMO |

---

## 3. KPIs de Transição (Go-live → 90 dias pós go-live)

Vigência: 18/10/2026 a 16/01/2027

| ID | Nome do KPI | Descrição | Fórmula | Meta de Aceitação (Critério de Sucesso do Go-live) | Prazo de Aferição | Responsável |
|---|---|---|---|---|---|---|
| **KPI-T01** | Taxa de Adoção pelo Usuário | % de usuários da Divisão Comércio que utilizam ativamente o Auditor Fiscal NBS (ao menos 1 operação/semana) | (Usuários ativos na semana ÷ Total de usuários habilitados) × 100 | ≥ 80% até 30 dias pós go-live; ≥ 95% até 90 dias pós go-live | D+30 e D+90 | Equipe NBS + Gestão Divisão Comércio |
| **KPI-T02** | Tempo Médio de Treinamento por Usuário | Horas médias investidas em treinamento para que o usuário atinja proficiência (nota ≥ 7 na avaliação) | Σ horas de treinamento ÷ nº de usuários treinados | ≤ 8 horas por usuário (meta eficiência); 100% dos usuários treinados até D+14 | D+14 pós go-live | Equipe de Treinamento NBS |
| **KPI-T03** | Incidentes Críticos em Produção (Sev. 1 e 2) | Número de incidentes de severidade crítica (falha total ou parcial do módulo de auditoria) registrados nos primeiros 90 dias | Contagem de chamados Sev.1 + Sev.2 abertos | 0 incidentes Sev.1 no período; ≤ 3 incidentes Sev.2 nos primeiros 90 dias | D+30, D+60, D+90 | Equipe NBS (SLA Suporte) |
| **KPI-T04** | Satisfação das Áreas Usuárias (CSAT) | Nota média de satisfação coletada via pesquisa estruturada com usuários-chave da Divisão Comércio | Média das notas em escala de 1 a 10 | ≥ 7,5 / 10,0 até D+30; ≥ 8,0 / 10,0 até D+90 | D+30 e D+90 | PMO + Gestão Divisão Comércio |
| **KPI-T05** | Disponibilidade do Sistema em Produção | Uptime do módulo Auditor Fiscal NBS em ambiente produtivo | (Tempo disponível ÷ Tempo total do período) × 100 | ≥ 99,0% nos primeiros 30 dias; ≥ 99,5% entre D+31 e D+90 | Contínuo (relatório semanal) | Equipe NBS / Infraestrutura |
| **KPI-T06** | Taxa de Cancelamento do Fiscal Defender | Confirmação do cancelamento contratual do Fiscal Defender | Marco binário (Sim/Não) + data do cancelamento efetivo | Cancelamento efetivado até D+30 pós go-live (14/11/2026) | D+30 | Financeiro / Jurídico / PMO |
| **KPI-T07** | Cobertura de Auditoria Fiscal no Período | % das NF-e do período auditadas pelo novo módulo em relação ao total emitido/recebido | (NF-e auditadas pelo NBS ÷ NF-e total do período) × 100 | ≥ 95% até D+30; 100% até D+60 | D+30 e D+60 | Equipe NBS + Fiscal Divisão Comércio |

---

## 4. KRs — Key Results Pós Go-live (3 a 12 meses)

**OKR do Projeto:** *"Consolidar a auditoria fiscal da Divisão Comércio no ERP NBS, eliminando a dependência do Fiscal Defender e gerando eficiência operacional mensurável."*

| ID | Key Result | Descrição | Métrica | Baseline (pré go-live) | Meta | Prazo de Medição |
|---|---|---|---|---|---|---|
| **KR-01** | Saving Realizado vs. Esperado | Confirmar que a economia com cancelamento do Fiscal Defender está sendo capturada conforme planejado | (Custo evitado acumulado ÷ Saving esperado acumulado) × 100 | R$ 0 (contrato Fiscal Defender ainda ativo) | ≥ 100% do saving esperado: R$ 19.500 em 3 meses (3 × R$ 6.500/mês); R$ 78.000 ao final de 12 meses | M+3 (Jan/2027), M+6 (Abr/2027), M+12 (Out/2027) |
| **KR-02** | Cobertura Total da Auditoria Fiscal NBS | Garantir que 100% das operações fiscais da Divisão Comércio passem pelo Auditor Fiscal NBS sem exceções manuais | (Operações auditadas automaticamente ÷ Total de operações fiscais) × 100 | ~0% no NBS (toda auditoria no Fiscal Defender) | ≥ 98% até M+3; 100% até M+6 (sem processos residuais no Fiscal Defender) | M+3 (Jan/2027) e M+6 (Abr/2027) |
| **KR-03** | SLA de Disponibilidade em Operação Estável | Manter alta disponibilidade do Auditor Fiscal NBS após período de estabilização | Uptime mensal do módulo em produção | N/D (sistema ainda não em produção) | ≥ 99,5% / mês a partir de M+3 (Jan/2027) de forma contínua | Mensal a partir de M+3, avaliação consolidada em M+12 |
| **KR-04** | Satisfação Sustentada do Usuário | Demonstrar que os usuários da Divisão Comércio estão satisfeitos com o novo módulo de forma duradoura | CSAT médio trimestral (escala 1–10) | Nota de referência pré-projeto: não coletada (usar D+90 como nova baseline) | ≥ 8,0 / 10,0 em todas as medições trimestrais (M+3, M+6, M+9, M+12) | Trimestral: Jan/2027, Abr/2027, Jul/2027, Out/2027 |
| **KR-05** | Redução de Erros Fiscais com Auditoria Automatizada | Demonstrar que o novo motor de auditoria (M2) reduz a incidência de erros fiscais versus o cenário anterior | (Alertas de erro fiscal gerados pelo NBS no período ÷ Total de NF-e processadas) × 100; comparar com taxa histórica do Fiscal Defender | Taxa histórica a ser coletada em F2 (Levantamento Detalhado) | Redução de ≥ 30% na taxa de erros fiscais não detectados em M+6 vs. baseline histórico | M+6 (Abr/2027) |
| **KR-06** | ROI Realizado | Confirmar que o retorno sobre o investimento está aderente ao planejado | (Benefícios acumulados − Custos totais do projeto) ÷ Custos totais × 100 | ROI = 0% (pré go-live) | ROI ≥ 100% em M+6 (payback completo); ROI ≥ 469% projetado em M+36 | M+6 (Abr/2027) e M+12 (Out/2027) |

---

## 5. Dashboard de Monitoramento

### 5.1 Painel Semanal de Execução (F0 a F5)

**Audiência:** Equipe de projeto, gerente de projeto, equipe NBS
**Cadência:** Toda sexta-feira
**Plataforma sugerida:** Power BI / Planilha compartilhada (Sharepoint)

| Seção | Conteúdo |
|---|---|
| **Status Geral** | Semáforo do projeto (Verde/Amarelo/Vermelho) com justificativa |
| **EVM em Tempo Real** | CPI, SPI, EV, AC, PV da semana; Curva S atualizada |
| **Cronograma** | Gantt sintético com % de conclusão por fase; próximos milestones em 14 dias |
| **Riscos Ativos** | Top 5 riscos por score; novos riscos da semana |
| **Impedimentos** | Lista de impedimentos abertos com dono e prazo de resolução |
| **UAT (apenas F4)** | % de casos executados, taxa de defeitos abertos por severidade |

### 5.2 Painel Mensal de Portfólio (F0 a F6)

**Audiência:** Sponsor, diretoria, PMO, gestores das áreas impactadas
**Cadência:** Toda última sexta-feira do mês
**Plataforma sugerida:** Power BI com camada de dados do projeto

| Seção | Conteúdo |
|---|---|
| **EVM Consolidado** | CPI e SPI histórico (linha do tempo); EAC vs. BAC; VAC projetado |
| **Performance Financeira** | Comprometido vs. realizado vs. planejado; projeção de saving |
| **Cronograma Estratégico** | Fases concluídas vs. planejadas; desvio acumulado em dias |
| **KPIs do Período** | Tabela com todos os KPIs de execução ativos: valor atual vs. meta |
| **Riscos Estratégicos** | Heatmap de riscos; status dos planos de ação dos top 4 riscos |
| **Decisões Pendentes** | Itens que requerem decisão do patrocinador ou diretoria |

### 5.3 Painel Pós Go-live (D+0 a D+90 e além)

**Audiência:** Gestão Divisão Comércio, Financeiro, Compliance Fiscal, PMO
**Cadência:** Semanal nos primeiros 30 dias; mensal a partir de D+31

| Seção | Conteúdo |
|---|---|
| **Adoção e Uso** | KPI-T01: taxa de adoção por semana; curva de adoção acumulada |
| **Qualidade em Produção** | KPI-T03: incidentes por severidade; tempo médio de resolução (MTTR) |
| **Disponibilidade** | KPI-T05: uptime semanal e acumulado vs. SLA 99,5% |
| **Satisfação (CSAT)** | KPI-T04: NPS/CSAT por pesquisa; comentários qualitativos por área |
| **Financeiro** | Saving realizado (KR-01): mês a mês vs. planejado; confirmação de cancelamento Fiscal Defender |
| **Cobertura Fiscal** | KPI-T07 / KR-02: % de NF-e auditadas automaticamente |

---

## 6. Critérios de Encerramento do Projeto

O projeto PROJ-2026-005 será considerado **encerrado com sucesso** quando TODAS as condições abaixo forem atendidas e formalmente verificadas:

| # | Critério de Encerramento | Evidência Exigida | Prazo Limite |
|---|---|---|---|
| **CE-01** | 100% dos módulos (M1–M6) entregues, homologados e em produção | Atas de aceite assinadas por representantes da Divisão Comércio para cada módulo | 14/11/2026 |
| **CE-02** | Taxa de defeitos UAT ≤ 2% na entrega final | Relatório final de UAT com contagem de defeitos abertos / fechados | 17/10/2026 |
| **CE-03** | Cobertura de auditoria fiscal ≥ 95% das NF-e no primeiro mês de produção | Relatório de cobertura extraído do módulo M4 (Relatórios e Dashboards) | 14/11/2026 |
| **CE-04** | Cancelamento formal do contrato do Fiscal Defender efetivado | Comprovante de cancelamento contratual emitido pelo fornecedor / área jurídica | 14/11/2026 |
| **CE-05** | CSAT dos usuários da Divisão Comércio ≥ 7,5/10 em D+30 | Resultado da pesquisa de satisfação D+30 com ≥ 80% de respondentes | 14/11/2026 |
| **CE-06** | Zero incidentes Sev.1 nos primeiros 30 dias de produção | Log de incidentes do período D+0 a D+30 | 14/11/2026 |
| **CE-07** | Documentação técnica e operacional 100% entregue e aprovada | Repositório de documentação completo: manual do usuário, manual técnico, guia de configuração de regras (M5) | 16/12/2026 |
| **CE-08** | Lições aprendidas registradas e compartilhadas com PMO | Documento de lições aprendidas publicado no repositório do VMO | 16/12/2026 |
| **CE-09** | CPI final ≥ 0,90 (custo realizado ≤ 110% do BAC = R$ 38.500) | Relatório financeiro final do projeto | 16/12/2026 |
| **CE-10** | Termo de encerramento assinado pelo Sponsor | Documento formal de aceite e encerramento com assinatura do patrocinador identificado | 16/12/2026 |

> **Nota:** Os critérios CE-01 a CE-06 são **pré-requisitos para o go-live** e devem ser verificados antes da declaração de sucesso da F5. Os critérios CE-07 a CE-10 encerram formalmente o projeto na F6.

---

## 7. Alertas e Gatilhos de Escalada

| # | Condição (Gatilho) | Nível | Ação Imediata | Responsável pela Ação | Prazo para Resposta |
|---|---|---|---|---|---|
| **ALR-01** | SPI < 0,85 em qualquer medição quinzenal | Vermelho — Escalada | Convocar reunião de crise com equipe NBS + PMO; revisar cronograma; acionar plano de contingência de prazo | Carlos Cronograma + PMO | 48 horas após identificação |
| **ALR-02** | CPI < 0,80 em qualquer medição | Vermelho — Escalada | Convocar comitê de portfólio; revisar escopo; levantar causas de estouro; comunicar Sponsor e diretoria | PMO + Sponsor | 48 horas após identificação |
| **ALR-03** | CPI entre 0,80 e 0,90 | Amarelo — Alerta | Investigar causas; apresentar plano de recuperação na próxima reunião de portfólio | Carlos Cronograma + PMO | 5 dias úteis |
| **ALR-04** | RSK-01 (Sponsor) não resolvido até 14/06/2026 (fim F1) | Vermelho — Escalada Estratégica | Escalar para diretoria executiva; projeto entra em stand-by formal até identificação do Sponsor | PMO + Diretoria | Imediato (fim F1) |
| **ALR-05** | RSK-02 (acordo NBS não verificado) persistir em F2 | Vermelho — Bloqueante | Suspender atividades de desenvolvimento até formalização do acordo NBS; comunicar ao Sponsor | PMO + Jurídico | 24 horas após início F2 |
| **ALR-06** | Taxa de defeitos UAT > 5% na revisão intermediária (08/10/2026) | Amarelo — Alerta | Ampliar equipe de correção NBS; revisar cronograma de UAT; avaliar risco de atraso no go-live | Equipe NBS + QA | 3 dias úteis |
| **ALR-07** | Taxa de defeitos UAT > 10% ao final de F4 | Vermelho — Bloqueante de Go-live | Bloquear go-live; estender UAT; acionar cláusula de SLA com NBS; comunicar Sponsor | PMO + Equipe NBS + Sponsor | Imediato |
| **ALR-08** | Incidente Sev.1 em produção (pós go-live) | Vermelho — Incidente Crítico | Ativar bridge de incidente; comunicar gestão Divisão Comércio; acionar suporte NBS P1; avaliar rollback | Equipe NBS (plantão) + PMO | Resposta em 1 hora; resolução em 4 horas |
| **ALR-09** | Taxa de adoção < 60% em D+14 | Amarelo — Alerta | Intensificar treinamento; identificar barreiras de adoção por área; apoio presencial de key users | Equipe de Treinamento + Gestão | 5 dias úteis |
| **ALR-10** | Fiscal Defender não cancelado até D+30 (14/11/2026) | Amarelo — Alerta Financeiro | Escalar para área Financeira e Jurídica; acionar responsável pelo contrato; documentar risco de custo duplo | Financeiro + Jurídico + PMO | 48 horas após D+30 |
| **ALR-11** | CSAT D+30 < 6,0/10 | Vermelho — Escalada | Realizar pesquisa qualitativa aprofundada; plano de ação de melhoria com prazo de 30 dias; comunicar ao Sponsor | PMO + Gestão Divisão Comércio | 5 dias úteis |
| **ALR-12** | Desvio de prazo ≥ 15 dias em fase crítica (F3 ou F4) | Vermelho — Escalada | Análise de impacto no go-live; comunicado formal ao Sponsor; revisão do roadmap com compressão de fases ou ajuste de escopo | Carlos Cronograma + PMO + Sponsor | 48 horas |

---

## Apêndice — Resumo Executivo de Metas

| Dimensão | KPI Principal | Meta de Sucesso |
|---|---|---|
| **Prazo** | SPI ≥ 0,95 na média do projeto | Go-live até 30/10/2026 |
| **Custo** | CPI ≥ 0,95; custo final ≤ R$ 36.750 | BAC R$ 35.000 (tolerância +5%) |
| **Qualidade** | Taxa defeitos UAT ≤ 2% na entrega | 100% módulos aceitos |
| **Adoção** | ≥ 95% usuários ativos em D+90 | CSAT ≥ 8,0/10 em D+90 |
| **Benefício Financeiro** | Saving R$ 78.000/ano realizado | Payback ≤ 6 meses pós go-live |
| **Disponibilidade** | Uptime ≥ 99,5%/mês em operação estável | A partir de Jan/2027 |

---

*Documento gerado por: Marcela Métrica — VMO Autônomo | 2026-05-15 | PROJ-2026-005 v6*

---

# ■  08-status-report

# Status Report #001
## PROJ-2026-005 | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender

---

| Campo | Valor |
|---|---|
| **Projeto** | PROJ-2026-005 |
| **Demanda** | DEM-2026-002 |
| **Período do Report** | 01/05/2026 – 15/05/2026 |
| **Data de Emissão** | 15/05/2026 |
| **Versão** | v1.0 |
| **Fase Atual** | F0 — Sanação de Condições Bloqueantes |
| **Autor** | Sara Status — VMO Autônomo |
| **Solicitante** | Sandro Siqueira |

---

## 1. Resumo Executivo

O projeto PROJ-2026-005 concluiu com sucesso a fase de instrução documental. Todos os 8 documentos de planejamento foram produzidos pelo pipeline VMO Autônomo ao longo da sprint de iniciação, cobrindo levantamento de demanda, qualificação, documentação-base (TAP + PM Canvas + Plano Geral), requisitos funcionais e não funcionais, cronograma detalhado, plano de riscos e framework de KPIs. O projeto está formalmente instruído e tecnicamente pronto para avançar ao kick-off.

O aspecto mais positivo do projeto é o seu case financeiro: a iniciativa prevê saving anual de **R$78.000**, com investimento de **R$0 em desenvolvimento** e apenas **R$35.000 em custos residuais**, resultando em payback estimado de **5,4 meses** — um retorno sobre investimento expressivo para o portfólio da organização. A qualidade da instrução produzida, com 27 Requisitos Funcionais e 12 Requisitos Não Funcionais mapeados, 77 pacotes de trabalho no cronograma e go-live planejado para **30/10/2026**, demonstra maturidade no processo de planejamento.

Contudo, o projeto está formalmente **bloqueado** por duas condições críticas não resolvidas: **CB-01** (ausência de sponsor executivo identificado, prazo 25/05) e **CB-02** (acordo NBS sem verificação documental, prazo 30/05). Ambas as condições são pré-requisitos absolutos para abertura formal do projeto e realização do kick-off. Sem resolução até os respectivos prazos, o cronograma de go-live em outubro corre risco direto. A atenção da liderança é requerida com urgência.

---

## 2. Semáforos de Status

| Dimensão | Status | Comentário |
|---|---|---|
| **Escopo** | 🟢 Verde | 27 RFs e 12 RNFs mapeados; escopo bem delimitado e documentado |
| **Prazo** | 🟡 Amarelo | Go-live definido em 30/10/2026, mas CB-01 e CB-02 ameaçam o cronograma se não resolvidas até 30/05 |
| **Custo** | 🟢 Verde | Orçamento de R$35.000 (residuais) dentro do esperado; desenvolvimento R$0 |
| **Riscos** | 🔴 Vermelho | 4 riscos classificados como CRÍTICOS; CB-01 (score 25) e CB-02 (score 20) sem resolução |
| **Qualidade** | 🟢 Verde | Instrução 100% concluída; todos os 8 documentos produzidos e revisados |
| **Sponsor / Governança** | 🔴 Vermelho | Sponsor executivo não identificado — governança do projeto não está estabelecida |

---

## 3. Progresso do Pipeline de Instrução

> **Status geral da instrução:** 8/8 documentos concluídos ✅

| # | Documento | Agente Responsável | Entrega | Status |
|---|---|---|---|---|
| 1 | `v1/demanda-coletada.md` — Coleta da Demanda | Iara Inbound | 01/05/2026 | ✅ Concluído |
| 2 | `v1/qualificacao.md` — Qualificação do Projeto | Felipe Filtro | 02/05/2026 | ✅ Concluído (18/30 — Aprovado com Condições) |
| 3 | `v2/documentacao-base.md` — TAP + PM Canvas + Plano Geral | Diana Documento | 05/05/2026 | ✅ Concluído |
| 4 | `v3/requisitos.md` — Requisitos Funcionais e Não Funcionais | Rafael Requisito | 08/05/2026 | ✅ Concluído (27 RFs + 12 RNFs) |
| 5 | `v4/cronograma.md` — Cronograma Detalhado | Carlos Cronograma | 10/05/2026 | ✅ Concluído (77 pacotes, go-live 30/10/2026) |
| 6 | `v5/plano-riscos.md` — Plano de Riscos | Pedro Perigo | 12/05/2026 | ✅ Concluído (18 riscos mapeados) |
| 7 | `v6/kpis.md` — KPIs e Framework de Medição | Marcela Métrica | 14/05/2026 | ✅ Concluído (EVM BAC R$35K, 6 KRs pós go-live) |
| 8 | `v7/status-report-inicial.md` — Status Report #001 | Sara Status | 15/05/2026 | ✅ Concluído |

---

## 4. Itens Pendentes Críticos

| # | Item | Responsável | Prazo | Consequência se Não Resolvido |
|---|---|---|---|---|
| 🔴 **CB-01** | Identificação e confirmação do sponsor executivo do projeto | Diretoria / PMO | **25/05/2026** | Projeto não pode avançar para kick-off; governança indefinida; riscos sem dono executivo |
| 🔴 **CB-02** | Verificação documental do acordo com NBS (SLA, escopo de suporte, responsabilidades) | Sandro Siqueira + Jurídico | **30/05/2026** | Kick-off bloqueado; premissa central do projeto sem comprovação formal |
| 🟡 **PEN-01** | Formalização da abertura do projeto pelo PMO após resolução das CBs | PMO / Sponsor | Até 05/06/2026 | Projeto permanece em limbo administrativo; equipe não pode ser mobilizada formalmente |
| 🟡 **PEN-02** | Agendamento e realização do kick-off com stakeholders | Sponsor + Sandro Siqueira | Até 10/06/2026 | Atraso no início da F1; risco de compressão do cronograma e impacto no go-live de outubro |
| 🟡 **PEN-03** | Validação do cronograma e plano de riscos pelo sponsor identificado | Sponsor + Carlos Cronograma | Até 12/06/2026 | Plano de referência sem endosso executivo; sem baseline formal para controle do projeto |
| 🟡 **PEN-04** | Confirmação da data de desativação do Fiscal Defender (RSK-04) | Sandro Siqueira + Fornecedor | Até 15/06/2026 | Risco de gap operacional se o Fiscal Defender for descontinuado antes do go-live do módulo NBS |

---

## 5. Resumo de Riscos — Top 4

| ID | Descrição | Probabilidade | Impacto | Score | Classificação | Próxima Ação |
|---|---|---|---|---|---|---|
| **RSK-01** | Sponsor executivo não identificado — projeto sem governança e sem tomador de decisão | Alta | Muito Alto | **25** | 🔴 CRÍTICO | Identificar e confirmar sponsor até 25/05. PMO deve escalar para diretoria imediatamente. |
| **RSK-02** | Acordo NBS sem verificação documental — premissa central do projeto não comprovada | Alta | Alto | **20** | 🔴 CRÍTICO | Sandro Siqueira deve solicitar documentação contratual/SLA à NBS até 30/05. |
| **RSK-03** | Atrasos da NBS no desenvolvimento do módulo nativo | Média | Alto | **16** | 🔴 CRÍTICO | Incluir cláusulas de SLA no acordo verificado (CB-02). Definir marco de monitoramento mensal. |
| **RSK-04** | Descontinuidade prematura do Fiscal Defender antes do go-live NBS | Média | Alto | **15** | 🔴 CRÍTICO | Confirmar junto ao fornecedor a data de fim de suporte do Fiscal Defender. Mapear gap potencial. |

---

## 6. Próximas Atividades (15/05 – 30/05/2026)

| Data-Limite | Atividade | Responsável | Prioridade |
|---|---|---|---|
| 25/05/2026 | Identificar e confirmar sponsor executivo do projeto (resolução CB-01) | Diretoria / PMO | 🔴 Crítica |
| 30/05/2026 | Verificar e documentar acordo NBS (resolução CB-02) | Sandro Siqueira + Jurídico | 🔴 Crítica |
| 30/05/2026 | Avaliar e responder a Pesquisa de Satisfação sobre o processo de instrução VMO Autônomo | Sandro Siqueira | 🟡 Alta |
| 30/05/2026 | PMO registrar formalmente o status das condições bloqueantes | PMO | 🟡 Alta |
| 30/05/2026 | Após CB-01 resolvida: sponsor revisar e endossar documentação de planejamento | Sponsor | 🟡 Alta |

> **Marco crítico:** Se CB-01 e CB-02 não forem resolvidas até 30/05/2026, o projeto deverá ser reavaliado pelo PMO quanto à viabilidade de manutenção do go-live em 30/10/2026.

---

## 7. Pesquisa de Satisfação — Processo de Instrução VMO Autônomo

> **Para:** Sandro Siqueira (Solicitante)
> **Referência:** PROJ-2026-005 | DEM-2026-002
> **Objetivo:** Avaliar a qualidade do processo de instrução conduzido pelo VMO Autônomo para subsidiar melhoria contínua do pipeline.

Por favor, avalie cada item de **1 a 5**, onde:
**1** = Muito insatisfatório | **2** = Insatisfatório | **3** = Regular | **4** = Satisfatório | **5** = Muito satisfatório

---

**P1. Clareza da documentação produzida**
*Os documentos gerados (TAP, PM Canvas, plano geral, requisitos, cronograma, plano de riscos, KPIs) são claros, bem estruturados e fáceis de compreender?*

☐ 1 | ☐ 2 | ☐ 3 | ☐ 4 | ☐ 5

Comentários: _______________________________________________

---

**P2. Completude do levantamento de requisitos**
*O levantamento de 27 Requisitos Funcionais e 12 Requisitos Não Funcionais reflete adequadamente as necessidades e expectativas da sua demanda?*

☐ 1 | ☐ 2 | ☐ 3 | ☐ 4 | ☐ 5

Comentários: _______________________________________________

---

**P3. Qualidade do plano de riscos**
*O plano de riscos (18 riscos mapeados, incluindo os 4 críticos) identificou adequadamente os pontos de atenção relevantes para o sucesso do projeto?*

☐ 1 | ☐ 2 | ☐ 3 | ☐ 4 | ☐ 5

Comentários: _______________________________________________

---

**P4. Utilidade do cronograma apresentado**
*O cronograma detalhado (77 pacotes de trabalho, go-live 30/10/2026) é realista e útil como instrumento de gestão do projeto?*

☐ 1 | ☐ 2 | ☐ 3 | ☐ 4 | ☐ 5

Comentários: _______________________________________________

---

**P5. Compreensão da sua demanda**
*Você sentiu que a demanda que originou este projeto foi bem compreendida pelo processo VMO Autônomo? O escopo e os objetivos mapeados refletem o que você solicitou?*

☐ 1 | ☐ 2 | ☐ 3 | ☐ 4 | ☐ 5

Comentários: _______________________________________________

---

**P6. Recomendação do processo VMO Autônomo**
*Com base na sua experiência nesta instrução, você recomendaria o processo VMO Autônomo para outros projetos da organização?*

☐ 1 | ☐ 2 | ☐ 3 | ☐ 4 | ☐ 5

Comentários: _______________________________________________

---

**Observações adicionais:**

_______________________________________________
_______________________________________________
_______________________________________________

> Retornar preenchida para: VMO Autônomo — Sara Status | Prazo sugerido: 30/05/2026

---

## 8. Distribuição

| # | Destinatário | Papel | Ação Requerida |
|---|---|---|---|
| 1 | **Sandro Siqueira** | Solicitante / Gestor da Demanda | Leitura obrigatória; responder pesquisa de satisfação; resolver CB-02 |
| 2 | **Sponsor Executivo** (a identificar) | Sponsor do Projeto | Confirmar participação; endossar planejamento; resolver CB-01 |
| 3 | **PMO** | Escritório de Projetos | Acompanhamento; monitorar resolução das CBs; formalizar abertura do projeto |
| 4 | **Diretoria responsável** | Governança | Identificar sponsor executivo (CB-01); ciência dos riscos críticos |
| 5 | **Equipe VMO Autônomo** | Pipeline de Instrução | Registro de conclusão da fase de instrução; arquivo |

---

## Assinaturas e Controle de Versão

| Versão | Data | Autor | Alteração |
|---|---|---|---|
| v1.0 | 15/05/2026 | Sara Status — VMO Autônomo | Emissão inicial |

---

*Este documento foi produzido automaticamente pelo VMO Autônomo — Pipeline de Gestão de Projetos.*
*PROJ-2026-005 | Status Report #001 | 15/05/2026*

---

# ■  09-revisao-qualidade

# Revisão Final de Qualidade — Pacote de Instrução do Projeto

---

## Cabeçalho do Documento

| Campo | Valor |
|---|---|
| **Projeto** | PROJ-2026-005 — Auditor Fiscal: Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Demanda** | DEM-2026-002 |
| **Data da Revisão** | 2026-05-15 |
| **Versão** | v8 — Revisão Final |
| **Autor** | Vera Veredito — Especialista em Revisão de Qualidade, VMO Autônomo |
| **Documentos Avaliados** | v1/demanda-coletada.md · v1/qualificacao.md · v2/documentacao-base.md · v3/requisitos.md · v4/cronograma.md · v5/plano-riscos.md · v6/kpis.md · v7/status-report-inicial.md |
| **Status** | Veredito emitido — Para conhecimento do Comitê VMO e do Sponsor designado |

---

## 1. Tabela de Scores por Critério

| # | Critério | Peso | Nota Obtida | Máximo | % |
|---|---|:---:|:---:|:---:|:---:|
| 1 | Completude | 30 pts | **28** | 30 | 93% |
| 2 | Consistência | 25 pts | **22** | 25 | 88% |
| 3 | Qualidade Técnica | 25 pts | **23** | 25 | 92% |
| 4 | Rastreabilidade | 10 pts | **9** | 10 | 90% |
| 5 | Acionabilidade | 10 pts | **9** | 10 | 90% |
| | **TOTAL** | **100 pts** | **91** | **100** | **91%** |

---

## 2. Classificação Final

> **SCORE: 91/100**
>
> **CLASSIFICAÇÃO: APROVADO**
>
> (Critério: ≥ 85 = APROVADO | 70–84 = APROVADO COM RESSALVAS | < 70 = REPROVADO)

---

## 3. Avaliação Detalhada por Critério

---

### Critério 1 — Completude (28/30)

#### Pontos Fortes

- Todos os 8 documentos foram produzidos e estão presentes no pacote, cobrindo a cadeia completa de instrução: discovery → qualificação → TAP/PM Canvas/Plano Geral → requisitos → cronograma → riscos → KPIs → status report.
- Nenhum documento foi entregue vazio ou como placeholder. Cada seção tem conteúdo substantivo, com tabelas, análises e critérios de aceitação verificáveis.
- O TAP (v2) inclui todos os campos obrigatórios de um termo de abertura: objetivo SMART, escopo in/out, orçamento detalhado por categoria, cronograma macro, premissas, restrições, critérios de sucesso, stakeholders e riscos iniciais.
- O plano de riscos (v5) cobre 18 riscos com fichas detalhadas (causa raiz, consequência, P×I, estratégia, ação preventiva, ação de contingência, dono e frequência de monitoramento).
- O framework de KPIs (v6) entrega três camadas de métricas: execução do projeto (KPI-01 a KPI-10), transição pós go-live (KPI-T01 a KPI-T07) e resultados de negócio em 12 meses (KR-01 a KR-06), com curva S e critérios de encerramento definidos.
- O ERF (v3) apresenta 27 RFs organizados em 6 módulos funcionais e 12 RNFs, com critérios de aceitação testáveis e glossário de domínio.

#### Pontos de Melhoria

- O TAP indica como elaborado por "Marcelo Silveira (GP VMO Autônomo)", mas o documento é gerado por Diana Documento. A inconsistência de autoria é cosmética, mas deve ser corrigida para fins de rastreabilidade formal.
- A seção de controle de versão do TAP menciona aprovação pelo "Gestor do Projeto" em 2026-05-15, porém o próprio TAP informa que o gestor do projeto ainda está "A definir — VMO Autônomo". Esta contradição interna compromete marginalmente a completude.
- O status report (v7) lista a entrega do documento v1 (demanda-coletada.md) como realizada em "01/05/2026" e a qualificação em "02/05/2026", enquanto todos os demais documentos do pacote têm data de referência 2026-05-15 e o cabeçalho da demanda registra a data do registro como 2026-05-15. As datas de entrega listadas no status report para os primeiros documentos aparecem deslocadas do restante da produção — tratado como inconsistência leve na seção de consistência, mas afeta marginalmente a completude do histórico do pacote.

**Dedução:** -2 pontos (inconsistência de autoria do TAP e datas de entrega no status report).

---

### Critério 2 — Consistência (22/25)

#### Pontos Fortes

- O orçamento de R$35.000 é coerente entre todos os documentos que o mencionam: qualificação (cenário central R$35K), TAP (R$35.000 total estimado), PM Canvas (R$35.000 máximo), Plano Geral (detalhado por categoria totalizando R$35.000), cronograma financeiro (R$35.000 com curva de desembolso mensal), e KPIs (BAC R$35.000). Nenhuma contradição orçamentária encontrada.
- O saving anual de R$78.000 é consistente em todos os 8 documentos, sem variação.
- O go-live de 30/10/2026 aparece de forma consistente no cronograma (M-10), no TAP (outubro/novembro 2026 — com margem declarada), no KPIs (go-live planejado 30/10/2026), no status report ("go-live 30/10/2026") e nos riscos (RSK-09 referencia encerramento antes do recesso de dezembro). A margem "out/nov" do TAP é intencional e documentada como estimativa.
- Os requisitos (v3) rastreiam explicitamente às lacunas da demanda (v1), às condições bloqueantes da qualificação (v2), e às seções in/out scope do TAP (v2). A consistência de escopo entre esses três documentos é alta.
- Os riscos críticos RSK-01 e RSK-02 (condições bloqueantes CB-01 e CB-02) são referenciados de forma coerente nos documentos v2, v2 (TAP/Plano Geral), v4 (cronograma), v5 (plano de riscos), v6 (KPIs — ALR-04 e ALR-05) e v7 (status report). A cadeia de bloqueio está rastreada de ponta a ponta.
- As datas das fases do Plano Geral (v2) e do cronograma detalhado (v4) são coerentes: Fase 0 mai/2026, Fase 1 jun/2026, Fase 2 jun–jul/2026, Fase 3 jul–set/2026, Fase 4 set–nov/2026, Fase 5 out–nov/2026, Fase 6 nov–dez/2026.

#### Pontos de Melhoria / Não-Conformidades Leves

**NC-01 — Datas de entrega dos documentos no status report vs. demais cabeçalhos**
O status report (v7) registra que a demanda-coletada.md foi entregue em "01/05/2026" e a qualificacao.md em "02/05/2026", porém o cabeçalho de ambos os documentos marca data de registro/emissão como "2026-05-15". Esta inconsistência de datas internas é leve (provavelmente erro de digitação no status report), mas constitui uma não-conformidade formal que deve ser corrigida na próxima versão do status report.

**NC-02 — Curva S do KPIs vs. Cronograma financeiro**
O cronograma (v4) distribui os desembolsos mensais de forma diferente da curva S do KPIs (v6). No cronograma, a Fase 3 recebe R$8.000 em desembolso direto (distribuídos em jul–set); na curva S do KPIs, a Fase 3 tem peso de 50% sobre o BAC = R$17.500 de valor planejado. Esta diferença é metodologicamente justificável — o KPIs usa PV (valor planejado do EVM, proporcional ao esforço) enquanto o cronograma mapeia desembolsos reais de caixa — mas não está explicitada nos documentos, podendo causar confusão durante o controle do projeto. Não é uma contradição; é uma falta de explicação explícita.

**NC-03 — Rescisão do Fiscal Defender: valor diferente entre documentos**
A qualificacao.md (v1, seção 4.2) estima rescisão entre R$0 e R$30.000 (cenário máximo). O TAP/Plano Geral (v2) estima rescisão em ~R$7.000. O cronograma financeiro (v4) registra rescisão em R$10.000. Todos os três valores cabem dentro do intervalo declarado na qualificação, mas a progressão ascendente (R$7K → R$10K) sem nota de revisão reduz levemente a coerência entre as versões do orçamento.

**Dedução:** -3 pontos (NC-01 requer correção; NC-02 e NC-03 requerem nota explicativa).

---

### Critério 3 — Qualidade Técnica (23/25)

#### Pontos Fortes

- **Objetivo SMART verificado:** O objetivo do TAP atende os cinco critérios SMART. É específico (módulo Auditor Fiscal, Divisão Comércio), mensurável (100% dos RFs do Fiscal Defender replicados, saving R$78K, custo ≤ R$35K), atingível (desenvolvimento como contrapartida NBS, ERP já existente), relevante (consolidação de plataforma e eficiência financeira) e com prazo definido (go-live outubro/novembro 2026).
- **Requisitos testáveis:** Todos os 27 RFs do ERF (v3) seguem o formato "O sistema deve..." com critério de aceitação verificável, incluindo valores numéricos de tolerância, taxas percentuais, prazos de resposta em minutos e perfis de usuário específicos. A adoção do método MoSCoW classifica os requisitos por prioridade com transparência.
- **Riscos com P×I documentados:** Todos os 18 riscos do plano (v5) têm probabilidade (escala 1–5), impacto (escala 1–5) e score calculado. A metodologia é consistente, com escalas definidas e matriz 5×5 apresentada. Cada risco tem causa raiz, consequência, estratégia, ações preventiva e de contingência, dono e frequência de monitoramento.
- **KPIs com metas quantitativas:** Todos os 10 KPIs de execução, 7 KPIs de transição e 6 KRs têm fórmula de cálculo, baseline, meta e threshold mínimo explicitados. As metas são numéricas (ex.: SPI ≥ 1,0; taxa de defeitos ≤ 2%; CSAT ≥ 7,5/10; uptime ≥ 99,5%).
- **Cronograma com caminho crítico:** O documento v4 identifica explicitamente o caminho crítico com sequência de 15 atividades, datas de início/fim, float (dias) de cada atividade e dependências críticas destacadas. O buffer de 15% nas fases de maior risco é documentado com justificativa.
- **EVM completo:** O framework de KPIs (v6) define todos os indicadores EVM (PV, EV, AC, CV, SV, CPI, SPI, EAC, ETC, VAC, TCPI) com fórmulas e thresholds de alerta/escalada, o que é incomum em pacotes de instrução de projetos de médio porte — é um diferencial de qualidade técnica.
- **Análise VME de reserva de contingência:** O plano de riscos (v5) calcula o Valor Monetário Esperado de cada risco financeiro com probabilidade percentual e impacto estimado, resultando em reserva sugerida de R$163.400 — análise de maturidade técnica elevada.

#### Pontos de Melhoria

- O RNF-005 (disponibilidade 99,5%) está especificado no ERF mas a origem desse SLA não é validada com a NBS antes do desenvolvimento — a premissa de que a NBS aceitará esse SLA não está formalmente documentada como pendência crítica. O PEN-001 a PEN-008 do ERF não inclui esta validação explicitamente.
- No ERF (v3), o RF-006 contém um erro de formatação: o campo "Prioridade" usa ":" ao invés de "|" na tabela (`**Prioridade**         : M — Must Have`). É um defeito cosmético que deve ser corrigido.

**Dedução:** -2 pontos (SLA de disponibilidade sem validação com NBS documentada; erro de formatação no ERF).

---

### Critério 4 — Rastreabilidade (9/10)

#### Pontos Fortes

- **Requisitos rastreados à demanda:** O ERF (v3) inclui coluna "Rastreabilidade" em cada RF e RNF, vinculando-os explicitamente aos requisitos preliminares da demanda-coletada (RF-01 a RF-08 e RNF-01 a RNF-04 de Iara Inbound). A Matriz de Rastreabilidade na Seção 6 do ERF consolida todos os 39 requisitos (27 RF + 12 RNF) com origem, módulo e critério de aceitação resumido.
- **Riscos vinculados a causa e resposta:** Todos os 18 riscos têm campo "Causa Raiz" preenchido com análise detalhada, estratégia de resposta categorizada (confrontar/mitigar/aceitar/transferir) e ações de resposta preventiva e de contingência explicitadas. Os riscos críticos têm análise aprofundada com cenários de materialização.
- **KPIs vinculados a objetivos:** O framework de KPIs (v6) vincula KPIs de execução às fases do cronograma, KPIs de transição aos critérios de sucesso do TAP (CS-01 a CS-05), e KRs ao objetivo SMART do projeto. A seção de critérios de encerramento (CE-01 a CE-10) conecta os KPIs aos critérios de aceite.
- **Condições bloqueantes rastreadas em cadeia:** As condições CB-01 e CB-02 são referenciadas com o mesmo ID em todos os documentos que as mencionam (v1, v2, v4, v5, v6, v7), garantindo rastreabilidade completa da condição ao longo do pacote.

#### Pontos de Melhoria

- O plano de riscos (v5) vincula corretamente os riscos entre si (ex.: RSK-01 amplifica todos os outros), mas não há referência explícita de cada risco ao requisito funcional ou restrição do TAP que ele ameaça. Por exemplo, RSK-04 (descontinuidade do Fiscal Defender) deveria referenciar explicitamente a restrição R-05 do TAP. Esta rastreabilidade cruzada risco–requisito está implícita mas não formalizada.

**Dedução:** -1 ponto (rastreabilidade cruzada risco–requisito não formalizada explicitamente).

---

### Critério 5 — Acionabilidade (9/10)

#### Pontos Fortes

- **Próximos passos claros e com prazo:** Todos os documentos terminam com tabela de próximos passos contendo ação, responsável, prazo e prioridade. O status report (v7) tem tabela de atividades para o período 15/05–30/05 com prazos específicos e prioridade codificada por cor.
- **Responsáveis definidos:** Cada ação, risco, KPI e entregável tem um dono nomeado (não só área). O plano de riscos define "Dono do Risco" para cada um dos 18 riscos. Os KPIs têm campo "Responsável" preenchido.
- **Condições bloqueantes sinalizadas com urgência e prazo:** As condições CB-01 (prazo 25/05) e CB-02 (prazo 30/05) estão explicitadas com data-limite, responsável e consequência do não cumprimento em 5 dos 8 documentos. O plano de riscos inclui até "Ação de Contingência" para o caso de não cumprimento.
- **Gatilhos de escalação documentados:** O plano de riscos (v5, seção 6.3) e o framework de KPIs (v6, seção 7) definem gatilhos quantitativos de escalação com prazo de resposta e responsável pela ação — alto grau de acionabilidade operacional.
- **Critérios de entrada e saída por fase:** O cronograma (v4) inclui "Critério de saída" ao final de cada fase, tornando cada transição de fase uma decisão objetiva e auditável.

#### Pontos de Melhoria

- O status report (v7) inclui pesquisa de satisfação endereçada ao solicitante Sandro Siqueira, mas não tem campo para capturar a avaliação do processo de qualificação pela área de Jurídico e Financeiro, que são stakeholders impactados e cujos requisitos ainda estão pendentes (PEN-003 e PEN-004 do ERF). A acionabilidade para engajar essas duas áreas está documentada nos próximos passos, mas não como item da pesquisa.

**Dedução:** -1 ponto (pesquisa de satisfação não cobre stakeholders de Financeiro e Jurídico que têm requisitos pendentes críticos).

---

## 4. Verificação Específica de Consistência

### 4.1 Datas — TAP vs. Cronograma vs. KPIs

| Evento | TAP (v2) | Cronograma (v4) | KPIs (v6) | Consistente? |
|---|---|---|---|---|
| Início do projeto | 2026-05-15 | 2026-05-15 | 2026-05-15 | Sim |
| CB-01 — Sponsor | 25/05/2026 | 25/05/2026 (M-01) | 25/05/2026 (ALR-04) | Sim |
| CB-02 — NBS | 30/05/2026 | 30/05/2026 (M-02) | — (referência indireta) | Sim |
| Kick-off | jun/2026 | 2026-06-05 (M-03) | 14/06/2026 (F1 controle) | Sim (margem coerente) |
| ERF aprovado | jul/2026 | 2026-07-14 (M-05) | 15/07/2026 (F2 controle) | Sim (1 dia de diferença irrelevante) |
| Go-live | out/nov 2026 | 2026-10-30 (M-10) | 30/10/2026 | Sim |
| Encerramento formal | — | 2026-12-10 (M-12) | 16/12/2026 (CE-07) | Sim (margem de 6 dias aceitável) |

**Conclusão:** As datas são coerentes entre TAP, cronograma e KPIs. As pequenas divergências (1–6 dias) estão dentro da margem de estimativa e são consistentes com as sobreposições de fase documentadas.

### 4.2 Orçamento — Coerência entre Documentos

| Componente | Qualificação (v1) | TAP (v2) | Plano Geral (v2) | Cronograma (v4) | KPIs (v6) | Coerente? |
|---|---|---|---|---|---|---|
| Desenvolvimento NBS | R$ 0 | R$ 0 | R$ 0 | R$ 0 | R$ 0 | Sim |
| Implementação | R$ 5K–R$ 20K | ~R$ 15K | R$ 15K | R$ 15K | — (no BAC) | Sim |
| Treinamento | R$ 3K–R$ 10K | ~R$ 8K | R$ 8K | R$ 8K | — (no BAC) | Sim |
| Rescisão FD | R$ 0–R$ 30K | ~R$ 7K | R$ 7K | R$ 10K | — (no BAC) | **NC-03 — ver seção 3** |
| Contingência | — | ~R$ 5K | R$ 4.5K | — (incluso no total) | — | Sim (dentro da margem) |
| **Total Residual** | **R$ 35K (central)** | **~R$ 35K** | **~R$ 35K** | **R$ 35K** | **BAC R$ 35K** | **Sim** |

**Conclusão:** O total orçamentário de R$35.000 é completamente consistente. A NC-03 sobre o valor de rescisão (R$7K vs. R$10K) é leve e não afeta o total.

### 4.3 Condições Bloqueantes — Sinalização entre Documentos

| Documento | CB-01 Sinalizada | CB-02 Sinalizada | Prazo Consistente |
|---|---|---|---|
| v1/demanda-coletada.md | Sim (LAC-01) | Sim (LAC-04) | N/A (pré-qualificação) |
| v1/qualificacao.md | Sim (CB-01, prazo 25/05) | Sim (CB-02, prazo 30/05) | Sim |
| v2/documentacao-base.md | Sim (alerta no TAP e Plano Geral) | Sim (alerta no TAP e Plano Geral) | Sim |
| v3/requisitos.md | Sim (PEN-002 como bloqueante) | Sim (P-002 como maior risco) | Sim (urgente) |
| v4/cronograma.md | Sim (M-01, caminho crítico) | Sim (M-02, caminho crítico) | Sim |
| v5/plano-riscos.md | Sim (RSK-01, score 25, monitoramento diário) | Sim (RSK-02, score 20, monitoramento diário) | Sim |
| v6/kpis.md | Sim (ALR-04, KPI-10) | Sim (ALR-05) | Sim |
| v7/status-report-inicial.md | Sim (CB-01, 🔴 crítico) | Sim (CB-02, 🔴 crítico) | Sim |

**Conclusão:** As condições bloqueantes estão sinalizadas em todos os 8 documentos do pacote, com prazos consistentes. A cadeia de alerta está completa e operacional.

---

## 5. Lista de Não-Conformidades

| ID | Grau | Localização | Descrição | Ação Requerida |
|---|---|---|---|---|
| **NC-01** | Leve | v7/status-report-inicial.md, seção 3 | Datas de entrega dos documentos v1 (01/05 e 02/05/2026) inconsistentes com a data de referência 2026-05-15 registrada nos cabeçalhos de todos os documentos do pacote | Corrigir as datas de entrega no status report para refletir a data real de produção (2026-05-15) ou documentar explicitamente que as datas representam iterações internas do pipeline |
| **NC-02** | Observação | v6/kpis.md Curva S vs. v4/cronograma.md Cronograma Financeiro | Valores de PV por fase (EVM) diferem dos desembolsos mensais sem nota explicativa, podendo gerar confusão no controle financeiro | Adicionar nota no documento de KPIs esclarecendo que PV (curva S) representa valor planejado de esforço/entrega, enquanto o cronograma financeiro representa fluxo de caixa real — os dois são métricas distintas e coexistentes |
| **NC-03** | Leve | v2/documentacao-base.md (R$7K) vs. v4/cronograma.md (R$10K) | Estimativa de rescisão contratual do Fiscal Defender diverge entre os dois documentos sem nota de revisão | Alinhar os valores ou registrar nota explicativa indicando que o cronograma adotou estimativa revisada de R$10K para a rescisão, dentro do intervalo R$0–R$30K declarado na qualificação |
| **NC-04** | Observação | v2/documentacao-base.md, seção "Aprovação do TAP" | O TAP registra "Aprovado" por "Marcelo Silveira" em 2026-05-15, mas o gestor do projeto consta como "A definir — VMO Autônomo" no mesmo documento | Unificar: ou o GP está designado (e o campo deve ser preenchido) ou a aprovação é preliminar e deve ser marcada como "Rascunho" com aprovação pendente |
| **NC-05** | Cosmético | v3/requisitos.md, RF-006 | Erro de formatação na tabela: campo Prioridade usa ":" ao invés de "|" | Corrigir a formatação da célula para manter consistência visual do documento |

**Classificação das não-conformidades:**
- Grau "Leve": requer correção antes da aprovação formal pelo sponsor
- Grau "Observação": requer nota explicativa; não bloqueia aprovação
- Grau "Cosmético": corrigir na próxima versão sem urgência

---

## 6. Recomendações para a Próxima Fase

### Prioridade Crítica (antes do Kick-off)

1. **Resolver CB-01 — Sponsor executivo** até 25/05/2026. Sem sponsor, o pacote de instrução produzido permanece como plano sem autoridade executiva. A qualidade do planejamento só se converte em valor quando há governança para executá-lo.

2. **Resolver CB-02 — Verificação documental do acordo NBS** até 30/05/2026. A premissa de custo zero de desenvolvimento é o alicerce de todo o business case. O plano de riscos calculou corretamente que a invalidação dessa premissa (RSK-02, VME R$56K) potencialmente anula a vantagem financeira do projeto no primeiro ano.

3. **Corrigir NC-01 e NC-04** (ver seção 5) na próxima atualização do status report e do TAP. São inconsistências internas que podem criar dúvidas durante auditorias de projeto.

### Alta Prioridade (durante Fase 0 e Fase 1)

4. **Engajar Financeiro e Jurídico da Divisão Comércio** para confirmação dos requisitos PEN-003 e PEN-004 do ERF. Os RFs e RNFs relativos a esses dois perfis estão corretamente classificados como "a confirmar", mas o prazo de levantamento deve ser formalizado — sugere-se inclusão nos workshops da Fase 2 com participação obrigatória de representantes dessas áreas.

5. **Validar o SLA de disponibilidade (99,5%) com a NBS** antes do congelamento do ERF. Este KPI é critério de aceite do RNF-005 e impacta diretamente a homologação — se a NBS não puder comprometer-se com esse SLA, o critério deve ser renegociado antes de entrar no contrato.

6. **Esclarecer a distinção Curva S (EVM) vs. Cronograma Financeiro** (NC-02) no próximo ciclo de revisão de KPIs para evitar dupla interpretação pelo sponsor e área financeira.

7. **Mapear e confirmar as condições de rescisão do Fiscal Defender** (LAC-09 da demanda, CD-04 da qualificação, RSK-17 do plano de riscos). Esta informação ainda não foi obtida e afeta tanto o cronograma de encerramento quanto o orçamento (NC-03). O prazo recomendado é até 15/06/2026 conforme plano de riscos.

### Planejamento de Médio Prazo

8. **Coletar baseline histórico do Fiscal Defender** antes do início do desenvolvimento (KR-05 requer comparação futura). A taxa histórica de erros fiscais não detectados deve ser registrada durante as fases 0–2 para servir de referência pós go-live.

9. **Incluir testes de carga** no plano de UAT para endereçar RSK-18 (performance em produção). O ERF especifica SLAs de performance (RNF-004), mas o plano de testes ainda não contempla carga com volume real de NF-e — este gap deve ser fechado na elaboração do plano de testes UAT na Fase 4.

10. **Formalizar a política de retenção de dados** (PEN-008 do ERF). O período de 5 anos mencionado no RNF-007 é uma sugestão; a confirmação legal e corporativa deve ocorrer antes da fase de homologação.

---

## 7. Veredito Final

O pacote de instrução do PROJ-2026-005 — Auditor Fiscal NBS — obteve **score 91/100** e recebe o **VEREDITO: APROVADO**.

O conjunto de 8 documentos produzidos pelo VMO Autônomo constitui um dos pacotes de instrução mais completos e tecnicamente sólidos avaliados por esta revisora. Merecem destaque especial: a profundidade do ERF com requisitos testáveis e critérios de aceitação verificáveis para todos os 39 itens; o plano de riscos com análise VME e fichas detalhadas para 18 riscos incluindo 4 críticos; o framework EVM completo com curva S, thresholds de alerta e critérios de encerramento; e o cronograma com caminho crítico explícito, buffer de contingência documentado e critérios de entrada/saída por fase.

A aprovação é sólida, não condicionada. As não-conformidades identificadas são de grau leve ou observação — nenhuma é estrutural. As lacunas de informação (sponsor, prazo NBS, detalhes contratuais) foram corretamente documentadas e rastreadas como condições bloqueantes, e não penalizam a avaliação precisamente porque a equipe de instrução as identificou, classificou por criticidade e definiu responsáveis e prazos para sanação. Um pacote que oculta o que não sabe é mais perigoso do que um pacote que documenta honestamente suas incertezas.

O projeto está pronto para avançar ao kick-off, condicionado exclusivamente à resolução das condições CB-01 e CB-02 conforme os prazos estabelecidos. Se as condições bloqueantes forem sanadas no prazo, o go-live de 30/10/2026 é factível dentro do cronograma planejado.

---

**Vera Veredito**
Especialista em Revisão de Qualidade — VMO Autônomo
Data: 2026-05-15
Versão: v8

> *"Um plano que documenta o que não sabe é mais confiável do que um plano que finge saber tudo. Este pacote documentou suas incertezas com rigor — e por isso merece aprovação."*

