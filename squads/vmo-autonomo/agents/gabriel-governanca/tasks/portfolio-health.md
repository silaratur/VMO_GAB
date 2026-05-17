---
task: "Portfolio Health Check"
order: 4
mode: on-demand
input:
  - state_files: "squads/vmo-autonomo/projects/*/state.json"
  - status_reports: "squads/vmo-autonomo/projects/*/04-monitoramento/status-report-*.md (mais recente por projeto)"
  - auditorias: "squads/vmo-autonomo/projects/*/05-encerramento/auditoria-governanca.md (se existir)"
output:
  - portfolio_health: "Relatório consolidado de saúde do portfólio com recomendações"
---

# Portfolio Health Check

Produz o relatório mensal de saúde do portfólio VMO — visão consolidada de todos os projetos ativos com foco em governança, compliance e nível de atenção requerida pelo GP. Enquanto os status reports individuais mostram como cada projeto está, o Portfolio Health mostra como o portfólio como um todo está sendo gerenciado.

## Process

1. **Varrer todos os projetos:** Listar todos os diretórios em `squads/vmo-autonomo/projects/` com `state.json` presente.
2. **Ler state.json de cada projeto:** Extrair status, projeto, demanda, score da Vera (se disponível) e data de atualização.
3. **Ler o status report mais recente de cada projeto:** Extrair semáforo, issues abertas e próximos passos.
4. **Ler auditoria de governança (se existir):** Verificar NCs abertas e status de compliance.
5. **Calcular saúde por projeto:** Cruzar os dados e atribuir nível de atenção (Verde / Amarelo / Vermelho).
6. **Identificar padrões:** Há riscos de governança comuns entre projetos? Há gargalos sistêmicos?
7. **Emitir recomendações consolidadas** para o GP VMO.

## Critérios de Saúde por Projeto

| Indicador | Verde | Amarelo | Vermelho |
|-----------|-------|---------|---------|
| NCs de governança abertas | 0 | 1-2 NC-MOD | Qualquer NC-CRÍTICA |
| CBs em aberto | 0 | 1 CB | 2+ CBs |
| Semáforo do último status report | Todos verdes | 1-2 amarelos | Qualquer vermelho |
| Score Vera | ≥ 90 | 85–89 | < 85 |
| Status do projeto | completed / running | checkpoint | Desconhecido |

## Output Format

```markdown
# Portfolio Health Check — VMO Autônomo
Data: YYYY-MM-DD | Auditor: Gabriel Governança
Projetos analisados: [N] | Período de referência: [mês/ano]

---

## Semáforo Consolidado do Portfólio

| Projeto | Nome | Status | Saúde | Score Vera | CBs Abertas | NCs Abertas | Atenção |
|---------|------|--------|-------|------------|-------------|-------------|---------|
| PROJ-2026-001 | [nome] | completed | 🟢 | 8,7/10 | 0 | 0 | Baixa |
| PROJ-2026-006 | [nome] | checkpoint | 🟡 | 9,2/10 | 2 | 0 | Média |

---

## Análise por Projeto

### PROJ-XXXX — [Nome]
**Status:** [completed / running / checkpoint / blocked]
**Score de qualidade (Vera):** [score]/10
**Saúde de governança:** 🟢/🟡/🔴

| Dimensão | Status | Observação |
|----------|--------|------------|
| Sponsor identificado | ✅/❌ | [nome, cargo] |
| Orçamento aprovado | ✅/❌ | [R$ valor] |
| CBs resolvidas | [N/N] | [lista de CBs abertas] |
| NCs de auditoria | [N abertas] | [tipos] |
| Último status report | [data] | [semáforo] |

[Repetir para cada projeto]

---

## Padrões e Riscos Sistêmicos

[Riscos que aparecem em múltiplos projetos — ex: "3 dos 4 projetos ativos têm sponsor não identificado"]

---

## Recomendações para o GP VMO

| Prioridade | Recomendação | Projetos Afetados | Prazo |
|------------|-------------|-------------------|-------|
| Alta | [ação] | PROJ-XXX, PROJ-YYY | [data] |
| Média | [ação] | [projetos] | [data] |

---

*Portfolio Health Check gerado por Gabriel Governança — Auditor de Governança VMO*
```

## Veto Conditions

Rejeitar e refazer se:
1. Algum projeto com pasta em `projects/` foi omitido do relatório
2. Recomendações sem projeto afetado identificado (recomendação genérica sem âncora)
