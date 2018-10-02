#!/usr/bin/env python
# -*- coding: UTF-8 -*-

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

try:
    con = psycopg2.connect("host=localhost dbname=projeto user=postgres password=123456")
    cur = con.cursor()
    cur.execute("update projeto.cliente set nome='L222PI' where id='2'")
    con.commit()
except Exception as e:
    print("Erro: %s" % e)
    print("Fazendo o rollback")
    con.rollback()
finally:
    print("Finalizando a conexão com o banco de dados")
    cur.close()
    con.close()
