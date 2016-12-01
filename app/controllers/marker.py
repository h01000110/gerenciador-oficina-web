from app import app
from flask import jsonify
import googlemaps
from app.models import tables


@app.route("/marker", methods=['GET', 'POST'])
def marker():
    gmaps = googlemaps.Client(key='AIzaSyBTAZR4fz-04spJRu7-9RylbyEvFqjY3WU')

    clientes = tables.Servico.query.all()
    end = []
    for i in clientes:
        end.append(i.endereco)

    dicio = {}
    for i in end:
        a = gmaps.geocode(i)[0]['geometry']['location']['lat']
        b = gmaps.geocode(i)[0]['geometry']['location']['lng']
        dicio[end.index(i)] = [a, b]

    return jsonify(dicio=dicio)
