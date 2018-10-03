"""
  Nesse script é feito o session
  e criado o primeiro registro  
  em nosso banco de dados.

  Modificado em 29 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db")  # 1
# engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
# engine = create_engine(
#    'postgresql+psycopg2://postgres:123456@localhost/projeto',
#    connect_args={'options': '-csearch_path=projeto'}
#)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()


class Usuario(Base):
    __tablename__ = 'usuarios'  # Nome da tabela é usuarios
    id = Column(Integer, primary_key=True)
    nome = Column(String)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        usuario = Usuario(nome="Vitor Mazuco")
        session.add(usuario)
        session.commit()
        print("Registro criado com sucesso!")
    except Exception as e:
        print("Falhou ao criar: %s" % e)
        print("Fazendo o rollback")
        session.rollback()
