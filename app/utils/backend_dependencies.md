
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

