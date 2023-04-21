from email import message
from wtforms import Form
from wtforms import StringField, TelField, IntegerField, EmailField,SelectField,RadioField
from wtforms import validators
from wtforms import EmailField

from flask_wtf import FlaskForm
from  wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


def my_validate(form, field):
    if len(str(field.data)) == 0:
        raise validators.ValidationError("El campo no tiene datos")

class ProductoForm(Form):
    id = IntegerField('id')
    Nombre = StringField('Nombre')                       
    Precio_Venta = IntegerField('Precio_Venta')
    Tamanio = IntegerField('Tamanio')
    Peso = IntegerField('Peso')
    Descripcion = StringField('Descripcion')
    Numero_Existencias = IntegerField('Numero_Existencias')
    Image_url = StringField('Image_url')

class RecetarioForm(Form):
    id = IntegerField('id')
    Nombre = StringField('Nombre:') 
    Descripcion = StringField('Descripcion:')
