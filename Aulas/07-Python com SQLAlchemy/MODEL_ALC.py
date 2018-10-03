"""
  Nesse script criamos um 
  model que faz o controle
  do banco de dados em Python.

  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine("sqlite:///banco.db")
# engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/projeto')
Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
