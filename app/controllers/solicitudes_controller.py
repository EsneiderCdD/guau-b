from flask import jsonify
from app.models import Perro, SolicitudAdopcion
from app.extensions import db
from app.utils.validators import validate_solicitud_data 

def crear_solicitud(data):
    try:
        # Validación explícita
        errores = validate_solicitud_data(data)
        if errores:
            return jsonify({'errores': errores}), 400

        id_perro = int(data['id_perro'])  # ya validado como número

        # Buscar el perro
        perro = Perro.query.get(id_perro)
        if not perro:
            return jsonify({'error': 'El perro no existe.'}), 404

        if perro.estado != 'disponible':
            return jsonify({'error': 'El perro no está disponible para adopción.'}), 400

        solicitud = SolicitudAdopcion(
            nombre_usuario=data['nombre_usuario'],
            mensaje=data['mensaje'],
            perro_id=id_perro
        )

        db.session.add(solicitud)
        db.session.commit()

        return jsonify({'mensaje': 'Solicitud creada exitosamente'}), 201

    except Exception as e:
        # Para producción puedes loguearlo mejor
        return jsonify({'error': 'Error inesperado en el servidor.', 'detalle': str(e)}), 500

