from flask import Flask
from dotenv import load_dotenv
import os

# 1. Cargar variables de entorno
load_dotenv()

# 2. Importar la extensión de SQLAlchemy
from app.extensions import db

def create_app():
    app = Flask(__name__)

    # 3. Configuración básica desde .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 4. Inicializar SQLAlchemy con el app
    db.init_app(app)

    # 5. Registrar Blueprints
    from app.routes.perros import perros_bp
    from app.routes.adopciones import adopciones_bp
    app.register_blueprint(perros_bp)
    app.register_blueprint(adopciones_bp)

    # 6. Ruta raíz
    @app.route('/')
    def index():
        return 'Servidor funcionando correctamente ✅'

    return app
