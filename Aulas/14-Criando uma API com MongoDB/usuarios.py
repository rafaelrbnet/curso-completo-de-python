from flask import Blueprint, jsonify, request
from Model import Ususarios

import json

usuarios = Blueprint("usuarios", __name__)


@usuarios.route("/usuarios/", methods=['GET'])
def index_usuarios():
    lista_usuarios = json.loads(Ususarios.objects.to_json())
    return jsonify({"usuarios": lista_usuarios})


@usuarios.route("/usuarios/", methods=['POST'])
def inserir_usuarios():
    try:
        dados = request.get_json()
        u = Ususarios
        for key in dados.keys():
            setattr(u, key, dados[key])
        u.save()
        return jsonify({"message": "Usuário cadastrado com sucesso"})
    except Exception as e:
        return jsonify({"message": "Falhou ao cadastrar: %s" % e})
