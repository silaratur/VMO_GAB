---
task: "Criar Mini-RFP (Work Request)"
order: 1
input:
  - documentacao_base: "TAP com objetivo, escopo, prazo, orçamento de referência e critérios de sucesso (projects/{project}/02-iniciacao/documentacao-base.md)"
  - requisitos: "ERF com RF e RNF priorizados por MoSCoW (projects/{project}/02-iniciacao/requisitos.md)"
  - web_search: "Pesquisa de mercado — tecnologias disponíveis, prazos típicos, referências de custo para o tipo de solução"
output:
  - work_request: "Mini-RFP completo pronto para envio a fornecedores potenciais"
---

# Criar Mini-RFP (Work Request)

Elabora o documento de solicitação de proposta (Mini-RFP / Work Request) que será enviado a fornecedores potenciais para habilitá-los a submeter propostas qualificadas. O Fábio não é especialista técnico — ele não sabe o que é melhor em termos de arquitetura, linguagem ou infraestrutura. Mas sabe exatamente o que os fornecedores precisam receber para elaborar uma proposta séria e comparável. O que ele não souber sobre tecnologia, ele pesquisa no mercado antes de escrever.

O WR é emitido na fase de iniciação, logo após a ERF — antes do cronograma detalhado e do plano de riscos internos. O objetivo é enviar as diretrizes ao mercado o quanto antes, para que fornecedores possam preparar propostas enquanto a equipe interna conclui o planejamento. Por isso, o cronograma do WR usa benchmarks de mercado e o prazo macro do TAP — não uma WBS detalhada.

## Process

1. **Ler o TAP e a ERF**: Extrair o contexto do projeto, o escopo funcional (módulos/funcionalidades), os RF Must Have, as restrições conhecidas (prazo, orçamento, exclusões) e os critérios de sucesso.

2. **Pesquisar o mercado (web_search)** — o que o Fábio não sabe, ele busca:
   - **Tecnologias disponíveis**: Quais plataformas, frameworks e stacks são usados para o tipo de solução solicitada? Quais são as mais adotadas no mercado brasileiro?
   - **Prazos típicos de mercado**: Quanto tempo projetos similares costumam levar? Quais fases são mais demoradas? Usar para validar/calibrar o prazo macro do TAP.
   - **Referências de custo**: Qual a faixa de investimento típica para soluções desse tipo e porte? Isso ajuda a posicionar o envelope de referência do WR de forma realista.
   - **Fornecedores qualificados**: Que tipo de empresa tem capacidade de entregar? Quais certificações ou experiências mínimas são relevantes para esse tipo de projeto?

3. **Redigir o contexto e justificativa**: Em até 1 página, sintetizar o problema de negócio, o impacto atual e o benefício esperado — derivado do TAP. Linguagem de mercado, não linguagem interna de PMO.

4. **Definir o objetivo da contratação**: O que o fornecedor vai entregar? Qual o resultado final esperado? Qual o critério de sucesso desta contratação (do ponto de vista do contratante)?

5. **Detalhar o escopo incluso**: Traduzir os RF Must Have da ERF para linguagem que um fornecedor compreende — sem jargões internos. Referenciar os IDs (RF001, RF002…) e agrupar por área funcional/módulo. Incluir observações sobre tecnologia com base na pesquisa de mercado.

6. **Declarar o escopo excluso com justificativa**: O que está explicitamente fora. Mínimo 3 exclusões, cada uma com justificativa. Isso protege o contratante de propostas que incluam serviços não solicitados.

7. **Documentar premissas e o que o grupo fornece**: O que o contratante vai disponibilizar ao fornecedor selecionado — acessos, dados, pontos focais, aprovações. Isso reduz o risco de o fornecedor incluir no preço algo que o grupo já provê.

8. **Estimar o cronograma esperado com marcos**: Sem ter o cronograma detalhado do Carlos, Fábio usa:
   - O prazo final do TAP (ex: 31/12/2026)
   - O prazo de kick-off estimado
   - Benchmarks de mercado pesquisados no step 2
   - Para derivar marcos de alto nível (kick-off, entregas parciais por módulo ou fase, UAT, go-live)
   - Indicar claramente que o cronograma detalhado será negociado com o fornecedor selecionado

9. **Listar os entregáveis obrigatórios com critério de aceite binário**: Cada entregável que o fornecedor deve entregar, com o critério que determina se foi aceito ou não.

10. **Definir a governança e comunicação esperada**: Frequência de status reports, reuniões de acompanhamento, canal de comunicação oficial, processo de aprovação de entregas.

11. **Estabelecer as condições comerciais**: Modelo de faturamento por marcos (nunca por hora), prazo de pagamento, regras de reajuste, penalidades por atraso, período de garantia e SLA de suporte pós-implantação. Usar o orçamento de referência do TAP para posicionar o envelope — com nota de que propostas acima do envelope precisam de justificativa.

12. **Transcrever o Artefato Obrigatório integralmente** (10 grupos / 41 itens): Esta seção é inegociável — toda proposta recebida deve conter este checklist preenchido. Transcrever exatamente os grupos abaixo.

13. **Definir o processo de submissão**: Prazo final, canal de envio (e-mail do GP), formato aceito (PDF + planilha), assunto do e-mail, contato para esclarecimentos técnicos e comerciais, condições de desclassificação automática.

## Artefato Obrigatório — 10 Grupos / 41 Itens

Este checklist deve ser transcrito integralmente na Seção do Artefato Obrigatório do WR:

```
Grupo 1 — Identificação da Proposta (6 itens):
  1.1 Nome do fornecedor
  1.2 Projeto / Demanda
  1.3 Tipo de solução (SaaS / Desenvolvimento / SAP)
  1.4 Data de recebimento da proposta
  1.5 Versão da proposta
  1.6 Validade da proposta (mín. 30 dias)

Grupo 2 — Escopo Detalhado da Entrega (6 itens):
  2.1 Objetivo da solução claramente descrito
  2.2 Funcionalidades incluídas detalhadas
  2.3 Módulos, programas ou componentes impactados listados
  2.4 Integrações descritas ou formalmente declaradas como não impactadas
  2.5 Relatórios impactados descritos ou declarados como não impactados
  2.6 Necessidade de licenças claramente informada ou declarada como não aplicável

Grupo 3 — Exclusões de Escopo (2 itens):
  3.1 Exclusões de escopo explicitamente listadas
  3.2 Não utilização de frases genéricas ou ambíguas

Grupo 4 — Premissas (3 itens):
  4.1 Premissas técnicas claramente descritas
  4.2 Premissas de acesso a ambientes e sistemas
  4.3 Premissas de aprovação das entregas intermediárias

Grupo 5 — Metodologia e Abordagem (3 itens):
  5.1 Metodologia adotada explicitamente definida
  5.2 Etapas do projeto claramente descritas
  5.3 Processo de validação e aceite das entregas definido

Grupo 6 — Entregáveis (9 itens):
  6.1 Especificação funcional
  6.2 Especificação técnica
  6.3 Documentação da solução/configuração
  6.4 Plano de testes detalhado
  6.5 Relatórios de execução de testes
  6.6 Plano de implantação / Cutover
  6.7 Plano de suporte pós-implantação
  6.8 Plano de repasse para sustentação
  6.9 Status reports periódicos previstos

Grupo 7 — Governança e Gestão (3 itens):
  7.1 Matriz RACI apresentada
  7.2 Matriz de riscos apresentada
  7.3 Plano de comunicação definido

Grupo 8 — Prazo, Cronograma e Equipe (5 itens):
  8.1 Prazo total de execução informado
  8.2 Cronograma macro apresentado
  8.3 Marcos de entrega definidos
  8.4 Equipe envolvida descrita
  8.5 Prazo para mobilização de recursos

Grupo 9 — Condições Comerciais e Financeiras (4 itens):
  9.1 Valor total do investimento informado
  9.2 Modelo de faturamento por marcos definido
  9.3 Critérios de validação dos marcos descritos
  9.4 Prazo e regras de pagamento definidos

Grupo 10 — Penalidades, Garantia e Sustentação (4 itens):
  10.1 Penalidades e multas previstas
  10.2 Período e condições de garantia definidos
  10.3 SLAs de suporte definidos
  10.4 Plano de sustentação apresentado
```

## Output Format

```markdown
# WORK REQUEST — [CÓDIGO DO PROJETO]
## [Nome Completo do Projeto]

**Versão:** 1.0 | **Data de Emissão:** YYYY-MM-DD | **Elaborado por:** VMO Consultoria
**Validade deste WR:** 60 dias a partir da data de emissão

---

## 1. Identificação do Projeto
[tabela com código, demanda, sponsor, GP, tipo de solução, prazo de submissão]

## 2. Contexto e Justificativa
[problema de negócio + ROI estimado — linguagem de mercado]

## 3. Objetivo da Contratação
[o que o fornecedor vai entregar + critério de sucesso]

## 4. Escopo da Contratação
### 4.1 Escopo Incluso
[tabela com RF Must Have por módulo/área funcional, referenciando IDs]
[nota sobre tecnologias baseada em pesquisa de mercado]

### 4.2 Escopo Excluso
[mínimo 3 exclusões com justificativa]

## 5. Premissas e Responsabilidades do Grupo
[o que o contratante fornece — acessos, dados, pontos focais, aprovações]

## 6. Cronograma Esperado
[marcos de alto nível com datas baseadas no prazo do TAP + benchmarks de mercado]
[nota: cronograma detalhado a ser negociado com o fornecedor selecionado]

## 7. Entregáveis Obrigatórios
[tabela com entregável + critério de aceite binário por item]

## 8. Governança e Comunicação
[frequência de reuniões, status reports, canal oficial, processo de aprovação]

## 9. Condições Comerciais
[faturamento por marcos, prazo de pagamento, penalidades, garantia, SLA]

## 10. Artefato Obrigatório — Conformidade da Proposta
[10 grupos / 41 itens transcritos integralmente com OK/NOK/Observações]

## 11. Processo de Submissão
[prazo, canal, formato, contatos, condições de desclassificação]

---
*Work Request emitido pelo VMO Consultoria em nome do grupo contratante.*
```

## Quality Criteria

- [ ] Identificação completa com código do projeto, demanda, tipo de solução e prazo de submissão
- [ ] Contexto e justificativa em linguagem de mercado (não linguagem interna de PMO)
- [ ] Todos os RF Must Have da ERF referenciados no escopo incluso com seus IDs
- [ ] Mínimo 3 exclusões explícitas com justificativa no escopo excluso
- [ ] Nota de tecnologia baseada em pesquisa de mercado (web_search executado)
- [ ] Cronograma com marcos de alto nível derivados do TAP + benchmarks
- [ ] Entregáveis com critério de aceite binário por item
- [ ] Condições comerciais com faturamento por marcos, penalidades e garantia
- [ ] Artefato Obrigatório com 10 grupos e 41 itens integralmente transcritos
- [ ] Processo de submissão com prazo final e canal de envio

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Escopo incluso sem referência aos IDs de RF da ERF
2. Ausência de escopo excluso ou escopo excluso com menos de 3 exclusões explícitas
3. Artefato Obrigatório incompleto — algum dos 10 grupos ou 41 itens ausente
4. Condições comerciais sem modelo de faturamento por marcos definido
5. Processo de submissão sem prazo final e canal de envio definidos
6. Nenhuma pesquisa de mercado realizada (cronograma baseado apenas no TAP sem benchmarks)
