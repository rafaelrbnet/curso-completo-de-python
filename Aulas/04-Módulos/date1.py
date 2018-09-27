#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Temos um script que simula a expiração 
  de um token de acesso. Criamos uma
  subtração de 2 objetos Datetime e nessa
  diminuição, ele nos retorna um outro objeto
  Datetime com a diferença nas datas.
  Agora podemos usar o método total_seconds
  que irá mudar o resultado em segundos e irá
  comparar com o valor de 3600 segundos que 
  equivale a 1h.


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

from datetime import datetime

acesso = datetime(2017,01,22,00,00,00)
atual = datetime(2017,01,22,01,02,00)

if (atual - acesso).total_seconds() > 3600:
	print "Seu token expirou"
else:
	print "Acesso liberado"






