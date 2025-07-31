from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required  # ✅ Para proteger la ruta
from app.controllers.solicitudes_controller import crear_solicitud  # Tu controlador

solicitudes_bp = Blueprint('solicitudes', __name__, url_prefix='/solicitudes')
@solicitudes_bp.route('/adoptar', methods=['POST'])
@jwt_required()
def solicitar_adopcion():
    data = request.json
    return crear_solicitud(data)
