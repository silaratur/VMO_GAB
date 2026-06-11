# Registro de Aprovação — Ajustes nos Monitores ZMMR_GSI02/03/04 (SAP ECC Módulo MM)

Projeto: PROJ-2026-008 | Demanda: DEM-2026-008 (Chamado 6898567 / Work Request 4918651)

## Decisão: APROVADO COM RESSALVAS (Waiver de Governança do GP VMO)

- **Data:** 2026-06-11
- **Aprovador:** GP VMO (decisão registrada via Checkpoint Step 16)
- **Pontuação de qualidade (Vera Veredito):** 8,23/10 (≅ 82,3/100) — APROVADO COM CONDIÇÕES
- **Auditoria de Governança (Gabriel Governança):** ❌ BLOQUEADO (1 NC-CRÍTICA + 3 NC-MOD) — **decisão sobreposta por waiver explícito do GP VMO**

## Natureza da Decisão

O GP VMO optou por **"Aprovar com waiver de governança"** — opção (c) recomendada como prerrogativa do GP VMO na Auditoria de Governança (`05-encerramento/auditoria-governanca.md`), em desacordo com a recomendação de Gabriel Governança (que recomendava registrar BLOQUEADO e reauditar em 2026-06-13, opção a).

Esta decisão **não altera nem contesta** as constatações de Vera Veredito ou de Gabriel Governança — ambas permanecem válidas e integralmente registradas nos respectivos relatórios. O waiver formaliza a **ciência e aceitação do risco** pelo GP VMO de iniciar a preparação da execução (mobilização, mas não necessariamente entregas em produção) **antes** da resolução formal de CB-1, CB-2 e da designação do GP do projeto, mantendo essas pendências sob monitoramento ativo via Status Report.

## Ressalvas Registradas (transportadas integralmente da Auditoria de Governança e da Revisão de Qualidade)

| ID | Origem | Descrição | Ação Corretiva | Responsável | Prazo |
|----|--------|-----------|----------------|-------------|-------|
| NC-001 (CRÍTICA) | Gabriel — D1 | Sponsor (Nubia Carla Freitas Santos Souza, Gerente Contábil) abaixo do nível mínimo Diretor+; CB-1 (aprovação formal de Diretoria) sem evidência documental | Diretoria formaliza aprovação do TAP (CB-1), por escrito, ou emite delegação formal de autoridade de sponsor | Tatiane Dias de Moraes / Projetos DTI | 2026-06-13 |
| (CB-2) | Gabriel — D1 | Cargo do aprovador técnico/orçamentário (Raphael Leitão Sbardelotti, "Gerente de TI") não confirmado | Confirmar cargo formal ou identificar o aprovador correto, por escrito | Tatiane Dias de Moraes / Projetos DTI | 2026-06-13 |
| NC-002 (MOD) | Gabriel — D1 / Vera — Cond. #1 | Gerente de Projeto não designado no TAP | SQUAD PM/MM designa o GP e atualiza o TAP para v1.1 | SQUAD PM/MM (Time de Sustentação ERP) | 2026-06-13 |
| NC-003 (MOD) | Gabriel — D2 / Vera — Cond. #3 | Divergência de prazo: TAP compromete 2026-09-30; Cronograma + buffer (15%) projeta 2026-10-10 (~10 dias) | GP VMO + Sponsor decidem entre comprimir cronograma (via CB-5) ou formalizar aditivo de prazo para 2026-10-10; registrar decisão por escrito | GP VMO + Sponsor | 2026-06-24 (M0) |
| NC-004 (MOD) | Gabriel — D2 / Vera — Cond. #4 | CB-Orçamento: teto declarado de R$ 30.000 vs. BAC com contingência de R$ 36.000 (e reserva de riscos calculada de R$ 26.800 vs. R$ 6.000 do TAP) sem reconciliação formal | GP VMO + Sponsor formalizam o teto orçamentário vigente e o tratamento do gap | GP VMO + Sponsor | 2026-06-24 (M0) |
| (CB-3) | qualificacao-aprovada | Destino exato do ajuste em ZMMR_GSI04 e relação com ZMMR_GSI01/item 6 não definidos | Esclarecer com Especialista Funcional (Jerfesson Fernandes Helmer) | SQUAD PM/MM + Tatiane/João Henrique | 2026-06-13 |
| (CB-4) | qualificacao-aprovada | Priorização entre itens do escopo ainda ambígua | Resolver com Sponsor | Tatiane / João Henrique | 2026-06-13 |
| (CB-5) | qualificacao-aprovada | Estimativa de esforço por fase (15 itens) ainda não entregue | Entregar estimativa | SQUAD PM/MM (Jerfesson Fernandes Helmer) | 2026-06-17 |
| (CB-6) | qualificacao-aprovada | Especificação funcional formal e plano de testes dos itens 13/14 ainda não elaborados | Elaborar especificação e plano de testes (pré-requisito da Onda 3, item 13 no caminho crítico) | SQUAD PM/MM + QA | 2026-06-24 |
| NC-005 (MENOR) | Gabriel — D3 | Inconsistência de escala entre `step-12-revisao-qualidade.md` ("≥85/100") e `quality-criteria.md` ("≥7,0/10") — framework VMO, não bloqueante para este projeto | Padronizar escala nos documentos do framework | Mantenedores VMO Autônomo | Sem prazo |

## Próximos Passos

1. **Kickoff da execução agendado para "em duas semanas" a partir desta aprovação → 2026-06-25**, alinhado ao prazo de CB-5 (2026-06-17) e próximo ao marco M0 do cronograma (2026-06-24, "CBs resolvidas"). Entre 2026-06-11 e 2026-06-25, o GP VMO acompanha a resolução de CB-1 a CB-6 via Status Report quinzenal.
2. **Status Report #002** deve reportar explicitamente o status de cada item da tabela de Ressalvas acima — em especial NC-001/CB-1, NC-002 e CB-2/CB-3/CB-4 (prazo 2026-06-13).
3. **Reauditoria de governança (Gabriel)** recomendada para 2026-06-13, focada em D1 (sponsor/GP) — não é necessário reexecutar a Vera Veredito, cujo veredicto de conteúdo permanece válido.
4. **Decisão conjunta NC-003/NC-004** (prazo/orçamento) deve ser registrada por escrito até M0 (2026-06-24), antes do go-live da Onda 1 (2026-07-15).
5. **Distribuir o pacote completo de iniciação** ao SQUAD PM/MM e a Tatiane Dias de Moraes / João Henrique, incluindo a Pesquisa de Satisfação de Iniciação (`04-monitoramento/status-report-2026-06-11.md`).
6. **Ativar monitoramento de KPIs** (CPI, SPI, cobertura por onda, gestão de riscos) conforme `03-planejamento/kpis.md`, com primeira medição alinhada ao kickoff (2026-06-25).

## Documentos Aprovados

| Documento | Caminho |
|---|---|
| Demanda Coletada | `01-qualificacao/demanda-coletada.md` |
| Qualificação | `01-qualificacao/qualificacao.md` |
| Gate de Qualificação | `01-qualificacao/gate-qualificacao.md` |
| Qualificação Aprovada | `01-qualificacao/qualificacao-aprovada.md` |
| Documentação Base (TAP + PM Canvas + Plano Geral) | `02-iniciacao/documentacao-base.md` |
| ERF — Especificação de Requisitos Funcionais | `02-iniciacao/requisitos.md` |
| Work Request (Mini-RFP) | `02-iniciacao/work-request.md` |
| Cronograma + WBS | `03-planejamento/cronograma.md` |
| Plano de Riscos | `03-planejamento/plano-riscos.md` |
| Framework de KPIs | `03-planejamento/kpis.md` |
| Status Report #001 + Pesquisa de Satisfação | `04-monitoramento/status-report-2026-06-11.md` |
| Revisão de Qualidade (Vera Veredito) | `05-encerramento/revisao-final.md` |
| Auditoria de Governança (Gabriel Governança) | `05-encerramento/auditoria-governanca.md` |
| Registro de Aprovação Final (este documento) | `05-encerramento/aprovacao-final.md` |
