from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from maestros import maestros
from cursos import cursos
from alumnos import alumnos
from consultas import consultas
from inicio import inicio
from models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(cursos)
app.register_blueprint(alumnos)
app.register_blueprint(inicio)
app.register_blueprint(consultas)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()
csrf.init_app(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()