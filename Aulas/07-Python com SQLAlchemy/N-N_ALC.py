"""
  Nesse script vamos o 
  conceito de N -> N


  Modificado em 30 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 03 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine, Table
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///banco.db")  # 1
# engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
# engine = create_engine(
#    'postgresql+psycopg2://postgres:123456@localhost/projeto',
#    connect_args={'options': '-csearch_path=projeto'}
# )
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

association_table = Table('analistas_servidores', Base.metadata,
                          Column('analistas_id', Integer, ForeignKey('analistas.id')),
                          Column('servidores_id', Integer, ForeignKey('servidores.id')))


class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer, primary_key=True)
    endereco = Column(String)


class Analistas(Base):
    __tablename__ = 'analistas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    servidores = relationship("Servidores", secondary=association_table)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        # Insere os analistas
        analista1 = Analistas(id=1, nome="Vitor Mazuco")
        analista2 = Analistas(id=2, nome="Alan Lopes")
        session.add(analista1)
        session.add(analista2)

        # Insere os servidores
        servidor1 = Servidores(id=3, endereco="192.168.1.156")
        servidor2 = Servidores(id=4, endereco="192.168.1.157")

        # Relaciona N-N Analista - Servidores
        analista1.servidores.append(servidor1)
        analista2.servidores.append(servidor2)
        analista2.servidores.append(servidor1)

        # Salva os servidores
        session.add(servidor1)
        session.add(servidor2)

        # Salva a sessão toda
        session.commit()
    except Exception as e:
        print("Falhou %s" % e)
        print("Fazendo o rollback")
        session.rollback()
