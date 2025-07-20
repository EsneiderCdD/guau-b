---

## 🧩 Escalabilidad futura

Este proyecto está preparado para crecer modularmente. A medida que se implementen más funcionalidades (registro, adopciones, tienda, seguridad), se prevé organizar el backend en capas como:

- `services/`: lógica de negocio.
- `repositories/`: abstracción para acceso a la base de datos.
- `middleware/`: autenticación, logs, etc.
- `exceptions/`: errores personalizados y respuestas limpias.

Por ahora no se implementan, pero su incorporación está planificada.
