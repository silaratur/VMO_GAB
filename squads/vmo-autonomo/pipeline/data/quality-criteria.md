# Quality Criteria — VMO Autônomo
# Critérios de Qualidade para Documentação de Projetos PMO/VMO

---

## Critérios Gerais (aplicam a todos os documentos)

- [ ] Documento tem título, data de criação e versão
- [ ] Solicitante e responsável identificados
- [ ] Linguagem clara, objetiva e em português formal
- [ ] Nenhuma seção obrigatória deixada em branco
- [ ] Consistência entre documentos (mesmos valores de prazo, custo, escopo)
- [ ] Não usa jargão sem definição prévia
- [ ] Aprovado pelo revisor antes de avançar

---

## Termo de Abertura do Projeto (TAP)

### Critérios Obrigatórios (BLOCKING)
- [ ] **Objetivo SMART**: Específico, Mensurável, Atingível, Relevante, Temporal
- [ ] **Sponsor identificado** com nome, cargo e nível de autoridade
- [ ] **Gerente de Projeto** designado com nível de autoridade documentado
- [ ] **Escopo delimitado**: lista de "dentro do escopo" e "fora do escopo"
- [ ] **Critérios de sucesso** mensuráveis (mínimo 3)
- [ ] **Orçamento aprovado** (mesmo que estimado, com faixa de variação)
- [ ] **Prazo de conclusão** definido com marco final

### Critérios de Qualidade
- [ ] Justificativa do projeto liga à estratégia organizacional
- [ ] Partes interessadas principais mapeadas (mínimo 5)
- [ ] Premissas e restrições listadas (mínimo 3 de cada)
- [ ] Riscos de alto nível identificados (mínimo 3)
- [ ] Benefícios esperados quantificados onde possível

---

## PM Canvas

### Critérios Obrigatórios (BLOCKING)
- [ ] **Todos os 9 blocos preenchidos** sem exceção
- [ ] **Consistência interna**: valores de prazo/custo/escopo batem entre blocos
- [ ] **Bloco "Por quê?"** conecta diretamente à estratégia organizacional

### Critérios de Qualidade
- [ ] Visual organizado e legível em formato de canvas
- [ ] Stakeholders do bloco "Quem?" coincidem com TAP
- [ ] Riscos do bloco "Riscos" antecipam o plano de riscos
- [ ] Premissas e restrições coerentes com TAP

---

## Especificação de Requisitos Funcionais (ERF)

### Critérios Obrigatórios (BLOCKING)
- [ ] **Requisitos priorizados** usando MoSCoW (Must/Should/Could/Won't)
- [ ] **Critério de aceitação** definido para cada requisito Must
- [ ] **ID único** para cada requisito (RF001, RNF001...)
- [ ] **Rastreabilidade**: cada requisito tem origem documentada

### Critérios de Qualidade
- [ ] Requisitos escritos na voz do usuário ("O sistema deve...")
- [ ] Nenhum requisito ambíguo (evitar "rápido", "fácil", "eficiente")
- [ ] Requisitos não-funcionais endereçados (performance, segurança, disponibilidade)
- [ ] Glossário de termos técnicos incluído

---

## WBS + Cronograma

### Critérios Obrigatórios (BLOCKING)
- [ ] **WBS com mínimo 3 níveis** de decomposição
- [ ] **Pacotes de trabalho** no último nível têm duração ≤ 2 semanas
- [ ] **Marcos principais** identificados (mínimo: início, meio, fim)
- [ ] **Dependências** documentadas entre atividades críticas
- [ ] **Caminho crítico** identificado

### Critérios de Qualidade
- [ ] 100% dos entregáveis do escopo cobertos na WBS
- [ ] Responsável designado por pacote de trabalho
- [ ] Baseline de prazo definida
- [ ] Buffer/reserva de contingência incluída

---

## Plano de Riscos

### Critérios Obrigatórios (BLOCKING)
- [ ] **Mínimo 5 riscos** identificados e documentados
- [ ] **Probabilidade e impacto** avaliados para cada risco (escala 1-5 ou H/M/L)
- [ ] **Estratégia de resposta** definida para cada risco
- [ ] **Responsável e prazo** por ação de resposta

### Critérios de Qualidade
- [ ] Riscos cobrem ao menos 4 categorias (técnico, financeiro, prazo, stakeholders)
- [ ] Riscos críticos (alta prob × alto impacto) têm plano de contingência
- [ ] Trigger (gatilho) de acionamento definido para cada risco crítico
- [ ] Reserva de contingência estimada e documentada

---

## KPIs e Performance

### Critérios Obrigatórios (BLOCKING)
- [ ] **CPI e SPI** definidos e baseline estabelecida
- [ ] **Frequência de medição** definida para cada KPI
- [ ] **Limites de alerta** (amarelo/vermelho) definidos para cada KPI
- [ ] **Responsável** pela coleta e reporte de cada KPI

### Critérios de Qualidade
- [ ] KPIs cobrem ao menos: prazo, custo, escopo, qualidade e satisfação
- [ ] KPIs vinculados aos critérios de sucesso do TAP
- [ ] Dashboard de saúde inclui semáforo visual

---

## Status Report

### Critérios Obrigatórios (BLOCKING)
- [ ] **Status geral** (semáforo: verde/amarelo/vermelho) presente
- [ ] **Data do report** e **período coberto** explícitos
- [ ] **Progresso** em percentual e comparado ao baseline
- [ ] **Issues abertas** com responsável e prazo de resolução

### Critérios de Qualidade
- [ ] Executivo pode ler apenas o resumo e ter visão completa
- [ ] Ações definidas são SMART (específicas, com responsável e prazo)
- [ ] Desvios do plano são explicados (não apenas reportados)
- [ ] Próximos passos claros para o período seguinte

---

## Pontuação Consolidada (Revisor)

| Documento | Peso | Mínimo p/ Aprovação |
|---|---|---|
| TAP | 25% | 7/10 (todos obrigatórios atendidos) |
| PM Canvas | 10% | 7/10 |
| ERF | 15% | 7/10 (todos obrigatórios atendidos) |
| WBS + Cronograma | 20% | 7/10 (todos obrigatórios atendidos) |
| Plano de Riscos | 15% | 7/10 (todos obrigatórios atendidos) |
| KPIs | 10% | 7/10 |
| Status Report | 5% | 7/10 |

**Aprovação global:** Pontuação ponderada ≥ 7,0 E nenhum critério BLOCKING não atendido.
