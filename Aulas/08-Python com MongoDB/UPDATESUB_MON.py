"""
  Nesse script vamos
  fazer atualizações
  em subdocumentos removendo
  o servidor dns e colocando
  o servidor powerdns

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
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo apt-get install python-pymongo")

client = MongoClient("127.0.0.1")
db = client["devops"]

db.fila.update({"_id": 1, "servidores.nome": "dns"}, {"$pull": {"servidores": {"nome": "dns"}}})
db.fila.update({"_id": 1}, {"$addToSet": {"servidores": {"nome": "powerdns", "endereco": "192.168.30.1"}}})

for r in db.fila.find():
    print("O analista:{}tem acesso aos servidores".format(r['analista']))
    for s in r['servidores']:
        print("Nome: {} - Endereço: {}".format(s['nome'], s['endereco']))
