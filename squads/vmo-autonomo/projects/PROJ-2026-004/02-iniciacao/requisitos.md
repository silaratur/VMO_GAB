# ERF — Especificação de Requisitos Funcionais
## PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação
## Grupo Águia Branca | DEM-2026-001

**Versão:** 3.0
**Data:** 2026-05-14
**Responsável:** Rafael Requisito — Especialista em Requisitos, VMO Autônomo
**Status:** Rascunho para revisão

---

## 1. Introdução e Objetivo

Este documento especifica os requisitos funcionais e não-funcionais da **Plataforma Interna de Gestão de Ideias de Inovação** do Grupo Águia Branca, desenvolvida no âmbito do projeto PROJ-2026-004.

### 1.1 Motivação
A organização utiliza atualmente uma solução terceirizada para gestão de ideias de inovação. Os principais motivadores da substituição são:
- Custo por licença/usuário incompatível com a escala do Grupo (holding + VixPar + VAB + comércio);
- Necessidade de expansão irrestrita a todos os colaboradores sem custo adicional;
- Controle total sobre dados, fluxos e customizações futuras.

### 1.2 Objetivo do Sistema
Prover uma plataforma web proprietária que permita a qualquer colaborador do Grupo Águia Branca submeter, acompanhar e colaborar com ideias de inovação, suportando o ciclo completo: captação → avaliação → aprovação → implementação → mensuração de ganhos.

### 1.3 Objetivo desta ERF
Definir de forma precisa, numerada e priorizada todos os requisitos que orientarão o desenvolvimento, a validação e a aceitação da plataforma, servindo como contrato técnico entre os stakeholders e a equipe de desenvolvimento.

---

## 2. Escopo da Especificação

### 2.1 Dentro do escopo
- Portal web de cadastro e gestão de ideias;
- Sistema de campanhas e desafios de inovação;
- Fluxo de aprovação multi-etapa (gestor de área + envolvidos);
- Módulo de mini gestão de projetos para ideias aprovadas;
- Módulo de mensuração de ganhos das ideias implementadas;
- Painel administrativo para o time de inovação;
- Relatórios e visibilidade para colaboradores e gestores;
- Autenticação e gestão de perfis de usuário;
- Suporte irrestrito a todos os colaboradores do Grupo (sem limitação de licença).

### 2.2 Fora do escopo (Won't Have — fase atual)
- Integração com sistemas legados (ERP, HRIS, AD/LDAP) — escopo inicial;
- Aplicativo móvel nativo (iOS/Android);
- Gamificação avançada (ranking, badges, pontuação pública);
- Inteligência artificial para triagem ou sugestão de ideias;
- Workflow de patente ou proteção de propriedade intelectual.

### 2.3 Premissas
- A transição deve ser transparente para os usuários: apenas o link de acesso muda;
- Não há requisito legal ou regulatório específico a ser atendido nesta fase;
- O prazo de entrega é dezembro/2026;
- O orçamento disponível é de até R$ 90.000,00.

---

## 3. Requisitos Funcionais (RF)

Os requisitos estão agrupados por módulo e classificados segundo a priorização MoSCoW:
- **M** = Must Have
- **S** = Should Have
- **C** = Could Have
- **W** = Won't Have (this time)

---

### M1 — Autenticação e Gestão de Usuários

---

#### RF001 — Cadastro de usuário por convite ou auto-registro
**Prioridade:** Must Have
**Descrição:** O sistema deve permitir que colaboradores do Grupo Águia Branca criem sua conta de acesso, seja por convite enviado pelo administrador ou por auto-registro com e-mail corporativo válido (@grupoaguiabranca.com.br e domínios das empresas do grupo).

**Critério de aceitação:**
- Um colaborador com e-mail corporativo válido consegue criar conta em até 3 minutos, sem auxílio do administrador.
- Tentativas de registro com e-mail fora dos domínios autorizados são bloqueadas com mensagem explicativa.
- O e-mail de confirmação é entregue em até 2 minutos após o registro.

---

#### RF002 — Autenticação com login e senha
**Prioridade:** Must Have
**Descrição:** O sistema deve autenticar usuários por e-mail e senha, com recuperação de senha via e-mail.

**Critério de aceitação:**
- O login com credenciais válidas concede acesso em até 3 segundos.
- Após 5 tentativas consecutivas de login com senha incorreta, a conta é temporariamente bloqueada por 15 minutos.
- A recuperação de senha via e-mail funciona dentro de 5 minutos e invalida o link após uso ou após 24 horas.

---

#### RF003 — Perfis de acesso (papéis/roles)
**Prioridade:** Must Have
**Descrição:** O sistema deve suportar ao menos os seguintes papéis: Colaborador, Gestor de Área, Time de Inovação (administrador) e Superadministrador. Cada papel tem permissões distintas definidas nesta ERF.

**Critério de aceitação:**
- Um Colaborador não consegue acessar funcionalidades restritas ao Time de Inovação ou ao Gestor.
- A troca de papel de um usuário pelo administrador tem efeito imediato, sem necessidade de novo login.
- Todos os acessos são registrados em log rastreável por usuário, data/hora e ação.

---

#### RF004 — Gestão de usuários pelo administrador
**Prioridade:** Must Have
**Descrição:** O Time de Inovação (admin) deve poder listar, buscar, ativar, desativar e alterar o papel de qualquer usuário da plataforma.

**Critério de aceitação:**
- O administrador visualiza lista paginada de todos os usuários com filtro por empresa do grupo, papel e status (ativo/inativo).
- A desativação de um usuário impede imediatamente novos logins sem excluir seu histórico de ideias.
- Qualquer alteração de papel é registrada em log com o usuário que realizou a ação e o horário.

---

#### RF005 — Autenticação por SSO (Single Sign-On)
**Prioridade:** Should Have
**Descrição:** Suportar login via provedor de identidade corporativo (ex.: Microsoft Entra ID / Azure AD), eliminando a necessidade de senha separada.

---

#### RF006 — Perfil do colaborador
**Prioridade:** Should Have
**Descrição:** Cada usuário deve ter um perfil editável contendo nome, foto, empresa do grupo, área/departamento e cargo. Esses dados são usados no cadastro de ideias e no fluxo de aprovação.

---

### M2 — Cadastro e Gestão de Ideias

---

#### RF007 — Formulário de cadastro de ideia
**Prioridade:** Must Have
**Descrição:** Qualquer colaborador autenticado deve poder submeter uma ideia por meio de formulário estruturado contendo: (a) título, (b) descrição do problema a resolver, (c) descrição da solução proposta, (d) ganhos esperados (financeiro, operacional, ambiental, social), (e) beneficiários/impactados, (f) recursos estimados necessários, (g) empresa/área do grupo relacionada. Atributos adicionais podem ser configurados pelo administrador.

**Critério de aceitação:**
- O formulário com todos os campos obrigatórios preenchidos é salvo com sucesso em até 5 segundos.
- Campos obrigatórios não preenchidos bloqueam o envio com mensagem de validação clara por campo.
- O colaborador recebe confirmação por e-mail em até 5 minutos após o envio bem-sucedido.
- A ideia cadastrada aparece no histórico do colaborador imediatamente após o envio.

---

#### RF008 — Rascunho de ideia
**Prioridade:** Must Have
**Descrição:** O colaborador deve poder salvar uma ideia como rascunho e retomá-la para edição antes de submetê-la formalmente.

**Critério de aceitação:**
- O rascunho é salvo automaticamente a cada 30 segundos durante o preenchimento e manualmente pelo botão "Salvar rascunho".
- O colaborador acessa seus rascunhos em área dedicada no painel e pode retomá-los sem perda de dados.
- Rascunhos não submetidos há mais de 90 dias exibem alerta de expiração, com prazo de 7 dias antes da exclusão automática.

---

#### RF009 — Vinculação de ideia a campanha
**Prioridade:** Must Have
**Descrição:** Durante o cadastro, o colaborador deve poder vincular sua ideia a uma campanha/desafio ativo. Ideias não vinculadas ficam classificadas como "espontâneas".

**Critério de aceitação:**
- A lista de campanhas ativas é exibida no formulário de cadastro.
- Ao selecionar uma campanha, os campos específicos dela são apresentados automaticamente.
- Ideias sem campanha vinculada são salvas com a classificação "Espontânea" e seguem o mesmo fluxo de aprovação.

---

#### RF010 — Histórico e acompanhamento de ideias pelo colaborador
**Prioridade:** Must Have
**Descrição:** O colaborador deve visualizar todas as suas ideias (enviadas e rascunhos) com o status atualizado de cada uma (ex.: Em análise, Em aprovação, Aprovada, Rejeitada, Em implementação, Concluída).

**Critério de aceitação:**
- O painel do colaborador lista todas as suas ideias ordenadas por data de envio (mais recente primeiro), com filtro por status.
- A transição de status é refletida no painel do colaborador em até 1 minuto após a ação do responsável.
- O colaborador recebe notificação por e-mail e na plataforma sempre que o status da sua ideia muda.

---

#### RF011 — Atributos configuráveis de ideia
**Prioridade:** Should Have
**Descrição:** O Time de Inovação deve poder adicionar campos customizados ao formulário de ideia (texto livre, seleção, data) sem necessidade de desenvolvimento.

---

#### RF012 — Anexos e evidências na ideia
**Prioridade:** Should Have
**Descrição:** O colaborador deve poder anexar arquivos (imagens, PDFs, planilhas) à ideia, com limite de 10 MB por arquivo e máximo de 5 arquivos por ideia.

---

#### RF013 — Comentários e colaboração na ideia
**Prioridade:** Could Have
**Descrição:** Usuários que participam do fluxo de aprovação ou são indicados como envolvidos devem poder comentar na ideia para enriquecê-la antes ou durante a avaliação.

---

### M3 — Campanhas e Desafios

---

#### RF014 — Criação e gestão de campanhas pelo Time de Inovação
**Prioridade:** Must Have
**Descrição:** O Time de Inovação deve poder criar campanhas/desafios com: título, descrição, objetivo, data de início, data de término, público-alvo (empresa do grupo, área ou todos) e campos adicionais específicos da campanha.

**Critério de aceitação:**
- Uma campanha criada com todos os campos obrigatórios é publicada imediatamente ou em data agendada configurada.
- A campanha aparece para os colaboradores do público-alvo em até 1 minuto após a publicação.
- Campanhas com data de término vencida são automaticamente encerradas e não recebem novas ideias, exibindo status "Encerrada".

---

#### RF015 — Visualização de campanhas ativas pelo colaborador
**Prioridade:** Must Have
**Descrição:** O colaborador deve visualizar todas as campanhas ativas com descrição, objetivo, prazo e número de ideias já submetidas para cada uma.

**Critério de aceitação:**
- A lista de campanhas ativas é acessível no menu principal sem necessidade de login (acesso público dentro da intranet) ou com login, conforme configuração do administrador.
- Campanhas encerradas ficam visíveis em seção de histórico, com seus resultados.
- O número de ideias por campanha é atualizado em tempo real (até 1 minuto de delay).

---

#### RF016 — Encerramento e resultado de campanha
**Prioridade:** Should Have
**Descrição:** Ao encerrar uma campanha, o Time de Inovação deve poder publicar um resumo com as ideias selecionadas e o resultado geral da campanha, visível a todos os participantes.

---

### M4 — Fluxo de Aprovação

---

#### RF017 — Roteamento automático para gestor de área
**Prioridade:** Must Have
**Descrição:** Ao submeter uma ideia, o sistema deve encaminhar automaticamente para o gestor da área do colaborador autor para primeira avaliação, com base no perfil do usuário.

**Critério de aceitação:**
- O gestor da área recebe notificação por e-mail e na plataforma em até 5 minutos após a submissão da ideia.
- O gestor acessa a ideia e pode: aprovar para análise do Time de Inovação, solicitar ajustes ao colaborador ou rejeitar com justificativa obrigatória.
- Ideias sem ação do gestor por 5 dias úteis geram alerta automático por e-mail ao gestor e ao Time de Inovação.

---

#### RF018 — Inclusão de envolvidos no fluxo de aprovação
**Prioridade:** Must Have
**Descrição:** Durante o cadastro da ideia, o colaborador deve poder indicar outros colaboradores como "envolvidos" (co-autores ou áreas impactadas). Esses envolvidos são notificados e podem participar do fluxo de aprovação.

**Critério de aceitação:**
- O colaborador busca envolvidos por nome ou e-mail e os adiciona à ideia antes do envio.
- Os envolvidos recebem notificação por e-mail e na plataforma em até 5 minutos após o envio da ideia.
- Os gestores dos envolvidos também são incluídos no fluxo de aprovação quando configurado pelo administrador.

---

#### RF019 — Avaliação pelo Time de Inovação
**Prioridade:** Must Have
**Descrição:** Após aprovação do gestor de área, o Time de Inovação deve avaliar a ideia com base em critérios configuráveis (ex.: viabilidade, impacto, alinhamento estratégico), podendo aprovar, solicitar ajustes ou rejeitar.

**Critério de aceitação:**
- O Time de Inovação visualiza fila de ideias aguardando avaliação, ordenada por data de entrada, com filtros por campanha, empresa e status.
- A avaliação registra o score de cada critério, comentário justificativo e decisão final.
- O colaborador e o gestor de área são notificados em até 5 minutos após a decisão do Time de Inovação.
- Toda decisão de rejeição exige justificativa com mínimo de 50 caracteres.

---

#### RF020 — Histórico de aprovações e rastreabilidade
**Prioridade:** Must Have
**Descrição:** Todas as etapas do fluxo de aprovação devem ser registradas com usuário responsável, data/hora e decisão tomada, formando um histórico auditável da ideia.

**Critério de aceitação:**
- O histórico completo de tramitações é acessível a qualquer membro do Time de Inovação e ao autor da ideia.
- Nenhuma etapa pode ser alterada retroativamente sem registro da modificação com usuário e timestamp.
- O relatório de auditoria do fluxo pode ser exportado em formato CSV ou PDF para qualquer ideia.

---

#### RF021 — Critérios de avaliação configuráveis
**Prioridade:** Should Have
**Descrição:** O Time de Inovação deve poder definir e personalizar os critérios de avaliação das ideias (nome, descrição, peso, escala de pontuação) sem necessidade de desenvolvimento.

---

#### RF022 — Fluxo de aprovação paralela (multi-gestor)
**Prioridade:** Could Have
**Descrição:** Para ideias que impactam múltiplas áreas, o sistema deve suportar aprovação simultânea pelos gestores de cada área envolvida, com regra de consenso configurável (todos aprovam ou maioria aprova).

---

### M5 — Gestão de Implementação (Mini Projetos)

---

#### RF023 — Criação de projeto a partir de ideia aprovada
**Prioridade:** Must Have
**Descrição:** Após aprovação final pelo Time de Inovação, deve ser possível converter a ideia em um mini projeto de implementação, com responsável, data prevista de início, data prevista de conclusão e marco(s) principais.

**Critério de aceitação:**
- O Time de Inovação converte uma ideia aprovada em projeto em até 3 cliques, sem re-digitação dos dados já existentes na ideia.
- O projeto criado é vinculado à ideia original e acessível pelo link da ideia.
- O responsável pelo projeto recebe notificação em até 5 minutos após a criação.

---

#### RF024 — Acompanhamento de marcos e status do projeto
**Prioridade:** Must Have
**Descrição:** O responsável pelo projeto deve poder registrar marcos (etapas planejadas), atualizar o status de cada marco (Não iniciado, Em andamento, Concluído, Bloqueado) e adicionar comentários de progresso.

**Critério de aceitação:**
- O projeto exibe linha do tempo com os marcos ordenados por data prevista.
- A atualização de status de um marco é salva em até 3 segundos e refletida imediatamente no painel do projeto.
- O Time de Inovação visualiza todos os projetos em andamento em painel consolidado com indicador de progresso por projeto.

---

#### RF025 — Notificações de prazo do projeto
**Prioridade:** Must Have
**Descrição:** O sistema deve enviar alertas automáticos quando um marco ou o prazo final do projeto estiver próximo (7 dias antes) ou vencido (no dia seguinte ao vencimento).

**Critério de aceitação:**
- O responsável pelo projeto e o Time de Inovação recebem e-mail de alerta 7 dias antes do vencimento de cada marco.
- Marcos vencidos (data passada sem status "Concluído") são marcados automaticamente como "Atrasado" e geram alerta no painel.
- O histórico de notificações enviadas é registrado e acessível ao administrador.

---

#### RF026 — Registro de equipe do projeto
**Prioridade:** Should Have
**Descrição:** O responsável pelo projeto deve poder registrar os membros da equipe de implementação, vinculando usuários da plataforma ou cadastrando nomes externos.

---

#### RF027 — Anexos e documentos do projeto
**Prioridade:** Should Have
**Descrição:** O responsável pelo projeto deve poder anexar documentos ao projeto (plano de ação, atas, apresentações), com as mesmas restrições de tamanho do módulo de ideias.

---

### M6 — Mensuração de Ganhos

---

#### RF028 — Registro de ganhos realizados
**Prioridade:** Must Have
**Descrição:** Ao concluir o projeto, o responsável deve registrar os ganhos efetivamente obtidos, preenchendo os mesmos tipos de ganho informados na ideia original (financeiro, operacional, ambiental, social) com valores reais e metodologia de cálculo utilizada.

**Critério de aceitação:**
- O formulário de registro de ganhos é acessível somente para projetos com status "Concluído" ou "Em conclusão".
- Ganhos financeiros são registrados em R$ com campo obrigatório de metodologia de cálculo (mínimo 100 caracteres).
- O Time de Inovação valida o registro de ganhos antes de sua publicação, podendo aprovar ou solicitar revisão.
- Após validação, os ganhos são agregados automaticamente nos relatórios e painéis consolidados.

---

#### RF029 — Comparativo entre ganhos estimados e realizados
**Prioridade:** Must Have
**Descrição:** O sistema deve exibir, para cada ideia implementada, o comparativo entre os ganhos estimados no cadastro e os ganhos efetivamente realizados após a implementação.

**Critério de aceitação:**
- O comparativo é exibido na página da ideia e no painel de projetos concluídos.
- Para ideias com ganho financeiro, o sistema calcula e exibe automaticamente o percentual de aderência (realizado/estimado × 100).
- O comparativo é incluído nos relatórios exportáveis do módulo de mensuração.

---

#### RF030 — Painel consolidado de ganhos
**Prioridade:** Should Have
**Descrição:** O Time de Inovação e a liderança devem acessar um painel com totais consolidados de ganhos por período, empresa do grupo, campanha e tipo de ganho.

---

### M7 — Painel Administrativo (Time de Inovação)

---

#### RF031 — Dashboard de visão geral
**Prioridade:** Must Have
**Descrição:** O Time de Inovação deve ter um dashboard com indicadores-chave: total de ideias cadastradas, ideias por status, ideias por campanha, projetos em andamento, projetos concluídos e ganhos totais registrados.

**Critério de aceitação:**
- O dashboard carrega em até 5 segundos com dados atualizados com no máximo 5 minutos de defasagem.
- Todos os indicadores são clicáveis e direcionam para a lista filtrada correspondente.
- O dashboard é responsivo e utilizável em telas de tablets e desktops.

---

#### RF032 — Configuração de notificações e e-mails automáticos
**Prioridade:** Must Have
**Descrição:** O administrador deve poder configurar quais eventos disparam notificações por e-mail e na plataforma (ex.: nova ideia, mudança de status, prazo vencido), e para quais papéis.

**Critério de aceitação:**
- O administrador acessa tela de configuração de notificações com lista de eventos configuráveis.
- Alterações nas configurações têm efeito a partir da próxima ocorrência do evento, sem necessidade de restart do sistema.
- As configurações de notificação são auditadas (quem alterou, quando e o que mudou).

---

#### RF033 — Gerenciamento de empresas e áreas do grupo
**Prioridade:** Must Have
**Descrição:** O administrador deve poder cadastrar e gerenciar as empresas do grupo (holding, VixPar, VAB, comércio) e suas respectivas áreas/departamentos, vinculando usuários a cada estrutura.

**Critério de aceitação:**
- O administrador cadastra empresas e áreas sem necessidade de desenvolvimento, por interface própria.
- A vinculação de um usuário a uma empresa/área é usada automaticamente no roteamento do fluxo de aprovação.
- Desativar uma área não exclui as ideias ou usuários vinculados a ela; apenas impede novos vínculos.

---

### M8 — Relatórios e Visibilidade

---

#### RF034 — Relatório de ideias por período e filtros
**Prioridade:** Must Have
**Descrição:** O Time de Inovação deve poder gerar relatórios de ideias com filtros combinados por: período, empresa do grupo, área, campanha, status e autor. O relatório deve ser exportável em CSV e PDF.

**Critério de aceitação:**
- O relatório com filtros aplicados é gerado em até 30 segundos para bases de até 10.000 ideias.
- A exportação em CSV mantém todos os campos do filtro aplicado.
- A exportação em PDF inclui cabeçalho com os filtros utilizados, data de geração e logotipo do grupo.

---

#### RF035 — Visibilidade pública das ideias aprovadas
**Prioridade:** Should Have
**Descrição:** Ideias aprovadas ou em implementação podem ser marcadas como "públicas" pelo Time de Inovação, tornando-se visíveis a todos os colaboradores no portal (sem necessidade de ser o autor), com objetivo de inspirar novas contribuições.

---

#### RF036 — Ranking de colaboradores e áreas
**Prioridade:** Could Have
**Descrição:** O sistema pode exibir ranking das áreas ou empresas com mais ideias submetidas e aprovadas, sem expor ranking individual de colaboradores por padrão (privacidade).

---

#### RF037 — Exportação de relatório de ganhos
**Prioridade:** Should Have
**Descrição:** O Time de Inovação deve poder exportar relatório consolidado de ganhos em CSV e PDF, com filtros por período, empresa e tipo de ganho, para apresentação à liderança.

---

## 4. Requisitos Não-Funcionais (RNF)

### RNF001 — Performance
**Categoria:** Performance
**Descrição:** As páginas principais da plataforma (dashboard, lista de ideias, formulário de ideia) devem carregar em até **3 segundos** em conexão de 10 Mbps. Operações de escrita (submissão de ideia, atualização de status) devem ser concluídas em até **5 segundos**.

### RNF002 — Escalabilidade de usuários
**Categoria:** Escalabilidade
**Descrição:** A plataforma deve suportar o acesso simultâneo de pelo menos **500 usuários** sem degradação de performance acima de 20% dos tempos definidos no RNF001. A arquitetura deve permitir escalonamento para até **10.000 usuários cadastrados** sem refatoração estrutural.

### RNF003 — Disponibilidade
**Categoria:** Disponibilidade
**Descrição:** A plataforma deve ter disponibilidade mínima de **99,5% em horário comercial** (segunda a sexta, 07h–20h, horário de Brasília), equivalente a no máximo 18 horas de indisponibilidade por ano nesse período. Janelas de manutenção programada devem ser comunicadas com pelo menos 48 horas de antecedência.

### RNF004 — Segurança — Autenticação e Autorização
**Categoria:** Segurança
**Descrição:** Todas as comunicações devem trafegar sobre HTTPS (TLS 1.2+). Senhas devem ser armazenadas com hash bcrypt (custo mínimo 10). Tokens de sessão devem expirar após 8 horas de inatividade. O sistema deve implementar controle de acesso baseado em papéis (RBAC) com verificação em cada requisição ao servidor.

### RNF005 — Segurança — Proteção de Dados
**Categoria:** Segurança
**Descrição:** Dados sensíveis dos usuários e das ideias devem ser armazenados em banco de dados com criptografia em repouso. Logs de acesso devem ser mantidos por mínimo de 12 meses. O sistema não deve expor dados de um colaborador a outro sem permissão explícita do sistema de papéis.

### RNF006 — Usabilidade
**Categoria:** Usabilidade
**Descrição:** A interface deve seguir princípios de usabilidade (Nielsen), ser em português brasileiro, responsiva para desktop e tablet (resolução mínima 1024×768) e acessível via navegadores modernos (Chrome, Edge, Firefox — últimas 2 versões). Um colaborador sem treinamento deve conseguir submeter uma ideia em até **5 minutos** na primeira utilização.

### RNF007 — Manutenibilidade
**Categoria:** Manutenibilidade
**Descrição:** O código-fonte deve ser entregue com cobertura de testes automatizados de pelo menos **70% das funções críticas** (fluxo de aprovação, autenticação, notificações). A documentação técnica deve incluir diagrama de arquitetura, modelo de dados e manual de deploy. O ambiente de desenvolvimento deve ser reproduzível via container (Docker/Docker Compose).

### RNF008 — Compatibilidade e Transição
**Categoria:** Compatibilidade
**Descrição:** A transição do sistema atual para a nova plataforma deve ser transparente: apenas o link de acesso muda. Os dados históricos existentes no sistema terceirizado devem ter plano de migração documentado (mesmo que a migração não seja realizada na fase inicial). Nenhuma funcionalidade ativa do sistema atual pode ficar indisponível durante a transição.

### RNF009 — Backup e Recuperação
**Categoria:** Confiabilidade
**Descrição:** O sistema deve realizar backup automático diário dos dados, com retenção mínima de 30 dias. O procedimento de restauração deve ser testado e documentado, com RTO (Recovery Time Objective) de até **4 horas** e RPO (Recovery Point Objective) de até **24 horas**.

### RNF010 — Auditabilidade
**Categoria:** Conformidade
**Descrição:** Toda ação relevante de negócio (criação/edição de ideia, mudança de status, aprovação/rejeição, alteração de perfil de usuário) deve ser registrada em log de auditoria com: usuário, timestamp, entidade afetada e valor anterior/posterior. Os logs devem ser imutáveis para usuários comuns.

---

## 5. Tabela Resumo MoSCoW

| Código | Módulo | Descrição Resumida | MoSCoW |
|--------|--------|--------------------|--------|
| RF001 | M1 | Cadastro de usuário | Must Have |
| RF002 | M1 | Autenticação com login e senha | Must Have |
| RF003 | M1 | Perfis de acesso (roles) | Must Have |
| RF004 | M1 | Gestão de usuários pelo admin | Must Have |
| RF005 | M1 | SSO corporativo | Should Have |
| RF006 | M1 | Perfil do colaborador | Should Have |
| RF007 | M2 | Formulário de cadastro de ideia | Must Have |
| RF008 | M2 | Rascunho de ideia | Must Have |
| RF009 | M2 | Vinculação de ideia a campanha | Must Have |
| RF010 | M2 | Histórico e acompanhamento de ideias | Must Have |
| RF011 | M2 | Atributos configuráveis de ideia | Should Have |
| RF012 | M2 | Anexos e evidências | Should Have |
| RF013 | M2 | Comentários e colaboração | Could Have |
| RF014 | M3 | Criação e gestão de campanhas | Must Have |
| RF015 | M3 | Visualização de campanhas ativas | Must Have |
| RF016 | M3 | Encerramento e resultado de campanha | Should Have |
| RF017 | M4 | Roteamento automático para gestor | Must Have |
| RF018 | M4 | Inclusão de envolvidos no fluxo | Must Have |
| RF019 | M4 | Avaliação pelo Time de Inovação | Must Have |
| RF020 | M4 | Histórico de aprovações e rastreabilidade | Must Have |
| RF021 | M4 | Critérios de avaliação configuráveis | Should Have |
| RF022 | M4 | Aprovação paralela multi-gestor | Could Have |
| RF023 | M5 | Criação de projeto a partir de ideia | Must Have |
| RF024 | M5 | Acompanhamento de marcos e status | Must Have |
| RF025 | M5 | Notificações de prazo do projeto | Must Have |
| RF026 | M5 | Registro de equipe do projeto | Should Have |
| RF027 | M5 | Anexos do projeto | Should Have |
| RF028 | M6 | Registro de ganhos realizados | Must Have |
| RF029 | M6 | Comparativo estimado vs. realizado | Must Have |
| RF030 | M6 | Painel consolidado de ganhos | Should Have |
| RF031 | M7 | Dashboard de visão geral | Must Have |
| RF032 | M7 | Configuração de notificações | Must Have |
| RF033 | M7 | Gerenciamento de empresas e áreas | Must Have |
| RF034 | M8 | Relatório de ideias com exportação | Must Have |
| RF035 | M8 | Visibilidade pública de ideias aprovadas | Should Have |
| RF036 | M8 | Ranking de colaboradores e áreas | Could Have |
| RF037 | M8 | Exportação de relatório de ganhos | Should Have |

**Contagem por classificação:**

| MoSCoW | Quantidade | % |
|--------|-----------|---|
| Must Have | 23 | 62% |
| Should Have | 10 | 27% |
| Could Have | 4 | 11% |
| Won't Have | 5 (fora do escopo) | — |
| **Total RFs** | **37** | 100% |

---

## 6. Glossário de Termos

| Termo | Definição |
|-------|-----------|
| **Colaborador** | Qualquer funcionário do Grupo Águia Branca (holding, VixPar, VAB, comércio) com acesso à plataforma. |
| **Ideia Espontânea** | Ideia submetida sem vínculo a uma campanha específica. |
| **Campanha / Desafio** | Iniciativa temática lançada pelo Time de Inovação para orientar a captação de ideias em um período definido. |
| **Time de Inovação** | Equipe do Grupo responsável por gerir o processo de inovação; possui papel de administrador na plataforma. |
| **Gestor de Área** | Colaborador com papel de gestor, responsável pela primeira avaliação das ideias de sua equipe. |
| **Envolvido** | Colaborador indicado pelo autor da ideia como co-autor ou representante de área impactada. |
| **Fluxo de Aprovação** | Sequência de etapas de avaliação e decisão pela qual uma ideia passa desde a submissão até a aprovação ou rejeição final. |
| **Mini Projeto** | Estrutura simplificada de gestão de projeto criada para acompanhar a implementação de uma ideia aprovada (marcos, responsáveis, prazos). |
| **Ganhos Estimados** | Benefícios projetados pelo colaborador no momento do cadastro da ideia. |
| **Ganhos Realizados** | Benefícios efetivamente obtidos após a implementação da ideia, registrados e validados pelo Time de Inovação. |
| **RBAC** | Role-Based Access Control — controle de acesso baseado em papéis/perfis de usuário. |
| **MoSCoW** | Método de priorização de requisitos: Must Have, Should Have, Could Have, Won't Have. |
| **RTO** | Recovery Time Objective — tempo máximo aceitável para restauração do sistema após falha. |
| **RPO** | Recovery Point Objective — quantidade máxima de dados que pode ser perdida em caso de falha (medida em tempo). |
| **SSO** | Single Sign-On — autenticação única que permite acesso a múltiplos sistemas com um só login. |
| **ERF** | Especificação de Requisitos Funcionais — este documento. |
| **VixPar** | Empresa do Grupo Águia Branca (transporte de passageiros). |
| **VAB** | Viação Águia Branca — empresa do Grupo (transporte rodoviário). |

---

## 7. Aprovação

| Papel | Nome | Assinatura | Data |
|-------|------|------------|------|
| Solicitante / Product Owner | | | |
| Responsável VMO (Projetos) | | | |
| Líder Técnico | | | |
| Time de Inovação (Sponsor) | | | |
| Rafael Requisito (Autor ERF) | Rafael Requisito — VMO Autônomo | *(gerado automaticamente)* | 2026-05-14 |

---

**Próximos passos recomendados:**
1. Revisão e validação deste documento com o solicitante (DEM-2026-001) e o Time de Inovação do Grupo Águia Branca.
2. Definição dos atributos adicionais do formulário de ideia (pendente com solicitante — RF007).
3. Validação da estrutura de empresas e áreas do grupo para configuração do RF033.
4. Estimativa técnica de esforço por módulo baseada nesta ERF.
5. Aprovação formal e baseline do documento antes do início do desenvolvimento.

---

*Documento gerado por: VMO Autônomo — Rafael Requisito*
*Projeto: PROJ-2026-004 | Demanda: DEM-2026-001*
*Data: 2026-05-14 | Versão: 3.0*
