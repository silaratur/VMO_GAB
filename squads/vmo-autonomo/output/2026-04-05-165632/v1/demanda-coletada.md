# Demanda Estruturada — Inclusão de Aprovador em Lançamentos Pré-Editados SAP FI
**ID Demanda:** DEM-2026-002
**Data de Coleta:** 2026-04-05
**Canal:** Documento PDF — Requisição formal via sistema de gestão de demandas DTI
**Run ID:** 2026-04-05-165632
**Coletado por:** Iara Inbound (VMO Autônomo)

---

## 1. Inventário de Materiais

| # | Arquivo / Fonte | Tipo | Data |
|---|---|---|---|
| 1 | `Requisição - os lançamentos pré editado - SAP FI novo.pdf` | Requisição formal DTI (formulário estruturado) | 23/02/2026 (última ação: 23/02/2026 08:26) |

**Observação:** Apenas um material foi disponibilizado. Não há documentação de processo, especificação técnica, histórico de aprovações ou comunicado complementar anexado.

---

## 2. Solicitante e Contexto Organizational

**Solicitante:** Ivanilde Ribeiro Machado — Cargo não especificado — VIX Manutenção (grupo não especificado)
**Beneficiado:** Ivanilde Ribeiro Machado — VIX Manutenção
**Área solicitante:** VIX Manutenção (divisão/grupo interno não especificado)
**Data da solicitação:** 23/02/2026 (data da última ação no sistema)
**Encaminhamento registrado:** Direcionar Requisição — 1° Nível — Corporativo — 23/02/2026 08:26

**Contexto/motivação:** A motivação de negócio não foi explicitada pelo solicitante. A requisição não descreve qual evento ou pressão operacional gerou a necessidade de um aprovador adicional. Não há referência a auditoria, falha de controle, mudança regulatória, reestruturação de alçadas ou incidente recente. Esta lacuna impede inferir urgência ou prioridade com segurança.

---

## 3. Necessidade de Negócio

O processo atual de aprovação de lançamentos pré-editados no módulo FI do SAP possui uma configuração de alçadas que, segundo o solicitante, necessita de reforço. A necessidade de negócio inferida — com ressalva de que não foi declarada explicitamente — é **garantir maior controle ou segregação de função no fluxo de aprovação de lançamentos contábeis pré-editados**, possivelmente para mitigar risco operacional, atender a requisito interno de controle interno ou responder a recomendação de auditoria.

**Importante:** Esta inferência está marcada como premissa assumida (ver Seção 6). A necessidade de negócio real deve ser confirmada com o solicitante.

---

## 4. Pedido Específico

Inserção de um aprovador adicional no fluxo de aprovação de lançamentos pré-editados realizados no SAP módulo FI, utilizando:
- **Transação de configuração do padrão de aprovadores:** ZFI0057
- **Transação utilizada na aprovação (workflow de caixa de entrada):** SBWP

O pedido é de natureza **configuracional no SAP** — não envolve desenvolvimento de novo código, mas sim parametrização de workflow existente na transação ZFI0057.

---

## 5. Classificação da Demanda

| Campo | Resposta Declarada |
|---|---|
| Necessidade para atendimento a requisito Legal ou Obrigatório? | Não |
| Solução já existe no mercado? | Não |
| Projeto semelhante já implantado no ambiente GAB? | Não |
| Esse projeto envolve ou impacta outras áreas de negócio? | Não |
| Esse projeto envolve ou impacta outras divisões de negócio? | Não |
| Requer Integração com outros sistemas? | Não |
| Área de negócio possui escopo detalhado da solução? | Não |
| Qual expectativa de investimento? | Menor de R$ 10.000,00 |
| Possui investimento aprovado? | Não |
| Se a demanda for urgente, justifique o motivo | Não informado |
| Processo envolvido está documentado? | Não |
| Informe o Centro de Custo ou Imobilizado | Não informado |
| Aumento de receita? | Não |
| Redução de custo? | Não |
| Melhoria de processo? | Não |
| Aumento de produtividade? | Não |
| Ganhos previstos (quantitativos e qualitativos) | Não informado |
| Indicador para medir ganhos e benefícios | Não informado |

**Observação crítica:** Todos os campos de ganhos e benefícios foram declarados como "Não" ou deixados em branco. Isso é inconsistente com a existência de uma demanda: se não há ganho previsto em nenhuma dimensão, a justificativa para execução do projeto precisa ser explicitada de outra forma (ex.: controle interno, requisito de auditoria, determinação de gestão).

---

## 6. Restrições e Premissas

**Restrições conhecidas:**
- Investimento declarado como inferior a R$ 10.000,00 — restrição orçamentária aplicável
- Investimento ainda **não aprovado** — execução não pode ser iniciada sem aprovação formal
- Processo envolvido **não está documentado** — risco de escopo mal definido durante implantação
- Escopo detalhado da solução **não existe** — DTI precisará construir o escopo antes de estimar esforço

**Premissas assumidas (não confirmadas pelo solicitante):**
- Premissa 1: A transação ZFI0057 é um desenvolvimento customizado (prefixo Z) existente no ambiente SAP da organização e já funcional — não há garantia explícita disso no material
- Premissa 2: A necessidade é de adicionar exatamente um aprovador (conforme texto: "mais um aprovador") — o perfil, alçada e posição desse aprovador no fluxo não foram especificados
- Premissa 3: O fluxo de aprovação via SBWP (SAP Business Workplace) já está ativo e operacional para este tipo de lançamento
- Premissa 4: A demanda não requer homologação em ambiente separado antes da produção — não mencionado
- Premissa 5: A necessidade de negócio subjacente é de controle interno ou segregação de funções — inferência sem confirmação

---

## 7. Lacunas de Informação

| # | Campo | Status | Ação Requerida |
|---|---|---|---|
| L01 | Cargo do solicitante | Não informado | Confirmar cargo/função de Ivanilde Ribeiro Machado para validar autoridade de solicitação |
| L02 | Grupo interno dentro de VIX Manutenção | Não informado | Identificar célula ou grupo específico dentro de VIX Manutenção para rastreabilidade |
| L03 | Motivação/pressão de negócio | Não informado | Perguntar ao solicitante: "O que motivou esta necessidade agora? Houve auditoria, incidente, reestruturação de alçadas ou determinação de gestão?" |
| L04 | Identidade do novo aprovador | Não informado | Perguntar: "Qual o nome, matrícula e cargo do aprovador a ser incluído?" |
| L05 | Posição do novo aprovador no fluxo | Não informado | Perguntar: "O novo aprovador deve ser inserido antes ou depois dos aprovadores existentes? Em qual etapa do workflow?" |
| L06 | Perfil/alçada do novo aprovador | Não informado | Perguntar: "Qual tipo de lançamento e qual faixa de valor o novo aprovador deverá cobrir?" |
| L07 | Centro de Custo ou Imobilizado | Não informado | Solicitar ao solicitante o centro de custo para imputação do projeto |
| L08 | Urgência e prazo desejado | Não informado | Campo de urgência em branco — perguntar: "Há uma data de necessidade ou evento que determina prazo de implantação?" (não aceitar "o quanto antes" como resposta) |
| L09 | Ganhos e benefícios esperados | Não informado | Perguntar: "Quais são os benefícios esperados com a inclusão do aprovador? Redução de risco, atendimento a controle interno, recomendação de auditoria?" |
| L10 | Indicador de sucesso | Não informado | Perguntar: "Como será medido o sucesso desta implantação?" |
| L11 | Aprovadores já existentes no fluxo | Não informado | Levantar com a equipe técnica SAP quais aprovadores estão configurados hoje na ZFI0057 para os lançamentos pré-editados de FI |
| L12 | Ambiente de homologação | Não informado | Confirmar com a equipe técnica se existe ambiente de homologação/qualidade para teste antes da produção |
| L13 | Aprovação do investimento | Declarado como "Não aprovado" | Identificar quem é o aprovador do orçamento e qual o processo para aprovação antes do início do projeto |
| L14 | Data exata da solicitação original | Não informado | O campo de data da requisição original não está presente — apenas a data da última ação (23/02/2026) é conhecida |

---

## 8. Avaliação Preliminar de Complexidade

**Classificação: BAIXA — com ressalva**

**Justificativa:**
- O pedido é de parametrização em transação SAP já existente (ZFI0057), sem desenvolvimento de nova funcionalidade
- Não há integrações com outros sistemas declaradas
- Não impacta outras áreas ou divisões (conforme declarado)
- Estimativa de investimento abaixo de R$ 10.000,00

**Ressalva:** A complexidade pode ser reclassificada para MÉDIA caso:
- A transação ZFI0057 exija ajuste de código ABAP além de parametrização
- O fluxo de aprovação existente não esteja documentado e exija análise prévia de mapeamento
- A aprovação do investimento gere dependências com ciclo orçamentário
- Houver necessidade de testes em ambiente de homologação com regressão do processo

A ausência de documentação do processo (declarado explicitamente no formulário) é o principal fator de risco de subestimação de esforço.

---

## 9. Resumo de Confirmação (para o Solicitante)

Prezada Ivanilde,

Recebemos sua requisição datada de 23/02/2026, referente à inclusão de um aprovador adicional no fluxo de lançamentos pré-editados no SAP FI, com configuração via transação ZFI0057 e aprovação pelo usuário via SBWP. Registramos a demanda sob o ID **DEM-2026-002**.

Para que possamos avançar com a qualificação e estimativa de esforço, precisamos esclarecer alguns pontos essenciais que não constaram na requisição original: (1) a motivação de negócio que originou esta necessidade; (2) a identificação completa do novo aprovador a ser incluído e sua posição no fluxo de aprovação; (3) o Centro de Custo para imputação do projeto; (4) a data ou prazo de necessidade de implantação; e (5) os ganhos ou benefícios esperados com esta mudança. Além disso, o investimento ainda consta como não aprovado — será necessário que a aprovação orçamentária ocorra antes do início de qualquer execução.

Entraremos em contato para coletar as informações pendentes listadas acima antes de encaminhar a demanda para a etapa de qualificação.

Atenciosamente,
Iara Inbound — VMO Autônomo | DTI

---

## 10. Próximos Passos

- Validar lacunas com solicitante (seção 7) — responsável: Iara Inbound / gestor da demanda
- Obter aprovação do investimento antes de qualquer avanço (L13)
- Encaminhar para qualificação técnica (Felipe Filtro) somente após resolução das lacunas críticas: L03, L04, L05, L07, L08
- Solicitar à equipe técnica SAP levantamento do estado atual da ZFI0057 (L11) em paralelo
