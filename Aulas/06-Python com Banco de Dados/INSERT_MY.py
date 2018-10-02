#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# INSERT_MY.py

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
import mysql.connector

con = None
try:
    con = mysql.connector.connect(user='root', password='root', host='localhost', database='projeto')
    cur = con.cursor()
    cur.execute("insert into cliente(id,nome,cpf) values('2', 'rafael','222.2.2.2.2.2.')")
    con.commit()
    cur.close()
    print("Registro criado com sucesso")
except Exception as e:
    print("Erro: %s" % e)
finally:
    if con is not None:
        print("Finalizando a conexão com o banco de dados")
        con.close()
