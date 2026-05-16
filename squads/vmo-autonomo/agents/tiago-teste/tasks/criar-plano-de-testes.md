---
task: "Criar Plano de Testes"
order: 2
input:
  - catalogo_uc: "Catálogo de casos de uso com fluxos completos da tarefa anterior"
  - erf: "ERF com requisitos RF e RNF priorizados com critérios de aceitação"
output:
  - plano_testes: "Plano de testes estruturado com casos de teste, ambiente, critérios de entrada/saída e matriz de rastreabilidade"
---

# Criar Plano de Testes

Estrutura o plano de testes completo do projeto seguindo a norma IEEE 829. A partir dos casos de uso mapeados e dos requisitos da ERF, define o escopo dos testes, o ambiente requerido, os critérios de entrada e saída da fase de testes, e os casos de teste individuais com rastreabilidade bidirecional para os requisitos. O objetivo é garantir cobertura de 100% dos RF e RNF Must Have e produzir um documento que qualquer QA engineer possa executar sem ambiguidade.

## Process

1. **Definir objetivo e escopo**: Documentar o que será testado (escopo incluso) e o que não será testado nesta fase (escopo excluso), com justificativa para exclusões.
2. **Documentar ambiente de testes**: Especificar servidor/infraestrutura, versão de banco de dados, fonte de dados de teste, ferramentas de execução e responsável pela configuração do ambiente.
3. **Definir critérios de entrada**: Condições que precisam ser verdadeiras antes de iniciar a execução dos testes (ex: ERF aprovada, ambiente configurado, dados de teste carregados).
4. **Definir critérios de saída**: Condições que encerram a fase de testes com aceite (ex: 100% dos CTs Must Have executados; taxa de aprovação ≥ 95% nos Must Have; zero defeitos de severidade Crítica abertos).
5. **Derivar casos de teste funcionais dos UCs**: Para cada UC Must Have, criar ao menos 2 CTs (fluxo principal + ao menos 1 alternativo ou exceção). Para Should Have e Could Have, ao menos 1 CT por UC.
6. **Derivar casos de teste não-funcionais dos RNFs**: Para cada RNF Must Have, criar ao menos 1 CT de verificação com método de execução específico (ex: teste de carga com JMeter, auditoria de segurança, teste de disponibilidade).
7. **Construir matriz de rastreabilidade RF ↔ CT**: Tabela que mostra, para cada RF e RNF, quais CTs o cobrem. Calcular percentual de cobertura por prioridade MoSCoW.
8. **Calcular e documentar resumo de cobertura**: Quantos requisitos de cada prioridade têm CT associado, em percentual.

## Output Format

```markdown
# PLANO DE TESTES — [Nome do Projeto]
Versão: 1.0 | Data: YYYY-MM-DD | Elaborado por: Tiago Teste (VMO)

---

## 1. Objetivo

[Objetivo do plano em 2-3 frases: o que será testado, qual o critério de aceite global e por que esses testes são necessários para autorizar o go-live]

---

## 2. Escopo

### 2.1 Incluso
- [Funcionalidade/módulo 1 — quais UCs e RFs são cobertos]
- [Funcionalidade/módulo 2]

### 2.2 Excluso
- [O que não será testado e por quê — ex: "Testes de stress com > 500 usuários simultâneos (fora do escopo de uso projetado para a fase 1)"]

---

## 3. Critérios de Entrada

Condições necessárias antes de iniciar a execução dos testes:
- [ ] ERF aprovada e publicada (versão ≥ 1.0)
- [ ] Catálogo de casos de uso aprovado
- [ ] Ambiente de testes configurado conforme Seção 5
- [ ] Dados de teste carregados e validados
- [ ] [Outros critérios específicos do projeto]

---

## 4. Critérios de Saída

Condições para encerramento da fase de testes com aceite formal:
- [ ] 100% dos casos de teste CT de categoria Must Have executados
- [ ] Taxa de aprovação ≥ 95% nos CTs Must Have
- [ ] Nenhum defeito de severidade Crítica ou Alta em aberto
- [ ] Defeitos de severidade Média com plano de resolução documentado e aceito pelo solicitante
- [ ] Relatório de execução de testes assinado pelo responsável do projeto

---

## 5. Ambiente de Testes

| Item | Especificação |
|------|--------------|
| Servidor de testes | [ex: VM Ubuntu 22.04, 8 vCPUs, 16GB RAM] |
| Banco de dados | [ex: PostgreSQL 15.3, instância isolada de produção] |
| Dados de teste | [ex: Massa sintética gerada com Faker; dados anonimizados de staging] |
| Ferramentas de execução | [ex: Testes funcionais: manual; Testes de carga: JMeter 5.6; Segurança: OWASP ZAP] |
| Responsável pelo ambiente | [Nome/perfil — ex: "Analista TI responsável pela configuração e manutenção"] |
| Janela de execução | [ex: Seg-Sex, 08h-18h; sem uso simultâneo com equipe de desenvolvimento] |

---

## 6. Casos de Teste

### 6.1 Testes Funcionais

| ID | Título | Referência | Prioridade | Pré-condição | Passos | Resultado Esperado | Aprovação |
|----|--------|------------|------------|--------------|--------|--------------------|-----------|
| CT001 | [Título descritivo — fluxo principal do UC] | UC001 / RF001 | Must Have | [estado inicial verificável] | 1. [ação do ator] 2. [ação do ator] 3. [verificação] | [comportamento específico que o sistema deve exibir — sem ambiguidade] | PASS / FAIL |
| CT002 | [Título — fluxo alternativo ou exceção do UC] | UC001 / RF001 | Must Have | [estado inicial] | 1. [ação] 2. [condição alternativa] 3. [verificação] | [resultado esperado do fluxo alternativo] | PASS / FAIL |
| CT003 | [Título — UC diferente] | UC002 / RF004, RF005 | Must Have | [pré-condição] | 1. [passo] 2. [passo] | [resultado] | PASS / FAIL |

### 6.2 Testes Não-Funcionais

| ID | Título | Referência | Prioridade | Pré-condição | Método de Verificação | Critério de Aprovação | Aprovação |
|----|--------|------------|------------|--------------|----------------------|-----------------------|-----------|
| CT_NF001 | [Título — ex: Carga com 50 usuários simultâneos] | RNF001 | Must Have | [ambiente com carga simulada] | [ex: Executar script JMeter com 50 usuários virtuais por 10 min] | [ex: Percentil 95 do tempo de resposta ≤ 3,0s em 100% das iterações] | PASS / FAIL |
| CT_NF002 | [Título — ex: Verificar criptografia TLS] | RNF003 | Must Have | [ambiente com tráfego simulado] | [ex: Captura de pacotes com Wireshark + verificação de certificado TLS] | [ex: 100% do tráfego usa TLS 1.3; certificado válido e não expirado] | PASS / FAIL |

---

## 7. Matriz de Rastreabilidade RF ↔ CT

| Requisito | Prioridade | Casos de Teste | Cobertura |
|-----------|------------|----------------|-----------|
| RF001 | Must Have | CT001, CT002 | ✅ Coberto |
| RF002 | Should Have | CT003 | ✅ Coberto |
| RF003 | Could Have | — | ⚠️ Não coberto (fora do escopo desta fase) |
| RNF001 | Must Have | CT_NF001 | ✅ Coberto |
| RNF002 | Must Have | CT_NF002 | ✅ Coberto |

---

## 8. Resumo de Cobertura

| Prioridade | Total de Requisitos | Com CT Associado | Cobertura |
|------------|--------------------|--------------------|-----------|
| Must Have (RF) | [N] | [N] | [100%] |
| Must Have (RNF) | [N] | [N] | [100%] |
| Should Have | [N] | [N] | [%] |
| Could Have | [N] | [N] | [%] |
| **Total** | **[N]** | **[N]** | **[%]** |
```

## Output Example

```markdown
# PLANO DE TESTES — SRF (Sistema de Rastreamento de Fornecedores)
Versão: 1.0 | Data: 2026-04-18 | Elaborado por: Tiago Teste (VMO)

---

## 1. Objetivo

Verificar que o Sistema de Rastreamento de Fornecedores (SRF) atende a 100% dos requisitos Must Have definidos na ERF v1.0 antes da autorização de go-live. Os testes cobrem as funcionalidades de monitoramento em tempo real, alertas automáticos de atraso e integração bidirecional com o SAP MM. O critério de aceite global é: taxa de aprovação ≥ 95% nos CTs Must Have e zero defeitos críticos ou altos em aberto.

---

## 2. Escopo

### 2.1 Incluso
- Monitoramento de entregas em tempo real (UC001, UC005 — RF001, RF002, RF008, RF009)
- Alertas automáticos de atraso com notificação por e-mail e Teams (UC002 — RF004, RF005)
- Integração com SAP MM: importação de pedidos e atualização de status (UC004 — RF006, RF007)
- Verificação de requisitos não-funcionais: performance (RNF001), disponibilidade (RNF002), segurança (RNF003, RNF004)

### 2.2 Excluso
- Testes de stress com > 200 usuários simultâneos (RNF001 define 50 usuários — stress test além do limite de projeto é escopo de fase 2)
- App mobile do fornecedor (plataforma mobile está fora do escopo do MVP — decisão TAP seção 3.2)
- Testes de integração com outros módulos SAP além do MM (fora do escopo conforme Q001 da ERF)

---

## 3. Critérios de Entrada

- [ ] ERF v1.0 aprovada pelo Rafael Requisito e assinada pelo solicitante
- [ ] Catálogo de casos de uso v1.0 aprovado
- [ ] Ambiente de testes configurado: servidor de testes disponível e banco de dados com dados sintéticos
- [ ] Integração SAP MM de testes configurada e funcionando (confirmado pela equipe TI SAP)
- [ ] Massa de dados de teste carregada: mínimo 20 pedidos de compra com entregas ativas simuladas

---

## 4. Critérios de Saída

- [ ] 100% dos CTs de categoria Must Have (CT001 a CT006, CT_NF001 a CT_NF004) executados
- [ ] Taxa de aprovação ≥ 95% nos CTs Must Have (máximo 1 falha aceitável na primeira execução)
- [ ] Nenhum defeito de severidade Crítica ou Alta em aberto ao final da execução
- [ ] Defeitos de severidade Média com plano de resolução aceito pela Ana Ferreira (responsável do projeto)
- [ ] Relatório de execução de testes assinado pela Ana Ferreira

---

## 5. Ambiente de Testes

| Item | Especificação |
|------|--------------|
| Servidor de testes | VM Ubuntu 22.04 LTS, 8 vCPUs, 32GB RAM, isolada de produção |
| Banco de dados | PostgreSQL 15.3, instância dedicada de testes com restore diário |
| Dados de teste | Massa sintética: 20 pedidos, 8 fornecedores Tier 1, histórico de 90 dias (gerado com script de seed) |
| Ferramentas de execução | Testes funcionais: execução manual com registro em planilha; Testes de carga: Apache JMeter 5.6.3; Segurança: OWASP ZAP 2.14 |
| Responsável pelo ambiente | Carlos Silva — Analista Sênior de TI |
| Janela de execução | Seg-Sex, 09h-17h; sem execução simultânea com pipeline de CI/CD |

---

## 6. Casos de Teste

### 6.1 Testes Funcionais

| ID | Título | Referência | Prioridade | Pré-condição | Passos | Resultado Esperado | Aprovação |
|----|--------|------------|------------|--------------|--------|--------------------|-----------|
| CT001 | Exibir mapa com entregas ativas — fluxo principal | UC001 / RF001, RF008 | Must Have | Usuário autenticado como "Analista Supply Chain"; 3 entregas ativas no sistema com atualização há < 15 min | 1. Acessar dashboard de monitoramento 2. Aguardar carregamento do mapa 3. Verificar pins de localização no mapa | Mapa exibido em ≤ 3s com exatamente 3 pins, um por entrega ativa; cada pin exibe: fornecedor, pedido e ETA | PASS / FAIL |
| CT002 | Filtrar entregas por fornecedor | UC001 / RF009 | Must Have | CT001 executado com PASS; 3 entregas de fornecedores distintos visíveis | 1. No dashboard, selecionar filtro "Fornecedor" 2. Escolher "Fornecedor A" 3. Verificar entregas exibidas | Mapa recarregado exibindo somente as entregas do Fornecedor A; contador de entregas atualizado | PASS / FAIL |
| CT003 | Exibir alerta de entrega com atraso previsto > 2h | UC002 / RF004, RF005 | Must Have | Entrega cadastrada com ETA que gera atraso simulado de 2h30min | 1. Sistema detecta atraso via processamento automático 2. Verificar envio de e-mail e Teams 3. Verificar conteúdo do alerta | Alerta enviado em até 5 min após detecção; conteúdo contém: fornecedor, pedido, produto, atraso estimado e responsável | PASS / FAIL |
| CT004 | Importar pedidos do SAP MM com status "aguardando entrega" | UC004 / RF006 | Must Have | Integração SAP MM de testes configurada; 5 pedidos com status "aguardando entrega" no SAP de testes | 1. Acionar importação manual (ou aguardar ciclo automático) 2. Verificar pedidos no SRF | 5 pedidos importados corretamente; status, fornecedor e produto coincidem com os dados do SAP | PASS / FAIL |
| CT005 | Fallback ao tentar exibir localização de entrega sem dados (> 15 min) | UC001 / RF001 | Must Have | Entrega cadastrada; atualização de localização pausada há 20 min | 1. Acessar dashboard 2. Localizar pin da entrega sem dados recentes | Pin da entrega exibe indicador "Sem atualização há 20 min"; nenhum erro de sistema; demais entregas exibidas normalmente | PASS / FAIL |
| CT006 | Consultar histórico de localização dos últimos 90 dias | UC003 / RF002 | Should Have | Entrega com histórico de localização com exatamente 90 dias de dados no banco | 1. Selecionar entrega no mapa 2. Acessar "Histórico" 3. Aplicar filtro de 90 dias | Sistema retorna registros de localização de 90 dias sem erro; formato: tabela com timestamp e coordenadas | PASS / FAIL |

### 6.2 Testes Não-Funcionais

| ID | Título | Referência | Prioridade | Pré-condição | Método de Verificação | Critério de Aprovação | Aprovação |
|----|--------|------------|------------|--------------|----------------------|-----------------------|-----------|
| CT_NF001 | Carga: 50 usuários simultâneos — dashboard | RNF001 | Must Have | Ambiente de testes com 20 entregas ativas; script JMeter configurado com 50 usuários virtuais | Executar script JMeter: 50 usuários, ramp-up de 60s, duração de 10 min | P95 do tempo de resposta do dashboard ≤ 3,0s; zero erros HTTP 5xx | PASS / FAIL |
| CT_NF002 | Criptografia: verificar TLS em trânsito | RNF003 | Must Have | OWASP ZAP configurado como proxy; acesso ao ambiente de testes | Capturar tráfego com ZAP; inspecionar certificado e protocolo | 100% do tráfego usa TLS 1.3 ou superior; certificado válido e emitido por CA confiável | PASS / FAIL |
| CT_NF003 | Criptografia: verificar AES-256 em repouso | RNF003 | Must Have | Acesso direto ao banco de dados de testes | Consultar tabelas de localização diretamente no banco de dados | Campos de localização (latitude, longitude) armazenados em formato criptografado (não legível em plain text) | PASS / FAIL |
| CT_NF004 | Conformidade LGPD: dados em servidores no Brasil | RNF004 | Must Have | Documentação de infraestrutura disponível | Verificar whois/geolocalização do IP do servidor + documentação do provedor cloud | 100% dos dados armazenados em data centers com localização confirmada no Brasil | PASS / FAIL |

---

## 7. Matriz de Rastreabilidade RF ↔ CT

| Requisito | Prioridade | Casos de Teste | Cobertura |
|-----------|------------|----------------|-----------|
| RF001 | Must Have | CT001, CT005 | ✅ Coberto |
| RF002 | Should Have | CT006 | ✅ Coberto |
| RF003 | Must Have | CT001 (verificação de ETA) | ✅ Coberto |
| RF004 | Must Have | CT003 | ✅ Coberto |
| RF005 | Must Have | CT003 | ✅ Coberto |
| RF006 | Must Have | CT004 | ✅ Coberto |
| RF007 | Must Have | CT004 | ✅ Coberto |
| RF008 | Must Have | CT001 | ✅ Coberto |
| RF009 | Must Have | CT002 | ✅ Coberto |
| RNF001 | Must Have | CT_NF001 | ✅ Coberto |
| RNF002 | Must Have | — | ⚠️ Pendente (monitoramento 30 dias pós-go-live) |
| RNF003 | Must Have | CT_NF002, CT_NF003 | ✅ Coberto |
| RNF004 | Must Have | CT_NF004 | ✅ Coberto |

---

## 8. Resumo de Cobertura

| Prioridade | Total de Requisitos | Com CT Associado | Cobertura |
|------------|--------------------|--------------------|-----------|
| Must Have (RF) | 8 | 8 | 100% ✅ |
| Must Have (RNF) | 4 | 3 | 75% ⚠️ (RNF002 avaliado pós-go-live) |
| Should Have | 1 | 1 | 100% ✅ |
| Could Have | 0 | 0 | — |
| **Total** | **13** | **12** | **92%** |
```

## Quality Criteria

- [ ] Objetivo do plano claro com critério de aceite global explícito
- [ ] Escopo incluso e excluso documentados com justificativa para exclusões
- [ ] Critérios de entrada com condições verificáveis (checklist)
- [ ] Critérios de saída com percentual de aprovação e severidade de defeitos
- [ ] Ambiente de testes especificado (servidor, banco, dados, ferramentas, responsável)
- [ ] Para cada UC Must Have: ao menos 2 CTs (fluxo principal + alternativo/exceção)
- [ ] Para cada RNF Must Have: ao menos 1 CT com método de verificação específico
- [ ] Todos os CTs têm: pré-condição, passos numerados, resultado esperado específico e PASS/FAIL
- [ ] Matriz de rastreabilidade RF ↔ CT presente e completa
- [ ] Resumo de cobertura com percentual por prioridade MoSCoW

## Veto Conditions

Rejeitar e refazer se qualquer uma das condições for verdadeira:
1. Algum RF Must Have sem ao menos 1 CT associado (cobertura obrigatória de 100%)
2. Algum CT sem resultado esperado específico (resultado "OK" ou "funciona" não é aceitável)
3. Matriz de rastreabilidade ausente ou incompleta (sem referência cruzada RF ↔ CT)
4. Critérios de entrada ou saída ausentes (plano sem condições de início e fim não é plano)
