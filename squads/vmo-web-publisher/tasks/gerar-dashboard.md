---
task: "Gerar Dashboard Principal (index.html)"
agent: lucas-layout
order: 2
---

# Gerar Dashboard Principal

## Objetivo

Gerar (ou atualizar) `output/site/index.html` com o resumo executivo de todos os projetos do portfólio.

## Seções obrigatórias

1. **Header fixo**: logo VMO Autônomo, badge "Ao Vivo", timestamp de atualização
2. **Métricas do portfólio**: 4 cards — Total de projetos, 🟢 Verde, 🟡 Atenção, 🔵 Em Instrução
3. **Banner de alertas** (se existirem CBs/NCs críticas ativas): destaque em vermelho com prazo
4. **Grid de cards de projetos**: um card por projeto com:
   - ID + badge de status
   - Nome do projeto
   - Cliente e sponsor
   - Semáforo em pills (5 dimensões)
   - Metadados-chave (BAC, go-live, score Vera, resultado Gabriel)
   - Barra de progresso
   - Link "Ver detalhes →" para `projetos/{ID}.html`

## Ordem dos projetos no grid

1. Projetos com status 🟢 Verde primeiro
2. Projetos 🟡 Atenção em seguida
3. Demandas 🔵 Em Instrução por último
4. Dentro de cada grupo: ordem crescente de ID

## Regra de badge de status

| Condição | Badge |
|----------|-------|
| Semáforo geral verde, sem CB ativa | `badge-verde` |
| Qualquer dimensão amarela ou CB aberta | `badge-atencao` |
| Riscos críticos ativos | `badge-atencao` |
| Projeto sem aprovação final (em instrução) | `badge-novo` |
