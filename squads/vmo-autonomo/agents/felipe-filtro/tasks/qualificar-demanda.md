---
task: "Qualificar Demanda"
order: 1
input:
  - demanda_estruturada: "Output do checkpoint de validação (demanda-validada.md)"
  - documentos_estrategicos: "OKRs ou objetivos organizacionais disponíveis"
output:
  - analise_qualificacao: "Avaliação dos 10 critérios (1-10 cada) com pontuação e justificativa"
  - classificacao: "PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA + time de sustentação ERP (se aplicável)"
  - decisao: "APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA"
  - proximos_passos: "Ações requeridas com responsável e prazo"
---

# Qualificar Demanda

Avalia se a demanda recebida deve ser transformada em projeto formal ou encaminhada como melhoria para o time de sustentação ERP. Aplica **10 critérios de qualificação** (pontuação 1–10 cada, máximo 100 pts) e emite uma **classificação** e um **parecer fundamentado** que habilita a decisão do GP ou do PMO.

O ponto central desta qualificação não é apenas decidir se a demanda "vale a pena" — é distinguir com precisão se ela requer **gestão de projeto formal** (pipeline VMO completo) ou se pode ser resolvida pelo **time de sustentação ERP** como melhoria. A classificação incorreta gera dois problemas igualmente prejudiciais: sobrecarregar o PMO com tarefas operacionais, ou subestimar projetos que precisam de governança formal.

---

## Process

1. **Carregar contexto estratégico**: Ler OKRs e objetivos organizacionais disponíveis para avaliar alinhamento.

2. **Avaliar os 10 critérios**: Para cada critério, atribuir pontuação de **1 a 10** com justificativa de ao menos 2 linhas baseada nos dados da demanda. Nunca atribuir pontuação por intuição — cada nota deve ser fundamentada com evidência da demanda.

3. **Calcular pontuação total**: Somar os 10 critérios (máximo 100) e calcular o percentual.

4. **Emitir a classificação** com base nos critérios 7–10 (complexidade):
   - **Projeto**: se ao menos 2 dos critérios 7–10 pontuarem ≥ 7/10 individualmente → a demanda exige gestão de projeto formal. Segue para o pipeline VMO completo.
   - **Melhoria Evolutiva**: pequeno ajuste funcional que não altera estrutura de processo, não exige integração significativa e pode ser resolvido autonomamente pelo time técnico.
   - **Melhoria Corretiva**: correção de erro ou comportamento inesperado do sistema. Independente da pontuação total, vai direto para sustentação.
   - Se for Melhoria, **indicar o time de Sustentação ERP responsável**:
     - **FI / CO / SD / Fiscal** — financeiro, contabilidade, vendas, fiscal
     - **PM / MM** — projetos, materiais, compras
     - **HCM** — recursos humanos, folha

5. **Emitir decisão** com base na pontuação total:
   - ≥ 75% (≥ 75 pts): **APROVADO**
   - 50–74% (50–74 pts) com condições resolvíveis: **APROVADO COM CONDIÇÕES**
   - < 50% (< 50 pts): **REPROVADO**
   - Informação insuficiente para avaliar: **EM ESPERA**

6. **Justificar tecnicamente** a classificação e o direcionamento. Evitar respostas genéricas, excessivamente longas ou muito técnicas.

7. **Definir próximos passos**: Para aprovação, listar ações de iniciação. Para condições, listar o que deve ser resolvido com responsável e prazo. Para reprovação, documentar motivo.

---

## Avaliação dos Critérios

### Critérios 1–6 — Valor da Demanda

**1. Alinhamento Estratégico:** Quão diretamente a demanda endereça um OKR, objetivo estratégico ou diretriz vigente? Quanto maior o alinhamento explícito e documentado, maior a nota.

**2. Viabilidade Técnica:** É tecnicamente realizável com os recursos e tecnologias disponíveis? Inclui avaliar: complexidade de implementação, necessidade de integração entre ERP e outros sistemas (se sim, qual o grau de dificuldade?), dependências de infraestrutura, e riscos técnicos conhecidos.

**3. Retorno sobre Investimento:** O benefício justifica o investimento? Avaliar: benefício estimado (economia, receita, redução de risco), custo estimado, payback em meses. Mesmo que estimado, deve ser quantificado com nível de confiança declarado.

**4. Urgência:** Qual o impacto de não fazer? Avaliar: pressão temporal concreta (eventos, prazos legais, custos acumulados), consequências da inação, e se há alternativa provisória disponível.

**5. Maturidade da Demanda:** O problema está suficientemente definido para ser transformado em projeto? Avaliar: clareza do problema real (vs. solução pré-concebida), completude das informações disponíveis, gaps conhecidos.

**6. Disponibilidade de Recursos:** Há equipe, orçamento e disponibilidade para executar? Avaliar: conflito com outros projetos do portfólio, orçamento sinalizado ou aprovado, disponibilidade de TI e áreas de negócio.

### Critérios 7–10 — Complexidade de Execução

**7. Esforço Estimado:** A execução demandará acima ou abaixo de 160 horas? Notas altas (≥7) indicam esforço acima de 160h — o que geralmente requer gestão formal. Considerar todas as fases: levantamento, desenvolvimento, testes e implantação.

**8. Impacto Organizacional:** Há impacto em múltiplas áreas da empresa? Avaliar: quantas unidades ou processos são afetados, se há necessidade de redefinição operacional, realocação de responsabilidades ou treinamento. Inclui avaliação de mudança de processo relevante — se há alteração de fluxo operacional, papéis ou ferramentas de trabalho.

**9. Governança Necessária:** A entrega exige acompanhamento formal de projeto — cronograma, comitê, gestão de stakeholders, controle de riscos? Notas altas (≥7) indicam que a entrega não pode ser gerida de forma autônoma pelo time técnico.

**10. Impacto Regulatório ou Financeiro:** Há relevância de impactos para compliance, legislação ou finanças? Avaliar: risco de auditoria, exigências legais, impacto em demonstrativos financeiros, obrigações fiscais ou financeiras derivadas da demanda.

---

## Output Format

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: [DEM-AAAA-NNN]
Data: YYYY-MM-DD
Analista: Felipe Filtro (VMO Autônomo)

---

## Resumo da Demanda
[2-3 linhas resumindo o problema e a solução solicitada — na linguagem do solicitante]

---

## Critérios de Qualificação

### Valor da Demanda

1. Alinhamento Estratégico      [N/10]
   [OKR/objetivo endereçado; nível de confiança: ALTO / MÉDIO / BAIXO]

2. Viabilidade Técnica          [N/10]
   [recursos disponíveis, complexidade técnica, necessidade de integração com outros sistemas e grau de dificuldade]

3. Retorno sobre Investimento   [N/10]
   [benefício estimado — R$ ou descrição; custo estimado; payback em meses; confiança: ALTA / MÉDIA / BAIXA]

4. Urgência                     [N/10]
   [impacto de não fazer; pressão temporal concreta — data, evento ou custo acumulado]

5. Maturidade da Demanda        [N/10]
   [clareza do problema, completude das informações; gaps identificados]

6. Disponibilidade de Recursos  [N/10]
   [equipe, orçamento, conflitos de portfólio]

### Complexidade de Execução

7. Esforço Estimado             [N/10]
   [estimativa de esforço total: acima ou abaixo de 160h; como chegou a essa estimativa]

8. Impacto Organizacional       [N/10]
   [áreas/divisões impactadas; mudanças de processo relevantes identificadas]

9. Governança Necessária        [N/10]
   [necessidade de cronograma formal, comitês, gestão de stakeholders e riscos]

10. Impacto Regulatório/Financeiro [N/10]
    [riscos de compliance, obrigações legais, impacto em demonstrativos ou auditorias]

---

## Resultado

**PONTUAÇÃO TOTAL: [total]/100 ([%]%)**

**CLASSIFICAÇÃO: [PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA]**
[Justificativa técnica da classificação: por que é projeto e não melhoria, ou vice-versa.
Se Melhoria → indicar time de sustentação ERP: FI/CO/SD/Fiscal | PM/MM | HCM]

**DECISÃO: [APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA]**

---

## Condições Bloqueantes (se aplicável)
- [condição específica que deve ser resolvida antes de prosseguir — não condições genéricas]

## Próximos Passos
| Ação | Responsável | Prazo |
|------|-------------|-------|
```

---

## Output Example

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-047
Data: 2026-04-11
Analista: Felipe Filtro (VMO Autônomo)

---

## Resumo da Demanda
A área de Supply Chain solicita um sistema de rastreamento em tempo real dos fornecedores Tier 1,
integrado ao SAP MM, com alertas automáticos para atrasos e dashboard de acompanhamento.
Motivado por 3 rupturas de fornecimento no Q1/2026 com custo de R$135.000.

---

## Critérios de Qualificação

### Valor da Demanda

1. Alinhamento Estratégico      8/10
   OKR Q1/2026: "Reduzir falhas de fornecimento em 30%" — endereçamento direto e documentado.
   Confiança: ALTA. Ata de reunião de board confirma pressão executiva pelo tema.

2. Viabilidade Técnica          6/10
   SAP MM possui API de integração confirmada pela TI. A complexidade da integração com
   rastreamento em tempo real é moderada-alta e requer POC técnica antes de confirmar viabilidade.
   Integração com sistemas de geolocalização dos fornecedores não foi avaliada — lacuna relevante.

3. Retorno sobre Investimento   8/10
   Custo estimado: R$280.000. Benefício: R$520.000/ano (prevenção de rupturas como as de Q1).
   Payback estimado: 6,5 meses. Confiança: MÉDIA — baseado em extrapolação do custo de Q1/2026.

4. Urgência                     9/10
   3 incidentes em Q1/2026 custaram R$135.000. Reunião de avaliação de fornecedores em
   julho/2026 exige solução implementada. Cada mês de atraso mantém o risco ativo.

5. Maturidade da Demanda        6/10
   Problema bem definido, solução técnica clara em alto nível. Gaps relevantes: sponsor não
   designado, orçamento não formalizado, escopo de integração com dispositivos dos fornecedores
   não levantado. Maturidade suficiente para avançar, mas com condições.

6. Disponibilidade de Recursos  6/10
   Orçamento sinalizado (aguarda formalização CAPEX). Equipe TI com 60% de disponibilidade —
   conflito com projeto SAP em paralelo é risco moderado. Recursos suficientes mas não
   confirmados.

### Complexidade de Execução

7. Esforço Estimado             9/10
   Estimativa mínima: 400h (desenvolvimento da integração SAP) + 100h (infraestrutura e testes)
   = 500h totais estimados. Muito acima do limiar de 160h. Alta complexidade de execução.

8. Impacto Organizacional       8/10
   Impacta Supply Chain, TI e indiretamente os 12 fornecedores Tier 1 (mudança de processo de
   atualização de localização). Mudança de processo relevante: analista passa de monitoramento
   reativo (e-mail) para proativo (dashboard). Requer treinamento e gestão de mudança.

9. Governança Necessária        9/10
   Projeto de 6+ meses, integração SAP, múltiplos fornecedores externos, prazo vinculado a
   evento externo. Exige cronograma formal, gestão de stakeholders, controle de riscos e
   comitê de acompanhamento. Não pode ser gerido autonomamente pelo time técnico.

10. Impacto Regulatório/Financeiro  6/10
    Custos de ruptura impactam demonstrativo financeiro (R$135k em Q1/2026). Não há risco
    regulatório direto. O impacto financeiro é real mas caracterizado como mitigação de custo
    operacional — sem obrigação legal ou auditoria envolvida.

---

## Resultado

**PONTUAÇÃO TOTAL: 75/100 (75%)**

**CLASSIFICAÇÃO: PROJETO**
Critérios 7–10 confirmam alta complexidade: esforço (9/10), impacto organizacional (8/10) e
governança necessária (9/10) pontuam acima de 7 individualmente — 3 dos 4 critérios de
complexidade indicam necessidade de gestão de projeto formal. A integração com SAP MM e a
mudança de processo multi-área tornam inviável o tratamento como melhoria pelo time de sustentação.
→ Encaminhar para pipeline VMO: TAP, ERF, Cronograma, Riscos, KPIs, Work Request.

**DECISÃO: APROVADO COM CONDIÇÕES**

---

## Condições Bloqueantes
1. Designar sponsor executivo com autoridade para aprovar TAP (nível Diretor ou superior)
2. Formalizar orçamento em CAPEX — aprovação financeira antes do kick-off
3. Levantar escopo de integração com dispositivos dos fornecedores antes da ERF

## Próximos Passos
| Ação | Responsável | Prazo |
|------|-------------|-------|
| Designar sponsor (Diretor+) | VP Supply Chain / CIO | 2026-04-14 |
| Formalizar orçamento CAPEX | Ana Ferreira + Financeiro | 2026-04-14 |
| Levantar integração com dispositivos Tier 1 | TI + Supply Chain | 2026-04-13 |
| Iniciar elaboração do TAP (após condições) | PMO | 2026-04-17 |
```

---

## Quality Criteria

- [ ] Resumo da demanda presente em linguagem clara (não jargão interno)
- [ ] Todos os 10 critérios avaliados com pontuação 1–10 e justificativa ≥ 2 linhas
- [ ] Pontuação total calculada corretamente (soma dos 10 critérios / 100)
- [ ] Classificação declarada: PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA
- [ ] Se Melhoria: time de sustentação ERP indicado (FI/CO/SD/Fiscal | PM/MM | HCM)
- [ ] Justificativa técnica da classificação — por que projeto e não melhoria (ou vice-versa)
- [ ] Decisão coerente com a pontuação (≥75% APROVADO, 50-74% COM CONDIÇÕES, <50% REPROVADO)
- [ ] Condições bloqueantes distintas de condições desejáveis
- [ ] Próximos passos com responsável e prazo

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. A decisão não corresponde à pontuação calculada (ex: "APROVADO" com pontuação 45%)
2. Algum critério avaliado sem justificativa de ao menos 1 linha
3. Classificação ausente (Projeto / Melhoria Corretiva / Melhoria Evolutiva)
4. Melhoria sem indicação do time de sustentação ERP responsável
5. Justificativa da classificação genérica — "parece ser projeto" sem evidência dos critérios 7–10
