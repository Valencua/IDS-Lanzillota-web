from flask import Blueprint, render_template
from web.constants import SEMANAS, DOCENTES, ENLACES, BIBLIOGRAFIA

index_bp = Blueprint('index', __name__)

@index_bp.route('/material-adicional')
def material():
    return render_template('public/material.html', enlaces=ENLACES, bibliografia=BIBLIOGRAFIA)

@index_bp.route('/docentes')
def docentes():
    return render_template('public/docentes.html', docentes=DOCENTES)

@index_bp.route('/cronograma')
def cronograma():
    return render_template('public/cronograma.html', semanas=SEMANAS)

@index_bp.route('/cursada')
def cursada():
    return render_template('public/cursada.html')

@index_bp.route('/')
def index():
    return render_template('public/inicio.html')