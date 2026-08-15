from flask import Blueprint, render_template

from web.constants import ENLACES, BIBLIOGRAFIA

material_bp = Blueprint('material', __name__)


@material_bp.route('/material-adicional')
def index():
    return render_template('site/material.html', enlaces=ENLACES, bibliografia=BIBLIOGRAFIA)
