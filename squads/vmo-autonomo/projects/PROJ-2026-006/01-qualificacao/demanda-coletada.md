# Demanda Coletada
Data da Coleta: 2026-05-16
Coletado por: Iara Inbound

---

## Fontes Consultadas

| # | Tipo | Identificador | Data | Participantes | Confiabilidade |
|---|------|---------------|------|---------------|----------------|
| F1 | Reunião gravada (Fireflies) | ID: 01KPV48BER47DVPT37Q0CGCNXN — "Discovery Demandas - Sara <> JADSON" | 22/04/2026 | Jadson (Solicitante), Sara (Coletora — Agente VMO) | Alta — fala direta do solicitante |
| F2 | Arquivo pré-processado | `squads/vmo-autonomo/output/materiais-demanda.md` | 2026-05-16 | Extração automatizada da reunião F1 | Média — derivado de F1, sem fonte primária independente |

---

## Dados da Demanda

| Campo | Valor Coletado | Fonte |
|-------|----------------|-------|
| **Solicitante** | Jadson | F1 — abertura da reunião |
| **Cargo/Área** | Gestor da Área de Inovação | F1 — identificação inicial |
| **Canal de coleta** | Reunião de discovery gravada | F1 — metadado da gravação |
| **Tipo de demanda** | Melhoria — substituição de plataforma terceira por solução própria | F1 — *"sai um sistema terceiro e entra um software próprio"* |
| **Pedido técnico** | Desenvolver plataforma web própria de gestão de ideias e inovação | F1 — descrição do solicitante |
| **Necessidade de negócio** | Reduzir custo de licenciamento (~R$80-90k/ano) e eliminar restrições de escala e customização impostas pela solução SaaS atual | F1 — *"Eu entendo que a solução atual é cara pelo que ela entrega. A meu ver, a gente pode fazer mais com menos"* |
| **Problema atual** | Plataforma SaaS terceira com custo elevado (~R$80-90k/ano), limitação de licenças por usuário e pouca aderência às particularidades do grupo | F1 — *"essa plataforma hoje custa algum dinheiro [...] se eu expandir para todos os funcionários do grupo, ela fica muito cara"* |
| **Solução atual** | Plataforma SaaS terceira (nome não informado pelo solicitante) | F1 — mencionada sem identificar o fornecedor |
| **Divisões impactadas** | Todas as divisões do grupo (usuários finais); Área de Inovação (gestora da plataforma) | F1 — *"ela já é usada pelo grupo, as outras divisões [...] a ideia é que elas continuem utilizando"* |
| **Requisito legal** | Nenhum | F1 — *"Não, nenhum requisito legal ou obrigatório, não"* |
| **Integração com outros sistemas** | Nenhuma no escopo inicial | F1 — *"A princípio não, pelo menos nesse primeiro momento não há necessidade de integração"* |
| **Orçamento aprovado** | Não — necessário levantar custos antes de aprovação formal | F1 — *"Não existe orçamento aprovado. A minha ideia é que a gente consiga levantar os custos primeiro"* |
| **Expectativa de investimento** | ~R$80-90k (equivalente ao custo anual da licença atual) com payback em 1 ano | F1 — *"minha expectativa é que a gente consiga desenvolver uma solução usando por volta desse valor"* |
| **Prazo desejado** | Dezembro de 2026 | F1 — *"até dezembro desse ano a gente tenha isso pronto"* |
| **Marco vinculado ao prazo** | Prêmio Inovação — lançamento previsto para janeiro de 2027 | F1 — *"ao lançamento do Prêmio Inovação [...] em janeiro de 27, já consiga utilizar essa nova solução"* |
| **Sponsor executivo** | Não identificado explicitamente na reunião | F1 — lacuna |
| **Time de desenvolvimento** | Não definido (interno, externo ou misto) | F1 — lacuna |
| **Infraestrutura/hospedagem** | Não mencionada | F1 — lacuna |
| **Número de usuários** | Não informado quantitativamente | F1 — lacuna |

### Funcionalidades mencionadas pelo Solicitante

| # | Funcionalidade | Descrição extraída | Fonte |
|---|----------------|--------------------|-------|
| F01 | Cadastro de ideias avulsas | Colaborador submete ideia descrevendo problema que resolve, ganhos e benefícios | F1 — *"cadastrar a sua ideia, qual o problema que ela resolve, quais os ganhos, benefícios e afins"* |
| F02 | Campanhas e desafios | Gestor de inovação publica desafios específicos; colaboradores submetem respostas | F1 — *"o time de inovação é o gestor dessa plataforma. Ele pode colocar desafios específicos, problemas específicos, campanha"* |
| F03 | Fluxo de aprovação | Ideia passa por aprovação do gestor da área e dos envolvidos identificados | F1 — *"essa ideia depois passa por um fluxo de aprovação, o gestor da área, os envolvidos ali"* |
| F04 | Mini gestão de projetos | Ideia aprovada recebe plano de ação macro e mensuração de ganhos | F1 — *"um módulo [...] que contemple uma mini gestão de projetos [...] pelo menos um nível de planejamento da implementação"* |
| F05 | Monitoramento de projetos | Dashboard de acompanhamento de projetos de inovação em andamento | F1 — *"a gente consegue monitorar todos os projetos de inovação que estão em andamento"* |

---

## Lacunas Identificadas

| # | Lacuna | Impacto | Ação requerida |
|---|--------|---------|----------------|
| L01 | **Sponsor executivo** — nenhum sponsor formal de nível diretoria/VP identificado | Alto — sem sponsor, aprovação de orçamento e prioridade institucional ficam sem respaldo | Perguntar a Jadson quem é o responsável executivo que autoriza o investimento |
| L02 | **Orçamento** — não aprovado; depende de levantamento de custos a ser realizado pelo VMO | Alto — sem orçamento aprovado, o projeto não pode ser formalmente iniciado | Definir processo e prazo para levantamento e aprovação do investimento |
| L03 | **Identificação da plataforma atual** — nome do fornecedor SaaS atual não informado | Médio — dificulta análise comparativa de funcionalidades e benchmarking de custo | Solicitar nome da plataforma atual a Jadson |
| L04 | **Número de usuários** — quantidade atual de licenças e projeção de usuários na nova plataforma não informadas | Médio — impacta escopo de infraestrutura e estimativa de custo de desenvolvimento | Solicitar dados de usuários ativos e projeção de expansão |
| L05 | **Atributos do cadastro de ideia** — campos exatos além dos mencionados (problema, ganhos, benefícios) não detalhados | Médio — necessário para levantamento completo de requisitos funcionais | Mapear formulário atual da plataforma como referência |
| L06 | **Critérios e etapas do fluxo de aprovação** — quem aprova, quantas etapas, critérios objetivos de aprovação/rejeição | Médio — sem isso, o módulo de fluxo não pode ser especificado | Conduzir sessão de mapeamento de processo com Jadson |
| L07 | **Infraestrutura e hospedagem** — onde a plataforma será hospedada (cloud, data center do grupo, misto) | Médio — define arquitetura e custo de operação | Perguntar sobre política de TI do grupo para hospedagem de sistemas próprios |
| L08 | **Time de desenvolvimento** — se o desenvolvimento será interno, fornecedor externo ou misto | Médio — define modelo de contratação e impacto no orçamento | Perguntar a Jadson e confirmar se há fornecedores preferências ou contratos já em vigor |
| L09 | **Critérios de sucesso mensuráveis** — como Jadson medirá se a plataforma foi bem-sucedida além do prazo e custo | Baixo | Incluir na próxima reunião de qualificação |

---

---

# Demanda Estruturada — Plataforma Própria de Gestão de Ideias e Inovação
Versão: 1.0
Data: 2026-05-16

## Identificação

| Campo | Valor |
|-------|-------|
| **ID Demanda** | DEM-2026-006 |
| **ID Projeto** | PROJ-2026-006 |
| **Nome Preliminar** | Plataforma Própria de Gestão de Ideias e Inovação |
| **Data de Coleta** | 2026-05-16 |
| **Data da Reunião de Origem** | 22/04/2026 |
| **Coletado por** | Iara Inbound (Agente VMO) |
| **Fonte primária** | Reunião gravada — Fireflies ID: 01KPV48BER47DVPT37Q0CGCNXN |

---

## Solicitante

| Campo | Valor |
|-------|-------|
| **Nome** | Jadson |
| **Cargo** | Gestor da Área de Inovação |
| **Grupo/Empresa** | Grupo (divisões: Comércio, Passageiros, Logística) |
| **Sponsor executivo** | Não identificado — Lacuna L01 |

---

## Classificação da Demanda

| Campo | Valor |
|-------|-------|
| **Tipo** | Melhoria |
| **Natureza** | Substituição de solução terceira por plataforma própria |
| **Complexidade estimada** | Alta — desenvolvimento de software do zero com múltiplos módulos |
| **Requisito legal** | Nenhum |
| **Urgência** | Alta — prazo vinculado a evento institucional (Prêmio Inovação, jan/2027) |

---

## Necessidade de Negócio

A área de Inovação do grupo utiliza uma plataforma SaaS terceira para gestão de ideias e iniciativas de colaboradores, com custo anual de R$80-90 mil. A solução atual impõe limitações de escala (custo por licença por usuário) e flexibilidade (baixa customização às particularidades do grupo), impedindo a expansão do programa de inovação para todos os colaboradores de forma economicamente viável.

**Premissa central:** O grupo já possui maturidade no processo de inovação e entende que é possível obter funcionalidade equivalente — ou superior — com custo menor, por meio de desenvolvimento próprio.

---

## Pedido Técnico

Desenvolver uma plataforma web própria que substitua a solução SaaS atual, contemplando os módulos de: cadastro de ideias, campanhas e desafios, fluxo de aprovação, mini gestão de projetos e monitoramento de resultados.

> **Distinção importante:** O pedido técnico (desenvolver software) é o meio. A necessidade de negócio (reduzir custo e ganhar escala/flexibilidade no programa de inovação) é o fim. A validação do projeto deve sempre verificar se o meio escolhido é o mais adequado para atingir o fim.

---

## Escopo Funcional Preliminar

| Módulo | Descrição | Status |
|--------|-----------|--------|
| Cadastro de ideias | Formulário de submissão com campos: problema, ganhos, benefícios e outros (ver L05) | Confirmado pelo solicitante |
| Campanhas e desafios | Publicação de desafios pela equipe de inovação; colaboradores respondem com ideias | Confirmado pelo solicitante |
| Fluxo de aprovação | Aprovação por gestor da área e partes interessadas; aprovação de ideia e de investimento | Confirmado — detalhes pendentes (L06) |
| Mini gestão de projetos | Plano de ação macro para implementação de ideias aprovadas | Confirmado pelo solicitante |
| Mensuração de ganhos | Acompanhamento dos resultados das ideias implementadas | Confirmado pelo solicitante |
| Dashboard de monitoramento | Visibilidade de projetos de inovação em andamento | Confirmado pelo solicitante |

**Fora do escopo (versão inicial):** Integrações com outros sistemas do grupo.

---

## Restrições

| # | Restrição | Origem |
|---|-----------|--------|
| R01 | Prazo de entrega: dezembro de 2026 | Solicitante — F1 |
| R02 | Orçamento-referência: ~R$80-90k (a ser validado no levantamento formal) | Solicitante — F1 |
| R03 | Transição transparente para usuários das demais divisões — impacto mínimo visível | Solicitante — F1 |
| R04 | Nenhuma integração com sistemas externos no escopo inicial | Solicitante — F1 |

---

## Premissas

| # | Premissa | Origem |
|---|----------|--------|
| P01 | O grupo possui infraestrutura ou capacidade de contratar hospedagem para a nova plataforma | Inferida — a confirmar (L07) |
| P02 | Haverá recursos de desenvolvimento disponíveis (internos ou externos) dentro do prazo e orçamento | Inferida — a confirmar (L08) |
| P03 | O processo de inovação atual está documentado ou pode ser mapeado rapidamente | Inferida da maturidade relatada pelo solicitante |
| P04 | Os usuários das demais divisões não precisarão ser re-treinados extensivamente na nova plataforma | Solicitante — F1: *"o que deve mudar para o usuário final é basicamente o link que ele acessa"* |

---

## Cronograma e Orçamento

| Campo | Valor | Observação |
|-------|-------|------------|
| **Prazo desejado** | Dezembro de 2026 | Vinculado ao Prêmio Inovação (jan/2027) |
| **Orçamento aprovado** | Não | Necessita levantamento formal de custos |
| **Expectativa do solicitante** | ~R$80-90k total de desenvolvimento | Baseado no custo anual da licença atual |
| **Expectativa de ROI** | Payback em 1 ano | Solicitante — F1 |
| **Custo atual a substituir** | R$80-90k/ano em licença SaaS | Solicitante — F1 |

---

## Impactos e Partes Interessadas

| Parte Interessada | Papel | Impacto |
|-------------------|-------|---------|
| Jadson (Inovação) | Solicitante / Gestor da plataforma | Direto — responsável pela plataforma |
| Colaboradores do grupo (todas as divisões) | Usuários finais | Direto — submissão e acompanhamento de ideias |
| Gestores de área | Aprovadores no fluxo | Direto — participam do processo de aprovação |
| Área de Tecnologia do grupo | Potencial executor ou suporte técnico | A confirmar — mencionado como possível executor de ideias aprovadas |
| Sponsor executivo | Aprovador do investimento | Não identificado — Lacuna L01 |

---

## Lacunas Críticas para Avanço

As lacunas abaixo devem ser resolvidas antes da qualificação formal e aprovação do projeto:

| Prioridade | Lacuna | Responsável pela resposta |
|------------|--------|--------------------------|
| Alta | L01 — Sponsor executivo não identificado | Jadson |
| Alta | L02 — Orçamento não aprovado | Jadson / Sponsor |
| Média | L03 — Nome da plataforma SaaS atual | Jadson |
| Média | L04 — Número de usuários atuais e projetados | Jadson |
| Média | L06 — Detalhamento do fluxo de aprovação | Jadson |
| Média | L07 — Definição de infraestrutura/hospedagem | Jadson / TI do grupo |
| Média | L08 — Modelo de desenvolvimento (interno/externo) | Jadson / Sponsor |

---

## Resumo para Confirmação pelo Solicitante

> "Jadson, registramos sua demanda da seguinte forma: **você quer construir uma plataforma própria do grupo para substituir a ferramenta que vocês usam hoje para gerenciar as ideias de inovação dos colaboradores**. A principal razão é que a solução atual custa entre R$80 e R$90 mil por ano e tem um limite de usuários que impede expandir o programa para todos os colaboradores. Com uma plataforma própria, vocês ganham flexibilidade para personalizar conforme as necessidades do grupo e eliminam esse custo recorrente de licença.
>
> A nova plataforma precisa permitir que qualquer colaborador registre uma ideia, que a equipe de inovação publique desafios para receber propostas, que as ideias passem por um processo de aprovação interno, e que as ideias aprovadas virem pequenos projetos acompanhados dentro da própria plataforma.
>
> O prazo que você colocou é dezembro de 2026, porque em janeiro de 2027 acontece o Prêmio Inovação e você quer que o grupo já esteja usando a plataforma nova nesse momento. O orçamento ainda não está aprovado — a proposta é que o VMO levante os custos de desenvolvimento primeiro.
>
> **Está correto esse entendimento?** Antes de avançarmos, precisamos de algumas informações complementares: quem seria o responsável executivo que vai aprovar o investimento, o nome da plataforma atual, e quantos colaboradores usam a ferramenta hoje."

---

*Documento gerado por Iara Inbound — Coletora de Demandas do VMO Autônomo*
*Próximo passo sugerido: encaminhar resumo ao solicitante Jadson para confirmação e resolução das lacunas prioritárias (L01, L02, L03, L04)*
