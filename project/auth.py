from itertools import product
from flask import Blueprint, render_template, redirect, url_for, request, flash

from werkzeug.security import generate_password_hash, check_password_hash


from flask_security import login_required, roles_accepted

from flask_security.utils import (
    login_user,
    logout_user,
    hash_password,
    encrypt_password,
)

from .models import Role, User

from . import db, userDataStore

from flask_security.decorators import roles_required

from .models import User, Product

from .forms import ProductForm
from project import forms

auth = Blueprint("auth", __name__, url_prefix="/security")


@auth.route("/login")
def login():
    return render_template("/security/login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):

        flash("El usuario y/o la contraseña son incorrectos")
        return redirect(url_for("auth.login"))

    login_user(user, remember=remember)
    return redirect(url_for("main.profile"))



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.principal"))
