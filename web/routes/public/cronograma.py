from flask import Blueprint, render_template

from web.services.cronograma import obtener_semanas

cronograma_bp = Blueprint('cronograma', __name__)


@cronograma_bp.route('/cronograma')
def index():
    return render_template('public/cronograma.html', semanas=obtener_semanas())