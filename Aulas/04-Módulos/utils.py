"""
  Esse arquivo possui
  várias funções que podem 
  ser usadas em outros 
  scripts em Python fazendo assim
  um reaproveitamento de código


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""
from datetime import date


def escrever_arquivo(nome, dados):
    with open("%s.txt" % nome, "w") as f:
        f.write(dados)


def ler_arquivo(nome):
    with open("%s.txt" % nome, "r") as f:
        var = f.read()
    return var


def data_atual():
    return date.today()
