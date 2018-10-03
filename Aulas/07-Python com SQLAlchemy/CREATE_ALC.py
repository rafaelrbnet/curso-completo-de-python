"""
  Nesse script é criado um arquivo em 
  sqlite nomeado de banco.db.
  Os principais navegadores usam como 
  armazenamento de dados, suas configurações
  e o seu cache. 

  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine

try:
    engine = create_engine("sqlite:///banco.db")
    # engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
    # engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/projeto')
    engine.connect()
    print(engine)
except Exception as e:
    print("Falhou a conexão %s" % e)
