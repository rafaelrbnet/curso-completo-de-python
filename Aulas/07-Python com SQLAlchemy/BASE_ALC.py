#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# BASE_ALC.py

"""
  Nesse script criamos um objeto Base
  que vamos usar durante todo o nosso
  banco de dados.


  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

try:
	from sqlalchemy import create_engine
	from sqlalchemy.ext.declarative import declarative_base
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")

try:
	engine = create_engine("sqlite:///banco.db")
	Base = declarative_base()
	print engine
	print Base
except Exception as e:
	print "Falhou a conexão %s"%e





















