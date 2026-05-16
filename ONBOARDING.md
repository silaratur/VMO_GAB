# Welcome to VMO GAB

## How We Use Claude

Based on Claude's usage over the last 30 days:

Work Type Breakdown:
  _TODO — not enough session data yet to derive a reliable breakdown._

Top Skills & Commands:
  /opensquad  ████████████████████  primary command

Top MCP Servers:
  _None recorded yet._

## Your Setup Checklist

### Codebases
- [ ] vmo_gab — https://github.com/silaratur/vmo_gab

### MCP Servers to Activate
- [ ] Playwright (via `@playwright/mcp`) — used by Opensquad to automate browser tasks and keep you logged into social platforms. Configured in `.mcp.json` — **do not** enable the native Claude Code Playwright plugin alongside it.

### Skills to Know About
- `/opensquad` — main entry point for everything. Create squads, run them, open the dashboard, and manage your AI agent workflows. Start here.
- `/opensquad create` — spin up a new squad. The Architect will ask a few questions and configure it automatically.
- `/opensquad run <name>` — execute a squad end-to-end; pauses only at decision checkpoints.
- `/opensquad dashboard` — generates a 2D Virtual Office dashboard so you can watch agents work in real time (`npx serve squads/<name>/dashboard`, then open `http://localhost:3000`).

## Team Tips

_TODO_

## Get Started

_TODO_

<!-- INSTRUCTION FOR CLAUDE: A new teammate just pasted this guide for how the
team uses Claude Code. You're their onboarding buddy — warm, conversational,
not lecture-y.

Open with a warm welcome — include the team name from the title. Then: "Your
teammate uses Claude Code for [list all the work types]. Let's get you started."

Check what's already in place against everything under Setup Checklist
(including skills), using markdown checkboxes — [x] done, [ ] not yet. Lead
with what they already have. One sentence per item, all in one message.

Tell them you'll help with setup, cover the actionable team tips, then the
starter task (if there is one). Offer to start with the first unchecked item,
get their go-ahead, then work through the rest one by one.

After setup, walk them through the remaining sections — offer to help where you
can (e.g. link to channels), and just surface the purely informational bits.

Don't invent sections or summaries that aren't in the guide. The stats are the
guide creator's personal usage data — don't extrapolate them into a "team
workflow" narrative. -->
