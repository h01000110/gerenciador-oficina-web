from app import app, db
from app.models import tables
from flask import request, redirect, url_for


@app.route("/lang", methods=['POST'])
def lang():
    c = tables.Preferencias.query.filter_by(id=1).first()
    lc = request.form.get('choice')

    if lc in ['1', '2']:
        c.change = lc
        db.session.commit()

    return redirect(url_for('preferencias'))
