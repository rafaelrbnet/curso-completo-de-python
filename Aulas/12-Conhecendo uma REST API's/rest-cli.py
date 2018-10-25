#!/usr/bin/python
# -*- coding: UTF-8 -*-
# rest_cli.py

import requests
import json
import sys


# Definir o caminho URL
def _url(path):
    return 'https://api.jsonbin.io/b/5bd0e259adf9f5652a649b79' + path


# Listar todos os itens no Json
def get_tasks():
    response = json.loads(requests.get(_url(''))._content)
    print(response)
    for key in response:
        print(key)
        # print("id: {}, nome: {}, email:{}".format(r[0], r[1], r[2]))


# Adicionar um item no Json
def add_task(email="", nome=""):
    return requests.post(_url('/usuarios/'), json={
        'email': email,
        'nome': nome,
    })


# Apagar um item no Json
def del_task(task_id):
    return requests.delete(_url('/usuarios/{:d}/'.format(task_id)))


# Atualizar um item no Json
def update_task(task_id, email, nome):
    url = _url('/usuarios/{:d}/'.format(task_id))
    return requests.put(url, json={
        'email': email,
        'nome': nome,
    })


if __name__ == '__main__':
    get_tasks()
    # add_task("Alan Post", "email.alan")
    # del_task(5)
    # update_task(5, "@@@@@@@", "vitor9")
    get_tasks()
