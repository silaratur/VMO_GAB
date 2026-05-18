# Documentação de Iniciação de Projeto
**Código:** PROJ-2026-004
**Data de Emissão:** 2026-05-14
**Responsável pela Documentação:** Diana Documento — PMO/VMO Consultoria

---

# DOCUMENTO 1 — TERMO DE ABERTURA DO PROJETO (TAP)

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Informação |
|---|---|
| Código do Projeto | PROJ-2026-004 |
| Nome do Projeto | Plataforma Interna de Gestão de Ideias de Inovação |
| Data de Emissão | 2026-05-14 |
| Solicitante | Jadson — Área de Inovação, Grupo Águia Branca |
| Sponsor | A DEFINIR *(condição bloqueante para início)* |
| Gerente do Projeto | A DESIGNAR *(pós aprovação do TAP e confirmação de sponsor)* |
| Empresa Contratante | VMO Consultoria |
| Cliente/Beneficiário | Grupo Águia Branca (holding, VixPar, VAB e divisões de comércio) |
| Qualificação do Projeto | 21/30 — 70% — **APROVADO COM CONDIÇÕES** |

---

## 2. OBJETIVO SMART

Desenvolver e entregar em produção uma plataforma web interna de gestão de ideias de inovação para o Grupo Águia Branca, com capacidade para atender 100% dos colaboradores da holding e divisões (estimado em 10.000+ usuários), contemplando cadastro de ideias, fluxo de aprovação gerencial, campanhas/desafios, módulo de gestão de projetos de implementação e módulo de mensuração de ganhos, **até 30 de novembro de 2026**, com investimento máximo de R$ 90.000,00 (noventa mil reais), eliminando o custo anual de R$ 80.000–90.000 com a plataforma terceirizada atualmente em uso.

**Critério de conclusão:** Plataforma em produção, validada em testes de aceitação pelo time de inovação, com ao menos 80% das funcionalidades requeridas homologadas pelo solicitante, disponível para acesso de todos os colaboradores antes do Prêmio Inovação de janeiro/2027.

---

## 3. JUSTIFICATIVA DE NEGÓCIO

O Grupo Águia Branca opera atualmente com plataforma terceirizada de gestão de ideias de inovação com custo anual de R$ 80.000–90.000 e modelo de licenciamento restritivo, que limita o número de usuários e inibe a democratização da inovação em todas as divisões do grupo.

A substituição por uma solução proprietária elimina o custo recorrente, remove a restrição de acesso, possibilita evolução contínua sem dependência de fornecedor externo e alinha-se ao objetivo estratégico do grupo de fortalecer a cultura de inovação com o Prêmio Inovação (janeiro/2027) como marco institucional.

O investimento de até R$ 90.000 se paga integralmente no primeiro ano de operação, com payback imediato a partir da descontinuação da plataforma terceirizada.

---

## 4. ESCOPO DO PROJETO

### 4.1 ESTÁ DENTRO DO ESCOPO

- Portal web responsivo de cadastro de ideias com campos: descrição do problema, ganhos esperados e benefícios
- Módulo de campanhas e desafios de inovação, gerenciáveis pelo time de inovação
- Fluxo de aprovação de ideias pelo gestor da área do colaborador proponente
- Módulo de mini gestão de projetos para acompanhamento da implementação de ideias aprovadas
- Módulo de mensuração e registro de ganhos obtidos com as ideias implementadas
- Gestão de perfis de usuários com controle de acesso por papel (colaborador, gestor, time de inovação, administrador)
- Capacidade de atendimento a todos os colaboradores do Grupo Águia Branca (holding + VixPar + VAB + divisões de comércio)
- Testes de aceitação com o time de inovação
- Documentação técnica e manual do usuário
- Implantação em ambiente de produção
- Treinamento do time de inovação e administradores da plataforma

### 4.2 ESTÁ FORA DO ESCOPO

- Integração com sistemas legados do Grupo Águia Branca (ERP, RH, folha de pagamento) — avaliação futura
- Integração com plataformas externas de inovação ou crowdsourcing
- Aplicativo mobile nativo (iOS/Android) — avaliação futura
- Migração de dados históricos da plataforma terceirizada atual
- Suporte técnico pós-implantação além do período de garantia (90 dias)
- Desenvolvimento de funcionalidades não listadas no escopo sem aprovação formal de mudança
- Treinamento presencial para todos os colaboradores (responsabilidade das divisões)
- Hospedagem e infraestrutura de produção (a cargo da área de TI do Grupo)

---

## 5. CRITÉRIOS DE SUCESSO

| # | Critério | Métrica / Evidência | Meta |
|---|---|---|---|
| CS-01 | Entrega em produção dentro do prazo | Data de go-live registrada | Até 30/11/2026 |
| CS-02 | Entrega dentro do orçamento aprovado | Custo total realizado | ≤ R$ 90.000,00 |
| CS-03 | Cobertura funcional homologada | % de funcionalidades requeridas aprovadas em UAT | ≥ 80% |
| CS-04 | Escalabilidade para todos os colaboradores | Teste de carga com usuários simultâneos | Suportar 500 usuários simultâneos sem degradação |
| CS-05 | Satisfação do solicitante | Avaliação formal pós-implantação | Nota ≥ 4,0/5,0 pelo time de inovação |
| CS-06 | Eliminação do custo recorrente | Cancelamento contratual da plataforma terceirizada | Confirmado até jan/2027 |
| CS-07 | Prazo de aprovação de ideias | Tempo médio de ciclo ideia → aprovação/rejeição | ≤ 7 dias úteis em operação normal |

---

## 6. STAKEHOLDERS

| Papel | Nome / Área | Tipo de Envolvimento |
|---|---|---|
| Solicitante | Jadson — Área de Inovação / Grupo Águia Branca | Decisor de requisitos, ponto focal, homologação |
| Sponsor | A DEFINIR *(condição bloqueante)* | Aprovação de orçamento, patrocínio executivo |
| Gerente do Projeto | A DESIGNAR — VMO Consultoria | Planejamento, execução, controle e entrega |
| Time de Inovação | Grupo Águia Branca | Usuários-chave, validação e homologação |
| Gestores de Área | Todas as divisões do Grupo | Usuários do fluxo de aprovação |
| Colaboradores | Holding, VixPar, VAB e divisões de comércio | Usuários finais do portal de ideias |
| TI / Infraestrutura | Grupo Águia Branca | Hospedagem, segurança e suporte de ambiente |
| PMO / VMO Consultoria | VMO Consultoria | Governança, documentação e qualidade |
| Fornecedor Atual | Plataforma terceirizada (a ser descontinuada) | Referência de funcionalidades e transição |

---

## 7. PREMISSAS

| # | Premissa |
|---|---|
| P-01 | O sponsor será identificado e formalmente designado antes do início da fase de planejamento detalhado |
| P-02 | O orçamento de até R$ 90.000 será aprovado antes do início da execução |
| P-03 | A área de TI do Grupo Águia Branca provisionará ambiente de homologação e produção sem custo adicional ao projeto |
| P-04 | O solicitante (Jadson) estará disponível para validações e aprovações ao longo do projeto |
| P-05 | O modelo de execução (equipe interna VMO, squads externos ou híbrido) será definido até o kick-off |
| P-06 | Não haverá integrações com sistemas legados no escopo desta fase |
| P-07 | Os colaboradores do Grupo têm acesso à internet corporativa para uso do portal web |
| P-08 | O prazo de 30/11/2026 é fixo e não negociável, dado o Prêmio Inovação em jan/2027 |

---

## 8. RESTRIÇÕES

| # | Restrição |
|---|---|
| R-01 | Orçamento máximo: R$ 90.000,00 (teto equivalente ao custo anual da plataforma atual) |
| R-02 | Prazo final: 30 de novembro de 2026 — inegociável |
| R-03 | Sponsor e orçamento são condições bloqueantes para início da execução |
| R-04 | Nenhuma integração com sistemas legados no escopo desta fase |
| R-05 | Modelo de execução ainda não definido — impacta planejamento de recursos |
| R-06 | A solução deve ser proprietária (não SaaS terceirizado) para eliminar custo recorrente |
| R-07 | Treinamento de todos os colaboradores não está no escopo da VMO — responsabilidade das divisões |

---

## 9. ORÇAMENTO ESTIMADO

| Item | Valor Estimado |
|---|---|
| Desenvolvimento da plataforma | R$ 60.000,00 |
| Testes, UAT e homologação | R$ 8.000,00 |
| Implantação e go-live | R$ 5.000,00 |
| Treinamento (time de inovação e admins) | R$ 2.000,00 |
| Documentação técnica e manuais | R$ 0,00 *(incluso no desenvolvimento)* |
| Gestão do projeto (GP) | R$ 0,00 *(a definir conforme modelo de execução)* |
| **Subtotal** | **R$ 75.000,00** |
| **Contingência (20%)** | **R$ 15.000,00** |
| **TOTAL COM CONTINGÊNCIA** | **R$ 90.000,00** |

> **Nota:** O orçamento total com contingência (R$ 90.000,00) coincide com o teto aprovável (custo anual da plataforma terceirizada). O uso da contingência requer aprovação formal do sponsor.
> **Status:** Orçamento NÃO aprovado. Aprovação pelo sponsor é condição bloqueante para início da execução.

---

## 10. CRONOGRAMA DE ALTO NÍVEL — MARCOS

| Marco | Descrição | Data Prevista |
|---|---|---|
| M-00 | Emissão e aprovação do TAP | 2026-05-14 *(este documento — pendente assinaturas)* |
| M-01 | Definição de sponsor e modelo de execução | Até 2026-06-13 |
| M-02 | Aprovação de orçamento | Até 2026-06-13 |
| M-03 | Kick-off oficial do projeto | 2026-06-16 |
| M-04 | Conclusão do planejamento detalhado e backlog | 2026-06-30 |
| M-05 | Entrega do MVP (portal de ideias + aprovação gerencial) | 2026-08-31 |
| M-06 | Entrega do módulo de campanhas e desafios | 2026-09-30 |
| M-07 | Entrega do módulo de gestão de projetos e mensuração | 2026-10-31 |
| M-08 | Testes de aceitação (UAT) | 2026-11-14 |
| M-09 | Go-live em produção | **2026-11-30** |
| M-10 | Encerramento do projeto e relatório final | 2026-12-15 |

---

## 11. ASSINATURAS

*Os campos abaixo devem ser preenchidos após designação formal dos responsáveis.*

| Papel | Nome | Assinatura | Data |
|---|---|---|---|
| Gerente do Projeto | _________________________ | _________________________ | ____/____/_____ |
| Sponsor | _________________________ | _________________________ | ____/____/_____ |
| Solicitante | Jadson | _________________________ | ____/____/_____ |
| PMO / VMO Consultoria | _________________________ | _________________________ | ____/____/_____ |

---
---

# DOCUMENTO 2 — PM CANVAS

**Projeto:** PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação
**Data:** 2026-05-14
**Versão:** 1.0

---

## BLOCO 1 — JUSTIFICATIVA (Por que fazer?)

O Grupo Águia Branca desembolsa R$ 80.000–90.000/ano em plataforma terceirizada de gestão de ideias com licenciamento restrito, que impede o acesso de todos os colaboradores e limita a escala da cultura de inovação. O desenvolvimento de solução proprietária elimina o custo recorrente com payback imediato no primeiro ano, remove restrições de licenciamento, confere autonomia evolutiva à organização e suporta o Prêmio Inovação (jan/2027) como marco institucional. A qualificação do projeto atingiu 70% (aprovado com condições), confirmando viabilidade estratégica condicionada à definição de sponsor, orçamento e modelo de execução.

---

## BLOCO 2 — PRODUTO / RESULTADO (O que entregar?)

**Plataforma web interna de gestão de ideias de inovação**, composta por:

1. **Portal de Ideias:** Cadastro de ideias com campos estruturados (problema, ganhos e benefícios esperados)
2. **Módulo de Campanhas/Desafios:** Gestão de campanhas temáticas lançadas pelo time de inovação
3. **Fluxo de Aprovação Gerencial:** Workflow de aprovação/rejeição de ideias pelo gestor da área do proponente
4. **Módulo de Mini Gestão de Projetos:** Acompanhamento da implementação de ideias aprovadas
5. **Módulo de Mensuração de Ganhos:** Registro e acompanhamento dos resultados obtidos
6. **Gestão de Usuários e Perfis:** Controle de acesso por papel (colaborador, gestor, time de inovação, admin)

**Entregável final:** Plataforma em produção, documentada, treinamento dos administradores e time de inovação concluído, com 100% dos módulos homologados pelo solicitante.

---

## BLOCO 3 — OBJETIVO SMART

Desenvolver e entregar em produção uma plataforma web interna de gestão de ideias de inovação para o Grupo Águia Branca, com capacidade para atender 100% dos colaboradores da holding e divisões, contemplando os 5 módulos funcionais definidos no escopo, **até 30 de novembro de 2026**, com investimento máximo de **R$ 90.000,00**, obtendo homologação de pelo menos 80% das funcionalidades pelo time de inovação em UAT formal e nota de satisfação ≥ 4,0/5,0, eliminando o custo anual de R$ 80.000–90.000 com plataforma terceirizada.

---

## BLOCO 4 — REQUISITOS PRINCIPAIS

| Código | Requisito | Prioridade |
|---|---|---|
| REQ-01 | Portal web acessível por qualquer colaborador do Grupo sem limitação de licença | Alta |
| REQ-02 | Cadastro de ideias com campos: descrição do problema, ganhos esperados, benefícios | Alta |
| REQ-03 | Fluxo de aprovação pelo gestor direto da área do colaborador proponente | Alta |
| REQ-04 | Módulo de campanhas e desafios gerenciáveis pelo time de inovação | Alta |
| REQ-05 | Módulo de gestão de projetos para acompanhar implementação de ideias aprovadas | Alta |
| REQ-06 | Módulo de mensuração e registro de ganhos obtidos com ideias implementadas | Alta |
| REQ-07 | Controle de acesso por perfil/papel (colaborador, gestor, inovação, admin) | Alta |
| REQ-08 | Suporte a todos os colaboradores do Grupo (holding, VixPar, VAB, comércio) | Alta |
| REQ-09 | Suportar 500 usuários simultâneos sem degradação de performance | Média |
| REQ-10 | Interface responsiva compatível com navegadores web modernos | Média |
| REQ-11 | Sem integrações com sistemas legados no escopo desta fase | Definidor de escopo |
| REQ-12 | Solução proprietária hospedada na infraestrutura do Grupo (sem SaaS) | Alta |

---

## BLOCO 5 — STAKEHOLDERS

| Papel | Nome / Área | Interesse / Influência |
|---|---|---|
| Solicitante / Ponto Focal | Jadson — Área de Inovação | Alto interesse, alta influência — decisor de requisitos |
| Sponsor Executivo | A DEFINIR *(condição bloqueante)* | Alto interesse, alta influência — aprovação de orçamento |
| Gerente do Projeto | A DESIGNAR — VMO Consultoria | Execução e entrega |
| Time de Inovação | Grupo Águia Branca | Usuários-chave, homologação e UAT |
| Gestores de Área | Todas as divisões | Fluxo de aprovação — engajamento necessário |
| Colaboradores | Holding, VixPar, VAB, comércio | Usuários finais — interesse direto |
| TI / Infraestrutura | Grupo Águia Branca | Provisionamento de ambiente, segurança |
| PMO | VMO Consultoria | Governança e controle |

---

## BLOCO 6 — EQUIPE

| Papel | Perfil Necessário | Status |
|---|---|---|
| Gerente do Projeto (GP) | Sênior, experiência em projetos de software | A DESIGNAR — pós aprovação do TAP |
| Arquiteto / Tech Lead | Full Stack, experiência em plataformas web escaláveis | A definir conforme modelo de execução |
| Desenvolvedor(es) Full Stack | Front-end + Back-end, frameworks web modernos | A definir conforme modelo de execução |
| Analista de Requisitos / UX | Levantamento, prototipação e experiência do usuário | A definir conforme modelo de execução |
| Analista de Testes (QA) | Testes funcionais, UAT e regressão | A definir conforme modelo de execução |
| Analista de Infraestrutura | TI Grupo Águia Branca — provisionamento de ambiente | Colaborador do cliente |
| Ponto Focal do Cliente | Jadson — Área de Inovação | Confirmado |

> **Nota:** A composição definitiva da equipe depende da definição do modelo de execução (equipe interna VMO, subcontratação ou modelo híbrido) — condição bloqueante identificada na qualificação.

---

## BLOCO 7 — PREMISSAS

| # | Premissa |
|---|---|
| P-01 | Sponsor executivo será identificado e designado antes do kick-off |
| P-02 | Orçamento de até R$ 90.000,00 será aprovado antes do início da execução |
| P-03 | TI do Grupo provisionará ambiente de homologação e produção sem custo ao projeto |
| P-04 | Jadson estará disponível para validações, refinamentos e aprovações durante todo o projeto |
| P-05 | Modelo de execução definido até kick-off (16/06/2026) |
| P-06 | Sem integrações com sistemas legados no escopo desta fase |
| P-07 | Colaboradores têm acesso à internet corporativa para uso do portal |
| P-08 | Prazo de 30/11/2026 é fixo e inegociável |

---

## BLOCO 8 — RESTRIÇÕES

| # | Restrição |
|---|---|
| R-01 | Orçamento máximo: **R$ 90.000,00** (teto = custo anual da plataforma terceirizada) |
| R-02 | Prazo final: **30 de novembro de 2026** — inegociável |
| R-03 | Sponsor e orçamento aprovado são condições bloqueantes para início da execução |
| R-04 | Modelo de execução não definido — impacta planejamento de recursos e cronograma detalhado |
| R-05 | Nenhuma integração com sistemas legados no escopo desta fase |
| R-06 | Solução deve ser proprietária — proibido uso de SaaS terceirizado que gere custo recorrente |
| R-07 | Treinamento de todos os colaboradores é responsabilidade das divisões, fora do escopo da VMO |

---

## BLOCO 9 — RISCOS (Top 3)

| # | Risco | Probabilidade | Impacto | Severidade | Resposta |
|---|---|---|---|---|---|
| RISCO-01 | **Sponsor não identificado ou orçamento não aprovado a tempo**, atrasando ou inviabilizando o início | Alta | Crítico | **Crítica** | Escalar imediatamente para liderança da VMO e do Grupo; definir data-limite de 13/06/2026; sem sponsor confirmado, projeto não avança |
| RISCO-02 | **Escopo não controlado (scope creep)** — solicitações de novas funcionalidades durante o desenvolvimento comprimem prazo e estouram orçamento | Média | Alto | **Alta** | Processo formal de gestão de mudanças; qualquer nova funcionalidade requer aprovação do sponsor e avaliação de impacto em prazo/custo |
| RISCO-03 | **Prazo insuficiente para desenvolvimento completo** — 5,5 meses de execução efetiva para plataforma completa com equipe a definir | Média | Alto | **Alta** | Adotar entrega em fases (MVP primeiro); priorizar funcionalidades críticas; monitorar velocidade de entrega a cada sprint |

---
---

# DOCUMENTO 3 — PLANO GERAL DO PROJETO

**Projeto:** PROJ-2026-004 — Plataforma Interna de Gestão de Ideias de Inovação
**Data:** 2026-05-14
**Versão:** 1.0
**Gerente do Projeto:** A DESIGNAR

---

## PLANO 1 — PLANO DE ESCOPO

### Definição de Escopo
O escopo é definido pela lista de funcionalidades aprovadas no TAP (seção 4.1) e pelo conjunto de entregas validadas com o solicitante Jadson. Qualquer item não listado como "dentro do escopo" é, por definição, fora do escopo.

### EAP — Estrutura Analítica do Projeto (Sumário)

```
PROJ-2026-004
├── 1. Iniciação
│   ├── 1.1 TAP, PM Canvas e Plano Geral
│   └── 1.2 Kick-off
├── 2. Planejamento
│   ├── 2.1 Levantamento detalhado de requisitos
│   ├── 2.2 Prototipação de interface (UX)
│   └── 2.3 Backlog priorizado
├── 3. Execução
│   ├── 3.1 Módulo: Portal de Ideias + Gestão de Usuários
│   ├── 3.2 Módulo: Campanhas e Desafios
│   ├── 3.3 Módulo: Fluxo de Aprovação Gerencial
│   ├── 3.4 Módulo: Mini Gestão de Projetos
│   └── 3.5 Módulo: Mensuração de Ganhos
├── 4. Testes e Homologação
│   ├── 4.1 Testes integrados (QA)
│   └── 4.2 UAT com time de inovação
├── 5. Implantação
│   ├── 5.1 Go-live em produção
│   └── 5.2 Treinamento de administradores e time de inovação
└── 6. Encerramento
    ├── 6.1 Documentação técnica e manual do usuário
    └── 6.2 Relatório final e lições aprendidas
```

### Controle de Escopo
- Toda solicitação de mudança de escopo deve seguir o processo formal do Plano de Mudanças
- Validações de escopo ocorrem ao final de cada módulo entregue
- Critério de aceite de cada entrega: aprovação formal por escrito do solicitante

---

## PLANO 2 — PLANO DE PRAZO

### Premissa de Prazo
Prazo final inegociável: **30 de novembro de 2026** (go-live em produção).
Execução efetiva: 16/06/2026 a 30/11/2026 = **24,5 semanas** (aproximadamente 5,5 meses).

### Cronograma Macro

| Fase | Período | Duração |
|---|---|---|
| Planejamento detalhado e backlog | 16/06 — 30/06/2026 | 2 semanas |
| Sprint 1 — Portal de Ideias + Usuários (MVP) | 01/07 — 31/08/2026 | 8 semanas |
| Sprint 2 — Campanhas + Fluxo de Aprovação | 01/09 — 30/09/2026 | 4 semanas |
| Sprint 3 — Gestão de Projetos + Mensuração | 01/10 — 31/10/2026 | 4 semanas |
| UAT e Testes de Aceitação | 01/11 — 14/11/2026 | 2 semanas |
| Correções pós-UAT e Go-live | 15/11 — 30/11/2026 | 2 semanas |
| Encerramento | 01/12 — 15/12/2026 | 2 semanas |

### Metodologia
Desenvolvimento ágil em sprints, com cerimônias de review e retrospectiva a cada entrega de módulo. O GP mantém cronograma atualizado semanalmente e reporta desvios superiores a 3 dias úteis imediatamente ao sponsor.

### Marcos Críticos
- **13/06/2026:** Sponsor confirmado + orçamento aprovado (condição bloqueante)
- **30/08/2026:** MVP em homologação
- **14/11/2026:** UAT concluído e aprovado
- **30/11/2026:** Go-live em produção *(data crítica inegociável)*

---

## PLANO 3 — PLANO DE CUSTO

### Orçamento Total Aprovado

| Item | Valor Base | Contingência (20%) | Total |
|---|---|---|---|
| Desenvolvimento | R$ 60.000,00 | — | R$ 60.000,00 |
| Testes e UAT | R$ 8.000,00 | — | R$ 8.000,00 |
| Implantação | R$ 5.000,00 | — | R$ 5.000,00 |
| Treinamento | R$ 2.000,00 | — | R$ 2.000,00 |
| **Subtotal** | **R$ 75.000,00** | **R$ 15.000,00** | **R$ 90.000,00** |

**Teto absoluto: R$ 90.000,00** — qualquer gasto acima requer aprovação do sponsor e é considerado estouro de orçamento.

### Controle de Custos
- Relatório financeiro mensal emitido pelo GP ao sponsor
- Alerta formal ao sponsor quando custo realizado atingir 80% do subtotal (R$ 60.000)
- Uso da contingência requer aprovação formal do sponsor por escrito
- Status atual: **orçamento não aprovado** — aprovação é condição bloqueante para início

### Benefício Financeiro Esperado
- Eliminação de R$ 80.000–90.000/ano de custo com plataforma terceirizada
- Payback imediato no primeiro ano de operação

---

## PLANO 4 — PLANO DE QUALIDADE

### Padrões de Qualidade
- Cobertura de testes unitários: ≥ 70% do código-fonte
- Zero defeitos críticos (P1) no go-live
- Defeitos de alta prioridade (P2): máximo 5 abertos no go-live, com plano de resolução em 15 dias
- Performance: tempo de resposta < 3 segundos para 95% das requisições sob carga de 500 usuários simultâneos
- Disponibilidade esperada pós-go-live: 99% em horário comercial

### Processo de Qualidade
- **Revisão de requisitos:** Antes do início de cada sprint, o GP valida os requisitos com o solicitante
- **Code review:** Todo código passa por revisão de pares antes de merge
- **Testes de integração:** Ao final de cada sprint, executados pelo time de QA
- **UAT (User Acceptance Testing):** 2 semanas (01–14/11/2026) com o time de inovação do Grupo
- **Critério de aprovação do UAT:** ≥ 80% dos casos de teste aprovados; todos os casos críticos aprovados
- **Relatório de qualidade:** Emitido ao final de cada sprint e ao final do UAT

### Ferramentas
- Gestão de defeitos: a definir na fase de planejamento detalhado
- Monitoramento de performance: a definir pela área de TI do Grupo

---

## PLANO 5 — PLANO DE RECURSOS

### Equipe Necessária

| Papel | Dedicação Estimada | Período | Origem |
|---|---|---|---|
| Gerente do Projeto | 40% | Jun–Dez/2026 | A designar — VMO |
| Arquiteto / Tech Lead | 80% | Jun–Nov/2026 | A definir (modelo de execução) |
| Desenvolvedor Full Stack (2x) | 100% cada | Jul–Nov/2026 | A definir (modelo de execução) |
| Analista UX / Requisitos | 80% | Jun–Set/2026 | A definir (modelo de execução) |
| Analista de QA | 80% | Out–Nov/2026 | A definir (modelo de execução) |
| Analista TI (cliente) | 20% | Jun–Nov/2026 | TI Grupo Águia Branca |
| Ponto Focal (cliente) | 20% | Jun–Dez/2026 | Jadson — Grupo Águia Branca |

### Modelo de Execução
**Status:** A definir — condição bloqueante identificada na qualificação do projeto.
Opções a avaliar: equipe interna VMO, subcontratação de squad externo, modelo híbrido.
Decisão necessária até: **13/06/2026**.

### Premissas de Recursos
- Recursos do cliente (TI e ponto focal) disponíveis conforme percentual definido
- Nenhum recurso do projeto desempenhará outras funções críticas simultâneas sem aprovação do GP

---

## PLANO 6 — PLANO DE COMUNICAÇÃO

### Matriz de Comunicação

| Comunicação | Público | Frequência | Formato | Responsável |
|---|---|---|---|---|
| Relatório de Status do Projeto | Sponsor, Solicitante, PMO | Quinzenal | Documento escrito + e-mail | GP |
| Relatório Financeiro | Sponsor | Mensal | Planilha de custos | GP |
| Review de Sprint | Solicitante + Time de Inovação | A cada entrega de módulo | Reunião + demonstração | GP + Tech Lead |
| Reunião de Acompanhamento | GP + Equipe | Semanal | Daily/Reunião | GP |
| Alerta de Risco/Desvio | Sponsor + Solicitante | Conforme ocorrência | E-mail formal | GP |
| Relatório Final | Sponsor, Solicitante, PMO | Encerramento (Dez/2026) | Documento formal | GP |
| Kick-off | Todos os stakeholders | Uma vez (Jun/2026) | Reunião presencial/virtual | GP |

### Canais e Ferramentas
- E-mail corporativo: comunicações formais e registros de decisão
- Ferramenta de gestão de projeto: a definir na fase de planejamento detalhado
- Repositório de documentos: a definir (SharePoint ou equivalente do Grupo)
- Reuniões: videoconferência ou presencial conforme disponibilidade

### Registro de Decisões
Toda decisão relevante tomada em reunião deve ser registrada em ata e distribuída em até 24 horas. Ausência de resposta em 48 horas equivale à aprovação tácita.

---

## PLANO 7 — PLANO DE RISCOS

### Registro de Riscos

| Código | Risco | Prob. | Impacto | Sev. | Resposta | Dono |
|---|---|---|---|---|---|---|
| RSK-01 | Sponsor não definido / orçamento não aprovado dentro do prazo-limite | Alta | Crítico | **Crítica** | Escalar para liderança VMO e Grupo; data-limite 13/06/2026; projeto suspenso se não resolvido | GP / PMO VMO |
| RSK-02 | Scope creep — requisitos novos durante execução | Média | Alto | **Alta** | Processo formal de mudanças; qualquer novo item avaliado com impacto em prazo e custo | GP |
| RSK-03 | Prazo insuficiente para desenvolvimento completo | Média | Alto | **Alta** | Entrega em fases (MVP primeiro); monitoramento de velocidade; priorização rigorosa | GP + Tech Lead |
| RSK-04 | Indisponibilidade de recursos-chave durante execução | Baixa | Alto | **Média** | Plano de backup por papel; contratos com cláusulas de substituição | GP |
| RSK-05 | Ambiente de TI não provisionado a tempo | Média | Médio | **Média** | Solicitar provisionamento na fase de planejamento; validar ambiente em Jul/2026 | GP + TI Grupo |
| RSK-06 | Baixa adoção pelos colaboradores após go-live | Baixa | Médio | **Baixa** | Comunicação interna antecipada; engajamento do time de inovação e gestores | Solicitante |

### Processo de Gestão de Riscos
- Revisão do registro de riscos: quinzenal, integrada ao relatório de status
- Novos riscos identificados pela equipe devem ser reportados ao GP em até 24 horas
- Riscos de severidade crítica ou alta disparam comunicação imediata ao sponsor

---

## PLANO 8 — PLANO DE AQUISIÇÕES

### Necessidades de Aquisição

| Item | Tipo | Necessidade | Prazo de Contratação |
|---|---|---|---|
| Equipe de desenvolvimento (se subcontratada) | Serviço | Conforme modelo de execução a definir | Até 13/06/2026 |
| Licenças de software/frameworks | Licença/Open Source | Priorizar soluções open source para reduzir custo | Até 30/06/2026 |
| Infraestrutura de produção | Serviço interno | Provisionado pela TI do Grupo (sem custo ao projeto) | A confirmar com TI |
| Ferramentas de gestão e QA | SaaS/Licença | A definir na fase de planejamento detalhado | Até 30/06/2026 |

### Política de Aquisições
- Priorizar soluções open source e frameworks sem custo de licença para maximizar o orçamento de desenvolvimento
- Contratações acima de R$ 5.000,00 requerem aprovação do sponsor
- Contratos de desenvolvimento (se subcontratado) devem incluir: cláusula de entrega por marcos, penalidade por atraso e cessão total de propriedade intelectual ao Grupo Águia Branca
- Toda aquisição deve ser registrada no controle financeiro do projeto

### Propriedade Intelectual
Todo código, documentação e artefatos produzidos no projeto são propriedade exclusiva do Grupo Águia Branca, conforme contrato de prestação de serviços VMO Consultoria.

---

## PLANO 9 — PLANO DE STAKEHOLDERS

### Análise de Stakeholders

| Stakeholder | Interesse | Influência | Engajamento Atual | Engajamento Desejado | Estratégia |
|---|---|---|---|---|---|
| Jadson (Solicitante) | Alto | Alta | Engajado | Engajado | Manter: reuniões de review, validações frequentes |
| Sponsor (A definir) | Alto | Crítica | Indefinido | Engajado | Identificar e engajar imediatamente — condição bloqueante |
| Time de Inovação | Alto | Média | Neutro | Engajado | Envolver no UAT; demonstrações de MVP |
| Gestores de Área | Médio | Média | Desinformado | Suportivo | Comunicar benefícios; treinamento do fluxo de aprovação |
| Colaboradores | Alto | Baixa | Desinformado | Suportivo | Comunicação interna coordenada pelo time de inovação |
| TI / Infraestrutura | Médio | Alta (em infra) | Neutro | Suportivo | Envolver desde a fase de planejamento; alinhar requisitos técnicos |
| PMO VMO | Médio | Alta (em governança) | Engajado | Engajado | Manter: reports de status e financeiros |

### Abordagem de Engajamento
- **Alta prioridade imediata:** Identificação e engajamento do sponsor executivo (pré-kick-off)
- **Prioridade alta:** Alinhamento com TI do Grupo para garantia de ambiente (pré-execução)
- **Prioridade média:** Comunicação com gestores de área sobre o fluxo de aprovação (pré-go-live)
- **Prioridade baixa:** Comunicação ampla com colaboradores (coordenada pelo time de inovação, não pela VMO)

### Expectativas Documentadas
- **Jadson:** Plataforma funcional antes do Prêmio Inovação (jan/2027), dentro do orçamento e com as funcionalidades requeridas
- **Colaboradores:** Interface simples, intuitiva, acessível sem limitação de licença
- **TI do Grupo:** Solução segura, hospedável na infraestrutura atual, sem overhead de manutenção complexo

---

## PLANO 10 — PLANO DE MUDANÇAS

### Princípio Geral
Qualquer alteração de escopo, prazo ou orçamento não prevista no TAP constitui uma mudança formal e deve seguir o processo descrito neste plano. Mudanças não aprovadas formalmente não serão executadas.

### Processo de Controle de Mudanças

| Etapa | Descrição | Responsável | Prazo |
|---|---|---|---|
| 1. Identificação | Qualquer membro da equipe ou stakeholder identifica necessidade de mudança | Quem identificou | Imediato |
| 2. Registro | Abertura de Solicitação de Mudança (SM) com descrição, justificativa e impactos estimados | GP | Até 24h após identificação |
| 3. Análise de Impacto | GP avalia impacto em escopo, prazo, custo, qualidade e riscos | GP + Tech Lead | Até 3 dias úteis |
| 4. Decisão | Aprovação ou rejeição pelo sponsor (mudanças com impacto em orçamento/prazo) ou pelo GP (mudanças internas sem impacto em baseline) | Sponsor / GP | Até 2 dias úteis após análise |
| 5. Implementação | Mudança aprovada é incorporada ao plano, cronograma e backlog | GP + Equipe | Conforme planejamento |
| 6. Comunicação | Stakeholders relevantes são notificados da mudança aprovada | GP | Até 24h após aprovação |

### Autoridade de Aprovação de Mudanças

| Tipo de Mudança | Autoridade |
|---|---|
| Mudanças de escopo (adição/remoção de funcionalidades) | Sponsor + Solicitante |
| Mudanças de prazo de marcos críticos | Sponsor |
| Uso da contingência orçamentária | Sponsor |
| Ajustes internos de cronograma sem impacto em marcos | GP |
| Substituição de recursos da equipe | GP (com ciência do sponsor) |

### Registro de Mudanças
Todas as solicitações de mudança (aprovadas ou rejeitadas) são registradas no Log de Mudanças do projeto, mantido pelo GP e disponível para consulta por todos os stakeholders. O log é revisado em cada reunião quinzenal de status.

### Linha de Base (Baseline)
- **Escopo baseline:** Definido na seção 4 do TAP
- **Prazo baseline:** Go-live em 30/11/2026
- **Custo baseline:** R$ 75.000,00 (subtotal sem contingência)
- Qualquer alteração à baseline requer aprovação formal conforme processo acima

---

## RESUMO DE CONSISTÊNCIA ENTRE DOCUMENTOS

| Parâmetro | TAP | PM Canvas | Plano Geral |
|---|---|---|---|
| Código do Projeto | PROJ-2026-004 | PROJ-2026-004 | PROJ-2026-004 |
| Data | 2026-05-14 | 2026-05-14 | 2026-05-14 |
| Prazo Final (Go-live) | 30/11/2026 | 30/11/2026 | 30/11/2026 |
| Orçamento Total | R$ 90.000,00 | R$ 90.000,00 | R$ 90.000,00 |
| Contingência | R$ 15.000,00 (20%) | Referenciada no Bloco 8 | R$ 15.000,00 (20%) |
| Sponsor | A definir (bloqueante) | A definir (bloqueante) | A definir (bloqueante) |
| GP | A designar | A designar | A designar |
| Funcionalidades | 5 módulos + usuários | 5 módulos + usuários | 5 módulos + usuários |

---

*Documento gerado por Diana Documento — PMO/VMO Consultoria*
*PROJ-2026-004 | Versão 1.0 | 2026-05-14*
