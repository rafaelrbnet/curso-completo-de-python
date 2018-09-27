#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Os dicionários funcionam muito 
  bem com as listas do Python, esse script 
  simula uma compra de um sistema de 
  e-commerce


  Modificado em 04 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

carrinho = []

produto1 = {"nome":"tenis","valor":21.32}
produto2 = {"nome":"meia","valor":31.32}
produto3 = {"nome":"camiseta","valor":31.32}
produto4 = {"nome":"shorts","valor":41.32}


carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)

print "Seu carrinho possui",len(carrinho),"itens"
total = 0
for c in carrinho:
	total += c["valor"]
print "O valor total é de:",total

