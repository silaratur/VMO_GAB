# Sizing Inicial de Escopo
**Projeto**: PROJ-2026-007
**Demanda**: DEM-2026-007 / Chamado 6800446
**Agente**: Rafael Requisito
**Data**: 2026-05-31
**Versão**: 1.0

---

## 1. Escopo Mapeado para Sizing

### O que está dentro do escopo (conhecido)

| # | Componente | Descrição | Fonte |
|---|-----------|-----------|-------|
| 1 | Integração SGMM03 → SAP (campos InterCompany) | Transmissão dos campos "Empresa a Contrato" inseridos na abertura de OM para o SAP | Chamado 6800446 + Mapeamento_SGMM03 |
| 2 | Campo CenPlan (Cenário) | Remoção de restrição ativa (vermelho) e habilitação para receber valor MAM1/MWV1 | Mapeamento_SGMM03 |
| 3 | Campo Empresa | Integração para criação e alteração de OM | Chamado 6800446 |
| 4 | Campo Contrato | Integração para criação e alteração de OM | Chamado 6800446 |
| 5 | Alteração de OM (além de criação) | Permitir edição dos campos já integrados após criação da OM | Chamado 6800446 |

### Escopo incerto — condicional

| # | Componente | Condição para entrar no escopo | Impacto no esforço |
|---|-----------|-------------------------------|-------------------|
| A | Campos adicionais: Tipo de Ordem, Prioridade, Locacional, Equipamento, Conjunto, Modelo, Ordem | Se confirmado escopo amplo (lista completa do mapeamento) | +40-80h adicionais |
| B | Configuração de autorização SAP para edição dos campos | Depende do nível de restrição ativa do CenPlan — pode ser config. simples ou desenvolvimento | +8-24h |

### Fora do escopo (presumido)

- Desenvolvimento de novos campos no SGMM03 (não mencionado)
- Modificação no processo de negócio InterCompany além dos campos técnicos
- Centro de Planejamento (já entregue — precedente existente)

---

## 2. Estimativa de Esforço por Fase

**Base da estimativa**: escopo mínimo confirmado (3 campos: Empresa, Contrato, CenPlan) + precedente da integração de Centro de Planejamento já entregue (reutilização de padrão esperada).

| Fase | Atividades Principais | Esforço Mín. (h) | Esforço Máx. (h) |
|------|----------------------|----------------:|----------------:|
| F1 — Requisitos Detalhados | Workshops de elicitação, mapeamento campo a campo, levantamento da restrição CenPlan | 8 | 16 |
| F2 — Design Técnico | Especificação da interface SGMM03↔SAP, mapeamento de dados, plano de configuração SAP | 16 | 24 |
| F3 — Desenvolvimento / Configuração | Desenvolvimento no SGMM03 + configuração/desenvolvimento SAP para remoção de restrição e recepção dos campos | 48 | 96 |
| F4 — Testes | Teste de integração end-to-end, UAT com equipes VIX e Holding DTI | 24 | 40 |
| F5 — Deploy / GMUD | Transport de request, janela de mudança, go-live assistido, suporte pós-implantação (5 dias) | 8 | 16 |
| **TOTAL — Escopo Mínimo** | | **104** | **192** |

**Escopo ampliado** (se campos adicionais forem confirmados — lacuna #4):

| Cenário | Esforço Total Estimado |
|---------|----------------------|
| Escopo mínimo (3 campos) | 104–192h |
| Escopo ampliado (8+ campos) | 144–272h |

---

## 3. Classificação de Esforço

| Classificação | Faixa | Enquadramento deste sizing |
|--------------|-------|--------------------------|
| PEQUENO | < 80h | — |
| MÉDIO | 80–160h | **Escopo mínimo (ponto médio: 148h)** |
| GRANDE | > 160h | **Escopo ampliado** / limite superior do mínimo |

**Classificação primária**: **MÉDIO** (escopo mínimo, ponto médio 148h)
**Classificação de risco**: **GRANDE** (se escopo for ampliado ou restrição CenPlan for mais complexa que config.)

---

## 4. Confiança da Estimativa

**Nível de confiança**: **BAIXO-MÉDIO (±40%)**

**Fatores que reduzem a confiança**:

1. **Escopo de campos não confirmado** (Lacuna #4 da demanda): O chamado cita 3 campos; o documento técnico lista 8+. A diferença pode duplicar o esforço de F3.
2. **Natureza da restrição CenPlan desconhecida**: A restrição em vermelho no SAP pode ser uma configuração de autorização (< 4h para remover) ou uma customização de negócio protegida (pode exigir análise funcional completa). Impossível estimar sem acesso ao ambiente SAP.
3. **Ausência de requisitos detalhados**: Este sizing é pré-elicitação. As estimativas de F3 podem variar significativamente após o detalhamento completo dos requisitos.
4. **Budget e prazo do cliente desconhecidos** (Lacunas #2 e #3): Sem referência de custo-teto, não é possível validar se o escopo está dentro da capacidade do cliente.

**O que aumenta a confiança**:
- Precedente da integração Centro de Planejamento já entregue (padrão de integração SGMM03↔SAP existe)
- Escopo técnico de campos relativamente delimitado no chamado (3 campos confirmados)
- Equipe técnica identificada (Holding DTI + consultoria externa a contratar)

---

## 5. Lacunas de Escopo que Impactam o Sizing

| # | Lacuna | Impacto no Esforço | Ação Necessária |
|---|--------|-------------------|----------------|
| L1 | Escopo exato dos campos (3 vs. 8+) | Alto — pode dobrar F3 | Confirmar com solicitante (Lacuna #4 demanda) |
| L2 | Natureza da restrição CenPlan no SAP | Alto — F2 e F3 dependem disso | Análise técnica inicial no SAP (< 4h investigação) |
| L3 | Padrão de integração do precedente (CenPlan já entregue) | Médio — pode reduzir F2 e F3 em 20-30% se reutilizável | Levantar documentação da integração anterior |

---

## 6. Nota para Felipe Filtro — Critério 7 (Esforço e Complexidade Técnica)

**Estimativa pré-requisitos (sizing inicial)**:

- **Escopo mínimo**: 104–192h (classificação **MÉDIO**, ponto médio 148h)
- **Escopo ampliado**: 144–272h (classificação **GRANDE**)
- **Confiança**: Baixo-Médio (±40%) — estimativa pré-elicitação
- **Recomendação para critério 7**: Usar faixa 104–192h como referência. Com escopo mínimo, o projeto se enquadra como **MÉDIO** em esforço. Com escopo ampliado, **GRANDE**.
- **Flag para avaliação**: A incerteza de escopo (L1) é o principal fator de risco. O critério 7 deve refletir a faixa, não um valor pontual. Se o critério 7 for determinante para a classificação PROJETO vs. MELHORIA, recomendo que Felipe registre o intervalo e marque como condicionante do escopo confirmado.
