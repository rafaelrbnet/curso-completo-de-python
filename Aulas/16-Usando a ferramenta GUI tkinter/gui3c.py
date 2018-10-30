#!/usr/bin/python
# -*- coding: UTF-8 -*-
# gui3c.py

import sys
from tkinter import *

class HelloCallable:
    def __init__(self):                        # __init__ executa na criação de objetos
        self.msg = 'Olá __call__ mundo'        # Ele chama a outra função dentro dessa string

    def __call__(self):
        print(self.msg)                        # __call__ é executado quando chamado
        sys.exit()                             # Sai do sistema

												# Comando chama a classe

widget = Button(None, text="Olá Python!", command=HelloCallable()) # Esse comando chama a classe

widget.pack()
widget.mainloop()
