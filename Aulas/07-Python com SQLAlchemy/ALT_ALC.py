#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ALT_ALC.py

"""
  Nesse script é criado 
  um banco de dados
  juntamente com algumas 
  colunas a serem preenchidas. 
  Esse arquivo é uma alternativa 
  ao META_ALC.py.


  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

try:
	from sqlalchemy import create_engine
	from sqlalchemy import MetaData, Column, Table, ForeignKey
	from sqlalchemy import Integer, String
except:
    sys.exit("[!] Por favor, intale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")

engine = create_engine('sqlite:///alternativa.db',
                       echo=True)
 
metadata = MetaData(bind=engine)
 
usuarios_tabela = Table('usuarios', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(40)),
                    Column('idade', Integer),
                    Column('senha', String),
                    )
 
enderecos_tabela = Table('endereco', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('id_usuario', None, ForeignKey('usuarios.id')),
                        Column('email', String, nullable=False)                            
                        )
 
# Cria todas as tabelas no banco de dados
metadata.create_all()




