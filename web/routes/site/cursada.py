from flask import Blueprint, render_template

cursada_bp = Blueprint('cursada', __name__)


@cursada_bp.route('/cursada')
def index():
    return render_template('site/cursada.html')
