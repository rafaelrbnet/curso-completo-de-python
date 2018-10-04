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