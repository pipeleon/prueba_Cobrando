## Prueba para Desarrollador Pyhton - COBRANDO BPO

Teniendo en cuenta el siguiente modelo elabore un micro servicio para la tabla
“empleado” el cual sea capaz de insertar, actualizar, borrar y consultar (CRUD)
información utilizando el FrameWork de Django.

## Requerimientos

- [Python 3+](https://python.org/) instalado en el sistema
- [Docker] (https://www.docker.com/) instalado en el sistema
- Poder escribir comandos basicos en una terminal (macOS, Linux or Windows)

Para comenzar se tiene que clonar este repositorio

```bash
~$ git clone https://github.com/pipeleon/prueba_Cobrando.git
```

## Docker Compose
Para ver la aplicacion se requiere correr los siguientes comandos para que se abra el puerto 1234 en localhost para que la imagen de Docker (basada en el DockerFile).

```bash
~$ docker-compose run web python3 Prueba/manage.py migrate
~$ docker-compose up
```

## Funcionamiento
En el browser se desplegara la aplicacion, en esta puedes visualizar los empleados en la base de datos local con la oportunidad de realizar 3 acciones: 
    - Insertar un nuevo empleado con todos sus campos
    - Actualizar un empleado de acuerdo a su Id y el campo que se quiera actualizar
    - Borrar un empleado de acuerdo a la ID

## Autor
[<img src="https://avatars.githubusercontent.com/u/91047947" width="110" style="border-radius: 50%"><br><sub>Felipe Leon<br><sup>@pipeleon](https://github.com/pipeleon) |
