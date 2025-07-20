from flask import jsonify
from app.models.perro import Perro
from app.extensions import db
from app.utils.serializers import serialize_perro

def get_perros():
    perros_disponibles = Perro.query.filter_by(estado="disponible").all()
    perros_serializados = [serialize_perro(p) for p in perros_disponibles]
    return jsonify(perros_serializados), 200
