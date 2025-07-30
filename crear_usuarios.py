# crear_usuarios.py

from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app()

usuarios_data = [
    {"nombre": "CarlosGM", "password": "CarlosGM"},
    {"nombre": "LauraMC", "password": "LauraMC"},
    {"nombre": "JuliánTR", "password": "JulianTR"},
]

with app.app_context():
    for user_data in usuarios_data:
        existente = Usuario.query.filter_by(nombre=user_data["nombre"]).first()
        if not existente:
            user = Usuario(nombre=user_data["nombre"], rol="user")
            user.set_password(user_data["password"])
            db.session.add(user)
            print(f"✅ Usuario {user.nombre} creado")
        else:
            print(f"⚠️ Usuario {user_data['nombre']} ya existe")

    db.session.commit()
    print("✅ Todos los usuarios fueron procesados correctamente.")
