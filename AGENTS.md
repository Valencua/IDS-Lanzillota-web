# AGENTS.md

Guide for agents (and people) working on **ids-web**. Keep it short and actionable.

## Overview

Server-rendered frontend (**Flask + Jinja2**) for the Lanzillotta "Introducción al Desarrollo de
Software" course site (FIUBA). Renders public pages and an admin panel, and consumes the backend
API **`ids-api`** over HTTP. It has **no database** of its own.

## How to run

```bash
setup_virtualenv.bat        # Windows
./setup_virtualenv.sh       # Linux / macOS

# or manually
python -m venv .venv && .venv\Scripts\activate   # (source .venv/bin/activate on Linux/macOS)
pip install -r requirements.txt
python app.py               # http://localhost:5001
```

Needs a `.env` (see `.env.example`). The admin panel requires `ids-api` running to log in; the
public pages degrade gracefully if the API is down.

## Environment (`.env`)

- `SECRET_KEY` — Flask session signing (random, ids-web only).
- `API_BASE_URL` — base URL of `ids-api` (default `http://localhost:5000/ids_api`).
- `API_KEY` — **shared** with `ids-api`; sent as the `X-API-Key` header. Empty if the API is public.

## Verification (run before considering a change done)

```bash
pip install -r requirements-dev.txt
pytest                        # tests de services (requests mockeado, sin red)
python -m compileall -q web app.py
python -c "import jinja2, pathlib; env=jinja2.Environment(); [env.parse(p.read_text(encoding='utf-8')) for p in pathlib.Path('templates').rglob('*.html')]; print('templates OK')"
```

Los tests cubren funciones puras, los services y las rutas (`test_client`) con `requests` mockeado
(`conftest.py` da las fixtures `respuesta_falsa` y `cargar_json`, y fija env dummy). No requieren
`ids-api` corriendo. Las respuestas de la API se guardan como **mocks JSON** en
`tests/resources/json/<dominio>/` y se cargan con `cargar_json` (patrón `<dominio>/<nombre>.json`).

## Code conventions

- **Functional style, no classes.** Data passed to templates as `dict`/`list`.
- **Spanish naming, no abbreviations** (self-explanatory variables).
- **Layers**: `routes` (Flask blueprints, presentation/flow) → `services` (HTTP calls to `ids-api`
  via `requests`). Routes hold no HTTP-client logic; services encapsulate the API calls.
- **Blueprints**: `web` → `site` (public pages, no prefix) + `admin` (`/admin`). Templates mirror
  this: `templates/site/` and `templates/admin/`.
- **All calls to `ids-api`** go through `web/services/*.py` and MUST include the API key via
  `api_headers()` (`web/constants.py`). **Public reads degrade gracefully**: on any non-200,
  return empty (`[]`/fallback) so the page still renders.
- **Admin auth**: `POST /login` on the API returns a JWT stored in `session['token']`; admin routes
  use `@admin_required` and send `Authorization: Bearer <token>`.

## Gotchas

- `API_KEY` must match `ids-api`'s (shared secret). Rotate it in both at once (see `manage-secrets`).
- `app.py` uses absolute paths (`BASE_DIR`) for `templates/` and `static/` so Vercel finds them.
- Vercel bundles everything (`includeFiles: "**"`) because it needs `templates/` and `static/`.
- Static domain data (links, bibliography) lives in `web/constants.py`; only docentes/cronograma
  come from the API.

## Deploy

Vercel (`vercel.json` → Python function over `app.py`, `includeFiles: "**"`). Set env vars in the
dashboard: `SECRET_KEY`, `API_BASE_URL` (the deployed API, not localhost), `API_KEY` (same as
`ids-api`).

## Git

- Commit messages in Spanish, focused on the "why".
- Do not push unless explicitly asked. The team merges to `main` via Pull Requests.

## Pointers

- Backend it consumes: `../ids-api` (see its `AGENTS.md` and `docs/swagger.yaml`).
