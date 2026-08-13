"""Autenticación del panel de administración: login, logout y el
decorador admin_required que protege las secciones internas.
"""
import os
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint('auth', __name__)


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('web.admin.auth.login'))
        return view(*args, **kwargs)
    return wrapped


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('admin'):
        return redirect(url_for('web.admin.panel.index'))

    error = None
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        password = request.form.get('password', '')

        if (usuario == os.getenv('ADMIN_USER')
                and password == os.getenv('ADMIN_PASSWORD')):
            session['admin'] = True
            return redirect(url_for('web.admin.panel.index'))

        error = 'Usuario o contraseña incorrectos.'

    return render_template('admin/login.html', error=error)


@auth_bp.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('web.admin.auth.login'))
