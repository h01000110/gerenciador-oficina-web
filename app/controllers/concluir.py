from app import app, db
from app.models import tables
from flask import redirect, url_for
import datetime


@app.route("/concluir/<int:id>")
def concluir(id):
    cliente = tables.Servico.query.filter_by(id=id).first()
    cliente.data_saida = datetime.datetime.now().strftime("%H:%M %d-%m-%Y")

    db.session.commit()

    return redirect(url_for('servicos'))
