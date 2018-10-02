#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# MODEL_ALC.py

"""
  Nesse script criamos um 
  model que faz o controle
  do banco de dados em Python.


  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

try:
	from sqlalchemy import create_engine
	from sqlalchemy import Column,Integer,String
	from sqlalchemy.ext.declarative import declarative_base
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")


engine = create_engine("sqlite:///banco.db")
Base = declarative_base()

class Usuario(Base):
	__tablename__ = 'usuarios'
	id = Column(Integer,primary_key=True)
	nome = Column(String)





















