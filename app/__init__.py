from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import cadastrar
from app.controllers import cadastro
from app.controllers import concluidos
from app.controllers import concluir
from app.controllers import deletar
from app.controllers import editar
from app.controllers import pdf
from app.controllers import servicos
from app.controllers import sobre
from app.models import tables
