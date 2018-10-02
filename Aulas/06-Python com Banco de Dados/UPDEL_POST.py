"""
  Nesse arquivo, forçamos o uso do
  rollback quando digitamos o update 
  de forma errada.

  Modificado em 27 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""
import psycopg2

con = None
try:
    con = psycopg2.connect("host=localhost dbname=projeto user=postgres password=123456")
    cur = con.cursor()
    cur.execute("update projeto.cliente set nome='Alberto' where id=1")
    print("Atualização feita com sucesso")
    cur.execute("delete from projeto.cliente where id=2")
    print("Registro apagado com sucesso")
    con.commit()
    cur.close()
except Exception as e:
    print("Erro: %s" % e)
    if con is not None:
        con.rollback()
finally:
    if con is not None:
        print("Finalizando a conexão com o banco de dados")
        con.close()



















