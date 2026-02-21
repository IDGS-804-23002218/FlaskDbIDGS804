from wtforms import EmailField
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

from wtforms import validators

class UserForm(FlaskForm):
    id= IntegerField('id',
    [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre = StringField("Nombre", {
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=1, max=20, message="required min=4 max=20")
    })
    apellidos= StringField("Apellidos", {
        validators.DataRequired(message="Los apellidos son requerido")
    })
    email = EmailField("Email", {
        validators.Email(message="Ingrese un correo valido")
    })
    telefono = StringField("Teléfono", {
        validators.DataRequired(message="Ingrese un teléfono valido")
    })