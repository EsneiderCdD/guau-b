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

# 👇 Nueva función: validación y extracción de datos desde un dict
def parsear_producto_data(data):
    nombre = data.get("nombre")
    precio = data.get("precio")
    stock = data.get("stock")

    if not nombre or precio is None or stock is None:
        raise ValueError("Faltan campos obligatorios: nombre, precio, stock")

    return {
        "nombre": nombre,
        "descripcion": data.get("descripcion", ""),
        "precio": precio,
        "stock": stock,
        "imagen_url": data.get("imagen_url", "")
    }
