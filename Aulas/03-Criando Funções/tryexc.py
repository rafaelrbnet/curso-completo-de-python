"""
  O uso do Try...Except serve para 
  lidar com o tratamento de
  exceções. O Try é utilizado quando
  não se quer executar um
  programa, caso haja um erro, ou seja,
  muito usado para verificar
  bugs do sistema. 


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 27 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

try:
    with open("teste.txt", 'r') as f:
        linhas = f.readlines()
        for linha in linhas:
            print(linha)
except Exception as e:
    print("Erro {}".format(e))
