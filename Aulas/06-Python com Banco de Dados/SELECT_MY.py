"""
  Nesse arquivo, vamos 
  fazer um teste de
  update e delete ao banco 
  de dados do MySQL.

  Modificado em 27 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 01 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""
import mysql.connector

con = None
try:
    con = mysql.connector.connect(user='root', password='root', host='localhost', database='projeto')

    cursor = con.cursor()
    cursor.execute("select id, nome, cpf from cliente")
    print("Primeiro registro ", cursor.fetchone())#Retira o primeiro registro do cursor
    print("Restante dos registros ", cursor.fetchall())

    cursor.close()
except Exception as e:
    print("Erro: %s"%e)
    if con is not None:
        con.rollback()
finally:
    if con is not None:
        print("Finalizando a conexão com o banco de dados")
        con.close()
