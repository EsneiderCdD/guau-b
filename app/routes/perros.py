from flask import Blueprint, jsonify
from app.controllers.perros_controller import get_perros
from app.models.perro import Perro
from app.utils.serializers import serialize_perro

perros_bp = Blueprint('perros', __name__, url_prefix='/perros')

@perros_bp.route('/', methods=['GET'])
def listar_perros():
    return get_perros()

@perros_bp.route('/<int:perro_id>', methods=['GET'])
def obtener_perro_por_id(perro_id):
    perro = Perro.query.get(perro_id)
    if not perro:
        return jsonify({'error': 'Perro no encontrado'}), 404
    return jsonify(serialize_perro(perro)), 200
