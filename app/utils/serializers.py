def serialize_perro(perro):
    return {
        "id": perro.id,
        "nombre": perro.nombre,
        "raza": perro.raza,
        "edad": perro.edad,
        "estado": perro.estado,
        "imagen_url": perro.imagen_url,  # Principal
        "imagen_card_uno": perro.imagen_card_uno,  # Nueva
        "imagen_card_dos": perro.imagen_card_dos,  # Nueva
        "tiempo_requerido": perro.tiempo_requerido,
        "requiere_experiencia": perro.requiere_experiencia,
        "apego_esperado": perro.apego_esperado
    }
