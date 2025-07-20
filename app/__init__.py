# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Aquí luego se agregarán las configuraciones, extensiones y Blueprints
    @app.route('/')
    def index():
        return 'Servidor funcionando correctamente ✅'

    return app
