from flask import Flask
from flask_migrate import Migrate
from app import create_app
from app.extensions import db
from app.models import Perro, SolicitudAdopcion  # importa todos los modelos aquí

app = create_app()
migrate = Migrate(app, db)
