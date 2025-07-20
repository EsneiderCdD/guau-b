from flask import jsonify
from app.models import Perro, SolicitudAdopcion
from app.extensions import db

def crear_solicitud(data):
    id_perro = data.get('id_perro')
    nombre_usuario = data.get('nombre_usuario')
    mensaje = data.get('mensaje')

    if not id_perro or not nombre_usuario:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    perro = Perro.query.get(id_perro)
    if not perro or perro.estado != 'disponible':
        return jsonify({'error': 'Perro no disponible'}), 400

    solicitud = SolicitudAdopcion(
        nombre_usuario=nombre_usuario,
        mensaje=mensaje,
        perro_id=id_perro
    )

    db.session.add(solicitud)
    db.session.commit()

    return jsonify({'mensaje': 'Solicitud creada exitosamente'}), 201
