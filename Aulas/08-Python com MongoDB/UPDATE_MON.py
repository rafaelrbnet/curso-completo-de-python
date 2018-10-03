#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#UPDATE_MON.py

"""
  Nesse script vamos
  fazer algumas 
  atualizações 

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

db.fila.update({"_id":2},{"$set":{"servico":"Linux"}})
db.fila.update({"_id":4},{"$set":{"servidor":"192.168.1.100"}}
)

for r in db.fila.find():
	print r
































