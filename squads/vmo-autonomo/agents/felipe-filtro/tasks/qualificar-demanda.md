---
task: "Qualificar Demanda"
order: 1
input:
  - demanda_estruturada: "Output do checkpoint de validação (demanda-validada.md)"
  - documentos_estrategicos: "OKRs ou objetivos organizacionais disponíveis"
output:
  - analise_qualificacao: "Avaliação dos 10 critérios (1-10 cada) com pontuação, justificativa e evidência declarada"
  - classificacao: "PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA + time de sustentação ERP (se aplicável)"
  - decisao: "APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA"
  - proximos_passos: "Ações requeridas com responsável e prazo"
---

# Qualificar Demanda

Avalia se a demanda recebida deve ser transformada em projeto formal ou encaminhada como
melhoria para o time de sustentação ERP. Aplica **10 critérios de qualificação** (pontuação
1–10 cada, máximo 100 pts) e emite uma **classificação** e um **parecer fundamentado** que
habilita a decisão do GP ou do PMO.

O ponto central desta qualificação não é apenas decidir se a demanda "vale a pena" — é
distinguir com precisão se ela requer **gestão de projeto formal** (pipeline VMO completo)
ou se pode ser resolvida pelo **time de sustentação ERP** como melhoria. A classificação
incorreta gera dois problemas igualmente prejudiciais: sobrecarregar o PMO com tarefas
operacionais, ou subestimar projetos que precisam de governança formal.

---

## Process

1. **Carregar contexto estratégico**: Ler OKRs e objetivos organizacionais disponíveis.

2. **Identificar e desafiar os Claims de Alto Risco** (antes de avaliar qualquer critério):
   Percorrer a demanda e identificar afirmações que se enquadram na tabela de Claims de Alto
   Risco do agente (replicação, custo zero, esforço baixo, já aprovado, sem integração, etc.).
   Para cada claim identificado:
   - Verificar se há evidência documental no material fornecido
   - Se SIM: registrar a evidência e prosseguir
   - Se NÃO ou PARCIAL: formular a pergunta exata que resolveria a dúvida e rebaixar a nota
     do critério afetado pelo grau de incerteza
   Esta etapa acontece ANTES de atribuir qualquer nota — ela define os tetos de confiança.

3. **Avaliar os 10 critérios**: Para cada critério, atribuir pontuação de **1 a 10** com:
   - Justificativa de ao menos 2 linhas baseada nos dados da demanda
   - Declaração explícita: **"Evidência disponível: SIM / NÃO / PARCIAL"**
   - Se SIM: citar a evidência (documento, e-mail, afirmação verificável)
   - Se NÃO ou PARCIAL: formular a pergunta que permitiria revisar a nota
   - Para notas ≥ 7: evidência compulsória — sem ela a nota máxima é 6
   - Para notas ≤ 3: declarar o que tornaria a nota mais alta

4. **Calcular pontuação total**: Somar os 10 critérios (máximo 100) e calcular o percentual.

5. **Emitir a classificação** com base nos critérios 7–10 (complexidade):
   - **Projeto**: se ao menos 2 dos critérios 7–10 pontuarem ≥ 7/10 individualmente
   - **Melhoria Evolutiva**: ajuste funcional sem estrutura de processo alterada
   - **Melhoria Corretiva**: correção de erro — vai direto para sustentação
   - Se for Melhoria → indicar time: **FI / CO / SD / Fiscal | PM / MM | HCM**

6. **Emitir decisão** com base na pontuação total:
   - ≥ 75% (≥ 75 pts): **APROVADO**
   - 50–74% (50–74 pts) com condições resolvíveis: **APROVADO COM CONDIÇÕES**
   - < 50% (< 50 pts): **REPROVADO**
   - Claims de risco não respondidos comprometem critérios: **EM ESPERA**

7. **Definir próximos passos**: Para aprovação, listar ações de iniciação. Para condições,
   listar o que deve ser resolvido com responsável e prazo. Para reprovação, documentar motivo.

---

## Avaliação dos Critérios

### Critérios 1–6 — Valor da Demanda

**1. Alinhamento Estratégico:** Quão diretamente a demanda endereça um OKR, objetivo
estratégico ou diretriz vigente? Quanto maior o alinhamento explícito e documentado,
maior a nota. Se "alinhado com digitalização" sem OKR específico: máximo 6/10.

**2. Viabilidade Técnica:** É tecnicamente realizável com os recursos disponíveis?
Avaliar: complexidade de implementação, integrações, dependências, riscos técnicos.
Se afirmado "é simples / replicação": exigir evidência da solução original e das
diferenças de ambiente antes de pontuar acima de 6/10.

**3. Retorno sobre Investimento:** O benefício justifica o investimento? Quantificar:
benefício estimado (R$ ou tempo), custo estimado, payback em meses. Se ROI afirmado
sem dados de volume ou custo real: confiança BAIXA, nota máxima 6/10.

**4. Urgência:** Qual o impacto de não fazer? Exigir: pressão temporal com DATA concreta
(não "ASAP" ou "urgente"), consequência quantificada da inação. "É urgente" sem data
e sem custo de inação = nota máxima 4/10.

**5. Maturidade da Demanda:** O problema está suficientemente definido? Avaliar:
clareza do problema real (vs. solução pré-concebida), completude das informações.
Se processo não documentado e escopo não declarado: máximo 5/10.

**6. Disponibilidade de Recursos:** Há equipe, orçamento e disponibilidade? Avaliar:
orçamento aprovado formalmente (não apenas sinalizado), conflitos de portfólio,
disponibilidade confirmada de TI. "Orçamento estimado" ≠ "orçamento aprovado".

### Critérios 7–10 — Complexidade de Execução

**7. Esforço Estimado:** Acima ou abaixo de 160 horas? Notas altas (≥7) indicam esforço
acima de 160h. Se afirmado "esforço baixo": exigir estimativa por fase (levantamento,
configuração, testes, go-live). Sem estimativa por fase: nota máxima 5/10 por incerteza.

**8. Impacto Organizacional:** Impacto em múltiplas áreas? Avaliar: quantas unidades,
mudança de processo, realocação de responsabilidades, treinamento. "Não impacta outras
áreas" sem evidência explícita: nota máxima 4/10 (desconfiar do escopo declarado).

**9. Governança Necessária:** Exige acompanhamento formal? Notas altas (≥7) indicam
que não pode ser gerido autonomamente pelo time técnico. Correlacionar com critério 7.

**10. Impacto Regulatório ou Financeiro:** Risco de compliance, lei, finanças? Avaliar:
risco de auditoria, obrigações legais, impacto em demonstrativos. Integrações bancárias
ou fiscais sempre merecem avaliar ao menos 4/10 pelo risco implícito.

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

## Claims de Alto Risco Identificados
| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| [afirmação identificada] | SIM / NÃO / PARCIAL | [critério afetado e teto de nota] |

---

## Critérios de Qualificação

1. Alinhamento Estratégico      [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [OKR/objetivo endereçado; nível de confiança: ALTO / MÉDIO / BAIXO]
   [Se NÃO/PARCIAL: "Para revisar esta nota, precisamos de: [pergunta específica]"]

2. Viabilidade Técnica          [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [recursos disponíveis, complexidade técnica, integrações avaliadas]
   [Se claim de replicação: o que foi verificado e o que não foi]

3. Retorno sobre Investimento   [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [benefício estimado — R$ ou descrição; custo estimado; payback em meses; confiança: ALTA/MÉDIA/BAIXA]

4. Urgência                     [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [data concreta; consequência quantificada da inação]

5. Maturidade da Demanda        [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [clareza do problema, completude das informações; gaps identificados]

6. Disponibilidade de Recursos  [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [orçamento aprovado ou sinalizado; conflitos de portfólio; disponibilidade TI]

7. Esforço Estimado             [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [estimativa por fase: levantamento Xh + config Yh + testes Zh + go-live Wh = total]
   [confiança: ALTA/MÉDIA/BAIXA; base da estimativa]

8. Impacto Organizacional       [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [áreas impactadas; mudanças de processo; treinamento necessário]

9. Governança Necessária        [N/10]
   Evidência disponível: SIM / NÃO / PARCIAL
   [cronograma formal necessário? comitê? gestão de stakeholders?]

10. Impacto Regulatório/Financeiro [N/10]
    Evidência disponível: SIM / NÃO / PARCIAL
    [riscos de compliance, obrigações legais, impacto em demonstrativos]

---

PONTUAÇÃO: [total]/100 ([%]%)

**CLASSIFICAÇÃO: [PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA]**
[Justificativa técnica da classificação com base nos critérios 7–10.
Se Melhoria → indicar time de sustentação ERP: FI/CO/SD/Fiscal | PM/MM | HCM]

**DECISÃO: [APROVADO / APROVADO COM CONDIÇÕES / REPROVADO / EM ESPERA]**
[Se EM ESPERA: listar as perguntas exatas que precisam ser respondidas antes da resubmissão]

---

## Condições Bloqueantes (se aplicável)
- **CB-[N]:** [condição específica com o que deve ser entregue para desbloqueio]

## Perguntas em Aberto (se EM ESPERA)
- **P-[N]:** [pergunta exata para [responsável] — resposta necessária até [prazo]]

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

RESUMO:
A área de Supply Chain solicita um sistema de rastreamento em tempo real dos fornecedores Tier 1,
integrado ao SAP MM, com alertas automáticos e dashboard de acompanhamento. O projeto é motivado
por 3 rupturas de fornecimento no Q1/2026 (custo de R$135k) e tem prazo vinculado à reunião de
avaliação de fornecedores em julho/2026. Aprovado com condições — sponsor e orçamento precisam
ser formalizados antes do início.

---

## Claims de Alto Risco Identificados
| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "Integração com SAP é simples" | NÃO | Critério 2: teto rebaixado para 6/10 até POC técnica |
| "Orçamento disponível" | PARCIAL | Critério 6: sinalizado, não aprovado formalmente |

---

## Critérios de Qualificação

1. Alinhamento Estratégico         8/10
   Evidência disponível: SIM
   OKR Q1/2026: "Reduzir falhas de fornecimento em 30%" — endereçamento direto e documentado.
   Confiança: ALTA. Ata de reunião de board confirma pressão executiva pelo tema.

2. Viabilidade Técnica             6/10
   Evidência disponível: PARCIAL
   SAP MM possui API de integração confirmada pela TI. Complexidade da integração com dispositivos
   de rastreamento dos fornecedores é moderada-alta e requer POC técnica. Confiança: MÉDIA.
   Claim "integração simples" não verificado — teto 6/10 aplicado até validação técnica.

3. Retorno sobre Investimento      8/10
   Evidência disponível: SIM
   Custo estimado: R$280.000. Benefício: R$520.000/ano (prevenção de rupturas). Payback: 6,5 meses.
   Confiança: MÉDIA — baseado em extrapolação do custo de Q1/2026.

4. Urgência                        9/10
   Evidência disponível: SIM
   3 incidentes em Q1/2026 com custo de R$135.000. Data concreta: reunião de avaliação de
   fornecedores em julho/2026 exige solução implementada. Consequência: cada mês de atraso
   mantém o risco de ruptura ativo.

5. Maturidade da Demanda           6/10
   Evidência disponível: PARCIAL
   Problema bem definido, solução técnica clara em alto nível. Gaps: sponsor não designado,
   orçamento não formalizado, escopo de integração com dispositivos dos fornecedores não levantado.

6. Disponibilidade de Recursos     6/10
   Evidência disponível: PARCIAL
   Orçamento sinalizado como disponível (aguarda formalização CAPEX). Equipe TI com 60% de
   disponibilidade — conflito moderado com projeto SAP em paralelo.

7. Esforço Estimado                9/10
   Evidência disponível: SIM
   Estimativa por fase: integração SAP (~200h) + rastreamento em tempo real (~120h) +
   alertas (~60h) + dashboard (~80h) + infraestrutura e testes (~100h) = ~560h totais.
   Muito acima de 160h. Confiança: MÉDIA.

8. Impacto Organizacional          8/10
   Evidência disponível: SIM
   Impacta Supply Chain, TI e indiretamente os 12 fornecedores Tier 1 como partes externas.
   Mudança de processo: analista passa de monitoramento reativo (e-mail) para proativo
   (dashboard em tempo real). Processo de acionamento de fornecedor também muda. Requer
   treinamento e gestão de mudança.

9. Governança Necessária           9/10
   Evidência disponível: SIM
   Projeto de 6+ meses com integração SAP, múltiplos fornecedores externos e prazo vinculado a
   evento externo. Exige cronograma formal, gestão de stakeholders, controle de riscos e comitê.

10. Impacto Regulatório/Financeiro  5/10
    Evidência disponível: PARCIAL
    Custos de ruptura impactam demonstrativo financeiro (R$135k em Q1/2026). Não há risco
    regulatório direto — impacto é mitigação de custo operacional, sem obrigação legal.

---

PONTUAÇÃO: 74/100 (74%)

**CLASSIFICAÇÃO: PROJETO**
Critérios 7–10: esforço (9), impacto org. (8), governança (9) pontuam ≥7 — 3 de 4 confirmam
necessidade de gestão formal. Integração bidirecional com SAP e mudança de processo em Supply
Chain tornam inviável tratamento como melhoria.

**DECISÃO: APROVADO COM CONDIÇÕES**

---

## Condições Bloqueantes
- **CB-1:** Designar sponsor executivo com autoridade para aprovar TAP (Diretor ou superior)
- **CB-2:** Formalizar orçamento em CAPEX — aprovação financeira antes do kick-off
- **CB-3:** Conduzir POC técnica de integração SAP + dispositivos fornecedores Tier 1

## Próximos Passos
| Ação | Responsável | Prazo |
|------|-------------|-------|
| Designar sponsor (Diretor+) | VP Supply Chain / CIO | 2026-04-14 |
| Formalizar orçamento CAPEX | Ana Ferreira + Financeiro | 2026-04-14 |
| Conduzir POC integração SAP + dispositivos | TI + Supply Chain | 2026-04-20 |
| Iniciar elaboração do TAP (após condições) | PMO | 2026-04-24 |
```

---

## Quality Criteria

- [ ] Tabela de Claims de Alto Risco preenchida (mesmo que vazia com "nenhum identificado")
- [ ] "Evidência disponível: SIM/NÃO/PARCIAL" declarado para cada um dos 10 critérios
- [ ] Notas ≥ 7 têm evidência citada explicitamente
- [ ] Notas ≤ 3 têm declaração do que tornaria a nota mais alta
- [ ] Pontuação total calculada corretamente (soma dos 10 critérios / 100)
- [ ] Classificação declarada: PROJETO / MELHORIA CORRETIVA / MELHORIA EVOLUTIVA
- [ ] Se Melhoria: time de sustentação ERP indicado
- [ ] Justificativa técnica da classificação baseada nos critérios 7–10
- [ ] Decisão coerente com a pontuação (≥75 APROVADO, 50-74 COM CONDIÇÕES, <50 REPROVADO)
- [ ] Se EM ESPERA: perguntas exatas listadas com responsável e prazo
- [ ] Condições bloqueantes distintas de condições desejáveis
- [ ] Próximos passos com responsável e prazo

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. A decisão não corresponde à pontuação calculada (ex: "APROVADO" com pontuação 45%)
2. Algum critério avaliado sem "Evidência disponível:" declarado
3. Nota ≥ 7 sem evidência citada (teto não foi aplicado)
4. Classificação ausente (Projeto / Melhoria Corretiva / Melhoria Evolutiva)
5. Melhoria sem indicação do time de sustentação ERP responsável
6. Tabela de Claims de Alto Risco ausente
7. Claim de replicação ou esforço baixo sem verificação documentada
