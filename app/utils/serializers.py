# app/utils/serializers.py

def serialize_perro(perro):
    return {
        "id": perro.id,
        "nombre": perro.nombre,
        "raza": perro.raza,
        "edad": perro.edad,
        "estado": perro.estado,
        "imagen_url": perro.imagen_url,
        "imagen_card_uno": perro.imagen_card_uno,
        "imagen_card_dos": perro.imagen_card_dos,
        "energia": perro.energia,
        "apego_vinculo": perro.apego_vinculo,
        "regulacion_emocional": perro.regulacion_emocional,
        "exploracion_libertad": perro.exploracion_libertad,
        "datos_fisicos": perro.datos_fisicos
    }
