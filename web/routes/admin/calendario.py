from flask import Blueprint, render_template, request, redirect, url_for, session, Response

from web.routes.admin.auth import admin_required, redirigir_a_login_sin_sesion
from web.services.cronograma import (
    obtener_semanas,
    actualizar_clase,
    body_desde_formulario,
    descargar_csv,
    publicar_csv,
)

calendario_bp = Blueprint('calendario', __name__)


def _redireccion_si_no_autorizado(resultado):
    if resultado.get('unauthorized'):
        return redirigir_a_login_sin_sesion()
    return None


@calendario_bp.route('/calendario', methods=['GET', 'POST'])
@admin_required
def index():
    error = None

    if request.method == 'POST':
        resultado = publicar_csv(session.get('token'), request.files.get('csv'))
        redireccion = _redireccion_si_no_autorizado(resultado)
        if redireccion:
            return redireccion
        if resultado.get('ok'):
            return redirect(url_for('web.admin.calendario.index'))
        error = resultado.get('error')

    return render_template(
        'admin/calendario.html',
        semanas=obtener_semanas(),
        error=error,
    )


@calendario_bp.route('/calendario/<int:clase_id>/editar', methods=['POST'])
@admin_required
def editar(clase_id):
    resultado = actualizar_clase(
        session.get('token'),
        clase_id,
        body_desde_formulario(request.form),
    )
    redireccion = _redireccion_si_no_autorizado(resultado)
    if redireccion:
        return redireccion

    if resultado.get('ok'):
        return redirect(url_for('web.admin.calendario.index'))

    return render_template(
        'admin/calendario.html',
        semanas=obtener_semanas(),
        error=resultado.get('error'),
    )


@calendario_bp.route('/calendario/csv')
@admin_required
def descargar():
    resultado = descargar_csv()
    if not resultado.get('ok'):
        return render_template(
            'admin/calendario.html',
            semanas=obtener_semanas(),
            error=resultado.get('error'),
        )

    return Response(
        resultado['contenido'],
        mimetype='text/csv',
        headers={'Content-Disposition': resultado['disposition']},
    )