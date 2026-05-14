# Output Examples — VMO Autônomo

---

## Exemplo 1: Qualificação de Demanda Aprovada

```
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data: 2026-04-10
Analista: VMO Autônomo — Felipe Filtro
ID da Demanda: DEM-2026-047

SOLICITANTE
  Nome: Ana Carolina Ferreira
  Cargo: Diretora de Operações
  Área: Supply Chain

DEMANDA
  "Implementar sistema de rastreamento em tempo real para 
  monitoramento de entregas de fornecedores críticos,
  integrando com o ERP SAP atual."

ANÁLISE DE QUALIFICAÇÃO

1. Alinhamento Estratégico          ALTO ✓
   OKR Q1/2026: "Reduzir falhas de fornecimento em 30%"
   Este projeto endereça diretamente este objetivo.
   Confiança: ALTA (documentação estratégica revisada)

2. Viabilidade Técnica              MÉDIO ✓
   SAP possui API de integração disponível.
   Solução de rastreamento (GPS + IoT) tecnicamente madura.
   Risco: integração legada pode requerer desenvolvimento adicional.
   Confiança: MÉDIA (requer POC técnica)

3. Retorno sobre Investimento       ALTO ✓
   Custo estimado: R$ 280.000 (desenvolvimento + implantação)
   Benefício estimado: R$ 520.000/ano (redução de perdas + multas)
   Payback estimado: 6,5 meses
   Confiança: MÉDIA (baseado em benchmarks do setor)

4. Urgência                         ALTO ✓
   3 incidentes de ruptura de fornecimento no último trimestre.
   Penalidade contratual de R$ 45.000 por incidente acumulada.
   Pressão do board para resolução até Q3/2026.

5. Maturidade da Demanda            MÉDIO ✓
   Solicitante tem visão clara do problema e benefício esperado.
   Solução técnica específica requer validação com TI.
   Gap: responsável técnico não identificado.

6. Disponibilidade de Recursos      MÉDIO ~
   Orçamento disponível: confirmado pela diretora.
   Equipe técnica: TI informa 60% de disponibilidade em Q2.
   Atenção: Projeto de atualização do SAP em paralelo pode gerar conflito.

PONTUAÇÃO CONSOLIDADA

  Alinhamento Estratégico:   5/5
  Viabilidade Técnica:       3/5
  Retorno sobre Investimento: 4/5
  Urgência:                  5/5
  Maturidade da Demanda:     3/5
  Disponibilidade de Recursos: 3/5
  ─────────────────────────
  TOTAL:                     23/30 (76,7%)

DECISÃO: APROVADO COMO PROJETO ✓

JUSTIFICATIVA:
  A demanda apresenta forte alinhamento estratégico e ROI positivo
  com payback inferior a 1 ano. Os pontos de atenção (disponibilidade 
  de TI e conflito com projeto SAP) devem ser gerenciados como riscos
  durante a iniciação.

PRÓXIMOS PASSOS:
  1. Designar sponsor formal: proposta = Diretor de TI em co-patrocínio
  2. Agendar reunião técnica com TI para POC de integração SAP
  3. Mapear conflito de recursos com projeto SAP (consultar PMO)
  4. Iniciar elaboração do TAP com prazo limite: 2026-04-20

CONDIÇÕES DE PROGRESSO:
  - Sponsor formal designado (bloqueante)
  - Orçamento preliminar formalizado em CAPEX/OPEX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Exemplo 2: Termo de Abertura do Projeto (TAP)

```
TERMO DE ABERTURA DO PROJETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Versão: 1.0
Data: 2026-04-15
Status: RASCUNHO — Aguardando Aprovação do Sponsor

IDENTIFICAÇÃO DO PROJETO
  Nome: Sistema de Rastreamento de Fornecedores (SRF)
  ID:   PROJ-2026-012
  Área Solicitante: Supply Chain
  Área Executora: TI — Sistemas Corporativos

AUTORIZAÇÃO
  Sponsor: Carlos Eduardo Mendes — Diretor de TI
  Co-Sponsor: Ana Carolina Ferreira — Diretora de Operações
  Gerente de Projeto: [A designar pelo PMO]
  Autoridade do GP: Aprovar gastos até R$ 15.000 / Contratar recursos internos

OBJETIVO DO PROJETO
  Implementar sistema de rastreamento em tempo real para monitoramento
  de entregas de fornecedores críticos (Tier 1), integrado ao SAP ERP,
  reduzindo incidentes de ruptura de fornecimento em 40% até 31/12/2026.

JUSTIFICATIVA
  No Q1/2026, a empresa registrou 3 incidentes de ruptura de fornecimento
  com custo total de R$ 135.000 (penalidades + perdas de produção).
  A ausência de visibilidade em tempo real impede ação preventiva.
  Este projeto suporta o OKR organizacional: "Reduzir falhas de
  fornecimento em 30% no ano de 2026".

ESCOPO
  DENTRO DO ESCOPO:
    - Módulo de rastreamento GPS para 12 fornecedores Tier 1
    - Integração com SAP MM (módulo de materiais)
    - Dashboard de monitoramento em tempo real
    - Alertas automáticos por e-mail/Teams para atrasos > 2h
    - Relatórios gerenciais mensais

  FORA DO ESCOPO:
    - Fornecedores Tier 2 e Tier 3 (fase futura)
    - Substituição ou upgrade do SAP
    - Integração com sistemas de fornecedores
    - Monitoramento de qualidade dos materiais entregues

CRITÉRIOS DE SUCESSO
  1. Cobertura de 100% dos fornecedores Tier 1 no sistema até 30/09/2026
  2. Redução de incidentes de ruptura de ≥ 40% no semestre pós-implantação
  3. Adoção pelo time de Supply Chain: ≥ 90% de uso ativo em 60 dias
  4. Satisfação do cliente interno (Supply Chain): ≥ 8/10 na pesquisa pós-go-live
  5. Sistema disponível 99,5% do tempo (exceto janelas de manutenção)

PREMISSAS
  - SAP atual possui API REST disponível para integração (confirmar com TI)
  - Fornecedores Tier 1 possuem smartphone ou dispositivo IoT disponível
  - Equipe de TI disponível em 60% no Q2/2026
  - Orçamento aprovado no CAPEX de 2026

RESTRIÇÕES
  - Prazo máximo: 31/12/2026 (ano fiscal)
  - Orçamento máximo: R$ 350.000 (incluindo contingência)
  - Solução deve ser cloud-native (política de infraestrutura corporativa)
  - Dados devem permanecer no Brasil (LGPD + política de dados)

RISCOS DE ALTO NÍVEL
  1. [ALTO] Conflito de recursos com projeto de atualização SAP (Q2/2026)
  2. [MÉDIO] Resistência de fornecedores à adoção do sistema de rastreamento
  3. [MÉDIO] Complexidade de integração SAP maior que estimada (API legada)
  4. [BAIXO] Mudança de escopo após aprovação do TAP

PARTES INTERESSADAS PRINCIPAIS
  - Carlos Eduardo Mendes (Sponsor, Diretor TI)
  - Ana Carolina Ferreira (Co-Sponsor, Diretora Supply Chain)
  - Time Supply Chain (usuários finais, 8 pessoas)
  - Time TI — Sistemas (equipe executora, 3-4 pessoas)
  - 12 fornecedores Tier 1 (afetados)
  - Diretoria Financeira (aprovação orçamentária)

ORÇAMENTO RESUMIDO
  Desenvolvimento e configuração:  R$ 180.000
  Infraestrutura cloud (12 meses): R$  45.000
  Licenças de software (1º ano):   R$  35.000
  Treinamento e change management: R$  20.000
  Reserva de contingência (20%):   R$  56.000
  ─────────────────────────────────────────
  TOTAL APROVADO:                  R$ 336.000

CRONOGRAMA SUMARIZADO
  Início:             2026-05-01
  Fase 1 (Requisitos): 2026-05-01 a 2026-05-31
  Fase 2 (Desenvolvimento): 2026-06-01 a 2026-08-31
  Fase 3 (Testes): 2026-09-01 a 2026-09-30
  Go-Live: 2026-10-01
  Pós-implantação: 2026-10-01 a 2026-12-31
  Encerramento: 2026-12-31

APROVAÇÃO
  Sponsor: _____________________ Data: _______
  Co-Sponsor: __________________ Data: _______
  PMO: _________________________ Data: _______
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Exemplo 3: Status Report com Semáforo

```
STATUS REPORT — PROJETO SRF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Período: 2026-07-01 a 2026-07-14
Data do Report: 2026-07-15
Gerente de Projeto: Marcelo Silveira

STATUS GERAL: 🟡 ATENÇÃO

  Cronograma: 🟡 ATENÇÃO  (SPI: 0,88)
  Custo:      🟢 NORMAL   (CPI: 1,02)
  Escopo:     🟢 NORMAL   (sem mudanças)
  Riscos:     🟡 ATENÇÃO  (1 risco alto ativo)
  Qualidade:  🟢 NORMAL

PROGRESSO
  Planejado: 55% | Realizado: 48% | Desvio: -7%

  Entregas Concluídas:
    ✓ Mapeamento de requisitos (100%)
    ✓ Arquitetura da solução aprovada (100%)
    ✓ Módulo GPS — desenvolvimento (100%)

  Em Andamento:
    ⏳ Integração SAP MM (65% — atrasada)
    ⏳ Dashboard de monitoramento (40%)

  Pendente:
    ○ Testes de integração (início previsto: 2026-07-28)
    ○ Treinamento de fornecedores

ANÁLISE DE DESVIO
  O atraso de 7% está concentrado na integração SAP MM.
  A API SAP possui limitações não documentadas que requerem
  desenvolvimento de middleware adicional (3 dias extras estimados).
  Este é o risco ID-003 que estava classificado como MÉDIO e foi
  elevado para ALTO nesta semana.

ISSUES ABERTAS

  | ID    | Issue | Impacto | Responsável | Prazo |
  |-------|-------|---------|-------------|-------|
  | I-007 | API SAP requer middleware adicional | Prazo +3d | Eng. Roberto Lima | 2026-07-20 |
  | I-008 | Fornecedor XYZ não respondeu ao onboarding | Cobertura | Ana Ferreira | 2026-07-17 |

RISCOS EM MONITORAMENTO

  | ID    | Risco | Prob | Impacto | Status |
  |-------|-------|------|---------|--------|
  | R-003 | Complexidade API SAP | ALTA | ALTO | ⚠️ MATERIALIZADO |
  | R-005 | Adoção fornecedores | MÉDIA | MÉDIO | 🔍 Monitorando |

PRÓXIMOS PASSOS (próximas 2 semanas)
  1. Concluir middleware SAP — Roberto Lima — 2026-07-20
  2. Iniciar testes de integração — Time TI — 2026-07-21
  3. Onboarding fornecedor XYZ — Ana Ferreira — 2026-07-17
  4. Revisão de cronograma com sponsor — GP — 2026-07-16

SOLICITAÇÃO AO SPONSOR
  Solicitar aprovação para estender prazo de go-live de 01/10 para
  15/10/2026 (+15 dias) para absorver impacto do middleware SAP.
  Custo adicional estimado: R$ 8.000 (dentro da reserva de contingência).

Próximo Report: 2026-07-29
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
