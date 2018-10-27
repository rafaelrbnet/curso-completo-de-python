#!/usr/bin/python
# -*- coding: UTF-8 -*-
# flask_application2.py

# Importação dos módulos
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Aqui serão listados os usuários"})


@app.route("/usuarios/", methods=["POST"])  # create
def insert_usuario():
    return jsonify(dict(message="Aqui serão criados os usuários"))


@app.route("/usuarios/<int:id>/", methods=["GET"])  # retrieve
def select_usuario(id):
    return jsonify(dict(message="Aqui será selecionado o usuário {}".format(id)))


@app.route("/usuarios/<int:id>/", methods=["PUT"])  # update
def update_usuario(id):
    return jsonify(dict(message="Aqui será atualizado o usuário {}".format(id)))


@app.route("/usuarios/<int:id>/", methods=["DELETE"])  # delete
def delete_usuario(id):
    return jsonify(dict(message="Aqui será apagado o usuário {}".format(id)))


if __name__ == '__main__':
    app.run(debug=True)
