---
task: "Coletar Demanda"
order: 1
input:
  - canal_entrada: "Canal detectado: ticket, e-mail, PDF, .msg, transcrição, texto direto ou materiais-demanda.md"
  - materiais_disponiveis: "Qualquer arquivo, texto ou referência fornecida pelo usuário ou disponível no contexto"
output:
  - demanda_estruturada: "Dados da demanda organizados em campos padronizados"
  - canal_documentado: "Canal de entrada identificado e fontes listadas"
  - lacunas_identificadas: "Lista de campos sem informação com ação requerida"
  - fonte_por_campo: "Rastreabilidade de origem para cada informação coletada"
---

# Coletar Demanda

Lê todos os materiais disponíveis em QUALQUER canal de entrada e extrai as informações
da demanda em formato estruturado e rastreável. É o primeiro passo do pipeline —
a qualidade desta coleta determina a de todos os documentos subsequentes.

## Canais Suportados

| Canal | Como detectar | Como extrair |
|-------|--------------|--------------|
| Ticket de service desk (PDF) | Arquivo .pdf no contexto | Ler com Read tool; extrair campos do formulário |
| E-mail (.msg) | Arquivo .msg no contexto | Extrair remetente, destinatários, assunto, corpo |
| E-mail (texto) | Texto colado ou em materiais-demanda.md | Extrair cabeçalho e corpo |
| PDF genérico | Arquivo .pdf | Ler e extrair dados relevantes |
| Transcrição Fireflies | Referência a reunião ou ID Fireflies | Usar skill fireflies_get_transcript |
| Texto direto | Conteúdo na conversa | Extrair diretamente |
| materiais-demanda.md | Arquivo em squads/.../output/ | Ler e processar normalmente |
| Múltiplos | Combinação dos acima | Consolidar com rastreabilidade por fonte |

## Process

1. **Inventariar fontes disponíveis**: Listar todos os materiais detectados com canal, tipo e data.
   Se nenhuma fonte for encontrada, parar e solicitar ao usuário antes de avançar.

2. **Extrair por campo e por fonte**: Para cada campo obrigatório abaixo, localizar a informação
   em cada fonte disponível. Registrar qual fonte forneceu cada dado.

3. **Detectar inconsistências entre fontes**: Se o mesmo campo aparecer com valores diferentes
   em fontes distintas, registrar AMBOS como inconsistência com flag `⚠️ INCONSISTÊNCIA`.

4. **Identificar lacunas**: Campos sem informação em NENHUMA fonte são marcados
   `[NÃO INFORMADO — requer esclarecimento]` com pergunta específica ao solicitante.

5. **Registrar contexto implícito**: Além dos campos formais, registrar qualquer informação
   contextual relevante (conflitos políticos mencionados, urgências entre-linhas, restrições
   não declaradas). Fonte sempre documentada.

## Output Format

```markdown
# Demanda Coletada
Data da Coleta: YYYY-MM-DD
Coletado por: Iara Inbound
Canal de Entrada: [ticket / e-mail / pdf / fireflies / direto / múltiplos — especificar]

## Fontes Consultadas
| # | Canal | Tipo | Descrição | Data |
|---|-------|------|-----------|------|
| 1 | ticket | PDF | Ticket #NNNN — Sistema X — Solicitação Y | YYYY-MM-DD |
| 2 | e-mail | .msg | De: Fulano → Para: PMO — Assunto Z | YYYY-MM-DD |

## Dados da Demanda

**Solicitante**
- Nome: [nome ou NÃO INFORMADO]
- Cargo: [cargo ou NÃO INFORMADO]
- Área/Divisão: [área ou NÃO INFORMADO]
- Contato: [e-mail/telefone ou NÃO INFORMADO]
- Fonte: [referência à fonte]

**Necessidade de Negócio**
[descrição do problema real, não da solução — o QUE está errado ou faltando]
Fonte: [referência]

**Pedido Específico**
[o que foi solicitado concretamente — a solução proposta pelo solicitante]
Fonte: [referência]

**Benefício Esperado**
[benefício descrito ou estimado — quantificado se disponível]
Fonte: [referência]

**Urgência e Prazo**
- Prazo desejado: [data concreta ou NÃO INFORMADO]
- Urgência declarada: [alta/média/baixa ou NÃO INFORMADO]
- Origem do prazo: [motivação real — evento, contrato, lei — ou NÃO INFORMADO]
- SLA do ticket (se aplicável): [prazo do ticket e status — em atraso, no prazo]
Fonte: [referência]

**Aprovações e Autorizações Identificadas**
[listar qualquer aprovação já concedida — mesmo informal via e-mail]
- [Nome, cargo, data, conteúdo da aprovação, condicional/incondicional]
Fonte: [referência]

**Contexto Organizacional**
- Divisão/empresa: [unidade de negócio]
- Área executora provável: [área de TI ou negócio]
- Projetos relacionados ou precedentes: [exemplos conhecidos no grupo]
- Restrições conhecidas: [prazo, orçamento, tecnologia, política]
- Stakeholders identificados: [nomes e papéis mencionados em qualquer fonte]
Fonte: [referência]

**Contexto Implícito** (informações entre-linhas ou subentendidas)
[registrar qualquer contexto que não foi declarado explicitamente mas é relevante]
Fonte: [referência]

## Lacunas Identificadas
| # | Campo | Status | Pergunta para Esclarecimento |
|---|-------|--------|------------------------------|
| 1 | [campo] | NÃO INFORMADO | [pergunta específica e direta] |

## Resumo para Confirmação
[3-5 linhas resumindo a demanda para validação com o solicitante antes de avançar]
```

## Quality Criteria

- [ ] Canal de entrada identificado e documentado
- [ ] Todas as fontes consultadas listadas com canal, tipo e data
- [ ] Cada campo tem referência explícita à fonte de origem
- [ ] Aprovações e autorizações já existentes documentadas (se houver)
- [ ] Lacunas documentadas com pergunta específica de esclarecimento
- [ ] Necessidade de negócio distinguida do pedido técnico (problema vs. solução)
- [ ] Inconsistências entre fontes sinalizadas com flag ⚠️
- [ ] Contexto implícito registrado quando identificado

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. O campo "Necessidade de Negócio" está vazio ou apenas repete o pedido técnico
2. Nenhum campo tem rastreabilidade de fonte documentada
3. Canal de entrada não foi identificado
4. Havia múltiplas fontes disponíveis mas apenas uma foi consultada
