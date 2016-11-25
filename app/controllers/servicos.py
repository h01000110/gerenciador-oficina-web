from app import app
from flask import render_template


@app.route("/")
def servicos():
    return render_template("servicos.html")
