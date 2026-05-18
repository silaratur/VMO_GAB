# DEMANDA VALIDADA — PROJ-2026-005
**Validado por:** Marcelo Silveira — VMO Consultoria
**Data de validação:** 2026-05-18
**Decisão:** ✅ CONFIRMADA — avançar para qualificação
**Observações:** Re-execução completa do pipeline v2 com novos agentes (Fábio Fornecedor + Gabriel Governança)

---

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
