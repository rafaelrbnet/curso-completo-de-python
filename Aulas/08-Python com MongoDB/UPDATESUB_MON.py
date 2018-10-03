#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#UPDATESUB_MON.py

"""
  Nesse script vamos
  fazer atualizações
  em subdocumentos removendo
  o servidor dns e colocando
  o servidor powerdns

  Modificado em 03 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

try:
	from pymongo import MongoClient
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo apt-get install python-pymongo")


client = MongoClient("127.0.0.1")
db=client["devops"]

db.fila.update({"_id":1,"servidores.nome":"dns"},{"$pull":{"servidores":{"nome":"dns"}}})
db.fila.update({"_id":1},{"$addToSet":{"servidores":{"nome":"powerdns","endereco":"192.168.30.1"}}})

for r in db.fila.find():
	print "O analista:",r['analista'],"tem acesso aos servidores"
	for s in r['servidores']:
		print s['nome']," - ",s['endereco']





