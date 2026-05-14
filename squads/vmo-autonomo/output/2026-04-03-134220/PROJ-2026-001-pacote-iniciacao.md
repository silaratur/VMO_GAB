# PACOTE DE INICIAÇÃO DE PROJETO
## PROJ-2026-001 — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados

**Cliente:** VIX Manutenção
**Emitido por:** VMO Consultoria — VMO Autônomo Squad
**Data de emissão:** 2026-04-03
**Versão:** 1.0
**Status:** APROVADO — 8.7/10

---

**Aprovado por:**
Marcelo Silveira — VMO Consultoria
2026-04-03 — Checkpoint Final (Step 12)

---

**Revisão de qualidade:**
Vera Veredito — Revisora de Qualidade VMO
Pontuação: **8.7/10** | Resultado: **🟢 APROVADO**

---

## SUMÁRIO

1. [Termo de Abertura do Projeto (TAP)](#1-termo-de-abertura-do-projeto-tap)
2. [PM Canvas](#2-pm-canvas)
3. [Plano Geral do Projeto](#3-plano-geral-do-projeto)
4. [Especificação de Requisitos Funcionais (ERF)](#4-especificação-de-requisitos-funcionais-erf)
5. [WBS e Cronograma](#5-wbs-e-cronograma)
6. [Plano de Riscos](#6-plano-de-riscos)
7. [Framework de KPIs](#7-framework-de-kpis)
8. [Status Report Inicial](#8-status-report-inicial)
9. [Revisão de Qualidade — Veredicto Final](#9-revisão-de-qualidade--veredicto-final)

---

---

# 1. TERMO DE ABERTURA DO PROJETO (TAP)

```
TERMO DE ABERTURA DO PROJETO
Versão: 1.0 | Data: 2026-04-03 | Status: RASCUNHO
```

---

## IDENTIFICAÇÃO

| Campo              | Valor                                              |
|--------------------|----------------------------------------------------|
| Nome do Projeto    | Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados |
| ID do Projeto      | PROJ-2026-001                                      |
| Demanda Originária | DEM-2026-001                                       |
| Área Solicitante   | VIX Manutenção                                     |
| Área Executora     | DTI — Diretoria de Tecnologia da Informação        |
| Data de Abertura   | 2026-04-03                                         |
| Versão             | 1.0                                                |

---

## AUTORIZAÇÃO

| Campo                  | Valor                                                                 |
|------------------------|-----------------------------------------------------------------------|
| Sponsor                | Andre Chieppe — Diretor Financeiro da VIX Manutenção |
| Solicitante            | Ivanilde Ribeiro Machado — VIX Manutenção                            |
| Gerente de Projeto     | A designar pelo PMO                                                   |
| Autoridade do GP       | Aprovar despesas até R$ 1.000 por item sem consulta ao sponsor; alterações de escopo requerem aprovação do sponsor; variações de cronograma superiores a 5 dias úteis requerem comunicação formal ao sponsor |

> **Nota:** A assinatura deste TAP pelo Sponsor é condição para o início das fases de execução. Enquanto o nome completo do Diretor Financeiro não for confirmado, este documento permanece em status RASCUNHO.

---

## OBJETIVO DO PROJETO (SMART)

Parametrizar o Diretor Financeiro da VIX Manutenção como aprovador obrigatório no fluxo de aprovação de lançamentos pré-editados do módulo SAP FI — utilizando as transações ZFI0057 e SBWP do ambiente SAP já implantado — de modo que 100% dos lançamentos pré-editados submetidos após a entrada em produção da solução passem pelo nível de aprovação do Diretor Financeiro, com o sistema em produção e em uso efetivo até **60 dias úteis** a contar da data de aprovação formal deste TAP.

**Desdobramento SMART:**

- **Específico:** Incluir o Diretor Financeiro como aprovador obrigatório no fluxo SAP FI para a categoria "lançamentos pré-editados", via parametrização nas transações ZFI0057 e SBWP.
- **Mensurável:** 100% dos lançamentos pré-editados passam pelo step de aprovação do Diretor Financeiro após a go-live; zero lançamentos aprovados sem essa etapa após a data de corte.
- **Atingível:** Tecnologia já implantada, sem integração externa, escopo restrito à parametrização; complexidade baixa confirmada pela análise comercial.
- **Relevante:** Eleva o nível de governança financeira, reduz risco de fraude e endereça lacuna identificada no processo de controle interno.
- **Temporal:** Sistema em produção com aprovação ativa até **60 dias úteis após aprovação do TAP**.

---

## JUSTIFICATIVA

O Diretor Financeiro da VIX Manutenção estava ausente do fluxo de aprovação de lançamentos pré-editados no SAP FI, criando uma lacuna de controle no processo de aprovação financeira. Essa ausência expõe a organização a risco de fraude e a fragilidades de governança, uma vez que lançamentos de maior relevância tramitam sem a ciência e aprovação do principal executivo financeiro da área.

A solução é de baixo custo e baixa complexidade técnica: utiliza infraestrutura SAP já implantada, sem necessidade de desenvolvimento de novas funcionalidades ou integração com sistemas externos. O benefício é imediato e direto — restaurar a cadeia de aprovação esperada pelo modelo de controle interno.

Alinhamento estratégico: a medida reforça a agenda de governança corporativa e maturidade de controles internos, consistente com as diretrizes de gestão de riscos da VMO Consultoria para seus clientes em transformação digital.

---

## ESCOPO

### DENTRO DO ESCOPO

1. Parametrização do Diretor Financeiro como aprovador obrigatório na transação **ZFI0057** para a categoria de lançamentos pré-editados no SAP FI.
2. Configuração e validação do fluxo de aprovação na transação **SBWP** (SAP Business Workplace — workflow de aprovação), incluindo roteamento correto da tarefa de aprovação para a caixa de entrada do Diretor Financeiro.
3. Realização de testes integrados em ambiente de qualidade (QAS) com cenários de aprovação, rejeição e roteamento de exceções antes da promoção para produção (PRD).
4. Treinamento/capacitação do Diretor Financeiro para uso da interface de aprovação no SBWP (aprovação via SAP GUI e/ou SAP Fiori, conforme disponibilidade do ambiente).
5. Documentação técnica da parametrização (manual de configuração) e documentação operacional (guia do aprovador).
6. Go-live supervisionado e acompanhamento pós-implantação por período mínimo de **10 dias úteis** após entrada em produção.

### FORA DO ESCOPO

1. Alteração de fluxos de aprovação de **outras categorias** de lançamentos SAP FI além dos lançamentos pré-editados (ex.: lançamentos manuais, estornos, compensações).
2. Desenvolvimento de novas funcionalidades, programas ABAP ou modificações no código-fonte do SAP — a solução limita-se à parametrização das transações existentes.
3. Integração com sistemas externos ao SAP (ex.: ERP de terceiros, sistemas de conciliação bancária, ferramentas de GRC externas).
4. Revisão ou redesenho do processo de negócio de aprovação financeira além da inclusão do novo aprovador (reengenharia de processo está fora do escopo).
5. Configuração de aprovadores em outros módulos SAP (MM, CO, SD, etc.) ou em outras transações além de ZFI0057 e SBWP.
6. Implantação de auditoria/log avançado de aprovações além dos recursos nativos já disponíveis no SAP FI.

---

## CRITÉRIOS DE SUCESSO

1. **Cobertura do fluxo de aprovação:** 100% dos lançamentos pré-editados submetidos no SAP FI após a data de go-live recebem task de aprovação na caixa do Diretor Financeiro, verificado por relatório de workflow extraído do SBWP na primeira semana após go-live.

2. **Zero bypass:** Nenhum lançamento pré-editado é contabilizado (status "postado") sem aprovação registrada do Diretor Financeiro, confirmado por auditoria de 30 dias de transações pós-go-live extraída da ZFI0057 ou relatório equivalente.

3. **Prazo de entrega:** Sistema em produção e aprovado pelo Sponsor com, no máximo, **60 dias úteis** a partir da data de assinatura deste TAP, sem extensão de prazo não autorizada.

4. **Custo dentro do orçamento aprovado:** Custo total do projeto encerrado dentro da faixa aprovada de até **R$ 8.640** (incluindo contingência de 20%), sem solicitação de orçamento adicional.

5. **Capacitação confirmada:** Aprovador (Diretor Financeiro) confirma, por aceite formal ou e-mail, ter recebido treinamento e ser capaz de operar o fluxo de aprovação no SBWP antes da go-live.

---

## PREMISSAS

1. O ambiente SAP FI de produção está implantado, estável e com as transações ZFI0057 e SBWP operacionais e acessíveis pela equipe de DTI.
2. Existe ambiente de qualidade (QAS) disponível para realização dos testes integrados antes da promoção para produção.
3. Andre Chieppe (Diretor Financeiro) está ciente do projeto, apoiará a iniciativa e terá disponibilidade para participar do treinamento e validar o fluxo antes da go-live.
4. A parametrização na ZFI0057 é suficiente para incluir o novo aprovador sem necessidade de desenvolvimento ABAP ou solicitação de suporte SAP (OSS).
5. A equipe de Basis / Administração SAP da DTI possui as autorizações necessárias para realizar as parametrizações nos ambientes QAS e PRD dentro do prazo do projeto.
6. O processo de gestão de mudanças (change management) do cliente para transporte entre ambientes SAP (DEV → QAS → PRD) terá janelas disponíveis compatíveis com o cronograma do projeto.

---

## RESTRIÇÕES

1. **Orçamento fixo:** Teto de R$ 8.640 (já incluindo contingência de 20%); qualquer necessidade adicional requer aprovação formal do Sponsor e revisão do TAP.
2. **Prazo máximo:** 60 dias úteis a partir da assinatura do TAP — prazo não prorrogável sem aprovação formal do Sponsor e comunicação ao PMO.
3. **Escopo de tecnologia:** A solução deve ser implementada exclusivamente por meio de parametrização das transações existentes (ZFI0057 e SBWP); qualquer necessidade de desenvolvimento ABAP ou aquisição de licença adicional deve ser escalada ao Sponsor como mudança de escopo.
4. **Ambiente de produção:** Nenhuma alteração pode ser realizada diretamente em PRD sem ter passado pelos testes em QAS e sem aprovação formal do Gerente de Projeto e do Sponsor.
5. **Conformidade com processo de change management do cliente:** Todos os transportes entre ambientes devem seguir o processo formal de gestão de mudanças do ambiente SAP do cliente.

---

## RISCOS DE ALTO NÍVEL

| # | Risco | Probabilidade | Impacto | Resposta Preliminar |
|---|-------|--------------|---------|---------------------|
| R01 | Indisponibilidade do ambiente QAS para testes no prazo planejado | Médio | Alto | Reservar janela de QAS com antecedência mínima de 2 semanas; incluir folga de 5 dias úteis no cronograma |
| R02 | Parametrização via ZFI0057 revelar limitação técnica exigindo desenvolvimento ABAP | Baixo | Alto | Spike técnico na fase de planejamento antes de qualquer comprometimento de prazo |
| R03 | Indisponibilidade ou baixa adesão do Diretor Financeiro para treinamento e validação | Médio | Médio | Engajar Sponsor; agendar treinamento com 10du de antecedência; alternativa assíncrona |
| R04 | Processo de change management incompatível com o cronograma do projeto | Médio | Médio | Mapear calendário de transportes na fase de iniciação; folga de 5du |
| R05 | Identificação tardia de outros aprovadores no fluxo atual impactados | Baixo | Médio | Mapear todos os aprovadores atuais do fluxo ZFI0057 antes de iniciar a parametrização |

---

## PARTES INTERESSADAS PRINCIPAIS

| Stakeholder | Papel no Projeto | Interesse / Influência | Engajamento Necessário |
|-------------|-----------------|----------------------|------------------------|
| Diretor Financeiro — VIX Manutenção | Sponsor / Aprovador final incluído no fluxo | Alto / Alto | Liderança ativa |
| Ivanilde Ribeiro Machado | Solicitante / Ponto focal de negócio | Alto / Médio | Colaborativo |
| Gerente de Projeto (a designar) | Responsável pela entrega | Alto / Alto | Liderança operacional |
| Equipe DTI / Basis SAP | Executora técnica | Médio / Alto | Colaborativo |
| PMO VMO Consultoria | Governança e acompanhamento | Médio / Médio | Monitoramento |
| Usuários do fluxo de aprovação SAP FI | Afetados pela mudança | Médio / Baixo | Informado |

---

## ORÇAMENTO RESUMIDO

| Item | Valor Estimado |
|------|----------------|
| Análise técnica e parametrização SAP (ZFI0057 + SBWP) | R$ 2.400 – R$ 4.800 |
| Testes integrados em QAS | R$ 720 – R$ 1.440 |
| Treinamento do aprovador e documentação | R$ 480 – R$ 960 |
| Acompanhamento pós go-live (10 dias úteis) | R$ 360 – R$ 720 |
| **Subtotal (sem contingência)** | **R$ 3.960 – R$ 7.920** |
| Contingência (20%) | R$ 792 – R$ 1.584 |
| **TOTAL APROVADO (teto máximo)** | **R$ 8.640** |

---

## CRONOGRAMA SUMARIZADO

| Fase | Descrição | Duração | Du Início | Du Fim |
|------|-----------|---------|-----------|--------|
| F1 — Iniciação | Assinatura do TAP, designação do GP, kickoff | 5 du | Du 1 | Du 5 |
| F2 — Planejamento | Análise técnica (spike), plano detalhado, mapeamento | 10 du | Du 6 | Du 15 |
| F3 — Execução / Parametrização | Parametrização em DEV, testes unitários, transporte para QAS | 15 du | Du 16 | Du 30 |
| F4 — Testes Integrados (QAS) | Testes de aprovação/rejeição, validação com área de negócio | 10 du | Du 31 | Du 40 |
| F5 — Go-Live (PRD) | Transporte para PRD, treinamento, entrada em produção | 5 du | Du 41 | Du 45 |
| F6 — Acompanhamento pós go-live | Monitoramento 10du, evidências de sucesso, encerramento | 15 du | Du 46 | Du 60 |
| **TOTAL** | | **60 dias úteis** | **Assinatura do TAP** | **Du 60** |

---

## APROVAÇÃO

Este Termo de Abertura do Projeto, quando assinado pelos abaixo identificados, autoriza formalmente o início do projeto **PROJ-2026-001**.

| Papel | Nome | Assinatura | Data |
|-------|------|-----------|------|
| Sponsor (Diretor Financeiro) | Andre Chieppe | __________________ | ___/___/______ |
| Solicitante | Ivanilde Ribeiro Machado | __________________ | ___/___/______ |
| Gerente de Projeto | *(a designar pelo PMO)* | __________________ | ___/___/______ |
| PMO VMO Consultoria | __________________ | __________________ | ___/___/______ |

---

---

# 2. PM CANVAS

```
PM CANVAS — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados
Versão: 1.0 | Data: 2026-04-03 | Projeto: PROJ-2026-001
```

---

| Bloco | Conteúdo |
|-------|----------|
| **1. POR QUÊ?** | O Diretor Financeiro estava ausente do fluxo de aprovação de lançamentos pré-editados no SAP FI, criando lacuna de controle e risco de fraude. **Benefícios:** Redução do risco de fraude; aumento da governança financeira; conformidade com o modelo de controle interno. |
| **2. O QUÊ?** | **Entregáveis:** E1 — Parametrização ativa em PRD (ZFI0057); E2 — Workflow SBWP configurado; E3 — Testes integrados aprovados em QAS; E4 — Treinamento do aprovador; E5 — Documentação técnica e operacional; E6 — Acompanhamento pós go-live 10du. **Produto final:** Fluxo de aprovação SAP FI operacional em PRD, com 100% dos lançamentos pré-editados passando pelo Diretor Financeiro. |
| **3. QUEM?** | **Sponsor:** Diretor Financeiro — VIX Manutenção. **Solicitante:** Ivanilde Ribeiro Machado. **GP:** A designar pelo PMO. **Equipe técnica:** DTI / Basis SAP. **Outros:** Usuários fluxo SAP FI; PMO VMO Consultoria. |
| **4. COMO?** | **Metodologia:** Gestão de projeto ágil-adaptativa em fases com gates de qualidade. **Abordagem técnica:** Parametrização via ZFI0057 + configuração SBWP + transporte controlado DEV → QAS → PRD + treinamento do Diretor Financeiro. **Ferramentas:** SAP FI (ZFI0057 + SBWP); MS Project / Planner; SharePoint / e-mail. |
| **5. QUANDO?** | M1 — Assinatura TAP: Du 1 \| M2 — Análise técnica concluída: Du 15 \| M3 — Aprovação QAS: Du 40 \| M4 — Go-Live PRD: Du 45 \| M5 — Encerramento: Du 60. **Prazo total:** 60 dias úteis a partir da assinatura do TAP. |
| **6. QUANTO?** | **Orçamento aprovado:** R$ 8.640 (teto, contingência 20% incluída). **Distribuição estimada:** Parametrização 60%; Testes 17%; Treinamento/docs 12%; Acomp. pós go-live 8%; Contingência 20% (sobre subtotal). **Custo de operação:** Zero — solução sobre infraestrutura SAP já licenciada. |
| **7. PREMISSAS** | P1 — Ambiente SAP FI (ZFI0057+SBWP) implantado e estável. P2 — Ambiente QAS disponível. P3 — Diretor Financeiro ciente, disponível e apoiador. P4 — DTI possui perfis SAP com autorização para parametrizar. P5 — Change management do cliente tem janelas compatíveis. P6 — Parametrização não requer nota SAP OSS. |
| **8. RESTRIÇÕES** | RT1 — Orçamento fixo R$ 8.640 (teto com contingência 20%). RT2 — Prazo máximo 60du sem prorrogação não autorizada. RT3 — Solução restrita à parametrização nas transações existentes (sem ABAP ou novas licenças). RT4 — Obrigatoriedade de seguir processo de change management do cliente para transportes DEV → QAS → PRD. RT5 — Alterações de escopo requerem aprovação formal do Sponsor. |
| **9. RISCOS** | R01 — Indisponibilidade QAS: Prob Médio \| Imp Alto → Mitigar: reservar janela com 2 semanas de antecedência. R02 — ABAP não previsto: Prob Baixo \| Imp Alto → Mitigar: spike técnico no planejamento. R03 — Baixa adesão do Diretor ao treinamento: Prob Médio \| Imp Médio → Mitigar: engajamento via Sponsor; treinamento assíncrono como backup. |

---

---

# 3. PLANO GERAL DO PROJETO

```
PLANO GERAL DO PROJETO
Projeto: PROJ-2026-001 | Versão: 1.0 | Data: 2026-04-03 | Status: RASCUNHO
```

---

## 1. GERENCIAMENTO DO ESCOPO

Escopo definido no TAP e limitado à parametrização das transações ZFI0057 e SBWP. Qualquer alteração de escopo passa pelo processo formal de Controle de Mudanças.

**EAP de Alto Nível:**
```
PROJ-2026-001
├── 1. Iniciação (TAP + Kickoff)
├── 2. Planejamento (Spike técnico + Plano detalhado)
├── 3. Parametrização DEV (ZFI0057 + SBWP + Testes unitários)
├── 4. Testes Integrados QAS (Transporte + Testes + Aceite negócio)
├── 5. Go-Live PRD (Treinamento + Transporte + Go-live supervisionado)
└── 6. Encerramento (Acompanhamento 10du + Evidências + Aceite final)
```

---

## 2. GERENCIAMENTO DO CRONOGRAMA

Cronograma em fases sequenciais com gates. Linha de base de 60du fixada após kickoff. Desvios > 5du comunicados formalmente ao Sponsor. Atualização semanal toda segunda-feira.

| Marco | Du a partir da assinatura do TAP |
|-------|----------------------------------|
| M1 — Assinatura do TAP / Kickoff | Du 1 |
| M2 — Análise técnica concluída e validada | Du 15 |
| M3 — Parametrização em DEV concluída | Du 30 |
| M4 — Aprovação QAS (go/no-go PRD) | Du 40 |
| M5 — Go-live PRD | Du 45 |
| M6 — Encerramento (evidências + aceite final) | Du 60 |

---

## 3. GERENCIAMENTO DOS CUSTOS

Orçamento teto R$ 8.640 (com contingência 20% incluída). Alerta ao Sponsor quando realizado ≥ R$ 6.912 (80% do teto). Paralisação e reunião de crise se realizado = 100% do teto.

---

## 4. GERENCIAMENTO DA QUALIDADE

Gate obrigatório de testes integrados em QAS antes de promoção para PRD.

**Critérios mínimos de aceite para go-live:**
1. 100% dos cenários de teste executados e aprovados em QAS.
2. Aceite formal da área de negócio registrado (e-mail ou ata).
3. Treinamento do aprovador concluído e confirmado.
4. Documentação técnica e operacional entregue e revisada.

---

## 5. GERENCIAMENTO DOS RECURSOS

**Matriz RACI Resumida:**

| Atividade | GP | DTI/Basis | Solicitante | Sponsor |
|-----------|-----|-----------|-------------|---------|
| Análise técnica | A | R | C | I |
| Parametrização DEV | A | R | I | I |
| Execução testes QAS | A | R | C | I |
| Aceite funcional QAS | A | C | R | I |
| Treinamento do aprovador | A | R | I | C |
| Go-live PRD | A | R | C | A |
| Encerramento | R | C | C | A |

*R=Responsável | A=Accountable | C=Consultado | I=Informado*

---

## 6. GERENCIAMENTO DAS COMUNICAÇÕES

| Comunicação | Audiência | Frequência | Canal | Responsável |
|-------------|-----------|-----------|-------|-------------|
| Status Report | Sponsor, PMO, Solicitante | Quinzenal | E-mail | GP |
| Ata de Reunião | Participantes | Por reunião (24h) | E-mail | GP |
| Alerta de Risco / Desvio | Sponsor, PMO | Ad hoc | E-mail + telefone | GP |
| Comunicado de Go-Live | Todos os usuários do fluxo | Uma vez | E-mail | GP / DTI |
| Relatório de Encerramento | Sponsor, PMO, Solicitante | Uma vez | E-mail + reunião | GP |
| Kickoff Meeting | Todos os stakeholders | Uma vez (Du 1) | Videoconferência / presencial | GP |
| Reunião de Gate (QAS → PRD) | Sponsor, GP, DTI, Solicitante | Uma vez (Du 40) | Videoconferência / presencial | GP |

---

## 7. GERENCIAMENTO DOS RISCOS

Ver Plano de Riscos (Documento 6). Registro revisado a cada status report quinzenal. Escalada ao Sponsor para qualquer risco que evolua para criticidade Alta.

---

## 8. GERENCIAMENTO DAS AQUISIÇÕES

Sem aquisições previstas. Projeto executado com recursos internos (DTI) e consultoria já contratada (VMO Consultoria). Qualquer necessidade emergente deve ser formalmente solicitada ao Sponsor antes de qualquer comprometimento.

---

## 9. GERENCIAMENTO DOS STAKEHOLDERS

| Stakeholder | Estratégia de Engajamento | Frequência |
|-------------|--------------------------|------------|
| Diretor Financeiro (Sponsor) | Engajar ativamente — aprovações formais, briefings diretos | Quinzenal + gates (Du 40 e Du 60) |
| Ivanilde Ribeiro Machado | Colaborar — validações, aceite QAS, comunicação go-live | Mínimo 3 pontos de contato |
| Equipe DTI / Basis | Gerenciar de perto — briefings técnicos, alocação | Semanal |
| PMO VMO Consultoria | Manter satisfeito — status reports, alertas de desvio | Quinzenal |
| Usuários do fluxo SAP FI | Informar — comunicado go-live com 3du de antecedência | Uma vez |

---

## 10. GERENCIAMENTO DAS MUDANÇAS

Toda solicitação de mudança de escopo, prazo ou orçamento deve ser documentada pelo GP, avaliada quanto ao impacto, e aprovada pelo Sponsor antes de ser implementada.

**Processo:**
```
1. Identificação (qualquer stakeholder)
2. GP documenta no FSM e avalia impacto
3. GP apresenta ao Sponsor com análise
4. Sponsor decide: APROVADO / REJEITADO / PENDENTE
5. GP atualiza o plano se aprovado
6. GP registra a decisão e comunica afetados
```

---

## CICLO DE VIDA E GATES DE QUALIDADE

| Gate | Ocorre em | Aprovadores |
|------|-----------|-------------|
| G1 — Iniciação → Planejamento | Du 5 (após kickoff) | Sponsor + PMO VMO |
| G2 — Planejamento → Execução | Du 15 (após análise técnica) | GP + Sponsor |
| G3 — Execução/DEV → Testes QAS | Du 30 (após parametrização DEV) | GP + DTI |
| G4 — Testes QAS → Go-Live PRD | Du 40 (após testes QAS) | Sponsor + GP + Solicitante |
| G5 — Encerramento | Du 60 (após acompanhamento pós go-live) | Sponsor + PMO VMO |

---

---

# 4. ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS (ERF)

```
ERF — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados
Versão: 1.0 | Data: 2026-04-03 | Referência: DEM-2026-001 / PROJ-2026-001
Analista: Rafael Requisito — Engenheiro de Requisitos | VMO Autônomo Squad
```

---

## 1. Requisitos Funcionais

### 1.1 Configuração de Aprovadores

| ID | Descrição | Prioridade | Critério de Aceitação |
|----|-----------|------------|-----------------------|
| RF001 | O sistema deve permitir a inclusão do Diretor Financeiro como aprovador adicional no fluxo de aprovação de lançamentos pré-editados do módulo SAP FI, por meio da transação ZFI0057. | **Must Have** | Após parametrização em ZFI0057, ao criar lançamento pré-editado de teste, o Diretor Financeiro deve aparecer como aprovador pendente no fluxo (verificável via SWI5 ou equivalente) — testado em QA antes de PRD. |
| RF002 | A transação ZFI0057 deve ser utilizada como único mecanismo de configuração do novo aprovador, sem alteração de código ABAP ou customização de tabelas SAP fora do escopo parametrizável. | **Must Have** | A configuração deve ser executada exclusivamente via ZFI0057. Não são permitidas modificações via SE11, SE38 ou SE16. A TR deve listar apenas objetos parametrizáveis da ZFI0057, sem transportar programas ABAP, tabelas Z ou objetos de desenvolvimento. |
| RF003 | O novo aprovador (Diretor Financeiro) deve ser identificado por seu ID de usuário SAP (SY-UNAME) ativo antes da parametrização. | **Must Have** | Antes da parametrização em DEV, o DTI deve fornecer documentalmente o ID SAP do Diretor Financeiro. Técnico deve verificar que o usuário está ativo na SU01 (status = Ativo) e não é usuário genérico ou de serviço (tipo = Dialog). |
| RF004 | Após a parametrização, o fluxo deve exigir a aprovação do Diretor Financeiro de forma obrigatória, não sendo possível contornar ou ignorar essa etapa. | **Must Have** | Em QA, criar 3 lançamentos pré-editados de teste e tentar efetivá-los sem aprovação do Diretor Financeiro. O sistema deve bloquear a efetivação e exibir mensagem de erro ou status "aguardando aprovação" em todos os 3 casos. |
| RF005 | A posição do Diretor Financeiro na cadeia de aprovação (sequencial ou paralela, e em qual posição) deve ser definida e documentada antes da parametrização. | **Must Have** | Documento de design (ou e-mail com confirmação do Sponsor) deve definir a posição antes da parametrização. Após parametrização em QA, verificar que o workflow dispara aprovadores exatamente na ordem/paralelismo documentado. |

### 1.2 Fluxo de Aprovação

| ID | Descrição | Prioridade | Critério de Aceitação |
|----|-----------|------------|-----------------------|
| RF006 | Após inclusão do novo aprovador, os lançamentos pré-editados devem ser encaminhados automaticamente à caixa SBWP do Diretor Financeiro, sem intervenção manual. | **Must Have** | Em QA, criar lançamento e concluir etapas anteriores. Em até 5 minutos, item de trabalho deve aparecer automaticamente na SBWP do Diretor Financeiro (verificar via SWIA ou SWI5). |
| RF007 | O item de trabalho na SBWP deve conter: número do documento, data, valor, centro de custo, conta contábil e responsável pelo lançamento. | **Must Have** | Em QA, verificar que os 6 campos listados estão visíveis e corretos no item de trabalho criado. |
| RF008 | O Diretor Financeiro deve poder executar "Aprovar" e "Rejeitar" diretamente do item de trabalho na SBWP, sem precisar acessar outras transações. | **Must Have** | Usuário de teste deve conseguir: (a) abrir item na SBWP; (b) clicar "Aprovar" e confirmar que lançamento avança; (c) em outro lançamento, clicar "Rejeitar" e confirmar retorno ao status pendente. Ambas ações completadas sem navegação para outras transações. |
| RF009 | Em caso de rejeição, o lançamento deve retornar ao status pendente de correção e o responsável deve receber notificação automática via SBWP com motivo. | **Should Have** | Em QA, rejeitar lançamento com motivo preenchido. Criador do lançamento deve receber item de trabalho de notificação em até 10 minutos, com o motivo. Lançamento deve constar como "rejeitado" na FB03. |
| RF010 | O fluxo configurado deve manter os aprovadores já existentes, adicionando o Diretor Financeiro de forma aditiva. | **Must Have** | Antes da parametrização, DTI documenta lista atual de aprovadores. Após parametrização em QA, verificar que todos os aprovadores pré-existentes ainda constam na mesma posição/ordem original, e o Diretor Financeiro foi adicionado sem substituir nenhum. |

### 1.3 Controle e Auditoria

| ID | Descrição | Prioridade | Critério de Aceitação |
|----|-----------|------------|-----------------------|
| RF011 | O sistema deve registrar no log de auditoria SAP cada ação de aprovação ou rejeição do Diretor Financeiro (ID do usuário, data/hora, número do documento, ação). | **Must Have** | Em QA, executar 2 aprovações e 1 rejeição. Consultar log via SWI5 ou SWIA — os 3 eventos devem estar registrados com todos os campos exigidos (ID usuário, data/hora com precisão de segundos, número do documento, ação). |
| RF012 | Nenhum lançamento pré-editado deve ser efetivado no SAP FI enquanto houver aprovação pendente do Diretor Financeiro. | **Must Have** | Tentar efetivar via FB01 um lançamento pendente de aprovação. O sistema deve bloquear a operação com mensagem de erro identificável. Registro do bloqueio deve ser verificável em log. |
| RF013 | A parametrização realizada na ZFI0057 deve ser transportada via ordem de transporte SAP (DEV → QA → PRD), com registro documentado de cada transporte. | **Must Have** | DTC deve listar: número da TR por ambiente, data/hora de execução, nome do técnico e status (sucesso/erro com resolução). Verificável via SE09/SE10. Nenhuma alteração pode constar como aplicada diretamente em PRD. |
| RF014 | Usuários com perfil de auditoria devem poder consultar o histórico de aprovações do Diretor Financeiro sem acesso de escrita. | **Should Have** | Usuário read-only deve conseguir consultar histórico via SWI5 ou equivalente sem erro de autorização. O mesmo usuário não deve conseguir executar ações de aprovação, rejeição ou modificação de configuração. |

---

## 2. Requisitos Não-Funcionais

| ID | Categoria | Descrição | Prioridade |
|----|-----------|-----------|------------|
| RNF001 | Segurança | A parametrização da ZFI0057 em PRD deve ser executada exclusivamente por usuário com perfil Basis ou equivalente com autorização F_BKPF_BUK, em sessão controlada e registrada. | Must Have |
| RNF002 | Segurança | O ID SAP do Diretor Financeiro vinculado ao fluxo deve ser o ID corporativo ativo — não é permitido uso de usuário genérico, compartilhado ou de serviço. | Must Have |
| RNF003 | Auditabilidade | Toda alteração da ZFI0057 deve ser transportada via TR SAP (DEV → QA → PRD), sem hot patch direto em produção. | Must Have |
| RNF004 | Performance | O item de trabalho deve aparecer na SBWP do Diretor Financeiro em até **5 minutos** após a conclusão da etapa anterior do fluxo (horário de pico: 08h00–18h00, dias úteis). | Must Have |
| RNF005 | Disponibilidade | A funcionalidade de aprovação via SBWP deve estar disponível durante 07h00–20h00 em dias úteis, respeitando as janelas de manutenção SAP estabelecidas. | Should Have |
| RNF006 | Rastreabilidade | A parametrização deve ser documentada em DTC contendo: print da ZFI0057 antes e depois da alteração, número da TR, datas de transporte por ambiente e nome do técnico. | Must Have |
| RNF007 | Compatibilidade | A configuração deve ser compatível com a versão SAP em uso, sem exigir aplicação de notas OSS adicionais além das já existentes. | Must Have |
| RNF008 | Segregação de Funções | O Diretor Financeiro, na condição de aprovador, não deve acumular o perfil de criador de lançamentos pré-editados no mesmo ambiente SAP. | Must Have |

---

## 3. Resumo de Priorização MoSCoW

| Prioridade | Qtde | % | IDs |
|------------|------|---|-----|
| Must Have | 19 | 86% | RF001, RF002, RF003, RF004, RF005, RF006, RF007, RF008, RF010, RF011, RF012, RF013, RNF001, RNF002, RNF003, RNF004, RNF006, RNF007, RNF008 |
| Should Have | 3 | 14% | RF009, RF014, RNF005 |
| Could Have | 0 | 0% | — |
| Won't Have | 0 | 0% | — |
| **Total** | **22** | **100%** | |

---

## 4. Perguntas Abertas (a resolver antes da parametrização)

| ID | Questão | Para quem | Prazo |
|----|---------|-----------|-------|
| PA001 | Qual é o ID de usuário SAP (SY-UNAME) do Diretor Financeiro? | Solicitante / DTI | Antes da parametrização |
| PA002 | O Diretor Financeiro deve ser incluído como aprovador sequencial ou paralelo? Em qual posição na cadeia? | Sponsor / Solicitante | Antes da parametrização |
| PA003 | Quais são os aprovadores atualmente configurados no fluxo ZFI0057? | DTI / Basis SAP | Antes da parametrização |
| PA004 | Existe janela de manutenção SAP disponível para transporte em PRD? Qual o calendário? | DTI / Basis SAP | Antes da execução em PRD |
| PA007 | Existe ambiente QA disponível? O Diretor Financeiro participará dos testes de aceite? | DTI / Sponsor | Antes dos testes |
| PA009 | O Diretor Financeiro já possui acesso à SBWP configurado em seu usuário SAP? | DTI / Basis SAP | Antes da parametrização |
| PA010 | Existe prazo ou evento crítico (auditoria, encerramento contábil) que determine data-limite de implementação? | Sponsor / Solicitante | Imediato |

---

## 5. Aprovação da ERF

| Papel | Nome | Assinatura | Data |
|-------|------|------------|------|
| Analista de Requisitos | Rafael Requisito (VMO Squad) | _________________ | 2026-04-03 |
| Solicitante | Ivanilde Ribeiro Machado (VIX Manutenção) | _________________ | __________ |
| Sponsor | Diretor Financeiro | _________________ | __________ |
| Responsável DTI | ________________________ | _________________ | __________ |
| PMO | ________________________ | _________________ | __________ |

> **Condição para início da parametrização:** As perguntas PA001, PA002, PA003 e PA007 devem ser respondidas e documentadas antes de iniciar qualquer parametrização. As demais (PA004, PA009, PA010) devem ser resolvidas antes da execução em PRD.

---

---

# 5. WBS E CRONOGRAMA

```
CRONOGRAMA — PROJ-2026-001
Versão: 1.0 | Data: 2026-04-03 | Gerado por: Carlos Cronograma — Planejador de Prazo
```

---

## WBS — Estrutura Analítica do Projeto

```
1.0 PROJ-2026-001 — Inclusão de Aprovador SAP FI
  │
  ├─ 1.1 Gerenciamento do Projeto
  │    ├─ 1.1.1 Elaboração e aprovação do TAP
  │    ├─ 1.1.2 Designação do Gerente de Projeto e kickoff
  │    ├─ 1.1.3 Status reports quinzenais (3 ciclos)
  │    └─ 1.1.4 Encerramento, aceite formal e lições aprendidas
  │
  ├─ 1.2 Planejamento Técnico
  │    ├─ 1.2.1 Análise técnica (spike)
  │    │    ├─ 1.2.1.1 Verificar parametrização ZFI0057 no ambiente DEV
  │    │    └─ 1.2.1.2 Confirmar viabilidade sem ABAP — relatório técnico
  │    ├─ 1.2.2 Mapeamento de stakeholders e fluxo atual
  │    └─ 1.2.3 Planejamento detalhado e reserva de janela QAS
  │
  ├─ 1.3 Parametrização e Testes em DEV
  │    ├─ 1.3.1.1 Incluir Diretor Financeiro como aprovador na ZFI0057
  │    ├─ 1.3.1.2 Configurar roteamento de tarefa no SBWP
  │    ├─ 1.3.2.1 Testar submissão → aprovação pelo Diretor Financeiro
  │    ├─ 1.3.2.2 Testar cenário de rejeição e roteamento de exceções
  │    └─ 1.3.3 Transporte DEV → QAS
  │
  ├─ 1.4 Testes Integrados em QAS
  │    ├─ 1.4.1.1 Validar transporte e ajustar perfis de acesso em QAS
  │    ├─ 1.4.2.1 Casos de teste: lançamento → fila SBWP Diretor
  │    ├─ 1.4.2.2 Casos de teste: aprovação, rejeição e retorno
  │    ├─ 1.4.2.3 Validação com Ivanilde Ribeiro Machado (UAT)
  │    └─ 1.4.3.1 Ajustes pós-teste e reteste (se necessário)
  │
  ├─ 1.5 Go-Live (PRD)
  │    ├─ 1.5.1.1 Elaborar guia do aprovador (SBWP)
  │    ├─ 1.5.1.2 Sessão de treinamento com o Diretor Financeiro ⭐
  │    ├─ 1.5.2.1 Solicitar janela de transporte (change management)
  │    ├─ 1.5.2.2 Executar transporte e validar em PRD ⭐
  │    └─ 1.5.3.1 Notificar usuários do fluxo sobre nova etapa
  │
  └─ 1.6 Acompanhamento Pós Go-Live
       ├─ 1.6.1.1 Monitorar fila SBWP do Diretor Financeiro ⭐
       ├─ 1.6.1.2 Confirmar ausência de bypass nos lançamentos
       ├─ 1.6.2.1 Extrair relatório de lançamentos com aprovação ⭐
       └─ 1.6.3.1 Aceite do Sponsor + documentação final ⭐
```

---

## Cronograma por Fase

> **Referência:** Du 1 = data de assinatura do TAP. Todas as durações em dias úteis.
> **Premissa:** Equipe Basis estimada a 70% de disponibilidade (projetos SAP concorrentes).

### Fase 1.1 — Iniciação (Du 1–5) ⭐ Caminho Crítico

| ID | Atividade | Du Início | Du Fim | Dur | Dep | Responsável |
|----|-----------|-----------|--------|-----|-----|-------------|
| 1.1.1 | Aprovação do TAP e designação do GP | Du 1 | Du 2 | 2du | — | PMO / Sponsor |
| 1.1.2 | Kickoff com DTI e solicitante | Du 3 | Du 5 | 3du | 1.1.1 | GP |

### Fase 1.2 — Planejamento Técnico (Du 6–15) ⭐ Caminho Crítico

| ID | Atividade | Du Início | Du Fim | Dur | Dep | Responsável |
|----|-----------|-----------|--------|-----|-----|-------------|
| 1.2.1.1 | Verificar ZFI0057 em DEV | Du 6 | Du 8 | 3du | 1.1.2 | Basis SAP |
| 1.2.1.2 | Relatório técnico de viabilidade | Du 9 | Du 10 | 2du | 1.2.1.1 | Basis SAP |
| 1.2.2.1 | Mapear aprovadores existentes no fluxo | Du 6 | Du 8 | 3du | 1.1.2 | GP + Negócio |
| 1.2.2.2 | Confirmar nome/ID SAP do Diretor Financeiro | Du 6 | Du 7 | 2du | 1.1.2 | GP |
| 1.2.3 | Plano detalhado + reserva de janela QAS | Du 11 | Du 15 | 5du | 1.2.1.2 | GP |

### Fase 1.3 — Parametrização DEV (Du 16–30) ⭐ Caminho Crítico

| ID | Atividade | Du Início | Du Fim | Dur | Dep | Responsável |
|----|-----------|-----------|--------|-----|-----|-------------|
| 1.3.1.1 | Parametrizar Diretor Financeiro na ZFI0057 (DEV) | Du 16 | Du 19 | 4du | 1.2.3 | Basis SAP |
| 1.3.1.2 | Configurar roteamento SBWP (DEV) | Du 20 | Du 23 | 4du | 1.3.1.1 | Basis SAP |
| 1.3.2.1 | Teste unitário: aprovação normal | Du 24 | Du 26 | 3du | 1.3.1.2 | Basis + Func |
| 1.3.2.2 | Teste unitário: rejeição e exceções | Du 27 | Du 28 | 2du | 1.3.2.1 | Basis + Func |
| 1.3.3 | Transporte DEV → QAS | Du 29 | Du 30 | 2du | 1.3.2.1 | Basis SAP |

### Fase 1.4 — Testes Integrados QAS (Du 31–42) ⭐ Caminho Crítico

| ID | Atividade | Du Início | Du Fim | Dur | Dep | Responsável |
|----|-----------|-----------|--------|-----|-----|-------------|
| 1.4.1.1 | Validar transporte e perfis QAS | Du 31 | Du 32 | 2du | 1.3.3 | Basis SAP |
| 1.4.2.1 | Testes: lançamento → fila SBWP Diretor | Du 33 | Du 35 | 3du | 1.4.1.1 | Func SAP |
| 1.4.2.2 | Testes: aprovação, rejeição, retorno | Du 36 | Du 38 | 3du | 1.4.2.1 | Func SAP |
| 1.4.2.3 | Validação com solicitante (UAT) | Du 39 | Du 40 | 2du | 1.4.2.2 | GP + Ivanilde |
| 1.4.3.1 | Ajustes pós-teste e reteste (se necessário) | Du 41 | Du 42 | 2du | 1.4.2.3 | Basis SAP |

### Fase 1.5 — Go-Live PRD (Du 43–47) ⭐ Caminho Crítico

| ID | Atividade | Du Início | Du Fim | Dur | Dep | Responsável |
|----|-----------|-----------|--------|-----|-----|-------------|
| 1.5.1.2 | Treinamento do Diretor Financeiro | Du 43 | Du 44 | 2du | 1.4.2.3 | GP |
| 1.5.2.2 | Executar transporte QAS → PRD + validar | Du 45 | Du 46 | 2du | 1.5.1.2 | Basis SAP |
| 1.5.3.1 | Comunicar usuários do fluxo | Du 47 | Du 47 | 1du | 1.5.2.2 | GP |

### Fase 1.6 — Acompanhamento Pós Go-Live (Du 48–52) ⭐ Caminho Crítico

| ID | Atividade | Du Início | Du Fim | Dur | Dep | Responsável |
|----|-----------|-----------|--------|-----|-----|-------------|
| 1.6.1.1 | Monitorar fila SBWP do Diretor (semanas 1–2) | Du 48 | Du 51 | 4du | 1.5.2.2 | GP + DTI |
| 1.6.1.2 | Confirmar ausência de bypass | Du 48 | Du 51 | 4du | 1.5.2.2 | Func SAP |
| 1.6.2.1 | Extrair relatório de cobertura | Du 52 | Du 52 | 1du | 1.6.1.2 | Func SAP |
| 1.6.3.1 | Aceite formal do Sponsor + encerramento | Du 52 | Du 52 | 1du | 1.6.2.1 | GP / Sponsor |

---

## Marcos Principais

| Marco | Du | Critério |
|-------|----|---------|
| M0 — TAP aprovado | Du 2 | TAP assinado pelo Sponsor e PMO |
| M1 — Kick-off | Du 5 | Reunião realizada, equipe mobilizada |
| M2 — Viabilidade técnica confirmada | Du 10 | Relatório Basis: sem ABAP necessário |
| M3 — Parametrização DEV concluída | Du 28 | Testes unitários aprovados em DEV |
| M4 — UAT aprovado em QAS | Du 40 | Validação da solicitante por e-mail/ata |
| M5 — Go-Live PRD | Du 46 | Primeiro lançamento real aprovado pelo Diretor |
| M6 — Encerramento formal | Du 52 | Aceite do Sponsor + relatório de cobertura 100% |

---

## Caminho Crítico ⭐

```
1.1.1 → 1.1.2 → 1.2.1.1 → 1.2.1.2 → 1.2.3 → 1.3.1.1 → 1.3.1.2
→ 1.3.2.1 → 1.3.3 → 1.4.1.1 → 1.4.2.1 → 1.4.2.2 → 1.4.2.3
→ 1.5.1.2 → 1.5.2.2 → 1.6.1.1 → 1.6.2.1 → 1.6.3.1
```

**Folga total do caminho crítico: 0 dias.** Qualquer atraso em atividade marcada com ⭐ impacta diretamente o deadline do projeto.

---

## Buffer de Contingência

| Item | Valor |
|------|-------|
| Prazo base (sem buffer) | 52 du |
| Buffer de gestão (15% de 52du) | + 8 du |
| **Deadline máximo (TAP)** | **Du 60** — teto inegociável sem revisão formal do TAP |

---

---

# 6. PLANO DE RISCOS

```
PLANO DE RISCOS — PROJ-2026-001
Versão: 1.0 | Data: 2026-04-03 | Gerado por: Pedro Perigo — Analista de Riscos VMO
```

---

## Registro de Riscos

| ID | Categoria | Risco | Prob (1–5) | Impacto (1–5) | Score | Nível | Estratégia |
|----|-----------|-------|-----------|--------------|-------|-------|------------|
| R01 | Técnico | A parametrização via ZFI0057 revelar limitação que exige desenvolvimento ABAP, expandindo custo e prazo além do aprovado | 2 | 5 | 10 | **ALTO** | Mitigar |
| R02 | Prazo | Indisponibilidade do ambiente QAS na janela planejada, impedindo execução dos testes integrados no prazo | 3 | 4 | 12 | **ALTO** | Mitigar |
| R03 | Stakeholders | Indisponibilidade ou resistência do Diretor Financeiro para treinamento e validação antes da go-live | 3 | 4 | 12 | **ALTO** | Mitigar |
| R04 | Prazo | Processo de change management incompatível com o cronograma, postergando o go-live | 3 | 3 | 9 | **MÉDIO** | Mitigar |
| R05 | Técnico | Identificação de outros aprovadores no fluxo atual impactados pela parametrização | 2 | 3 | 6 | **MÉDIO** | Mitigar |
| R06 | Financeiro | Custo real superar o teto de R$ 8.640 por necessidade não prevista | 2 | 3 | 6 | **MÉDIO** | Aceitar com contingência |
| R07 | Stakeholders | Resistência dos usuários do fluxo à nova etapa de aprovação | 2 | 2 | 4 | **BAIXO** | Mitigar |

*Escala: 1=Muito Baixa, 2=Baixa, 3=Média, 4=Alta, 5=Muito Alta | ALTO: Score ≥ 9 | MÉDIO: 5–8 | BAIXO: ≤ 4*

---

## Plano de Resposta a Riscos

### R01 — Limitação técnica ZFI0057 exigindo ABAP | ALTO

**Gatilho:** Equipe Basis confirma, durante o spike técnico (Du 6–10), que a parametrização na ZFI0057 não suporta o novo aprovador sem criação de programa ABAP customizado.

**Plano de Mitigação:**
- Executar spike técnico detalhado nos Du 6–10
- Validar parametrização em ambiente DEV como primeiro entregável
- Consultar notas SAP (OSS) sobre ZFI0057 durante o spike

**Plano de Contingência (se materializado):**
- Escalar imediatamente ao Sponsor com análise de impacto (custo e prazo adicionais)
- Avaliar aprovação manual temporária via SBWP até solução definitiva
- Solicitar revisão formal do TAP com novo orçamento e prazo

**Responsável:** GP + Basis SAP | **Ação de mitigação:** Du 6–10

---

### R02 — Indisponibilidade do ambiente QAS | ALTO

**Gatilho:** Na Du 25, equipe Basis confirma que QAS está ocupado sem previsão de liberação na janela planejada (Du 31–40).

**Plano de Mitigação:**
- Reservar formalmente janela de QAS durante o planejamento (Du 11–15)
- Incluir folga de 5du no planejamento de testes
- Mapear projetos concorrentes que usam QAS durante Du 31–42

**Plano de Contingência (se materializado):**
- Acionar buffer de contingência (Du 52–60) para absorver o atraso
- Se atraso superar 8du (buffer total), escalar ao Sponsor para revisão de prazo
- Avaliar execução de testes parciais em DEV para reduzir dependência do QAS

**Responsável:** GP | **Ação de mitigação:** Du 11–15

---

### R03 — Indisponibilidade ou resistência do Diretor Financeiro | ALTO

**Gatilho:** Na Du 37, Diretor Financeiro não confirma disponibilidade para treinamento (Du 43–44) ou informa impossibilidade de participação.

**Plano de Mitigação:**
- Engajar o Sponsor (o próprio Diretor Financeiro, neste caso) desde o kickoff
- Comunicar formalmente a data de treinamento com 10du de antecedência mínima
- Preparar material de treinamento assíncrono (guia escrito + vídeo tutorial)

**Plano de Contingência (se materializado):**
- Disponibilizar treinamento assíncrono para o Diretor realizar no seu tempo
- Colher aceite formal por e-mail após treinamento assíncrono
- Se Diretor não aceitar nenhuma modalidade no prazo: escalar ao PMO e Comitê de Governança

> **Observação:** Este risco tem natureza especial — o Sponsor é o próprio aprovador. Esse duplo papel reduz o risco de resistência, mas pode gerar indisponibilidade por agenda executiva.

**Responsável:** GP | **Ação de mitigação:** Du 5 (kickoff) e Du 33 (confirmação de agenda)

---

### R04 a R07 — Riscos MÉDIO e BAIXO

| ID | Risco | Mitigação Principal | Responsável | Prazo |
|----|-------|---------------------|-------------|-------|
| R04 | Janelas de transporte PRD incompatíveis | Mapear calendário de transportes PRD em Du 11–15; solicitar janela com antecedência mínima de 10du | GP + Basis SAP | Du 11–15 |
| R05 | Outros aprovadores impactados | Mapear TODOS os aprovadores atuais na ZFI0057 antes de iniciar parametrização; validar com área de negócio | GP + Basis | Du 6–8 |
| R06 | Custo real supera teto | Contingência 20% já incluída; alertar Sponsor se custo real tender a superar R$ 7.200 | GP | Contínuo |
| R07 | Resistência usuários ao novo fluxo | Comunicar a mudança com 5du de antecedência; explicar motivo (governança); disponibilizar suporte pós go-live | GP | Du 47 |

---

## Reserva de Contingência (Valor Esperado)

| ID | Risco | Prob. | Impacto Financeiro Estimado | Valor Esperado |
|----|-------|-------|----------------------------|----------------|
| R01 | Limitação técnica ABAP | 0,20 | R$ 15.000 (est. custo ABAP) | R$ 3.000 |
| R02 | Indisponibilidade QAS | 0,30 | R$ 2.000 (custo de atraso ~5du) | R$ 600 |
| R03 | Indisponibilidade Diretor | 0,30 | R$ 1.500 (custo de atraso ~3du) | R$ 450 |
| R04 | Janelas transporte PRD | 0,30 | R$ 1.000 (custo de atraso ~2du) | R$ 300 |
| R05 | Aprovadores impactados | 0,20 | R$ 3.000 (redesenho do fluxo) | R$ 600 |
| R06 | Custo supera teto | 0,20 | R$ 2.000 (custo adicional típico) | R$ 400 |
| R07 | Resistência usuários | 0,20 | R$ 500 (suporte adicional) | R$ 100 |
| **TOTAL** | | | | **R$ 5.450** |

> **Atenção ao Sponsor:** A reserva de contingência embutida no orçamento (20% de R$ 7.200 ≈ R$ 1.440) é **inferior** ao valor esperado calculado (R$ 5.450) — principalmente pelo risco R01 (ABAP), que sozinho gera R$ 3.000 de valor esperado. O GP deve sinalizar ao Sponsor no kickoff que R01, se materializado, requer revisão formal do TAP independentemente da reserva existente.

---

## Frequência de Revisão do Registro de Riscos

| Ciclo | Frequência | Responsável |
|-------|------------|-------------|
| Status report quinzenal | A cada 2 semanas | GP |
| Gate review (a cada fase) | Ao final de F2, F3, F4 | GP + Sponsor |
| Monitoramento contínuo ALTO | Semanal (R01, R02, R03) | GP |

---

---

# 7. FRAMEWORK DE KPIs

```
FRAMEWORK DE KPIs — PROJ-2026-001
Versão: 1.0 | Data: 2026-04-03 | Gerado por: Marcela Métrica — Monitora de Performance VMO
```

---

## Semáforo de Saúde do Projeto

| Dimensão | 🟢 Verde | 🟡 Amarelo | 🔴 Vermelho |
|---|---|---|---|
| **Prazo** | SPI ≥ 0,95 | 0,85 ≤ SPI < 0,95 | SPI < 0,85 |
| **Custo** | CPI ≥ 0,95 | 0,85 ≤ CPI < 0,95 | CPI < 0,85 |
| **Escopo** | 100% dos critérios de aceitação atendidos, zero desvios abertos | 1 desvio aberto ou critério pendente de verificação | 2+ desvios abertos ou critério de aceitação reprovado |
| **Riscos** | Nenhum risco ALTO ativo materializado; todos com plano de resposta documentado | 1 risco ALTO ativo sem plano de resposta concluído | Risco ALTO materializado (R01, R02 ou R03) impactando prazo ou custo |
| **Satisfação** | Aprovador confirma treinamento e aceita sistema antes do go-live; zero reclamações de bypass | Aprovador confirma treinamento mas levanta ressalvas de usabilidade | Aprovador não confirma treinamento até Du 50 ou rejeita aceite do sistema |

---

## KPIs de Desempenho do Projeto (EVM)

| KPI | Fórmula | Baseline | Meta | 🟡 Alerta | 🔴 Crítico | Freq. |
|---|---|---|---|---|---|---|
| **CPI** | CPI = EV / AC | 1,00 (Du 0) | CPI ≥ 1,00 | 0,85 ≤ CPI < 0,95 | CPI < 0,85 | Semanal (2ª feira) |
| **SPI** | SPI = EV / PV | 1,00 (Du 0) | SPI ≥ 1,00 | 0,85 ≤ SPI < 0,95 | SPI < 0,85 | Semanal (2ª feira) |
| **EAC** | EAC = BAC / CPI | R$ 8.640 (Du 0) | EAC ≤ R$ 8.640 | R$ 8.640 < EAC ≤ R$ 9.500 | EAC > R$ 9.500 | Semanal (2ª feira) |
| **VAC** | VAC = BAC − EAC | R$ 0,00 (Du 0) | VAC ≥ R$ 0 | −R$ 860 ≤ VAC < R$ 0 | VAC < −R$ 860 | Semanal (2ª feira) |
| **CV** | CV = EV − AC | R$ 0,00 (Du 0) | CV ≥ 0 | −R$ 500 ≤ CV < 0 | CV < −R$ 500 | Semanal (2ª feira) |
| **SV** | SV = EV − PV | R$ 0,00 (Du 0) | SV ≥ 0 | −10% do PV acumulado | < −15% do PV acumulado | Semanal (2ª feira) |

**BAC:** R$ 8.640 | **Prazo Baseline:** Du 60 | **Moeda:** BRL

---

## KPIs de Resultado do Projeto (Key Results)

| KPI | Descrição | Meta | 🟡 Alerta | 🔴 Crítico | Freq. |
|---|---|---|---|---|---|
| **KR-1** — Taxa de Cobertura de Aprovação | % dos lançamentos pré-editados que passaram pelo fluxo de aprovação do Diretor Financeiro (medido via SBWP na 1ª semana após go-live) | 100% na semana 1 pós go-live | 90% ≤ taxa < 100% | < 90% | Diária pós go-live |
| **KR-2** — Taxa de Bypass Zero | Número de lançamentos contabilizados sem aprovação do Diretor nos 30 dias pós go-live | 0 bypass | 1 bypass (ação corretiva imediata) | ≥ 2 bypasses ou 1 não corrigido em 48h | Diária (auditoria via SBWP) |
| **KR-3** — Prazo de Entrega em Produção | Du de go-live efetivo em relação ao baseline Du 60 | Go-live até Du 60 | Du 55–60 com risco de atraso identificado | Go-live após Du 60 | Semanal; confirmação no marco M6 |
| **KR-4** — Aderência ao Teto de Custo | Custo total (AC final) versus teto aprovado R$ 8.640 | AC final ≤ R$ 8.640 | R$ 8.000 ≤ AC final ≤ R$ 8.640 | AC final > R$ 8.640 | Semanal e ao encerramento |
| **KR-5** — Confirmação de Treinamento do Aprovador | Confirmação formal (e-mail ou lista de presença) do Diretor Financeiro de que recebeu e concluiu o treinamento antes do go-live | Confirmação obtida até Du 52 | Du 46–52 com pendência de assinatura | Diretor não confirma até Du 52 | Uma vez (marco M5/M6) |

---

## Marcos EVM e PV Planejado

| Marco | Du | Entregável Principal | PV Acumulado |
|---|---|---|---|
| M0 — TAP Assinado | Du 2 | TAP aprovado e assinado | 5% — R$ 432 |
| M1 — Requisitos Aprovados | Du 5 | Documento de requisitos aceito | 12% — R$ 1.037 |
| M2 — Baseline Estabelecido | Du 10 | Cronograma, riscos e KPIs aprovados | 20% — R$ 1.728 |
| M3 — Config. QAS Aprovada | Du 28 | Configuração SAP FI em QAS validada | 55% — R$ 4.752 |
| M4 — Testes Integrados OK | Du 40 | Resultados de testes aprovados | 75% — R$ 6.480 |
| M5 — Treinamento Concluído | Du 46 | Confirmação formal do Diretor | 88% — R$ 7.603 |
| M6 — Go-Live / Produção | Du 52 | Sistema em produção + aceite | 96% — R$ 8.294 |
| M7 — Encerramento | Du 60 | Auditoria 30 dias + lições aprendidas | 100% — R$ 8.640 |

---

## Frequência de Reporting

| Relatório | Conteúdo | Frequência | Audiência |
|---|---|---|---|
| Dashboard Semanal | Semáforo + CPI + SPI + EV/PV/AC + VAC | Toda segunda-feira | GP + Sponsor |
| Relatório de Marco | Status completo EVM + KRs + riscos ativos + próximos passos | A cada marco (M0–M7) | Sponsor + Comitê |
| Alerta de Threshold | Notificação imediata quando qualquer KPI entra em zona 🔴 | Ad hoc (imediato) | GP + Sponsor |
| Relatório de Encerramento | EAC final + VAC final + todos os KRs verificados + lições aprendidas | Du 60 | Todos os stakeholders |

---

---

# 8. STATUS REPORT INICIAL

```
STATUS REPORT INICIAL — PROJ-2026-001
Versão: 1.0 | Período: 2026-04-03 (Iniciação) | Gerado por: Sara Status — Redatora de Relatórios VMO
```

---

## STATUS GERAL: 🟢 VERDE

| Dimensão | Status | Observação |
|----------|--------|------------|
| Cronograma | 🟢 VERDE | Projeto em fase de iniciação — TAP aguarda assinatura |
| Custo | 🟢 VERDE | Dentro do teto aprovado de R$ 8.640 |
| Escopo | 🟢 VERDE | Sem mudanças de escopo |
| Riscos | 🟡 ATENÇÃO | 3 riscos ALTO identificados — mitigações em planejamento |
| Qualidade | 🟢 VERDE | Documentação de iniciação completa e validada pelo VMO |

> **Nota:** O status 🟡 em Riscos é preventivo — os riscos ALTO (R01, R02, R03) ainda não se materializaram e têm planos de mitigação definidos. O status consolidado permanece 🟢 pois não há desvio operacional nesta fase.

---

## SUMÁRIO EXECUTIVO

O projeto **PROJ-2026-001** foi formalmente iniciado com a conclusão da documentação de iniciação pelo VMO Autônomo. A demanda consiste na inclusão do **Diretor Financeiro** como aprovador obrigatório no fluxo de lançamentos pré-editados do SAP FI, via parametrização das transações ZFI0057 e SBWP. O objetivo é elevar o nível de governança financeira e reduzir o risco de fraude.

O projeto foi qualificado com **22/30 pontos (73%) — APROVADO COM CONDIÇÕES**, após complementação das lacunas críticas pelo responsável do PMO. O TAP está redigido e aguarda assinatura do Sponsor (Diretor Financeiro). Com a assinatura, o cronograma de 60 dias úteis será ativado e o Gerente de Projeto designado.

**Investimento aprovado:** R$ 8.640 (teto, incluindo contingência de 20%)
**Deadline:** Du 60 a contar da assinatura do TAP
**Sponsor confirmado:** Andre Chieppe — Diretor Financeiro. TAP pronto para assinatura.

---

## PROGRESSO

| Item | Status | Observação |
|------|--------|------------|
| Documentação de iniciação | ✅ Concluída | TAP, PM Canvas, Plano Geral, ERF, Cronograma, Riscos, KPIs |
| TAP — aprovação do Sponsor | ⏳ Pendente | Aguarda assinatura do Diretor Financeiro |
| Designação do Gerente de Projeto | ⏳ Pendente | A ser feito após assinatura do TAP |
| Kickoff | ⏳ Pendente | Planejado para Du 3–5 após assinatura do TAP |
| Spike técnico (viabilidade ZFI0057) | ⏳ Pendente | Planejado para Du 6–10 |

**Progresso geral:** 0% (fase pré-execução — projeto ainda não iniciado formalmente)
**Desvio:** 0 — dentro do planejado

---

## RISCOS EM MONITORAMENTO

| ID | Risco | Nível | Status | Ação Imediata |
|----|-------|-------|--------|---------------|
| R01 | Limitação técnica ZFI0057 exigindo ABAP | 🔴 ALTO | Não materializado | Spike técnico planejado Du 6–10 |
| R02 | Indisponibilidade ambiente QAS | 🔴 ALTO | Não materializado | Reservar janela QAS em Du 11–15 |
| R03 | Indisponibilidade Diretor Financeiro | 🔴 ALTO | Não materializado | Engajar no kickoff (Du 3–5) |
| R04 | Janelas transporte PRD incompatíveis | 🟡 MÉDIO | Não materializado | Mapear calendário em Du 11–15 |
| R05 | Outros aprovadores impactados | 🟡 MÉDIO | Não materializado | Mapear fluxo atual em Du 6–8 |
| R06 | Custo supera teto R$ 8.640 | 🟡 MÉDIO | Monitoramento | Contingência 20% incluída |
| R07 | Resistência usuários do fluxo | 🟢 BAIXO | Não materializado | Comunicação antes do go-live |

---

## ISSUES ABERTAS

| ID | Issue | Impacto | Responsável | Prazo |
|----|-------|---------|-------------|-------|
| I-001 | ~~Nome completo do Diretor Financeiro não confirmado~~ — **RESOLVIDA**: Sponsor confirmado como Andre Chieppe | Bloqueio removido — TAP pronto para assinatura | PMO / Solicitante | ✅ Resolvida em 2026-04-05 |
| I-002 | Gerente de Projeto não designado | Bloqueia kickoff e início da execução | PMO | Imediato após assinatura do TAP |

---

## PRÓXIMOS 3 PASSOS

| # | Ação | Responsável | Prazo |
|---|------|-------------|-------|
| 1 | ✅ Sponsor confirmado: **Andre Chieppe** — Obter assinatura formal do TAP | PMO / Andre Chieppe | Imediato |
| 2 | Designar Gerente de Projeto para PROJ-2026-001 | PMO VMO Consultoria | Após assinatura do TAP |
| 3 | Realizar kickoff com DTI e solicitante (Du 3–5) | GP designado | Após designação do GP |

---

## INFORMAÇÕES DO PROJETO

| Campo | Valor |
|-------|-------|
| ID do Projeto | PROJ-2026-001 |
| Demanda Originária | DEM-2026-001 |
| Sponsor | Andre Chieppe — Diretor Financeiro — VIX Manutenção |
| Solicitante | Ivanilde Ribeiro Machado — VIX Manutenção |
| Gerente de Projeto | A designar pelo PMO |
| Orçamento aprovado | R$ 8.640 (teto) |
| Prazo máximo | Du 60 (a contar da assinatura do TAP) |
| Próximo report | Du 15 (quinzenal, após kickoff) |

---

---

# 9. REVISÃO DE QUALIDADE — VEREDICTO FINAL

```
REVISÃO DE QUALIDADE — VMO AUTÔNOMO
PROJ-2026-001 | Data: 2026-04-03 | Revisora: Vera Veredito | Revisão: 1 de 3
```

---

## VEREDICTO: 🟢 APROVADO

---

## PONTUAÇÃO CONSOLIDADA

| Documento | Peso | Pontuação | Status |
|-----------|------|-----------|--------|
| TAP | 25% | 8.5/10 | 🟢 Aprovado |
| PM Canvas | 10% | 9.0/10 | 🟢 Aprovado |
| ERF | 15% | 8.5/10 | 🟢 Aprovado |
| Cronograma | 20% | 9.0/10 | 🟢 Aprovado |
| Plano de Riscos | 15% | 8.5/10 | 🟢 Aprovado |
| KPIs | 10% | 9.0/10 | 🟢 Aprovado |
| Status Report | 5% | 8.5/10 | 🟢 Aprovado |
| **CONSOLIDADO** | **100%** | **8.7/10** | **🟢 APROVADO** |

**Cálculo:** (8.5×0.25)+(9.0×0.10)+(8.5×0.15)+(9.0×0.20)+(8.5×0.15)+(9.0×0.10)+(8.5×0.05) = **8.70/10**

Limiar de aprovação: ≥ 7.0 sem critérios BLOCKING. **Resultado: ACIMA DO LIMIAR.**

---

## VERIFICAÇÃO DE CRITÉRIOS BLOCKING

| Documento | Critério BLOCKING | Status |
|-----------|-------------------|--------|
| TAP | Objetivo SMART com métrica e prazo | ✅ ATENDIDO |
| TAP | Sponsor identificado com cargo e autoridade | ✅ ATENDIDO |
| TAP | Escopo delimitado (dentro e fora) | ✅ ATENDIDO |
| TAP | Mínimo 3 critérios de sucesso mensuráveis | ✅ ATENDIDO (5 critérios) |
| PM Canvas | Todos os 9 blocos preenchidos | ✅ ATENDIDO |
| ERF | Priorização MoSCoW aplicada | ✅ ATENDIDO |
| ERF | Critério de aceitação para todos os Must Have | ✅ ATENDIDO |
| ERF | ID único por requisito (RF/RNF) | ✅ ATENDIDO |
| Cronograma | WBS com mínimo 3 níveis | ✅ ATENDIDO |
| Cronograma | Caminho crítico identificado | ✅ ATENDIDO (⭐) |
| Cronograma | Buffer de contingência centralizado | ✅ ATENDIDO (8du) |
| Riscos | Mínimo 5 riscos documentados | ✅ ATENDIDO (7 riscos) |
| Riscos | Probabilidade e impacto por risco | ✅ ATENDIDO |
| Riscos | Estratégia de resposta por risco | ✅ ATENDIDO |
| Riscos | Trigger para riscos ALTO | ✅ ATENDIDO (R01, R02, R03) |
| KPIs | CPI e SPI presentes | ✅ ATENDIDO |
| KPIs | KPIs derivados dos critérios de sucesso | ✅ ATENDIDO (5 KRs) |
| Status Report | Semáforo consolidado presente | ✅ ATENDIDO |
| Status Report | Issues com dono e prazo | ✅ ATENDIDO |

**Nenhum critério BLOCKING não atendido.**

---

## VERIFICAÇÃO DE CONSISTÊNCIA CROSS-DOCUMENTO

| Campo | TAP | Cronograma | KPIs | Status Report | Consistente? |
|-------|-----|------------|------|---------------|-------------|
| Prazo máximo | 60du | 60du (52+8 buffer) | Du 60 | 60du | ✅ |
| Orçamento teto | R$ 8.640 | — | BAC R$ 8.640 | R$ 8.640 | ✅ |
| Sponsor | Diretor Financeiro | — | — | Diretor Financeiro | ✅ |
| Critérios de sucesso | 5 critérios | M0–M6 alinhados | 5 KRs (1:1) | 5 entregas | ✅ |
| Riscos de alto nível | 5 no TAP | — | 3 ALTOs no semáforo | 7 no report | ✅ |

---

## PONTOS FORTES

1. **Qualificação com resolução de lacunas exemplar:** A decisão inicial EM ESPERA foi corretamente revertida para APROVADO COM CONDIÇÕES após complementação das informações críticas pelo responsável do PMO. O processo funcionou como filtro de maturidade, não como barreira burocrática.

2. **Rastreabilidade end-to-end:** Cada critério de sucesso do TAP tem um KR correspondente nos KPIs com threshold de alerta. A cadeia TAP → KPIs → Status Report é coerente e completamente auditável.

3. **Plano de Riscos com análise contextual:** A observação sobre R03 (o Sponsor é também o Aprovador a ser incluído no fluxo) demonstra análise contextual e não mecânica — insight raro e de alto valor para a gestão do projeto.

4. **Cronograma com premissa de disponibilidade documentada:** A estimativa explícita de 70% de disponibilidade da equipe Basis protege o projeto de expectativas irrealistas — boa prática frequentemente omitida em projetos de TI.

5. **Documentação completa em único ciclo:** 7 documentos de iniciação produzidos sem necessidade de revisão ou retrabalho, demonstrando a eficácia do pipeline VMO Autônomo.

---

## SUGESTÕES (não bloqueantes — para a fase de execução)

1. **RACI explícito:** Quando o GP for designado, elaborar tabela RACI para os papéis do projeto — o projeto tem poucos atores mas a ausência do GP hoje cria um vazio de responsabilidade.

2. **Atenção à reserva de contingência vs. valor esperado de riscos:** O valor esperado calculado dos riscos (R$ 5.450) supera a contingência do orçamento (R$ 1.440). O GP deve apresentar este dado ao Sponsor no kickoff — especialmente o risco R01 (limitação ABAP), que sozinho geraria R$ 3.000 de valor esperado.

3. **Pesquisa de satisfação da iniciação:** Incluir avaliação da qualidade da documentação de iniciação pelo Sponsor no kickoff seria valioso para o aprendizado organizacional do VMO.

---

## APROVAÇÃO FINAL

**Pontuação:** 8.7/10 — **APROVADO**
**Aprovado por:** Marcelo Silveira — VMO Consultoria
**Data:** 2026-04-03 — Checkpoint Final (Step 12)

---

*Documento gerado por Vera Veredito — Revisora de Qualidade VMO | VMO Autônomo Squad*
*Revisão 1 de 3 — 2026-04-03 — VEREDICTO: APROVADO*

---

---

*Pacote de iniciação consolidado pelo VMO Autônomo Squad — VMO Consultoria*
*Gerado em: 2026-04-03 | Pipeline: 12 steps | Score: 8.7/10 | Status: APROVADO*
*Todos os documentos deste pacote estão em versão 1.0 e aguardam assinatura formal do Sponsor para ativação do projeto.*
