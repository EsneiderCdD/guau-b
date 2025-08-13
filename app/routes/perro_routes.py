from flask import Blueprint, request
from app.controllers.perros_controller import actualizar_perro

perro_bp = Blueprint("perro_bp", __name__)

@perro_bp.route("/perros/<int:perro_id>", methods=["PUT"])
def actualizar_perro_route(perro_id):
    data = request.get_json()
    return actualizar_perro(perro_id, data)
