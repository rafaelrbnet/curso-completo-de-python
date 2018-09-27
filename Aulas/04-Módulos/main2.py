#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo possui
  várias funções que podem 
  ser usadas em outros 
  scripts em Python fazendo assim
  um reaproveitamento de código


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importa o arquivo utils.py que se localiza no diretório 'modulos'.
from modulos import utils as outro_nome

outro_nome.escreverArquivo("dados","Esses são os conteúdos dos arquivos")

print outro_nome.lerArquivo("dados")

print outro_nome.dataAtual()




