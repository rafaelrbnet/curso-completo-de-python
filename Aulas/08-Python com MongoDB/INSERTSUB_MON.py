"""
  Nesse script vamos
  usar a lógica do
  subdocumento 

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
    sys.exit("[!] Por favor, intale a biblioteca pymongo")

client = MongoClient("localhost")
db = client["devops"]

db.fila.remove()

servidor1 = {"endereco": "192.168.0.1", "nome": "dns", "analista": "1"}
servidor2 = {"endereco": "192.168.0.2", "nome": "postgres", "analista": "1"}

servidores = [servidor1, servidor2]

db.fila.insert({"_id": 1, "analista": "Alan Turing", "servidores": servidores})

for r in db.fila.find():
    print("O analista:", r['analista'], "tem acesso aos servidores")
    for s in r['servidores']:
        print(s['nome'], " - ", s['endereco'])
