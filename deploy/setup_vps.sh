#!/bin/bash
# Script de configuração inicial da VPS
# Execute uma vez como root: bash setup_vps.sh

set -e

APP_DIR="/opt/vmo_gab"
APP_USER="root"
REPO_URL="https://github.com/silaratur/VMO_GAB.git"

echo "==> Atualizando sistema..."
apt-get update -qq && apt-get upgrade -y -qq

echo "==> Instalando dependências..."
apt-get install -y -qq python3 python3-pip python3-venv git

echo "==> Clonando repositório..."
if [ -d "$APP_DIR" ]; then
    cd "$APP_DIR" && git pull origin main
else
    git clone "$REPO_URL" "$APP_DIR"
fi

echo "==> Criando ambiente virtual..."
cd "$APP_DIR"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt --quiet

echo "==> Criando arquivo .env..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "ATENCAO: edite o arquivo $APP_DIR/.env com suas configuracoes!"
fi

echo "==> Configurando serviço systemd..."
cat > /etc/systemd/system/vmo_gab.service <<EOF
[Unit]
Description=VMO GAB FastAPI App
After=network.target

[Service]
User=$APP_USER
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=3
EnvironmentFile=$APP_DIR/.env

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable vmo_gab
systemctl start vmo_gab

echo ""
echo "==> Setup concluido!"
echo "    Status: $(systemctl is-active vmo_gab)"
echo "    API:    http://$(hostname -I | awk '{print $1}'):8000"
echo ""
echo "Proximos passos:"
echo "  1. Edite $APP_DIR/.env com suas configuracoes"
echo "  2. Configure os secrets no GitHub (VPS_HOST, VPS_USER, VPS_SSH_KEY)"
echo "  3. Adicione a chave publica do GitHub Actions ao ~/.ssh/authorized_keys"
