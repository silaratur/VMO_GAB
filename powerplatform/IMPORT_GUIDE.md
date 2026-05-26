# VMO GAB — Guia de Importação no Power Platform

**Versão:** 1.0.0 | **Ambiente alvo:** Microsoft 365 Business | **Última atualização:** 2026-05-26

---

## Visão Geral da Solução

```
VMO_GAB_Solution.zip
├── Manifests
│   ├── solution.xml          — Metadados da solução
│   ├── customizations.xml    — Lista de componentes
│   └── [Content_Types].xml
│
├── Workflows/ (13 Power Automate Flows)
│   ├── VMO_Main_Pipeline.json           — Orquestrador principal (16 etapas)
│   ├── VMO_Iara_CapturarDemanda.json    — Captura demanda
│   ├── VMO_Felipe_QualificarDemanda.json— Qualificação (10 critérios)
│   ├── VMO_Diana_CriarDocumentos.json   — TAP + PM Canvas
│   ├── VMO_Rafael_LevantarRequisitos.json— Requisitos RF/RNF
│   ├── VMO_Fabio_GerarWorkRequest.json  — Work Request
│   ├── VMO_Carlos_CriarCronograma.json  — WBS + Cronograma
│   ├── VMO_Pedro_AnaliseRiscos.json     — Matriz de riscos
│   ├── VMO_Marcela_DefinirKPIs.json     — KPI framework
│   ├── VMO_Sara_StatusReport.json       — Status reports semanais
│   ├── VMO_Vera_RevisaoQualidade.json   — Revisão de qualidade
│   ├── VMO_Gabriel_Governanca.json      — Gates de governança
│   └── VMO_Publisher_Dashboard.json     — Atualização dashboard (6h)
│
├── CanvasApps/
│   └── VMO_GAB_Dashboard/              — 6 telas do dashboard
│       ├── App.fx.yaml                  — Configuração principal
│       ├── Connections.json             — Fontes de dados
│       └── Screens/
│           ├── Dashboard.fx.yaml        — Mission Control
│           ├── KPIs.fx.yaml             — Dashboard de KPIs
│           ├── Riscos.fx.yaml           — Matriz de riscos
│           └── ...
│
└── botcomponents/
    └── VMO_Assistente/                 — Bot Copilot Studio
        ├── bot.yaml                    — Configuração do bot
        └── topics/
            ├── NovaDemanda.yaml        — Iara: captura demanda
            ├── ConsultarProjeto.yaml   — Consulta status
            ├── ConsultarKPIs.yaml      — Marcela: KPIs
            ├── GerarRelatorio.yaml     — Sara: status report
            ├── AuditoriaGovernanca.yaml— Gabriel: gates
            ├── PipelineCompleto.yaml   — Pipeline full
            └── Help.yaml              — Ajuda
```

---

## Pré-requisitos

| Requisito | Detalhe |
|-----------|---------|
| Microsoft 365 Business | Plano Basic, Standard ou Premium |
| SharePoint Online | Permissão de Site Collection Admin |
| Power Automate | Licença incluída no M365 |
| Power Apps | Licença incluída no M365 |
| Copilot Studio | Trial gratuito ou licença add-on |
| Power Platform CLI (PAC) | Para empacotar Canvas App em .msapp |

---

## PASSO 1 — Setup do SharePoint (obrigatório primeiro)

### 1.1 Criar Site SharePoint

1. Acesse o SharePoint Online da sua organização
2. Crie um novo **Team Site** chamado `VMO`
   - URL sugerida: `https://SUAEMPRESA.sharepoint.com/sites/VMO`
3. Anote a URL completa

### 1.2 Criar as Listas (PowerShell)

```powershell
# Instalar dependência (uma vez)
Install-Module -Name PnP.PowerShell -Force -Scope CurrentUser

# Executar o setup
cd powerplatform/scripts
.\setup-sharepoint-lists.ps1 -SiteUrl "https://SUAEMPRESA.sharepoint.com/sites/VMO"
```

> **Resultado:** 12 listas e 1 biblioteca de documentos criadas automaticamente.

### 1.3 Verificar Listas Criadas

Acesse o SharePoint e confirme que estas listas existem:
- VMO_Projetos
- VMO_Demandas
- VMO_Documentos
- VMO_Requisitos
- VMO_Riscos
- VMO_KPIs
- VMO_Cronograma
- VMO_Alertas
- VMO_Gates
- VMO_StatusReports
- VMO_DashboardData
- VMO_Documentos_Lib (Biblioteca)

---

## PASSO 2 — Gerar o Pacote ZIP

```powershell
cd powerplatform/scripts
.\build-solution.ps1
# Gera: powerplatform/VMO_GAB_Solution.zip
```

**Para empacotar o Canvas App em .msapp (requer PAC CLI):**

```powershell
# Instalar PAC CLI
winget install Microsoft.PowerAppsCLI

# Build com Canvas App empacotado
.\build-solution.ps1 -PackCanvasApp
```

---

## PASSO 3 — Importar a Solução

### 3.1 Via Power Platform Admin Center (Recomendado)

1. Acesse [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com)
2. Selecione seu **Environment**
3. Vá em **Solutions** → **Import Solution**
4. Clique **Browse** e selecione `VMO_GAB_Solution.zip`
5. Clique **Next**

### 3.2 Configurar Conexões

Durante a importação, configure as conexões:

| Conexão | Tipo | Ação |
|---------|------|------|
| SharePoint Online | Shared | Selecione sua conta e o site VMO |
| Approvals | Shared | Selecione sua conta Microsoft |
| Office 365 Outlook | Shared | Selecione sua conta de email |
| Microsoft Teams | Shared | Selecione sua conta Teams |

> **Atenção:** Crie as conexões ANTES de importar se quiser evitar reconfigurações.

### 3.3 Configurar Variáveis de Ambiente

Após a importação, configure as variáveis:

| Variável | Valor |
|----------|-------|
| `vmo_SharePointSiteUrl` | `https://SUAEMPRESA.sharepoint.com/sites/VMO` |
| `vmo_ApprovalEmail` | Email do gestor que aprova os gates |
| `vmo_TeamsChannelId` | ID do canal Teams para notificações |

---

## PASSO 4 — Configurar os Flows

Após importar, os flows precisam ser ativados e configurados:

### 4.1 Atualizar URLs dos Flows

No **VMO_Main_Pipeline**, substitua os placeholders nas ações HTTP:
```
https://prod-XX.brazilsouth.logic.azure.com/workflows/VMO_Iara/...
```
Pelas URLs reais de cada flow (disponíveis em Power Automate → Detalhes do flow).

**Script de atualização automática:**

```powershell
# Após importar, use o Power Automate Management connector
# ou atualize manualmente os 11 endpoints HTTP no flow principal
```

### 4.2 Ativar Todos os Flows

1. Acesse [make.powerautomate.com](https://make.powerautomate.com)
2. Em **My Flows** → **Solutions** → **VMO_GAB**
3. Ative cada flow na ordem:
   1. VMO_Iara_CapturarDemanda
   2. VMO_Felipe_QualificarDemanda
   3. VMO_Diana_CriarDocumentos
   4. VMO_Rafael_LevantarRequisitos
   5. VMO_Fabio_GerarWorkRequest
   6. VMO_Carlos_CriarCronograma
   7. VMO_Pedro_AnaliseRiscos
   8. VMO_Marcela_DefinirKPIs
   9. VMO_Sara_StatusReport
   10. VMO_Vera_RevisaoQualidade
   11. VMO_Gabriel_Governanca
   12. VMO_Publisher_Dashboard
   13. **VMO_Main_Pipeline** (por último)

---

## PASSO 5 — Configurar o Canvas App

### 5.1 Importar via PAC CLI

```bash
# Instalar PAC CLI
winget install Microsoft.PowerAppsCLI

# Fazer login
pac auth create --environment YOUR_ENV_ID

# Empacotar fontes YAML em .msapp
pac canvas pack \
  --sources "powerplatform/canvas-app/VMO_GAB_Dashboard" \
  --msapp "VMO_GAB_Dashboard.msapp"

# Importar no ambiente
pac application import --msapp "VMO_GAB_Dashboard.msapp"
```

### 5.2 Configurar Fontes de Dados

1. Abra o app no [make.powerapps.com](https://make.powerapps.com)
2. Em **Data** → **Add data** → **SharePoint**
3. Adicione o site `https://SUAEMPRESA.sharepoint.com/sites/VMO`
4. Selecione todas as listas VMO_*
5. Salve e publique

### 5.3 Substituir URL nos Formulas

Na tela `App.fx.yaml`, linha:
```
SPSite: ="https://SUAEMPRESA.sharepoint.com/sites/VMO"
```
Substitua `SUAEMPRESA` pelo seu tenant.

---

## PASSO 6 — Configurar o Copilot Studio Bot

### 6.1 Criar Bot no Copilot Studio

1. Acesse [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Clique **Create** → **New copilot**
3. Nome: `VMO Assistente`
4. Idioma: `Português (Brasil)`

### 6.2 Importar Tópicos

Para cada arquivo em `copilot-studio/VMO_Assistente/topics/`:

1. No Copilot Studio, vá em **Topics** → **Add topic** → **From blank**
2. No editor, clique em **YAML** e cole o conteúdo do arquivo
3. Salve e ative o tópico

**Ordem de importação:**
1. Help.yaml
2. NovaDemanda.yaml
3. ConsultarProjeto.yaml
4. ConsultarKPIs.yaml
5. GerarRelatorio.yaml
6. AuditoriaGovernanca.yaml
7. PipelineCompleto.yaml

### 6.3 Conectar Bot aos Flows

Para cada tópico que chama um flow (InvokeFlowAction):

1. No Copilot Studio, abra o tópico
2. Clique na ação **Call an action**
3. Selecione **Power Automate flow**
4. Vincule ao flow correspondente

### 6.4 Publicar no Teams

1. No Copilot Studio → **Channels** → **Microsoft Teams**
2. Clique **Add to Teams**
3. Configure permissões e publique

---

## PASSO 7 — Teste de Fumaça

### 7.1 Testar Pipeline Completo

```
No Teams, abra o VMO Assistente e digite:
"quero abrir um projeto"

Siga o fluxo de perguntas da Iara.
Verifique se o item foi criado no SharePoint VMO_Demandas.
```

### 7.2 Testar Flow Principal

1. No Power Automate, abra `VMO_Main_Pipeline`
2. Clique **Test** → **Manually**
3. Insira payload de teste:
```json
{
  "Title": "Projeto Teste",
  "Descricao": "Descrição detalhada do projeto de teste para validar o pipeline VMO completo.",
  "Solicitante": "João Silva",
  "Canal": "Teams"
}
```

### 7.3 Verificar Canvas App

1. Abra o Power Apps em [make.powerapps.com](https://make.powerapps.com)
2. Abra `VMO GAB — Dashboard`
3. Confirme que as telas carregam e os dados aparecem

---

## Arquitetura da Solução

```
                    ┌─────────────────────┐
                    │   USUÁRIO (Teams)   │
                    └──────────┬──────────┘
                               │ fala com
                    ┌──────────▼──────────┐
                    │   COPILOT STUDIO    │
                    │   VMO Assistente    │
                    │  (11 agentes como   │
                    │    bot topics)      │
                    └──────────┬──────────┘
                               │ chama flows via
                    ┌──────────▼──────────┐
                    │   POWER AUTOMATE    │
                    │  13 Flows/Agentes   │
                    │  + 3 Gates humanos  │
                    └──────────┬──────────┘
                               │ lê/grava
                    ┌──────────▼──────────┐
                    │  SHAREPOINT ONLINE  │
                    │   12 Listas + 1     │
                    │    Biblioteca       │
                    └──────────┬──────────┘
                               │ expõe dados para
                    ┌──────────▼──────────┐
                    │   POWER APPS        │
                    │   Canvas App        │
                    │   6 telas dashboard │
                    └─────────────────────┘
```

---

## Troubleshooting

| Problema | Causa provável | Solução |
|----------|----------------|---------|
| Flow não encontra lista SharePoint | URL incorreta | Verificar `vmo_SharePointSiteUrl` |
| Aprovação não chega | Email incorreto | Verificar `vmo_ApprovalEmail` |
| Canvas App mostra dados vazios | Fontes de dados não configuradas | Passo 5.2 |
| Bot não reconhece intenção | Tópico desativado | Ativar tópico no Copilot Studio |
| Flow falha na ação HTTP | URL de outro flow incorreta | Atualizar endpoints no Main Pipeline |
| Erro 401 no SharePoint | Conexão expirada | Reconectar SharePoint no Power Automate |

---

## Suporte

- **Documentação Power Platform:** [learn.microsoft.com/power-platform](https://learn.microsoft.com/power-platform)
- **PAC CLI:** [aka.ms/PowerAppsCLI](https://aka.ms/PowerAppsCLI)
- **PnP PowerShell:** [pnp.github.io/powershell](https://pnp.github.io/powershell)
- **Issues do projeto:** GitHub → silaratur/VMO_GAB
