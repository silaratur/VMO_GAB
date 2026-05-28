# Especificação de Requisitos Funcionais (ERF) — DEM-2026-008
Projeto: Integração SGMM03 — Campos Empresa e Contrato (InterCompany)
Versão: 1.0 | Data: 2026-05-28
Analista: Rafael Requisito (VMO Autônomo)
Origem: Chamado #6800446 + Mapeamento_SGMM03_InterCompany.pdf

---

## 1. Requisitos Funcionais

### 1.1 Integração do Campo EMPRESA (Criação de OM)

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF001 | O sistema deve ler o campo **Empresa** da OM no SGM e gravá-lo no campo correspondente da OM no SAP via interface SGMM03 no evento de **criação** de nova OM | Must Have | Ao criar uma OM InterCompany no SGM com o campo Empresa preenchido, a OM criada no SAP deve conter o mesmo valor no campo Empresa — verificado em 100% dos casos de teste de criação (mínimo 10 OMs de teste) | Ticket #6800446 + Mapeamento SGMM03 |
| RF002 | O sistema deve preservar o valor do campo Empresa integrado quando a OM no SAP sofrer alterações que não modifiquem o campo Empresa | Must Have | Ao alterar campos não relacionados à Empresa em uma OM SAP (ex: descrição, prioridade), o campo Empresa deve permanecer inalterado — verificado em 5 cenários de alteração | TAP — Escopo 1 |
| RF003 | O sistema deve tratar o caso de campo Empresa vazio no SGM sem gerar erro de integração | Should Have | Quando o campo Empresa no SGM estiver vazio durante a criação de OM, a integração deve prosseguir normalmente (sem falha) e gravar valor nulo/branco no SAP — sem interrupção do fluxo SGMM03 | Análise técnica — anti-pattern de tratamento de nulos |

### 1.2 Integração do Campo EMPRESA (Alteração de OM)

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF004 | O sistema deve ler o campo **Empresa** da OM no SGM e atualizá-lo no SAP via interface SGMM03 no evento de **alteração** de OM existente | Must Have | Ao alterar o campo Empresa de uma OM existente no SGM, a OM no SAP deve refletir o novo valor do campo Empresa após a sincronização — verificado em 100% dos casos de teste de alteração (mínimo 5 OMs de teste) | Ticket #6800446 — "alteração destes campos no SAP" |
| RF005 | O sistema deve registrar log/rastreabilidade quando o campo Empresa for alterado via integração SGMM03 | Should Have | O log de integração SGMM03 deve conter registro de data/hora, valor anterior e novo valor para cada alteração do campo Empresa via integração | Requisito de auditoria InterCompany |

### 1.3 Integração do Campo CONTRATO (Criação de OM)

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF006 | O sistema deve ler o campo **Contrato** da OM no SGM e gravá-lo no campo correspondente da OM no SAP via interface SGMM03 no evento de **criação** de nova OM | Must Have | Ao criar uma OM InterCompany no SGM com o campo Contrato preenchido, a OM criada no SAP deve conter o mesmo valor no campo Contrato — verificado em 100% dos casos de teste de criação (mínimo 10 OMs de teste) | Ticket #6800446 + Mapeamento SGMM03 |
| RF007 | O sistema deve validar que o valor do campo Contrato recebido do SGM é um contrato válido e ativo no SAP antes de gravar | Should Have | Ao receber um valor de Contrato inválido ou inativo do SGM, a integração deve registrar o erro no log sem interromper a criação da OM — a OM é criada no SAP com o campo Contrato vazio e uma mensagem de aviso é gerada | Análise técnica — integridade referencial |
| RF008 | O sistema deve tratar o caso de campo Contrato vazio no SGM sem gerar erro de integração | Should Have | Quando o campo Contrato no SGM estiver vazio durante a criação de OM, a integração deve prosseguir normalmente e gravar valor nulo/branco no SAP — sem interrupção do fluxo SGMM03 | Análise técnica |

### 1.4 Integração do Campo CONTRATO (Alteração de OM)

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF009 | O sistema deve ler o campo **Contrato** da OM no SGM e atualizá-lo no SAP via interface SGMM03 no evento de **alteração** de OM existente | Must Have | Ao alterar o campo Contrato de uma OM existente no SGM, a OM no SAP deve refletir o novo valor do campo Contrato após a sincronização — verificado em 100% dos casos de teste de alteração (mínimo 5 OMs de teste) | Ticket #6800446 — "alteração destes campos no SAP" |
| RF010 | O sistema deve registrar log/rastreabilidade quando o campo Contrato for alterado via integração SGMM03 | Should Have | O log de integração SGMM03 deve conter registro de data/hora, valor anterior e novo valor para cada alteração do campo Contrato via integração | Requisito de auditoria InterCompany |

### 1.5 Tratamento de Erros e Monitoramento

| ID | Descrição | Prioridade | Critério de Aceitação | Origem |
|----|-----------|------------|----------------------|--------|
| RF011 | O sistema deve gerar alerta/notificação quando ocorrer falha na integração dos campos Empresa ou Contrato | Must Have | Falhas de integração dos campos RF001 ou RF006 devem gerar mensagem de erro no log da interface SGMM03 e notificação ao responsável técnico — verificado simulando falha de integração em ambiente QAS | Análise técnica — monitoramento |
| RF012 | O sistema deve disponibilizar relatório de rastreabilidade comparando os valores dos campos Empresa e Contrato entre SGM e SAP para OMs InterCompany | Could Have | Relatório acessível no SAP listando OMs InterCompany com comparativo de campos Empresa/Contrato entre SGM e SAP nos últimos 30 dias | Análise técnica — controle de qualidade pós-go-live |

---

## 2. Requisitos Não-Funcionais

| ID | Categoria | Descrição | Prioridade | Critério de Aceitação |
|----|-----------|-----------|------------|----------------------|
| RNF001 | Performance | A integração dos campos Empresa e Contrato via SGMM03 deve ser concluída em até **30 segundos** após o evento de criação ou alteração de OM no SGM | Must Have | Teste de performance: 20 OMs criadas/alteradas no SGM; o tempo entre o evento no SGM e a gravação no SAP é ≤ 30 segundos em 100% dos casos |
| RNF002 | Disponibilidade | A integração SGMM03 para os campos Empresa e Contrato deve operar durante o mesmo horário de disponibilidade da interface SGMM03 existente | Must Have | A integração dos novos campos não reduz a janela de disponibilidade da interface SGMM03 — verificado pelos logs de disponibilidade nos primeiros 15 dias de produção |
| RNF003 | Integridade de Dados | Em caso de falha na integração, a OM no SAP deve ser criada/alterada normalmente sem os novos campos — a integração dos campos Empresa/Contrato é aditiva e não deve impedir a criação/alteração principal da OM | Must Have | Simulação de falha nos campos Empresa/Contrato durante testes QAS: a OM principal é criada corretamente no SAP, com apenas os novos campos ausentes e registro de erro no log |
| RNF004 | Segurança | Os dados dos campos Empresa e Contrato transmitidos via SGMM03 devem respeitar as permissões de acesso existentes no SAP PM — usuários sem permissão de visualizar contratos InterCompany não devem ter acesso via integração | Should Have | Teste de controle de acesso: usuário com perfil restrito não visualiza campos de contratos InterCompany que não tem permissão — validado pelo time de segurança da DTI |
| RNF005 | Rastreabilidade | Todas as integrações dos campos Empresa e Contrato via SGMM03 devem ser registradas no log de mensagens da interface (WE05/WE09 SAP), incluindo data/hora, tipo de evento (criação/alteração) e resultado (sucesso/erro) | Must Have | Log de integração WE05/WE09 contém registros de todas as OMs processadas com data/hora, tipo de evento e status — verificado nos testes de integração em QAS |
| RNF006 | Manutenibilidade | A implementação deve ser documentada tecnicamente (especificação funcional, especificação técnica, manual de sustentação) de forma que o time de sustentação ERP PM/FI da DTI possa manter e suportar a solução sem dependência da consultora | Must Have | Time de sustentação DTI PM/FI realiza walkthrough da documentação técnica e confirma suficiência para manutenção — aceite formal antes do encerramento do projeto |

---

## 3. Resumo de Priorização MoSCoW

| Prioridade | Qtde RF | Qtde RNF | Total | Percentual |
|------------|---------|---------|-------|-----------|
| Must Have | 6 (RF001, RF004, RF006, RF009, RF011 + RF002 parcial) | 4 (RNF001, RNF002, RNF003, RNF005, RNF006) | 11 | 55% |
| Should Have | 5 (RF002, RF003, RF005, RF007, RF008, RF010) | 1 (RNF004) | 6 | 30% |
| Could Have | 1 (RF012) | 0 | 1 | 5% |
| Won't Have | 0 | 0 | 0 | 0% |
| **TOTAL** | **12** | **6** | **18** | **100%** |

> **Nota:** Must Have cobre os 4 requisitos centrais do escopo (RF001, RF004, RF006, RF009 — os 2 campos × 2 eventos) + RF011 (tratamento de erros) + todos os RNFs de integridade e rastreabilidade. O projeto é considerado bem-sucedido quando todos os 11 Must Haves forem aceitos.

---

## 4. Glossário

| Termo | Definição |
|-------|-----------|
| **OM** | Ordem de Manutenção — registro no SAP PM que documenta uma solicitação de manutenção de equipamento |
| **SGM** | Sistema de Gerenciamento de Manutenção — sistema de origem que integra com o SAP via SGMM03 |
| **SGMM03** | Identificação da interface de integração entre SGM e SAP no fluxo InterCompany |
| **InterCompany** | Fluxo de transação entre duas empresas do mesmo grupo (ex: VIX Matriz e outra empresa do GAB) |
| **Campo Empresa** | Campo na OM que identifica a empresa do grupo à qual a ordem de manutenção está vinculada |
| **Campo Contrato** | Campo na OM que identifica o contrato (inter-empresas) ao qual a ordem de manutenção está vinculada |
| **Evento de Criação** | Quando uma nova OM é criada no SGM e replicada para o SAP via integração SGMM03 |
| **Evento de Alteração** | Quando uma OM existente no SAP é atualizada via integração SGMM03 após alteração no SGM |
| **BAPI/RFC** | Chamadas de função SAP usadas para criar/alterar registros via programação ou integração |
| **DEV/QAS/PRD** | Ambientes SAP: Desenvolvimento / Qualidade (Staging) / Produção |
| **UAT** | User Acceptance Testing — testes de aceitação realizados pelos usuários finais (VIX Matriz) |
| **WE05/WE09** | Transações SAP para visualização de logs de mensagens de interface (IDoc monitor) |
| **IDoc** | Intermediate Document — estrutura de dados SAP usada para troca de mensagens entre sistemas |
| **DTI** | Diretoria de Tecnologia da Informação do Grupo Águia Branca |
| **PM/FI** | Módulos SAP: Plant Maintenance (manutenção) e Financial Accounting (contabilidade) |

---

## 5. Aprovação

```
Analista de Requisitos: Rafael Requisito (VMO Autônomo)  Data: 2026-05-28
Solicitante: ___________________________________          Data: ___________
             Jenifer dos Santos Carvalho (VIX Matriz)
GP/PMO: ________________________________________         Data: ___________
```
