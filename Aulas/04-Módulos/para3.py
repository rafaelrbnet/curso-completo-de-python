#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Agora que todos os comandos foram 
  feitos, podemos fazer a conexão e 
  executar os comandos de forma remota.


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

from paramiko.client import SSHClient
import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("192.168.1.12",username='root',password='123456')
stdin,stdout,stderr = client.exec_command("ls -la")

print stdout.read()










