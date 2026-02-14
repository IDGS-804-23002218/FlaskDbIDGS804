from wtforms import EmailField, Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

from wtforms import validators

class UserForm(Form):
    id= IntegerField('id',
    [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre = StringField("Nombre", {
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=1, max=20, message="required min=4 max=20")
    })
    apaterno= StringField("Apaterno", {
        validators.DataRequired(message="El apellido es requerido")
    })
    email = EmailField("Correo", {
        validators.Email(message="Ingrese Correo valido")
    })