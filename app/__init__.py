from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS  # ← NUEVO

# 1. Cargar variables de entorno
load_dotenv()

# 2. Importar la extensión de SQLAlchemy
from app.extensions import db

def create_app():
    app = Flask(__name__)
    
    # 3. Habilitar CORS
    CORS(app)  # ← NUEVO

    # 4. Configuración desde .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 5. Inicializar extensiones
    db.init_app(app)

    # 6. Registrar Blueprints
    from app.routes.perros import perros_bp
    from app.routes.solicitudes import solicitudes_bp
    app.register_blueprint(perros_bp)
    app.register_blueprint(solicitudes_bp)

    # 7. Ruta raíz de prueba
    @app.route('/')
    def index():
        return 'Servidor funcionando correctamente ✅'

    return app
