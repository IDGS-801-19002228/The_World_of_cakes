
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

users_roles_admin = db.Table('users_roles_admin',
    db.Column('adminId', db.Integer, db.ForeignKey('admin.id')),
    db.Column('roleId', db.Integer, db.ForeignKey('role_admin.id')))

class Admin(db.Model, UserMixin):
    """User account model"""
    
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    roles = db.relationship('Role_admin',
        secondary=users_roles_admin,
        backref= db.backref('admins', lazy='dynamic'))


class Role_admin(RoleMixin, db.Model):
    """Role model"""

    __tablename__ = 'role_admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description =  db.Column(db.String(255))
    
class Product(db.Model, UserMixin):
    """Producto account model"""
    __tablename__ = 'product'
    id_empleado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio_Venta = db.Column(db.Integer, nullable=False)
    tamanio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    numero_Existencias = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    
class Empleado(db.Model, UserMixin):
    """Employe account model"""
    
    __tablename__ = 'empleado'
    id_empleado = db.Column(db.Integer, primary_key=True)
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
    nombre_producto = db.Column(db.String(15))
    cantidad_unidad = db.Column(db.String(50))
    precio_venta = db.Column(db.String(100))
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id_empleado'))
    

class Recetario(db.Model, UserMixin):
    """Recetario account model"""
    __tablename__ = 'recetario'
    id_recetario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    numero_Existencias = db.Column(db.Integer, nullable=False)