"""Consumo de la API (ids-api) para el cronograma."""
import logging
from datetime import datetime

import requests

from web.constants import API_BASE_URL, api_headers

logger = logging.getLogger(__name__)

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
        'hitos': hitos,
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
        response = requests.get(f'{API_BASE_URL}/cronograma/clases', headers=api_headers(), timeout=10)

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
            headers=api_headers({'Authorization': f'Bearer {token}'}),
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

    for hito in form.getlist('hito'):
        texto = hito.strip()
        if texto:
            contenidos.append({'texto': texto, 'hito': True})

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


def descargar_csv() -> dict:
    """Proxy de GET /cronograma/csv: devuelve el archivo tal cual lo arma la API."""
    try:
        response = requests.get(f'{API_BASE_URL}/cronograma/csv', headers=api_headers(), timeout=15)
        if response.status_code == 200:
            return {
                'ok': True,
                'contenido': response.content,
                'disposition': response.headers.get(
                    'Content-Disposition',
                    'attachment; filename="cronograma.csv"',
                ),
            }
        return {'ok': False, 'error': _mensaje_error_api(response)}
    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
        return {'ok': False, 'error': 'No se pudo conectar con el servidor. Intentá más tarde.'}
    except Exception as e:
        logger.error(f"Error al descargar el cronograma: {e}")
        return {'ok': False, 'error': 'Ocurrió un error al descargar el calendario.'}

def publicar_csv(token: str, archivo) -> dict:
    """Reemplaza el cronograma vía PUT /cronograma/csv (archivo tal cual)."""
    if not archivo or not archivo.filename:
        return {'ok': False, 'error': 'Elegí un archivo CSV para publicar.'}
    try:
        response = requests.put(
            f'{API_BASE_URL}/cronograma/csv',
            files={'archivo': (archivo.filename, archivo.stream, 'text/csv')},
            headers=api_headers({'Authorization': f'Bearer {token}'}),
            timeout=30,
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
        logger.error(f"Error al publicar el CSV: {e}")
        return {'ok': False, 'error': 'Ocurrió un error al publicar el calendario.'}
