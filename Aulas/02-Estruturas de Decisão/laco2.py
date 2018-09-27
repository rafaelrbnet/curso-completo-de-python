#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

servidores = ["dns","database","webserver","ldap","mongodb"]


# O comando continue é usado para trabalhar com exeção de uma lista. 
for s in servidores:
	if s == "webserver":
		print "Essa atualização não pode ser executada",s
		continue
	print "Atualizado"
