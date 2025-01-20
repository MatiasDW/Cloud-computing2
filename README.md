# File Storage API

Una API construida con **FastAPI** para la autenticación de usuarios y la gestión de archivos, incluyendo funcionalidades de registro, login, logout, introspección de tokens y CRUD de archivos. Esta aplicación está preparada para ejecutarse en Docker.

---

## **Características**
1. **Autenticación de usuarios**:
   - Registro (`/auth/register`).
   - Login (`/auth/login`).
   - Logout (`/auth/logout`).
   - Introspección de token (`/auth/introspect`).

2. **Gestión de archivos**:
   - Crear, listar, obtener, actualizar y eliminar archivos (`/files` y subrutas).

3. **Documentación interactiva**:
   - Disponible en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## **Requisitos Previos**
1. **Docker** y **Docker Compose** instalados en tu máquina.
2. Opcional: Python 3.10+ si deseas ejecutarlo localmente sin Docker.

---

## **Instrucciones para Ejecutar**

### **Con Docker**
1. Construir la imagen:
   ```bash
   docker-compose build
