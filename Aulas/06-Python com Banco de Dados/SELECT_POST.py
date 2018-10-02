#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Nesse arquivo, usamos os comandos
  fetchone e fatchall 

  Modificado em 27 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 01 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""
import psycopg2

try:
    con = psycopg2.connect("host=localhost dbname=projeto user=postgres password=123456")
    cur = con.cursor()
    cur.execute("select id, nome, cpf from projeto.cliente")
    print("Primeiro registro ", cur.fetchone())
    print("Todos os registros ", cur.fetchall())
except Exception as e:
    print("Erro: %s" % e)
finally:
    print("Finalizando a conexão com o banco de dados")
    cur.close
    con.close
