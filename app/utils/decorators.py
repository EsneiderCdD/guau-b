from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from app.models.usuario import Usuario

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = Usuario.query.get(user_id)
        if not user or user.rol != 'admin':
            return jsonify({"error": "Acceso no autorizado"}), 403
        return fn(*args, **kwargs)
    return wrapper
