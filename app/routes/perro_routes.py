from flask import Blueprint, request, jsonify
from app.models.perro import Perro
from app.extensions import db
from app.utils.serializers import serialize_perro

perro_bp = Blueprint("perro_bp", __name__)

@perro_bp.route("/perros/<int:perro_id>", methods=["PUT"])
def actualizar_perro(perro_id):
    perro = Perro.query.get(perro_id)

    if not perro:
        return jsonify({"error": "Perro no encontrado"}), 404

    data = request.get_json()

    # Actualizamos solo si el campo viene en el JSON
    if "nombre" in data:
        perro.nombre = data["nombre"]
    if "raza" in data:
        perro.raza = data["raza"]
    if "edad" in data:
        perro.edad = data["edad"]
    if "descripcion" in data:
        perro.descripcion = data["descripcion"]
    if "estado" in data:
        perro.estado = data["estado"]
    if "imagen_url" in data:
        perro.imagen_url = data["imagen_url"]
    if "imagen_card_uno" in data:
        perro.imagen_card_uno = data["imagen_card_uno"]
    if "imagen_card_dos" in data:
        perro.imagen_card_dos = data["imagen_card_dos"]
    if "tiempo_requerido" in data:
        perro.tiempo_requerido = data["tiempo_requerido"]
    if "requiere_experiencia" in data:
        perro.requiere_experiencia = data["requiere_experiencia"]
    if "apego_esperado" in data:
        perro.apego_esperado = data["apego_esperado"]

    db.session.commit()

    return jsonify(serialize_perro(perro)), 200
