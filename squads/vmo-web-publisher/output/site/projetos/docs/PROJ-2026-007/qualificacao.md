ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-007
Chamado: 6800446
Data: 2026-05-31
Analista: Felipe Filtro (VMO Autônomo)
Versão: 3.0 — FINAL (critério 7 atualizado com sizing de Rafael Requisito)

RESUMO:
A Holding DTI / VIX Matriz demanda o desenvolvimento de integração SAP/SGMM03 para transmitir os
dados de "Empresa a Contrato" na abertura de Ordens de Manutenção (OM) no processo InterCompany.
Campo CenPlan com restrição ativa no SAP. Precedente técnico: integração de Centro de Planejamento
entregue. Processo de cotação com 4 consultorias em andamento.

HISTÓRICO DE VERSÕES:
- v1.0 (reprovada por Oscar): 3 erros metodológicos — esforço por benchmark, impacto intercompany
  inferido sem confirmação, GMUD como indicador de projeto.
- v2.0 (EM ESPERA): critérios 7/8/9 corrigidos; critério 7 aguardando Rafael Requisito.
- v3.0 (FINAL): critério 7 atualizado com sizing.md de Rafael Requisito (esforço por fase).

DECISÃO FINAL: APROVADO COM CONDIÇÕES — Classificação: MELHORIA EVOLUTIVA
Condições: (a) escopo de campos confirmado; (b) sponsor executivo designado antes de
qualquer contratação; (c) revisão para PROJETO se esforço ampliado (>160h) for confirmado.

---

## Claims de Alto Risco Identificados

| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "É similar ao que já existe" (Centro de Planejamento entregue) | PARCIAL — precedente técnico, campo CenPlan tem restrição ativa (diferença relevante) | Critério 2: teto 6/10 até confirmação técnica |
| "Múltiplas empresas impactadas" (inferência por InterCompany) | NÃO confirmado — InterCompany mesma divisão = mesma área operacional | Critério 8: 3/10 — não pode ser alto sem confirmação de times distintos |
| Esforço por benchmark | INVÁLIDO — substituído por sizing.md de Rafael Requisito | Critério 7: 6/10 escopo mínimo, condicional 7/10 escopo ampliado |
| GMUD como indicador de projeto | INVÁLIDO — GMUD aplica-se a qualquer mudança SAP | Critério 9: 4/10 — GMUD não diferencia projeto de melhoria |
| Budget disponível | NÃO — nenhuma aprovação formal identificada | Critério 6: 3/10 — sem sponsor e sem budget formalizados |

---

## Critérios de Qualificação

1. Alinhamento Estratégico           6/10
   Evidência: PARCIAL
   A demanda faz parte do projeto maior Integração SAP + SGM (SGM 003) — iniciativa ativa de
   digitalização da Holding DTI. O contexto InterCompany indica impacto em operações do grupo.
   Porém: nenhum OKR ou objetivo estratégico formal citado nas fontes disponíveis.
   Para revisar: documento de OKRs ou plano estratégico TI referenciando o programa SGM 003.
   Confiança: MÉDIA.

2. Viabilidade Técnica               6/10
   Evidência: PARCIAL
   Precedente técnico confirmado: integração de Centro de Planejamento (mesma iniciativa) já entregue.
   Porém: campo CenPlan apresenta restrição ativa no SAP (vermelho) — indica diferença técnica
   relevante; pode exigir configuração adicional de autorização SAP além da integração padrão.
   Claim "replicação simples" verificado como PARCIAL — teto 6/10 aplicado.
   Para revisar: análise técnica das diferenças entre integração Centro de Planejamento (entregue)
   e Empresa/Contrato/CenPlan (demandado). Confirmação de como remover restrição do CenPlan.
   Confiança: MÉDIA.

3. Retorno sobre Investimento        4/10
   Evidência: NÃO
   Nenhum dado financeiro disponível: custo do projeto aguardando propostas de consultorias.
   Volume de OM InterCompany afetadas não informado. Benefício da inação não quantificado.
   O processo InterCompany é operacionalmente crítico, mas sem dados de volume e custo, o ROI
   não pode ser estimado com confiança.
   Para revisar: (a) proposta de consultoria selecionada com valor; (b) volume mensal de OM
   InterCompany afetadas; (c) custo/impacto do fluxo bloqueado atual.
   Confiança: BAIXA.

4. Urgência                          6/10
   Evidência: PARCIAL
   SLA do chamado expirado há 81:42h (atraso ~13 dias além de 15/05/2026). Processo de cotação
   ativo com 4 consultorias. Porém: deadline de GO-LIVE não informado — sem data concreta com
   consequência quantificada da inação.
   Para revisar: data-limite de produção com justificativa de negócio (evento, contrato, auditoria).
   Confiança: MÉDIA.

5. Maturidade da Demanda             5/10
   Evidência: PARCIAL
   Problema técnico bem definido (campos específicos, documento de mapeamento existente).
   Gaps: sponsor ausente, budget não aprovado, escopo definitivo dos campos não confirmado
   (risco de expansão de 3 para 8+ campos do mapeamento).
   Confiança: MÉDIA.

6. Disponibilidade de Recursos       3/10
   Evidência: NÃO
   Orçamento: nenhuma aprovação formal documentada. Sponsor executivo: não identificado.
   Sem comprometimento formal de recursos financeiros ou humanos de nível decisório.
   Para revisar: aprovação formal de budget (CAPEX/OPEX) + sponsor com cargo Diretor+.
   Confiança: BAIXA.

7. Esforço Estimado                  6/10
   Evidência: SIM (sizing.md — Rafael Requisito, 2026-05-31)
   Sizing inicial por Rafael Requisito com base no escopo mapeado da demanda validada:

   ESCOPO MÍNIMO (3 campos: Empresa, Contrato, CenPlan):
   - F1 Requisitos:          8–16h
   - F2 Design Técnico:      16–24h
   - F3 Desenvolvimento SAP: 48–96h
   - F4 Testes:              24–40h
   - F5 Deploy/GMUD:          8–16h
   - TOTAL:                 104–192h → Classificação: MÉDIO (80–160h) — ponto médio 148h

   ESCOPO AMPLIADO (8+ campos do mapeamento):
   - TOTAL:                 144–272h → Classificação: GRANDE (>160h)

   Confiança do sizing: BAIXO-MÉDIO (±40%) — pré-elicitação formal de requisitos.
   Nota de Rafael para este critério: "Se o critério 7 for determinante para PROJETO vs. MELHORIA,
   registrar o intervalo e marcar como condicionante do escopo confirmado."

   Pontuação por escopo:
   - Escopo mínimo (MÉDIO, ~148h): 6/10
   - Escopo ampliado (GRANDE, ~200h): 7/10

   Nota pontuação aplicada: 7/10 — ESCOPO AMPLIADO CONFIRMADO PELO USUÁRIO NO CHECKPOINT.
   O usuário confirmou no Checkpoint Step 9 que o escopo real cobre os 8+ campos do mapeamento,
   não apenas os 3 campos (Empresa/Contrato/CenPlan) do chamado.
   Confiança: ALTA (escopo confirmado diretamente pelo responsável técnico).

8. Impacto Organizacional            3/10
   Evidência: NÃO
   A versão v1 inferiu impacto multi-empresa por ser "processo InterCompany". Esta inferência
   estava errada: processos InterCompany de mesma divisão de negócio são operados pelo mesmo
   grupo de pessoas. VIX Matriz e Holding DTI estão no mesmo grupo — sem confirmação de que
   times operacionais distintos (diferentes gerências/vice-presidências) são envolvidos, o
   impacto organizacional é baixo.
   Para revisar: confirmar quantas equipes operacionais distintas precisarão mudar seu processo
   após a integração — se for confirmado mais de uma gerência distinta, revisar para 6-7/10.
   Confiança: BAIXA.

9. Governança Necessária             4/10
   Evidência: PARCIAL
   A versão v1 usou GMUD como indicador de governança formal — equivocado. GMUD aplica-se a
   QUALQUER mudança SAP, inclusive melhorias simples. Não diferencia projeto de melhoria.
   Fatores que efetivamente indicam governança formal neste caso: 4 consultorias gerenciadas
   em paralelo e sponsor ausente. A gestão de cotação de fornecedor é, porém, operação padrão
   da Holding DTI (não requer Comitê Diretivo específico).
   Para revisar: confirmar se o projeto exige Comitê Diretivo, aprovações fora do DTI ou gestão
   de stakeholders além de VIX Matriz + Holding DTI.
   Confiança: BAIXA-MÉDIA.

10. Impacto Regulatório/Financeiro   6/10
    Evidência: PARCIAL
    InterCompany envolve transações entre empresas do grupo — com impacto potencial em conciliação
    contábil intercompany (FI/CO SAP). Dados incorretos de Empresa/Contrato em OM podem gerar
    divergências em fechamento intercompany e risco de auditoria interna.
    Sem confirmação de obrigação fiscal ou regulatória externa.
    Para revisar: confirmar impacto no módulo FI/CO e se há obrigação de conformidade externa.
    Confiança: MÉDIA.

---

PONTUAÇÃO FINAL: 50/100 = 50%

Detalhamento:
  Valor (critérios 1–6):         6 + 6 + 4 + 6 + 5 + 3 = 30/60
  Complexidade (critérios 7–10): 7 + 3 + 4 + 6 = 20/40

  [Atualização Checkpoint Step 9: critério 7 revisado de 6→7/10 com escopo ampliado confirmado]

Critérios de complexidade ≥ 7/10: 1 (Critério 7 = 7/10)
Limiar PROJETO: mínimo 2 critérios de complexidade (7–10) com nota ≥ 7/10
→ Limiar NÃO ATINGIDO — apenas 1 critério atingiu ≥7.

CLASSIFICAÇÃO: MELHORIA EVOLUTIVA
→ Encaminhar para time de Sustentação ERP (PM/MM) ou iniciativa de evolução SAP.

NOTA: Para atingir o limiar PROJETO, é necessário que ao menos 1 dos critérios 8, 9 ou 10
também atinja ≥7/10. Com os dados disponíveis:
  - Critério 8 (3/10): precisaria de confirmação de times operacionais distintos (≥2 gerências)
  - Critério 9 (4/10): precisaria de confirmação de Comitê Diretivo ou aprovações fora do DTI
  - Critério 10 (6/10): precisaria de confirmação de obrigação fiscal/regulatória externa

DECISÃO: APROVADO COM CONDIÇÕES

Condições obrigatórias antes de avanço:
- C1: Designar sponsor executivo (Diretor+) antes de qualquer aprovação de contratação
- C2: Confirmar se times operacionais distintos (diferentes gerências) são impactados — pode
  elevar critério 8 e mudar classificação para PROJETO
- C3: Confirmar nível de governança exigido (Comitê Diretivo?) — pode elevar critério 9

---

## Resumo de Lacunas para Próxima Etapa

| # | Lacuna | Impacto | Ação |
|---|--------|---------|------|
| L1 | Escopo de campos (3 vs. 8+) | Alto — pode mudar classificação para PROJETO | Confirmar com Jenifer/VIX Matriz |
| L2 | Sponsor executivo | Alto — sem sponsor não há aprovação de budget | Identificar com Mara Rubia / DTI |
| L3 | Budget formal | Alto — sem aprovação formal, contratação em risco | Necessário antes de seleção de consultoria |
| L4 | Times operacionais distintos | Médio — pode elevar critério 8 para 6-7/10 | Mapear áreas impactadas após go-live |
| L5 | Restrição CenPlan (natureza) | Médio — impacta F2 e F3 do sizing | Investigação técnica SAP (4h estimadas) |
