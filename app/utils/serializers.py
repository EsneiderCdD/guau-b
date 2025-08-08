def serialize_perro(perro):
    return {
        "id": perro.id,
        "nombre": perro.nombre,
        "raza": perro.raza,
        "edad": perro.edad,
        "estado": perro.estado,
        "imagen_url": perro.imagen_url,
        "tiempo_requerido": perro.tiempo_requerido,
        "requiere_experiencia": perro.requiere_experiencia,
        "apego_esperado": perro.apego_esperado
    }
