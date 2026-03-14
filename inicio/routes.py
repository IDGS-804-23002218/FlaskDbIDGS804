from inicio import inicio
from flask import render_template

@inicio.route("/")
def index():
    return render_template("inicio/index.html")