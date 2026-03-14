from cursos import cursos
from flask import render_template, request, redirect, url_for, flash
import forms
from models import db, Curso, Alumnos, Maestros

@cursos.route("/cursos", methods=["GET", "POST"])
def listadoCurso():
    lista = Curso.query.all()
    return render_template("cursos/listadoCursos.html", cursos=lista)

@cursos.route("/cursos/agregar", methods=["GET", "POST"])
def agregar():
    create_form = forms.CursoForm(request.form)
    if request.method == "POST":
        maestro_id = request.form.get('maestro_id')
        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=int(maestro_id) if maestro_id else None
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.listadoCurso'))
    lista_maestros = Maestros.query.all()
    return render_template("cursos/agregarCursos.html", form=create_form, maestros=lista_maestros)

@cursos.route("/cursos/detalles", methods=["GET"])
def detalles():
    id = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id == id).first()
    return render_template("cursos/detallesCursos.html", curso=curso)

@cursos.route("/cursos/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.CursoForm(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id
    if request.method == "POST":
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = int(request.form.get('maestro_id'))
        db.session.commit()
        return redirect(url_for('cursos.listadoCurso'))
    lista_maestros = Maestros.query.all()
    return render_template("cursos/modificarCursos.html", form=create_form, maestros=lista_maestros)

@cursos.route("/cursos/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.CursoForm(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id
    if request.method == "POST":
        id = create_form.id.data
        curso = db.session.get(Curso, id)
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.listadoCurso'))
    return render_template("cursos/eliminarCursos.html", form=create_form)

@cursos.route("/cursos/inscribir", methods=["GET", "POST"])
def inscribir():
    if request.method == "POST":
        alumno_id = request.form.get('alumno_id')
        curso_id = request.form.get('curso_id')
        alumno = db.session.get(Alumnos, alumno_id)
        curso = db.session.get(Curso, curso_id)
        if alumno and curso:
            if alumno in curso.alumnos:
                flash(f"{alumno.nombre} {alumno.apellidos} ya está inscrito en este curso.", "error")
            else:
                curso.alumnos.append(alumno)
                db.session.commit()
                flash(f"{alumno.nombre} {alumno.apellidos} inscrito correctamente.", "success")
        return redirect(url_for('cursos.inscribir', id=curso_id))
    curso_id = request.args.get('id')
    curso = Curso.query.get(curso_id)
    alumnos = Alumnos.query.all()
    return render_template("cursos/inscribir.html", curso=curso, alumnos=alumnos)
