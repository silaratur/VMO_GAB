# ESPECIFICAÇÃO DE REQUISITOS FUNCIONAIS (ERF)

**Projeto:** Caminhos Estratégicos do ERP GAB — PROJ-2026-003
**Tipo:** Assessment de Seleção de Plataforma ERP
**Versão:** 1.0
**Data:** 2026-05-14
**Autor:** Rafael Requisito — VMO Consultoria
**Status:** Aguardando Aprovação

---

> **Nota de Escopo:** Este documento especifica os requisitos do **processo de assessment e gestão do projeto**, não de um sistema de TI a ser desenvolvido. Os "entregáveis" são produtos de consultoria (workshops, relatórios, score model, pacote RFP). Os "usuários" são os papéis que executam e consomem o processo (equipe VMO, equipe KPMG, sponsors do GAB).

---

## 1. Requisitos Funcionais

### 1.1 Planejamento e Governança

| ID | Descrição | MoSCoW | Critério de Aceitação | Origem |
|----|-----------|--------|-----------------------|--------|
| RF-PG-01 | O processo deve realizar um Kick Off Executivo formal com presença de ao menos 1 sponsor de cada uma das 3 entidades (Holding, VixPar, VAB) antes do início dos workshops de elicitação. | Must Have | Ata de Kick Off assinada por ao menos 1 representante de cada entidade; registro de presença arquivado no SharePoint; data de realização ≤ D+3 do início da Fase 1 (≤ 04/04/2026). | TAP — Escopo Item 4 |
| RF-PG-02 | O processo deve manter um plano de projeto com cronograma detalhado (WBS de no mínimo 2 níveis) cobrindo as 5 semanas da Fase 1, identificando marcos, responsáveis e dependências críticas entre atividades. | Must Have | Plano aprovado por GP interno (Marcelo Silveira) e pelo Gerente Sênior KPMG (Wallacy Lima) antes do Kick Off; cronograma publicado no SharePoint; pelo menos 1 atualização semanal registrada em cada Status Report. | TAP — Governança |
| RF-PG-03 | O processo deve definir e documentar a matriz RACI para todas as atividades de assessment, especificando os papéis da equipe VMO, KPMG e do cliente (GAB) em cada entrega. | Must Have | Documento de RACI revisado e aceito por Rodrigo Figaro (KPMG) e Marcelo Silveira (GAB) antes do Kick Off; sem atividade sem Responsável (R) atribuído. | TAP — Governança |
| RF-PG-04 | O processo deve identificar e registrar os riscos do projeto em uma matriz de riscos com ao menos 5 riscos identificados, cada um com probabilidade (Alta/Média/Baixa), impacto (Alto/Médio/Baixo), score resultante e plano de resposta documentado. | Must Have | Matriz de riscos publicada no SharePoint até D+5 do início da fase; matriz revisada em cada reunião de Comitê Executivo semanal; ao menos 1 atualização por semana com novos riscos ou atualização de status. | TAP — Governança |
| RF-PG-05 | O processo deve monitorar e controlar desvios de prazo, escopo e custo durante as 5 semanas, registrando qualquer desvio superior a 10% da baseline no Status Report da semana em que ocorrer, com plano de ação corretiva. | Must Have | Nenhum desvio de prazo ou escopo permanece sem registro ou plano de ação por mais de 5 dias úteis; evidência nos Status Reports de no mínimo 4 semanas com análise de variação. | TAP — Critérios de Sucesso |
| RF-PG-06 | O processo deve realizar o encerramento formal da Fase 1 com aprovação documentada dos 3 sponsors, incluindo aceite das entregas, lições aprendidas registradas e avaliação NPS dos sponsors coletada. | Must Have | Documento de encerramento com assinaturas dos 3 sponsors (Décio Chieppe, Paula Barcelos, Patrícia Poubel) arquivado até 08/05/2026; NPS coletado de cada sponsor com pontuação numérica registrada. | TAP — Critérios de Sucesso Item 6 |

---

### 1.2 Workshops de Entendimento de Processos

| ID | Descrição | MoSCoW | Critério de Aceitação | Origem |
|----|-----------|--------|-----------------------|--------|
| RF-WK-01 | O processo deve conduzir workshops de entendimento de processos cobrindo as 7 áreas funcionais definidas (Manutenção/Frotas, Suprimentos, Finanças, Fiscal, DP/SESMT, RH, Tecnologia) em cada uma das 3 entidades (Holding, VixPar, VAB), totalizando mínimo de 21 sessões de workshop (7 áreas × 3 entidades). | Must Have | Registro de realização (ata ou gravação) para cada uma das 21 combinações área-entidade; 100% de cobertura verificável no encerramento da Fase 1; ao menos 1 representante da área participante com poder de validar o processo atual presente em cada sessão. | TAP — Escopo Item 1; Critério de Sucesso Item 2 |
| RF-WK-02 | Cada workshop deve produzir um artefato de saída documentando o processo AS-IS da área na respectiva entidade, contendo: fluxo do processo atual, sistemas utilizados, volume de transações (quando disponível), principais dores/gaps e requisitos de negócio preliminares levantados. | Must Have | Artefato de saída produzido e validado pelo representante da área em até 2 dias úteis após a sessão; artefato publicado no SharePoint; sem workshop com artefato em branco. | TAP — Escopo Item 1 |
| RF-WK-03 | O processo deve preparar e enviar convocatória formal para cada workshop com antecedência mínima de 3 dias úteis, incluindo: pauta, objetivos da sessão, lista de participantes esperados, materiais de leitura prévia (se houver) e link de conferência ou endereço físico. | Must Have | 100% das convocatórias enviadas com ≥ 3 dias úteis de antecedência; sem workshop realizado sem convocatória registrada; taxa de comparecimento do representante-chave da área ≥ 80% das sessões. | TAP — Governança |
| RF-WK-04 | O processo deve consolidar os outputs de todos os workshops em um documento de mapeamento de processos consolidado, destacando similaridades e divergências entre as 3 entidades por área funcional, para uso como insumo direto do Score Model. | Must Have | Documento de mapeamento consolidado entregue até o final da Semana 3 (≤ 24/04/2026); cada área funcional representada com análise comparativa entre entidades; documento aprovado pelo Gerente Sênior KPMG antes da etapa de avaliação de plataformas. | TAP — Escopo Item 1 |
| RF-WK-05 | O processo deve garantir a participação da equipe KPMG (ao menos o Gerente Sênior Wallacy Lima ou analista designado) como co-facilitadores nos workshops das áreas de maior complexidade: Finanças, Fiscal e Tecnologia. | Should Have | Registro de presença da equipe KPMG nos workshops de Finanças, Fiscal e Tecnologia de ao menos 2 das 3 entidades; evidência de facilitação conjunta na ata de cada sessão. | TAP — Governança; Parceiro KPMG |
| RF-WK-06 | O processo deve identificar, durante os workshops, os processos que são candidatos a diferenciadores competitivos do GAB (processos únicos ou críticos para o negócio), documentando-os separadamente como critérios de peso elevado na avaliação das plataformas. | Should Have | Ao menos 3 processos diferenciadores identificados e documentados com justificativa de negócio; esses processos mapeados explicitamente para critérios do Score Model. | TAP — Escopo Item 2 |

---

### 1.3 Avaliação de Plataformas (Score Model)

| ID | Descrição | MoSCoW | Critério de Aceitação | Origem |
|----|-----------|--------|-----------------------|--------|
| RF-SM-01 | O processo deve avaliar cada uma das 3 plataformas candidatas (SAP S/4HANA Rise, Oracle ERP Cloud, TOTVS Protheus) em todos os 6 pilares do Score Model com ponderação percentual definida e documentada antes do início da avaliação, totalizando 100% da ponderação entre os pilares. | Must Have | Score Model com 6 pilares e pesos percentuais publicado e aprovado por Rodrigo Figaro (KPMG) e Décio Chieppe (GAB) antes do início das avaliações; soma dos pesos = 100%; nenhuma plataforma com pilar não avaliado. | TAP — Escopo Item 2; Critério de Sucesso Item 1 |
| RF-SM-02 | O Score Model deve ser construído de forma que ao menos 70% dos critérios de avaliação sejam derivados de fontes objetivas mensuráveis: demonstrações gravadas ou ao vivo, respostas a RFI, benchmarks de mercado publicados ou estudos de caso verificáveis. | Must Have | Planilha do Score Model com coluna de fonte por critério preenchida; ao calcular a proporção de critérios classificados como "objetivo" vs. "subjetivo", o resultado deve ser ≥ 70% objetivos; essa proporção documentada no relatório final. | TAP — Critério de Sucesso Item 4 |
| RF-SM-03 | O processo deve conduzir sessões de demonstração (demos) de cada plataforma candidata com os fornecedores, com roteiro padronizado de cenários de negócio derivados dos workshops, permitindo avaliação comparativa padronizada. | Must Have | Sessão de demo realizada para cada uma das 3 plataformas com roteiro idêntico de cenários; participação de ao menos 1 representante de cada área funcional das 3 entidades no conjunto das demos; atas e gravações arquivadas. | TAP — Critério de Sucesso Item 4 |
| RF-SM-04 | O processo deve enviar RFI (Request for Information) padronizado para os 3 fornecedores das plataformas candidatas, com conjunto de perguntas igual para todos, e registrar as respostas recebidas como insumo formal para o Score Model. | Must Have | RFI enviado para os 3 fornecedores com ao menos 20 dias de antecedência do prazo de entrega da recomendação; respostas recebidas e arquivadas no SharePoint; critérios do Score Model derivados de respostas ao RFI identificados explicitamente na planilha. | TAP — Critério de Sucesso Item 4 |
| RF-SM-05 | O processo deve calcular o Score final de cada plataforma candidata aplicando os pesos dos pilares sobre as pontuações obtidas em cada critério, gerando uma pontuação ponderada total para cada plataforma, com ranking final documentado. | Must Have | Planilha de Score Model com fórmulas auditáveis (sem valores hardcoded ocultos); Score calculado por pilar e total para cada plataforma; ranking final com delta de pontuação entre as plataformas apresentado no relatório. | TAP — Critério de Sucesso Item 1 |
| RF-SM-06 | O processo deve elaborar uma análise de sensibilidade do Score Model testando ao menos 2 cenários alternativos de ponderação de pilares (além do cenário base), demonstrando a robustez ou fragilidade da recomendação. | Should Have | Seção de análise de sensibilidade no relatório final com 2 cenários alternativos; para cada cenário alternativo, o ranking resultante apresentado; conclusão indicando se a recomendação se mantém estável ou depende fortemente dos pesos. | TAP — Critério de Sucesso Item 1; Qualidade da Recomendação |
| RF-SM-07 | O processo deve incluir na avaliação, para cada plataforma candidata, a análise de fit funcional com as 7 áreas cobertas nos workshops, identificando lacunas (gaps) funcionais e as formas de endereçamento previstas (configuração padrão, customização, parceiro). | Must Have | Matriz de fit funcional 7 áreas × 3 plataformas preenchida no relatório; cada célula com classificação (Nativo / Configurável / Gap com solução / Gap sem solução) e fonte da classificação registrada. | TAP — Escopo Item 2 |
| RF-SM-08 | O processo deve avaliar cada plataforma candidata sob o pilar financeiro/TCO (Total Cost of Ownership), incluindo estimativa de custos de licença/subscrição, implementação, sustentação e migração para os primeiros 5 anos, com fontes documentadas para cada estimativa. | Should Have | Tabela de TCO por plataforma com 4 categorias de custo e horizonte de 5 anos; fontes documentadas (cotação de fornecedor, benchmark KPMG, estimativa de mercado) para cada linha de custo; apresentado no relatório final e nos insumos de RFP. | TAP — Escopo Item 2 |

---

### 1.4 Entregáveis e Documentação

| ID | Descrição | MoSCoW | Critério de Aceitação | Origem |
|----|-----------|--------|-----------------------|--------|
| RF-ED-01 | O processo deve produzir e entregar o Relatório de Recomendação de Plataforma ERP até 08/05/2026, contendo: sumário executivo, metodologia do assessment, resultados por pilar do Score Model, análise comparativa das 3 plataformas, recomendação fundamentada e próximos passos. | Must Have | Relatório entregue até 08/05/2026 em formato PDF e editável (.docx ou .pptx); Score Model documentado por pilar com fontes; recomendação explícita de uma das 3 plataformas com justificativa mínima de 3 argumentos objetivos; aprovação dos 3 sponsors registrada. | TAP — Escopo Item 3; Critério de Sucesso Item 1 |
| RF-ED-02 | O processo deve produzir e entregar o Pacote de Insumos para RFP até 08/05/2026, contendo: shortlist de 2 fornecedores recomendados, critérios de seleção preliminares para o processo de RFP, glossário de termos técnicos e um sumário dos gaps identificados que o RFP deverá abordar. | Must Have | Pacote entregue até 08/05/2026; shortlist com exatamente 2 fornecedores identificados com justificativa; ao menos 15 critérios de seleção preliminares listados e categorizados; documento aprovado pelos sponsors. | TAP — Escopo Item 6; Critério de Sucesso Item 5 |
| RF-ED-03 | O processo deve produzir Status Reports semanais toda quarta-feira durante as 5 semanas da Fase 1, em formato PDF, contendo: status semáforo (vermelho/amarelo/verde) por dimensão (prazo, escopo, custo, qualidade, riscos), resumo das atividades da semana, próximas atividades e issues abertas. | Must Have | 5 Status Reports produzidos nas datas corretas (08/04, 15/04, 22/04, 29/04, 06/05); publicados no SharePoint até às 18h da quarta-feira; nenhum Status Report com dimensão sem avaliação semáforo. | TAP — Escopo Item 5; Governança |
| RF-ED-04 | O processo deve produzir Flash Reports diários (todos os dias úteis) durante as 5 semanas, enviados por e-mail até as 18h de cada dia útil, contendo: atividades concluídas no dia, atividades previstas para o próximo dia útil e eventuais bloqueios ou escalações. | Must Have | 25 Flash Reports produzidos (5 semanas × 5 dias úteis); enviados por e-mail para lista de distribuição incluindo todos os stakeholders listados; nenhum dia útil sem Flash Report exceto feriados documentados previamente. | TAP — Escopo Item 5; Governança |
| RF-ED-05 | O processo deve preparar e apresentar material de Comitê Executivo toda quinta-feira durante as 5 semanas da Fase 1, em formato de apresentação (.pptx ou equivalente), cobrindo: avanço do projeto, decisões necessárias, riscos críticos e próximas milestones. | Must Have | 5 apresentações de Comitê produzidas e apresentadas nas datas corretas (09/04, 16/04, 23/04, 30/04, 07/05); material enviado aos participantes com ao menos 2 horas de antecedência; ata de cada reunião publicada no SharePoint em até 24 horas após a reunião. | TAP — Escopo Item 5; Governança |
| RF-ED-06 | O processo deve manter repositório centralizado de documentos no SharePoint do projeto, com estrutura de pastas padronizada, controle de versão explícito (v1.0, v1.1, v2.0) e permissões de acesso adequadas por perfil (equipe VMO, equipe KPMG, sponsors GAB). | Must Have | Repositório SharePoint ativo desde D+2 do início da Fase 1; estrutura de pastas aprovada pelo GP interno; 100% dos artefatos formais publicados no SharePoint; nenhum artefato aprovado em versão inferior à 1.0. | TAP — Governança |
| RF-ED-07 | O processo deve produzir ata formal de cada workshop realizado, contendo: data, local/modalidade, participantes (nome e cargo), pauta cumprida, principais conclusões, decisões tomadas, pendências com responsável e prazo, e assinatura eletrônica ou confirmação por e-mail do facilitador e do representante da área. | Must Have | 100% dos workshops com ata produzida em até 2 dias úteis após a sessão; ata publicada no SharePoint; confirmação de recebimento do representante da área registrada. | TAP — Escopo Item 1 |
| RF-ED-08 | O processo deve elaborar e entregar o Relatório de Encerramento da Fase 1 até 08/05/2026, documentando: resumo das entregas realizadas vs. planejadas, desvios e suas justificativas, lições aprendidas, recomendações para a Fase 2 e NPS dos sponsors. | Must Have | Relatório de Encerramento entregue e aprovado pelos sponsors até 08/05/2026; seção de lições aprendidas com ao menos 5 itens; NPS de cada sponsor com pontuação numérica registrada. | TAP — Escopo Item 8; Critério de Sucesso Item 6 |

---

### 1.5 Comunicação com Stakeholders

| ID | Descrição | MoSCoW | Critério de Aceitação | Origem |
|----|-----------|--------|-----------------------|--------|
| RF-CS-01 | O processo deve manter plano de comunicação formal documentando: cada tipo de comunicação (Flash Report, Status Report, Comitê, ad hoc), frequência, canal, responsável pelo envio e lista de destinatários por tipo. | Must Have | Plano de comunicação aprovado pelos sponsors antes do Kick Off; lista de distribuição validada com e-mails ativos de todos os stakeholders; nenhuma comunicação formal enviada fora dos canais definidos. | TAP — Governança |
| RF-CS-02 | O processo deve escalar imediatamente (em até 4 horas úteis) ao Sócio KPMG (Rodrigo Figaro) e ao VP do GAB (Décio Chieppe) qualquer evento que coloque em risco os critérios de sucesso da Fase 1, incluindo: recusa de participação de área funcional, indisponibilidade de fornecedor para demo ou mudança de escopo solicitada. | Must Have | Registro de todas as escalações realizadas com data/hora, canal utilizado, conteúdo e resposta recebida; nenhuma situação de risco crítico permanece sem escalação por mais de 4 horas úteis. | TAP — Governança; Critérios de Sucesso |
| RF-CS-03 | O processo deve obter aprovação formal (e-mail ou assinatura) dos 3 sponsors para os seguintes artefatos antes de avançar para a etapa subsequente: (a) Plano do Projeto, (b) Score Model com pesos, (c) Relatório de Recomendação. | Must Have | Evidência de aprovação (e-mail ou documento assinado) de Décio Chieppe, Paula Barcelos e Patrícia Poubel nos 3 artefatos listados; nenhum artefato avança para uso sem aprovação dos 3 sponsors. | TAP — Governança; Critérios de Sucesso Item 3 |
| RF-CS-04 | O processo deve conduzir reunião de apresentação final do Relatório de Recomendação com presença dos 3 sponsors, equipe VMO e equipe KPMG, utilizando sessão via Microsoft Teams com gravação, até 08/05/2026. | Must Have | Reunião realizada até 08/05/2026 com presença confirmada de ao menos 1 representante de cada entidade; gravação arquivada no SharePoint; ata com decisão de aprovação ou solicitação de revisão registrada. | TAP — Critério de Sucesso Item 3 |
| RF-CS-05 | O processo deve coletar feedback estruturado dos participantes após cada workshop por meio de formulário padronizado (no máximo 5 perguntas), avaliando: clareza da condução, relevância do conteúdo, qualidade da facilitação e expectativas para próximos passos. | Should Have | Formulário de feedback enviado para todos os participantes em até 24 horas após cada workshop; taxa de resposta ≥ 60%; resultados consolidados apresentados no Status Report da semana correspondente. | Qualidade do Processo |
| RF-CS-06 | O processo deve disponibilizar canal de comunicação direto (grupo no Microsoft Teams ou equivalente) entre a equipe VMO e os pontos focais das 3 entidades para resolução ágil de dúvidas operacionais, com comprometimento de resposta em até 1 dia útil. | Should Have | Canal criado até D+2 do início da Fase 1; todos os pontos focais adicionados; log de interações mantido; nenhuma dúvida operacional sem resposta por mais de 1 dia útil. | TAP — Governança |

---

### 1.6 Encerramento e Transição para Fase 2

| ID | Descrição | MoSCoW | Critério de Aceitação | Origem |
|----|-----------|--------|-----------------------|--------|
| RF-ET-01 | O processo deve entregar shortlist formal de 2 plataformas/fornecedores recomendados para a Fase 2 (RFP), com justificativa fundamentada no Score Model e nos gaps identificados nos workshops. | Must Have | Shortlist entregue como componente do Pacote de Insumos para RFP até 08/05/2026; exatamente 2 fornecedores identificados; para cada fornecedor, ao menos 3 argumentos objetivos derivados do Score Model. | TAP — Critério de Sucesso Item 5 |
| RF-ET-02 | O processo deve produzir lista de critérios de seleção preliminares para o processo de RFP, derivados dos gaps identificados nos workshops e das avaliações do Score Model, organizados por categoria (funcional, técnico, financeiro, estratégico). | Must Have | Ao menos 15 critérios de seleção preliminares documentados, categorizados e priorizados (Must Have / Should Have para o RFP); entregues como parte do Pacote de Insumos para RFP até 08/05/2026. | TAP — Escopo Item 6; Critério de Sucesso Item 5 |
| RF-ET-03 | O processo deve realizar reunião de handover formal entre a equipe VMO e o GP interno do GAB (Marcelo Silveira) transferindo todos os artefatos, senhas de acesso a repositórios e responsabilidades operacionais da Fase 1 antes do encerramento. | Must Have | Reunião de handover realizada até 08/05/2026; lista de artefatos entregues assinada por Marcelo Silveira; nenhum artefato produzido na Fase 1 sem localização registrada no SharePoint. | TAP — Escopo Item 8 |
| RF-ET-04 | O processo deve documentar os principais riscos e premissas identificados na Fase 1 que são relevantes para o planejamento da Fase 2 (RFP), como insumo para o TAP da próxima fase. | Should Have | Seção de riscos e premissas para a Fase 2 incluída no Relatório de Encerramento; ao menos 5 riscos/premissas documentados com descrição e recomendação de mitigação para a equipe da Fase 2. | TAP — Escopo Item 8 |
| RF-ET-05 | O processo deve consolidar e entregar o arquivo histórico completo do projeto (atas, artefatos, planilhas, apresentações, correspondências formais) em repositório SharePoint com estrutura final organizada, até a data de encerramento formal. | Should Have | Repositório SharePoint com 100% dos artefatos formais publicados, organizados por pasta e versão, acessível ao GP interno e sponsors; nenhum artefato com acesso bloqueado para os perfis autorizados. | TAP — Escopo Item 8 |

---

## 2. Requisitos Não-Funcionais

| ID | Categoria | Descrição | MoSCoW | Critério de Aceitação |
|----|-----------|-----------|--------|-----------------------|
| RNF-01 | Prazo | Todas as 8 entregas formais (Kick Off, 5 Status Reports, Relatório de Recomendação, Pacote RFP, Relatório de Encerramento) devem ser realizadas dentro das datas comprometidas no plano do projeto, com desvio máximo tolerado de 1 dia útil para entregas intermediárias e zero tolerância para a entrega final de 08/05/2026. | Must Have | Desvio de prazo ≤ 1 dia útil para entregas intermediárias; entrega final até 08/05/2026 às 23:59; qualquer desvio registrado no Status Report com justificativa e plano de recuperação. |
| RNF-02 | Objetividade da Avaliação | O Score Model deve ter ≥ 70% dos seus critérios de avaliação derivados de fontes objetivas e verificáveis (demos, RFI, benchmarks publicados), não de percepções individuais não documentadas. | Must Have | Planilha do Score Model com coluna "Tipo de Fonte" (Objetivo / Subjetivo) preenchida para cada critério; contagem resultando em ≥ 70% de critérios objetivos; auditável por terceiro sem acesso à equipe do projeto. |
| RNF-03 | Qualidade da Documentação | Nenhum artefato formal (relatório, ata, score model, pacote RFP) pode conter termos vagos não definidos no Glossário (Seção 4) ou afirmações não fundamentadas em evidência documentada. | Must Have | Revisão de qualidade realizada por ao menos um membro sênior (VMO ou KPMG) antes de cada entrega formal; nenhum artefato aprovado com itens de revisão abertos de prioridade alta. |
| RNF-04 | Confidencialidade | Todos os documentos contendo informações estratégicas, financeiras ou operacionais do GAB devem ser classificados como "Confidencial" e compartilhados exclusivamente com os stakeholders autorizados listados no plano de comunicação. | Must Have | 100% dos artefatos formais com cabeçalho de classificação de confidencialidade; nenhum documento enviado para destinatário fora da lista de distribuição aprovada; evidência de controle de acesso no SharePoint. |
| RNF-05 | Disponibilidade da Equipe | A equipe designada pela VMO para a Fase 1 deve estar disponível para execução das atividades do projeto por ao menos 80% da jornada semanal durante as 5 semanas, sem substituição de membro sênior sem aprovação prévia do GP e do Sócio KPMG. | Must Have | Nenhuma substituição de membro sênior sem aprovação documentada; registro de ausências superiores a 2 dias consecutivos comunicado ao GP interno com antecedência de ao menos 3 dias úteis. |
| RNF-06 | Rastreabilidade | Cada critério do Score Model deve ser rastreável a ao menos um requisito de negócio identificado nos workshops, e cada requisito de negócio deve ser rastreável a ao menos uma área funcional de uma entidade específica. | Must Have | Matriz de rastreabilidade Score Model ↔ Workshop ↔ Entidade publicada no repositório; sem critério de avaliação sem origem documentada. |
| RNF-07 | Neutralidade da Avaliação | O processo de avaliação das plataformas deve ser conduzido de forma neutra, sem conflito de interesses declarado; nenhum membro da equipe VMO ou KPMG pode ter relação comercial ativa com qualquer dos 3 fornecedores avaliados não previamente declarada e aceita pelos sponsors. | Must Have | Declaração de conflito de interesses assinada por todos os membros das equipes VMO e KPMG antes do início das avaliações; declarações arquivadas no SharePoint; quaisquer conflitos declarados comunicados aos sponsors antes de decidir sobre permanência no projeto. |
| RNF-08 | Língua e Formatação | Todos os artefatos formais devem ser produzidos em português brasileiro, com revisão ortográfica e gramatical, fontes e templates padronizados conforme o padrão de documentação VMO. | Should Have | Nenhum artefato formal entregue aos sponsors com erros ortográficos ou gramaticais identificados na revisão; template padronizado aplicado a 100% dos artefatos; nenhum termo em idioma estrangeiro sem tradução ou definição entre parênteses. |
| RNF-09 | Tempo de Resposta a Escalações | Situações de risco crítico ao projeto (bloqueio de workshops, recusa de fornecedor, mudança de escopo) devem ser escaladas e ter resposta de encaminhamento registrada em no máximo 4 horas úteis a partir da identificação. | Must Have | Log de escalações com timestamp de identificação e de resposta; nenhuma escalação crítica com gap de tempo > 4 horas úteis sem registro de justificativa. |
| RNF-10 | Satisfação dos Sponsors | O NPS médio dos 3 sponsors ao final da Fase 1 deve ser ≥ 7,0 em escala de 0 a 10. | Must Have | NPS coletado individualmente de cada sponsor por formulário padronizado até 08/05/2026; média aritmética dos 3 NPS ≥ 7,0; resultados documentados no Relatório de Encerramento. |
| RNF-11 | Independência de Plataforma de Trabalho | Os artefatos entregues devem ser acessíveis em Microsoft Office (Word, Excel, PowerPoint) e/ou PDF, sem dependência de softwares proprietários adicionais não disponíveis nos ambientes do GAB. | Should Have | 100% dos artefatos entregues em formato .docx/.xlsx/.pptx e/ou .pdf; nenhum artefato acessível apenas em ferramentas não disponíveis no ambiente padrão do GAB. |
| RNF-12 | Auditabilidade do Score Model | A planilha do Score Model deve ser construída de forma auditável: fórmulas expostas, sem macros ocultas, com guia de instruções de uso integrado, permitindo que terceiro não participante do projeto reproduza o cálculo a partir dos dados brutos. | Should Have | Score Model revisado por membro não participante da construção que consegue reproduzir o resultado final sem assistência; guia de instruções presente na primeira aba da planilha. |

---

## 3. Resumo de Priorização MoSCoW

### Requisitos Funcionais

| Prioridade | Quantidade | Percentual |
|------------|------------|------------|
| Must Have  | 22         | 81,5%      |
| Should Have | 5         | 18,5%      |
| Could Have | 0          | 0%         |
| Won't Have | 0          | 0%         |
| **Total**  | **27**     | **100%**   |

### Requisitos Não-Funcionais

| Prioridade | Quantidade | Percentual |
|------------|------------|------------|
| Must Have  | 9          | 75,0%      |
| Should Have | 3         | 25,0%      |
| Could Have | 0          | 0%         |
| Won't Have | 0          | 0%         |
| **Total**  | **12**     | **100%**   |

### Totais Consolidados

| Prioridade | RF | RNF | Total | % Total |
|------------|----|-----|-------|---------|
| Must Have  | 22 | 9   | 31    | 79,5%   |
| Should Have | 5 | 3   | 8     | 20,5%   |
| Could Have | 0  | 0   | 0     | 0%      |
| Won't Have | 0  | 0   | 0     | 0%      |
| **Total**  | **27** | **12** | **39** | **100%** |

> **Nota de Priorização:** A concentração de Must Haves reflete a natureza do projeto — um assessment com prazo rígido de 5 semanas onde quase todas as atividades são interdependentes e críticas para o critério de sucesso principal (recomendação de plataforma em 08/05/2026). Os Should Haves representam elementos de qualidade que, se não entregues, reduzem a robustez do processo mas não inviabilizam o objetivo central.

---

## 4. Glossário

| Termo | Definição no Contexto do Projeto |
|-------|----------------------------------|
| **Assessment** | Processo estruturado de avaliação e análise comparativa de plataformas ERP com objetivo de produzir recomendação fundamentada, sem incluir implementação ou configuração de software. |
| **AS-IS** | Descrição do estado atual de um processo de negócio, incluindo fluxo, sistemas utilizados e volumes, antes de qualquer mudança decorrente de novo sistema. |
| **Benchmark** | Dado de mercado publicado por fonte independente (analistas como Gartner ou Forrester, associações setoriais, estudos de caso verificáveis) utilizado como referência objetiva na avaliação de plataformas. |
| **Comitê Executivo** | Reunião semanal de governança com participação dos sponsors do GAB e equipes VMO/KPMG, realizada toda quinta-feira via Microsoft Teams, com pauta e ata formais. |
| **Critério de Avaliação** | Elemento específico e mensurável utilizado no Score Model para pontuar cada plataforma candidata dentro de um pilar, classificado como objetivo (fonte verificável) ou subjetivo (percepção). |
| **ERP** | Enterprise Resource Planning — plataforma de software integrado que suporta processos de negócio de múltiplas áreas funcionais (Finanças, RH, Suprimentos, etc.) em uma base de dados unificada. |
| **Flash Report** | Comunicado diário enviado por e-mail até as 18h de cada dia útil, contendo síntese das atividades do dia e do próximo dia útil, além de bloqueios e escalações. Máximo 1 página. |
| **GAB** | Grupo Águia Branca — holding e suas subsidiárias VixPar (logística) e VAB (transporte de passageiros), cliente do projeto. |
| **Gap Funcional** | Capacidade de negócio identificada nos workshops que não é suportada nativamente pela plataforma avaliada, exigindo customização, integração com sistema terceiro ou mudança de processo. |
| **Holding** | Entidade corporativa central do Grupo Águia Branca, responsável pelas funções corporativas e controle das subsidiárias VixPar e VAB. |
| **KPMG** | KPMG Consultoria Ltda. — parceiro de consultoria no projeto, responsável pela metodologia Powered Enterprise e pelo Score Model. |
| **MoSCoW** | Método de priorização de requisitos que classifica cada item em Must Have (obrigatório), Should Have (importante), Could Have (desejável) ou Won't Have (fora do escopo atual). |
| **NPS** | Net Promoter Score — métrica de satisfação em escala de 0 a 10 onde ≥ 9 = promotor, 7-8 = neutro, ≤ 6 = detrator. Para este projeto, o critério de sucesso é NPS médio dos sponsors ≥ 7,0. |
| **Oracle ERP Cloud** | Plataforma ERP em nuvem da Oracle Corporation, uma das 3 plataformas candidatas avaliadas neste assessment. |
| **Pilar (Score Model)** | Uma das 6 dimensões de avaliação do Score Model KPMG Powered Enterprise, cada uma com peso percentual definido e conjunto de critérios associados. Os 6 pilares são: (1) Funcionalidade, (2) Tecnologia e Arquitetura, (3) Financeiro/TCO, (4) Implementação e Suporte, (5) Estratégia do Fornecedor, (6) Adequação ao GAB. |
| **Plataforma Candidata** | Uma das 3 soluções ERP em avaliação: SAP S/4HANA Rise, Oracle ERP Cloud e TOTVS Protheus. |
| **Powered Enterprise** | Metodologia de avaliação e seleção de plataformas ERP da KPMG, que inclui o Score Model com 6 pilares ponderados como ferramenta central de avaliação comparativa. |
| **RACI** | Matriz de responsabilidades que define para cada atividade quem é Responsável (R), Aprovador (A), Consultado (C) e Informado (I). |
| **RFI** | Request for Information — questionário padronizado enviado aos fornecedores das plataformas candidatas para coletar informações técnicas, funcionais e comerciais de forma estruturada e comparável. |
| **RFP** | Request for Proposal — processo formal de seleção de fornecedor com escopo detalhado, critérios de avaliação e solicitação de proposta comercial. A RFP é o objeto da Fase 2 do projeto, fora do escopo desta ERF. |
| **SAP S/4HANA Rise** | Plataforma ERP em nuvem da SAP SE, uma das 3 plataformas candidatas avaliadas neste assessment. |
| **Score Model** | Planilha de avaliação comparativa estruturada com critérios ponderados por pilar, utilizada para calcular a pontuação de cada plataforma candidata e gerar o ranking que fundamenta a recomendação. |
| **Shortlist** | Lista reduzida de 2 plataformas/fornecedores recomendados para avançar ao processo de RFP na Fase 2, derivada do ranking do Score Model. |
| **Sponsor** | Executivo com autoridade de decisão e aprovação no projeto. Neste projeto: Décio Chieppe (VP Holding), Paula Barcelos (Diretora VAB) e Patrícia Poubel (Diretora VixPar). |
| **Status Report** | Relatório semanal de status do projeto, produzido toda quarta-feira em formato PDF, com avaliação semáforo por dimensão e publicado no SharePoint. |
| **TAP** | Termo de Abertura do Projeto — documento de iniciação que define escopo, objetivos, critérios de sucesso, stakeholders e premissas do PROJ-2026-003. |
| **TCO** | Total Cost of Ownership — custo total de propriedade da plataforma ao longo do tempo, incluindo licença/subscrição, implementação, sustentação e migração, tipicamente projetado para um horizonte de 5 anos. |
| **TOTVS Protheus** | Plataforma ERP da TOTVS S.A., uma das 3 plataformas candidatas avaliadas neste assessment. |
| **VAB** | Viação Águia Branca S.A. — subsidiária do GAB atuante no segmento de transporte rodoviário de passageiros. |
| **VixPar** | VixPar Logística — subsidiária do GAB atuante no segmento de logística e transporte de cargas. |
| **VMO** | Value Management Office — denominação da estrutura de gestão e do modelo de consultoria da VMO Consultoria, responsável pela condução deste projeto. |
| **Workshop** | Sessão estruturada de elicitação de processos, conduzida com representantes de uma área funcional de uma entidade, com facilitador designado, pauta definida e artefato de saída obrigatório. |

---

## 5. Perguntas Abertas — Requerem Validação

> Os itens abaixo foram identificados durante a elicitação como ambiguidades ou lacunas que precisam ser respondidas pelos stakeholders antes da finalização desta ERF.

| ID | Questão | Destinatário | Impacto nos Requisitos |
|----|---------|--------------|------------------------|
| PA-01 | Quais são os 6 pilares exatos do Score Model Powered Enterprise e seus respectivos pesos percentuais? O documento TAP menciona "6 pilares ponderados" sem detalhar os pesos. Os pesos já estão pré-definidos pela KPMG ou serão definidos conjuntamente com os sponsors? | Rodrigo Figaro (KPMG) / Décio Chieppe (GAB) | RF-SM-01, RF-SM-05, RF-SM-06 |
| PA-02 | Existe modelo/template padrão da KPMG para o RFI a ser enviado aos fornecedores, ou ele será construído do zero com base nos outputs dos workshops? Qual o prazo mínimo acordado com os fornecedores para resposta ao RFI? | Wallacy Lima (KPMG) | RF-SM-04 |
| PA-03 | As 21 sessões de workshop (7 áreas × 3 entidades) podem ser realizadas de forma combinada (ex.: área de Finanças com representantes das 3 entidades em uma única sessão) ou obrigatoriamente separadas por entidade? | Décio Chieppe / Marcelo Silveira | RF-WK-01 |
| PA-04 | Qual o formato esperado para a coleta do NPS dos sponsors — formulário digital, entrevista estruturada ou outra modalidade? A pontuação é individual ou coletiva por entidade? | Marcelo Silveira (GP GAB) | RF-PG-06, RNF-10 |
| PA-05 | Existem restrições de confidencialidade específicas para as respostas ao RFI dos fornecedores? As respostas podem ser compartilhadas integralmente com todos os sponsors ou há necessidade de anonimização de alguma informação comercial? | Rodrigo Figaro (KPMG) / Décio Chieppe | RF-SM-04, RNF-04 |
| PA-06 | O Score Model final deve ser entregue como planilha Excel editável ou somente o relatório de resultados? Há restrição de acesso à planilha base (com fórmulas expostas) para os sponsors? | Décio Chieppe / Wallacy Lima | RF-SM-05, RNF-12 |

---

## 6. Aprovação

| Papel | Nome | Assinatura | Data |
|-------|------|------------|------|
| Gerente do Projeto (VMO) | _______________________ | _______________________ | ___/___/_____ |
| Gerente do Projeto (GAB) | Marcelo Silveira | _______________________ | ___/___/_____ |
| Gerente Sênior (KPMG) | Wallacy Lima | _______________________ | ___/___/_____ |
| Sponsor — Holding | Décio Chieppe | _______________________ | ___/___/_____ |
| Sponsor — VAB | Paula Barcelos | _______________________ | ___/___/_____ |
| Sponsor — VixPar | Patrícia Poubel | _______________________ | ___/___/_____ |

---

*Documento produzido por Rafael Requisito — Engenheiro de Requisitos | VMO Consultoria*
*Próxima revisão: após validação das Perguntas Abertas (PA-01 a PA-06)*
*Versão 1.0 — 2026-05-14*
