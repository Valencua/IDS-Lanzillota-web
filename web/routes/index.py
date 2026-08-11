from flask import Blueprint, render_template
from web.constants import SEMANAS, DOCENTES, ENLACES, BIBLIOGRAFIA

index_bp = Blueprint('index', __name__)

@index_bp.route('/material-adicional')
def material():
    return render_template('material.html', enlaces=ENLACES, bibliografia=BIBLIOGRAFIA)

@index_bp.route('/docentes')
def docentes():
    return render_template('docentes.html', docentes=DOCENTES)

@index_bp.route('/cronograma')
def cronograma():
    return render_template('cronograma.html', semanas=SEMANAS)

@index_bp.route('/cursada')
def cursada():
    return render_template('cursada.html')

@index_bp.route('/')
def index():
    return render_template('inicio.html')