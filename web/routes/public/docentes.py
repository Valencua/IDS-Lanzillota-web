from flask import Blueprint, render_template

from web.constants import DOCENTES

docentes_bp = Blueprint('docentes', __name__)


@docentes_bp.route('/docentes')
def index():
    return render_template('public/docentes.html', docentes=DOCENTES)
