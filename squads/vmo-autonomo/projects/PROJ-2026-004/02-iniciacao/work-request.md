# WORK REQUEST — PROJ-2026-004
## Plataforma Interna de Gestão de Ideias de Inovação

**Versão:** 1.0 | **Data de Emissão:** 2026-05-18 | **Elaborado por:** VMO Consultoria — Fábio Fornecedor
**Validade deste WR:** 60 dias a partir da data de emissão

---

## 1. Identificação do Projeto

| Campo | Informação |
|---|---|
| Código do Projeto | PROJ-2026-004 |
| Nome do Projeto | Plataforma Interna de Gestão de Ideias de Inovação |
| Cliente | Grupo Águia Branca (holding + VixPar + VAB + divisões) |
| Solicitante | Jadson — Área de Inovação, Grupo Águia Branca |
| Sponsor | A DEFINIR (condição registrada no TAP — pendência a ser regularizada antes da assinatura contratual) |
| Gestão do Projeto | VMO Consultoria |
| Tipo de Solução | Desenvolvimento web sob medida (plataforma proprietária) |
| Usuários Alvo | 10.000+ colaboradores do grupo (holding, VixPar, VAB e demais divisões) |
| Prazo Limite de Entrega | 30/11/2026 |
| Orçamento Total Aprovado | R$ 90.000,00 |
| Data de Emissão deste WR | 2026-05-18 |
| Validade da Proposta | 60 dias a partir de 2026-05-18 |

---

## 2. Contexto e Justificativa

O Grupo Águia Branca, conglomerado com atuação em transporte de passageiros, logística e demais divisões de negócio, possui uma base de mais de 10.000 colaboradores distribuídos entre a holding e suas empresas coligadas (VixPar, VAB e outras). A Área de Inovação do grupo, liderada pelo solicitante Jadson, identificou a necessidade de estruturar um canal formal e escalável para captura, avaliação e acompanhamento de ideias geradas pelos próprios colaboradores.

Atualmente, o processo de gestão de ideias carece de uma plataforma proprietária que una: (a) o registro estruturado de oportunidades de melhoria, (b) o fluxo de aprovação hierárquico, (c) o acompanhamento de projetos derivados e (d) a mensuração dos ganhos efetivos obtidos. Soluções SaaS de mercado como Exago, Qmarkets e Brightidea custam entre R$ 50.000 e R$ 150.000 por ano em licenciamento, sem contar customizações, e não oferecem a flexibilidade de integração futura com os sistemas legados do grupo nem o controle total sobre os dados corporativos.

A construção de uma plataforma proprietária representa um investimento de R$ 90.000 com retorno sobre investimento potencial já no primeiro ano, tanto pela economia em licenças quanto pela geração de valor a partir das ideias implementadas. O prazo de 30/11/2026 está alinhado ao ciclo de planejamento estratégico do grupo para 2027, permitindo que a plataforma esteja operacional antes do início do próximo exercício.

---

## 3. Objetivo da Contratação

Contratar empresa especializada em desenvolvimento web para projetar, construir, testar, implantar e documentar uma **Plataforma Interna de Gestão de Ideias de Inovação** de uso exclusivo do Grupo Águia Branca, contemplando:

- Portal web responsivo acessível a todos os 10.000+ colaboradores do grupo, sem limitação de licença por usuário;
- Fluxo completo de ciclo de vida de uma ideia: cadastro → avaliação pelo gestor → aprovação → acompanhamento como projeto → registro de ganhos;
- Módulo de campanhas e desafios de inovação administrável pelo time de inovação;
- Controle de acesso granular por papéis (colaborador, gestor, time de inovação, administrador);
- Entrega dentro do prazo de 30/11/2026 e do orçamento de R$ 90.000,00;
- Propriedade intelectual total transferida ao Grupo Águia Branca ao final do contrato.

---

## 4. Escopo da Contratação

### 4.1 Escopo Incluso

Abaixo estão listados os Requisitos Funcionais (RF) de caráter **Must Have** que compõem obrigatoriamente o escopo desta contratação. A proposta do fornecedor deve endereçar todos os itens sem exceção.

| ID | Requisito Funcional | Descrição |
|---|---|---|
| RF001 | Cadastro de usuário | Cadastro por convite (link tokenizado enviado por e-mail) ou auto-registro com validação de domínio de e-mail corporativo (@grupoaguiabranca.com.br e domínios afiliados das divisões). |
| RF002 | Login e autenticação segura | Autenticação com credenciais locais (e-mail + senha com política de complexidade) e suporte a MFA (autenticação multifator) como camada opcional. Sessões com timeout configurável. |
| RF003 | Portal web responsivo de cadastro de ideias | Interface acessível em desktop e dispositivos móveis via browser. Formulário estruturado contemplando: descrição do problema identificado, ganhos esperados (financeiros, operacionais, estratégicos) e benefícios qualitativos. Possibilidade de anexar arquivos de suporte (imagens, planilhas, apresentações). |
| RF004 | Módulo de campanhas e desafios de inovação | Painel administrativo para o time de inovação criar, publicar, encerrar e arquivar campanhas temáticas ou desafios com prazo definido. Ideias podem ser associadas a uma campanha vigente ou submetidas de forma livre. |
| RF005 | Fluxo de aprovação de ideias | Workflow de aprovação pelo gestor direto do colaborador proponente. Estados mínimos: Rascunho → Submetida → Em Análise → Aprovada / Reprovada / Devolvida para Revisão. Notificações automáticas por e-mail a cada mudança de estado. |
| RF006 | Módulo de mini gestão de projetos | Para ideias aprovadas: criação de projeto vinculado à ideia de origem, com campos de responsável, equipe, prazo previsto, marcos, percentual de avanço e status. Visão Kanban ou lista configurável. |
| RF007 | Módulo de mensuração e registro de ganhos | Registro estruturado dos ganhos efetivamente obtidos após a implementação: valor financeiro economizado ou gerado, tipo de ganho (custo, receita, qualidade, segurança, outros), data de apuração e evidências anexas. |
| RF008 | Gestão de perfis e controle de acesso por papel | Quatro papéis mínimos: (1) Colaborador — submete e acompanha suas próprias ideias; (2) Gestor — aprova/reprova ideias de sua equipe; (3) Time de Inovação — gerencia campanhas, visualiza todas as ideias, relatórios globais; (4) Administrador — gestão de usuários, papéis, configurações da plataforma. |
| RF009 | Capacidade para 10.000+ usuários sem limitação de licença | Arquitetura e licenciamento que suportem todos os colaboradores do grupo (holding + VixPar + VAB + divisões) sem custo adicional por usuário. Testes de carga devem validar o suporte a pelo menos 500 usuários simultâneos. |
| RF010 | Testes de aceitação com o time de inovação (UAT) | Ciclo formal de UAT com duração mínima de 2 semanas, conduzido pelo time de inovação em ambiente de homologação. Gestão de defeitos com rastreabilidade. Critério de conclusão: zero defeitos críticos em aberto. |
| RF011 | Documentação técnica e manual do usuário | Documentação técnica (arquitetura, stack, modelo de dados, APIs internas, instruções de deploy) e manual do usuário final por papel (colaborador, gestor, time de inovação, administrador), em português brasileiro. |
| RF012 | Implantação em ambiente de produção | Publicação da plataforma no ambiente de infraestrutura provido pelo TI do Grupo Águia Branca. Inclui configuração de variáveis de ambiente, scripts de migração de banco de dados e procedimento de rollback documentado. |
| RF013 | Treinamento do time de inovação e administradores | Sessão de treinamento presencial ou remota (mínimo 4 horas) para o time de inovação e administradores da plataforma. Inclui material de apoio (slides/vídeo gravado) entregue ao cliente. |

### 4.2 Escopo Excluso

Os itens abaixo estão **expressamente fora** do escopo desta contratação. Qualquer necessidade futura relacionada a estes itens deverá ser tratada como aditivo contratual ou novo projeto.

| # | Item Excluído | Justificativa |
|---|---|---|
| EX01 | Integração com sistemas legados (ERP, RH, folha de pagamento) | Escopo reservado para fase futura do projeto, após estabilização da plataforma e mapeamento detalhado das APIs dos sistemas legados. Incluir nesta fase aumentaria o risco técnico e o prazo além do limite de 30/11/2026. |
| EX02 | Aplicativo mobile nativo (iOS e Android) | Avaliação postergada para após a validação da plataforma web. A interface web responsiva (RF003) atende ao acesso via dispositivos móveis por browser. O desenvolvimento de apps nativos representa escopo e orçamento adicionais. |
| EX03 | Migração de dados históricos de plataforma terceirizada | A responsabilidade pela extração, curadoria e eventual migração de dados de eventuais plataformas anteriores é do time de inovação do Grupo Águia Branca. O fornecedor não possui acesso nem SLA sobre dados de terceiros. |
| EX04 | Suporte técnico pós-implantação além do período de garantia de 90 dias | O contrato contempla 90 dias de garantia após o go-live (correção de defeitos sem custo). Contratos de suporte e manutenção evolutiva após esse período deverão ser negociados separadamente. |
| EX05 | Hospedagem e infraestrutura de ambiente de produção | A contratação e operação dos servidores, banco de dados, CDN e certificados SSL em produção são de responsabilidade exclusiva da área de TI do Grupo Águia Branca, conforme premissa acordada. |

---

## 5. Premissas e Responsabilidades do Grupo

O Grupo Águia Branca compromete-se a providenciar os seguintes recursos e condições para viabilizar a execução do projeto dentro do prazo e orçamento estabelecidos. O não cumprimento de qualquer premissa abaixo poderá impactar o cronograma e deverá ser formalmente registrado como impedimento pelo Gestor do Projeto VMO.

| # | Premissa / Responsabilidade do Grupo | Prazo de Disponibilização |
|---|---|---|
| P01 | Infraestrutura de hospedagem e servidores em ambiente de produção, incluindo sistema operacional, banco de dados relacional e servidor de aplicação, provisionados e acessíveis ao fornecedor para implantação (RF012). | Até 4 semanas antes do prazo de implantação (até 31/10/2026) |
| P02 | Domínios de e-mail corporativo válidos e documentados para uso na autenticação: @grupoaguiabranca.com.br e todos os domínios afiliados das divisões do grupo. Lista formal entregue ao fornecedor no kick-off. | Até a data do kick-off |
| P03 | Designação formal de pontos focais do time de inovação para condução do UAT (RF010), com disponibilidade mínima de 20 horas/semana durante o período de testes. | Até 2 semanas antes do início do UAT |
| P04 | Disponibilização de ambiente de staging/homologação (com acesso ao fornecedor) para execução dos testes integrados e do UAT, equivalente ao ambiente de produção em configuração. | Até o início da fase de testes integrados |
| P05 | Treinamento de usuários finais (colaboradores e gestores operacionais) nas divisões do grupo — responsabilidade das próprias divisões, com material de apoio entregue pelo fornecedor (RF013). | Após o go-live, a cargo das divisões |
| P06 | Designação de um representante técnico de TI do Grupo para apoio ao fornecedor nas atividades de implantação em produção e integração com a infraestrutura interna. | A partir do início da fase de implantação |
| P07 | Disponibilidade do solicitante (Jadson) e/ou representante da Área de Inovação para aprovação de artefatos, participação em reuniões de checkpoint e validação de decisões de produto, com SLA de resposta de até 3 dias úteis. | Durante todo o projeto |
| P08 | Definição e comunicação formal do Sponsor do projeto ao GP VMO, necessária para habilitação do TAP e início contratual. | Antes da assinatura do contrato |

---

## 6. Cronograma Esperado

O prazo final de entrega é **30/11/2026**. Considerando a data de emissão deste WR (2026-05-18), a validade de 60 dias para recebimento de propostas e o benchmark de mercado para desenvolvimento web de porte médio (4 a 8 meses para plataformas similares), o cronograma abaixo apresenta os marcos obrigatórios que o fornecedor deve respeitar.

**Premissa de início contratual:** cenário base de **2026-08-01** (após processo de seleção, negociação e assinatura de contrato estimados em 45 dias a partir do encerramento das propostas em 2026-07-17).

> Nota: O fornecedor deve apresentar em sua proposta o cronograma detalhado com datas específicas, respeitando o prazo final de 30/11/2026 e a lógica de dependência entre fases.

| Marco | Entregável Principal | Prazo Esperado | Duração Estimada |
|---|---|---|---|
| M0 — Kick-off e Alinhamento | Reunião de kick-off realizada; plano de projeto detalhado aprovado; lista de domínios de e-mail recebida; ambiente de staging provisionado | 2026-08-08 | 1 semana |
| M1 — Arquitetura e Design | Documento de arquitetura técnica (stack, modelo de dados, integrações); protótipos de telas (wireframes ou mockups) aprovados pelo time de inovação | 2026-08-29 | 3 semanas |
| M2 — Módulo de Autenticação e Usuários | RF001 + RF002 + RF008 funcionais em ambiente de desenvolvimento; testes unitários executados | 2026-09-19 | 3 semanas |
| M3 — Portal de Ideias e Campanhas | RF003 + RF004 funcionais em ambiente de desenvolvimento; testes unitários executados | 2026-10-10 | 3 semanas |
| M4 — Fluxo de Aprovação e Gestão de Projetos | RF005 + RF006 + RF007 funcionais em ambiente de desenvolvimento; testes de integração executados | 2026-10-31 | 3 semanas |
| M5 — Integração, Testes de Carga e UAT | RF009 validado (testes de carga >= 500 usuários simultâneos); ciclo de UAT (RF010) iniciado e concluído; todos os defeitos críticos corrigidos | 2026-11-14 | 2 semanas |
| M6 — Implantação, Documentação e Treinamento | RF011 + RF012 + RF013 entregues; plataforma em produção e acessível; treinamento realizado; go-live formal | **2026-11-28** | 2 semanas |
| M7 — Aceite Final | Termo de Aceite Final assinado pelo cliente; entrega de código-fonte e artefatos; início da garantia de 90 dias | **2026-11-30** | 2 dias |

**Duração total do projeto:** aproximadamente 17 semanas (4 meses), dentro da faixa de 4 a 8 meses do benchmark de mercado para soluções similares.

---

## 7. Entregáveis Obrigatórios

Todos os entregáveis abaixo são condição necessária para o aceite do respectivo marco e para liberação do pagamento associado. O critério de aceite é **binário**: o entregável está completo e aprovado (OK) ou não está (NOK — bloqueador de pagamento).

| # | Entregável | Marco Associado | Critério de Aceite (binário) |
|---|---|---|---|
| E01 | Plano de Projeto detalhado com cronograma, matriz de responsabilidades (RACI) e plano de comunicação | M0 | Aprovado formalmente pelo GP VMO e pelo solicitante via e-mail |
| E02 | Documento de Arquitetura Técnica (stack tecnológico, modelo de dados, diagrama de componentes, política de segurança) | M1 | Aprovado pelo GP VMO e pelo representante de TI do Grupo |
| E03 | Protótipos de interface (wireframes ou mockups de alta fidelidade) para os fluxos principais | M1 | Aprovado pelo time de inovação via e-mail |
| E04 | Módulo de autenticação e gestão de usuários (RF001 + RF002 + RF008) funcional em ambiente de desenvolvimento | M2 | Demonstração ao vivo para GP VMO; zero defeitos críticos |
| E05 | Portal de ideias responsivo e módulo de campanhas (RF003 + RF004) funcional em ambiente de desenvolvimento | M3 | Demonstração ao vivo para GP VMO; zero defeitos críticos |
| E06 | Fluxo de aprovação (RF005), mini gestão de projetos (RF006) e mensuração de ganhos (RF007) funcionais em ambiente de desenvolvimento | M4 | Demonstração ao vivo para GP VMO; zero defeitos críticos |
| E07 | Relatório de testes de carga atestando suporte a >= 500 usuários simultâneos (RF009) | M5 | Relatório assinado pelo fornecedor; evidência de execução do teste |
| E08 | Relatório de UAT (RF010) com lista de defeitos encontrados, status de resolução e aprovação do time de inovação | M5 | Assinado pelo ponto focal do time de inovação; zero defeitos críticos em aberto |
| E09 | Documentação técnica completa e manuais do usuário por papel (RF011) | M6 | Entregue em formato digital (PDF + editorável); aprovada pelo GP VMO |
| E10 | Plataforma implantada e acessível em ambiente de produção (RF012) | M6 | URL de produção funcionando; checklist de go-live preenchido e aprovado pelo TI do Grupo |
| E11 | Treinamento do time de inovação e administradores realizado (RF013), com lista de presença e material entregue | M6 | Lista de presença assinada; material enviado ao cliente |
| E12 | Código-fonte completo e versionado entregue em repositório Git privado do cliente | M7 | Repositório acessível e com histórico de commits; aprovado pelo TI do Grupo |
| E13 | Termo de Aceite Final assinado pelas partes | M7 | Documento assinado pelo Sponsor e pelo GP VMO |

---

## 8. Governança e Comunicação

### 8.1 Estrutura de Governança

| Papel | Responsável | Escopo de Decisão |
|---|---|---|
| Sponsor do Projeto | A DEFINIR (pendência registrada no TAP) | Aprovação de mudanças de escopo, orçamento e prazo; aceite final |
| Solicitante / Product Owner | Jadson — Área de Inovação | Validação de requisitos, aprovação de protótipos, condução do UAT |
| Gestor do Projeto (GP) | VMO Consultoria | Gestão de escopo, prazo, custo, riscos e comunicação entre partes |
| Representante Técnico TI Grupo | A designar pelo Grupo Águia Branca | Aprovação de arquitetura, infraestrutura e implantação |
| Gerente do Projeto do Fornecedor | A designar pelo fornecedor contratado | Execução técnica, entrega de artefatos, gestão da equipe de desenvolvimento |

### 8.2 Rituais de Comunicação

| Ritual | Frequência | Participantes | Responsável pela Condução |
|---|---|---|---|
| Reunião de Status Semanal | Semanal (toda segunda-feira) | GP VMO + GP Fornecedor + Jadson | GP VMO |
| Checkpoint de Marco | A cada entrega de marco | GP VMO + GP Fornecedor + Solicitante + TI Grupo (quando aplicável) | GP VMO |
| Reunião de Risco e Impedimentos | Quinzenal ou sob demanda | GP VMO + GP Fornecedor | GP VMO |
| Relatório de Status | Quinzenal | GP VMO → Sponsor + Solicitante | GP VMO |
| Revisão de UAT | Durante o período de UAT | Time de inovação + Fornecedor + GP VMO | Solicitante (Jadson) |

### 8.3 Gestão de Mudanças

Toda alteração de escopo, prazo ou orçamento deve seguir o processo formal de Change Request (CR):
1. Solicitante ou fornecedor registra CR por e-mail ao GP VMO com descrição, impacto estimado e justificativa;
2. GP VMO analisa e apresenta análise de impacto ao Sponsor em até 5 dias úteis;
3. Sponsor aprova ou rejeita formalmente;
4. CR aprovado é refletido no plano de projeto e contrato (via aditivo se houver impacto financeiro).

### 8.4 Canal Oficial de Comunicação

- **E-mail do GP VMO:** a ser definido no kick-off
- **Plataforma de gestão de projeto:** a ser definida no kick-off (Jira, Trello, ClickUp ou equivalente)
- **Repositório de documentos:** pasta compartilhada (Google Drive ou SharePoint do Grupo), acessível a todas as partes

---

## 9. Condições Comerciais

### 9.1 Orçamento e Envelopes de Referência por Marco

O orçamento total aprovado é de **R$ 90.000,00 (noventa mil reais)**. O pagamento será realizado em marcos, conforme tabela abaixo. Os percentuais são referência para negociação — o fornecedor pode propor redistribuição desde que justificada e sem alterar o total.

| Marco | Evento Gatilho do Pagamento | Valor de Referência | % do Total |
|---|---|---|---|
| M0 — Kick-off | Assinatura do contrato e realização do kick-off | R$ 18.000,00 | 20% |
| M2 — Autenticação e Usuários | Aceite formal de E04 pelo GP VMO | R$ 13.500,00 | 15% |
| M3 — Portal de Ideias e Campanhas | Aceite formal de E05 pelo GP VMO | R$ 13.500,00 | 15% |
| M4 — Fluxo de Aprovação e Gestão de Projetos | Aceite formal de E06 pelo GP VMO | R$ 13.500,00 | 15% |
| M5 — UAT Concluído | Aceite formal de E07 + E08 (relatório de carga + UAT aprovado) | R$ 13.500,00 | 15% |
| M7 — Aceite Final | Assinatura do Termo de Aceite Final (E13) + entrega de código-fonte (E12) | R$ 18.000,00 | 20% |
| **TOTAL** | | **R$ 90.000,00** | **100%** |

### 9.2 Condições de Faturamento

- O faturamento de cada parcela está condicionado à aprovação formal do entregável pelo GP VMO ou pelo Sponsor, conforme indicado;
- O fornecedor deverá emitir Nota Fiscal de Serviços (NFS-e) contra o CNPJ do Grupo Águia Branca, com descritivo do marco correspondente;
- O prazo de pagamento após aprovação e recebimento da NFS-e é de **15 (quinze) dias úteis**;
- Retenções legais (ISS, PIS, COFINS, CSLL, IR) serão aplicadas conforme legislação vigente;
- Quaisquer reajustes deverão ser negociados via CR e aditivo contratual.

### 9.3 Penalidades

| Evento | Penalidade |
|---|---|
| Atraso na entrega de marco sem justificativa formal aceita pelo GP VMO | Multa de 0,5% do valor total do contrato por dia de atraso, limitada a 10% do valor total |
| Entrega de artefato com defeitos críticos recusados no aceite | Prazo adicional de até 10 dias úteis para correção; se não corrigido, retenção da parcela correspondente até resolução |
| Abandono do projeto pelo fornecedor | Devolução de 100% dos valores pagos referentes a entregas não aceitas + multa de 10% sobre o valor total do contrato |
| Descumprimento de cláusulas de confidencialidade | Multa de R$ 50.000,00 por ocorrência, independentemente de outros danos |

### 9.4 Garantia

- **Período de garantia:** 90 (noventa) dias corridos a partir da data de assinatura do Termo de Aceite Final;
- Durante a garantia, o fornecedor corrigirá, sem custo adicional, defeitos funcionais identificados pelo cliente que sejam decorrentes de falha no desenvolvimento;
- Não estão cobertos pela garantia: alterações de escopo, falhas de infraestrutura do cliente, uso indevido da plataforma ou defeitos decorrentes de customizações realizadas pelo cliente sem anuência do fornecedor;
- O período de garantia não se confunde com suporte técnico continuado, que deverá ser contratado separadamente.

### 9.5 Propriedade Intelectual

Ao final do contrato, mediante quitação integral do valor contratual, a **propriedade intelectual total** da plataforma desenvolvida — incluindo código-fonte, banco de dados, documentação e artefatos — é transferida integralmente ao Grupo Águia Branca. O fornecedor não poderá reutilizar, comercializar ou licenciar o código desenvolvido especificamente para este projeto a terceiros.

---

## 10. Artefato Obrigatório — Checklist de Qualificação Técnica

O fornecedor deve responder **integralmente** a todos os 10 grupos e 41 itens abaixo, preenchendo as colunas OK, NOK ou Observações para cada item. A não resposta a qualquer item implica desclassificação automática da proposta. O checklist deve ser entregue em planilha (Excel ou Google Sheets) além de incorporado ao documento de proposta em PDF.

**Legenda:** OK = Atende integralmente | NOK = Não atende | Observações = Atende parcialmente ou com ressalvas (detalhar)

---

### GRUPO 1 — Capacidade Técnica e Portfólio

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 1.1 | O fornecedor possui portfólio comprovado de ao menos 2 (dois) projetos de desenvolvimento web sob medida entregues nos últimos 3 anos, com escopo equivalente (portal corporativo, plataforma B2B ou SaaS) | | | |
| 1.2 | O fornecedor possui experiência com desenvolvimento de plataformas multiusuário com controle de acesso por papéis (RBAC) | | | |
| 1.3 | O fornecedor possui casos de uso com bases de usuários de 5.000+ usuários em ambientes de produção | | | |
| 1.4 | O fornecedor pode fornecer ao menos 2 (duas) referências de clientes anteriores com projetos similares, com contato disponível para verificação | | | |
| 1.5 | O fornecedor possui equipe técnica dedicada ao projeto com ao menos: 1 arquiteto/tech lead, 2 desenvolvedores full-stack, 1 designer UX/UI e 1 analista de QA | | | |

---

### GRUPO 2 — Stack Tecnológico e Arquitetura

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 2.1 | O fornecedor utiliza stack tecnológico moderno e mantido ativamente (ex.: Django/Python, Node.js, Laravel/PHP, ou equivalente para backend; React, Vue.js, Angular ou equivalente para frontend) | | | |
| 2.2 | A arquitetura proposta é baseada em camadas (frontend, backend, banco de dados) com separação clara de responsabilidades e documentada | | | |
| 2.3 | O fornecedor adota banco de dados relacional (PostgreSQL, MySQL ou equivalente) com modelo de dados versionado e migrations automatizadas | | | |
| 2.4 | O fornecedor entregará o código-fonte versionado em repositório Git, com histórico de commits e branching strategy documentada | | | |
| 2.5 | A solução é responsiva por design, compatível com os principais browsers (Chrome, Firefox, Edge, Safari) e acessível em dispositivos móveis via browser | | | |

---

### GRUPO 3 — Segurança e Autenticação

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 3.1 | O fornecedor implementa autenticação segura com hash de senhas (bcrypt ou Argon2), política de senha forte e bloqueio por tentativas excessivas | | | |
| 3.2 | O fornecedor suporta autenticação multifator (MFA/2FA) como camada adicional opcional para usuários | | | |
| 3.3 | O fornecedor implementa controle de sessão com timeout configurável e invalidação segura de tokens | | | |
| 3.4 | O fornecedor adota práticas de segurança OWASP Top 10 no desenvolvimento, com evidência (checklist ou relatório de análise) | | | |
| 3.5 | A plataforma será desenvolvida com suporte a HTTPS/TLS obrigatório em produção | | | |

---

### GRUPO 4 — Escalabilidade e Performance

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 4.1 | O fornecedor apresenta estratégia de arquitetura para suportar 10.000+ usuários cadastrados sem degradação de performance | | | |
| 4.2 | O fornecedor realizará testes de carga formais (com ferramenta como Locust, k6, JMeter ou equivalente) validando suporte a >= 500 usuários simultâneos | | | |
| 4.3 | O fornecedor apresenta estratégia de cache (nível de aplicação ou banco de dados) para as consultas de maior volume | | | |
| 4.4 | O fornecedor adota paginação e carregamento assíncrono (lazy loading) nas listagens de ideias, projetos e relatórios | | | |

---

### GRUPO 5 — Implantação e Infraestrutura

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 5.1 | O fornecedor é capaz de realizar implantação em infraestrutura on-premise ou nuvem privada gerenciada pelo cliente (sem dependência de plataforma de hospedagem específica do fornecedor) | | | |
| 5.2 | O fornecedor entregará scripts de deploy automatizado (Docker, Docker Compose, scripts shell ou equivalente) com instruções documentadas | | | |
| 5.3 | O fornecedor entregará procedimento formal de rollback documentado e testado | | | |
| 5.4 | O fornecedor entregará scripts de backup e restore do banco de dados com instruções de operação | | | |
| 5.5 | O fornecedor cooperará com o time de TI do Grupo Águia Branca nas atividades de implantação em produção, incluindo transferência de conhecimento operacional | | | |

---

### GRUPO 6 — Qualidade e Testes

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 6.1 | O fornecedor adota práticas de testes automatizados (testes unitários e/ou de integração) com cobertura mínima de 60% do código backend | | | |
| 6.2 | O fornecedor conduzirá ciclo formal de UAT com o time de inovação do cliente, com gestão de defeitos em ferramenta rastreável (Jira, GitHub Issues, Trello ou equivalente) | | | |
| 6.3 | O fornecedor define critério de saída do UAT: zero defeitos classificados como críticos em aberto na data de aceite | | | |
| 6.4 | O fornecedor realizará testes de regressão após correção de defeitos identificados no UAT antes de solicitar novo aceite | | | |

---

### GRUPO 7 — Documentação

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 7.1 | O fornecedor entregará documentação técnica em português brasileiro: arquitetura, stack, modelo de dados, APIs internas e instruções de deploy | | | |
| 7.2 | O fornecedor entregará manuais do usuário diferenciados por papel (colaborador, gestor, time de inovação, administrador) em português brasileiro | | | |
| 7.3 | O fornecedor entregará material de treinamento (slides e/ou vídeo gravado) para uso posterior pelo cliente no treinamento de novos usuários | | | |
| 7.4 | Toda documentação será entregue em formato digital editável (Word/Google Docs ou Markdown) além de PDF | | | |

---

### GRUPO 8 — Gestão de Projeto e Comunicação

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 8.1 | O fornecedor designará um Gerente de Projeto dedicado como ponto de contato único com o GP VMO | | | |
| 8.2 | O fornecedor participará de reuniões de status semanais com o GP VMO e o solicitante do Grupo Águia Branca | | | |
| 8.3 | O fornecedor apresentará relatório de progresso quinzenal com status de entregas, riscos identificados e impedimentos | | | |
| 8.4 | O fornecedor utilizará ferramenta de gestão de projeto compartilhada (Jira, Trello, ClickUp ou equivalente) com acesso ao GP VMO e ao cliente | | | |
| 8.5 | O fornecedor possui processo formal de gestão de mudanças de escopo (Change Request) com análise de impacto documentada | | | |

---

### GRUPO 9 — Aspectos Jurídicos e Contratuais

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 9.1 | O fornecedor aceita cláusula de transferência total de propriedade intelectual ao Grupo Águia Branca ao final do contrato, mediante quitação integral | | | |
| 9.2 | O fornecedor aceita cláusula de confidencialidade (NDA) cobrindo todos os dados, processos e informações do Grupo Águia Branca acessados durante o projeto | | | |
| 9.3 | O fornecedor aceita o modelo de pagamento por marcos conforme descrito na Seção 9 deste Work Request | | | |
| 9.4 | O fornecedor aceita o período de garantia de 90 dias corridos após o Aceite Final, com correção de defeitos sem custo adicional | | | |
| 9.5 | O fornecedor está em situação regular perante o fisco federal, estadual e municipal (CNPJ ativo, certidões negativas de débito disponíveis) | | | |

---

### GRUPO 10 — Proposta Comercial e Prazo

| # | Item de Verificação | OK | NOK | Observações |
|---|---|---|---|---|
| 10.1 | O valor total da proposta está dentro do orçamento aprovado de R$ 90.000,00 (noventa mil reais) | | | |
| 10.2 | O fornecedor apresenta cronograma detalhado com datas específicas por marco, respeitando o prazo final de 30/11/2026 | | | |
| 10.3 | O fornecedor apresenta composição de preço detalhada por fase/módulo, permitindo análise de aderência ao escopo | | | |
| 10.4 | O fornecedor declara que o escopo descrito neste Work Request está integralmente contemplado na proposta, sem custos adicionais não declarados | | | |
| 10.5 | A proposta tem validade mínima de 60 dias a partir da data de submissão | | | |
| 10.6 | O fornecedor apresenta plano de contingência para riscos críticos identificados (saída de membros-chave da equipe, atrasos técnicos, incompatibilidade com infraestrutura do cliente) | | | |

---

**TOTAL DE ITENS:** 41 itens distribuídos em 10 grupos

**Instrução ao Fornecedor:** Preencha cada célula OK, NOK ou Observações. Respostas "OK" sem evidência serão desclassificadas na etapa de due diligence técnica. Para itens NOK ou com ressalvas, detalhe nas Observações o motivo e a solução alternativa proposta, se houver.

---

## 11. Processo de Submissão

### 11.1 Prazo de Submissão

As propostas devem ser enviadas até **15 (quinze) dias corridos** a partir da data de emissão deste Work Request, ou seja, até **2026-06-02** (segunda-feira), às **18h00 (horário de Brasília)**.

Propostas recebidas após esse prazo não serão consideradas no processo de seleção, salvo prorrogação formal comunicada pelo GP VMO a todos os fornecedores convidados.

### 11.2 Canal de Envio

- **Canal exclusivo:** e-mail ao Gestor do Projeto VMO (endereço a ser informado no convite formal)
- **Assunto do e-mail:** `[PROPOSTA] PROJ-2026-004 — Plataforma de Gestão de Ideias — [Nome da Empresa Fornecedora]`
- Propostas enviadas por qualquer outro canal (WhatsApp, plataformas de licitação, entrega física) não serão aceitas

### 11.3 Formato Obrigatório da Proposta

A proposta deve ser enviada em **dois arquivos**:

| Arquivo | Formato | Conteúdo Obrigatório |
|---|---|---|
| Proposta Técnica e Comercial | PDF (não editável) | Apresentação da empresa, portfólio, equipe, cronograma detalhado, escopo técnico, composição de preço por marco, condições comerciais e plano de contingência |
| Checklist de Qualificação | Planilha Excel (.xlsx) ou Google Sheets (link compartilhado) | Todos os 10 grupos e 41 itens da Seção 10 preenchidos integralmente com colunas OK, NOK e Observações |

A ausência de qualquer um dos dois arquivos implica desclassificação automática.

### 11.4 Critérios de Avaliação e Seleção

A avaliação das propostas seguirá o modelo de pontuação ponderada:

| Critério | Peso |
|---|---|
| Adequação técnica ao escopo (aderência ao checklist, arquitetura proposta) | 35% |
| Experiência comprovada e qualidade do portfólio | 25% |
| Preço total e distribuição por marcos | 25% |
| Prazo e viabilidade do cronograma proposto | 15% |

Fornecedores com pontuação final abaixo de 70% na avaliação técnica (critérios 1 e 2) serão eliminados antes da análise comercial.

### 11.5 Processo de Due Diligence

O GP VMO poderá solicitar, após a análise inicial das propostas:
- Apresentação presencial ou por videoconferência (até 1 hora) para esclarecimentos técnicos;
- Verificação de referências com clientes anteriores indicados na proposta;
- Validação de certidões e documentação jurídica (CNPJ, certidões negativas, contrato social).

### 11.6 Comunicação do Resultado

- O resultado da seleção será comunicado a todos os fornecedores participantes em até **10 dias úteis** após o prazo de submissão;
- O fornecedor selecionado receberá a minuta contratual em até 5 dias úteis após a comunicação do resultado;
- O prazo para assinatura do contrato é de até 5 dias úteis após o envio da minuta.

### 11.7 Esclarecimentos sobre este WR

Dúvidas sobre o escopo, requisitos ou condições deste Work Request devem ser enviadas por e-mail ao GP VMO com o assunto `[DUVIDA WR] PROJ-2026-004` até **5 (cinco) dias corridos** antes do prazo de submissão. As respostas serão enviadas a todos os fornecedores convidados simultaneamente, garantindo isonomia no processo.

---

*Este Work Request foi elaborado por VMO Consultoria — Fábio Fornecedor, com base nas informações fornecidas pelo solicitante Jadson (Área de Inovação, Grupo Águia Branca) e no benchmark de mercado de soluções similares. Todas as informações aqui contidas são confidenciais e de uso exclusivo dos fornecedores convidados a participar deste processo.*

*Validade deste documento: 60 dias a partir de 2026-05-18 (vence em 2026-07-17).*
