from app import app
from flask import render_template
from app.controllers.estatisticas import Estatistica


@app.route("/sobre")
def sobre():
    title = 'Sobre'
    fmes = Estatistica().fatura
    pfmes = Estatistica().pfatura
    afmes = Estatistica().afatura
    sfmes = Estatistica().sfatura
    spfmes = Estatistica().spfatura
    safmes = Estatistica().safatura
    ante = Estatistica().ante
    passado = Estatistica().passado
    atual = Estatistica().atual

    return render_template("sobre.html", title=title, fmes=fmes, pfmes=pfmes,
                           afmes=afmes, sfmes=sfmes, spfmes=spfmes,
                           safmes=safmes, ante=ante, passado=passado,
                           atual=atual)
