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
        return None

    # Pesos totales por dimensión
    W_TIEMPO = 40
    W_EXPERIENCIA = 30
    W_APEGO = 30

    # Máximas diferencias posibles
    M_TIEMPO = 2
    M_EXPERIENCIA = 1
    M_APEGO = 2

    # Penalización por unidad (p = w / m)
    P_TIEMPO = W_TIEMPO / M_TIEMPO  # 20
    P_EXPERIENCIA = W_EXPERIENCIA / M_EXPERIENCIA  # 30
    P_APEGO = W_APEGO / M_APEGO  # 15

    # Diferencias absolutas
    diff_tiempo = abs(perro.tiempo_requerido - usuario_match.tiempo_disponible)
    diff_experiencia = abs(perro.requiere_experiencia - usuario_match.experiencia)
    diff_apego = abs(perro.apego_esperado - usuario_match.apego_emocional)

    # Penalización total usando p en lugar de w
    penalizacion = (
        diff_tiempo * P_TIEMPO +
        diff_experiencia * P_EXPERIENCIA +
        diff_apego * P_APEGO
    )

    # Compatibilidad final
    compatibilidad = max(0, 100 - penalizacion)
    return compatibilidad
