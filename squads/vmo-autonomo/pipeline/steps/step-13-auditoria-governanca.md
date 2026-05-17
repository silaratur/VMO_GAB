---
execution: inline
agent: gabriel-governanca
inputFile: squads/vmo-autonomo/projects/{project}/05-encerramento/revisao-final.md
outputFile: squads/vmo-autonomo/projects/{project}/05-encerramento/auditoria-governanca.md
on_reject: 5
---

# Step 13: Auditoria de Governança VMO

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/01-qualificacao/qualificacao-aprovada.md` — CBs registradas e decisão de aprovação
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — TAP (sponsor, escopo, orçamento, critérios de sucesso)
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md` — ERF com RF/RNF para rastreabilidade
- `squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md` — baseline de prazo
- `squads/vmo-autonomo/projects/{project}/03-planejamento/plano-riscos.md` — riscos e reserva
- `squads/vmo-autonomo/projects/{project}/03-planejamento/kpis.md` — BAC e KPIs (consistência com TAP)
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/work-request.md` — Mini-RFP emitido para fornecedores
- `squads/vmo-autonomo/projects/{project}/04-monitoramento/status-report-{date}.md` — último status report
- `squads/vmo-autonomo/projects/{project}/05-encerramento/revisao-final.md` — veredicto da Vera

## Instructions

### Process

1. **Executar tarefa `auditoria-governanca.md`**: Realizar a auditoria completa nos 5 domínios (Sponsor, Rastreabilidade, Políticas VMO, Completude, Riscos de Governança).
2. **Classificar todas as não-conformidades**: Cada NC classificada como CRÍTICA, MODERADA ou MENOR.
3. **Emitir veredicto de governança**:
   - APROVADO: zero NC-CRÍTICAS e menos de 3 NC-MODERADAS
   - APROVADO COM RESSALVAS: zero NC-CRÍTICAS mas 3+ NC-MODERADAS (projeto avança com plano de correção)
   - REPROVADO: qualquer NC-CRÍTICA presente → retorna ao agente responsável (on_reject: 5 para retrabalho de documentação base)
4. **Definir ações corretivas**: Para cada NC, ação, responsável e prazo.
5. **Salvar output**: Escrever relatório completo em `squads/vmo-autonomo/projects/{project}/05-encerramento/auditoria-governanca.md`.

## Output Format

```markdown
# Auditoria de Governança VMO — [PROJ-CODE]
[relatório completo conforme template da task auditoria-governanca.md]
[incluir: veredicto, D1-D5 auditados, tabela de NCs, recomendações]
```

## Diferença em relação à Revisão da Vera (Step 12)

| Aspecto | Vera Veredito (Step 12) | Gabriel Governança (Step 13) |
|---------|------------------------|------------------------------|
| Foco | Qualidade do conteúdo dos documentos | Conformidade do processo de governança |
| Avalia | Se o TAP tem objetivo SMART | Se o sponsor tem nível Diretor+ |
| Avalia | Se a ERF tem critérios de aceitação | Se as CBs foram resolvidas com evidência |
| Avalia | Se o cronograma tem caminho crítico | Se os documentos são consistentes entre si |
| Avalia | Se o plano de riscos tem VME calculado | Se o WR foi emitido e está completo |
| Bloqueia por | Score < 85 ou bloqueador crítico de conteúdo | NC-CRÍTICA de processo ou 3+ NC-MOD |

## Veto Conditions

Reject and redo if ANY are true:
1. Algum dos 5 domínios não foi auditado
2. NC-CRÍTICA presente mas veredicto marcado como APROVADO
3. Alguma NC sem ação corretiva definida com responsável e prazo

## Quality Criteria

- [ ] Todos os 5 domínios auditados com evidência documental citada
- [ ] Cada NC classificada (CRÍTICA / MODERADA / MENOR)
- [ ] Veredicto claro e coerente com as NCs encontradas
- [ ] Rastreabilidade cross-document verificada numericamente
- [ ] Se REPROVADO: instrução específica de qual agente deve corrigir o quê
