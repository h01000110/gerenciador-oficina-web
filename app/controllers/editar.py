from app import app, db
from app.models import tables
from flask import redirect, url_for, request, render_template
from app.controllers.estatisticas import Estatistica


@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    cliente = tables.Servico.query.filter_by(id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        cpf = request.form.get("cpf")
        placa = request.form.get("placa")
        carro = request.form.get("carro")
        preco = request.form.get("preco")
        descricao = request.form.get("descricao")
        pago = request.form.get("pago")

        if nome and telefone and email and cpf and placa and carro\
           and preco and descricao and pago:
            cliente.nome = nome
            cliente.telefone = telefone
            cliente.email = email
            cliente.cpf = cpf
            cliente.placa = placa
            cliente.carro = carro
            cliente.preco = preco
            cliente.descricao = descricao
            cliente.pago = pago

            db.session.commit()
            return redirect(url_for("servicos"))

    fmes = Estatistica().fatura
    pfmes = Estatistica().pfatura
    afmes = Estatistica().afatura
    sfmes = Estatistica().sfatura
    spfmes = Estatistica().spfatura
    safmes = Estatistica().safatura
    ante = Estatistica().ante
    passado = Estatistica().passado
    atual = Estatistica().atual

    return render_template("editar.html", cliente=cliente, fmes=fmes,
                           pfmes=pfmes, afmes=afmes, sfmes=sfmes,
                           spfmes=spfmes, safmes=safmes, ante=ante,
                           passado=passado, atual=atual)
