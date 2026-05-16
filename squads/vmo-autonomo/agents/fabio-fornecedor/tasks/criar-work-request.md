---
task: "Criar Work Request"
order: 1
input:
  - documentacao_base: "TAP com objetivo, escopo, sponsor e critérios de sucesso (projects/{project}/02-iniciacao/documentacao-base.md)"
  - requisitos: "ERF com RF e RNF priorizados por MoSCoW (projects/{project}/02-iniciacao/requisitos.md)"
  - cronograma: "WBS e cronograma com marcos e caminho crítico (projects/{project}/03-planejamento/cronograma.md)"
  - plano_riscos: "Registro de riscos e plano de resposta (projects/{project}/03-planejamento/plano-riscos.md)"
  - kpis: "Framework de KPIs e baseline financeiro (projects/{project}/03-planejamento/kpis.md)"
output:
  - work_request: "Work Request completo pronto para envio a fornecedores"
---

# Criar Work Request

Estrutura o documento oficial de Solicitação de Trabalho (Work Request — WR) do projeto, destinado a fornecedores que serão convidados a apresentar propostas. O WR sintetiza toda a documentação de iniciação em um único documento orientado ao mercado: objetivo claro, escopo detalhado, condições comerciais, entregáveis obrigatórios e o artefato de conformidade que toda proposta recebida deve preencher. Um WR bem estruturado elimina ambiguidade, produz propostas comparáveis e protege o grupo em eventuais disputas contratuais.

## Process

1. **Extrair identificação do projeto**: Do TAP, coletar código do projeto, nome completo, sponsor, Gerente de Projeto VMO, tipo de solução e data de emissão do WR.
2. **Redigir contexto e justificativa**: Em até 1 página, sintetizar o problema de negócio, o impacto atual da falta da solução e o benefício esperado com a contratação — derivado diretamente da seção de justificativa do TAP e da análise de ROI da qualificação.
3. **Definir objetivo da contratação**: 1–3 parágrafos descrevendo o que o grupo espera contratar, o resultado esperado e o critério de sucesso da contratação (baseado nos critérios de sucesso do TAP).
4. **Detalhar escopo incluso**: Listar os requisitos funcionais Must Have da ERF que fazem parte desta contratação, referenciando os IDs (RF001, RF002…). Agrupar por área funcional. Detalhar integrações, relatórios e componentes impactados.
5. **Declarar escopo excluso**: Listar explicitamente o que NÃO faz parte desta contratação — funcionalidades Should Have ou Could Have que ficam para fases futuras, sistemas fora do perímetro, módulos adjacentes não impactados. Mínimo 3 exclusões explícitas.
6. **Documentar premissas e responsabilidades do grupo**: O que o contratante fornece — acessos a ambientes, dados de teste, pontos focais técnicos, aprovações de entregas intermediárias, infraestrutura.
7. **Definir cronograma esperado**: Derivar do cronograma do projeto — prazo total de execução, fases e marcos principais com datas esperadas. Incluir prazo máximo para mobilização de equipe do fornecedor após assinatura do contrato.
8. **Listar entregáveis obrigatórios com critério de aceite**: Para cada entregável (especificação funcional, técnica, plano de testes, cutover, etc.), definir o critério de aceite binário que autoriza a aprovação.
9. **Definir governança e comunicação**: Estrutura de reuniões, frequência de status reports, matriz RACI esperada, canal oficial de comunicação.
10. **Estabelecer condições comerciais**: Modelo de faturamento por marcos, prazo de pagamento após aceite do marco, regras de aditivo de escopo, penalidades por atraso, período de garantia e SLAs de suporte pós-implantação.
11. **Transcrever o Artefato Obrigatório integralmente**: Incluir os 10 grupos e 41 itens do checklist de conformidade exatamente como definido abaixo, com colunas OK / NOK / Observações em branco para o fornecedor preencher.
12. **Definir processo de submissão**: Prazo final para recebimento de propostas, canal de envio (e-mail do GP ou portal), formato aceito (PDF + planilha), contato para esclarecimentos técnicos e contato para esclarecimentos comerciais.

## Output Format

```markdown
# WORK REQUEST — [CÓDIGO DO PROJETO]
## [Nome Completo do Projeto]

**Versão:** 1.0 | **Data de Emissão:** YYYY-MM-DD | **Elaborado por:** VMO Consultoria
**Validade deste WR:** 60 dias a partir da data de emissão

---

## 1. Identificação do Projeto

| Campo | Informação |
|-------|-----------|
| Código do Projeto | PROJ-YYYY-NNN |
| Nome do Projeto | [nome completo] |
| Código da Demanda | DEM-YYYY-NNN |
| Tipo de Solução | [SaaS / Desenvolvimento / SAP / Híbrido] |
| Sponsor | [nome e cargo] |
| Gerente de Projeto (VMO) | [nome] |
| Data de Emissão | YYYY-MM-DD |
| Prazo para Submissão de Proposta | YYYY-MM-DD |

---

## 2. Contexto e Justificativa

[2–3 parágrafos: problema de negócio, impacto atual, benefício esperado com a contratação.
Incluir o ROI estimado e o custo do não-fazer quando disponível.]

---

## 3. Objetivo da Contratação

[1–3 parágrafos: o que o grupo contrata, o resultado esperado e o critério de sucesso.
Derivar diretamente dos critérios de sucesso do TAP.]

---

## 4. Escopo da Contratação

### 4.1 Escopo Incluso

| ID | Requisito | Descrição | Prioridade |
|----|-----------|-----------|------------|
| RF001 | [nome] | [descrição do requisito] | Must Have |
| RF002 | [nome] | [descrição] | Must Have |
| [demais RF Must Have da ERF] | | | |

**Integrações:** [listar sistemas integrados ou declarar "Não há integrações no escopo desta contratação"]
**Relatórios:** [listar relatórios impactados ou declarar "Não há relatórios no escopo"]
**Licenças:** [declarar necessidade de licenças ou "Não aplicável"]

### 4.2 Escopo Excluso

As seguintes funcionalidades, sistemas e serviços estão explicitamente **fora** do escopo desta contratação:

1. **[Exclusão 1]** — [justificativa: fase futura / fora do perímetro / decisão de negócio]
2. **[Exclusão 2]** — [justificativa]
3. **[Exclusão 3]** — [justificativa]
[mínimo 3 exclusões explícitas]

---

## 5. Premissas e Responsabilidades do Grupo

O grupo contratante se compromete a fornecer:

- [ ] Acesso aos ambientes de desenvolvimento, qualidade e produção com perfis adequados
- [ ] Ponto focal técnico dedicado para esclarecimento de dúvidas (máximo 1 dia útil de SLA)
- [ ] Aprovação formal de entregas intermediárias em até [N] dias úteis após recebimento
- [ ] Dados de teste anonimizados para execução do plano de testes
- [ ] [outras responsabilidades específicas do projeto]

---

## 6. Cronograma Esperado

| Marco | Descrição | Data Esperada | Critério de Aceite |
|-------|-----------|---------------|-------------------|
| M0 | Assinatura do contrato e mobilização | YYYY-MM-DD | Equipe do fornecedor identificada e acessos provisionados |
| M1 | [Marco 1 do projeto] | YYYY-MM-DD | [critério de aceite binário] |
| M2 | [Marco 2] | YYYY-MM-DD | [critério] |
| [demais marcos] | | | |
| Mn | Go-live e encerramento | YYYY-MM-DD | Aprovação formal em produção |

**Prazo máximo de mobilização:** O fornecedor deve mobilizar 100% da equipe proposta em até **[N] dias úteis** após assinatura do contrato.

---

## 7. Entregáveis Obrigatórios

| # | Entregável | Descrição | Critério de Aceite | Marco de Pagamento |
|---|-----------|-----------|-------------------|-------------------|
| 1 | Especificação Funcional | Documento detalhando comportamento esperado de cada requisito | Aprovação do GP e área de negócio em até 5 dias úteis | M1 |
| 2 | Especificação Técnica | Arquitetura, componentes e design técnico da solução | Aprovação da equipe técnica interna em até 5 dias úteis | M1 |
| 3 | Documentação da Solução/Configuração | Manual de configuração e operação | Aprovação do GP | M(n-1) |
| 4 | Plano de Testes Detalhado | Casos de teste funcionais e não-funcionais com critérios PASS/FAIL | Aprovação do GP e QA | M2 |
| 5 | Relatórios de Execução de Testes | Resultado de cada caso de teste executado | Taxa de aprovação ≥ 95% nos Must Have; zero defeitos críticos | M(n-1) |
| 6 | Plano de Implantação / Cutover | Passo a passo de go-live com rollback plan | Aprovação do GP e TI | M(n-1) |
| 7 | Plano de Suporte Pós-Implantação | SLAs e canais de atendimento pós go-live | Aprovação do GP | Mn |
| 8 | Plano de Repasse para Sustentação | Transferência de conhecimento para equipe interna | Aprovação do GP e TI | Mn |
| 9 | Status Reports Periódicos | Relatório quinzenal de progresso durante execução | Enviado dentro do prazo; aprovado pelo GP | Contínuo |

---

## 8. Governança e Comunicação

- **Reunião de kickoff:** Obrigatória em até 5 dias úteis após assinatura do contrato
- **Status reports:** Quinzenais, enviados ao GP até toda sexta-feira
- **Reuniões de acompanhamento:** [frequência] com pauta e ata registradas
- **Canal oficial de comunicação:** E-mail institucional do GP + ferramenta de gestão do projeto
- **Escalada:** Qualquer desvio de prazo > 5 dias úteis deve ser comunicado com antecedência mínima de 3 dias úteis com plano de recuperação

---

## 9. Condições Comerciais

### 9.1 Modelo de Faturamento
O faturamento ocorre exclusivamente por **marcos de entrega aprovados**. Nenhum pagamento é realizado por horas trabalhadas ou período.

| Marco | % do Valor Total | Condição de Faturamento |
|-------|-----------------|------------------------|
| M0 — Mobilização | [%] | Contrato assinado e equipe mobilizada |
| M1 — [descrição] | [%] | [critério de aceite do marco] |
| [demais marcos] | | |
| Mn — Go-live e encerramento | [%] | Aprovação formal em produção |

### 9.2 Prazo de Pagamento
Pagamento em até **[N] dias úteis** após emissão de nota fiscal vinculada ao aceite formal do marco pelo GP.

### 9.3 Reajuste e Aditivos
- Reajuste de valor somente por aditivo contratual formal, aprovado pelo VMO e sponsor
- Alterações de escopo que impactem prazo ou custo exigem Change Request aprovado antes da execução

### 9.4 Penalidades
- Atraso em marco de entrega: multa de **[%]** do valor do marco por semana de atraso, limitada a **[%]** do valor total do contrato
- Não conformidade de entregável após 2 ciclos de correção: multa de **[%]** do valor do marco

### 9.5 Garantia
- Período de garantia: **[N] meses** após aceite do go-live
- Durante a garantia: correção de defeitos sem custo adicional em até **[N] dias úteis** por severidade
- SLA de atendimento pós-garantia: [definição de SLA por severidade]

---

## 10. Artefato Obrigatório — Conformidade da Proposta

**INSTRUÇÃO AO FORNECEDOR:** Toda proposta submetida deve incluir este artefato preenchido integralmente. Propostas com itens NOK sem justificativa ou com campos em branco **não serão aceitas para avaliação**.

### 1. Identificação da Proposta

| Item | Informação | OK | NOK | Observações |
|------|-----------|:--:|:---:|-------------|
| 1.1 | Nome do fornecedor | ☐ | ☐ | |
| 1.2 | Projeto / Demanda | ☐ | ☐ | |
| 1.3 | Tipo de solução (SaaS / Desenvolvimento / SAP) | ☐ | ☐ | |
| 1.4 | Data de recebimento da proposta | ☐ | ☐ | |
| 1.5 | Versão da proposta | ☐ | ☐ | |
| 1.6 | Validade da proposta (mín. 30 dias) | ☐ | ☐ | |

### 2. Escopo Detalhado da Entrega

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 2.1 | Objetivo da solução claramente descrito | ☐ | ☐ | |
| 2.2 | Funcionalidades incluídas detalhadas | ☐ | ☐ | |
| 2.3 | Módulos, programas ou componentes impactados listados | ☐ | ☐ | |
| 2.4 | Integrações descritas ou formalmente declaradas como não impactadas | ☐ | ☐ | |
| 2.5 | Relatórios impactados descritos ou declarados como não impactados | ☐ | ☐ | |
| 2.6 | Necessidade de licenças claramente informada ou declarada como não aplicável | ☐ | ☐ | |

### 3. Exclusões de Escopo

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 3.1 | Exclusões de escopo explicitamente listadas | ☐ | ☐ | |
| 3.2 | Não utilização de frases genéricas ou ambíguas | ☐ | ☐ | |

### 4. Premissas

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 4.1 | Premissas técnicas claramente descritas | ☐ | ☐ | |
| 4.2 | Premissas de acesso a ambientes e sistemas | ☐ | ☐ | |
| 4.3 | Premissas de aprovação das entregas intermediárias | ☐ | ☐ | |

### 5. Metodologia e Abordagem

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 5.1 | Metodologia adotada explicitamente definida | ☐ | ☐ | |
| 5.2 | Etapas do projeto claramente descritas | ☐ | ☐ | |
| 5.3 | Processo de validação e aceite das entregas definido | ☐ | ☐ | |

### 6. Entregáveis

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 6.1 | Especificação funcional | ☐ | ☐ | |
| 6.2 | Especificação técnica | ☐ | ☐ | |
| 6.3 | Documentação da solução/configuração | ☐ | ☐ | |
| 6.4 | Plano de testes detalhado | ☐ | ☐ | |
| 6.5 | Relatórios de execução de testes | ☐ | ☐ | |
| 6.6 | Plano de implantação / Cutover | ☐ | ☐ | |
| 6.7 | Plano de suporte pós-implantação | ☐ | ☐ | |
| 6.8 | Plano de repasse para sustentação | ☐ | ☐ | |
| 6.9 | Status reports periódicos previstos | ☐ | ☐ | |

### 7. Governança e Gestão

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 7.1 | Matriz RACI apresentada | ☐ | ☐ | |
| 7.2 | Matriz de riscos apresentada | ☐ | ☐ | |
| 7.3 | Plano de comunicação definido | ☐ | ☐ | |

### 8. Prazo, Cronograma e Equipe

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 8.1 | Prazo total de execução informado | ☐ | ☐ | |
| 8.2 | Cronograma macro apresentado | ☐ | ☐ | |
| 8.3 | Marcos de entrega definidos | ☐ | ☐ | |
| 8.4 | Equipe envolvida descrita | ☐ | ☐ | |
| 8.5 | Prazo para mobilização de recursos | ☐ | ☐ | |

### 9. Condições Comerciais e Financeiras

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 9.1 | Valor total do investimento informado | ☐ | ☐ | |
| 9.2 | Modelo de faturamento por marcos definido | ☐ | ☐ | |
| 9.3 | Critérios de validação dos marcos descritos | ☐ | ☐ | |
| 9.4 | Prazo e regras de pagamento definidos | ☐ | ☐ | |

### 10. Penalidades, Garantia e Sustentação

| Item | Requisito | OK | NOK | Observações |
|------|----------|:--:|:---:|-------------|
| 10.1 | Penalidades e multas previstas | ☐ | ☐ | |
| 10.2 | Período e condições de garantia definidos | ☐ | ☐ | |
| 10.3 | SLAs de suporte definidos | ☐ | ☐ | |
| 10.4 | Plano de sustentação apresentado | ☐ | ☐ | |

---

## 11. Processo de Submissão de Propostas

| Item | Informação |
|------|-----------|
| **Prazo final de submissão** | YYYY-MM-DD às HH:MM (horário de Brasília) |
| **Canal de envio** | [e-mail do GP] com cópia para [e-mail VMO] |
| **Formato obrigatório** | PDF (proposta completa) + planilha Excel (precificação detalhada por marco) |
| **Assunto do e-mail** | `[PROJ-YYYY-NNN] Proposta Comercial — [Nome do Fornecedor]` |
| **Esclarecimentos técnicos** | [nome e e-mail do ponto focal técnico] até [data limite para perguntas] |
| **Esclarecimentos comerciais** | [nome e e-mail do GP ou área de compras] |
| **Sessão de Q&A** | [data e formato — reunião online / assíncrono via e-mail] |

**Nota:** Propostas recebidas após o prazo, em formato diferente do especificado ou sem o Artefato Obrigatório (Seção 10) preenchido serão automaticamente desclassificadas.

---

*Work Request emitido pelo VMO Consultoria em nome do grupo contratante.*
*Versão 1.0 — Documento de uso restrito.*
```

## Output Example

```markdown
# WORK REQUEST — PROJ-2026-001
## Sistema de Rastreamento de Fornecedores Tier 1 (SRF)

**Versão:** 1.0 | **Data de Emissão:** 2026-04-20 | **Elaborado por:** VMO Consultoria
**Validade deste WR:** 60 dias a partir da data de emissão

---

## 1. Identificação do Projeto

| Campo | Informação |
|-------|-----------|
| Código do Projeto | PROJ-2026-001 |
| Nome do Projeto | Sistema de Rastreamento de Fornecedores Tier 1 (SRF) |
| Código da Demanda | DEM-2026-001 |
| Tipo de Solução | Desenvolvimento / Integração SAP |
| Sponsor | Ana Carolina Ferreira — Diretora de Operações |
| Gerente de Projeto (VMO) | [Nome GP VMO] |
| Data de Emissão | 2026-04-20 |
| Prazo para Submissão de Proposta | 2026-05-05 |

---

## 2. Contexto e Justificativa

O grupo enfrenta recorrentes rupturas de fornecimento causadas pela falta de visibilidade em tempo real sobre o status de entregas dos fornecedores Tier 1. No Q1/2026, 3 incidentes de ruptura geraram impacto financeiro estimado em R$ 135.000 em custos operacionais e perda de produção.

A solução atual depende de atualizações manuais via e-mail, com latência de até 4 horas para detecção de atrasos. O custo do não-fazer — mantendo o processo atual — é estimado em R$ 540.000 por ano com tendência crescente dado o aumento do volume de pedidos projetado para 2026.

A contratação do SRF visa eliminar essa lacuna de visibilidade, com ROI estimado de 215% e payback em 18 meses (dados da qualificação DEM-2026-001, aprovada em 2026-04-12).

---

## 3. Objetivo da Contratação

Contratar o desenvolvimento e implantação de um sistema de rastreamento em tempo real para entregas de fornecedores Tier 1, integrado ao SAP MM, com alertas automáticos de atraso e dashboard de monitoramento para a equipe de Supply Chain.

O critério de sucesso desta contratação é: **100% dos fornecedores Tier 1 com localização de entrega visível em tempo real (latência máxima de 15 minutos) até 30/10/2026**, com taxa de falsos alertas inferior a 5%.

---

[demais seções seguindo o formato acima, preenchidas com dados reais do projeto]
```

## Quality Criteria

- [ ] Identificação completa: código do projeto, demanda, sponsor, GP, tipo de solução, data de emissão e prazo de submissão
- [ ] Contexto com problema de negócio, impacto atual e ROI referenciado da qualificação
- [ ] Objetivo com critério de sucesso mensurável e com prazo
- [ ] Escopo incluso com IDs de RF da ERF referenciados (mínimo todos os Must Have)
- [ ] Escopo excluso com mínimo 3 exclusões explícitas e justificadas
- [ ] Premissas e responsabilidades do grupo listadas com checkboxes
- [ ] Cronograma com marcos e datas esperadas derivadas do cronograma do projeto
- [ ] Entregáveis com critério de aceite binário por entregável
- [ ] Condições comerciais com modelo por marcos, penalidades e garantia
- [ ] Artefato Obrigatório (10 grupos, 41 itens) transcrito integralmente com OK/NOK/Observações
- [ ] Processo de submissão com prazo, canal, formato e contatos definidos

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Escopo incluso sem referência aos IDs de RF da ERF
2. Ausência de escopo excluso ou escopo excluso com menos de 3 exclusões explícitas
3. Artefato Obrigatório incompleto — algum dos 10 grupos ou 41 itens ausente
4. Condições comerciais sem modelo de faturamento por marcos definido
5. Processo de submissão sem prazo final e canal de envio definidos
