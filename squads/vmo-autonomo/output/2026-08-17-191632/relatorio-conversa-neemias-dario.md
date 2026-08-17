# Relatório Completo da Conversa — Discovery Demandas

**Reunião:** Discovery Demandas - Dario Demanda <> Neemias Buceli
**Data:** 17/08/2026 — 18:56 UTC
**Duração:** ~11 minutos
**Participantes:** Neemias Buceli (Solicitante — Time Data AI) | Dário (Agente Discovery)
**Link do Transcript:** https://app.fireflies.ai/view/01M08HA35T9P10W3SYTH94MTRH
**Status:** Processado

---

## 1. Contexto e Objetivo

Neemias Buceli, do time de **Data AI** do Grupo Águia Branca, solicitou a elaboração de um **estudo de viabilidade** para avaliar três soluções de **agentes multiagentes com capacidade de resposta por voz (Voice Mode)**.

O objetivo é documentar prós e contras de cada caminho, incluindo uma recomendação, **sem entrar em detalhes de implementação**.

---

## 2. As Três Soluções Avaliadas

### Solução 1 — Fireflies (Voice Mode atual)
| Aspecto | Detalhe |
|---|---|
| **Status** | Funcional, operando atualmente |
| **Homologação** | Não homologada na organização |
| **Risco** | Custo desconhecido para deploy interno; falta de governança corporativa |
| **Vantagem** | Já funciona com voice mode completo |

### Solução 2 — Microsoft Teams + Copilot Studio
| Aspecto | Detalhe |
|---|---|
| **Status** | Toggle de voice calling habilitado, mas funcionalidade ainda em desenvolvimento |
| **Homologação** | Homologada pela organização |
| **Risco** | Prazo incerto (estimativa de 1 a 3 meses para disponibilidade de voz) |
| **Vantagem** | Governança Microsoft integrada; solução multiagente já operando em modo texto; publicação automática no Teams |

### Solução 3 — Azure Telefonia (Central Azure)
| Aspecto | Detalhe |
|---|---|
| **Status** | Disponível, requer habilitação de número telefônico |
| **Homologação** | Homologada pela organização |
| **Risco** | Escopo restrito a call center; processo de implementação mais complexo |
| **Vantagem** | Protocolos de segurança específicos para voz; adequada para atendimento ao cliente |

---

## 3. Requisito Fundamental

> A solução escolhida **deve ter capacidade de integrar modalidade de voz** (resposta por áudio), independentemente do caminho tecnológico adotado.

- **Público-alvo:** Toda a organização, com foco inicial na área de **Sistemas ERP**
- **Modalidade:** Resposta por áudio (não apenas interação por texto)

---

## 4. Critérios de Avaliação Definidos

| # | Critério |
|---|---|
| 1 | Custo |
| 2 | Prazo |
| 3 | Capacidades Técnicas |
| 4 | Governança |
| 5 | Risco |
| 6 | Segurança |
| 7 | Conformidade legal (LGPD e políticas internas) |

---

## 5. Stakeholders e Responsabilidades

| Papel | Responsável | Ação |
|---|---|---|
| **Solicitante** | Neemias Buceli (Data AI) | Fornecer informações e validar estudo |
| **Avaliação técnica / Timeline** | Time de Sistemas ERP | Definir prazos e avaliar implementação |
| **Áreas envolvidas** | Call Center, ITeam | Participar da decisão futura |

---

## 6. Action Items

| Responsável | Ação | Prazo |
|---|---|---|
| Neemias Buceli | Fornecer todas as informações relevantes para o estudo | Imediato |
| Agente (Pipeline VMO) | Estruturar estudo de viabilidade comparando as 3 soluções com foco em custo, prazo, capacidade técnica, governança, risco, segurança e conformidade | **18/08/2026 (amanhã)** |
| Agente (Pipeline VMO) | Incluir variáveis de custo e operacional relevantes para cada solução | **18/08/2026 (amanhã)** |

---

## 7. Decisões e Restrições

- O estudo **pode incluir uma recomendação**, mas **não deve detalhar implementação**
- **Orçamento de implementação** não é foco neste momento
- O **prazo é urgente**: entrega para o dia seguinte (18/08/2026)
- Timeline de implementação deve ser consultado com o **time de Sistemas ERP**

---

## 8. Análise Estratégica Preliminar

### Governança e Compliance
- **Microsoft Teams** oferece a melhor governança integrada, alinhada às políticas internas
- **Fireflies** apresenta riscos significativos por falta de homologação — potencial problema em governança e compliance
- **Azure Telefonia** possui governança adequada, mas limitada ao contexto de call center

### Viabilidade Técnica
- **Fireflies** é a única solução com voice mode totalmente funcional hoje
- **Microsoft Teams** está mais perto da solução ideal (homologado + governança), mas a funcionalidade de voz tem prazo incerto
- **Azure Telefonia** é viável tecnicamente, porém com escopo restrito

### Impacto Organizacional
- A solução deve atender toda a organização (não apenas call center)
- A escolha impacta diretamente a experiência do usuário final
- A decisão posiciona o Grupo Águia Branca na adoção de soluções inteligentes

---

## 9. Palavras-chave

`Solução multiagentes` · `Voice Mode` · `Estudo de viabilidade` · `Microsoft Teams` · `Fireflies` · `Azure Telefonia` · `Copilot Studio` · `LGPD` · `Governança` · `Sistemas ERP`

---

## 10. Transcript Completo

<details>
<summary>Clique para expandir o transcript completo</summary>

```
[00:00 - 00:02] Agent: Neemias Buceli, obrigado por participar.
[00:02 - 00:03] Agent: Como você está hoje?
[00:04 - 00:06] Neemias Buceli: Olá Adário, estou bem.
[00:07 - 00:08] Agent: Ótimo, então vamos começar.
[00:09 - 00:13] Agent: Conte comigo qual é a necessidade ou oportunidade que motivou esta solicitação?
[00:14 - 00:46] Neemias Buceli: Estamos definindo uma decisão onde temos uma solução antigênica funcionando que não está homologada dentro da empresa e funciona muito bem ali usando o ViceMode via Fireflies, mas temos uma solução dentro que é homologada pela própria Microsoft, onde a gente consegue ter as soluções multiagênticas funcionando e homologada e com a governança da Microsoft dentro do Copilot Studio.
[00:46 - 01:12] Neemias Buceli: E conseguimos fazer com que a solução seja autopublicada no team, se interage, enfim, só não tem a funcionalidade de voz ainda, mas já tem o toggle de voz calling a neighbor, mas quando interajo e faço a solicitação via call do agente, ele retorna, o bot retorna, dizendo que you're working on it, basicamente eles estão trabalhando na solução.
[01:12 - 01:20] Neemias Buceli: E tem uma outra solução que é ir por um caminho de telefonia, mas aí teria que ir dentro do Central da Azure, habilitar um número, enfim.
[01:20 - 01:28] Neemias Buceli: Então tem esses três caminhos, gostaria que você elaborasse uma documentação estruturada para definir esses três caminhos.
[01:30 - 01:30] Agent: Entendi.
[01:30 - 01:37] Agent: Você tem três caminhos possíveis para uma solução de agentes e quer a documentação estruturada para avaliar cada um deles.
[01:37 - 01:40] Agent: Deixa eu ter certeza que estou compreendendo o cenário de forma correta.
[01:40 - 01:45] Agent: Você está falando de um estudo de viabilidade para definir qual dessas três abordagens seguir, certo?
[01:45 - 01:49] Agent: Ou já existe uma decisão tomada e você quer documentar cada caminho para...
[01:49 - 01:49] Neemias Buceli: Isso aí.
[01:49 - 01:51] Neemias Buceli: Estudo de viabilidade.
[01:52 - 01:52] Agent: Perfeito.
[01:53 - 01:56] Agent: Então é um estudo de viabilidade para escolher entre os três caminhos.
[01:56 - 01:57] Agent: Deixa eu entender melhor o contexto.
[01:58 - 02:02] Agent: Qual é o problema de negócio que essas soluções de agentes estão tentando resolver?
[02:02 - 02:05] Agent: O que hoje não funciona bem ou o que vocês precisam melhorar?
[02:06 - 02:08] Neemias Buceli: Eu já te contextualizei.
[02:08 - 02:10] Neemias Buceli: Que é fazer um...
[02:10 - 02:17] Neemias Buceli: Que é para fazer o scratch de um sistema multiagente, independente de uma solução X, Y ou Z.
[02:17 - 02:23] Neemias Buceli: Enfim, o objetivo é definir a funcionalidade de voice mode.
[02:24 - 02:26] Agent: Pode continuar, estou te ouvindo.
[02:27 - 02:27] Neemias Buceli: Terminei.
[02:29 - 02:38] Agent: Certo, então o objetivo é definir a funcionalidade de qual seria essa funcionalidade, qual capacidade ou serviço você quer que esse sistema multiagente entregue.
[02:40 - 02:45] Neemias Buceli: Eu já te contextualizei, não é necessariamente uma solução X ou Y.
[02:46 - 02:53] Neemias Buceli: Independente da solução agêntica, ela tem que ter possibilidade de ter a copulação da feature de modalidade de voz.
[02:55 - 02:56] Agent: Ah, entendi agora.
[02:56 - 03:05] Agent: Então o requisito fundamental é que a solução escolhida tenha a capacidade de integrar modalidade de voz, seja qual for o caminho que vocês seguirem.
[03:06 - 03:07] Agent: Deixa eu voltar um passo então.
[03:07 - 03:16] Agent: Quando você fala em modalidade de voz, isso é para que os usuários interajam com esses agentes por telefone ou é para que os agentes respondam com áudio também dentro do Teams ou de outro canal?
[03:17 - 03:18] Neemias Buceli: Respondam com áudio.
[03:19 - 03:20] Agent: Certo.
[03:20 - 03:23] Agent: Então a capacidade de responder com áudio é essencial.
[03:23 - 03:26] Agent: E quem seriam os usuários finais dessa solução?
[03:26 - 03:32] Agent: Quais áreas ou públicos dentro do Grupo Águia Branca usariam esses agentes multiagentes com modalidade de voz?
[03:32 - 03:36] Neemias Buceli: Toda a organização a priori a área de sistemática RP.
[03:38 - 03:43] Agent: Gotia, então é para toda a organização com foco inicial na área de sistemas e IRP.
[03:43 - 03:44] Agent: E como funciona hoje?
[03:44 - 03:50] Agent: Como essas áreas lidam com as demandas ou processos que esses agentes viriam automatizar ou facilitar?
[03:51 - 03:55] Neemias Buceli: Não faz parte do seu escopo nesse momento.
[03:55 - 04:05] Neemias Buceli: O objetivo é fazer a viabilidade de prós e contras desses três caminhos que eu te apresentei.
[04:07 - 04:20] Agent: Então, o foco principal é mesmo fazer a viabilidade, documentar os prós e contras dos três caminhos que você mencionou, a solução via Fireflies, a solução homologada Microsoft com Teams e o caminho via Telefonia com Azure.
[04:20 - 04:23] Agent: Antes de estruturar essa viabilidade, deixa eu entender melhor.
[04:23 - 04:28] Agent: Qual desses três caminhos você e seu time acreditam ser o mais viável tecnicamente?
[04:28 - 04:31] Agent: Ou todos estão no mesmo patamar de incerteza?
[04:33 - 04:50] Neemias Buceli: O caminho do Fireflies ao problema de não ser homologado e teria que ter um estudo de viabilidade de custo dessa solução deployada dentro da organização.
[04:51 - 05:04] Neemias Buceli: Na solução da Microsoft via Teams já existe o toggle enabled ali para soluções agênticas, mas ainda não está funcionando, provavelmente daqui um mês, dois, três meses, enfim, não tem uma definição.
[05:04 - 05:16] Neemias Buceli: E para a solução da Azure de telefonia ali seria para um público em específico que já começaria a trabalhar ali pensando em call center indo para esse escopo.
[05:18 - 05:19] Agent: Ótimo, isso clareia bastante.
[05:20 - 05:22] Agent: Então você tem três cenários bem distintos.
[05:22 - 05:30] Agent: Fireflies, não homologado, precisa de estudo de custo Microsoft Teams, homologado, mas funcionalidade ainda em desenvolvimento, prazo incerto.
[05:30 - 05:34] Agent: Azul e Telefonia, homologado, mas direcionado para Call Center.
[05:34 - 05:44] Agent: Para estruturar bem essa viabilidade, preciso entender qual é o timeline que vocês têm em mente, ou seja, em quanto tempo vocês precisam dessa solução de agentes multiagentes com voz operacional.
[05:45 - 05:56] Neemias Buceli: Esse tipo de solução você pode redirecionar ali para o time de sistemática ERP que vai conseguir responder melhor o deadline.
[05:57 - 05:58] Agent: Entendido.
[05:58 - 06:01] Agent: Então o time de sistemas ERP é quem tem a visão do timeline.
[06:01 - 06:04] Agent: Deixa eu confirmar então quem mais precisa estar envolvido nessa decisão.
[06:05 - 06:14] Agent: Além do time de sistemas ERP, existem outras áreas ou pessoas que precisam aprovar ou patrocinar esse estudo de viabilidade como seu solicitante formal dessa demanda.
[06:25 - 06:34] Agent: Perfeito, então além do time de sistemas ERP, o Call Center e o ITeam também precisam estar envolvidos.
[06:34 - 06:36] Neemias Buceli: E você qual é seu papel nessa solicitação?
[06:37 - 06:43] Agent: Certo, então você está solicitando isso em nome do Call Center e do ITeam ou você faz parte desse time?
[06:47 - 06:50] Agent: Desculpa, não consegui entender bem.
[06:51 - 06:52] Agent: Você faz parte do time de Data AI?
[06:55 - 06:59] Agent: Ótimo, então você é do time de Data e Air e está trazendo essa solicitação.
[06:59 - 07:04] Agent: E além de você, o time de sistemas ERP também será responsável por avaliar e implementar isso, certo?
[07:04 - 07:08] Agent: Existe um sponsor ou gestor que precisa aprovar essa viabilidade?
[07:10 - 07:17] Neemias Buceli: A priori, você só precisa trazer essa documentação de viabilidade.
[07:18 - 07:20] Neemias Buceli: Não precisa definir implementação nada.
[07:20 - 07:22] Neemias Buceli: Trazer um estudo de viabilidade.
[07:23 - 07:24] Agent: Perfeito, entendi.
[07:24 - 07:32] Agent: O escopo é apenas o estudo de viabilidade, documentar os prós e contras dos três caminhos, sem chegar a uma recomendação de implementação.
[07:32 - 07:33] Agent: Agora, para estruturar bem esse estudo...
[07:33 - 07:34] Agent: Estudo.
[07:34 - 07:41] Neemias Buceli: De viabilidade, você pode recomendar um caminho, mas não necessariamente você precisa trazer a implementação.
[07:42 - 07:43] Agent: Entendi.
[07:43 - 07:48] Agent: Então, o estudo de viabilidade pode incluir uma recomendação, mas sem entrar em detalhes de implementação.
[07:49 - 07:54] Agent: Voltando à pergunta, quais critérios vocês querem que eu avalie ao comparar esses três caminhos?
[07:54 - 07:56] Agent: O que é mais relevante para a decisão?
[07:57 - 07:59] Agent: Custo, prazo, capacidades técnicas, governança risco?
[08:00 - 08:02] Neemias Buceli: Todos esses que você trouxe.
[08:03 - 08:09] Agent: Perfeito, então, eu vou avaliar custo, prazo, capacidades técnicas, governança e risco para cada um dos três caminhos.
[08:10 - 08:11] Agent: Uma última coisa antes de ir finalizar...
[08:17 - 08:19] Agent: Ótimo, segurança entra na avaliação também.
[08:19 - 08:24] Agent: Então vou considerar custo-prazo, capacidades técnicas, governança, risco e segurança.
[08:24 - 08:29] Agent: E sobre requisitos legais ou contratuais, não existe algo específico que eu deva levar em conta?
[08:29 - 08:34] Agent: Conformidade de dados, LGPD ou políticas internas que impactam essa solução?
[08:35 - 08:37] Neemias Buceli: Sim, esses itens que você trouxe.
[08:39 - 08:39] Agent: Entendi.
[08:40 - 08:45] Agent: Então vou considerar a conformidade, LGPD e políticas internas como parte da avaliação de requisitos legais.
[08:45 - 08:48] Agent: Deixa eu fazer um resumo do que entendi para ter certeza que está tudo certo.
[08:49 - 08:55] Agent: Você precisa de um estudo de viabilidade para avaliar três caminhos de solução multiagente com capacidade de voz.
[08:55 - 09:04] Agent: Fireflies, não homologado, Microsoft Teams, homologado, funcionalidade em desenvolvimento, e Azure Telefonia, homologado, direcionado ao call center.
[09:05 - 09:12] Agent: O estudo deve analisar custo, prazo, capacidades técnicas, governança, risco e segurança, incluindo requisitos legais e conformidade.
[09:12 - 09:18] Agent: O objetivo é documentar prós e contras e, se possível, trazer uma recomendação, mas sem detalhar em implementação.
[09:18 - 09:23] Agent: Isso representa corretamente sua necessidade ou existe algo importante que você gostaria de complementar?
[09:24 - 09:24] Neemias Buceli: Sim, recomendo.
[09:25 - 09:25] Neemias Buceli: Exatamente.
[09:29 - 09:30] Neemias Buceli: É minha necessidade.
[09:31 - 09:36] Agent: Perfeito, então esse resumo representa sua necessidade.
[09:36 - 09:41] Agent: Uma última coisa, você tem algum prazo em mente para quando esse estudo de viabilidade precisa estar pronto?
[09:42 - 09:43] Neemias Buceli: Preciso para amanhã.
[09:44 - 09:45] Agent: Amanhã, certo.
[09:45 - 09:46] Agent: Isso é bem apertado.
[09:46 - 09:52] Agent: E em relação ao orçamento, existe alguma aprovação ou expectativa de investimento para esse estudo de viabilidade?
[10:03 - 10:06] Neemias Buceli: A priori, só traz o estudo de viabilidade.
[10:08 - 10:14] Agent: Então, o foco é entregar o estudo de viabilidade em si, sem preocupação com o orçamento de implementação neste momento.
[10:17 - 10:20] Neemias Buceli: Você traz eventuais variáveis sobre isso.
[10:21 - 10:24] Agent: Certo, eu trago as variáveis que forem relevantes no estudo.
[10:24 - 10:26] Agent: Obrigado por andar comigo nessa conversa.
[10:26 - 10:36] Agent: Vou estruturar o estudo de viabilidade com os três caminhos, analisando custo, prazos, capacidades técnicas, governança, risco, segurança e conformidade e trago uma recomendação ao final.
[10:36 - 10:40] Agent: Tendo em vista que você precisa disso amanhã, vou priorizar isso.
[10:40 - 10:42] Agent: Você tem mais alguma coisa a adicionar?
[10:42 - 10:44] Neemias Buceli: Não, that's it.
[10:45 - 10:48] Agent: Obrigado por compartilhar tudo isso comigo hoje.
[10:48 - 10:52] Agent: Vou estruturar o estudo de viabilidade e você receberá em breve.
[10:52 - 10:52] Agent: Até logo.
[10:53 - 10:53] Neemias Buceli: Ok, senhor.
[10:55 - 10:57] Agent: Ótimo. Obrigado novamente e até breve.
```

</details>

---

*Relatório gerado automaticamente pelo VMO Autônomo em 17/08/2026 a partir do Fireflies (ID: 01M08HA35T9P10W3SYTH94MTRH)*
