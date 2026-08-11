from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route('/cursada')
def cursada():
    return render_template('cursada.html')

@index_bp.route('/')
def index():
    return render_template('inicio.html')