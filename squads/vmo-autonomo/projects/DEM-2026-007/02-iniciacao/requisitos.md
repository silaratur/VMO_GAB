# Especificação de Requisitos Funcionais (ERF)
Projeto: DEM-2026-007 — Implantação DDA SAP — VAB Matriz
Elaborado por: Rafael Requisito (VMO Autônomo)
Data: 2026-05-20
Versão: 1.0

> **Nota CB-2:** Esta ERF levanta os requisitos conhecidos com base na demanda e no precedente da
> Divisão Logística. Os requisitos marcados com [CB-2] dependem de confirmação técnica no
> levantamento junto ao DTI — podem ser refinados sem implicar nova qualificação.

---

## Resumo MoSCoW

| Prioridade | Qtd RF | Qtd RNF |
|-----------|--------|---------|
| Must Have | 5 | 4 |
| Should Have | 3 | 1 |
| Could Have | 2 | 0 |
| Won't Have | 2 | 0 |
| **Total** | **12** | **5** |

---

## Glossário

| Termo | Definição |
|-------|-----------|
| DDA | Débito Direto Autorizado — serviço bancário que permite ao favorecido (credor) enviar eletronicamente os dados do boleto diretamente ao banco do pagador, eliminando a necessidade de envio físico do boleto |
| Boleto | Documento de cobrança bancária com código de barras e dados de pagamento |
| CNAB 240 | Padrão de arquivo de troca de dados bancários com 240 posições por linha (norma FEBRABAN) |
| FEBAN | Módulo SAP de interface bancária (Financial Electronic Banking), responsável pelo processamento de arquivos CNAB |
| CP | Contas a Pagar — área responsável pelo processamento e pagamento de boletos na VAB Matriz |
| SAP FI | Módulo de Financeiro do SAP, onde são processados os pagamentos |
| Arquivo de Retorno DDA | Arquivo CNAB 240 enviado pelo Santander contendo os boletos disponíveis para pagamento via DDA |
| Habilitação DDA | Processo de cadastro junto ao banco para receber boletos eletronicamente via DDA |

---

## Requisitos Funcionais

### RF001 — Recepção automática de arquivo DDA do Santander
**Prioridade:** Must Have
**Origem:** Demanda principal (Ticket #6700943) + E-mail Noemia
**Descrição:** O sistema deve receber e processar automaticamente o arquivo CNAB 240 com os
boletos disponíveis via DDA enviados pelo Santander para a conta da VAB Matriz.
**Critério de aceitação:** Dado que o Santander envia um arquivo DDA em D, o SAP deve ter
processado automaticamente o arquivo e disponibilizado os boletos para pagamento em D+0
(mesmo dia útil) ou no máximo em D+1 às 08h00.
**[CB-2]:** Mecanismo de recepção (FTP, SFTP, API ou outro) a confirmar com DTI.

---

### RF002 — Importação automática de boletos no SAP FI
**Prioridade:** Must Have
**Origem:** Demanda principal + precedente Div. Logística
**Descrição:** O sistema deve importar automaticamente os dados dos boletos DDA recebidos
(valor, data de vencimento, cedente, código de barras) para o SAP FI, sem necessidade de
digitação manual por parte do usuário.
**Critério de aceitação:** Dado um arquivo DDA recebido com N boletos, o SAP deve registrar
N documentos de previsão de pagamento no FI, com zero digitação manual pelo usuário.

---

### RF003 — Visualização de boletos DDA no SAP FI
**Prioridade:** Must Have
**Origem:** Necessidade operacional equipe CP
**Descrição:** O usuário de CP deve poder visualizar no SAP FI os boletos disponíveis via DDA,
com dados completos (cedente, valor, vencimento, código de barras) antes de efetuar o pagamento.
**Critério de aceitação:** O usuário de CP consegue, em no máximo 3 cliques a partir da tela
principal do SAP FI, visualizar a lista de boletos DDA com todos os dados relevantes.

---

### RF004 — Processamento de pagamento de boleto DDA no SAP
**Prioridade:** Must Have
**Origem:** Fluxo operacional CP
**Descrição:** O usuário de CP deve poder executar o pagamento de um boleto DDA diretamente
no SAP FI sem precisar digitar o código de barras — o sistema deve utilizar os dados
importados automaticamente via DDA.
**Critério de aceitação:** O usuário de CP consegue efetuar o pagamento de um boleto DDA
importado sem digitar nenhum dado manualmente; o pagamento é processado com os dados do DDA.

---

### RF005 — Confirmação de recepção e importação DDA
**Prioridade:** Must Have
**Origem:** Governança de processo financeiro
**Descrição:** O sistema deve registrar log de cada arquivo DDA recebido e processado,
indicando data/hora de recepção, quantidade de boletos, status de importação (sucesso/erro)
e identificação do arquivo.
**Critério de aceitação:** Para cada arquivo DDA processado, existe um registro de log acessível
ao usuário de CP/supervisor com: data/hora, qtd boletos, status (sucesso ou erro com descrição).

---

### RF006 — Notificação de boletos DDA disponíveis
**Prioridade:** Should Have
**Origem:** Melhoria de processo operacional
**Descrição:** O sistema deve notificar os usuários de CP quando novos boletos DDA forem
importados com sucesso, informando quantidade e valor total disponível para pagamento.
**Critério de aceitação:** O usuário de CP recebe notificação (e-mail ou alerta SAP) em até
30 minutos após a importação bem-sucedida do arquivo DDA.

---

### RF007 — Rejeição e log de boletos DDA com erro
**Prioridade:** Should Have
**Origem:** Controle de qualidade de dados financeiros
**Descrição:** O sistema deve identificar e registrar boletos DDA com dados inválidos ou
incompletos, isolando-os do fluxo normal e notificando o usuário responsável.
**Critério de aceitação:** Boleto com dados inválidos (formato CNAB incorreto, vencimento
no passado) é isolado com mensagem de erro descritiva; não impede processamento dos demais.

---

### RF008 — Consulta histórica de boletos DDA
**Prioridade:** Should Have
**Origem:** Controle e auditoria do processo CP
**Descrição:** O usuário deve poder consultar no SAP FI o histórico de boletos DDA recebidos,
pagos e pendentes por período.
**Critério de aceitação:** O usuário consegue consultar boletos DDA por período (início/fim),
cedente e status (recebido / pago / pendente / com erro) em no máximo 5 segundos de resposta.

---

### RF009 — Configuração de conta corrente VAB para DDA
**Prioridade:** Could Have
**Origem:** Necessidade técnica [CB-2]
**Descrição:** O sistema deve permitir configurar qual(is) conta(s) corrente(s) Santander
da VAB Matriz está habilitada para receber DDA, com possibilidade de adicionar ou desabilitar
contas sem necessidade de intervenção técnica.
**[CB-2]:** A ser confirmado se necessário como RF Must Have após levantamento técnico.

---

### RF010 — Reprocessamento manual de arquivo DDA com falha
**Prioridade:** Could Have
**Origem:** Recuperação de falhas operacionais
**Descrição:** O usuário técnico (DTI) deve poder reprocessar manualmente um arquivo DDA
que falhou na importação automática, sem necessidade de novo envio pelo Santander.
**Critério de aceitação:** O usuário DTI consegue reprocessar um arquivo DDA falhado em
no máximo 5 minutos de operação; o resultado do reprocessamento é registrado no log.

---

### RF-WONT-01 — Integração com outros bancos além do Santander
**Prioridade:** Won't Have (esta versão)
**Motivo:** Fora do escopo declarado. Santander é o único banco desta implementação.

### RF-WONT-02 — Emissão de boletos pela VAB Matriz via DDA
**Prioridade:** Won't Have
**Motivo:** Fora do escopo. Esta implementação é apenas para recepção/pagamento de boletos
de terceiros, não emissão de boletos pela VAB.

---

## Requisitos Não-Funcionais

### RNF001 — Disponibilidade
**Prioridade:** Must Have
**Descrição:** O processo de recepção e importação DDA deve estar disponível durante o
horário bancário (08h00 às 18h00, dias úteis).
**Critério de aceitação:** Disponibilidade ≥ 99,5% no horário bancário. Manutenção
programada apenas fora do horário bancário.

---

### RNF002 — Performance
**Prioridade:** Must Have
**Descrição:** O arquivo DDA recebido do Santander deve ser processado e os boletos
disponibilizados no SAP FI em tempo operacionalmente útil.
**Critério de aceitação:** Processamento completo de arquivo DDA com até 500 boletos
em ≤ 30 minutos da disponibilização do arquivo pelo Santander.

---

### RNF003 — Segurança
**Prioridade:** Must Have
**Descrição:** A transmissão de dados financeiros entre Santander e SAP deve ser protegida.
**Critério de aceitação:** Transmissão de arquivo DDA via protocolo seguro (SFTP ou equivalente
aprovado pelo Grupo); dados não trafegam em texto simples; acesso à funcionalidade DDA restrito
a perfis de usuário CP e DTI FI definidos no SAP.

---

### RNF004 — Compatibilidade
**Prioridade:** Must Have
**Descrição:** A solução deve ser compatível com a versão SAP em produção na VAB Matriz e
com o padrão CNAB 240 do Santander.
**Critério de aceitação:** A solução funciona sem upgrade de versão SAP; arquivo CNAB 240
Santander processado corretamente (validar com layouts disponíveis na Div. Logística). [CB-2]

---

### RNF005 — Rastreabilidade
**Prioridade:** Should Have
**Descrição:** Cada pagamento realizado via DDA deve ser rastreável ao arquivo DDA de origem.
**Critério de aceitação:** Para qualquer pagamento FI realizado via DDA, é possível identificar
o arquivo DDA de origem, data de recepção e dados do boleto original.

---

## Rastreabilidade

| ID Requisito | Origem | Critério de Sucesso TAP |
|-------------|--------|------------------------|
| RF001, RF002 | Ticket #6700943 + E-mail Noemia | CS-1 (recepção automática 100%) |
| RF003, RF004 | Necessidade operacional CP | CS-1 + CS-2 (zero dependência terceiros) |
| RF005, RF007 | Controle processo financeiro | CS-1 (qualidade importação) |
| RF006 | Melhoria operacional | CS-3 (satisfação ≥ 8/10) |
| RF008 | Auditoria CP | CS-2 (rastreabilidade) |
| RNF001–004 | Padrões técnicos Grupo | CS-4 (go-live 30/09/2026) |

---

## Aprovação da ERF

> Esta ERF está em rascunho e deve ser validada por Noemia Tambara Cardoso Malini
> (coordenadora do processo) e pelo recurso técnico DTI designado após o gate de kick-off.
> A validação consiste em: (1) confirmação de que os Must Haves cobrem a necessidade; (2)
> confirmação dos critérios de aceitação; (3) refinamento dos itens marcados com [CB-2].

| Papel | Nome | Validação | Data |
|-------|------|----------|------|
| Coordenadora processo | Noemia Tambara Cardoso Malini | __________ | ______ |
| Recurso técnico DTI | A designar | __________ | ______ |
| VMO | — | __________ | ______ |
