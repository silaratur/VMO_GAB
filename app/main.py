from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

app = FastAPI(title="VMO GAB API", version="1.0.0")

_env = Environment(loader=FileSystemLoader(str(Path(__file__).parent / "templates")), autoescape=True)

TEAMS = [
    {
        "name": "Backend",
        "description": "APIs e infraestrutura",
        "color": "color-purple",
        "members": [
            {"name": "Ana Lima", "initials": "AL", "role": "Tech Lead", "badge": "Lead", "badge_class": "lead", "color": "color-purple", "active": True},
            {"name": "Carlos Souza", "initials": "CS", "role": "Dev Senior", "badge": "Dev", "badge_class": "dev", "color": "color-blue", "active": True},
            {"name": "Fernanda Melo", "initials": "FM", "role": "Dev Pleno", "badge": "Dev", "badge_class": "dev", "color": "color-blue", "active": True},
        ],
    },
    {
        "name": "Frontend",
        "description": "Interfaces e experiência",
        "color": "color-blue",
        "members": [
            {"name": "João Alves", "initials": "JA", "role": "Tech Lead", "badge": "Lead", "badge_class": "lead", "color": "color-purple", "active": True},
            {"name": "Mariana Costa", "initials": "MC", "role": "Designer UI", "badge": "Design", "badge_class": "design", "color": "color-green", "active": True},
            {"name": "Pedro Nunes", "initials": "PN", "role": "Dev Junior", "badge": "Dev", "badge_class": "dev", "color": "color-blue", "active": False},
        ],
    },
    {
        "name": "Qualidade",
        "description": "Testes e garantia de qualidade",
        "color": "color-orange",
        "members": [
            {"name": "Sofia Rocha", "initials": "SR", "role": "QA Lead", "badge": "Lead", "badge_class": "lead", "color": "color-purple", "active": True},
            {"name": "Lucas Ferreira", "initials": "LF", "role": "QA Analyst", "badge": "QA", "badge_class": "qa", "color": "color-orange", "active": True},
        ],
    },
    {
        "name": "Produto",
        "description": "Estratégia e roadmap",
        "color": "color-green",
        "members": [
            {"name": "Beatriz Santos", "initials": "BS", "role": "Product Manager", "badge": "Lead", "badge_class": "lead", "color": "color-purple", "active": True},
            {"name": "Rafael Gomes", "initials": "RG", "role": "Designer UX", "badge": "Design", "badge_class": "design", "color": "color-green", "active": True},
        ],
    },
]


@app.get("/", tags=["status"])
def root():
    return {"status": "ok", "message": "VMO GAB API is running"}


@app.get("/health", tags=["status"])
def health():
    return {"status": "healthy"}


@app.get("/opensquad", response_class=HTMLResponse, tags=["dashboard"])
def opensquad():
    all_members = [m for team in TEAMS for m in team["members"]]
    html = _env.get_template("opensquad.html").render(
        teams=TEAMS,
        total_teams=len(TEAMS),
        total_members=len(all_members),
        active_members=sum(1 for m in all_members if m["active"]),
    )
    return HTMLResponse(content=html)
