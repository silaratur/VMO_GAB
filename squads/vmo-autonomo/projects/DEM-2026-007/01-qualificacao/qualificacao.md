ANÁLISE DE QUALIFICAÇÃO DE DEMANDA
ID: DEM-2026-007
Ticket: #6700943
Data: 2026-05-20 (revisado com contexto de e-mails anexados ao ticket)
Analista: Felipe Filtro (VMO Autônomo)

---

## Resumo da Demanda

A área de Contas a Pagar da VAB Matriz solicita a automação da importação do DDA
(Débito Direto Autorizado) no SAP, eliminando o processo manual de impressão e digitação
de código de barras de boletos. A demanda está inserida no contexto do projeto estratégico
**"Controladoria do Futuro"** (conforme nomeado pela coordenadora Noemia Malini nos e-mails
de acompanhamento). A solução equivalente já está implantada na VIX e na Divisão Logística
do ambiente GAB. A integração envolve SAP x Santander. A implementação foi descrita
como "replicação do modelo existente com ajustes para o Contas a Pagar da VAB".

Aprovações gerenciais já concedidas via e-mail:
- **Walace Bacelar da Silva (Holding)** — 08/04/2026: autorizado, condicionado a custo zero
- **Gladston Campos (Gerência de TI e Projetos Estratégicos)** — 06/05/2026: "Aprovado!"

---

## Critérios de Qualificação

### Valor da Demanda

1. Alinhamento Estratégico        7/10
   Demanda inserida explicitamente no contexto do projeto "Controladoria do Futuro",
   que indica uma iniciativa estratégica de digitalização e eficiência financeira da VAB.
   A nomeação do projeto e o envolvimento de Walace Bacelar (Holding) e Hugo Paradella
   (Holding Assessoria) no e-mail de 08/04 indicam relevância além do operacional.
   Sem OKR formalmente declarado, mas com âncora estratégica identificada. Confiança: MÉDIA-ALTA.

2. Viabilidade Técnica            8/10
   Alta viabilidade confirmada pela própria solicitante: "trata-se da replicação do modelo
   existente, com alguns ajustes necessários para atender às demandas específicas do Contas
   a Pagar da VAB." Integração SAP x Santander já homologada e em produção na Divisão
   Logística (mesmo ambiente GAB) e na VIX. Risco técnico muito baixo.

3. Retorno sobre Investimento     7/10
   Investimento estimado < R$10K com retorno em eliminação de retrabalho (impressão,
   digitação, solicitação de boletos a terceiros) e ganho de autonomia no processamento
   de pagamentos. Payback estimado: 2–4 meses, assumindo 20–30 min/dia de retrabalho
   eliminado. A autorização de Walace foi condicionada a custo zero — o que indica que
   qualquer investimento necessário precisará de nova validação financeira.
   Confiança: MÉDIA — sem dados de volume de boletos declarados pelo solicitante.

4. Urgência                       6/10
   Ticket em atraso há mais de 200h no SLA (aberto em 07/04, prazo era 15/04). A aprovação
   gerencial foi dada já em 08/04 (D+1 por Gladston) e em 06/05 (Walace). O fato de o ticket
   permanecer sem responsável atribuído por 43 dias após as aprovações indica que a urgência
   operacional é real, mas não crítica o suficiente para travar operação. Criticidade: Normal.

5. Maturidade da Demanda          5/10
   A descrição no ticket é sucinta (1 linha), mas os e-mails agregam contexto relevante:
   solução definida como replicação, escopo direcionado a Contas a Pagar da VAB, referência
   técnica clara (VIX + Divisão Logística). Gaps remanescentes: processo atual não
   documentado, sem dados de volume de boletos, sem definição dos tipos de DDA contemplados.
   Maturidade suficiente para iniciar levantamento, mas não para fechar escopo.

6. Disponibilidade de Recursos    6/10
   Aprovação gerencial obtida por dois gestores (Gladston e Walace). Walace condicionou
   a "custo zero" — o que exige formalização do orçamento antes de qualquer gasto. Gladston
   disse "Aprovado!" sem condição, sendo o gerente de TI e Projetos Estratégicos.
   Orçamento estimado < R$10K, mas sem aprovação financeira formal. Sem responsável técnico
   atribuído no ticket. Condição parcialmente atendida — desbloqueável em prazo curto.

### Complexidade de Execução

7. Esforço Estimado               3/10
   Estimativa: 80–120 horas totais (levantamento + configuração SAP + testes + go-live).
   Abaixo do limiar de 160h, graças ao reaproveitamento da solução já existente. A própria
   solicitante confirma tratar-se de "replicação com ajustes" — não de desenvolvimento
   do zero. Esforço adequado para sustentação ERP, sem necessidade de gestão de projeto formal.

8. Impacto Organizacional         3/10
   Impacto restrito à área de Contas a Pagar da VAB Matriz. O solicitante declarou
   explicitamente que não impacta outras áreas ou divisões. Mudança de processo é pontual:
   elimina etapa manual de digitação/impressão sem redefinir estrutura operacional ou
   responsabilidades. Nenhum treinamento significativo esperado.

9. Governança Necessária          3/10
   Não requer comitê formal, cronograma extenso ou gestão de múltiplos stakeholders.
   As aprovações já foram dadas informalmente por e-mail — a formalização via orçamento
   e designação de responsável técnico é suficiente. O time de sustentação FI pode
   gerenciar a entrega com acompanhamento básico.

10. Impacto Regulatório/Financeiro  4/10
    Integração bancária CNAB/EDI com Santander é padrão e já homologada no ambiente.
    Sem requisito legal ou obrigação regulatória específica. Impacto no processo de
    pagamento sem reflexo em demonstrativos financeiros ou auditorias. A condição de
    Walace ("presumindo custo zero") cria um risco financeiro menor se houver necessidade
    de qualquer investimento não previsto.

---

## Resultado

**PONTUAÇÃO TOTAL: 52/100 (52%)**

**CLASSIFICAÇÃO: MELHORIA EVOLUTIVA**
Os critérios de complexidade (7–10) confirmam: nenhum atinge ≥ 7/10 individualmente.
Esforço estimado abaixo de 160h (replicação confirmada), impacto restrito a uma área,
sem governança formal necessária. Não caracteriza projeto VMO completo.
→ Time de Sustentação ERP responsável: **FI** (Financeiro — Contas a Pagar / Integração Bancária)

**DECISÃO: APROVADO COM CONDIÇÕES**
A pontuação (52%) está na faixa de aprovação condicional. As aprovações gerenciais já foram
obtidas via e-mail (Gladston em 08/04 e Walace em 06/05). As condições remanescentes são
pontuais e desbloqueáveis em prazo curto: formalização do orçamento e designação de
responsável técnico.

---

## Condições Bloqueantes

1. **Formalizar orçamento junto ao Financeiro** (CC 200195148) — Walace autorizou
   assumindo custo zero. Se houver qualquer investimento (mesmo < R$10K), a aprovação
   formal é obrigatória antes do início. Gladston aprovou sem condição de custo — confirmar
   com ele se a aprovação cobre eventuais gastos de implementação.
2. **Designar responsável técnico no Projetos DTI** — ticket aberto há 43 dias sem
   responsável atribuído. Gladston Campos (gerente de TI e Projetos Estratégicos) é o
   ponto de contato natural para essa designação.

## Condições Desejáveis (não bloqueantes)

- Documentar processo atual: quem executa, volume de boletos/mês, tipos de DDA contemplados
- Contato com Santander para confirmar habilitação DDA na conta VAB Matriz
- Acesso à documentação técnica da implementação na Divisão Logística (configuração CNAB/SAP)

---

## Contexto dos E-mails Anexados

| Data | De | Para | Conteúdo-chave |
|------|-----|------|----------------|
| 07/04/2026 | Noemia Malini | Walace / Gladston | Solicitação de autorização — "Controladoria do Futuro" / replicação da VIX |
| 08/04/2026 | Walace Bacelar (Holding) | Noemia | Autorizado — "presumindo que não haverá custos adicionais" |
| 07/04/2026 | Noemia Malini | Gladston Campos | ENC: Registro do ticket — ciência |
| 06/05/2026 | Gladston Campos (Gerência TI/Projetos) | Noemia | "Aprovado!" — sem condição |

---

## Próximos Passos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Designar responsável técnico no ticket #6700943 | Gladston Campos | 2026-05-22 |
| Confirmar com Gladston se aprovação cobre custos < R$10K | Projetos DTI / Noemia | 2026-05-22 |
| Formalizar orçamento < R$10K (CC 200195148) se necessário | Noemia + Financeiro VAB | 2026-05-27 |
| Enviar questionário de levantamento ao Lucas Medeiros | Projetos DTI | 2026-05-22 |
| Iniciar levantamento técnico com equipe da Divisão Logística | Responsável DTI designado | Após designação |
