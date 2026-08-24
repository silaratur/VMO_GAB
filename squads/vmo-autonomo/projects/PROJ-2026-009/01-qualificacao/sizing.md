# Sizing Inicial de Escopo

**Projeto:** PROJ-2026-009
**Demanda:** DEM-2026-009
**Data:** 2026-08-24
**Analista:** Rafael Requisito — Engenheiro de Requisitos
**Fase:** Pré-qualificação (subsidia critério 7 do Felipe Filtro)

---

## Escopo Preliminar Identificado

| # | Componente | Tipo | Clareza do Escopo |
|---|-----------|------|-------------------|
| 1 | Integração SAP → GRLOG para centros de custo | Integração | Claro — entidades e fluxo declarados [01:40-02:08] |
| 2 | Integração SAP → GRLOG para centros de lucro | Integração | Claro — mesmo fluxo da linha 1, entidade diferente |
| 3 | Integração SAP → GRLOG para clientes | Integração | Claro — mesmo mecanismo, terceira entidade |
| 4 | Mapeamento de campos SAP → GRLOG | Configuração | Incerto — regras de correspondência não detalhadas (Lacuna L7) |
| 5 | Rotina de sincronização diária automatizada | Desenvolvimento | Incerto — método de integração não definido: API, RFC, flat file ou middleware (Lacuna L4) |
| 6 | Tratamento de erros e notificações | Desenvolvimento | A confirmar — nenhum requisito de erro/rollback foi discutido (Lacuna L8) |
| 7 | Monitoramento e logs da integração | Configuração | A confirmar — não mencionado, mas implícito para operação |

---

## Estimativa de Esforço por Fase

| Fase | Atividades | Estimativa | Confiança | Premissas |
|------|-----------|------------|-----------|-----------|
| Levantamento de requisitos | Elicitação com Jairo e equipe GRLOG; mapeamento de campos SAP→GRLOG; definição do método de integração com DTI; documentação de regras de negócio | 40–60h | MÉDIA | DTI participa ativamente; acesso aos ambientes SAP e GRLOG disponível para análise; 2-3 workshops necessários |
| Desenvolvimento/Configuração | Desenvolvimento da rotina de integração (extração SAP, transformação, carga GRLOG); configuração de agendamento diário; tratamento de erros e retry; logs e notificações | 80–140h | BAIXA | Depende fortemente do método de integração: API REST com documentação boa = ~80h; RFC SAP com customização = ~120h; middleware (ex: PI/PO) = ~140h. Premissa: 3 entidades com estrutura similar reduzem retrabalho por reuso |
| Testes e homologação | Testes unitários da integração; testes integrados com dados reais (ambiente de homologação); UAT com equipe de Gestão da Receita; validação de dados no BI GRLOG | 40–60h | MÉDIA | Ambientes de homologação SAP e GRLOG disponíveis; massa de teste representativa; 1 ciclo de UAT com correções |
| Go-live e suporte inicial | Deploy em produção; monitoramento da primeira semana de execução diária; ajustes finos; documentação operacional; treinamento da equipe de suporte | 20–30h | ALTA | Deploy padrão com rollback planejado; equipe de suporte existente absorve operação |
| **TOTAL** | | **180–290h** | **BAIXA** | Faixa ampla reflete a incerteza sobre método de integração e mapeamento de campos |

---

## Classificação de Esforço

- [ ] < 80h — Melhoria Corretiva/Evolutiva simples
- [ ] 80–160h — Melhoria Evolutiva complexa
- [X] > 160h — **Projeto formal** (exige pipeline VMO completo)

**Justificativa:** Mesmo no cenário otimista (180h), o esforço ultrapassa o limiar de 160h. A integração entre dois sistemas corporativos (SAP e GRLOG) com 3 entidades, rotina automatizada diária, tratamento de erros e impacto em +200 usuários configura complexidade de projeto, não de melhoria evolutiva.

---

## Fatores de Risco que Afetam o Esforço

| Fator | Impacto se confirmado | Probabilidade |
|-------|----------------------|---------------|
| Método de integração via RFC SAP customizado (sem API REST disponível) | +40–60h sobre cenário base | MÉDIA — SAP geralmente oferece RFC para dados cadastrais, mas depende da versão e módulo |
| Campos SAP com transformação necessária (não cópia direta) | +20–30h para regras de mapeamento e validação | MÉDIA — solicitante mencionou "mesmos campos" [02:25-02:44], mas pode haver divergências |
| Necessidade de middleware corporativo (SAP PI/PO ou similar) | +30–50h de configuração e testes adicionais | BAIXA — depende da arquitetura de integração da empresa |
| Múltiplos ambientes SAP (produção, homologação, desenvolvimento) com configurações diferentes | +15–25h de configuração por ambiente | MÉDIA — padrão em empresas com SAP |
| Requisitos adicionais de segurança/compliance para dados de clientes | +20–40h para criptografia, auditoria, LGPD | BAIXA — solicitante indicou "nenhum requisito legal/regulatório" [08:29], mas dados de clientes podem acionar LGPD |

---

## Lacunas de Escopo (para ERF futura)

| # | Lacuna | Por que afeta o esforço |
|---|--------|------------------------|
| 1 | Método de integração (API, RFC, flat file, middleware) | Pode variar de 80h (API documentada) a 140h (RFC customizado). É o maior fator de incerteza da estimativa. |
| 2 | Mapeamento de campos entre SAP e GRLOG | Se houver transformação além de cópia direta, adiciona 20-30h de regras de negócio e testes. |
| 3 | Volumetria diária de registros novos | Alto volume (>1000/dia) pode exigir otimização de performance; baixo volume (<50/dia) simplifica. |
| 4 | Existência de APIs ou serviços já disponíveis no SAP/GRLOG | Serviços existentes reduziriam significativamente o desenvolvimento (até -40h). |
| 5 | Tratamento de cenários de falha e requisitos de SLA | Se exigido SLA de 99.9% com retry automático e alertas, adiciona 20-30h sobre o básico. |

---

## Nota para Felipe Filtro

**Classificação: Projeto formal (>160h).** O esforço total estimado é de **180–290h** com confiança **BAIXA** — a faixa é ampla porque o método de integração SAP→GRLOG não foi definido (API vs RFC vs middleware). Mesmo no cenário mais otimista (180h), ultrapassa o limiar de melhoria evolutiva. O escopo envolve integração entre dois sistemas corporativos com 3 entidades, rotina automatizada diária e impacto em +200 usuários, o que confirma a classificação como projeto. Para o critério 7 (Esforço Estimado), recomendo pontuar como **Projeto** com nota indicativa de complexidade média-alta.

---

*Sizing executado por Rafael Requisito — Engenheiro de Requisitos | VMO Autônomo Squad | 2026-08-24*
