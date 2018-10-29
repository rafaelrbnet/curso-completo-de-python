-- Instalação do Docker para Mongo DB
docker run -d -p 27017:27017 -v D:\Docker\data mongo
docker ps
docker run -it --link 6c9e3eb72f9c:mongo --rm mongo mongo --host mongo

use admin
db.createUser(
  {
    user: "root",
    pwd: "123456",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)

-- Outro método
docker pull tutum/mongodb

docker run -d -p 27017:27017 -p 28017:28017 -e AUTH=no tutum/mongodb

Criação de servidor especificando uma senha
docker run -d -p 27017:27017 -p 28017:28017 -e MONGODB_PASS="mypass" tutum/mongodb

O próximo passo será subir o seu servidor mongo. Para isso, execute os passos abaixo:

docker ps -a
Esse comando irá listar os seus containers que não estão em execução, copie o containerID do mongo e execute o comando abaixo no seu terminal:

docker start 77b903780b83

