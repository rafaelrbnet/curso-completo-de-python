#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#INSERTSUB_MON.py

"""
  Nesse script vamos
  usar a lógica do
  subdocumento 

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

db.fila.remove()

servidor1 = {"endereco":"192.168.0.1","nome":"dns"}
servidor2 = {"endereco":"192.168.0.2","nome":"postgres"}

servidores = []

servidores.append(servidor1)
servidores.append(servidor2)

db.fila.insert({"_id":1,"analista":"Alan Turing","servidores":servidores})

for r in db.fila.find():
	print "O analista:",r['analista'],"tem acesso aos servidores"
	for s in r['servidores']:
		print s['nome']," - ",s['endereco']











