"""Blueprint padre para la zona de administración (requiere login).

Anida sub-blueprints definidos en otros módulos para mantener cada
sección en su propio archivo.
"""
from flask import Blueprint

from web.routes.admin.auth import auth_bp
from web.routes.admin.panel import panel_bp
from web.routes.admin.equipo import equipo_bp
from web.routes.admin.calendario import calendario_bp

admin_bp = Blueprint('admin', __name__)
admin_bp.register_blueprint(auth_bp)
admin_bp.register_blueprint(panel_bp)
admin_bp.register_blueprint(equipo_bp)
admin_bp.register_blueprint(calendario_bp)
