---
execution: subagent
agent: iara-inbound
outputFile: squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md
model_tier: powerful
---

# Step 01: Coletar Demanda

## Canal de Entrada — Detecção Automática

A Iara Inbound aceita demandas de QUALQUER canal. Antes de executar, ela inventaria
o que está disponível no contexto atual e em disco, priorizando nesta ordem:

1. **Arquivos anexados na sessão** — PDFs, .msg, .docx, imagens, transcrições
2. **`squads/vmo-autonomo/output/materiais-demanda.md`** — arquivo pré-posicionado (canal legado)
3. **Conteúdo colado diretamente na conversa** — texto de ticket, e-mail, WhatsApp, formulário
4. **Transcrições Fireflies** — reuniões de discovery (via skill `fireflies`)
5. **Nenhum material encontrado** → perguntar ao usuário antes de avançar

Se mais de um canal estiver disponível, usar todos e documentar cada fonte separadamente.
Se nenhum material estiver disponível, interromper e apresentar:
```
⚠️ Iara não encontrou materiais de demanda.
Por favor, forneça pelo menos um dos seguintes:
- Arquivo do ticket (PDF, .msg)
- Texto do e-mail ou mensagem
- Arquivo pré-posicionado em squads/vmo-autonomo/output/materiais-demanda.md
```

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/pipeline/data/domain-framework.md` — framework PMO para contexto
- `squads/vmo-autonomo/pipeline/data/anti-patterns.md` — anti-padrões de captação

## Instructions

### Process
1. **Detectar e inventariar fontes disponíveis**: Verificar cada canal da lista acima.
   Registrar o canal detectado e listar todos os materiais encontrados com tipo e data.
2. **Executar tarefa `coletar-demanda.md`**: Seguir a task de coleta multi-canal estruturada.
3. **Executar tarefa `extrair-contexto.md`**: Normalizar e estruturar os dados coletados.
4. **Salvar output**: Escrever o documento em `squads/vmo-autonomo/projects/{project}/01-qualificacao/demanda-coletada.md`.

## Output Format

```markdown
# Demanda Coletada + Estruturada
Canal de Entrada: [ticket / e-mail / pdf / fireflies / direto / múltiplos]
[output combinado das tasks coletar-demanda e extrair-contexto]
[ver tasks para formato detalhado]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Output não inclui seção de lacunas de informação
2. Nenhum campo tem rastreabilidade de fonte documentada
3. Canal de entrada não foi identificado e registrado
4. Nenhum material foi encontrado e o pipeline avançou mesmo assim (deve ter parado)

## Quality Criteria

- [ ] Canal de entrada identificado e documentado
- [ ] Todas as fontes consultadas listadas com data e tipo
- [ ] Cada campo tem referência à fonte de origem
- [ ] Lacunas documentadas com perguntas de esclarecimento
- [ ] Resumo de confirmação para o solicitante incluído
