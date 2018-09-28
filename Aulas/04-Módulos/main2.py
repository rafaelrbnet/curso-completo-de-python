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

# Importa o arquivo utils.py que se localiza no diretório 'modulos'.
from .modulos import utils as outro_nome

outro_nome.escrever_arquivo("dados", "Esses são os conteúdos dos arquivos3")

print(outro_nome.ler_arquivo("dados"))

print(outro_nome.data_atual())




