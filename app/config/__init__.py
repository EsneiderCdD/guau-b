from flask import Flask
from dotenv import load_dotenv
import os

# 1. Cargar variables de entorno desde .env
load_dotenv()

# 2. Importar extensiones
from app.extensions import db  # si luego agregas migrate, irá aquí también

def create_app():
    app = Flask(__name__)

    # 3. Cargar configuración basada en FLASK_ENV
    env_config = os.getenv("FLASK_ENV", "development").capitalize() + "Config"
    app.config.from_object(f"config.config.{env_config}")

    # 4. Inicializar extensiones
    db.init_app(app)

    # 5. Registrar Blueprints
    from app.routes.perros import perros_bp
    app.register_blueprint(perros_bp)

    # 6. Ruta raíz
    @app.route('/')
    def index():
        return 'Servidor funcionando correctamente ✅'

    return app
