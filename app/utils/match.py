# app/utils/match.py

def calcular_compatibilidad(usuario_match, perro):
    """
    Calcula el nivel de compatibilidad entre un usuario y un perro
    usando la fórmula psicométrica definida.
    Retorna un número entre 0 y 100, o None si no hay perfil completo.
    """

    # Validar que ambos perfiles estén completos
    if (
        usuario_match.tiempo_disponible is None or
        usuario_match.experiencia is None or
        usuario_match.apego_emocional is None or
        perro.tiempo_requerido is None or
        perro.requiere_experiencia is None or
        perro.apego_esperado is None
    ):
        return None  # No se puede calcular sin todos los datos

    # Ponderaciones
    PESO_TIEMPO = 40
    PESO_EXPERIENCIA = 30
    PESO_APEGO = 30

    # Diferencias absolutas
    diff_tiempo = abs(perro.tiempo_requerido - usuario_match.tiempo_disponible)
    diff_experiencia = abs(perro.requiere_experiencia - usuario_match.experiencia)
    diff_apego = abs(perro.apego_esperado - usuario_match.apego_emocional)

    penalizacion = (
        diff_tiempo * PESO_TIEMPO +
        diff_experiencia * PESO_EXPERIENCIA +
        diff_apego * PESO_APEGO
    )

    compatibilidad = max(0, 100 - penalizacion)  # Evita que baje de 0
    return compatibilidad
