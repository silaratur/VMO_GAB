---
type: checkpoint
outputFile: squads/vmo-autonomo/projects/{project}/05-encerramento/aprovacao-final.md
---

# Step 12: Checkpoint — Aprovar Documentação Final

## Purpose

Este é o checkpoint de aprovação final do pacote de iniciação do projeto. O solicitante/patrocinador revisa e aprova formalmente todos os documentos produzidos antes do projeto avançar para a fase de execução.

## Context to Present to User

Antes de apresentar as perguntas ao usuário, exibir um resumo do pacote:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📋 PACOTE DE INICIAÇÃO — PRONTO PARA APROVAÇÃO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Projeto: [Nome do Projeto]
Pontuação de Qualidade: [Score]/100
Status da Revisão: ✅ APROVADO pelo Revisor de Qualidade

Documentos produzidos:
  ✅ TAP — Termo de Abertura do Projeto
  ✅ PM Canvas — 9 blocos preenchidos
  ✅ ERF — Especificação de Requisitos Funcionais
  ✅ Cronograma — WBS + Datas + Caminho Crítico
  ✅ Plano de Riscos — Registro + Plano de Resposta
  ✅ Framework de KPIs — EVM + Semáforo de Saúde
  ✅ Status Report #001 — Iniciação concluída
  ✅ Pesquisa de Satisfação — Template pronto

Todos os documentos em: squads/vmo-autonomo/projects/{project}/05-encerramento/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Checkpoint Questions

### Pergunta 1: Aprovação do Pacote

> Você revisou o pacote de documentação de iniciação do projeto. Qual é sua decisão?

Opções:
- **Aprovar e iniciar execução** — Documentação aprovada, projeto pode avançar
- **Aprovar com ressalvas** — Aprovado, mas com ajustes menores a fazer durante execução
- **Solicitar revisão parcial** — Um ou mais documentos precisam de ajuste antes de aprovar
- **Reprovar e retrabalhar** — Documentação insuficiente, retornar ao início da documentação

### Pergunta 2 (se "Aprovar" ou "Aprovar com ressalvas"): Confirmação do Kickoff

> Quando deseja agendar o kickoff do projeto?

Opções:
- **Esta semana** — Kickoff imediato
- **Próxima semana** — Uma semana de preparação
- **Em duas semanas** — Período de preparação estendido
- **Definir depois** — Aprovar sem data de kickoff agora

### Pergunta 2 (se "Solicitar revisão parcial"): Qual documento revisar?

> Qual documento precisa de ajuste?

Opções:
- **TAP ou PM Canvas** — Documentação base do projeto
- **ERF ou Cronograma** — Requisitos ou planejamento de prazo
- **Riscos ou KPIs** — Gestão de riscos ou indicadores
- **Status Report** — Relatório inicial ou pesquisa de satisfação

## Branching Logic

| Decisão | Próxima ação |
|---------|-------------|
| Aprovar / Aprovar com ressalvas | Salvar aprovação → Pipeline concluído → Apresentar resumo final |
| Solicitar revisão parcial | Retornar ao step correspondente (Step 5 para doc base, Step 6 para ERF, Step 7 para cronograma, Step 8 para riscos, Step 9 para KPIs, Step 10 para status report) |
| Reprovar e retrabalhar | Retornar ao Step 5 com instrução de revisão completa |

## Output to Save

Independente da decisão, salvar o registro da aprovação:

```markdown
# Registro de Aprovação — [Nome do Projeto]

## Decisão: [APROVADO | APROVADO COM RESSALVAS | REVISÃO PARCIAL | REPROVADO]
- Data: [data]
- Aprovador: [nome do usuário]
- Pontuação de qualidade: [score]/100

## Ressalvas (se houver)
[Pontos de atenção registrados]

## Próximos Passos
[Data de kickoff definida ou próxima ação acordada]

## Documentos Aprovados
[Lista dos documentos com path de cada arquivo]
```

## Completion Message

Se aprovado, exibir ao usuário:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🎉 PROJETO APROVADO — INICIAÇÃO CONCLUÍDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O pacote de iniciação foi aprovado e o projeto está
autorizado a avançar para a fase de execução.

Próximos passos:
  1. Distribuir documentação para o time
  2. Agendar reunião de kickoff
  3. Ativar monitoramento de KPIs (CPI, SPI)
  4. Responder a Pesquisa de Satisfação de Iniciação

Para monitorar o projeto, use:
  /opensquad run vmo-autonomo

Documentação completa em:
  squads/vmo-autonomo/projects/{project}/05-encerramento/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
