---
task: "Qualificar Demanda"
order: 1
input:
  - demanda_estruturada: "Output do checkpoint de validação (demanda-validada.md)"
  - documentos_estrategicos: "OKRs ou objetivos organizacionais disponíveis"
output:
  - analise_qualificacao: "Avaliação dos 10 critérios (escala 1-10, máx 100 pts) com pontuação e justificativa"
  - classificacao: "PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA + time de sustentação ERP"
  - decisao: "APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA"
  - proximos_passos: "Ações requeridas com responsável e prazo"
---

# Qualificar Demanda

Avalia se a demanda recebida deve ser transformada em projeto formal, aplicando os **10 critérios de qualificação do VMO** (pontuação 1–10 cada, máximo 100 pts). Emite um parecer fundamentado que habilita a decisão do GP ou do PMO.

Classifica solicitações no contexto de demandas de TI para ERP, distinguindo entre **Projeto** e **Melhoria**, e direcionando corretamente ao PMO ou ao time de Sustentação ERP responsável.

---

## Process

1. **Carregar contexto estratégico**: Ler OKRs e objetivos organizacionais disponíveis para avaliar alinhamento.
2. **Avaliar os 10 critérios**: Para cada critério, atribuir pontuação de **1 a 10** com justificativa de ao menos 2 linhas baseada nos dados da demanda.
3. **Calcular pontuação total**: Somar os 10 critérios (máximo 100) e calcular percentual.
4. **Emitir decisão**:
   - ≥ 75% = **APROVADO**
   - 50–74% com condições resolvíveis = **APROVADO COM CONDIÇÕES**
   - < 50% = **REPROVADO**
   - Informação insuficiente = **EM ESPERA**
5. **Definir próximos passos**: Para aprovação, listar ações de iniciação. Para condições, listar o que deve ser resolvido. Para reprovação, documentar motivo.

---

## Avaliação dos Critérios

### Critérios 1–6 — Valor da Demanda

**1. Alinhamento Estratégico**: Quão diretamente a demanda endereça um OKR, objetivo estratégico ou diretriz vigente? Quanto maior o alinhamento explícito e documentado, maior a nota.

**2. Viabilidade Técnica + Integração entre Sistemas**: Avaliar se a demanda é tecnicamente realizável com os recursos disponíveis. **Obrigatório avaliar explicitamente**: há necessidade de integração entre ERP e outros sistemas? Se sim, qual é o grau de complexidade dessa integração (simples leitura de dados, API bidirecional, middleware)? Integrações aumentam o risco técnico e devem reduzir a nota se não forem validadas.

**3. Retorno sobre Investimento**: O benefício justifica o investimento? Estimar: benefício (economia, receita, redução de risco), custo estimado, payback em meses. Declarar nível de confiança da estimativa.

**4. Urgência**: Qual o impacto de não fazer? Avaliar pressão temporal concreta (evento, prazo legal, custo acumulado) e a disponibilidade de alternativa provisória.

**5. Maturidade da Demanda**: O problema está suficientemente definido para virar projeto? Avaliar clareza do problema, completude das informações e lacunas críticas identificadas.

**6. Disponibilidade de Recursos**: Há equipe, orçamento e disponibilidade para executar? Avaliar conflito com portfólio, orçamento aprovado ou sinalizado, disponibilidade das áreas envolvidas.

### Critérios 7–10 — Complexidade de Execução

**7. Esforço Estimado**: A execução demandará acima ou abaixo de **160 horas**? Notas altas (≥7) indicam esforço acima de 160h considerando todas as fases: levantamento, desenvolvimento, testes e implantação. Demandas acima de 160h geralmente requerem gestão formal de projeto.

**8. Impacto Organizacional + Mudança de Processo**: Avaliar abrangência da demanda na organização. **Obrigatório avaliar explicitamente**: ocorre alteração relevante de processo? Quais fluxos operacionais, papéis, responsabilidades ou ferramentas de trabalho mudam? Impacto em múltiplas áreas com mudança de processo aumenta a necessidade de gestão formal.

**9. Governança Necessária**: A entrega exige acompanhamento formal — cronograma, comitês, stakeholders, gestão de riscos? Notas altas (≥7) indicam que a entrega não pode ser gerida autonomamente pelo time técnico.

**10. Impacto Regulatório ou Financeiro**: Há relevância de impactos para compliance, legislação ou finanças? Considerar: auditoria, exigências legais, riscos fiscais, impacto em demonstrativos financeiros.

---

## Classificação Final

Com base nos critérios 7–10, defina se a demanda é:

- **Projeto**: se ao menos 2 dos critérios 7–10 pontuarem ≥ 7/10 individualmente → exige gestão de projeto formal, segue pipeline VMO completo.
- **Melhoria Evolutiva**: pequeno ajuste funcional sem mudança estrutural de processo e esforço baixo → Sustentação ERP.
- **Melhoria Corretiva**: correção de erro ou comportamento inesperado → Sustentação ERP, independente da pontuação total.

Se Melhoria, indicar qual time de Sustentação ERP irá atuar:
- **FI / CO / SD / Fiscal** — financeiro, contabilidade, vendas, fiscal
- **PM / MM** — projetos, materiais, compras
- **HCM** — recursos humanos, folha

---

## Justificativa

Explique tecnicamente o motivo da classificação e direcionamento. Evite respostas genéricas, excessivamente longas ou muito técnicas.

---

## Output Format

```markdown
ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: [DEM-AAAA-NNN]
Data: YYYY-MM-DD
Analista: Felipe Filtro (VMO Autônomo)

RESUMO:
[Resumo executivo — corpo da mensagem de retorno ao solicitante. Claro, direto, sem jargão interno.]

---

CRITÉRIOS DE QUALIFICAÇÃO

1. Alinhamento Estratégico         [N/10]
   [OKR/objetivo endereçado; nível de confiança]

2. Viabilidade Técnica             [N/10]
   [recursos, tecnologia, complexidade]
   → Integração entre sistemas: [descrever se há integração com ERP ou outros sistemas, grau de complexidade e risco]

3. Retorno sobre Investimento      [N/10]
   [benefício estimado — R$ ou descrição; custo estimado; payback em meses; confiança: ALTA/MÉDIA/BAIXA]

4. Urgência                        [N/10]
   [impacto de não fazer; pressão temporal concreta]

5. Maturidade da Demanda           [N/10]
   [clareza do problema, completude das informações; gaps identificados]

6. Disponibilidade de Recursos     [N/10]
   [equipe, orçamento, conflitos de portfólio]

7. Esforço Estimado                [N/10]
   [estimativa de esforço total: acima ou abaixo de 160h; base da estimativa]

8. Impacto Organizacional          [N/10]
   [áreas/divisões impactadas]
   → Mudança de processo: [descrever se há alteração de fluxo operacional, papéis, responsabilidades ou ferramentas de trabalho]

9. Governança Necessária           [N/10]
   [necessidade de cronograma formal, comitês, gestão de stakeholders e riscos]

10. Impacto Regulatório/Financeiro [N/10]
    [riscos de compliance, obrigações legais, impacto em demonstrativos ou auditorias]

---

PONTUAÇÃO: [total]/100 ([%]%)
CLASSIFICAÇÃO: [PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA]
[Se Melhoria → time: FI/CO/SD/Fiscal | PM/MM | HCM]
DECISÃO: [APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA]

CONDIÇÕES BLOQUEANTES (se aplicável):
- [condição específica que deve ser resolvida antes de prosseguir]

PRÓXIMOS PASSOS:
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

RESUMO:
A área de Supply Chain solicita um sistema de rastreamento em tempo real dos fornecedores Tier 1,
integrado ao SAP MM, com alertas automáticos e dashboard de acompanhamento. O projeto é motivado
por 3 rupturas de fornecimento no Q1/2026 (custo de R$135k) e tem prazo vinculado à reunião de
avaliação de fornecedores em julho/2026. Aprovado com condições — sponsor e orçamento precisam
ser formalizados antes do início.

---

CRITÉRIOS DE QUALIFICAÇÃO

1. Alinhamento Estratégico         8/10
   OKR Q1/2026: "Reduzir falhas de fornecimento em 30%" — endereçamento direto e documentado.
   Confiança: ALTA. Ata de reunião de board confirma pressão executiva pelo tema.

2. Viabilidade Técnica             6/10
   SAP MM possui API de integração confirmada pela TI. Complexidade da integração com dispositivos
   de rastreamento dos fornecedores é moderada-alta e requer POC técnica. Confiança: MÉDIA.
   → Integração entre sistemas: SIM — integração bidirecional com SAP MM para importação de pedidos
   e atualização de status. Grau de complexidade: ALTO. Risco de escopo relevante — requer POC
   antes de comprometer o prazo.

3. Retorno sobre Investimento      8/10
   Custo estimado: R$280.000. Benefício: R$520.000/ano (prevenção de rupturas). Payback: 6,5 meses.
   Confiança: MÉDIA — baseado em extrapolação do custo de Q1/2026.

4. Urgência                        9/10
   3 incidentes em Q1/2026 com custo de R$135.000. Reunião de avaliação de fornecedores em
   julho/2026 exige solução implementada. Cada mês de atraso mantém o risco ativo.

5. Maturidade da Demanda           6/10
   Problema bem definido, solução técnica clara em alto nível. Gaps relevantes: sponsor não
   designado, orçamento não formalizado, escopo de integração com dispositivos dos fornecedores
   não levantado.

6. Disponibilidade de Recursos     6/10
   Orçamento sinalizado como disponível (aguarda formalização CAPEX). Equipe TI com 60% de
   disponibilidade — conflito moderado com projeto SAP em paralelo.

7. Esforço Estimado                9/10
   Estimativa: integração SAP (~200h) + rastreamento em tempo real (~120h) + alertas (~60h)
   + dashboard (~80h) + infraestrutura e testes (~100h) = ~560h totais. Muito acima de 160h.

8. Impacto Organizacional          8/10
   Impacta Supply Chain, TI e indiretamente os 12 fornecedores Tier 1 como partes externas.
   → Mudança de processo: SIM — analista de Supply Chain passa de monitoramento reativo (e-mail)
   para proativo (dashboard em tempo real). Processo de acionamento de fornecedor também muda.
   Requer treinamento e gestão de mudança.

9. Governança Necessária           9/10
   Projeto de 6+ meses com integração SAP, múltiplos fornecedores externos e prazo vinculado a
   evento externo. Exige cronograma formal, gestão de stakeholders, controle de riscos e comitê.

10. Impacto Regulatório/Financeiro  5/10
    Custos de ruptura impactam demonstrativo financeiro (R$135k em Q1/2026). Não há risco
    regulatório direto — impacto é mitigação de custo operacional, sem obrigação legal.

---

PONTUAÇÃO: 74/100 (74%)
CLASSIFICAÇÃO: PROJETO
Critérios 7–10: esforço (9), impacto org. (8), governança (9) pontuam ≥7 — 3 de 4 confirmam
necessidade de gestão formal. Integração bidirecional com SAP e mudança de processo em Supply
Chain tornam inviável tratamento como melhoria.
DECISÃO: APROVADO COM CONDIÇÕES

CONDIÇÕES BLOQUEANTES:
1. Designar sponsor executivo com autoridade para aprovar TAP (Diretor ou superior)
2. Formalizar orçamento em CAPEX — aprovação financeira antes do kick-off
3. Validar escopo de integração com dispositivos dos fornecedores Tier 1 (POC técnica)

PRÓXIMOS PASSOS:
| Ação | Responsável | Prazo |
|------|-------------|-------|
| Designar sponsor (Diretor+) | VP Supply Chain / CIO | 2026-04-14 |
| Formalizar orçamento CAPEX | Ana Ferreira + Financeiro | 2026-04-14 |
| Conduzir POC integração SAP + dispositivos | TI + Supply Chain | 2026-04-20 |
| Iniciar elaboração do TAP (após condições) | PMO | 2026-04-24 |
```

---

## Quality Criteria

- [ ] Resumo executivo presente — claro e sem jargão interno
- [ ] Todos os 10 critérios avaliados com pontuação 1–10 e justificativa ≥ 2 linhas
- [ ] Critério 2 inclui avaliação explícita de integração entre sistemas (mesmo que a resposta seja "não há")
- [ ] Critério 8 inclui avaliação explícita de mudança de processo (mesmo que a resposta seja "não há")
- [ ] Pontuação total calculada corretamente (soma / 100)
- [ ] Classificação declarada: PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA
- [ ] Se Melhoria: time de sustentação ERP indicado (FI/CO/SD/Fiscal | PM/MM | HCM)
- [ ] Decisão coerente com a pontuação (≥75% APROVADO; 50–74% COM CONDIÇÕES; <50% REPROVADO)
- [ ] Condições bloqueantes distintas de condições desejáveis
- [ ] Próximos passos com responsável e prazo

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. A decisão não corresponde à pontuação calculada (ex: "APROVADO" com 45%)
2. Algum critério avaliado sem justificativa de ao menos 1 linha
3. Critério 2 sem avaliação explícita de integração entre sistemas
4. Critério 8 sem avaliação explícita de mudança de processo
5. Classificação ausente ou sem justificativa com base nos critérios 7–10
