"""Consumo de la API (ids-api) para los datos de docentes."""
import logging
import requests
import base64

from web.constants import API_BASE_URL, api_headers
from web.services.respuestas_api import mensaje_error_api, respuesta_no_autorizada

logger = logging.getLogger(__name__)


def obtener_docentes() -> list[dict]:
    """Consume la API para obtener la lista de docentes.

    Cada docente tiene la forma {id, nombre, apellido, email, rol, foto},
    donde `foto` es un data URI base64 (o None).

    Devuelve [] si la API no responde o no hay docentes (204).
    """
    try:
        response = requests.get(f'{API_BASE_URL}/docentes', headers=api_headers(), timeout=10)

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
    except Exception as error:
        logger.error(f"Error al obtener docentes: {error}")

    return []


def archivo_a_data_uri(archivo) -> str | None:
    """Convierte un FileStorage de Flask en data URI base64, o None si está vacío."""
    if not archivo or not archivo.filename:
        return None

    contenido = archivo.read()
    
    if not contenido:
        return None

    mime = archivo.mimetype or 'image/jpeg'
    
    if mime == 'image/jpg':
        mime = 'image/jpeg'

    codificado = base64.b64encode(contenido).decode('ascii')
    
    return f'data:{mime};base64,{codificado}'


def crear_docente(token: str, datos: dict) -> dict:
    """Crea un docente vía POST /docentes (requiere JWT admin)."""
    try:
        response = requests.post(
            f'{API_BASE_URL}/docentes',
            json=datos,
            headers=api_headers({'Authorization': f'Bearer {token}'}),
            timeout=15,
        )

        if response.status_code == 201:
            return {'ok': True}

        no_autorizada = respuesta_no_autorizada(response)
        
        if no_autorizada:
            return no_autorizada

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
        
        return {'ok': False, 'error': 'No se pudo conectar con el servidor. Intentá más tarde.'}

    except Exception as error:
        logger.error(f"Error al crear docente: {error}")
        
        return {'ok': False, 'error': 'Ocurrió un error al agregar el docente.'}


def actualizar_docente(token: str, docente_id: int, datos: dict) -> dict:
    """Actualiza un docente vía PUT /docentes/<id>."""
    try:
        response = requests.put(
            f'{API_BASE_URL}/docentes/{docente_id}',
            json=datos,
            headers=api_headers({'Authorization': f'Bearer {token}'}),
            timeout=15,
        )

        if response.status_code == 200:
            return {'ok': True}

        no_autorizada = respuesta_no_autorizada(response)
        
        if no_autorizada:
            return no_autorizada

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
        
        return {'ok': False, 'error': 'No se pudo conectar con el servidor. Intentá más tarde.'}

    except Exception as error:
        logger.error(f"Error al actualizar docente: {error}")
        
        return {'ok': False, 'error': 'Ocurrió un error al guardar el docente.'}


def eliminar_docente(token: str, docente_id: int) -> dict:
    """Elimina un docente vía DELETE /docentes/<id>."""
    try:
        response = requests.delete(
            f'{API_BASE_URL}/docentes/{docente_id}',
            headers=api_headers({'Authorization': f'Bearer {token}'}),
            timeout=10,
        )

        if response.status_code == 204:
            return {'ok': True}

        no_autorizada = respuesta_no_autorizada(response)
        
        if no_autorizada:
            return no_autorizada

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
        
        return {'ok': False, 'error': 'No se pudo conectar con el servidor. Intentá más tarde.'}

    except Exception as error:
        logger.error(f"Error al eliminar docente: {error}")
        
        return {'ok': False, 'error': 'Ocurrió un error al eliminar el docente.'}