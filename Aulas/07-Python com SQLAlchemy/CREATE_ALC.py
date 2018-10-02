#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# CREATE_ALC.py

"""
  Nesse script é criado um arquivo em 
  sqlite nomeado de banco.db.
  Os principais navegadores usam como 
  armazenamento de dados, suas configurações
  e o seu cache. 


  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

try:
	from sqlalchemy import create_engine
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")

try:
	engine = create_engine("sqlite:///banco.db")
	print engine
except Exception as e:
	print "Falhou a conexão %s"%e
















