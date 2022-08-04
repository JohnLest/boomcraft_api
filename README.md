# Three-tiers architecture template in Python

This is a template for a three-tiers architecture with [FastAPI](https://fastapi.tiangolo.com/) and [sqlAlchemy](https://www.sqlalchemy.org/)

## App 
This is the Presentation layer.
It contains the `Main` and the `Routers` class
## BLL
This is the Business Logic Layer

## DAL
This is the Data Access Layer

## Model
This layer contains the data object with [`pydantic`](https://pydantic-docs.helpmanual.io/)

## Tools
This is a package that contains different gerneric tools. This is the same as [tools_python](https://github.com/JohnLest/tools_python)

## To install with docker and docker-compose

### MariaDB
Mariadb is installed with the docker-compose.yml 
When you are in the folder with the docker-compose.yml file, insert this command in you shell : 
`docker-compose -d `

### Boomcraft API 
The boomcraft api is installed with the Dockerfile 
 First build the image with this command : 
 `docker build -t boomcraft_api_image .`
 Second, start the container with this command : 
 `docker run -d --name boomcraft_api -p 40000:40000 boomcraft_api_image`

 for more information go to the web site : https://fastapi.tiangolo.com/deployment/docker/
