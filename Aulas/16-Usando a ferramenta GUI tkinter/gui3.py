#!/usr/bin/python
# -*- coding: UTF-8 -*-
# gui3.py

import sys
from tkinter import *

root = Tk()
root.geometry("200x200")

def quit():                                  # a custom callback handler
    print('Olá, estou indo embora!')       # kill windows and process
    sys.exit()


widget = Button(None, text='Hello event world', command=quit)
widget.pack()
widget.mainloop()









