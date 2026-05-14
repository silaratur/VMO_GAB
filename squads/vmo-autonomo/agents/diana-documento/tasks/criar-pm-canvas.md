---
task: "Criar PM Canvas"
order: 2
input:
  - tap: "Termo de Abertura aprovado (output da tarefa anterior)"
output:
  - pm_canvas: "PM Canvas completo em formato de 9 blocos"
---

# Criar PM Canvas

Cria o PM Canvas do projeto — uma visualização estratégica em 9 blocos que sintetiza os elementos essenciais do projeto em uma única página. O PM Canvas complementa o TAP oferecendo uma visão integrada e escaneável ideal para apresentações executivas e alinhamento de equipe.

## Process

1. **Ler o TAP completo**: Extrair todos os dados necessários para os 9 blocos.
2. **Preencher os 9 blocos em sequência lógica**: Começar pelo "Por quê?" (justificativa) e "O quê?" (entregáveis), que são os blocos âncora dos demais.
3. **Verificar coerência entre blocos**: O bloco "Quando?" deve ter os mesmos marcos do TAP. O bloco "Quanto?" deve ter o mesmo orçamento.
4. **Garantir que os blocos "contem uma história"**: Lendo os 9 blocos em sequência, o projeto deve fazer sentido narrativamente.
5. **Formatar como canvas visual**: Usar tabela Markdown simulando a grade do PM Canvas.

## Output Format

```markdown
# PM CANVAS — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD

┌─────────────────────────────────────────────────────────────────┐
│                      PM CANVAS                                  │
├──────────────────┬──────────────────┬───────────────────────────┤
│  1. POR QUÊ?     │  2. O QUÊ?       │  3. QUEM?                 │
│  [justificativa] │  [entregáveis]   │  [equipe + stakeholders]  │
├──────────────────┼──────────────────┼───────────────────────────┤
│  4. COMO?        │  5. QUANDO?      │  6. QUANTO?               │
│  [metodologia]   │  [marcos/prazo]  │  [orçamento]              │
├──────────────────┼──────────────────┼───────────────────────────┤
│  7. PREMISSAS    │  8. RESTRIÇÕES   │  9. RISCOS                │
│  [premissas]     │  [restrições]    │  [riscos top 3]           │
└──────────────────┴──────────────────┴───────────────────────────┘
```

## Output Example

```markdown
# PM CANVAS — Sistema de Rastreamento de Fornecedores (SRF)
Versão: 1.0 | Data: 2026-04-15

┌────────────────────────────────────────────────────────────────────────────┐
│                         PM CANVAS — PROJETO SRF                            │
├──────────────────────┬─────────────────────────┬──────────────────────────┤
│  1. POR QUÊ?         │  2. O QUÊ?              │  3. QUEM?                │
│                      │                         │                          │
│ 3 rupturas de        │ • Dashboard tempo real  │ Sponsor: C. Mendes (TI)  │
│ fornecimento em Q1   │ • Alertas automáticos   │ Co-Sp.: A. Ferreira (SC) │
│ = R$ 135k de perdas  │   para atrasos > 2h     │ GP: A designar           │
│                      │ • Integração SAP MM     │ Equipe TI: 3-4 pessoas   │
│ OKR: -30% falhas     │ • Cobertura 12 Tier 1   │ Usuários: Supply Chain   │
│ de fornecimento      │ • Relatórios gerenciais │ Fornecedores: 12 Tier 1  │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│  4. COMO?            │  5. QUANDO?             │  6. QUANTO?              │
│                      │                         │                          │
│ Metodologia ágil     │ Início: 01/05/2026      │ Desenvolvimento: 180k    │
│ com sprints de 2     │ Req:    01/05–31/05      │ Infra cloud:      45k   │
│ semanas              │ Dev:    01/06–31/08      │ Licenças:          35k  │
│                      │ Testes: 01/09–30/09      │ Treinamento:       20k  │
│ Stack: GPS/IoT +     │ Go-live: 01/10/2026     │ Contingência:      56k  │
│ API SAP REST         │ Encerr: 31/12/2026      │ ─────────────────────── │
│                      │                         │ TOTAL: R$ 336.000        │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│  7. PREMISSAS        │  8. RESTRIÇÕES          │  9. RISCOS               │
│                      │                         │                          │
│ • SAP tem API REST   │ • Prazo: antes dez/2026 │ • Conflito recursos      │
│   disponível         │ • Orçamento: ≤ R$336k   │   com projeto SAP [ALTO] │
│ • Fornecedores têm   │ • Cloud-native obrig.   │ • Resistência            │
│   smartphone/IoT     │ • Dados no Brasil (LGPD)│   fornecedores [MÉDIO]  │
│ • TI disponível 60%  │ • Sem substituição SAP  │ • Complexidade API SAP  │
│   no Q2/2026         │ • Dados em tempo real   │   maior que estimada    │
│                      │   (≤ 15 min delay)      │   [MÉDIO]               │
└──────────────────────┴─────────────────────────┴──────────────────────────┘
```

## Quality Criteria

- [ ] Todos os 9 blocos preenchidos sem blocos vazios
- [ ] Valores de prazo, custo e orçamento idênticos ao TAP
- [ ] Bloco "Quem?" inclui sponsor, GP, equipe e usuários
- [ ] Bloco "Riscos" lista ao menos 3 riscos com classificação
- [ ] Canvas legível em formato tabular (Markdown)

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Qualquer bloco dos 9 está vazio ou preenchido apenas com "Ver TAP"
2. O prazo ou orçamento no Canvas contradiz os valores do TAP
