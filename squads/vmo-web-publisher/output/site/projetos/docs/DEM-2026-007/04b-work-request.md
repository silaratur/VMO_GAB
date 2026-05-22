# WORK REQUEST — DEM-2026-007
## Implantação DDA (Débito Direto Autorizado) no SAP FI — Contas a Pagar VAB Matriz

Elaborado por: Fábio Fornecedor (VMO Autônomo)
Data de emissão: 2026-05-20
Versão: 1.0
Destinatário: DTI — Sustentação ERP FI / Grupo Águia Branca

---

## 1. Identificação

| Campo | Valor |
|-------|-------|
| Código do Projeto | DEM-2026-007 / PROJ-VAB-2026-DDA |
| Tipo de solicitação | Melhoria Evolutiva ERP FI (replicação com ajustes) |
| Área demandante | VAB Matriz — Contas a Pagar |
| Sponsor provisório | Gladston Campos — Gerência TI e Projetos Estratégicos, VAB Matriz |
| Ponto focal negócio | Noemia Tambara Cardoso Malini (noemia@...) |
| Gerente de Projeto | A designar pelo DTI após gate de kick-off |
| Centro de custo | 200195148 |

---

## 2. Contexto e Problema de Negócio

O Contas a Pagar da VAB Matriz processa boletos de fornecedores e tributos de forma manual:
os colaboradores imprimem boletos físicos ou digitam manualmente os códigos de barras no SAP.
Quando o boleto não está disponível no sistema no momento do pagamento, o colaborador depende
de terceiros para obtê-lo, gerando atrasos, erros e desgaste operacional da equipe.

A solução DDA (Débito Direto Autorizado) permite que o Santander entregue eletronicamente os
dados dos boletos diretamente ao SAP via arquivo CNAB 240, eliminando o processo manual.

**ROI contextual:** Benefício = eliminação de trabalho manual de CP + redução de erros e atrasos
de pagamento. Custo alvo = R$0 (horas internas DTI). Payback: imediato (sem investimento externo).

**Precedente interno:** A solução DDA está implantada e em produção na Divisão Logística do mesmo
ambiente SAP (Grupo Águia Branca) e na unidade VIX. Este WR solicita a replicação para a VAB Matriz
com os ajustes específicos do CP.

---

## 3. Objetivo

Configurar e disponibilizar em produção a recepção automática de boletos via DDA no SAP FI
da VAB Matriz (integração SAP x Santander / CNAB 240), replicando o modelo da Divisão Logística
com os ajustes necessários para o processo de Contas a Pagar da VAB, com go-live até **30/09/2026**.

---

## 4. Escopo Incluso

| # | Entregável | RF Referência | Critério de Aceite |
|---|-----------|--------------|-------------------|
| E-01 | Levantamento técnico: análise dos parâmetros DDA da Div. Logística e mapeamento dos ajustes para VAB CP | RF001, RF002 [CB-2] | Documento de análise com lista dos ajustes e estimativa de esforço aprovado pelo GP |
| E-02 | Habilitação DDA na conta Santander da VAB Matriz | RF001 | Confirmação escrita do Santander de habilitação DDA ativa para a conta VAB |
| E-03 | Configuração do FEBAN/SAP FI para recepção CNAB 240 DDA | RF001, RF002 | Arquivo DDA teste importado com sucesso em ambiente de homologação |
| E-04 | Ajustes de configuração específicos para o CP da VAB (delta da Div. Logística) | RF002, RF003 [CB-2] | Todos os ajustes identificados no E-01 implementados e testados em homologação |
| E-05 | Testes de integração SAP x Santander (homologação) | RF001–RF005 | 100% dos RFs Must Have validados em homologação com participação da equipe CP |
| E-06 | Testes de aceitação do usuário (UAT) | RF001–RF005 | Assinatura de aprovação da Noemia Tambara e do recurso CP validador |
| E-07 | Go-live supervisionado e acompanhamento (30 dias) | Todos RFs | Go-live em produção com monitoramento por 30 dias; zero incidentes críticos |
| E-08 | Treinamento da equipe CP da VAB Matriz | RF003, RF004 | 100% da equipe CP treinada com avaliação ≥ 7/10 |
| E-09 | Documentação técnica da implementação | — | Documento com configurações SAP, parâmetros CNAB e diferenças em relação à Div. Logística |

---

## 5. Escopo Excluso

| # | Item excluído | Motivo |
|---|--------------|--------|
| EX-01 | Outros bancos além do Santander | Fora do escopo desta versão |
| EX-02 | Emissão de boletos pela VAB (DDA de saída) | Não é DDA recepção |
| EX-03 | Outras divisões do Grupo além da VAB Matriz | Expansão futura |
| EX-04 | Upgrade ou migração de versão do SAP | Restrição de ambiente |
| EX-05 | Automação de outros processos de AP além do DDA | Fora do escopo declarado |
| EX-06 | Desenvolvimento ABAP novo (se confirmado na análise) | Se identificado, será CR formal antes de execução |

---

## 6. Premissas

1. O ambiente SAP FI da VAB Matriz é equivalente ao da Divisão Logística para a configuração DDA
2. A Divisão Logística disponibilizará seus parâmetros de configuração como referência
3. O Santander habilitará o DDA para a conta VAB Matriz em até 15 dias corridos após solicitação
4. Os ajustes necessários são de parametrização (não ABAP) — a confirmar no E-01
5. Nenhum custo externo será incorrido (restrição de autorização do Holding)
6. A equipe CP da VAB estará disponível para UAT e treinamento conforme cronograma

---

## 7. Cronograma Esperado (Marcos)

| Marco | Data Estimada | Critério de Conclusão |
|-------|--------------|----------------------|
| M-0: Gate de Kick-off | Junho/2026 | CB-3 e CB-Sponsor resolvidas |
| M-1: Levantamento técnico concluído | 2 semanas pós-kick-off | E-01 entregue e aprovado |
| M-2: Habilitação Santander confirmada | 3 semanas pós-kick-off | E-02 concluído |
| M-3: Configuração SAP FI e ajustes concluídos | 5 semanas pós-kick-off | E-03 + E-04 em homologação |
| M-4: Testes de integração aprovados | 7 semanas pós-kick-off | E-05 + E-06 assinados |
| M-5: Go-live | 8 semanas pós-kick-off | E-07 iniciado |
| M-6: Encerramento | 30/09/2026 | E-07–E-09 concluídos |

> Prazo total estimado: 8–10 semanas pós-kick-off (dependente do resultado do E-01 / CB-2).
> Go-live meta: 30/09/2026.

---

## 8. Entregáveis com Critério de Aceite Binário

| Entregável | Aceito quando | Não aceito se |
|------------|--------------|---------------|
| E-01 Análise técnica | Lista de ajustes com estimativa aprovada pelo GP | Análise vaga sem itens específicos ou sem estimativa de esforço |
| E-02 Habilitação Santander | Confirmação escrita do banco | Confirmação verbal ou sem data de ativação |
| E-03+E-04 Config SAP | Arquivo DDA teste importado com sucesso em homologação | Erro em qualquer RF Must Have no ambiente de homologação |
| E-05+E-06 Testes | Assinatura de aceite da Noemia e do validador CP | Teste parcial ou sem assinatura formal |
| E-07 Go-live | Sistema em produção sem incidentes críticos por 5 dias úteis | Qualquer incidente crítico (pagamento errado, perda de dado) nos primeiros 5 dias |
| E-08 Treinamento | 100% equipe CP treinada, avaliação ≥ 7/10 | Equipe treinada parcialmente ou avaliação < 7/10 |
| E-09 Documentação | Documento entregue antes do encerramento | Documentação ausente no encerramento |

---

## 9. Governança

| Papel | Nome | Responsabilidade |
|-------|------|-----------------|
| Sponsor provisório | Gladston Campos | Aprovar marcos, decidir sobre mudanças de escopo |
| Ponto focal negócio | Noemia Tambara | Validar E-01, participar do UAT, assinar E-06 |
| GP (a designar) | DTI | Gerenciar execução, status reports, gestão de riscos |
| VMO | — | Governança, gate de kick-off, auditoria final |

**Comunicação:** Status reports quinzenais ao sponsor. Incidentes críticos comunicados imediatamente.
**Mudanças:** Qualquer mudança de escopo, prazo ou custo exige Change Request formal aprovado.

---

## 10. Condições Comerciais

| Item | Condição |
|------|---------|
| Modelo de execução | Interno DTI — sem contrato externo (meta) |
| Custo aprovado | R$0 externo (horas internas DTI não contabilizadas como investimento) |
| Reserva de contingência | R$2.000 (somente para eventualidades imprevistas, com autorização prévia) |
| Faturamento por marcos | N/A — execução interna |
| Penalidade por atraso | N/A — DTI interna |
| Garantia pós-go-live | 30 dias de suporte pós-implantação incluídos no escopo (E-07) |
| Condição de contratação externa | Somente se E-01 identificar necessidade; exige re-autorização do Holding antes de qualquer contratação |

---

## 11. Artefato Obrigatório de Resposta

O executor desta demanda deve preencher este artefato antes do gate de kick-off:

| # | Grupo | Item | OK | NOK | Observações |
|---|-------|------|----|----|-------------|
| **G1** | **Viabilidade Técnica** | | | | |
| 1.1 | Técnica | Configuração DDA FEBAN já conhecida pela equipe | ☐ | ☐ | |
| 1.2 | Técnica | Versão SAP VAB compatível com config Div. Logística | ☐ | ☐ | |
| 1.3 | Técnica | Layout CNAB 240 Santander disponível para análise | ☐ | ☐ | |
| 1.4 | Técnica | Ajustes necessários são apenas parametrização (sem ABAP) | ☐ | ☐ | Se NOK: detalhar no campo observações |
| 1.5 | Técnica | Estimativa de esforço total por fase viável em ≤ 10 semanas | ☐ | ☐ | |
| **G2** | **Habilitação Bancária** | | | | |
| 2.1 | Banco | Conta Santander VAB habilitada para DDA | ☐ | ☐ | |
| 2.2 | Banco | Contato Santander identificado para habilitação | ☐ | ☐ | |
| 2.3 | Banco | Prazo de habilitação Santander: ≤ 15 dias úteis | ☐ | ☐ | |
| **G3** | **Recursos** | | | | |
| 3.1 | Recursos | Recurso técnico DTI FI designado | ☐ | ☐ | Nome: ________ |
| 3.2 | Recursos | Disponibilidade confirmada para o prazo proposto | ☐ | ☐ | % disponibilidade: __ |
| 3.3 | Recursos | Sem conflito de portfólio identificado | ☐ | ☐ | |
| **G4** | **Referência Logística** | | | | |
| 4.1 | Referência | Documentação técnica Div. Logística disponível | ☐ | ☐ | |
| 4.2 | Referência | Responsável técnico Logística disponível para consulta | ☐ | ☐ | |
| 4.3 | Referência | Parâmetros de config FEBAN da Logística compartilháveis | ☐ | ☐ | |
| **G5** | **Escopo e Ajustes** | | | | |
| 5.1 | Escopo | Lista preliminar de ajustes necessários para CP VAB | ☐ | ☐ | |
| 5.2 | Escopo | Nenhum ajuste identificado exige desenvolvimento ABAP novo | ☐ | ☐ | Se NOK: impacto em prazo e custo |
| 5.3 | Escopo | Escopo dentro do prazo de 8–10 semanas | ☐ | ☐ | |
| **G6** | **Custos** | | | | |
| 6.1 | Custo | Implementação realizável sem custo externo (DTI interna) | ☐ | ☐ | |
| 6.2 | Custo | Sem necessidade de novas licenças SAP ou bancárias | ☐ | ☐ | |
| 6.3 | Custo | Custo externo: R$0 (ou valor específico se NOK em 6.1/6.2) | ☐ | ☐ | Valor: R$_____ |
| **G7** | **Testes e Qualidade** | | | | |
| 7.1 | Qualidade | Ambiente de homologação SAP disponível | ☐ | ☐ | |
| 7.2 | Qualidade | Possibilidade de testes DDA com Santander em homologação | ☐ | ☐ | |
| 7.3 | Qualidade | Equipe CP disponível para UAT (1 semana) | ☐ | ☐ | |
| **G8** | **Documentação** | | | | |
| 8.1 | Docs | Documentação técnica será produzida pelo executor | ☐ | ☐ | |
| 8.2 | Docs | Treinamento da equipe CP incluído na proposta | ☐ | ☐ | |
| **G9** | **Riscos** | | | | |
| 9.1 | Risco | Executor confirmou ciência dos riscos R-001 a R-005 do plano | ☐ | ☐ | |
| 9.2 | Risco | Nenhum risco crítico adicional identificado | ☐ | ☐ | Se NOK: descrever |
| **G10** | **Aprovações e Compliance** | | | | |
| 10.1 | Aprovação | Aprovação do sponsor para início está confirmada | ☐ | ☐ | |
| 10.2 | Aprovação | CB-3 (custo zero / autorização Holding) entendida e aceita | ☐ | ☐ | |
| 10.3 | Aprovação | CB-Sponsor será resolvida antes do kick-off | ☐ | ☐ | |

---

## 12. Processo de Submissão da Resposta

| Item | Detalhe |
|------|---------|
| Prazo de resposta | Até 5 dias úteis após recebimento deste WR |
| Canal de submissão | E-mail para Noemia Tambara (coordenadora) com cópia para VMO e Gladston Campos |
| Formato | Artefato Obrigatório preenchido + estimativa de esforço por fase (E-01 preliminar) + confirmação de disponibilidade do recurso técnico DTI |
| Dúvidas sobre o WR | Contato: Noemia Tambara Cardoso Malini — VAB Matriz |
| Data limite para kick-off | Junho 2026 (após CBs resolvidas e artefato obrigatório aprovado) |
