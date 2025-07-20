def validate_solicitud_data(data):
    errors = {}

    if 'id_perro' not in data:
        errors['id_perro'] = 'Este campo es requerido.'
    elif not isinstance(data['id_perro'], int) or data['id_perro'] <= 0:
        errors['id_perro'] = 'Debe ser un número entero positivo.'

    if 'nombre_usuario' not in data:
        errors['nombre_usuario'] = 'Este campo es requerido.'
    elif not isinstance(data['nombre_usuario'], str) or not data['nombre_usuario'].strip():
        errors['nombre_usuario'] = 'Debe ser un texto no vacío.'

    if 'mensaje' not in data:
        errors['mensaje'] = 'Este campo es requerido.'
    elif not isinstance(data['mensaje'], str) or len(data['mensaje'].strip()) < 10:
        errors['mensaje'] = 'Debe tener al menos 10 caracteres.'

    return errors
