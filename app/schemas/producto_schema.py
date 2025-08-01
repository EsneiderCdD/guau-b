# app/schemas/producto_schema.py

def serialize_producto(producto):
    return {
        "id": producto.id,
        "nombre": producto.nombre,
        "descripcion": producto.descripcion,
        "precio": float(producto.precio),
        "stock": producto.stock,
        "imagen_url": producto.imagen_url,
        "created_at": producto.created_at.isoformat()
    }
