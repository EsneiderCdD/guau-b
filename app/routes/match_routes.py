# app/routes/match_routes.py

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.usuario import Usuario
from app.models.perro import Perro
from app.models.match_usuario import MatchUsuario
from app.utils.match import calcular_compatibilidad
from app.extensions import db

match_bp = Blueprint('match', __name__, url_prefix='/match')


@match_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_match(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    perfil = MatchUsuario.query.filter_by(usuario_id=usuario.id).first()
    if not perfil:
        return jsonify({'error': 'El usuario no tiene perfil de matching'}), 400

    perros = Perro.query.filter_by(estado='disponible').all()
    resultados = []

    for perro in perros:
        compat = calcular_compatibilidad(perfil, perro)
        if compat is not None:
            resultados.append({
                "perro_id": perro.id,
                "nombre": perro.nombre,
                "raza": perro.raza,
                "edad": perro.edad,
                "descripcion": perro.descripcion,
                "imagen_url": perro.imagen_url,
                "compatibilidad": compat
            })

    resultados_ordenados = sorted(resultados, key=lambda x: x["compatibilidad"], reverse=True)

    return jsonify(resultados_ordenados), 200


@match_bp.route('/responder', methods=['POST'])
@jwt_required()
def responder_encuesta():
    user_id = get_jwt_identity()
    data = request.get_json()

    # Extraer y validar datos
    t = data.get('tiempo_disponible')
    e = data.get('experiencia')
    a = data.get('apego_emocional')

    if t not in [1, 2, 3] or e not in [0, 1] or a not in [0, 1, 2]:
        return jsonify({'error': 'Valores inválidos. Verifica T(1-3), E(0-1), A(0-2).'}), 400

    perfil = MatchUsuario.query.filter_by(usuario_id=user_id).first()

    if perfil:
        perfil.tiempo_disponible = t
        perfil.experiencia = e
        perfil.apego_emocional = a
        mensaje = 'Perfil actualizado'
    else:
        perfil = MatchUsuario(
            usuario_id=user_id,
            tiempo_disponible=t,
            experiencia=e,
            apego_emocional=a
        )
        db.session.add(perfil)
        mensaje = 'Perfil creado'

    db.session.commit()
    return jsonify({'mensaje': f'{mensaje} correctamente'}), 200
