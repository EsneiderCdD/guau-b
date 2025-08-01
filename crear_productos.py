# scripts/insertar_productos.py

from app import create_app
from app.extensions import db
from app.models.producto import Producto

app = create_app()

# Contexto de aplicación necesario para trabajar con db
with app.app_context():
    productos = [
        Producto(nombre="Camiseta Guau", descripcion="Camiseta oficial con logo Guau", precio=19.99, stock=10, imagen_url="https://via.placeholder.com/150"),
        Producto(nombre="Taza Guau", descripcion="Taza de cerámica con diseño de patitas", precio=12.50, stock=25, imagen_url="https://via.placeholder.com/150"),
        Producto(nombre="Collar Personalizado", descripcion="Collar con nombre grabado", precio=15.00, stock=5, imagen_url="https://via.placeholder.com/150")
    ]

    db.session.bulk_save_objects(productos)
    db.session.commit()
    print("✅ Productos insertados con éxito.")
