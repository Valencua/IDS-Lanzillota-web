from flask import Blueprint, render_template, request, redirect, url_for, session

from web.routes.admin.auth import admin_required, redirigir_a_login_sin_sesion
from web.services.docentes import (
    obtener_docentes,
    crear_docente,
    actualizar_docente,
    eliminar_docente,
    archivo_a_data_uri,
)

equipo_bp = Blueprint('equipo', __name__)

def _resultado_o_redirect(resultado):
    if resultado.get('ok'):
        return redirect(url_for('web.admin.equipo.index'))

    if resultado.get('unauthorized'):
        return redirigir_a_login_sin_sesion()

    return None

@equipo_bp.route('/equipo', methods=['GET', 'POST'])
@admin_required
def index():
    error = None

    if request.method == 'POST':
        email = request.form.get('email', '').strip() or None
        foto = archivo_a_data_uri(request.files.get('foto'))

        resultado = crear_docente(session.get('token'), {
            'nombre': request.form.get('nombre', '').strip(),
            'apellido': request.form.get('apellido', '').strip(),
            'rol': request.form.get('rol', '').strip(),
            'email': email,
            'foto': foto,
        })

        redireccion = _resultado_o_redirect(resultado)
        if redireccion:
            return redireccion

        error = resultado.get('error')

    return render_template(
        'admin/equipo.html',
        docentes=obtener_docentes(),
        error=error,
    )

@equipo_bp.route('/equipo/<int:docente_id>/editar', methods=['POST'])
@admin_required
def editar(docente_id):
    email = request.form.get('email', '').strip() or None
    foto = archivo_a_data_uri(request.files.get('foto'))

    datos = {
        'nombre': request.form.get('nombre', '').strip(),
        'apellido': request.form.get('apellido', '').strip(),
        'rol': request.form.get('rol', '').strip(),
        'email': email,
    }
    if foto:
        datos['foto'] = foto

    resultado = actualizar_docente(session.get('token'), docente_id, datos)
    redireccion = _resultado_o_redirect(resultado)
    if redireccion:
        return redireccion

    return render_template(
        'admin/equipo.html',
        docentes=obtener_docentes(),
        error=resultado.get('error'),
    )


@equipo_bp.route('/equipo/<int:docente_id>/eliminar', methods=['POST'])
@admin_required
def eliminar(docente_id):
    resultado = eliminar_docente(session.get('token'), docente_id)
    redireccion = _resultado_o_redirect(resultado)
    if redireccion:
        return redireccion

    return render_template(
        'admin/equipo.html',
        docentes=obtener_docentes(),
        error=resultado.get('error'),
    )