# DOCUMENTAÇÃO BASE DO PROJETO
## DEM-2026-001 — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados

Versão: 1.0 | Data: 2026-04-03 | Gerado por: Diana Documento — Arquiteta de Projetos VMO

---

---

# TASK 1 — TERMO DE ABERTURA DO PROJETO (TAP)

---

```
TERMO DE ABERTURA DO PROJETO
Versão: 1.1 | Data: 2026-04-05 | Status: AGUARDANDO ASSINATURA
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
| Gerente de Projeto     | A designar pelo PMO                                                  |
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
4. **Ambiente de produção:** Nenhuma alteração pode ser realizada diretamente em PRD sem ter passado pelos testes em QAS e sem aprovação formal do Gerente de Projeto e do Sponsor (ou preposto designado).
5. **Conformidade com processo de change management do cliente:** Todos os transportes entre ambientes devem seguir o processo formal de gestão de mudanças do ambiente SAP do cliente.

---

## RISCOS DE ALTO NÍVEL

| # | Risco | Probabilidade | Impacto | Resposta Preliminar |
|---|-------|--------------|---------|---------------------|
| R01 | Indisponibilidade do ambiente QAS para testes no prazo planejado, atrasando a validação e a go-live | Médio | Alto | Reservar janela de QAS com antecedência mínima de 2 semanas; incluir folga de 5 dias úteis no cronograma de testes |
| R02 | A parametrização via ZFI0057 revelar limitação técnica exigindo desenvolvimento ABAP não previsto, impactando custo e prazo | Baixo | Alto | Realizar análise técnica detalhada (spike técnico) na fase de planejamento antes de qualquer comprometimento de prazo; escalar ao Sponsor imediatamente se confirmado |
| R03 | Indisponibilidade ou baixa adesão do Diretor Financeiro para treinamento e validação antes da go-live, postergando a entrada em produção | Médio | Médio | Engajar o Sponsor para garantir compromisso do Diretor Financeiro desde o início; agendar treinamento com antecedência de 10 dias úteis; ter alternativa de treinamento assíncrono (vídeo + guia) |
| R04 | Processo de change management do cliente (janelas de transporte PRD) incompatível com o cronograma do projeto | Médio | Médio | Mapear calendário de transportes na fase de iniciação; planejar transporte PRD com margem de 5 dias úteis antes do prazo final |
| R05 | Identificação tardia de outros aprovadores no fluxo atual impactados pela parametrização, gerando resistência ou necessidade de redesenho | Baixo | Médio | Mapear todos os aprovadores atuais do fluxo ZFI0057 antes de iniciar a parametrização; validar com área de negócio |

---

## PARTES INTERESSADAS PRINCIPAIS

| Stakeholder | Papel no Projeto | Interesse / Influência | Nível de Engajamento Necessário |
|-------------|-----------------|----------------------|---------------------------------|
| Diretor Financeiro — VIX Manutenção | Sponsor / Aprovador final incluído no fluxo | Alto / Alto | Liderança ativa — aprovar TAP, validar solução, participar de treinamento |
| Andre Chieppe — Diretor Financeiro — VIX Manutenção | Sponsor / Aprovador final incluído no fluxo | Alto / Alto | Liderança ativa |
| Ivanilde Ribeiro Machado | Solicitante / Ponto focal da área de negócio | Alto / Médio | Colaborativo — validar requisitos, participar de testes de aceitação |
| Gerente de Projeto (a designar pelo PMO) | Responsável pela entrega | Alto / Alto | Liderança operacional do projeto |
| Equipe DTI / Basis SAP | Executora técnica | Médio / Alto | Colaborativo — executar parametrização, testes e transporte |
| PMO VMO Consultoria | Governança e acompanhamento | Médio / Médio | Monitoramento — receber status reports e validar entregas nos gates |
| Usuários do fluxo de aprovação SAP FI | Afetados pela mudança no fluxo | Médio / Baixo | Informado — comunicar a mudança antes da go-live |

---

## ORÇAMENTO RESUMIDO

| Item | Valor Estimado |
|------|----------------|
| Análise técnica e parametrização SAP (ZFI0057 + SBWP) | R$ 2.400 – R$ 4.800 |
| Testes integrados em QAS | R$ 720 – R$ 1.440 |
| Treinamento do aprovador e documentação | R$ 480 – R$ 960 |
| Acompanhamento pós go-live (10 dias úteis) | R$ 360 – R$ 720 |
| **Subtotal (sem contingência)** | **R$ 3.960 – R$ 7.920** |
| Contingência (20%) | R$ 792 – R$ 1.584 *(já incluída na faixa aprovada)* |
| **TOTAL APROVADO (teto máximo)** | **R$ 8.640** |

> Faixa estimada total (já com contingência embutida na faixa comercial aprovada): **R$ 4.320 – R$ 8.640**. O valor de **R$ 8.640** é o teto aprovado para este projeto.

---

## CRONOGRAMA SUMARIZADO

| Fase | Descrição | Duração Estimada | Data Início (ref.) | Data Fim (ref.) |
|------|-----------|-----------------|-------------------|-----------------|
| F1 — Iniciação | Assinatura do TAP, designação do GP, kickoff | 5 du | Du 1 | Du 5 |
| F2 — Planejamento | Análise técnica detalhada (spike), plano detalhado, mapeamento de stakeholders e riscos | 10 du | Du 6 | Du 15 |
| F3 — Execução / Parametrização | Parametrização em DEV, testes unitários, transporte para QAS | 15 du | Du 16 | Du 30 |
| F4 — Testes Integrados (QAS) | Testes de aprovação/rejeição, validação com área de negócio, ajustes | 10 du | Du 31 | Du 40 |
| F5 — Go-Live (PRD) | Transporte para PRD, treinamento do aprovador, entrada em produção supervisionada | 5 du | Du 41 | Du 45 |
| F6 — Acompanhamento pós go-live | Monitoramento de 10 du, coleta de evidências de sucesso, encerramento | 15 du | Du 46 | Du 60 |
| **TOTAL** | | **60 dias úteis** | **Dia da assinatura do TAP** | **Du 60** |

> Datas absolutas serão definidas após assinatura formal do TAP e designação do Gerente de Projeto.

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

# TASK 2 — PM CANVAS

---

```
PM CANVAS — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados
Versão: 1.0 | Data: 2026-04-03 | Projeto: PROJ-2026-001
```

---

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│          PM CANVAS — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados                 │
│          PROJ-2026-001 | Versão 1.0 | 2026-04-03                                             │
├──────────────────────────────┬───────────────────────────────┬─────────────────────────────-─┤
│  1. POR QUÊ?                 │  2. O QUÊ?                    │  3. QUEM?                     │
│                              │                               │                               │
│  O Diretor Financeiro estava │  ENTREGÁVEIS:                 │  SPONSOR:                     │
│  ausente do fluxo de         │  E1 — Parametrização ativa    │  Diretor Financeiro           │
│  aprovação de lançamentos    │       em PRD: ZFI0057 com     │  VIX Manutenção               │
│  pré-editados no SAP FI,     │       Diretor Financeiro como │                               │
│  criando lacuna de controle  │       aprovador obrigatório   │  SOLICITANTE:                 │
│  e risco de fraude.          │  E2 — Workflow SBWP           │  Ivanilde Ribeiro Machado     │
│                              │       configurado e roteando  │                               │
│  A ausência impede que o     │       tarefas corretamente    │  GERENTE DO PROJETO:          │
│  principal executivo         │  E3 — Testes integrados       │  A designar pelo PMO          │
│  financeiro da área exerça   │       executados e aprovados  │                               │
│  sua responsabilidade de     │       em QAS                  │  EQUIPE TÉCNICA:              │
│  controle sobre lançamentos  │  E4 — Treinamento do          │  DTI / Basis SAP              │
│  de maior materialidade.     │       aprovador realizado     │                               │
│                              │  E5 — Documentação técnica    │  STAKEHOLDERS CHAVE:          │
│  BENEFÍCIOS ESPERADOS:       │       e operacional entregue  │  - Usuários fluxo SAP FI      │
│  - Redução do risco de       │  E6 — Acompanhamento pós      │  - PMO VMO Consultoria        │
│    fraude no processo de     │       go-live de 10 du com    │  - Área de Controles          │
│    lançamentos pré-editados  │       evidências coletadas    │    Internos (se aplicável)    │
│  - Aumento da governança     │                               │                               │
│    financeira com a          │  PRODUTO FINAL:               │                               │
│    participação do Diretor   │  Fluxo de aprovação SAP FI    │                               │
│    Financeiro no processo    │  operacional em PRD, com      │                               │
│  - Conformidade com o        │  100% dos lançamentos         │                               │
│    modelo de controle        │  pré-editados passando pelo   │                               │
│    interno esperado          │  Diretor Financeiro           │                               │
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────┤
│  4. COMO?                    │  5. QUANDO?                   │  6. QUANTO?                   │
│                              │                               │                               │
│  METODOLOGIA:                │  MARCOS PRINCIPAIS:           │  ORÇAMENTO APROVADO:          │
│  Gestão de projeto ágil-     │                               │  Teto: R$ 8.640               │
│  adaptativa em fases com     │  M1 — Assinatura do TAP       │  (contingência 20% incluída)  │
│  gates de qualidade.         │       Dia 1 (Du 1)            │                               │
│  Projeto de baixa            │                               │  FAIXA ESTIMADA:              │
│  complexidade — equipe       │  M2 — Análise técnica         │  R$ 4.320 – R$ 8.640          │
│  enxuta, reuniões objetivas, │       concluída               │                               │
│  entregáveis documentados.   │       Du 15                   │  DISTRIBUIÇÃO ESTIMADA:       │
│                              │                               │  - Parametrização: 60%        │
│  ABORDAGEM TÉCNICA:          │  M3 — Aprovação QAS           │  - Testes: 17%                │
│  - Parametrização via        │       (go/no-go para PRD)     │  - Treinamento/docs: 12%      │
│    ZFI0057 para inclusão do  │       Du 40                   │  - Acomp. pós go-live: 8%     │
│    aprovador no fluxo        │                               │  - Contingência: 20%          │
│  - Configuração do workflow  │  M4 — GO-LIVE em PRD          │    (sobre subtotal)           │
│    SBWP para roteamento      │       Du 45                   │                               │
│    correto da tarefa         │                               │  CUSTO DE OPERAÇÃO:           │
│  - Transporte controlado     │  M5 — Encerramento do         │  Zero — solução sobre         │
│    DEV → QAS → PRD           │       projeto (evidências     │  infraestrutura SAP já        │
│  - Treinamento prático do    │       coletadas + aceite)     │  licenciada                   │
│    Diretor Financeiro no     │       Du 60                   │                               │
│    SBWP antes da go-live     │                               │                               │
│                              │  PRAZO TOTAL: 60 dias úteis   │                               │
│  FERRAMENTAS:                │  a partir da assinatura       │                               │
│  - SAP FI (ZFI0057 + SBWP)  │  do TAP                       │                               │
│  - MS Project / Planner      │                               │                               │
│    (cronograma)              │                               │                               │
│  - SharePoint / e-mail       │                               │                               │
│    (comunicação e docs)      │                               │                               │
├──────────────────────────────┼───────────────────────────────┼───────────────────────────────┤
│  7. PREMISSAS                │  8. RESTRIÇÕES                │  9. RISCOS                    │
│                              │                               │                               │
│  P1 — Ambiente SAP FI        │  RT1 — Orçamento fixo em      │  R01 — Indisponibilidade      │
│       (ZFI0057 + SBWP)       │        R$ 8.640 (teto         │  do QAS no prazo planejado    │
│       implantado, estável e  │        aprovado com           │  → Prob: Médio | Imp: Alto    │
│       acessível à DTI        │        contingência 20%       │  → Mitigar: reservar janela   │
│                              │        incluída)              │    com 2 semanas de           │
│  P2 — Ambiente QAS           │                               │    antecedência               │
│       disponível para testes │  RT2 — Prazo máximo de 60     │                               │
│       antes da go-live       │        dias úteis sem         │  R02 — Necessidade de         │
│                              │        prorrogação não        │  desenvolvimento ABAP não     │
│  P3 — Diretor Financeiro     │        autorizada             │  previsto na parametrização   │
│       ciente, disponível e   │                               │  → Prob: Baixo | Imp: Alto    │
│       apoiador da iniciativa │  RT3 — Solução restrita à     │  → Mitigar: spike técnico     │
│                              │        parametrização nas     │    na fase de planejamento    │
│  P4 — DTI possui perfis SAP  │        transações existentes  │                               │
│       com autorização para   │        (sem dev ABAP ou       │  R03 — Baixa adesão do        │
│       parametrizar ZFI0057   │        novas licenças)        │  Diretor Financeiro ao        │
│       em QAS e PRD           │                               │  treinamento pré go-live      │
│                              │  RT4 — Obrigatoriedade de     │  → Prob: Médio | Imp: Médio   │
│  P5 — Processo de change     │        seguir o processo de   │  → Mitigar: engajamento       │
│       management do cliente  │        change management do   │    via Sponsor; treinamento   │
│       tem janelas            │        cliente para           │    assíncrono como backup     │
│       compatíveis com o      │        transportes DEV →      │                               │
│       cronograma do projeto  │        QAS → PRD              │                               │
│                              │                               │                               │
│  P6 — A parametrização não   │  RT5 — Alterações de escopo   │                               │
│       requer nota SAP OSS    │        requerem aprovação      │                               │
│       nem suporte do         │        formal do Sponsor e    │                               │
│       fabricante             │        revisão do TAP         │                               │
└──────────────────────────────┴───────────────────────────────┴───────────────────────────────┘
```

---

---

# TASK 3 — PLANO GERAL DO PROJETO

---

```
PLANO GERAL DO PROJETO
Projeto: PROJ-2026-001 — Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados
Versão: 1.1 | Data: 2026-04-05 | Status: AGUARDANDO ASSINATURA DO TAP
```

---

## 1. GERENCIAMENTO DO ESCOPO

**Abordagem:** O escopo está definido no TAP (PROJ-2026-001 v1.0) e limitado à parametrização das transações ZFI0057 e SBWP para inclusão do Diretor Financeiro como aprovador obrigatório de lançamentos pré-editados. Qualquer alteração de escopo passa pelo processo formal de Controle de Mudanças (ver Plano 10).

**Ferramenta:** Documento de Escopo (EAP de 2 níveis suficiente para este projeto) + Matriz de Rastreabilidade de Requisitos simplificada.

**Responsável:** Gerente de Projeto.

**EAP de Alto Nível:**

```
PROJ-2026-001
├── 1. Iniciação
│   ├── 1.1 Assinatura do TAP
│   └── 1.2 Kickoff
├── 2. Planejamento
│   ├── 2.1 Análise técnica (spike)
│   └── 2.2 Plano detalhado aprovado
├── 3. Parametrização (DEV)
│   ├── 3.1 Configuração ZFI0057
│   ├── 3.2 Configuração SBWP
│   └── 3.3 Testes unitários em DEV
├── 4. Testes Integrados (QAS)
│   ├── 4.1 Transporte DEV → QAS
│   ├── 4.2 Execução dos testes integrados
│   └── 4.3 Validação e aceite da área de negócio
├── 5. Go-Live (PRD)
│   ├── 5.1 Treinamento do aprovador
│   ├── 5.2 Transporte QAS → PRD
│   └── 5.3 Go-live supervisionado
└── 6. Encerramento
    ├── 6.1 Acompanhamento pós go-live (10 du)
    ├── 6.2 Coleta de evidências de sucesso
    └── 6.3 Encerramento formal e lições aprendidas
```

**Validação de escopo:** Aceite formal de cada entregável pela área solicitante (Ivanilde Ribeiro Machado) e pelo Sponsor nos gates de qualidade.

---

## 2. GERENCIAMENTO DO CRONOGRAMA

**Abordagem:** Cronograma em fases sequenciais com gates (ver seção Ciclo de Vida e Gates). Linha de base de 60 dias úteis fixada após kickoff. Desvios superiores a 5 dias úteis são formalmente comunicados ao Sponsor.

**Ferramenta:** MS Project ou Planner (lista de tarefas com dependências, datas e responsáveis). Para projeto desta complexidade, planilha de cronograma simplificada é admissível.

**Responsável:** Gerente de Projeto.

**Frequência de atualização:** Semanal (toda segunda-feira), com status consolidado no status report quinzenal ao Sponsor.

**Marcos de referência:**

| Marco | Prazo (du a partir da assinatura do TAP) |
|-------|------------------------------------------|
| M1 — Assinatura do TAP / Kickoff | Du 1 |
| M2 — Análise técnica concluída e validada | Du 15 |
| M3 — Parametrização em DEV concluída | Du 30 |
| M4 — Aprovação QAS (go/no-go PRD) | Du 40 |
| M5 — Go-live PRD | Du 45 |
| M6 — Encerramento (evidências + aceite final) | Du 60 |

---

## 3. GERENCIAMENTO DOS CUSTOS

**Abordagem:** Orçamento base de R$ 4.320 – R$ 8.640 (teto aprovado: R$ 8.640, com contingência de 20% já incluída). Gastos registrados pelo GP a cada evento de custo. Reserva de contingência gerenciada pelo GP dentro do teto aprovado; reserva de gestão (acima do teto) requer aprovação do Sponsor.

**Ferramenta:** Planilha de controle de custos (comprometido vs. realizado vs. orçado) — atualizada a cada evento de custo ou semanalmente (o que ocorrer primeiro).

**Responsável:** Gerente de Projeto (registro e controle); Sponsor (aprovação de variações acima do teto).

**Limites de alerta:**
- Custo realizado ≥ 80% do teto (≥ R$ 6.912) → alerta formal ao Sponsor.
- Custo realizado ≥ 100% do teto → paralisação e reunião de crise com Sponsor.

---

## 4. GERENCIAMENTO DA QUALIDADE

**Abordagem:** Qualidade garantida por gate de testes integrados obrigatório em QAS antes de qualquer promoção para PRD. Critérios de aceite definidos nos casos de teste (ver abaixo). Revisão de qualidade da documentação pelo GP antes de cada entrega ao cliente.

**Ferramenta:** Casos de teste documentados (aprovação, rejeição, roteamento de exceção) + Checklist de aceite por entregável.

**Responsável:** DTI (execução dos testes técnicos); Ivanilde Ribeiro Machado / área de negócio (aceite funcional em QAS); GP (validação da documentação).

**Critérios mínimos de aceite para go-live:**
1. 100% dos cenários de teste executados e aprovados em QAS.
2. Aceite formal da área de negócio registrado (e-mail ou assinatura em ata).
3. Treinamento do aprovador concluído e confirmado.
4. Documentação técnica e operacional entregue e revisada.

---

## 5. GERENCIAMENTO DOS RECURSOS

**Abordagem:** Equipe enxuta — projeto de baixa complexidade não justifica estrutura ampliada. Alocação parcial (part-time) da equipe técnica DTI é suficiente. Responsabilidades definidas na matriz RACI abaixo.

**Ferramenta:** Matriz RACI + calendário de alocação simplificado acordado no kickoff.

**Responsável:** GP coordena a alocação; DTI fornece o recurso técnico de Basis/SAP FI.

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

*R=Responsável pela execução | A=Accountable (aprova) | C=Consultado | I=Informado*

**Recursos necessários estimados:**
- 1 consultor SAP FI/Basis (part-time, DTI) — análise, parametrização, testes e go-live
- 1 Gerente de Projeto (part-time, PMO VMO)
- Disponibilidade do Diretor Financeiro para treinamento (~2h)
- Disponibilidade de Ivanilde para kickoff, validação de requisitos e aceite (~4h total)

---

## 6. GERENCIAMENTO DAS COMUNICAÇÕES

**Abordagem:** Comunicação objetiva e direcionada ao papel de cada stakeholder. Documentos formais por e-mail com confirmação de recebimento. Atas de reunião em até 24h após cada reunião. Canal único oficial: e-mail corporativo + SharePoint do projeto (ou pasta compartilhada acordada no kickoff).

**Ferramenta:** E-mail corporativo (comunicações formais) + SharePoint / pasta compartilhada (repositório de documentos) + reuniões por videoconferência ou presenciais.

**Responsável:** GP é responsável por todas as comunicações formais do projeto.

**Tabela de Comunicações:**

| Comunicação | Audiência | Frequência | Canal | Responsável | Formato |
|-------------|-----------|-----------|-------|-------------|---------|
| Status Report do Projeto | Sponsor, PMO VMO, Solicitante | Quinzenal | E-mail | GP | Relatório de 1 página (RAG status: Escopo / Prazo / Custo / Riscos) |
| Ata de Reunião | Todos os participantes da reunião | Por reunião (em até 24h) | E-mail | GP | Ata padronizada com decisões e encaminhamentos |
| Alerta de Risco / Desvio | Sponsor, PMO VMO | Ad hoc (quando identificado) | E-mail + telefone | GP | Comunicado de desvio com análise de impacto e proposta de ação |
| Comunicado de Go-Live | Todos os usuários do fluxo SAP FI afetados | Uma vez (antes da go-live) | E-mail | GP / DTI | Comunicado de mudança com orientações básicas |
| Relatório de Encerramento | Sponsor, PMO VMO, Solicitante | Uma vez (ao final do projeto) | E-mail + reunião de encerramento | GP | Relatório de encerramento PMBOK simplificado |
| Kickoff Meeting | Todos os stakeholders | Uma vez (Du 1) | Videoconferência ou presencial | GP | Apresentação + ata |
| Reunião de Gate (QAS → PRD) | Sponsor, GP, DTI, Solicitante | Uma vez (Du 40) | Videoconferência ou presencial | GP | Checklist de gate + decisão formal go/no-go |

---

## 7. GERENCIAMENTO DOS RISCOS

**Abordagem:** Identificação inicial no TAP (5 riscos de alto nível). Revisão do registro de riscos em cada status report quinzenal. Resposta baseada em mitigação preventiva para riscos Médio/Alto; aceitação para riscos Baixo/Baixo.

**Ferramenta:** Registro de Riscos (planilha) atualizado quinzenalmente pelo GP.

**Responsável:** GP (identificação, avaliação e coordenação das respostas); DTI (execução de respostas técnicas).

**Escala de avaliação:**
- Probabilidade: Baixo / Médio / Alto
- Impacto: Baixo / Médio / Alto
- Criticidade = Probabilidade × Impacto (matriz 3x3)

**Registro de Riscos Inicial:**

| ID | Risco | Prob. | Imp. | Criticidade | Resposta | Responsável |
|----|-------|-------|------|-------------|----------|-------------|
| R01 | Indisponibilidade do QAS no prazo | Médio | Alto | Alta | Mitigar: reservar janela com 2 semanas de antecedência | GP + DTI |
| R02 | Necessidade de dev ABAP não previsto | Baixo | Alto | Média | Mitigar: spike técnico na fase de planejamento (Du 6-15) | DTI / Basis |
| R03 | Baixa adesão do Diretor Financeiro ao treinamento | Médio | Médio | Média | Mitigar: engajamento via Sponsor; backup assíncrono | GP + Sponsor |
| R04 | Janelas de transporte PRD incompatíveis | Médio | Médio | Média | Mitigar: mapear calendário na iniciação; folga de 5 du | GP + DTI |
| R05 | Impacto em outros aprovadores do fluxo atual | Baixo | Médio | Baixa | Mitigar: mapear aprovadores atuais antes de parametrizar | DTI + Solicitante |

**Gatilho para escalada ao Sponsor:** Qualquer risco que evolua para criticidade Alta durante o projeto.

---

## 8. GERENCIAMENTO DAS AQUISIÇÕES

**Abordagem:** Projeto executado com recursos internos (DTI) e/ou consultoria já contratada (VMO Consultoria). Não há previsão de aquisições externas — nenhum software adicional, licença SAP extra ou serviço de terceiros é necessário para a parametrização.

**Ferramenta:** Não aplicável — sem aquisições previstas.

**Responsável:** GP monitora a necessidade; qualquer aquisição não prevista (ex.: licença adicional por limitação técnica identificada) deve ser formalmente solicitada ao Sponsor como mudança de escopo/custo.

**Premissa:** Se durante a análise técnica (spike — Du 6-15) for identificada a necessidade de suporte SAP (nota OSS) ou serviço externo, o GP avaliará o impacto no orçamento e comunicará o Sponsor antes de qualquer comprometimento.

---

## 9. GERENCIAMENTO DOS STAKEHOLDERS

**Abordagem:** Mapeamento inicial de stakeholders no TAP. Estratégia de engajamento diferenciada por nível de influência e interesse. Revisão do engajamento a cada status report quinzenal.

**Ferramenta:** Registro de Stakeholders + Matriz Poder × Interesse.

**Responsável:** GP (gestão do engajamento); Sponsor (engajamento do Diretor Financeiro quando necessário).

**Estratégia por stakeholder:**

| Stakeholder | Estratégia de Engajamento | Frequência de Contato |
|-------------|--------------------------|----------------------|
| Diretor Financeiro (Sponsor) | Engajar ativamente — aprovações formais, briefings diretos do GP, convites para gates de qualidade | Quinzenal (status report) + gates (du 40 e du 60) |
| Ivanilde Ribeiro Machado (Solicitante) | Colaborar — validações de requisito, aceite em QAS, comunicação de go-live | Conforme necessidade do projeto (mínimo 3 pontos de contato: kickoff, aceite QAS, encerramento) |
| Equipe DTI / Basis | Gerenciar de perto — briefings técnicos, alocação, suporte | Semanal (reunião de trabalho) |
| PMO VMO Consultoria | Manter satisfeito — status reports quinzenais, alertas de desvio | Quinzenal |
| Usuários do fluxo SAP FI | Informar — comunicado de go-live com antecedência mínima de 3 du | Uma vez antes da go-live |

---

## 10. GERENCIAMENTO DAS MUDANÇAS

**Abordagem:** Toda solicitação de mudança de escopo, prazo ou orçamento deve ser documentada formalmente pelo GP, avaliada quanto ao impacto nos três parâmetros (escopo/prazo/custo), e aprovada pelo Sponsor antes de ser implementada. Mudanças não aprovadas não são executadas.

**Ferramenta:** Formulário de Solicitação de Mudança (FSM) — versão simplificada (campos: descrição da mudança, solicitante, data, impacto estimado em escopo/prazo/custo, decisão do Sponsor).

**Responsável:** GP (recebe, avalia e documenta); Sponsor (aprova ou rejeita).

**Processo:**

```
1. Identificação da necessidade de mudança (qualquer stakeholder)
       ↓
2. GP documenta a solicitação no FSM e avalia impacto
       ↓
3. GP apresenta ao Sponsor com análise de impacto
       ↓
4. Sponsor decide: APROVADO / REJEITADO / PENDENTE (informação adicional)
       ↓
5. GP atualiza o plano (TAP, cronograma, orçamento) se aprovado
   OU comunica a rejeição ao solicitante se rejeitado
       ↓
6. GP registra a decisão no log de mudanças e comunica a todos os afetados
```

**Critério de urgência:** Mudanças com impacto crítico no go-live (ex.: bloqueio técnico identificado) podem ser decididas em call de urgência com o Sponsor em até 24h.

---

## CICLO DE VIDA E GATES DE QUALIDADE

**Ciclo de vida do projeto:** Preditivo em fases com gates de progressão. A progressão entre fases é condicionada à aprovação formal nos gates. Nenhuma fase inicia antes do gate da fase anterior ser aprovado.

**Tabela de Gates:**

| Gate | Ocorre em | Critérios de Progressão (todos devem ser atendidos) | Aprovadores |
|------|-----------|-----------------------------------------------------|-------------|
| **G1 — Iniciação → Planejamento** | Du 5 (após kickoff) | TAP assinado pelo Sponsor; GP designado; time definido; repositório do projeto criado | Sponsor + PMO VMO |
| **G2 — Planejamento → Execução** | Du 15 (após análise técnica) | Análise técnica concluída sem bloqueadores identificados (ou plano de mitigação aprovado); cronograma detalhado aprovado; orçamento confirmado dentro do teto; riscos mapeados no registro | GP + Sponsor |
| **G3 — Execução/DEV → Testes QAS** | Du 30 (após parametrização DEV) | Parametrização concluída em DEV; testes unitários executados e aprovados; transporte DEV→QAS realizado; casos de teste para QAS documentados | GP + DTI |
| **G4 — Testes QAS → Go-Live PRD** | Du 40 (após testes QAS) | 100% dos cenários de teste executados e aprovados em QAS; aceite formal da área de negócio (Ivanilde) obtido; treinamento do Diretor Financeiro agendado; plano de go-live aprovado; transporte QAS→PRD autorizado | Sponsor + GP + Solicitante |
| **G5 — Encerramento** | Du 60 (após acompanhamento pós go-live) | Go-live em PRD com 10 du de operação estável; evidências dos critérios de sucesso coletadas (relatório de 100% de cobertura do fluxo; zero bypass); documentação entregue e aceita; relatório de encerramento aprovado; lições aprendidas registradas | Sponsor + PMO VMO |

---

## CONSIDERAÇÕES FINAIS DO PLANO GERAL

Este Plano Geral, combinado com o TAP (PROJ-2026-001) e o PM Canvas, constitui a documentação base de iniciação do projeto. O nível de detalhe dos planos subsidiários é proporcional à complexidade do projeto — baixa — e será expandido pelo Gerente de Projeto designado durante a fase de Planejamento (Du 6-15), conforme a análise técnica revelar requisitos adicionais.

**Próximos passos imediatos:**
1. Confirmar nome completo do Diretor Financeiro (Sponsor) para finalizar o TAP.
2. PMO designar o Gerente de Projeto.
3. Agendar kickoff (Du 1 após assinatura do TAP).
4. Reservar janela de QAS para testes (Du 31-40).

---

*Documento gerado por Diana Documento — Arquiteta de Projetos, Squad VMO Autônomo*
*VMO Consultoria | PROJ-2026-001 | Versão 1.0 | 2026-04-03*
