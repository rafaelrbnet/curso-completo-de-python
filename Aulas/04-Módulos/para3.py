"""
  Agora que todos os comandos foram 
  feitos, podemos fazer a conexão e 
  executar os comandos de forma remota.


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from paramiko.client import SSHClient
import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


try:
    client.connect("xxx", username='xxx', password='xxx')
    stdin, stdout, stderr = client.exec_command("ls -la")
    print(stdout.read())
except Exception as e:
    print("Erro {}".format(e))















