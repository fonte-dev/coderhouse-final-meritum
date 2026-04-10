# MERITUM - Plataforma para Acompañantes Terapéuticos

Proyecto Final para el curso de Python/Django en Coderhouse.
MERITUM es una aplicación web estilo blog y red profesional diseñada para que los Acompañantes Terapéuticos en Argentina puedan documentar casos, compartir artículos y comunicarse entre colegas.

## 🚀 Funcionalidades
* **Blog de Casos:** Sistema CRUD completo para artículos con texto enriquecido (CKEditor) e imágenes.
* **Cuentas de Usuario:** Sistema de registro, login, logout y cambio de contraseñas.
* **Perfiles Profesionales:** Cada usuario tiene un perfil editable con su propio avatar, biografía y datos personales.
* **Mensajería Interna:** Bandeja de entrada privada para la comunicación entre usuarios registrados.
* **Buscador:** Búsqueda en tiempo real de artículos por título o subtítulo.
* **Acerca de Mí:** Página estática de presentación del desarrollador, cumpliendo con la consigna.


## 🛠️ Tecnologías Utilizadas
* Python
* Django
* SQLite3 (Base de datos)
* Bootstrap 5 (Frontend)
* CKEditor

## ⚙️ Instrucciones para ejecutar el proyecto (Local)

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/fonte-dev/coderhouse-final-meritum
    ```

2. Crear y activar el entorno virtual:
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplicar las migraciones a la base de datos:
    ```bash
    python manage.py migrate
    ```

5. Crear un superusuario (opcional):
    ```bash
    python manage.py createsuperuser
    ```

6. Correr el servidor:
    ```bash
    python manage.py runserver
    ```