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
    
class MaestroForm(FlaskForm):
    matricula = IntegerField('Matricula', [
        validators.number_range(min=1, message="Valor no válido")
    ])
    nombre = StringField("Nombre", {
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=1, max=50)
    })
    apellidos = StringField("Apellidos", {
        validators.DataRequired(message="Los apellidos son requeridos")
    })
    especialidad = StringField("Especialidad", {
        validators.DataRequired(message="La especialidad es requerida")
    })
    email = EmailField("Email", {
        validators.Email(message="Ingrese un correo válido")
    })

class CursoForm(FlaskForm):
    id = IntegerField('id', [validators.optional()])
    nombre = StringField("Nombre del Curso", {
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=1, max=150)
    })
    descripcion = StringField("Descripción", {
        validators.DataRequired(message="La descripción es requerida")
    })
    maestro_id = IntegerField("Matrícula del Maestro", [
        validators.optional()
    ])
