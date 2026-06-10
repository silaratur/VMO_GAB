# Demanda Validada — DEM-2026-008
Projeto: PROJ-2026-008
Data: 2026-06-10
Validado por: Marcelo Silveira (GP VMO)

## Decisão do Checkpoint

**Confirmar e avançar** — o resumo da demanda coletada (`01-qualificacao/demanda-coletada.md`) foi validado sem correções. As 14 lacunas identificadas (L1–L14) são registradas como pendências a resolver durante a qualificação e fases subsequentes, sem bloquear o avanço para a análise de qualificação.

## Pontos de atenção encaminhados para a Fase de Qualificação (Felipe Filtro)

1. **L4/L5 — Aprovação de Diretoria não confirmada**: o arquivo "APROVAÇÃO - DIRETOR DA ÁREA.pdf" contém, pelo conteúdo extraído, o e-mail da Gerente Contábil (Nubia), não de um Diretor; e a aprovação de "André" mencionada por Tatiane não está documentada.
2. **L3 — Cargo de Gerente de TI não comprovado**: Raphael Leitão Sbardelotti respondeu "De acordo." mas seu cargo formal não consta em nenhuma assinatura capturada.
3. **L7 — Divergência de priorização**: Prioridade "Baixa" (Work Request) vs. Criticidade "2 - Alta" / SLA 1 semana (chamado).

Estes três pontos têm relação direta com a regra de governança "Nunca validar demanda sem aprovações obrigatórias" (Diretoria + Gerente de TI) e devem ser tratados como **Condições Bloqueantes (CB) candidatas** no parecer de qualificação.

## Resumo da Demanda (confirmado)

Conjunto de 15 ajustes adaptativos nos monitores SAP ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 (módulo MM, transações ME51N/ME52N/ME21N/ME22N/ZMMTR002/AS01/AS02), solicitado por Tatiane Dias de Moraes (Coordenadora de Controle de Ativos e Recebimento Fiscal — VIXPar/VIX Matriz) e João Henrique, com especialista técnico de referência Jerfesson Fernandes Helmer. Objetivo: dar autonomia aos usuários para alterar/excluir processos nos monitores, ampliar campos exibidos, automatizar integrações entre PM/AS02 e os monitores GSI, e implementar lógica de estorno de fatura/pedido com log de auditoria. Investimento estimado até R$ 30.000 (declarado como aprovado). Benefício esperado: aumento de produtividade no processo de criação de imobilizado de frota e entrada de notas fiscais.

## Próximo Passo

Avançar para Step 4 — Qualificar Demanda (Felipe Filtro).
