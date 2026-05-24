# Especificação de Requisitos Funcionais (ERF)

**Projeto:** PROJ-2026-006 — Plataforma Própria de Gestão de Ideias e Inovação
**Demanda:** DEM-2026-006
**Versão:** 1.0
**Data:** 2026-05-16
**Autor:** Rafael Requisito — Engenheiro de Requisitos
**Solicitante:** Jadson — Gestor de Inovação
**Status:** Aguardando validação do solicitante

---

## Sumário

1. [Objetivo do Documento](#1-objetivo-do-documento)
2. [Escopo da Versão 1](#2-escopo-da-versão-1)
3. [Convenções e Método de Priorização](#3-convenções-e-método-de-priorização)
4. [Glossário de Termos do Domínio](#4-glossário-de-termos-do-domínio)
5. [Requisitos Funcionais por Módulo](#5-requisitos-funcionais-por-módulo)
   - [M1 — Cadastro de Ideias](#m1--cadastro-de-ideias)
   - [M2 — Campanhas e Desafios](#m2--campanhas-e-desafios)
   - [M3 — Fluxo de Aprovação](#m3--fluxo-de-aprovação)
   - [M4 — Mini Gestão de Projetos](#m4--mini-gestão-de-projetos)
   - [M5 — Mensuração de Ganhos](#m5--mensuração-de-ganhos)
   - [M6 — Dashboard e Monitoramento](#m6--dashboard-e-monitoramento)
6. [Requisitos Não-Funcionais](#6-requisitos-não-funcionais)
7. [Resumo de Priorização MoSCoW](#7-resumo-de-priorização-moscow)
8. [Rastreabilidade](#8-rastreabilidade)
9. [Restrições e Premissas](#9-restrições-e-premissas)
10. [Critérios de Aceite Globais](#10-critérios-de-aceite-globais)
11. [Seção de Aprovação](#11-seção-de-aprovação)

---

## 1. Objetivo do Documento

Este documento especifica os Requisitos Funcionais (RF) e Requisitos Não-Funcionais (RNF) da Plataforma de Gestão de Ideias e Inovação da VMO Consultoria. Os requisitos foram elicitados a partir da demanda qualificada DEM-2026-006, aprovada com condições (score 21/30, 70%), e derivados das descrições funcionais fornecidas pelo solicitante Jadson, Gestor de Inovação.

O documento serve como contrato de entendimento entre a equipe de requisitos, o solicitante e a equipe de desenvolvimento. Nenhum desenvolvimento deve iniciar sem a aprovação formal deste documento pelo solicitante.

---

## 2. Escopo da Versão 1

**Incluído no escopo v1:**
- Portal web para submissão e gestão de ideias
- Cadastro e publicação de campanhas e desafios
- Fluxo de aprovação em duas dimensões (viabilidade e investimento)
- Mini gestão de projetos para ideias aprovadas
- Registro e comparação de ganhos realizados vs. prometidos
- Dashboard com visibilidade diferenciada por perfil de acesso

**Explicitamente fora do escopo v1:**
- Integração com sistemas externos (SAP, ERP, sistemas de RH)
- Aplicativo mobile (iOS ou Android)
- Funcionalidades de gamificação (pontos, badges, ranking público)
- Notificações por SMS ou WhatsApp

---

## 3. Convenções e Método de Priorização

### Identificação de Requisitos

- **RF[módulo][sequencial]** — Requisito Funcional. Exemplo: RF101 (Módulo 1, requisito 1)
- **RNF[categoria][sequencial]** — Requisito Não-Funcional. Exemplo: RNFP01 (Performance, requisito 1)

### Priorização MoSCoW

| Sigla | Significado | Critério de uso |
|-------|------------|-----------------|
| **M** | Must Have | Sem este requisito o sistema não entrega o objetivo central; bloqueia o go-live |
| **S** | Should Have | Alto valor de negócio; deve ser entregue se houver tempo e budget |
| **C** | Could Have | Desejável; inclui se sobrarem recursos após M e S |
| **W** | Won't Have (v1) | Fora do escopo atual; candidato para v2 |

### Critérios de Aceitação

Todos os requisitos **Must Have** possuem critério de aceitação mensurável no formato:
> **Dado** [contexto], **Quando** [ação], **Então** [resultado verificável].

---

## 4. Glossário de Termos do Domínio

| Termo | Definição |
|-------|-----------|
| **Ideia** | Proposta de melhoria, inovação ou solução submetida por um colaborador, contendo no mínimo: descrição do problema que resolve, benefícios esperados e ganhos estimados. |
| **Ideia Avulsa** | Ideia submetida espontaneamente pelo colaborador, sem vínculo com uma campanha ou desafio específico. |
| **Ideia de Campanha** | Ideia submetida como resposta a uma campanha ou desafio publicado pelo time de inovação. Mantém vínculo rastreável com a campanha de origem. |
| **Campanha** | Iniciativa temática de coleta de ideias publicada pelo time de inovação, com período definido de início e fim, tema central e critérios de avaliação. |
| **Desafio** | Variante de campanha com problema específico e bem delimitado a ser resolvido. Pode ter restrições adicionais (orçamento máximo, área alvo, tecnologia proibida). |
| **Colaborador** | Qualquer funcionário da organização com acesso ao portal que pode submeter ideias e acompanhar o status de suas submissões. |
| **Gestor de Área** | Líder direto do colaborador que submeteu a ideia; participa obrigatoriamente do fluxo de aprovação como primeiro aprovador. |
| **Gestor de Inovação** | Responsável pelo programa de inovação; publica campanhas, monitora o funil de ideias e gerencia o processo de aprovação. |
| **Administrador** | Perfil com acesso irrestrito ao sistema; gerencia usuários, perfis e configurações da plataforma. |
| **Fluxo de Aprovação** | Sequência estruturada de etapas pelas quais uma ideia submetida passa antes de ser aprovada ou rejeitada. Inclui aprovação do gestor de área e de partes interessadas identificadas no cadastro. |
| **Dimensão de Aprovação** | Perspectiva de avaliação de uma ideia. Na v1 existem duas dimensões: (a) Viabilidade técnica/operacional e (b) Investimento necessário. |
| **Parte Interessada** | Pessoa ou área identificada no cadastro da ideia como relevante para sua aprovação ou implementação, além do gestor de área. |
| **Plano de Ação Macro** | Conjunto de tarefas de alto nível criado para orientar a implementação de uma ideia aprovada. Contém no mínimo: tarefa, responsável e prazo. |
| **Ganho Prometido** | Benefício quantificado declarado pelo autor no momento do cadastro da ideia (ex: redução de custo em R$X, aumento de produtividade em Y%). |
| **Ganho Realizado** | Benefício efetivamente obtido após a implementação da ideia, registrado pela equipe responsável e comparado com o ganho prometido. |
| **Funil de Ideias** | Representação do volume de ideias em cada etapa do ciclo de vida: Submetida → Em Análise → Aprovada → Em Implementação → Concluída → Rejeitada. |
| **Perfil de Acesso** | Conjunto de permissões atribuído a um usuário que define o que ele pode visualizar e executar na plataforma. Os perfis são: Colaborador, Gestor de Área, Gestor de Inovação e Administrador. |
| **Status da Ideia** | Estado atual da ideia no ciclo de vida. Estados válidos: Rascunho, Submetida, Em Análise, Aprovada, Rejeitada, Em Implementação, Concluída. |
| **Métrica de Resultado** | Indicador calculado automaticamente pela plataforma para medir a efetividade do programa de inovação (ex: taxa de aprovação, ROI médio, tempo médio de implementação). |

---

## 5. Requisitos Funcionais por Módulo

---

### M1 — Cadastro de Ideias

#### Contexto

Colaboradores acessam o portal e submetem ideias individualmente. A submissão pode ser avulsa ou vinculada a uma campanha ativa. O formulário deve capturar informações suficientes para que aprovadores tomem decisões fundamentadas.

---

**RF101 — Submissão de Ideia pelo Colaborador**
- **Prioridade:** Must Have
- **Descrição:** O colaborador deve ser capaz de submeter uma ideia por meio de formulário web contendo os campos obrigatórios: título, descrição do problema que resolve, benefícios esperados, ganhos estimados (campo livre com valor e unidade de medida) e área de impacto. Campos opcionais: anexos (até 5 arquivos, máximo 10 MB cada), partes interessadas sugeridas e observações adicionais.
- **Critério de Aceitação:**
  - Dado que o colaborador está autenticado e acessa o formulário de nova ideia,
  - Quando preenche todos os campos obrigatórios e clica em "Submeter",
  - Então a ideia é salva com status "Submetida", um ID único é gerado (formato IDEA-AAAA-NNNNNN), o colaborador recebe confirmação visual na tela e notificação por e-mail com o ID gerado, e o gestor de área do colaborador recebe notificação de nova ideia pendente de análise.

---

**RF102 — Rascunho de Ideia**
- **Prioridade:** Should Have
- **Descrição:** O colaborador deve poder salvar uma ideia como rascunho antes de submetê-la formalmente. Rascunhos não iniciam o fluxo de aprovação. O colaborador pode retomar, editar e submeter o rascunho a qualquer momento.
- **Critério de Aceitação:**
  - Dado que o colaborador está preenchendo o formulário de ideia,
  - Quando clica em "Salvar Rascunho" sem preencher todos os campos obrigatórios,
  - Então a ideia é salva com status "Rascunho", nenhuma notificação é enviada a aprovadores, e o rascunho aparece na área "Minhas Ideias" do colaborador com indicação visual clara de que ainda não foi submetido.

---

**RF103 — Identificação de Ideia de Campanha vs. Avulsa**
- **Prioridade:** Must Have
- **Descrição:** Ao iniciar o cadastro de uma ideia, o colaborador deve indicar explicitamente se a ideia é avulsa ou vinculada a uma campanha ativa. Caso vinculada a uma campanha, o sistema deve exibir o tema e as regras da campanha durante o preenchimento.
- **Critério de Aceitação:**
  - Dado que o colaborador inicia o cadastro de uma ideia,
  - Quando seleciona uma campanha ativa da lista,
  - Então o formulário exibe o banner da campanha, o tema e os critérios da campanha, e a ideia é gravada com o atributo "campanha_id" preenchido com o ID da campanha selecionada.
  - Quando seleciona "Ideia Avulsa",
  - Então o formulário não exibe referência a campanhas e o atributo "campanha_id" fica nulo.

---

**RF104 — Edição de Ideia em Rascunho**
- **Prioridade:** Should Have
- **Descrição:** O colaborador deve poder editar qualquer campo de uma ideia com status "Rascunho". Ideias com status "Submetida" ou posterior não podem ser editadas pelo colaborador sem ação de um aprovador.
- **Critério de Aceitação:**
  - Dado que o colaborador acessa uma ideia com status "Rascunho",
  - Quando altera qualquer campo e clica em "Salvar",
  - Então as alterações são gravadas e um histórico de versões registra a data, hora e usuário da alteração.

---

**RF105 — Acompanhamento de Status pelo Autor**
- **Prioridade:** Must Have
- **Descrição:** O colaborador deve poder visualizar, em área exclusiva "Minhas Ideias", todas as ideias que submeteu, com o status atual, data de submissão, data da última atualização e o nome do aprovador responsável pela etapa corrente.
- **Critério de Aceitação:**
  - Dado que o colaborador acessa "Minhas Ideias",
  - Quando a lista é carregada,
  - Então todas as suas ideias são exibidas em ordem cronológica decrescente, com status visualmente diferenciado por cor (conforme guia de cores definido no protótipo), e a página carrega em menos de 3 segundos com até 100 ideias na lista.

---

**RF106 — Notificação de Mudança de Status**
- **Prioridade:** Must Have
- **Descrição:** O autor da ideia deve receber notificação por e-mail sempre que o status de sua ideia mudar (ex: de "Submetida" para "Em Análise", de "Em Análise" para "Aprovada" ou "Rejeitada"). A notificação deve conter: o novo status, o nome do aprovador que realizou a ação e, no caso de rejeição, o motivo informado.
- **Critério de Aceitação:**
  - Dado que um aprovador altera o status de uma ideia,
  - Quando a ação é confirmada,
  - Então o sistema envia e-mail ao autor da ideia em até 5 minutos, contendo: ID da ideia, título, novo status, nome do aprovador e data/hora da ação. Em caso de rejeição, o e-mail inclui obrigatoriamente o campo "Motivo da Rejeição".

---

### M2 — Campanhas e Desafios

#### Contexto

O time de inovação publica campanhas e desafios para direcionar a coleta de ideias. Deve haver diferenciação visual clara entre ideias avulsas e ideias de campanha tanto na submissão quanto na visualização.

---

**RF201 — Criação de Campanha**
- **Prioridade:** Must Have
- **Descrição:** O Gestor de Inovação deve poder criar uma campanha informando: título, descrição do tema central, data de início, data de encerramento, área(s) alvo, critérios de avaliação e imagem de capa (opcional). A campanha só fica visível aos colaboradores após publicação explícita.
- **Critério de Aceitação:**
  - Dado que o Gestor de Inovação acessa "Gerenciar Campanhas" e clica em "Nova Campanha",
  - Quando preenche todos os campos obrigatórios (título, descrição, data de início, data de encerramento) e clica em "Publicar",
  - Então a campanha recebe status "Ativa", aparece na lista de campanhas disponíveis para todos os colaboradores, e o Gestor de Inovação recebe confirmação na tela com o ID da campanha gerado (formato CAMP-AAAA-NNN).

---

**RF202 — Encerramento Automático de Campanha**
- **Prioridade:** Must Have
- **Descrição:** O sistema deve encerrar automaticamente uma campanha ao atingir sua data de fim, alterando o status para "Encerrada" e impedindo novas submissões vinculadas a ela. Ideias já vinculadas e em andamento no fluxo de aprovação não são afetadas.
- **Critério de Aceitação:**
  - Dado que uma campanha tem data de encerramento configurada,
  - Quando a data de encerramento é atingida (às 23:59 do dia definido),
  - Então o sistema altera o status da campanha para "Encerrada" automaticamente sem intervenção manual, o formulário de submissão remove a campanha da lista de campanhas disponíveis, e o Gestor de Inovação recebe notificação por e-mail informando o encerramento e o total de ideias recebidas.

---

**RF203 — Criação de Desafio com Restrições**
- **Prioridade:** Should Have
- **Descrição:** O Gestor de Inovação deve poder criar um desafio (variante de campanha) com restrições adicionais: orçamento máximo para a solução proposta, área(s) de atuação permitida(s) e requisitos mínimos da proposta (campo texto livre). O formulário de ideia vinculada a um desafio deve exibir essas restrições de forma destacada.
- **Critério de Aceitação:**
  - Dado que o Gestor de Inovação cria um desafio e define orçamento máximo de R$50.000,
  - Quando um colaborador submete uma ideia vinculada a esse desafio informando ganho estimado acima do orçamento máximo,
  - Então o sistema exibe alerta informando que o custo declarado excede o orçamento máximo do desafio (sem bloquear a submissão, apenas alertando).

---

**RF204 — Diferenciação Visual de Ideias por Origem**
- **Prioridade:** Must Have
- **Descrição:** Em todas as telas onde ideias são listadas (dashboard, funil, área de aprovação), ideias de campanha devem ser visualmente distinguíveis de ideias avulsas por meio de etiqueta, ícone ou cor específica conforme definido no protótipo de interface.
- **Critério de Aceitação:**
  - Dado que uma lista de ideias é exibida contendo ideias avulsas e ideias de campanha,
  - Quando o usuário visualiza a lista,
  - Então cada ideia de campanha exibe o nome da campanha de origem em destaque visual (etiqueta colorida ou ícone com tooltip), e ideias avulsas exibem marcação "Avulsa" ou equivalente, sendo possível distinguir a origem de cada ideia sem abrir o detalhe.

---

**RF205 — Listagem e Filtro de Campanhas**
- **Prioridade:** Should Have
- **Descrição:** Colaboradores devem poder visualizar a lista de campanhas ativas com filtro por área, ordenação por data de encerramento e indicação do número de ideias já submetidas em cada campanha. Gestores de Inovação visualizam também campanhas encerradas e em rascunho.
- **Critério de Aceitação:**
  - Dado que o colaborador acessa "Campanhas",
  - Quando aplica filtro por área,
  - Então a lista exibe somente campanhas da área selecionada em até 2 segundos, e cada campanha exibe: título, prazo de encerramento em dias restantes e contador de ideias submetidas.

---

### M3 — Fluxo de Aprovação

#### Contexto

Após a submissão, a ideia passa por fluxo estruturado de aprovação. O fluxo inclui obrigatoriamente o gestor de área do colaborador e pode incluir outras partes interessadas identificadas no cadastro. A aprovação ocorre em duas dimensões independentes: viabilidade e investimento.

---

**RF301 — Aprovação pelo Gestor de Área**
- **Prioridade:** Must Have
- **Descrição:** Após a submissão de uma ideia, o gestor de área do colaborador deve receber notificação e ter acesso à ideia para aprovar ou rejeitar. A aprovação é registrada na dimensão "Viabilidade". O gestor deve informar obrigatoriamente um parecer (texto livre, mínimo 50 caracteres) antes de confirmar a decisão.
- **Critério de Aceitação:**
  - Dado que uma ideia foi submetida e o gestor de área está autenticado,
  - Quando o gestor acessa a ideia, registra um parecer com mínimo de 50 caracteres e clica em "Aprovar — Viabilidade",
  - Então a ideia avança no fluxo, o status é atualizado para "Em Análise", o parecer é gravado com data, hora e nome do aprovador, e o Gestor de Inovação é notificado por e-mail.
  - Quando o gestor clica em "Rejeitar" sem preencher o parecer,
  - Então o sistema bloqueia a ação e exibe mensagem: "O campo 'Parecer' é obrigatório para rejeitar uma ideia. Mínimo de 50 caracteres."

---

**RF302 — Aprovação de Investimento**
- **Prioridade:** Must Have
- **Descrição:** Além da aprovação de viabilidade, a ideia deve passar por aprovação na dimensão "Investimento", realizada pelo Gestor de Inovação ou por um aprovador financeiro configurável pelo Administrador. O aprovador de investimento pode: aprovar o orçamento solicitado, aprovar com valor ajustado (informando novo valor) ou rejeitar justificando.
- **Critério de Aceitação:**
  - Dado que a ideia foi aprovada na dimensão "Viabilidade" pelo gestor de área,
  - Quando o aprovador financeiro acessa a ideia e aprova com valor ajustado de R$X,
  - Então o sistema registra o valor aprovado (diferente do solicitado), o status da ideia permanece "Em Análise" até aprovação de ambas as dimensões, e o autor da ideia recebe notificação informando que a dimensão de investimento foi aprovada com valor ajustado de R$X.

---

**RF303 — Aprovação Paralela de Múltiplas Partes Interessadas**
- **Prioridade:** Should Have
- **Descrição:** O fluxo de aprovação deve suportar múltiplas partes interessadas além do gestor de área. As aprovações das partes interessadas adicionais ocorrem em paralelo (não em sequência). A ideia só avança quando todas as aprovações obrigatórias forem registradas.
- **Critério de Aceitação:**
  - Dado que uma ideia foi submetida com 2 partes interessadas adicionais identificadas,
  - Quando o gestor de área aprova a viabilidade,
  - Então os 2 aprovadores adicionais recebem notificação simultânea e a ideia só avança para "Aprovada" quando todas as aprovações necessárias (gestor de área + 2 partes interessadas + aprovador financeiro) forem registradas.

---

**RF304 — Histórico do Fluxo de Aprovação**
- **Prioridade:** Must Have
- **Descrição:** Toda ideia deve manter histórico completo e imutável de todas as ações do fluxo de aprovação, contendo: nome do aprovador, data e hora da ação, dimensão aprovada, decisão tomada (aprovado/rejeitado/aprovado com ressalva) e parecer registrado.
- **Critério de Aceitação:**
  - Dado que um aprovador registra uma decisão em uma ideia,
  - Quando qualquer usuário com acesso à ideia abre o "Histórico de Aprovações",
  - Então o histórico exibe todas as ações em ordem cronológica crescente, nenhum registro pode ser editado ou excluído após confirmação, e o histórico é exportável em formato PDF.

---

**RF305 — Prazo de Resposta dos Aprovadores**
- **Prioridade:** Should Have
- **Descrição:** O Gestor de Inovação deve poder configurar um prazo máximo (em dias) para que cada aprovador responda. Ao atingir o prazo sem resposta, o sistema envia lembrete automático por e-mail ao aprovador e ao Gestor de Inovação.
- **Critério de Aceitação:**
  - Dado que um prazo de 5 dias úteis foi configurado para aprovadores,
  - Quando o prazo é atingido sem ação do aprovador,
  - Então o sistema envia e-mail de lembrete ao aprovador e ao Gestor de Inovação no dia seguinte ao vencimento, e a ideia é marcada visualmente no painel de aprovações como "Pendente — Prazo Excedido".

---

**RF306 — Rejeição com Motivo Obrigatório**
- **Prioridade:** Must Have
- **Descrição:** Qualquer rejeição de ideia em qualquer etapa do fluxo requer preenchimento obrigatório do campo "Motivo da Rejeição" (texto livre, mínimo 50 caracteres). O motivo é exibido ao autor da ideia na notificação e no histórico.
- **Critério de Aceitação:**
  - Dado que um aprovador tenta rejeitar uma ideia,
  - Quando o campo "Motivo da Rejeição" está vazio ou com menos de 50 caracteres e o aprovador clica em "Rejeitar",
  - Então o sistema bloqueia a submissão e exibe mensagem de erro informando o requisito de mínimo de 50 caracteres. A rejeição só é registrada quando o campo está preenchido corretamente.

---

### M4 — Mini Gestão de Projetos

#### Contexto

Ideias aprovadas (nas duas dimensões) recebem um plano de ação macro para orientar a implementação. A equipe responsável registra tarefas, atualiza o status e acompanha o progresso até a conclusão.

---

**RF401 — Criação de Plano de Ação para Ideia Aprovada**
- **Prioridade:** Must Have
- **Descrição:** Quando uma ideia recebe status "Aprovada", o Gestor de Inovação ou o responsável pela implementação deve criar um plano de ação macro contendo: nome do responsável pela implementação, data de início prevista, data de conclusão prevista e pelo menos uma tarefa. Enquanto o plano não for criado, a ideia fica com status "Aprovada — Aguardando Plano".
- **Critério de Aceitação:**
  - Dado que uma ideia está com status "Aprovada",
  - Quando o responsável acessa a ideia e clica em "Criar Plano de Ação", preenche os campos obrigatórios e salva,
  - Então o status da ideia muda para "Em Implementação", o plano é gravado, e o autor da ideia recebe notificação por e-mail informando o responsável pela implementação e a data prevista de conclusão.

---

**RF402 — Gerenciamento de Tarefas do Plano**
- **Prioridade:** Must Have
- **Descrição:** O plano de ação deve suportar lista de tarefas onde cada tarefa contém: título da tarefa, responsável (usuário do sistema), data de início, data de entrega e status (Pendente, Em Andamento, Concluída, Bloqueada). O responsável pela implementação pode adicionar, editar e excluir tarefas enquanto a ideia está com status "Em Implementação".
- **Critério de Aceitação:**
  - Dado que o plano de ação existe com pelo menos uma tarefa,
  - Quando o responsável adiciona uma nova tarefa preenchendo título, responsável e data de entrega,
  - Então a tarefa é salva e exibida na lista do plano. Quando o responsável exclui uma tarefa, o sistema solicita confirmação antes de excluir e registra no histórico o nome do usuário que excluiu e a data/hora.

---

**RF403 — Atualização de Status das Tarefas**
- **Prioridade:** Must Have
- **Descrição:** O responsável por uma tarefa (ou o responsável pela implementação da ideia) deve poder atualizar o status de cada tarefa. A atualização de status deve registrar data e hora automaticamente. Quando todas as tarefas estiverem com status "Concluída", o sistema deve sugerir ao responsável marcar a ideia como "Concluída".
- **Critério de Aceitação:**
  - Dado que todas as tarefas do plano estão com status "Concluída",
  - Quando o sistema detecta essa condição,
  - Então exibe notificação/banner ao responsável pela implementação: "Todas as tarefas foram concluídas. Deseja registrar a ideia como Concluída e iniciar o registro de ganhos realizados?" com botão de ação direta.

---

**RF404 — Percentual de Progresso do Plano**
- **Prioridade:** Should Have
- **Descrição:** O sistema deve calcular e exibir automaticamente o percentual de progresso do plano de ação baseado na proporção de tarefas concluídas sobre o total de tarefas (ex: 3 de 5 tarefas concluídas = 60%). O percentual deve ser atualizado em tempo real sem necessidade de recarregar a página.
- **Critério de Aceitação:**
  - Dado que um plano tem 5 tarefas e 2 estão com status "Concluída",
  - Quando o usuário visualiza o plano,
  - Então o sistema exibe "40% concluído" ou barra de progresso equivalente, e o valor é atualizado automaticamente quando qualquer tarefa muda de status.

---

**RF405 — Adição de Comentários no Plano**
- **Prioridade:** Could Have
- **Descrição:** Os membros da equipe de implementação devem poder adicionar comentários livres no plano de ação para comunicação interna e registro de impedimentos ou decisões relevantes.
- **Critério de Aceitação:**
  - Dado que o usuário acessa o plano de ação de uma ideia em implementação,
  - Quando adiciona um comentário e clica em "Postar",
  - Então o comentário é gravado com nome do autor e data/hora e exibido em ordem cronológica.

---

### M5 — Mensuração de Ganhos

#### Contexto

Após a conclusão da implementação, a equipe registra os ganhos efetivamente obtidos e a plataforma compara com os ganhos prometidos no momento do cadastro da ideia, gerando métricas do programa de inovação.

---

**RF501 — Registro de Ganhos Realizados**
- **Prioridade:** Must Have
- **Descrição:** Ao marcar uma ideia como "Concluída", o responsável pela implementação deve obrigatoriamente registrar os ganhos realizados informando: tipo de ganho (deve coincidir com as categorias disponíveis no cadastro original), valor realizado e unidade de medida. É permitido registrar ganhos parciais (com justificativa) ou ausência de ganhos (com justificativa obrigatória).
- **Critério de Aceitação:**
  - Dado que o responsável acessa o formulário de encerramento de uma ideia,
  - Quando informa ganho realizado de R$15.000 em "Redução de Custo" e clica em "Confirmar Conclusão",
  - Então o sistema grava o ganho realizado, altera o status da ideia para "Concluída", calcula automaticamente a variação entre ganho prometido e ganho realizado (ex: prometido R$20.000, realizado R$15.000 = -25%), e exibe o resultado da comparação na tela de confirmação.

---

**RF502 — Comparação Ganho Prometido vs. Realizado**
- **Prioridade:** Must Have
- **Descrição:** Para cada ideia concluída, o sistema deve exibir comparação clara entre ganho prometido (registrado no cadastro) e ganho realizado (registrado no encerramento), incluindo: valor prometido, valor realizado, variação absoluta e variação percentual. Caso o ganho realizado seja 0 (zero), deve exibir "Ganho não realizado — [motivo informado]".
- **Critério de Aceitação:**
  - Dado que uma ideia concluída tem ganho prometido de R$20.000 e ganho realizado de R$15.000,
  - Quando qualquer usuário com acesso abre o detalhe da ideia,
  - Então a seção "Ganhos" exibe: Prometido: R$20.000 | Realizado: R$15.000 | Variação: -R$5.000 (-25%), com indicação visual (cor verde se realizado >= prometido, cor vermelha se realizado < prometido).

---

**RF503 — Métricas Agregadas do Programa de Inovação**
- **Prioridade:** Must Have
- **Descrição:** O sistema deve calcular e disponibilizar as seguintes métricas agregadas do programa, atualizadas automaticamente: (a) total de ideias submetidas, (b) taxa de aprovação (ideias aprovadas / ideias submetidas), (c) taxa de implementação (ideias concluídas / ideias aprovadas), (d) ganho total realizado acumulado, (e) ganho total prometido acumulado, (f) tempo médio de ciclo (submissão → conclusão em dias). As métricas devem ser filtráveis por período e por campanha.
- **Critério de Aceitação:**
  - Dado que o Gestor de Inovação acessa o painel de métricas,
  - Quando seleciona o período "Janeiro a Março de 2026",
  - Então o sistema exibe as 6 métricas listadas referentes ao período selecionado em até 5 segundos, e o Gestor pode exportar o painel em formato PDF ou Excel.

---

**RF504 — Histórico de Ganhos por Ideia**
- **Prioridade:** Should Have
- **Descrição:** Cada ideia deve manter histórico de todos os registros de ganho realizados, permitindo registros parciais ao longo do tempo (ex: ganho mensal recorrente). Cada registro deve conter: data do registro, valor, responsável pelo registro e observações.
- **Critério de Aceitação:**
  - Dado que uma ideia concluída tem 3 registros de ganho realizados em meses diferentes,
  - Quando o usuário acessa o histórico de ganhos da ideia,
  - Então o sistema exibe os 3 registros em ordem cronológica com soma cumulativa atualizada automaticamente.

---

### M6 — Dashboard e Monitoramento

#### Contexto

O dashboard oferece visibilidade consolidada de todos os projetos de inovação. O conteúdo exibido e o nível de detalhe variam conforme o perfil do usuário.

---

**RF601 — Dashboard do Colaborador**
- **Prioridade:** Must Have
- **Descrição:** O colaborador deve ter acesso a um dashboard pessoal exibindo: minhas ideias submetidas (com status), campanhas ativas disponíveis para submissão, e resumo de ganhos realizados de suas ideias concluídas.
- **Critério de Aceitação:**
  - Dado que o colaborador autentica no sistema,
  - Quando acessa o dashboard,
  - Então visualiza exclusivamente suas próprias ideias e não tem acesso ao funil global de ideias de outros colaboradores. O dashboard carrega em até 3 segundos.

---

**RF602 — Dashboard do Gestor de Inovação**
- **Prioridade:** Must Have
- **Descrição:** O Gestor de Inovação deve ter acesso a dashboard executivo contendo: funil de ideias (todas as etapas), ideias pendentes de aprovação com prazo, ideias em implementação com status de progresso, métricas consolidadas do programa (conforme RF503) e lista de campanhas ativas com contador de ideias.
- **Critério de Aceitação:**
  - Dado que o Gestor de Inovação autentica no sistema,
  - Quando acessa o dashboard,
  - Então visualiza o funil completo de todas as ideias da organização, pode aplicar filtros por área, período e campanha, e o dashboard carrega em até 5 segundos com até 500 ideias no banco.

---

**RF603 — Dashboard do Gestor de Área**
- **Prioridade:** Must Have
- **Descrição:** O Gestor de Área deve ter acesso a dashboard com foco em aprovações: ideias de sua equipe pendentes de aprovação, histórico de aprovações realizadas por ele e visibilidade das ideias de sua equipe em implementação.
- **Critério de Aceitação:**
  - Dado que o Gestor de Área autentica no sistema,
  - Quando acessa o dashboard,
  - Então visualiza somente ideias submetidas por colaboradores de sua equipe (conforme estrutura hierárquica cadastrada) e as ideias pendentes de sua aprovação são destacadas no topo da lista.

---

**RF604 — Filtros e Busca no Dashboard**
- **Prioridade:** Should Have
- **Descrição:** O dashboard do Gestor de Inovação deve oferecer filtros combinados por: status da ideia, área de origem, campanha, responsável pela implementação, período de submissão e período de encerramento previsto. Adicionalmente, deve haver campo de busca textual por título ou ID da ideia.
- **Critério de Aceitação:**
  - Dado que o Gestor de Inovação aplica filtro combinado (área = "TI" + status = "Em Implementação"),
  - Quando confirma os filtros,
  - Então a lista exibe apenas ideias que satisfazem simultaneamente os dois critérios, em até 3 segundos, e o estado dos filtros é mantido durante a sessão do usuário.

---

**RF605 — Exportação de Relatório**
- **Prioridade:** Should Have
- **Descrição:** O Gestor de Inovação deve poder exportar a lista de ideias visível no dashboard com os filtros ativos em formato Excel (.xlsx) e PDF. O arquivo exportado deve conter todos os campos visíveis na tela mais os campos: data de submissão, nome do autor, ganho prometido, ganho realizado e variação.
- **Critério de Aceitação:**
  - Dado que o Gestor de Inovação aplicou filtros no dashboard,
  - Quando clica em "Exportar Excel",
  - Então o download do arquivo .xlsx inicia em até 10 segundos, o arquivo contém todas as ideias filtradas (sem limite de linhas) e inclui os campos adicionais especificados, com cabeçalho de colunas legível.

---

## 6. Requisitos Não-Funcionais

---

### Categoria: Performance

**RNFP01 — Tempo de Resposta de Páginas**
- **Prioridade:** Must Have
- **Descrição:** Todas as páginas do sistema devem carregar completamente (conteúdo principal visível) em até 3 segundos para usuários com conexão de 10 Mbps ou superior, medido sob carga normal (até 100 usuários simultâneos).
- **Critério de Aceitação:** Testes de carga com 100 usuários simultâneos usando ferramenta homologada (ex: k6, JMeter) devem demonstrar que o percentil 95 do tempo de carregamento de páginas é igual ou inferior a 3 segundos. Exceções documentadas: dashboard do Gestor de Inovação (até 5 segundos) e exportação de relatórios (até 10 segundos).

---

**RNFP02 — Capacidade de Usuários Simultâneos**
- **Prioridade:** Must Have
- **Descrição:** O sistema deve suportar até 200 usuários simultâneos sem degradação mensurável de performance (variação máxima de 20% no tempo de resposta base).
- **Critério de Aceitação:** Teste de carga com 200 usuários simultâneos executando ações de leitura e submissão não deve causar erros de timeout e o tempo de resposta não deve exceder 120% do tempo de resposta medido com 50 usuários.

---

**RNFP03 — Tempo de Processamento de Notificações**
- **Prioridade:** Should Have
- **Descrição:** Notificações por e-mail devem ser enviadas em até 5 minutos após o evento que as originou (mudança de status, nova aprovação pendente, etc.).
- **Critério de Aceitação:** Em ambiente de homologação, ao simular 50 eventos simultâneos de mudança de status, 95% dos e-mails devem ser entregues na caixa de entrada dos destinatários em até 5 minutos após o evento.

---

### Categoria: Segurança

**RNFS01 — Autenticação Obrigatória**
- **Prioridade:** Must Have
- **Descrição:** Todo acesso ao sistema deve exigir autenticação prévia. O sistema deve suportar autenticação via SSO corporativo (SAML 2.0 ou OAuth 2.0) como método primário, com fallback para autenticação por e-mail/senha com senha de no mínimo 8 caracteres contendo letras maiúsculas, minúsculas, números e símbolo especial.
- **Critério de Aceitação:** Qualquer tentativa de acesso a URLs do sistema sem sessão autenticada deve redirecionar para a página de login. Após 5 tentativas de login com credenciais incorretas, a conta deve ser bloqueada por 15 minutos. O sistema deve registrar log de cada tentativa de login (sucesso e falha) com IP, data e hora.

---

**RNFS02 — Controle de Acesso por Perfil**
- **Prioridade:** Must Have
- **Descrição:** O sistema deve implementar controle de acesso baseado em perfil (RBAC). Cada operação deve ser autorizada com base no perfil do usuário autenticado. Usuários não devem ter acesso a dados de outros usuários fora das permissões de seu perfil.
- **Critério de Aceitação:** Testes de segurança devem validar que: (a) um Colaborador não consegue acessar ideias de outros colaboradores via URL direta, (b) um Gestor de Área não consegue aprovar ideias fora de sua equipe, (c) modificação dos parâmetros de requisição HTTP para elevar privilégios é bloqueada com resposta HTTP 403.

---

**RNFS03 — Proteção de Dados em Trânsito e em Repouso**
- **Prioridade:** Must Have
- **Descrição:** Toda comunicação entre cliente e servidor deve ser protegida por TLS 1.2 ou superior. Dados sensíveis em banco de dados (senhas, tokens) devem ser armazenados com hash seguro (bcrypt com custo mínimo 10 ou Argon2). Backups devem ser criptografados.
- **Critério de Aceitação:** Varredura com ferramenta de análise SSL (ex: SSL Labs) deve retornar nota A ou superior. Inspeção do banco de dados não deve revelar senhas em texto claro. Política de retenção de backups mínima: 30 dias com criptografia AES-256.

---

**RNFS04 — Auditoria e Rastreabilidade de Ações**
- **Prioridade:** Should Have
- **Descrição:** O sistema deve manter log de auditoria para todas as operações de escrita (criação, edição, exclusão, mudança de status) registrando: usuário, ação realizada, entidade afetada, data/hora e IP de origem. Os logs devem ser imutáveis e retidos por no mínimo 12 meses.
- **Critério de Aceitação:** O Administrador deve poder consultar logs de auditoria filtrados por usuário, tipo de ação e período. Os logs não devem ser deletáveis por nenhum perfil incluindo o Administrador via interface da aplicação.

---

### Categoria: Disponibilidade

**RNFD01 — Uptime Mínimo**
- **Prioridade:** Must Have
- **Descrição:** O sistema deve garantir disponibilidade mínima de 99% medida mensalmente, excluindo janelas de manutenção programada previamente comunicadas com 48 horas de antecedência.
- **Critério de Aceitação:** Monitoramento mensal (ex: UptimeRobot ou equivalente) deve registrar disponibilidade igual ou superior a 99% (máximo de 7,2 horas de indisponibilidade por mês). SLA deve ser formalizado com a equipe de infraestrutura antes do go-live.

---

**RNFD02 — Backup e Recuperação**
- **Prioridade:** Must Have
- **Descrição:** O sistema deve realizar backup automático completo do banco de dados diariamente (à 1h00) e backup incremental a cada 4 horas. O tempo máximo de recuperação (RTO) é de 4 horas e a perda máxima de dados aceitável (RPO) é de 4 horas.
- **Critério de Aceitação:** Teste de recuperação de desastre deve ser executado ao menos uma vez antes do go-live, restaurando um backup completo e verificando integridade dos dados em ambiente de homologação. O tempo total de restauração deve ser registrado e deve ser igual ou inferior a 4 horas.

---

### Categoria: Usabilidade

**RNFU01 — Interface Responsiva**
- **Prioridade:** Must Have
- **Descrição:** A interface do sistema deve ser responsiva, funcionando corretamente em resoluções de desktop (1280x768 ou superior) e tablet (768x1024). O layout deve se adaptar sem perda de funcionalidade ou necessidade de scroll horizontal.
- **Critério de Aceitação:** Testes manuais nas resoluções 1280x768, 1440x900 e 768x1024 devem confirmar que todos os formulários, listas e dashboards são utilizáveis sem scroll horizontal. Imagens e tabelas devem adaptar-se automaticamente à largura da tela.

---

**RNFU02 — Acessibilidade WCAG 2.1**
- **Prioridade:** Should Have
- **Descrição:** O sistema deve atender ao nível AA das diretrizes WCAG 2.1, incluindo: contraste mínimo de 4.5:1 para texto normal, navegação completa por teclado, atributos ARIA em componentes interativos e textos alternativos em imagens funcionais.
- **Critério de Aceitação:** Varredura automatizada com ferramenta WAVE ou axe-core não deve apresentar erros críticos (nível A e AA). Pelo menos um teste de navegação por teclado deve ser executado para os fluxos críticos: submissão de ideia e aprovação.

---

**RNFU03 — Mensagens de Erro Claras**
- **Prioridade:** Must Have
- **Descrição:** Todas as mensagens de erro e validação devem ser escritas em linguagem clara e orientada à ação do usuário (não técnica). Mensagens de validação de formulário devem aparecer próximas ao campo com problema, não apenas no topo da página.
- **Critério de Aceitação:** Revisão de UX com ao menos 3 usuários representativos (colaborador, gestor de área, gestor de inovação) deve confirmar que as mensagens de erro são compreendidas sem necessidade de explicação adicional. Nenhuma mensagem deve expor códigos de erro internos ou stack traces ao usuário final.

---

**RNFU04 — Suporte a Idioma Português Brasileiro**
- **Prioridade:** Must Have
- **Descrição:** Toda a interface, incluindo labels, mensagens de erro, notificações por e-mail e documentação de ajuda embutida, deve estar em Português Brasileiro. Datas devem seguir o formato dd/mm/aaaa e valores monetários o formato R$ X.XXX,XX.
- **Critério de Aceitação:** Revisão de conteúdo por membro da equipe de inovação deve confirmar ausência de textos em outros idiomas na interface. Datas e valores monetários devem ser exibidos nos formatos especificados em todos os contextos da aplicação.

---

## 7. Resumo de Priorização MoSCoW

### Requisitos Funcionais

| Módulo | Must Have | Should Have | Could Have | Won't Have v1 | Total |
|--------|-----------|-------------|------------|---------------|-------|
| M1 — Cadastro de Ideias | 4 (RF101, RF103, RF105, RF106) | 2 (RF102, RF104) | 0 | 0 | 6 |
| M2 — Campanhas e Desafios | 2 (RF201, RF202, RF204) | 2 (RF203, RF205) | 0 | 0 | 5 |
| M3 — Fluxo de Aprovação | 3 (RF301, RF302, RF304, RF306) | 2 (RF303, RF305) | 0 | 0 | 6 |
| M4 — Mini Gestão de Projetos | 3 (RF401, RF402, RF403) | 1 (RF404) | 1 (RF405) | 0 | 5 |
| M5 — Mensuração de Ganhos | 3 (RF501, RF502, RF503) | 1 (RF504) | 0 | 0 | 4 |
| M6 — Dashboard e Monitoramento | 3 (RF601, RF602, RF603) | 2 (RF604, RF605) | 0 | 0 | 5 |
| **Total RF** | **18** | **10** | **1** | **0** | **31** |
| **Percentual RF** | **58%** | **32%** | **3%** | **0%** | **100%** |

> Nota de correção: RF204 (Diferenciação Visual) foi classificado como Must Have — conta 3 Must Have no M2. RF301, RF302, RF304 e RF306 são 4 Must Have no M3.

### Contagem Corrigida por Módulo

| Módulo | Must Have | Should Have | Could Have | Total |
|--------|-----------|-------------|------------|-------|
| M1 | 4 | 2 | 0 | 6 |
| M2 | 3 | 2 | 0 | 5 |
| M3 | 4 | 2 | 0 | 6 |
| M4 | 3 | 1 | 1 | 5 |
| M5 | 3 | 1 | 0 | 4 |
| M6 | 3 | 2 | 0 | 5 |
| **Total RF** | **20** | **10** | **1** | **31** |
| **%** | **64.5%** | **32.3%** | **3.2%** | **100%** |

### Requisitos Não-Funcionais

| Categoria | Must Have | Should Have | Could Have | Total |
|-----------|-----------|-------------|------------|-------|
| Performance | 2 (RNFP01, RNFP02) | 1 (RNFP03) | 0 | 3 |
| Segurança | 3 (RNFS01, RNFS02, RNFS03) | 1 (RNFS04) | 0 | 4 |
| Disponibilidade | 2 (RNFD01, RNFD02) | 0 | 0 | 2 |
| Usabilidade | 2 (RNFU01, RNFU03, RNFU04) | 1 (RNFU02) | 0 | 4 |
| **Total RNF** | **9** | **3** | **0** | **13** |
| **%** | **69.2%** | **23.1%** | **0%** | **100%** |

### Consolidado Geral

| Prioridade | RF | RNF | Total | % do Total |
|------------|-----|-----|-------|------------|
| Must Have | 20 | 9 | 29 | 65.9% |
| Should Have | 10 | 3 | 13 | 29.5% |
| Could Have | 1 | 0 | 1 | 2.3% |
| Won't Have v1 | 0 | 0 | 0 | 0% |
| **Total** | **31** | **13** | **44** | **100%** |

---

## 8. Rastreabilidade

### Matriz de Rastreabilidade RF → Módulo Funcional

| ID | Título Resumido | Módulo | Origem na Demanda |
|----|----------------|--------|-------------------|
| RF101 | Submissão de Ideia | M1 | Demanda DEM-2026-006 — M1 |
| RF102 | Rascunho de Ideia | M1 | Boa prática UX — derivado M1 |
| RF103 | Identificação Avulsa vs. Campanha | M1/M2 | Demanda DEM-2026-006 — M1/M2 |
| RF104 | Edição de Rascunho | M1 | Boa prática — derivado M1 |
| RF105 | Acompanhamento de Status | M1 | Demanda DEM-2026-006 — M1 |
| RF106 | Notificação de Mudança de Status | M1 | Demanda DEM-2026-006 — M1 |
| RF201 | Criação de Campanha | M2 | Demanda DEM-2026-006 — M2 |
| RF202 | Encerramento Automático de Campanha | M2 | Demanda DEM-2026-006 — M2 |
| RF203 | Criação de Desafio com Restrições | M2 | Demanda DEM-2026-006 — M2 |
| RF204 | Diferenciação Visual Avulsa vs. Campanha | M2 | Demanda DEM-2026-006 — M2 |
| RF205 | Listagem e Filtro de Campanhas | M2 | Boa prática — derivado M2 |
| RF301 | Aprovação pelo Gestor de Área | M3 | Demanda DEM-2026-006 — M3 |
| RF302 | Aprovação de Investimento | M3 | Demanda DEM-2026-006 — M3 |
| RF303 | Aprovação Paralela de Partes Interessadas | M3 | Demanda DEM-2026-006 — M3 |
| RF304 | Histórico do Fluxo de Aprovação | M3 | Boa prática — rastreabilidade |
| RF305 | Prazo de Resposta dos Aprovadores | M3 | Boa prática — derivado M3 |
| RF306 | Rejeição com Motivo Obrigatório | M3 | Boa prática — qualidade do processo |
| RF401 | Criação de Plano de Ação | M4 | Demanda DEM-2026-006 — M4 |
| RF402 | Gerenciamento de Tarefas | M4 | Demanda DEM-2026-006 — M4 |
| RF403 | Atualização de Status das Tarefas | M4 | Demanda DEM-2026-006 — M4 |
| RF404 | Percentual de Progresso | M4 | Boa prática — derivado M4 |
| RF405 | Comentários no Plano | M4 | Boa prática — comunicação da equipe |
| RF501 | Registro de Ganhos Realizados | M5 | Demanda DEM-2026-006 — M5 |
| RF502 | Comparação Ganho Prometido vs. Realizado | M5 | Demanda DEM-2026-006 — M5 |
| RF503 | Métricas Agregadas do Programa | M5 | Demanda DEM-2026-006 — M5/M6 |
| RF504 | Histórico de Ganhos por Ideia | M5 | Boa prática — derivado M5 |
| RF601 | Dashboard do Colaborador | M6 | Demanda DEM-2026-006 — M6 |
| RF602 | Dashboard do Gestor de Inovação | M6 | Demanda DEM-2026-006 — M6 |
| RF603 | Dashboard do Gestor de Área | M6 | Demanda DEM-2026-006 — M6 |
| RF604 | Filtros e Busca no Dashboard | M6 | Boa prática — derivado M6 |
| RF605 | Exportação de Relatório | M6 | Demanda DEM-2026-006 — M6 |

---

## 9. Restrições e Premissas

### Restrições

| ID | Restrição | Impacto |
|----|-----------|---------|
| REST-01 | Prazo de entrega: Dezembro de 2026 | Escopo Should Have e Could Have pode ser cortado se necessário |
| REST-02 | Orçamento referência: ~R$100.000 | Arquitetura e tecnologias devem ser compatíveis com o budget |
| REST-03 | Sem integração com sistemas externos na v1 | Dados de usuários e estrutura hierárquica serão cadastrados manualmente ou via importação CSV |
| REST-04 | Sem aplicativo mobile na v1 | Interface web responsiva deve cobrir acesso via dispositivos móveis |
| REST-05 | Sem gamificação na v1 | Rankings, pontos e badges não serão desenvolvidos |

### Premissas

| ID | Premissa | Risco se falsa |
|----|----------|----------------|
| PREM-01 | A estrutura hierárquica (gestor de área de cada colaborador) estará disponível para importação antes do go-live | Fluxo de aprovação não funciona sem hierarquia definida |
| PREM-02 | A empresa possui servidor de e-mail (SMTP) disponível para envio de notificações | Notificações por e-mail (RF106, RF201, RF302 etc.) não funcionam |
| PREM-03 | O Gestor de Inovação participará de sessões de validação do protótipo antes do desenvolvimento | Risco de retrabalho de interface e fluxos |
| PREM-04 | A plataforma será hospedada em ambiente cloud com capacidade de escalar verticalmente | RNFP01, RNFP02, RNFD01 e RNFD02 dependem da infraestrutura adequada |
| PREM-05 | SSO corporativo estará disponível ou o time de TI fornecerá credenciais de teste antes do início do desenvolvimento | RNFS01 pode requerer fallback apenas por e-mail/senha |

---

## 10. Critérios de Aceite Globais

Os critérios a seguir são condição necessária para aceite do sistema pela VMO Consultoria, independente dos critérios por requisito:

1. **Cobertura de testes:** Todos os requisitos Must Have possuem caso de teste associado e aprovado em ambiente de homologação.
2. **Dados de teste:** O ambiente de homologação deve conter ao menos 50 ideias em diferentes estados para validação dos dashboards e métricas.
3. **Treinamento:** Manual do usuário e sessão de treinamento (mínimo 1 hora) para Gestores de Inovação e Administradores antes do go-live.
4. **Migração zero-impacto:** A transição para a nova plataforma deve ser planejada para não interromper programas de inovação em curso.
5. **Documentação técnica:** Documentação de API, arquitetura de banco de dados e guia de deploy entregues junto com o sistema.

---

## 11. Seção de Aprovação

Este documento deve ser aprovado pelo solicitante antes de prosseguir para a fase de design de solução e prototipagem.

---

**Aprovação do Solicitante**

| Campo | Preenchimento |
|-------|--------------|
| Nome completo | |
| Cargo | Gestor de Inovação |
| Data da aprovação | |
| Assinatura | |
| Observações / ressalvas | |

---

**Aprovação da Engenharia de Requisitos**

| Campo | Preenchimento |
|-------|--------------|
| Nome completo | Rafael Requisito |
| Cargo | Engenheiro de Requisitos — VMO Autônomo |
| Data | 2026-05-16 |
| Versão aprovada | 1.0 |

---

**Histórico de Revisões**

| Versão | Data | Autor | Alterações |
|--------|------|-------|-----------|
| 0.1 | 2026-05-16 | Rafael Requisito | Elicitação inicial — Task 1 (levantamento de RF e RNF) |
| 1.0 | 2026-05-16 | Rafael Requisito | Documento completo — Task 2 (ERF com critérios de aceitação, MoSCoW, glossário) |

---

*Documento gerado pelo agente Rafael Requisito — VMO Autônomo | PROJ-2026-006 | Fase 02 — Iniciação*
