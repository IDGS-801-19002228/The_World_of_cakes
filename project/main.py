
from multiprocessing.dummy import current_process
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import logging

from . import db

main = Blueprint('main',__name__)

#Definimos la ruta principal
@main.route('/')
def index():
    return render_template('login.html')

#Definimos la ruta a la pagina de perfil
@main.route('/admin')
@login_required #Para proteger la ruta con inicio de session
def admin():
    return redirect(url_for('auth.verProductos'))

#Definimos la ruta a la pagina de perfil
@main.route('/usuario')
@login_required #Para proteger la ruta con inicio de session
def usuario():
    return render_template('inicioUsuario.html', name=current_user.name)