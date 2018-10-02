Comandos Docker para instalação das maquinas de cada banco

-- Mysql
docker run -d -p 3306:3306 --name mysql-db -e MYSQL_ROOT_PASSWORD=root mysql:5.6
docker exec -it mysql1 mysql -u root -p


-- Postgresql
docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres
docker exec -it my-postgres bash


root@cb9222b1f718:/# psql -U postgres
psql (10.3 (Debian 10.3-1.pgdg90+1))
Type "help" for help.
postgres=# CREATE DATABASE mytestdb;
CREATE DATABASE
postgres=#\q