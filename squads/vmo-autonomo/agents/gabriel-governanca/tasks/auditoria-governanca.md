---
task: "Auditoria de Governança VMO"
order: 1
mode: pipeline
input:
  - pacote_iniciacao: "Todos os documentos em projects/{project}/ (todas as fases)"
  - qualificacao: "projects/{project}/01-qualificacao/qualificacao-aprovada.md"
  - documentacao_base: "projects/{project}/02-iniciacao/documentacao-base.md"
  - requisitos: "projects/{project}/02-iniciacao/requisitos.md"
  - cronograma: "projects/{project}/03-planejamento/cronograma.md"
  - plano_riscos: "projects/{project}/03-planejamento/plano-riscos.md"
  - kpis: "projects/{project}/03-planejamento/kpis.md"
  - work_request: "projects/{project}/02-iniciacao/work-request.md"
  - status_report: "projects/{project}/04-monitoramento/status-report-*.md (mais recente)"
  - revisao_vera: "projects/{project}/05-encerramento/revisao-final.md"
output:
  - auditoria: "Relatório de auditoria de governança com veredicto e recomendações"
---

# Auditoria de Governança VMO

Realiza a auditoria formal de governança do pacote de iniciação do projeto, verificando **conformidade com os padrões e processos VMO** — independente da qualidade documental avaliada pela Vera Veredito. Esta task examina o COMO o projeto foi gerenciado, não apenas o QUE foi documentado. É a última barreira antes do checkpoint de aprovação final.

A distinção com a revisão da Vera é explícita: Vera avalia se os documentos têm qualidade (conteúdo correto, objetivo SMART, critérios de aceitação, etc.). Gabriel audita se o processo de governança foi seguido (sponsor correto, CBs resolvidas, conformidade com políticas do grupo, rastreabilidade entre documentos, ausência de inconsistências sistêmicas).

## Domínios de Auditoria

### D1 — Governança de Sponsor e Autorização

Verifica:
- O TAP identifica um sponsor com nome e cargo explícitos?
- O cargo do sponsor atende ao mínimo de **Diretor ou superior** (política do grupo)?
- Se o campo sponsor está como "[A DEFINIR]" — isso é uma **não-conformidade crítica** (NC-CRÍTICA) que bloqueia o projeto
- A qualificação aprovada registra as condições bloqueantes CB-01 e CB-02?
- Existe evidência documental de resolução das CBs (não apenas afirmação verbal)?

### D2 — Rastreabilidade e Consistência Cross-Document

Verifica se os documentos são mutuamente consistentes:
- Prazo no TAP = Prazo no PM Canvas = Prazo no Cronograma?
- Orçamento no TAP = BAC nos KPIs = Envelope de referência no WR?
- Escopo declarado no TAP está mapeado nos requisitos RF Must Have?
- Critérios de sucesso do TAP têm KPIs correspondentes?
- Módulos no WR correspondem ao escopo do TAP e ERF?

Qualquer inconsistência entre documentos é registrada como **não-conformidade moderada (NC-MOD)** — não bloqueia individualmente, mas o acúmulo pode bloquear.

### D3 — Conformidade com Políticas VMO

Verifica a aplicação dos padrões obrigatórios do grupo:
- Work Request emitido antes do envio a fornecedores? (existência do arquivo WR)
- WR contém o Artefato Obrigatório completo (10 grupos / 41 itens)?
- Revisão de qualidade da Vera foi executada e aprovada (score ≥ 85)?
- Condições bloqueantes da qualificação foram formalmente registradas no TAP?
- Sponsor mínimo Diretor+ está documentado (não apenas mencionado)?

### D4 — Completude da Documentação de Iniciação

Verifica se todos os entregáveis obrigatórios existem e têm conteúdo:
- `01-qualificacao/demanda-coletada.md` — existe e não está vazio?
- `01-qualificacao/qualificacao.md` — existe com pontuação e decisão?
- `01-qualificacao/qualificacao-aprovada.md` — existe com aprovação do GP?
- `02-iniciacao/documentacao-base.md` — existe com TAP + Canvas + Plano Geral?
- `02-iniciacao/requisitos.md` — existe com RF + RNF + MoSCoW?
- `03-planejamento/cronograma.md` — existe com WBS + marcos + caminho crítico?
- `03-planejamento/plano-riscos.md` — existe com mínimo 5 riscos e reserva calculada?
- `03-planejamento/kpis.md` — existe com EVM (CPI, SPI, EAC, VAC)?
- `02-iniciacao/work-request.md` — existe e está completo?
- `04-monitoramento/status-report-*.md` — existe ao menos um?
- `05-encerramento/revisao-final.md` — existe com score ≥ 85?

### D5 — Riscos de Governança não Cobertos

Verifica se o plano de riscos inclui os riscos de governança obrigatórios:
- Risco de sponsor ausente ou sem autoridade suficiente? (se sponsor a definir)
- Risco de orçamento não aprovado? (se CB-02 aberta)
- Risco de mudança de escopo sem controle formal?
- Se algum desses riscos de governança não está no plano → **NC-MOD**

## Process

1. **Verificar D1 (Governança de Sponsor):** Ler qualificacao-aprovada.md e documentacao-base.md. Confirmar sponsor nomeado com cargo Diretor+. Registrar NC-CRÍTICA se ausente.
2. **Verificar D2 (Rastreabilidade):** Comparar os campos críticos (prazo, orçamento, escopo) entre todos os documentos. Registrar cada inconsistência como NC-MOD.
3. **Verificar D3 (Políticas VMO):** Confirmar existência e completude do WR, score da Vera, CBs no TAP.
4. **Verificar D4 (Completude):** Verificar existência de cada arquivo listado. Usar Bash `test -s` para confirmar que não está vazio.
5. **Verificar D5 (Riscos de governança):** Ler plano-riscos.md e confirmar cobertura dos riscos de governança.
6. **Calcular resultado:** Classificar todas as não-conformidades encontradas e emitir veredicto.
7. **Emitir recomendações:** Para cada NC, documentar a ação corretiva, responsável e prazo.

## Classificação de Não-Conformidades

| Tipo | Critério | Impacto |
|------|----------|---------|
| **NC-CRÍTICA** | Sponsor ausente ou abaixo do nível mínimo; ausência de documento obrigatório; score Vera < 85 | **BLOQUEIA** o projeto — não avança para o checkpoint final |
| **NC-MODERADA** | Inconsistência entre documentos; risco de governança não mapeado; CB sem evidência de resolução | Acumulação de 3+ NC-MOD = **BLOQUEIA** |
| **NC-MENOR** | Imprecisões de formato, recomendações de melhoria | Não bloqueia — registrada para ciência |

## Output Format

```markdown
# Auditoria de Governança VMO — [PROJ-CODE]
Data: YYYY-MM-DD | Auditor: Gabriel Governança | Projeto: [nome]

---

## VEREDICTO: [APROVADO ✅ | APROVADO COM RESSALVAS ⚠️ | REPROVADO ❌]

[Justificativa do veredicto em 2-3 linhas]

---

## D1 — Governança de Sponsor

| Item | Status | Evidência | Classificação |
|------|--------|-----------|---------------|
| Sponsor identificado | ✅/❌ | [nome, cargo, documento] | — / NC-CRÍTICA |
| Nível Diretor ou superior | ✅/❌ | [cargo verificado] | — / NC-CRÍTICA |
| CB-01 registrada na qualificação | ✅/❌ | [referência] | — / NC-MOD |
| CB-02 registrada na qualificação | ✅/❌ | [referência] | — / NC-MOD |

## D2 — Rastreabilidade Cross-Document

| Campo | TAP | Canvas | Cronograma | KPIs | WR | Status |
|-------|-----|--------|------------|------|----|--------|
| Prazo | [data] | [data] | [data] | — | [data] | ✅/⚠️ |
| Orçamento | [R$] | [R$] | — | [BAC] | [envelope] | ✅/⚠️ |
| Escopo (módulos) | [M1-M6] | [M1-M6] | [M1-M6] | — | [M1-M6] | ✅/⚠️ |

## D3 — Conformidade com Políticas VMO

| Política | Status | Detalhe |
|----------|--------|---------|
| Work Request emitido | ✅/❌ | [referência ao arquivo] |
| Artefato Obrigatório (10 grupos) | ✅/❌ | [verificação] |
| Score Vera ≥ 85 | ✅/❌ | [score obtido] |
| CBs formalizadas no TAP | ✅/❌ | [seção do TAP] |

## D4 — Completude da Documentação

| Documento | Arquivo | Existe | Conteúdo | Status |
|-----------|---------|--------|----------|--------|
| Demanda Coletada | 01-qualificacao/demanda-coletada.md | ✅/❌ | ✅/❌ | OK / NC |
| [demais documentos] | | | | |

## D5 — Riscos de Governança

| Risco | Coberto no plano | Classificação |
|-------|-----------------|---------------|
| Sponsor ausente/insuficiente | ✅/❌ | — / NC-MOD |
| Orçamento não aprovado | ✅/❌ | — / NC-MOD |
| Mudança de escopo sem CR | ✅/❌ | — / NC-MOD |

---

## Consolidado de Não-Conformidades

| ID | Domínio | Descrição | Tipo | Ação Corretiva | Responsável | Prazo |
|----|---------|-----------|------|----------------|-------------|-------|
| NC-001 | D1 | Sponsor não identificado | CRÍTICA | Identificar Diretor+ responsável | Jadson | [data] |
| [demais NCs] | | | | | | |

**Total NC-CRÍTICAS:** [N] | **Total NC-MOD:** [N] | **Total NC-MENORES:** [N]

---

## Recomendações para a Fase de Execução

[Lista de recomendações proativas para evitar problemas de governança durante a execução]

---

*Auditoria realizada por Gabriel Governança — Auditor de Governança VMO*
*Próximo passo: [encaminhar para o checkpoint final / retornar ao agente responsável pela correção]*
```

## Quality Criteria

- [ ] Todos os 5 domínios auditados com evidência documental
- [ ] Cada NC classificada como CRÍTICA, MODERADA ou MENOR
- [ ] Veredicto claro: APROVADO / APROVADO COM RESSALVAS / REPROVADO
- [ ] Cada NC com ação corretiva, responsável e prazo definidos
- [ ] Rastreabilidade cross-document verificada numericamente (não por impressão)

## Veto Conditions

Rejeitar e refazer se:
1. Algum domínio não foi auditado (verificação parcial não é auditoria)
2. NC-CRÍTICA identificada mas veredicto marcado como APROVADO
3. Alguma NC sem ação corretiva definida
