#!/usr/bin/env python
# -*- coding: UTF-8 -*-

usuario = "vitor"
password = "123456"


login = raw_input("Digite o seu login de usuário: ")
senha = raw_input("Digite a sua senha: ")

if (login == usuario) and (senha == password):
    print "Usuário autenticado com sucesso!"
    print "Seja Bem Vindo %s "%login
else:
    print "Acesso Negado!" 
