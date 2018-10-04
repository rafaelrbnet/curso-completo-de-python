"""
  Nesse script vamos
  fazer algumas 
  atualizações 

  Modificado em 03 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 03 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3\
"""

import sys

try:
    from pymongo import MongoClient
except:
    sys.exit("[!] Por favor, instale a biblioteca pymongo com o comando: sudo apt-get install python-pymongo")


client = MongoClient("127.0.0.1")
db=client["devops"]

db.fila.update({"_id": 2}, {"$set": {"servico": "Linux"}})
db.fila.update({"_id": 4}, {"$set": {"servidor": "192.168.1.100"}})


for r in db.fila.find():
    print(r)
































