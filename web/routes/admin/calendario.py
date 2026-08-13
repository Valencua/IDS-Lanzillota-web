from flask import Blueprint, render_template
from web.routes.admin.auth import admin_required
from web.constants import SEMANAS

calendario_bp = Blueprint('calendario', __name__)


@calendario_bp.route('/calendario')
@admin_required
def index():
    return render_template('admin/calendario.html', semanas=SEMANAS)
