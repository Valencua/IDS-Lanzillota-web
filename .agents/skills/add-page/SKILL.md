---
name: add-page
description: Add a page/route to the frontend (Flask blueprint + Jinja template, optionally consuming ids-api)
argument-hint: "[zone and page, e.g. 'site/novedades' or 'admin/reportes']"
allowed-tools:
  - read
  - edit
  - write
  - grep
  - glob
  - exec
permissions:
  allow:
    - Read(**)
    - Exec(python -m compileall*)
    - Exec(python*)
  ask:
    - Write(web/**)
    - Write(templates/**)
---

Add a new page: **$ARGUMENTS**. Read `AGENTS.md` first and mirror the existing pages.

## Checklist

1. **Route** in the right blueprint:
   - Public → `web/routes/site/<pagina>.py` (registered in `web/routes/site/__init__.py`).
   - Admin → `web/routes/admin/<pagina>.py` (registered in `web/routes/admin/__init__.py`), and
     protect it with `@admin_required`.
   Keep the route thin: it renders a template and delegates any API call to a service.

2. **Template** in `templates/site/<pagina>.html` or `templates/admin/<pagina>.html`, extending
   `base.html`. Guard optional/empty data with `{% if %}` so it renders cleanly when the API has
   no data.

3. **Service** (only if the page needs data from `ids-api`): add a function in
   `web/services/<recurso>.py` that calls the API with `requests` + `api_headers(...)`. **Degrade
   gracefully**: on any non-200, return empty/fallback (don't raise). For admin writes, send
   `Authorization: Bearer {session['token']}` (merged via `api_headers`).

4. **Navigation**: add the link in `templates/base.html` (navbar) with `url_for('web.site.<x>...'`
   / `web.admin.<x>...`) if the page should be reachable from the menu.

5. **Verify:**
   ```bash
   python -m compileall -q web app.py
   python -c "import jinja2, pathlib; env=jinja2.Environment(); [env.parse(p.read_text(encoding='utf-8')) for p in pathlib.Path('templates').rglob('*.html')]; print('templates OK')"
   ```

Report the files added/changed. Note: static domain data (links, bibliography) lives in
`web/constants.py`; only docentes/cronograma come from the API.
