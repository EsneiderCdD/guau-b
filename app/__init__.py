from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuración básica desde .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')

    # Registro del Blueprint de perros
    from app.routes.perros import perros_bp
    app.register_blueprint(perros_bp)

    # Ruta raíz
    @app.route('/')
    def index():
        return 'Servidor funcionando correctamente ✅'

    return app
