from app import app
from flask import render_template


@app.route("/mapa")
def mapa():
    return render_template("mapa.html")
