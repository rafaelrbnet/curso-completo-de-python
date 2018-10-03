"""
  Nesse script é criado 
  um banco de dados
  juntamente com algumas 
  colunas a serem preenchidas. 
  Esse arquivo é uma alternativa 
  ao META_ALC.py.

  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String

# engine = create_engine("sqlite:///banco.db")
# engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
engine = create_engine(
    'postgresql+psycopg2://postgres:123456@localhost/projeto',
    connect_args={'options': '-csearch_path=projeto'}
)
metadata = MetaData(bind=engine)

usuarios_tabela = Table('usuarios', metadata,
                        Column('id', Integer, primary_key=True, autoincrement=True),
                        Column('nome', String(40)),
                        Column('idade', Integer),
                        Column('senha', String(100)),
                        )

enderecos_tabela = Table('endereco', metadata,
                         Column('id', Integer, primary_key=True, autoincrement=True),
                         Column('id_usuario', None, ForeignKey('usuarios.id')),
                         Column('email', String(100), nullable=False)
                         )

# Cria todas as tabelas no banco de dados
metadata.create_all()
