ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-007
Ticket: #6700943
Data: 2026-05-20
Analista: Felipe Filtro (VMO Autônomo)

---

## Resumo da Demanda

A área financeira da VAB Matriz solicita a automação da importação do DDA (Débito Direto Autorizado)
no SAP, eliminando o processo manual de impressão de boletos e digitação de código de barras.
A solução equivalente já está implantada na Divisão Logística do mesmo ambiente GAB e na unidade VIX,
tornando o caso de reaproveitamento técnico muito favorável. A integração envolve SAP x Santander.

---

## Critérios de Qualificação

### Valor da Demanda

1. Alinhamento Estratégico        6/10
   Demanda alinhada com objetivos genéricos de digitalização e eficiência operacional em processos
   financeiros. Sem OKR ou diretriz estratégica explicitamente declarada pelo solicitante. Confiança: MÉDIA.
   A ausência de ancoragem em objetivo formal limita a nota — a demanda tem valor, mas não foi
   posicionada estrategicamente pelo solicitante.

2. Viabilidade Técnica            8/10
   Alta viabilidade técnica. A integração SAP x Santander já foi desenvolvida, homologada e está
   em produção na Divisão Logística (mesmo ambiente GAB). A VIX também opera a solução.
   O risco técnico é muito baixo: reaproveitamento direto de interface bancária existente, com
   adaptação mínima para a conta/CNPJ da VAB Matriz. Nenhuma dependência tecnológica nova identificada.

3. Retorno sobre Investimento     7/10
   Investimento estimado abaixo de R$10K com retorno em eliminação de retrabalho (impressão,
   digitação, solicitação a terceiros) e ganho de autonomia no processo de pagamento.
   Payback estimado: 2 a 4 meses, assumindo 20–30 min/dia eliminados de retrabalho operacional.
   Confiança: MÉDIA — sem dados de volume de boletos ou custo-hora declarados pelo solicitante.

4. Urgência                       5/10
   O ticket está em atraso há 204h em relação ao SLA (aberto em 07/04, prazo era 15/04). Contudo,
   a própria área classificou a criticidade como "3 - Normal" e não houve impacto em receita ou
   operação declarado. Custo de inação é real (desgaste contínuo) mas sem ruptura de processo.
   Sem prazo externo, evento crítico ou obrigação legal. Urgência moderada.

5. Maturidade da Demanda          4/10
   Demanda pouco madura em termos de documentação. Descrição da solicitação tem apenas 1 linha.
   Processo atual não está documentado: sem dados de volume de boletos, sem identificação de
   quem executa o processo manual, sem especificação do escopo (quais tipos de DDA: fornecedores,
   tributos, outras cobranças). A referência à Divisão Logística indica que a solução é conhecida,
   mas a demanda em si carece de detalhamento mínimo. Gap crítico: sem escopo, a execução pode
   sofrer escorregamento de prazo e expectativas.

6. Disponibilidade de Recursos    4/10
   Orçamento não aprovado — condição bloqueante. Sem responsável designado no ticket.
   O valor estimado (< R$10K) é baixo e tecnicamente aprovável em caráter de urgência,
   mas o processo formal de aprovação não foi iniciado. Conflito de portfólio não identificado,
   o que é positivo, mas não compensa a ausência de aprovação orçamentária.

### Complexidade de Execução

7. Esforço Estimado               3/10
   Estimativa: 80–120 horas totais (levantamento + configuração SAP + testes + go-live).
   Abaixo do limiar de 160h que define projeto formal. Essa estimativa baseia-se no alto grau
   de reaproveitamento da solução da Divisão Logística — configuração de interface bancária CNAB,
   adaptação para CNPJ/conta da VAB Matriz e validação com Santander. Esforço baixo, adequado
   para sustentação.

8. Impacto Organizacional         3/10
   Impacto restrito à área financeira/contas a pagar da VAB Matriz. O próprio solicitante
   declarou que o projeto não envolve nem impacta outras áreas ou divisões de negócio.
   Mudança de processo é pontual: elimina etapa manual sem redefinir estrutura operacional,
   papéis ou responsabilidades de forma relevante. Nenhum treinamento significativo esperado.

9. Governança Necessária          3/10
   Não requer comitê de acompanhamento, cronograma formal extenso ou gestão de múltiplos
   stakeholders. Trata-se de replicação de solução já homologada no mesmo ambiente. O time
   de sustentação FI pode gerenciar autonomamente com acompanhamento básico do solicitante.
   Não há dependências externas complexas além da confirmação com o Santander.

10. Impacto Regulatório/Financeiro  4/10
    A integração bancária (CNAB/EDI com Santander) é padrão no setor e já homologada.
    Sem requisito legal ou obrigação regulatória específica declarada. O impacto é no processo
    operacional de pagamento — não em demonstrativos financeiros, obrigações fiscais ou
    auditorias. Risco regulatório baixo.

---

## Resultado

**PONTUAÇÃO TOTAL: 47/100 (47%)**

**CLASSIFICAÇÃO: MELHORIA EVOLUTIVA**
Os critérios de complexidade (7–10) confirmam: nenhum dos quatro pontua ≥ 7/10. Esforço abaixo
de 160h, impacto restrito a uma área, sem governança formal necessária. Não caracteriza projeto.
A demanda é uma melhoria evolutiva no processo de pagamento — replicação de solução existente
com adaptação mínima.
→ Time de Sustentação ERP responsável: **FI** (Financeiro — Contas a Pagar / Integração Bancária)

**DECISÃO: EM ESPERA**
A pontuação total (47%) está abaixo do limiar de 50% para aprovação. Os fatores que
penalizam a nota — maturidade baixa (4/10) e recursos não aprovados (4/10) — são
resolvíveis em prazo curto. A demanda tem mérito técnico e precedente interno claro.
Recomendo resubmissão após resolução das condições listadas abaixo.

---

## Condições Bloqueantes

1. **Aprovação formal do orçamento** (< R$10K, CC 200195148) — sem aprovação financeira,
   o time de sustentação não pode iniciar a execução.
2. **Designação de responsável técnico** pelo time Projetos DTI — ticket sem responsável atribuído
   há 43 dias.
3. **Documentação mínima do processo atual** — quem executa, volume de boletos/mês, tipos de
   DDA a contemplar (fornecedores, tributos, outros). Sem isso, o escopo não pode ser fechado.

## Condições Desejáveis (não bloqueantes)

- Confirmação com o Santander de que a conta da VAB Matriz está habilitada para DDA
- Identificação do responsável técnico da Divisão Logística que implementou a solução original,
  para transferência de conhecimento

---

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Aprovar orçamento < R$10K (CC 200195148) | Lucas Medeiros / Financeiro VAB | 2026-05-27 |
| Designar responsável técnico no Projetos DTI | Gestão Projetos DTI | 2026-05-22 |
| Documentar processo atual e volume de boletos | Lucas Medeiros | 2026-05-27 |
| Confirmar habilitação DDA no Santander (VAB Matriz) | Lucas Medeiros / Banco | 2026-05-27 |
| Resubmeter demanda para qualificação final | Felipe Filtro / VMO | Após condições |
