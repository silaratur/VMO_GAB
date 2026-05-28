# Qualificação Aprovada — DEM-2026-008
Versão: 1.0
Data: 2026-05-28
Aprovado por: Checkpoint Step 6 — AUTO-APROVADO (Pipeline VMO Autônomo)

---

## Identificação

| Campo | Valor |
|-------|-------|
| ID da Demanda | DEM-2026-008 |
| Nome Preliminar do Projeto | Integração SGMM03 — Campos Empresa e Contrato (InterCompany) |
| Sistema | Sistemática ERP > Solicitação de Novas Demandas / Projetos |
| Ticket | #6800446 |
| Data de Abertura do Ticket | 08/05/2026 |
| Data da Qualificação | 28/05/2026 |

---

## Decisão de Qualificação

| Dimensão | Resultado |
|----------|-----------|
| **Pontuação** | 50/100 (50%) |
| **Decisão** | APROVADO COM CONDIÇÕES |
| **Classificação** | MELHORIA EVOLUTIVA |
| **Time de Execução** | Sustentação ERP — PM / FI (com consultoria externa) |
| **Gate de Governança** | PASS |

---

## Stakeholders Identificados

| Nome | Papel | Área |
|------|-------|------|
| Jenifer dos Santos Carvalho | Solicitante / Beneficiada | VIX Matriz |
| Mara Rubia Silva Rocha | Gestora do chamado / Responsável Holding DTI | Holding DTI |
| Jhonny Henrique M. F. de Freitas | Parte interessada | VIX Matriz |
| João Gabriel Virígio Barbierato | Parte interessada | VIX Matriz |
| **Sponsor: A DEFINIR (CB-1)** | Sponsor executivo Diretor+ | A confirmar |
| Consultora selecionada (a definir) | Executora técnica | Externa |

---

## Escopo Aprovado

**O que está dentro do escopo:**
- Integração dos campos **Empresa** e **Contrato** da OM via interface SGMM03 (SGM → SAP)
- Suporte ao evento de **criação** de OM no SAP
- Suporte ao evento de **alteração** de OM no SAP
- Módulo SAP: PM (Plant Maintenance) com impacto em FI (campos InterCompany)
- Ambiente: VIX Matriz (a confirmar mandante/versão — lacuna L7)

**O que está fora do escopo:**
- Integração de outros campos da interface SGMM03 (escopo separado se necessário)
- Campo Cenário/CenPlan (tem restrição técnica conhecida — demanda separada)
- Alterações no sistema SGM (origem dos dados)
- Outras interfaces de integração SAP além da SGMM03
- Implantação em outras divisões ou empresas do grupo (exceto se confirmado em L4)

---

## Condições Bloqueantes para Início

| CB | Descrição | Responsável | Prazo |
|----|-----------|-------------|-------|
| **CB-1** | Identificar e nomear sponsor com nível Diretor ou superior | PMO / Holding DTI | 30/05/2026 |
| **CB-2** | Formalizar orçamento aprovado após equalização das propostas (retorno esperado 29/05) | Sponsor designado + Mara Rubia | 02/06/2026 |
| **CB-3** | Confirmar escopo técnico formal dos campos Empresa e Contrato com consultora selecionada | DTI + Consultora | Pré-kick-off |

---

## Estimativas de Referência

| Parâmetro | Estimativa |
|-----------|------------|
| Esforço estimado (por analogia) | ~80–120 horas de consultoria SAP |
| Custo referencial | R$ 18.000 – R$ 48.000 (aguardar propostas) |
| Prazo estimado de execução | 4–8 semanas após kick-off |
| Contingência recomendada | 20% sobre o valor contratado |

---

## Próximos Passos Aprovados

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Receber e equalizar propostas das 4 consultorias | Mara Rubia (Holding DTI) | 29/05/2026 |
| Nomear sponsor com nível Diretor+ | PMO / Holding DTI | 30/05/2026 |
| Formalizar orçamento aprovado | Sponsor + Mara Rubia | 02/06/2026 |
| Elaborar TAP, PM Canvas e Plano Geral | Diana Documento (VMO) | Iniciado após CBs |
| Elaborar ERF com RF e RNF | Rafael Requisito (VMO) | Junto com TAP |
| Emitir Work Request para consultoras | Fábio Fornecedor (VMO) | Após ERF |

---

## Nota do Checkpoint

> **Checkpoint Step 6 — AUTO-APROVADO em 2026-05-28**
>
> Qualificação aprovada com condições. O pacote de iniciação (TAP, ERF, WR, Cronograma, Riscos,
> KPIs, Status Report) deve ser elaborado com as 3 CBs registradas. O sponsor será marcado como
> "[A CONFIRMAR — CB-1]" no TAP enquanto a CB-1 não for resolvida. O orçamento no TAP usará
> o envelope referencial (R$ 35.000) com nota de que deve ser substituído pelo valor contratado
> após seleção da consultora.
