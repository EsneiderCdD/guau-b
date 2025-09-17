# app/routes/match_routes.py

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.usuario import Usuario
from app.models.perro import Perro
from app.models.match_usuario import MatchUsuario
from app.utils.match import calcular_compatibilidad
from app.utils.serializers import serialize_perro, serialize_match_usuario
from app.extensions import db

match_bp = Blueprint('match', __name__, url_prefix='/match')

@match_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_match(usuario_id):
    """
    Devuelve lista de perros (estado 'disponible') con su compatibilidad
    respecto al usuario con id = usuario_id.
    """
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
    """
    Recibe payload con el perfil del usuario y lo crea/actualiza en MatchUsuario.
    Espera JSON con cualquiera de estos formatos:
    1) { "vector": [energia, apego_vinculo, regulacion_emocional, exploracion_libertad], "datos_fisicos": {...} }
    2) { "energia": x, "apego_vinculo": y, "regulacion_emocional": z, "exploracion_libertad": w, "datos_fisicos": {...} }

    Valores válidos para dimensiones: números entre 0 y 4 (acepta floats).
    """
    user_id = get_jwt_identity()
    data = request.get_json() or {}

    # aceptar vector o campos individuales
    vector = data.get('vector')
    if vector and isinstance(vector, (list, tuple)) and len(vector) >= 4:
        try:
            energia = float(vector[0])
            apego_vinculo = float(vector[1])
            regulacion_emocional = float(vector[2])
            exploracion_libertad = float(vector[3])
        except (ValueError, TypeError):
            return jsonify({'error': 'Vector inválido. Debe contener números.'}), 400
    else:
        try:
            energia = float(data.get('energia', 0))
            apego_vinculo = float(data.get('apego_vinculo', 0))
            regulacion_emocional = float(data.get('regulacion_emocional', 0))
            exploracion_libertad = float(data.get('exploracion_libertad', 0))
        except (ValueError, TypeError):
            return jsonify({'error': 'Campos de dimensiones inválidos.'}), 400

    # validar rango 0..4
    for val in (energia, apego_vinculo, regulacion_emocional, exploracion_libertad):
        if val < 0 or val > 4:
            return jsonify({'error': 'Cada dimensión debe estar entre 0 y 4.'}), 400

    datos_fisicos = data.get('datos_fisicos')

    perfil = MatchUsuario.query.filter_by(usuario_id=user_id).first()

    if perfil:
        perfil.energia = energia
        perfil.apego_vinculo = apego_vinculo
        perfil.regulacion_emocional = regulacion_emocional
        perfil.exploracion_libertad = exploracion_libertad
        perfil.datos_fisicos = datos_fisicos
        mensaje = 'Perfil actualizado'
    else:
        perfil = MatchUsuario(
            usuario_id=user_id,
            energia=energia,
            apego_vinculo=apego_vinculo,
            regulacion_emocional=regulacion_emocional,
            exploracion_libertad=exploracion_libertad,
            datos_fisicos=datos_fisicos
        )
        db.session.add(perfil)
        mensaje = 'Perfil creado'

    db.session.commit()

    return jsonify({
        'mensaje': f'{mensaje} correctamente',
        'perfil': serialize_match_usuario(perfil)
    }), 200


@match_bp.route('/me', methods=['GET'])
@jwt_required()
def obtener_mi_perfil():
    """
    Devuelve el perfil de matching del usuario autenticado.
    """
    user_id = get_jwt_identity()
    perfil = MatchUsuario.query.filter_by(usuario_id=user_id).first()
    if not perfil:
        return jsonify({'error': 'No existe perfil para este usuario'}), 404
    return jsonify(serialize_match_usuario(perfil)), 200
