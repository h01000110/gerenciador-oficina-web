from app import app, db
from app.models import tables
from flask import request, redirect, url_for


@app.route("/cadastro", methods=['POST'])
def cadastro():
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
            for i in preco:
                if i not in '0123456789':
                    return redirect(url_for("cadastrar"))

            c = tables.Servico(nome, telefone, email, cpf, placa, carro,
                               preco, descricao, pago)
            db.session.add(c)
            db.session.commit()

    return redirect(url_for("servicos"))
