# app/routes/productos_routes.py

from flask import Blueprint
from app.controllers.producto_controller import obtener_productos, crear_producto
from app.utils.decorators import admin_required  # 👈 asegurate que el path esté bien

productos_bp = Blueprint("productos", __name__, url_prefix="/productos")

productos_bp.route("/", methods=["GET"])(obtener_productos)

# 👇 Nueva ruta protegida
productos_bp.route("/", methods=["POST"])(admin_required(crear_producto))
