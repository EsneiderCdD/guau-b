from flask import Blueprint, request, jsonify

adopciones_bp = Blueprint('adopciones', __name__, url_prefix='/adopciones')

@adopciones_bp.route('/adoptar', methods=['POST'])
def crear_solicitud():
    # Lógica se implementará más adelante
    return jsonify({"mensaje": "Ruta POST /adoptar disponible"}), 200
