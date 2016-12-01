from app import app, db
from app.models import tables
from flask import redirect, url_for, request, render_template


@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    cliente = tables.Servico.query.filter_by(id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        cpf = request.form.get("cpf")
        endereco = request.form.get("endereco")
        placa = request.form.get("placa")
        carro = request.form.get("carro")
        preco = request.form.get("preco")
        descricao = request.form.get("descricao")
        pago = request.form.get("pago")

        if nome and telefone and email and cpf and placa and carro\
           and endereco and preco and descricao and pago:
            for i in preco:
                if i not in '0123456789':
                    return redirect(url_for("servicos"))

            cliente.nome = nome
            cliente.telefone = telefone
            cliente.email = email
            cliente.cpf = cpf
            cliente.endereco = endereco
            cliente.placa = placa
            cliente.carro = carro
            cliente.preco = preco
            cliente.descricao = descricao
            cliente.pago = pago

            db.session.commit()
            return redirect(url_for("servicos"))

    return render_template("editar.html", cliente=cliente)
