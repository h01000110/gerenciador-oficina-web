from app import app
from flask import render_template


@app.route("/preferencias")
def preferencias():
    return render_template("preferencias.html")
