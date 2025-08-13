import random
from datetime import datetime
from app import create_app
from app.extensions import db
from app.models.perro import Perro

# Inicializar la app de Flask y el contexto de la base de datos
app = create_app()
app.app_context().push()

# Datos para generar valores aleatorios
nombres = ["Rocky", "Luna", "Max", "Toby", "Nala", "Coco", "Simba", "Maya", "Bobby", "Kira"]
razas = ["Labrador", "Pastor Alemán", "Golden Retriever", "Beagle", "Bulldog", "Boxer", "Husky", "Poodle"]
estados = ["disponible", "adoptado"]

def seed_perros(cantidad=10):
    for _ in range(cantidad):
        perro = Perro(
            nombre=random.choice(nombres),
            raza=random.choice(razas),
            edad=random.randint(1, 12),
            descripcion=f"Un perro muy {random.choice(['juguetón', 'tranquilo', 'cariñoso', 'protector'])}.",
            estado=random.choice(estados),
            imagen_url="https://via.placeholder.com/300",
            imagen_card_uno="https://via.placeholder.com/150",
            imagen_card_dos="https://via.placeholder.com/150",
            created_at=datetime.utcnow(),
            tiempo_requerido=random.randint(1, 3),
            requiere_experiencia=random.randint(1, 3),
            apego_esperado=random.randint(1, 3)
        )
        db.session.add(perro)

    db.session.commit()
    print(f"✅ {cantidad} perros insertados correctamente.")

if __name__ == "__main__":
    seed_perros(15)  # Cambia 15 por la cantidad que quieras
