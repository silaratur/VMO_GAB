# Planejamento de Prazo — DEM-2026-007
Projeto: Implantação DDA SAP — VAB Matriz
Elaborado por: Carlos Cronograma (VMO Autônomo)
Data: 2026-05-20
Versão: 1.0

> **Premissa de prazo:** Este cronograma assume kick-off em 08/06/2026 (após resolução de
> CB-3 e CB-Sponsor). Se o kick-off atrasar, todas as datas deslizam proporcionalmente.
> A data de go-live de 30/09/2026 é a meta orientativa — o cronograma base (sem buffer) entrega
> go-live em 31/08/2026, reservando setembro como buffer de contingência.

---

## WBS — Estrutura Analítica do Projeto

```
DEM-2026-007 — Implantação DDA SAP VAB Matriz
│
├── 1. INICIAÇÃO E PRÉ-REQUISITOS
│   ├── 1.1 Resolução de condições bloqueantes de kick-off
│   │   ├── 1.1.1 Resolver CB-3 (formalização de custos + autorização Holding)
│   │   ├── 1.1.2 Identificar sponsor Diretor+ (CB-Sponsor)
│   │   └── 1.1.3 Gate de Kick-off (Gabriel Governança)
│   └── 1.2 Mobilização
│       ├── 1.2.1 Designação do recurso técnico DTI FI
│       └── 1.2.2 Kickoff meeting (GP + Noemia + equipe DTI)
│
├── 2. LEVANTAMENTO TÉCNICO (CB-2)
│   ├── 2.1 Análise da implementação DDA da Div. Logística
│   │   ├── 2.1.1 Reunião técnica com equipe Logística
│   │   ├── 2.1.2 Revisão dos parâmetros FEBAN/SAP Logística
│   │   └── 2.1.3 Revisão do layout CNAB 240 Santander em uso
│   ├── 2.2 Mapeamento dos ajustes para o CP VAB
│   │   ├── 2.2.1 Reunião com Noemia: especificidades do CP VAB
│   │   ├── 2.2.2 Análise das diferenças de processo e configuração
│   │   └── 2.2.3 Definição final da lista de ajustes
│   └── 2.3 Entregável E-01: Documento de análise técnica aprovado
│
├── 3. CONFIGURAÇÃO E IMPLEMENTAÇÃO
│   ├── 3.1 Habilitação DDA no Santander (em paralelo)
│   │   ├── 3.1.1 Contato com Santander para processo de habilitação
│   │   ├── 3.1.2 Documentação e envio dos dados da conta VAB
│   │   └── 3.1.3 Confirmação de habilitação ativa (E-02)
│   ├── 3.2 Configuração SAP FI — Base DDA
│   │   ├── 3.2.1 Configurar FEBAN: parâmetros básicos DDA (replicar Logística)
│   │   ├── 3.2.2 Configurar empresa VAB Matriz no FEBAN
│   │   └── 3.2.3 Configurar conta corrente Santander VAB
│   ├── 3.3 Ajustes específicos CP VAB
│   │   ├── 3.3.1 Implementar ajustes identificados no E-01
│   │   └── 3.3.2 Validação interna dos ajustes (DTI)
│   └── 3.4 Configuração de perfis de acesso SAP
│       └── 3.4.1 Definir e configurar perfis de usuário DDA (CP + DTI FI)
│
├── 4. TESTES
│   ├── 4.1 Testes de homologação SAP x Santander
│   │   ├── 4.1.1 Solicitar arquivo DDA de teste ao Santander
│   │   ├── 4.1.2 Processar arquivo DDA teste no SAP (E-03)
│   │   └── 4.1.3 Validar todos os RFs Must Have em homologação
│   ├── 4.2 Testes de aceitação do usuário (UAT) — E-05 + E-06
│   │   ├── 4.2.1 Preparar roteiro de UAT
│   │   ├── 4.2.2 Executar UAT com equipe CP VAB
│   │   └── 4.2.3 Aprovação e assinatura Noemia (E-06)
│   └── 4.3 Correções pós-UAT (se necessário)
│
├── 5. GO-LIVE E IMPLANTAÇÃO
│   ├── 5.1 Treinamento equipe CP (E-08)
│   │   ├── 5.1.1 Preparar material de treinamento
│   │   └── 5.1.2 Executar treinamento
│   ├── 5.2 Go-live supervisionado (E-07)
│   │   ├── 5.2.1 Migrar configuração para produção
│   │   ├── 5.2.2 Acompanhamento do 1º dia em produção
│   │   └── 5.2.3 Monitoramento pós-go-live (30 dias)
│   └── 5.3 Documentação técnica (E-09)
│       └── 5.3.1 Produzir documento técnico final (diferenças vs. Logística)
│
└── 6. ENCERRAMENTO
    ├── 6.1 Pesquisa de satisfação equipe CP (CS-3)
    ├── 6.2 Relatório de encerramento
    └── 6.3 Aceite formal e arquivamento
```

---

## Cronograma Detalhado

**Data de referência:** Kick-off = 08/06/2026

| ID | Atividade | Início | Fim | Duração | Dependência | Responsável | Marco |
|----|-----------|--------|-----|---------|------------|-------------|-------|
| **FASE 0: PRÉ-KICK-OFF** | | **20/05** | **06/06** | **12d** | | | |
| 0.1 | Resolver CB-3 (custos + Holding) | 20/05 | 27/05 | 5d | — | Noemia/Gladston/Walace | |
| 0.2 | Identificar sponsor Diretor+ (CB-Sponsor) | 20/05 | 30/05 | 8d | — | Gladston | |
| 0.3 | Gate de Kick-off (Gabriel) | 02/06 | 06/06 | 3d | 0.1, 0.2 | VMO/Gabriel | **M-0** |
| **FASE 1: MOBILIZAÇÃO** | | **09/06** | **13/06** | **3d** | | | |
| 1.1 | Designar recurso técnico DTI FI | 09/06 | 09/06 | 1d | M-0 | Gladston | |
| 1.2 | Kickoff meeting | 10/06 | 13/06 | 2d | 1.1 | GP | |
| **FASE 2: LEVANTAMENTO TÉCNICO** | | **16/06** | **27/06** | **10d** | | | |
| 2.1 | Reunião com equipe Logística + revisão params | 16/06 | 20/06 | 5d | 1.2 | Recurso DTI | |
| 2.2 | Reunião com Noemia + análise diferenças CP VAB | 23/06 | 25/06 | 3d | 2.1 | Recurso DTI + Noemia | |
| 2.3 | Documento E-01 produzido e aprovado | 26/06 | 27/06 | 2d | 2.2 | Recurso DTI/GP | **M-1** |
| **FASE 3: CONFIG + HABILITAÇÃO (paralelas)** | | **30/06** | **25/07** | **20d** | | | |
| 3.1 | Contato Santander + processo habilitação DDA | 30/06 | 11/07 | 10d | M-1 | Noemia/Tesouraria | |
| 3.2 | Configuração SAP FEBAN base (replicar Logística) | 30/06 | 11/07 | 10d | M-1 | Recurso DTI | |
| 3.3 | Confirmação habilitação Santander (E-02) | 14/07 | 18/07 | 5d | 3.1 | Santander/Noemia | **M-2** |
| 3.4 | Implementar ajustes específicos CP VAB (E-01) | 14/07 | 25/07 | 10d | 3.2, M-1 | Recurso DTI | |
| 3.5 | Configurar perfis de acesso SAP | 23/07 | 25/07 | 3d | 3.2 | Recurso DTI | |
| **FASE 4: TESTES** | | **28/07** | **15/08** | **15d** | | | |
| 4.1 | Solicitar arquivo DDA teste ao Santander | 28/07 | 29/07 | 2d | 3.3, 3.4 | Recurso DTI | |
| 4.2 | Testes homologação SAP x Santander (E-03) | 30/07 | 08/08 | 8d | 4.1 | Recurso DTI | **M-3** |
| 4.3 | UAT com equipe CP VAB (E-05) | 11/08 | 14/08 | 4d | 4.2 | CP VAB/GP | |
| 4.4 | Aceite UAT assinado por Noemia (E-06) | 15/08 | 15/08 | 1d | 4.3 | Noemia | **M-4** |
| **FASE 5: GO-LIVE** | | **18/08** | **29/08** | **10d** | | | |
| 5.1 | Preparar e executar treinamento CP (E-08) | 18/08 | 21/08 | 4d | M-4 | Recurso DTI | |
| 5.2 | Deploy em produção + dia 1 supervisionado | 25/08 | 25/08 | 1d | 5.1 | Recurso DTI/GP | **M-5** |
| 5.3 | Monitoramento pós-go-live (30 dias) | 26/08 | 26/09 | 23d úteis | 5.2 | GP/Recurso DTI | |
| 5.4 | Documentação técnica final (E-09) | 18/08 | 29/08 | 10d | M-4 | Recurso DTI | |
| **FASE 6: ENCERRAMENTO** | | **29/09** | **30/09** | **2d** | | | |
| 6.1 | Pesquisa de satisfação equipe CP | 29/09 | 29/09 | 1d | 5.3 | GP | |
| 6.2 | Relatório + aceite formal | 30/09 | 30/09 | 1d | 6.1 | GP/VMO | **M-6** |

---

## Marcos Principais

| Marco | Data | Critério de Conclusão |
|-------|------|-----------------------|
| M-0 | 06/06/2026 | Gate de Kick-off aprovado (CB-3 + CB-Sponsor resolvidas) |
| M-1 | 27/06/2026 | E-01: Levantamento técnico aprovado (CB-2 resolvida) |
| M-2 | 18/07/2026 | E-02: Habilitação Santander DDA confirmada |
| M-3 | 08/08/2026 | E-03+E-04: Config SAP + testes homologação aprovados |
| M-4 | 15/08/2026 | E-05+E-06: UAT assinado pela Noemia |
| M-5 | 25/08/2026 | Go-live em produção |
| M-6 | 30/09/2026 | Encerramento formal + aceite |

---

## Caminho Crítico

```
Kick-off (M-0) → Levantamento técnico (M-1) → Habilitação Santander (M-2)
             ↕
     Config SAP + ajustes → Testes homologação (M-3) → UAT (M-4) → Go-live (M-5) → Encerramento (M-6)
```

**Atividades críticas (zero folga):**
- 0.1 Resolver CB-3 → 0.3 Gate kick-off → 1.2 Kickoff meeting → 2.1-2.3 Levantamento →
  3.1 Habilitação Santander → 3.3-3.4 Config+Ajustes → 4.2 Testes → 4.3-4.4 UAT →
  5.2 Go-live → 5.3 Monitoramento → 6.2 Encerramento

**Risco crítico de caminho:** A habilitação do Santander (3.1 a 3.3) é o fator externo mais
incerto — se demorar mais de 15 dias úteis, atrasa o caminho crítico diretamente.

---

## Esforço Estimado por Fase

| Fase | Esforço DTI (h) | Esforço Negócio (h) | Total |
|------|---------------|---------------------|-------|
| 0. Pré-kick-off (CBs) | 2h | 16h | 18h |
| 1. Mobilização | 4h | 4h | 8h |
| 2. Levantamento técnico (CB-2) | 32h | 8h | 40h |
| 3. Config + Habilitação | 40h | 8h | 48h |
| 4. Testes | 24h | 16h | 40h |
| 5. Go-live + treinamento + docs | 24h | 8h | 32h |
| 6. Encerramento | 4h | 2h | 6h |
| **Total** | **130h** | **62h** | **192h** |

> **Nota CB-2:** Se os ajustes forem somente parametrização (P-5 confirmada), esforço DTI
> estimado é 100–130h (Melhoria Evolutiva). Se envolverem desenvolvimento ABAP, esforço pode
> atingir 160–200h — neste caso, projeto deve ser reclassificado antes do kick-off.
> Esta estimativa assume P-5 verdadeira.

---

## Buffer de Contingência

| Item | Valor |
|------|-------|
| Prazo base (kick-off ao go-live) | 11 semanas (08/06 a 25/08/2026) |
| Buffer de contingência (15%) | 1,65 semanas ≈ 8 dias úteis |
| Buffer aplicado | Setembro 2026 (26/08 a 30/09/2026 = 26 dias úteis) |
| **Prazo com buffer** | **30/09/2026 (go-live meta)** |

O buffer de contingência de setembro absorve: (1) atraso na habilitação Santander; (2)
retrabalho pós-UAT; (3) ajustes identificados como mais complexos que parametrização (CB-2).
Não absorve: reclassificação como PROJETO (exige novo ciclo de planejamento).
