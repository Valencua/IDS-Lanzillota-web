---
name: manage-secrets
description: Generate and rotate the frontend secrets (Flask SECRET_KEY and the shared API_KEY)
allowed-tools:
  - exec
permissions:
  allow:
    - Exec(python*)
---

Generate or rotate the secrets for `ids-web`. **Never** print or commit real values into tracked
files — only output them for the user to paste into their local `.env` and the Vercel dashboard.

## Secrets

### `SECRET_KEY` (Flask session signing, ids-web only)
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Rotating it invalidates existing sessions (users must log in again). It is **not** shared with anyone.

### `API_KEY` (shared with `ids-api`)
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
This value must be the **same** in:
- `ids-web` → env `API_KEY` (sent as `X-API-Key`).
- `ids-api` → env `API_KEY`.
- The Bruno collection → its `api_key` environment variable.

## Rotation (API_KEY)

Rotate it **everywhere at once** to avoid `401`s:
1. Generate the new value.
2. Update `ids-web` and `ids-api` (both local `.env` and both Vercel projects) **together**.
3. Update the Bruno `api_key` variable.
4. Redeploy both services if already deployed.

> ⚠️ If you change `API_KEY` in `ids-api` but not in `ids-web` (or vice versa), the frontend gets
> `401` on every call to the API.

## Notes

- On Vercel, set these as environment variables in the dashboard, not via `.env`.
- `ids-web` does NOT have `JWT_SECRET`: it never signs tokens, only relays the JWT from `/login`.
