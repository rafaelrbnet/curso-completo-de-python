#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# TOKEN_ALC.py

"""
  Nesse script vamos o 
  conceito de Tokens 
  com o SQLAlchemy


  Modificado em 31 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

try:
	from sqlalchemy import create_engine
	from sqlalchemy import Column,Integer,String,ForeignKey,Table
	from sqlalchemy.ext.declarative import declarative_base	
	from sqlalchemy.orm import sessionmaker,relationship
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")


engine = create_engine("sqlite:///banco3.db")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Tokens(Base):
	__tablename__ = 'tokens'
	id = Column(Integer,primary_key=True)
	analista_id = Column(Integer,ForeignKey('analistas.id'))
	servidor_id = Column(Integer,ForeignKey('servidores.id'))
	token = Column(String)
	servidor = relationship("Servidores")
	analista = relationship("Analistas")
	
class Analistas(Base):
	__tablename__ = 'analistas' 
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	tokens = relationship("Tokens")

class Servidores(Base):
	__tablename__ = 'servidores'
	id = Column(Integer,primary_key=True)
	endereco = Column(String)

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	try:
		analista = Analistas(id=1,nome="Vitor Mazuco")
		servidor1 = Servidores(id=2,endereco="192.168.1.156")
		token = Tokens(id=3,token="xpto2017")
		token.servidor = servidor1
		analista.tokens.append(token)
		session.add(analista)
		session.add(token)
		session.add(servidor1)
		session.commit()
	except Exception as e:
		print "Falhou %s"%e
		print "Fazendo o rollback"
		session.rollback()











