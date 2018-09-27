"""
  Um função em programação serve
  para que seja possível utilizar 
  as variaveis com o mesmo nome
  sem necessitar escrever por cima
  a variavel já com valor escrito.


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 27 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

servidor = "192.168.1.26"  # Variavél


def alterar_servidor(ip):
    global servidor  # Chama a variavel global do arquivo
    servidor = ip  # Faz a sobreescrita


print("Servidor atual é: {}".format(servidor))
alterar_servidor("192.168.3.26")  # Chama a função alterarServidor
print("Servidor alterado o IP para: {}".format(servidor))
