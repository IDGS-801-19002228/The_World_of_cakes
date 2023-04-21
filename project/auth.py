from itertools import product
import random
from flask import Blueprint, render_template, redirect, url_for, request, flash

from werkzeug.security import generate_password_hash, check_password_hash


from flask_security import login_required, roles_accepted

from flask_security.utils import (
    login_user,
    logout_user,
    hash_password,
    encrypt_password,
)


from .models import Merma, Product, Recetario, Role, User

from . import db, userDataStore

from flask_security.decorators import roles_required

from .models import User, Empleado, Proveedor

from .forms import ClienteForm, ProductForm, EmpleadoForm, ProveedorForm, RecetarioForm
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
    return redirect(url_for("main.principal"))


@auth.route("/register")
def register():
    return render_template("/security/register.html")


@auth.route("/register", methods=["POST"])
def register_post():
    name = request.form.get("name"),
    ApellidoP = request.form.get("ApellidoP")
    ApellidoM = request.form.get("ApellidoM"),
    Numero_cliente = random.randint(1, 10),
    Fecha_nacimiento = request.form.get("Fecha_nacimiento"),
    Calle = request.form.get("Calle"),
    NumeroCasa = request.form.get("NumeroCasa"),
    Colonia = request.form.get("Colonia"),
    Codigo_postal = request.form.get("Codigo_postal"),
    TelefonoC = request.form.get("TelefonoC")
    email = request.form.get("email"),
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    #usuarios=User.query.all()
    if user:
        flash("El correo electrónico ya existe")
        return redirect(url_for("auth.register"))

    userDataStore.create_user(
        name=name,
        ApellidoP = ApellidoP,
        ApellidoM = ApellidoM,
        Numero_cliente = Numero_cliente,
        Fecha_nacimiento = Fecha_nacimiento,
        Calle = Calle,
        NumeroCasa = NumeroCasa,
        Colonia = Colonia,
        Codigo_postal = Codigo_postal,
        TelefonoC = TelefonoC,
        email=email,
        password=generate_password_hash(password, method="sha256"),
    )

    db.session.commit()

    return redirect(url_for("auth.login"))

'''@auth.route("/register_admin")
def register_admin():
    return render_template("/security/register_admin.html")

@auth.route("/register_admin", methods=["POST"])
def register_post_admin():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    admin = Admin.query.filter_by(email=email).first()

    if admin:
        flash("El correo electrónico ya existe")
        return redirect(url_for("auth.register_admin"))

    userDataStore2.create_user(
        name=name,
        email=email,
        password=generate_password_hash(password, method="sha256"),
    )

    db.session.commit()

    return redirect(url_for("auth.login"))'''

#----------------------------------------------------------------------------

@auth.route("/productos", methods=["GET"])
def productos():
    productos=Product.query.all() 
    return render_template("productos.html",productos=productos)

#Seccion Administrador

@auth.route("/pedidos", methods=["GET"])
def pedidos():
    productos=Product.query.all() 
    return render_template("productos.html",productos=productos)

@auth.route("/finanzas", methods=["GET"])
@login_required
@roles_required("admin")
def finanzas():
    return render_template("finanzas.html")

@auth.route("/clientes_admin", methods=["GET"])
@login_required
@roles_required("admin")
def clientes_admin():        
    usuarios=User.query.all() 
    return render_template("clientes_admin.html",usuarios=usuarios)

@auth.route("/empleados", methods=["GET","POST"])
@login_required
@roles_required("admin")
def empleados():
    create_form = forms.EmpleadoForm(request.form)
    if request.method == 'POST':
        emple= Empleado(name=create_form.name.data,
                        ApellidoP=create_form.ApellidoP.data,
                        ApellidoM=create_form.ApellidoM.data,
                        Numero_empleado=random.randint(1, 10),
                        Fecha_nacimiento=create_form.Fecha_nacimiento.data,
                        Calle=create_form.Calle.data,
                        NumeroCasa=create_form.NumeroCasa.data,
                        Colonia=create_form.Colonia.data,
                        Codigo_postal=create_form.Codigo_postal.data,
                        email=create_form.email.data,
                        password=create_form.password.data,
                        TelefonoC=create_form.TelefonoC.data,
                        estatus = 1)
        
        userDataStore.create_user(
            name=create_form.name.data,
            email=create_form.email.data,
            ApellidoP=create_form.ApellidoP.data,
            ApellidoM=create_form.ApellidoM.data,
            Fecha_nacimiento=create_form.Fecha_nacimiento.data,
            Calle=create_form.Calle.data,
            NumeroCasa=create_form.NumeroCasa.data,
            Colonia=create_form.Colonia.data,
            Codigo_postal=create_form.Codigo_postal.data,
            TelefonoC=create_form.TelefonoC.data,
            password=generate_password_hash(create_form.password.data, method="sha256"),
    )

        db.session.add(emple)
        db.session.commit()
        
        flash('El empleado se registro correctamente')
        return redirect(url_for('auth.empleados'))
    empleados=Empleado.query.all() 
    return render_template("empleados.html",form=create_form,empleados=empleados)


@auth.route("/administracion_admin", methods=["GET","POST"])
@login_required
@roles_required("admin")
def administracion_admin():
    create_form = forms.ProductForm(request.form)
    if request.method == 'POST':
        prod= Product(nombre=create_form.Nombre.data,
                        precio_Venta=create_form.Precio_Venta.data,
                        tamanio=create_form.Tamanio.data,
                        peso=create_form.Peso.data,
                        descripcion=create_form.Descripcion.data,
                        numero_Existencias=create_form.Numero_Existencias.data,
                        image_url=create_form.Image_url.data)
        
        db.session.add(prod)
        db.session.commit()
        
        flash('El producto se registro correctamente')
        return redirect(url_for('auth.administracion_admin'))
    productos=Product.query.all() 
    
    return render_template("administracion_admin.html", form=create_form,productos=productos)


@auth.route("/modificar",methods=["GET","POST"])
@login_required
@roles_required("admin")
def modificar():
    create_form2=forms.ProductForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from alumnos where id==id
        prod1=db.session.query(Product).filter(Product.id==id).first()
        create_form2.id.data=id
        create_form2.Nombre.data=prod1.nombre
        create_form2.Precio.data=prod1.precio
        create_form2.Descripcion.data=prod1.descripcion
        create_form2.Image_url.data=prod1.image_url
        
    if request.method=='POST':
        #Select * from alumnos where id==id
        id = create_form2.id.data
        prod2=db.session.query(Product).filter(Product.id==id).first()
        
        prod2.nombre=create_form2.Nombre.data
        prod2.precio=create_form2.Precio.data
        prod2.descripcion=create_form2.Descripcion.data
        prod2.image_url=create_form2.Image_url.data
        db.session.add(prod2)
        db.session.commit()
        flash('El producto se actualizo correctamente')
        return redirect(url_for('auth.administracion'))
    return render_template('modificar.html',form=create_form2)

@auth.route("/eliminar",methods=['GET','POST'])
@login_required
@roles_required("admin")
def eliminar():
    create_form3=forms.ProductForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from productos where id==id
        prod1=db.session.query(Product).filter(Product.id==id).first()
        create_form3.id.data=id
        create_form3.Nombre.data=prod1.nombre
        create_form3.Precio.data=prod1.precio
        create_form3.Descripcion.data=prod1.descripcion
        create_form3.Image_url.data=prod1.image_url
        
    if request.method=='POST':
        id = create_form3.id.data
        prod2=db.session.query(Product).filter(Product.id==id).first()
        prod2.nombre=create_form3.Nombre.data
        prod2.precio=create_form3.Precio.data
        prod2.descripcion=create_form3.Descripcion.data
        prod2.image_url=create_form3.Image_url.data
        db.session.delete(prod2)
        db.session.commit()
        flash('El producto se elimino correctamente')
        return redirect(url_for('auth.administracion'))
    return render_template('eliminar.html',form=create_form3)

#--------------------------------------------------------------------------------
#INSERT PROVEEDOR CON SESION ADMINISTRADOR

@auth.route("/proveedor_admin", methods=["GET","POST"])
@login_required
@roles_required("admin")
def proveedor_admin():
    create_form = forms.ProveedorForm(request.form)
    if request.method == 'POST':
        prov= Proveedor(rfc = create_form.rfc.data,
                       domicilio = create_form.domicilio.data,
                       razon_social = create_form.razon_social.data,
                       nombre = create_form.nombre.data,
                       telefono = create_form.telefono.data,
                       descripcion = create_form.descripcion.data,
                       estatus=1)
        
        db.session.add(prov)
        db.session.commit()
        
        flash('El producto se registro correctamente')
        return redirect(url_for('auth.proveedor_admin'))
    proveedores=Proveedor.query.all() 
    
    return render_template("proveedor_admin.html", form=create_form,proveedores=proveedores)

'''@auth.route("/cliente_admin", methods=["GET","POST"])
@login_required
@roles_required("admin")
def insert_cliente():
    create_form = forms.ClienteForm(request.form)
    if request.method == 'POST':
        clie= Cliente(rfc = create_form.rfc.data,
                       domicilio = create_form.domicilio.data,
                       razon_social = create_form.razon_social.data,
                       nombre = create_form.nombre.data,
                       telefono = create_form.telefono.data,
                       descripcion = create_form.descripcion.data,
                       estatus=1)
        
        db.session.add(clie)
        db.session.commit()
        
        flash('El producto se registro correctamente')
        return redirect(url_for('auth.cliente_admin'))
    clientes=Cliente.query.all() 
    
    return render_template("cliente_admin.html", form=create_form,clientes=clientes)'''


@auth.route("/merma_admin", methods=['GET','POST'])
def insertarMerma():
    create_form = forms.MermaForm(request.form)
  
   
    if request.method == 'POST':
        
        merma = Merma(
                       nombre_producto = create_form.nombre_producto.data,
                       cantidad_unidad = create_form.cantidad_unidad.data,
                       precio_venta = create_form.precio_venta.data,
                      )
       #Realizar el insert en la bd
        db.session.add(merma)
        db.session.commit()
        
        flash('La merma se registro correctamente')
        return redirect(url_for('auth.merma_admin'))
    
    mermas=Merma.query.all() 
    return render_template('merma_admin.html',form = create_form, mermas=mermas)

@auth.route("/registroRecetario_admin", methods=['GET','POST'])
def registroRecetario():
    create_form = forms.RecetarioForm(request.form)
    if request.method == 'POST':
        rece = Recetario(nombre = create_form.nombre.data,      
                            descripcion = create_form.descripcion.data,
                            numero_Existencias = create_form.numero_existencias.data
                            )
        #Realizar el insert en la bd
        db.session.add(rece)
        db.session.commit()
        
        flash('La receta se registro correctamente')
        return redirect(url_for('auth.recetario'))
    
    recetas=Recetario.query.all() 
    return render_template('recetario.html',form = create_form, recetas=recetas)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.principal"))

# SECCION DE SESION CON EMPLEADO

@auth.route("/administracion_empleado", methods=["GET","POST"])
@login_required
@roles_required("empleado")
def administracion_empleado():
    create_form = forms.ProductForm(request.form)
    if request.method == 'POST':
        prod= Product(nombre=create_form.Nombre.data,
                        precio=create_form.Precio.data,
                        descripcion=create_form.Descripcion.data,
                        image_url=create_form.Image_url.data)
        
        db.session.add(prod)
        db.session.commit()
        
        flash('El producto se registro correctamente')
        return redirect(url_for('auth.administracion_empleado'))
    productos=Product.query.all() 
    
    return render_template("administracion_empleado.html", form=create_form,productos=productos)

@auth.route("/modificar_e",methods=["GET","POST"])
@login_required
@roles_required("empleado")
def modificar_e():
    create_form2=forms.ProductForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from alumnos where id==id
        prod1=db.session.query(Product).filter(Product.id==id).first()
        create_form2.id.data=id
        create_form2.Nombre.data=prod1.nombre
        create_form2.Precio.data=prod1.precio
        create_form2.Descripcion.data=prod1.descripcion
        create_form2.Image_url.data=prod1.image_url
        
    if request.method=='POST':
        #Select * from alumnos where id==id
        id = create_form2.id.data
        prod2=db.session.query(Product).filter(Product.id==id).first()
        
        prod2.nombre=create_form2.Nombre.data
        prod2.precio=create_form2.Precio.data
        prod2.descripcion=create_form2.Descripcion.data
        prod2.image_url=create_form2.Image_url.data
        db.session.add(prod2)
        db.session.commit()
        flash('El producto se actualizo correctamente')
        return redirect(url_for('emple.administracion'))
    return render_template('modificar.html',form=create_form2)

@auth.route("/eliminar_e",methods=['GET','POST'])
@login_required
@roles_required("empleado")
def eliminar_e():
    create_form3=forms.ProductForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from productos where id==id
        prod1=db.session.query(Product).filter(Product.id==id).first()
        create_form3.id.data=id
        create_form3.Nombre.data=prod1.nombre
        create_form3.Precio.data=prod1.precio
        create_form3.Descripcion.data=prod1.descripcion
        create_form3.Image_url.data=prod1.image_url
        
    if request.method=='POST':
        id = create_form3.id.data
        prod2=db.session.query(Product).filter(Product.id==id).first()
        prod2.nombre=create_form3.Nombre.data
        prod2.precio=create_form3.Precio.data
        prod2.descripcion=create_form3.Descripcion.data
        prod2.image_url=create_form3.Image_url.data
        db.session.delete(prod2)
        db.session.commit()
        flash('El producto se elimino correctamente')
        return redirect(url_for('emple.administracion'))
    return render_template('eliminar.html',form=create_form3)


@auth.route("/pedidos_empleado", methods=["GET"])
@login_required
@roles_required("empleado")
def pedidos_empleado():
    productos=Product.query.all() 
    return render_template("productos.html",productos=productos)

@auth.route("/finanzas_empleado", methods=["GET"])
@login_required
@roles_required("empleado")
def finanzas_empleado():
    return render_template("finanzas.html")
