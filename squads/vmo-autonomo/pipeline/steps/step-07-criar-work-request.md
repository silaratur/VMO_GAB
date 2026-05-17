---
execution: subagent
agent: fabio-fornecedor
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md
outputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/work-request.md
model_tier: powerful
---

# Step 07: Criar Work Request (Mini-RFP)

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — TAP com objetivo, escopo, sponsor, critérios de sucesso, prazo e orçamento de referência
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md` — ERF com RF e RNF Must Have que serão exigidos dos fornecedores
- Web search disponível para: prazos típicos de mercado, tecnologias disponíveis, referências de custo para o tipo de solução solicitada

**Nota:** Este step roda logo após a ERF (Step 6), antes do cronograma e riscos internos. O WR vai ao mercado enquanto a equipe interna continua o planejamento detalhado — por isso o Fábio usa o prazo macro do TAP e pesquisa de mercado para estimar marcos, não o cronograma do Carlos (que ainda não existe).

## Instructions

### Process
1. **Executar tarefa `criar-work-request.md`**: Elaborar o Mini-RFP completo com pesquisa de mercado para contextualizar tecnologias e prazos típicos.
2. **Verificar completude do Artefato Obrigatório**: Confirmar que todos os 10 grupos e 41 itens estão presentes com colunas OK / NOK / Observações.
3. **Validar referências cruzadas**: Cada RF Must Have da ERF deve aparecer no escopo incluso do WR; exclusões do TAP devem aparecer no escopo excluso.
4. **Salvar output**: Escrever o WR completo em `squads/vmo-autonomo/projects/{project}/02-iniciacao/work-request.md`.

## Output Format

```markdown
# WORK REQUEST — [CÓDIGO DO PROJETO]
## [Nome Completo do Projeto]

[WR completo conforme template da task criar-work-request.md]
[incluir: identificação, contexto, objetivo, escopo incluso/excluso, premissas,
cronograma esperado (baseado em TAP + benchmarks de mercado), entregáveis,
governança, condições comerciais, artefato obrigatório (10 grupos / 41 itens),
processo de submissão]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Escopo incluso sem referência a IDs de RF da ERF
2. Nenhuma exclusão de escopo explícita documentada
3. Artefato Obrigatório com qualquer dos 10 grupos ausente ou incompleto
4. Condições comerciais sem modelo de faturamento por marcos
5. Processo de submissão sem prazo final de recebimento de propostas

## Quality Criteria

- [ ] Identificação completa do projeto (código, demanda, sponsor, GP, tipo de solução)
- [ ] Contexto com problema de negócio e ROI referenciado do TAP
- [ ] Todos os RF Must Have da ERF referenciados no escopo incluso
- [ ] Mínimo 3 exclusões explícitas no escopo excluso
- [ ] Cronograma com marcos de alto nível (baseados no prazo do TAP + benchmarks de mercado)
- [ ] Entregáveis com critério de aceite binário por item
- [ ] Condições comerciais com faturamento por marcos, penalidades e garantia
- [ ] Artefato Obrigatório com 10 grupos e 41 itens integralmente transcritos
- [ ] Processo de submissão com prazo, canal, formato e contatos
