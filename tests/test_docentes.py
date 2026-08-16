import base64
from types import SimpleNamespace

import requests

from web.services import docentes


def _archivo_falso(filename='foto.png', contenido=b'abc', mimetype='image/png'):
    return SimpleNamespace(filename=filename, read=lambda: contenido, mimetype=mimetype)


# --- archivo_a_data_uri (función pura) ---

def test_archivo_a_data_uri_ok():
    data_uri = docentes.archivo_a_data_uri(_archivo_falso(contenido=b'abc', mimetype='image/png'))

    assert data_uri == 'data:image/png;base64,' + base64.b64encode(b'abc').decode('ascii')


def test_archivo_a_data_uri_jpg_se_normaliza():
    data_uri = docentes.archivo_a_data_uri(_archivo_falso(mimetype='image/jpg'))

    assert data_uri.startswith('data:image/jpeg;base64,')


def test_archivo_a_data_uri_vacio_es_none():
    assert docentes.archivo_a_data_uri(None) is None
    assert docentes.archivo_a_data_uri(_archivo_falso(filename='')) is None
    assert docentes.archivo_a_data_uri(_archivo_falso(contenido=b'')) is None


# --- obtener_docentes / crear_docente (requests mockeado) ---

def test_obtener_docentes_ok(monkeypatch, respuesta_falsa, cargar_json):
    lista = cargar_json('json/docentes/lista.json')
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: respuesta_falsa(200, lista))

    assert docentes.obtener_docentes() == lista


def test_obtener_docentes_error_devuelve_vacio(monkeypatch, respuesta_falsa):
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: respuesta_falsa(404))

    assert docentes.obtener_docentes() == []


def test_crear_docente_ok(monkeypatch, respuesta_falsa):
    monkeypatch.setattr(requests, 'post', lambda *args, **kwargs: respuesta_falsa(201))

    assert docentes.crear_docente('tok', {'nombre': 'Ada'}) == {'ok': True}


def test_crear_docente_no_autorizado(monkeypatch, respuesta_falsa):
    monkeypatch.setattr(requests, 'post', lambda *args, **kwargs: respuesta_falsa(401))

    resultado = docentes.crear_docente('tok', {'nombre': 'Ada'})

    assert resultado['ok'] is False and resultado['unauthorized'] is True


def test_crear_docente_error_muestra_mensaje(monkeypatch, respuesta_falsa, cargar_json):
    error = cargar_json('json/errors/email_duplicado.json')
    monkeypatch.setattr(requests, 'post', lambda *args, **kwargs: respuesta_falsa(409, error))

    resultado = docentes.crear_docente('tok', {'nombre': 'Ada'})

    assert resultado['ok'] is False
    assert resultado['error'] == 'El email ya está en uso por otro docente.'


def test_actualizar_docente_ok(monkeypatch, respuesta_falsa):
    monkeypatch.setattr(requests, 'put', lambda *args, **kwargs: respuesta_falsa(200))

    assert docentes.actualizar_docente('tok', 1, {'nombre': 'Ada'}) == {'ok': True}


def test_actualizar_docente_no_autorizado(monkeypatch, respuesta_falsa):
    monkeypatch.setattr(requests, 'put', lambda *args, **kwargs: respuesta_falsa(401))

    assert docentes.actualizar_docente('tok', 1, {})['unauthorized'] is True


def test_eliminar_docente_ok(monkeypatch, respuesta_falsa):
    monkeypatch.setattr(requests, 'delete', lambda *args, **kwargs: respuesta_falsa(204))

    assert docentes.eliminar_docente('tok', 1) == {'ok': True}


def test_eliminar_docente_error_muestra_mensaje(monkeypatch, respuesta_falsa):
    monkeypatch.setattr(
        requests, 'delete',
        lambda *args, **kwargs: respuesta_falsa(404, {'errors': [{'message': 'no existe'}]}),
    )

    resultado = docentes.eliminar_docente('tok', 1)

    assert resultado['ok'] is False and 'no existe' in resultado['error']
