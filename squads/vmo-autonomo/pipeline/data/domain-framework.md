# Domain Framework — VMO Autônomo
# Ciclo de Vida de Iniciação de Projetos: da Demanda à Documentação Completa

---

## Fase 1: Captação de Demanda

**Objetivo:** Coletar e consolidar todas as informações disponíveis sobre a necessidade do solicitante.

### Processo

1. **Leitura de fontes disponíveis**
   - E-mails relacionados à demanda
   - Atas de reunião e transcrições
   - Documentos de briefing ou apresentações
   - Formulários de solicitação
   - Mensagens de Teams/Slack

2. **Extração de dados estruturados**
   - Solicitante (nome, cargo, área)
   - Descrição da necessidade
   - Benefício esperado
   - Urgência e prazo desejado
   - Contexto organizacional

3. **Normalização e estruturação**
   - Organizar dados em formato padronizado
   - Identificar lacunas de informação
   - Formular perguntas de esclarecimento se necessário

---

## Fase 2: Qualificação da Demanda

**Objetivo:** Determinar se a demanda deve ser transformada em projeto.

### Critérios de Qualificação

| Critério | Peso | Descrição |
|---|---|---|
| Alinhamento estratégico | Alto | Está alinhado com objetivos da organização? |
| Viabilidade técnica | Alto | É tecnicamente realizável com os recursos disponíveis? |
| Retorno sobre investimento | Alto | O benefício justifica o investimento? |
| Urgência | Médio | Qual é o impacto de não fazer? |
| Maturidade da demanda | Médio | A necessidade está suficientemente definida? |
| Disponibilidade de recursos | Médio | Há equipe e orçamento disponíveis? |

### Resultado da Qualificação
- **APROVADO COMO PROJETO**: Seguir para iniciação
- **APROVADO COMO TAREFA**: Demanda pequena, não requer projeto formal
- **REPROVADO**: Não atende critérios mínimos
- **EM ESPERA**: Aguardar mais informações ou momento adequado

---

## Fase 3: Documentação de Iniciação

**Objetivo:** Criar toda a documentação necessária para autorizar e iniciar o projeto.

### Sequência de Documentos

```
TAP (Termo de Abertura)
    ↓
PM Canvas (visão em 9 blocos)
    ↓
ERF (Especificação de Requisitos Funcionais)
    ↓
WBS (Estrutura Analítica do Projeto)
    ↓
Cronograma Detalhado
    ↓
Plano de Riscos
    ↓
Framework de KPIs
    ↓
Status Report Inicial
```

---

## Fase 4: Revisão e Aprovação

**Objetivo:** Garantir qualidade e completude de todos os documentos antes da aprovação formal.

### Checklist de Aprovação

**TAP aprovado se:**
- Tem objetivo SMART
- Sponsor identificado e com autoridade
- Escopo delimitado (dentro/fora)
- Orçamento e prazo aprovados

**PM Canvas aprovado se:**
- Todos os 9 blocos preenchidos
- Consistência entre blocos verificada
- Stakeholders mapeados

**Plano Geral aprovado se:**
- Todos os 10 planos subsidiários endereçados
- Abordagem metodológica definida
- Critérios de sucesso mensuráveis

**ERF aprovada se:**
- Requisitos priorizados (MoSCoW)
- Critérios de aceitação definidos
- Rastreabilidade documentada

**Cronograma aprovado se:**
- WBS com pelo menos 3 níveis
- Marcos principais identificados
- Dependências documentadas
- Caminho crítico estimado

**Plano de Riscos aprovado se:**
- Mínimo 5 riscos identificados
- Todos com probabilidade e impacto avaliados
- Estratégia de resposta para cada risco
- Responsável e prazo definidos

---

## Ciclo de Monitoramento (Execução)

**Frequência recomendada:**
- **Daily/Semanal:** Atualização de progresso, issues abertas
- **Quinzenal:** Status Report formal com EVM
- **Mensal:** Revisão de riscos e atualização de plano
- **Por Fase/Marco:** Pesquisa de satisfação do cliente

### Semáforo de Saúde do Projeto

| Indicador | Verde | Amarelo | Vermelho |
|---|---|---|---|
| Cronograma (SPI) | ≥ 0,95 | 0,85–0,95 | < 0,85 |
| Custo (CPI) | ≥ 0,95 | 0,85–0,95 | < 0,85 |
| Escopo | Sem mudanças | 1–2 mudanças | > 2 mudanças |
| Riscos | Sob controle | 1 risco alto | > 1 risco crítico |
| Satisfação cliente | ≥ 8/10 | 6–7/10 | < 6/10 |

---

## Entregáveis por Fase

| Fase | Agente | Entregável | Formato |
|---|---|---|---|
| Captação | Iara Inbound | demanda-coletada.md | Markdown |
| Qualificação | Felipe Filtro | qualificacao.md | Markdown |
| Documentação | Diana Documento | tap.md, pm-canvas.md, plano-geral.md | Markdown |
| Requisitos | Rafael Requisito | erf.md | Markdown |
| Cronograma | Carlos Cronograma | wbs.md, cronograma.md | Markdown |
| Riscos | Pedro Perigo | plano-riscos.md, risk-register.md | Markdown |
| KPIs | Marcela Métrica | kpis.md | Markdown |
| Reports | Sara Status | status-report.md, pesquisa-satisfacao.md | Markdown |
| Revisão | Vera Veredito | revisao-final.md | Markdown |
