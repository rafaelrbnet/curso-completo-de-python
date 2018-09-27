#!/usr/bin/env python
# -*- coding: UTF-8 -*-

animais = ["gato","cachorro","papagaio"]

animais.append("boi") # add um item ao final dessa lista
print animais

animais.insert(2,"boi") # add um item na posição 2 da lista
print animais

animais.remove("boi") # remove o item da lista
print animais

animais.pop() # remove último item da lista
print animais

animais.pop(1) # remove o item na posição 1 da lista
print animais

animais.count("gato") # mostra a posição em que o item aparece na lista

