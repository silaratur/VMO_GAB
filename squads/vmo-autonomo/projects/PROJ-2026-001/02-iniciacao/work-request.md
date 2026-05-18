# WORK REQUEST — PROJ-2026-001
## Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados

**Versão:** 1.0 | **Data de Emissão:** 2026-05-18 | **Elaborado por:** VMO Consultoria — Fábio Fornecedor
**Validade deste WR:** 60 dias a partir da data de emissão

---

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Detalhe |
|---|---|
| **ID do Projeto** | PROJ-2026-001 |
| **Nome do Projeto** | Inclusão de Aprovador SAP FI — Lançamentos Pré-Editados |
| **Cliente** | VIX Manutenção (Grupo GAB) |
| **Sponsor** | Andre Chieppe — Diretor Financeiro, VIX Manutenção |
| **Gerente de Projeto** | A designar pelo PMO após assinatura do TAP |
| **Área Demandante** | Diretoria Financeira — VIX Manutenção |
| **Módulo SAP** | FI (Finance) |
| **Tipo de Solução** | Parametrização SAP — sem desenvolvimento ABAP |
| **Orçamento Máximo** | R$ 8.640,00 (incluindo 20% de contingência) |
| **Prazo de Execução** | 60 dias úteis a partir da assinatura do TAP |
| **Data de Emissão do WR** | 2026-05-18 |
| **Prazo para Submissão de Propostas** | 2026-06-06 (15 dias úteis após emissão) |
| **Kickoff Estimado** | 2026-06-13 |
| **Go-live Estimado** | 2026-09-30 |

---

## 2. CONTEXTO E JUSTIFICATIVA

### 2.1 Problema de Negócio

A VIX Manutenção opera com o módulo SAP FI para registro de lançamentos contábeis pré-editados. No processo atual, lançamentos desse tipo podem ser postados diretamente na base produtiva sem passar pela aprovação formal do Diretor Financeiro (DF), Andre Chieppe. Essa lacuna gera dois riscos concretos:

1. **Risco de Conformidade:** Lançamentos contábeis relevantes — com impacto em centros de custo, contas patrimoniais e demonstrações financeiras — são efetivados sem evidência de aprovação da alçada diretora, comprometendo a trilha de auditoria.
2. **Risco Operacional:** Sem bloqueio técnico, a postagem ocorre mesmo quando o lançamento aguarda análise, impossibilitando o controle por regras de negócio e exigindo retrabalho manual para estorno ou correção.

A ausência desse controle expõe o Grupo GAB a inconsistências em auditorias internas e externas, além de elevar o risco de fraude ou erro não detectado no ciclo de aprovação financeira.

### 2.2 Justificativa da Contratação

A solução consiste exclusivamente em **parametrização da transação ZFI0057**, nativa do ambiente SAP FI já implantado na VIX Manutenção. Não há necessidade de desenvolvimento ABAP, integração externa ou aquisição de licença adicional. O esforço é pontual, de baixo risco técnico e totalmente reversível via ordem de transporte.

### 2.3 ROI Esperado

| Benefício | Impacto Estimado |
|---|---|
| Eliminação de retrabalho (estorno/correção manual) | Redução de horas de backoffice financeiro |
| Conformidade com política de alçadas do Grupo GAB | Redução de achados em auditoria interna/externa |
| Bloqueio técnico de postagem não aprovada | Eliminação de risco de lançamento indevido |
| Rastreabilidade completa via CDHDR/CDPOS | Atendimento a requisitos de controles internos (SOX-like) |

O custo máximo do projeto (R$ 8.640,00) é recuperado na primeira ocorrência de estorno evitado ou achado de auditoria não materializado.

---

## 3. OBJETIVO DA CONTRATAÇÃO

Contratar fornecedor especializado em SAP FI para **parametrizar o fluxo de aprovação de lançamentos pré-editados**, incluindo o Diretor Financeiro como aprovador obrigatório na cadeia de aprovação, com encaminhamento automático de task via SBWP, bloqueio técnico de postagem enquanto aprovação pendente, e rastreabilidade completa via log de auditoria SAP — tudo realizado exclusivamente por parametrização da transação ZFI0057, sem qualquer desenvolvimento ABAP ou alteração de código-fonte.

---

## 4. ESCOPO DA CONTRATAÇÃO

### 4.1 Escopo Incluso

O fornecedor deverá atender integralmente aos seguintes requisitos funcionais:

| ID | Requisito | Descrição |
|---|---|---|
| **RF001** | Parametrização do DF como aprovador obrigatório | Configurar o Diretor Financeiro como aprovador obrigatório para lançamentos pré-editados via transação ZFI0057 |
| **RF002** | Uso exclusivo de ZFI0057 | Toda a parametrização deve ser realizada exclusivamente pela transação ZFI0057 — vedada qualquer alteração em objetos ABAP |
| **RF003** | Identificação do ID SAP do DF | Levantar e validar o ID de usuário SAP do Diretor Financeiro antes do início da parametrização |
| **RF004** | Aprovação obrigatória sem bypass | A aprovação do DF deve ser tecnicamente obrigatória — nenhum perfil ou papel SAP poderá contornar o passo de aprovação |
| **RF005** | Posição do DF na cadeia de aprovação | Definir e documentar a posição exata do DF na cadeia de aprovação existente, preservando os aprovadores já configurados |
| **RF006** | Encaminhamento automático ao SBWP | O sistema deve encaminhar automaticamente a task de aprovação para a caixa de entrada SBWP do DF assim que o lançamento for submetido |
| **RF007** | Item de trabalho com informações completas | O item de trabalho no SBWP deve conter: número do lançamento, data, valor, centro de custo, conta contábil e responsável pelo lançamento |
| **RF008** | Ações Aprovar/Rejeitar direto do SBWP | O DF deve conseguir aprovar ou rejeitar o lançamento diretamente pelo SBWP, sem necessitar navegar para outra transação |
| **RF009** | Fluxo de rejeição com retorno e notificação | Em caso de rejeição, o lançamento deve retornar ao status anterior (pré-editado) e o criador do lançamento deve receber notificação automática |
| **RF010** | Aprovadores existentes sem alteração | Os aprovadores já parametrizados no fluxo atual devem ser mantidos integralmente, sem nenhuma alteração em suas configurações |
| **RF011** | Log de auditoria via CDHDR/CDPOS | Toda ação do DF (aprovação ou rejeição) deve gerar registro rastreável nas tabelas SAP CDHDR/CDPOS |
| **RF012** | Bloqueio técnico de postagem | Enquanto a aprovação do DF estiver pendente, o sistema deve bloquear tecnicamente qualquer tentativa de postagem do lançamento |
| **RF013** | Parametrização via ordem de transporte | A parametrização deve ser transportada seguindo o ciclo DEV → QAS → PRD via ordem de transporte SAP padrão |
| **RF014** | Consulta de histórico por perfil de auditoria | Usuários com perfil de auditoria devem conseguir consultar o histórico completo de aprovações/rejeições dos lançamentos pré-editados |

### 4.2 Escopo Excluso

Os seguintes itens estão **expressamente fora do escopo** deste Work Request:

1. **Outros módulos SAP** — Nenhuma configuração, parametrização ou análise em módulos MM, CO, SD, HR, PP ou quaisquer outros módulos além do FI.
2. **Desenvolvimento ABAP ou modificação de código-fonte** — Vedado o desenvolvimento de programas Z, enhancements, user exits, BADIs ou qualquer alteração de objetos de repositório ABAP.
3. **Integração com sistemas externos** — Nenhuma integração com ERP paralelo, sistemas de terceiros, RPA, APIs externas ou middleware.
4. **Outros tipos de lançamento SAP FI** — A solução aplica-se exclusivamente a lançamentos pré-editados; lançamentos avulsos, periódicos, de estorno ou de qualquer outro tipo estão fora do escopo.
5. **Reengenharia do processo de aprovação** — O fornecedor não deve propor ou executar redesenho do fluxo de aprovação existente; a parametrização deve ser realizada dentro da estrutura atual.
6. **Treinamento de usuários finais em massa** — Está previsto apenas treinamento do Diretor Financeiro (Andre Chieppe) conforme premissas; programas de capacitação para demais usuários estão excluídos.

---

## 5. PREMISSAS E RESPONSABILIDADES DO GRUPO

O cliente (VIX Manutenção / Grupo GAB) se compromete a disponibilizar os seguintes recursos e condições durante toda a execução do projeto:

| # | Premissa / Responsabilidade do Grupo |
|---|---|
| 1 | **Ambiente SAP FI de Produção** implantado, estável e operacional na data de kickoff |
| 2 | **Ambiente QAS disponível** para execução dos testes de homologação antes do transporte para PRD |
| 3 | **Equipe de Basis/DTI** com autorizações SAP_BASIS habilitadas para criação e liberação de ordens de transporte |
| 4 | **Calendário de transportes SAP** disponível e compartilhado com o fornecedor até o kickoff |
| 5 | **Andre Chieppe (Diretor Financeiro) disponível** para sessão de treinamento e para validação funcional no ambiente QAS |
| 6 | **Designação do GP** pelo PMO dentro de 5 dias úteis após assinatura do TAP |
| 7 | **Homologação dos entregáveis** em até 5 dias úteis após entrega formal de cada marco |
| 8 | **Fornecimento do ID SAP do DF** à equipe do fornecedor até o 2.º dia útil após kickoff |
| 9 | **Acesso ao ambiente DEV** liberado para o consultor do fornecedor até o 1.º dia útil após kickoff |
| 10 | **Aprovação formal de cada entregável** pelo GP designado, usando os critérios binários definidos na Seção 7 |

> **Atenção:** O não cumprimento de qualquer premissa acima pelo cliente poderá implicar revisão de prazo proporcional ao tempo de bloqueio, sem penalidade ao fornecedor, desde que formalmente comunicado via canal de governança (ver Seção 8).

---

## 6. CRONOGRAMA ESPERADO

| Marco | Descrição | Data Estimada |
|---|---|---|
| **M0** | Emissão do Work Request | 2026-05-18 |
| **M1** | Prazo para submissão de propostas | 2026-06-06 |
| **M2** | Avaliação e seleção do fornecedor | 2026-06-11 |
| **M3** | Assinatura do TAP / Início do prazo contratual | 2026-06-12 |
| **M4** | Kickoff do projeto | 2026-06-13 |
| **M5** | Levantamento e validação do ID SAP do DF + mapeamento da cadeia de aprovação atual | 2026-06-20 |
| **M6** | Parametrização concluída em DEV + documentação técnica | 2026-07-11 |
| **M7** | Testes em QAS aprovados pelo cliente (homologação) | 2026-08-08 |
| **M8** | Transporte para PRD + validação em produção | 2026-09-05 |
| **M9** | Go-live — encerramento técnico e treinamento do DF | 2026-09-30 |

> **Base de cálculo:** 60 dias úteis a partir de M3 (2026-06-12), considerando calendário comercial brasileiro. Datas sujeitas a ajuste mediante acordo formal entre as partes no kickoff.

---

## 7. ENTREGÁVEIS OBRIGATÓRIOS

Todos os entregáveis abaixo são obrigatórios. O critério de aceite é **binário**: o entregável está aceito (SIM) ou não está aceito (NÃO) — não existe aceite parcial.

| # | Entregável | Marco Associado | Critério de Aceite (Binário) |
|---|---|---|---|
| **E1** | Documento de Análise da Cadeia de Aprovação Atual | M5 | SIM: documento aprovado pelo GP, contendo cadeia atual mapeada e posição definida para o DF. NÃO: qualquer item ausente ou não aprovado pelo GP. |
| **E2** | Registro do ID SAP do DF validado | M5 | SIM: ID SAP confirmado pelo Basis/DTI e registrado em ata. NÃO: ausência de confirmação formal. |
| **E3** | Parametrização concluída em DEV (ZFI0057) | M6 | SIM: todos os 14 RFs parametrizados e verificáveis em DEV pelo cliente. NÃO: qualquer RF pendente ou não verificável. |
| **E4** | Documentação Técnica da Parametrização | M6 | SIM: documento descrevendo cada configuração realizada, com prints de telas e referências de tabelas SAP. NÃO: ausência de qualquer RF documentado. |
| **E5** | Roteiro de Testes (casos de teste) | M6 | SIM: roteiro cobrindo todos os 14 RFs com passos, dados de entrada, resultado esperado e campo de resultado. NÃO: qualquer RF sem caso de teste. |
| **E6** | Relatório de Testes em QAS aprovado | M7 | SIM: todos os casos de teste executados com resultado conforme, assinado pelo GP e pelo DF. NÃO: qualquer caso de teste reprovado ou não executado. |
| **E7** | Ordem de Transporte DEV→QAS→PRD executada | M8 | SIM: ordem de transporte liberada e aplicada em PRD sem erros, confirmada pelo Basis. NÃO: erro no transporte ou ausência de confirmação do Basis. |
| **E8** | Validação pós-transporte em PRD | M8 | SIM: ao menos um lançamento pré-editado real processado com aprovação do DF em PRD, com log CDHDR/CDPOS capturado. NÃO: ausência de evidência de funcionamento em PRD. |
| **E9** | Registro de Treinamento do DF | M9 | SIM: ata de treinamento assinada por Andre Chieppe, comprovando sessão realizada. NÃO: ausência de ata assinada. |
| **E10** | Relatório de Encerramento do Projeto | M9 | SIM: documento com resumo da solução, evidências de go-live, lições aprendidas e term sheet de aceite assinado pelo Sponsor. NÃO: ausência de qualquer seção ou assinatura. |

---

## 8. GOVERNANÇA E COMUNICAÇÃO

### 8.1 Estrutura de Governança

| Papel | Responsável | Atribuição |
|---|---|---|
| **Sponsor** | Andre Chieppe (Diretor Financeiro — VIX Manutenção) | Aprovação final do go-live; escalação de bloqueios estratégicos |
| **Gerente de Projeto (GP)** | A designar pelo PMO | Gestão do projeto, aprovação formal de entregáveis, controle de prazo e orçamento |
| **Consultor Líder (Fornecedor)** | A indicar na proposta | Execução técnica, entrega dos artefatos, comunicação com GP |
| **Analista Basis/DTI** | VIX Manutenção | Suporte a autorizações, transportes e acesso a ambientes |

### 8.2 Comunicação

- **Reunião de Status Semanal:** toda segunda-feira, 30 minutos, formato a combinar no kickoff (presencial ou videoconferência).
- **Canal oficial de comunicação:** e-mail corporativo, com GP em cópia em todas as mensagens técnicas.
- **Comunicação de bloqueios:** bloqueios que impactem prazo ou orçamento devem ser reportados ao GP em até 24 horas após identificação, com plano de mitigação sugerido.
- **Aprovação de entregáveis:** o GP tem até **5 dias úteis** após a entrega formal para aceitar (SIM) ou rejeitar (NÃO) cada entregável, com justificativa escrita no caso de rejeição.
- **Retrabalho:** em caso de rejeição, o fornecedor tem até **5 dias úteis** para corrigir e reapresentar o entregável, sem custo adicional.

### 8.3 Gestão de Mudanças

Qualquer alteração de escopo, prazo ou orçamento requer **Change Request (CR)** formal, aprovado pelo Sponsor antes da execução. CRs não aprovados não serão executados nem faturados.

---

## 9. CONDIÇÕES COMERCIAIS

### 9.1 Orçamento

| Item | Valor |
|---|---|
| Orçamento base do projeto | R$ 7.200,00 |
| Contingência (20%) | R$ 1.440,00 |
| **Orçamento máximo total** | **R$ 8.640,00** |

Propostas acima do orçamento máximo serão automaticamente desclassificadas.

### 9.2 Faturamento por Marcos

O pagamento será realizado conforme entrega e aceite formal dos marcos abaixo:

| Marco | Entregáveis Associados | % do Contrato | Valor (base R$ 8.640,00) |
|---|---|---|---|
| **Marco 1** — Assinatura do contrato / kickoff | — | 20% | R$ 1.728,00 |
| **Marco 2** — Parametrização em DEV + Documentação Técnica | E1, E2, E3, E4, E5 | 30% | R$ 2.592,00 |
| **Marco 3** — Testes em QAS aprovados | E6 | 25% | R$ 2.160,00 |
| **Marco 4** — Go-live em PRD + Encerramento | E7, E8, E9, E10 | 25% | R$ 2.160,00 |
| **Total** | | **100%** | **R$ 8.640,00** |

> Faturamento condicionado ao aceite formal (critério SIM) de todos os entregáveis associados ao marco.

### 9.3 Penalidades por Atraso

- **Atraso imputável ao fornecedor:** multa de 0,5% do valor total do contrato por dia útil de atraso em cada marco, limitada a 10% do valor total.
- **Atraso imputável ao cliente:** prazo estendido proporcionalmente, sem penalidade ao fornecedor, desde que o bloqueio seja formalmente comunicado e aceito pelo GP.

### 9.4 Garantia de Funcionamento

- O fornecedor garante o funcionamento da solução parametrizada por **90 dias corridos** após o go-live em PRD (garantia mínima obrigatória — propostas com prazo inferior serão desclassificadas).
- Falhas na parametrização identificadas dentro do período de garantia serão corrigidas sem custo adicional, em prazo a ser acordado com o GP (máximo 5 dias úteis).
- Após o encerramento do período de garantia, qualquer manutenção ou ajuste será objeto de novo Work Request.

### 9.5 Propriedade Intelectual

Todos os artefatos entregues (documentação, roteiros de teste, relatórios) são de propriedade exclusiva da VIX Manutenção / Grupo GAB a partir do aceite formal. A parametrização realizada no ambiente SAP do cliente é de sua propriedade integral.

---

## 10. ARTEFATO OBRIGATÓRIO — CONFORMIDADE DA PROPOSTA

A proposta comercial só será considerada válida se acompanhada da tabela de conformidade abaixo, **completamente preenchida** pelo fornecedor. Propostas sem este artefato ou com itens em branco serão desclassificadas.

**Instrução:** Para cada item, marque **OK** (atende plenamente), **NOK** (não atende) ou **Parcial** (atende com ressalva — obrigatório descrever em Observações).

---

### Grupo 1 — Qualificação do Fornecedor (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 1.1 | Empresa com CNPJ ativo e regularidade fiscal comprovada (certidões em validade) | | | |
| 1.2 | Experiência comprovada em projetos SAP FI (mínimo 2 projetos com documentação de referência) | | | |
| 1.3 | Consultor designado com certificação SAP FI ou experiência equivalente documentada | | | |
| 1.4 | Referências de clientes em projetos similares de parametrização SAP FI (mínimo 1 referência com contato) | | | |

---

### Grupo 2 — Entendimento do Escopo (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 2.1 | Proposta demonstra entendimento dos 14 requisitos funcionais (RF001 a RF014) | | | |
| 2.2 | Proposta confirma que a solução será realizada exclusivamente via ZFI0057, sem ABAP | | | |
| 2.3 | Proposta identifica e declara o que está fora do escopo (alinhado à Seção 4.2) | | | |
| 2.4 | Proposta descreve abordagem técnica para cada RF, com nível de detalhe suficiente para avaliação | | | |

---

### Grupo 3 — Plano de Trabalho e Cronograma (5 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 3.1 | Plano de trabalho com marcos alinhados ao cronograma da Seção 6 | | | |
| 3.2 | Prazo total dentro dos 60 dias úteis a partir do kickoff | | | |
| 3.3 | Estimativa de horas por fase / atividade declarada | | | |
| 3.4 | Plano de testes descrito, cobrindo todos os 14 RFs | | | |
| 3.5 | Estratégia de transporte DEV→QAS→PRD descrita | | | |

---

### Grupo 4 — Entregáveis (5 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 4.1 | Proposta lista e descreve todos os 10 entregáveis obrigatórios (E1 a E10) | | | |
| 4.2 | Proposta apresenta modelo ou índice da Documentação Técnica (E4) | | | |
| 4.3 | Proposta apresenta modelo ou estrutura do Roteiro de Testes (E5) | | | |
| 4.4 | Proposta confirma emissão do Relatório de Encerramento (E10) com termo de aceite | | | |
| 4.5 | Proposta confirma emissão de ata de treinamento assinada pelo DF (E9) | | | |

---

### Grupo 5 — Condições Comerciais (5 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 5.1 | Valor total da proposta dentro do orçamento máximo de R$ 8.640,00 | | | |
| 5.2 | Proposta apresenta composição de preço por marco, alinhada à Seção 9.2 | | | |
| 5.3 | Proposta aceita as penalidades por atraso descritas na Seção 9.3 | | | |
| 5.4 | Proposta aceita o período de garantia mínimo de 90 dias corridos após go-live | | | |
| 5.5 | Proposta declara prazo de validade da oferta (mínimo 30 dias corridos) | | | |

---

### Grupo 6 — Gestão de Riscos (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 6.1 | Proposta identifica os principais riscos técnicos do projeto | | | |
| 6.2 | Proposta descreve plano de mitigação para cada risco identificado | | | |
| 6.3 | Proposta declara dependências críticas do lado do cliente (alinhadas às premissas da Seção 5) | | | |
| 6.4 | Proposta descreve processo de escalonamento em caso de bloqueio crítico | | | |

---

### Grupo 7 — Premissas Aceitas (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 7.1 | Fornecedor aceita que o cliente fornecerá ambiente SAP FI PRD estável e QAS disponível | | | |
| 7.2 | Fornecedor aceita que o cliente fornecerá equipe Basis/DTI com SAP_BASIS durante o projeto | | | |
| 7.3 | Fornecedor aceita que o calendário de transportes SAP será fornecido até o kickoff | | | |
| 7.4 | Fornecedor aceita que o ID SAP do DF será fornecido até o 2.º dia útil após kickoff | | | |

---

### Grupo 8 — Governança e Comunicação (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 8.1 | Fornecedor aceita reunião de status semanal no formato definido pelo cliente | | | |
| 8.2 | Fornecedor aceita comunicar bloqueios em até 24 horas via canal oficial | | | |
| 8.3 | Fornecedor aceita o processo de aprovação de entregáveis em até 5 dias úteis pelo GP | | | |
| 8.4 | Fornecedor aceita o processo de Change Request para alterações de escopo | | | |

---

### Grupo 9 — Conformidade Técnica SAP (4 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 9.1 | Proposta confirma que nenhum objeto ABAP será criado ou modificado | | | |
| 9.2 | Proposta confirma que os aprovadores existentes não serão alterados (RF010) | | | |
| 9.3 | Proposta confirma geração de log em CDHDR/CDPOS para todas as ações do DF (RF011) | | | |
| 9.4 | Proposta confirma que o bloqueio técnico de postagem (RF012) será implementado via parametrização, sem ABAP | | | |

---

### Grupo 10 — Declarações do Fornecedor (6 itens)

| # | Item | OK | NOK | Observações |
|---|---|---|---|---|
| 10.1 | Fornecedor declara não ter conflito de interesse com a VIX Manutenção ou Grupo GAB | | | |
| 10.2 | Fornecedor declara que os dados do cliente serão tratados com confidencialidade | | | |
| 10.3 | Fornecedor declara ter lido e compreendido integralmente este Work Request | | | |
| 10.4 | Fornecedor declara que o consultor designado estará disponível durante todo o projeto | | | |
| 10.5 | Fornecedor declara capacidade de iniciar o projeto na data de kickoff estimada (2026-06-13) | | | |
| 10.6 | Fornecedor declara que todos os 41 itens desta tabela foram avaliados e respondidos | | | |

---

**Resumo de Conformidade (preencher pelo fornecedor):**

| | Quantidade |
|---|---|
| Itens OK | ___ / 41 |
| Itens NOK | ___ / 41 |
| Itens Parcial | ___ / 41 |

> **Regra de desclassificação:** Propostas com qualquer item **NOK** nos Grupos 1, 2, 5 ou 10 serão automaticamente desclassificadas. Itens **Parcial** nos demais grupos serão avaliados pela VMO Consultoria com base nas observações declaradas.

---

## 11. PROCESSO DE SUBMISSÃO

### 11.1 Prazo e Canal

- **Prazo final para envio:** **2026-06-06, até 18h00 (horário de Brasília)**
- **Canal de envio:** e-mail para o GP designado pelo PMO, com cópia para Andre Chieppe (sponsor)
- **Assunto obrigatório do e-mail:** `[PROPOSTA] PROJ-2026-001 — [Nome do Fornecedor]`

### 11.2 Documentos Obrigatórios na Proposta

| # | Documento | Formato |
|---|---|---|
| 1 | Proposta Técnica (descrevendo abordagem para cada RF) | PDF |
| 2 | Proposta Comercial (com composição de preço por marco) | PDF |
| 3 | Tabela de Conformidade (Seção 10) completamente preenchida | PDF ou planilha |
| 4 | Currículo do consultor designado | PDF |
| 5 | Documentação de referência (mínimo 2 projetos SAP FI) | PDF |
| 6 | Certidões de regularidade fiscal (CNPJ, FGTS, Trabalhista) | PDF |

### 11.3 Critérios de Avaliação

As propostas válidas (sem desclassificação automática) serão avaliadas pelos seguintes critérios, em ordem de peso:

| Critério | Peso |
|---|---|
| Adequação técnica (cobertura dos 14 RFs) | 40% |
| Preço total (menor preço dentro do orçamento) | 30% |
| Experiência comprovada em SAP FI | 20% |
| Qualidade do plano de trabalho e cronograma | 10% |

### 11.4 Esclarecimentos

Dúvidas sobre este Work Request devem ser enviadas por e-mail até **2026-05-30** (5 dias úteis antes do prazo de submissão). As respostas serão consolidadas e enviadas a todos os fornecedores convidados simultaneamente, preservando a confidencialidade de quem perguntou.

### 11.5 Sigilo e Confidencialidade

Este documento é de uso restrito e destinado exclusivamente aos fornecedores convidados. Sua reprodução, distribuição ou uso para fins outros que não a elaboração da proposta é vedada sem autorização prévia da VMO Consultoria e da VIX Manutenção.

---

*Work Request emitido pelo VMO Consultoria em nome da VIX Manutenção.*
