from flask import Flask
from flask_migrate import Migrate
from flask.cli import FlaskGroup
from app import create_app
from app.extensions import db

# ⏬ Importar TODOS los modelos para que Alembic los detecte
from app.models.perro import Perro
from app.models.solicitud_adopcion import SolicitudAdopcion
from app.models.usuario import Usuario

app = create_app()
migrate = Migrate(app, db)

# ⏬ Habilita comandos de Flask CLI
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
