# crear_admin.py

from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app()

with app.app_context():
    admin = Usuario(nombre="EsneiderCdD")
    admin.set_password("EsneiderCdD")
    db.session.add(admin)
    db.session.commit()
    print("✅ Usuario administrador creado con éxito.")
