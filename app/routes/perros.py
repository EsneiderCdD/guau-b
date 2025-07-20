from flask import Blueprint, jsonify
from app.models import Perro

perros_bp = Blueprint('perros', __name__, url_prefix='/perros')

@perros_bp.route('/', methods=['GET'])
def get_perros():
    perros = Perro.query.all()
    resultado = [{
        'id': p.id,
        'nombre': p.nombre,
        'raza': p.raza,
        'edad': p.edad,
        'descripcion': p.descripcion,
        'estado': p.estado,
        'imagen_url': p.imagen_url,
        'created_at': p.created_at.isoformat() if p.created_at else None
    } for p in perros]
    
    return jsonify(resultado)
