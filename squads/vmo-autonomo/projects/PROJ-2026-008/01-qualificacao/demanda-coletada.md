# DEMANDA COLETADA — DEM-2026-008

**Coletado por:** Iara Inbound (Coletora de Demandas — VMO Autônomo)
**Data de coleta:** 2026-06-10
**Cliente:** Grupo Águia Branca (divisão VIX Logística / VIXPar)

---

## 1. Fontes Consultadas

| # | Fonte | Tipo | Data do documento/registro |
|---|-------|------|------------------------------|
| 1 | "06005284_001_Melhorias_Monitor_WorkRequest_4918651_ATUAL.docx" — Work Request, escopo técnico detalhado | Documento de escopo (Work Request) | Não datado explicitamente no corpo extraído — requer esclarecimento |
| 2 | Chamado nº 6898567 — Sistema Business Desk Águia Branca, "Sistemática ERP > Solicitação de Novas Demandas / Projetos" | Registro de chamado (Service Desk v.8 / Atendame) | Abertura: 09/06/2026 12:00 |
| 2a | E-mail original de Tatiane Dias de Moraes para Raphael Leitão Sbardelotti e Nubia Carla Freitas Santos Souza | E-mail (anexo ao chamado) | 06/03/2026 10:55–10:56 |
| 2b | E-mail "APROVAÇÃO - GERENTE DE TI" — Raphael Leitão Sbardelotti | E-mail (anexo ao chamado, "Re:") | 10/03/2026 10:11 |
| 2c | E-mail "APROVAÇÃO - GESTOR DIRETO" / arquivo "APROVAÇÃO - DIRETOR DA ÁREA.pdf" — Nubia Carla Freitas Santos Souza | E-mail (anexo ao chamado) | 11/03/2026 09:13–09:14 |

---

## 2. Dados da Demanda

### 2.1 Solicitante

- **Nome:** Tatiane Dias de Moraes
- **Cargo:** Coordenadora de Controle de Ativos e Recebimento Fiscal (chamado registra também "COORD. DE AVALIACAO DE PATRIMONIO" — ⚠️ INCONSISTÊNCIA: dois títulos de cargo distintos aparecem nas fontes para a mesma pessoa — Fonte 2, dado cadastral vs. assinatura do e-mail Fonte 2c)
- **Empresa/Divisão:** VIXPar (Contabilidade) / VIX Matriz, conforme registros — Fonte 2
- **Matrícula:** 300513103 — Fonte 2
- **E-mail:** Tatiane@vix.com.br — Fonte 1 e Fonte 2
- **Telefone/Ramal:** (27) 2125-1905 / Celular 27999784169 — Fonte 2
- **Hierarquia (sistema):** DIV. LOGISTICA/VIX/VITORIA/Users/Contabilidade (300113000) — Fonte 2
- **Superior Hierárquico (campo do sistema):** Tatiane Dias de Moraes (autorreferência) — ⚠️ INCONSISTÊNCIA: o sistema aponta a própria solicitante como sua superiora hierárquica; provável erro de cadastro do Service Desk — Fonte 2. Requer esclarecimento sobre quem é o superior hierárquico real de Tatiane.

**Solicitante/Provedor de Requisitos adicional (Fonte 1):**
- **Nome:** João Henrique
- **E-mail:** joaomerlo@vix.com.br
- Papel exato de João Henrique na demanda — NÃO INFORMADO — requer esclarecimento (cargo, departamento, relação hierárquica com Tatiane).

**Beneficiado:** Tatiane Dias de Moraes (VIX Matriz) — Fonte 2 (idêntico ao Solicitante)

**Especialista técnico designado (lado Águia Branca/SAP):**
- **Nome:** Jerfesson Fernandes Helmer — jerfesson@aguiabranca.com.br — Fonte 1
- Papel: especialista responsável por alterações já realizadas (V1) nos monitores ZMMR_GSI01 a ZMMR_GSI04 — Fonte 1

**Grupo Solucionador designado:** Projetos DTI — Fonte 2
**Responsável pelo atendimento:** Não Informado — Fonte 2

### 2.2 Necessidade de Negócio

Conforme Fonte 1 (campo "Situação Atual/Problema"): os usuários do setor de Contabilidade/Controle de Ativos (VIX/VIXPar) atualmente não possuem autonomia para alterar e excluir processos nos monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 (e, conforme histórico de alterações, também ZMMR_GSI01). Essa limitação:
- Reduz a completude e a aderência dos monitores às necessidades do setor;
- Prejudica a otimização dos ajustes e o fechamento contábil mensal;
- Impacta negativamente o processo de criação e legalização de equipamentos/frota (ativos imobilizados).

**Necessidade de negócio síntese:** maior autonomia operacional, completude funcional e agilidade no processo de criação e legalização de imobilizados (frota), e na escrituração fiscal (entrada de notas fiscais) vinculada a esse processo, com ganho de tempo no fechamento mensal.

⚠️ Nota de método (Iara Inbound): a Necessidade de Negócio acima foi extraída do campo "Situação Atual/Problema" da Fonte 1, que mistura diagnóstico de problema com elementos de solução proposta. Os 15 itens do escopo detalhado (seção 3 abaixo) constituem o **Pedido Específico** (a solução técnica proposta), e não devem ser confundidos com a necessidade de negócio em si.

### 2.3 Pedido Específico

Solicitação de ajustes/melhorias adaptativas (intervenção de Integração) nos monitores SAP ECC módulo MM: **ZMMR_GSI01, ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04**, transações relacionadas: ME51N, ME52N, ME21N, ME22N, ZMMTR002, AS01, AS02.

- **Equipe responsável (lado fornecedor SAP):** SQUAD PM/MM
- **Tipo de Atendimento:** Demanda
- **Tipo de Intervenção:** Adaptativa
- **Intervenção SAP:** Integração
- **Prioridade declarada (Fonte 1):** Baixa — ⚠️ INCONSISTÊNCIA: a Fonte 2 classifica a Criticidade do chamado como "2 - Alta" e o SLA da atividade como 1 semana. Há divergência entre a prioridade declarada no Work Request (Baixa) e a criticidade/SLA do chamado de Service Desk (Alta / 1 semana). Requer esclarecimento de qual classificação deve prevalecer para fins de priorização no backlog do VMO.

O escopo detalhado é composto por **15 itens rastreáveis**, documentados na íntegra na Seção 3 (Anexo — Tabela de Escopo Detalhado).

### 2.4 Benefício Esperado

Conforme Fonte 2 (formulário do chamado):
- **Aumento de receita?** Não
- **Redução de custo?** Não
- **Melhoria de processo?** Não — ⚠️ INCONSISTÊNCIA: o texto descritivo da "Situação Atual/Problema" (Fonte 1) e o próprio título/descrição da demanda indicam explicitamente objetivo de melhoria de processo ("tornará o monitor mais completo... otimizando os ajustes e o fechamento do mês"), mas o campo estruturado "Melhoria de processo?" no formulário do chamado foi marcado "Não". Requer esclarecimento — possível erro de preenchimento do formulário.
- **Aumento de produtividade?** Sim
- **Quantificação do ganho (texto literal da Fonte 2):** "Maior eficiência, agilidade e assertividade no processo de criação de imobilizado de frota e entrada de notas fiscais."
- **Indicador para medir ganhos:** N/A — NÃO INFORMADO — requer esclarecimento: qual métrica/indicador será usado para validar o ganho de produtividade após a entrega (ex.: tempo médio de fechamento mensal, nº de retrabalhos/estornos, tempo de criação de imobilizado).

### 2.5 Urgência e Prazo

- **Prazo da Atividade (Fonte 2):** 1 semana (Situação SLA: No Prazo, Tempo Restante: 35:17 hs)
- **Data de Abertura:** 09/06/2026 12:00
- **Data Início Prevista:** 09/06/2026 12:00
- **Data Término Prevista:** 16/06/2026 12:00
- **Data Início Real:** Não Iniciada
- **Data Término Real:** Não encerrada
- **Justificativa de urgência (campo "Se a demanda for urgente, justifique o motivo"):** N/A — Fonte 2
- **Necessidade Legal/Obrigatória?** Não — Fonte 2

⚠️ INCONSISTÊNCIA: o SLA de 1 semana para um pacote de 15 itens de ajuste em monitores SAP (alguns envolvendo lógica de estorno e geração automática de MIRO) parece tecnicamente desproporcional ao escopo. A Prioridade declarada no Work Request é "Baixa", mas o SLA do chamado é de apenas 1 semana com Criticidade "2 - Alta". Requer esclarecimento sobre o prazo real esperado pelo Solicitante e sobre como esse prazo foi definido.

Não há, nas fontes anexadas, qualquer citação a CEO, Diretor ou VP como origem ou justificativa de urgência da demanda — portanto, a sinalização `⚠️ CLAIM SEM EVIDÊNCIA` (regra de governança 2) **não se aplica** a este caso com base nas fontes disponíveis.

### 2.6 Aprovações e Autorizações Identificadas

Conforme regra de governança 1, uma demanda só é considerada **VALIDADA** se possuir: (i) aprovação formal de **Diretoria** da área solicitante; e (ii) aprovação do **Gerente de TI** da divisão solicitante. Avaliação abaixo:

| Documento anexado ao chamado (nome do arquivo) | Conteúdo real identificado | Quem assina | Cargo declarado | Data | Atende a quê (governança)? |
|---|---|---|---|---|---|
| "APROVAÇÃO - GERENTE DE TI.pdf" | E-mail "Re: Melhorias Monitor de Requisições SAP - Aquisição de frota" — corpo: "De acordo." | Raphael Leitão Sbardelotti | Não declarado explicitamente no corpo do e-mail; referenciado no contexto do chamado como aprovador de TI / "Gerente de TI" | 10/03/2026 10:11 | Possível atendimento ao requisito **(ii) Gerente de TI** — porém o cargo de Raphael não está formalmente declarado em nenhuma assinatura nas fontes. **NÃO CONFIRMADO — requer esclarecimento**: qual o cargo formal de Raphael Leitão Sbardelotti? |
| "APROVAÇÃO - GESTOR DIRETO.pdf" | E-mail de Nubia Carla Freitas Santos Souza, corpo: "Tatiane, De acordo." (também encaminhado/"ENC:" para registro) | Nubia Carla Freitas Santos Souza | Gerente Contábil — Contabilidade — VIXPar | 11/03/2026 09:13–09:14 | Aprovação de **Gestor Direto / Gerente Contábil** — não corresponde a Diretoria nem a Gerente de TI |
| "APROVAÇÃO - DIRETOR DA ÁREA.pdf" | ⚠️ INCONSISTÊNCIA: o nome do arquivo indica aprovação de **Diretor da Área**, mas o conteúdo extraído deste anexo, conforme indicado na Fonte 2, **corresponde ao mesmo e-mail da Nubia Carla Freitas Santos Souza (Gerente Contábil)** — não há, no conteúdo, evidência de aprovação por um Diretor | Nubia Carla Freitas Santos Souza (conforme conteúdo) | Gerente Contábil (conforme conteúdo) — divergente do nome do arquivo ("Diretor da Área") | 11/03/2026 09:13–09:14 (mesma data do item acima) | **NÃO ATENDE** ao requisito (i) Diretoria. Nome do arquivo sugere aprovação de Diretor, mas conteúdo não confirma. **Requer verificação do PDF original** para confirmar se há, de fato, conteúdo adicional de um Diretor que não foi capturado na extração, ou se o arquivo foi nomeado incorretamente / anexado em duplicidade. |
| Documento de escopo (.docx) | Fonte 1 — escopo técnico detalhado | — | — | — | Anexo de escopo, não constitui aprovação |

**Avaliação de Governança (Regra 1):**

- **(i) Aprovação formal de Diretoria da área solicitante:** **NÃO CONFIRMADA**. O único documento cujo nome de arquivo sugere aprovação de Diretor ("APROVAÇÃO - DIRETOR DA ÁREA.pdf") tem, segundo o conteúdo extraído disponível, o mesmo teor do e-mail da Gerente Contábil (Nubia), não de um Diretor. Adicionalmente, no e-mail original (Fonte 2a, 06/03/2026), Tatiane menciona explicitamente: *"@Nubia Carla Freitas Santos Souza, precisaremos também da aprovação do André."* — não há, nas fontes anexadas, qualquer e-mail de aprovação assinado por "André". **Lacuna confirmada.**
- **(ii) Aprovação do Gerente de TI da divisão solicitante:** **PARCIALMENTE INDICADA, NÃO CONFIRMADA FORMALMENTE**. Existe um e-mail de "De acordo." de Raphael Leitão Sbardelotti, anexado sob o nome "APROVAÇÃO - GERENTE DE TI.pdf", respondendo ao pedido de aprovação de Tatiane. Contudo, o cargo de Raphael não está formalmente declarado em nenhuma assinatura capturada nas fontes — a atribuição "Gerente de TI" decorre apenas do nome do arquivo e do contexto do pedido de Tatiane (que pede aprovação "para seguirmos com o projeto na TI"). **Requer confirmação formal do cargo de Raphael Leitão Sbardelotti.**

**Conclusão de Governança:** Com base nas evidências documentais disponíveis, **a demanda DEM-2026-008 NÃO PODE SER CONSIDERADA "VALIDADA"** segundo a regra de governança 1, pois:
1. Não há evidência de aprovação de Diretoria da área solicitante (a aprovação de "André", citada como necessária por Tatiane, não está documentada; e o arquivo nomeado "APROVAÇÃO - DIRETOR DA ÁREA.pdf" não contém, segundo o conteúdo extraído, manifestação de um Diretor).
2. A aprovação do Gerente de TI (Raphael Leitão Sbardelotti) está presente como manifestação ("De acordo."), mas o cargo formal de "Gerente de TI" não está comprovado documentalmente nas fontes — requer confirmação.

### 2.7 Contexto Organizacional

- **Empresa:** Grupo Águia Branca — Divisão VIX Logística / VIXPar — Setor Contabilidade / Controle de Ativos e Recebimento Fiscal
- **Imobilizado relacionado:** VIX – 2800184-0 — Fonte 2
- **Investimento esperado:** Até R$ 30.000 — Fonte 2
- **Investimento aprovado?** Sim — Fonte 2 (NOTA: esta resposta "Sim" no formulário do chamado não especifica por quem o investimento foi aprovado nem aponta para um documento específico de aprovação financeira/orçamentária distinto das aprovações de e-mail tratadas na Seção 2.6 — requer esclarecimento sobre a fonte/evidência da aprovação de investimento)
- **Projeto semelhante já implantado no GAB?** Sim — "Monitores de requisição, pedido e imobilizado" — Fonte 2
- **Impacta outras áreas de negócio?** Não — Fonte 2
- **Impacta outras divisões de negócio?** Não — Fonte 2
- **Requer integração com outros sistemas externos?** Não — Fonte 2 (observação: a própria Fonte 1 classifica a "Intervenção SAP" como "Integração", o que se refere à integração entre módulos/transações internas do SAP ECC MM, e não a sistemas externos — sem inconsistência real, apenas dois sentidos distintos do termo "integração")
- **Processo documentado?** Sim — Fonte 2
- **Solução já existe no mercado?** Não — Fonte 2

### 2.8 Contexto Implícito

(Inferências sinalizadas como tal — não tratadas como fato confirmado)

- A V1 dos ajustes nos monitores ZMMR_GSI01–04 já foi implementada anteriormente por Jerfesson Fernandes Helmer (Fonte 1, "Histórico de Alterações"); a presente demanda (DEM-2026-008) parece ser uma **evolução/V2** desse mesmo conjunto de monitores — requer confirmação se há relação formal de dependência/sequência entre a V1 já entregue e os 15 itens ora solicitados.
- O título do e-mail original ("Melhorias Monitor de Requisições SAP - Aquisição de frota") sugere que o foco de negócio principal é o processo de **aquisição e legalização de frota (veículos/equipamentos/implementos)**, com a parte de notas fiscais (MIRO/GSI03/GSI04) sendo um processo correlato/dependente.
- O nome "ZMMR_GSI01" aparece no Histórico de Alterações da Fonte 1 e no Caminho de Menu/Transação, mas **nenhum dos 15 itens do escopo detalhado faz referência explícita a ZMMR_GSI01** — requer esclarecimento se há ajustes pendentes para GSI01 não descritos no escopo, ou se a menção a GSI01 no cabeçalho é resquício de um escopo anterior (V1).

---

## 3. Anexo — Tabela de Escopo Detalhado (15 itens, Fonte 1)

| Item | Monitor(es)/Tela(s) afetados | Descrição resumida | Observações / rastreabilidade |
|---|---|---|---|
| 1 | ME53N, ZMMTR002, GSI02 | Criar campo "Classificação" na aba Dados de Cliente da ME53N; tratar obrigatoriedade via ZMMTR002; exibir como coluna no GSI02 | — |
| 2 | ME53N (ZLV/ZLP), GSI02 | Trazer campo "Vencimento NF" (já existente na ME53N para requisições ZLV/ZLP) como coluna no monitor de ativos GSI02 | Campo já existe na origem; trata-se de exposição no monitor |
| 3 | ME53N, GSI02 | Trazer campo "CR" (já existente na ME53N) como coluna no GSI02 | Campo já existe na origem; trata-se de exposição no monitor |
| 4 | ME53N, GSI02 | Trazer campo "Data Liberação/aprovação" da requisição (ME53N) como coluna no GSI02 | — |
| 5 | ME22N, GSI03 | Quando o monitor detectar a criação da aba "Histórico do pedido" na ME22N (lançamentos de MIRO via GRC, fora do monitor), carregar automaticamente o nº da MIRO para a etapa de fatura no GSI03 e marcar (flegar) automaticamente a etapa | Trata casos de lançamento "fora do fluxo padrão" do monitor |
| 6 | GSI03 / GSI04 | Trazer "Data de lançamento" da fatura (MIRO) como coluna do monitor | ⚠️ Texto da Fonte 1 cita ambos GSI03 e GSI04 — requer esclarecimento sobre qual(is) monitor(es) efetivamente deve(m) receber a coluna |
| 7 | PM (cadastro de equipamento), AS02 | Ao cadastrar veículo/equipamento em PM, atualizar automaticamente o campo "Placa do veículo" na aba Dados Dependentes de Tempo do imobilizado (AS02) | — |
| 8 | GSI03 (Legalização) | Para máquinas/implementos não emplacados, marcar automaticamente a etapa de Legalização como concluída (não requerem atuação de legalização) | — |
| 9 | GSI04 | Incluir "Nº de Requisição de Compra" como parâmetro de seleção (busca por nº da RC) | — |
| 10 | GSI02, GSI03, GSI04 | Permitir alterar o campo "Tipo de Veículo" mesmo após a criação do pedido, propagando a regularização para GSI02, GSI03 e GSI04 (atualmente só permitido antes da criação do pedido) | Mudança de regra de negócio existente |
| 11 | GSI02 | Listar o campo "Tipo de Veículo" como coluna no GSI02 | Relacionado ao item 10 |
| 12 | GSI03 | Permitir alteração do XML inserido incorretamente, desde que a etapa de PM não esteja legalizada nem o equipamento criado | Possui condição/restrição de elegibilidade |
| 13 | GSI03, GSI04 | Estorno: ao estornar a MIRO, excluir do GSI03/GSI04 o link da Fatura, atualizar status e log da requisição identificando o estorno; permitir inserir nova MIRO atualizando ambos os monitores. Regras: (a) não estornar pedido se houver MIRO ativa (estorno deve seguir ordem fatura→pedido); (b) ao excluir pedido, remover link da requisição, permitir nova inclusão e registrar estorno + nova inclusão no log | Item de maior complexidade lógica do escopo (múltiplas regras de negócio encadeadas) |
| 14 | GSI03 (Criar Fatura / MIRO) | Campo "DT. Básica" (aba Pagamentos) hoje é preenchido automaticamente com a data de criação do pedido — deve ficar em branco e só ser preenchido quando "Data da Fatura" (aba Dados Básicos) for informada. Campo "Vencimento Em" deve ser calculado como "DT. Básica" + "Condição de Pagamento" | Alteração de comportamento padrão de preenchimento automático |
| 15 | GSI02 (aba Atribuições), AS01 | Incluir o campo "Grupo deprec." no cadastro de imobilizado via GSI02 — campo já existe na AS01 mas não aparece no cadastro feito pelo monitor | — |

---

## 4. Lacunas Identificadas (Consolidado)

| # | Lacuna | Pergunta específica para o Solicitante |
|---|---|---|
| L1 | Cargo formal de João Henrique e seu papel na demanda | Qual o cargo, departamento e relação hierárquica de João Henrique (joaomerlo@vix.com.br) com Tatiane, em relação a esta demanda? |
| L2 | Superior hierárquico real de Tatiane | O sistema indica Tatiane como sua própria superiora hierárquica (autorreferência). Quem é, de fato, o superior hierárquico de Tatiane na estrutura VIXPar/Contabilidade? |
| L3 | Cargo formal de Raphael Leitão Sbardelotti | É possível confirmar formalmente (ex.: assinatura de e-mail completa, organograma) se Raphael Leitão Sbardelotti ocupa o cargo de Gerente de TI da divisão solicitante? |
| L4 | Aprovação de Diretoria (regra de governança 1) | Existe e-mail/documento formal de aprovação por um Diretor da área solicitante? O e-mail original de Tatiane menciona necessidade de aprovação de "André" — há essa aprovação documentada em algum lugar não anexado a este chamado? |
| L5 | Inconsistência nome de arquivo "APROVAÇÃO - DIRETOR DA ÁREA.pdf" | É possível reabrir o PDF original anexado sob esse nome para confirmar se ele contém, de fato, manifestação de um Diretor (além do e-mail da Nubia já identificado), ou se o arquivo foi nomeado/anexado incorretamente? |
| L6 | Evidência da aprovação de investimento (até R$ 30K) | Qual documento/processo formal evidencia a aprovação do investimento de até R$ 30K mencionada no chamado (campo "Possui investimento aprovado? Sim")? |
| L7 | Prioridade vs. SLA divergentes | A Fonte 1 declara Prioridade "Baixa", enquanto o chamado (Fonte 2) tem Criticidade "2 - Alta" e SLA de 1 semana. Qual classificação deve prevalecer para o backlog do VMO, e qual o prazo real esperado? |
| L8 | Campo "Melhoria de processo?" = Não | O formulário do chamado indica "Melhoria de processo? Não", em aparente contradição com a descrição textual da demanda. Este campo foi preenchido corretamente? |
| L9 | Indicador de medição de ganhos (N/A) | Qual indicador/métrica será usado para validar o ganho de produtividade esperado após a entrega (ex.: tempo de fechamento mensal, nº de estornos, tempo de criação de imobilizado)? |
| L10 | Item 6 — GSI03 vs. GSI04 | A coluna "Data de lançamento" da fatura (MIRO) deve ser incluída no GSI03, no GSI04, ou em ambos? |
| L11 | Relação entre V1 (já implementada) e os 15 itens (V2) | Os 15 itens descritos são uma evolução (V2) da V1 já implementada por Jerfesson? Há dependências entre eles que afetem sequenciamento? |
| L12 | Menção a ZMMR_GSI01 sem item de escopo correspondente | ZMMR_GSI01 aparece no cabeçalho/histórico do Work Request e no caminho de transações, mas nenhum dos 15 itens menciona GSI01 explicitamente. Há ajustes pendentes para GSI01 que não foram descritos no escopo desta demanda? |
| L13 | Data de elaboração do documento de escopo (Fonte 1) | Qual a data de criação/última revisão do documento "06005284_001_Melhorias_Monitor_WorkRequest_4918651_ATUAL.docx"? |
| L14 | Responsável designado pelo atendimento | O campo "Responsável" do chamado está como "Não Informado". Quem será o responsável técnico designado pela Projetos DTI para conduzir esta demanda? |

**Total de lacunas identificadas: 14**

---

## 5. Resumo para Confirmação

Prezada Tatiane,

Para darmos sequência ao processamento da demanda **DEM-2026-008** ("Ajustes nos Monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 — SAP ECC MM"), reunimos as informações recebidas via documento de escopo técnico (Work Request 4918651) e via chamado nº 6898567 (Business Desk).

**Confirmamos o entendimento de que:**
- A necessidade de negócio central é dar autonomia aos usuários de Contabilidade/Controle de Ativos para alterar e excluir processos nos monitores, tornando-os mais completos e ágeis para o fechamento mensal e o processo de criação/legalização de frota.
- O pedido específico compreende 15 itens de ajuste detalhados (ver tabela na Seção 3), envolvendo os monitores ZMMR_GSI02, GSI03 e GSI04, e telas/transações ME51N, ME52N, ME21N, ME22N, ZMMTR002, AS01, AS02.
- O benefício esperado declarado é "aumento de produtividade", com ganho qualitativo descrito como maior eficiência, agilidade e assertividade na criação de imobilizado de frota e entrada de notas fiscais.
- O investimento estimado é de até R$ 30.000, com indicação de que já está aprovado.

**Antes de prosseguirmos, precisamos de esclarecimentos sobre 14 pontos** (detalhados na Seção 4), com destaque para os seguintes itens críticos de governança:
1. **Não localizamos evidência documental de aprovação de Diretoria** da área solicitante. O arquivo nomeado "APROVAÇÃO - DIRETOR DA ÁREA.pdf" parece, pelo conteúdo, corresponder à aprovação da Gerente Contábil (Nubia), e não a um Diretor. Adicionalmente, o e-mail original de Tatiane menciona a necessidade de aprovação do "André", que não está documentada.
2. **A aprovação do Gerente de TI** está indicada por um "De acordo." de Raphael Leitão Sbardelotti, mas seu cargo formal não está confirmado nas fontes — solicitamos confirmação.
3. Há divergência entre a Prioridade "Baixa" do Work Request e a Criticidade "Alta"/SLA de 1 semana do chamado — qual deve prevalecer?

Aguardamos retorno para classificar formalmente esta demanda e dar sequência à etapa de qualificação.

---
---

# DEMANDA ESTRUTURADA — DEM-2026-008

## 1. Identificação

- **ID da Demanda:** DEM-2026-008
- **Título:** Ajustes nos Monitores ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 — SAP ECC Módulo MM
- **Data de Coleta:** 2026-06-10
- **Origem:** Chamado nº 6898567 (Business Desk Águia Branca) + Work Request 4918651 (documento de escopo técnico)
- **Sistema afetado:** SAP ECC, Módulo MM
- **Squad/Equipe sugerida:** SQUAD PM/MM (conforme Fonte 1)
- **Status de Governança:** **NÃO VALIDADA** — pendente confirmação de aprovação de Diretoria e de cargo formal do Gerente de TI (ver Seção "Demanda Coletada", item 2.6)

## 2. Solicitante

- **Nome:** Tatiane Dias de Moraes
- **Cargo:** Coordenadora de Controle de Ativos e Recebimento Fiscal (⚠️ ver inconsistência de cargo na Demanda Coletada, item 2.1)
- **Empresa/Divisão:** VIXPar / VIX Matriz — Contabilidade
- **E-mail:** Tatiane@vix.com.br
- **Matrícula:** 300513103
- **Co-solicitante / Provedor de Requisitos:** João Henrique (joaomerlo@vix.com.br) — papel não esclarecido (Lacuna L1)
- **Especialista técnico de referência:** Jerfesson Fernandes Helmer (jerfesson@aguiabranca.com.br)

## 3. Resumo da Demanda

Conjunto de 15 ajustes adaptativos nos monitores SAP ZMMR_GSI02, ZMMR_GSI03 e ZMMR_GSI04 (módulo MM), visando conceder autonomia aos usuários de Contabilidade/Controle de Ativos para alterar e excluir processos diretamente nos monitores, ampliar campos disponíveis (Classificação, Vencimento NF, CR, Data Liberação/aprovação, Tipo de Veículo, Grupo deprec., Nº RC), automatizar integrações (placa do veículo, MIRO, legalização de máquinas não emplacadas) e implementar lógica de estorno de fatura/pedido com atualização de status e log.

## 4. Necessidade de Negócio

Os usuários do setor de Contabilidade/Controle de Ativos (VIX/VIXPar) não possuem autonomia suficiente para corrigir e gerenciar processos nos monitores de requisição/pedido/imobilizado, o que compromete a agilidade do fechamento contábil mensal e do processo de criação e legalização de equipamentos de frota.

## 5. Resultado Esperado

- Maior autonomia dos usuários sobre os monitores (alteração e exclusão de processos).
- Monitores mais completos, com novos campos e parâmetros de busca.
- Automação de integrações entre PM/imobilizado (AS02) e os monitores GSI.
- Tratamento sistemático de estornos de fatura (MIRO) e pedido, com log de auditoria.
- Resultado declarado (Fonte 2): "Maior eficiência, agilidade e assertividade no processo de criação de imobilizado de frota e entrada de notas fiscais."
- **Indicador de sucesso:** NÃO INFORMADO — requer esclarecimento (Lacuna L9).

## 6. Contexto Estratégico

- Demanda classificada como "Melhoria" de sistemática ERP, sem necessidade de adequação legal/regulatória (Fonte 2: "Necessidade Legal/Obrigatório? Não").
- Não há, nas fontes, citação de CEO/Diretor/VP como origem ou justificativa de urgência — regra de governança 2 (`⚠️ CLAIM SEM EVIDÊNCIA`) **não aplicável** com base nas evidências disponíveis.
- Existe precedente: "Projeto semelhante já implantado no GAB? Sim — Monitores de requisição, pedido e imobilizado" (Fonte 2). Possível relação com a V1 já entregue por Jerfesson Fernandes Helmer (Fonte 1) — relação não confirmada (Lacuna L11).
- Não há impacto declarado em outras áreas/divisões de negócio, nem necessidade declarada de integração com sistemas externos (Fonte 2).

## 7. Estimativas Preliminares

- **Investimento esperado:** Até R$ 30.000 (Fonte 2)
- **Investimento aprovado:** Sim, segundo formulário do chamado — evidência documental específica NÃO INFORMADA (Lacuna L6)
- **Prazo do chamado (SLA):** 1 semana (09/06/2026 a 16/06/2026), Criticidade "2 - Alta" (Fonte 2)
- **Prioridade declarada no Work Request:** Baixa (Fonte 1)
- ⚠️ **INCONSISTÊNCIA entre Prioridade (Baixa) e SLA/Criticidade (Alta, 1 semana)** — requer esclarecimento (Lacuna L7) antes de qualquer estimativa de cronograma de execução.

## 8. Premissas

- Premissa 1: os 15 itens do escopo (Fonte 1) representam o conjunto completo e atual da solicitação técnica, conforme aprovado pelos "usuários-chave" mencionados no campo "Solução Proposta".
- Premissa 2: o documento de escopo (Fonte 1) já passou por uma rodada de alinhamento com usuários-chave antes do encaminhamento ao chamado 6898567, embora a data desse alinhamento não esteja explícita (Lacuna L13).
- Premissa 3: o monitor ZMMR_GSI01, citado no cabeçalho/histórico, não requer ajustes adicionais nesta demanda, salvo indicação contrária do Solicitante (Lacuna L12).
- Premissa 4: "Tatiane e João Henrique" (Fonte 1) representam, em conjunto, o Solicitante/Provedor de Requisitos desta demanda, ainda que o chamado 6898567 (Fonte 2) registre apenas Tatiane como Solicitante/Beneficiado formal.

## 9. Restrições

- Restrição 1 (Item 12 do escopo): alteração de XML incorreto no GSI03 só é permitida se a etapa de PM não estiver legalizada nem o equipamento criado.
- Restrição 2 (Item 13 do escopo): não é possível estornar pedido se houver MIRO ativa; o estorno deve seguir obrigatoriamente a ordem fatura → pedido.
- Restrição 3 (Item 10 do escopo): atualmente, a alteração do campo "Tipo de Veículo" só é permitida antes da criação do pedido — a demanda solicita flexibilizar essa restrição existente, propagando a alteração para GSI02, GSI03 e GSI04.
- Restrição 4 (organizacional): a demanda não pode ser considerada "VALIDADA" pelo VMO sem as duas aprovações exigidas pela governança (Diretoria + Gerente de TI), atualmente não comprovadas (ver Seção "Demanda Coletada", item 2.6).
- Restrição 5 (orçamentária): teto de investimento de até R$ 30.000 (Fonte 2), sem detalhamento de como esse valor foi estimado frente aos 15 itens de escopo.

## 10. Lacunas para Resolução

Ver tabela consolidada de 14 lacunas na Seção "Demanda Coletada", item 4 (L1 a L14). Lacunas críticas para avanço imediato:
- **L4 e L5** (governança — aprovação de Diretoria / inconsistência de arquivo "APROVAÇÃO - DIRETOR DA ÁREA.pdf")
- **L3** (cargo formal do Gerente de TI)
- **L7** (priorização — Baixa vs. Alta/SLA 1 semana)
- **L10 e L12** (esclarecimentos técnicos de escopo — item 6 GSI03/GSI04 e menção a GSI01)

## 11. Resumo para Confirmação pelo Solicitante

A demanda DEM-2026-008 foi estruturada a partir do Work Request 4918651 e do chamado 6898567. O escopo compreende 15 itens de ajuste nos monitores ZMMR_GSI02/03/04 (SAP MM), com investimento estimado de até R$ 30.000 e prazo de SLA de 1 semana (a confirmar dada a divergência com a prioridade "Baixa" declarada).

**Pendência crítica:** a demanda não atende, no momento, aos critérios de governança do VMO (aprovação de Diretoria + Gerente de TI confirmadas formalmente). Solicitamos à Tatiane Dias de Moraes:
1. Confirmação/obtenção da aprovação formal de um Diretor da área solicitante (incluindo a aprovação de "André" mencionada no e-mail de 06/03/2026, ou esclarecimento de que ela não é mais necessária).
2. Confirmação do cargo formal de Raphael Leitão Sbardelotti como Gerente de TI da divisão.
3. Esclarecimento sobre a inconsistência do arquivo "APROVAÇÃO - DIRETOR DA ÁREA.pdf".
4. Resposta às demais 11 lacunas listadas na Seção 4 da Demanda Coletada, especialmente quanto à priorização (Baixa vs. Alta/SLA) e ao indicador de sucesso do projeto.

Somente após a resolução dessas pendências o VMO poderá classificar formalmente esta demanda como **VALIDADA** e avançar para a etapa de priorização e planejamento.
