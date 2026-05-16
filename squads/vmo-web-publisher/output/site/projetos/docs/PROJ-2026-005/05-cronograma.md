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
