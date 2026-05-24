---
task: "Espelhar Documentos dos Projetos"
agent: lucas-layout
order: 4
type: required
---

# Espelhar Documentos dos Projetos

> ⚠️ **Esta task é OBRIGATÓRIA em todo run do vmo-web-publisher.** Um run que gera HTML sem executar esta task está incompleto.

## Objetivo

Para cada projeto identificado no Step 1 (scan), copiar os arquivos `.md` fonte de `squads/vmo-autonomo/projects/{ID}/` para `squads/vmo-web-publisher/output/site/projetos/docs/{ID}/`.

Isso garante que os documentos reais do projeto estejam acessíveis diretamente a partir do dashboard — mantendo a pasta `docs/` sempre sincronizada com `vmo-autonomo/projects/`.

---

## Processo

Para cada `{ID}` encontrado em `squads/vmo-autonomo/projects/`:

1. Criar (ou atualizar) a pasta `output/site/projetos/docs/{ID}/`
2. Copiar cada arquivo listado na tabela de mapeamento abaixo
3. Se o arquivo fonte não existir (fase não concluída), pular silenciosamente — não gerar erro
4. Se houver múltiplos `status-report-*.md`, usar o mais recente (maior nome lexicográfico)
5. Registrar quais arquivos foram copiados para o log do run

---

## Mapeamento Fonte → Destino

| Arquivo fonte em `squads/vmo-autonomo/projects/{ID}/` | Destino em `output/site/projetos/docs/{ID}/` |
|-------------------------------------------------------|----------------------------------------------|
| `01-qualificacao/qualificacao.md` | `01-qualificacao.md` |
| `01-qualificacao/demanda-coletada.md` | `02-demanda-coletada.md` |
| `02-iniciacao/documentacao-base.md` | `03-tap-canvas-plano-geral.md` |
| `02-iniciacao/requisitos.md` | `04-erf-requisitos.md` |
| `03-planejamento/cronograma.md` | `05-cronograma.md` |
| `03-planejamento/plano-riscos.md` | `06-plano-riscos.md` |
| `03-planejamento/kpis.md` | `07-kpis.md` |
| `04-monitoramento/status-report-*.md` (mais recente) | `08-status-report.md` |
| `05-encerramento/revisao-final.md` | `09-revisao-final.md` |
| `05-encerramento/aprovacao-final.md` | `10-aprovacao-final.md` |
| `05-encerramento/auditoria-governanca.md` | `11-auditoria-governanca.md` |

---

## Estrutura de Output esperada

```
output/site/projetos/docs/
  PROJ-2026-001/
    01-qualificacao.md
    02-demanda-coletada.md
    03-tap-canvas-plano-geral.md
    04-erf-requisitos.md
    05-cronograma.md
    06-plano-riscos.md
    07-kpis.md
    08-status-report.md
    09-revisao-final.md
    10-aprovacao-final.md
    11-auditoria-governanca.md
  PROJ-2026-003/
    [mesma estrutura]
  PROJ-2026-004/
    [mesma estrutura]
  PROJ-2026-005/
    [mesma estrutura]
  PROJ-2026-006/
    [mesma estrutura]
  DEM-2026-007/
    [mesma estrutura, com os arquivos disponíveis]
```

---

## Quality Criteria

- [ ] Pasta `docs/{ID}/` criada para cada projeto identificado no scan
- [ ] Pelo menos `01-qualificacao.md` presente para qualquer projeto com qualificação concluída
- [ ] Arquivos ausentes (fases não concluídas) foram pulados sem erro
- [ ] `08-status-report.md` corresponde ao status-report mais recente do projeto
- [ ] Nenhum arquivo foi escrito diretamente em `squads/vmo-autonomo/projects/` (nunca sobrescrever a fonte)

## Veto Conditions

Rejeitar e refazer o run se qualquer das seguintes condições for verdadeira:
1. Algum projeto tem página HTML gerada mas **não tem pasta `docs/{ID}/`**
2. Arquivo foi escrito na pasta fonte (`vmo-autonomo/`) em vez da pasta de output
3. O mapeamento de nomes foi ignorado (arquivos copiados com nome original em vez do nome padronizado)
