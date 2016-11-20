from app import app
from app.models import tables
from flask import render_template
from app.controllers.estatisticas import Estatistica


@app.route("/")
def servicos():
    title = 'Serviços em Andamento'
    clientes = tables.Servico.query.all()
    fmes = Estatistica().fatura
    pfmes = Estatistica().pfatura
    afmes = Estatistica().afatura
    sfmes = Estatistica().sfatura
    spfmes = Estatistica().spfatura
    safmes = Estatistica().safatura
    ante = Estatistica().ante
    passado = Estatistica().passado
    atual = Estatistica().atual

    return render_template("servicos.html", title=title, clientes=clientes,
                           fmes=fmes, pfmes=pfmes, afmes=afmes, sfmes=sfmes,
                           spfmes=spfmes, safmes=safmes, ante=ante,
                           passado=passado, atual=atual)
