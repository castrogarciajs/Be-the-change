# Be me Changes

- Aplicacion de nota escrita en django en donde podras **_guardar, eliminar, actulilzar, y leer_** tus notas.
  Esta aplicacion es inspirada en el block de nota de nuestros dispositivos, cuenta con: **_autenticación, autorización_** con el fin de hacer seguras nuestra gestion de tareas.

## uso

Puedes clonar este repositorio

1.

```git
git clone https://github.com/sebastian01w/Be-the-change.git
```

2.

Ejecuta el comando:

```py
python manage.py runserver 8080
```

3.  Vista en el puerto: 8080

![django](https://i.postimg.cc/ryPYQsLF/django.png)

## Endpoints

1. Autenticación

- `/`: Ruta principal
- `login/`: Ruta de iniciar sesion
- `register/`: Ruta de registrarse
- `logout/`: Cerrar session

2. Dashboard

- `create/task/`: Crear tareas
- `tasks/`: Tus tareas
- `tasks/completed/`: Tareas completada

3. id

- `task/<int:id>`: Tarea por id
- `task/<int:id>/complete`: Tareas completada por id
- `task/<int:id>/delete`: Eliminar tarea por id

## LICENSE

- Este proyecto esta bajo la `LICENSE` MIT sientete libre de hacer con lo que gustes y expandes tus ideas

## Autor

- Johan Sebastian castro Garcia
  `Github`: sebastian01w
  <br>
  `Email`: johancs.mm@gmail.com
