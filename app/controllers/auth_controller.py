from flask import request, jsonify
from app.models.usuario import Usuario
from app.extensions import db
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

def login_user():
    data = request.get_json()

    nombre = data.get("nombre")
    password = data.get("password")

    if not nombre or not password:
        return jsonify({"error": "Nombre y contraseña requeridos"}), 400

    user = Usuario.query.filter_by(nombre=nombre).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    # ✅ Convertir el ID a string para el token
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "nombre": user.nombre,
            "rol": user.rol
        }
    }), 200

def registrar_usuario():
    data = request.get_json()
    nombre = data.get("nombre")
    password = data.get("password")

    if not nombre or not password:
        return jsonify({"error": "Nombre y contraseña requeridos"}), 400

    existente = Usuario.query.filter_by(nombre=nombre).first()
    if existente:
        return jsonify({"error": "El nombre ya está en uso"}), 409

    nuevo_usuario = Usuario(nombre=nombre)
    nuevo_usuario.set_password(password)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario registrado correctamente",
        "usuario": {
            "id": nuevo_usuario.id,
            "nombre": nuevo_usuario.nombre
        }
    }), 201
