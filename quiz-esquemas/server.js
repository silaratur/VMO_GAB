const express = require('express');
const Database = require('better-sqlite3');
const QRCode = require('qrcode');
const { v4: uuidv4 } = require('uuid');
const path = require('path');
const os = require('os');

const app = express();
const PORT = process.env.PORT || 3000;
const db = new Database('respostas.db');

// Init DB
db.exec(`
  CREATE TABLE IF NOT EXISTS respostas (
    id TEXT PRIMARY KEY,
    nome TEXT,
    idade TEXT,
    profissao TEXT,
    respostas TEXT,
    palavra_marcante TEXT,
    criado_em TEXT
  )
`);

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

function getLocalIP() {
  const interfaces = os.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      if (iface.family === 'IPv4' && !iface.internal) return iface.address;
    }
  }
  return 'localhost';
}

// Submit respostas
app.post('/api/resposta', (req, res) => {
  const { nome, idade, profissao, respostas, palavra_marcante } = req.body;
  const id = uuidv4();
  const criado_em = new Date().toISOString();
  db.prepare(`INSERT INTO respostas VALUES (?, ?, ?, ?, ?, ?, ?)`)
    .run(id, nome, idade, profissao, JSON.stringify(respostas), palavra_marcante, criado_em);
  res.json({ id });
});

// Buscar resultado individual
app.get('/api/resposta/:id', (req, res) => {
  const row = db.prepare('SELECT * FROM respostas WHERE id = ?').get(req.params.id);
  if (!row) return res.status(404).json({ erro: 'Não encontrado' });
  row.respostas = JSON.parse(row.respostas);
  res.json(row);
});

// Listar todas as respostas (para o palestrante)
app.get('/api/respostas', (req, res) => {
  const rows = db.prepare('SELECT * FROM respostas ORDER BY criado_em DESC').all();
  rows.forEach(r => { r.respostas = JSON.parse(r.respostas); });
  res.json(rows);
});

// QR code da URL do formulário
app.get('/api/qrcode', async (req, res) => {
  const ip = getLocalIP();
  const url = `http://${ip}:${PORT}`;
  const qr = await QRCode.toDataURL(url, { width: 300, margin: 2 });
  res.json({ url, qr });
});

app.listen(PORT, '0.0.0.0', () => {
  const ip = getLocalIP();
  console.log(`\n✅ App rodando!`);
  console.log(`   Participantes: http://${ip}:${PORT}`);
  console.log(`   Dashboard:     http://${ip}:${PORT}/dashboard.html\n`);
});
