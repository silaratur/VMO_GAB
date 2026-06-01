# Squad Memory: VMO Autônomo

## Estilo de Escrita

## Design Visual

## Estrutura de Conteúdo

## Proibições Explícitas

- **Nunca validar demanda sem aprovações obrigatórias (regra GP — 2026-05-24):** Toda demanda, independente da origem ou criticidade declarada, só pode ser considerada VALIDADA se possuir: (1) aprovação formal em nível de Diretoria da área solicitante; (2) aprovação do Gerente de TI da divisão solicitante. Sem ambas, a demanda retorna ao solicitante para complementação — independente de urgência declarada, prazo de SLA ou pressão política.

- **Nunca aceitar citação de alta patente sem evidência documental (regra GP — 2026-05-24):** Toda vez que uma demanda citar CEO, Diretor Executivo, VP ou outra alta patente como origem ou justificativa de urgência, é OBRIGATÓRIO ter evidência documental comprobatória (e-mail, ata de reunião, documento assinado, print de mensagem oficial). A citação sem evidência não pode sustentar nota de urgência acima de 3/10 (Felipe) nem dispensar qualquer condição de processo. Iara deve sinalizar como `⚠️ CLAIM SEM EVIDÊNCIA` e classificar como Lacuna de alto impacto. Felipe deve rebaixar o critério de Urgência proporcionalmente.

## Técnico (específico do squad)

- **REGRAS METODOLÓGICAS DO FELIPE FILTRO — CRÍTICO (validadas 2026-05-31 no PROJ-2026-007):**
  1. **Esforço (critério 7) exige Rafael Requisitos**: Felipe NÃO pode estimar esforço por benchmark. O dimensionamento de esforço só é válido após levantamento inicial de escopo por Rafael Requisitos. Sem esse dado, critério 7 = EM ESPERA.
  2. **InterCompany mesma divisão = mesma área operacional**: Processos InterCompany de empresas da mesma divisão de negócio são operados pelo mesmo grupo de pessoas. Não conta como impacto multi-área sem confirmação de que equipes de diferentes gerências são afetadas.
  3. **GMUD não diferencia projeto de melhoria**: Toda mudança SAP (inclusive simples) passa por GMUD (transport request, janela operacional). GMUD é critério de mudança SAP, não de complexidade de gestão. Felipe NÃO deve usar GMUD como indicador de governança formal (critério 9).
  4. **Implicação de fluxo**: Step 5 "Rafael Sizing" criado no pipeline v4.0.0 entre Checkpoint Validar Demanda (Step 4) e Felipe Qualificar (Step 6) — implementado e validado.

- **Regra de estrutura de pastas (2026-05-24):** Toda nova pasta de projeto `projects/{PROJ-CODE}/` deve ter TODAS as 5 subpastas de fase criadas imediatamente na inicialização: `01-qualificacao`, `02-iniciacao`, `03-planejamento`, `04-monitoramento`, `05-encerramento`. Git não rastreia diretórios vazios — criar `.gitkeep` em todas as pastas que ainda não possuem arquivos, para que a estrutura completa apareça no repositório remoto desde o início. O `.gitkeep` é removido quando o primeiro arquivo real for escrito na pasta.

- **Nova estrutura de pastas validada (2026-05-16):** A migração de `output/{run_id}/v{N}/` para `projects/{PROJ-CODE}/{fase}/` funciona corretamente. Todos os 10 agentes escreveram nos caminhos corretos com placeholder `{project}` resolvido. Estrutura de fases: 01-qualificacao, 02-iniciacao, 03-planejamento, 04-monitoramento, 05-encerramento.
- **Fábio Fornecedor validado (Step 10):** Primeiro run completo com o agente de Work Request. Score 8,5/10 na revisão da Vera. Artefato Obrigatório (10 grupos / 41 itens) transcrito corretamente. Inconsistência narrativa identificada: seção de contexto deve referenciar "plataforma SaaS terceira" (não "planilhas e e-mails") para projetos de substituição de sistema.
- **Ressalva de sponsor registrada pelo GP:** Nivel mínimo de sponsor para aprovação de TAP é Diretor ou superior. Registrar como condição bloqueante CB-01 explícita no TAP, não apenas como lacuna genérica.

## Run History

### Re-execução 2026-05-18 — Pipeline v2 (4 projetos simultâneos)

**Objetivo:** Aplicar os 2 novos steps do pipeline v2 (Step 7 — Fábio Fornecedor / Work Request; Step 13 — Gabriel Governança / Auditoria de Governança) em todos os projetos sem esse tratamento.

**Nova estrutura de pastas aplicada:** `projects/{PROJ-CODE}/{01-qualificacao, 02-iniciacao, 03-planejamento, 04-monitoramento, 05-encerramento}/`

**Resultados:**

| Projeto | Score Vera | Auditoria Gabriel | Aprovação Final |
|---------|-----------|-------------------|-----------------|
| PROJ-2026-001 — SAP FI Aprovador | 8.7/10 | APROVADO COM RESSALVAS (NC-MENOR: TAP sem assinatura) | ✅ APROVADO |
| PROJ-2026-003 — Caminhos ERP GAB | 9.0/10 | APROVADO (3 riscos preventivos) | ✅ APROVADO |
| PROJ-2026-004 — Plataforma Ideias | 10.0/10 | REPROVADO NC-CRÍTICA (sponsor A DEFINIR) | ✅ APROVADO com ciência |
| PROJ-2026-005 — Auditor Fiscal NBS | 9.1/10 | REPROVADO NC-CRÍTICA (sponsor CB-01, prazo 25/05) | ✅ APROVADO com ciência |

**Aprendizados do pipeline v2:**
- Fábio Fornecedor (Step 7): WRs gerados para todos os 4 projetos com 10 grupos / 41 itens do Artefato Obrigatório. Subagentes atingiram rate limit — executar inline é mais confiável para runs múltiplos simultâneos.
- Gabriel Governança (Step 13): Auditoria crítica de sponsor funcionou corretamente como filtro de governança. PROJ-004 e PROJ-005 corretamente REPROVADOS por sponsor ausente, com ciência do GP registrada em aprovacao-final.md.
- Sponsor ausente é NC-CRÍTICA recorrente — reforçar no onboarding de novas demandas: sponsor deve ser identificado ANTES do pipeline iniciar.
- Nova estrutura de pastas por fase facilita rastreabilidade mas exige que todos os agentes resolvam o placeholder `{project}` corretamente.

### Run 2026-05-15-150000 — PROJ-2026-005

**Demanda:** Auditor Fiscal — Módulo Nativo NBS em Substituição ao Fiscal Defender. Solicitante: Sandro Siqueira (Coordenador de Contabilidade, Divisão Comércio, Grupo Águia Branca). Saving: R$78K/ano, custo zero de desenvolvimento (contrapartida contratual NBS).
**Score qualificação:** 18/30 (60%) — APROVADO COM CONDIÇÕES
**Score revisão final (Vera):** 91/100 — APROVADO
**Aprovado por:** Marcelo Silveira (GP VMO)

**Aprendizados do processo:**
- Demanda coletada via Fireflies (reunião "Discovery Demandas - Hugo <> Sandro Siqueira", ID: 01KRP1TW4YV4TZMB3V0044FD16, 2026-05-15).
- Projetos onde o desenvolvimento é de responsabilidade de fornecedor externo (NBS) têm risco central diferente: a verificação documental do acordo é a condição bloqueante mais crítica, não o orçamento interno.
- Score de qualificação mais baixo (18/30) não impede instrução quando o ROI é robusto e as lacunas estão bem documentadas — GP pode aprovar com condições.
- VME (R$145,4K) superou orçamento do projeto (R$35K) por ampla margem — o risco RSK-02 (acordo NBS) domina: se materializado, business case colapsa.
- 27 RFs em 6 módulos funcionais + 12 RNFs — padrão mais denso que PROJ-2026-004 (37 RFs, mas projeto maior); proporção RF/módulo similar.
- Buffer de 15% aplicado em fases 3-4 (desenvolvimento e UAT) — mesma metodologia de PROJ-2026-004, confirmando padrão.
- 5 não-conformidades leves identificadas por Vera (nenhuma estrutural); score 91/100 é robusto para projeto com tantas lacunas declaradas.

**Condições bloqueantes identificadas:**
1. Sponsor executivo — identificar até 25/05/2026
2. Acordo NBS verificado documentalmente — confirmar até 30/05/2026

**Outputs gerados (8 documentos):**
- `v1/demanda-coletada.md` — Iara Inbound
- `v1/qualificacao.md` — Felipe Filtro (18/30, 60%)
- `v2/documentacao-base.md` — Diana Documento (TAP + PM Canvas + Plano Geral)
- `v3/requisitos.md` — Rafael Requisito (27 RFs + 12 RNFs)
- `v4/cronograma.md` — Carlos Cronograma (77 pacotes, 12 marcos, go-live 30/10/2026)
- `v5/plano-riscos.md` — Pedro Perigo (18 riscos, VME R$145,4K, reserva R$163,4K)
- `v6/kpis.md` — Marcela Métrica (EVM BAC R$35K, curva S, 6 KRs pós-go-live)
- `v7/status-report-inicial.md` — Sara Status (Status Report #001 + pesquisa satisfação)
- `v8/revisao-final.md` — Vera Veredito (Score 91/100 — APROVADO)

### Run 2026-05-14-201500 — PROJ-2026-004

**Demanda:** Plataforma Interna de Gestão de Ideias de Inovação — substitui plataforma terceirizada (~R$80-90K/ano). Solicitante: Jadson (Área de Inovação, Grupo Águia Branca). Prazo: dezembro/2026 (Prêmio Inovação jan/2027).
**Score qualificação:** 21/30 (70%) — APROVADO COM CONDIÇÕES
**Score revisão final (Vera):** 100/100 — APROVADO
**Aprovado por:** Marcelo Silveira (GP VMO)

**Aprendizados do processo:**
- Demanda coletada via Fireflies (reunião "Discovery Demandas - Sara <> JADSON", ID: 01KPV48BER47DVPT37Q0CGCNXN, 2026-04-22). Integração Fireflies→pipeline funcionou bem.
- Sponsor não identificado é a condição bloqueante mais crítica — documentado como RSK-01 (score 20, crítico). Todos os documentos devem destacar esta dependência de forma explícita e consistente.
- 37 RFs em 6 módulos funcionais (M1-M6) + 10 RNFs — escopo bem definido para plataforma web corporativa sem integrações.
- Buffer de 15% aplicado por fase de desenvolvimento — metodologia a reutilizar em projetos de software.
- Execução paralela de agentes (Diana + Rafael) economiza tempo significativo quando leem do mesmo input.

**Condições bloqueantes identificadas:**
1. Sponsor executivo — identificar até 13/06/2026
2. Orçamento aprovado (R$90K) — aprovar até 13/06/2026
3. Modelo de execução (TI interna / externo / misto) — definir até kick-off

**Outputs gerados (8 documentos):**
- `v1/demanda-coletada.md` — Iara Inbound
- `v1/qualificacao.md` — Felipe Filtro (21/30, 70%)
- `v2/documentacao-base.md` — Diana Documento (TAP + PM Canvas + Plano Geral)
- `v3/requisitos.md` — Rafael Requisito (37 RFs + 10 RNFs)
- `v4/cronograma.md` — Carlos Cronograma (WBS + 9 marcos + caminho crítico, go-live 28/11/2026)
- `v5/plano-riscos.md` — Pedro Perigo (12 riscos, reserva R$10.5K alocada)
- `v6/kpis.md` — Marcela Métrica (EVM BAC R$75K, curva S, 5 KRs pós-go-live)
- `v7/status-report-inicial.md` — Sara Status (Status Report #001 + pesquisa satisfação)
- `v8/revisao-final.md` — Vera Veredito (Score 100/100 — APROVADO)

### Run 2026-04-03-134220 — PROJ-2026-001

**Demanda:** Inclusão de Aprovador SAP FI (ZFI0057 + SBWP) — VIX Manutenção
**Score final:** 8.7/10 — APROVADO
**Aprovado por:** Marcelo Silveira

**Aprendizados do processo:**
- Qualificação inicial marcou EM ESPERA (14/30) por falta de contexto real da demanda — motivação real (Diretor Financeiro fora do fluxo, risco de fraude) só foi revelada no checkpoint Step 4. O pipeline de qualificação funcionou corretamente como filtro de maturidade.
- O sponsor sendo o mesmo que o aprovador incluído no fluxo é uma situação recorrente em projetos SAP FI de governança — reduz risco de resistência mas mantém risco de indisponibilidade por agenda executiva.
- Valor esperado de riscos (R$5.450) superou reserva de contingência orçamentária (R$1.440) — principalmente pelo risco de ABAP (R$3.000 esperado). Sinalizar ao sponsor no kickoff.
- Premissa de disponibilidade da equipe Basis a 70% deve ser explicitada no cronograma em projetos SAP concorrentes.

**Outputs gerados:**
- 7 documentos de iniciação (TAP, PM Canvas, Plano Geral, ERF, Cronograma, Plano de Riscos, KPIs)
- Status Report Inicial + Revisão de Qualidade
- Pacote consolidado: PROJ-2026-001-pacote-iniciacao.md
