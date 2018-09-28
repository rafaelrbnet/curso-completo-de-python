"""
  Ao executar o script, é possível
  ver que um objeto do SSHClient
  foi criado e qual posição na
  memória ele está armazenado.


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from paramiko.client import SSHClient

client = SSHClient()

print(client)




















