from app import app
from app.models import tables
from flask import render_template, make_response
import pdfkit
import datetime


@app.route("/pdf")
def pdf():
    date = datetime.datetime.now().strftime("%H:%M_%d-%m-%Y")
    clientes = tables.Servico.query.filter(tables.Servico.data_saida
                                           .contains('20'))

    rendered = render_template('pdf-file.html', clientes=clientes, date=date)
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'attachment; filename=backup_' + date + '.pdf'

    return response
