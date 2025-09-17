# app/utils/match.py

import math

def calcular_compatibilidad(perfil_usuario, perro):
    """
    Calcula la compatibilidad entre perfil_usuario (MatchUsuario model) y perro (Perro model)
    usando la distancia euclidiana entre los vectores de 4 dimensiones:
    (energia, apego_vinculo, regulacion_emocional, exploracion_libertad).

    Devuelve un número float entre 0.00 y 100.00 redondeado a 2 decimales.
    Si los datos faltan o hay error, devuelve None.
    """
    try:
        u = [
            float(perfil_usuario.energia or 0.0),
            float(perfil_usuario.apego_vinculo or 0.0),
            float(perfil_usuario.regulacion_emocional or 0.0),
            float(perfil_usuario.exploracion_libertad or 0.0)
        ]
        p = [
            float(perro.energia or 0.0),
            float(perro.apego_vinculo or 0.0),
            float(perro.regulacion_emocional or 0.0),
            float(perro.exploracion_libertad or 0.0)
        ]

        # distancia euclidiana
        distancia = math.sqrt(sum((pi - ui) ** 2 for pi, ui in zip(p, u)))

        # Dmax para escala 0-4 en 4 dimensiones
        Dmax = math.sqrt((4 ** 2) * 4)  # = 8

        compat = 100 * (1 - (distancia / Dmax))
        # clamp 0..100
        compat_clamped = max(0.0, min(100.0, compat))
        return round(compat_clamped, 2)
    except Exception:
        return None
