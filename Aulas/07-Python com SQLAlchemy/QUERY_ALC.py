#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# QUERY_ALC.py

"""
  Nesse script é feito a 
  busca de dados de um registro.
  Na lijnha first() retorna apenas
  o objeto Usuario.  


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
		usuario = session.query(Usuario).filter(Usuario.id==1).first()
		print usuario.id,usuario.nome
		usuarios = session.query(Usuario).all()
		print "Listando todos"
		for u in usuarios:
			print u.id,u.nome
	except Exception as e:
		print "Falhou %s"%e











