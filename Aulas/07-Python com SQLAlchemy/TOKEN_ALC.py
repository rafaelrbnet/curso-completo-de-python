"""
  Nesse script vamos o 
  conceito de Tokens 
  com o SQLAlchemy

  Modificado em 31 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 02 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import hashlib

engine = create_engine("sqlite:///banco.db")  # 1
# engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
#engine = create_engine(
#    'postgresql+psycopg2://postgres:123456@localhost/projeto',
#    connect_args={'options': '-csearch_path=projeto'}
#)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    analista_id = Column(Integer, ForeignKey('analistas.id'))
    servidor_id = Column(Integer, ForeignKey('servidores.id'))
    token = Column(String(100))
    servidor = relationship("Servidores")
    analista = relationship("Analistas")


class Analistas(Base):
    __tablename__ = 'analistas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    tokens = relationship("Tokens")


class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    endereco = Column(String(100))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        # Prepara o Analista
        analista = Analistas(nome="Vitor Mazuc2")

        # Insere e Resgata o Id do analista a ser inserido
        session.add(analista)
        session.flush()
        print("Analista inserido {}".format(analista.id))

        # Prepara o Servidor
        servidor1 = Servidores(endereco="192.168.1.152")

        # Insere e Resgata o Id do servidor a ser inserido
        session.add(servidor1)
        session.flush()
        print("Servidor inserido {}".format(servidor1.id))

        # Prepara o Hash com o identificador do analista
        ids = str("{}-{}".format(analista.id, servidor1.id))
        print("ids {}".format(ids))
        hash_object = hashlib.sha256(ids.encode('utf-8')).hexdigest()

        # Prepara o Token
        token = Tokens(token=hash_object)

        # Relaciona o Token com O servidor
        token.servidor = servidor1
        token.analista = analista

        # Insere os registros
        session.add(token)

        session.commit()
    except Exception as e:
        print("Falhou %s" % e)
        print("Fazendo o rollback")
        session.rollback()
