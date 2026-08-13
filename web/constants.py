SEMANAS = [
    {"semana": 1, "clases": [
        {"fecha": "09/03", "nro": 1, "tipo": "Presencial", "titulo": "Introducción a la materia",
         "contenidos": ["Presentación de la materia", "Introducción a Linux (FileSystem, carpetas)", "Terminal y comandos básicos (cd, ls, cat, cp, mv, sudo...)"],
         "entrega": "Entrega del enunciado TP1"},
        {"fecha": "11/03", "nro": 2, "tipo": "Virtual", "titulo": "Instalación de Linux",
         "contenidos": ["Opciones de instalación (WSL, VM, Dual boot)", "Repaso general de comandos", "¿Qué es bash?", "Variables de entorno", "Estructuras condicionales e iterativas", "Mi primer script"]},
    ]},
    {"semana": 2, "clases": [
        {"fecha": "16/03", "nro": 3, "tipo": "Virtual", "titulo": "Continuación Bash",
         "contenidos": ["Estructuras condicionales e iterativas", "Pipelines, redirecciones, listas (&&, ||, ;)", "Scripts (búsqueda, reemplazo, manejo de archivos)"]},
        {"fecha": "18/03", "nro": 4, "tipo": "Virtual", "titulo": "Git",
         "contenidos": ["Repositorios y estados", "Comandos básicos (status, add, commit, push, pull, clone)", "Github: asociar SSH, subir repositorio"]},
    ]},
    {"semana": 3, "clases": [
        {"fecha": "23/03", "nro": 5, "tipo": "Feriado"},
        {"fecha": "25/03", "nro": 6, "tipo": "Presencial", "titulo": "Ejercitación TP1 (obligatoria)",
         "contenidos": ["Ejercitación integral de comandos", "Consultas Linux", "Ejercicios de scripting"],
         "entrega": "Clase obligatoria: resolución del ejercicio TP1 de bash"},
    ]},
    {"semana": 4, "clases": [
        {"fecha": "30/03", "nro": 7, "tipo": "Virtual", "titulo": "Python + Flask",
         "contenidos": ["Repaso Python", "Instalación de Flask", "Introducción a Flask"]},
        {"fecha": "01/04", "nro": 8, "tipo": "Virtual", "titulo": "API RESTful",
         "contenidos": ["¿Qué es una API?", "¿Qué es REST?", "Ejemplo"],
         "entrega": "Entrega enunciado TP2 BackEnd"},
    ]},
    {"semana": 5, "clases": [
        {"fecha": "06/04", "nro": 9, "tipo": "Virtual", "titulo": "SQL",
         "contenidos": ["¿Qué es una BDD? ¿Qué es SQL?", "BDD relacionales", "CREATE / DROP TABLE", "SELECT-FROM-WHERE"]},
        {"fecha": "08/04", "nro": 10, "tipo": "Virtual", "titulo": "SQL (parte 2)",
         "contenidos": ["Tipos de datos", "INSERT, UPDATE, DELETE", "AUTO_INCREMENT, PK"]},
    ]},
    {"semana": 6, "clases": [
        {"fecha": "13/04", "nro": 11, "tipo": "Virtual", "titulo": "Git avanzado",
         "contenidos": ["Ramas (checkout, branch)", "git restore, staging", "git log y git diff", "Github Project"]},
        {"fecha": "15/04", "nro": 12, "tipo": "Virtual", "titulo": "Metodologías ágiles",
         "contenidos": ["Introducción a la agilidad", "Kanban", "Herramientas (Jira, Trello, Asana, Basecamp...)"]},
    ]},
    {"semana": 7, "clases": [
        {"fecha": "20/04", "nro": 13, "tipo": "Presencial", "titulo": "Ejercitación Backend",
         "contenidos": ["Ejercitación integral de Backend"],
         "entrega": "Clase obligatoria TP N°2"},
        {"fecha": "22/04", "nro": 14, "tipo": "Sin clases", "titulo": "Elecciones en FIUBA (no hay clases)"},
    ]},
    {"semana": 8, "clases": [
        {"fecha": "27/04", "nro": 15, "tipo": "Virtual", "titulo": "Consultas primer parcial",
         "contenidos": ["Repaso y consultas previas al parcial"]},
        {"fecha": "29/04", "nro": 16, "tipo": "Presencial", "titulo": "Parcial",
         "contenidos": ["Primer parcial"]},
    ]},
    {"semana": 9, "clases": [
        {"fecha": "04/05", "nro": 17, "tipo": "Virtual", "titulo": "Introducción a Front End",
         "contenidos": ["Intro a HTML", "Intro a CSS", "Intro a JavaScript", "Mi primer código en Flask"],
         "entrega": "Entrega enunciado TP Integrador"},
        {"fecha": "06/05", "nro": 18, "tipo": "Virtual", "titulo": "Front End con Flask",
         "contenidos": ["Flask con HTML + CSS (ejemplo asistido)"]},
    ]},
    {"semana": 10, "clases": [
        {"fecha": "11/05", "nro": 19, "tipo": "Virtual", "titulo": "HTML y CSS",
         "contenidos": ["HTML: estructura y etiquetas básicas", "CSS: clases e IDs, atributos básicos", "Flexbox (direction, justify, align)"]},
        {"fecha": "13/05", "nro": 20, "tipo": "Virtual", "titulo": "JavaScript + HTML",
         "contenidos": ["JavaScript + HTML continuación", "Ejercitación"],
         "entrega": "Entrega parcial TP Integrador: alcance, backlog y mockup"},
    ]},
    {"semana": 11, "clases": [
        {"fecha": "18/05", "nro": 21, "tipo": "Presencial", "titulo": "Integración Front + Backend",
         "contenidos": ["Ejercitación integral Front + Backend", "Crear API consumiendo datos de una base", "SQL Joins"]},
        {"fecha": "20/05", "nro": 22, "tipo": "Virtual", "titulo": "Debugging + Testing",
         "contenidos": ["Debugging", "Testing"],
         "entrega": "Entrega parcial TP Integrador: listado de endpoints y backend"},
    ]},
    {"semana": 12, "clases": [
        {"fecha": "25/05", "nro": 23, "tipo": "Feriado"},
        {"fecha": "27/05", "nro": 24, "tipo": "Virtual", "titulo": "TP Integrador",
         "contenidos": ["Trabajo sobre el TP Integrador"],
         "entrega": "Entrega parcial: endpoints y backend"},
    ]},
    {"semana": 13, "clases": [
        {"fecha": "01/06", "nro": 25, "tipo": "Virtual", "titulo": "Docker",
         "contenidos": ["¿Qué es Docker? Diferencia con VM", "Container vs imagen", "Comandos básicos (run, ps, exec, images, pull...)"]},
        {"fecha": "03/06", "nro": 26, "tipo": "Presencial", "titulo": "Consultas del TP",
         "contenidos": ["Consultas del TP"],
         "entrega": "Entrega parcial: templates e integración front con backend"},
    ]},
    {"semana": 14, "clases": [
        {"fecha": "08/06", "nro": 27, "tipo": "Virtual", "titulo": "Docker (parte 2) + Compose",
         "contenidos": ["Dockerfile, volúmenes y puertos", "docker build", "Docker Compose (compose.yaml)", "Comandos (build, up, stop, down)"]},
        {"fecha": "10/06", "nro": 28, "tipo": "Presencial", "titulo": "1er Recuperatorio",
         "contenidos": ["Primer recuperatorio"]},
    ]},
    {"semana": 15, "clases": [
        {"fecha": "15/06", "nro": 29, "tipo": "Feriado"},
        {"fecha": "17/06", "nro": 30, "tipo": "Presencial", "titulo": "Entrega TP Integrador",
         "contenidos": ["1er Entrega TP Integrador y Defensa"]},
    ]},
    {"semana": 16, "clases": [
        {"fecha": "22/06", "nro": 31, "tipo": "Presencial", "titulo": "Defensas y consultas TP",
         "entrega": "Defensas presenciales y consultas TP"},
        {"fecha": "24/06", "nro": 32, "tipo": "Presencial", "titulo": "2da Entrega TP Integrador",
         "contenidos": ["2da entrega TP Integrador y Defensa"]},
    ]},
]

DOCENTES = [
    {"nombre": "Nestor", "apellido": "Palaveccino",  "rol": "Ayudante", "foto": "docentes/nestor.jpg"},
    {"nombre": "Chaves", "apellido": "Leonel", "rol": "Ayudante", "foto": "docentes/leonel.jpg"},
    {"nombre": "Bruno", "apellido": "Lanzillotta",  "rol": "Profesor", "foto": "docentes/bruno.jpg"},
    {"nombre": "Cristian Martin", "apellido": "Sosa", "rol": "Ayudante", "foto": "docentes/cristian.jpg"},
    {"nombre": "Tomás", "apellido": "Villegas", "rol": "Ayudante", "foto": "docentes/tomas.jpg"},
]

BIBLIOGRAFIA = [
    {"texto": "Bash Beginners Guide - Machtelt Garrels"},
    {"texto": "Communicating the User Experience - Richard Caddick, Steve Cable"},
    {"texto": "Introduction to Linux - Machtelt Garrels"},
    {"texto": "Test Driven Development By Example - Kent Beck"},
]

ENLACES = [
    {"texto": "Códigos EMMET", "url": "https://drive.google.com/file/d/1H0COwPY28acPIhz8fGGMpN467ZGMS4hg/view"},
    {"texto": "Comandos UNIX", "url": "https://drive.google.com/file/d/1e8wOwxJp9gc7uQw8JKKa4MT-BCDTqJaC/view"},
    {"texto": "MUO - How to Install Ubuntu on VMware Workstation", "url": "https://www.makeuseof.com/install-ubuntu-on-vmware-workstation/"},
    {"texto": "Instalación de WSL", "url": "https://learn.microsoft.com/es-es/windows/wsl/install"},
    {"texto": "WSL | Ubuntu", "url": "https://ubuntu.com/desktop/wsl"},
    {"texto": "Cómo instalar Ubuntu en un ordenador", "url": "https://www.hostinger.com.ar/tutoriales/como-instalar-ubuntu"},
    {"texto": "Exámenes pasados + cheat-sheets de git", "url": "https://drive.google.com/drive/folders/1GFYdrU_kwFVtWhygoDHgydbS3YLcCK_T?usp=sharing"},
]