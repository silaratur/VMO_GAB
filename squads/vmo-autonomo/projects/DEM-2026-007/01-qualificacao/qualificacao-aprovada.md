# Qualificação Aprovada — DEM-2026-007
Data: 2026-05-20
Aprovado para: Fase de Documentação (Steps 7–13)
Decisão checkpoint Step 6: AVANÇAR PARA DOCUMENTAÇÃO

---

## Identificação do Projeto

| Campo | Valor |
|-------|-------|
| ID | DEM-2026-007 |
| Nome | Implantação DDA (Débito Direto Autorizado) no SAP — VAB Matriz |
| Solicitante | Lucas Medeiros Pereira |
| Coordenadora | Noemia Tambara Cardoso Malini |
| Área solicitante | VAB Matriz — Contas a Pagar (CP) |
| Área executora | DTI — Sustentação ERP FI |
| Classificação | MELHORIA EVOLUTIVA → Sustentação ERP FI (provisória — CB-2 confirma ou reclassifica) |
| Score qualificação | 49/100 (49%) |
| Integração | SAP x Santander (DDA / CNAB 240) |

---

## Necessidade de Negócio

O processo atual de pagamento de boletos na VAB Matriz exige que os colaboradores imprimam
boletos físicos ou digitem manualmente o código de barras no sistema SAP. Quando o boleto não
está disponível no sistema no momento do pagamento, o colaborador precisa solicitá-lo a
terceiros, gerando desgaste físico e psicológico, atrasos e dependência de outros colaboradores.
A demanda é a automação do recebimento eletrônico de boletos via DDA diretamente no SAP,
eliminando o processo manual.

## Solução Proposta

Replicação do modelo DDA já implantado e em produção na Divisão Logística (mesmo ambiente SAP/GAB)
e na unidade VIX, com ajustes para o Contas a Pagar da VAB Matriz. Integração: SAP FI x Santander
via arquivo CNAB 240 / serviço DDA bancário.

**CB-2 aberta:** Natureza e extensão dos ajustes a ser levantada pelo Rafael Requisito (Step 8)
junto ao DTI. Resultado pode reclassificar para PROJETO se esforço > 160h.

---

## Stakeholders

| Nome | Papel | Área |
|------|-------|------|
| Lucas Medeiros Pereira | Solicitante / Beneficiado | VAB Matriz — CP |
| Noemia Tambara Cardoso Malini | Coordenadora do processo | VAB Matriz |
| Gladston Campos | Aprovador de negócio / Gerência TI VAB | VAB Matriz |
| Walace Bacelar da Silva | Autorizador Holding (condicional a custo zero) | Holding |
| Viviane Cristina Caliari | Referência DTI Holding | Holding DTI |
| Henrique Demoner De Lima | Stakeholder VAB | VAB Matriz |
| Wellington Gonçalves Teodoro da Silva | Stakeholder VAB | VAB Matriz |
| Ana Luisa Curcio Magalhaes | Referência Holding DTI | Holding DTI |

---

## Aprovações

| Aprovador | Data | Natureza |
|-----------|------|----------|
| Gladston Campos | 06/05/2026 | INCONDICIONAL — "Aprovado!" |
| Walace Bacelar da Silva (Holding) | 08/04/2026 | CONDICIONAL — custo zero; re-autorização necessária se houver custo |

---

## Benefícios Esperados

1. Eliminação de 100% da digitação manual de código de barras no SAP
2. Eliminação da dependência de terceiros para obtenção de boletos no momento do pagamento
3. Eliminação de impressão de papel de boletos
4. Redução de atrasos e erros no processamento de pagamentos
5. Alívio de desgaste físico e psicológico da equipe de CP

---

## Parâmetros de Projeto

| Parâmetro | Valor | Status |
|-----------|-------|--------|
| Investimento externo estimado | R$0 a R$8.000 | A confirmar no kick-off gate (CB-3) |
| Esforço DTI estimado | 80–160h | A confirmar no levantamento técnico (CB-2) |
| Prazo estimado | 3 meses pós-kick-off | Depende de CB-2 |
| Prazo meta | Setembro 2026 | Orientativo |
| Urgência | Normal (Criticidade 3) | Sem data-limite obrigatória |
| Precedente | DDA Div. Logística (GAB) + VIX | Confirmado em produção |

---

## Condições de Kick-off (Não Bloqueiam Esta Fase)

| CB | Descrição | Responsável |
|----|-----------|-------------|
| CB-2 | Levantamento técnico dos ajustes — a resolver no Step 8 (Rafael Requisito) | DTI / Rafael |
| CB-3 (Gate KO) | Formalização de custos + re-autorização Holding antes do kickoff | Noemia → Gladston → Walace |
| CB-Sponsor | Sponsor Diretor+ identificado ou escalada formal | A definir |

---

## Contexto Técnico

- SAP FI em produção na VAB Matriz (mesmo ambiente Grupo Águia Branca)
- DDA já operacional na Divisão Logística do GAB (mesmo SAP) — precedente direto
- Banco: Santander — integração via CNAB 240 / DDA
- Habilitação DDA no Santander VAB Matriz: a confirmar (L5)
- Centro de Custo: 200195148

---

## Critérios de Sucesso (para validação no encerramento)

1. 100% dos boletos DDA Santander importados automaticamente no SAP sem digitação manual
2. Zero atrasos de pagamento causados por ausência de boleto digital em 60 dias pós-go-live
3. Satisfação da equipe CP ≥ 8/10 na pesquisa pós-implantação
4. Go-live até 30/09/2026 (meta orientativa)
