"""Consumo de la API (ids-api) para los datos de docentes."""
import logging
import requests

from web.constants import API_BASE_URL

logger = logging.getLogger(__name__)


def obtener_docentes() -> list[dict]:
    """Consume la API para obtener la lista de docentes.

    Cada docente tiene la forma {id, nombre, apellido, email, rol, foto},
    donde `foto` es un data URI base64 (o None).

    Devuelve [] si la API no responde o no hay docentes (204).
    """
    try:
        response = requests.get(f'{API_BASE_URL}/docentes', timeout=10)

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f"No se pudo conectar con la API en {API_BASE_URL}")
    except Exception as e:
        logger.error(f"Error al obtener docentes: {e}")

    return []
