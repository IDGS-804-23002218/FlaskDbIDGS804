from consultas import consultas
from flask import render_template, request, flash
from models import db, Curso, Alumnos

@consultas.route("/consultas", methods=["GET"])
def index():
    cursos = Curso.query.all()
    alumnos = Alumnos.query.all()

    curso_id = request.args.get('curso_id')
    alumno_id = request.args.get('alumno_id')

    alumnos_en_curso = []
    cursos_de_alumno = []
    curso_seleccionado = None
    alumno_seleccionado = None

    if curso_id:
        curso_seleccionado = db.session.get(Curso, int(curso_id))
        if curso_seleccionado:
            alumnos_en_curso = curso_seleccionado.alumnos
            if not alumnos_en_curso:
                flash("Este curso no tiene alumnos inscritos.", "error")

    if alumno_id:
        alumno_seleccionado = db.session.get(Alumnos, int(alumno_id))
        if alumno_seleccionado:
            cursos_de_alumno = alumno_seleccionado.cursos
            if not cursos_de_alumno:
                flash("Este alumno no está inscrito en ningún curso.", "error")

    return render_template("consultas/index.html",
        cursos=cursos,
        alumnos=alumnos,
        alumnos_en_curso=alumnos_en_curso,
        cursos_de_alumno=cursos_de_alumno,
        curso_seleccionado=curso_seleccionado,
        alumno_seleccionado=alumno_seleccionado
    )