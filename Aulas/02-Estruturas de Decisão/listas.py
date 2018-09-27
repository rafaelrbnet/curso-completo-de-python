#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

# As listas do Python tem o poder de receber qualquer tipo de valor, inclusive as conexões por socket, instâncias de objeto, retorno de um BD, etc.

usuarios = []

nome = ""

while nome != "sair": # Enquando o nome for diferente de 'sair'
	nome = raw_input("Digite o nome:")
	if nome == "sair":
		print "Saindo do Chat"
		break  # O script parou por aqui
	if not nome in usuarios:
		print nome+" entrou no chat"
		usuarios.append(nome)
	for u in usuarios:
		print u+" está online"
