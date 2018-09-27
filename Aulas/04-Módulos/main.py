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

# Importa o arquivo utils.py que se localiza dentro desse diretório.
import utils

# Reutiliza a função escreverArquivo do arquivo utils.py
utils.escreverArquivo("dados","Esses são os conteúdos dos arquivos")

# Reutiliza a função lerArquivo do arquivo utils.py
print utils.lerArquivo("dados")

# Reutiliza a função dataAtual do arquivo utils.py
print utils.dataAtual()




