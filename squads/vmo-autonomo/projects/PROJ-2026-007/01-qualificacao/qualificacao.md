ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-007
Chamado: 6800446
Data: 2026-05-31 (revisão — critérios 7, 8, 9 corrigidos por falha metodológica na v1)
Analista: Felipe Filtro (VMO Autônomo)
Versão: 2.0

RESUMO:
A Holding DTI / VIX Matriz demanda o desenvolvimento de integração SAP/SGMM03 para transmitir os
dados de "Empresa a Contrato" na abertura de Ordens de Manutenção (OM) no processo InterCompany.
Campo CenPlan com restrição ativa no SAP. Precedente técnico: integração de Centro de Planejamento
entregue. Processo de cotação com 4 consultorias em andamento.
NOTA DE REVISÃO: A versão anterior desta análise cometeu três erros metodológicos: (1) esforço
estimado por benchmark sem dados de requisitos — inválido; (2) impacto organizacional inferido
por "InterCompany" sem confirmar se envolve times distintos; (3) GMUD usado como indicador de
governança de projeto — equivocado, pois GMUD é padrão para qualquer mudança SAP, inclusive
melhorias simples. Os critérios 7, 8 e 9 foram revisados abaixo.
DECISÃO: EM ESPERA — Critério 7 (Esforço) aguarda consulta a Rafael Requisitos para
dimensionamento de esforço baseado em requisitos, não em benchmark.

---

## Claims de Alto Risco Identificados

| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "É similar ao que já existe" (Centro de Planejamento entregue) | PARCIAL — precedente técnico, mas campo CenPlan tem restrição ativa (diferença relevante) | Critério 2: teto 6/10 até confirmação técnica das diferenças |
| "Múltiplas empresas impactadas" (inferência por InterCompany) | NÃO — não confirmado que são times operacionais distintos | Critério 8: não pode ser pontuado alto sem confirmação; InterCompany mesma divisão = mesma área |
| Esforço estimado por benchmark (250-320h) | NÃO — estimativa sem base em requisitos ou proposta formal | Critério 7: EM ESPERA — só Rafael Requisitos pode fornecer estimativa válida |
| GMUD como indicador de projeto | NÃO — GMUD aplica-se a qualquer mudança SAP, inclusive melhorias simples | Critério 9: GMUD não diferencia projeto de melhoria; corrigido |
| Budget disponível | NÃO — nenhuma aprovação formal identificada | Critério 6: nota rebaixada sem sponsor e sem budget |

---

## Critérios de Qualificação

1. Alinhamento Estratégico           6/10
   Evidência disponível: PARCIAL
   A demanda insere-se no projeto maior de Integração SAP + SGM (SGM 003) — iniciativa ativa de
   digitalização da Holding DTI. Contexto InterCompany indica impacto em operações do grupo.
   Porém: nenhum OKR ou objetivo estratégico formal citado nas fontes.
   Para revisar: documento de OKRs ou plano estratégico de TI referenciando o programa SGM 003.
   Confiança: MÉDIA.

2. Viabilidade Técnica               6/10
   Evidência disponível: PARCIAL
   Precedente técnico confirmado: integração de Centro de Planejamento (mesma iniciativa) já entregue.
   Porém: campo CenPlan apresenta restrição ativa no SAP (vermelho) — indica diferença técnica
   relevante em relação ao entregável anterior. Pode exigir configuração específica de permissão
   SAP para o campo CenPlan além da integração padrão.
   Claim "replicação simples" verificado como PARCIAL — restrição de campo não documentada na
   solução anterior. Teto 6/10 aplicado.
   Para revisar: análise técnica das diferenças de implementação entre Centro de Planejamento
   (entregue) e Empresa/Contrato/CenPlan (demandado).
   Confiança: MÉDIA.

3. Retorno sobre Investimento        4/10
   Evidência disponível: NÃO
   Nenhum dado financeiro disponível: custo do projeto aguardando propostas de consultorias.
   Volume de OM InterCompany afetadas não informado. Benefício financeiro da inação não quantificado.
   O processo InterCompany é operacionalmente crítico para o grupo, mas sem dados de volume e
   custo, o ROI não pode ser estimado com confiança acima de BAIXA.
   Para revisar: (a) proposta de consultoria selecionada com valor; (b) volume mensal de OM
   InterCompany afetadas; (c) custo ou impacto estimado do fluxo bloqueado.
   Confiança: BAIXA.

4. Urgência                          6/10
   Evidência disponível: PARCIAL
   SLA do chamado expirado há 81:42h (atraso de ~13 dias além de 15/05/2026). Processo de cotação
   ativo com 4 consultorias. Porém: deadline de GO-LIVE não informado — sem data concreta com
   consequência quantificada da inação.
   Para revisar: data-limite de produção com justificativa de negócio (evento, contrato, auditoria).
   Confiança: MÉDIA.

5. Maturidade da Demanda             5/10
   Evidência disponível: PARCIAL
   Problema técnico bem definido (campos específicos identificados, documento de mapeamento existente).
   Gaps de gestão: sponsor não identificado, budget não aprovado, escopo definitivo dos campos
   não confirmado (risco de expansão para outros campos do mapeamento).
   Confiança: MÉDIA.

6. Disponibilidade de Recursos       3/10
   Evidência disponível: NÃO
   Orçamento: nenhuma aprovação formal documentada. Sponsor executivo: não identificado.
   Sem comprometimento formal de recursos (financeiros ou humanos de nível decisório).
   Para revisar: aprovação formal de budget (CAPEX/OPEX) + sponsor designado com cargo Diretor+.
   Confiança: BAIXA.

7. Esforço Estimado                  EM ESPERA
   Evidência disponível: NÃO
   Não há proposta de consultoria disponível, nem levantamento de requisitos realizado.
   A estimativa anterior desta análise (250-320h por benchmark) foi classificada como inválida:
   o dimensionamento de esforço de uma integração SAP só pode ser feito após o detalhamento
   de requisitos por especialista.
   Ação requerida: consultar Rafael Requisitos para levantamento inicial de escopo e estimativa
   de esforço por fase (levantamento, desenvolvimento, testes, homologação).
   Nota provisória (apenas para cálculo parcial): 3/10 — reflete ausência total de dados;
   a nota deve ser revisada após input de Rafael.
   Para validar: levantamento de requisitos por Rafael Requisitos OU proposta formal de
   consultoria selecionada com estimativa por fase.
   Confiança: NÃO APLICÁVEL.

8. Impacto Organizacional            3/10
   Evidência disponível: NÃO
   A versão anterior inferiu impacto multi-empresa por ser "processo InterCompany". Esta inferência
   estava errada: processos InterCompany de mesma divisão de negócio são operados pelo mesmo
   grupo de pessoas (analistas de manutenção, TI — mesma equipe). VIX Matriz e Holding DTI
   estão dentro do mesmo grupo — sem confirmação de que times operacionais distintos são
   envolvidos, o impacto organizacional é baixo.
   Claim "múltiplas empresas = múltiplas áreas" verificado como NÃO — falta confirmação.
   Para revisar: confirmar quantas equipes operacionais distintas (de diferentes gerências ou
   vice-presidências) precisarão mudar seu processo após a integração.
   Confiança: BAIXA.

9. Governança Necessária             4/10
   Evidência disponível: PARCIAL
   A versão anterior usou GMUD (gestão de mudança SAP, transport request, janela operacional)
   como indicador de necessidade de governança formal. Isso estava errado: GMUD aplica-se a
   QUALQUER mudança SAP — inclusive melhorias simples. Não é critério diferenciador de projeto.
   O que efetivamente indica governança formal: sponsor ausente, múltiplos vendedores gerenciados
   em paralelo, cronograma com go-live de risco e stakeholders de diferentes níveis hierárquicos
   com expectativas divergentes. Estes fatores existem parcialmente aqui (4 consultorias, sponsor
   ausente), mas a gestão de cotação de fornecedor é operação padrão da Holding DTI.
   Para revisar: confirmar se o projeto exige Comitê Diretivo, aprovações fora do DTI ou
   gestão de stakeholders além da VIX Matriz + Holding DTI.
   Confiança: BAIXA-MÉDIA.

10. Impacto Regulatório/Financeiro   6/10
    Evidência disponível: PARCIAL
    InterCompany envolve transações entre empresas do grupo — com impacto potencial em conciliação
    contábil intercompany (FI/CO SAP). Dados incorretos de Empresa/Contrato em OM podem gerar
    divergências em fechamento intercompany. Risco de auditoria interna identificado.
    Sem confirmação de obrigação fiscal ou regulatória externa.
    Para revisar: confirmar impacto no módulo FI/CO e se há obrigação de conformidade externa.
    Confiança: MÉDIA.

---

PONTUAÇÃO PARCIAL: 43/90 (critério 7 em espera, excluído do cálculo — 9 critérios avaliados)
(Se critério 7 = 3/10 provisório: 46/100 = 46%)

**CLASSIFICAÇÃO TENTATIVA: MELHORIA EVOLUTIVA**
Critérios 7–10 revisados: Esforço (EM ESPERA/3), Impacto Org. (3), Governança (4), Regulatório (6).
Nenhum dos critérios 7–10 atingiu ≥ 7/10 com a metodologia corrigida. Sem ao menos 2 critérios
de complexidade confirmando necessidade de gestão formal, a classificação provisória é Melhoria
Evolutiva → time PM/MM (Plant Maintenance / Materials Management) da Sustentação ERP.
ATENÇÃO: Esta classificação é PROVISÓRIA. O critério 7 (Esforço) está EM ESPERA. Se Rafael
Requisitos confirmar esforço > 160h com dados concretos de requisitos, a classificação deve
ser revisada para PROJETO.

**DECISÃO: EM ESPERA**
Aguardando levantamento inicial de esforço por Rafael Requisitos antes de emitir decisão final.
A pontuação atual (46/100) e a classificação provisória (Melhoria Evolutiva) não são definitivas
enquanto o critério 7 não for fundamentado em dados de requisitos.

---

## Condições para Resolução do EM ESPERA

- **P-1:** Rafael Requisitos — realizar levantamento inicial de escopo e estimativa de esforço por fase (levantamento, desenvolvimento/config SAP, testes, homologação). Resposta necessária antes da retomada desta qualificação.
- **P-2:** Confirmar quantas equipes operacionais distintas (diferentes gerências) serão impactadas após a integração — para revisão do critério 8.
- **P-3:** Confirmar se há necessidade de Comitê Diretivo ou aprovações além de DTI/VIX para revisão do critério 9.

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Levantamento inicial de escopo e esforço por Rafael Requisitos | VMO / Rafael Requisitos | 2026-06-07 |
| Confirmar impacto em equipes operacionais distintas | GP VMO + VIX Matriz / DTI | 2026-06-07 |
| Receber propostas das consultorias (prazo já vencido — 29/05) | Mara Rubia / DTI | IMEDIATO |
| Retomar qualificação com dados de P-1, P-2 e P-3 | Felipe Filtro | Após respostas acima |
