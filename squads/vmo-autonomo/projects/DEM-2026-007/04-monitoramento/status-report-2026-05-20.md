# Status Report #001 — DEM-2026-007
Implantação DDA SAP — Contas a Pagar VAB Matriz
Período: Iniciação (20/05/2026)
Data do Report: 2026-05-20
Elaborado por: Sara Status (VMO Autônomo)

---

## STATUS GERAL: 🟡 ATENÇÃO — Aguardando Kick-off

| Dimensão | Status | Observação |
|----------|--------|-----------|
| **Cronograma** | 🟢 Verde | Fase de iniciação concluída; kick-off meta: 08/06/2026 |
| **Custo** | 🟢 Verde | R$0 externo até o momento; meta custo zero |
| **Escopo** | 🟢 Verde | Definido no TAP; CB-2 a confirmar no levantamento técnico |
| **Riscos** | 🔴 Vermelho | R-001 CRÍTICO e R-005 ALTO ativos; CBs pré-kick-off pendentes |
| **Governança** | 🟡 Amarelo | 3 CBs de kick-off abertas (CB-3, CB-Sponsor); aguardando resolução |
| **Qualidade docs** | 🟢 Verde | Documentação de iniciação completa |

**Status geral 🟡 ATENÇÃO:** A fase de iniciação foi concluída com todos os documentos produzidos.
O projeto não pode avançar para kick-off até a resolução das 3 Condições Bloqueantes.
O risco R-001 (autorização Holding) está classificado como CRÍTICO e deve ser endereçado
imediatamente.

---

## Progresso da Iniciação

### Documentos Produzidos ✅

| Documento | Fase | Status |
|-----------|------|--------|
| demanda-coletada.md | Intake | ✅ CONCLUÍDO — Iara Inbound |
| gate-intake.md | Governança | ✅ PASS — Gabriel Governança |
| qualificacao.md (v2) | Qualificação | ✅ CONCLUÍDO — Felipe Filtro (49/100 EM ESPERA) |
| gate-qualificacao.md (v2) | Governança | ✅ PASS — Gabriel Governança |
| qualificacao-aprovada.md | Gateway | ✅ CONCLUÍDO — Aprovado para documentação |
| documentacao-base.md | Iniciação | ✅ CONCLUÍDO — Diana Documento (TAP + PM Canvas + Plano Geral) |
| requisitos.md | Iniciação | ✅ CONCLUÍDO — Rafael Requisito (ERF: 12 RF + 5 RNF) |
| work-request.md | Iniciação | ✅ CONCLUÍDO — Fábio Fornecedor (WR: 10 grupos / 41 itens) |
| cronograma.md | Planejamento | ✅ CONCLUÍDO — Carlos Cronograma (WBS 3 níveis, 6 marcos) |
| plano-riscos.md | Planejamento | ✅ CONCLUÍDO — Pedro Perigo (10 riscos, 4 categorias) |
| kpis.md | Planejamento | ✅ CONCLUÍDO — Marcela Métrica (EVM + 6 KRs) |

### Pendente (pré-kick-off)

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Resolver CB-3: formalizar custos + re-autorização Holding | Noemia → Gladston → Walace Bacelar | 27/05/2026 |
| Identificar sponsor Diretor+ (CB-Sponsor) | Gladston Campos | 30/05/2026 |
| Submeter Work Request ao DTI | Noemia/GP | 23/05/2026 |
| Gate de Kick-off (Gabriel Governança) | VMO | 06/06/2026 |

---

## Riscos em Destaque

| ID | Risco | Nível | Status | Ação imediata |
|----|-------|-------|--------|---------------|
| R-001 | Autorização Holding condicional a custo zero | 🔴 CRÍTICO | Ativo | Confirmar custo zero com DTI antes do kick-off |
| R-005 | Sponsor sem alçada Diretor+ | 🔴 ALTO | Ativo | Gladston deve identificar Diretor+ até 30/05 |
| R-002 | Ajustes complexos (CB-2) | 🟡 ALTO | Monitorando | A resolver no levantamento técnico (M-1) |
| R-003 | Habilitação Santander demorada | 🟡 ALTO | Monitorando | Iniciar contato no kick-off |
| R-006 | Recurso DTI sem disponibilidade/conhecimento | 🟡 ALTO | Monitorando | Confirmar no artefato WR antes do kick-off |

---

## Marcos

| Marco | Data Prevista | Status |
|-------|--------------|--------|
| Iniciação concluída | 20/05/2026 | ✅ CONCLUÍDO |
| Resolução CB-3 + CB-Sponsor | 30/05/2026 | ⏳ Pendente |
| M-0 — Gate de Kick-off | 06/06/2026 | ⏳ Aguardando CBs |
| M-1 — Levantamento técnico | 27/06/2026 | ○ Futuro |
| M-2 — Habilitação Santander | 18/07/2026 | ○ Futuro |
| M-3 — Config + testes | 08/08/2026 | ○ Futuro |
| M-4 — UAT aprovado | 15/08/2026 | ○ Futuro |
| M-5 — Go-live | 25/08/2026 | ○ Futuro |
| M-6 — Encerramento | 30/09/2026 | ○ Futuro |

---

## Próximos Passos (2 semanas)

| # | Ação | Responsável | Data |
|---|------|-------------|------|
| 1 | Submeter Work Request ao DTI (contato: Gladston) | Noemia | 23/05/2026 |
| 2 | Resolver CB-3: confirmar custo zero ou obter nova autorização Holding | Noemia → Gladston → Walace | 27/05/2026 |
| 3 | Identificar sponsor Diretor+ para o projeto | Gladston Campos | 30/05/2026 |
| 4 | DTI responder ao artefato obrigatório do Work Request | Recurso DTI (a designar) | 30/05/2026 |
| 5 | Gate de Kick-off com Gabriel Governança (VMO) | VMO | 06/06/2026 |
| 6 | Kickoff meeting (após gate aprovado) | GP + equipe | 10/06/2026 |

---

## Solicitação ao Sponsor

Gladston Campos: para que o projeto avance para kick-off, são necessárias duas ações imediatas:
1. **CB-Sponsor (urgente até 30/05):** Identificar um patrocinador com nível Diretor+ para o projeto. Sem esta autoridade formal, decisões de escopo/custo podem ser contestadas.
2. **CB-3 (urgente até 27/05):** Confirmar com Walace Bacelar/Holding que o projeto terá custo zero (DTI interna), ou obter nova autorização formal caso haja qualquer custo externo. A autorização atual do Holding é explicitamente condicional a custo zero.

---

Próximo Report: após gate de kick-off (M-0 — 06/06/2026)

---

# Pesquisa de Satisfação — Fase de Iniciação

**Destinatário:** Noemia Tambara Cardoso Malini e Lucas Medeiros Pereira
**Data de envio:** 20/05/2026
**Objetivo:** Validar se a documentação de iniciação reflete corretamente a necessidade de negócio

---

**NPS da fase de iniciação**
Em uma escala de 0 a 10, quão satisfeito(a) você está com o processo de documentação da sua demanda pelo VMO Autônomo?
( ) 0–6 (insatisfeito) ( ) 7–8 (neutro) ( ) 9–10 (muito satisfeito)

**Validação de conteúdo**

1. O TAP descreve corretamente a necessidade de negócio e a solução proposta?
   ( ) Sim, está correto  ( ) Parcialmente — o que está incorreto: _____________  ( ) Não

2. Os critérios de sucesso do TAP refletem o que você espera do projeto?
   ( ) Sim  ( ) Parcialmente — o que ajustar: _____________  ( ) Não

3. O escopo "dentro/fora" do TAP está alinhado com sua expectativa?
   ( ) Sim  ( ) Parcialmente — o que ajustar: _____________  ( ) Não

4. Os requisitos da ERF cobrem o que você precisa do DDA?
   ( ) Sim  ( ) Parcialmente  ( ) Não — o que está faltando: _____________

**Qualitativo**

5. Há algo na documentação que não foi capturado corretamente?

6. Há alguma informação adicional que você gostaria de incluir antes do kick-off?
