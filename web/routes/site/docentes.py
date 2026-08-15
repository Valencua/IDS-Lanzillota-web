from flask import Blueprint, render_template

from web.services.docentes import obtener_docentes

docentes_bp = Blueprint('docentes', __name__)


@docentes_bp.route('/docentes')
def index():
    return render_template('site/docentes.html', docentes=obtener_docentes())
