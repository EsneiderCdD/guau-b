from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.solicitudes_controller import (
    crear_solicitud,
    obtener_solicitudes,
    obtener_solicitud_por_id,
    eliminar_solicitud
)
from app.models.usuario import Usuario

solicitudes_bp = Blueprint('solicitudes', __name__, url_prefix='/solicitudes')

@solicitudes_bp.route('/adoptar', methods=['POST'])
@jwt_required()
def solicitar_adopcion():
    data = request.json
    return crear_solicitud(data)

# NUEVO
@solicitudes_bp.route('/', methods=['GET'])
@jwt_required()
def listar_solicitudes():
    usuario_id = get_jwt_identity()
    usuario = Usuario.query.get(usuario_id)
    if not usuario or usuario.rol != 'admin':

        return jsonify({'error': 'Acceso no autorizado'}), 403
    return obtener_solicitudes()

# NUEVO
@solicitudes_bp.route('/<int:solicitud_id>', methods=['GET'])
@jwt_required()
def ver_solicitud(solicitud_id):
    usuario_id = get_jwt_identity()
    usuario = Usuario.query.get(usuario_id)
    if not usuario or usuario.rol != 'admin':
        return jsonify({'error': 'Acceso no autorizado'}), 403
    return obtener_solicitud_por_id(solicitud_id)

# NUEVO
@solicitudes_bp.route('/<int:solicitud_id>', methods=['DELETE'])
@jwt_required()
def borrar_solicitud(solicitud_id):
    usuario_id = get_jwt_identity()
    usuario = Usuario.query.get(usuario_id)
    if not usuario or usuario.rol != 'admin':
        return jsonify({'error': 'Acceso no autorizado'}), 403
    return eliminar_solicitud(solicitud_id)
