# scripts/insertar_datos_prueba.py

from app import create_app
from app.extensions import db
from app.models.usuario import Usuario
from app.models.perro import Perro
from app.models.match_usuario import MatchUsuario

app = create_app()

with app.app_context():
    # 1. Crear perros de prueba
    perros_data = [
        {
            "nombre": "Rocky",
            "edad": 4,
            "raza": "Labrador",
            "descripcion": "Energético y leal",
            "imagen_url": "https://via.placeholder.com/150",
            "estado": "disponible",
            "tiempo_requerido": 3,
            "requiere_experiencia": 1,
            "apego_esperado": 2
        },
        {
            "nombre": "Luna",
            "edad": 2,
            "raza": "Beagle",
            "descripcion": "Curiosa y juguetona",
            "imagen_url": "https://via.placeholder.com/150",
            "estado": "disponible",
            "tiempo_requerido": 2,
            "requiere_experiencia": 0,
            "apego_esperado": 2
        },
        {
            "nombre": "Coco",
            "edad": 1,
            "raza": "Criollo",
            "descripcion": "Tranquilo y amoroso",
            "imagen_url": "https://via.placeholder.com/150",
            "estado": "disponible",
            "tiempo_requerido": None,  # Perro sin perfil completo
            "requiere_experiencia": None,
            "apego_esperado": None
        }
    ]

    for data in perros_data:
        existente = Perro.query.filter_by(nombre=data["nombre"]).first()
        if not existente:
            nuevo_perro = Perro(**data)
            db.session.add(nuevo_perro)
            print(f"✅ Perro {data['nombre']} insertado")
        else:
            print(f"⚠️ Perro {data['nombre']} ya existe")

    # 2. Asociar MatchUsuario a usuarios existentes
    match_data = [
        {
            "usuario_nombre": "CarlosGM",
            "tiempo_disponible": 3,
            "experiencia": 1,
            "apego_emocional": 2
        },
        {
            "usuario_nombre": "LauraMC",
            "tiempo_disponible": 2,
            "experiencia": 0,
            "apego_emocional": 1
        },
        {
            "usuario_nombre": "JuliánTR",
            "tiempo_disponible": 1,
            "experiencia": 1,
            "apego_emocional": 0
        }
    ]

    for match in match_data:
        usuario = Usuario.query.filter_by(nombre=match["usuario_nombre"]).first()
        if usuario:
            ya_registrado = MatchUsuario.query.filter_by(usuario_id=usuario.id).first()
            if not ya_registrado:
                nuevo_match = MatchUsuario(
                    usuario_id=usuario.id,
                    tiempo_disponible=match["tiempo_disponible"],
                    experiencia=match["experiencia"],
                    apego_emocional=match["apego_emocional"]
                )
                db.session.add(nuevo_match)
                print(f"✅ MatchUsuario para {usuario.nombre} creado")
            else:
                print(f"⚠️ {usuario.nombre} ya tiene un perfil de match")
        else:
            print(f"❌ Usuario {match['usuario_nombre']} no encontrado")

    db.session.commit()
    print("🎉 Todos los datos fueron insertados correctamente.")
