from flask import Blueprint, render_template, request, redirect, url_for, session, Response

from web.routes.admin.auth import admin_required
from web.services.cronograma import (
    obtener_semanas,
    actualizar_clase,
    body_desde_formulario,
    exportar_csv,
    publicar_csv,
)

calendario_bp = Blueprint('calendario', __name__)


def _si_no_autorizado(resultado):
    if resultado.get('unauthorized'):
        session.pop('token', None)
        session.pop('usuario', None)
        return redirect(url_for('web.admin.auth.login'))
    return None


@calendario_bp.route('/calendario', methods=['GET', 'POST'])
@admin_required
def index():
    error = None

    if request.method == 'POST':
        resultado = publicar_csv(session.get('token'), request.files.get('csv'))
        redir = _si_no_autorizado(resultado)
        if redir:
            return redir
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
    redir = _si_no_autorizado(resultado)
    if redir:
        return redir

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
    contenido = exportar_csv()
    return Response(
        contenido,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename="cronograma.csv"'},
    )