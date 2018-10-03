"""
  Nesse script vamos o 
  conceito de 1 -> N

  Modificado em 30 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 02 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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


class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    dependentes = relationship("Dependentes")


class Dependentes(Base):
    __tablename__ = 'dependentes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        # Insere o Funcionário
        funcionario = Funcionario(nome="Vitor Mazuco")
        session.add(funcionario)

        # Insere os dependentes
        dependente1 = Dependentes(nome="Joao")
        dependente2 = Dependentes(nome="Maria")

        # Relaciona 1-N Funcionário com Dependente
        funcionario.dependentes.append(dependente1)
        funcionario.dependentes.append(dependente2)

        # Insere os Dependentes
        session.add(dependente1)
        session.add(dependente2)

        # Salva a sessão
        session.commit()
    except Exception as e:
        print("Falhou %s" % e)
        print("Fazendo o rollback")
        session.rollback()
