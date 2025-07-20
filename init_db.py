# init_db.py
from app import create_app
from app.extensions import db
from app.models.perro import Perro

from datetime import datetime

# Crear app y contexto
app = create_app()

with app.app_context():
    # Crear todas las tablas
    db.drop_all()  # ⚠️ Elimina todo antes (opcional, solo para reiniciar)
    db.create_all()
    print("✅ Tablas creadas")

    # Datos de prueba
    if not Perro.query.first():  # Evita duplicados si ya existen
        perros = [
            Perro(nombre='Luna', raza='Labrador', edad=3, descripcion='Amigable y juguetona.'),
            Perro(nombre='Max', raza='Pastor Alemán', edad=5, descripcion='Fiel y protector.'),
            Perro(nombre='Kira', raza='Beagle', edad=2, descripcion='Muy curiosa y energética.'),
        ]
        db.session.add_all(perros)
        db.session.commit()
        print("🐶 Perros de prueba insertados")
    else:
        print("ℹ️ Ya hay perros en la base, no se insertaron duplicados.")
