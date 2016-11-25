from app import db
import datetime


class Servico(db.Model):
    __tablename__ = 'servicos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    email = db.Column(db.String)
    cpf = db.Column(db.String)
    placa = db.Column(db.String)
    carro = db.Column(db.String)
    preco = db.Column(db.String)
    descricao = db.Column(db.String)
    pago = db.Column(db.String)
    data_entrada = db.Column(db.String)
    data_saida = db.Column(db.String)

    def __init__(self, nome, telefone, email, cpf, placa,
                 carro, preco, descricao, pago, data_entrada=None,
                 data_saida=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.placa = placa
        self.carro = carro
        self.preco = preco
        self.descricao = descricao
        self.pago = pago
        if data_entrada is None:
            data_entrada = datetime.datetime.now().strftime("%H:%M %d-%m-%Y")
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def __repr__(self):
        return '<Cliente: %r>' % self.nome


class Preferencias(db.Model):
    __tablename__ = 'preferencias'

    id = db.Column(db.Integer, primary_key=True)
    change = db.Column(db.String)

    def __init__(self, change):
        self.change = change


db.create_all()


c = Preferencias.query.filter_by(id=1).first()

if c is None:
        a = '1'
        b = Preferencias(a)
        db.session.add(b)
        db.session.commit()
