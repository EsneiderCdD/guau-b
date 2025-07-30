from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.perros_controller import get_perros
from app.models.perro import Perro
from app.utils.serializers import serialize_perro
from app.utils.decorators import admin_required
from app.extensions import db

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

@perros_bp.route('/', methods=['POST'])
@jwt_required()
@admin_required
def crear_perro():
    data = request.get_json()

    nombre = data.get("nombre")
    edad = data.get("edad")
    raza = data.get("raza")
    descripcion = data.get("descripcion")
    imagen_url = data.get("imagen_url")

    if not nombre or not edad or not raza:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    nuevo_perro = Perro(
        nombre=nombre,
        edad=edad,
        raza=raza,
        descripcion=descripcion,
        imagen_url=imagen_url,
        estado='disponible'
    )

    db.session.add(nuevo_perro)
    db.session.commit()

    return jsonify(serialize_perro(nuevo_perro)), 201

@perros_bp.route('/<int:perro_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def eliminar_perro(perro_id):
    perro = Perro.query.get(perro_id)
    if not perro:
        return jsonify({'error': 'Perro no encontrado'}), 404

    db.session.delete(perro)
    db.session.commit()

    return jsonify({'mensaje': 'Perro eliminado correctamente'}), 200
