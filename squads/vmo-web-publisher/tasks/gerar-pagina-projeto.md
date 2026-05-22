---
task: "Gerar Página HTML por Projeto"
agent: lucas-layout
order: 3
---

# Gerar Página HTML por Projeto

Para cada projeto identificado no scan, gerar (ou atualizar) o arquivo `output/site/projetos/{ID}.html`.

## Fontes de dados (ordem de leitura)

1. `squads/vmo-autonomo/projects/{ID}/state.json` — status do pipeline
2. `squads/vmo-autonomo/projects/{ID}/04-monitoramento/status-report-*.md` — semáforo e progresso
3. `squads/vmo-autonomo/projects/{ID}/03-planejamento/kpis.md` — CPI, SPI, BAC
4. `squads/vmo-autonomo/projects/{ID}/03-planejamento/plano-riscos.md` — riscos ativos
5. `squads/vmo-autonomo/projects/{ID}/03-planejamento/cronograma.md` — marcos e deadline
6. `squads/vmo-autonomo/projects/{ID}/05-encerramento/aprovacao-final.md` — decisão e score final
7. `squads/vmo-autonomo/projects/{ID}/05-encerramento/auditoria-governanca.md` — NCs e ressalvas
8. `squads/vmo-autonomo/projects/{ID}/05-encerramento/revisao-final.md` — score Vera Veredito

## Seções obrigatórias da página HTML

1. **Hero block**: ID, título, status badge, metadados (cliente, sponsor, BAC, go-live, fase, aprovação final)
2. **Semáforo de dimensões**: tabela com prazo, custo, escopo, riscos, qualidade — com dot colorido e observação
3. **Revisão de qualidade**: scores de Vera Veredito e Gabriel Governança, NCs identificadas
4. **Progresso**: barra(s) de progresso com % instrução e % execução
5. **Marcos**: timeline com datas e status (✅/⏳/⚠️/🎯)
6. **Riscos ativos**: lista com nível (CRÍTICO/ALTO/MÉDIO/BAIXO) e descrição
7. **Próximos passos**: ações pendentes com responsável e prazo
8. **Condições bloqueantes** (se existirem): destaque visual em vermelho com prazo e responsável
9. **Link de volta**: `← Dashboard` no header

## Regra de status badge

| Condição | Badge |
|----------|-------|
| Status geral 🟢 em todos os semáforos | `badge-verde` |
| Qualquer semáforo 🟡, sem CB ativa | `badge-atencao` |
| CB ativa ou NC-CRÍTICA não resolvida | `badge-atencao` com banner vermelho |
| Projeto em instrução (sem aprovação final) | `badge-novo` (cyan) |
| Semáforo 🔴 em risco ou sponsor | `badge-atencao` com alert vermelho |

## Nota importante

Esta task gera apenas o HTML. O espelhamento dos documentos fonte é feito pela task `espelhar-documentos.md` (Step 4) — as duas tasks são complementares e ambas obrigatórias por run.
