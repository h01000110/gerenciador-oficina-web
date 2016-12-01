from app import app
from app.controllers.estatisticas import Estatistica
from app.models import tables
import linecache


@app.context_processor
def variaveis():
    lc = tables.Preferencias.query.filter_by(id=1).first()

    if lc.change == '1':
        lang = 'app/static/lang/ptBR.lang'
    elif lc.change == '2':
        lang = 'app/static/lang/enUS.lang'

    var = {'version': '0.0.3',
           'clientes': tables.Servico.query.all(),
           'clientes_completos': tables.Servico.query.order_by(tables.Servico
                                                               .data_saida),
           'fmes': Estatistica().fatura,
           'pfmes': Estatistica().pfatura,
           'afmes': Estatistica().afatura,
           'sfmes': Estatistica().sfatura,
           'spfmes': Estatistica().spfatura,
           'safmes': Estatistica().safatura,
           'ante': Estatistica().ante,
           'passado': Estatistica().passado,
           'atual': Estatistica().atual
           }

    for i in range(1, 76):
        var['lang_' + str(i)] = linecache.getline(lang, i)

    return var
