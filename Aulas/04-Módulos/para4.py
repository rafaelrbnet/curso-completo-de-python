#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Para saber se um comando
  foi ou não executado,
  devemos usar o exit_status()
  Nesse script, executamos
  um comando errado de  
  propósito.


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

from paramiko.client import SSHClient
import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("192.168.1.12",username='root',password='123456')
stdin,stdout,stderr = client.exec_command("ls -la") # Comando executado errado de propósito.

if stderr.channel.recv_exit_status() !=0:
	print stderr.channel.recv_exit_status()
	print stderr.read()
else:
	print stdout.read()


















