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

    perro = Perro.query.get(perro_id)
    if not perro:
        return jsonify({'error': 'Perro no encontrado'}), 404

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

# NUEVO
def obtener_solicitudes():
    solicitudes = SolicitudAdopcion.query.all()
    resultado = []
    for s in solicitudes:
        resultado.append({
            'id': s.id,
            'usuario_id': s.usuario_id,
            'perro_id': s.perro_id,
            'estado': s.estado,
            'mensaje': s.mensaje,
            'created_at': s.created_at.isoformat()
        })
    return jsonify(resultado), 200

# NUEVO
def obtener_solicitud_por_id(solicitud_id):
    solicitud = SolicitudAdopcion.query.get(solicitud_id)
    if not solicitud:
        return jsonify({'error': 'Solicitud no encontrada'}), 404

    return jsonify({
        'id': solicitud.id,
        'usuario_id': solicitud.usuario_id,
        'perro_id': solicitud.perro_id,
        'estado': solicitud.estado,
        'mensaje': solicitud.mensaje,
        'created_at': solicitud.created_at.isoformat()
    }), 200

# NUEVO
def eliminar_solicitud(solicitud_id):
    solicitud = SolicitudAdopcion.query.get(solicitud_id)
    if not solicitud:
        return jsonify({'error': 'Solicitud no encontrada'}), 404

    db.session.delete(solicitud)
    db.session.commit()
    return jsonify({'mensaje': 'Solicitud eliminada'}), 200
