# Anti-Patterns — VMO Autônomo
# Erros Comuns em Gestão de Projetos PMO/VMO

---

## Anti-Patterns de Captação de Demanda

### Nunca Fazer
1. **Assumir que a demanda está completa sem verificar lacunas**: O solicitante raramente fornece todas as informações necessárias na primeira interação. Sempre verificar: quem, o quê, por quê, quando, quanto.
2. **Ignorar o contexto organizacional**: Uma demanda nunca existe no vácuo. Ignorar o contexto (histórico de projetos similares, conflitos de recursos, política interna) leva a projetos que fracassam por razões não técnicas.
3. **Registrar apenas a solução pedida, não o problema real**: Solicitantes frequentemente chegam com a solução definida ("quero um sistema X"), mas o problema real pode ter soluções mais simples ou eficazes.
4. **Aceitar prazos sem questionar**: "Quero isso em 2 semanas" raramente é uma restrição absoluta. Sempre investigar a origem do prazo antes de aceitá-lo como fato.

### Sempre Fazer
1. **Documentar a fonte e data de cada informação coletada**: Essencial para rastreabilidade e resolução de conflitos futuros.
2. **Confirmar com o solicitante o resumo da demanda antes de avançar**: O checkpoint evita retrabalho por mal-entendido.
3. **Registrar o que NÃO foi possível obter**: Gaps documentados são tão valiosos quanto informações confirmadas.

---

## Anti-Patterns de Qualificação

### Nunca Fazer
1. **Aprovar projeto por pressão política sem embasamento técnico**: Um dos maiores geradores de projetos fracassados. O VMO deve manter critérios objetivos independentemente de hierarquia.
2. **Qualificar baseado apenas na descrição do solicitante**: O solicitante tem viés natural. Sempre cruzar com alinhamento estratégico documentado da organização.
3. **Ignorar a capacidade real de recursos**: Aprovar projetos sem verificar disponibilidade de equipe e orçamento resulta em portfólio superlotado e projetos que avançam à metade.
4. **Não documentar o raciocínio da decisão de qualificação**: Decisões sem justificativa documentada criam disputas internas e dificultam aprendizado organizacional.

### Sempre Fazer
1. **Quantificar o benefício esperado, mesmo que estimado**: "Benefício estimado de R$ 200k em 12 meses, com confiança média" é sempre melhor que "benefício alto".
2. **Consultar documentos estratégicos da organização antes de qualificar**: OKRs, mapa estratégico, portfólio aprovado.
3. **Registrar demandas REPROVADAS com justificativa**: Forma um banco de conhecimento que evita submissões repetidas da mesma ideia.

---

## Anti-Patterns de Documentação

### Nunca Fazer
1. **Criar TAP sem objetivo SMART**: Objetivos vagos como "melhorar a experiência do cliente" não permitem medir sucesso. Sempre específico: "Reduzir o tempo de atendimento de 5 para 2 dias úteis até 31/12/2026".
2. **Deixar seções obrigatórias "a definir"**: Um TAP com sponsor "a definir" não é um TAP. Não avançar sem preencher os campos críticos.
3. **Copiar e colar documentação de projetos anteriores sem adaptar**: Prática extremamente comum e perigosa. Cada projeto tem suas peculiaridades; reutilizar sem revisar introduz erros e contradições.
4. **Criar documentos isolados sem consistência entre si**: O TAP diz "R$ 500k de orçamento", o PM Canvas diz "R$ 300k". Inconsistências destroem a credibilidade da documentação.
5. **Documentar requisitos ambíguos**: "O sistema deve ser rápido" não é um requisito. "O sistema deve responder em até 2 segundos para 95% das requisições" é.

### Sempre Fazer
1. **Verificar consistência cross-documento antes de finalizar**: Prazo, custo e escopo devem ser idênticos em todos os documentos da iniciação.
2. **Incluir critérios de sucesso mensuráveis no TAP**: O que precisa ser verdade no final do projeto para que ele seja considerado bem-sucedido?
3. **Versionar todos os documentos**: Sempre registrar versão, data e autor. Mudanças significativas geram nova versão, não sobrescrevem.

---

## Anti-Patterns de Cronograma

### Nunca Fazer
1. **Criar cronograma sem WBS**: Estimar duração de tarefas sem antes decompor o escopo em pacotes de trabalho resulta em omissões e subestimativas sistemáticas.
2. **Ignorar dependências entre atividades**: O caminho crítico de um projeto é definido pelas dependências. Ignorá-las faz o cronograma ser otimista por definição.
3. **Não incluir buffer de contingência**: Projetos sem reservas de tempo falham na primeira mudança. Padrão: 10-20% do prazo total como reserva de gestão.
4. **Estimar duração sem consultar quem vai executar**: Quem cria o cronograma raramente é quem executa. Estimar sem envolver o time produz números irrealistas.

### Sempre Fazer
1. **Definir critério de conclusão para cada pacote de trabalho**: O que significa "feito" para cada tarefa deve ser claro e verificável.
2. **Revisar o cronograma com o sponsor antes de basear**: O baseline é um compromisso. Ambos os lados precisam concordar.

---

## Anti-Patterns de Gestão de Riscos

### Nunca Fazer
1. **Identificar riscos apenas no início e nunca mais revisar**: Riscos mudam. O registro de riscos deve ser revisado a cada ciclo de status report.
2. **Tratar todos os riscos com a mesma urgência**: Um risco com probabilidade 10% e impacto baixo não merece o mesmo esforço que um risco com probabilidade 80% e impacto crítico.
3. **Confundir risco com problema**: Risco é algo que PODE ocorrer. Problema é algo que JÁ ocorreu. Gerenciar problemas como riscos atrasa a resposta necessária.
4. **Criar plano de riscos sem responsável e prazo**: Um plano sem owner não é um plano. É uma lista de intenções.

### Sempre Fazer
1. **Definir trigger (gatilho) para cada risco crítico**: Qual evento ou sinal indica que o risco está se materializando?
2. **Calcular reserva de contingência baseada no valor esperado dos riscos**: Soma(probabilidade × impacto financeiro) de todos os riscos identificados.

---

## Anti-Patterns de Monitoramento e Reports

### Nunca Fazer
1. **Reportar apenas o que está bem**: Status reports que omitem problemas são inúteis para decisão. O relatório existe para habilitar ação corretiva, não para tranquilizar stakeholders.
2. **Usar percentual de conclusão sem método objetivo**: "70% concluído" diz pela percepção de quem executa. EVM (Earned Value) diz pela realidade dos entregáveis completados.
3. **Criar reports muito longos sem sumário executivo**: Um relatório de 20 páginas que o sponsor não lê não serve para nada. Sempre incluir sumário de 1 página no topo.
4. **Não registrar as decisões tomadas nos reports**: O histórico de decisões é parte do acervo do projeto e essencial para auditoria e aprendizado.

### Sempre Fazer
1. **Incluir semáforo visual no topo de todo status report**: Verde/Amarelo/Vermelho é a primeira coisa que o sponsor procura.
2. **Listar cada issue aberta com responsável, prazo e próximo passo**: Issues sem dono e sem prazo nunca são resolvidas.
3. **Comparar sempre com o baseline (não com o último report)**: A comparação com o plano original revela a tendência real do projeto.
