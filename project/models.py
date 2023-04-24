
import datetime
from . import db
from flask_sqlalchemy import SQLAlchemy

from flask_security import UserMixin, RoleMixin


users_roles = db.Table('users_roles',
    db.Column('userId', db.Integer, db.ForeignKey('user.id')),
    db.Column('roleId', db.Integer, db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    """User account model"""
    
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ApellidoP = db.Column(db.String(255), nullable=False)
    ApellidoM = db.Column(db.String(255), nullable=False)
    Numero_cliente = db.Column(db.String(255))
    Fecha_nacimiento = db.Column(db.String(255))
    Calle = db.Column(db.String(255))
    NumeroCasa = db.Column(db.Integer)
    Colonia = db.Column(db.String(255))
    Codigo_postal = db.Column(db.Integer)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    TelefonoC = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    roles = db.relationship('Role',
        secondary=users_roles,
        backref= db.backref('users', lazy='dynamic'))

class Role(RoleMixin, db.Model):
    """Role model"""

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description =  db.Column(db.String(255))
    
class Product(db.Model, UserMixin):
    """Producto account model"""
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Precio_Venta = db.Column(db.Integer, nullable=False)
    Tamanio = db.Column(db.Integer, nullable=False)
    Peso = db.Column(db.Integer, nullable=False)
    Descripcion = db.Column(db.String(255), nullable=False)
    Numero_Existencias = db.Column(db.Integer, nullable=False)
    Image_url = db.Column(db.Text(255), nullable=False)
    cantidad = db.Column(db.String(50))
    id_materiaPrima =  db.Column(db.Integer,db.ForeignKey('materia_prima.id'),)
    
class Empleado(db.Model, UserMixin):
    """Employe account model"""
    
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ApellidoP = db.Column(db.String(255))
    ApellidoM = db.Column(db.String(255))
    Numero_empleado = db.Column(db.String(255))
    Fecha_nacimiento = db.Column(db.String(255))
    Calle = db.Column(db.String(255))
    NumeroCasa = db.Column(db.Integer)
    Colonia = db.Column(db.String(255))
    Codigo_postal = db.Column(db.Integer)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    TelefonoC = db.Column(db.String(255))
    estatus = db.Column(db.Integer)

class Proveedor (db.Model, UserMixin):
    
    __tablename__ = 'proveedor' #mapear la tabla
    #especificar el tipo de dato atributos de tal tabla
    id = db.Column(db.Integer,primary_key = True)
    rfc = db.Column(db.String(15))
    domicilio = db.Column(db.String(50))
    razon_social = db.Column(db.String(100))
    nombre = db.Column(db.String(50))
    telefono = db.Column(db.String(12))
    descripcion = db.Column(db.String(255))
    estatus = db.Column(db.Integer)

class Merma (db.Model, UserMixin):

    __tablename__ = 'merma' #mapear la tabla
    #especificar el tipo de dato atributos de tal tabla
    id = db.Column(db.Integer,primary_key = True)
    nombre_producto = db.Column(db.String(255))
    cantidad_unidad = db.Column(db.String(255))
    precio_venta = db.Column(db.String(100))
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id'))
    

class Recetario(db.Model, UserMixin):
    """Recetario account model"""
    __tablename__ = 'recetario'
    id_recetario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    numero_Existencias = db.Column(db.Integer, nullable=False)
    
    
class DetalleCompraMateria (db.Model, UserMixin):
    _tablename_ = 'detalle_compra_materiap' #mapear la tabla 
    
    #especificar el tipo de dato atributos de tal tabla
    id = db.Column(db.Integer,primary_key = True)  
    cantidad = db.Column(db.String(50))
    costo = db.Column(db.Integer)
    id_compraMateria = db.Column(db.Integer,db.ForeignKey('compra_materia.id')),
    id_materiaPrima =  db.Column(db.Integer,db.ForeignKey('materia_prima.id'))
    

class CompraMateriaPrima (db.Model,UserMixin):
    _tablename_ = 'compra_materia' #mapear la tabla 
    
    #especificar el tipo de dato atributos de tal tabla
    id = db.Column(db.Integer,primary_key = True)  
    fecha_Compra = db.Column(db.DateTime, default = datetime.datetime.now) #crear un campo para registar la fecha y la hora actual 
    folio = db.Column(db.String(255))
    id_proveedor = db.Column(db.Integer,db.ForeignKey('proveedor.id'))
    id_Empleado =  db.Column(db.Integer,db.ForeignKey('empleado.id'))

class MateriaPrima (db.Model, UserMixin):
    _tablename_ = 'materia_prima' #mapear la tabla 
    
    id = db.Column(db.Integer,primary_key = True) 
    nombre = db.Column(db.String(50))
    marca = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
    unidad_medida = db.Column(db.String(10))
    
class Pedidos (db.Model,UserMixin):
    _tablename_ = 'pedidos' #mapear la tabla 
    
    #especificar el tipo de dato atributos de tal tabla
    id = db.Column(db.Integer,primary_key = True)  
    fecha = db.Column(db.DateTime, default = datetime.datetime.now) #crear un campo para registar la fecha y la hora actual 
    id_cliente =  db.Column(db.Integer,db.ForeignKey('user.id'))
    id_producto =  db.Column(db.Integer,db.ForeignKey('product.id'))
    total = db.Column(db.Integer)
    estatus= db.Column(db.Integer)
    