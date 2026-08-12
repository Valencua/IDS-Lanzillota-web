# IDS-Lanzillota-web

Página informativa de la cátedra de Lanzillotta de **Introducción al Desarrollo de Software** (FIUBA).

Sitio web desarrollado con **Flask + Jinja**, con las secciones: Inicio, Cursada, Cronograma, Docentes y Material adicional.

## Tecnologías

- **Python 3.10+**
- **Flask 3.0.3** (servidor web y routing)
- **Jinja2 3.1.2** (motor de templates)
- **HTML + CSS** (sin frameworks de front)
- Tipografías vía Google Fonts: **Afacad**, **Akatab** y **DM Mono**
- Deploy en **Vercel**

## Instalación y ejecución local

```bash
# 1. Clonar el repositorio (rama develop)
git clone -b develop https://github.com/Valencua/IDS-Lanzillota-web.git
cd IDS-Lanzillota-web

# 2. Crear y activar un entorno virtual
python -m venv venv

#   Linux / macOS:
source venv/bin/activate

# 3. Instalar las dependencias
pip install -r requirements.txt

# 4. Levantar el servidor
python app.py
```
```
IDS-Lanzillota-web/
├── app.py                     
├── requirements.txt           # Dependencias de Python (Flask, Jinja2)
├── vercel.json                # Configuración de despliegue en Vercel
├── README.md
├── LICENSE
├── .gitignore
│
├── web/                       
│   ├── __init__.py
│   ├── constants.py           # Datos de las páginas (semanas, docentes, enlaces, etc.)
│   └── routes/
│       ├── __init__.py        # Blueprint principal "web"
│       └── index.py           # Rutas de todas las páginas
│
├── templates/                 # Templates para Jinja2
│   ├── base.html              # Layout base (navbar + bloques comunes)
│   ├── inicio.html            # Página de inicio
│   ├── cursada.html           # Contenidos y requisitos de la cursada
│   ├── cronograma.html        # Cronograma de clases
│   ├── docentes.html          # Equipo docente
│   └── material.html          # Material adicional (bibliografía y enlaces)
│
└── static/
    ├── css/
    │   └── styles.css         # Estilos de todo el sitio
    └── img/                   # Imágenes, íconos SVG y patrones
        ├── logo.png
        ├── docentes-banner.png
        ├── pattern.png / pattern2.png / books.svg   # Patrones de fondo
        ├── *.svg              # Íconos (slack, whatsapp, youtube, drive, meet, etc.)
        └── docentes/          # Fotos de los docentes
            ├── bruno.jpg
            ├── cristian.jpg
            ├── leonel.jpg
            ├── nestor.jpg
            └── tomas.jpg
