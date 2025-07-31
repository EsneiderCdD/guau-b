from flask import jsonify
from app.models.solicitud_adopcion import SolicitudAdopcion
from app.models.perro import Perro
from app.extensions import db
from flask_jwt_extended import get_jwt_identity
from app.models.usuario import Usuario

def crear_solicitud(data):
    usuario_id = get_jwt_identity()
    perro_id = data.get('perro_id')
    mensaje = data.get('mensaje')

    # Verificar que el perro exista
    perro = Perro.query.get(perro_id)
    if not perro:
        return jsonify({'error': 'Perro no encontrado'}), 404

    # Verificar si ya existe una solicitud pendiente del mismo usuario y perro
    solicitud_existente = SolicitudAdopcion.query.filter_by(
        usuario_id=usuario_id,
        perro_id=perro_id,
        estado='pendiente'
    ).first()
    if solicitud_existente:
        return jsonify({'error': 'Ya enviaste una solicitud pendiente para este perro.'}), 400

    nueva_solicitud = SolicitudAdopcion(
        usuario_id=usuario_id,
        perro_id=perro_id,
        mensaje=mensaje
    )

    db.session.add(nueva_solicitud)
    db.session.commit()

    return jsonify({
        'mensaje': 'Solicitud enviada con éxito',
        'solicitud': {
            'id': nueva_solicitud.id,
            'usuario_id': usuario_id,
            'perro_id': perro_id,
            'estado': nueva_solicitud.estado
        }
    }), 201
