# Sistema para gestionar las entregas de proyectos

El proyecto consiste en el desarrollo de un sistema web que tiene con principal objetivo agilizar las entregas de las tareas, asignación de tareas y seguimiento de tareas además de centralizar toda la información de las tareas y proyectos dentro del sistema web y no depender de otros software, por lo cual la con la implementación de este sistema web se busca solucionar estos problemas y agilizar los procesos de desarrollo de los proyectos.

## Tecnologías utilizadas

- HTML
- CSS
- JavaScript
- Python
- Django

## Features

- Integración con `slack`
- Uso de `select2` para filtros
- Drag and drop para la carga de archivos
- Generar reportes en formatos CSV, Excel y PDF
- Sistema de comentarios con Markdown

## Instalación

Clonar el repositorio

```
git clone git@github.com:wicho97/batoro.git
```

Crear un entorno virtual dentro de la carpeta `batoro`

```
cd batoro
python3 -m venv .venv
```

Activar el entorno virtual `.venv` e instalar dependencias

```
source .venv/bin/activate
pip install -r requirements.txt
```

Dentro la carpeta `batoro` que contiene el archivo `settings.py` crear el archivo `.env`

```
touch .env
```

Dentro del archivo `.env` colocamos lo siguiente

```
SECRET_KEY = '....your secret key ....'
SLACK_API_TOKEN = '....your secret key ....'
```

Migrar los modelos y crear el `superuser`

```
python3 manage.py migrate
python3 manage.py createsuperuser
```

Por último ejecutamos el proyecto

```
python3 manage.py runserver
```

Al iniciar sesión con el `superuser` por primera vez y acceder a la ruta `http://127.0.0.1:8000/account/edit/` no mostrará un error, para solucionar esto debemos accedemos a la ruta `http://127.0.0.1:8000/admin/account/profile/add/` y crear el perfil del usuario.

Dentro del perfil del usuario se encuentra el campo `Slack user id` este campo sirve para enviar las notificaciones al usuario mediante `slack`, en este campo debemos colocar el ID de usuario de nuestra cuenta de `slack`

