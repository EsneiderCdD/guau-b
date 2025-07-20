# config/config.py

import os
from dotenv import load_dotenv

# Carga las variables desde .env
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
    DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///default.db")
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"


class ProductionConfig(Config):
    FLASK_ENV = "production"


class TestingConfig(Config):
    TESTING = True
    FLASK_ENV = "testing"
