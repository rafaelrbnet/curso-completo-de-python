"""
  Para saber se um comando
  foi ou não executado,
  devemos usar o exit_status()
  Nesse script, executamos
  um comando errado de  
  propósito.


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
    stdin, stdout, stderr = client.exec_command("ls -la")  # Comando executado errado de propósito.

    if stderr.channel.recv_exit_status() != 0:
        print(stderr.channel.recv_exit_status())

        print(stderr.read().replace(r"\n", r"\r\n"))
    else:
        ret = stdout.read()
        print(ret)

except Exception as e:
    print("Erro {}".format(e))




















