from app.models import tables
import datetime


def Fatura(x):
    x = tables.Servico.query.filter(tables.Servico.data_entrada.
                                    contains('-' + x + '-'))\
                            .filter_by(pago="Sim").all()
    fatura = 0
    for i in x:
        b = x.index(i)
        fatura += int(x[b].preco)
    return fatura


class Estatistica():
    def __init__(self):
        hoje = datetime.datetime.now().strftime("%m")

        self.atual = hoje

        if hoje is '01':
            self.passado = '12'
        else:
            self.passado = str(int(hoje) - 1)
            if self.passado in '123456789':
                self.passado = '0' + self.passado

        if hoje is '2':
            self.ante = '12'
        else:
            self.ante = str(int(hoje) - 2)
            if self.ante in '123456789':
                self.ante = '0' + self.ante

        self.fatura = int(Fatura(self.atual))
        self.pfatura = int(Fatura(self.passado))
        self.afatura = int(Fatura(self.ante))
        self.sfatura = self.fatura
        self.spfatura = self.pfatura
        self.safatura = self.afatura

        if self.fatura == 0:
            self.fatura = 1

        if self.pfatura == 0:
            self.pfatura = 1

        if self.afatura == 0:
            self.afatura = 1

        if self.fatura > self.pfatura and self.fatura > self.afatura:
            self.ffatura = self.fatura
        else:
            if self.pfatura > self.afatura:
                self.ffatura = self.pfatura
            else:
                self.ffatura = self.afatura

        self.fatura = (self.fatura / self.ffatura) * 100
        self.pfatura = (self.pfatura / self.ffatura) * 100
        self.afatura = (self.afatura / self.ffatura) * 100
