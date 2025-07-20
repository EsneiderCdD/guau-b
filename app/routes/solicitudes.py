from flask import Blueprint, request, jsonify
from app.controllers.solicitudes_controller import crear_solicitud

solicitudes_bp = Blueprint('solicitudes', __name__, url_prefix='/solicitudes')

@solicitudes_bp.route('/adoptar', methods=['POST'])
def solicitar_adopcion():
    data = request.json
    return crear_solicitud(data)
