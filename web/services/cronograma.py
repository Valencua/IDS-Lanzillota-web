"""Consumo de la API (ids-api) para el cronograma."""
import csv
import io
import logging
from datetime import datetime

import requests

from web.constants import API_BASE_URL

logger = logging.getLogger(__name__)

CSV_HEADER = ['semana', 'fecha', 'tipo', 'titulo', 'contenidos', 'hito']


def _mensaje_error_api(response) -> str:
    try:
        data = response.json()
        errores = data.get('errors') or []
        if errores:
            textos = [
                e.get('description') or e.get('message') or ''
                for e in errores
            ]
            return ' '.join(t for t in textos if t) or 'Error de validación.'
    except Exception:
        pass
    return f'Error del servidor (HTTP {response.status_code}).'


def _unauthorized(response) -> dict | None:
    if response.status_code in (401, 403):
        return {
            'ok': False,
            'error': 'Sesión expirada. Volvé a iniciar sesión.',
            'unauthorized': True,
        }
    return None


def _fecha_iso_a_corta(fecha_iso: str) -> str:
    """2026-03-09 → 09/03 (lo que muestra la tabla)."""
    try:
        return datetime.strptime(str(fecha_iso)[:10], '%Y-%m-%d').strftime('%d/%m')
    except ValueError:
        return str(fecha_iso)


def _fecha_iso_a_csv(fecha_iso: str) -> str:
    """2026-03-09 → 09/03/2026."""
    try:
        return datetime.strptime(str(fecha_iso)[:10], '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        return str(fecha_iso)


def _clase_para_vista(clase: dict) -> dict:
    """Adapta el DTO de la API al formato de la tabla (contenidos + hito en rojo)."""
    items = clase.get('contenidos') or []
    contenidos = []
    hitos = []

    for item in items:
        if isinstance(item, str):
            if item.strip():
                contenidos.append(item.strip())
            continue
        texto = str(item.get('texto') or '').strip()
        if not texto:
            continue
        if item.get('hito'):
            hitos.append(texto)
        else:
            contenidos.append(texto)

    fecha_iso = clase.get('fecha') or ''

    return {
        'id': clase.get('id'),
        'semana': clase.get('semana'),
        'fecha': _fecha_iso_a_corta(fecha_iso),
        'fecha_iso': str(fecha_iso)[:10],
        'tipo': clase.get('tipo') or '',
        'titulo': clase.get('titulo') or '',
        'contenidos': contenidos,
        'hito': ' · '.join(hitos),
    }


def _agrupar_semanas(clases: list[dict]) -> list[dict]:
    por_semana: dict[int, list[dict]] = {}

    for clase in clases:
        vista = _clase_para_vista(clase)
        semana = vista.get('semana') or 0
        por_semana.setdefault(semana, []).append(vista)

    return [
        {'semana': semana, 'clases': items}
        for semana, items in sorted(por_semana.items())
    ]


def obtener_semanas() -> list[dict]:
    """Lista el cronograma agrupado por semana, listo para la tabla."""
    try:
        response = requests.get(f'{API_BASE_URL}/cronograma/clases', timeout=10)

        if response.status_code == 200:
            return _agrupar_semanas(response.json() or [])

        if response.status_code == 204:
            return []

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
    except Exception as e:
        logger.error(f"Error al obtener el cronograma: {e}")

    return []


def actualizar_clase(token: str, clase_id: int, datos: dict) -> dict:
    """Actualiza una clase vía PUT /cronograma/clases/<id>."""
    try:
        response = requests.put(
            f'{API_BASE_URL}/cronograma/clases/{clase_id}',
            json=datos,
            headers={'Authorization': f'Bearer {token}'},
            timeout=15,
        )

        unauthorized = _unauthorized(response)
        if unauthorized:
            return unauthorized

        if response.status_code == 200:
            return {'ok': True}

        return {'ok': False, 'error': _mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
        return {'ok': False, 'error': 'No se pudo conectar con el servidor. Intentá más tarde.'}

    except Exception as e:
        logger.error(f"Error al actualizar la clase: {e}")
        return {'ok': False, 'error': 'Ocurrió un error al guardar la clase.'}


def body_desde_formulario(form) -> dict:
    """Arma el JSON de la API a partir del form de editar clase."""
    contenidos = []

    for linea in (form.get('contenidos') or '').splitlines():
        texto = linea.strip()
        if texto:
            contenidos.append({'texto': texto, 'hito': False})

    hito = (form.get('hito') or '').strip()
    if hito:
        contenidos.append({'texto': hito, 'hito': True})

    titulo = (form.get('titulo') or '').strip() or None
    semana_raw = (form.get('semana') or '').strip()
    semana = int(semana_raw) if semana_raw.isdigit() else semana_raw

    return {
        'semana': semana,
        'fecha': (form.get('fecha') or '').strip(),
        'tipo': (form.get('tipo') or '').strip(),
        'titulo': titulo,
        'contenidos': contenidos,
    }


def exportar_csv() -> str:
    """CSV en el formato del panel: semana,fecha,tipo,titulo,contenidos,hito."""
    salida = io.StringIO()
    escritor = csv.writer(salida)
    escritor.writerow(CSV_HEADER)

    try:
        response = requests.get(f'{API_BASE_URL}/cronograma/clases', timeout=10)
        clases = response.json() if response.status_code == 200 else []
    except Exception as e:
        logger.error(f"Error al exportar el cronograma: {e}")
        clases = []

    for clase in clases or []:
        vista = _clase_para_vista(clase)
        escritor.writerow([
            vista['semana'],
            _fecha_iso_a_csv(vista['fecha_iso']),
            vista['tipo'],
            vista['titulo'],
            ';'.join(vista['contenidos']),
            vista['hito'],
        ])

    return salida.getvalue()


def _csv_vista_a_api(contenido: str) -> str:
    """Convierte el CSV del panel al formato que espera la API (pares texto,True/False)."""
    filas = [f for f in csv.reader(io.StringIO(contenido)) if any(c.strip() for c in f)]

    if not filas:
        return contenido

    if filas[0] and filas[0][0].strip().lower() == 'semana':
        filas = filas[1:]

    salida = io.StringIO()
    escritor = csv.writer(salida)
    escritor.writerow(['semana', 'fecha', 'tipo', 'titulo'])

    for campos in filas:
        semana = campos[0].strip() if len(campos) > 0 else ''
        fecha = campos[1].strip() if len(campos) > 1 else ''
        tipo = campos[2].strip() if len(campos) > 2 else ''
        titulo = campos[3].strip() if len(campos) > 3 else ''
        contenidos_txt = campos[4].strip() if len(campos) > 4 else ''
        hito = campos[5].strip() if len(campos) > 5 else ''

        fila = [semana, fecha, tipo, titulo]
        for item in contenidos_txt.split(';'):
            texto = item.strip()
            if texto:
                fila.extend([texto, 'False'])
        if hito:
            fila.extend([hito, 'True'])

        escritor.writerow(fila)

    return salida.getvalue()


def publicar_csv(token: str, archivo) -> dict:
    """Reemplaza el cronograma vía PUT /cronograma/csv."""
    if not archivo or not archivo.filename:
        return {'ok': False, 'error': 'Elegí un archivo CSV para publicar.'}

    try:
        bruto = archivo.read()
        texto = bruto.decode('utf-8-sig')
        csv_api = _csv_vista_a_api(texto)

        response = requests.put(
            f'{API_BASE_URL}/cronograma/csv',
            files={'archivo': ('cronograma.csv', csv_api.encode('utf-8'), 'text/csv')},
            headers={'Authorization': f'Bearer {token}'},
            timeout=30,
        )

        unauthorized = _unauthorized(response)
        if unauthorized:
            return unauthorized

        if response.status_code == 200:
            return {'ok': True}

        return {'ok': False, 'error': _mensaje_error_api(response)}

    except UnicodeDecodeError:
        return {'ok': False, 'error': 'El CSV tiene que estar en UTF-8.'}

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
        return {'ok': False, 'error': 'No se pudo conectar con el servidor. Intentá más tarde.'}

    except Exception as e:
        logger.error(f"Error al publicar el CSV: {e}")
        return {'ok': False, 'error': 'Ocurrió un error al publicar el calendario.'}