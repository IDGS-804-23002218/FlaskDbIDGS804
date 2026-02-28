from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import datetime

db= SQLAlchemy()
class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(200))
    email=db.Column(db.String(120))
    telefono=db.Column(db.String(20))
    create_date = db.Column(db.DateTime, server_default=func.now())
    
class Maestros (db.Model):
    __tablename__ = 'maestros'
    matricula=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(50))
    especialidad=db.Column(db.String(50))
    email=db.Column(db.String(50))
    
