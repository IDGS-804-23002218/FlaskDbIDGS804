from . import maestros
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from maestros.routes import maestros, maestros

from models import db
from models import Alumnos, Maestros

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

@maestros.route("/maestros", methods=["GET","POST"])
@maestros.route("/index")
def index():
    create_form=forms.MaestroForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros)

@maestros.route("/maestros/agregar", methods=["GET", "POST"])
def agregar():
    create_form = forms.MaestroForm(request.form)
    if request.method == "POST":
        mae = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(mae)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    return render_template("maestros/agregarMaes.html", form=create_form)

@maestros.route("/maestros/detalles", methods=["GET"])
def detalles():
    if request.method == "GET":
        matricula=request.args.get('matricula')
        mae=db.session.query(Maestros).filter(Maestros.matricula==matricula).first() 
        nombre=mae.nombre
        apellidos=mae.apellidos
        especialidad=mae.especialidad
        email=mae.email
        return render_template("maestros/detallesMaes.html", matricula=matricula, nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)

@maestros.route("/maestros/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.MaestroForm(request.form)
    if request.method == "GET":
        matricula = request.args.get('matricula')
        mae = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.matricula.data = mae.matricula
        create_form.nombre.data = mae.nombre
        create_form.apellidos.data = mae.apellidos
        create_form.especialidad.data = mae.especialidad
        create_form.email.data = mae.email
    if request.method == "POST":
        matricula = request.args.get('matricula')
        mae = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        mae.nombre = create_form.nombre.data
        mae.apellidos = create_form.apellidos.data
        mae.especialidad = create_form.especialidad.data
        mae.email = create_form.email.data
        db.session.commit()
        return redirect(url_for('maestros.index'))
    return render_template("maestros/modificarMaes.html", form=create_form)

@maestros.route("/maestros/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.MaestroForm(request.form)
    if request.method == "GET":
        matricula = request.args.get('matricula')
        mae = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.matricula.data = mae.matricula
        create_form.nombre.data = mae.nombre
        create_form.apellidos.data = mae.apellidos
        create_form.especialidad.data = mae.especialidad
        create_form.email.data = mae.email
    if request.method == "POST":
        matricula = create_form.matricula.data
        mae = Maestros.query.get(matricula)
        db.session.delete(mae)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    return render_template("maestros/eliminarMaes.html", form=create_form)