# app/models/match_usuario.py

from datetime import datetime
from app.extensions import db

class MatchUsuario(db.Model):
    __tablename__ = 'match_usuarios'

    id = db.Column(db.Integer, primary_key=True)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    tiempo_disponible = db.Column(db.Integer, nullable=False)        # 1–3
    experiencia = db.Column(db.Integer, nullable=False)              # 0–1
    apego_emocional = db.Column(db.Integer, nullable=False)          # 0–2

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones (opcional, útil para acceso directo desde Usuario)
    usuario = db.relationship('Usuario', backref='matchs')

    def __repr__(self):
        return f"<MatchUsuario usuario_id={self.usuario_id}>"
