from app import app
from flask import render_template


@app.route("/concluidos")
def concluidos():
    return render_template("concluidos.html")
