---
execution: subagent
agent: fabio-fornecedor
inputFile: squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md
outputFile: squads/vmo-autonomo/projects/{project}/03-planejamento/work-request.md
model_tier: powerful
---

# Step 10: Criar Work Request

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/documentacao-base.md` — TAP com objetivo, escopo, sponsor, critérios de sucesso e baseline financeiro
- `squads/vmo-autonomo/projects/{project}/02-iniciacao/requisitos.md` — ERF com RF Must Have (escopo incluso) e demais requisitos (candidatos a escopo excluso)
- `squads/vmo-autonomo/projects/{project}/03-planejamento/cronograma.md` — marcos e datas esperadas para o cronograma do WR
- `squads/vmo-autonomo/projects/{project}/03-planejamento/plano-riscos.md` — riscos relevantes para definir premissas e condições comerciais
- `squads/vmo-autonomo/projects/{project}/03-planejamento/kpis.md` — baseline financeiro (BAC) para referência nas condições comerciais

## Instructions

### Process
1. **Executar tarefa `criar-work-request.md`**: Gerar o WR completo seguindo o template e os dados do projeto.
2. **Verificar completude do Artefato Obrigatório**: Confirmar que todos os 10 grupos e 41 itens estão presentes com colunas OK / NOK / Observações.
3. **Validar referências cruzadas**: Cada RF Must Have da ERF deve aparecer no escopo incluso do WR com seu ID; funcionalidades Should Have e Could Have devem aparecer no escopo excluso.
4. **Salvar output**: Escrever o WR completo em `squads/vmo-autonomo/projects/{project}/03-planejamento/work-request.md`.

## Output Format

```markdown
# WORK REQUEST — [CÓDIGO DO PROJETO]
## [Nome Completo do Projeto]

[WR completo conforme template da task criar-work-request.md]
[incluir: identificação, contexto, objetivo, escopo incluso/excluso, premissas,
cronograma, entregáveis, governança, condições comerciais, artefato obrigatório
(10 grupos / 41 itens), processo de submissão]
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
- [ ] Contexto com problema de negócio e ROI referenciado
- [ ] Objetivo com critério de sucesso mensurável
- [ ] Todos os RF Must Have da ERF referenciados no escopo incluso
- [ ] Mínimo 3 exclusões explícitas no escopo excluso
- [ ] Cronograma com marcos e datas derivados do cronograma do projeto
- [ ] Entregáveis com critério de aceite binário por item
- [ ] Condições comerciais com faturamento por marcos, penalidades e garantia
- [ ] Artefato Obrigatório com 10 grupos e 41 itens integralmente transcritos
- [ ] Processo de submissão com prazo, canal, formato e contatos
