# WORK REQUEST — WR-2026-006
## Plataforma Própria de Gestão de Ideias e Inovação

---

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Valor |
|---|---|
| **Código do Projeto** | PROJ-2026-006 |
| **Código da Demanda** | DEM-2026-006 |
| **Código do Work Request** | WR-2026-006 |
| **Nome do Projeto** | Plataforma Própria de Gestão de Ideias e Inovação |
| **Empresa Contratante** | Grupo (divisões: Comércio, Passageiros, Logística) |
| **Gestora do Projeto** | VMO Consultoria |
| **GP Responsável** | A ser preenchido após identificação do sponsor |
| **Solicitante** | Jadson — Gestor de Inovação |
| **Tipo de Solução** | Desenvolvimento de software sob medida (SaaS proprietário) |
| **Data de Emissão do WR** | 16/05/2026 |
| **Prazo de Submissão de Propostas** | **06/06/2026 às 23h59 (horário de Brasília)** |
| **Validade da Proposta** | 30 dias corridos a partir da data de submissão |
| **Data Esperada de Kick-off** | 24/06/2026 |
| **Envelope de Investimento de Referência** | R$ 100.000,00 (inclui contingência de 20%) |

---

## 2. CONTEXTO E JUSTIFICATIVA

### 2.1 Problema

O Grupo opera atualmente sem uma plataforma estruturada para captação, avaliação e acompanhamento de ideias de inovação. O processo vigente é conduzido via planilhas Excel e e-mails, resultando em:

- **Perda de ideias:** colaboradores não possuem canal formal e rastreável para submissão. Estimativa interna aponta que mais de 60% das ideias geradas em reuniões e workshops não são registradas formalmente.
- **Ausência de ciclo de aprovação:** inexistência de workflow de aprovação com histórico auditável, o que impede prestação de contas e rastreabilidade.
- **Mensuração impossível:** sem registro estruturado de ganhos prometidos versus realizados, o ROI do programa de inovação é impossível de calcular e comunicar à liderança.
- **Engajamento reduzido:** a falta de visibilidade sobre o status das ideias submetidas desmotiva a participação dos colaboradores.
- **Retrabalho operacional:** o time de inovação gasta em média 12 horas/semana compilando manualmente relatórios de status do programa.

### 2.2 Justificativa de Negócio e ROI

| Indicador | Valor Estimado |
|---|---|
| **Economia em retrabalho operacional** | R$ 45.000/ano (12h/semana × 50 semanas × custo médio analista) |
| **Ganho em ideias capturadas e implementadas** | R$ 40.000/ano (conservador: 2 ideias/ano com ganho médio R$20k) |
| **Economia total estimada** | **R$ 85.000/ano** |
| **Investimento de referência** | R$ 100.000 |
| **Payback estimado** | **~14 meses** |
| **ROI ao final do 2º ano** | ~70% |

A contratação é classificada como **investimento de alta prioridade** pela Gestão de Inovação, com patrocínio da liderança executiva do Grupo.

---

## 3. OBJETIVO DA CONTRATAÇÃO

### 3.1 Objetivo

Contratar fornecedor para **desenvolver, implantar e homologar uma plataforma web proprietária de gestão de ideias e inovação**, cobrindo os módulos M1 a M6 definidos na Especificação de Requisitos Funcionais (ERF — DEM-2026-006), integrada ao SSO corporativo do Grupo, e operacional em ambiente de produção até 07/12/2026.

### 3.2 Critério de Sucesso da Contratação

A contratação será considerada bem-sucedida quando **todos** os critérios abaixo forem atendidos simultaneamente:

| # | Critério de Sucesso | Verificação |
|---|---|---|
| CS-01 | Todos os módulos M1 a M6 entregues, homologados e aceitos formalmente pelo GP | Ata de aceite assinada por cada marco |
| CS-02 | UAT concluído com taxa de defeitos críticos abertos igual a zero | Relatório de UAT aprovado pelo GP |
| CS-03 | Tempo de resposta ≤ 3s para 95% das requisições com 200 usuários simultâneos | Relatório de teste de carga aprovado |
| CS-04 | Disponibilidade ≥ 99,5% em horário comercial aferida no primeiro mês de produção | Relatório de uptime aprovado |
| CS-05 | SSO corporativo (SAML 2.0 ou OAuth 2.0) funcional em produção | Evidência de login via SSO aprovada |
| CS-06 | Go-live em produção aprovado até 07/12/2026 | Aceite formal de go-live assinado |
| CS-07 | Documentação técnica e manual do usuário entregues e aprovados | Aceite formal de documentação |

---

## 4. ESCOPO INCLUSO

### 4.1 Requisitos Funcionais Must Have — Módulos M1 a M6

| Módulo | ID RF | Requisito Funcional | Critério de Aceite Mínimo |
|---|---|---|---|
| **M1 — Cadastro de Ideias** | RF-01 | Portal web para colaboradores submeterem ideias com campos: problema que resolve, ganhos esperados, benefícios, responsável, área e atributos complementares | Formulário de submissão funcional com todos os campos obrigatórios validados |
| **M1 — Cadastro de Ideias** | RF-02 | Suporte a rascunhos antes da submissão formal | Ideia salva como rascunho não aparece no pipeline de aprovação |
| **M1 — Cadastro de Ideias** | RF-03 | Submissão de ideias avulsas e vinculadas a campanhas | Fluxo bifurcado conforme origem da ideia (avulsa x campanha) |
| **M2 — Campanhas e Desafios** | RF-04 | Módulo para criação de campanhas com prazo, descrição e objetivo pelo time de inovação | CRUD de campanha funcional com controle de acesso por perfil |
| **M2 — Campanhas e Desafios** | RF-05 | Encerramento automático de campanha por data ou manual pelo gestor | Campanha encerrada não aceita novas submissões |
| **M2 — Campanhas e Desafios** | RF-06 | Diferenciação visual entre ideias avulsas e ideias de campanha | Distinção visual clara na interface (etiqueta, cor ou ícone) |
| **M3 — Fluxo de Aprovação** | RF-07 | Workflow de aprovação em duas dimensões: (a) viabilidade pelo gestor da área; (b) aprovação do investimento necessário | Ambas as aprovações obrigatórias para ideia avançar no pipeline |
| **M3 — Fluxo de Aprovação** | RF-08 | Aprovação paralela por múltiplos aprovadores quando aplicável | Notificação enviada a todos aprovadores simultaneamente; qualquer um pode aprovar ou rejeitar |
| **M3 — Fluxo de Aprovação** | RF-09 | Histórico imutável de aprovações (aprovador, data, hora, decisão, motivo) | Histórico auditável e não editável após registro |
| **M3 — Fluxo de Aprovação** | RF-10 | Rejeição com motivo obrigatório e comunicação ao autor | Campo de motivo de rejeição obrigatório; autor notificado automaticamente |
| **M4 — Mini Gestão de Projetos** | RF-11 | Plano de ação para ideias aprovadas: tarefas com responsável e prazo | Criação de tarefas vinculadas à ideia aprovada, com responsável e data-limite |
| **M4 — Mini Gestão de Projetos** | RF-12 | Atualização de status e progresso percentual da ideia | Campo de percentual de conclusão editável pelo responsável |
| **M4 — Mini Gestão de Projetos** | RF-13 | Comentários e atualizações da equipe por ideia | Thread de comentários por ideia com registro de autor e timestamp |
| **M5 — Mensuração de Ganhos** | RF-14 | Registro de ganhos realizados versus ganhos prometidos por ideia | Campos de ganho prometido (no cadastro) e ganho realizado (após implementação) |
| **M5 — Mensuração de Ganhos** | RF-15 | Métricas agregadas do programa de inovação | Dashboard com totais: ideias submetidas, aprovadas, implementadas, ganho total |
| **M5 — Mensuração de Ganhos** | RF-16 | Histórico de ganhos por ideia e por período | Filtro de período aplicado às métricas de ganhos |
| **M6 — Dashboard e Monitoramento** | RF-17 | Visões diferenciadas por perfil: colaborador, gestor de área, gestor de inovação, admin | Cada perfil enxerga apenas o conjunto de dados e ações pertinentes ao seu papel |
| **M6 — Dashboard e Monitoramento** | RF-18 | Filtros por status, campanha, área e período | Filtros combinados funcionais sem degradação de performance |
| **M6 — Dashboard e Monitoramento** | RF-19 | Exportação de dados | Exportação em formato CSV ou XLSX das listagens principais |

### 4.2 Requisitos Não-Funcionais Must Have

| ID RNF | Requisito | Critério de Aceite |
|---|---|---|
| RNF-01 | Tempo de resposta ≤ 3s para 95% das requisições com até 200 usuários simultâneos | Relatório de teste de carga aprovado pelo GP com evidências |
| RNF-02 | Autenticação via SSO corporativo (SAML 2.0 ou OAuth 2.0) | Login via SSO funcional em ambiente de produção |
| RNF-03 | Disponibilidade ≥ 99,5% em horário comercial (07h–20h, seg–sex) | SLA verificado em relatório de uptime do primeiro mês de produção |
| RNF-04 | Interface responsiva (desktop e mobile web) | Funcional e usável em resolução mínima de 375px (mobile web) e 1280px (desktop) |
| RNF-05 | Dados de usuários e ideias criptografados em repouso (AES-256) | Evidência técnica de configuração de criptografia em repouso |

---

## 5. ESCOPO EXCLUSO

O fornecedor **não deve** incluir, orçar ou propor os itens abaixo. Qualquer entrega nestes itens requer aditivo de escopo formalizado e aprovado pelo GP antes da execução.

| # | Item Excluso | Justificativa |
|---|---|---|
| EX-01 | Integrações com sistemas externos (SAP, ERP, RH, financeiro) | Fora do escopo da versão 1. Integrações serão avaliadas em projeto separado após estabilização da plataforma. |
| EX-02 | Aplicativo mobile nativo (iOS e/ou Android) | A interface web responsiva (RNF-04) é suficiente para as necessidades da versão 1. App nativo implica custo e prazo incompatíveis com o envelope atual. |
| EX-03 | Funcionalidades de gamificação ou ranking público de inovadores | Fora do escopo da versão 1 por decisão do Gestor de Inovação. O impacto cultural desse tipo de funcionalidade requer análise separada antes da implementação. |
| EX-04 | Sustentação e manutenção evolutiva pós-garantia | Constitui escopo de contrato separado a ser negociado após o go-live. O presente WR cobre apenas desenvolvimento, implantação e período de garantia de 90 dias. |
| EX-05 | Migração de dados históricos da plataforma ou processos anteriores | Responsabilidade da equipe interna do Grupo com suporte pontual do fornecedor. O suporte do fornecedor neste item limita-se a orientação técnica sobre formato de importação — sem execução da migração. |
| EX-06 | Infraestrutura de hospedagem (servidores, cloud, CDN) | O Grupo provê o ambiente de infraestrutura. O fornecedor deve entregar a aplicação pronta para implantação no ambiente fornecido pelo Grupo. |

---

## 6. PREMISSAS E RESPONSABILIDADES DO GRUPO

### 6.1 Premissas do Projeto

O Work Request é emitido com base nas seguintes premissas. A quebra de qualquer premissa deve ser comunicada imediatamente ao GP para avaliação de impacto em prazo e custo.

| # | Premissa |
|---|---|
| P-01 | O ambiente de homologação estará disponível ao fornecedor em até 5 dias úteis após o kick-off (M0). |
| P-02 | O ambiente de produção estará disponível ao fornecedor em até 5 dias úteis antes do go-live (M6). |
| P-03 | O Grupo disponibilizará ponto focal técnico dedicado com latência de resposta máxima de 1 dia útil para dúvidas e decisões técnicas. |
| P-04 | A aprovação formal de entregas intermediárias pelo Grupo ocorrerá em até 5 dias úteis após o recebimento do entregável. |
| P-05 | As credenciais e documentação do SSO corporativo (SAML 2.0 ou OAuth 2.0) serão disponibilizadas ao fornecedor até 5 dias úteis após o kick-off. |
| P-06 | O Grupo disponibilizará base de usuários anonimizada e ideias mockadas para uso em testes. |
| P-07 | A definição dos campos customizados do formulário de cadastro de ideia será finalizada e entregue ao fornecedor até o final do M1 (31/07/2026). |

### 6.2 Responsabilidades do Grupo (Contratante)

| # | Responsabilidade | Prazo |
|---|---|---|
| R-01 | Fornecer acesso ao ambiente de homologação com perfis adequados | Até 5 dias úteis após kick-off |
| R-02 | Fornecer acesso ao ambiente de produção com perfis adequados | Até 5 dias úteis antes do go-live |
| R-03 | Disponibilizar ponto focal técnico dedicado (identificado nominalmente até o kick-off) | Durante todo o projeto |
| R-04 | Aprovar formalmente entregas intermediárias em até 5 dias úteis | Em cada marco de entrega |
| R-05 | Fornecer dados de teste (usuários anonimizados, ideias mockadas) | Até 5 dias úteis após kick-off |
| R-06 | Fornecer credenciais e documentação do SSO corporativo | Até 5 dias úteis após kick-off |
| R-07 | Definir e entregar lista final de campos customizados do formulário | Até 31/07/2026 (M1) |
| R-08 | Mobilizar equipe interna para participação no UAT | Até 20/11/2026 (M5) |
| R-09 | Executar a migração de dados históricos com orientação técnica do fornecedor | Responsabilidade exclusiva do Grupo |

---

## 7. CRONOGRAMA ESPERADO

O fornecedor deve apresentar proposta de cronograma compatível com as datas abaixo. Desvios superiores a 5 dias úteis em qualquer marco devem ser justificados na proposta.

| Marco | Descrição | Data Esperada | Critério de Aceite |
|---|---|---|---|
| **M0** | Kick-off e mobilização da equipe | 24/06/2026 | Ata de kick-off assinada por ambas as partes; equipe do fornecedor formalmente apresentada; plano de projeto detalhado entregue |
| **M1** | Especificação funcional e técnica aprovada | 31/07/2026 | Documento de especificação funcional e técnica (casos de uso, modelo de dados, arquitetura) aprovado formalmente pelo GP com aceite escrito |
| **M2** | Módulos M1 (Cadastro de Ideias) e M2 (Campanhas) entregues e aprovados em homologação | 04/09/2026 | RF-01 a RF-06 funcionais e aprovados em ambiente de homologação; relatório de testes unitários e integração aprovado pelo GP |
| **M3** | Módulos M3 (Fluxo de Aprovação) e M4 (Mini Gestão de Projetos) entregues e aprovados em homologação | 09/10/2026 | RF-07 a RF-13 funcionais e aprovados em homologação; histórico de aprovações auditável verificado; relatório de testes aprovado |
| **M4** | Módulos M5 (Mensuração de Ganhos) e M6 (Dashboard) entregues e aprovados em homologação | 13/11/2026 | RF-14 a RF-19 funcionais e aprovados em homologação; RNF-01 a RNF-05 verificados; relatório de teste de carga aprovado |
| **M5** | UAT (User Acceptance Testing) concluído e aprovado | 20/11/2026 | Relatório de UAT com zero defeitos críticos abertos, aprovado formalmente pelo Gestor de Inovação e GP |
| **M6** | Go-live em ambiente de produção aprovado | 07/12/2026 | Plataforma operacional em produção com SSO ativo; aceite formal de go-live assinado pelo GP e sponsor |
| **M7** | Encerramento do projeto e repasse para sustentação | 31/12/2026 | Documentação técnica e manual do usuário aprovados; período de garantia formalmente iniciado; ata de encerramento assinada |

**Prazo máximo de mobilização:** 5 dias úteis após assinatura do contrato.

---

## 8. ENTREGÁVEIS OBRIGATÓRIOS

O fornecedor deve entregar **todos** os artefatos abaixo. A ausência de qualquer entregável implica bloqueio do pagamento do marco correspondente.

| # | Entregável | Marco de Pagamento | Critério de Aceite |
|---|---|---|---|
| E-01 | Plano de projeto detalhado (cronograma, equipe, riscos, comunicação) | M0 | Documento aprovado pelo GP com ata de kick-off |
| E-02 | Documento de especificação funcional e técnica (casos de uso, modelo de dados, arquitetura de solução, diagramas) | M1 | Aprovação formal escrita do GP em até 5 dias úteis após entrega |
| E-03 | Protótipo navegável de baixa/média fidelidade (UX/UI) aprovado | M1 | Aceite escrito do Gestor de Inovação |
| E-04 | Código-fonte dos Módulos M1 e M2 com testes unitários e integração | M2 (Marco de pagamento 2) | Pull request revisado e aprovado; cobertura de testes ≥ 70%; relatório de testes aprovado |
| E-05 | Código-fonte dos Módulos M3 e M4 com testes unitários e integração | M3 (Marco de pagamento 3) | Pull request revisado e aprovado; cobertura de testes ≥ 70%; relatório de testes aprovado |
| E-06 | Código-fonte dos Módulos M5 e M6 com testes unitários e integração | M4 (Marco de pagamento 4) | Pull request revisado e aprovado; cobertura de testes ≥ 70%; relatório de teste de carga aprovado (RNF-01) |
| E-07 | Relatório de UAT com evidências de testes e log de defeitos resolvidos | M5 (Marco de pagamento 5) | Zero defeitos críticos abertos; aprovado pelo Gestor de Inovação e GP |
| E-08 | Plataforma implantada e funcional em ambiente de produção | M6 (Marco de pagamento 6) | Aceite formal de go-live pelo GP e sponsor; SSO funcional verificado |
| E-09 | Documentação técnica completa (arquitetura, APIs, configuração de ambiente, runbook operacional) | M7 (Marco de pagamento 7) | Aprovada pelo ponto focal técnico do Grupo |
| E-10 | Manual do usuário (por perfil: colaborador, gestor de área, gestor de inovação, admin) | M7 (Marco de pagamento 7) | Aprovado pelo Gestor de Inovação |
| E-11 | Treinamento da equipe interna (mínimo 2 sessões: usuários-chave e administradores) | M7 (Marco de pagamento 7) | Lista de presença e avaliação de reação aprovadas pelo GP |
| E-12 | Código-fonte completo entregue em repositório Git sob controle do Grupo | M7 (Marco de pagamento 7) | Repositório acessível pelo Grupo com histórico completo de commits |

---

## 9. GOVERNANÇA E COMUNICAÇÃO

### 9.1 Estrutura de Governança

| Papel | Responsabilidade | Organização |
|---|---|---|
| **Sponsor** | Aprovação final de investimento e escalada executiva | Grupo |
| **Gestor de Inovação (Solicitante)** | Validação de requisitos funcionais; aceite do UAT e manuais | Grupo |
| **Ponto Focal Técnico** | Decisões técnicas; acesso a ambientes; validação de arquitetura | Grupo |
| **Gerente de Projeto (GP)** | Gestão do contrato, cronograma, riscos e aceites formais | VMO Consultoria |
| **Líder Técnico do Fornecedor** | Entrega técnica; qualidade do código; arquitetura da solução | Fornecedor |
| **Gerente de Conta do Fornecedor** | Comunicação comercial; escalada interna; SLA de garantia | Fornecedor |

### 9.2 Rituais de Comunicação

| Ritual | Frequência | Participantes | Formato |
|---|---|---|---|
| Status Report semanal | Semanal (toda sexta-feira) | GP, Fornecedor | Relatório escrito via e-mail (template fornecido pelo GP) |
| Reunião de acompanhamento | Quinzenal | GP, Ponto Focal Técnico, Líder Técnico do Fornecedor | Videoconferência — pauta e ata obrigatórias |
| Reunião de aceite de marco | A cada marco | GP, Gestor de Inovação, Fornecedor | Presencial ou videoconferência — ata de aceite assinada |
| Reunião de escalada | Sob demanda | Sponsor, GP, Fornecedor | Convocada pelo GP com antecedência mínima de 24h |

### 9.3 Canal Oficial de Comunicação

- **Canal primário:** e-mail corporativo com GP (endereço a ser informado no contrato)
- **Documentação:** repositório compartilhado fornecido pelo GP (pasta de projeto)
- **Urgências:** WhatsApp Business do GP (para comunicação de incidentes críticos apenas)
- **Aceites formais:** exclusivamente por e-mail com confirmação de leitura ou assinatura digital

---

## 10. CONDIÇÕES COMERCIAIS

### 10.1 Modelo de Faturamento por Marcos

O faturamento é **exclusivamente por marcos de entrega aprovados**. O fornecedor **não deve** apresentar proposta baseada em horas, mensalidades, adiantamentos ou qualquer outro modelo diferente de marcos. Propostas com modelo de faturamento diferente de marcos serão **desclassificadas**.

| Marco de Pagamento | Entregáveis Vinculados | % Máximo do Valor Total |
|---|---|---|
| Pagamento 1 — Marco M0 (Kick-off) | E-01 | 10% |
| Pagamento 2 — Marco M1 (Especificação aprovada) | E-02, E-03 | 15% |
| Pagamento 3 — Marco M2 (M1+M2 em homologação) | E-04 | 15% |
| Pagamento 4 — Marco M3 (M3+M4 em homologação) | E-05 | 20% |
| Pagamento 5 — Marco M4 (M5+M6 em homologação) | E-06 | 15% |
| Pagamento 6 — Marco M5 (UAT aprovado) | E-07 | 10% |
| Pagamento 7 — Marco M6 (Go-live aprovado) | E-08 | 10% |
| Pagamento 8 — Marco M7 (Encerramento) | E-09, E-10, E-11, E-12 | 5% |
| **Total** | | **100%** |

> O fornecedor pode propor distribuição diferente da sugerida acima, desde que nenhum marco individual ultrapasse 25% do valor total e o primeiro pagamento (kick-off) não ultrapasse 10%.

### 10.2 Condições de Pagamento

- Pagamento em até **30 dias úteis** após aceite formal do marco pelo GP, com nota fiscal correspondente emitida
- O aceite formal é formalizado por ata assinada ou e-mail de aceite pelo GP
- Nota fiscal deve ser emitida somente após aceite formal — notas emitidas antes do aceite não iniciam o prazo de pagamento

### 10.3 Envelope de Investimento

- Envelope de referência: **R$ 100.000,00** (inclui contingência de 20%)
- Propostas dentro do envelope: avaliadas normalmente
- Propostas acima do envelope: consideradas apenas se acompanhadas de justificativa técnica detalhada e análise de benefício incremental. O GP reserva-se o direito de desclassificar propostas acima do envelope sem análise adicional
- Propostas com redução de escopo para caber no envelope: **não serão aceitas** — o escopo M1-M6 e todos os RNFs Must Have são inegociáveis

### 10.4 Penalidades por Atraso

- **Penalidade:** 2% do valor do marco por semana de atraso (ou fração de semana)
- **Teto:** limitada a 10% do valor total do contrato
- Atraso causado por omissão do Grupo (ex.: aprovação fora do prazo de 5 dias úteis) **não gera penalidade** ao fornecedor — o prazo é suspenso pelo período da omissão do contratante
- Atrasos superiores a 3 semanas em qualquer marco habilitam o Grupo a rescindir o contrato sem ônus, retendo os valores já pagos pelos marcos entregues e aceitos

### 10.5 Garantia e SLA Pós-Go-Live

- **Período de garantia:** 90 dias corridos após aceite formal do go-live (M6)
- Correção de defeitos identificados na garantia: **sem custo adicional**

| Severidade do Defeito | SLA de Atendimento | SLA de Resolução |
|---|---|---|
| **CRÍTICO** (plataforma indisponível ou perda de dados) | ≤ 1h | ≤ 8h |
| **ALTO** (funcionalidade principal comprometida, sem workaround) | ≤ 4h | ≤ 24h |
| **MÉDIO** (funcionalidade degradada, workaround disponível) | ≤ 8h | ≤ 5 dias úteis |
| **BAIXO** (cosmético, sem impacto funcional) | ≤ 1 dia útil | A combinar com GP |

- Descumprimento de SLA de garantia: 1% do valor total do contrato por ocorrência, limitado a 5% acumulado

---

## 11. ARTEFATO OBRIGATÓRIO — CHECKLIST DE CONFORMIDADE DA PROPOSTA

**Este artefato é de preenchimento obrigatório pelo fornecedor.** A proposta que não inclua este checklist preenchido em sua totalidade será **automaticamente desclassificada**, independentemente de seu mérito técnico ou comercial.

O fornecedor deve preencher as colunas OK, NOK e Observações para cada item. A coluna OK/NOK deve conter exclusivamente os valores **OK** ou **NOK**. Observações são obrigatórias para todos os itens marcados como NOK e facultativas para itens OK.

---

### GRUPO 1 — IDENTIFICAÇÃO DA PROPOSTA (6 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 1.1 | A proposta identifica o fornecedor com razão social, CNPJ, endereço, telefone e e-mail de contato | | |
| 1.2 | A proposta identifica o responsável legal da empresa (nome, cargo, CPF ou RG) com poderes para assinar contrato | | |
| 1.3 | A proposta referencia explicitamente o código WR-2026-006 e o código do projeto PROJ-2026-006 | | |
| 1.4 | A proposta declara validade mínima de 30 dias corridos a partir da data de submissão | | |
| 1.5 | A proposta declara o valor total global em reais (R$), discriminado por marco de pagamento | | |
| 1.6 | A proposta é assinada pelo responsável legal ou procurador com poderes comprovados | | |

---

### GRUPO 2 — ESCOPO DETALHADO DA ENTREGA (6 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 2.1 | A proposta confirma o atendimento integral aos requisitos funcionais RF-01 a RF-19 (Módulos M1 a M6) | | |
| 2.2 | A proposta confirma o atendimento integral aos requisitos não-funcionais RNF-01 a RNF-05 | | |
| 2.3 | A proposta descreve a arquitetura técnica da solução proposta (stack tecnológico, modelo de implantação, integrações internas previstas) | | |
| 2.4 | A proposta descreve como será implementado o SSO corporativo (SAML 2.0 ou OAuth 2.0) e quais informações são necessárias do Grupo para a integração | | |
| 2.5 | A proposta descreve a estratégia de testes (unitários, integração, carga e UAT) com critérios de cobertura | | |
| 2.6 | A proposta descreve a estratégia de implantação em produção (rollout, rollback, janela de manutenção) | | |

---

### GRUPO 3 — EXCLUSÕES DE ESCOPO (2 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 3.1 | A proposta declara explicitamente que não inclui integrações com sistemas externos (SAP, ERP, RH), aplicativo mobile nativo, gamificação/ranking e migração de dados históricos | | |
| 3.2 | A proposta declara explicitamente que sustentação e manutenção evolutiva pós-garantia não estão incluídas neste escopo e constituirão contrato separado | | |

---

### GRUPO 4 — PREMISSAS (3 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 4.1 | A proposta declara as premissas assumidas pelo fornecedor e confirma ciência das premissas listadas na Seção 6 deste WR | | |
| 4.2 | A proposta declara que o prazo proposto pressupõe a disponibilização dos ambientes de homologação e produção nas datas previstas pelo Grupo | | |
| 4.3 | A proposta declara que o prazo proposto pressupõe a latência máxima de 1 dia útil do ponto focal técnico do Grupo para resposta a dúvidas técnicas | | |

---

### GRUPO 5 — METODOLOGIA E ABORDAGEM (3 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 5.1 | A proposta descreve a metodologia de desenvolvimento adotada (ex.: Scrum, Kanban, híbrido) com justificativa de adequação ao projeto | | |
| 5.2 | A proposta descreve o processo de gestão de mudanças de escopo (change request), incluindo como impactos em prazo e custo serão comunicados e aprovados | | |
| 5.3 | A proposta descreve o processo de controle de qualidade e como defeitos identificados em homologação serão rastreados e resolvidos | | |

---

### GRUPO 6 — ENTREGÁVEIS (9 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 6.1 | A proposta confirma a entrega do Plano de Projeto detalhado (E-01) no marco M0 | | |
| 6.2 | A proposta confirma a entrega do Documento de Especificação Funcional e Técnica (E-02) e Protótipo navegável (E-03) no marco M1 | | |
| 6.3 | A proposta confirma a entrega do código-fonte de M1 e M2 com testes (E-04) no marco M2 | | |
| 6.4 | A proposta confirma a entrega do código-fonte de M3 e M4 com testes (E-05) no marco M3 | | |
| 6.5 | A proposta confirma a entrega do código-fonte de M5 e M6 com testes e relatório de carga (E-06) no marco M4 | | |
| 6.6 | A proposta confirma a entrega do Relatório de UAT com zero defeitos críticos abertos (E-07) no marco M5 | | |
| 6.7 | A proposta confirma a entrega da plataforma implantada em produção com SSO funcional (E-08) no marco M6 | | |
| 6.8 | A proposta confirma a entrega da documentação técnica completa e manuais do usuário por perfil (E-09 e E-10) no marco M7 | | |
| 6.9 | A proposta confirma a entrega do treinamento (mínimo 2 sessões) e do código-fonte completo em repositório Git (E-11 e E-12) no marco M7 | | |

---

### GRUPO 7 — GOVERNANÇA E GESTÃO (3 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 7.1 | A proposta nomeia o Gerente de Projeto do fornecedor (nome, e-mail, telefone) que será o interlocutor oficial com o GP da VMO Consultoria | | |
| 7.2 | A proposta nomeia o Líder Técnico (nome, e-mail, telefone) responsável pela arquitetura e qualidade da entrega | | |
| 7.3 | A proposta confirma disponibilidade para participação nos rituais de comunicação definidos na Seção 9 deste WR (status report semanal, reunião quinzenal, reunião de aceite por marco) | | |

---

### GRUPO 8 — PRAZO, CRONOGRAMA E EQUIPE (5 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 8.1 | A proposta apresenta cronograma detalhado compatível com os 8 marcos definidos na Seção 7, com datas específicas para cada entregável | | |
| 8.2 | A proposta confirma capacidade de mobilização em até 5 dias úteis após assinatura do contrato | | |
| 8.3 | A proposta apresenta a composição nominal da equipe designada para o projeto (nome, papel, dedicação percentual, experiência relevante) | | |
| 8.4 | A proposta apresenta currículos ou perfis (LinkedIn) dos membros sênior da equipe (Líder Técnico e demais sêniors) | | |
| 8.5 | A proposta apresenta ao menos 2 cases de projetos similares (desenvolvimento de plataformas web SaaS) entregues nos últimos 3 anos, com contato de referência | | |

---

### GRUPO 9 — CONDIÇÕES COMERCIAIS E FINANCEIRAS (4 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 9.1 | A proposta apresenta valor total global em reais (R$) com discriminação por marco de pagamento, em conformidade com o modelo de faturamento por marcos definido na Seção 10 | | |
| 9.2 | O valor total da proposta está dentro do envelope de investimento de referência de R$ 100.000,00 — OU a proposta superior ao envelope é acompanhada de justificativa técnica detalhada e análise de benefício incremental | | |
| 9.3 | A proposta confirma aceitação do prazo de pagamento de 30 dias úteis após aceite formal do marco | | |
| 9.4 | A proposta não inclui cobrança por horas extras, adicionais não previstos ou taxa de mobilização além dos marcos definidos | | |

---

### GRUPO 10 — PENALIDADES, GARANTIA E SUSTENTAÇÃO (4 itens)

| # | Item | OK / NOK | Observações |
|---|---|---|---|
| 10.1 | A proposta confirma aceite da penalidade de 2% do valor do marco por semana de atraso, limitada a 10% do valor total do contrato | | |
| 10.2 | A proposta confirma garantia de 90 dias corridos após aceite do go-live, com correção de defeitos sem custo adicional | | |
| 10.3 | A proposta confirma os SLAs de garantia: CRÍTICO ≤ 8h resolução, ALTO ≤ 24h, MÉDIO ≤ 5 dias úteis | | |
| 10.4 | A proposta declara que sustentação e manutenção evolutiva pós-garantia não estão incluídas neste escopo e que o fornecedor tem interesse/disponibilidade para negociar contrato separado de sustentação após o go-live | | |

---

## 12. PROCESSO DE SUBMISSÃO DE PROPOSTAS

### 12.1 Prazo Final

**Data limite de submissão:** 06/06/2026 (sábado) às 23h59 (horário de Brasília)

Propostas recebidas após esse prazo serão **automaticamente desclassificadas**, independentemente do motivo do atraso.

### 12.2 Canal de Submissão

- **E-mail exclusivo para propostas:** propostas-wr2026006@vmoconsultoria.com.br
- O assunto do e-mail deve ser exatamente: `[PROPOSTA] WR-2026-006 — [Razão Social do Fornecedor]`
- Confirmação de recebimento: o GP enviará confirmação em até 1 dia útil. Caso não receba confirmação, o fornecedor deve contatar o GP imediatamente pelo e-mail de contato abaixo

### 12.3 Formato Obrigatório

A proposta deve ser submetida em um único arquivo PDF, organizado na seguinte ordem:

1. Carta de apresentação (máximo 1 página) com declaração de conformidade com o WR
2. Proposta técnica (seções correspondentes aos Grupos 2 a 8 do Artefato Obrigatório)
3. Proposta comercial (seções correspondentes aos Grupos 9 e 10 do Artefato Obrigatório)
4. **Artefato Obrigatório completo** (todos os 10 grupos e 41 itens preenchidos com OK/NOK/Observações)
5. Currículos/perfis da equipe (como anexo separado em PDF)
6. Cases e referências (como anexo separado em PDF)

### 12.4 Critérios de Desclassificação Automática

A proposta será desclassificada automaticamente, sem análise de mérito, se qualquer das condições abaixo for verificada:

| # | Condição de Desclassificação |
|---|---|
| DC-01 | Submissão fora do prazo (após 06/06/2026 às 23h59) |
| DC-02 | Artefato Obrigatório (Seção 11) ausente ou com qualquer dos 10 grupos incompleto |
| DC-03 | Modelo de faturamento diferente de marcos (ex.: por horas, mensalidades, adiantamento) |
| DC-04 | Escopo incluso sem confirmação explícita de atendimento aos módulos M1 a M6 |
| DC-05 | Proposta não assinada pelo responsável legal ou procurador com poderes |
| DC-06 | Validade da proposta inferior a 30 dias corridos |

### 12.5 Contatos

| Papel | Nome | E-mail | Telefone |
|---|---|---|---|
| Gerente de Projeto | A ser preenchido após identificação do sponsor | — | — |
| Gestor de Inovação (dúvidas de escopo funcional) | Jadson | jadson@grupo.com.br | A confirmar |
| Canal de propostas | — | propostas-wr2026006@vmoconsultoria.com.br | — |

> Dúvidas sobre o escopo ou processo de submissão devem ser enviadas **exclusivamente por e-mail** até **30/05/2026 às 18h00**. Respostas serão consolidadas e enviadas a todos os fornecedores convidados simultaneamente, garantindo isonomia no processo seletivo.

### 12.6 Cronograma do Processo Seletivo

| Etapa | Data |
|---|---|
| Emissão do WR e convite aos fornecedores | 16/05/2026 |
| Prazo para envio de dúvidas | 30/05/2026 às 18h00 |
| Respostas consolidadas a todos os fornecedores | 03/06/2026 |
| Prazo final de submissão de propostas | **06/06/2026 às 23h59** |
| Análise técnica e comercial das propostas | 09/06 a 16/06/2026 |
| Comunicação do resultado e negociação final | 18/06/2026 |
| Assinatura de contrato | Até 20/06/2026 |
| Kick-off | 24/06/2026 |

---

*WR emitido por Fábio Fornecedor — Especialista em Solicitação de Trabalho*
*VMO Consultoria — Gestão de Projetos e Inovação*
*Data de emissão: 16/05/2026*
*Versão: 1.0*
