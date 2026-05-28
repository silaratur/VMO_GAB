# WORK REQUEST — DEM-2026-008
## Integração SGMM03 — Campos Empresa e Contrato (InterCompany) — VIX Matriz

**Versão:** 1.0 | **Data de Emissão:** 2026-05-28
**Código:** DEM-2026-008
**Ticket de Origem:** #6800446
**Responsável:** Mara Rubia Silva Rocha (Holding DTI)
**GP/PMO:** A designar

---

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Valor |
|-------|-------|
| Código do Projeto | DEM-2026-008 |
| Demanda de Origem | Chamado #6800446 — Sistemática ERP |
| Tipo de Solução | Desenvolvimento/Configuração SAP (módulo PM/FI) |
| Sponsor | A confirmar — Diretor ou superior (CB-1) |
| GP/PMO | A designar |
| Solicitante | Jenifer dos Santos Carvalho — VIX Matriz |
| Responsável DTI | Mara Rubia Silva Rocha — Holding DTI |
| Validade da Proposta Esperada | Mínimo 30 dias a partir do recebimento |

---

## 2. CONTEXTO E PROBLEMA DE NEGÓCIO

A VIX Matriz opera com integração entre o sistema de gerenciamento de manutenção (SGM) e o SAP
via interface **SGMM03**, no fluxo denominado **InterCompany**. Neste fluxo, as Ordens de Manutenção
(OMs) são criadas e gerenciadas primariamente no SGM e replicadas para o SAP PM para fins de
controle, custeio e relatórios gerenciais.

**O problema atual:** Os campos **Empresa** e **Contrato** inseridos pela equipe de manutenção
durante a abertura de OM no SGM **não são transmitidos automaticamente ao SAP**. Isso obriga
a equipe a preencher manualmente esses campos no SAP após cada criação ou alteração de OM —
gerando retrabalho operacional contínuo e risco de inconsistência de dados entre os dois sistemas.

**Precedente técnico positivo:** O campo **Centro de Planejamento** foi integrado com sucesso
anteriormente nessa mesma interface SGMM03, demonstrando viabilidade técnica para a integração
incremental de campos adicionais.

**Urgência:** O chamado está em atraso de SLA desde 15/05/2026. O processo de seleção de
consultoria foi iniciado e este Work Request formaliza a contratação.

---

## 3. OBJETIVO DA CONTRATAÇÃO

Contratar serviço de consultoria SAP especializada em módulo PM/FI para:

1. Analisar e especificar tecnicamente a integração dos campos Empresa e Contrato na interface SGMM03
2. Implementar a integração para os eventos de **criação** e **alteração** de Ordens de Manutenção
3. Realizar testes completos nos ambientes DEV, QAS e PRD
4. Apoiar o go-live e período de estabilização
5. Documentar tecnicamente a solução e repassar ao time de sustentação DTI

**Critério de sucesso desta contratação:** 100% das OMs InterCompany criadas ou alteradas após
o go-live têm os campos Empresa e Contrato gravados automaticamente no SAP, com aceite formal
da VIX Matriz e documentação entregue ao time de sustentação.

---

## 4. ESCOPO INCLUSO

### 4.1 Análise e Especificação

- **RF001/RF006:** Análise técnica dos campos Empresa e Contrato na estrutura da OM SAP PM — identificação dos campos SAP correspondentes, BAPIs/RFCs/IDocs necessários
- Mapeamento técnico completo da integração: leitura do SGM → transmissão via SGMM03 → gravação no SAP
- Especificação funcional detalhada da solução proposta
- Especificação técnica (identificação de objetos SAP, programas, user-exits ou BAdIs envolvidos)

### 4.2 Desenvolvimento e Configuração SAP

- **RF001:** Implementação da leitura e gravação do campo Empresa no evento de **criação** de OM
- **RF004:** Implementação da leitura e atualização do campo Empresa no evento de **alteração** de OM
- **RF006:** Implementação da leitura e gravação do campo Contrato no evento de **criação** de OM
- **RF009:** Implementação da leitura e atualização do campo Contrato no evento de **alteração** de OM
- **RF011:** Implementação de tratamento de erros com log/notificação em caso de falha
- **RNF001:** Garantia de performance ≤ 30 segundos por evento de integração
- **RNF003:** Implementação de lógica não-bloqueante (falha nos campos novos não impede a OM principal)
- **RNF005:** Rastreabilidade no log de mensagens WE05/WE09 do SAP

### 4.3 Testes

- Testes unitários e de integração em ambiente DEV
- Testes sistêmicos em ambiente QAS (a ser conduzido com apoio da DTI)
- Suporte ao UAT realizado pela VIX Matriz em ambiente QAS
- Relatório de execução de testes com evidências (printscreens ou logs)

### 4.4 Implantação e Go-live

- Plano de implantação (cutover) com janela de transporte DEV → QAS → PRD
- Suporte ao go-live em produção (presença ou disponibilidade remota no dia)
- Monitoramento dos primeiros 3 dias úteis após go-live
- Período de garantia de **15 dias corridos** após go-live

### 4.5 Documentação e Repasse

- Especificação funcional (para usuários finais e negócio)
- Especificação técnica (para sustentação ERP — identificação de todos os objetos SAP modificados)
- Manual de monitoramento da integração (como verificar logs, tratar erros comuns)
- Walkthrough presencial ou remoto de repasse ao time de sustentação DTI PM/FI

---

## 5. ESCOPO EXCLUSO

| Exclusão | Justificativa |
|----------|---------------|
| Alterações no sistema SGM | Sistema de origem — fora da responsabilidade desta contratação. O SGM é mantido por equipe própria. |
| Integração de outros campos da interface SGMM03 além de Empresa e Contrato | Escopo estrito — outros campos são demandas separadas com avaliação própria de custo/prazo |
| Campo Cenário/CenPlan (MAM1/MWV1) | Tem restrição técnica conhecida — tratamento separado, não faz parte desta contratação |
| Novas interfaces de integração SAP | A solução deve ser implementada exclusivamente dentro da interface SGMM03 existente |
| Implantação em outras divisões ou empresas do grupo além da VIX Matriz | O escopo atual é VIX Matriz. Outras empresas requerem análise de impacto separada |
| Modificações na estrutura de dados do SAP PM (criação de novos campos Z) | A implementação deve usar campos SAP existentes — sem criação de campos customizados no dicionário de dados |

---

## 6. PREMISSAS E RESPONSABILIDADES DO CONTRATANTE

O Grupo Águia Branca / DTI disponibilizará ao fornecedor selecionado:

1. **Acesso aos ambientes SAP:** DEV, QAS e PRD com perfil adequado para desenvolvimento e transporte
2. **Documentação disponível:** Mapeamento_SGMM03_InterCompany.pdf e especificação da interface existente
3. **Ponto focal técnico:** Analista DTI para acompanhar o desenvolvimento e aprovar avanços
4. **Usuários para UAT:** Equipe VIX Matriz (Jenifer dos Santos Carvalho como responsável) para testes de aceitação
5. **Janelas de transporte:** Coordenação das janelas de transporte DEV→QAS→PRD conforme calendário de mudanças do grupo
6. **Aprovação de cada ambiente:** GP/DTI aprova promoção entre ambientes antes de qualquer transporte

---

## 7. CRONOGRAMA ESPERADO (MARCOS DE ALTO NÍVEL)

| Marco | Data Esperada | Descrição |
|-------|--------------|-----------|
| M0 — Recebimento de Propostas | 29/05/2026 (já previsto) | Equalização das 4 propostas em andamento |
| M1 — Seleção e Contratação | Até 13/06/2026 | Assinatura do contrato com consultora selecionada |
| M2 — Kick-off | 16/06/2026 | Reunião de início com DTI, VIX Matriz e consultora |
| M3 — Especificação Técnica Aprovada | 20/06/2026 | Especificação funcional e técnica aprovada pelo GP |
| M4 — Desenvolvimento Completo (DEV) | 04/07/2026 | 100% dos RF Must Have implementados em DEV |
| M5 — Testes QAS Aprovados | 11/07/2026 | Testes sistêmicos QAS aprovados pela DTI |
| M6 — UAT Aprovado | 18/07/2026 | UAT aprovado pela VIX Matriz (Jenifer) |
| M7 — Go-live PRD | 21/07/2026 | Transporte para produção com go-live autorizado |
| M8 — Estabilização e Encerramento | 08/08/2026 | 15 dias de produção estável + documentação entregue |

> **Nota:** O fornecedor pode propor cronograma alternativo com justificativa. Cronograma detalhado
> será negociado com o fornecedor selecionado e incorporado ao contrato. O prazo final (M8) é
> **08/08/2026** — inclui buffer de contingência de 15% sobre o prazo de execução.

---

## 8. ENTREGÁVEIS OBRIGATÓRIOS E CRITÉRIOS DE ACEITE

| # | Entregável | Critério de Aceite Binário |
|---|-----------|---------------------------|
| E1 | Especificação Funcional | Aprovada pelo GP e pela VIX Matriz antes do início do desenvolvimento — SIM/NÃO |
| E2 | Especificação Técnica | Aprovada pelo GP e pelo analista técnico DTI — SIM/NÃO |
| E3 | Relatório de Testes DEV | Todos os RF001, RF004, RF006, RF009, RF011 testados com evidências — SIM/NÃO |
| E4 | Relatório de Testes QAS | Testes sistêmicos executados e aprovados pelo GP/DTI — SIM/NÃO |
| E5 | Relatório de UAT | VIX Matriz aprova todos os Must Have com aceite assinado — SIM/NÃO |
| E6 | Plano de Implantação (Cutover) | Plano com janela, rollback e responsáveis aprovado pelo GP antes do go-live — SIM/NÃO |
| E7 | Documentação Técnica completa | Spec funcional + spec técnica + manual de monitoramento entregues à DTI — SIM/NÃO |
| E8 | Walkthrough de repasse | Sessão de repasse com time sustentação DTI PM/FI com confirmação de suficiência — SIM/NÃO |
| E9 | Relatório de estabilização | 15 dias de produção documentados com zero incidentes relacionados à integração — SIM/NÃO |

---

## 9. GOVERNANÇA E COMUNICAÇÃO

| Comunicação | Audiência | Frequência | Canal |
|-------------|-----------|------------|-------|
| Status Report da consultora | GP + Mara Rubia | Semanal (durante execução) | E-mail |
| Reunião de acompanhamento | GP + Consultora | Semanal | Teams ou presencial |
| Aprovação de entregáveis | GP / Sponsor | Por marco | E-mail com registro |
| Alertas de desvio | GP + Mara Rubia | Imediato (quando identificado) | E-mail + Teams |
| Comunicado de go-live | Todos stakeholders | Pontual | E-mail |

**Canal oficial:** E-mail para Mara Rubia Silva Rocha (Holding DTI) com cópia para GP designado

---

## 10. CONDIÇÕES COMERCIAIS

**Modelo de faturamento:** Por marcos de entregáveis aprovados (não por hora):
- Marco M3 (Especificação Aprovada): 25% do valor total
- Marco M6 (UAT Aprovado): 50% do valor total
- Marco M8 (Encerramento): 25% do valor total

**Envelope de referência:** R$ 18.000 a R$ 40.000 (faixa referencial — propostas acima do teto
precisam de justificativa técnica detalhada e aprovação do sponsor).

**Prazo de pagamento:** 30 dias da aprovação do marco correspondente.

**Penalidades por atraso:** Atraso no go-live (M7) superior a 5 dias úteis sem justificativa
aceita pelo GP: multa de 1% do valor total por dia de atraso, limitada a 10%.

**Período de garantia:** 15 dias corridos após o go-live em produção, com SLA de atendimento
de incidentes críticos em até 4 horas úteis (resposta) e 24 horas úteis (correção).

**Suporte pós-garantia:** Proposta opcional de SLA de suporte por 6 meses após o encerramento.

---

## 11. ARTEFATO OBRIGATÓRIO — CHECKLIST DE PROPOSTA

**ATENÇÃO:** Toda proposta submetida DEVE conter este checklist preenchido com as colunas
OK / NOK / Observações. Propostas sem o artefato completo serão **desclassificadas automaticamente**.

```
Grupo 1 — Identificação da Proposta
  1.1 Nome do fornecedor                                      [ ] OK  [ ] NOK  Obs:
  1.2 Projeto / Demanda (DEM-2026-008)                        [ ] OK  [ ] NOK  Obs:
  1.3 Tipo de solução (SAP PM/FI — Desenvolvimento)           [ ] OK  [ ] NOK  Obs:
  1.4 Data de recebimento da proposta                         [ ] OK  [ ] NOK  Obs:
  1.5 Versão da proposta                                      [ ] OK  [ ] NOK  Obs:
  1.6 Validade da proposta (mín. 30 dias)                     [ ] OK  [ ] NOK  Obs:

Grupo 2 — Escopo Detalhado da Entrega
  2.1 Objetivo da solução claramente descrito                 [ ] OK  [ ] NOK  Obs:
  2.2 Funcionalidades incluídas detalhadas (RF001–RF011)      [ ] OK  [ ] NOK  Obs:
  2.3 Módulos SAP impactados listados (PM, FI, SGMM03)        [ ] OK  [ ] NOK  Obs:
  2.4 Integrações descritas (SGMM03 SGM↔SAP)                 [ ] OK  [ ] NOK  Obs:
  2.5 Relatórios/logs impactados descritos (WE05/WE09)        [ ] OK  [ ] NOK  Obs:
  2.6 Necessidade de licenças informada ou declarada N/A      [ ] OK  [ ] NOK  Obs:

Grupo 3 — Exclusões de Escopo
  3.1 Exclusões explicitamente listadas                       [ ] OK  [ ] NOK  Obs:
  3.2 Sem frases genéricas ou ambíguas nas exclusões          [ ] OK  [ ] NOK  Obs:

Grupo 4 — Premissas
  4.1 Premissas técnicas claramente descritas                 [ ] OK  [ ] NOK  Obs:
  4.2 Premissas de acesso a ambientes SAP (DEV/QAS/PRD)       [ ] OK  [ ] NOK  Obs:
  4.3 Premissas de aprovação de entregas intermediárias       [ ] OK  [ ] NOK  Obs:

Grupo 5 — Metodologia e Abordagem
  5.1 Metodologia adotada explicitamente definida             [ ] OK  [ ] NOK  Obs:
  5.2 Etapas do projeto claramente descritas                  [ ] OK  [ ] NOK  Obs:
  5.3 Processo de validação e aceite das entregas definido    [ ] OK  [ ] NOK  Obs:

Grupo 6 — Entregáveis
  6.1 Especificação funcional                                 [ ] OK  [ ] NOK  Obs:
  6.2 Especificação técnica                                   [ ] OK  [ ] NOK  Obs:
  6.3 Documentação da solução/configuração SAP                [ ] OK  [ ] NOK  Obs:
  6.4 Plano de testes detalhado                               [ ] OK  [ ] NOK  Obs:
  6.5 Relatórios de execução de testes (DEV+QAS+UAT)          [ ] OK  [ ] NOK  Obs:
  6.6 Plano de implantação / Cutover                          [ ] OK  [ ] NOK  Obs:
  6.7 Plano de suporte pós-implantação (garantia 15 dias)     [ ] OK  [ ] NOK  Obs:
  6.8 Plano de repasse para sustentação DTI PM/FI             [ ] OK  [ ] NOK  Obs:
  6.9 Status reports semanais durante a execução              [ ] OK  [ ] NOK  Obs:

Grupo 7 — Cronograma e Prazos
  7.1 Cronograma detalhado por fase/marco                     [ ] OK  [ ] NOK  Obs:
  7.2 Data de go-live proposta (meta: 21/07/2026)             [ ] OK  [ ] NOK  Obs:
  7.3 Data de encerramento proposta (meta: 08/08/2026)        [ ] OK  [ ] NOK  Obs:

Grupo 8 — Equipe e Qualificações
  8.1 CV do consultor SAP PM principal (anos experiência PM)  [ ] OK  [ ] NOK  Obs:
  8.2 Experiência em integração SAP/interfaces comprovada     [ ] OK  [ ] NOK  Obs:
  8.3 Experiência com módulo FI (campos InterCompany)         [ ] OK  [ ] NOK  Obs:

Grupo 9 — Condições Comerciais
  9.1 Valor total e composição (por fase/marco)               [ ] OK  [ ] NOK  Obs:
  9.2 Modelo de faturamento por marcos (não por hora)         [ ] OK  [ ] NOK  Obs:
  9.3 Período de garantia declarado (mínimo 15 dias)          [ ] OK  [ ] NOK  Obs:
  9.4 Política de atendimento de incidentes críticos          [ ] OK  [ ] NOK  Obs:

Grupo 10 — Conformidade
  10.1 Proposta dentro do prazo de submissão                  [ ] OK  [ ] NOK  Obs:
  10.2 Formato aceito (PDF + planilha separada para custos)   [ ] OK  [ ] NOK  Obs:
  10.3 Artefato obrigatório (este checklist) preenchido       [ ] OK  [ ] NOK  Obs:
```

---

## 12. PROCESSO DE SUBMISSÃO

**Prazo final de recebimento de propostas:** 29/05/2026 (já em curso — confirmação deste WR)

**Canal de envio:** E-mail para Mara Rubia Silva Rocha — Holding DTI
Assunto obrigatório: `[PROPOSTA] DEM-2026-008 — SGMM03 Empresa/Contrato — [Nome do Fornecedor]`

**Formato aceito:**
- 1 arquivo PDF com a proposta completa
- 1 planilha separada com composição de custos detalhada por fase

**Contato para esclarecimentos técnicos:** Mara Rubia Silva Rocha — Holding DTI (via ticket #6800446)

**Contato para esclarecimentos comerciais:** Mara Rubia Silva Rocha — Holding DTI

**Condições de desclassificação automática:**
- Proposta sem o Artefato Obrigatório (Grupo 10) preenchido
- Proposta sem valor total declarado
- Proposta sem data de go-live proposta
- Proposta recebida após o prazo final (quando em novo ciclo de cotação)
- Escopo proposto que inclua alterações no SGM (fora do escopo excluso)
