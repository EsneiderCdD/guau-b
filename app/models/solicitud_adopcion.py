from datetime import datetime
from app.extensions import db
from .perro import Perro  # Relación con modelo Perro

class SolicitudAdopcion(db.Model):
    __tablename__ = 'solicitudes_adopcion'

    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.Text)
    estado = db.Column(db.String(20), default='pendiente')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    perro_id = db.Column(db.Integer, db.ForeignKey('perros.id'), nullable=False)
    perro = db.relationship('Perro', backref=db.backref('solicitudes', lazy=True))

    def __repr__(self):
        return f"<SolicitudAdopcion {self.nombre_usuario} - Perro ID {self.perro_id}>"
