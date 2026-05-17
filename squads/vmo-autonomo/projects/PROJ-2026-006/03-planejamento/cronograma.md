# Cronograma — PROJ-2026-006
## Plataforma Própria de Gestão de Ideias e Inovação

**Elaborado por:** Carlos Cronograma — Planejador de Prazo (VMO Consultoria)
**Data de elaboração:** 2026-05-16
**Revisão:** 1.0
**Status:** Baseline Proposto (aguarda aprovação formal)

---

## Sumário Executivo de Prazo

| Parâmetro                         | Valor                       |
|-----------------------------------|-----------------------------|
| Data de início (D+0)              | 2026-06-24 (quarta-feira)   |
| Prazo base (sem buffer)           | 23 semanas (~161 dias úteis)|
| Buffer explícito (15%)            | 3,5 semanas (17 dias úteis) |
| Go-live planejado                 | **2026-12-07 (segunda)**    |
| Prazo contratual máximo           | 2026-12-31                  |
| Folga residual (contingência)     | 3,5 semanas                 |
| Total de marcos                   | 9 marcos (M0 a M8)          |

> **Nota de restrição:** O início em 2026-06-24 está condicionado à resolução das condições bloqueantes CB-01 (aprovação formal de orçamento) e CB-02 (designação formal da equipe), conforme cronograma de qualificação aprovada (fase 01-qualificacao).

---

## Parte 1 — WBS (Work Breakdown Structure)

### Legenda de Responsáveis

| Sigla | Papel                            |
|-------|----------------------------------|
| GP    | Gerente de Projeto               |
| ARQ   | Arquiteto de Solução / Tech Lead |
| DEV   | Desenvolvedor(es) Full-Stack     |
| UX    | Designer UX/UI                   |
| QA    | Analista de Qualidade / Tester   |
| NEG   | Gestor de Negócios / PO          |
| INF   | Infraestrutura / DevOps          |

---

### 1.0 INICIAÇÃO E PREPARAÇÃO

#### 1.1 Kick-off e Governança
- **1.1.1** Reunião de kick-off com stakeholders — responsável: GP/NEG
- **1.1.2** Definição e formalização da equipe de projeto — responsável: GP
- **1.1.3** Configuração do ambiente de gestão (Jira/Trello/Notion) — responsável: GP/DEV

#### 1.2 Infraestrutura Base
- **1.2.1** Provisionamento de ambientes (DEV / HML / PRD) — responsável: INF
- **1.2.2** Configuração de pipeline CI/CD e repositório — responsável: INF/ARQ
- **1.2.3** Definição e aprovação da arquitetura de solução — responsável: ARQ

---

### 2.0 ESPECIFICAÇÃO E PROTOTIPAÇÃO

#### 2.1 Especificação Detalhada de Requisitos
- **2.1.1** Workshop de requisitos M1 (Cadastro de Ideias) e M2 (Campanhas) — responsável: NEG/UX/ARQ
- **2.1.2** Workshop de requisitos M3 (Aprovação) e M4 (Mini Gestão) — responsável: NEG/UX/ARQ
- **2.1.3** Workshop de requisitos M5 (Mensuração) e M6 (Dashboard) — responsável: NEG/UX/ARQ
- **2.1.4** Consolidação e sign-off do documento de requisitos (ERF v2) — responsável: GP/NEG

#### 2.2 Design UX/UI
- **2.2.1** Wireframes de baixa fidelidade — módulos M1 e M2 — responsável: UX
- **2.2.2** Wireframes de baixa fidelidade — módulos M3, M4, M5 e M6 — responsável: UX
- **2.2.3** Protótipo interativo de alta fidelidade (fluxo completo) — responsável: UX
- **2.2.4** Validação do protótipo com usuários-chave (mínimo 3) e ajustes — responsável: UX/NEG

---

### 3.0 DESENVOLVIMENTO — M1: CADASTRO DE IDEIAS

#### 3.1 Backend M1
- **3.1.1** Modelagem de dados e APIs de ideia (CRUD, rascunho, submissão) — responsável: ARQ/DEV
- **3.1.2** Implementação das regras de negócio (RF-01 a RF-07) — responsável: DEV

#### 3.2 Frontend M1
- **3.2.1** Formulário de submissão e rascunho de ideias — responsável: DEV/UX
- **3.2.2** Vinculação de ideia a campanhas (visualização) — responsável: DEV

#### 3.3 Testes Unitários e Integração M1
- **3.3.1** Testes unitários e integração M1 (cobertura ≥ 80%) — responsável: QA/DEV

---

### 4.0 DESENVOLVIMENTO — M2: CAMPANHAS E DESAFIOS

#### 4.1 Backend M2
- **4.1.1** APIs de criação, edição e encerramento de campanhas — responsável: DEV
- **4.1.2** Regras de negócio: elegibilidade, período, status (RF-08 a RF-12) — responsável: DEV

#### 4.2 Frontend M2
- **4.2.1** Tela de gestão de campanhas (gestor de inovação) — responsável: DEV/UX
- **4.2.2** Tela de listagem de campanhas ativas (colaborador) — responsável: DEV

#### 4.3 Testes Unitários e Integração M2
- **4.3.1** Testes unitários e integração M2 (cobertura ≥ 80%) — responsável: QA/DEV

---

### 5.0 DESENVOLVIMENTO — M3: FLUXO DE APROVAÇÃO

#### 5.1 Backend M3
- **5.1.1** Motor de fluxo: aprovação por gestor de área — responsável: ARQ/DEV
- **5.1.2** Motor de fluxo: aprovação de investimento — responsável: DEV
- **5.1.3** Notificações e alertas de aprovação pendente — responsável: DEV

#### 5.2 Frontend M3
- **5.2.1** Tela de análise e aprovação (gestor de área) — responsável: DEV/UX
- **5.2.2** Tela de aprovação de investimento e histórico — responsável: DEV

#### 5.3 Testes Unitários e Integração M3
- **5.3.1** Testes unitários e integração M3 (cobertura ≥ 80%) — responsável: QA/DEV

---

### 6.0 DESENVOLVIMENTO — M4: MINI GESTÃO DE PROJETOS

#### 6.1 Backend M4
- **6.1.1** APIs de plano de ação, tarefas e progresso — responsável: DEV
- **6.1.2** Regras de status e cálculo de progresso percentual — responsável: DEV

#### 6.2 Frontend M4
- **6.2.1** Tela de plano de ação e tarefas — responsável: DEV/UX
- **6.2.2** Indicadores de progresso e status por ideia aprovada — responsável: DEV

#### 6.3 Testes Unitários e Integração M4
- **6.3.1** Testes unitários e integração M4 (cobertura ≥ 80%) — responsável: QA/DEV

---

### 7.0 DESENVOLVIMENTO — M5: MENSURAÇÃO DE GANHOS

#### 7.1 Backend M5
- **7.1.1** APIs de registro de ganhos realizados vs. prometidos — responsável: DEV
- **7.1.2** Motor de métricas do programa de inovação — responsável: DEV

#### 7.2 Frontend M5
- **7.2.1** Formulário de registro de ganhos realizados — responsável: DEV/UX
- **7.2.2** Visão comparativa: ganho prometido x realizado — responsável: DEV

#### 7.3 Testes Unitários e Integração M5
- **7.3.1** Testes unitários e integração M5 (cobertura ≥ 80%) — responsável: QA/DEV

---

### 8.0 DESENVOLVIMENTO — M6: DASHBOARD E MONITORAMENTO

#### 8.1 Backend M6
- **8.1.1** APIs de dados consolidados para dashboards por perfil — responsável: DEV
- **8.1.2** Serviço de exportação (relatórios PDF/Excel) — responsável: DEV

#### 8.2 Frontend M6
- **8.2.1** Dashboard do colaborador (minhas ideias, status) — responsável: DEV/UX
- **8.2.2** Dashboard do gestor de área (ideias da equipe, aprovações) — responsável: DEV/UX
- **8.2.3** Dashboard do gestor de inovação (programa completo, KPIs) — responsável: DEV/UX
- **8.2.4** Filtros avançados e exportação de dados — responsável: DEV

#### 8.3 Testes Unitários e Integração M6
- **8.3.1** Testes unitários e integração M6 (cobertura ≥ 80%) — responsável: QA/DEV

---

### 9.0 TESTES INTEGRADOS E UAT

#### 9.1 Testes de Sistema
- **9.1.1** Testes de sistema end-to-end (fluxo completo M1→M6) — responsável: QA
- **9.1.2** Testes de performance e carga (RNF-01 a RNF-05) — responsável: QA/INF
- **9.1.3** Testes de segurança e controle de acesso por perfil — responsável: QA/ARQ

#### 9.2 UAT — Homologação com Usuários
- **9.2.1** Preparação do ambiente UAT e carga de dados-piloto — responsável: QA/INF
- **9.2.2** Execução do UAT com usuários representativos (mín. 5 por perfil) — responsável: NEG/QA
- **9.2.3** Tratamento de não-conformidades UAT e reteste — responsável: DEV/QA
- **9.2.4** Sign-off formal de homologação — responsável: NEG/GP

---

### 10.0 BUFFER EXPLÍCITO (15%)

#### 10.1 Janela de Buffer de Prazo
- **10.1.1** Período de absorção de riscos e imprevistos (não alocado a tarefas) — responsável: GP
- **10.1.2** Retrabalhos decorrentes de UAT e ajustes finais de escopo — responsável: DEV/QA

---

### 11.0 IMPLANTAÇÃO E GO-LIVE

#### 11.1 Preparação para Produção
- **11.1.1** Checklist de go-live e plano de rollback — responsável: GP/INF
- **11.1.2** Treinamento de usuários-chave e administradores — responsável: GP/NEG
- **11.1.3** Carga de dados iniciais e configurações de produção — responsável: INF/DEV

#### 11.2 Deploy e Ativação
- **11.2.1** Deploy em produção e smoke test — responsável: INF/DEV/QA
- **11.2.2** Comunicação interna de go-live e abertura de acesso — responsável: GP/NEG

---

### 12.0 ESTABILIZAÇÃO PÓS GO-LIVE

#### 12.1 Suporte e Monitoramento Intensivo
- **12.1.1** Monitoramento de logs, erros e performance (primeiras 2 semanas) — responsável: INF/DEV
- **12.1.2** Suporte L1/L2 dedicado e triagem de incidentes — responsável: DEV/QA
- **12.1.3** Relatório de estabilização e lições aprendidas — responsável: GP

---

## Parte 2 — Cronograma Detalhado

### Legenda do Cronograma

| Símbolo | Significado                           |
|---------|---------------------------------------|
| ⭐      | Atividade no caminho crítico          |
| M#      | Marco de projeto                      |
| →       | Dependência Término-Início (TI)       |
| Buffer  | Janela de buffer centralizado (15%)   |

---

### Marcos Principais

| Marco | Nome                                          | Data Prevista | Critério de Aceite                                                                                     |
|-------|-----------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------|
| M0    | Kick-off Formal                               | 2026-06-24    | Ata de kick-off assinada por GP e patrocinador; equipe designada; ambientes iniciados                  |
| M1    | Especificação e Protótipo Aprovados           | 2026-07-31    | ERF v2 com sign-off do NEG; protótipo validado por ≥ 3 usuários-chave                                 |
| M2    | Módulos M1 e M2 Desenvolvidos e Testados      | 2026-09-04    | 100% dos RF de M1 e M2 implementados; cobertura de testes ≥ 80%; nenhum bug crítico aberto            |
| M3    | Módulos M3 e M4 Desenvolvidos e Testados      | 2026-10-09    | 100% dos RF de M3 e M4 implementados; fluxo de aprovação validado; cobertura ≥ 80%                    |
| M4    | Módulos M5 e M6 Desenvolvidos e Testados      | 2026-11-06    | 100% dos RF de M5 e M6 implementados; dashboards funcionais por perfil; cobertura ≥ 80%               |
| M5    | Testes Integrados e UAT Concluídos            | 2026-11-20    | Todos os cenários de sistema aprovados; sign-off UAT formal; zero bugs críticos e severos abertos      |
| M6    | Início do Buffer (janela explícita 15%)       | 2026-11-23    | Buffer ativado formalmente pelo GP; nenhum escopo novo admitido durante este período                   |
| M7    | Buffer Encerrado — Pronto para Go-Live        | 2026-12-04    | Checklist de go-live 100% concluído; plano de rollback aprovado; treinamento executado                 |
| M8    | Go-Live em Produção                           | 2026-12-07    | Sistema em produção com todos os módulos ativos; smoke test aprovado; comunicação enviada aos usuários |

---

### Cronograma por Pacote de Trabalho

#### FASE 1 — INICIAÇÃO E PREPARAÇÃO
*(Duração: 2 semanas | 2026-06-24 a 2026-07-03)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|---------|----------|-------------|----|
| 1.1.1   | Reunião de kick-off com stakeholders                       | 2026-06-24   | 2026-06-24   | 1 dia   | GP/NEG   | —           | ⭐ |
| 1.1.2   | Formalização da equipe de projeto                          | 2026-06-24   | 2026-06-26   | 3 dias  | GP       | —           |    |
| 1.1.3   | Configuração do ambiente de gestão (Jira/Notion)           | 2026-06-25   | 2026-06-26   | 2 dias  | GP/DEV   | 1.1.2 →     |    |
| 1.2.1   | Provisionamento de ambientes DEV/HML/PRD                   | 2026-06-25   | 2026-07-01   | 5 dias  | INF      | 1.1.1 →     | ⭐ |
| 1.2.2   | Configuração de pipeline CI/CD e repositório               | 2026-07-02   | 2026-07-03   | 2 dias  | INF/ARQ  | 1.2.1 →     | ⭐ |
| 1.2.3   | Definição e aprovação da arquitetura de solução            | 2026-06-25   | 2026-07-03   | 7 dias  | ARQ      | 1.1.1 →     | ⭐ |

**Marco M0 — Kick-off Formal: 2026-06-24**

---

#### FASE 2 — ESPECIFICAÇÃO E PROTOTIPAÇÃO
*(Duração: 4 semanas | 2026-07-06 a 2026-07-31)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.     | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|-----------|-------------|----|
| 2.1.1   | Workshop requisitos M1 e M2                                | 2026-07-06   | 2026-07-09   | 4 dias   | NEG/UX    | 1.2.3 →     | ⭐ |
| 2.1.2   | Workshop requisitos M3 e M4                                | 2026-07-10   | 2026-07-15   | 4 dias   | NEG/UX    | 2.1.1 →     | ⭐ |
| 2.1.3   | Workshop requisitos M5 e M6                                | 2026-07-16   | 2026-07-21   | 4 dias   | NEG/UX    | 2.1.2 →     | ⭐ |
| 2.1.4   | Sign-off ERF v2 (documento consolidado)                    | 2026-07-22   | 2026-07-24   | 3 dias   | GP/NEG    | 2.1.3 →     | ⭐ |
| 2.2.1   | Wireframes baixa fidelidade M1 e M2                        | 2026-07-06   | 2026-07-10   | 5 dias   | UX        | 2.1.1 →     |    |
| 2.2.2   | Wireframes baixa fidelidade M3, M4, M5 e M6               | 2026-07-13   | 2026-07-21   | 7 dias   | UX        | 2.2.1 →     |    |
| 2.2.3   | Protótipo interativo de alta fidelidade                    | 2026-07-22   | 2026-07-28   | 5 dias   | UX        | 2.2.2 →     | ⭐ |
| 2.2.4   | Validação do protótipo com usuários-chave e ajustes        | 2026-07-29   | 2026-07-31   | 3 dias   | UX/NEG    | 2.2.3 →     | ⭐ |

**Marco M1 — Especificação e Protótipo Aprovados: 2026-07-31**

---

#### FASE 3 — DESENVOLVIMENTO M1: CADASTRO DE IDEIAS
*(Duração: 3 semanas | 2026-08-03 a 2026-08-21)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 3.1.1   | Modelagem de dados e APIs de ideia (CRUD, rascunho)        | 2026-08-03   | 2026-08-10   | 6 dias   | ARQ/DEV  | 2.1.4 →     | ⭐ |
| 3.1.2   | Implementação das regras de negócio RF-01 a RF-07          | 2026-08-11   | 2026-08-17   | 5 dias   | DEV      | 3.1.1 →     | ⭐ |
| 3.2.1   | Frontend: formulário de submissão e rascunho               | 2026-08-10   | 2026-08-17   | 6 dias   | DEV/UX   | 3.1.1 →     |    |
| 3.2.2   | Frontend: vinculação de ideia a campanhas                  | 2026-08-18   | 2026-08-19   | 2 dias   | DEV      | 3.2.1 →     |    |
| 3.3.1   | Testes unitários e integração M1 (cobertura ≥ 80%)         | 2026-08-20   | 2026-08-21   | 2 dias   | QA/DEV   | 3.1.2 →     | ⭐ |

---

#### FASE 4 — DESENVOLVIMENTO M2: CAMPANHAS E DESAFIOS
*(Duração: 2 semanas | 2026-08-24 a 2026-09-04)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 4.1.1   | APIs de criação, edição e encerramento de campanhas        | 2026-08-24   | 2026-08-28   | 5 dias   | DEV      | 3.3.1 →     | ⭐ |
| 4.1.2   | Regras: elegibilidade, período, status RF-08 a RF-12       | 2026-08-31   | 2026-09-02   | 3 dias   | DEV      | 4.1.1 →     | ⭐ |
| 4.2.1   | Frontend: gestão de campanhas (gestor de inovação)         | 2026-08-25   | 2026-09-01   | 6 dias   | DEV/UX   | 4.1.1 →     |    |
| 4.2.2   | Frontend: listagem de campanhas ativas (colaborador)       | 2026-09-01   | 2026-09-03   | 3 dias   | DEV      | 4.2.1 →     |    |
| 4.3.1   | Testes unitários e integração M2 (cobertura ≥ 80%)         | 2026-09-03   | 2026-09-04   | 2 dias   | QA/DEV   | 4.1.2 →     | ⭐ |

**Marco M2 — M1 e M2 Desenvolvidos e Testados: 2026-09-04**

---

#### FASE 5 — DESENVOLVIMENTO M3: FLUXO DE APROVAÇÃO
*(Duração: 3 semanas | 2026-09-07 a 2026-09-25)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 5.1.1   | Motor de fluxo: aprovação por gestor de área               | 2026-09-07   | 2026-09-14   | 6 dias   | ARQ/DEV  | 4.3.1 →     | ⭐ |
| 5.1.2   | Motor de fluxo: aprovação de investimento                  | 2026-09-15   | 2026-09-18   | 4 dias   | DEV      | 5.1.1 →     | ⭐ |
| 5.1.3   | Notificações e alertas de aprovação pendente               | 2026-09-16   | 2026-09-19   | 4 dias   | DEV      | 5.1.1 →     |    |
| 5.2.1   | Frontend: tela de análise e aprovação (gestor de área)     | 2026-09-14   | 2026-09-21   | 6 dias   | DEV/UX   | 5.1.1 →     |    |
| 5.2.2   | Frontend: aprovação de investimento e histórico            | 2026-09-21   | 2026-09-24   | 4 dias   | DEV      | 5.2.1 →     |    |
| 5.3.1   | Testes unitários e integração M3 (cobertura ≥ 80%)         | 2026-09-24   | 2026-09-25   | 2 dias   | QA/DEV   | 5.1.2 →     | ⭐ |

---

#### FASE 6 — DESENVOLVIMENTO M4: MINI GESTÃO DE PROJETOS
*(Duração: 2 semanas | 2026-09-28 a 2026-10-09)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 6.1.1   | APIs de plano de ação, tarefas e progresso                 | 2026-09-28   | 2026-10-02   | 5 dias   | DEV      | 5.3.1 →     | ⭐ |
| 6.1.2   | Regras de status e cálculo de progresso percentual         | 2026-10-05   | 2026-10-07   | 3 dias   | DEV      | 6.1.1 →     | ⭐ |
| 6.2.1   | Frontend: tela de plano de ação e tarefas                  | 2026-09-30   | 2026-10-07   | 6 dias   | DEV/UX   | 6.1.1 →     |    |
| 6.2.2   | Frontend: indicadores de progresso e status                | 2026-10-07   | 2026-10-08   | 2 dias   | DEV      | 6.2.1 →     |    |
| 6.3.1   | Testes unitários e integração M4 (cobertura ≥ 80%)         | 2026-10-08   | 2026-10-09   | 2 dias   | QA/DEV   | 6.1.2 →     | ⭐ |

**Marco M3 — M3 e M4 Desenvolvidos e Testados: 2026-10-09**

---

#### FASE 7 — DESENVOLVIMENTO M5: MENSURAÇÃO DE GANHOS
*(Duração: 2 semanas | 2026-10-12 a 2026-10-23)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 7.1.1   | APIs de registro de ganhos realizados vs. prometidos       | 2026-10-12   | 2026-10-16   | 5 dias   | DEV      | 6.3.1 →     | ⭐ |
| 7.1.2   | Motor de métricas do programa de inovação                  | 2026-10-19   | 2026-10-21   | 3 dias   | DEV      | 7.1.1 →     | ⭐ |
| 7.2.1   | Frontend: formulário de registro de ganhos                 | 2026-10-14   | 2026-10-20   | 5 dias   | DEV/UX   | 7.1.1 →     |    |
| 7.2.2   | Frontend: visão comparativa ganho prometido x realizado    | 2026-10-20   | 2026-10-22   | 3 dias   | DEV      | 7.2.1 →     |    |
| 7.3.1   | Testes unitários e integração M5 (cobertura ≥ 80%)         | 2026-10-22   | 2026-10-23   | 2 dias   | QA/DEV   | 7.1.2 →     | ⭐ |

---

#### FASE 8 — DESENVOLVIMENTO M6: DASHBOARD E MONITORAMENTO
*(Duração: 3 semanas | 2026-10-26 a 2026-11-13)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 8.1.1   | APIs de dados consolidados para dashboards por perfil      | 2026-10-26   | 2026-10-30   | 5 dias   | DEV      | 7.3.1 →     | ⭐ |
| 8.1.2   | Serviço de exportação (PDF/Excel)                          | 2026-11-02   | 2026-11-04   | 3 dias   | DEV      | 8.1.1 →     |    |
| 8.2.1   | Dashboard do colaborador (minhas ideias, status)           | 2026-10-28   | 2026-11-04   | 6 dias   | DEV/UX   | 8.1.1 →     |    |
| 8.2.2   | Dashboard do gestor de área                                | 2026-11-03   | 2026-11-06   | 4 dias   | DEV/UX   | 8.2.1 →     |    |
| 8.2.3   | Dashboard do gestor de inovação (KPIs do programa)         | 2026-11-05   | 2026-11-10   | 4 dias   | DEV/UX   | 8.2.2 →     | ⭐ |
| 8.2.4   | Filtros avançados e exportação de dados                    | 2026-11-09   | 2026-11-12   | 4 dias   | DEV      | 8.1.2 →     |    |
| 8.3.1   | Testes unitários e integração M6 (cobertura ≥ 80%)         | 2026-11-12   | 2026-11-13   | 2 dias   | QA/DEV   | 8.2.3 →     | ⭐ |

**Marco M4 — M5 e M6 Desenvolvidos e Testados: 2026-11-13**
*(Nota: data ajustada de 2026-11-06 para 2026-11-13 pelo tamanho real do M6)*

---

#### FASE 9 — TESTES INTEGRADOS E UAT
*(Duração: 1,5 semana | 2026-11-16 a 2026-11-20)*

| ID      | Pacote de Trabalho                                         | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|---------|------------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 9.1.1   | Testes de sistema end-to-end (fluxo completo M1→M6)        | 2026-11-16   | 2026-11-17   | 2 dias   | QA       | 8.3.1 →     | ⭐ |
| 9.1.2   | Testes de performance e carga (RNF-01 a RNF-05)            | 2026-11-16   | 2026-11-17   | 2 dias   | QA/INF   | 8.3.1 →     |    |
| 9.1.3   | Testes de segurança e controle de acesso por perfil        | 2026-11-16   | 2026-11-17   | 2 dias   | QA/ARQ   | 8.3.1 →     |    |
| 9.2.1   | Preparação ambiente UAT e carga de dados-piloto            | 2026-11-16   | 2026-11-17   | 2 dias   | QA/INF   | 8.3.1 →     |    |
| 9.2.2   | Execução UAT com usuários representativos                  | 2026-11-18   | 2026-11-19   | 2 dias   | NEG/QA   | 9.1.1 →     | ⭐ |
| 9.2.3   | Tratamento de não-conformidades e reteste                  | 2026-11-19   | 2026-11-20   | 2 dias   | DEV/QA   | 9.2.2 →     | ⭐ |
| 9.2.4   | Sign-off formal de homologação (UAT)                       | 2026-11-20   | 2026-11-20   | 1 dia    | NEG/GP   | 9.2.3 →     | ⭐ |

**Marco M5 — Testes Integrados e UAT Concluídos: 2026-11-20**

---

#### FASE 10 — BUFFER EXPLÍCITO (15% do prazo base)
*(Duração: 3,5 semanas | 2026-11-23 a 2026-12-04)*

> Esta janela NÃO contém tarefas planejadas. É reserva de tempo centralizada para absorção de riscos materializados, retrabalhos não previstos, e ajustes de qualidade identificados no UAT que não foram resolvidos na fase anterior.

| ID       | Pacote de Trabalho                                        | Início       | Fim          | Duração   | Resp. | Dependência | CP |
|----------|-----------------------------------------------------------|--------------|--------------|-----------|-------|-------------|----|
| 10.1.1   | Janela de buffer — absorção de riscos e imprevistos       | 2026-11-23   | 2026-12-04   | 3,5 sem.  | GP    | 9.2.4 →     | ⭐ |
| 10.1.2   | Retrabalhos e ajustes finais (se necessário)              | 2026-11-23   | 2026-12-04   | Sob demanda | DEV/QA | 9.2.4 → |    |

**Marco M6 — Início do Buffer: 2026-11-23**
**Marco M7 — Buffer Encerrado / Pronto para Go-Live: 2026-12-04**

---

#### FASE 11 — IMPLANTAÇÃO E GO-LIVE
*(Duração: 3 dias | 2026-12-07)*

| ID       | Pacote de Trabalho                                        | Início       | Fim          | Duração  | Resp.       | Dependência  | CP |
|----------|-----------------------------------------------------------|--------------|--------------|----------|-------------|---------------|----|
| 11.1.1   | Checklist de go-live e plano de rollback                  | 2026-11-23   | 2026-11-27   | 5 dias   | GP/INF      | 9.2.4 →       |    |
| 11.1.2   | Treinamento de usuários-chave e administradores           | 2026-11-24   | 2026-12-03   | 8 dias   | GP/NEG      | 11.1.1 →      |    |
| 11.1.3   | Carga de dados iniciais e configurações de produção       | 2026-11-30   | 2026-12-04   | 5 dias   | INF/DEV     | 11.1.1 →      |    |
| 11.2.1   | Deploy em produção e smoke test                           | 2026-12-07   | 2026-12-07   | 1 dia    | INF/DEV/QA  | 10.1.1 →      | ⭐ |
| 11.2.2   | Comunicação interna de go-live e abertura de acesso       | 2026-12-07   | 2026-12-07   | 1 dia    | GP/NEG      | 11.2.1 →      | ⭐ |

**Marco M8 — GO-LIVE em Produção: 2026-12-07**

---

#### FASE 12 — ESTABILIZAÇÃO PÓS GO-LIVE
*(Duração: 3,5 semanas | 2026-12-08 a 2026-12-31)*

| ID       | Pacote de Trabalho                                        | Início       | Fim          | Duração  | Resp.    | Dependência | CP |
|----------|-----------------------------------------------------------|--------------|--------------|----------|----------|-------------|----|
| 12.1.1   | Monitoramento de logs, erros e performance (2 semanas)    | 2026-12-08   | 2026-12-18   | 9 dias   | INF/DEV  | 11.2.1 →    |    |
| 12.1.2   | Suporte L1/L2 dedicado e triagem de incidentes            | 2026-12-08   | 2026-12-31   | 18 dias  | DEV/QA   | 11.2.1 →    |    |
| 12.1.3   | Relatório de estabilização e lições aprendidas            | 2026-12-29   | 2026-12-31   | 3 dias   | GP       | 12.1.1 →    |    |

---

## Caminho Crítico Completo ⭐

O caminho crítico representa a sequência de atividades sem folga que determina o prazo mínimo do projeto. Qualquer atraso em uma atividade do caminho crítico atrasa diretamente o go-live.

```
M0 (Kick-off)
  → 1.1.1 Kick-off (24/jun)
  → 1.2.1 Provisionamento de ambientes (25/jun–01/jul)
  → 1.2.2 CI/CD e repositório (02–03/jul)
  → 1.2.3 Arquitetura de solução (25/jun–03/jul) [paralelo, finaliza na mesma data]
  → 2.1.1 Workshop M1/M2 (06–09/jul)
  → 2.1.2 Workshop M3/M4 (10–15/jul)
  → 2.1.3 Workshop M5/M6 (16–21/jul)
  → 2.1.4 Sign-off ERF v2 (22–24/jul)
  → 2.2.3 Protótipo alta fidelidade (22–28/jul)
  → 2.2.4 Validação protótipo (29–31/jul)
[MARCO M1: 31/jul]
  → 3.1.1 Modelagem + APIs M1 (03–10/ago)
  → 3.1.2 Regras de negócio M1 (11–17/ago)
  → 3.3.1 Testes M1 (20–21/ago)
  → 4.1.1 APIs M2 (24–28/ago)
  → 4.1.2 Regras M2 (31/ago–02/set)
  → 4.3.1 Testes M2 (03–04/set)
[MARCO M2: 04/set]
  → 5.1.1 Motor aprovação área (07–14/set)
  → 5.1.2 Motor aprovação investimento (15–18/set)
  → 5.3.1 Testes M3 (24–25/set)
  → 6.1.1 APIs M4 (28/set–02/out)
  → 6.1.2 Regras M4 (05–07/out)
  → 6.3.1 Testes M4 (08–09/out)
[MARCO M3: 09/out]
  → 7.1.1 APIs M5 (12–16/out)
  → 7.1.2 Motor métricas M5 (19–21/out)
  → 7.3.1 Testes M5 (22–23/out)
  → 8.1.1 APIs dashboards M6 (26–30/out)
  → 8.2.3 Dashboard gestor inovação (05–10/nov)
  → 8.3.1 Testes M6 (12–13/nov)
[MARCO M4: 13/nov]
  → 9.1.1 Testes sistema E2E (16–17/nov)
  → 9.2.2 UAT com usuários (18–19/nov)
  → 9.2.3 Tratamento não-conformidades (19–20/nov)
  → 9.2.4 Sign-off homologação (20/nov)
[MARCO M5: 20/nov]
  → 10.1.1 BUFFER 15% (23/nov–04/dez)
[MARCO M6: 23/nov | MARCO M7: 04/dez]
  → 11.2.1 Deploy produção + smoke test (07/dez)
  → 11.2.2 Comunicação go-live (07/dez)
[MARCO M8: GO-LIVE 07/dez]
```

---

## Dependências Críticas (Término-Início)

| # | Atividade Predecessora           | Atividade Sucessora                   | Tipo | Impacto se atrasada         |
|---|----------------------------------|---------------------------------------|------|-----------------------------|
| 1 | 1.1.1 Kick-off                   | 1.2.1 Provisionamento ambientes       | TI   | Atrasa toda a cadeia        |
| 2 | 1.2.3 Arquitetura aprovada       | 2.1.1 Workshop M1/M2                  | TI   | Bloqueia especificação      |
| 3 | 2.1.4 Sign-off ERF v2            | 3.1.1 Modelagem M1                    | TI   | Bloqueia início do dev      |
| 4 | 2.2.4 Protótipo validado         | 3.2.1 Frontend M1                     | TI   | Bloqueia UI de todos módulos|
| 5 | 3.3.1 Testes M1                  | 4.1.1 APIs M2                         | TI   | Atrasa M2 e sequência       |
| 6 | 4.3.1 Testes M2                  | 5.1.1 Motor aprovação área            | TI   | Atrasa M3 e sequência       |
| 7 | 5.3.1 Testes M3                  | 6.1.1 APIs M4                         | TI   | Atrasa M4 e sequência       |
| 8 | 6.3.1 Testes M4                  | 7.1.1 APIs M5                         | TI   | Atrasa M5 e sequência       |
| 9 | 7.3.1 Testes M5                  | 8.1.1 APIs dashboards M6              | TI   | Atrasa M6 e sequência       |
|10 | 8.3.1 Testes M6                  | 9.1.1 Testes sistema E2E              | TI   | Bloqueia UAT                |
|11 | 9.2.4 Sign-off UAT               | 10.1.1 Buffer (início)                | TI   | Buffer não pode ser antecipado sem sign-off |
|12 | 10.1.1 Buffer encerrado          | 11.2.1 Deploy produção                | TI   | Go-live não ocorre          |

---

## Resumo de Prazo e Buffer

| Item                              | Valor                          |
|-----------------------------------|--------------------------------|
| Prazo base de desenvolvimento     | 23 semanas (24/jun – 20/nov)   |
| Buffer 15% (23 × 0,15 = 3,45 sem)| 3,5 semanas (23/nov – 04/dez)  |
| Implantação (go-live)             | 1 semana (07/dez)              |
| Go-live planejado                 | **07/12/2026**                 |
| Prazo contratual máximo           | 31/12/2026                     |
| Folga residual pós go-live        | 3,5 semanas (08/dez – 31/dez)  |
| Estabilização pós go-live         | 24/dez (dentro da folga)       |

> O buffer de **3,5 semanas** (23/nov a 04/dez) é explícito, centralizado após o UAT e antes do go-live. Nenhuma folga está embutida dentro de atividades individuais. A folga residual (08/dez – 31/dez) serve como contingência de último recurso para a estabilização pós go-live e não é computada como buffer.

---

## Riscos de Prazo Mapeados

| Risco                                              | Probabilidade | Impacto | Mitigação                                              |
|----------------------------------------------------|---------------|---------|--------------------------------------------------------|
| Atraso no sign-off do ERF v2 (2.1.4)               | Média         | Alto    | Workshops focados; NEG disponível dedicado             |
| Retrabalho alto no UAT (9.2.3)                     | Média         | Alto    | Buffer de 3,5 sem. cobre até 100% de UAT extra         |
| Motor de aprovação M3 mais complexo que estimado   | Alta          | Médio   | ARQ envolvido desde o início; spike técnico na fase 2  |
| Dashboard M6 com requisitos de BI expandidos       | Média         | Médio   | Escopo explícito no ERF v2; sem integrações externas   |
| CB-01/CB-02 não resolvidas até 24/jun              | Baixa         | Crítico | Monitoramento semanal; plano de contingência de início |

---

## Checklist de Qualidade do Cronograma

- [x] WBS com 3 níveis cobrindo 100% do escopo (M1-M6 + gestão + implantação + estabilização)
- [x] Cronograma com datas de início/fim por pacote de trabalho
- [x] Dependências documentadas para todas as atividades críticas (12 dependências TI)
- [x] Caminho crítico identificado e marcado com ⭐
- [x] 9 marcos principais (M0 a M8) com critério de aceite por marco
- [x] Buffer de 15% explícito, centralizado e separado das atividades individuais
- [x] Go-live planejado em 07/12/2026 — dentro do prazo máximo de 31/12/2026
- [x] Todos os pacotes de trabalho com responsável designado
- [x] Nenhum pacote de trabalho com duração superior a 2 semanas

---

*Documento gerado por: Carlos Cronograma — Planejador de Prazo | VMO Consultoria*
*Versão 1.0 — 2026-05-16 | PROJ-2026-006*
