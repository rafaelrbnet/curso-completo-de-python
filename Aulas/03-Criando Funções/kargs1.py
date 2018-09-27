"""
  Nesse script mostra um jeito de
  descobrir quais foram as chaves
  e os seus valores representados


  Criado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 27 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""


def descobre_dicionario(**kwargs):
    for k in kwargs.keys():
        print("Chave: {}".format(k))
        print("tem o valor de: {}".format(kwargs[k]))


descobre_dicionario(nome="Alan Kay")
descobre_dicionario(figura="Denis Ritchie")
