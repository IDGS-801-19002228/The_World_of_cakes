from flask import Blueprint, render_template, redirect, url_for, request, flash

from werkzeug.security import generate_password_hash, check_password_hash

from .models import Usuario, Producto, Recetario
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


@auth.route("/register")
def register():
    return render_template("/security/register.html")


@auth.route("/register", methods=["POST"])
def register_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        flash("El correo electrónico ya existe")
        return redirect(url_for("auth.register"))

    userDataStore.create_user(
        name=name,
        email=email,
        password=generate_password_hash(password, method="sha256"),
    )

    db.session.commit()

    return redirect(url_for("auth.login"))

# Todo LO DE PRODUCTOS ES PARTE HECHA POR PAULINA --------------------------
@auth.route("/registro", methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        pos = Producto(nombre = request.form['nombre'], 
                       precio_Venta = request.form['precio_Venta'], 
                       tamanio = request.form['tamanio'],
                       peso = request.form['peso'],          
                       descripcion = request.form['descripcion'],
                       numero_Existencias = request.form['numero_Existencias'],
                       image_url = 1)
        #Realizar el insert en la bd
        db.session.add(pos)
        db.session.commit()
        return redirect(url_for('auth.verProductos'))


@auth.route("/modificarProducto",methods=["GET","POST"])
def modificarProducto():
    create_form= forms.ProductoForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from alumns where id == id 
        produ = db.session.query(Producto).filter(Producto.id==id).first()
        create_form.id.data = id
        create_form.Nombre.data = produ.nombre
        create_form.Precio_Venta.data = produ.precio_Venta
        create_form.Tamanio.data = produ.tamanio
        create_form.Peso.data = produ.peso
        create_form.Descripcion.data = produ.descripcion
        create_form.Numero_Existencias.data = produ.numero_Existencias
    if request.method=='POST':
        id = create_form.id.data
        produ = db.session.query(Producto).filter(Producto.id==id).first()
        produ.nombre = create_form.Nombre.data 
        produ.precio_Venta = create_form.Precio_Venta.data 
        produ.tamanio = create_form.Tamanio.data
        produ.peso = create_form.Peso.data
        produ.descripcion= create_form.Descripcion.data
        produ.numero_Existencias = create_form.Numero_Existencias.data

        db.session.add(produ)
        db.session.commit()
        return redirect(url_for('auth.verProductos'))
    return render_template('modificarProducto.html', forms=create_form)



@auth.route("/eliminarProducto",methods=["GET","POST"])
def eliminarProducto():
    create_form= forms.ProductoForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from alumns where id == id 
        produ = db.session.query(Producto).filter(Producto.id==id).first()
        create_form.id.data = id
        create_form.Nombre.data = produ.nombre
        create_form.Precio_Venta.data = produ.precio_Venta
        create_form.Tamanio.data = produ.tamanio
        create_form.Peso.data = produ.peso
        create_form.Descripcion.data = produ.descripcion
        create_form.Numero_Existencias.data = produ.numero_Existencias
    if request.method=='POST':
        id = create_form.id.data
        produ = db.session.query(Producto).filter(Producto.id==id).first()
        produ.nombre = create_form.Nombre.data 
        produ.precio_Venta = create_form.Precio_Venta.data 
        produ.tamanio = create_form.Tamanio.data
        produ.peso = create_form.Peso.data
        produ.descripcion= create_form.Descripcion.data
        produ.numero_Existencias = create_form.Numero_Existencias.data

        db.session.delete(produ)
        db.session.commit()
        return redirect(url_for('auth.verProductos'))
    return render_template('eliminarProducto.html', forms=create_form)



@auth.route('/verProductos')
def verProductos():
    create_form = forms.ProductoForm(request.form)
    #select * from alumnos
    producto = Producto.query.all()
    return render_template('producto.html', form = create_form, producto = producto)
    
# Todo LO DE RECETARIO ES PARTE HECHA POR PAULINA --------------------------
@auth.route("/registroRecetario", methods=['GET','POST'])
def registroRecetario():
    if request.method == 'POST':
        rece = Recetario(nombre = request.form['nombre'],      
                       descripcion = request.form['descripcion'])
        #Realizar el insert en la bd
        db.session.add(rece)
        db.session.commit()
        return redirect(url_for('auth.verRecetario'))

@auth.route('/verRecetario')
def verRecetario():
    create_form = forms.RecetarioForm(request.form)
    #select * from recetario
    recetario = Recetario.query.all()
    return render_template('recetario.html', form = create_form, recetario = recetario)

@auth.route("/modificarRecetario",methods=["GET","POST"])
def modificarRecetario():
    create_form= forms.RecetarioForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from recetario where id == id 
        rece = db.session.query(Recetario).filter(Recetario.id==id).first()
        create_form.id.data = id
        create_form.Nombre.data = rece.nombre
        create_form.Descripcion.data = rece.descripcion
    if request.method=='POST':
        id = create_form.id.data
        rece = db.session.query(Recetario).filter(Recetario.id==id).first()
        rece.nombre = create_form.Nombre.data 
        rece.descripcion= create_form.Descripcion.data


        db.session.delete(rece)
        db.session.commit()
        return redirect(url_for('auth.verRecetario'))
    return render_template('modificarRecetario.html', forms=create_form)



@auth.route("/eliminarRecetario",methods=["GET","POST"])
def eliminarRecetario():
    create_form= forms.RecetarioForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from recetario where id == id 
        rece = db.session.query(Recetario).filter(Recetario.id==id).first()
        create_form.id.data = id
        create_form.Nombre.data = rece.nombre
        create_form.Descripcion.data = rece.descripcion
    if request.method=='POST':
        id = create_form.id.data
        rece = db.session.query(Recetario).filter(Recetario.id==id).first()
        rece.nombre = create_form.Nombre.data 
        rece.descripcion= create_form.Descripcion.data


        db.session.delete(rece)
        db.session.commit()
        return redirect(url_for('auth.verRecetario'))
    return render_template('eliminarRecetario.html', forms=create_form)




@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.principal"))
