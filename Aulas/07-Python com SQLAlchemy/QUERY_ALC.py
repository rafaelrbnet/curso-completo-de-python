"""
  Nesse script é feito a 
  busca de dados de um registro.
  Na lijnha first() retorna apenas
  o objeto Usuario.

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

# engine = create_engine("sqlite:///banco.db")  # 1
# engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
engine = create_engine(
    'postgresql+psycopg2://postgres:123456@localhost/projeto',
    connect_args={'options': '-csearch_path=projeto'}
)
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
        usuario = session.query(Usuario).filter(Usuario.id == 1).first()
        print(usuario.id, usuario.nome)
        usuarios = session.query(Usuario).all()
        print("Listando todos")
        for u in usuarios:
            print(u.id, u.nome)
    except Exception as e:
        print("Falhou %s" % e)
