# DEMANDA VALIDADA — PROJ-2026-001
**Validado por:** Marcelo Silveira — VMO Consultoria
**Data de validação:** 2026-05-18
**Decisão:** ✅ CONFIRMADA — avançar para qualificação
**Observações:** Re-execução completa do pipeline v2 com novos agentes (Fábio Fornecedor + Gabriel Governança)

---

# DEMANDA COLETADA — PROJ-2026-001
**Agente:** Iara Inbound — Coletora de Demandas VMO
**Data de reconstrução:** 2026-05-18
**Fonte:** PROJ-2026-001-pacote-iniciacao.md (run 2026-04-03)
**Status:** RECONSTRUÍDA para re-execução pipeline v2

---

## IDENTIFICAÇÃO DA DEMANDA

| Campo | Valor |
|-------|-------|
| ID da Demanda | DEM-2026-001 |
| ID do Projeto | PROJ-2026-001 |
| Nome | Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados |
| Área Solicitante | VIX Manutenção |
| Solicitante | Ivanilde Ribeiro Machado — VIX Manutenção |
| Sponsor | Andre Chieppe — Diretor Financeiro da VIX Manutenção |
| Data de Abertura | 2026-04-03 |
| Canal de Entrada | PMO VMO Consultoria — demanda direta do cliente |

---

## DESCRIÇÃO DA DEMANDA

O Diretor Financeiro da VIX Manutenção está **ausente do fluxo de aprovação de lançamentos pré-editados no SAP FI**, criando uma lacuna de controle no processo de aprovação financeira. A solicitante (Ivanilde Ribeiro Machado) demanda a parametrização do Diretor Financeiro como aprovador obrigatório no fluxo SAP FI para a categoria "lançamentos pré-editados", via transações **ZFI0057** e **SBWP** do ambiente SAP já implantado.

### Dor / Problema

- Lançamentos pré-editados de alto valor tramitam sem ciência e aprovação do principal executivo financeiro
- Ausência expõe a organização a risco de fraude e fragilidades de governança
- Lacuna identificada no processo de controle interno que precisa ser corrigida

### Solicitação

Parametrizar o Diretor Financeiro como aprovador obrigatório no fluxo de aprovação de lançamentos pré-editados do módulo SAP FI, de modo que **100% dos lançamentos submetidos após go-live passem pelo nível de aprovação** do Diretor Financeiro.

---

## CONTEXTO DO NEGÓCIO

- **Organização:** VIX Manutenção (empresa do grupo GAB)
- **Sistema:** SAP FI — módulo já implantado e operacional
- **Transações envolvidas:** ZFI0057 (parametrização de aprovadores) e SBWP (workflow de aprovação)
- **Solução:** Exclusivamente parametrização — sem desenvolvimento ABAP, sem novas licenças
- **Complexidade:** Baixa — tecnologia já implantada, escopo restrito

---

## REQUISITOS DE ALTO NÍVEL

1. Parametrizar o Diretor Financeiro como aprovador obrigatório na ZFI0057 para lançamentos pré-editados
2. Configurar e validar o fluxo de aprovação no SBWP (roteamento da task de aprovação)
3. Executar testes integrados em ambiente QAS (aprovação, rejeição, roteamento de exceções)
4. Treinar/capacitar o Diretor Financeiro para uso da interface SBWP
5. Documentação técnica (manual de configuração) e operacional (guia do aprovador)
6. Go-live supervisionado + acompanhamento pós-implantação por mínimo 10 dias úteis

---

## RESTRIÇÕES DECLARADAS

- **Orçamento máximo:** R$ 8.640 (incluindo contingência de 20%)
- **Prazo máximo:** 60 dias úteis a partir da assinatura do TAP
- **Escopo de tecnologia:** Apenas parametrização das transações existentes — nenhum desenvolvimento ABAP
- **Processo de change management:** Todos os transportes devem seguir o processo formal SAP do cliente

---

## PREMISSAS IDENTIFICADAS

- Ambiente SAP FI de produção está implantado e estável
- Existe ambiente QAS disponível para testes
- Andre Chieppe (Diretor Financeiro) está ciente e apoiará o projeto
- A parametrização via ZFI0057 é suficiente sem necessidade de ABAP
- Equipe de Basis/DTI possui as autorizações necessárias

---

## CRITÉRIOS DE SUCESSO (SMART)

1. **100% cobertura:** Todos os lançamentos pré-editados recebem task de aprovação na caixa do DF — verificado por relatório SBWP na primeira semana após go-live
2. **Zero bypass:** Nenhum lançamento contabilizado sem aprovação registrada — auditoria 30 dias pós go-live via ZFI0057
3. **Prazo:** Sistema em produção com ≤ 60 dias úteis da assinatura do TAP
4. **Custo:** Dentro da faixa aprovada de R$ 8.640
5. **Capacitação:** Diretor Financeiro confirma capacidade operacional antes do go-live

---

## ANÁLISE INICIAL DE VIABILIDADE

| Critério | Avaliação |
|----------|-----------|
| Viabilidade técnica | ✅ Alta — parametrização padrão SAP |
| Viabilidade financeira | ✅ Alta — orçamento razoável para o escopo |
| Viabilidade operacional | ✅ Alta — equipe interna disponível |
| Alinhamento estratégico | ✅ Reforça governança e controles internos |
| Risco geral | 🟡 Baixo-Médio |

**Recomendação Iara:** DEMANDA QUALIFICÁVEL — encaminhar para Step 3 (Felipe Filtro).

---

*Documento reconstruído por Iara Inbound em 2026-05-18 a partir do PROJ-2026-001-pacote-iniciacao.md para suporte à re-execução do pipeline v2 com novos agentes (Fábio Fornecedor e Gabriel Governança).*
