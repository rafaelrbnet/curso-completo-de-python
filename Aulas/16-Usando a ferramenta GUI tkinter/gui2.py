#!/usr/bin/python
# -*- coding: UTF-8 -*-
# gui2.py

"""
  Nesse script vamos
  trabalhar com o 
  aplicativo GUI tkinter


  Modificado em 12 de maio de 2017
  por Vitor Mazuco (contato@vmzsolutions.com.br)
"""

import sys
from tkinter import *

root = Tk()
root.geometry("500x500")

widget = Button(None, text='Olá Mundo', command=sys.exit)
widget.pack(fill=BOTH, expand=1)
widget.mainloop()









