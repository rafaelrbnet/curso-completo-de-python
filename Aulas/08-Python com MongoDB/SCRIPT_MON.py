"""
  Nesse script vamos
  rodar alguns scripts
  em python com o banco de 
  dados do MongoDB

  Modificado em 03 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 03 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

import sys

try:
    from pymongo import MongoClient
except:
    sys.exit("[!] Por favor, instale a biblioteca pymongo")

client = MongoClient("127.0.0.1")
db = client["devops"]

db.fila.remove()  # Apagar os dados escritos previamente
db.fila.insert({"_id": 1, "servico": "Intranet", "status": 0})
db.fila.insert({"_id": 2, "servico": "WebSite", "status": 0})
db.fila.insert({"_id": 3, "servico": "Backup", "status": 0})
db.fila.insert({"_id": 4, "servidor": "192.168.25.1", "nome": "Asterisk"})
db.fila.insert({"_id": 5, "servidor": "192.168.25.2", "nome": "FreeNas"})
db.fila.insert({"_id": 6, "servidor": "192.168.25.3", "nome": "pfSense"})

for r in db.fila.find():
    print(r)
