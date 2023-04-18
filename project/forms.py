from email import message
from wtforms import Form
from wtforms import StringField, TelField, IntegerField, EmailField,SelectField,RadioField, FloatField
from wtforms import validators
from wtforms import EmailField

from flask_wtf import FlaskForm
from  wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


def my_validate(form, field):
    if len(str(field.data)) == 0:
        raise validators.ValidationError("El campo no tiene datos")


class proveedorForm(Form):
    id_proveedor=IntegerField('id')
    rfc= SelectField('rfc')
    domicilio= SelectField('Domicilio')
    razon_Social:SelectField('Razon_Social') 
    nombre = SelectField('Nombre')
    telefono = SelectField('Telefono')
    descripcion = SelectField('Descripcion')
    estatus = SelectField('estatus')

class mermaForm(Form):
    id: IntegerField('id')
    nombreProducto = StringField('nombreProducto:')
    cantidad= IntegerField('cantidad y/o unidad:')
    precioVenta= FloatField('precio venta o compra:')