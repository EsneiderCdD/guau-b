# app/controllers/producto_controller.py

from flask import jsonify
from app.models.producto import Producto
from app.extensions import db
from app.schemas.producto_schema import serialize_producto

def obtener_productos():
    productos = Producto.query.all()
    productos_serializados = [serialize_producto(p) for p in productos]
    return jsonify(productos_serializados), 200
