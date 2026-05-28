ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-008
Data: 2026-05-28
Analista: Felipe Filtro (VMO Autônomo)

RESUMO:
A VIX Matriz solicita a integração dos campos "Empresa" e "Contrato" da Ordem de Manutenção (OM)
no fluxo InterCompany da interface SGMM03 (SAP + SGM). Atualmente, esses dados inseridos no SGM
durante a abertura de OM não são transmitidos automaticamente ao SAP, obrigando operadores a
preencherem manualmente os campos Empresa e Contrato no SAP — gerando retrabalho e risco de
inconsistência entre os sistemas. A demanda é técnica e cirúrgica: integrar dois campos específicos
em uma interface já existente, para os eventos de criação E alteração de OM. Existe precedente
técnico positivo: o campo Centro de Planejamento foi implementado anteriormente na mesma interface.
O ticket está em atraso de SLA (81h42min) e 4 consultorias estão em processo de precificação
com retorno esperado em 29/05/2026.

---

## Claims de Alto Risco Identificados

| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "Mesma interface SGMM03 já existente — é integração incremental" | PARCIAL — precedente do Centro de Planejamento confirmado, mas escopo técnico dos campos Empresa/Contrato não documentado em detalhe | Critério 2 (Viabilidade Técnica): teto rebaixado para 7/10 até especificação técnica pelos fornecedores |
| "Campo Cenário/CenPlan tem restrição técnica conhecida" | SIM — mencionado no mapeamento técnico como campo crítico com restrição | Risco técnico documentado; não afeta escopo desta demanda mas impacta análise de complexidade |
| Orçamento em precificação — sem valor aprovado | SIM — explicitamente não aprovado, 4 consultorias em cotação | Critério 6 (Recursos): nota máxima 5/10 — orçamento não formalizado |
| Sponsor não identificado | SIM — lacuna L2 explicitamente documentada | Critério 6 e CB-Sponsor: condição bloqueante obrigatória |

---

## Critérios de Qualificação

1. Alinhamento Estratégico          7/10
   Evidência disponível: PARCIAL
   A demanda está alinhada com a diretriz geral de integridade de dados e eficiência operacional
   do processo de manutenção. O fluxo InterCompany SGMM03 é parte da operação crítica da VIX Matriz.
   Não foi apresentado OKR ou objetivo estratégico documentado explicitamente — porém a lógica de
   completar a integração de uma interface já existente tem alinhamento implícito alto.
   Confiança: MÉDIA. Para revisar esta nota: confirmar se há diretriz de digitalização/integração
   do processo PM documentada para VIX Matriz em 2026.

2. Viabilidade Técnica              7/10
   Evidência disponível: PARCIAL
   A interface SGMM03 já existe e opera. O campo Centro de Planejamento foi implementado
   anteriormente nesta mesma interface — precedente técnico positivo confirmado. A adição dos
   campos Empresa e Contrato segue o padrão já estabelecido. Existem 4 consultorias em processo
   de precificação, indicando maturidade do processo de contratação. O campo Cenário/CenPlan tem
   restrição técnica identificada — não é desta demanda, mas revela que a interface tem
   complexidades. Teto 7/10 aplicado até especificação técnica formal ser validada pelos fornecedores.
   Confiança: MÉDIA. Para revisar: especificação técnica dos campos Empresa e Contrato nas BAPIs/RFCs
   SAP do módulo PM e validação do ambiente (mandante/versão).

3. Retorno sobre Investimento       5/10
   Evidência disponível: NÃO
   Benefícios são descritos qualitativamente: eliminação de retrabalho manual, redução de
   inconsistências de dados. Não há quantificação de volume (OMs/mês), tempo médio de retrabalho
   por OM, ou estimativa financeira do benefício. Custo também não foi formalizado (em precificação).
   Payback não calculável com dados disponíveis. Confiança: BAIXA.
   Para revisar: volume mensal de OMs InterCompany afetadas (lacuna L5) e estimativa de tempo de
   retrabalho por OM para calcular benefício anual.

4. Urgência                         4/10
   Evidência disponível: NÃO
   O ticket está em atraso de SLA (81h42min desde 15/05/2026), mas isso reflete urgência de
   processo interno de PMO/DTI, não urgência de negócio. Não há data concreta vinculada a evento
   de negócio (auditoria, contrato, go-live de outro sistema). A presença de 4 consultorias em
   cotação indica processo organizado, não emergência. O impacto da inação é retrabalho operacional
   contínuo, sem ruptura de processo declarada.
   Para elevar a nota: identificar se existe evento de negócio (auditoria, entrega contratual,
   go-live) que exige esta entrega até uma data específica.

5. Maturidade da Demanda            6/10
   Evidência disponível: PARCIAL
   O problema está bem definido — integrar dois campos específicos (Empresa e Contrato) em uma
   interface existente (SGMM03). A existência do documento "Mapeamento_SGMM03_InterCompany.pdf"
   indica nível de detalhamento acima da média para uma demanda inicial. Gaps: cargo da solicitante
   não confirmado, sponsor não identificado, orçamento não definido, volume de impacto não levantado,
   detalhamento técnico dos campos não formalizado em especificação.
   Confiança: MÉDIA.

6. Disponibilidade de Recursos      4/10
   Evidência disponível: NÃO
   Orçamento em fase de precificação — não aprovado formalmente. Sponsor com nível Diretor+
   não identificado. 4 consultorias externas estão sendo avaliadas, o que indica disponibilidade
   de mercado, mas sem commitments formais. Equipe interna de DTI (Mara Rubia) está gerenciando
   o processo, mas não há designação formal de analista técnico interno.
   Para elevar a nota: formalização de orçamento aprovado e designação de sponsor.

7. Esforço Estimado                 5/10
   Evidência disponível: NÃO
   Não há estimativa formal disponível. Com base no precedente de Centro de Planejamento (mesma
   interface, campo único) e no escopo desta demanda (2 campos, criação + alteração), estimativa
   inferida por analogia: levantamento técnico (~16h) + configuração/desenvolvimento (~40h) +
   testes em ambiente de desenvolvimento e QA (~24h) + validação e go-live (~8h) = ~88h totais.
   Nota 5/10 por incerteza — sem estimativa formal por fase dos fornecedores. Confiança: BAIXA.
   Para revisar: aguardar propostas das consultorias com estimativa de esforço por fase.

8. Impacto Organizacional           4/10
   Evidência disponível: PARCIAL
   O impacto é declarado como circunscrito à integração SGMM03 para OMs InterCompany da VIX Matriz.
   Contudo, a lacuna L4 levanta dúvida relevante: outras empresas/áreas usam o mesmo fluxo
   InterCompany? O ticket não declara impacto em outras divisões. Pela natureza de um fluxo
   InterCompany, há probabilidade de impacto em pelo menos a empresa parceira no fluxo.
   A mudança de processo é baixa (automatização de preenchimento manual existente).
   Nota 4/10 pela incerteza sobre abrangência do fluxo InterCompany.

9. Governança Necessária            4/10
   Evidência disponível: PARCIAL
   O esforço estimado (~88h) e o escopo técnico restrito (2 campos em interface existente) indicam
   que a demanda pode ser gerida com governança leve — não requer gestão de projeto formal completa
   com PMO. O processo de cotação com múltiplas consultorias adiciona necessidade de gestão
   comercial, mas a execução técnica em si é de baixa complexidade governamental.
   Nota 4/10 — governança de melhoria, não de projeto.

10. Impacto Regulatório/Financeiro  4/10
    Evidência disponível: PARCIAL
    Os campos Empresa e Contrato em OMs InterCompany têm relevância para alocação de custos e
    controle financeiro entre empresas do grupo (natureza InterCompany). Inconsistência nestes
    campos pode gerar erros em relatórios financeiros intercompany e eventuais problemas de
    reconciliação contábil. Não há risco regulatório externo declarado, mas o impacto contábil
    interno justifica nota acima de 2.

---

PONTUAÇÃO: 50/100 (50%)

**CLASSIFICAÇÃO: MELHORIA EVOLUTIVA**
Critérios 7–10 de complexidade: esforço estimado (5/10), impacto organizacional (4/10),
governança necessária (4/10), impacto regulatório (4/10) — nenhum atinge 7/10 individualmente.
O escopo é restrito (2 campos em interface existente), com esforço estimado abaixo de 160h e
sem mudança estrutural de processo. A demanda segue o padrão de melhoria incremental em
integração SAP existente.

**Time de Sustentação ERP indicado: PM (Plant Maintenance / Manutenção)**
A integração SGMM03 é parte do módulo PM do SAP — os campos Empresa e Contrato em OMs são
objetos do módulo PM integrado ao módulo FI (para alocação de custos InterCompany).
Time recomendado: **PM / FI** — dado o caráter intercompany dos campos, recomenda-se
participação do time de FI na validação dos campos de custo.

**DECISÃO: APROVADO COM CONDIÇÕES**
Pontuação de 50/100 (50%) — limiar mínimo para aprovação com condições.
A demanda é técnica, viável e tem precedente positivo. As condições bloqueantes são resolvíveis
no curto prazo (aguardar propostas dos fornecedores em 29/05 e identificar sponsor).

---

## Condições Bloqueantes

- **CB-1 — CB-Sponsor:** Identificar e nomear sponsor com nível Diretor ou superior para esta
  demanda. Atualmente não há sponsor declarado — Mara Rubia (Holding DTI) é gestora do chamado,
  mas não tem autoridade de sponsor executivo. Requerido antes da emissão do TAP.

- **CB-2 — CB-Orçamento:** Formalizar orçamento aprovado após recebimento e equalização das
  propostas em 29/05/2026. O TAP não pode ser finalizado sem envelope de orçamento aprovado.

- **CB-3 — Escopo Técnico Formal:** Confirmar o escopo técnico dos campos Empresa e Contrato
  junto com a consultora selecionada — incluindo o comportamento esperado na criação e na
  alteração de OM. Esta condição é de menor impacto, mas necessária antes do kick-off.

## Análise Comercial

**BENEFÍCIOS ESPERADOS**
| Benefício | Valor Estimado | Prazo | Confiança |
|-----------|----------------|-------|-----------|
| Eliminação de retrabalho manual (Empresa+Contrato) | Não quantificado — estimado 5-10 min/OM | Imediato ao go-live | BAIXA |
| Redução de inconsistências de dados entre SGM e SAP | Não quantificado | Imediato | BAIXA |
| Agilidade no processo InterCompany de manutenção | Não quantificado | Imediato | BAIXA |
Total de benefícios anuais estimados: **Não quantificável com dados atuais**

**CUSTO DO PROJETO (estimativa referencial — aguardar propostas 29/05)**
| Item | Estimativa Referencial |
|------|------------------------|
| Desenvolvimento/Configuração SAP (consultoria) | R$ 15.000 – R$ 40.000 |
| Testes e validação | Incluído na consultoria |
| Gestão interna (DTI) | Custo de oportunidade — sem desembolso |
| Contingência (20%) | R$ 3.000 – R$ 8.000 |
**TOTAL REFERENCIAL: R$ 18.000 – R$ 48.000** (aguardar propostas para precisar)

**CUSTO DE NÃO-FAZER**
Manutenção indefinida do retrabalho manual para cada OM InterCompany aberta/alterada na
VIX Matriz. O impacto aumenta proporcionalmente ao volume de OMs. Risco de inconsistência
de dados nos campos Empresa/Contrato pode gerar erros em relatórios financeiros InterCompany.

**PROPOSTA DE VALOR**
"A integração dos campos Empresa e Contrato na interface SGMM03 elimina o retrabalho manual
no processo de abertura e alteração de Ordens de Manutenção InterCompany na VIX Matriz,
garantindo consistência automática dos dados entre SGM e SAP. Com investimento estimado entre
R$ 18k e R$ 48k (aguardar propostas) e aproveitamento da interface SGMM03 já implantada,
o projeto é de baixo risco técnico e alto impacto operacional para a equipe de manutenção."

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Receber e equalizar propostas das 4 consultorias | Mara Rubia (Holding DTI) | 29/05/2026 |
| Identificar e nomear sponsor com nível Diretor+ | PMO / Holding DTI | 30/05/2026 |
| Formalizar orçamento aprovado pós-equalização | Sponsor designado | 02/06/2026 |
| Emitir Work Request formal para consultoria selecionada | PMO (Fábio Fornecedor) | 03/06/2026 |
| Iniciar elaboração do TAP e ERF | Diana Documento / Rafael Requisito | 04/06/2026 |
