from flask import Blueprint, jsonify

perros_bp = Blueprint('perros', __name__, url_prefix='/perros')

@perros_bp.route('/')
def get_perros():
    return jsonify({"message": "Ruta modular perros funcionando ✅ "})
