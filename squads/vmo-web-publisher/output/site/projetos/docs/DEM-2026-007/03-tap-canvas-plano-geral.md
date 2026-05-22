# Documentação Base de Iniciação — Implantação DDA SAP — VAB Matriz
Elaborado por: Diana Documento (VMO Autônomo)
Data: 2026-05-20
Versão: 1.0 — Rascunho para aprovação do sponsor

---

## TERMO DE ABERTURA DO PROJETO (TAP)

---

### Identificação do Projeto

| Campo | Valor |
|-------|-------|
| Nome do Projeto | Implantação DDA (Débito Direto Autorizado) no SAP — Contas a Pagar VAB Matriz |
| ID | DEM-2026-007 |
| Código Interno | PROJ-VAB-2026-DDA |
| Área Solicitante | VAB Matriz — Contas a Pagar |
| Área Executora | DTI — Sustentação ERP FI |
| Centro de Custo | 200195148 |
| Integração Principal | SAP FI x Santander (DDA / CNAB 240) |

---

### Autorização

| Papel | Nome | Cargo | Autoridade |
|-------|------|-------|------------|
| Sponsor (provisório) | Gladston Campos | Gerência TI e Projetos Estratégicos — VAB Matriz | Aprovar demandas técnicas; autoridade orçamentária a confirmar (CB-Sponsor) |
| Solicitante | Lucas Medeiros Pereira | VAB Matriz — CP | Beneficiário do projeto |
| Coordenadora de Processo | Noemia Tambara Cardoso Malini | VAB Matriz | Ponto focal do negócio |
| Gerente de Projeto | A designar pelo DTI | — | A definir no kick-off |
| Autoridade do GP | A definir no kick-off | — | — |

> **Nota de governança:** CB-Sponsor em aberto — sponsor Diretor+ não identificado.
> Gladston Campos (Gerente) exerce o papel provisoriamente. Resolução obrigatória antes do gate de kick-off.

---

### Objetivo do Projeto

Implantar a recepção automática de boletos via DDA (Débito Direto Autorizado) integrada ao
SAP FI para o Contas a Pagar da VAB Matriz, mediante replicação com ajustes do modelo em
produção na Divisão Logística do Grupo Águia Branca, **eliminando 100% da digitação manual
de códigos de barras e 100% da dependência de terceiros para obtenção de boletos**, com
go-live operacional até **30/09/2026**.

---

### Justificativa

O processo atual de pagamento de boletos no CP da VAB Matriz exige impressão física ou
digitação manual do código de barras no SAP. Quando o boleto não está disponível no sistema
no momento do pagamento, o colaborador precisa solicitá-lo a terceiros, causando atrasos,
erros e desgaste operacional contínuo da equipe. A solução de DDA já está implantada e em
produção na Divisão Logística do Grupo Águia Branca (mesmo ambiente SAP) e na unidade VIX,
demonstrando viabilidade técnica e organizacional. A iniciativa está alinhada com o
programa "Controladoria do Futuro" da VAB Matriz e com os objetivos de automação financeira
do Grupo Águia Branca.

---

### Escopo

**DENTRO DO ESCOPO:**
- Configuração do serviço DDA no ambiente SAP FI da VAB Matriz
- Integração SAP x Santander via CNAB 240 para recepção eletrônica de boletos
- Habilitação da conta corrente Santander da VAB Matriz para o serviço DDA (junto ao banco)
- Ajustes de configuração específicos para o processo de CP da VAB Matriz (a especificar no Step 8)
- Testes integrados com ambiente Santander (homologação DDA)
- Treinamento da equipe de CP da VAB Matriz no novo processo
- Documentação técnica da implementação (diferencial em relação à Div. Logística)
- Go-live supervisionado com acompanhamento pós-implantação (30 dias)

**FORA DO ESCOPO:**
- Outras divisões do Grupo Águia Branca (expansão futura, se aplicável)
- Outros bancos além do Santander
- Automação de outros processos de Contas a Pagar além de DDA
- Substituição ou upgrade de versão do SAP FI
- Integração com outros módulos SAP além do FI (CO, MM — apenas se identificado como necessário nos ajustes)
- Gestão de boletos emitidos pela VAB (foco é recebimento de boletos de fornecedores/tributos)

---

### Critérios de Sucesso

| # | Critério | Métrica | Prazo de Verificação |
|---|---------|---------|----------------------|
| CS-1 | Recepção automática de boletos DDA | 100% dos boletos DDA Santander importados no SAP sem digitação manual | 30 dias pós-go-live |
| CS-2 | Eliminação de dependência de terceiros | Zero ocorrências de atraso de pagamento por ausência de boleto digital | 60 dias pós-go-live |
| CS-3 | Satisfação da equipe CP | Nota ≥ 8/10 na pesquisa pós-implantação | 30 dias pós-go-live |
| CS-4 | Prazo de entrega | Go-live em produção até 30/09/2026 | Data de go-live |

---

### Premissas

| # | Premissa |
|---|----------|
| P-1 | O ambiente SAP FI da VAB Matriz é equivalente ao da Divisão Logística para fins de configuração DDA |
| P-2 | A Divisão Logística disponibilizará seus parâmetros de configuração DDA como referência para a equipe técnica |
| P-3 | O banco Santander aprovará a habilitação DDA para a conta da VAB Matriz em prazo compatível com o cronograma |
| P-4 | A equipe de Contas a Pagar da VAB Matriz participará dos testes e treinamento conforme convocação |
| P-5 | Os "ajustes necessários" identificados por Noemia são de parametrização, não de desenvolvimento ABAP (a confirmar no Step 8) |
| P-6 | O investimento será zero ou suportado por horas de DTI interna (sem custo externo), satisfazendo a condição do Holding |

---

### Restrições

| # | Restrição |
|---|-----------|
| R-1 | Kickoff somente após formalização de custos e re-autorização do Holding (CB-3) |
| R-2 | Sponsor com autoridade Diretor+ deve ser identificado antes do kickoff (CB-Sponsor) |
| R-3 | Investimento externo máximo: R$0 — sem custo externo (condição Holding); se necessário custo externo, nova autorização obrigatória |
| R-4 | Go-live somente com homologação completa junto ao Santander |
| R-5 | Solução deve replicar o padrão CNAB 240 já aprovado no Grupo (mesma estrutura da Div. Logística) |
| R-6 | Sem impacto em outros módulos SAP em produção (restrição de ambiente de produção) |

---

### Riscos de Alto Nível

| ID | Risco | Probabilidade | Impacto | Nível |
|----|-------|--------------|---------|-------|
| R-001 | Autorização Holding torna-se inválida se houver qualquer custo externo | ALTA | ALTO | CRÍTICO |
| R-002 | "Ajustes necessários" revelam-se mais complexos que replicação (reclassificação para PROJETO) | MÉDIA | ALTO | ALTO |
| R-003 | Habilitação DDA no Santander demora mais que o planejado | MÉDIA | MÉDIO | MÉDIO |
| R-004 | Ambiente técnico da VAB difere da Div. Logística de forma não antecipada | BAIXA | ALTO | MÉDIO |
| R-005 | Resistência da equipe CP à mudança de processo | BAIXA | BAIXO | BAIXO |

---

### Partes Interessadas Principais

| Nome | Papel | Influência | Engajamento atual |
|------|-------|-----------|-------------------|
| Gladston Campos | Sponsor provisório / Gerência TI VAB | ALTA | FAVORÁVEL |
| Walace Bacelar da Silva | Autorizador Holding | ALTA | CONDICIONAL |
| Noemia Tambara Cardoso Malini | Coordenadora de processo | MÉDIA | FAVORÁVEL |
| Lucas Medeiros Pereira | Solicitante / Beneficiado | MÉDIA | FAVORÁVEL |
| Viviane Cristina Caliari | Referência DTI Holding | MÉDIA | NEUTRO |
| Equipe CP VAB Matriz | Usuários finais | MÉDIA | FAVORÁVEL |
| Recurso técnico DTI (a designar) | Executor técnico | ALTA | A definir |

---

### Orçamento Resumido

| Item | Valor | Observação |
|------|-------|------------|
| Horas DTI interna (estimativa) | 80–160h × custo interno | Não contabilizado como investimento externo |
| Consultoria/serviços externos | R$0 | Meta (condição Holding) |
| Licenças adicionais | R$0 | Não previsto (replicação de config existente) |
| Reserva de contingência | R$2.000 | Para eventualidades não previstas |
| **TOTAL INVESTIMENTO EXTERNO** | **R$0 – R$2.000** | **A confirmar no gate de kick-off (CB-3)** |

> Nota: se o levantamento técnico (CB-2) revelar necessidade de consultoria externa, o
> orçamento será revisado e uma nova autorização do Holding será necessária antes do kickoff.

---

### Cronograma Sumarizado

| Marco | Data Estimada | Observação |
|-------|--------------|------------|
| Resolução CB-3 e CB-Sponsor | Até 30/05/2026 | Pré-requisito para kick-off |
| Gate de Kick-off | Junho 2026 | Após CBs resolvidas |
| Levantamento técnico (CB-2) | Junho 2026 — 2 semanas | Rafael Requisito + DTI |
| Configuração SAP + DDA Santander | Julho 2026 — 4 semanas | DTI + banco |
| Testes integrados | Agosto 2026 — 2 semanas | DTI + equipe CP |
| Go-live e treinamento | Setembro 2026 — 1 semana | — |
| **Go-live meta** | **30/09/2026** | — |
| Acompanhamento pós-go-live | Outubro 2026 — 30 dias | — |

---

### Aprovação do TAP

| Papel | Nome | Assinatura | Data |
|-------|------|-----------|------|
| Sponsor (provisório) | Gladston Campos | __________________ | ________ |
| Coordenadora processo | Noemia Tambara | __________________ | ________ |
| VMO | — | __________________ | ________ |

---

## PM CANVAS

---

| Bloco | Conteúdo |
|-------|----------|
| **1. JUSTIFICATIVA** | O processo manual de boletos no CP da VAB Matriz gera desgaste operacional, erros e dependência de terceiros. A solução DDA elimina o problema com precedente interno (Div. Logística) comprovado. |
| **2. OBJETIVO SMART** | Implantar DDA no SAP FI da VAB Matriz, eliminando 100% da digitação manual e da dependência de terceiros para boletos, com go-live até 30/09/2026. |
| **3. BENEFÍCIOS** | (1) Zero digitação manual de código de barras; (2) Zero dependência de terceiros para boletos; (3) Redução de erros e atrasos de pagamento; (4) Alívio do desgaste da equipe CP; (5) Processo alinhado ao padrão GAB (Div. Logística + VIX) |
| **4. PRODUTO / ENTREGÁVEIS** | (1) DDA configurado no SAP FI VAB Matriz em produção; (2) Integração SAP x Santander CNAB 240 operacional; (3) Equipe CP treinada; (4) Documentação técnica da implementação; (5) Pesquisa de satisfação pós-go-live |
| **5. REQUISITOS** | RF: recepção automática de boletos DDA; importação SAP sem digitação manual; visualização e processamento no SAP FI. RNF: disponibilidade ≥ 99,5%; processamento de arquivo CNAB em ≤ 30 min; compatibilidade com versão SAP em uso. |
| **6. STAKEHOLDERS** | Sponsor: Gladston Campos (VAB TI). Solicitante: Lucas Medeiros (VAB CP). Coordenadora: Noemia Tambara (VAB). Autorizador: Walace Bacelar (Holding). Executores: DTI FI (a designar). Banco: Santander. Usuários: equipe CP VAB. |
| **7. EQUIPE** | GP: a designar pelo DTI. Recurso técnico FI SAP: a designar pelo DTI. Ponto focal negócio: Noemia. Suporte banco: Santander (agência VAB). |
| **8. PREMISSAS E RESTRIÇÕES** | Premissas: ambiente SAP equivalente à Div. Logística; ajustes são parametrização (não ABAP); Santander habilita DDA em tempo hábil; investimento zero externo. Restrições: kickoff somente após CB-3 e CB-Sponsor; sem custo externo sem re-autorização Holding. |
| **9. RISCOS** | (CRÍTICO) Autorização Holding inválida se houver custo. (ALTO) Ajustes mais complexos que replicação → reclassificação PROJETO. (MÉDIO) Habilitação Santander demorada. (MÉDIO) Diferença de ambiente VAB vs. Logística. |

---

## PLANO GERAL DO PROJETO

---

### 1. Plano de Gerenciamento de Escopo

O escopo será gerenciado com base no TAP e na ERF (Especificação de Requisitos Funcionais — Step 8).
Qualquer alteração de escopo pós-baseline requer Change Request formal aprovado pelo sponsor.
O levantamento técnico dos ajustes (CB-2) no Step 8 é o mecanismo de refinamento do escopo dentro
das condições aprovadas neste TAP. Se o resultado do Step 8 ampliar o escopo significativamente,
o projeto será reclassificado como PROJETO e passará por novo ciclo de qualificação.

### 2. Plano de Gerenciamento de Cronograma

Metodologia: cronograma em fases com marcos binários (entregável completo / não completo).
Ferramenta: documento `cronograma.md` (Carlos Cronograma — Step 10).
Desvios de até 5 dias são gerenciados pelo GP. Desvios > 5 dias exigem notificação ao sponsor.
Buffer de contingência: 15% do prazo total, centralizado ao final do projeto.
Revisão de cronograma: a cada 2 semanas e em cada marco.

### 3. Plano de Gerenciamento de Custos

Investimento meta: R$0 (custo interno DTI). Limite máximo externo: R$2.000 (reserva de contingência).
Qualquer gasto externo exige autorização prévia do sponsor E re-autorização do Holding (CB-3).
Acompanhamento: EVM simplificado com CPI e SPI a cada 2 semanas.
Desvios de custo acima de R$500 exigem notificação imediata ao sponsor.

### 4. Plano de Gerenciamento da Qualidade

Critérios de qualidade definidos na ERF (critérios de aceitação por RF).
Testes obrigatórios antes do go-live: testes de unidade (config SAP), testes de integração
(SAP x Santander), testes de aceitação do usuário (equipe CP VAB) com assinatura de aprovação.
Critério de go-live: 100% dos RFs Must Have validados em homologação.

### 5. Plano de Gerenciamento de Recursos

Recurso técnico DTI: a designar por Gladston Campos após gate de kick-off.
Ponto focal de negócio: Noemia Tambara — dedicação parcial (~2h/semana para validações).
Equipe CP: participação nos testes de aceitação (1 semana) e treinamento (0,5 dia).
Nenhum recurso externo previsto (meta custo zero).

### 6. Plano de Gerenciamento das Comunicações

| Comunicação | Frequência | Canal | Destinatários |
|-------------|-----------|-------|---------------|
| Status Report | Quinzenal | E-mail | Gladston, Noemia, VMO |
| Reunião de ponto de controle | Por marco | Teams/presencial | GP + Noemia + DTI |
| Notificação de risco materializado | Imediato | E-mail/Teams | Sponsor + VMO |
| Pesquisa de satisfação | Pós-go-live (30 dias) | Formulário | Equipe CP VAB |

### 7. Plano de Gerenciamento de Riscos

Riscos identificados no TAP (5 riscos de alto nível).
Plano detalhado em `plano-riscos.md` (Pedro Perigo — Step 11).
Revisão de riscos: a cada 2 semanas e em cada marco.
Trigger para escalonamento: qualquer risco CRÍTICO ou ALTO que materializar vai imediatamente
ao sponsor.

### 8. Plano de Gerenciamento de Aquisições

Não há aquisições externas previstas (meta custo zero).
Se o levantamento técnico (CB-2) revelar necessidade de consultoria:
(1) orçamento revisado e aprovado pelo sponsor; (2) re-autorização do Holding obtida (CB-3);
(3) processo de contratação interno conforme política do Grupo.

### 9. Plano de Gerenciamento de Stakeholders

Engajamento monitorado via status reports quinzenais.
Walace Bacelar (Holding): comunicação via Noemia → Gladston → Walace para qualquer
mudança de custo ou escopo que afete a condição de sua autorização.
Equipe CP: envolvida nos testes de aceitação e treinamento — participação obrigatória.
Santander: ponto de contato a ser estabelecido pela Noemia/tesouraria VAB para habilitação DDA.

### 10. Plano de Gerenciamento de Integração (mudanças)

Todas as mudanças de baseline (escopo, prazo, custo) exigem Change Request formal.
GP tem autoridade para aceitar mudanças de até 1 dia de prazo e R$0 de custo.
Mudanças acima desses limites exigem aprovação do sponsor.
Mudanças que afetem a condição de custo zero da autorização Holding exigem aprovação adicional
de Walace Bacelar antes de serem implementadas.
