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

def serialize_match_usuario(perfil):
    if perfil is None:
        return None
    return {
        "id": perfil.id,
        "usuario_id": perfil.usuario_id,
        "energia": perfil.energia,
        "apego_vinculo": perfil.apego_vinculo,
        "regulacion_emocional": perfil.regulacion_emocional,
        "exploracion_libertad": perfil.exploracion_libertad,
        "datos_fisicos": perfil.datos_fisicos,
        "created_at": perfil.created_at.isoformat() if perfil.created_at else None,
        "updated_at": perfil.updated_at.isoformat() if perfil.updated_at else None
    }
