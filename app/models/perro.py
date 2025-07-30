from datetime import datetime
from app.extensions import db

class Perro(db.Model):
    __tablename__ = 'perros'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(20), default='disponible')  
    imagen_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Perro {self.nombre}>"
