---
execution: subagent
agent: iara-inbound
inputFile: squads/vmo-autonomo/output/materiais-demanda.md
outputFile: squads/vmo-autonomo/output/demanda-coletada.md
model_tier: powerful
---

# Step 01: Coletar Demanda

## Context Loading

Load these files before executing:
- `squads/vmo-autonomo/output/materiais-demanda.md` — materiais fornecidos pelo usuário (e-mails, documentos, atas, formulários)
- `squads/vmo-autonomo/pipeline/data/domain-framework.md` — framework do domínio PMO para contexto
- `squads/vmo-autonomo/pipeline/data/anti-patterns.md` — anti-padrões de captação para evitar

## Instructions

### Process
1. **Inventariar os materiais fornecidos**: Listar todos os arquivos e conteúdos disponíveis com tipo e data.
2. **Executar tarefa `coletar-demanda.md`**: Ler agente Iara Inbound e seguir a task de coleta estruturada.
3. **Executar tarefa `extrair-contexto.md`**: Normalizar e estruturar os dados coletados em formato padronizado.
4. **Salvar output**: Escrever o documento completo em `squads/vmo-autonomo/output/demanda-coletada.md`.

## Output Format

```markdown
# Demanda Coletada + Estruturada
[output combinado das tasks coletar-demanda e extrair-contexto]
[ver tasks para formato detalhado]
```

## Output Example

```markdown
# Demanda Estruturada — Rastreamento de Fornecedores Tier 1
ID Demanda: DEM-2026-047
Data: 2026-04-10
Canal: E-mail
Coletado por: Iara Inbound (VMO Autônomo)

Solicitante: Ana Carolina Ferreira — Diretora de Operações — Supply Chain

Necessidade de Negócio:
Falta de visibilidade em tempo real sobre status de entregas de fornecedores
Tier 1 resultou em 3 rupturas de fornecimento no Q1/2026 com custo de R$135k.

Pedido Específico:
Sistema de rastreamento integrado ao SAP com alertas automáticos e dashboard.

[... resto do documento conforme template da task]

Lacunas: orçamento, sponsor, disponibilidade TI (ver seção de lacunas)
Próximo passo: validar com solicitante antes de avançar para qualificação.
```

## Veto Conditions

Reject and redo if ANY are true:
1. Output não inclui seção de lacunas de informação
2. Nenhuma informação de fonte/rastreabilidade documentada nos campos

## Quality Criteria

- [ ] Todas as fontes disponíveis foram consultadas e listadas
- [ ] Demanda estruturada com campos padronizados preenchidos
- [ ] Lacunas documentadas com perguntas de esclarecimento
- [ ] Resumo de confirmação para o solicitante incluído
