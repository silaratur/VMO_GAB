ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-008 | Data: 2026-07-07
Analista: Felipe Filtro (VMO Autônomo)

RESUMO:
Três áreas do Grupo Águia Branca (Financeiro, Suprimentos, Gestão de Riscos e Desempenho Organizacional) solicitam, via Alessandra Comério (solicitante formal, Financeiro), a saída de um processo manual de fluxo de caixa e orçamento (Excel + extrações SAP) para uma solução estruturada no TVM — com sponsor Paula Barcelos (CEO). O sizing do Rafael Requisito aponta esforço de 206–334h (Projeto formal), acima do que o orçamento hoje sinalizado (R$30.000–32.000) parece comportar quando somado a licenças, infraestrutura e treinamento. Nenhuma fonte quantificou benefício financeiro. Aprovado com condições — há lacunas de governança (Regra GP 2026-05-24), de viabilidade técnica e de maturidade da frente Financeiro que precisam ser resolvidas antes do TAP.

---

## Claims de Alto Risco Identificados

| Claim | Evidência disponível | Impacto na análise |
|-------|---------------------|--------------------|
| "Sponsor = CEO (Paula Barcelos), aprovação já concedida" | PARCIAL | Confirmado nesta sessão pelo Coordenador PMO (Marcelo Silveira), mas sem evidência documental (e-mail, ata assinada) conforme Regra GP 2026-05-24. Critério 6 rebaixado até formalização. |
| "Orçamento de R$30.000–32.000 já aprovado pela CEO" | PARCIAL | Aprovação de identidade confirmada pelo PMO, mas valor não documentado formalmente e — mais crítico — parece subdimensionado frente ao esforço estimado pelo sizing (ver Análise Comercial). Critério 6 rebaixado. |
| "É urgente" (prazo de 30 dias, "forte urgência sinalizada pela Paula") | PARCIAL | Sem data-alvo concreta (calendário) nem consequência financeira quantificada da não-entrega. Critério 4 com teto aplicado (máx. 4/10 conforme regra). |
| "TVM suporta projeções analíticas por linha e dashboards/BI" | NÃO | Dúvida técnica explicitamente registrada como em aberto nas próprias atas (item de ação pendente com a equipe técnica TVM). Critério 2 rebaixado. |
| "Nenhum requisito legal, regulatório ou contratual identificado" (Thamyris, Wellington) | PARCIAL | Afirmação verbal sem análise formal de compliance/auditoria — dado que o sistema alimenta apresentações à diretoria e contabilidade gerencial, mantém-se nota mínima de cautela no critério 10. |

---

## Critérios de Qualificação

1. Alinhamento Estratégico      6/10
   Evidência disponível: PARCIAL
   A iniciativa se conecta a uma "nova governança de controle de caixa" do grupo (citada por Wellington) e ao uso já consolidado do TVM pela VIX, mas nenhuma fonte cita um OKR ou objetivo estratégico formal e documentado. Confiança: MÉDIA. Teto de 6/10 aplicado (regra: alinhamento genérico sem OKR específico = máximo 6/10).

2. Viabilidade Técnica          5/10
   Evidência disponível: PARCIAL
   Configuração-padrão nos moldes VIX tem precedente técnico (item forte). Porém 5 dos 14 componentes de escopo do sizing (projeções analíticas por linha, dashboards/BI, integração com sistema Atenas, rastreabilidade a nível de nota fiscal, níveis de permissão) têm viabilidade técnica não confirmada pelas próprias fontes. Confiança: BAIXA nesses pontos.
   Para revisar esta nota: confirmação técnica da equipe TVM sobre os 5 itens listados no sizing.md.

3. Retorno sobre Investimento   3/10
   Evidência disponível: NÃO
   Nenhuma das 3 fontes quantificou benefício em R$ ou em horas economizadas — os benefícios descritos (credibilidade, previsibilidade, produtividade) são qualitativos. Sem dado de benefício, não é possível calcular payback real (ver Análise Comercial). Nota reflete ausência de evidência, não pessimismo sobre o valor do projeto.
   Para revisar esta nota: quantificar ao menos um benefício principal (ex.: horas/mês do analista Lucas hoje dedicadas ao processo manual × custo-hora; custo de retrabalho por inconsistência de dados apresentados à diretoria).

4. Urgência                     4/10
   Evidência disponível: PARCIAL
   Prazo declarado de "30 dias" por Thamyris e Wellington, mas a partir de datas de entrevista distintas (02/07 e 03/07) e sem data-alvo de calendário. "Forte urgência sinalizada pela Paula" é citação verbal, sem consequência financeira quantificada da inação. Teto de 4/10 aplicado (regra: urgência sem data concreta e sem custo de inação).

5. Maturidade da Demanda        4/10
   Evidência disponível: PARCIAL
   Duas das 3 frentes (Suprimentos, Riscos/Desempenho) têm escopo razoavelmente claro; a frente Financeiro (Alessandra) permanece com levantamento parcial (prazo, sistemas, critérios de sucesso pendentes — sessão de continuação ainda não realizada). Classificação (projeto vs. melhoria) já resolvida por este parecer, mas isso não estava maduro no intake.

6. Disponibilidade de Recursos  3/10
   Evidência disponível: PARCIAL
   Sponsor com identidade agora confirmada (Paula Barcelos, CEO) pelo PMO, mas sem documento formal de aprovação (Regra GP 2026-05-24). Orçamento sinalizado (R$30-32k) mas não documentado e com forte suspeita de estar subdimensionado frente ao esforço estimado (ver critério 7 e Análise Comercial). Disponibilidade da equipe técnica TVM para o projeto não confirmada por nenhuma fonte.
   Para revisar esta nota: evidência documental da aprovação (CEO) + reconciliação do valor orçado com o esforço estimado + confirmação de disponibilidade da equipe técnica TVM.

7. Esforço Estimado             9/10
   Evidência disponível: SIM
   Sizing.md (Rafael Requisito): levantamento 40–56h + desenvolvimento/configuração 110–190h + testes 32–48h + go-live 24–40h = 206–334h totais. Muito acima do limiar de 160h. Confiança: BAIXA (puxada pelos 5 itens de viabilidade técnica não confirmada), mas mesmo no piso da faixa o esforço já classifica como Projeto.

8. Impacto Organizacional       8/10
   Evidência disponível: SIM
   Impacta diretamente Financeiro, Suprimentos e Gestão de Riscos e Desempenho Organizacional, e indiretamente Contabilidade Gerencial e Alta Direção (consumidora das informações). Mudança de processo real: de consolidação manual em Excel para operação estruturada no TVM, com forte dependência atual concentrada em uma única pessoa (Thamyris) a ser redistribuída.

9. Governança Necessária        8/10
   Evidência disponível: SIM
   Três frentes distintas, sponsor de nível CEO, dependência crítica de uma pessoa-chave, e 5 itens de escopo com viabilidade técnica ainda não confirmada que podem alterar significativamente o cronograma. Isso exige acompanhamento formal de portfólio, não gestão informal por equipe técnica.

10. Impacto Regulatório/Financeiro 5/10
    Evidência disponível: PARCIAL
    Nenhuma fonte identificou requisito legal/regulatório explícito, mas o sistema alimenta diretamente informações de fluxo de caixa e orçamento apresentadas à diretoria e usadas por contabilidade gerencial — erros de segregação de receita ou de rastreabilidade têm potencial impacto em demonstrativos financeiros. Nota mínima de cautela mantida (regra: integrações financeiras merecem ao menos 4/10 pelo risco implícito).

---

PONTUAÇÃO: 55/100 (55%)

**CLASSIFICAÇÃO: PROJETO**
Critérios 7–10 (Esforço 9, Impacto Organizacional 8, Governança 8, Regulatório/Financeiro 5): 3 de 4 pontuam ≥7/10, confirmando a necessidade de gestão de projeto formal. Consistente com a leitura de Wellington ("projeto", não melhoria pontual) e com o sizing do Rafael (206–334h). A leitura inicial de Alessandra ("melhoria de processo") refletia apenas a fatia Financeiro do escopo, sem visibilidade das outras duas frentes.

**DECISÃO: APROVADO COM CONDIÇÕES**
Pontuação de 55% está na faixa 50–74%. As condições abaixo são resolvíveis e não indicam inviabilidade do projeto — indicam maturidade insuficiente para autorizar o TAP hoje.

---

## Condições Bloqueantes

- **CB-1:** Evidência documental (e-mail, ata assinada, comunicado oficial) da aprovação da CEO Paula Barcelos como sponsor — a confirmação verbal do PMO nesta sessão resolve a *identidade*, não a exigência de documentação da Regra GP 2026-05-24.
- **CB-2:** Aprovação formal e documentada de Diretoria da área solicitante (Financeiro) e do Gerente de TI da divisão solicitante — nenhuma das duas está presente em nenhuma fonte (Regra GP 2026-05-24, obrigatória para VALIDAÇÃO da demanda).
- **CB-3:** Reconciliar o orçamento aprovado (R$30.000–32.000) com o esforço estimado pelo sizing (206–334h) — ver Análise Comercial abaixo; há risco real de o valor aprovado não cobrir desenvolvimento + licenças + infraestrutura + treinamento.
- **CB-4:** Concluir a sessão de continuação com Alessandra (frente Financeiro) — prazo, sistemas/integrações, critérios de sucesso e capacidade técnica do TVM para essa frente ainda não levantados.
- **CB-5:** Confirmação técnica da equipe TVM sobre os 5 itens de viabilidade incerta do sizing (projeções analíticas por linha, dashboards/BI, integração com Atenas, rastreabilidade a nota fiscal, níveis de permissão).
- **CB-6:** Quantificação de ao menos um benefício financeiro principal, para permitir cálculo de ROI e payback reais no Termo de Abertura.

---

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Obter evidência documental da aprovação da CEO (sponsor) | Marcelo Silveira (PMO) / Paula Barcelos | Antes do TAP |
| Obter aprovação formal de Diretoria (Financeiro) e Gerente de TI da divisão | PMO / Alessandra Comério | Antes da validação final da demanda |
| Reconciliar orçamento com esforço estimado | Felipe Filtro (PMO) / Cássio (líder técnico) | Antes do TAP |
| Concluir sessão de continuação com Alessandra | Alessandra Comério / PMO | Curto prazo (já registrado como ação pendente desde a Ata 1) |
| Validar viabilidade técnica dos 5 itens do sizing | Equipe técnica TVM | 2 semanas |
| Quantificar ao menos 1 benefício financeiro principal | Alessandra Comério / Thamyris / PMO | Antes do TAP |

---

# ANÁLISE COMERCIAL — Implantação/Expansão do TVM (Fluxo de Caixa e Suprimentos)
Data: 2026-07-07

BENEFÍCIOS ESPERADOS
| Benefício | Valor Estimado | Prazo | Confiança |
|-----------|----------------|-------|-----------|
| Redução de horas manuais de consolidação (Thamyris/analista Lucas) | Não quantificado — nenhuma fonte informou volume de horas/mês | - | BAIXA |
| Maior credibilidade/assertividade dos números à diretoria (Financeiro) | Não quantificado | - | - |
| Visibilidade financeira das compras para Suprimentos (negociação de prazos) | Não quantificado | - | - |
| Previsibilidade de caixa (90 dias) e alertas de consumo orçamentário | Não quantificado | - | - |
Total de benefícios anuais estimados: **NÃO CALCULÁVEL** — nenhuma das 3 fontes forneceu valor monetário ou volume de horas para nenhum benefício. Este é o principal motivo da nota baixa no critério 3 (ROI).

CUSTO DO PROJETO (estimativa preliminar, baseada no sizing do Rafael Requisito)
| Item | Estimativa | Base |
|------|------------|------|
| Desenvolvimento/Implantação | R$ 30.900 – R$ 50.100 | 206–334h × ~R$150/h (taxa de referência para configuração/desenvolvimento TVM — não confirmada com o fornecedor/equipe técnica) |
| Infraestrutura (12 meses) | Não informado — presumível baixo incremental, pois reaproveita instância já utilizada pela VIX | A confirmar com equipe técnica TVM |
| Licenças (usuários adicionais Financeiro/Suprimentos/Riscos) | Não informado | A confirmar |
| Treinamento e change management (3 áreas) | R$ 5.000 – R$ 8.000 (estimativa preliminar) | Estimativa própria — não confirmada |
| Contingência (20%) | R$ 7.180 – R$ 11.620 | Sobre desenvolvimento + treinamento |
TOTAL ESTIMADO: **R$ 43.080 – R$ 69.720** (excluindo infraestrutura e licenças ainda não informadas)

⚠️ **Alerta de reconciliação (CB-3):** o orçamento hoje sinalizado como aprovado (R$30.000–32.000) cobre, na melhor hipótese, apenas o piso da faixa de desenvolvimento (206h) — e nem isso, uma vez somados treinamento e contingência. Nenhuma fonte confirmou se o valor aprovado é apenas para desenvolvimento ou para o projeto como um todo. Este é o ponto de maior risco financeiro identificado nesta qualificação.

MÉTRICAS DE RETORNO
- Payback: **NÃO CALCULÁVEL** — ausência de benefício financeiro quantificado em qualquer fonte.
- ROI em 12 e 24 meses: **NÃO CALCULÁVEL** pelo mesmo motivo.
- Nível de confiança geral: BAIXA (tanto por ausência de dado de benefício quanto por incerteza no custo real).

CUSTO DE NÃO-FAZER
Descrito qualitativamente pelas 3 fontes: manutenção da dependência crítica de poucas pessoas (Thamyris, analista Lucas), continuidade de baixa rastreabilidade de despesas (impedindo validação de números apresentados à diretoria), e ausência de visibilidade financeira das compras para negociação com fornecedores. Nenhuma fonte quantificou este custo em R$ — recomenda-se fazê-lo antes do TAP (CB-6), já que isso fortaleceria significativamente a nota de ROI e de Urgência.

PROPOSTA DE VALOR
"A iniciativa de expansão do TVM para fluxo de caixa e suprimentos no Grupo Águia Branca, com investimento preliminar estimado entre R$43.000 e R$70.000 (a reconciliar com o orçamento de R$30-32k já sinalizado pela CEO), busca substituir um processo hoje inteiramente manual e concentrado em poucas pessoas por uma governança de caixa estruturada e automatizada — nos moldes já validados pela VIX. O retorno financeiro exato ainda não pode ser declarado: nenhuma das 3 entrevistas de discovery quantificou o benefício em reais, o que é a principal lacuna a resolver antes da elaboração do Termo de Abertura."
