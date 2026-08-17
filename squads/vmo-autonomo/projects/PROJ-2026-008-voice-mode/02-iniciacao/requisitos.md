# Especificação de Requisitos Funcionais (ERF)

**Projeto:** PROJ-2026-008-voice-mode
**Data:** 17/08/2026
**Analista:** Rafael Requisito
**Versão:** 1.0

---

## Glossário

| Termo | Definição |
|---|---|
| **Voice Mode** | Funcionalidade que permite a agentes multiagentes responder com áudio em tempo real |
| **Agente Multiagente** | Sistema de IA composto por múltiplos agentes especializados que colaboram para resolver tarefas |
| **Homologação** | Processo formal de aprovação de ferramenta/plataforma para uso corporativo |
| **TCO** | Total Cost of Ownership — custo total de propriedade ao longo do tempo |
| **LGPD** | Lei Geral de Proteção de Dados (Lei 13.709/2018) |

---

## Requisitos Funcionais

### Must Have (Obrigatórios)

| ID | Requisito | Critério de Aceitação | Prioridade | Origem |
|---|---|---|---|---|
| RF001 | O estudo deve comparar as 3 soluções (Fireflies, Microsoft Teams/Copilot Studio, Azure Telefonia) em formato estruturado | Documento contém seção dedicada para cada solução com análise nos 7 critérios | Must | Demanda validada [01:20-01:28] |
| RF002 | O estudo deve avaliar cada solução nos 7 critérios definidos: custo, prazo, capacidades técnicas, governança, risco, segurança, conformidade LGPD | Cada solução avaliada em cada um dos 7 critérios com justificativa documentada | Must | Demanda validada [07:57-08:37] |
| RF003 | O estudo deve incluir matriz de prós e contras para cada solução | Tabela com mínimo 3 prós e 3 contras por solução | Must | Demanda validada [04:05] |
| RF004 | O estudo deve incluir uma recomendação fundamentada | Seção de recomendação com justificativa técnica e de negócio | Must | Demanda validada [07:34-07:41] |
| RF005 | O estudo deve analisar conformidade com LGPD e políticas internas | Seção de conformidade com checklist de requisitos legais por solução | Must | Demanda validada [08:29-08:37] |

### Should Have (Importantes)

| ID | Requisito | Critério de Aceitação | Prioridade | Origem |
|---|---|---|---|---|
| RF006 | O estudo deve incluir estimativa de custos (TCO) para cada solução | Tabela com custos estimados de licenciamento, infra e operação | Should | Demanda validada [10:17-10:20] |
| RF007 | O estudo deve avaliar o roadmap de cada solução | Timeline estimado de disponibilidade de Voice Mode para cada plataforma | Should | Sizing — pesquisa técnica |
| RF008 | O estudo deve incluir análise de governança corporativa por solução | Comparação de modelos de governança (Microsoft vs. terceiros vs. Azure) | Should | Demanda validada [07:57] |

### Could Have (Desejáveis)

| ID | Requisito | Critério de Aceitação | Prioridade | Origem |
|---|---|---|---|---|
| RF009 | O estudo deve incluir resumo executivo de 1 página | Sumário visual com recomendação e semáforo por critério | Could | Quality criteria — executivo |
| RF010 | O estudo deve incluir matriz de decisão ponderada | Tabela com pesos por critério e pontuação total por solução | Could | Best practice — análise comparativa |

### Won't Have (Fora do Escopo)

| ID | Requisito | Motivo da Exclusão |
|---|---|---|
| RF011 | Plano de implementação da solução escolhida | Fora do escopo — demanda validada [07:10-07:22] |
| RF012 | Prova de conceito (POC) das soluções | Fora do escopo — prazo de 1 dia não permite |
| RF013 | Negociação comercial com fornecedores | Fora do escopo — TAP seção 4 |

---

## Requisitos Não-Funcionais

| ID | Requisito | Critério de Aceitação | Categoria |
|---|---|---|---|
| RNF001 | O documento deve ser entregue em formato Markdown ou PDF legível | Documento renderiza corretamente em visualizadores padrão | Usabilidade |
| RNF002 | A análise de cada solução deve ser baseada em fontes verificáveis | Cada afirmação técnica referencia documentação oficial ou fonte identificável | Qualidade |
| RNF003 | O estudo deve ser compreensível por stakeholders não-técnicos | Linguagem acessível, glossário incluído, sem jargões sem definição | Usabilidade |
| RNF004 | O documento deve seguir os padrões VMO de documentação | Conformidade com quality-criteria.md e domain-framework.md | Conformidade |

---

## Rastreabilidade

| Requisito | Origem | Validação |
|---|---|---|
| RF001-RF005 | Transcrição Fireflies — conversa Neemias/Dário | Confirmação do solicitante [09:24-09:30] |
| RF006-RF008 | Transcrição Fireflies + sizing.md + best practices | Pendente validação do solicitante |
| RF009-RF010 | Best practices de análise comparativa | Desejável — não obrigatório |
| RNF001-RNF004 | Padrões VMO internos | Revisão pela Vera Veredito |
