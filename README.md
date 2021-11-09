# EasyBroker

Esta es una pequeña Api la cual realiza peticiones a la Api de EasyBroker la informacion octenida es almasenada en una basa de datos para su porterior manipulacion en esta api solo se octinene la informacion de ``` properties ``` 🚀

colsulte el la Api de EasyBroker para mas informacion
* [API de EasyBroker] (https://ayuda.easybroker.com/article/330-api-de-easybroker-beta)

_El sitio tiene una base de datos postgres_

_Estos le permitirán obtener una copia del proyecto de trabajo en su máquina local para su desarrollo y prueba ._

Consulte Implementación para aprender cómo implementar el proyecto..


### Prerequisites  📋


```
Docker-compose
ubuntu terminal
```

### Instalación 🔧
en el terminal ubicado en la carpeta donde tienes este proyecto, puedes mirar las carpetas y archivos que tiene el proyecto con el comando ls,
luego ejecuta lo siguiente .
```
git clone https://github.com/Dimaps716/EasyBroker.git
```

This will install the dependencies and requirements of the project.

```
docker-compose build
```
run migrations

```
docker-compose run web python manage.py makemigrations

docker-compose run web python manage.py migrate

```
for now the database is empty
```
docker-compose ps
```
create a user
```
docker-compose run web python manage
.py createsuperuser
```

here you can see the images and their status
```
docker-compose up
```
this will activate the servers

```
http://localhost:8000/admin
```
enter a couple of categories and a couple of products and you're done
## Built with 🛠️


* [Docker] (https://docs.docker.com/compose/reference/run/)
* [Django] (https://www.djangoproject.com/)
* [python] (https://www.python.org/)


## Authors ✒️


*  Dimanso perez - [Dimaps716] (https://github.com/Dimaps716)


## License 📄

This project is under the License (Your License) - see the  (LICENSE.md) file for details

## Expressions of Gratitude 🎁

* Tell others about this project 📢
* Invite a beer 🍺 or a coffee ☕ to someone on the team.
* Give thanks publicly 🤓.




---
⌨️ with ❤️ by [Dimaps716] (https://github.com/Dimaps716) 😊
