from app import app
from flask import render_template


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
