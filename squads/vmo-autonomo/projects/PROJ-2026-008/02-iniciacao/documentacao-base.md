# Documentação Base de Iniciação — PROJ-2026-008
Demanda de origem: DEM-2026-008
Autora: Diana Documento (Arquiteta de Projetos, VMO Autônomo)
Data: 2026-07-07
Status: RASCUNHO — Documentos elaborados com 6 condições bloqueantes (CBs) ainda em aberto (ver `qualificacao-aprovada.md`). O GP (Marcelo Silveira, PMO) decidiu avançar a documentação em paralelo à resolução das CBs, não após.

---

# DOCUMENTO 1 — TERMO DE ABERTURA DO PROJETO (TAP)

```
TERMO DE ABERTURA DO PROJETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Versão: 1.0
Data: 2026-07-07
Status: RASCUNHO — Aguardando resolução das Condições Bloqueantes (CB-1 a CB-6) e Aprovação Formal do Sponsor

IDENTIFICAÇÃO DO PROJETO
  Nome: Implantação/Expansão do TVM para Fluxo de Caixa, Controle
        Orçamentário e Rastreabilidade de Riscos (Grupo Águia Branca)
  ID:    PROJ-2026-008
  Demanda de origem: DEM-2026-008
  Área Solicitante: Financeiro (com Suprimentos e Gestão de Riscos e
        Desempenho Organizacional como áreas coimpactadas — projeto
        único com 3 frentes, não 3 projetos separados)
  Área Executora: Equipe técnica TVM / TI (líder técnico: Cássio)

AUTORIZAÇÃO
  Sponsor: Paula Barcelos — CEO
    ⚠️ ATENÇÃO (CB-1): identidade e cargo do sponsor confirmados
    VERBALMENTE nesta sessão pelo Coordenador PMO (Marcelo Silveira).
    NÃO existe ainda evidência documental formal (e-mail, ata assinada
    ou comunicado oficial) desta aprovação, conforme exigido pela
    Regra GP 2026-05-24. Este TAP NÃO deve ser tratado como assinado
    ou formalmente aprovado até que essa evidência seja produzida.
  Solicitante formal: Alessandra Comério — Financeiro
  Líder técnico: Cássio
  Gerente de Projeto: A designar (PMO ainda não alocou GP formal)
  Autoridade do GP (proposta, a confirmar na designação):
    Aprovar gastos operacionais até R$ 3.000 sem escalar ao sponsor;
    Solicitar recursos das 3 áreas impactadas via seus respectivos
    gestores (Alessandra/Financeiro, Wellington Gonçalves/Suprimentos,
    Thamyris/Riscos e Desempenho Organizacional).

OBJETIVO DO PROJETO (SMART)
  Substituir o processo hoje manual de controle de fluxo de caixa e
  orçamento (Excel + extrações SAP), concentrado em poucas pessoas
  (com forte dependência de Thamyris), por uma operação estruturada
  no TVM (nos moldes já validados pela VIX), cobrindo de forma
  unificada as 3 frentes do Grupo Águia Branca:
    (1) Financeiro — fluxo de caixa segregado por tipo de negócio e
        categoria de despesa até o LAIR, com apresentação à diretoria
        sem depender de consolidação manual semanal;
    (2) Suprimentos — controle orçamentário com baseline atualizado
        automaticamente e alertas de consumo por faixa (70%/85%);
    (3) Riscos/Desempenho — rastreabilidade de custos e previsão de
        caixa ampliada de horizonte mensal para 90 dias.
  Métrica de sucesso: as 3 frentes operando no TVM em produção, com
  eliminação da consolidação manual em Excel como fonte primária de
  informação para diretoria.
  Prazo: DATA-ALVO = T0 + ~13,4 SEMANAS ÚTEIS (~67 dias úteis) até o
    Go-live (M4), e T0 + ~90 DIAS ÚTEIS até o Encerramento formal
    (M6, inclui 1 ciclo de acompanhamento pós-go-live), sendo T0 o
    kick-off do projeto (designação formal do GP + resolução de CB-4
    e CB-5). Fonte: cronograma detalhado (`cronograma.md`, Carlos
    Cronograma, Step 17), que aplica a mesma premissa de capacidade
    (~30h úteis/semana) usada anteriormente neste TAP, mas agora
    incluindo (a) buffer de gestão de 15% e (b) o ciclo de
    acompanhamento pós-go-live de 1 mês exigido pelo próprio Critério
    de Sucesso #2 abaixo — ambos ausentes do cálculo simplificado
    anterior ("T + 7 semanas úteis", que cobria apenas o piso do
    sizing sem buffer nem pós-go-live). Este valor substitui a
    estimativa anterior. Detalhe:
      Baseline sem buffer até M4 (Go-live): T0 + ~58 dias úteis (~11,6 sem.)
      + Buffer de gestão (15%):             + ~9 dias úteis (~1,7 sem.)
      = Data-alvo Go-live (M4) com buffer:   T0 + ~67 dias úteis (~13,4 sem.)
      + Acompanhamento pós-go-live (M5) e Encerramento (M6): + ~30 dias corridos
      = Data-alvo Encerramento (M6):         T0 + ~90 dias úteis
    Ainda é uma data-alvo relativa a T0 (não uma data de calendário
    fixa) — a data de calendário real depende da confirmação de T0
    (kick-off), que por sua vez depende da resolução de CB-1/CB-2 e
    da designação do GP. Os "30 dias" citados nas atas (Thamyris,
    Wellington) continuam sendo tratados como o prazo de URGÊNCIA
    sinalizado pelas áreas solicitantes, não como esta data-alvo — o
    próprio sizing (206–334h de esforço) é incompatível com uma
    entrega total em
    30 dias corridos. Este TAP NÃO adota "30 dias" como prazo de
    entrega do projeto; adota T0 + ~13,4 semanas úteis (Go-live) e
    T0 + ~90 dias úteis (Encerramento) como data-alvo, com "urgência
    declarada: 30 dias" mantida como insumo de priorização, não como
    compromisso de prazo.

JUSTIFICATIVA
  O Grupo Águia Branca opera hoje o controle de fluxo de caixa e
  orçamento de forma manual (Excel + extrações do SAP), com forte
  concentração de conhecimento e execução em uma única pessoa
  (Thamyris), baixa rastreabilidade de despesas até o nível de nota
  fiscal, e ausência de visibilidade financeira das compras para
  negociação com fornecedores. O TVM já está implantado e validado
  na VIX (outra empresa do grupo), o que reduz o risco técnico do
  núcleo de escopo (configuração-padrão). A qualificação (Felipe
  Filtro, 55/100 — Aprovado com Condições) classificou a iniciativa
  como PROJETO formal (não melhoria pontual), com esforço estimado de
  206–334h, impacto organizacional alto (8/10) e necessidade de
  governança formal (8/10) dada a atuação em 3 frentes simultâneas.
  O benefício financeiro ainda não foi quantificado por nenhuma das
  fontes (CB-6) — este TAP avança com base no valor qualitativo
  (redução de dependência de pessoa-chave, credibilidade de números
  à diretoria, previsibilidade de caixa), registrando a quantificação
  como pendência a resolver antes da validação final.

ESCOPO
  DENTRO DO ESCOPO:
    Frente Financeiro:
      - Migração do fluxo de caixa (ingressos, egressos, LAIR) de
        Excel para o TVM
      - Segregação de receitas por tipo de negócio (ex.: "Squad",
        cartão por bandeira)
      - Despesas agrupadas por categoria (manutenção, combustível,
        TI) até o LAIR
      - Automação da apresentação à diretoria (substitui consolidação
        semanal manual)
    Frente Suprimentos:
      - Painel de baseline orçado com atualização automática por
        lançamento
      - Projeção de pagamentos parcelados (30/60/90 dias)
      - Alertas automáticos por faixa de consumo do orçado (70%/85%)
      - Visibilidade financeira das compras para negociação com
        fornecedores
    Frente Riscos/Desempenho Organizacional:
      - Ampliação do horizonte de previsão de caixa de mensal para
        90 dias
      - Rastreabilidade de custos (nível a confirmar tecnicamente —
        ver Premissas)

  FORA DO ESCOPO (nesta fase):
    - Projeções analíticas por linha (receita/despesa) para orçado
      vs. realizado — condicionado à confirmação técnica do TVM
      (CB-5); se confirmado viável, tratar como possível ampliação
      de escopo formal, não incorporação automática
    - Dashboards gráficos e integração com BI — tratado como "plus"
      nas atas, capacidade técnica não confirmada; permanece fora do
      escopo até avaliação técnica e decisão formal de priorização
    - Integração com o sistema Atenas (2 empresas fora do SAP) — a
      ser avaliada tecnicamente antes de qualquer compromisso de
      entrega
    - Definição de níveis de permissão/acesso para ampliação a outros
      gestores além das 3 áreas já mapeadas
    - Qualquer substituição ou alteração da estrutura de lançamento
      no SAP (o projeto atua sobre o TVM; mudanças estruturais no
      SAP, se necessárias para rastreabilidade a nota fiscal, exigem
      novo estudo de viabilidade e escopo à parte)

CRITÉRIOS DE SUCESSO
  1. As 3 frentes (Financeiro, Suprimentos, Riscos/Desempenho)
     operando em produção no TVM, com Excel deixando de ser a fonte
     primária de apresentação de números à diretoria
  2. Horizonte de previsão de caixa ampliado de mensal para 90 dias,
     validado em uso real por pelo menos 1 ciclo mensal completo
  3. Alertas automáticos de consumo orçamentário (70%/85%) ativos e
     testados para Suprimentos em pelo menos 1 ciclo orçamentário
  4. Redução mensurável da dependência de uma única pessoa (Thamyris)
     na consolidação manual — meta a quantificar com a área (CB-6
     pendente: nenhuma fonte informou volume de horas/mês hoje gasto)
  5. Adoção pelas 3 áreas impactadas: uso ativo do TVM como ferramenta
     primária em, no mínimo, 90 dias após o respectivo go-live de
     cada frente

PREMISSAS
  1. A confirmação verbal do PMO sobre Paula Barcelos (CEO) como
     sponsor é considerada válida para fins de identidade, mas a
     evidência documental formal (e-mail, ata assinada) ainda está
     PENDENTE (CB-1) e deve ser obtida antes da validação final da
     demanda, conforme Regra GP 2026-05-24
  2. Viabilidade técnica do TVM para os 5 itens de escopo incerto
     (projeções analíticas por linha, dashboards/BI, integração
     Atenas, rastreabilidade a nível de nota fiscal, níveis de
     permissão ampliados) ainda NÃO foi confirmada pela equipe
     técnica TVM (CB-5) — o dimensionamento de esforço e cronograma
     assume, na ausência de confirmação, o cenário mais conservador
     (piso da faixa de 206h) apenas para os itens já claros
  3. O TVM comporta o núcleo do escopo (itens de configuração-padrão)
     com base no precedente já validado na VIX, reduzindo o risco
     técnico dessa parte específica
  4. Pressupõe-se que a sessão de continuação com Alessandra (frente
     Financeiro, CB-4) ocorrerá em curto prazo e antes do início
     formal do desenvolvimento; requisitos adicionais dessa sessão
     podem alterar escopo e esforço
  5. Equipe técnica TVM tem disponibilidade para o projeto — não
     confirmada por nenhuma fonte até o momento

RESTRIÇÕES
  1. Orçamento sinalizado como aprovado pela CEO está na faixa de
     R$ 30.000–32.000, mas a reconciliação com o esforço estimado
     (206–334h, custo real projetado de R$ 43.080–69.720) está
     PENDENTE (CB-3) — este TAP não assume que o valor sinalizado
     cobre o escopo total do projeto
  2. Aprovação formal e documentada de Diretoria (área Financeiro) e
     do Gerente de TI da divisão solicitante é exigida pela Regra GP
     2026-05-24 e ainda não foi obtida (CB-2) — pendente antes da
     validação final da demanda
  3. Prazo declarado de "30 dias" nas atas não corresponde a uma
     data-alvo de calendário confirmada nem é compatível com o
     esforço estimado (206–334h); o prazo real de entrega será
     definido no cronograma detalhado (Step 16, Carlos Cronograma)
  4. Nenhum benefício financeiro foi quantificado até o momento
     (CB-6), o que limita a capacidade de calcular payback/ROI real
     neste TAP
  5. Levantamento da frente Financeiro (Alessandra) está incompleto
     — sessão de continuação ainda não concluída (CB-4)

RISCOS DE ALTO NÍVEL
  1. [ALTO] Dependência crítica de uma única pessoa (Thamyris) para
     conhecimento do processo atual e para validação de requisitos
     da frente Riscos/Desempenho — indisponibilidade dela pode
     atrasar significativamente o levantamento e a homologação
  2. [ALTO] Risco orçamentário: o valor aprovado (R$ 30-32k) pode ser
     insuficiente frente ao custo real estimado (R$ 43-70k); se não
     reconciliado antes do início do desenvolvimento (CB-3), há risco
     de paralisação ou redução forçada de escopo no meio do projeto
  3. [ALTO] Viabilidade técnica não confirmada para 5 dos 14
     componentes de escopo do sizing (projeções analíticas, dashboards
     /BI, integração Atenas, rastreabilidade a NF, permissões
     ampliadas); se o TVM não suportar algum destes, pode ser
     necessário desenvolvimento adicional ou solução alternativa,
     impactando prazo e custo (ver sizing.md, fatores de risco)
  4. [MÉDIO] Ausência de evidência documental formal do sponsor e das
     aprovações de Diretoria/Gerente de TI (CB-1, CB-2) pode bloquear
     a validação final da demanda conforme governança interna (Regra
     GP 2026-05-24), mesmo com a documentação de iniciação já pronta
  5. [MÉDIO] Requisitos da frente Financeiro ainda incompletos (CB-4)
     podem introduzir escopo adicional relevante após o início formal
     do projeto
  6. [BAIXO-MÉDIO] Ausência de benefício financeiro quantificado
     (CB-6) dificulta priorização e defesa orçamentária do projeto
     frente a outras iniciativas do portfólio

PARTES INTERESSADAS PRINCIPAIS
  - Paula Barcelos (Sponsor, CEO) — aprovação ainda sujeita a
    formalização documental (CB-1)
  - Alessandra Comério (Solicitante formal, Financeiro)
  - Cássio (Líder técnico da demanda)
  - Wellington Gonçalves (Gestor de Suprimentos)
  - Thamyris (Gestão de Riscos e Desempenho Organizacional —
    dependência crítica de processo atual)
  - Equipe técnica TVM (execução técnica, disponibilidade não
    confirmada)
  - Marcelo Silveira (Coordenador PMO e Sustentação ERP — ponto de
    governança e acompanhamento das CBs)
  - Diretoria/Alta Direção (consumidora das informações de fluxo de
    caixa e orçamento; aprovação formal ainda pendente — CB-2)
  - Gerente de TI da divisão solicitante (aprovação formal pendente
    — CB-2)

ORÇAMENTO RESUMIDO
  Faixa sinalizada como aprovada pela CEO: R$ 30.000 – R$ 32.000
  ⚠️ RECONCILIAÇÃO PENDENTE (CB-3): estimativa de custo real do
  projeto, com base no sizing (206–334h) e taxa de referência de
  desenvolvimento/configuração TVM (~R$150/h, não confirmada com
  fornecedor/equipe técnica):
    Desenvolvimento/Implantação:        R$ 30.900 – R$ 50.100
    Treinamento e change management:    R$  5.000 – R$  8.000
    Contingência (20% s/ dev+treino):   R$  7.180 – R$ 11.620
    Infraestrutura (12 meses):          Não informado (reaproveita
                                         instância já usada pela VIX)
    Licenças (usuários adicionais):     Não informado
    ─────────────────────────────────────────────────────────
    TOTAL ESTIMADO (excl. infra/licenças): R$ 43.080 – R$ 69.720
  Este TAP registra as DUAS faixas explicitamente — a aprovada
  (R$30-32k) e a estimada pelo sizing (R$43-70k) — e trata a
  reconciliação entre elas como condição bloqueante (CB-3) a
  resolver antes da validação final da demanda e, idealmente, antes
  do início do desenvolvimento.

CRONOGRAMA SUMARIZADO
  Status: A DETALHAR no Step 16 (Carlos Cronograma), com base na WBS
  e nas 4 fases já dimensionadas no sizing:
    Fase 1 — Levantamento de requisitos detalhado:     40 – 56h
    Fase 2 — Desenvolvimento/Configuração:             110 – 190h
    Fase 3 — Testes e homologação (UAT 3 frentes):     32 – 48h
    Fase 4 — Go-live e suporte inicial (3 frentes):     24 – 40h
    TOTAL:                                              206 – 334h
  Data-alvo PROVISÓRIA de entrega: T + 7 SEMANAS ÚTEIS, onde T =
  designação formal do GP + resolução de CB-4/CB-5 (cálculo: piso
  do sizing de 206h ÷ ~30h úteis/semana de dedicação parcial da
  equipe ≈ 7 semanas úteis). Não é uma data de calendário fixa —
  é um marcador temporal mensurável que será confirmado (e ajustado
  conforme necessário) no cronograma detalhado. Data de início real:
  A CONFIRMAR — depende da resolução de CB-4 (sessão com Alessandra)
  e CB-5 (viabilidade técnica dos 5 itens incertos), que afetam
  diretamente o dimensionamento real do cronograma. Os "30 dias"
  citados nas atas são tratados como sinalização de urgência do
  solicitante, não como esta data-alvo nem como prazo de entrega do
  projeto.

APROVAÇÃO
  Sponsor: _____________________ Data: _______
           (Paula Barcelos — PENDENTE evidência documental, CB-1)
  PMO:     _____________________ Data: _______
           (Marcelo Silveira)
  Diretoria Financeiro: _________ Data: _______  (PENDENTE, CB-2)
  Gerente de TI:         _________ Data: _______  (PENDENTE, CB-2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

# DOCUMENTO 2 — PM CANVAS

```
PM CANVAS — PROJ-2026-008
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Implantação/Expansão do TVM para Fluxo de Caixa, Controle
Orçamentário e Rastreabilidade de Riscos (Grupo Águia Branca)
Data: 2026-07-07 | Versão: 1.0 | Status: RASCUNHO (CBs em aberto)

┌─────────────────────────────────────────────────────────────┐
│ 1. JUSTIFICATIVA DO PROJETO                                  │
├─────────────────────────────────────────────────────────────┤
│ Processo atual de fluxo de caixa e orçamento é manual        │
│ (Excel + extrações SAP), concentrado em poucas pessoas       │
│ (dependência crítica de Thamyris), com baixa rastreabilidade │
│ e ausência de visibilidade financeira integrada. O TVM já    │
│ opera com sucesso na VIX (outra empresa do grupo), reduzindo │
│ o risco técnico do núcleo de escopo. Benefício financeiro    │
│ ainda NÃO quantificado (CB-6 pendente) — justificativa hoje  │
│ é predominantemente qualitativa (governança de caixa,        │
│ redução de dependência de pessoa-chave, credibilidade de     │
│ números à diretoria).                                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 2. OBJETIVOS SMART                                           │
├─────────────────────────────────────────────────────────────┤
│ Substituir o controle manual (Excel/SAP) por operação        │
│ estruturada no TVM nas 3 frentes — Financeiro (fluxo de      │
│ caixa segregado até o LAIR), Suprimentos (baseline           │
│ orçamentário com alertas 70%/85%) e Riscos/Desempenho        │
│ (previsão de caixa a 90 dias) — com as 3 frentes em produção │
│ e Excel deixando de ser fonte primária para a diretoria.     │
│ Prazo (data-alvo PROVISÓRIA): T + 7 semanas úteis, sendo T a │
│ designação do GP e a resolução de CB-4/CB-5 (piso do sizing  │
│ de 206h ÷ ~30h úteis/semana ≈ 7 semanas). Sujeito a           │
│ confirmação no cronograma detalhado (Carlos Cronograma, Step │
│ 16) — "30 dias" das atas é urgência declarada, não esta       │
│ data-alvo nem prazo de entrega confirmado.                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 3. BENEFÍCIOS ESPERADOS                                      │
├─────────────────────────────────────────────────────────────┤
│ - Redução da dependência crítica de uma única pessoa         │
│   (Thamyris) — horas/mês não quantificadas ainda (CB-6)      │
│ - Maior credibilidade/assertividade dos números à diretoria  │
│ - Visibilidade financeira das compras para negociação com    │
│   fornecedores (Suprimentos)                                 │
│ - Previsibilidade de caixa (90 dias) e alertas de consumo    │
│   orçamentário                                                │
│ INFORMAÇÃO PENDENTE — requer validação com Alessandra/       │
│ Thamyris/PMO: quantificação em R$ ou horas de ao menos 1      │
│ benefício principal (CB-6), necessária para cálculo de ROI e  │
│ payback reais.                                                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 4. PRODUTOS E REQUISITOS                                     │
├─────────────────────────────────────────────────────────────┤
│ - TVM configurado para fluxo de caixa segregado por tipo de  │
│   negócio e categoria de despesa (Financeiro)                │
│ - Painel Suprimentos com baseline orçado automático e        │
│   alertas de consumo (70%/85%)                                │
│ - Previsão de caixa ampliada para 90 dias (Riscos/Desempenho)│
│ - Requisitos completos da frente Financeiro: PENDENTE (CB-4, │
│   sessão de continuação com Alessandra ainda não concluída)  │
│ - Viabilidade técnica de 5 itens (projeções analíticas por    │
│   linha, dashboards/BI, integração Atenas, rastreabilidade a  │
│   NF, permissões ampliadas): INFORMAÇÃO PENDENTE — requer     │
│   validação com equipe técnica TVM (CB-5)                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 5. EQUIPE E RESPONSABILIDADES                                │
├─────────────────────────────────────────────────────────────┤
│ - Sponsor: Paula Barcelos (CEO) — identidade confirmada       │
│   verbalmente; evidência documental PENDENTE (CB-1)          │
│ - Solicitante formal: Alessandra Comério (Financeiro)         │
│ - Líder técnico: Cássio                                       │
│ - Ponto focal Suprimentos: Wellington Gonçalves               │
│ - Ponto focal Riscos/Desempenho: Thamyris                     │
│ - Gerente de Projeto: A designar pelo PMO                     │
│ - PMO/Governança: Marcelo Silveira                            │
│ - Equipe técnica TVM: disponibilidade não confirmada          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 6. PREMISSAS E RESTRIÇÕES                                    │
├─────────────────────────────────────────────────────────────┤
│ PREMISSAS:                                                    │
│ - TVM comporta o núcleo do escopo com base no precedente da  │
│   VIX                                                         │
│ - Sessão de continuação com Alessandra ocorre em curto prazo │
│ RESTRIÇÕES:                                                   │
│ - Orçamento aprovado (R$30-32k) vs. custo estimado real       │
│   (R$43-70k): reconciliação PENDENTE (CB-3)                   │
│ - Aprovação formal de Diretoria Financeiro e Gerente de TI    │
│   (Regra GP 2026-05-24): PENDENTE (CB-2)                      │
│ - Prazo real de entrega: a validar no cronograma (não é       │
│   "30 dias")                                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 7. GRUPOS DE ENTREGA / LINHA DO TEMPO                        │
├─────────────────────────────────────────────────────────────┤
│ Fase 1 — Levantamento de requisitos detalhado:    40–56h      │
│ Fase 2 — Desenvolvimento/Configuração:            110–190h    │
│ Fase 3 — Testes e homologação (UAT 3 frentes):    32–48h      │
│ Fase 4 — Go-live e suporte inicial (3 frentes):    24–40h      │
│ TOTAL: 206–334h | Data-alvo PROVISÓRIA: T + 7 semanas úteis   │
│ (T = designação do GP + resolução CB-4/CB-5). Datas de        │
│ calendário: A CONFIRMAR no cronograma detalhado (Step 16,     │
│ Carlos Cronograma)                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 8. CUSTOS                                                    │
├─────────────────────────────────────────────────────────────┤
│ Faixa aprovada pela CEO: R$ 30.000 – R$ 32.000                │
│ Estimativa real (sizing): R$ 43.080 – R$ 69.720               │
│   (Dev/Implantação R$30,9-50,1k + Treinamento R$5-8k +        │
│    Contingência 20% R$7,18-11,62k; infra e licenças não       │
│    informadas ainda)                                          │
│ RECONCILIAÇÃO PENDENTE (CB-3) — mesma faixa e mesma pendência │
│ registradas no TAP.                                            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 9. RISCOS                                                    │
├─────────────────────────────────────────────────────────────┤
│ [ALTO] Dependência crítica de Thamyris                        │
│ [ALTO] Insuficiência orçamentária frente ao esforço estimado  │
│ [ALTO] Viabilidade técnica não confirmada em 5 de 14 itens    │
│ [MÉDIO] Ausência de evidência documental (sponsor/Diretoria/  │
│         Gerente de TI) pode bloquear validação formal          │
│ [MÉDIO] Escopo adicional da frente Financeiro ainda não       │
│         levantado                                              │
│ [BAIXO-MÉDIO] Benefício financeiro não quantificado dificulta │
│         defesa orçamentária                                    │
└─────────────────────────────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

# DOCUMENTO 3 — PLANO GERAL DO PROJETO (10 Planos Subsidiários PMBOK)

```
PLANO GERAL DO PROJETO — PROJ-2026-008
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data: 2026-07-07 | Versão: 1.0 | Status: RASCUNHO (CBs em aberto)
Consistência: mesmo prazo (data-alvo provisória T + 7 semanas úteis,
a confirmar em data de calendário no cronograma detalhado), mesmo
orçamento (faixa R$30-32k aprovada / R$43-70k estimada, reconciliação
pendente CB-3) e mesmo escopo (3 frentes) do TAP e do PM Canvas.

1. PLANO DE GERENCIAMENTO DO ESCOPO
   Escopo definido pelas 3 frentes (Financeiro, Suprimentos,
   Riscos/Desempenho), com 9 componentes de escopo claro e 5
   componentes de viabilidade incerta (CB-5). Qualquer inclusão dos
   5 itens incertos ou de itens hoje "fora de escopo" (dashboards/BI,
   integração Atenas) exige mudança formal de escopo aprovada pelo
   sponsor/GP, não incorporação automática. Detalhamento em ERF
   (Rafael Requisito, próxima fase).

2. PLANO DE GERENCIAMENTO DO CRONOGRAMA
   Cronograma detalhado a ser construído por Carlos Cronograma
   (Step 16) com base na WBS, a partir das 4 fases do sizing (206–
   334h). Data-alvo PROVISÓRIA de entrega: T + 7 semanas úteis,
   onde T = designação formal do GP + resolução de CB-4 (sessão com
   Alessandra) e CB-5 (viabilidade técnica dos 5 itens incertos).
   Cálculo: piso do sizing (206h) ÷ ~30h úteis/semana de dedicação
   parcial da equipe ≈ 7 semanas úteis — estimativa provisória, não
   data de calendário fixa, sujeita a confirmação/ajuste no
   cronograma detalhado. "30 dias" das atas tratado como urgência
   declarada, não como esta data-alvo. Marcos mínimos: fim do
   levantamento, fim do desenvolvimento, fim dos testes/UAT (3
   frentes), go-live por frente.

3. PLANO DE GERENCIAMENTO DE CUSTOS
   Orçamento sinalizado como aprovado: R$30.000–32.000. Estimativa
   real de custo (sizing): R$43.080–69.720. Reconciliação pendente
   (CB-3) é o item crítico deste plano — nenhum compromisso de custo
   final deve ser assumido até a equipe técnica e o PMO confirmarem
   taxa/hora, infraestrutura e licenças. Controle de custo via CPI
   a partir do início da execução formal.

4. PLANO DE GERENCIAMENTO DA QUALIDADE
   Critérios de aceitação a definir em conjunto com ERF (Rafael
   Requisito). Padrão de qualidade de referência: configuração já
   validada na VIX para itens de precedente técnico. Para os 5 itens
   incertos, qualidade será condicionada à confirmação técnica prévia
   (CB-5) antes de qualquer critério de aceite ser fechado.

5. PLANO DE GERENCIAMENTO DE RECURSOS
   Recursos-chave: Cássio (líder técnico), equipe técnica TVM
   (disponibilidade não confirmada), pontos focais das 3 áreas
   (Alessandra/Financeiro, Wellington/Suprimentos, Thamyris/Riscos).
   Risco de recurso crítico: dependência de uma única pessoa
   (Thamyris) para conhecimento do processo atual — plano deve
   prever redistribuição de conhecimento como entregável do próprio
   projeto, não apenas como risco a mitigar.

6. PLANO DE GERENCIAMENTO DAS COMUNICAÇÕES
   Reporte periódico ao PMO (Marcelo Silveira) e ao sponsor (Paula
   Barcelos, quando formalmente designada) sobre status das CBs em
   aberto e do progresso das 3 frentes. Comunicação dedicada a cada
   área impactada (Financeiro, Suprimentos, Riscos/Desempenho) dado
   que cada uma tem seu próprio ponto focal e cronograma de adoção.

7. PLANO DE GERENCIAMENTO DE RISCOS
   Registro inicial de riscos de alto nível já no TAP (dependência de
   Thamyris, insuficiência orçamentária, viabilidade técnica incerta
   em 5 itens, ausência de evidência documental de governança, escopo
   adicional da frente Financeiro, benefício não quantificado).
   Detalhamento completo (probabilidade, impacto, resposta,
   responsável, prazo) a cargo de Pedro Perigo em fase posterior do
   pipeline.

8. PLANO DE GERENCIAMENTO DE AQUISIÇÕES
   Nenhuma aquisição externa identificada até o momento — o TVM já é
   ferramenta do grupo (uso corrente na VIX). Possível necessidade de
   aquisição de licenças adicionais para usuários de Financeiro/
   Suprimentos/Riscos: INFORMAÇÃO PENDENTE — requer validação com
   equipe técnica TVM/fornecedor (mesma pendência do orçamento,
   CB-3).

9. PLANO DE GERENCIAMENTO DE STAKEHOLDERS
   Mapeamento inicial: sponsor (Paula Barcelos, CEO — pendente
   formalização CB-1), solicitante formal (Alessandra Comério),
   líder técnico (Cássio), pontos focais de Suprimentos (Wellington
   Gonçalves) e Riscos/Desempenho (Thamyris), Diretoria/Alta Direção
   (consumidora das informações, aprovação formal pendente CB-2),
   Gerente de TI da divisão (aprovação formal pendente CB-2), PMO
   (Marcelo Silveira, governança). Estratégia de engajamento prioriza
   fechar CB-1/CB-2 (evidência documental) e CB-4 (sessão com
   Alessandra) nas próximas semanas.

10. PLANO DE GERENCIAMENTO DE MUDANÇAS (INTEGRAÇÃO)
    Qualquer alteração de escopo, prazo ou custo em relação ao que
    está registrado neste Plano Geral, no TAP e no PM Canvas deve
    passar por controle formal de mudança, com aprovação do GP
    designado e, conforme o impacto, do sponsor. Este plano trata
    explicitamente as 6 CBs abertas (CB-1 a CB-6) como itens sob
    monitoramento ativo de integração — a resolução de cada uma pode
    gerar necessidade de replanejamento (ex.: CB-3 reconciliação de
    orçamento pode forçar redução de escopo; CB-5 pode remover ou
    confirmar os 5 itens incertos).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Verificação Final de Consistência (Diana Documento)

| Dimensão | TAP | PM Canvas | Plano Geral | Consistente? |
|----------|-----|-----------|--------------|--------------|
| Prazo | Data-alvo PROVISÓRIA = T + 7 semanas úteis (T = designação do GP + resolução CB-4/CB-5; cálculo: 206h ÷ ~30h úteis/semana ≈ 7 semanas), a confirmar em data de calendário no cronograma detalhado (Step 16); "30 dias" das atas = urgência declarada, não esta data-alvo | Idêntico | Idêntico | ✅ |
| Orçamento | R$30-32k aprovado / R$43-70k estimado (reconciliação pendente, CB-3) | Idêntico | Idêntico | ✅ |
| Escopo | 3 frentes unificadas (Financeiro, Suprimentos, Riscos/Desempenho), 9 itens claros dentro + 5 itens incertos fora até confirmação técnica | Idêntico | Idêntico | ✅ |
| Sponsor | Paula Barcelos (CEO) — identidade confirmada verbalmente, evidência documental pendente (CB-1) | Idêntico | Idêntico | ✅ |
| CBs pendentes (6) | Todas as 6 registradas explicitamente (Premissas/Restrições/Riscos) | Todas as 6 registradas (blocos 1, 3, 4, 6, 8, 9) | Todas as 6 registradas (planos 3, 5, 7, 8, 9, 10) | ✅ |

Nenhum bloco do PM Canvas ficou vazio; todos os 10 planos subsidiários foram endereçados; objetivo SMART tem métrica (3 frentes em produção, Excel deixando de ser fonte primária) e agora também o componente Temporal (T + 7 semanas úteis como data-alvo provisória, mensurável, sem fingir uma data de calendário que ainda não existe). Documentos aprovados para prosseguir ao Step seguinte (Rafael Requisito — ERF completa), mantendo as 6 CBs como pendências ativas de acompanhamento pelo PMO.
