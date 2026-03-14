from maestros import maestros
from flask import render_template, request, redirect, url_for, flash
import forms
from models import db, Maestros

@maestros.route("/maestros", methods=["GET", "POST"])
def listadoMaes():
    create_form = forms.MaestroForm(request.form)
    lista = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=lista)

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
        return redirect(url_for('maestros.listadoMaes'))
    return render_template("maestros/agregarMaes.html", form=create_form)

@maestros.route("/maestros/detalles", methods=["GET"])
def detalles():
    matricula = request.args.get('matricula')
    mae = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
    return render_template("maestros/detallesMaes.html", mae=mae)

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
        return redirect(url_for('maestros.listadoMaes'))
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
        mae = db.session.get(Maestros, matricula)
        if mae.cursos:
            flash(f"No se puede eliminar a {mae.nombre}, tiene {len(mae.cursos)} curso(s) asignado(s).", "error")
            return redirect(url_for('maestros.listadoMaes'))
        db.session.delete(mae)
        db.session.commit()
        return redirect(url_for('maestros.listadoMaes'))
    return render_template("maestros/eliminarMaes.html", form=create_form)