# app/routes/match_routes.py

from flask import Blueprint, jsonify
from app.models.usuario import Usuario
from app.models.perro import Perro
from app.models.match_usuario import MatchUsuario
from app.utils.match import calcular_compatibilidad

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
