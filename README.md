# ids-web

Página informativa de la cátedra de Lanzillotta de **Introducción al Desarrollo de Software** (FIUBA).

Sitio web desarrollado con **Flask + Jinja**, con las secciones públicas: Inicio, Cursada, Cronograma, Docentes y Material adicional; y un **panel de administración** protegido por login.

## Tecnologías

- **Python 3.10+**
- **Flask 3.0.3** (servidor web y routing)
- **Jinja2 3.1.2** (motor de templates)
- **python-dotenv 1.0.1** (carga de variables de entorno)
- **HTML + CSS + JavaScript** (sin frameworks de front)
- Tipografías vía Google Fonts: **Afacad**, **Akatab** y **DM Mono**
- Deploy en **Vercel**

## Variables de entorno

La aplicación necesita un archivo `.env` en la raíz del proyecto. Podés partir de la plantilla incluida:

```bash
# Linux / macOS
cp .env.example .env

# Windows
copy .env.example .env
```

| Variable         | Descripción                                                                    |
|------------------|--------------------------------------------------------------------------------|
| `SECRET_KEY`     | Clave usada por Flask para firmar las sesiones. Debe ser aleatoria.            |
| `API_BASE_URL`   | URL base de la API (ids-api). Opcional (default `http://localhost:5000/ids_api`). |

> Las credenciales del panel de administración **ya no viven en el frontend**: el
> login se valida contra la API (ids-api), que las guarda en su propio `.env`.

Para generar una `SECRET_KEY` aleatoria:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

> El archivo `.env` está en `.gitignore` y **no debe subirse al repositorio**.

## Instalación y ejecución local

### Opción A — Scripts de setup (recomendado)

Los scripts crean el entorno virtual, instalan las dependencias, generan el `.env` desde la plantilla y levantan la app automáticamente.

**Con virtualenv:**

```bash
# Windows
setup_virtualenv.bat

# Linux / macOS
chmod +x setup_virtualenv.sh
./setup_virtualenv.sh
```

**Con pipenv:**

```bash
# Windows
setup_pipenv.bat

# Linux / macOS
chmod +x setup_pipenv.sh
./setup_pipenv.sh
```

> Tras la primera ejecución, revisá el `.env` generado y completá `SECRET_KEY` (y, si tu API no corre en el default, `API_BASE_URL`).

### Opción B — Manual

```bash
# 1. Crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# 2. Instalar las dependencias
pip install -r requirements.txt

# 3. Configurar variables de entorno
cp .env.example .env             # y completar los valores

# 4. Levantar el servidor
python app.py
```

Una vez iniciada, la web estará disponible en `http://localhost:5001/`.

## Páginas

| Ruta                   | Acceso   | Descripción                                        |
|------------------------|----------|----------------------------------------------------|
| `/`                    | Público  | Inicio (hero terminal, enlaces y novedades)        |
| `/cursada`             | Público  | Contenidos y requisitos de la cursada              |
| `/cronograma`          | Público  | Cronograma de clases por semana                    |
| `/docentes`            | Público  | Equipo docente                                     |
| `/material-adicional`  | Público  | Bibliografía y enlaces de interés                  |
| `/admin/login`         | Público  | Formulario de login del panel de administración    |
| `/admin/`              | Privado  | Panel de administración (requiere login)           |
| `/admin/equipo`        | Privado  | Gestión del equipo docente                         |
| `/admin/calendario`    | Privado  | Gestión del calendario                             |
| `/admin/logout`        | Privado  | Cierra la sesión de administración                 |

## Panel de administración

El panel vive bajo el prefijo `/admin`. El login (`web/services/auth.py`) delega la verificación de credenciales en la API (`POST /login`), que devuelve un **JWT**. Ese token se guarda en la sesión (`session['token']`) y las rutas privadas usan el decorador `admin_required` (ver `web/routes/admin/auth.py`) para exigir su presencia; si no hay token, se redirige a `/admin/login`. El token se enviará como `Authorization: Bearer <token>` en las operaciones de administración contra la API.

## Estructura del proyecto

```
ids-web/
├── app.py                     # Entry point Flask (puerto 5001, logging + errorhandler 404)
├── requirements.txt           # Dependencias de Python (Flask, Jinja2, python-dotenv)
├── vercel.json                # Configuración de despliegue en Vercel
├── .env.example               # Plantilla de variables de entorno
├── setup_virtualenv.bat/.sh   # Scripts de setup con virtualenv
├── setup_pipenv.bat/.sh       # Scripts de setup con pipenv
├── README.md
├── LICENSE
├── .gitignore
│
├── web/
│   ├── __init__.py
│   ├── constants.py           # Datos de las páginas (semanas, docentes, enlaces, bibliografía)
│   └── routes/
│       ├── __init__.py        # Blueprint principal "web" + registro de sub-blueprints
│       ├── public/            # Sub-blueprint "public" (una sección por archivo)
│       │   ├── __init__.py    #   registra home / cursada / cronograma / docentes / material
│       │   ├── home.py        #   inicio (/)
│       │   ├── cursada.py     #   /cursada
│       │   ├── cronograma.py  #   /cronograma
│       │   ├── docentes.py    #   /docentes
│       │   └── material.py    #   /material-adicional
│       └── admin/             # Sub-blueprint "admin" (una sección por archivo)
│           ├── __init__.py    #   registra auth / panel / equipo / calendario
│           ├── auth.py        #   login, logout y decorador admin_required
│           ├── panel.py       #   dashboard (/admin/)
│           ├── equipo.py      #   /admin/equipo
│           └── calendario.py  #   /admin/calendario
│
├── templates/                 # Templates Jinja2
│   ├── base.html              # Layout base (navbar + bloques comunes)
│   ├── 404.html               # Página de error 404
│   ├── public/                # Vistas públicas
│   │   ├── inicio.html        # Página de inicio
│   │   ├── cursada.html       # Contenidos y requisitos de la cursada
│   │   ├── cronograma.html    # Cronograma de clases
│   │   ├── docentes.html      # Equipo docente
│   │   └── material.html      # Material adicional (bibliografía y enlaces)
│   └── admin/                 # Vistas del panel de administración
│       ├── login.html         # Login del panel de admin
│       ├── panel.html         # Dashboard del panel de admin
│       ├── equipo.html        # Gestión del equipo docente
│       └── calendario.html    # Gestión del calendario
│
└── static/
    ├── css/
    │   └── styles.css         # Estilos de todo el sitio
    ├── js/
    │   └── main.js            # Interacciones del front (menú, modal, etc.)
    └── img/                   # Imágenes, íconos SVG y patrones
        ├── logo.png
        ├── docentes-banner.png
        ├── *.svg              # Íconos (slack, whatsapp, youtube, drive, meet, etc.)
        └── docentes/          # Fotos de los docentes
```
