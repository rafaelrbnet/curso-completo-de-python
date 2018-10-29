import datetime

from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db": "dexter-api"}
db = MongoEngine(app)

db = MongoEngine(app)


class Ususarios(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(defaults=datetime.datetime.now())


class Grupos(db.Document):
    nome = db.StringField(unique=True)
    integrantes = db.ListField()


if __name__ == '__main__':
    u = Ususarios()
    u.nome = "Rafael"
    u.email = "rafael.rbnet@gmail.com"
    u.save()
    print("Usuário cadastrado com sucesso")
    g = Grupos()
    g.nome = "Comercial"
    g.integrantes.append(u)
    g.save()
    print("Grupo cadastrado com sucesso")