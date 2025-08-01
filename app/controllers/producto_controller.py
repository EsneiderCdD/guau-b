# app/controllers/producto_controller.py

from flask import jsonify, request
from app.models.producto import Producto
from app.extensions import db
from app.schemas.producto_schema import serialize_producto, parsear_producto_data

def obtener_productos():
    productos = Producto.query.all()
    productos_serializados = [serialize_producto(p) for p in productos]
    return jsonify(productos_serializados), 200

# 👇 NUEVO: Crear producto
def crear_producto():
    try:
        data = request.get_json()
        producto_data = parsear_producto_data(data)

        nuevo_producto = Producto(**producto_data)
        db.session.add(nuevo_producto)
        db.session.commit()

        return jsonify({
            "mensaje": "Producto creado con éxito",
            "producto": serialize_producto(nuevo_producto)
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error inesperado al crear producto"}), 500
