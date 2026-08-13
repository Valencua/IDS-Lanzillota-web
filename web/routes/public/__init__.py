"""Blueprint padre para la zona pública del sitio (sin login).

Anida sub-blueprints definidos en otros módulos para mantener cada
sección en su propio archivo.
"""
from flask import Blueprint

from web.routes.public.home import home_bp
from web.routes.public.cursada import cursada_bp
from web.routes.public.cronograma import cronograma_bp
from web.routes.public.docentes import docentes_bp
from web.routes.public.material import material_bp

public_bp = Blueprint('public', __name__)
public_bp.register_blueprint(home_bp)
public_bp.register_blueprint(cursada_bp)
public_bp.register_blueprint(cronograma_bp)
public_bp.register_blueprint(docentes_bp)
public_bp.register_blueprint(material_bp)
