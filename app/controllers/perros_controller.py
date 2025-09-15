from flask import jsonify
from app.models.perro import Perro
from app.extensions import db
from app.utils.serializers import serialize_perro

def get_perros():
    perros_disponibles = Perro.query.filter_by(estado="disponible").all()
    perros_serializados = [serialize_perro(p) for p in perros_disponibles]
    return jsonify(perros_serializados), 200
def actualizar_perro(perro_id, data):
    perro = Perro.query.get(perro_id)
    if not perro:
        return jsonify({"error": "Perro no encontrado"}), 404

    campos = [
        "nombre", "raza", "edad", "descripcion", "estado",
        "imagen_url", "imagen_card_uno", "imagen_card_dos",
        "energia", "apego_vinculo", "regulacion_emocional",
        "exploracion_libertad", "datos_fisicos"
    ]
    
    for campo in campos:
        if campo in data:
            setattr(perro, campo, data[campo])

    db.session.commit()

    return jsonify(serialize_perro(perro)), 200
