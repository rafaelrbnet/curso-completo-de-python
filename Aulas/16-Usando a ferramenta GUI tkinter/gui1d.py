#!/usr/bin/python
# -*- coding: UTF-8 -*-
# gui1d.py

"""
  Nesse script vamos
  trabalhar com o 
  aplicativo GUI tkinter


  Modificado em 12 de maio de 2017
  por Vitor Mazuco (contato@vmzsolutions.com.br)
"""

from tkinter import *

root = Tk()
root.geometry("200x500") # Escolha o tipo de geometria

widget = Label(root)
widget.config(text='Olá Mundo!')
widget.pack(side=LEFT, expand=YES, fill=BOTH)
root.title('TKinter Teste')
root.mainloop()



















