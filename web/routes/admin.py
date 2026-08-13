import os
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from web.constants import DOCENTES

admin_bp = Blueprint('admin', __name__)

def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('web.admin.login'))
        return view(*args, **kwargs)
    return wrapped


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('admin'):
        return redirect(url_for('web.admin.admin_panel'))

    error = None
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        password = request.form.get('password', '')

        if (usuario == os.getenv('ADMIN_USER')
                and password == os.getenv('ADMIN_PASSWORD')):
            session['admin'] = True
            return redirect(url_for('web.admin.admin_panel'))

        error = 'Usuario o contraseña incorrectos.'

    return render_template('admin/login.html', error=error)

@admin_bp.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('web.admin.login'))

@admin_bp.route('/')
@admin_required
def admin_panel():
    return render_template('admin/panel.html')

@admin_bp.route('/equipo')
@admin_required
def equipo():
    return render_template('admin/equipo.html', docentes=DOCENTES)
    
@admin_bp.route('/calendario')
@admin_required
def calendario():
    return render_template('admin/calendario.html')