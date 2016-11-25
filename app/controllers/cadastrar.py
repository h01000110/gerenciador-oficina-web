from app import app
from flask import render_template


@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")
