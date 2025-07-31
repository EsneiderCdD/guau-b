from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# 1. Cargar variables de entorno desde .env
load_dotenv()

# 2. Importar extensiones
from app.extensions import db

def create_app():
    app = Flask(__name__)

    # 3. Habilitar CORS
    CORS(app)

    # 4. Configuración del entorno
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'another-fallback-secret')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 5. Inicializar extensiones
    db.init_app(app)
    jwt = JWTManager(app)

    # 6. Registrar Blueprints
    from app.routes.perros import perros_bp
    from app.routes.solicitudes import solicitudes_bp
    from app.routes.auth import auth_bp  # 👈 NUEVO
    
    app.register_blueprint(perros_bp)
    app.register_blueprint(solicitudes_bp)
    app.register_blueprint(auth_bp)  # 👈 NUEVO

    # 7. Ruta de prueba
    @app.route('/')
    def index():
        return 'Servidor funcionando correctamente ✅'

    return app
