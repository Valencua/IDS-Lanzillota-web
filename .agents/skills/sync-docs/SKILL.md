---
name: sync-docs
description: Audit and update README.md so the documentation matches the current frontend code
allowed-tools:
  - read
  - edit
  - grep
  - glob
permissions:
  allow:
    - Read(**)
  ask:
    - Write(README.md)
---

Keep `README.md` in sync with the code. **Only touch documentation** — never change app code here.
(`ids-web` has no OpenAPI spec; the API contract is documented in `../ids-api/docs/swagger.yaml`.)

## Sources of truth

- `app.py` and `web/routes/**` — registered blueprints, pages and URL prefixes (`site`, `/admin`).
- `web/constants.py` — env vars read (`API_BASE_URL`, `API_KEY`) and static page data.
- `web/services/**` — which data comes from `ids-api`.
- `.env.example` — the full set of environment variables.
- `vercel.json` — deploy config.

## What to check and fix in `README.md`

- **Environment variables** table lists exactly what the app reads (`SECRET_KEY`, `API_BASE_URL`,
  `API_KEY`) with defaults, matching `.env.example`.
- **Project structure** tree reflects the real files/dirs (`web/routes/site`, `web/routes/admin`,
  `web/services`, `templates/site`, `templates/admin`, `.agents/`, etc.).
- **Pages/routes** description matches the actual blueprints and pages.
- **Setup / deploy** steps match the scripts and `vercel.json`.
- No stale references (removed pages, old folder names like `public`, old env vars).

## Deliverable

Report the mismatches found and the fixes applied. If everything was already consistent, say so.
