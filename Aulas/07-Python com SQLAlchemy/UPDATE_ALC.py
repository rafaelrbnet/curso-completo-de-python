#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# UPDATE_ALC.py

"""
  Nesse script é apagado
  o registro em nosso 
  banco de dados.


  Modificado em 30 de março de 2017
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
	__tablename__ = 'usuarios' 
	id = Column(Integer,primary_key=True)
	nome = Column(String)

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	try:
		usuario = session.query(Usuario).filter(Usuario.id==1).first()
		usuario.nome = "Nathalia"
		session.commit()
		print "Registro alterado com sucesso!"
	except Exception as e:
		print "Falhou %s"%e
		print "Fazendo o rollback"
		session.rollback()











