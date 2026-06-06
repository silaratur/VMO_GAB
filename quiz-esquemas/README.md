# Questionário de Esquemas — App para Palestrante

205 perguntas · 16 esquemas · YSQ Feminino

## Rodar localmente

```bash
npm install
node server.js
```

Acesse: `http://localhost:3000`  
Dashboard: `http://localhost:3000/dashboard.html`

---

## Deploy com URL pública (Railway — gratuito)

1. Crie conta em https://railway.app
2. Clique em **New Project → Deploy from GitHub repo**
3. Aponte para este repositório, pasta `quiz-esquemas/`
4. O Railway vai gerar uma URL do tipo `https://quiz-esquemas-xxx.up.railway.app`
5. Configure a variável de ambiente:
   ```
   BASE_URL = https://sua-url.up.railway.app
   PORT = 3000
   ```
6. Abra o dashboard em `https://sua-url.up.railway.app/dashboard.html`  
   → O QR Code já estará com a URL correta para qualquer celular escanear

---

## Deploy com Render (alternativa gratuita)

1. Crie conta em https://render.com
2. New → Web Service → Connect GitHub
3. Root Directory: `quiz-esquemas`
4. Build Command: `npm install`
5. Start Command: `node server.js`
6. Adicione env var: `BASE_URL = https://seu-app.onrender.com`

---

## Uso durante a palestra

| Quem | URL |
|------|-----|
| Participantes (celular) | `https://sua-url/` (via QR code) |
| Palestrante (dashboard) | `https://sua-url/dashboard.html` |
| Resultado individual | `https://sua-url/resultado.html?id=XXX` |

### Fluxo:
1. Palestrante abre o dashboard → aba **QR Code** → projeta na tela
2. Participantes escaneiam e respondem as 205 perguntas
3. Dashboard atualiza automaticamente a cada 15 segundos
4. Palestrante acompanha resultados em tempo real (grupo + individual)
5. Ao final, aba **Palavras** mostra a nuvem de palavras marcantes
