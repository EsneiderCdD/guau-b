from datetime import datetime
from app.extensions import db
from .perro import Perro 
from .usuario import Usuario  

class SolicitudAdopcion(db.Model):
    __tablename__ = 'solicitudes_adopcion'

    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.Text)
    estado = db.Column(db.String(20), default='pendiente')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    perro_id = db.Column(db.Integer, db.ForeignKey('perros.id'), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('solicitudes', lazy=True))
    perro = db.relationship('Perro', backref=db.backref('solicitudes', lazy=True))

    def __repr__(self):
        return f"<SolicitudAdopcion Usuario {self.usuario_id} - Perro {self.perro_id}>"
