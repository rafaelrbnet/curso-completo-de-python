"""
  Nesse script somamos a quantia 
  de argumentos passados dentro de 
  uma função, a execução desse código
  pode ser lidado segundo a sua quantis
  de argumentos que recebe.


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 27 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""


def calcular(*args):
    if len(args) == 1:
        print("A área do quadrado é :{}".format((args[0] * args[0])))
    elif len(args) == 2:
        print("A área do retângulo é: {}".format(args[0] * args[1]))
    elif len(args) == 3:
        print("A área do paralelepipedo é {}".format(args[0] * args[1] * args[2]))


calcular(2)
calcular(4, 2)
calcular(1, 2, 3)
