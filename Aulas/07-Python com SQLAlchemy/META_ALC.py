#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# META_ALC.py

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
	from sqlalchemy import Column,Integer,String
	from sqlalchemy.ext.declarative import declarative_base
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")


engine = create_engine("sqlite:///banco.db")
Base = declarative_base()

class Usuario(Base):
	__tablename__ = 'usuarios' # Nome da tabela é usuarios
	id = Column(Integer,primary_key=True)
	nome = Column(String)

if __name__ == '__main__':
	Base.metadata.create_all(engine)













