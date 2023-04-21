
from multiprocessing.dummy import current_process
from flask import Blueprint, Flask, render_template

from flask_security import login_required, current_user, roles_accepted

from flask_security.decorators import roles_required


from . import db

from .models import Role

import logging

main = Blueprint('main',__name__)

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

app = Flask(__name__)
app.logger.info('Se inicio la aplicacion')

@main.route('/')
def principal():
    return render_template('index.html')

@main.route('/inicio')
def inicio():
    return render_template('inicio.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/contacto')
def contacto():
    return render_template('contacto.html')
