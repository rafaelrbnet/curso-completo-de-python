#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Com os parâmetros adicionais
  ficou assim.


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

from paramiko.client import SSHClient
import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print client














