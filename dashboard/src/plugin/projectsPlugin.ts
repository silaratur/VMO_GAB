import type { Plugin } from "vite";
import fs from "node:fs";
import fsp from "node:fs/promises";
import path from "node:path";
import type { IncomingMessage, ServerResponse } from "node:http";

function resolveProjectsSiteDir(): string {
  const candidates = [
    path.resolve(process.cwd(), "../squads/vmo-web-publisher/output/site"),
    path.resolve(process.cwd(), "squads/vmo-web-publisher/output/site"),
  ];
  for (const c of candidates) {
    if (fs.existsSync(c)) return c;
  }
  return candidates[0];
}

const MIME: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".css":  "text/css",
  ".js":   "application/javascript",
  ".png":  "image/png",
  ".jpg":  "image/jpeg",
  ".svg":  "image/svg+xml",
  ".ico":  "image/x-icon",
};

export function projectsPlugin(): Plugin {
  return {
    name: "vmo-projects-static",
    configureServer(server) {
      const siteDir = resolveProjectsSiteDir();

      server.middlewares.use(async (req: IncomingMessage, res: ServerResponse, next: () => void) => {
        const url = req.url ?? "/";

        // Only handle /projects/* routes
        if (!url.startsWith("/projects")) return next();

        // Strip /projects prefix to get the file path
        let filePath = url.slice("/projects".length) || "/";
        // Remove query strings
        filePath = filePath.split("?")[0];
        // Default to index.html
        if (filePath === "/" || filePath === "") filePath = "/index.html";

        const fullPath = path.join(siteDir, filePath);
        const ext = path.extname(fullPath).toLowerCase();

        try {
          const stat = await fsp.stat(fullPath);
          if (!stat.isFile()) return next();

          const content = await fsp.readFile(fullPath);
          const mime = MIME[ext] ?? "application/octet-stream";

          res.setHeader("Content-Type", mime);
          res.setHeader("Cache-Control", "no-cache");
          res.end(content);
        } catch {
          // File not found — let Vite handle it
          next();
        }
      });
    },
  };
}
