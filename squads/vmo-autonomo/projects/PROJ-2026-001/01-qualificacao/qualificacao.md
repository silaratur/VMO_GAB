# Parecer de Qualificação — Inclusão de Aprovador SAP FI Lançamentos Pré-Editados

**ID:** DEM-2026-001
**Data:** 2026-04-03
**Analista:** Felipe Filtro — Analista de Qualificação VMO

---

## ANÁLISE DE QUALIFICAÇÃO DE DEMANDA

```
ID: DEM-2026-001
Data: 2026-04-03

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CRITÉRIOS DE QUALIFICAÇÃO

1. Alinhamento Estratégico    2/5
   O solicitante declarou que a demanda NÃO atende requisito legal ou obrigatório
   e NÃO impacta outras áreas ou divisões. Nenhum OKR ou objetivo estratégico foi
   mencionado. A demanda parece ser pontual e operacional — ajuste de configuração
   de sistema sem conexão declarada com iniciativas estratégicas. Sem sponsor
   identificado para confirmar alinhamento com prioridades corporativas.
   Confiança: BAIXA.

2. Viabilidade Técnica        4/5
   A solução é parametrização interna no SAP, sistema já implantado. As
   transações mencionadas (ZFI0057 e SBWP) são conhecidas no ambiente SAP FI.
   Não há integração com outros sistemas declarada. Tecnicamente é uma mudança
   de configuração de baixa complexidade, desde que o aprovador a ser incluído
   seja identificado. O único bloqueio técnico é a ausência do nome do novo
   aprovador (L11). Confiança: ALTA.

3. Retorno sobre Investimento 1/5
   Todos os campos de ganho foram respondidos como "Não" pelo solicitante:
   sem aumento de receita, sem redução de custo, sem melhoria de processo,
   sem aumento de produtividade. Nenhum indicador de benefício foi declarado.
   A faixa de investimento é baixa (< R$ 10.000), mas sem benefício quantificável
   o ROI é indefinido — impossível calcular payback. O risco de "custo de
   não-fazer" existe (risco de controle interno), mas não foi declarado.
   Confiança: MUITO BAIXA.

4. Urgência                   2/5
   Nenhuma justificativa de urgência foi declarada. O campo específico para
   isso foi deixado em branco. A data da requisição (23/02/2026) e a data atual
   (03/04/2026) indicam 39 dias de espera sem avanço — o que contradiz urgência
   alta. A ausência de prazo e urgência declarados não implica que não existam,
   mas formalmente não há evidência de pressão temporal. Confiança: BAIXA.

5. Maturidade da Demanda      2/5
   O pedido técnico é claro (incluir aprovador no fluxo ZFI0057/SBWP), mas o
   problema de negócio real (L3) não foi declarado. O solicitante não possui
   escopo detalhado, o processo não está documentado, o aprovador a ser incluído
   não está identificado (L11), e o sponsor não foi informado (L9). Dos 12
   campos fundamentais levantados, 12 constam como lacunas — a demanda está
   tecnicamente descrita mas contextualmente vazia. Confiança: BAIXA.

6. Disponibilidade de Recursos 3/5
   O investimento estimado é baixo (< R$ 10.000), dentro de uma faixa operacional
   que normalmente não requer aprovação de comitê. A área de DTI é a executora
   provável. O risco principal não é escassez de recursos, mas ausência de
   autorização formal (sem investimento aprovado e sem sponsor). Parametrizar SAP
   FI requer acesso ao ambiente produtivo e janela de manutenção — recursos
   padrão para DTI. Confiança: MÉDIA.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PONTUAÇÃO: 14/30 (47%)
DECISÃO: EM ESPERA

Justificativa: A pontuação de 47% está abaixo do limiar de reprovação (< 50%),
mas a decisão não é REPROVADO porque a demanda tem viabilidade técnica alta e
custo baixo. O problema é ausência de informação, não falta de mérito. A demanda
aguarda resolução das lacunas críticas antes de nova avaliação.
```

---

## ANÁLISE COMERCIAL

```
BENEFÍCIOS ESPERADOS
| Benefício | Valor Estimado | Prazo | Confiança |
|-----------|----------------|-------|-----------|
| Melhoria de controle interno / segregação de funções | Não quantificado | Imediato | N/A |
| Redução de risco de auditoria (potencial) | Não quantificado | - | BAIXA |
| Conformidade com política interna (potencial) | Não quantificado | - | BAIXA |

Total de benefícios anuais estimados: NÃO QUANTIFICÁVEL com os dados disponíveis.

CUSTO DO PROJETO
| Item | Estimativa |
|------|------------|
| Configuração/parametrização SAP (1-2 dias técnico) | R$ 2.400 – R$ 4.800 |
| Testes e validação | R$ 800 – R$ 1.600 |
| Documentação mínima | R$ 400 – R$ 800 |
| Contingência (20%) | R$ 720 – R$ 1.440 |
TOTAL ESTIMADO: R$ 4.320 – R$ 8.640

MÉTRICAS DE RETORNO
- Payback: INCALCULÁVEL — nenhum benefício financeiro declarado
- ROI em 12 meses: INDEFINIDO
- ROI em 24 meses: INDEFINIDO
- Nível de confiança geral: BAIXA

CUSTO DE NÃO-FAZER
Se motivação for controle interno / segregação de funções:
→ Risco de não-conformidade em auditoria interna ou externa
→ Potencial de fraude ou erro não detectado nos lançamentos FI
→ Custo de achados de auditoria tipicamente superior a R$ 10.000 em correção

Se motivação for operacional (ex: troca de responsável):
→ Bloqueio operacional na aprovação de lançamentos
→ Custo de horas paradas ou workaround manual não mensurado

PROPOSTA DE VALOR (condicional — aguarda confirmação de L3)
"A inclusão de um aprovador adicional no fluxo de lançamentos pré-editados
do SAP FI, com investimento estimado entre R$ 4.320 e R$ 8.640, mitiga o
risco de controle interno atualmente existente no processo de aprovação e
garante a continuidade operacional. O valor estratégico depende da confirmação
do motivo real que originou esta demanda (L3)."
```

---

## CONDIÇÕES BLOQUEANTES (EM ESPERA)

| # | Condição | Ação Requerida | Responsável | Prazo |
|---|----------|----------------|-------------|-------|
| C1 | Motivação real da demanda não declarada (L3) | Entrevistar solicitante para identificar o problema de negócio | Analista PMO | A definir |
| C2 | Sponsor / Gestor responsável não identificado (L9) | Identificar e designar sponsor com autoridade para aprovar | Analista PMO | A definir |
| C3 | Aprovador a incluir não nomeado (L11) | Confirmar quem será o aprovador adicionado ao fluxo | Solicitante | A definir |
| C4 | Benefício esperado não declarado (L4) | Obter declaração de benefício, mesmo que qualitativo | Solicitante | A definir |

---

## PRÓXIMOS PASSOS

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Contatar Ivanilde Ribeiro Machado para esclarecimento das 4 condições bloqueantes | Analista PMO | A definir |
| Reagendar qualificação após retorno do solicitante | Felipe Filtro | Após C1–C4 |
| Se motivação for controle interno: elevar para parecer de conformidade | PMO Corporativo | Após C1 |
| Se motivação for operacional: qualificar como demanda de baixa complexidade (provável APROVADO COM CONDIÇÕES) | Felipe Filtro | Após C1 |

---

*Parecer emitido por Felipe Filtro — Analista de Qualificação | VMO Autônomo Squad*
*Versão 1.0 — 2026-04-03 — Status: EM ESPERA (aguarda resolução de C1–C4)*
