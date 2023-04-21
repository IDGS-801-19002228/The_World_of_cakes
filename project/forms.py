from email import message
from wtforms import Form
from wtforms import StringField, TelField, IntegerField, EmailField,SelectField,RadioField
from wtforms import validators
from wtforms import EmailField

from flask_wtf import FlaskForm
from  wtforms.fields import StringField, PasswordField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired


def my_validate(form, field):
    if len(str(field.data)) == 0:
        raise validators.ValidationError("El campo no tiene datos")

class ProductForm(Form):
    id = IntegerField('id')
    Nombre = StringField('Nombre:')                       
    Precio = IntegerField('Precio:')
    Descripcion = StringField('Descripcion:')
    Image_url = StringField('Image_url')
    #submit = SubmitField('Enviar')
    
class EmpleadoForm(Form):
    id_empleado = IntegerField('id_empleado')
    Nombre = StringField('Nombre:')
    ApellidoP = StringField('ApellidoP:')
    ApellidoM = StringField('ApellidoM:')
    Numero_empleado = StringField('Numero_empleado:')
    Fecha_nacimiento = StringField('Fecha_nacimiento:')
    Calle = StringField('Calle:')
    NumeroCasa = IntegerField('NumeroCasa:')
    Colonia = StringField('Colonia:')
    Codigo_postal = IntegerField('Codigo_postal:')
    Correo_electronico = StringField('Correo_electronico')
    TelefonoC = StringField('TelefonoC')

class ProveedorForm(Form):
    id = IntegerField('Proveedor')
    rfc = StringField('Rfc')
    nombre = StringField('Nombre')
    telefono = StringField('Número Telefonico')
    domicilio = StringField('Domicilio')
    razon_social = StringField('Razon social')
    descripcion = TextAreaField('Descripcion')
    
class MermaForm (Form):
    id = IntegerField('Id Merma')
    nombre_producto = StringField('Nombre del producto')
    cantidad_unidad = IntegerField('Cantidad o unidad:')
    precio_venta = FloatField('Precio venta / Precio compra')