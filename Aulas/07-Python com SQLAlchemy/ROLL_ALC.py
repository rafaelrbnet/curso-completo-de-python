#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ROLL_ALC.py

"""
  Nesse script é feito o session
  e criado o primeiro registro  
  em nosso banco de dados.


  Modificado em 29 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

try:
	from sqlalchemy import create_engine
	from sqlalchemy import Column,Integer,String
	from sqlalchemy.ext.declarative import declarative_base	
	from sqlalchemy.orm import sessionmaker
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")


engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

class Usuario(Base):
	__tablename__ = 'usuarios' # Nome da tabela é usuarios
	id = Column(Integer,primary_key=True)
	nome = Column(String)

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	try:
		usuario = Usuario(id=4,nome="Vitor Mazuco")
		session.add(usuario)
		session.commit()
		print "Registro criado com sucesso!"
	except Exception as e:
		print "Falhou ao criar: %s"%e
		print "Fazendo o rollback"
		session.rollback()











