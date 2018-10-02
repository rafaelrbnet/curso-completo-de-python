"""
  Nesse arquivo, vamos fazer um teste de
  conexão ao banco de dados 
  do MySQL.


  Modificado em 27 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""
import sys

try:
    import mysql.connector
    from mysql.connector import errorcode
except:
    sys.exit('[!] Por favor, instale a biblioteca mysql.connector')

try:
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='projeto')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Acesso negado")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(err)
else:
    cnx.close()

print('Conect')





