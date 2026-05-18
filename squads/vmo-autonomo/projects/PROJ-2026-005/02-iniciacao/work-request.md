# WORK REQUEST — PROJ-2026-005
## Auditor Fiscal — Módulo Nativo NBS

**Versão:** 1.0 | **Data de Emissão:** 2026-05-18 | **Elaborado por:** VMO Consultoria — Fábio Fornecedor
**Validade deste WR:** 60 dias a partir da data de emissão

---

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Detalhe |
|---|---|
| **ID do Projeto** | PROJ-2026-005 |
| **Nome do Projeto** | Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender |
| **Cliente** | Divisão Comércio — Grupo Águia Branca |
| **Solicitante** | Sandro Siqueira — Coordenador de Contabilidade, Divisão Comércio |
| **Sponsor** | A designar pelo Grupo Águia Branca antes de 2026-06-06 |
| **Gerente de Projeto** | A designar pelo PMO após aprovação do WR |
| **Área Demandante** | Contabilidade — Divisão Comércio |
| **Fornecedor Alvo** | NBS — fornecedora do ERP corporativo do Grupo Águia Branca |
| **Tipo de Solução** | Desenvolvimento de módulo nativo no ERP NBS existente (evolução do produto) |
| **Orçamento de Referência** | R$ 150.000 – R$ 400.000 (benchmark de mercado para módulos fiscais de complexidade equivalente; valor contratual a negociar com a NBS) |
| **Prazo de Referência** | 6 a 12 meses após assinatura do contrato (benchmark de mercado para módulos fiscais desta complexidade) |
| **Data de Emissão do WR** | 2026-05-18 |
| **Prazo para Submissão de Proposta** | 2026-06-06 (15 dias úteis após emissão) |
| **Kickoff Estimado** | A confirmar após assinatura do contrato |

> **Nota sobre o modelo de contratação:** Este Work Request é endereçado diretamente à NBS como fornecedora do ERP, solicitando o desenvolvimento do módulo Auditor Fiscal como evolução nativa da plataforma. O orçamento e o prazo serão definidos na negociação com a NBS, tendo como referência os benchmarks de mercado indicados acima.

---

## 2. CONTEXTO E JUSTIFICATIVA

### 2.1 Problema de Negócio

A Divisão Comércio do Grupo Águia Branca opera atualmente com o **Fiscal Defender** como solução de auditoria e validação de documentos fiscais eletrônicos. A ferramenta cobre processos críticos de compliance: validação de NF-e, detecção de inconsistências entre campos CFOP, NCM e alíquotas declaradas, identificação de pagamentos indevidos ou duplicados, e detecção de possíveis fraudes.

O Fiscal Defender é uma solução de terceiro que opera de forma desacoplada do ERP NBS: os dados de NF-e precisam ser exportados da base NBS para alimentar o sistema de auditoria externo, criando uma dependência de integração frágil e um custo recorrente de licenciamento. Esse modelo gera três riscos concretos:

1. **Risco de Integração:** A sincronia entre a base NBS e o Fiscal Defender depende de processos de exportação que, quando falham, criam janelas de auditoria não coberta — NF-e registradas no ERP que permanecem sem auditoria por horas ou dias sem detecção imediata.
2. **Risco de Conformidade:** A auditoria fiscal opera sobre uma cópia dos dados, não sobre a fonte. Divergências entre a base NBS e os dados auditados pelo Fiscal Defender não são raras e comprometem a confiabilidade dos resultados apresentados em auditorias internas e externas.
3. **Risco Financeiro:** O contrato do Fiscal Defender representa custo recorrente anual que não possui perspectiva de redução tarifária, sendo renovado sistematicamente sem melhoria de cobertura funcional.

### 2.2 Justificativa da Contratação

A solução identificada é o desenvolvimento de um **módulo nativo de Auditor Fiscal diretamente no ERP NBS**, operando sobre a mesma base de dados do ERP sem qualquer integração ou exportação de dados. A NBS, como fornecedora do ERP, é a única entidade com acesso completo ao código-fonte, ao modelo de dados e à arquitetura da plataforma para desenvolver esse módulo com a profundidade técnica necessária.

O módulo nativo elimina todos os riscos de integração do modelo atual, consolida o ecossistema fiscal dentro de uma única plataforma gerida por um único fornecedor e transfere à NBS a responsabilidade de manter o módulo atualizado conforme a evolução da legislação tributária — que é parte do serviço de manutenção do ERP já contratado.

### 2.3 ROI Esperado

| Benefício | Impacto Estimado |
|---|---|
| Eliminação do custo de licença do Fiscal Defender | Saving recorrente anual (a confirmar com Sandro Siqueira) |
| Eliminação de retrabalho com integração e sincronia de dados | Redução de horas da equipe de TI e Contabilidade |
| Auditoria sobre dado nativo (sem janelas de não-cobertura) | Redução de risco de conformidade e de exposição a multas |
| Consolidação de plataforma ERP (single vendor para o ciclo fiscal) | Redução de complexidade operacional e de risco de continuidade |
| Manutenção legislativa automatizada pela NBS | Eliminação de dependência de terceiro em processo crítico de compliance |

---

## 3. OBJETIVO DA CONTRATAÇÃO

Contratar a NBS para **desenvolver o módulo Auditor Fiscal como componente nativo do ERP NBS**, capaz de realizar auditoria automatizada e completa de NF-e diretamente sobre a base de dados do ERP, substituindo integralmente o Fiscal Defender nas funções de: ingestão de NF-e, auditoria de conformidade fiscal e tributária, detecção de inconsistências (CFOP, NCM, alíquotas declaradas vs. tabelas legais), identificação de pagamentos indevidos ou duplicados, detecção de possíveis fraudes, emissão de alertas de risco de multa, geração de relatórios operacionais e gerenciais, controle de acesso por perfil e trilha de auditoria completa de ações — tudo operando nativamente no ERP NBS, sem integração externa, sem exportação de dados e sem dependência de sistemas de terceiros.

---

## 4. ESCOPO DA CONTRATAÇÃO

### 4.1 Escopo Incluso

O módulo a ser desenvolvido pela NBS deverá atender integralmente aos seguintes requisitos funcionais (Must Have):

| ID | Requisito | Descrição |
|---|---|---|
| **RF-INF-01** | Ingestão automática de NF-e da base NBS | O módulo deve acessar, ler e processar NF-e já registradas na base de dados do ERP NBS sem exportação de dados para sistemas externos, sem criação de arquivo intermediário e sem nova entrada de dados pelo usuário. NF-e disponível na base NBS deve estar acessível ao módulo em até 5 minutos após o registro (modo de processamento contínuo). |
| **RF-AUD-01** | Auditoria automatizada de conformidade fiscal e tributária | O módulo deve executar auditoria automatizada de cada NF-e processada, verificando conformidade com a legislação tributária aplicável (ICMS, IPI, PIS/COFINS, CST/CSOSN) e com as regras configuradas pela equipe de Contabilidade, sem necessidade de intervenção manual para cada documento. |
| **RF-AUD-02** | Detecção de inconsistências entre NF-e (CFOP, NCM, alíquotas declaradas vs. tabelas legais) | O módulo deve calcular os valores tributários esperados para cada item da NF-e com base no NCM, CFOP, CST/CSOSN e alíquotas vigentes, comparando com os valores declarados pelo emitente e sinalizando divergências. Deve ainda verificar se o CFOP declarado é compatível com a natureza da operação registrada no ERP. |
| **RF-AUD-03** | Identificação de pagamentos indevidos ou duplicados | O módulo deve identificar NF-e duplicadas (por cruzamento de chave de acesso, CNPJ emitente, número, série e valor), NF-e canceladas com pagamento pendente ou já realizado, e outros padrões que caracterizem risco de pagamento indevido, bloqueando o fluxo de pagamento e gerando alerta imediato ao Analista Financeiro. |
| **RF-AUD-04** | Detecção de possíveis fraudes em NF-e | O módulo deve detectar sinais de fraude documental, incluindo: NF-e emitidas por fornecedores com CNPJ inapto, suspenso ou cancelado na base cadastral do ERP; NF-e com chave de acesso não autorizada pela SEFAZ (status diferente de "autorizado de uso"); e valores atípicos em relação ao histórico do fornecedor (critério configurável pelo Administrador). |
| **RF-AUD-05** | Emissão de alertas de risco de multa por irregularidades fiscais | O módulo deve gerar alertas classificados por nível de criticidade (Alta, Média, Baixa) quando identificar NF-e com divergência tributária que configure risco de autuação fiscal, com tempo máximo de geração do alerta de 15 minutos após a conclusão do processamento da NF-e (modo de processamento contínuo). |
| **RF-REL-01** | Relatórios operacionais acessíveis diretamente no ERP NBS | O módulo deve gerar relatório operacional listando todas as NF-e auditadas em intervalo de datas definido pelo usuário, contendo: chave de acesso, número, série, CNPJ emitente, data de emissão, valor total, status de auditoria, códigos de alerta e data do processamento — exportável em XLSX e PDF diretamente do ERP NBS, em até 60 segundos para lotes de até 10.000 NF-e. |
| **RF-REL-02** | Relatórios gerenciais com visão consolidada da saúde fiscal | O módulo deve gerar relatório gerencial com indicadores de conformidade: total de NF-e processadas, percentual aprovadas sem ressalvas, percentual com alertas por categoria, valor total em risco e evolução mês a mês, para período selecionável de até 24 meses consecutivos — exportável em XLSX e PDF. |
| **RF-INT-01** | Integração com Power BI para dashboards gerenciais (opcional) | O módulo deve expor os dados de resultados de auditoria, alertas e indicadores gerenciais por mecanismo compatível com Power BI Desktop e Power BI Service da Microsoft (API REST, OData endpoint ou view de banco de dados de leitura), permitindo construção de dashboards externos sem desenvolvimento adicional pelo cliente. Este requisito é opcional (Could Have) e deve ser contemplado na proposta com declaração explícita de atendimento ou não atendimento. |
| **RF-SEG-01** | Controle de acesso por perfil | O módulo deve controlar o acesso às funcionalidades por perfil de usuário integrado ao mecanismo de autenticação do ERP NBS, com no mínimo os seguintes perfis segregados: Analista de Contabilidade, Supervisor de Contabilidade, Analista Financeiro, Analista Jurídico e Administrador do Sistema (TI / NBS). Cada perfil deve acessar exclusivamente as funcionalidades e dados para os quais tem permissão — vedada exposição de dados de funcionalidade restrita ao perfil não autorizado. |
| **RF-RAT-01** | Trilha de auditoria completa de todas as ações realizadas no módulo | O módulo deve registrar em log imutável todas as ações de usuário que alteram dados ou configurações, incluindo: login do usuário, data/hora (fuso UTC-3, formato ISO 8601), tipo de ação, entidade afetada e valores anteriores e posteriores à alteração. O log não pode ser editado ou excluído por nenhum perfil de usuário, incluindo o Administrador. Período mínimo de retenção: 5 anos. |

### 4.2 Escopo Excluso

Os seguintes itens estão **expressamente fora do escopo** deste Work Request, com justificativa:

| # | Item Excluído | Justificativa |
|---|---|---|
| 1 | **Emissão de NF-e** | O módulo Auditor Fiscal audita documentos fiscais já emitidos e registrados no ERP; a emissão de NF-e é funcionalidade existente em módulo separado do ERP NBS e não é substituída por este desenvolvimento. |
| 2 | **Escrituração fiscal (SPED Fiscal, EFD-Contribuições e obrigações acessórias)** | A escrituração fiscal é processo separado do processo de auditoria de NF-e; o módulo Auditor Fiscal não substitui nem interfere com os módulos de obrigações acessórias do ERP NBS. |
| 3 | **Transmissão de NF-e para a SEFAZ** | O módulo opera sobre NF-e já recebidas, processadas e com status de autorização SEFAZ já registrado na base NBS; a transmissão para a SEFAZ é responsabilidade do módulo de emissão do ERP NBS. |
| 4 | **Auditoria de NF-e de outras divisões do Grupo Águia Branca além da Divisão Comércio** | O escopo desta fase está restrito à Divisão Comércio. Extensão do módulo para outras divisões do Grupo é projeto futuro e não deve ser contemplada nesta proposta. |
| 5 | **Integração com sistemas fiscais externos além da base NBS** | A solução deve ser 100% nativa no ERP NBS. Qualquer integração com sistemas externos ao ERP (sistemas de terceiros, APIs de órgãos fiscais, middleware externo) está fora do escopo desta contratação. |

---

## 5. PREMISSAS E RESPONSABILIDADES DO GRUPO

O cliente (Divisão Comércio / Grupo Águia Branca) se compromete a disponibilizar os seguintes recursos e condições durante toda a execução do projeto:

> **Nota sobre premissas deste projeto:** diferentemente de projetos com fornecedor externo, a NBS tem acesso próprio à sua base de código e infraestrutura. As premissas abaixo cobrem os insumos de negócio e validação que somente o cliente pode fornecer, necessários para que o desenvolvimento seja tecnicamente correto e funcionalmente validado.

| # | Premissa / Responsabilidade do Grupo |
|---|---|
| 1 | **Designação formal do Sponsor** pelo Grupo Águia Branca antes do prazo de submissão da proposta (2026-06-06), para que haja aprovação formal do WR e emissão de Purchase Order |
| 2 | **Participação de Sandro Siqueira** (Coordenador de Contabilidade) como ponto focal para validação de regras fiscais, aprovação de critérios de auditoria e homologação dos entregáveis funcionais ao longo de todo o projeto |
| 3 | **Fornecimento de exemplos de NF-e reais (anonimizados)** para uso em ambiente de homologação, abrangendo os cenários de auditoria previstos no módulo (NF-e com inconsistências de alíquota, NF-e duplicadas, NF-e canceladas, CNPJ inapto, CFOP incompatível, etc.) |
| 4 | **Disponibilização de ambiente de homologação NBS** para testes e validação do módulo antes da entrada em produção, com dados anonimizados e segregado do ambiente de produção |
| 5 | **Fornecimento das tabelas fiscais de referência atualizadas** (CFOP, NCM, alíquotas de ICMS por UF, CST/CSOSN, exceções tributárias vigentes para as operações da Divisão Comércio) antes do início da configuração das regras de auditoria no módulo |
| 6 | **Participação dos representantes das áreas Financeiro e Jurídico** da Divisão Comércio em sessões de levantamento de requisitos para os fluxos e relatórios específicos dessas áreas, e nos testes de aceitação (UAT) correspondentes |
| 7 | **Homologação dos entregáveis** em até 10 dias úteis após entrega formal de cada marco, com aceite formal (SIM/NÃO) e justificativa escrita em caso de rejeição |
| 8 | **Fornecimento da documentação completa do Fiscal Defender** (regras de auditoria configuradas, relatórios em uso, perfis de usuário, fluxos operacionais) para referência no desenvolvimento do módulo substituto — entregue à NBS até o início do desenvolvimento |
| 9 | **Designação de representante de TI** com autorização para gestão de ambientes, acesso a dados de homologação e suporte à integração com Power BI (se RF-INT-01 for contemplado) |
| 10 | **Aprovação formal de cada entregável** pelo GP designado, usando os critérios binários definidos na Seção 7 |

> **Atenção:** O não cumprimento de qualquer premissa acima pelo cliente poderá implicar revisão de prazo proporcional ao tempo de bloqueio, sem penalidade à NBS, desde que formalmente comunicado via canal de governança (ver Seção 8).

---

## 6. CRONOGRAMA ESPERADO

> **Nota metodológica:** As datas abaixo são marcos de referência baseados em benchmark de mercado para módulos fiscais de complexidade equivalente. O cronograma detalhado será acordado entre as partes após aprovação da proposta técnica da NBS, com ajuste à capacidade da equipe NBS e às janelas de disponibilidade do cliente. Datas são estimativas, não compromisos contratuais desta fase.

| Marco | Descrição | Referência de Prazo |
|---|---|---|
| **M0** | Emissão do Work Request | 2026-05-18 |
| **M1** | Prazo para submissão de proposta da NBS | 2026-06-06 |
| **M2** | Avaliação e aprovação da proposta técnica e comercial | 2026-06-13 |
| **M3** | Assinatura do contrato / Início do prazo contratual | A confirmar |
| **M4** | Kickoff do projeto com NBS | A confirmar (até 15 dias após M3) |
| **M5** | Entrega do Documento de Arquitetura e Especificação Técnica do módulo | M3 + 45 dias (referência) |
| **M6** | Desenvolvimento concluído em ambiente de desenvolvimento NBS | M3 + 4 a 6 meses (referência de mercado) |
| **M7** | Homologação pelo cliente em ambiente de teste (UAT) | M6 + 30 a 45 dias |
| **M8** | Go-live em produção + treinamento concluído | M7 + 30 dias |
| **M9** | Encerramento formal e início do período de garantia | Após aceite do go-live |

> **Referência de mercado:** Módulos fiscais para ERPs de porte médio têm prazo de desenvolvimento de 6 a 12 meses. Parceiros SAP com módulos similares (FISCOsolve, Synchro, Mastersaf) entregam módulos de auditoria fiscal nativa em 8 a 12 meses. A complexidade adicional das validações NBS (Nomenclatura Brasileira de Serviços) representa um fator de complexidade que deve ser declarado na proposta técnica da NBS.

---

## 7. ENTREGÁVEIS OBRIGATÓRIOS

Todos os entregáveis abaixo são obrigatórios. O critério de aceite é **binário**: o entregável está aceito (SIM) ou não está aceito (NÃO) — não existe aceite parcial.

| # | Entregável | Marco Associado | Critério de Aceite (Binário) |
|---|---|---|---|
| **E1** | Proposta Técnica detalhada (arquitetura do módulo, abordagem de desenvolvimento, tecnologias utilizadas, integração com ERP NBS) | M1 | SIM: proposta cobre todos os RFs do Escopo Incluso com descrição técnica de implementação, identifica claramente o que está incluído e o que está fora do escopo, e é aprovada pelo GP e por Sandro Siqueira. NÃO: qualquer RF sem cobertura técnica descrita ou ausência de aprovação. |
| **E2** | Proposta Comercial com cronograma de pagamentos por marcos e garantias contratuais | M1 | SIM: proposta apresenta valor total, detalhamento por fase, cronograma de pagamentos vinculado a marcos, prazo total de desenvolvimento e período de garantia mínimo de 90 dias — todos dentro das condições desta Seção e da Seção 9. NÃO: qualquer item ausente ou condição incompatível com este WR. |
| **E3** | Documento de Arquitetura Técnica do Módulo (modelo de dados, integração com base NBS, mecanismo de acesso a NF-e, modelo de segurança) | M5 | SIM: documento aprovado pelo GP e pela equipe de TI do cliente, descrevendo arquitetura completa sem dependências externas ao ERP NBS, modelo de dados e estratégia de acesso nativo. NÃO: ausência de qualquer componente técnico ou não aprovação pelo cliente. |
| **E4** | Módulo desenvolvido e disponível em ambiente de homologação, cobrindo todos os RFs Must Have (RF-INF-01, RF-AUD-01 a RF-AUD-05, RF-REL-01, RF-REL-02, RF-SEG-01, RF-RAT-01) | M6 | SIM: todos os 10 RFs Must Have verificáveis e funcionais em ambiente de homologação NBS. NÃO: qualquer RF Must Have pendente, não funcional ou não verificável no ambiente de homologação. |
| **E5** | Roteiro de Testes (casos de teste cobrindo todos os RFs Must Have, com passos, dados de entrada, resultado esperado e campo de resultado) | M6 | SIM: roteiro com caso de teste para cada RF Must Have, com dados de teste baseados nos exemplos de NF-e fornecidos pelo cliente (Premissa 3), aprovado pelo GP e por Sandro Siqueira. NÃO: qualquer RF Must Have sem caso de teste ou roteiro não aprovado. |
| **E6** | Relatório de Testes de Homologação (UAT) com evidências, assinado pelo cliente | M7 | SIM: todos os casos de teste do roteiro (E5) executados com resultado conforme, com evidências (prints ou logs), assinado pelo GP, por Sandro Siqueira e pelos representantes de Financeiro e Jurídico. NÃO: qualquer caso de teste reprovado, não executado ou ausência de assinatura de algum representante do cliente. |
| **E7** | Documentação do usuário: manuais de operação por perfil (Contabilidade, Financeiro, Jurídico, Administrador) | M7 | SIM: manual de operação para cada um dos 5 perfis de usuário (RF-SEG-01), descrevendo todas as funcionalidades acessíveis ao perfil, com prints de telas da versão homologada, aprovado por Sandro Siqueira. NÃO: ausência de manual para qualquer perfil ou não aprovação pelo solicitante. |
| **E8** | Módulo implantado e operacional em produção, com validação pós-go-live | M8 | SIM: módulo ativo em ambiente de produção NBS, com ao menos um lote real de NF-e processado e resultado de auditoria verificado por Sandro Siqueira, sem erros críticos. NÃO: qualquer falha de implantação em produção ou ausência de validação pelo cliente. |
| **E9** | Registro de Treinamento das equipes de Contabilidade, Financeiro e Jurídico | M8 | SIM: ata de treinamento assinada pelos representantes das três áreas, comprovando sessão realizada para cada perfil, com material didático entregue. NÃO: ausência de ata assinada por qualquer área ou ausência de entrega do material didático. |
| **E10** | Relatório de Encerramento do Projeto (resumo da solução implantada, evidências de go-live, conformidade com os RFs, lições aprendidas, term sheet de aceite final) | M9 | SIM: documento com todas as seções preenchidas, evidências de funcionamento em produção, lista de RFs atendidos com referência cruzada aos casos de teste, e term sheet de aceite assinado pelo Sponsor. NÃO: ausência de qualquer seção, de evidências ou da assinatura do Sponsor. |

---

## 8. GOVERNANÇA E COMUNICAÇÃO

### 8.1 Estrutura de Governança

| Papel | Responsável | Atribuição |
|---|---|---|
| **Sponsor** | A designar pelo Grupo Águia Branca | Aprovação final do go-live; escalação de bloqueios estratégicos; assinatura do term sheet de encerramento |
| **Gerente de Projeto (GP)** | A designar pelo PMO | Gestão do projeto, aprovação formal de entregáveis, controle de prazo e orçamento, interface com a NBS |
| **Ponto Focal Técnico-Funcional** | Sandro Siqueira — Coordenador de Contabilidade | Validação de regras fiscais, aprovação de critérios de auditoria, aceite funcional dos entregáveis |
| **Gestor do Projeto (NBS)** | A indicar pela NBS na proposta | Coordenação do desenvolvimento, entrega dos artefatos, comunicação com o GP do cliente |
| **Responsável Técnico NBS** | A indicar pela NBS na proposta | Arquitetura técnica do módulo, integração com a base NBS, suporte ao UAT |
| **Analista de TI (Cliente)** | A designar pelo Grupo Águia Branca | Suporte ao acesso de ambientes, integração com Power BI (se aplicável), gestão do ambiente de homologação |

### 8.2 Comunicação

- **Reunião de Status Quinzenal:** a cada duas semanas, 45 minutos, formato a combinar no kickoff (presencial ou videoconferência).
- **Canal oficial de comunicação:** e-mail corporativo, com GP em cópia em todas as mensagens técnicas e decisões relevantes.
- **Comunicação de bloqueios:** bloqueios que impactem prazo ou escopo devem ser reportados ao GP em até 24 horas após identificação, com descrição do impacto e plano de mitigação sugerido.
- **Aprovação de entregáveis:** o GP tem até **10 dias úteis** após a entrega formal para aceitar (SIM) ou rejeitar (NÃO) cada entregável, com justificativa escrita no caso de rejeição.
- **Retrabalho:** em caso de rejeição de entregável, a NBS tem até **10 dias úteis** para corrigir e reapresentar, sem custo adicional, desde que a rejeição seja fundamentada em não conformidade com os critérios definidos neste WR.
- **Relatório de status:** a NBS deve enviar relatório quinzenal de progresso ao GP até a véspera de cada reunião de status, contendo: atividades concluídas, atividades em andamento, próximas atividades, riscos identificados e eventuais bloqueios.

### 8.3 Gestão de Mudanças

Qualquer alteração de escopo, prazo ou condições comerciais requer **Change Request (CR)** formal, submetido pela NBS ao GP com justificativa técnica e impacto declarado, aprovado pelo Sponsor antes da execução. CRs não aprovados formalmente não serão executados nem faturados.

---

## 9. CONDIÇÕES COMERCIAIS

### 9.1 Orçamento de Referência

| Item | Referência |
|---|---|
| Custo de referência para módulos fiscais integrados em ERPs de porte médio | R$ 200.000 – R$ 500.000 |
| **Envelope máximo aceitável para este projeto** | **R$ 400.000** |
| Propostas acima do envelope máximo | Desclassificadas automaticamente |

> **Nota:** O envelope máximo de R$ 400.000 é o teto de referência de mercado para módulos fiscais desta complexidade. A VMO Consultoria espera que a proposta da NBS, como fornecedora do ERP com acesso direto à base de código, apresente proposta competitiva dentro desse envelope. Propostas com valor justificado tecnicamente entre R$ 150.000 e R$ 400.000 serão avaliadas na íntegra.

### 9.2 Faturamento por Marcos

O pagamento será realizado conforme entrega e aceite formal dos marcos abaixo. A proposta da NBS deve apresentar a distribuição de valores por marco, alinhada à seguinte referência:

| Marco | Entregáveis Associados | % de Referência |
|---|---|---|
| **Marco 1** — Assinatura do contrato / kickoff | — | 10% |
| **Marco 2** — Documento de Arquitetura Técnica aprovado | E3 | 15% |
| **Marco 3** — Desenvolvimento concluído em homologação | E4, E5 | 35% |
| **Marco 4** — Homologação (UAT) aprovada + Documentação de usuário | E6, E7 | 25% |
| **Marco 5** — Go-live em produção + Treinamento + Encerramento | E8, E9, E10 | 15% |
| **Total** | | **100%** |

> A proposta da NBS pode sugerir distribuição alternativa de marcos e percentuais, desde que: (a) o percentual de go-live (Marco 5) seja no mínimo 15%; (b) nenhum marco único represente mais de 40% do valor total; e (c) a estrutura seja previamente aprovada pelo Sponsor do cliente.

> Faturamento condicionado ao aceite formal (critério SIM) de todos os entregáveis associados ao marco. Pagamentos realizados em até **15 dias corridos** após o aceite formal.

### 9.3 Penalidades por Atraso

- **Atraso imputável à NBS:** multa de 0,5% do valor total do contrato por semana de atraso em cada marco, limitada a 10% do valor total do contrato.
- **Atraso imputável ao cliente:** prazo estendido proporcionalmente, sem penalidade à NBS, desde que o bloqueio seja formalmente comunicado e aceito pelo GP com evidências do bloqueio causado pelo cliente.

### 9.4 Garantia de Funcionamento

- A NBS garante o funcionamento do módulo em produção por **mínimo de 90 dias corridos** após o go-live (propostas com prazo inferior serão desclassificadas).
- Falhas de funcionamento identificadas dentro do período de garantia serão corrigidas sem custo adicional, em prazo máximo de 10 dias úteis para falhas críticas (que impedem a operação) e 20 dias úteis para falhas não críticas.
- Alterações de escopo ou novas funcionalidades solicitadas durante o período de garantia serão tratadas como novo Work Request.
- Após o período de garantia, a manutenção evolutiva e corretiva do módulo segue o contrato de suporte e manutenção do ERP NBS vigente entre as partes.

### 9.5 Manutenção Legislativa

A proposta deve declarar expressamente o compromisso da NBS de manter o módulo atualizado conforme a evolução da legislação tributária brasileira, incluindo:
- Atualização de tabelas fiscais (NCM, CFOP, alíquotas de ICMS por UF) dentro do ciclo normal de atualização do ERP NBS;
- Compatibilidade do módulo com novas versões do ERP NBS em até 30 dias após o lançamento de versão que afete o módulo;
- Incorporação de mudanças legislativas com vigência publicada com mais de 30 dias de antecedência, antes da data de vigência.

### 9.6 Propriedade Intelectual

Todos os artefatos de documentação entregues (manuais, roteiros de teste, relatórios de encerramento) são de propriedade exclusiva do Grupo Águia Branca / Divisão Comércio a partir do aceite formal. O módulo desenvolvido, sendo componente do ERP NBS, segue as condições de propriedade intelectual do contrato de fornecimento do ERP vigente — que devem ser declaradas expressamente pela NBS na proposta.

---

## 10. ARTEFATO OBRIGATÓRIO — CONFORMIDADE DA PROPOSTA

A proposta técnica e comercial da NBS só será considerada válida se acompanhada da tabela de conformidade abaixo, **completamente preenchida**. Propostas sem este artefato ou com itens em branco serão desclassificadas.

**Instrução:** Para cada item, marque **OK** (atende plenamente), **NOK** (não atende) ou **Parcial** (atende com ressalva — obrigatório descrever em Observações).

---

### Grupo 1 — Qualificação da NBS como Fornecedora do Módulo (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 1.1 | NBS declara que possui acesso completo ao código-fonte, modelo de dados e arquitetura do ERP para desenvolver o módulo como componente nativo, sem dependência de terceiros | | | |
| 1.2 | NBS comprova experiência prévia no desenvolvimento de módulos fiscais nativos ou módulos de auditoria tributária sobre a plataforma ERP NBS (mínimo 1 módulo em produção com documentação de referência) | | | |
| 1.3 | NBS apresenta equipe técnica designada para o projeto com experiência comprovada em desenvolvimento fiscal/tributário e conhecimento da legislação tributária brasileira aplicável (ICMS, IPI, PIS/COFINS, NCM, CFOP, CST/CSOSN) | | | |
| 1.4 | NBS declara que o desenvolvimento deste módulo não impactará negativamente o roadmap nem a disponibilidade dos demais módulos do ERP em uso pelo Grupo Águia Branca durante o período de desenvolvimento | | | |

---

### Grupo 2 — Entendimento do Escopo (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 2.1 | Proposta demonstra entendimento técnico de todos os 11 requisitos do Escopo Incluso (RF-INF-01, RF-AUD-01 a RF-AUD-05, RF-REL-01, RF-REL-02, RF-INT-01, RF-SEG-01, RF-RAT-01), com descrição da abordagem de implementação de cada um | | | |
| 2.2 | Proposta confirma que o módulo será desenvolvido como componente 100% nativo do ERP NBS, operando sobre a mesma base de dados do ERP, sem integração externa, sem exportação de dados e sem dependência de sistemas de terceiros para a operação de auditoria | | | |
| 2.3 | Proposta identifica e declara o que está fora do escopo (alinhado à Seção 4.2), confirmando que emissão de NF-e, escrituração SPED, transmissão SEFAZ, extensão para outras divisões e integração com sistemas externos NBS estão fora do escopo desta contratação | | | |
| 2.4 | Proposta declara posição sobre o RF-INT-01 (integração com Power BI), indicando se será atendido (OK), não atendido (NOK) ou atendido parcialmente (Parcial), com descrição técnica do mecanismo de integração proposto em caso de atendimento | | | |

---

### Grupo 3 — Plano de Trabalho e Cronograma (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 3.1 | Proposta apresenta plano de trabalho com fases, atividades e marcos compatíveis com os marcos de referência da Seção 6 (Arquitetura, Desenvolvimento, Homologação, Go-live) | | | |
| 3.2 | Prazo total de desenvolvimento declarado na proposta está dentro da referência de 6 a 12 meses após kickoff, com justificativa técnica para o prazo proposto | | | |
| 3.3 | Proposta apresenta estimativa de esforço (horas ou dias por fase/atividade) e alocação da equipe, permitindo avaliação da viabilidade do prazo proposto | | | |
| 3.4 | Plano de testes descrito, cobrindo os 10 RFs Must Have com estratégia de execução do UAT com a equipe do cliente (Contabilidade, Financeiro, Jurídico), e estratégia de implantação em produção com plano de operação paralela com o Fiscal Defender (mínimo 30 dias antes do desligamento) | | | |

---

### Grupo 4 — Entregáveis (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 4.1 | Proposta lista e descreve todos os 10 entregáveis obrigatórios (E1 a E10) com prazo estimado para cada um | | | |
| 4.2 | Proposta apresenta índice ou estrutura do Documento de Arquitetura Técnica (E3), demonstrando que cobrirá modelo de dados, integração nativa com a base NBS, mecanismo de controle de acesso e trilha de auditoria imutável | | | |
| 4.3 | Proposta apresenta estrutura do Roteiro de Testes (E5), demonstrando que cobrirá todos os 10 RFs Must Have com casos de teste verificáveis baseados em NF-e reais anonimizadas fornecidas pelo cliente | | | |
| 4.4 | Proposta confirma entrega de manuais de operação por perfil (E7) para todos os 5 perfis definidos no RF-SEG-01, e emissão do Relatório de Encerramento (E10) com term sheet de aceite assinado pelo Sponsor | | | |

---

### Grupo 5 — Condições Comerciais (5 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 5.1 | Valor total da proposta está dentro do envelope máximo de R$ 400.000 | | | |
| 5.2 | Proposta apresenta composição de preço por marco, compatível com a estrutura de referência da Seção 9.2 (ou proposta alternativa justificada com os limites da Seção 9.2) | | | |
| 5.3 | Proposta aceita as penalidades por atraso descritas na Seção 9.3 (0,5% por semana, limitado a 10% do contrato) | | | |
| 5.4 | Proposta aceita o período de garantia mínimo de 90 dias corridos após go-live, com os prazos de correção definidos na Seção 9.4 | | | |
| 5.5 | Proposta declara posição sobre manutenção legislativa (Seção 9.5), confirmando ou detalhando as condições de atualização de tabelas fiscais e compatibilidade com novas versões do ERP | | | |

---

### Grupo 6 — Gestão de Riscos (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 6.1 | Proposta identifica os principais riscos técnicos do projeto, incluindo: risco de complexidade das regras NBS (Nomenclatura Brasileira de Serviços), risco de performance em lotes grandes de NF-e, risco de compatibilidade com versões futuras do ERP e risco de escopo de regras tributárias não mapeadas | | | |
| 6.2 | Proposta descreve plano de mitigação para cada risco identificado, com responsável e prazo | | | |
| 6.3 | Proposta declara dependências críticas do lado do cliente (alinhadas às premissas da Seção 5), identificando quais itens, se não fornecidos pelo cliente no prazo, impactarão o cronograma de desenvolvimento | | | |
| 6.4 | Proposta descreve processo de escalonamento em caso de bloqueio crítico, incluindo o nível de escalação dentro da NBS e o prazo máximo para resposta ao GP do cliente | | | |

---

### Grupo 7 — Premissas Aceitas (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 7.1 | NBS aceita que o cliente fornecerá exemplos de NF-e reais anonimizados para uso nos testes de homologação, cobrindo os cenários de auditoria previstos no módulo | | | |
| 7.2 | NBS aceita que o cliente fornecerá as tabelas fiscais de referência atualizadas (CFOP, NCM, alíquotas por UF, CST/CSOSN) antes do início da configuração das regras de auditoria | | | |
| 7.3 | NBS aceita que o cliente fornecerá ambiente de homologação disponível com dados anonimizados antes do início da fase de testes, e que eventuais indisponibilidades do ambiente imputáveis ao cliente serão formalmente comunicadas para extensão proporcional do prazo | | | |
| 7.4 | NBS aceita que a documentação completa do Fiscal Defender (regras, relatórios, perfis, fluxos) será fornecida pelo cliente antes do início do desenvolvimento, e que informações adicionais não fornecidas no prazo poderão impactar o cronograma | | | |

---

### Grupo 8 — Governança e Comunicação (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 8.1 | NBS aceita reunião de status quinzenal no formato definido pelo cliente (presencial ou videoconferência), com relatório de progresso entregue 1 dia útil antes de cada reunião | | | |
| 8.2 | NBS aceita comunicar bloqueios que impactem prazo ou escopo em até 24 horas após a identificação, via canal oficial, com descrição do impacto e plano de mitigação sugerido | | | |
| 8.3 | NBS aceita o processo de aprovação de entregáveis em até 10 dias úteis pelo GP do cliente, e o processo de retrabalho em até 10 dias úteis em caso de rejeição fundamentada | | | |
| 8.4 | NBS aceita o processo de Change Request formal para qualquer alteração de escopo, prazo ou condições comerciais, com aprovação prévia do Sponsor do cliente antes da execução | | | |

---

### Grupo 9 — Conformidade Técnica do Módulo (6 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 9.1 | Proposta confirma que o módulo operará nativamente sobre a base de dados do ERP NBS, sem exportação de dados para sistemas externos durante o processo de auditoria | | | |
| 9.2 | Proposta confirma que uma NF-e registrada na base NBS estará disponível para processamento pelo módulo em até 5 minutos após o registro (modo de processamento contínuo), conforme RF-INF-01 | | | |
| 9.3 | Proposta confirma que o log de auditoria de ações (RF-RAT-01) será imutável e não poderá ser editado ou excluído por nenhum perfil de usuário, incluindo o Administrador, com retenção mínima de 5 anos | | | |
| 9.4 | Proposta confirma que o controle de acesso por perfil (RF-SEG-01) será integrado ao mecanismo de autenticação existente do ERP NBS, sem sistema de autenticação paralelo, e que usuário com perfil inadequado receberá mensagem de acesso não autorizado sem exposição de dados da funcionalidade restrita | | | |
| 9.5 | Proposta descreve como o módulo atenderá à conformidade com a LGPD para dados pessoais eventualmente presentes em NF-e (CPF de destinatários, transportadores), com segregação de acesso por perfil | | | |
| 9.6 | Proposta confirma que o módulo não modificará registros originais de NF-e na base NBS, gravando os resultados de auditoria em estrutura de dados separada e vinculada à chave de acesso da NF-e | | | |

---

### Grupo 10 — Declarações da NBS (9 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 10.1 | NBS declara não ter conflito de interesse com o Grupo Águia Branca / Divisão Comércio que impeça a prestação objetiva e imparcial dos serviços de desenvolvimento | | | |
| 10.2 | NBS declara que todos os dados do cliente acessados durante o desenvolvimento e os testes serão tratados com confidencialidade e utilizados exclusivamente para fins deste projeto | | | |
| 10.3 | NBS declara que os dados do cliente serão descartados ou devolvidos ao término do projeto, conforme política de segurança da informação acordada contratualmente | | | |
| 10.4 | NBS declara ter lido e compreendido integralmente este Work Request, incluindo todos os requisitos, premissas, entregáveis, condições comerciais e critérios de aceite | | | |
| 10.5 | NBS declara que a equipe técnica designada para o projeto estará disponível durante todo o período de desenvolvimento, e que eventuais substituições de membros-chave serão comunicadas ao GP com antecedência mínima de 15 dias e estarão sujeitas à aprovação do cliente | | | |
| 10.6 | NBS declara capacidade de iniciar o projeto (kickoff) em até 15 dias úteis após a assinatura do contrato | | | |
| 10.7 | NBS declara que o desenvolvimento deste módulo não introduzirá componentes de software de terceiros sem licença compatível com o uso comercial do Grupo Águia Branca | | | |
| 10.8 | NBS declara as condições de propriedade intelectual aplicáveis ao módulo desenvolvido, incluindo se o cliente terá direito de uso perpétuo do módulo independentemente da continuidade do contrato de ERP | | | |
| 10.9 | NBS declara que todos os 41 itens desta tabela foram avaliados e respondidos, e que a proposta submetida está em conformidade com os termos deste Work Request | | | |

---

**Resumo de Conformidade (preencher pela NBS):**

| | Quantidade |
|---|---|
| Itens OK | ___ / 41 |
| Itens NOK | ___ / 41 |
| Itens Parcial | ___ / 41 |

> **Regra de desclassificação:** Propostas com qualquer item **NOK** nos Grupos 1, 2, 5 ou 10 serão automaticamente desclassificadas. Itens **Parcial** nos demais grupos serão avaliados pela VMO Consultoria com base nas observações declaradas.

---

## 11. PROCESSO DE SUBMISSÃO

### 11.1 Prazo e Canal

- **Prazo final para envio:** **2026-06-06, até 18h00 (horário de Brasília)**
- **Canal de envio:** e-mail para o GP designado pelo PMO, com cópia para o Sponsor e para Sandro Siqueira
- **Assunto obrigatório do e-mail:** `[PROPOSTA] PROJ-2026-005 — Auditor Fiscal Módulo NBS — NBS`

### 11.2 Documentos Obrigatórios na Proposta

| # | Documento | Formato |
|---|---|---|
| 1 | Proposta Técnica (arquitetura do módulo, abordagem por RF, tecnologias, plano de trabalho, equipe, cronograma) | PDF |
| 2 | Proposta Comercial (valor por marco, composição de custos, condições de pagamento) | PDF |
| 3 | Tabela de Conformidade (Seção 10) completamente preenchida e assinada pelo responsável técnico da NBS | PDF |
| 4 | CVs dos profissionais técnicos designados para o projeto (líder técnico, arquiteto, especialista fiscal) | PDF |
| 5 | Documentação de referência de módulo fiscal nativo ou equivalente desenvolvido pela NBS (mínimo 1 caso de referência) | PDF |
| 6 | Cronograma físico-financeiro detalhado por fase e atividade | PDF ou XLSX |
| 7 | Declaração de propriedade intelectual sobre o módulo a ser desenvolvido | PDF |

### 11.3 Critérios de Avaliação

A proposta da NBS será avaliada pelos seguintes critérios:

| Critério | Peso |
|---|---|
| Adequação técnica (cobertura dos RFs Must Have e qualidade da arquitetura proposta) | 35% |
| Prazo total de desenvolvimento e qualidade do plano de trabalho | 25% |
| Preço total (dentro do envelope máximo de R$ 400.000) | 20% |
| Qualidade do plano de testes, homologação e estratégia de operação paralela | 10% |
| Condições de manutenção legislativa e garantia pós go-live | 10% |

### 11.4 Esclarecimentos

Dúvidas sobre este Work Request devem ser enviadas por e-mail até **2026-05-30** para o GP designado pelo PMO, com cópia para Sandro Siqueira, com assunto `[DÚVIDA] PROJ-2026-005 — NBS`. As respostas serão consolidadas e enviadas em até 3 dias úteis após o recebimento.

### 11.5 Sigilo e Confidencialidade

Este documento é de uso restrito e destinado exclusivamente à NBS e aos stakeholders internos do Grupo Águia Branca / Divisão Comércio envolvidos na avaliação. Sua reprodução, distribuição ou uso para fins outros que não a elaboração da proposta é vedada sem autorização prévia da VMO Consultoria e do Grupo Águia Branca.

---

## APROVAÇÕES

| Papel | Nome | Assinatura | Data |
|---|---|---|---|
| **Elaboração** | Fábio Fornecedor — VMO Consultoria | | 2026-05-18 |
| **Validação Técnica e Funcional** | Sandro Siqueira — Coordenador de Contabilidade, Divisão Comércio | | |
| **Aprovação** | Sponsor — Grupo Águia Branca (a designar) | | Até 2026-06-06 |

---

*Work Request emitido pela VMO Consultoria em nome da Divisão Comércio — Grupo Águia Branca.*
*Documento confidencial — uso restrito ao Grupo Águia Branca e à NBS.*
*Versão 1.0 | Emitido em 2026-05-18 | PROJ-2026-005*
