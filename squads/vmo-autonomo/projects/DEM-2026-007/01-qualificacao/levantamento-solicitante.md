# Questionário de Levantamento — DEM-2026-007
**Ticket #6700943 — Importação Automática DDA no SAP (VAB Matriz)**
**Projeto: Controladoria do Futuro**
Data de envio: 2026-05-20
Destinatários: Lucas Medeiros Pereira / Noemia Tambara Cardoso Malini (VAB Matriz)

---

A demanda foi qualificada como **Melhoria Evolutiva — APROVADA COM CONDIÇÕES**.
Aprovações gerenciais já obtidas: Gladston Campos (08/04) e Walace Bacelar (06/05).
Para iniciar o levantamento técnico, precisamos das informações abaixo. Por favor,
responda até **27/05/2026**.

---

## Bloco 1 — Processo Atual

**1.1** Como é feito hoje o pagamento de boletos que chegam sem DDA?
Descreva o passo a passo: quem imprime, quem digitaliza o código, quem lança no SAP.

**1.2** Qual o volume médio de boletos processados por mês na VAB Matriz?
_(ex: 150 boletos/mês, sendo 80 de fornecedores e 70 de tributos)_

**1.3** Qual o tempo médio gasto por colaborador nesse processo manual por semana?
_(ex: ~2 horas/semana somando toda a equipe)_

**1.4** Com que frequência ocorre o problema de boleto "não anexado na hora do pagamento"?
_(ex: ~3 vezes por semana, gerando X minutos de atraso ou renegociação)_

---

## Bloco 2 — Escopo da Solução

**2.1** Quais tipos de DDA devem ser contemplados nesta primeira entrega?
- [ ] Boletos de fornecedores (contas a pagar)
- [ ] Tributos e impostos
- [ ] Concessionárias (energia, água, telecomunicações)
- [ ] Outros — especificar: _______________

**2.2** Qual banco(s) emite(m) os boletos que precisam ser recebidos via DDA?
_(A integração atual mapeada é SAP x Santander — há outros bancos envolvidos?)_

**2.3** A conta bancária Santander da VAB Matriz já está cadastrada e habilitada para
receber DDA eletronicamente? Já foi verificado com o gerente de relacionamento do banco?

**2.4** No SAP da VAB Matriz, o módulo FI (Contas a Pagar) está ativo e em uso regular?
Há alguma particularidade de customização que diferencie da Divisão Logística?

---

## Bloco 3 — Referência Interna (Divisão Logística)

**3.1** Você sabe quem foi o responsável técnico pela implantação do DDA na Divisão Logística?
_(nome + contato, se possível — para reaproveitar a configuração)_

**3.2** A Divisão Logística usa exatamente o mesmo banco (Santander) e o mesmo ambiente SAP
(GAB)? Ou há diferenças de ambiente ou banco que precisam ser mapeadas?

**3.3** Você tem acesso à documentação daquela implantação (especificação técnica, layout
do arquivo CNAB, configuração SAP)? Se sim, por favor compartilhe — isso reduz
significativamente o esforço de desenvolvimento.

---

## Bloco 4 — Aprovação e Governança

**4.1** O orçamento estimado (< R$10.000, CC 200195148) já foi submetido para aprovação?
Se não, qual é o processo e quem deve aprovar?

**4.2** Quem é o sponsor desta iniciativa — isto é, o responsável por autorizar formalmente
o início e validar a entrega? (Idealmente um gestor de nível coordenação ou superior)

**4.3** Há algum prazo específico para que esta melhoria entre em produção?
_(ex: antes do fechamento do mês de julho, antes de evento específico)_

---

## Bloco 5 — Impacto e Validação

**5.1** Quem valida a entrega no lado do negócio? Qual seria o critério de aceite —
como você vai saber que a solução está funcionando corretamente?
_(ex: "os boletos aparecem automaticamente no SAP dentro de X horas após emissão pelo banco")_

**5.2** Há alguma restrição de horário para processar o arquivo DDA?
_(ex: precisa estar disponível até as 9h para o processamento do dia)_

---

**Envie suas respostas para:** Projetos DTI (ticket #6700943) ou diretamente ao responsável designado.

Dúvidas: entre em contato com o Grupo Solucionador Projetos DTI.

---
_Documento gerado pelo VMO Autônomo | DEM-2026-007 | 2026-05-20_
