from flask import Blueprint, render_template, request

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def login():
    return render_template('login.html')
