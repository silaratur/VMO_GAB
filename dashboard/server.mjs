#!/usr/bin/env node
/**
 * Opensquad Dashboard — Production Server
 *
 * - Serves the Vite build (dist/) as a static SPA
 * - GET  /api/snapshot       → squad list + last known states
 * - POST /api/push-state/:squad → receives live state from Claude Code runner
 * - WS   /__squads_ws        → real-time state updates to browser
 */
import { createServer } from "node:http";
import { WebSocketServer, WebSocket } from "ws";
import fsp from "node:fs/promises";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { parse as parseYaml } from "yaml";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PORT = parseInt(process.env.PORT ?? "3001", 10);
const STATIC_DIR = path.resolve(__dirname, "dist");
const SQUADS_DIR = process.env.SQUADS_DIR
  ? path.resolve(process.env.SQUADS_DIR)
  : (() => {
      for (const c of [
        path.resolve(__dirname, "../squads"),
        path.resolve(__dirname, "squads"),
      ]) {
        if (fs.existsSync(c)) return c;
      }
      return path.resolve(__dirname, "../squads");
    })();

// ── In-memory pushed-state cache (from Claude Code runner) ──────────────────
const PUSH_TTL_MS = 24 * 60 * 60 * 1000;
/** @type {Map<string, { state: object, pushedAt: number }>} */
const pushedStates = new Map();
setInterval(() => {
  const now = Date.now();
  for (const [k, v] of pushedStates) {
    if (now - v.pushedAt > PUSH_TTL_MS) pushedStates.delete(k);
  }
}, 60_000);

// ── Squad discovery ──────────────────────────────────────────────────────────
async function discoverSquads() {
  let entries;
  try { entries = await fsp.readdir(SQUADS_DIR, { withFileTypes: true }); }
  catch { return []; }

  const squads = [];
  for (const e of entries) {
    if (!e.isDirectory() || e.name.startsWith(".") || e.name.startsWith("_")) continue;
    const yamlPath = path.join(SQUADS_DIR, e.name, "squad.yaml");
    try {
      const parsed = parseYaml(await fsp.readFile(yamlPath, "utf-8"));
      const s = parsed?.squad;
      if (s) {
        squads.push({
          code: s.code ?? e.name,
          name: s.name ?? e.name,
          description: s.description ?? "",
          icon: s.icon ?? "📋",
          agents: Array.isArray(s.agents) ? s.agents.filter(a => typeof a === "string") : [],
        });
        continue;
      }
    } catch {}
    squads.push({ code: e.name, name: e.name, description: "", icon: "📋", agents: [] });
  }
  return squads;
}

function isValidState(d) {
  return d && typeof d === "object" && typeof d.status === "string"
    && d.step != null && Array.isArray(d.agents);
}

async function readFileStates() {
  const states = {};
  let entries;
  try { entries = await fsp.readdir(SQUADS_DIR, { withFileTypes: true }); }
  catch { return states; }
  for (const e of entries) {
    if (!e.isDirectory()) continue;
    try {
      const raw = await fsp.readFile(path.join(SQUADS_DIR, e.name, "state.json"), "utf-8");
      const parsed = JSON.parse(raw);
      if (isValidState(parsed)) states[e.name] = parsed;
    } catch {}
  }
  return states;
}

async function buildSnapshot() {
  const [squads, fileStates] = await Promise.all([discoverSquads(), readFileStates()]);
  const activeStates = { ...fileStates };
  for (const [k, v] of pushedStates) activeStates[k] = v.state;
  return { type: "SNAPSHOT", squads, activeStates };
}

// ── WebSocket ────────────────────────────────────────────────────────────────
const httpServer = createServer();
const wss = new WebSocketServer({ noServer: true });

httpServer.on("upgrade", (req, socket, head) => {
  if (req.url === "/__squads_ws") {
    wss.handleUpgrade(req, socket, head, ws => wss.emit("connection", ws));
  } else {
    socket.destroy();
  }
});

wss.on("connection", async ws => {
  try { ws.send(JSON.stringify(await buildSnapshot())); } catch {}
});

function broadcast(msg) {
  const data = JSON.stringify(msg);
  for (const c of wss.clients) {
    if (c.readyState === WebSocket.OPEN) try { c.send(data); } catch {}
  }
}

// ── Static file serving ──────────────────────────────────────────────────────
const MIME = {
  ".html": "text/html; charset=utf-8",
  ".js": "application/javascript", ".mjs": "application/javascript",
  ".css": "text/css", ".json": "application/json",
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml", ".ico": "image/x-icon",
  ".woff": "font/woff", ".woff2": "font/woff2",
};

async function serveStatic(req, res) {
  let urlPath = (req.url ?? "/").split("?")[0];
  if (urlPath === "/" || !path.extname(urlPath)) urlPath = "/index.html";
  const filePath = path.resolve(STATIC_DIR, "." + urlPath);
  if (!filePath.startsWith(STATIC_DIR)) { res.writeHead(403); res.end("Forbidden"); return; }
  try {
    const content = await fsp.readFile(filePath);
    const ext = path.extname(filePath).toLowerCase();
    res.setHeader("Content-Type", MIME[ext] ?? "application/octet-stream");
    res.setHeader("Cache-Control", ext === ".html" ? "no-cache" : "public, max-age=604800, immutable");
    res.writeHead(200);
    res.end(content);
  } catch {
    // SPA fallback
    try {
      const index = await fsp.readFile(path.join(STATIC_DIR, "index.html"));
      res.setHeader("Content-Type", "text/html; charset=utf-8");
      res.setHeader("Cache-Control", "no-cache");
      res.writeHead(200);
      res.end(index);
    } catch {
      res.writeHead(404); res.end("Not found");
    }
  }
}

// ── HTTP routing ─────────────────────────────────────────────────────────────
httpServer.on("request", async (req, res) => {
  const url = req.url ?? "/";

  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") { res.writeHead(204); res.end(); return; }

  // GET /health
  if (req.method === "GET" && url === "/health") {
    res.writeHead(200); res.end("OK"); return;
  }

  // GET /api/snapshot
  if (req.method === "GET" && url === "/api/snapshot") {
    try {
      const snap = await buildSnapshot();
      res.setHeader("Content-Type", "application/json");
      res.setHeader("Cache-Control", "no-cache");
      res.writeHead(200);
      res.end(JSON.stringify(snap));
    } catch { res.writeHead(500); res.end("Internal Server Error"); }
    return;
  }

  // POST /api/push-state/:squadName
  const pushMatch = url.match(/^\/api\/push-state\/([^/?]+)/);
  if (req.method === "POST" && pushMatch) {
    const squadName = decodeURIComponent(pushMatch[1]);
    let body = "";
    req.on("data", chunk => { body += chunk; });
    req.on("end", () => {
      try {
        const state = JSON.parse(body);
        if (!isValidState(state)) { res.writeHead(400); res.end("Invalid state"); return; }
        pushedStates.set(squadName, { state, pushedAt: Date.now() });
        broadcast({ type: "SQUAD_UPDATE", squad: squadName, state });
        res.writeHead(204); res.end();
      } catch { res.writeHead(400); res.end("Bad request"); }
    });
    return;
  }

  await serveStatic(req, res);
});

httpServer.listen(PORT, () => {
  console.log(`[dashboard] http://localhost:${PORT}`);
  console.log(`[dashboard] squads: ${SQUADS_DIR}`);
  console.log(`[dashboard] static: ${STATIC_DIR}`);
});
