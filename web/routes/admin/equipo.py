from flask import Blueprint, render_template

from web.constants import DOCENTES
from web.routes.admin.auth import admin_required

equipo_bp = Blueprint('equipo', __name__)


@equipo_bp.route('/equipo')
@admin_required
def index():
    return render_template('admin/equipo.html', docentes=DOCENTES)
