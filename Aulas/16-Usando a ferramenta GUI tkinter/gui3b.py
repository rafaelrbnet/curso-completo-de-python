#!/usr/bin/python
# -*- coding: UTF-8 -*-
# gui3b.py

import sys
from tkinter import *

root = Tk()
root.geometry("200x200")

# Tkinter com Classe
class tkinter_Classe:
    def __init__(self):
        widget = Button(None, text="Olá Python!", command=self.quit) # Chama a função 'quit' quando o botão é pressionado
        widget.pack()

    def quit(self):
        print("Olá tkinter com Classe!")   
        sys.exit()                          

tkinter_Classe() # Chama a classe 'tkinter_Classe'
mainloop()






