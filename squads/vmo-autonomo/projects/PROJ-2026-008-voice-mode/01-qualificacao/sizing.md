# Sizing Inicial de Escopo

**Projeto:** PROJ-2026-008-voice-mode
**Data:** 17/08/2026
**Analista:** Rafael Requisito
**Fase:** Pré-qualificação (para subsidiar critério 7 — Esforço)

---

## Escopo Preliminar Identificado

Com base na demanda validada, o escopo consiste em **elaborar um estudo de viabilidade** comparando três soluções multiagentes com Voice Mode. Não é um projeto de implementação de sistema — é um projeto de análise e documentação técnica.

### Funcionalidades/Entregas Identificadas
1. **Levantamento técnico** das 3 soluções (Fireflies, Microsoft Teams/Copilot Studio, Azure Telefonia)
2. **Análise comparativa** nos 7 critérios definidos (custo, prazo, capacidades técnicas, governança, risco, segurança, conformidade LGPD)
3. **Matriz de prós e contras** para cada solução
4. **Avaliação de custos** — estimativa de TCO para cada caminho
5. **Análise de conformidade** — LGPD, políticas internas, governança corporativa
6. **Documento de recomendação** — parecer com justificativa técnica e de negócio
7. **Apresentação executiva** — resumo para tomada de decisão

---

## Estimativa de Esforço por Fase

| Fase | Atividades principais | Esforço estimado | Confiança |
|------|----------------------|------------------|-----------|
| Levantamento de requisitos | Coleta de informações técnicas das 3 soluções; entrevistas com áreas (ERP, Call Center, ITeam); análise de documentação Microsoft/Azure | 16-24h | MÉDIA |
| Pesquisa e análise técnica | Pesquisa de funcionalidades de cada plataforma; análise de roadmap Microsoft para Voice Mode; levantamento de custos de licenciamento e infra | 24-32h | BAIXA |
| Elaboração do estudo | Redação do documento comparativo; construção da matriz de decisão; análise de riscos e conformidade | 16-24h | MÉDIA |
| Revisão e validação | Revisão com stakeholders; ajustes; aprovação | 8-16h | MÉDIA |
| **TOTAL** | | **64-96h** | **MÉDIA** |

---

## Classificação de Esforço

- [x] **< 80h → Melhoria Corretiva/Evolutiva simples** (cenário otimista: 64h)
- [x] **80–160h → Melhoria Evolutiva complexa** (cenário pessimista: 96h)
- [ ] > 160h → Projeto formal

**Classificação predominante:** Faixa de transição entre Melhoria Evolutiva simples e complexa. O esforço concentra-se em pesquisa e análise, não em desenvolvimento técnico. Entretanto, a natureza estratégica da decisão (impacto em toda a organização) pode justificar gestão formal.

---

## Fatores de Risco que Afetam o Esforço

| Fator | Impacto no Esforço | Direção |
|---|---|---|
| Disponibilidade de informações de custo das plataformas | Se custos não estiverem acessíveis, pesquisa adicional necessária | ↑ Aumenta |
| Roadmap de Voice Mode da Microsoft não publicado oficialmente | Análise pode ser inconclusiva quanto a prazo | ↑ Aumenta |
| Prazo apertado (entrega em 1 dia) | Reduz escopo de pesquisa, mas aumenta risco de qualidade | ↑↓ Variável |
| Solicitante bem informado sobre as 3 soluções | Reduz tempo de levantamento | ↓ Diminui |
| Escopo restrito a análise (sem implementação) | Elimina fase de desenvolvimento | ↓ Diminui |

---

## Lacunas de Escopo (para ERF futura)

1. **Requisitos de integração:** Quais sistemas internos precisam se integrar com a solução de voz?
2. **Volume de uso esperado:** Quantos usuários simultâneos? Quantas chamadas/interações por dia?
3. **Requisitos de SLA:** Disponibilidade mínima, tempo de resposta do voice agent?
4. **Requisitos de idioma:** Apenas português ou multilíngue?
5. **Requisitos de gravação/auditoria:** As interações de voz precisam ser gravadas e armazenadas?

---

## Perguntas para Confirmar Escopo

1. O estudo deve incluir estimativa de custos de implementação de cada solução ou apenas análise qualitativa?
2. Existe alguma prova de conceito (POC) já realizada com alguma das soluções que possa ser referenciada?
3. Qual é o nível de detalhe esperado na análise de segurança e LGPD — checklist básico ou parecer jurídico completo?
4. A apresentação executiva deve ser em formato específico (PPT, documento, dashboard)?
5. Há restrição de orçamento que descarte automaticamente alguma das soluções?
