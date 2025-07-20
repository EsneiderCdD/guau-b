# Backend - Dependencias del Proyecto

Este documento describe las dependencias del backend para el proyecto **Guau**, una plataforma para adopción de perritos, compras de productos relacionados, y funcionalidades futuras como emparejamiento con perros según la personalidad del usuario.

---

## 🚀 Dependencias ya instaladas (esenciales)

| Paquete              | Descripción breve                                                                                                                                     |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Flask**            | Framework web liviano para construir el backend. Maneja rutas, peticiones, respuestas, etc.                                                             |
| **Flask-SQLAlchemy**| ORM para manejar base de datos relacional (PostgreSQL en este caso) con un enfoque orientado a objetos.                                                  |
| **python-dotenv**    | Permite cargar las variables del archivo `.env`, como claves secretas, URIs de la base de datos, modo debug, etc.                                       |
| **Flask-CORS**       | Permite que tu frontend (React) se conecte sin errores de origen cruzado (CORS).                                                                         |
| **psycopg2-binary**  | Conector entre Python y la base de datos PostgreSQL.                                                                                                     |

---

## 📊 Dependencias sugeridas a mediano y corto plazo

Estas librerías no se instalan inmediatamente, pero forman parte de la hoja de ruta.

| Paquete               | Cuándo usarlo                        | Descripción                                                                                                            |
|-----------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Flask-Migrate**     | Corto plazo (con modelos BD)        | Para manejar migraciones de base de datos a través de comandos, usando Alembic.                                        |
| **Flask-Bcrypt**      | Al implementar registro/login       | Encripta contraseñas de usuarios de forma segura.                                                                     |
| **Flask-Login**       | Registro/login                      | Manejo de sesiones, login persistente, usuarios logueados.                                                             |
| **Flask-JWT-Extended**| Alternativa a Flask-Login (API)     | Para proteger rutas usando tokens JWT, ideal si queremos consumir desde el frontend como SPA.                         |
| **Flask-Mail**        | Confirmaciones de correo            | Enviar correos para confirmar registros, recuperar contraseña, etc.                                                    |
| **Flask-Admin**       | Panel de administración             | Crear un panel visual para gestionar usuarios, productos, adopciones, etc.                                             |
| **Marshmallow**       | A mediano plazo (API limpia)        | Serializar y validar datos de entrada/salida.                                                                          |
| **Flask-Testing**     | A futuro (test unitarios)           | Facilita tests automáticos del backend.                                                                                |
| **gunicorn**          | En deploy (Railway)                 | Servidor de producción WSGI para correr el backend con mayor rendimiento.                                             |

---

## 🪡 Consideraciones sobre el enfoque

- Usaremos **PostgreSQL** local primero, luego desplegado.
- Frontend en **React**, separado, alojado en **Vercel**.
- Backend en **Railway**, por eso `gunicorn` será relevante.
- Los entornos virtuales y `requirements.txt` permitirán replicar el ambiente fácilmente.
- El proyecto evolucionará de manera modular (BluePrints), por eso **autenticación**, **migraciones** y **paneles** se irán integrando paso a paso.

---

## 🔹 Para instalar en el futuro:

Cuando decidas avanzar con alguna funcionalidad nueva (como login, admin, envío de correos), recuerda revisar esta lista y ejecutar:

```bash
pip install nombre-del-paquete
```

Y luego:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Siguiente paso

Ya con estas dependencias iniciales instaladas y este documento como guía, estamos listos para avanzar con:
- Modelado de datos (usuarios, perritos, productos)
- Seguridad
- Rutas protegidas y funcionalidad de adopción
- Conexión con el frontend

---

Cualquier nueva necesidad debe validarse contra esta guía para mantener el proyecto limpio y manejable. ¡Continuemos!

