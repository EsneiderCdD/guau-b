# scripts/probar_matching.py

from app import create_app
from app.extensions import db
from app.models.usuario import Usuario
from app.models.perro import Perro
from app.models.match_usuario import MatchUsuario
from app.utils.match import calcular_compatibilidad

app = create_app()

with app.app_context():
    nombre_usuario = input("🧪 Ingresa el nombre del usuario a evaluar (ej. CarlosGM): ").strip()

    usuario = Usuario.query.filter_by(nombre=nombre_usuario).first()

    if not usuario:
        print(f"❌ Usuario '{nombre_usuario}' no encontrado.")
        exit()

    perfil = MatchUsuario.query.filter_by(usuario_id=usuario.id).first()

    if not perfil:
        print(f"⚠️ El usuario '{usuario.nombre}' no tiene perfil psicométrico aún.")
        exit()

    perros_disponibles = Perro.query.filter_by(estado='disponible').all()

    resultados = []

    for perro in perros_disponibles:
        score = calcular_compatibilidad(perfil, perro)
        if score is not None:
            resultados.append((perro.nombre, score))

    if resultados:
        print(f"\n🐶 Resultados de matching para '{usuario.nombre}':\n")
        for nombre, compat in sorted(resultados, key=lambda x: x[1], reverse=True):
            print(f" - {nombre}: {compat}% compatibilidad")
    else:
        print("⚠️ Ningún perro tiene perfil completo para comparar.")
