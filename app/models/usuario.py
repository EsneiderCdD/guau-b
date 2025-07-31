# app/models/usuario.py

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    # Nombre simple (tipo nickname)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    # Contraseña en forma de hash
    password_hash = db.Column(db.String(256), nullable=False)
    # Rol del usuario ('admin' por defecto)
    rol = db.Column(db.String(20), default='user')  # ya no "admin"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Usuario {self.nombre}>"

    # Métodos auxiliares
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
