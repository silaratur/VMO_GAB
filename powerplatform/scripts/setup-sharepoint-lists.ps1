<#
.SYNOPSIS
    Cria todas as listas SharePoint necessárias para o VMO GAB no Power Platform.

.DESCRIPTION
    Este script usa PnP PowerShell para criar as 10 listas SharePoint do VMO GAB:
    VMO_Projetos, VMO_Demandas, VMO_Documentos, VMO_Requisitos, VMO_Riscos,
    VMO_KPIs, VMO_Cronograma, VMO_Alertas, VMO_Gates, VMO_StatusReports, VMO_DashboardData

.PARAMETER SiteUrl
    URL do site SharePoint onde as listas serão criadas.
    Exemplo: https://suaempresa.sharepoint.com/sites/VMO

.EXAMPLE
    .\setup-sharepoint-lists.ps1 -SiteUrl "https://suaempresa.sharepoint.com/sites/VMO"

.PREREQUISITES
    Install-Module -Name PnP.PowerShell -Force
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$SiteUrl,

    [Parameter(Mandatory=$false)]
    [switch]$LimparListasExistentes = $false
)

# === VERIFICAR DEPENDÊNCIAS ===
if (-not (Get-Module -ListAvailable -Name "PnP.PowerShell")) {
    Write-Host "Instalando PnP.PowerShell..." -ForegroundColor Yellow
    Install-Module -Name PnP.PowerShell -Force -Scope CurrentUser
}

Import-Module PnP.PowerShell

# === CONECTAR ===
Write-Host "`n🔗 Conectando ao SharePoint: $SiteUrl" -ForegroundColor Cyan
Connect-PnPOnline -Url $SiteUrl -UseWebLogin

Write-Host "✅ Conectado com sucesso!`n" -ForegroundColor Green

# === FUNÇÃO AUXILIAR ===
function New-VmoList {
    param($ListName, $Description, $Fields)

    Write-Host "📋 Criando lista: $ListName" -ForegroundColor Yellow

    if ($LimparListasExistentes) {
        try { Remove-PnPList -Identity $ListName -Force -ErrorAction SilentlyContinue } catch {}
    }

    try {
        $list = New-PnPList -Title $ListName -Template GenericList -OnQuickLaunch
        Set-PnPList -Identity $ListName -Description $Description

        foreach ($field in $Fields) {
            $params = @{
                List        = $ListName
                DisplayName = $field.DisplayName
                InternalName= $field.InternalName
                Type        = $field.Type
                Required    = $field.Required
            }
            if ($field.Choices) { $params.Choices = $field.Choices }
            if ($field.DefaultValue) { $params.DefaultValue = $field.DefaultValue }

            Add-PnPField @params | Out-Null
        }
        Write-Host "   ✅ $ListName criada com $($Fields.Count) colunas" -ForegroundColor Green
    }
    catch {
        Write-Host "   ⚠️  Erro ao criar $ListName : $($_.Exception.Message)" -ForegroundColor Red
    }
}

# =======================================================
# LISTA 1: VMO_PROJETOS
# =======================================================
New-VmoList -ListName "VMO_Projetos" -Description "Registro principal de projetos do VMO GAB" -Fields @(
    @{ DisplayName="Descrição";        InternalName="Descricao";        Type="Note";    Required=$false }
    @{ DisplayName="Status";           InternalName="Status";           Type="Choice";  Required=$true;
       Choices=@("INICIADO","EM_QUALIFICACAO","QUALIFICADO","DOCUMENTOS_CRIADOS","EM_ANDAMENTO","APROVADO","CONCLUIDO","CANCELADO","REPROVADO_GATE1","REPROVADO_GATE2","REPROVADO_GATE3") }
    @{ DisplayName="Fase";             InternalName="Fase";             Type="Choice";  Required=$false;
       Choices=@("01_CAPTURA","02_QUALIFICACAO","03_DOCUMENTACAO","04_EXECUCAO","05_ENCERRAMENTO","INTAKE_REJEITADO","QUALIFICACAO_REJEITADA","PRONTO_EXECUCAO") }
    @{ DisplayName="Responsável";      InternalName="Responsavel";      Type="Text";    Required=$false }
    @{ DisplayName="Patrocinador";     InternalName="Patrocinador";     Type="Text";    Required=$false }
    @{ DisplayName="Data Início";      InternalName="DataInicio";       Type="DateTime";Required=$false }
    @{ DisplayName="Data Fim Prevista";InternalName="DataFim";          Type="DateTime";Required=$false }
    @{ DisplayName="Data Aprovação";   InternalName="DataAprovacao";    Type="DateTime";Required=$false }
    @{ DisplayName="Health Score";     InternalName="HealthScore";      Type="Number";  Required=$false }
    @{ DisplayName="Score Qualificação";InternalName="ScoreQualificacao";Type="Number"; Required=$false }
    @{ DisplayName="Classificação";    InternalName="Classificacao";    Type="Choice";  Required=$false;
       Choices=@("PROJETO","CORRETIVA","EVOLUTIVA") }
    @{ DisplayName="Recomendação";     InternalName="Recomendacao";     Type="Text";    Required=$false }
    @{ DisplayName="Demanda ID";       InternalName="DemandaID";        Type="Text";    Required=$false }
    @{ DisplayName="Agente Qualificação";InternalName="AgenteQualificacao";Type="Text"; Required=$false }
    @{ DisplayName="CPI";              InternalName="CPI";              Type="Number";  Required=$false }
    @{ DisplayName="SPI";              InternalName="SPI";              Type="Number";  Required=$false }
    @{ DisplayName="Orçamento";        InternalName="Orcamento";        Type="Currency";Required=$false }
    @{ DisplayName="Área";             InternalName="Area";             Type="Text";    Required=$false }
)

# =======================================================
# LISTA 2: VMO_DEMANDAS
# =======================================================
New-VmoList -ListName "VMO_Demandas" -Description "Demandas recebidas pelo Agente Iara Inbound" -Fields @(
    @{ DisplayName="Descrição";       InternalName="Descricao";       Type="Note";    Required=$true }
    @{ DisplayName="Solicitante";     InternalName="Solicitante";     Type="Text";    Required=$true }
    @{ DisplayName="Canal";           InternalName="Canal";           Type="Choice";  Required=$false;
       Choices=@("Teams","Email","Formulário","Oral","WhatsApp","Outro") }
    @{ DisplayName="Data Recebimento";InternalName="DataRecebimento"; Type="DateTime";Required=$false }
    @{ DisplayName="Status";          InternalName="Status";          Type="Choice";  Required=$false;
       Choices=@("AGUARDANDO_GATE1","APROVADO_GATE1","REPROVADO_GATE1","EM_QUALIFICACAO","QUALIFICADO") }
    @{ DisplayName="ID Demanda";      InternalName="IDDemanda";       Type="Text";    Required=$false }
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$false }
    @{ DisplayName="Agente";          InternalName="Agente";          Type="Text";    Required=$false }
    @{ DisplayName="Documentação OK"; InternalName="DocumentacaoOK";  Type="Boolean"; Required=$false }
    @{ DisplayName="Área";            InternalName="Area";            Type="Text";    Required=$false }
    @{ DisplayName="Prazo Esperado";  InternalName="PrazoEsperado";   Type="Text";    Required=$false }
    @{ DisplayName="Orçamento Estimado";InternalName="OrcamentoEstimado";Type="Text"; Required=$false }
)

# =======================================================
# LISTA 3: VMO_DOCUMENTOS
# =======================================================
New-VmoList -ListName "VMO_Documentos" -Description "Documentos gerados pelos agentes VMO (TAP, PM Canvas, ERF, etc.)" -Fields @(
    @{ DisplayName="Tipo";            InternalName="Tipo";            Type="Choice";  Required=$true;
       Choices=@("TAP","PM_CANVAS","PLANO_GERAL","REQUISITOS","WORK_REQUEST","CRONOGRAMA","RISCOS","KPIS","STATUS_REPORT","AUDITORIA","QUALIFICACAO") }
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$true }
    @{ DisplayName="URL Documento";   InternalName="ConteudoURL";     Type="URL";     Required=$false }
    @{ DisplayName="Versão";          InternalName="Versao";          Type="Text";    Required=$false;   DefaultValue="1.0" }
    @{ DisplayName="Status";          InternalName="Status";          Type="Choice";  Required=$false;
       Choices=@("RASCUNHO","REVISAO","APROVADO","REPROVADO","PUBLICADO") }
    @{ DisplayName="Autor (Agente)";  InternalName="Agente";          Type="Text";    Required=$false }
    @{ DisplayName="Data Criação";    InternalName="DataCriacao";     Type="DateTime";Required=$false }
)

# =======================================================
# LISTA 4: VMO_REQUISITOS
# =======================================================
New-VmoList -ListName "VMO_Requisitos" -Description "Requisitos funcionais e não-funcionais — Agente Rafael" -Fields @(
    @{ DisplayName="Tipo";            InternalName="Tipo";            Type="Choice";  Required=$true;
       Choices=@("RF","RNF","REGRA_NEGOCIO","RESTRICAO") }
    @{ DisplayName="Prioridade";      InternalName="Prioridade";      Type="Choice";  Required=$true;
       Choices=@("MUST","SHOULD","COULD","WONT") }
    @{ DisplayName="Descrição";       InternalName="Descricao";       Type="Note";    Required=$true }
    @{ DisplayName="Critério Aceitação";InternalName="CriterioAceitacao";Type="Note"; Required=$false }
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$true }
    @{ DisplayName="Status";          InternalName="Status";          Type="Choice";  Required=$false;
       Choices=@("PENDENTE","APROVADO","REPROVADO","IMPLEMENTADO","TESTADO") }
    @{ DisplayName="ID Requisito";    InternalName="IDRequisito";     Type="Text";    Required=$false }
    @{ DisplayName="Ator";            InternalName="Ator";            Type="Text";    Required=$false }
)

# =======================================================
# LISTA 5: VMO_RISCOS
# =======================================================
New-VmoList -ListName "VMO_Riscos" -Description "Registro de riscos — Agente Pedro Perigo" -Fields @(
    @{ DisplayName="Categoria";       InternalName="Categoria";       Type="Choice";  Required=$true;
       Choices=@("TECNICO","CRONOGRAMA","CUSTO","RECURSOS","EXTERNO","GOVERNANCA","QUALIDADE","SEGURANÇA") }
    @{ DisplayName="Probabilidade";   InternalName="Probabilidade";   Type="Number";  Required=$true }
    @{ DisplayName="Impacto";         InternalName="Impacto";         Type="Number";  Required=$true }
    @{ DisplayName="Score";           InternalName="Score";           Type="Number";  Required=$false }
    @{ DisplayName="Estratégia";      InternalName="Estrategia";      Type="Choice";  Required=$false;
       Choices=@("EVITAR","TRANSFERIR","MITIGAR","ACEITAR") }
    @{ DisplayName="Gatilho";         InternalName="Gatilho";         Type="Note";    Required=$false }
    @{ DisplayName="Resposta";        InternalName="Resposta";        Type="Note";    Required=$false }
    @{ DisplayName="Reserva Contingência";InternalName="ReservaContingencia";Type="Currency";Required=$false }
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$true }
    @{ DisplayName="Status";          InternalName="Status";          Type="Choice";  Required=$false;
       Choices=@("ABERTO","MONITORANDO","FECHADO","MATERIALIZADO") }
    @{ DisplayName="Responsável";     InternalName="Responsavel";     Type="Text";    Required=$false }
)

# =======================================================
# LISTA 6: VMO_KPIs
# =======================================================
New-VmoList -ListName "VMO_KPIs" -Description "KPIs e métricas de performance — Agente Marcela" -Fields @(
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$true }
    @{ DisplayName="CPI";             InternalName="CPI";             Type="Number";  Required=$false }
    @{ DisplayName="SPI";             InternalName="SPI";             Type="Number";  Required=$false }
    @{ DisplayName="IHP";             InternalName="IHP";             Type="Number";  Required=$false }
    @{ DisplayName="IHG";             InternalName="IHG";             Type="Number";  Required=$false }
    @{ DisplayName="IHC";             InternalName="IHC";             Type="Number";  Required=$false }
    @{ DisplayName="ISC";             InternalName="ISC";             Type="Number";  Required=$false }
    @{ DisplayName="Health Score";    InternalName="HealthScore";     Type="Number";  Required=$false }
    @{ DisplayName="Status";          InternalName="Status";          Type="Choice";  Required=$false;
       Choices=@("VERDE","AMARELO","VERMELHO") }
    @{ DisplayName="Data";            InternalName="Data";            Type="DateTime";Required=$false }
    @{ DisplayName="Semana";          InternalName="Semana";          Type="Text";    Required=$false }
    @{ DisplayName="Variância Custo"; InternalName="VarianciaCusto";  Type="Number";  Required=$false }
    @{ DisplayName="Variância Prazo"; InternalName="VarianciaPrazo";  Type="Number";  Required=$false }
    @{ DisplayName="EV";              InternalName="EV";              Type="Currency";Required=$false }
    @{ DisplayName="AC";              InternalName="AC";              Type="Currency";Required=$false }
    @{ DisplayName="PV";              InternalName="PV";              Type="Currency";Required=$false }
)

# =======================================================
# LISTA 7: VMO_CRONOGRAMA
# =======================================================
New-VmoList -ListName "VMO_Cronograma" -Description "Cronograma e WBS — Agente Carlos Cronograma" -Fields @(
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$true }
    @{ DisplayName="Nível WBS";       InternalName="NivelWBS";        Type="Choice";  Required=$false;
       Choices=@("1","2","3") }
    @{ DisplayName="WBS Code";        InternalName="WBSCode";         Type="Text";    Required=$false }
    @{ DisplayName="Tarefa";          InternalName="Tarefa";          Type="Note";    Required=$false }
    @{ DisplayName="Data Início";     InternalName="DataInicio";      Type="DateTime";Required=$false }
    @{ DisplayName="Data Fim";        InternalName="DataFim";         Type="DateTime";Required=$false }
    @{ DisplayName="Duração (dias)";  InternalName="DuracaoDias";     Type="Number";  Required=$false }
    @{ DisplayName="Responsável";     InternalName="Responsavel";     Type="Text";    Required=$false }
    @{ DisplayName="Status";          InternalName="Status";          Type="Choice";  Required=$false;
       Choices=@("PLANEJADO","EM_ANDAMENTO","CONCLUIDO","ATRASADO","BLOQUEADO") }
    @{ DisplayName="Caminho Crítico"; InternalName="CaminhosCritico"; Type="Boolean"; Required=$false }
    @{ DisplayName="% Concluído";     InternalName="PercConcluido";   Type="Number";  Required=$false }
    @{ DisplayName="Predecessoras";   InternalName="Predecessoras";   Type="Text";    Required=$false }
)

# =======================================================
# LISTA 8: VMO_ALERTAS
# =======================================================
New-VmoList -ListName "VMO_Alertas" -Description "Alertas e notificações do portfolio VMO" -Fields @(
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$false }
    @{ DisplayName="Severidade";      InternalName="Severidade";      Type="Choice";  Required=$true;
       Choices=@("CRITICO","ALTO","MEDIO","BAIXO") }
    @{ DisplayName="Mensagem";        InternalName="Mensagem";        Type="Note";    Required=$true }
    @{ DisplayName="Data Alerta";     InternalName="DataAlerta";      Type="DateTime";Required=$false }
    @{ DisplayName="Resolvido";       InternalName="Resolvido";       Type="Boolean"; Required=$false }
    @{ DisplayName="Data Resolução";  InternalName="DataResolucao";   Type="DateTime";Required=$false }
    @{ DisplayName="Tipo";            InternalName="Tipo";            Type="Choice";  Required=$false;
       Choices=@("PRAZO","CUSTO","RISCO","GOVERNANCA","QUALIDADE","RECURSO") }
    @{ DisplayName="Agente Origem";   InternalName="AgenteOrigem";    Type="Text";    Required=$false }
)

# =======================================================
# LISTA 9: VMO_GATES
# =======================================================
New-VmoList -ListName "VMO_Gates" -Description "Gates de governança e aprovações — Agente Gabriel" -Fields @(
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$true }
    @{ DisplayName="Tipo Gate";       InternalName="Tipo";            Type="Choice";  Required=$true;
       Choices=@("INTAKE","QUALIFICACAO","FINAL","CHANGE_CONTROL","QUALIDADE") }
    @{ DisplayName="Status";          InternalName="Status";          Type="Choice";  Required=$false;
       Choices=@("PENDENTE","APROVADO","REPROVADO","BLOQUEADO","APROVADO_COM_RESSALVAS") }
    @{ DisplayName="Decisor";         InternalName="Decisor";         Type="Text";    Required=$false }
    @{ DisplayName="Data Decisão";    InternalName="DataDecisao";     Type="DateTime";Required=$false }
    @{ DisplayName="Comentários";     InternalName="Comentarios";     Type="Note";    Required=$false }
    @{ DisplayName="Checklist Completo";InternalName="ChecklistCompleto";Type="Boolean";Required=$false }
    @{ DisplayName="Docs Faltantes";  InternalName="DocumentosFaltantes";Type="Note"; Required=$false }
    @{ DisplayName="Score Governança";InternalName="ScoreGovernanca"; Type="Number";  Required=$false }
    @{ DisplayName="Ciclo";           InternalName="Ciclo";           Type="Number";  Required=$false }
    @{ DisplayName="Condições Bloqueantes";InternalName="CondicoesBloqueantes";Type="Note";Required=$false }
)

# =======================================================
# LISTA 10: VMO_STATUS_REPORTS
# =======================================================
New-VmoList -ListName "VMO_StatusReports" -Description "Status reports semanais — Agente Sara Status" -Fields @(
    @{ DisplayName="Projeto ID";      InternalName="ProjetoID";       Type="Text";    Required=$true }
    @{ DisplayName="Semana";          InternalName="Semana";          Type="Text";    Required=$false }
    @{ DisplayName="Data";            InternalName="Data";            Type="DateTime";Required=$false }
    @{ DisplayName="CPI";             InternalName="CPIVal";          Type="Number";  Required=$false }
    @{ DisplayName="SPI";             InternalName="SPIVal";          Type="Number";  Required=$false }
    @{ DisplayName="Status Geral";    InternalName="StatusGeral";     Type="Choice";  Required=$false;
       Choices=@("VERDE","AMARELO","VERMELHO") }
    @{ DisplayName="Status Prazo";    InternalName="StatusPrazo";     Type="Choice";  Required=$false;
       Choices=@("VERDE","AMARELO","VERMELHO") }
    @{ DisplayName="Status Custo";    InternalName="StatusCusto";     Type="Choice";  Required=$false;
       Choices=@("VERDE","AMARELO","VERMELHO") }
    @{ DisplayName="Status Escopo";   InternalName="StatusEscopo";    Type="Choice";  Required=$false;
       Choices=@("VERDE","AMARELO","VERMELHO") }
    @{ DisplayName="Issues";          InternalName="Issues";          Type="Note";    Required=$false }
    @{ DisplayName="Próximas Ações";  InternalName="ProximasAcoes";   Type="Note";    Required=$false }
    @{ DisplayName="Conteúdo";        InternalName="Conteudo";        Type="Note";    Required=$false }
    @{ DisplayName="Link Documento";  InternalName="LinkDocumento";   Type="URL";     Required=$false }
    @{ DisplayName="Resumo Executivo";InternalName="ResumoExecutivo"; Type="Note";    Required=$false }
)

# =======================================================
# LISTA 11: VMO_DASHBOARD_DATA (para Canvas App)
# =======================================================
New-VmoList -ListName "VMO_DashboardData" -Description "Dados consolidados para o Canvas App Dashboard" -Fields @(
    @{ DisplayName="Total Projetos";  InternalName="TotalProjetos";   Type="Number";  Required=$false }
    @{ DisplayName="Projetos Ativos"; InternalName="ProjetosAtivos";  Type="Number";  Required=$false }
    @{ DisplayName="Health Score";    InternalName="HealthScore";     Type="Number";  Required=$false }
    @{ DisplayName="Total Alertas";   InternalName="TotalAlertas";    Type="Number";  Required=$false }
    @{ DisplayName="Alertas Críticos";InternalName="AlertasCriticos"; Type="Number";  Required=$false }
    @{ DisplayName="Total Riscos";    InternalName="TotalRiscos";     Type="Number";  Required=$false }
    @{ DisplayName="Riscos Altos";    InternalName="RiscosAltos";     Type="Number";  Required=$false }
    @{ DisplayName="Última Atualização";InternalName="UltimaAtualizacao";Type="DateTime";Required=$false }
    @{ DisplayName="Dados JSON";      InternalName="DadosJSON";       Type="Note";    Required=$false }
    @{ DisplayName="CPI Médio";       InternalName="CPIMedio";        Type="Number";  Required=$false }
    @{ DisplayName="SPI Médio";       InternalName="SPIMedio";        Type="Number";  Required=$false }
)

# =======================================================
# CRIAR BIBLIOTECA DE DOCUMENTOS
# =======================================================
Write-Host "`n📁 Criando Biblioteca de Documentos: VMO_Projetos" -ForegroundColor Yellow
try {
    New-PnPList -Title "VMO_Documentos_Lib" -Template DocumentLibrary -OnQuickLaunch
    Write-Host "   ✅ Biblioteca VMO_Documentos_Lib criada" -ForegroundColor Green
} catch {
    Write-Host "   ℹ️  Biblioteca já existe ou erro: $($_.Exception.Message)" -ForegroundColor DarkYellow
}

# =======================================================
# RELATÓRIO FINAL
# =======================================================
Write-Host "`n" + "="*60 -ForegroundColor Cyan
Write-Host "✅ SETUP CONCLUÍDO!" -ForegroundColor Green
Write-Host "="*60 -ForegroundColor Cyan
Write-Host "`nListas criadas no SharePoint ($SiteUrl):" -ForegroundColor White
Write-Host "  1. VMO_Projetos       — Registro principal de projetos" -ForegroundColor Gray
Write-Host "  2. VMO_Demandas       — Demandas (Agente Iara)" -ForegroundColor Gray
Write-Host "  3. VMO_Documentos     — Metadados de documentos" -ForegroundColor Gray
Write-Host "  4. VMO_Requisitos     — Requisitos RF/RNF (Agente Rafael)" -ForegroundColor Gray
Write-Host "  5. VMO_Riscos         — Registro de riscos (Agente Pedro)" -ForegroundColor Gray
Write-Host "  6. VMO_KPIs           — KPIs e métricas (Agente Marcela)" -ForegroundColor Gray
Write-Host "  7. VMO_Cronograma     — WBS e cronograma (Agente Carlos)" -ForegroundColor Gray
Write-Host "  8. VMO_Alertas        — Alertas e notificações" -ForegroundColor Gray
Write-Host "  9. VMO_Gates          — Gates de governança (Agente Gabriel)" -ForegroundColor Gray
Write-Host " 10. VMO_StatusReports  — Status reports (Agente Sara)" -ForegroundColor Gray
Write-Host " 11. VMO_DashboardData  — Dados para Canvas App" -ForegroundColor Gray
Write-Host " 12. VMO_Documentos_Lib — Biblioteca de documentos gerados" -ForegroundColor Gray

Write-Host "`n🔜 Próximo passo: Execute build-solution.ps1 para gerar o pacote ZIP" -ForegroundColor Cyan
