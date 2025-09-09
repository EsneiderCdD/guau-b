# app/models/match_usuario.py

from datetime import datetime
from app.extensions import db

class MatchUsuario(db.Model):
    __tablename__ = 'match_usuarios'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    # ---- 4 dimensiones (0–4) ----
    energia = db.Column(db.Float, nullable=True)
    apego_vinculo = db.Column(db.Float, nullable=True)
    regulacion_emocional = db.Column(db.Float, nullable=True)
    exploracion_libertad = db.Column(db.Float, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    usuario = db.relationship('Usuario', backref='matchs')

    def __repr__(self):
        return f"<MatchUsuario usuario_id={self.usuario_id}>"
