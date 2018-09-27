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
from datetime import date

def escreverArquivo(nome,dados):
	with open("%s.txt"%nome,"w") as f:
		f.write(dados)

def lerArquivo(nome):
	with open("%s.txt"%nome,"r") as f:
		var = f.read()
	return var

def dataAtual():
	return date.today()














