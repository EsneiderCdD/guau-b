# app/routes/productos_routes.py

from flask import Blueprint
from app.controllers.producto_controller import (
    obtener_productos,
    crear_producto,
    eliminar_producto
)
from app.utils.decorators import admin_required

productos_bp = Blueprint("productos", __name__, url_prefix="/productos")

productos_bp.route("/", methods=["GET"])(obtener_productos)

productos_bp.route("/", methods=["POST"])(admin_required(crear_producto))

# 🗑️ Eliminar producto (solo admin)
productos_bp.route("/<int:producto_id>", methods=["DELETE"])(admin_required(eliminar_producto))
