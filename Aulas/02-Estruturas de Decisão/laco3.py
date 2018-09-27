#!/usr/bin/env python
# -*- coding: UTF-8 -*- 


servidores = ["dns","database","webserver","voip","mongodb"]


# O comando continue é usado para trabalhar com exeção de uma lista. 
for s in servidores:
	if s == "ldap":
		print "O servidor ldap não pode estar na lista",s
		break
	else:
		print "Todos os servidores estão atualizados"
print "Finalizando o programa"
