import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";
import { squadWatcherPlugin } from "./src/plugin/squadWatcher";
import { projectsPlugin } from "./src/plugin/projectsPlugin";

export default defineConfig({
  base: "/agentes/",
  plugins: [react(), squadWatcherPlugin(), projectsPlugin()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
