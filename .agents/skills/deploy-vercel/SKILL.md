---
name: deploy-vercel
description: Checklist to deploy the frontend to Vercel (config and required environment variables)
allowed-tools:
  - read
  - grep
  - glob
permissions:
  allow:
    - Read(**)
---

Guide the deploy of `ids-web` to Vercel. Mostly a checklist; do not commit secrets.

## Config

- `vercel.json` defines a Python function over `app.py` with `includeFiles: "**"` — needed because
  a server-rendered frontend must bundle `templates/` and `static/` (unlike an API).
- `app.py` builds absolute paths (`BASE_DIR`) for `templates/`/`static/` so they resolve on Vercel.

## Environment variables (Vercel dashboard, NOT via .env)

- `SECRET_KEY` — long random value (`python -c "import secrets; print(secrets.token_hex(32))"`).
- `API_BASE_URL` — URL of the **deployed** `ids-api` (e.g. `https://<api>.vercel.app/ids_api`), not
  `localhost`.
- `API_KEY` — same value as `ids-api` (only if the API enforces it).

## Notes

- The frontend has no database; it depends on `ids-api` being reachable at `API_BASE_URL`.
- Public pages degrade gracefully if the API is down; the admin panel needs the API to log in.
