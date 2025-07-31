from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app()

with app.app_context():
    admin = Usuario(
        nombre="EsneiderCadavid",
        rol="admin"  # 👈 Aquí lo defines explícitamente
    )
    admin.set_password("EsneiderCadavid")
    db.session.add(admin)
    db.session.commit()
    print("✅ Usuario administrador creado con éxito.")
