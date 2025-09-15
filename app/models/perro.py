# app/models/perro.py

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
    imagen_card_uno = db.Column(db.String(255), nullable=True)
    imagen_card_dos = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

 
    energia = db.Column(db.Float, nullable=True)
    apego_vinculo = db.Column(db.Float, nullable=True)
    regulacion_emocional = db.Column(db.Float, nullable=True)
    exploracion_libertad = db.Column(db.Float, nullable=True)

    
    datos_fisicos = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f"<Perro {self.nombre}>"
