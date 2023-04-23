from email import message
from wtforms import Form
from wtforms import StringField, TelField, IntegerField, EmailField,SelectField,RadioField
from wtforms import validators
from wtforms import EmailField

from flask_wtf import FlaskForm
from  wtforms.fields import DateField, StringField, PasswordField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired


def my_validate(form, field):
    if len(str(field.data)) == 0:
        raise validators.ValidationError("El campo no tiene datos")

'''class ProductForm(Form):
    id = IntegerField('id')
    Nombre = StringField('Nombre:')                       
    Precio = IntegerField('Precio:')
    Descripcion = StringField('Descripcion:')
    Image_url = StringField('Image_url')
    #submit = SubmitField('Enviar')'''

class ProductForm(Form):
    id = IntegerField('id:')
    Nombre = StringField('Nombre:',[
        validators.DataRequired(message='El campo es requerido')
    ])                       
    Precio_Venta = IntegerField('Precio_Venta:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Tamanio = IntegerField('Porciones:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Peso = IntegerField('Peso:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Descripcion = StringField('Descripcion:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Numero_Existencias = IntegerField('Numero_Existencias:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Image_url = TextAreaField('URL:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    
class EmpleadoForm(Form):
    id = IntegerField('id_empleado')
    name = StringField('Nombre:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    ApellidoP = StringField('ApellidoP:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    ApellidoM = StringField('ApellidoM:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Numero_empleado = StringField('Numero_empleado:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Fecha_nacimiento = StringField('Fecha_nacimiento:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Calle = StringField('Calle:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    NumeroCasa = IntegerField('NumeroCasa:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Colonia = StringField('Colonia:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Codigo_postal = IntegerField('Codigo_postal:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    email = StringField('Correo_electronico:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    password = PasswordField('Contraseña:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    TelefonoC = StringField('TelefonoC:',[
        validators.DataRequired(message='El campo es requerido')
    ])

class ProveedorForm(Form):
    id = IntegerField('Proveedor')
    rfc = StringField('Rfc:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre = StringField('Nombre:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    telefono = StringField('Número Telefonico',[
        validators.DataRequired(message='El campo es requerido')
    ])
    domicilio = StringField('Domicilio:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    razon_social = StringField('Razon social:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    descripcion = TextAreaField('Descripcion:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    estatus = IntegerField('Estatus')
    
class MermaForm (Form):
    id = IntegerField('Id Merma')
    nombre_producto = StringField('Nombre del producto:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    cantidad_unidad = IntegerField('Cantidad o unidad:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    precio_venta = FloatField('Precio venta / Precio compra:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    id_empleado = FloatField('id empleado:')
    
class RecetarioForm(Form):
    id_recetario = IntegerField('id_recetario')
    nombre = StringField('Nombre:',[
        validators.DataRequired(message='El campo es requerido')
    ]) 
    descripcion = StringField('Descripcion:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    numero_existencias = IntegerField('Numero_existencias:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    
class ClienteForm(Form):
    id = IntegerField('id_cliente')
    Nombre = StringField('Nombre:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    ApellidoP = StringField('ApellidoP:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    ApellidoM = StringField('ApellidoM:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Numero_cliente = StringField('Numero_cliente:')
    Fecha_nacimiento = StringField('Fecha_nacimiento:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Calle = StringField('Calle:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    NumeroCasa = IntegerField('NumeroCasa:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Colonia = StringField('Colonia:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Codigo_postal = IntegerField('Codigo_postal:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Correo_electronico = StringField('Correo_electronico',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Contraseña = StringField('Contraseña',[
        validators.DataRequired(message='El campo es requerido')
    ])
    Telefono = StringField('Telefono',[
        validators.DataRequired(message='El campo es requerido')
    ])
    
class CompraForm (Form):
    id = IntegerField('id')
    fecha_compra = DateField('fecha_compra:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    folio =IntegerField('folio',[
        validators.DataRequired(message='El campo es requerido')
    ])
    id_Proveedor = SelectField('Proveedor') 
    id_Empleado = IntegerField('Empleado')  
    cantidad = IntegerField('Cantidad:',[
        validators.DataRequired(message='El campo es requerido')
    ])
    costo = IntegerField('costo:',[
        validators.DataRequired(message='El campo es requerido')
    ])