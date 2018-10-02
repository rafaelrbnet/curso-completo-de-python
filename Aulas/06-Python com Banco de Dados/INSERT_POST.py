"""
  O registro usando o DML, ficará ravado na 
  memória ate que seja executado o comando
  commit, caso contrário não será gravado. 


  Modificado em 22 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 01 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""
import psycopg2

con = None
try:
    con = psycopg2.connect("host=localhost dbname=projeto user=postgres password=123456")
    cur = con.cursor()
    cur.execute("insert into projeto.cliente(id,nome,cpf) values(4, 'vitor3','333.333.222.555')")
    con.commit()
    cur.close()
    print("Registro criado com sucesso")
except Exception as e:
    print("Erro: %s" % e)
    print("Fazendo o rollback")
    if con is not None:
        con.rollback()
finally:
    print("Finalizando a conexão com o banco de dados")
    if con is not None:
        con.close()
