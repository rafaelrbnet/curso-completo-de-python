#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#CLASS1.py

"""
  O primeiro parâmeto self
  é obrigatório, pois é 
  com ele que o Python  
  consegue diferenciar
  os métodos das funções.


  Modificado em 06 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

class Servidor:
	memoria = 1024
	disco = 50
	cpu = 1
	
	def contratarMemoria(self,memoria):
		self.memoria += memoria

	def contratarCpu(self,cpu):
		self.cpu += cpu

	def contratarDisco(self,disco):
		self.disco += disco

dns = Servidor()

dns.contratarMemoria(1024)
dns.contratarCpu(3)
dns.contratarDisco(50)

print "O servidor tem as seguintes configurações: CPU %s, Memória: %s, Disco %s GB "%(dns.cpu,dns.memoria,dns.disco)



























