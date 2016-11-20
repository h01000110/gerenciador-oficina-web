from app import app, db
from app.models import tables
from flask import redirect, url_for, request


@app.route("/deletar/<int:id>")
def deletar(id):
    base = request.url_root
    origem = request.referrer
    origem = origem.split(base)[1]

    if origem == '':
        origem = 'servicos'

    cliente = tables.Servico.query.filter_by(id=id).first()

    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for(origem))
