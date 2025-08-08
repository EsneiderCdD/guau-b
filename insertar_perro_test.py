# insertar_perro_test.py

from app import create_app
from app.extensions import db
from app.models.perro import Perro

app = create_app()

with app.app_context():
    nuevo_perro = Perro(
        nombre="TestDog",
        edad=5,
        raza="Mestizo",
        descripcion="Perro para prueba directa en BD",
        imagen_url="https://example.com/testdog.jpg",
        estado="disponible",
        tiempo_requerido=2,
        requiere_experiencia=1,
        apego_esperado=0
    )

    db.session.add(nuevo_perro)
    db.session.commit()

    print(f"✅ Perro insertado con ID: {nuevo_perro.id}")

    # Confirmar que las dimensiones se guardaron correctamente
    perro_guardado = Perro.query.get(nuevo_perro.id)
    print("📄 Dimensiones guardadas:")
    print("  Tiempo requerido:", perro_guardado.tiempo_requerido)
    print("  Requiere experiencia:", perro_guardado.requiere_experiencia)
    print("  Apego esperado:", perro_guardado.apego_esperado)
