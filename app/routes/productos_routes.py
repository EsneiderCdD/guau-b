# app/routes/productos_routes.py

from flask import Blueprint
from app.controllers.producto_controller import obtener_productos

productos_bp = Blueprint("productos", __name__, url_prefix="/productos")

# Ruta pública para obtener productos
productos_bp.route("/", methods=["GET"])(obtener_productos)
